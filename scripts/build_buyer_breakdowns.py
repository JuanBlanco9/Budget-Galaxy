#!/usr/bin/env python3
"""Build per-department breakdowns to honestly explain Recipients totals.

Procurement data shows DWP as a "buyer" of £349B. Reality: most of that £
flows through to citizens (Universal Credit, State Pension, PIP, Housing
Benefit) — NOT to 31 commercial suppliers. Conflating the two on
budgetgalaxy.com is misleading.

This script reads data/uk/uk_budget_tree_2024.json, classifies each L2
sub-line of each major department as either 'transfer' (to citizens / NGOs
/ public bodies) or 'procurement' (commercial supplier flows), and writes
a JSON the frontend can use to:
  1. Show a "what this £ really is" breakdown panel for big buyers
  2. Flag buyers whose totals are dominated by transfers

Output: data/uk/buyer_breakdowns_2024.json

Schema:
{
  "department-for-work-and-pensions": {
    "name": "Department for Work and Pensions",
    "slug": "department-for-work-and-pensions",
    "total_gbp_2024": 297400000000,
    "transfer_total":   292500000000,
    "procurement_total":  4900000000,
    "transfer_pct": 98,
    "is_transfer_dominant": true,
    "top_lines": [
      {"name": "10.2 Old age; of which: pensions", "value": 143247160000, "kind": "transfer"},
      ...
    ]
  },
  ...
}
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.setrecursionlimit(50000)

ROOT = Path(__file__).resolve().parent.parent
TREE = ROOT / "data/uk/uk_budget_tree_2024.json"
OUT = ROOT / "data/uk/buyer_breakdowns_2024.json"

# COFOG Social protection (10.x) — transfers to individuals
COFOG_TRANSFER_PREFIXES = ("10.",)
# COFOG Education (09.x) + Health (07.x) — typically grants to public bodies
# (academies, universities, NHS trusts) rather than commercial procurement
COFOG_GRANT_PREFIXES = ("09.", "9.", "07.", "7.")

# Names for transfer-to-individual (citizens get the money)
TRANSFER_PATTERNS = [
    r"\bpension(s)?\b",
    r"\bbenefit(s)?\b",
    r"\bcredit(s)?\b",
    r"\ballowance(s)?\b",
    r"\bincome support\b",
    r"\btax credits\b",
    r"\bchild benefit\b",
    r"\bfamily benefit",
    r"\bdisability\b",
    r"\bsickness\b",
    r"\bunemployment\b",
    r"\bhousing benefit\b",
    r"\bwinter fuel\b",
    r"\bcost of living\b",
    r"\bold age\b",
    r"\bsuperannuation\b",
    r"\bcompensation scheme(s)?\b",
]
TRANSFER_RE = re.compile("|".join(TRANSFER_PATTERNS), re.IGNORECASE)

# Names for grant-to-public-body (NHS trusts, schools, universities, councils, devolved)
GRANT_PATTERNS = [
    r"\bnhs\b",
    r"\btrust(s)?\b",
    r"\bcommissioning\b",
    r"\bcommissioning board\b",
    r"\bicb\b",
    r"\bacademies\b",
    r"\bacademy\b",
    r"\bschool(s)?\b",
    r"\buniversity\b",
    r"\buniversities\b",
    r"\btertiary education\b",
    r"\bprimary education\b",
    r"\bsecondary education\b",
    r"\beducation not definable\b",
    r"\bblock grant\b",
    r"\brevenue support grant\b",
    r"\bequalisation\b",
    r"\bsubvention\b",
    r"\blocal government\b",
    r"\blocal authorit",
    r"\bcouncil(s)?\b",
    r"\bborough\b",
    r"\bcounty council",
    r"\bdistrict council",
    r"\bunitary\b",
    r"\bmetropolitan\b",
    r"\bshire\b",
    r"\bdevolved\b",
    r"\bscottish\b",
    r"\bwelsh\b",
    r"\bnorthern ireland\b",
    r"\bgrant(s)? to\b",
    r"\bsubsidy\b",
    r"\bsubsidies\b",
    r"\baid\b",
    r"\bsupport to\b",
]
GRANT_RE = re.compile("|".join(GRANT_PATTERNS), re.IGNORECASE)

# Department-level signals where the whole entity is dominated by transfers
TRANSFER_DOMINANT_DEPTS = {
    "department for work and pensions",
    "scotland office and office of the advocate general",
    "wales office",
    "northern ireland office",
    "cabinet office: civil superannuation",
    "teachers' pension scheme (england and wales)",
    "armed forces pension and compensation schemes",
    "royal mail statutory pension scheme",
    "ministry of justice: judicial pensions scheme",
    "united kingdom atomic energy authority pension schemes",
    "foreign, commonwealth and development office: overseas superannuation",
}


def classify_line(name):
    """Returns 'transfer' (citizens), 'grant' (public bodies/NGOs), or 'procurement' (commercial suppliers)."""
    if not name:
        return "procurement"
    nm = name.strip()
    # COFOG code prefixes
    for p in COFOG_TRANSFER_PREFIXES:
        if nm.startswith(p):
            return "transfer"
    for p in COFOG_GRANT_PREFIXES:
        if nm.startswith(p):
            return "grant"
    # Name patterns — transfer first (more specific), then grant
    if TRANSFER_RE.search(nm):
        return "transfer"
    if GRANT_RE.search(nm):
        return "grant"
    return "procurement"


def slugify(name):
    s = re.sub(r"[^a-z0-9]+", "-", (name or "").lower()).strip("-")
    return s


def main():
    tree = json.loads(TREE.read_text(encoding="utf-8"))
    out = {}
    for dept in (tree.get("children") or []):
        name = dept.get("name") or ""
        total = dept.get("value") or 0
        if total < 1e8:  # skip tiny entities
            continue
        children = dept.get("children") or []
        # Sort by £
        sub = sorted(
            ((c.get("name") or "", c.get("value") or 0) for c in children),
            key=lambda x: -x[1],
        )
        # Sum across ALL children (not just top-12) for honest bucket totals
        transfer_total = 0
        grant_total = 0
        procurement_total = 0
        for sn, sv in sub:
            kind = classify_line(sn)
            if kind == "transfer":
                transfer_total += sv
            elif kind == "grant":
                grant_total += sv
            else:
                procurement_total += sv
        # Top-12 used only for the displayable list
        top = []
        for sn, sv in sub[:12]:
            top.append({"name": sn, "value": sv, "kind": classify_line(sn)})
        # Dept-level override (whole-entity transfer signals)
        if name.lower() in TRANSFER_DOMINANT_DEPTS:
            transfer_total = sum(sv for _, sv in sub)
            grant_total = 0
            procurement_total = 0
        children_sum = transfer_total + grant_total + procurement_total
        # Use children_sum (not dept.value) for percentages — some dept nodes
        # carry a value that's not exactly the sum of children (parent-only
        # admin vs leaf detail). We classify based on what we can see.
        denom = children_sum if children_sum > 0 else total
        pct_transfer = round(transfer_total / denom * 100) if denom > 0 else 0
        pct_grant = round(grant_total / denom * 100) if denom > 0 else 0
        pct_procurement = round(procurement_total / denom * 100) if denom > 0 else 0

        # Display name in title-case (tree has many uppercase)
        disp = name
        if disp.isupper():
            disp = " ".join(w.capitalize() if len(w) > 3 or i == 0 else w.lower()
                            for i, w in enumerate(disp.split()))
            # Tidy known acronyms
            for acr in ("HMRC", "DWP", "MOD", "DfE", "DCMS", "DBT", "DESNZ", "DSIT",
                       "FCDO", "HMT", "MOJ", "DEFRA", "DHSC", "MHCLG"):
                disp = re.sub(rf"\b{acr.lower()}\b", acr, disp, flags=re.IGNORECASE)

        slug = slugify(name)
        out[slug] = {
            "name": disp,
            "slug": slug,
            "total_gbp_2024": total,
            "transfer_total": transfer_total,
            "grant_total": grant_total,
            "procurement_total": procurement_total,
            "transfer_pct": pct_transfer,
            "grant_pct": pct_grant,
            "procurement_pct": pct_procurement,
            "is_transfer_dominant": pct_transfer >= 60,
            "is_grant_dominant": pct_grant >= 60,
            "is_low_procurement": pct_procurement < 20,
            "top_lines": top,
        }

    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUT} · {len(out)} departments")
    # Top by spend, with composition
    rows = sorted(out.values(), key=lambda r: -r["total_gbp_2024"])[:20]
    print()
    print(f"{'TOTAL':>9}  {'TRANS':>5}  {'GRANT':>5}  {'PROC':>5}  NAME")
    for r in rows:
        flags = []
        if r["is_transfer_dominant"]: flags.append("TRANS")
        if r["is_grant_dominant"]: flags.append("GRANT")
        if r["is_low_procurement"]: flags.append("LOW-PROC")
        f = " · ".join(flags)
        print(f"£{r['total_gbp_2024']/1e9:>7.1f}B  {r['transfer_pct']:>4}%  {r['grant_pct']:>4}%  {r['procurement_pct']:>4}%  {r['name']:<55}  {f}")


if __name__ == "__main__":
    main()
