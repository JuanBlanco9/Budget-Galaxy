#!/usr/bin/env python3
"""MAP pipeline step 3 — aggregate contracts into buyer + supplier summaries.

Output:
  data/map/buyers.json       — each buyer: name, postcode, lat/lng, £ total, n_contracts, n_suppliers, type
  data/map/suppliers.json    — each supplier: name, ch_number (if any), postcode, lat/lng, £ total, n_contracts, n_buyers
  data/map/buyer_to_suppliers.json — {buyer_id: [{supplier_key, £, n_contracts}]} top-50 per buyer
  data/map/supplier_to_buyers.json — reverse
"""
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
CONTRACTS = ROOT / "data/procurement/contracts_flat_2024.jsonl"
POSTCODES = ROOT / "data/map/postcodes_cache.json"
OUT_DIR = ROOT / "data/map"

POSTCODE_RE = re.compile(r"^[A-Z]{1,2}\d[A-Z\d]?\s*\d[A-Z]{2}$", re.IGNORECASE)


def normalise_pc(pc):
    if not pc:
        return None
    pc = str(pc).strip().upper().replace(" ", "")
    if len(pc) < 5 or len(pc) > 7:
        return None
    pc = pc[:-3] + " " + pc[-3:]
    return pc if POSTCODE_RE.match(pc) else None


def classify_buyer(name):
    if not name:
        return "other"
    n = name.lower()
    if "nhs" in n or "icb" in n or "integrated care" in n:
        return "nhs"
    if any(w in n for w in ["council", "borough", "county council", "city of", "district council"]):
        return "council"
    if "university" in n or "college" in n or "school" in n:
        return "education"
    if "police" in n or "fire" in n or "constabulary" in n:
        return "police_fire"
    if "department" in n or "ministry" in n or "hm " in n or "home office" in n or "cabinet office" in n or "foreign" in n or "treasury" in n:
        return "central_govt"
    if "authority" in n or "agency" in n:
        return "agency"
    if "trust" in n and "nhs" not in n:
        return "trust"
    return "other"


def slug_buyer(name, postcode):
    """Create a stable buyer ID."""
    s = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")[:80]
    if postcode:
        s += "__" + postcode.replace(" ", "").lower()
    return s


