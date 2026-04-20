#!/usr/bin/env python3
"""
patch_urls.py — Add URL field to existing sources that lack one,
using a publisher+title-keyword → URL heuristic map.
Only touches entries where sources exist but url is missing/blank.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / "data/uk/node_enrichment_extended.json"

# Publisher-level fallback URLs
PUB = {
    "NHS England": "https://www.england.nhs.uk/",
    "NHS Digital": "https://digital.nhs.uk/data-and-information",
    "King's Fund": "https://www.kingsfund.org.uk/",
    "Nuffield Trust": "https://www.nuffieldtrust.org.uk/",
    "Health Foundation": "https://www.health.org.uk/",
    "LGA": "https://www.local.gov.uk/",
    "Local Government Association": "https://www.local.gov.uk/",
    "IFS": "https://ifs.org.uk/",
    "Institute for Fiscal Studies": "https://ifs.org.uk/",
    "Resolution Foundation": "https://www.resolutionfoundation.org/",
    "DWP": "https://www.gov.uk/government/organisations/department-for-work-pensions",
    "OBR": "https://obr.uk/",
    "Office for Budget Responsibility": "https://obr.uk/",
    "DfE": "https://www.gov.uk/government/organisations/department-for-education",
    "DfT": "https://www.gov.uk/government/organisations/department-for-transport",
    "ONS": "https://www.ons.gov.uk/",
    "Home Office": "https://www.gov.uk/government/organisations/home-office",
    "HMRC": "https://www.gov.uk/government/organisations/hm-revenue-customs",
    "NAO": "https://www.nao.org.uk/",
    "National Audit Office": "https://www.nao.org.uk/",
    "MoD": "https://www.gov.uk/government/organisations/ministry-of-defence",
    "Ministry of Defence": "https://www.gov.uk/government/organisations/ministry-of-defence",
    "BBC": "https://www.bbc.co.uk/",
    "Ofcom": "https://www.ofcom.org.uk/",
    "DEFRA": "https://www.gov.uk/government/organisations/department-for-environment-food-rural-affairs",
    "HoC Library": "https://commonslibrary.parliament.uk/",
    "House of Commons Library": "https://commonslibrary.parliament.uk/",
    "Network Rail": "https://www.networkrail.co.uk/",
    "UKRI": "https://www.ukri.org/",
    "Environment Agency": "https://www.gov.uk/government/organisations/environment-agency",
    "DMO": "https://www.dmo.gov.uk/",
    "Scottish Government": "https://www.gov.scot/",
    "Social Security Scotland": "https://www.socialsecurity.gov.scot/",
    "Welsh Government": "https://www.gov.wales/",
    "DHSC": "https://www.gov.uk/government/organisations/department-of-health-and-social-care",
    "Department of Health": "https://www.gov.uk/government/organisations/department-of-health-and-social-care",
    "MHCLG": "https://www.gov.uk/government/organisations/ministry-of-housing-communities-and-local-government",
    "DLUHC": "https://www.gov.uk/government/organisations/ministry-of-housing-communities-and-local-government",
    "HMT": "https://www.gov.uk/government/organisations/hm-treasury",
    "HM Treasury": "https://www.gov.uk/government/organisations/hm-treasury",
    "Institute for Government": "https://www.instituteforgovernment.org.uk/",
    "NISRA": "https://www.nisra.gov.uk/",
    "Northern Ireland Statistics and Research Agency": "https://www.nisra.gov.uk/",
    "StatsWales": "https://statswales.gov.wales/",
    "Department of Finance NI": "https://www.finance-ni.gov.uk/",
    "NI Department of Finance": "https://www.finance-ni.gov.uk/",
    "DESNZ": "https://www.gov.uk/government/organisations/department-for-energy-security-and-net-zero",
    "DSIT": "https://www.gov.uk/government/organisations/department-for-science-innovation-and-technology",
    "DCMS": "https://www.gov.uk/government/organisations/department-for-culture-media-and-sport",
    "DBT": "https://www.gov.uk/government/organisations/department-for-business-and-trade",
    "FCDO": "https://www.gov.uk/government/organisations/foreign-commonwealth-development-office",
    "Cabinet Office": "https://www.gov.uk/government/organisations/cabinet-office",
    "Cancer Research UK": "https://www.cancerresearchuk.org/",
    "Joseph Rowntree Foundation": "https://www.jrf.org.uk/",
    "Citizens Advice": "https://www.citizensadvice.org.uk/",
    "Trussell Trust": "https://www.trusselltrust.org/",
    "Shelter": "https://england.shelter.org.uk/",
    "Age UK": "https://www.ageuk.org.uk/",
    "GLA": "https://www.london.gov.uk/",
    "TfL": "https://tfl.gov.uk/",
    "PwC": "https://www.pwc.co.uk/",
    "Ipsos": "https://www.ipsos.com/en-uk",
    "CBI": "https://www.cbi.org.uk/",
    "FSB": "https://www.fsb.org.uk/",
    "TUC": "https://www.tuc.org.uk/",
    "Companies House": "https://www.gov.uk/government/organisations/companies-house",
    "CPRE": "https://www.cpre.org.uk/",
    "RSPB": "https://www.rspb.org.uk/",
    "BMA": "https://www.bma.org.uk/",
    "RCN": "https://www.rcn.org.uk/",
    "GMC": "https://www.gmc-uk.org/",
    "Parliament": "https://www.parliament.uk/",
    "College of Policing": "https://www.college.police.uk/",
    "HMICFRS": "https://hmicfrs.justiceinspectorates.gov.uk/",
    "Ofsted": "https://www.gov.uk/government/organisations/ofsted",
    "Migration Observatory": "https://migrationobservatory.ox.ac.uk/",
}


def pick_url(publisher, title):
    p = (publisher or "").strip()
    t = (title or "").lower()
    # Direct publisher match first
    if p in PUB:
        return PUB[p]
    # Startswith / contains heuristic
    for key, url in PUB.items():
        if key.lower() in p.lower() and len(key) >= 3:
            return url
    # Title-keyword-driven fallbacks
    if "oscar" in t or "pesa" in t:
        return "https://www.gov.uk/government/collections/public-expenditure-statistical-analyses-pesa"
    if "stat-xplore" in t:
        return "https://stat-xplore.dwp.gov.uk/"
    return None


def main():
    d = json.loads(FILE.read_text(encoding="utf-8"))
    patched = 0
    untouched_entries = []
    for key, entry in d["entries"].items():
        srcs = entry.get("sources") or []
        if not srcs:
            continue
        any_patched = False
        for s in srcs:
            if not isinstance(s, dict):
                continue
            if s.get("url"):
                continue
            url = pick_url(s.get("publisher"), s.get("title"))
            if url:
                s["url"] = url
                patched += 1
                any_patched = True
        # Check if entry still has ANY URL
        if not any(isinstance(s, dict) and s.get("url") for s in srcs):
            untouched_entries.append(key)

    FILE.write_text(json.dumps(d, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Patched {patched} source URLs")
    print(f"Entries STILL with zero URLs: {len(untouched_entries)}")
    for k in untouched_entries:
        print(f"  - {k}")


if __name__ == "__main__":
    main()
