#!/usr/bin/env python3
"""MAP pipeline step 5 — resolve supplier postcodes via local CH index.

Reads:
  data/map/suppliers.json (current supplier records)
  data/map/ch_postcode_by_number.json (CH BCD index by ch_number)
  data/map/ch_postcode_by_name.json   (CH BCD index by normalised name)

Writes:
  data/map/supplier_postcodes_resolved.json — { supplier_id: {postcode, source} }
  scripts/_postcodes_new_to_geocode.txt — new postcodes to geocode

Strategy:
  1. Supplier already has postcode → skip
  2. Supplier has ch_number → lookup by_number
  3. Supplier no ch_number → fuzzy name match to by_name
  4. Drop junk entries (placeholder names, generic lists)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SUPPLIERS = ROOT / "data/map/suppliers.json"
BY_NUM = ROOT / "data/map/ch_postcode_by_number.json"
BY_NAME = ROOT / "data/map/ch_postcode_by_name.json"
OUT_RESOLVED = ROOT / "data/map/supplier_postcodes_resolved.json"
OUT_NEW_PCS = ROOT / "scripts/_postcodes_new_to_geocode.txt"

GEO_CACHE = ROOT / "data/map/postcodes_cache.json"


def normalise_name(name):
    if not name:
        return None
    n = name.upper()
    n = re.sub(r"[.,;:'\"`]", "", n)
    n = re.sub(r"\s+LIMITED\s*$", " LTD", n)
    n = re.sub(r"\s+", " ", n).strip()
    key = re.sub(r"[^A-Za-z0-9]", "", n).lower()
    return key if key else None


# Known junk patterns in OCDS supplier_name fields
JUNK_NAME_PATTERNS = [
    re.compile(r"^a list of", re.I),
    re.compile(r"^please see", re.I),
    re.compile(r"^not applicable", re.I),
    re.compile(r"^n/a$", re.I),
    re.compile(r"^tbc$", re.I),
    re.compile(r"^to be confirmed", re.I),
    re.compile(r"^various suppliers", re.I),
    re.compile(r"^multiple suppliers", re.I),
    re.compile(r"^see attachment", re.I),
    re.compile(r"attached", re.I),
]


def is_junk(name):
    if not name or len(name) < 2 or len(name) > 200:
        return True
    for p in JUNK_NAME_PATTERNS:
        if p.search(name):
            return True
    return False


def main():
    suppliers = json.loads(SUPPLIERS.read_text(encoding="utf-8"))
    print(f"Loading CH indexes...")
    by_number = json.loads(BY_NUM.read_text(encoding="utf-8"))
    by_name = json.loads(BY_NAME.read_text(encoding="utf-8"))
    geo_cache = json.loads(GEO_CACHE.read_text(encoding="utf-8")) if GEO_CACHE.exists() else {}

    print(f"Processing {len(suppliers):,} suppliers...")
    resolved = {}  # supplier_id → {postcode, source}
    stats = {
        "already_has_postcode": 0,
        "resolved_via_ch_number": 0,
        "resolved_via_name": 0,
        "no_ch_no_name_match": 0,
        "junk": 0,
        "ch_number_not_in_index": 0,
    }

    new_postcodes = set()

    for sid, s in suppliers.items():
        name = s.get("name")
        ch = s.get("ch_number")

        # Skip junk
        if is_junk(name):
            stats["junk"] += 1
            continue

        # Already has postcode (187 curated)
        if s.get("postcode"):
            stats["already_has_postcode"] += 1
            continue

        pc = None
        source = None

        # Try ch_number first
        if ch and ch in by_number:
            pc = by_number[ch]
            source = "ch_number"
            stats["resolved_via_ch_number"] += 1
        elif ch:
            stats["ch_number_not_in_index"] += 1

        # Fallback to name match
        if not pc:
            nk = normalise_name(name)
            if nk and nk in by_name:
                pc = by_name[nk]["postcode"]
                source = "name_match"
                stats["resolved_via_name"] += 1

        if pc:
            resolved[sid] = {"postcode": pc, "source": source}
            if pc not in geo_cache:
                new_postcodes.add(pc)
        else:
            stats["no_ch_no_name_match"] += 1

    print(f"\nResults:")
    for k, v in stats.items():
        print(f"  {k}: {v:,}")
    print(f"\nTotal newly resolved postcodes: {len(resolved):,}")
    print(f"Unique postcodes to geocode: {len(new_postcodes):,}")

    OUT_RESOLVED.parent.mkdir(parents=True, exist_ok=True)
    OUT_RESOLVED.write_text(json.dumps(resolved, ensure_ascii=False, indent=0), encoding="utf-8")
    OUT_NEW_PCS.write_text("\n".join(sorted(new_postcodes)) + "\n", encoding="utf-8")

    print(f"\nWrote {OUT_RESOLVED}")
    print(f"Wrote {OUT_NEW_PCS}")


if __name__ == "__main__":
    main()
