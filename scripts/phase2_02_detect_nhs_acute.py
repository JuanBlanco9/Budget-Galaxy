"""Detect Phase 2 shared-parent orphans under NHS Acute Trusts.

Per handoff: 132 orphan nodes · £6.0B absorbed (low-hanging fruit, easy quick win).
"""
import json
import re
import sys
from collections import defaultdict, Counter
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(50000)

with open('data/uk/node_enrichment_extended.json', encoding='utf-8') as f:
    ext = json.load(f)
with open('data/uk/uk_budget_tree_2024.json', encoding='utf-8') as f:
    tree = json.load(f)
keys = set(ext['entries'].keys())

# Build scoped aliases: (name, parent) -> set of keys
aliases_scoped = defaultdict(set)
for k, e in ext['entries'].items():
    for a in (e.get('aliases') or []):
        if isinstance(a, dict) and a.get('name') and a.get('parent'):
            aliases_scoped[(a['name'], a['parent'])].add(k)

TARGET_CATEGORIES = {'NHS Acute Trusts'}

def find_target_subtree(n, chain=[]):
    results = []
    name = n.get('name','')
    if name in TARGET_CATEGORIES:
        for t in (n.get('children') or []):
            tname = t.get('name','')
            if 'Trust' in tname or 'Health Board' in tname:
                results.append((t, chain + [name]))
    for c in (n.get('children') or []):
        results.extend(find_target_subtree(c, chain + [name]))
    return results

trust_subtrees = find_target_subtree(tree)
print(f'NHS Acute Trusts found: {len(trust_subtrees)}')

orphans = []

def walk_node(n, trust_name, chain):
    name = n.get('name','')
    v = n.get('value') or 0
    if name and v > 0:
        composite_key = f"{name} — {trust_name}"
        if composite_key in keys:
            covered = True
        elif (name, trust_name) in aliases_scoped:
            covered = True
        elif name in keys:
            covered = 'shared-parent'
        else:
            covered = False
        if not covered or covered == 'shared-parent':
            orphans.append({
                'trust': trust_name,
                'sub_line': name,
                'value': v,
                'path': ' → '.join(chain + [name]),
                'coverage': covered,
                'depth': len(chain),
            })
    for c in (n.get('children') or []):
        walk_node(c, trust_name, chain + [name])

def walk_trust_sublines(trust_node, trust_name, chain):
    for child in (trust_node.get('children') or []):
        walk_node(child, trust_name, chain + [trust_node.get('name','')])

for trust_node, chain in trust_subtrees:
    tname = trust_node.get('name','')
    walk_trust_sublines(trust_node, tname, chain)

print(f'Orphans under Acute trusts: {len(orphans)}')
print(f'Total £ absorbed: £{sum(o["value"] for o in orphans)/1e9:.2f}B')

by_subline = Counter(o['sub_line'] for o in orphans)
print('Top 15 orphan sub-line names:')
for name, n in by_subline.most_common(15):
    total = sum(o['value'] for o in orphans if o['sub_line']==name)
    print(f'  {n:4d}  £{total/1e9:>6.2f}B  {name}')

os.makedirs('data/uk/factcheck', exist_ok=True)
with open('data/uk/factcheck/phase2_acute_orphans.json', 'w', encoding='utf-8') as f:
    json.dump(orphans, f, indent=2, ensure_ascii=False)
print(f'\nWrote data/uk/factcheck/phase2_acute_orphans.json ({len(orphans)} orphans)')

# Build slice for next wave (top 132 by £, or all if <132)
orphans.sort(key=lambda x: -x['value'])
slice1 = [o for o in orphans if f"{o['sub_line']} — {o['trust']}" not in keys][:132]
print(f'Slice 1 candidates: {len(slice1)}')

# Split into 3 batches for next wave
batches = [slice1[i::3] for i in range(3)]
for i, b in enumerate(batches):
    p = f'scripts/hand_curation_briefs/phase2_acute_slice1_{chr(65+i)}.json'
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(b, f, ensure_ascii=False, indent=2)
    print(f'  batch {chr(65+i)}: {len(b)} entries')
