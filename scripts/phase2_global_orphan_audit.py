"""Global orphan detection across entire UK budget tree.

Walks every node in the tree, identifies which still resolve to a shared-parent
fallback (no composite key + no scoped alias). Groups by depth + parent category
to find clusters worth procedural-fallback or hand-curation.
"""
import json
import sys
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(50000)

with open('data/uk/node_enrichment_extended.json', encoding='utf-8') as f:
    ext = json.load(f)
with open('data/uk/uk_budget_tree_2024.json', encoding='utf-8') as f:
    tree = json.load(f)
keys = set(ext['entries'].keys())

aliases_scoped = defaultdict(set)
for k, e in ext['entries'].items():
    for a in (e.get('aliases') or []):
        if isinstance(a, dict) and a.get('name') and a.get('parent'):
            aliases_scoped[(a['name'], a['parent'])].add(k)

orphans = []
def walk(n, chain=[]):
    name = n.get('name','')
    v = n.get('value') or 0
    if name and v > 5e5 and len(chain) >= 2:  # >£500k threshold for global
        composite = f"{name} — {chain[-1]}"
        if composite not in keys:
            # Try: any alias (name, ancestor) covers?
            covered = False
            for anc in reversed(chain):
                if (name, anc) in aliases_scoped:
                    covered = True; break
            # Also: name itself as direct key (shared-parent) counts as orphan if at depth >=3
            if not covered:
                orphans.append({
                    'name': name,
                    'parent': chain[-1] if chain else '',
                    'value': v,
                    'depth': len(chain),
                    'path': ' → '.join(chain[-3:] + [name]),
                })
    for c in (n.get('children') or []):
        walk(c, chain + [name])
walk(tree)

print(f'Total orphans (>£500k, depth >=2, no composite or alias): {len(orphans)}')
print(f'Total £ absorbed: £{sum(o["value"] for o in orphans)/1e9:.2f}B')

# Group by parent + depth
by_parent = defaultdict(list)
for o in orphans:
    by_parent[o['parent']].append(o)
print(f'\nTop 20 parents with most orphans:')
sorted_parents = sorted(by_parent.items(), key=lambda x: -sum(o['value'] for o in x[1]))[:20]
for p, os in sorted_parents:
    total_v = sum(o['value'] for o in os) / 1e9
    print(f'  {len(os):4d} orphans · £{total_v:>6.2f}B · parent: {p[:60]}')

# Group by name (which sub-line types are most affected)
by_name = Counter()
by_name_v = defaultdict(float)
for o in orphans:
    by_name[o['name']] += 1
    by_name_v[o['name']] += o['value']
print(f'\nTop 20 sub-line types still orphan:')
for nm, n in by_name.most_common(20):
    print(f'  {n:4d} × {nm[:60]} (£{by_name_v[nm]/1e9:.2f}B)')

# Save
with open('data/uk/factcheck/global_orphans.json', 'w', encoding='utf-8') as f:
    json.dump(orphans, f, ensure_ascii=False, indent=2)
print(f'\nWrote data/uk/factcheck/global_orphans.json')
