#!/usr/bin/env python3
"""Backfill top_buyer_type + buyer_type_breakdown in data/suppliers_v2/*.json.

For each of the 19,238 v2 supplier files, look up their contract flows in
data/procurement/contracts_flat_2024.jsonl, classify £ by buyer_type, and
write the dominant type + breakdown back into the supplier file.

Match strategy:
  1. Direct: contract.supplier_ch_number == supplier.company_number
  2. Fallback: normalised name match (contract.supplier_name/legal_name vs
     supplier.display_name/official_name/previous_names)
"""
import json
import re
import sys
import glob
import os
from pathlib import Path
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(50000)

ROOT = Path('.')
V2_DIR = ROOT / 'data/suppliers_v2'
CONTRACTS = ROOT / 'data/procurement/contracts_flat_2024.jsonl'

def classify_buyer(name):
    if not name:
        return 'other'
    n = name.lower()
    if 'nhs' in n or 'icb' in n or 'integrated care' in n:
        return 'nhs'
    if any(w in n for w in ['council', 'borough', 'county council', 'city of', 'district council']):
        return 'council'
    if 'university' in n or 'college' in n or 'school' in n:
        return 'education'
    if 'police' in n or 'fire' in n or 'constabulary' in n:
        return 'police_fire'
    if 'department' in n or 'ministry' in n or 'hm ' in n or 'home office' in n or 'cabinet office' in n or 'foreign' in n or 'treasury' in n:
        return 'central_govt'
    if 'authority' in n or 'agency' in n:
        return 'agency'
    if 'trust' in n and 'nhs' not in n:
        return 'trust'
    return 'other'

def normalize_name(s):
    if not s:
        return ''
    s = s.lower().strip()
    s = re.sub(r'\b(limited|ltd|plc|llp|public limited company|company)\b\.?', '', s)
    s = re.sub(r'[^a-z0-9]+', '', s)
    return s

# Step 1: build rosetta (name → ch) from 19,238 v2 files
print('Loading v2 suppliers and building name rosetta...', flush=True)
rosetta = {}  # normalized_name -> ch
ch_to_path = {}
ch_set = set()
v2_files = sorted(glob.glob(str(V2_DIR / '[0-9A-Z]*.json')))
print(f'  v2 files: {len(v2_files):,}', flush=True)

for path in v2_files:
    ch = os.path.basename(path).replace('.json','')
    ch_set.add(ch)
    ch_to_path[ch] = path
    try:
        with open(path, encoding='utf-8') as f:
            d = json.load(f)
    except Exception:
        continue
    names = []
    for k in ('display_name', 'official_name'):
        if d.get(k):
            names.append(d[k])
    for pn in (d.get('previous_names') or []):
        if isinstance(pn, dict) and pn.get('name'):
            names.append(pn['name'])
    for n in names:
        norm = normalize_name(n)
        if len(norm) < 4:  # skip tiny normalisations to avoid collisions
            continue
        # First write wins; don't overwrite (longer-history names lose)
        if norm not in rosetta:
            rosetta[norm] = ch

print(f'  rosetta size: {len(rosetta):,}', flush=True)

# Step 2: walk contracts, accumulate £ per (ch, buyer_type)
print('Walking contracts...', flush=True)
flow_by_ch = defaultdict(lambda: defaultdict(float))
hit_ch = 0
hit_name = 0
miss = 0
miss_with_val = 0
total_contracts = 0

with open(CONTRACTS, encoding='utf-8') as f:
    for line in f:
        try:
            d = json.loads(line)
        except Exception:
            continue
        total_contracts += 1
        sch = (d.get('supplier_ch_number') or '').strip()
        sname = (d.get('supplier_name') or d.get('supplier_legal_name') or '').strip()
        bname = (d.get('buyer_name') or '').strip()
        val = d.get('award_value_gbp') or d.get('tender_value_gbp') or 0
        try:
            val = float(val) if val else 0
        except Exception:
            val = 0
        # Resolve to v2 ch
        target_ch = None
        if sch and sch in ch_set:
            target_ch = sch
            hit_ch += 1
        elif sch:
            # Try zero-stripped and zero-padded variants
            stripped = sch.lstrip('0')
            for cand in (stripped, sch.zfill(8), sch.zfill(7)):
                if cand in ch_set:
                    target_ch = cand
                    hit_ch += 1
                    break
        if not target_ch and sname:
            norm = normalize_name(sname)
            if norm in rosetta:
                target_ch = rosetta[norm]
                hit_name += 1
        if not target_ch:
            miss += 1
            if val > 0:
                miss_with_val += 1
            continue
        bt = classify_buyer(bname)
        flow_by_ch[target_ch][bt] += val

print(f'  contracts walked: {total_contracts:,}')
print(f'  hit by ch:   {hit_ch:,}')
print(f'  hit by name: {hit_name:,}')
print(f'  miss total:  {miss:,} (with £>0: {miss_with_val:,})')
print(f'  suppliers with flows: {len(flow_by_ch):,}')

# Step 3: write back into v2 files
print('Writing top_buyer_type into v2 files...', flush=True)
written = 0
unchanged = 0
type_counter = Counter()

for ch, types in flow_by_ch.items():
    path = ch_to_path.get(ch)
    if not path:
        continue
    total = sum(types.values())
    if total <= 0:
        continue
    primary = max(types.items(), key=lambda kv: kv[1])[0]
    breakdown = {t: round(v / total, 4) for t, v in types.items()}
    breakdown = dict(sorted(breakdown.items(), key=lambda kv: -kv[1]))
    try:
        with open(path, encoding='utf-8') as f:
            d = json.load(f)
        d['top_buyer_type'] = primary
        d['buyer_type_breakdown'] = breakdown
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        written += 1
        type_counter[primary] += 1
    except Exception as e:
        print(f'  ERROR {path}: {e}')

# Suppliers with no flows → mark as 'other' explicitly to avoid filter ambiguity
no_flow_ch = ch_set - set(flow_by_ch.keys())
for ch in no_flow_ch:
    path = ch_to_path.get(ch)
    if not path:
        continue
    try:
        with open(path, encoding='utf-8') as f:
            d = json.load(f)
        if d.get('top_buyer_type'):
            unchanged += 1
            continue
        d['top_buyer_type'] = 'other'
        d['buyer_type_breakdown'] = {}
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        written += 1
        type_counter['other'] += 1
    except Exception:
        pass

print(f'\n  suppliers written: {written:,}')
print(f'  suppliers unchanged: {unchanged:,}')
print(f'  primary type distribution:')
for t, n in sorted(type_counter.items(), key=lambda kv: -kv[1]):
    print(f'    {t:15s} {n:>6,}')
