"""Detect Phase 2 orphan sub-lines under NHS Specialist / Community / Ambulance Trusts.

Adapts the Acute detector (phase2_02_detect_nhs_acute.py) to the three remaining
NHS provider categories that haven't been audited yet.
"""
import json
import re
import sys
import os
from collections import defaultdict, Counter
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(50000)

with open('data/uk/node_enrichment_extended.json', encoding='utf-8') as f:
    ext = json.load(f)
with open('data/uk/uk_budget_tree_2024.json', encoding='utf-8') as f:
    tree = json.load(f)
keys = set(ext['entries'].keys())

# Scoped aliases: (name, parent) → set of keys
aliases_scoped = defaultdict(set)
for k, e in ext['entries'].items():
    for a in (e.get('aliases') or []):
        if isinstance(a, dict) and a.get('name') and a.get('parent'):
            aliases_scoped[(a['name'], a['parent'])].add(k)

CATEGORIES = ['NHS Specialist Trusts', 'NHS Community Trusts', 'NHS Ambulance Trusts']

def find_target_subtree(n, target, chain=[]):
    results = []
    name = n.get('name','')
    if name == target:
        for t in (n.get('children') or []):
            tname = t.get('name','')
            if 'Trust' in tname or 'Health Board' in tname:
                results.append((t, chain + [name]))
    for c in (n.get('children') or []):
        results.extend(find_target_subtree(c, target, chain + [name]))
    return results

def collect_orphans(target_category):
    trust_subtrees = find_target_subtree(tree, target_category)
    orphans = []
    def walk_node(n, trust_name, chain):
        name = n.get('name','')
        v = n.get('value') or 0
        if name and v > 1e5:  # skip dust < £100k
            composite = f'{name} — {trust_name}'
            if composite not in keys and (name, trust_name) not in aliases_scoped:
                orphans.append({
                    'trust': trust_name,
                    'sub_line': name,
                    'value': v,
                    'parent_line': chain[-1] if chain else '',
                })
        for c in (n.get('children') or []):
            walk_node(c, trust_name, chain + [name])
    for trust_node, chain in trust_subtrees:
        tname = trust_node.get('name', '')
        for child in (trust_node.get('children') or []):
            walk_node(child, tname, chain + [trust_node.get('name', '')])
    return trust_subtrees, orphans

# Run for all 3 categories
all_data = {}
total_orphans = 0
total_gbp = 0
for cat in CATEGORIES:
    trusts, orphans = collect_orphans(cat)
    all_data[cat] = {'trusts': trusts, 'orphans': orphans}
    total_orphans += len(orphans)
    total_gbp += sum(o['value'] for o in orphans)
    print(f'\n=== {cat} ===')
    print(f'  Trusts in tree: {len(trusts)}')
    print(f'  Orphan sub-lines: {len(orphans)}')
    print(f'  Total £: £{sum(o["value"] for o in orphans)/1e9:.2f}B')
    by_subline = Counter(o['sub_line'] for o in orphans)
    print(f'  Top sub-line types ({min(10, len(by_subline))} of {len(by_subline)}):')
    for n, c in by_subline.most_common(10):
        total = sum(o['value'] for o in orphans if o['sub_line']==n)/1e9
        print(f'    {c:4d}  £{total:>5.2f}B  {n}')

print(f'\n=== COMBINED TOTAL ===')
print(f'  Orphans across 3 categories: {total_orphans}')
print(f'  Total £: £{total_gbp/1e9:.2f}B')

# Write per-category files for the curation pipeline to consume
out_dir = Path('data/uk/factcheck')
out_dir.mkdir(exist_ok=True, parents=True)
for cat in CATEGORIES:
    slug = cat.lower().replace('nhs ', '').replace(' trusts', '').replace(' ', '_')
    orphans = all_data[cat]['orphans']
    orphans.sort(key=lambda x: -x['value'])
    p = out_dir / f'phase2_{slug}_orphans.json'
    p.write_text(json.dumps(orphans, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  wrote {p} · {len(orphans)} entries')
