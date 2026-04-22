#!/usr/bin/env python3
"""Bulk enrichment phase 1: build profile skeletons from Companies House BCD.

For every unique supplier in data/map/suppliers.json that has a ch_number
(or can be resolved by name), read the BCD zip once more and extract the
full record (name, address, SIC, accounts category, previous names, etc.).

Output:
  data/suppliers_v2/{CH_NUMBER}.json  — one skeleton profile per supplier
  data/suppliers_v2/_index.json       — compact index: ch_number → summary
  data/suppliers_v2/_coverage.json    — stats on coverage, misses, sources

No CH API calls — pure local BCD parsing. ~30 min for 40k suppliers.
"""
import csv
import json
import io
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BCD_ZIP = ROOT / "data/map/ch_bcd/BasicCompanyData-2026-04.zip"
SUPPLIERS_MAP = ROOT / "data/map/suppliers.json"
RESOLVED = ROOT / "data/map/supplier_postcodes_resolved.json"
OUT_DIR = ROOT / "data/suppliers_v2"
OUT_INDEX = OUT_DIR / "_index.json"
OUT_COVERAGE = OUT_DIR / "_coverage.json"

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
    n = re.sub(r"[.,;:'\"`]", "", n)
    n = re.sub(r"\s+LIMITED\s*$", " LTD", n)
    n = re.sub(r"\s+", " ", n).strip()
    key = re.sub(r"[^A-Za-z0-9]", "", n).lower()
    return key if key else None


def build_ch_targets():
    """Return (ch_targets, name_targets) — the sets we need to extract from BCD."""
    suppliers = json.loads(SUPPLIERS_MAP.read_text(encoding="utf-8"))
    ch_targets = set()
    name_targets = {}  # normalised_name → supplier_id for backfill
    for sid, s in suppliers.items():
        if s.get("ch_number"):
            ch_targets.add(s["ch_number"].strip())
        elif s.get("name"):
            nk = normalise_name(s["name"])
            if nk:
                name_targets[nk] = sid
    return ch_targets, name_targets, suppliers


def extract_bcd_rows(ch_targets, name_targets):
    """Stream BCD zip → return dict ch_number → full row dict."""
    rows_by_ch = {}
    rows_by_name_key = {}
    stats = {"rows": 0, "ch_hits": 0, "name_hits": 0}
    with zipfile.ZipFile(BCD_ZIP) as z:
        inner = [n for n in z.namelist() if n.endswith(".csv")][0]
        with z.open(inner) as fh:
            reader = csv.DictReader(io.TextIOWrapper(fh, encoding="utf-8-sig", errors="replace"))
            reader.fieldnames = [f.strip() if f else f for f in (reader.fieldnames or [])]
            for row in reader:
                row = {k.strip() if k else k: v for k, v in row.items()}
                stats["rows"] += 1
                ch = (row.get("CompanyNumber") or "").strip()
                if not ch:
                    continue
                if ch in ch_targets:
                    rows_by_ch[ch] = row
                    stats["ch_hits"] += 1
                    continue
                # Name fallback
                nk = normalise_name(row.get("CompanyName"))
                if nk and nk in name_targets:
                    rows_by_name_key.setdefault(nk, row)
                    stats["name_hits"] += 1
                if stats["rows"] % 500_000 == 0:
                    print(f"  {stats['rows']:,} BCD rows · {stats['ch_hits']:,} ch-hits · {stats['name_hits']:,} name-hits")
    return rows_by_ch, rows_by_name_key, stats