def main():
    geo = json.loads(POSTCODES.read_text(encoding="utf-8"))

    # Aggregation tables
    buyer_agg = defaultdict(lambda: {
        "name": None, "postcode": None, "type": None,
        "total_gbp_2024": 0.0, "n_contracts": 0, "supplier_keys": set(),
    })
    supplier_agg = defaultdict(lambda: {
        "name": None, "ch_number": None, "postcode": None,
        "total_gbp_2024": 0.0, "n_contracts": 0, "buyer_keys": set(),
    })
    buyer_supplier_flow = defaultdict(lambda: defaultdict(lambda: {"gbp": 0.0, "n": 0}))
    supplier_buyer_flow = defaultdict(lambda: defaultdict(lambda: {"gbp": 0.0, "n": 0}))

    rows_kept = 0
    rows_dropped = 0
    with CONTRACTS.open(encoding="utf-8") as f:
        for line in f:
            try:
                d = json.loads(line)
            except Exception:
                rows_dropped += 1
                continue

            bname = (d.get("buyer_name") or "").strip()
            bpc = normalise_pc(d.get("buyer_postcode"))
            sname = (d.get("supplier_name") or d.get("supplier_legal_name") or "").strip()
            sch = d.get("supplier_ch_number")
            spc = normalise_pc(d.get("supplier_postcode"))
            val = d.get("award_value_gbp") or d.get("tender_value_gbp") or 0
            try:
                val = float(val) if val else 0
            except Exception:
                val = 0

            if not bname or not sname:
                rows_dropped += 1
                continue

            buyer_key = slug_buyer(bname, bpc)
            supplier_key = (sch or "").strip() or slug_buyer(sname, spc)

            b = buyer_agg[buyer_key]
            b["name"] = b["name"] or bname
            b["postcode"] = b["postcode"] or bpc
            b["type"] = b["type"] or classify_buyer(bname)
            b["total_gbp_2024"] += val
            b["n_contracts"] += 1
            b["supplier_keys"].add(supplier_key)

            s = supplier_agg[supplier_key]
            s["name"] = s["name"] or sname
            s["ch_number"] = s["ch_number"] or sch
            s["postcode"] = s["postcode"] or spc
            s["total_gbp_2024"] += val
            s["n_contracts"] += 1
            s["buyer_keys"].add(buyer_key)

            flow = buyer_supplier_flow[buyer_key][supplier_key]
            flow["gbp"] += val
            flow["n"] += 1

            flow = supplier_buyer_flow[supplier_key][buyer_key]
            flow["gbp"] += val
            flow["n"] += 1

            rows_kept += 1

    print(f"Rows kept: {rows_kept:,} · dropped: {rows_dropped:,}")
    print(f"Unique buyers: {len(buyer_agg):,}")
    print(f"Unique suppliers: {len(supplier_agg):,}")

    # Finalise buyer records with geo
    buyers_out = {}
    buyers_no_geo = 0
    for k, b in buyer_agg.items():
        g = geo.get(b["postcode"]) if b["postcode"] else None
        if not g:
            buyers_no_geo += 1
        buyers_out[k] = {
            "id": k,
            "name": b["name"],
            "postcode": b["postcode"],
            "lat": g["lat"] if g else None,
            "lng": g["lng"] if g else None,
            "lad24_cd": g["lad24_cd"] if g else None,
            "lad24_nm": g["lad24_nm"] if g else None,
            "region": g["region"] if g else None,
            "country": g["country"] if g else None,
            "type": b["type"],
            "total_gbp_2024": round(b["total_gbp_2024"], 2),
            "n_contracts": b["n_contracts"],
            "n_suppliers": len(b["supplier_keys"]),
        }
    print(f"Buyers without geo: {buyers_no_geo:,}")

    # Finalise supplier records — also merge in supplier_index postcodes
    supidx_by_chnum = {}
    supidx_file = ROOT / "data/suppliers/_index.json"
    if supidx_file.exists():
        for e in json.loads(supidx_file.read_text(encoding="utf-8")):
            if e.get("company_number"):
                supidx_by_chnum[e["company_number"]] = e

    # Load per-supplier postcodes from individual JSONs
    sup_pc_by_ch = {}
    for fn in (ROOT / "data/suppliers").iterdir():
        if fn.name.startswith("_"):
            continue
        try:
            sup = json.loads(fn.read_text(encoding="utf-8"))
            ro = (sup.get("identity") or {}).get("registered_office") or {}
            pc = normalise_pc(ro.get("postal_code") if isinstance(ro, dict) else None)
            ch = (sup.get("identity") or {}).get("ch_number")
            if ch and pc:
                sup_pc_by_ch[ch] = pc
        except Exception:
            pass

    suppliers_out = {}
    suppliers_no_geo = 0
    for k, s in supplier_agg.items():
        pc = s["postcode"]
        # If supplier has ch_number and we have postcode from supplier JSON, use that
        if s["ch_number"] and s["ch_number"] in sup_pc_by_ch:
            pc = sup_pc_by_ch[s["ch_number"]]
        g = geo.get(pc) if pc else None
        if not g:
            suppliers_no_geo += 1
        suppliers_out[k] = {
            "id": k,
            "name": s["name"],
            "ch_number": s["ch_number"],
            "postcode": pc,
            "lat": g["lat"] if g else None,
            "lng": g["lng"] if g else None,
            "lad24_cd": g["lad24_cd"] if g else None,
            "lad24_nm": g["lad24_nm"] if g else None,
            "region": g["region"] if g else None,
            "country": g["country"] if g else None,
            "total_gbp_2024": round(s["total_gbp_2024"], 2),
            "n_contracts": s["n_contracts"],
            "n_buyers": len(s["buyer_keys"]),
            "in_curated_index": bool(s["ch_number"] and s["ch_number"] in supidx_by_chnum),
        }
    print(f"Suppliers without geo: {suppliers_no_geo:,}")

    # Top-50 flows per buyer/supplier
    buyer_to_suppliers_top = {}
    for bk, flows in buyer_supplier_flow.items():
        top = sorted(flows.items(), key=lambda x: -x[1]["gbp"])[:50]
        buyer_to_suppliers_top[bk] = [
            {"supplier_id": sk, "gbp": round(v["gbp"], 2), "n_contracts": v["n"]}
            for sk, v in top
        ]

    supplier_to_buyers_top = {}
    for sk, flows in supplier_buyer_flow.items():
        top = sorted(flows.items(), key=lambda x: -x[1]["gbp"])[:50]
        supplier_to_buyers_top[sk] = [
            {"buyer_id": bk, "gbp": round(v["gbp"], 2), "n_contracts": v["n"]}
            for bk, v in top
        ]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "buyers.json").write_text(json.dumps(buyers_out, ensure_ascii=False), encoding="utf-8")
    (OUT_DIR / "suppliers.json").write_text(json.dumps(suppliers_out, ensure_ascii=False), encoding="utf-8")
    (OUT_DIR / "buyer_to_suppliers.json").write_text(json.dumps(buyer_to_suppliers_top, ensure_ascii=False), encoding="utf-8")
    (OUT_DIR / "supplier_to_buyers.json").write_text(json.dumps(supplier_to_buyers_top, ensure_ascii=False), encoding="utf-8")

    # Summary
    stats = {
        "rows_kept": rows_kept,
        "rows_dropped": rows_dropped,
        "unique_buyers": len(buyers_out),
        "unique_suppliers": len(suppliers_out),
        "buyers_with_geo": len(buyers_out) - buyers_no_geo,
        "suppliers_with_geo": len(suppliers_out) - suppliers_no_geo,
        "buyers_without_geo": buyers_no_geo,
        "suppliers_without_geo": suppliers_no_geo,
    }
    (OUT_DIR / "_aggregate_stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")

    # File sizes
    import os
    print(f"\nOutput file sizes:")
    for fn in ["buyers.json", "suppliers.json", "buyer_to_suppliers.json", "supplier_to_buyers.json"]:
        size = os.path.getsize(OUT_DIR / fn)
        print(f"  {fn}: {size/1024:.1f}KB")


if __name__ == "__main__":
    main()
