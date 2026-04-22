#!/usr/bin/env python3
"""MAP pipeline step 4 — build local Companies House postcode lookup index.

Reads the Companies House Basic Company Data bulk CSV (~6M rows), extracts
ch_number + normalised_name + postcode. Writes two JSON indexes:

  data/map/ch_postcode_by_number.json — { "02401034": "DL1 1RW" }
  data/map/ch_postcode_by_name.json   — { "studentloanscompanyltd": {"ch": "02401034", "postcode": "DL1 1RW"} }
"""
import csv
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ZIP_PATH = ROOT / "data/map/ch_bcd/BasicCompanyData-2026-04.zip"
OUT_BY_NUMBER = ROOT / "data/map/ch_postcode_by_number.json"
OUT_BY_NAME = ROOT / "data/map/ch_postcode_by_name.json"

POSTCODE_RE = re.compile(r"^[A-Z]{1,2}\d[A-Z\d]?\s*\d[A-Z]{2}$", re.IGNORECASE)


def normalise_pc(pc):
    if not pc:
        return None
    pc = str(pc).strip().upper().replace(" ", "")
    if len(pc) < 5 or len(pc) > 7:
        return None
    pc = pc[:-3] + " " + pc[-3:]
    return pc if POSTCODE_RE.match(pc) else None


def normalise_name(name):
    if not name:
        return None
    n = name.upper()
    # Strip trailing punctuation noise
    n = re.sub(r"[.,;:'\"`]", "", n)
    # Normalise common suffixes
    n = re.sub(r"\s+LIMITED\s*$", " LTD", n)
    n = re.sub(r"\s+PLC\s*$", " PLC", n)
    # Collapse whitespace + strip
    n = re.sub(r"\s+", " ", n).strip()
    # Final: lowercase + alphanum only for indexing
    key = re.sub(r"[^A-Za-z0-9]", "", n).lower()
    return key if key else None


def main():
    if not ZIP_PATH.exists():
        raise SystemExit(f"Missing {ZIP_PATH} — download CH BCD first (map_03 prereq)")

    by_number = {}
    by_name = {}
    stats = {"rows": 0, "with_postcode": 0, "indexed": 0}

    with zipfile.ZipFile(ZIP_PATH) as z:
        inner_files = [n for n in z.namelist() if n.endswith(".csv")]
        print(f"Zip contains {len(inner_files)} CSV file(s): {inner_files}")
        for inner in inner_files:
            with z.open(inner) as fh:
                import io
                reader = csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace"))
                # CH CSV has leading spaces in some column names — strip them
                reader.fieldnames = [f.strip() if f else f for f in (reader.fieldnames or [])]
                for row in reader:
                    # Also strip whitespace on value keys (defensive)
                    row = {k.strip() if k else k: v for k, v in row.items()}
                    stats["rows"] += 1
                    if stats["rows"] % 500000 == 0:
                        print(f"  {stats['rows']:,} rows processed · {stats['indexed']:,} indexed")
                    num = (row.get("CompanyNumber") or "").strip()
                    if not num:
                        continue
                    name = (row.get("CompanyName") or "").strip()
                    pc = normalise_pc(row.get("RegAddress.PostCode"))
                    if pc:
                        stats["with_postcode"] += 1
                    # Index by number (always)
                    by_number[num] = pc  # may be None, we still record the number
                    # Index by normalised name → pick shortest ch_number if collision
                    nk = normalise_name(name)
                    if nk and pc:  # only index named entries that have postcodes
                        existing = by_name.get(nk)
                        if not existing or len(existing["ch"]) > len(num):
                            by_name[nk] = {"ch": num, "postcode": pc}
                    if num and pc:
                        stats["indexed"] += 1

    # Drop the None-postcode entries from by_number (they're just noise)
    by_number_clean = {k: v for k, v in by_number.items() if v}

    print(f"\nRows read: {stats['rows']:,}")
    print(f"Rows with postcode: {stats['with_postcode']:,}")
    print(f"Indexed by ch_number: {len(by_number_clean):,}")
    print(f"Indexed by normalised_name: {len(by_name):,}")

    OUT_BY_NUMBER.parent.mkdir(parents=True, exist_ok=True)
    OUT_BY_NUMBER.write_text(json.dumps(by_number_clean, ensure_ascii=False), encoding="utf-8")
    OUT_BY_NAME.write_text(json.dumps(by_name, ensure_ascii=False), encoding="utf-8")

    import os
    print(f"\nFile sizes:")
    print(f"  ch_postcode_by_number.json: {os.path.getsize(OUT_BY_NUMBER)/1e6:.1f}MB")
    print(f"  ch_postcode_by_name.json:   {os.path.getsize(OUT_BY_NAME)/1e6:.1f}MB")


if __name__ == "__main__":
    main()
