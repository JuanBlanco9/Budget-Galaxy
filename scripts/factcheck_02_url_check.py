"""Phase 3 fact-check step 2: URL resolvability via parallel HEAD requests."""
import json
import sys
import urllib.request
import urllib.error
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.stdout.reconfigure(encoding='utf-8')
socket.setdefaulttimeout(15)

INPUT = sys.argv[1] if len(sys.argv) > 1 else 'data/uk/factcheck/top_entries.json'
OUTPUT = sys.argv[2] if len(sys.argv) > 2 else 'data/uk/factcheck/url_results.json'
data = json.load(open(INPUT, encoding='utf-8'))
all_urls = []
for e in data:
    for u in e['urls']:
        all_urls.append((e['key'], u))

print(f'Checking {len(all_urls)} URLs...', flush=True)

def head(item):
    key, url = item
    req = urllib.request.Request(url, method='HEAD',
        headers={'User-Agent': 'Mozilla/5.0 (BudgetGalaxy factcheck)'})
    try:
        resp = urllib.request.urlopen(req, timeout=15)
        return (key, url, resp.status, None)
    except urllib.error.HTTPError as e:
        if e.code in (403, 405):
            # Some servers reject HEAD; try GET
            req2 = urllib.request.Request(url, method='GET',
                headers={'User-Agent': 'Mozilla/5.0 (BudgetGalaxy factcheck)'})
            try:
                resp = urllib.request.urlopen(req2, timeout=15)
                return (key, url, resp.status, 'head-rejected-get-ok')
            except Exception as e2:
                return (key, url, None, f'{e.code} then {type(e2).__name__}:{e2}')
        return (key, url, e.code, str(e))
    except Exception as e:
        return (key, url, None, f'{type(e).__name__}:{e}')

results = []
with ThreadPoolExecutor(max_workers=20) as ex:
    futures = {ex.submit(head, item): item for item in all_urls}
    for i, f in enumerate(as_completed(futures), 1):
        r = f.result()
        results.append(r)
        if i % 25 == 0:
            print(f'  {i}/{len(all_urls)}', flush=True)

ok = [r for r in results if r[2] and r[2] < 400]
bad = [r for r in results if not r[2] or r[2] >= 400]
print(f'\nOK (2xx/3xx): {len(ok)} / {len(results)}')
print(f'BAD (4xx/5xx/error): {len(bad)}')
print('\nBAD urls:')
for key, url, code, err in sorted(bad, key=lambda x: (x[0], x[1])):
    print(f'  [{code or "ERR"}] {key[:50]:<50} {url}')
    if err and code is None:
        print(f'         {err[:150]}')

json.dump(
    [{'key': k, 'url': u, 'status': s, 'error': e} for k, u, s, e in results],
    open(OUTPUT, 'w', encoding='utf-8'),
    indent=2, ensure_ascii=False
)
print(f'\nWrote {OUTPUT}')
