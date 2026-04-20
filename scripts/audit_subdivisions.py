#!/usr/bin/env python3
"""
audit_subdivisions.py — Walk the children/grandchildren of every Tier A
department and classify each by enrichment tier. Identifies the specific
sub-nodes that need custom curation to avoid "DWP is gold but its first
child is Tier B-compact MEH" pattern.

Output:
  data/uk/_subdivision_audit.json  — machine-readable per-department report
  stdout — priority list of sub-nodes to hand-curate next
"""
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
TREE = ROOT / "data/uk/uk_budget_tree_2024.json"
EXT = ROOT / "data/uk/node_enrichment_extended.json"
COMPACT = ROOT / "data/uk/program_enrichment.json"
RICH = ROOT / "data/uk/enrichment_top50.json"
OUT = ROOT / "data/uk/_subdivision_audit.json"


def load():
    tree = json.loads(TREE.read_text(encoding="utf-8"))
    ext = json.loads(EXT.read_text(encoding="utf-8"))
    compact = json.loads(COMPACT.read_text(encoding="utf-8"))
    rich_list = json.loads(RICH.read_text(encoding="utf-8"))

    ext_keys = set(ext.get("entries", {}).keys())
    # Aliases can be strings (unscoped) or {name, parent} dicts (scoped).
    # For auditing we union both into ext_aliases as plain names — this slightly
    # over-counts but matches the reality that a scoped-alias-registered node
    # IS covered in gold when the loader is parent-aware.
    ext_aliases = set()
    for e in ext.get("entries", {}).values():
        for a in e.get("aliases") or []:
            if isinstance(a, str):
                ext_aliases.add(a)
            elif isinstance(a, dict) and a.get("name"):
                ext_aliases.add(a["name"])
    rich_names = {e.get("name") for e in rich_list if e.get("name")}

    return tree, ext, ext_keys, ext_aliases, rich_names, compact


def classify(name, ext_keys, ext_aliases, rich_names, compact_keys):
    if name in ext_keys:
        return "A"
    if name in ext_aliases:
        return "A-alias"
    if name in rich_names:
        return "B-rich"
    if name in compact_keys:
        return "B-compact"
    return "D-fallback"


# Tier A parent departments we've invested in
TIER_A_PARENTS = [
    "DEPARTMENT FOR WORK AND PENSIONS",
    "DEPARTMENT OF HEALTH",
    "DEPARTMENT FOR EDUCATION",
    "HOME OFFICE",
    "MINISTRY OF HOUSING, COMMUNITIES AND LOCAL GOVERNMENT",
    "MINISTRY OF JUSTICE",
    "HM TREASURY",
    "DEPARTMENT FOR TRANSPORT",
    "DEPARTMENT FOR ENERGY SECURITY AND NET ZERO",
    "DEPARTMENT FOR CULTURE, MEDIA AND SPORT",
    "DEPARTMENT FOR SCIENCE, INNOVATION AND TECHNOLOGY",
    "DEPARTMENT FOR ENVIRONMENT, FOOD AND RURAL AFFAIRS",
    "MINISTRY OF DEFENCE",
    "HM REVENUE AND CUSTOMS",
    "NHS Provider Sector",
    "Local Government (England)",
    "SCOTTISH GOVERNMENT",
    "NORTHERN IRELAND EXECUTIVE",
    "WELSH ASSEMBLY GOVERNMENT",
]

PLACEHOLDER_PATTERN = re.compile(
    r"^(n/a|Not known|\d+\.\d+ [A-Z]|.*\boffset\b.*|.*\bReserves\b.*)", re.IGNORECASE
)


def is_meaningful(name, value):
    """Skip OSCAR placeholders and tiny values when prioritising."""
    if not name:
        return False
    nm = name.strip()
    if nm.lower() in ("n/a", "not known", "unclassified", "tbd"):
        return False
    # Keep COFOG codes — they ARE meaningful programme aggregates
    return True


