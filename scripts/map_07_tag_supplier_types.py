#!/usr/bin/env python3
"""MAP pipeline step 7 — tag each curated supplier with its dominant buyer type.

For each of the 400 curated suppliers in data/suppliers/_index.json, look up
their contract flows in data/map/supplier_to_buyers.json, classify the £
by buyer_type from data/map/buyers.json, and attribute a primary_buyer_type
(the type getting the biggest share of the supplier's total £).

Writes back to data/suppliers/_index.json with two new fields:
  - primary_buyer_type: "nhs" | "council" | "central_govt" | "police_fire" | "education" | "agency" | "other"
  - buyer_type_breakdown: {"nhs": 0.67, "council": 0.21, "other": 0.12}
"""
import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
SUPPLIER_INDEX = ROOT / "data/suppliers/_index.json"
SUPPLIER_TO_BUYERS = ROOT / "data/map/supplier_to_buyers.json"
BUYERS = ROOT / "data/map/buyers.json"


def main():
    idx = json.loads(SUPPLIER_INDEX.read_text(encoding="utf-8"))
    s2b = json.loads(SUPPLIER_TO_BUYERS.read_text(encoding="utf-8"))
    buyers = json.loads(BUYERS.read_text(encoding="utf-8"))

    # Buyer id → type lookup
    buyer_type = {bid: b.get("type", "other") for bid, b in buyers.items()}

    stats_found = 0
    stats_no_contracts = 0
    type_counter = defaultdict(int)

    for entry in idx:
        ch = entry.get("company_number")
        if not ch:
            entry["primary_buyer_type"] = "other"
            entry["buyer_type_breakdown"] = {}
            continue
        # s2b keys use either ch_number (for matched suppliers) or slug for unmatched
        flows = s2b.get(ch) or []
        if not flows:
            # Try the slug-style key (fallback)
            stats_no_contracts += 1
            entry["primary_buyer_type"] = "other"
            entry["buyer_type_breakdown"] = {}
            continue
        type_totals = defaultdict(float)
        total = 0.0
        for f in flows:
            t = buyer_type.get(f["buyer_id"], "other")
            type_totals[t] += f["gbp"]
            total += f["gbp"]
        if total == 0:
            entry["primary_buyer_type"] = "other"
            entry["buyer_type_breakdown"] = {}
            continue
        primary = max(type_totals.items(), key=lambda kv: kv[1])[0]
        breakdown = {t: round(v / total, 4) for t, v in type_totals.items()}
        entry["primary_buyer_type"] = primary
        entry["buyer_type_breakdown"] = dict(sorted(breakdown.items(), key=lambda kv: -kv[1]))
        stats_found += 1
        type_counter[primary] += 1

    print(f"Curated suppliers total: {len(idx):,}")
    print(f"With contract flows found: {stats_found:,}")
    print(f"No contracts in map data: {stats_no_contracts:,}")
    print(f"\nPrimary buyer type distribution:")
    for t, n in sorted(type_counter.items(), key=lambda kv: -kv[1]):
        print(f"  {t:20s} {n:>4}")

    SUPPLIER_INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nWrote {SUPPLIER_INDEX}")


if __name__ == "__main__":
    main()
