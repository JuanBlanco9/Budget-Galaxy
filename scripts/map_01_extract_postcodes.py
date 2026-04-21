#!/usr/bin/env python3
"""MAP pipeline step 1 — extract all unique postcodes from 2024 contracts.

Output: scripts/_postcodes_to_geocode.txt (one postcode per line)
"""
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
CONTRACTS = ROOT / "data/procurement/contracts_flat_2024.jsonl"
OUT_POSTCODES = ROOT / "scripts/_postcodes_to_geocode.txt"
OUT_STATS = ROOT / "data/map/_postcode_stats.json"

# UK postcode regex (rough)
POSTCODE_RE = re.compile(r"^[A-Z]{1,2}\d[A-Z\d]?\s*\d[A-Z]{2}$", re.IGNORECASE)


def normalise(pc):
    if not pc:
        return None
    pc = str(pc).strip().upper()
    # Insert space before last 3 chars if missing
    pc = pc.replace(" ", "")
    if len(pc) < 5 or len(pc) > 7:
        return None
    pc = pc[:-3] + " " + pc[-3:]
    if not POSTCODE_RE.match(pc):
        return None
    return pc


def main():
    buyer_pcs = set()
    supplier_pcs = set()
    stats = {
        "rows_read": 0,
        "buyer_has_postcode": 0,
        "supplier_has_postcode": 0,
        "buyer_postcodes_unique": 0,
        "supplier_postcodes_unique": 0,
        "all_unique_postcodes": 0,
    }
    with CONTRACTS.open(encoding="utf-8") as f:
        for line in f:
            stats["rows_read"] += 1
            try:
                d = json.loads(line)
            except Exception:
                continue
            bp = normalise(d.get("buyer_postcode"))
            sp = normalise(d.get("supplier_postcode"))
            if bp:
                buyer_pcs.add(bp)
                stats["buyer_has_postcode"] += 1
            if sp:
                supplier_pcs.add(sp)
                stats["supplier_has_postcode"] += 1

    # Also harvest postcodes from supplier index
    supidx = ROOT / "data/suppliers/_index.json"
    if supidx.exists():
        for entry in json.loads(supidx.read_text(encoding="utf-8")):
            # _index entries don't carry postcode; skip
            pass
    # Per-supplier registered office postcodes
    for fn in (ROOT / "data/suppliers").iterdir():
        if fn.name.startswith("_"):
            continue
        try:
            sup = json.loads(fn.read_text(encoding="utf-8"))
        except Exception:
            continue
        ro = (sup.get("identity") or {}).get("registered_office") or {}
        pc = normalise(ro.get("postal_code") if isinstance(ro, dict) else None)
        if pc:
            supplier_pcs.add(pc)

    all_pcs = buyer_pcs | supplier_pcs
    stats["buyer_postcodes_unique"] = len(buyer_pcs)
    stats["supplier_postcodes_unique"] = len(supplier_pcs)
    stats["all_unique_postcodes"] = len(all_pcs)

    OUT_STATS.parent.mkdir(parents=True, exist_ok=True)
    OUT_STATS.write_text(json.dumps(stats, indent=2), encoding="utf-8")
    OUT_POSTCODES.write_text("\n".join(sorted(all_pcs)) + "\n", encoding="utf-8")

    print(f"Contracts rows read: {stats['rows_read']:,}")
    print(f"Rows with buyer postcode: {stats['buyer_has_postcode']:,}")
    print(f"Rows with supplier postcode: {stats['supplier_has_postcode']:,}")
    print(f"Unique buyer postcodes: {stats['buyer_postcodes_unique']:,}")
    print(f"Unique supplier postcodes: {stats['supplier_postcodes_unique']:,}")
    print(f"Total unique postcodes to geocode: {stats['all_unique_postcodes']:,}")
    print(f"\nWrote {OUT_POSTCODES}")


if __name__ == "__main__":
    main()
