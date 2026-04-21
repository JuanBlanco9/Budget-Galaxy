#!/usr/bin/env python3
"""MAP pipeline step 2 — batch geocode postcodes via postcodes.io bulk API.

Output: data/map/postcodes_cache.json
Format: { "AB1 2CD": {"lat": 51.5, "lng": -0.12, "lad24_cd": "E06000001", "lad24_nm": "...", "region": "London"} }
"""
import json
import urllib.request
import urllib.error
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "scripts/_postcodes_to_geocode.txt"
OUT = ROOT / "data/map/postcodes_cache.json"

API = "https://api.postcodes.io/postcodes"


def bulk_lookup(postcodes):
    """POST up to 100 postcodes at a time."""
    body = json.dumps({"postcodes": postcodes}).encode("utf-8")
    req = urllib.request.Request(API, data=body, method="POST",
                                  headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    postcodes = [ln.strip() for ln in INPUT.read_text(encoding="utf-8").splitlines() if ln.strip()]
    print(f"Geocoding {len(postcodes):,} postcodes in batches of 100...")

    # Load existing cache so we can resume
    cache = {}
    if OUT.exists():
        try:
            cache = json.loads(OUT.read_text(encoding="utf-8"))
            print(f"  cache hit: {len(cache):,} existing entries")
        except Exception:
            cache = {}

    to_lookup = [p for p in postcodes if p not in cache]
    print(f"  {len(to_lookup):,} new postcodes to look up")

    batch_size = 100
    hits = 0
    misses = 0
    for i in range(0, len(to_lookup), batch_size):
        batch = to_lookup[i:i + batch_size]
        try:
            result = bulk_lookup(batch)
        except Exception as e:
            print(f"  batch {i//batch_size + 1} error: {e}")
            time.sleep(2)
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
                hits += 1
            else:
                cache[q] = None
                misses += 1

        if (i // batch_size + 1) % 5 == 0:
            # Periodic save
            OUT.parent.mkdir(parents=True, exist_ok=True)
            OUT.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
            print(f"  progress: {i + len(batch)}/{len(to_lookup)} · saved cache")

        time.sleep(0.1)  # tiny delay between batches

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cache, ensure_ascii=False, indent=0), encoding="utf-8")

    total = len(cache)
    resolved = sum(1 for v in cache.values() if v)
    print(f"\nDone: {total:,} cached · {resolved:,} resolved ({resolved/total*100:.1f}%)")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
