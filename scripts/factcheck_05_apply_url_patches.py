"""Apply url_patches.json to node_enrichment_extended.json."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ENR = Path('data/uk/node_enrichment_extended.json')
URL_PATCHES = Path('data/uk/factcheck/url_patches.json')

ext = json.load(ENR.open(encoding='utf-8'))
patches = json.load(URL_PATCHES.open(encoding='utf-8'))['url_patches']

applied = {'repair': 0, 'fallback': 0, 'keep': 0, 'skip': 0}
failed = []

for pt in patches:
    action = pt.get('action', 'repair')
    key = pt['entry_key']
    idx = pt['source_index']
    old = pt['old_url']

    if action == 'keep_as_is':
        applied['keep'] += 1
        continue

    new = pt.get('new_url') or pt.get('fallback_url')
    if not new:
        failed.append((key, idx, 'no new_url or fallback_url'))
        continue

    ent = ext['entries'].get(key)
    if not ent:
        failed.append((key, idx, 'entry missing'))
        continue
    srcs = ent.get('sources') or []
    if idx >= len(srcs):
        failed.append((key, idx, f'source_index out of range (len={len(srcs)})'))
        continue
    current = srcs[idx].get('url')
    if current != old:
        # URL drifted from expected old — skip to be safe
        failed.append((key, idx, f'current url != old_url · current={current!r}'))
        continue

    srcs[idx]['url'] = new
    if action == 'fallback_publisher_root':
        applied['fallback'] += 1
    else:
        applied['repair'] += 1

print(f'Applied: repair={applied["repair"]} · fallback={applied["fallback"]} · keep={applied["keep"]}')
print(f'Failed: {len(failed)}')
for k, i, r in failed:
    print(f'  {k[:50]} [src#{i}] {r}')

if applied['repair'] or applied['fallback']:
    ENR.write_text(json.dumps(ext, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'\nWrote {ENR.name}')