def main():
    tree, ext, ext_keys, ext_aliases, rich_names, compact = load()
    compact_keys = set(compact.keys())

    report = {"generated": "2026-04-20", "parents": {}}
    priority_targets = []

    top_children = tree.get("children", [])
    top_by_name = {c.get("name"): c for c in top_children}

    for parent_name in TIER_A_PARENTS:
        parent = top_by_name.get(parent_name)
        if not parent:
            continue

        kids = parent.get("children", []) or []
        # Sort by value descending
        kids_sorted = sorted(kids, key=lambda c: -(c.get("value") or 0))

        parent_record = {
            "parent_value_B": round(parent.get("value", 0) / 1e9, 2),
            "children_count": len(kids),
            "children_by_tier": defaultdict(int),
            "meaningful_children_bigger_than_1B": [],
            "grandchildren_big_gaps": [],
        }

        for child in kids_sorted:
            cname = child.get("name", "")
            cval = child.get("value", 0) or 0
            tier = classify(cname, ext_keys, ext_aliases, rich_names, compact_keys)
            parent_record["children_by_tier"][tier] += 1

            # Flag meaningful children >£1B not in Tier A
            if (
                is_meaningful(cname, cval)
                and cval >= 1e9
                and tier not in ("A", "A-alias")
            ):
                entry = {
                    "name": cname,
                    "value_B": round(cval / 1e9, 2),
                    "tier": tier,
                    "parent": parent_name,
                    "has_top_suppliers": bool(child.get("_top_suppliers")),
                    "children_count": len(child.get("children") or []),
                }
                parent_record["meaningful_children_bigger_than_1B"].append(entry)
                # Add to global priority if big
                if cval >= 5e9:
                    priority_targets.append(entry)

            # Walk grandchildren to spot big gaps one more level down
            for gc in (child.get("children") or []):
                gname = gc.get("name", "")
                gval = gc.get("value", 0) or 0
                if (
                    is_meaningful(gname, gval)
                    and gval >= 5e9
                ):
                    gtier = classify(gname, ext_keys, ext_aliases, rich_names, compact_keys)
                    if gtier not in ("A", "A-alias"):
                        parent_record["grandchildren_big_gaps"].append({
                            "name": gname,
                            "value_B": round(gval / 1e9, 2),
                            "tier": gtier,
                            "parent_child": cname,
                            "parent_top": parent_name,
                        })

        parent_record["children_by_tier"] = dict(parent_record["children_by_tier"])
        report["parents"][parent_name] = parent_record

    # Sort priority targets
    priority_targets.sort(key=lambda x: -x["value_B"])
    report["priority_targets_gt_5B"] = priority_targets

    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    # Human summary
    print("=" * 80)
    print("SUB-DIVISION AUDIT — curated parents + their children")
    print("=" * 80)

    # Per parent — tier distribution of direct children
    print(f"\n{'Parent':50s}  A+A-alias  B-rich  B-compact  D  Kids  £B")
    print("-" * 95)
    for parent_name in TIER_A_PARENTS:
        pr = report["parents"].get(parent_name)
        if not pr:
            continue
        t = pr["children_by_tier"]
        a = t.get("A", 0) + t.get("A-alias", 0)
        br = t.get("B-rich", 0)
        bc = t.get("B-compact", 0)
        d = t.get("D-fallback", 0)
        print(
            f"{parent_name[:48]:50s}  {a:3d}        {br:3d}     {bc:3d}        {d:2d}  {pr['children_count']:3d}   £{pr['parent_value_B']}B"
        )

    # Most critical: big meaningful children not in Tier A
    print("\n\n" + "=" * 80)
    print("PRIORITY: meaningful children >£1B in curated-parent branches, NOT in Tier A")
    print("=" * 80)
    all_priority = []
    for parent_name in TIER_A_PARENTS:
        pr = report["parents"].get(parent_name)
        if not pr:
            continue
        for ch in pr["meaningful_children_bigger_than_1B"]:
            all_priority.append(ch)
    all_priority.sort(key=lambda x: -x["value_B"])

    for ch in all_priority[:50]:
        tag = f"[{ch['tier']}]"
        ts = " 🧾supp" if ch["has_top_suppliers"] else ""
        print(f"  £{ch['value_B']:7.2f}B  {tag:12s}  {ch['name'][:55]:55s}  ← {ch['parent'][:30]}{ts}")

    # Grandchildren >£5B gaps
    print("\n" + "=" * 80)
    print("DEEPER: grandchildren >£5B not in Tier A (two levels down from curated parents)")
    print("=" * 80)
    gc_priority = []
    for parent_name in TIER_A_PARENTS:
        pr = report["parents"].get(parent_name)
        if not pr:
            continue
        for gc in pr["grandchildren_big_gaps"]:
            gc_priority.append(gc)
    gc_priority.sort(key=lambda x: -x["value_B"])
    for gc in gc_priority[:30]:
        tag = f"[{gc['tier']}]"
        print(f"  £{gc['value_B']:7.2f}B  {tag:12s}  {gc['name'][:55]:55s}  ← {gc['parent_child'][:30]} ← {gc['parent_top'][:15]}")

    # Totals
    total_gap_value = sum(x["value_B"] for x in all_priority if x["tier"] != "B-rich")
    print(f"\n\nTotal £ of priority targets (>£1B, not Tier A, not even B-rich): £{total_gap_value:.1f}B")
    print(f"Full report: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
