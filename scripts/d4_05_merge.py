"""Merge D4_05_drugs_{A,B,C,D}.py into node_enrichment_extended.json with strict validation."""
import json
import runpy
import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ENR = Path('data/uk/node_enrichment_extended.json')
BATCHES = ['scripts/D4_05_drugs_A.py', 'scripts/D4_05_drugs_B.py',
           'scripts/D4_05_drugs_C.py', 'scripts/D4_05_drugs_D.py']

ext = json.load(ENR.open(encoding='utf-8'))
existing = set(ext['entries'].keys())

# Load expected trust list from brief JSONs
expected_trusts = set()
for b in 'ABCD':
    data = json.load(open(f'scripts/hand_curation_briefs/D4_05_drugs_{b}.json', encoding='utf-8'))
    for r in data:
        expected_trusts.add(r['trust'])

merged = {}
issues = []

for path in BATCHES:
    p = Path(path)
    if not p.exists():
        issues.append(f'MISSING: {path}')
        continue
    ns = runpy.run_path(str(p))
    NEW = ns.get('NEW') or {}
    print(f'\n{p.name}: {len(NEW)} entries')

    for k, e in NEW.items():
        # Validate key format
        if ' \u2014 ' not in k:
            issues.append(f'[{p.name}] bad separator: {k}')
            continue
        # Validate aliases
        als = e.get('aliases') or []
        if not als or not isinstance(als[0], dict):
            issues.append(f'[{p.name}] {k}: missing/bad aliases')
            continue
        parent = als[0].get('parent','')
        if parent not in expected_trusts:
            issues.append(f'[{p.name}] {k}: alias parent not in expected trusts: {parent!r}')
            continue
        # Validate stats, sources, fields
        if len(e.get('key_stats') or []) < 6:
            issues.append(f'[{p.name}] {k}: key_stats < 6')
            continue
        srcs = e.get('sources') or []
        if not srcs or any(not (isinstance(s,dict) and s.get('url','').startswith('https://')) for s in srcs):
            issues.append(f'[{p.name}] {k}: source missing or non-https url')
            continue
        if not all(e.get(f) for f in ['description','beneficiaries','legal_basis','notes','related']):
            issues.append(f'[{p.name}] {k}: missing core field')
            continue
        # Check dup
        if k in existing:
            issues.append(f'[{p.name}] {k}: DUPLICATE vs existing enrichment')
            continue
        if k in merged:
            issues.append(f'[{p.name}] {k}: DUPLICATE across batches')
            continue
        merged[k] = e

# Summary
print(f'\n=== MERGE SUMMARY ===')
print(f'Valid new entries: {len(merged)}')
print(f'Issues: {len(issues)}')
for i in issues[:30]:
    print(f'  - {i}')
if len(issues) > 30:
    print(f'  ... +{len(issues)-30} more')

# Coverage check
covered = {als[0]['parent'] for k, e in merged.items() for als in [e.get('aliases') or [{}]]}
missing_trusts = expected_trusts - covered
print(f'\nTrust coverage: {len(covered)}/{len(expected_trusts)} (missing {len(missing_trusts)})')
if missing_trusts:
    print('Missing trusts:')
    for t in sorted(missing_trusts)[:10]:
        print(f'  - {t}')

if issues and not merged:
    print('\nABORT: no valid entries to merge')
    sys.exit(1)

# Ask for confirmation via CLI arg
if '--apply' in sys.argv:
    import shutil
    backup = ENR.with_suffix('.json.bak.d4_05')
    if not backup.exists():
        shutil.copy(ENR, backup)
        print(f'Backup: {backup.name}')
    ext['entries'].update(merged)
    ENR.write_text(json.dumps(ext, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'\nApplied {len(merged)} entries · total entries now: {len(ext["entries"]):,}')
else:
    print('\n(dry run — add --apply to write)')
