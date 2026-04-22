"""Merge D4_06_clinical_{A,B,C,D}.py into node_enrichment_extended.json with validation."""
import json
import runpy
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ENR = Path('data/uk/node_enrichment_extended.json')
BATCHES = ['scripts/D4_06_clinical_A.py', 'scripts/D4_06_clinical_B.py',
           'scripts/D4_06_clinical_C.py', 'scripts/D4_06_clinical_D.py']

ext = json.load(ENR.open(encoding='utf-8'))
existing = set(ext['entries'].keys())

expected_trusts = set()
for b in 'ABCD':
    data = json.load(open(f'scripts/hand_curation_briefs/D4_06_clinical_{b}.json', encoding='utf-8'))
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
    print(f'{p.name}: {len(NEW)} entries')
    for k, e in NEW.items():
        if ' \u2014 ' not in k:
            issues.append(f'[{p.name}] bad separator: {k}')
            continue
        als = e.get('aliases') or []
        if not als or not isinstance(als[0], dict):
            issues.append(f'[{p.name}] {k}: missing aliases')
            continue
        parent = als[0].get('parent','')
        if parent not in expected_trusts:
            issues.append(f'[{p.name}] {k}: alias parent not in expected trusts: {parent!r}')
            continue
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
        if k in existing:
            issues.append(f'[{p.name}] {k}: DUPLICATE vs existing')
            continue
        if k in merged:
            issues.append(f'[{p.name}] {k}: DUPLICATE across batches')
            continue
        merged[k] = e

print(f'\nValid new: {len(merged)} · Issues: {len(issues)}')
for i in issues[:20]:
    print(f'  - {i}')

covered = {als[0]['parent'] for k, e in merged.items() for als in [e.get('aliases') or [{}]]}
missing = expected_trusts - covered
print(f'Trust coverage: {len(covered)}/{len(expected_trusts)} (missing {len(missing)})')
for t in sorted(missing)[:10]:
    print(f'  missing: {t}')

if '--apply' in sys.argv and merged:
    import shutil
    backup = ENR.with_suffix('.json.bak.d4_06')
    if not backup.exists():
        shutil.copy(ENR, backup)
        print(f'Backup: {backup.name}')
    ext['entries'].update(merged)
    ENR.write_text(json.dumps(ext, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Applied {len(merged)} entries · total: {len(ext["entries"]):,}')
else:
    print('(dry run — add --apply)')
