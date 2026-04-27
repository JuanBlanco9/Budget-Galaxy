#!/usr/bin/env python3
"""Refresh suppliers_v2/_index.json from the live per-supplier JSONs.

Every time a CH API batch runs, the per-file enrichment_stages flip to true,
but _index.json keeps the original BCD-phase skeleton view. This script
re-reads all per-supplier files and rewrites _index.json so the frontend
shows accurate ENRICHED/BASIC badges.
"""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "data/suppliers_v2"
OUT_INDEX = OUT_DIR / "_index.json"


def main():
    files = [f for f in os.listdir(OUT_DIR) if not f.startswith("_") and f.endswith(".json")]
    print(f"Scanning {len(files):,} supplier files...")
    index = {}
    for fn in files:
        try:
            p = json.loads((OUT_DIR / fn).read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  skip {fn}: {e}")
            continue
        ch = p.get("company_number")
        if not ch:
            continue
        index[ch] = {
            "company_number": ch,
            "display_name": p.get("display_name"),
            "status": (p.get("ch_profile") or {}).get("company_status") or p.get("status"),
            "total_gbp_2024": (p.get("spend_profile") or {}).get("total_gbp_2024", 0),
            "n_contracts": (p.get("spend_profile") or {}).get("n_contracts", 0),
            "n_buyers": (p.get("spend_profile") or {}).get("n_buyers", 0),
            "sic_codes": (p.get("sic_codes") or [])[:1],
            "postcode": (p.get("registered_office") or {}).get("postal_code"),
            "lad24_nm": (p.get("geo") or {}).get("lad24_nm"),
            "incorporated": p.get("incorporated"),
            "age_years": p.get("age_years"),
            "enrichment_stages": p.get("enrichment_stages") or {},
            "top_buyer_type": p.get("top_buyer_type"),
            "buyer_type_breakdown": p.get("buyer_type_breakdown") or {},
        }
    OUT_INDEX.write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
    n_enriched = sum(1 for e in index.values() if e["enrichment_stages"].get("ch_api_profile"))
    n_typed = sum(1 for e in index.values() if e.get("top_buyer_type") and e["top_buyer_type"] != "other")
    print(f"Wrote {OUT_INDEX} · {len(index):,} entries · {n_enriched:,} enriched with CH API · {n_typed:,} with non-other top_buyer_type")
    # Buyer type distribution
    from collections import Counter
    bt = Counter(e.get("top_buyer_type") or "(none)" for e in index.values())
    for t, n in sorted(bt.items(), key=lambda kv: -kv[1]):
        print(f"  {t:15s} {n:>6,}")


if __name__ == "__main__":
    main()
