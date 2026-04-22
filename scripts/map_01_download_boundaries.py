"""Download UK admin boundary GeoJSONs from ONS Open Geography Portal.

Uses the ArcGIS REST FeatureServer endpoints with BGC (Boundaries Generalised
Clipped, 200m tolerance) variants for pre-simplified polygons.

Layers pulled:
  1. Countries (4: Eng/Sco/Wal/NI)
  2. Regions (9, England only)
  3. Counties + Unitary Authorities (~152)
  4. Local Authority Districts / LAD24 (~361)  — "councils" layer
  5. Westminster Constituencies July 2024 (650)
  6. NHS Integrated Care Boards (42, England only)
  7. Police Force Areas (45)

Saves to data/map/boundaries/<layer>.geojson (pretty-printed gzipped).
"""
import gzip
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

OUT_DIR = Path('data/map/boundaries')
OUT_DIR.mkdir(parents=True, exist_ok=True)

UA = 'Mozilla/5.0 (BudgetGalaxy boundary fetch)'

# ONS Open Geography Portal ArcGIS FeatureServer endpoints.
# Pattern: https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/<SERVICE>/FeatureServer/0/query
#   with ?where=1=1&outFields=<fields>&f=geojson&resultRecordCount=N&resultOffset=N for paging.
# BGC = Boundaries Generalised Clipped, ~20% of full resolution.
LAYERS = [
    {
        'key': 'countries',
        'service': 'Countries_December_2023_Boundaries_UK_BGC',
        'name_field': 'CTRY23NM',
        'code_field': 'CTRY23CD',
        'description': 'UK Countries (4)',
    },
    {
        'key': 'regions',
        'service': 'Regions_December_2022_EN_BGC',
        'name_field': 'RGN22NM',
        'code_field': 'RGN22CD',
        'description': 'English Regions (9)',
    },
    {
        'key': 'ctyua',
        'service': 'Counties_and_Unitary_Authorities_December_2023_UK_BGC',
        'name_field': 'CTYUA23NM',
        'code_field': 'CTYUA23CD',
        'description': 'Counties + Unitary Authorities (~152)',
    },
    {
        'key': 'lad',
        'service': 'Local_Authority_Districts_May_2024_Boundaries_UK_BGC',
        'name_field': 'LAD24NM',
        'code_field': 'LAD24CD',
        'description': 'Local Authority Districts May 2024 (~361)',
    },
    {
        'key': 'constituencies',
        'service': 'Westminster_Parliamentary_Constituencies_July_2024_Boundaries_UK_BGC',
        'name_field': 'PCON24NM',
        'code_field': 'PCON24CD',
        'description': 'Westminster Constituencies 2024 (650)',
    },
    {
        'key': 'nhs_icb',
        'service': 'Integrated_Care_Boards_April_2023_EN_BGC',
        'name_field': 'ICB23NM',
        'code_field': 'ICB23CD',
        'description': 'NHS Integrated Care Boards (42)',
    },
    {
        'key': 'police',
        'service': 'Police_Force_Areas_December_2023_EW_BGC',
        'name_field': 'PFA23NM',
        'code_field': 'PFA23CD',
        'description': 'Police Force Areas (~45)',
    },
]

ESMARspQHYMw9BZ9 = 'https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services'

def build_query_url(service, offset=0, count=2000, out_fields='*'):
    params = {
        'where': '1=1',
        'outFields': out_fields,
        'f': 'geojson',
        'resultRecordCount': count,
        'resultOffset': offset,
        'returnGeometry': 'true',
    }
    return f'{ESMARspQHYMw9BZ9}/{service}/FeatureServer/0/query?' + urllib.parse.urlencode(params)


def fetch_layer(service, out_fields='*'):
    """Download all features with paging. Return a FeatureCollection."""
    features = []
    offset = 0
    COUNT = 2000
    while True:
        url = build_query_url(service, offset, COUNT, out_fields)
        req = urllib.request.Request(url, headers={'User-Agent': UA})
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=90) as r:
                    data = json.loads(r.read().decode('utf-8'))
                break
            except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError) as e:
                if attempt == 2:
                    raise
                print(f'    retry {attempt+1}/3 after {e}', flush=True)
                time.sleep(2 * (attempt + 1))
        batch = data.get('features') or []
        features.extend(batch)
        if len(batch) < COUNT or not data.get('properties', {}).get('exceededTransferLimit'):
            break
        offset += COUNT
        print(f'    paging: offset={offset} · features so far={len(features)}', flush=True)
    return {'type': 'FeatureCollection', 'features': features}


def main():
    total_before = 0
    total_after = 0
    results = []
    for layer in LAYERS:
        key = layer['key']
        svc = layer['service']
        desc = layer['description']
        print(f'\n[{key}] {desc}', flush=True)
        print(f'  service: {svc}', flush=True)
        try:
            fc = fetch_layer(svc)
        except Exception as e:
            print(f'  FAILED: {e}', flush=True)
            results.append({'key': key, 'status': 'failed', 'error': str(e)})
            continue
        n_features = len(fc.get('features') or [])
        print(f'  features: {n_features}', flush=True)

        # Strip properties to just name + code to minimize size
        nf = layer['name_field']
        cf = layer['code_field']
        stripped = []
        for f in fc['features']:
            p = f.get('properties') or {}
            new_p = {
                'name': p.get(nf) or p.get(nf.replace('NM', '23NM')) or '',
                'code': p.get(cf) or p.get(cf.replace('CD', '23CD')) or '',
            }
            stripped.append({
                'type': 'Feature',
                'properties': new_p,
                'geometry': f.get('geometry'),
            })
        fc_clean = {'type': 'FeatureCollection', 'features': stripped}
        raw = json.dumps(fc_clean, ensure_ascii=False).encode('utf-8')
        total_before += len(raw)

        # Save uncompressed + gzip
        out_path = OUT_DIR / f'{key}.geojson'
        out_gz = OUT_DIR / f'{key}.geojson.gz'
        out_path.write_bytes(raw)
        with gzip.open(out_gz, 'wb', compresslevel=9) as g:
            g.write(raw)
        gz_size = out_gz.stat().st_size
        total_after += gz_size
        print(f'  out: {out_path.name} ({len(raw)/1e6:.2f}MB raw) · {out_gz.name} ({gz_size/1e6:.2f}MB gz)', flush=True)
        results.append({'key': key, 'status': 'ok', 'n_features': n_features, 'raw_mb': len(raw)/1e6, 'gz_mb': gz_size/1e6})

    print(f'\n=== SUMMARY ===')
    print(f'Raw total: {total_before/1e6:.2f}MB · Gzipped total: {total_after/1e6:.2f}MB')
    json.dump(results, open(OUT_DIR / '_manifest.json', 'w', encoding='utf-8'), indent=2)
    print(f'Manifest: {OUT_DIR}/_manifest.json')


if __name__ == '__main__':
    main()
