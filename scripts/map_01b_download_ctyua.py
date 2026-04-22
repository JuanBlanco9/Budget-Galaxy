"""Download Counties + Unitary Authorities boundary (retry with correct service name)."""
import gzip
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
OUT_DIR = Path('data/map/boundaries')
SERVICE = 'Counties_and_Unitary_Authorities_December_2022_UK_BGC'
NAME_FIELD = 'CTYUA22NM'
CODE_FIELD = 'CTYUA22CD'
UA = 'Mozilla/5.0 (BudgetGalaxy boundary fetch)'

url = (
    f'https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/{SERVICE}/FeatureServer/0/query?'
    + urllib.parse.urlencode({
        'where': '1=1', 'outFields': '*', 'f': 'geojson',
        'resultRecordCount': 500, 'resultOffset': 0, 'returnGeometry': 'true',
    })
)
req = urllib.request.Request(url, headers={'User-Agent': UA})
with urllib.request.urlopen(req, timeout=120) as r:
    data = json.loads(r.read().decode('utf-8'))

stripped = []
for f in data.get('features') or []:
    p = f.get('properties') or {}
    stripped.append({
        'type': 'Feature',
        'properties': {'name': p.get(NAME_FIELD, ''), 'code': p.get(CODE_FIELD, '')},
        'geometry': f.get('geometry'),
    })
fc = {'type': 'FeatureCollection', 'features': stripped}
raw = json.dumps(fc, ensure_ascii=False).encode('utf-8')
(OUT_DIR / 'ctyua.geojson').write_bytes(raw)
with gzip.open(OUT_DIR / 'ctyua.geojson.gz', 'wb', compresslevel=9) as g:
    g.write(raw)
print(f'ctyua: {len(stripped)} features · {len(raw)/1e6:.2f}MB raw · {(OUT_DIR / "ctyua.geojson.gz").stat().st_size/1e6:.2f}MB gz')
