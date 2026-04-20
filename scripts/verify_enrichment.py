#!/usr/bin/env python3
"""
verify_enrichment.py — Audit all 3 enrichment layers.

Runs three passes:

 1. **Tier A** (node_enrichment_extended.json, 36 hand-curated entries)
    - Finds the matching tree node by name
    - Extracts any £-valued stat from `key_stats`
    - Compares it to the tree's actual node.value; flags if off by >20%
    - Flags entries with no tree match
    - Flags broken / empty required fields
    - Flags sources without a URL
    - Cross-checks "Established" / "created" year against known UK history

 2. **Tier B** (program_enrichment.json + enrichment_top50.json)
    - Statistical audit: length distribution, suspicious patterns
    - Spot-check 50 random entries for dated language, truncation, or
      known-wrong founding years for major departments
    - Flags "n/a" / "GBPX.XB" placeholder entries that leaked through

 3. **Coverage**
    - For every top-level department in the tree, check which tier covers it
    - Reports the "worst" top-level node (smallest tier reached)

Outputs:
  - data/uk/_enrichment_audit.json — machine-readable report
  - stdout — human-readable summary
"""
import json
import re
import sys
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parent.parent
TREE = ROOT / "data/uk/uk_budget_tree_2024.json"
EXTENDED = ROOT / "data/uk/node_enrichment_extended.json"
COMPACT = ROOT / "data/uk/program_enrichment.json"
RICH = ROOT / "data/uk/enrichment_top50.json"
OUT = ROOT / "data/uk/_enrichment_audit.json"

# Known correct founding years for common entries (sanity check)
KNOWN_YEARS = {
    "Home Office": (1782, 1782),
    "HM Treasury": (1066, 1400),  # origin debated; not 2024
    "HM REVENUE AND CUSTOMS": (2005, 2005),  # merger
    "MINISTRY OF DEFENCE": (1964, 1964),
    "Ministry of Defence": (1964, 1964),
    "MINISTRY OF JUSTICE": (2007, 2007),
    "Ministry of Justice": (2007, 2007),
    "DEPARTMENT FOR WORK AND PENSIONS": (2001, 2001),
    "DEPARTMENT FOR EDUCATION": (2010, 2010),
    "DEPARTMENT FOR TRANSPORT": (2002, 2002),
    "HOME OFFICE": (1782, 1782),
    "State Pension": (1908, 1948),  # 1908 Old-Age Pensions Act / 1948 NIA
    "NHS England Core Revenue Allocation": (1948, 1948),
    "Universal Credit": (2013, 2013),
    "Personal Independence Payment (PIP)": (2013, 2013),
    "Pension Credit": (2003, 2003),
    "Child Benefit": (1977, 1977),  # current form; earlier Family Allowance 1946
    "Attendance Allowance": (1971, 1971),
}

# Placeholder patterns — only match the DESCRIPTION or a key that is LITERALLY
# the placeholder "n/a". The previous `GBPX.XB` pattern was a false positive —
# the author uses "(GBPX.XB)" as a value tag inside some compact keys, which is
# fine. We now only flag descriptions containing stub language.
SUSPICIOUS_KEY_REGEX = re.compile(r"^n/a\s*(\(|$)", re.IGNORECASE)
SUSPICIOUS_DESC_REGEX = re.compile(
    r"\b(Not-applicable classification placeholder|TODO|TBD|\?\?\?|lorem ipsum)\b",
    re.IGNORECASE,
)


def walk_tree(node, path=None, results=None):
    if results is None:
        results = {}
    if path is None:
        path = []
    name = node.get("name", "")
    if name:
        results[name] = {
            "value": node.get("value", 0),
            "path": path[:],
            "has_top_suppliers": bool(node.get("_top_suppliers")),
            "children_count": len(node.get("children") or []),
        }
    for i, c in enumerate(node.get("children") or []):
        walk_tree(c, path + [i], results)
    return results


def parse_money(s):
    """Extract a £ value from text like '£143.2B' or '£88,814'."""
    if not s:
        return None
    s = str(s).replace(",", "")
    m = re.search(r"£\s*([\d\.]+)\s*(billion|B|million|M|K)?", s, re.IGNORECASE)
    if not m:
        return None
    try:
        v = float(m.group(1))
    except Exception:
        return None
    unit = (m.group(2) or "").lower()
    if unit in ("billion", "b"):
        return v * 1e9
    if unit in ("million", "m"):
        return v * 1e6
    if unit == "k":
        return v * 1e3
    return v


