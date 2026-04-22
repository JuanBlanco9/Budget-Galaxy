"""Apply patches.json to node_enrichment_extended.json with strict validation."""
import json
import sys
import shutil
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ENR = Path('data/uk/node_enrichment_extended.json')
PATCHES = Path('data/uk/factcheck/patches.json')

ext = json.load(ENR.open(encoding='utf-8'))
p = json.load(PATCHES.open(encoding='utf-8'))
patches = p['patches']

applied = []
failed = []

for i, pt in enumerate(patches):
    key = pt['entry_key']
    field = pt['field']
    find = pt['find']
    replace = pt['replace']
    ent = ext['entries'].get(key)
    if not ent:
        failed.append((i, pt, 'entry not found'))
        continue

    if field == 'key_stats':
        idx = pt.get('kstat_index')
        sub = pt.get('kstat_subfield', 'value')
        try:
            stat = ent['key_stats'][idx]
        except (KeyError, IndexError, TypeError):
            failed.append((i, pt, f'key_stats[{idx}] not found'))
            continue
        original = stat.get(sub, '')
        count = original.count(find)
        if count == 0:
            failed.append((i, pt, f'find not in key_stats[{idx}].{sub}'))
            continue
        if count > 1:
            failed.append((i, pt, f'find appears {count}x — ambiguous'))
            continue
        stat[sub] = original.replace(find, replace, 1)
        applied.append((i, pt))
    elif field in ('description', 'notes'):
        original = ent.get(field, '')
        count = original.count(find)
        if count == 0:
            failed.append((i, pt, f'find not in {field}'))
            continue
        if count > 1:
            failed.append((i, pt, f'find appears {count}x in {field} — ambiguous'))
            continue
        ent[field] = original.replace(find, replace, 1)
        applied.append((i, pt))
    else:
        failed.append((i, pt, f'unsupported field {field!r}'))

print(f'Applied: {len(applied)} / {len(patches)}')
print(f'Failed: {len(failed)}')
if failed:
    print('\n--- FAILED ---')
    for i, pt, reason in failed:
        print(f'  #{i} [{pt.get("severity","?"):6s}] {pt["entry_key"][:50]} · {pt["drift_ref"]}')
        print(f'         reason: {reason}')
        print(f'         find:   {pt["find"][:120]}')

if applied:
    # Backup then write
    backup = ENR.with_suffix('.json.bak.factcheck')
    if not backup.exists():
        shutil.copy(ENR, backup)
        print(f'\nBackup: {backup.name}')
    ENR.write_text(json.dumps(ext, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'\nWrote {ENR.name} ({len(applied)} patches applied)')

# Audit
if applied:
    from collections import Counter
    sev = Counter(pt.get('severity','?') for _, pt in applied)
    print(f'Applied by severity: {dict(sev)}')
