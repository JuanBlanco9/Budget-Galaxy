"""Phase 2 — detect shared-parent orphans under NHS Mental Health Trusts.

Per handoff, the 18% gap: entries whose key matches 'Social Fund - Cold Weather Payment',
'Drugs costs' etc. at a LOWER level get resolved via scoped alias to a HIGHER entry
(usually the parent trust/COFOG). This detection script finds nodes in the tree whose
name has NO direct entry and NO trust-scoped alias — they inherit from higher.

For NHS MH specifically: 3,190 orphan nodes per handoff, £122B absorbed.
"""
import json
import sys
import re
from collections import defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ext = json.load(open('data/uk/node_enrichment_extended.json', encoding='utf-8'))
tree = json.load(open('data/uk/uk_budget_tree_2024.json', encoding='utf-8'))
keys = set(ext['entries'].keys())

# Build scoped aliases: (name, parent) → key
aliases_scoped = defaultdict(set)
for k, e in ext['entries'].items():
    for a in (e.get('aliases') or []):
        if isinstance(a, dict) and a.get('name') and a.get('parent'):
            aliases_scoped[(a['name'], a['parent'])].add(k)

# Collect composite keys already in enrichment (em-dash format)
composite_pairs = set()
for k in keys:
    if ' \u2014 ' in k:
        sub, _, trust = k.partition(' \u2014 ')
        composite_pairs.add((sub.strip(), trust.strip()))

# Walk tree under NHS Mental Health Trusts; find nodes lacking direct+alias coverage
TARGET_CATEGORIES = {'NHS Mental Health Trusts'}

def find_target_subtree(n, chain=[]):
    """Return list of (trust_node, chain_to_trust) for every trust under target categories."""
    results = []
    name = n.get('name','')
    if name in TARGET_CATEGORIES:
        # Children are the trusts
        for t in (n.get('children') or []):
            tname = t.get('name','')
            if 'Trust' in tname or 'Health Board' in tname:
                results.append((t, chain + [name]))
    for c in (n.get('children') or []):
        results.extend(find_target_subtree(c, chain + [name]))
    return results

trust_subtrees = find_target_subtree(tree)
print(f'NHS Mental Health Trusts found: {len(trust_subtrees)}')

# For each trust, walk sub-lines and identify orphans
orphans = []  # {trust, sub_line, value, path}

def walk_trust_sublines(trust_node, trust_name, chain):
    for child in (trust_node.get('children') or []):
        walk_node(child, trust_name, chain + [trust_node.get('name','')])

def walk_node(n, trust_name, chain):
    name = n.get('name','')
    v = n.get('value') or 0
    if name and v > 0:
        # Is this node covered by (a) a direct key matching its composite or (b) a scoped alias?
        composite_key = f"{name} \u2014 {trust_name}"
        if composite_key in keys:
            covered = True
        elif (name, trust_name) in aliases_scoped:
            covered = True
        elif name in keys:
            # Name as direct key — probably shared parent fallback
            covered = 'direct-match-likely-shared'
        else:
            covered = False
        if not covered or covered == 'direct-match-likely-shared':
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

for trust_node, chain in trust_subtrees:
    tname = trust_node.get('name','')
    walk_trust_sublines(trust_node, tname, chain)

print(f'Orphan sub-lines under MH Trusts: {len(orphans)}')
print(f'Total £ absorbed: £{sum(o["value"] for o in orphans)/1e9:.2f}B')

# Breakdown by depth
from collections import Counter
by_depth = Counter(o['depth'] for o in orphans)
print(f'By depth: {dict(by_depth)}')
by_subline = Counter(o['sub_line'] for o in orphans)
print('Top 15 orphan sub-line names:')
for name, n in by_subline.most_common(15):
    total = sum(o['value'] for o in orphans if o['sub_line']==name)
    print(f'  {n:4d}  £{total/1e9:>6.2f}B  {name}')

# Save full list
Path('data/uk/factcheck').mkdir(parents=True, exist_ok=True)
json.dump(orphans, open('data/uk/factcheck/phase2_mh_orphans.json','w', encoding='utf-8'),
          indent=2, ensure_ascii=False)
print(f'\nWrote data/uk/factcheck/phase2_mh_orphans.json ({len(orphans)} orphans)')

# For the FIRST slice of wave 2, pick a tractable subset:
# - Only orphans at a standardized sub-line level (depth-3 "Staff Costs", "Premises", etc.)
# - Top 200 by £ to maximize coverage
# - Limit to most-common sub-line names (covers most MH trusts)
standard_sublines = {name for name, n in by_subline.most_common(20) if n >= 10}
print(f'\nStandard sub-lines (>=10 occurrences): {len(standard_sublines)}')

first_slice = [o for o in orphans if o['sub_line'] in standard_sublines]
first_slice.sort(key=lambda x: -x['value'])
first_slice = first_slice[:200]

# Exclude composite keys that ARE in enrichment already (re-check)
first_slice = [o for o in first_slice if f"{o['sub_line']} \u2014 {o['trust']}" not in keys]
print(f'First slice (top 200, not yet covered): {len(first_slice)}')

json.dump(first_slice, open('data/uk/factcheck/phase2_mh_slice1.json','w', encoding='utf-8'),
          indent=2, ensure_ascii=False)

# Split into 3 batches for wave 2 (will be 3 agents)
batches = [first_slice[i::3] for i in range(3)]
for i, b in enumerate(batches):
    p = Path(f'data/uk/factcheck/phase2_mh_slice1_{chr(65+i)}.json')
    p.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  batch {chr(65+i)}: {len(b)} entries')

print(f'\nWave 2 ready: 3 batches for NHS MH Phase 2 shared-parent first slice.')
