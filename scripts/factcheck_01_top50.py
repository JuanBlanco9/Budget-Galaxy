"""Phase 3 fact-check step 1: identify top-50 entries by £ and dump URL list."""
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

ext = json.load(open('data/uk/node_enrichment_extended.json', encoding='utf-8'))
tree = json.load(open('data/uk/uk_budget_tree_2024.json', encoding='utf-8'))

vals = {}
def walk(n):
    name = n.get('name')
    v = n.get('value') or 0
    if name and v > vals.get(name, 0):
        vals[name] = v
    for c in (n.get('children') or []):
        walk(c)
walk(tree)

def entry_value(k, e):
    cands = [k]
    for a in (e.get('aliases') or []):
        if isinstance(a, dict) and a.get('name'):
            cands.append(a['name'])
        elif isinstance(a, str):
            cands.append(a)
    return max((vals.get(c, 0) for c in cands), default=0)

ranked = sorted(
    ((k, entry_value(k, e), e) for k, e in ext['entries'].items()),
    key=lambda x: -x[1]
)
THRESHOLD_GBP = 30e9
top = [(k, v, e) for k, v, e in ranked if v > THRESHOLD_GBP][:30]

print(f'Total entries: {len(ext["entries"]):,}')
print(f'Top-{len(top)} above £{THRESHOLD_GBP/1e9:.0f}B:\n')
for i, (k, v, e) in enumerate(top, 1):
    srcs = len(e.get('sources') or [])
    stats = len(e.get('key_stats') or [])
    print(f'  {i:2d}. £{v/1e9:>7.2f}B  {k[:70]:<70}  stats={stats:2d} srcs={srcs}')

out = []
for k, v, e in top:
    urls = [s.get('url') for s in (e.get('sources') or []) if isinstance(s, dict) and s.get('url')]
    out.append({
        'key': k,
        'value_gbp': v,
        'urls': urls,
        'n_stats': len(e.get('key_stats') or []),
        'description': e.get('description'),
        'notes': e.get('notes'),
        'key_stats': e.get('key_stats'),
        'sources': e.get('sources'),
    })
import os
os.makedirs('data/uk/factcheck', exist_ok=True)
json.dump(out, open('data/uk/factcheck/top_entries.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
n_urls = sum(len(x['urls']) for x in out)
print(f'\nWrote data/uk/factcheck/top_entries.json · {len(out)} entries · {n_urls} URLs')
