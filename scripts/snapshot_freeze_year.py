#!/usr/bin/env python3
"""Freeze a year-snapshot of Budget Galaxy data.

Run AFTER all enrichment for the year is complete, BEFORE starting work on
the next year. CH API returns "current state" not historical, so without
this freeze, refreshing for year N+1 corrupts the year N picture.

Usage:
  py scripts/snapshot_freeze_year.py 2024
  py scripts/snapshot_freeze_year.py 2024 --as-of 2026-04-27

Output:
  data/suppliers_snapshots/<year>/
    suppliers/                  ← per-supplier files (with as_of_date stamped)
    suppliers_index.json        ← curated 400 index
    suppliers_v2_index.json     ← bulk-enriched index
    node_enrichment.json        ← hand-curated narratives
    budget_tree.json            ← tree structure
    buyers.json
    suppliers_summary.json
    buyer_to_suppliers.json
    supplier_to_buyers.json
    _manifest.json              ← metadata + sha256 index
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
import sys
import glob
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.stdout.reconfigure(encoding="utf-8")
sys.setrecursionlimit(50000)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("year", type=int, help="Fiscal year to freeze, e.g. 2024")
    ap.add_argument("--as-of", default=None, help="ISO date for as_of_date stamp (default: today)")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    year = args.year
    as_of = args.as_of or dt.date.today().isoformat()
    snap_root = ROOT / f"data/suppliers_snapshots/{year}"

    if snap_root.exists():
        print(f"ERROR: {snap_root} already exists. Refusing to overwrite.", file=sys.stderr)
        print("If you really want to refresh, delete the directory first.", file=sys.stderr)
        sys.exit(1)

    print(f"Freezing year {year} · as_of {as_of}")
    print(f"Target: {snap_root}")
    print()

    sources = [
        # (live path, snapshot relative path, kind)
        ("data/suppliers/_index.json",         "suppliers_index.json",     "json"),
        ("data/suppliers_v2/_index.json",      "suppliers_v2_index.json",  "json"),
        ("data/uk/node_enrichment_extended.json", "node_enrichment.json",  "json"),
        (f"data/uk/uk_budget_tree_{year}.json",   "budget_tree.json",       "json"),
        ("data/map/buyers.json",                  "buyers.json",            "json"),
        ("data/map/suppliers.json",               "suppliers_summary.json", "json"),
        ("data/map/buyer_to_suppliers.json",      "buyer_to_suppliers.json","json"),
        ("data/map/supplier_to_buyers.json",      "supplier_to_buyers.json","json"),
    ]

    if args.dry_run:
        print("Would copy these:")
        for src, dst, _ in sources:
            full = ROOT / src
            sz = full.stat().st_size if full.exists() else 0
            print(f"  {src}  →  {dst}   ({sz/1024/1024:.1f}MB)")
        n_v2 = len(glob.glob(str(ROOT / "data/suppliers_v2/[0-9A-Z]*.json")))
        print(f"  data/suppliers_v2/*.json  →  suppliers/  ({n_v2:,} files, with as_of_date stamp)")
        return

    snap_root.mkdir(parents=True, exist_ok=False)
    (snap_root / "suppliers").mkdir(exist_ok=False)

    manifest = {
        "year": year,
        "as_of_date": as_of,
        "frozen_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "schema_version": "1.0",
        "files": {},
    }

    # 1. Copy aggregate JSON files
    for src, dst, _kind in sources:
        full = ROOT / src
        if not full.exists():
            print(f"  WARN missing: {src}")
            continue
        target = snap_root / dst
        shutil.copy2(full, target)
        manifest["files"][dst] = {
            "source": src,
            "size_bytes": target.stat().st_size,
            "sha256": sha256_file(target),
        }
        print(f"  copied {src}  →  {dst}  ({target.stat().st_size/1024/1024:.1f}MB)")

    # 2a. Copy curated 400 individual files (rich hand-curated profiles)
    print()
    print("Copying + stamping curated 400 supplier profiles...")
    cur_files = sorted(glob.glob(str(ROOT / "data/suppliers/[0-9A-Z]*.json")))
    cur_dir = snap_root / "suppliers_curated"
    cur_dir.mkdir(exist_ok=False)
    n_cur = 0
    for src_path in cur_files:
        try:
            with open(src_path, encoding="utf-8") as f:
                d = json.load(f)
        except Exception:
            continue
        d["as_of_date"] = as_of
        d["data_year"] = year
        with open(cur_dir / os.path.basename(src_path), "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        n_cur += 1
    print(f"  copied {n_cur:,} curated profiles")
    manifest["files"]["suppliers_curated/"] = {"n_files": n_cur}

    # 2b. Copy + stamp every per-supplier v2 file
    print()
    print("Stamping + copying per-supplier v2 files...")
    v2_files = sorted(glob.glob(str(ROOT / "data/suppliers_v2/[0-9A-Z]*.json")))
    n_stamped = 0
    n_skipped = 0
    sup_dir = snap_root / "suppliers"
    for src_path in v2_files:
        try:
            with open(src_path, encoding="utf-8") as f:
                d = json.load(f)
        except Exception as e:
            print(f"  skip {os.path.basename(src_path)}: {e}")
            n_skipped += 1
            continue
        d["as_of_date"] = as_of
        d["data_year"] = year
        with open(sup_dir / os.path.basename(src_path), "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        n_stamped += 1
        if n_stamped % 2000 == 0:
            print(f"    {n_stamped:,} / {len(v2_files):,}")

    manifest["files"]["suppliers/"] = {
        "n_files": n_stamped,
        "n_skipped": n_skipped,
    }
    print(f"  stamped {n_stamped:,} supplier files (skipped {n_skipped})")

    # 3. Counts breakdown
    enriched = sum(
        1 for p in v2_files
        if os.path.exists(p) and (
            (lambda d: (d.get("enrichment_stages") or {}).get("ch_api_profile"))(
                json.load(open(p, encoding="utf-8"))
            )
        )
    )
    manifest["counts"] = {
        "n_suppliers_v2": n_stamped,
        "n_suppliers_v2_enriched": enriched,
        "n_suppliers_v2_basic": n_stamped - enriched,
    }

    # Try to count budget tree entries
    try:
        ne = json.load(open(snap_root / "node_enrichment.json", encoding="utf-8"))
        manifest["counts"]["n_node_enrichment_entries"] = len(ne.get("entries", {}))
    except Exception:
        pass
    try:
        cur = json.load(open(snap_root / "suppliers_index.json", encoding="utf-8"))
        manifest["counts"]["n_suppliers_curated"] = len(cur) if isinstance(cur, list) else 0
    except Exception:
        pass

    # 4. Write manifest
    (snap_root / "_manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print()
    print(f"Manifest written: {snap_root / '_manifest.json'}")
    print(f"Counts: {json.dumps(manifest['counts'], indent=2)}")
    print()
    print("Next step (manual):")
    print(f"  git add data/suppliers_snapshots/{year}/")
    print(f"  git commit -m 'snapshot: freeze {year} fiscal year'")
    print(f"  git tag -a snapshot-{year} -m 'Frozen state at fiscal {year} close'")


if __name__ == "__main__":
    main()