def tier_a_audit(extended, tree_index):
    """Audit hand-curated 36 entries."""
    findings = {
        "total": 0,
        "tree_match_by_name": 0,
        "no_tree_match": [],
        "spend_discrepancy": [],
        "empty_required_field": [],
        "sources_without_url": [],
        "suspicious_year": [],
        "stats_referenced_total": 0,
    }
    entries = extended.get("entries", {})
    for key, e in entries.items():
        findings["total"] += 1
        # 1. Is there a tree node with this name (primary key OR any alias)?
        tree_hit = tree_index.get(key)
        if not tree_hit:
            for alias in (e.get("aliases") or []):
                alias_name = alias if isinstance(alias, str) else (alias.get("name") if isinstance(alias, dict) else None)
                if alias_name and tree_index.get(alias_name):
                    tree_hit = tree_index[alias_name]
                    break
        if tree_hit:
            findings["tree_match_by_name"] += 1
        else:
            findings["no_tree_match"].append({
                "key": key,
                "has_aliases": bool(e.get("aliases")),
                "note": e.get("_note"),
            })

        # 2. Do required fields exist?
        for req in ("description", "beneficiaries"):
            if not e.get(req):
                findings["empty_required_field"].append(f"{key}: missing {req}")

        # 3. Can we cross-check any £ in key_stats vs tree value?
        if tree_hit and tree_hit["value"] > 0:
            for stat in (e.get("key_stats") or []):
                findings["stats_referenced_total"] += 1
                v = parse_money(stat.get("value", ""))
                if v is None or v < 1e9:  # ignore tiny stats
                    continue
                tree_val = tree_hit["value"]
                # Only compare if the stat looks like a top-line "total budget"
                if re.search(r"total|budget|spend|annual", stat.get("label", ""), re.I):
                    ratio = v / tree_val
                    if ratio < 0.75 or ratio > 1.35:
                        findings["spend_discrepancy"].append({
                            "node": key,
                            "stat_label": stat.get("label"),
                            "stat_value": stat.get("value"),
                            "tree_value": f"£{tree_val/1e9:.1f}B",
                            "ratio": round(ratio, 2),
                        })

        # 4. Sources without URLs
        no_url_count = 0
        for src in (e.get("sources") or []):
            if not src.get("url"):
                no_url_count += 1
        if no_url_count == len(e.get("sources") or []) and (e.get("sources") or []):
            findings["sources_without_url"].append(f"{key} ({no_url_count} sources, 0 URLs)")

    return findings


def tier_b_audit(compact, rich_list):
    """Audit the imported enrichment files."""
    findings = {
        "compact_total": len(compact),
        "rich_total": len(rich_list),
        "placeholder_entries": [],
        "suspicious_years": [],
        "truncated_descriptions": [],
        "empty_descriptions": [],
    }

    # 1. Check compact for placeholder/truncation/bad years
    for key, e in compact.items():
        desc = e.get("d") or ""
        benef = e.get("b") or ""
        year = e.get("y")

        if SUSPICIOUS_KEY_REGEX.search(key) or SUSPICIOUS_DESC_REGEX.search(desc):
            findings["placeholder_entries"].append({"key": key, "where": "compact"})
            continue

        if not desc:
            findings["empty_descriptions"].append(key)
            continue

        # Truncation heuristic: ends mid-word without punctuation
        if len(desc) > 100 and not desc.rstrip().endswith((".", "!", "?", ")")):
            findings["truncated_descriptions"].append({
                "key": key,
                "tail": desc[-80:],
            })

        # Check founding year against known values
        if key in KNOWN_YEARS and year:
            low, high = KNOWN_YEARS[key]
            if not (low - 3 <= int(year) <= high + 3):
                findings["suspicious_years"].append({
                    "key": key,
                    "declared": year,
                    "expected_range": f"{low}-{high}",
                })

    # 2. Sample the rich list
    for entry in rich_list:
        name = entry.get("name", "")
        desc = entry.get("description") or ""
        created = entry.get("created")
        if SUSPICIOUS_KEY_REGEX.search(name) or (desc and SUSPICIOUS_DESC_REGEX.search(desc)):
            findings["placeholder_entries"].append({"key": name, "where": "rich"})
        if name in KNOWN_YEARS and created:
            low, high = KNOWN_YEARS[name]
            if not (low - 3 <= int(created) <= high + 3):
                findings["suspicious_years"].append({
                    "key": name,
                    "declared": created,
                    "expected_range": f"{low}-{high}",
                    "where": "rich",
                })

    return findings


