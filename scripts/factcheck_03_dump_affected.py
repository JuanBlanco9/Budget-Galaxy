"""Dump the exact text of each entry that has a DRIFTED finding so we can craft verbatim patches."""
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

a = json.load(open('data/uk/factcheck/batch_A_findings.json', encoding='utf-8'))
b = json.load(open('data/uk/factcheck/batch_B_findings.json', encoding='utf-8'))
ext = json.load(open('data/uk/node_enrichment_extended.json', encoding='utf-8'))

affected = {}
for ent in a + b:
    drifts = [f for f in ent['findings'] if f['status'] == 'DRIFTED']
    if drifts:
        affected[ent['key']] = drifts

for key, drifts in affected.items():
    e = ext['entries'].get(key)
    if not e:
        print(f'### {key} — NOT FOUND IN ENRICHMENT')
        continue
    print(f'\n{"="*80}\n### {key}  ({len(drifts)} drifts)\n{"="*80}')
    print(f'\n--- description ---\n{e.get("description","")}')
    print(f'\n--- notes ---\n{e.get("notes","")}')
    print(f'\n--- key_stats ---')
    for s in e.get('key_stats', []):
        print(f'  {s.get("label")}: {s.get("value")}')
    print(f'\n--- drifts to fix ---')
    for i, d in enumerate(drifts, 1):
        print(f'  {i}. [{d.get("severity","?")}] {d["claim"][:120]}')
        print(f'     -> {d.get("correct_value","")[:200]}')
