#!/usr/bin/env python3
"""MAP pipeline step 6 — geocode the newly-resolved supplier postcodes.

Appends to existing data/map/postcodes_cache.json.
"""
import json
import urllib.request
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "scripts/_postcodes_new_to_geocode.txt"
CACHE = ROOT / "data/map/postcodes_cache.json"
API = "https://api.postcodes.io/postcodes"


def bulk_lookup(postcodes):
    body = json.dumps({"postcodes": postcodes}).encode("utf-8")
    req = urllib.request.Request(API, data=body, method="POST",
                                  headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    new_pcs = [ln.strip() for ln in INPUT.read_text(encoding="utf-8").splitlines() if ln.strip()]
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    to_lookup = [p for p in new_pcs if p not in cache]
    print(f"New postcodes: {len(new_pcs):,}")
    print(f"Not yet cached: {len(to_lookup):,}")

    if not to_lookup:
        print("Nothing to lookup.")
        return

    batch_size = 100
    for i in range(0, len(to_lookup), batch_size):
        batch = to_lookup[i:i + batch_size]
        try:
            result = bulk_lookup(batch)
        except Exception as e:
            print(f"  batch {i//batch_size + 1} error: {e}")
            time.sleep(3)
            continue

        for item in result.get("result", []):
            q = item.get("query")
            r = item.get("result")
            if q and r:
                cache[q] = {
                    "lat": r.get("latitude"),
                    "lng": r.get("longitude"),
                    "lad24_cd": r.get("codes", {}).get("admin_district"),
                    "lad24_nm": r.get("admin_district"),
                    "region": r.get("region"),
                    "country": r.get("country"),
                    "european_electoral_region": r.get("european_electoral_region"),
                    "nuts": r.get("nuts"),
                }
            else:
                cache[q] = None

        if (i // batch_size + 1) % 10 == 0:
            CACHE.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
            print(f"  progress: {i + len(batch):,}/{len(to_lookup):,} · saved cache")

        time.sleep(0.1)

    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")
    total = len(cache)
    resolved = sum(1 for v in cache.values() if v)
    print(f"\nCache total: {total:,} · resolved: {resolved:,} ({resolved/total*100:.1f}%)")


if __name__ == "__main__":
    main()
