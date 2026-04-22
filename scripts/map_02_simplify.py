"""Simplify boundary GeoJSONs with Douglas-Peucker via shapely.

Per-layer tolerance (degrees, ~111km/degree at UK):
  countries        0.005   ~500m   (baseline, always visible, needs detail for Scottish coast)
  regions          0.008   ~800m
  ctyua            0.005   ~500m
  lad              0.003   ~300m   (councils, main interaction layer)
  constituencies   0.004   ~400m
  nhs_icb          0.008   ~800m
  police           0.008   ~800m

Also reduces coordinate precision to 5 decimals (~1m resolution, plenty for UK admin).
"""
import gzip
import json
import sys
from pathlib import Path
from shapely.geometry import shape, mapping
from shapely.ops import transform

sys.stdout.reconfigure(encoding='utf-8')
BOUND = Path('data/map/boundaries')

LAYER_TOL = {
    'countries': 0.005,
    'regions': 0.008,
    'ctyua': 0.005,
    'lad': 0.003,
    'constituencies': 0.004,
    'nhs_icb': 0.008,
    'police': 0.008,
}

def round_coords(obj, prec=5):
    """Recursively round all coordinate numbers to `prec` decimal places."""
    if isinstance(obj, float):
        return round(obj, prec)
    if isinstance(obj, list):
        return [round_coords(x, prec) for x in obj]
    return obj

def simplify_feature(f, tol):
    g = f.get('geometry')
    if not g:
        return f
    geom = shape(g)
    if geom.is_empty:
        return f
    simp = geom.simplify(tol, preserve_topology=True)
    if simp.is_empty:
        simp = geom
    new_geom = mapping(simp)
    # Round coords
    new_geom['coordinates'] = round_coords(new_geom['coordinates'], 5)
    return {'type': 'Feature', 'properties': f.get('properties', {}), 'geometry': new_geom}

def main():
    total_before = 0
    total_after = 0
    for key, tol in LAYER_TOL.items():
        raw_path = BOUND / f'{key}.geojson'
        if not raw_path.exists():
            print(f'[{key}] SKIP (missing)')
            continue
        raw = raw_path.read_bytes()
        before = len(raw)
        fc = json.loads(raw)
        n = len(fc.get('features') or [])
        simp_features = [simplify_feature(f, tol) for f in fc['features']]
        out_fc = {'type': 'FeatureCollection', 'features': simp_features}
        out_raw = json.dumps(out_fc, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
        after = len(out_raw)
        # Overwrite raw + gz
        raw_path.write_bytes(out_raw)
        with gzip.open(BOUND / f'{key}.geojson.gz', 'wb', compresslevel=9) as g:
            g.write(out_raw)
        gz_size = (BOUND / f'{key}.geojson.gz').stat().st_size
        total_before += before
        total_after += gz_size
        print(f'[{key}] tol={tol}° · {n} features · {before/1e6:.2f}MB → {after/1e6:.2f}MB raw · {gz_size/1e6:.2f}MB gz ({gz_size/before*100:.0f}% of original raw)')
    print(f'\n=== TOTAL ===')
    print(f'Pre-simplify raw: {total_before/1e6:.2f}MB')
    print(f'Post-simplify gz: {total_after/1e6:.2f}MB · savings {(1-total_after/total_before)*100:.1f}%')

if __name__ == '__main__':
    main()