def bcd_to_skeleton(row, supplier_record):
    """Convert a BCD row + our supplier aggregate into a skeleton profile."""
    ch = (row.get("CompanyNumber") or "").strip()
    pc = normalise_pc(row.get("RegAddress.PostCode"))
    sic_codes = []
    sic_labels = []
    for i in range(1, 5):
        val = (row.get(f"SICCode.SicText_{i}") or "").strip()
        if val and val != "None Supplied":
            # Format: "64929 - Other credit granting"
            if " - " in val:
                code, label = val.split(" - ", 1)
                sic_codes.append(code.strip())
                sic_labels.append(label.strip())
            else:
                sic_codes.append(val)
                sic_labels.append("")
    prev_names = []
    for i in range(1, 11):
        pn = (row.get(f"PreviousName_{i}.CompanyName") or "").strip()
        pd = (row.get(f"PreviousName_{i}.CONDATE") or "").strip()
        if pn:
            prev_names.append({"name": pn, "condate": pd or None})
    incorp = (row.get("IncorporationDate") or "").strip() or None
    diss = (row.get("DissolutionDate") or "").strip() or None

    # Translate CompanyCategory → our type vocabulary
    cat = (row.get("CompanyCategory") or "").strip()
    if "Limited" in cat or "LLP" in cat or "plc" in cat.lower():
        type_code = "ltd" if "Limited" in cat else ("llp" if "LLP" in cat else "plc")
    else:
        type_code = cat.lower().replace(" ", "_") or "unknown"

    skel = {
        "schema_version": "v2",
        "company_number": ch,
        "display_name": (row.get("CompanyName") or "").title(),
        "official_name": row.get("CompanyName") or "",
        "status": (row.get("CompanyStatus") or "").lower().replace(" ", "_") or None,
        "type": type_code,
        "category_raw": cat,
        "jurisdiction": (row.get("CountryOfOrigin") or "").lower().replace(" ", "-") or None,
        "incorporated": incorp,
        "dissolved": diss,
        "age_years": None,
        "sic_codes": sic_codes,
        "sic_labels": sic_labels,
        "previous_names": prev_names,
        "registered_office": {
            "address_line_1": row.get("RegAddress.AddressLine1") or "",
            "address_line_2": row.get("RegAddress.AddressLine2") or "",
            "post_town": row.get("RegAddress.PostTown") or "",
            "county": row.get("RegAddress.County") or "",
            "country": row.get("RegAddress.Country") or "",
            "postal_code": pc,
        },
        "accounts": {
            "category": row.get("Accounts.AccountCategory") or None,
            "last_made_up": row.get("Accounts.LastMadeUpDate") or None,
            "next_due": row.get("Accounts.NextDueDate") or None,
            "ref_day": row.get("Accounts.AccountRefDay") or None,
            "ref_month": row.get("Accounts.AccountRefMonth") or None,
        },
        "mortgages": {
            "num_charges": int(row.get("Mortgages.NumMortCharges") or 0),
            "num_outstanding": int(row.get("Mortgages.NumMortOutstanding") or 0),
            "num_part_satisfied": int(row.get("Mortgages.NumMortPartSatisfied") or 0),
            "num_satisfied": int(row.get("Mortgages.NumMortSatisfied") or 0),
        },
        "spend_profile": {
            "total_gbp_2024": supplier_record.get("total_gbp_2024", 0),
            "n_contracts": supplier_record.get("n_contracts", 0),
            "n_buyers": supplier_record.get("n_buyers", 0),
        },
        "geo": {
            "lat": supplier_record.get("lat"),
            "lng": supplier_record.get("lng"),
            "lad24_cd": supplier_record.get("lad24_cd"),
            "lad24_nm": supplier_record.get("lad24_nm"),
            "region": supplier_record.get("region"),
        },
        "sources": [
            {"publisher": "Companies House", "title": "Basic Company Data 2026-04", "url": f"https://find-and-update.company-information.service.gov.uk/company/{ch}"},
        ],
        "enrichment_stages": {
            "bcd_skeleton": True,
            "ch_api_profile": False,
            "ch_api_officers": False,
            "ch_api_pscs": False,
            "ch_api_accounts_pdf": False,
        },
    }
    # Normalise incorporated date (BCD = DD/MM/YYYY → ISO YYYY-MM-DD)
    if incorp and "/" in incorp:
        parts = incorp.split("/")
        if len(parts) == 3 and len(parts[2]) == 4:
            incorp = f"{parts[2]}-{parts[1].zfill(2)}-{parts[0].zfill(2)}"
            skel["incorporated"] = incorp
    # Compute age
    if incorp:
        try:
            yr = int(incorp[:4])
            skel["age_years"] = 2026 - yr
        except Exception:
            pass
    return skel


def main():
    print("Phase 1 · bulk supplier enrichment from Companies House BCD")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    ch_targets, name_targets, suppliers_map = build_ch_targets()
    print(f"Unique ch_numbers to match: {len(ch_targets):,}")
    print(f"Name-based fallback targets: {len(name_targets):,}")

    print("\nStreaming BCD zip...")
    rows_by_ch, rows_by_name_key, stats = extract_bcd_rows(ch_targets, name_targets)
    print(f"\nBCD rows scanned: {stats['rows']:,}")
    print(f"CH-number matches: {stats['ch_hits']:,}")
    print(f"Name-based matches: {stats['name_hits']:,}")

    # Load also the earlier-resolved postcodes mapping
    resolved = {}
    if RESOLVED.exists():
        resolved = json.loads(RESOLVED.read_text(encoding="utf-8"))

    # Now write skeleton files
    written = 0
    missed = []
    index = {}
    for sid, supplier in suppliers_map.items():
        ch = supplier.get("ch_number")
        row = None
        if ch and ch in rows_by_ch:
            row = rows_by_ch[ch]
        if not row:
            # Try name match
            nk = normalise_name(supplier.get("name"))
            if nk and nk in rows_by_name_key:
                row = rows_by_name_key[nk]
        if not row:
            missed.append(sid)
            continue

        skel = bcd_to_skeleton(row, supplier)
        ch_final = skel["company_number"] or sid
        out_path = OUT_DIR / f"{ch_final}.json"
        out_path.write_text(json.dumps(skel, ensure_ascii=False, indent=2), encoding="utf-8")
        index[ch_final] = {
            "company_number": ch_final,
            "display_name": skel["display_name"],
            "status": skel["status"],
            "total_gbp_2024": skel["spend_profile"]["total_gbp_2024"],
            "n_contracts": skel["spend_profile"]["n_contracts"],
            "n_buyers": skel["spend_profile"]["n_buyers"],
            "sic_codes": skel["sic_codes"][:1],
            "postcode": skel["registered_office"]["postal_code"],
            "lad24_nm": skel["geo"]["lad24_nm"],
            "incorporated": skel["incorporated"],
            "age_years": skel["age_years"],
            "enrichment_stages": skel["enrichment_stages"],
        }
        written += 1
        if written % 2000 == 0:
            print(f"  written: {written:,}")

    print(f"\nTotal skeleton files: {written:,}")
    print(f"Missed (no BCD match): {len(missed):,}")

    OUT_INDEX.write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
    OUT_COVERAGE.write_text(json.dumps({
        "total_suppliers": len(suppliers_map),
        "skeletons_written": written,
        "missed": len(missed),
        "missed_sample": missed[:100],
        "bcd_snapshot": "2026-04-01",
    }, indent=2), encoding="utf-8")

    print(f"\nWrote {OUT_INDEX}")
    print(f"Wrote {OUT_COVERAGE}")


if __name__ == "__main__":
    main()
