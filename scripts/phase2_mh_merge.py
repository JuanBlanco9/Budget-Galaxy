"""Merge phase2_mh_*.py files into node_enrichment_extended.json with strict validation.

Skips duplicates (entries that became covered between brief generation and agent return).
"""
import json
import runpy
import sys
import shutil
import os
import glob

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(50000)

ENR = 'data/uk/node_enrichment_extended.json'
with open(ENR, encoding='utf-8') as fh:
    ext = json.load(fh)
existing = set(ext['entries'].keys())

# Pick up any phase2_mh_*.py file in scripts/
candidates = sorted(glob.glob('scripts/phase2_mh_*.py'))
print(f'Found {len(candidates)} phase2_mh files: {[os.path.basename(p) for p in candidates]}')

merged = {}
skipped_dup = []
issues = []

for path in candidates:
    ns = runpy.run_path(path)
    NEW = ns.get('NEW') or {}
    name = os.path.basename(path)
    print(f'\n{name}: {len(NEW)} entries')
    for k, e in NEW.items():
        if ' \u2014 ' not in k:
            issues.append(f'[{name}] bad sep: {k}')
            continue
        als = e.get('aliases') or []
        if not als or not isinstance(als[0], dict) or not als[0].get('parent'):
            issues.append(f'[{name}] missing alias parent: {k}')
            continue
        if len(e.get('key_stats') or []) < 6:
            issues.append(f'[{name}] key_stats < 6: {k}')
            continue
        srcs = e.get('sources') or []
        if not srcs or any(not (isinstance(s,dict) and s.get('url','').startswith('https://')) for s in srcs):
            issues.append(f'[{name}] bad sources: {k}')
            continue
        if not all(e.get(f) for f in ['description','beneficiaries','legal_basis','notes','related']):
            issues.append(f'[{name}] missing core field: {k}')
            continue
        if k in existing:
            skipped_dup.append(k)
            continue
        if k in merged:
            issues.append(f'[{name}] dup across phase2 files: {k}')
            continue
        merged[k] = e

print(f'\n=== SUMMARY ===')
print(f'Valid new: {len(merged)}')
print(f'Skipped (already in enrichment): {len(skipped_dup)}')
for d in skipped_dup[:10]: print(f'  - {d}')
print(f'Issues: {len(issues)}')
for i in issues[:10]: print(f'  - {i}')

if '--apply' in sys.argv and merged:
    backup = ENR.replace('.json', '.json.bak.phase2_mh')
    if not os.path.exists(backup):
        shutil.copy(ENR, backup)
        print(f'Backup: {os.path.basename(backup)}')
    ext['entries'].update(merged)
    with open(ENR, 'w', encoding='utf-8') as fh:
        json.dump(ext, fh, ensure_ascii=False, indent=2)
    print(f'Applied {len(merged)} entries · total: {len(ext["entries"]):,}')
else:
    print('\n(dry run — add --apply to write)')