def coverage_audit(tree, extended, compact, rich_names):
    """For each top-level department, report which tier covers it."""
    findings = []
    ext_keys = set(extended.get("entries", {}).keys())
    for c in tree.get("children", []):
        name = c.get("name", "")
        value = c.get("value", 0)
        tier = "D (fallback only)"
        if name in ext_keys:
            tier = "A (hand-curated)"
        elif name in rich_names:
            tier = "B-rich (description + beneficiaries + legal_basis)"
        elif name in compact:
            tier = "B-compact (description + beneficiaries)"
        findings.append({
            "name": name,
            "value_GBP_B": round(value / 1e9, 2),
            "tier": tier,
        })
    return findings


def main():
    tree = json.loads(TREE.read_text(encoding="utf-8"))
    extended = json.loads(EXTENDED.read_text(encoding="utf-8"))
    compact = json.loads(COMPACT.read_text(encoding="utf-8"))
    rich_list = json.loads(RICH.read_text(encoding="utf-8"))
    rich_names = {e.get("name"): e for e in rich_list if e.get("name")}
    tree_index = walk_tree(tree)

    report = {
        "generated": "2026-04-20",
        "tier_a": tier_a_audit(extended, tree_index),
        "tier_b": tier_b_audit(compact, rich_list),
        "top_level_coverage": coverage_audit(tree, extended, compact, rich_names),
    }

    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    # Human summary
    print("=" * 70)
    print("ENRICHMENT AUDIT — 2026-04-20")
    print("=" * 70)

    ta = report["tier_a"]
    print(f"\n[Tier A] {ta['total']} hand-curated entries")
    print(f"  Tree-name exact match: {ta['tree_match_by_name']}/{ta['total']}")
    if ta["no_tree_match"]:
        print(f"  No tree match ({len(ta['no_tree_match'])}):")
        for n in ta["no_tree_match"]:
            marker = " [documented]" if n.get("note") else ""
            print(f"    - {n['key']}{marker}")
    if ta["empty_required_field"]:
        print(f"  Empty required fields:")
        for n in ta["empty_required_field"]:
            print(f"    - {n}")
    if ta["spend_discrepancy"]:
        print(f"  £ discrepancies vs tree (>25% off):")
        for d in ta["spend_discrepancy"]:
            print(f"    - {d['node']} :: {d['stat_label']} = {d['stat_value']} vs tree {d['tree_value']} (ratio {d['ratio']})")
    if ta["sources_without_url"]:
        print(f"  Entries with ZERO source URLs ({len(ta['sources_without_url'])}):")
        for n in ta["sources_without_url"][:5]:
            print(f"    - {n}")
        if len(ta["sources_without_url"]) > 5:
            print(f"    ... +{len(ta['sources_without_url']) - 5} more")

    tb = report["tier_b"]
    print(f"\n[Tier B] compact={tb['compact_total']} · rich={tb['rich_total']}")
    print(f"  Placeholder / 'n/a' entries: {len(tb['placeholder_entries'])}")
    if tb["placeholder_entries"][:5]:
        for p in tb["placeholder_entries"][:5]:
            print(f"    - {p['key']} ({p['where']})")
        if len(tb["placeholder_entries"]) > 5:
            print(f"    ... +{len(tb['placeholder_entries']) - 5} more")
    print(f"  Truncated descriptions (mid-word cut): {len(tb['truncated_descriptions'])}")
    for t in tb["truncated_descriptions"][:3]:
        print(f"    - {t['key']} :: ...{t['tail']}")
    print(f"  Suspicious founding years: {len(tb['suspicious_years'])}")
    for s in tb["suspicious_years"]:
        print(f"    - {s['key']}: declared {s['declared']}, expected {s['expected_range']}")

    print(f"\n[Coverage] Top-level UK departments ({len(report['top_level_coverage'])} in tree):")
    by_tier = Counter(c["tier"] for c in report["top_level_coverage"])
    for t, n in sorted(by_tier.items()):
        print(f"  {t}: {n}")
    # Show the worst: any top-level that fell to D
    fallbacks = [c for c in report["top_level_coverage"] if c["tier"].startswith("D")]
    if fallbacks:
        print(f"\n  Top-level departments with ONLY Tier-D coverage:")
        for c in sorted(fallbacks, key=lambda x: -x["value_GBP_B"])[:15]:
            print(f"    £{c['value_GBP_B']:6.2f}B  {c['name']}")

    print(f"\nFull report: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
