#!/usr/bin/env python3
"""
breakdown_nodes.py — Full inventory of UK tree nodes for enrichment planning.

Produces:
  data/uk/_node_breakdown.json   — full per-node record
  stdout: pivot tables by (depth × value-bucket × current tier)

The goal is to know EXACTLY what we have, at what quality, so we can plan a
multi-week campaign to lift every clickable node to State-Pension-level
quality.
"""
import json
import re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent
TREE = ROOT / "data/uk/uk_budget_tree_2024.json"
EXT = ROOT / "data/uk/node_enrichment_extended.json"
COMPACT = ROOT / "data/uk/program_enrichment.json"
RICH = ROOT / "data/uk/enrichment_top50.json"
POPS = ROOT / "data/uk/ons/gss_population_mid2023.json"
OUT = ROOT / "data/uk/_node_breakdown.json"

VALUE_BUCKETS = [
    (100e9,  "£100B+"),
    (10e9,   "£10-100B"),
    (1e9,    "£1-10B"),
    (100e6,  "£100M-1B"),
    (10e6,   "£10-100M"),
    (1e6,    "£1-10M"),
    (0,      "<£1M"),
]


def bucket_for(v):
    for threshold, label in VALUE_BUCKETS:
        if v >= threshold:
            return label
    return "<£1M"


def norm(s):
    return re.sub(r"[^a-z0-9]", "", str(s or "").lower())


def walk(node, depth=0, path=None, results=None):
    if results is None:
        results = []
    if path is None:
        path = []
    results.append({
        "depth": depth,
        "name": node.get("name", ""),
        "value": node.get("value", 0) or 0,
        "path": path[:],
        "children_count": len(node.get("children") or []),
        "has_top_suppliers": bool(node.get("_top_suppliers")),
        "has_source_meta": bool(node.get("_source")),
        "has_trust_meta": bool(node.get("_sector") or node.get("_icb")),
    })
    for i, c in enumerate(node.get("children") or []):
        walk(c, depth + 1, path + [i], results)
    return results


def classify_tier(node, ext_keys, ext_aliases, rich_names, compact_keys, pop_norms):
    """Match the frontend's 4-tier cascade."""
    name = node["name"]
    # Tier A — extended by primary key OR alias
    if name in ext_keys:
        return "A"
    if name in ext_aliases:
        return "A (via alias)"
    # Tier B — rich
    if name in rich_names:
        return "B-rich"
    # Tier B — compact
    if name in compact_keys:
        return "B-compact"
    # Tier C — council or council-service (procedural)
    path = node["path"]
    if len(path) >= 2:
        # Synthesise ancestor names from path + tree (need the tree)
        # Here we approximate: tier parent presence is checked at render time.
        # We only record a hint — real Tier C match needs full walker.
        pass
    return None  # fall-through


def main():
    tree = json.loads(TREE.read_text(encoding="utf-8"))
    ext = json.loads(EXT.read_text(encoding="utf-8"))
    compact = json.loads(COMPACT.read_text(encoding="utf-8"))
    rich_list = json.loads(RICH.read_text(encoding="utf-8"))
    pops_file = json.loads(POPS.read_text(encoding="utf-8"))

    ext_keys = set(ext.get("entries", {}).keys())
    ext_aliases = set()
    for entry in ext.get("entries", {}).values():
        for a in entry.get("aliases") or []:
            ext_aliases.add(a)
    rich_names = set(e.get("name") for e in rich_list if e.get("name"))
    compact_keys = set(compact.keys())

    pop_norms = {
        norm(info["name"]): info["population"]
        for info in (pops_file.get("populations") or {}).values()
    }

    # Also build a flat index for ancestor lookup
    flat = walk(tree)
    # Index by path-tuple for ancestor walking
    by_path = {tuple(n["path"]): n for n in flat}

    # LG tier names for Tier C detection
    LG_TIERS = {
        "Shire Counties", "London Boroughs", "Metropolitan Districts",
        "Unitary Authorities", "Shire Districts", "Other Authorities",
    }

    def ancestors_of(n):
        """Return list of ancestor nodes (excluding self, including root at [])."""
        out = []
        for i in range(len(n["path"])):
            out.append(by_path[tuple(n["path"][:i])])
        return out

    # Classify every node
    records = []
    for n in flat:
        rec = {
            "depth": n["depth"],
            "name": n["name"],
            "value": n["value"],
            "value_B": round(n["value"] / 1e9, 4),
            "value_bucket": bucket_for(n["value"]),
            "path": n["path"],
            "children_count": n["children_count"],
            "has_top_suppliers": n["has_top_suppliers"],
            "has_source_meta": n["has_source_meta"],
            "has_trust_meta": n["has_trust_meta"],
        }
        # Tier A / B match
        tier = classify_tier(n, ext_keys, ext_aliases, rich_names, compact_keys, pop_norms)
        if not tier:
            # Tier C heuristic: is node a council or council-service leaf?
            ancs = ancestors_of(n)
            if ancs:
                parent = ancs[-1]
                gp = ancs[-2] if len(ancs) >= 2 else None
                if parent["name"] in LG_TIERS:
                    # council — check if we have a pop for it
                    stripped = re.sub(
                        r"\b(CC|MBC|UA|Borough|City|District|County|Council|Corporation)\b",
                        "", n["name"], flags=re.I).strip()
                    if pop_norms.get(norm(n["name"])) or pop_norms.get(norm(stripped)):
                        tier = "C-council-with-pop"
                    else:
                        tier = "C-council-no-pop"
                elif gp and gp["name"] in LG_TIERS:
                    # council-service leaf
                    tier = "C-service"
        if not tier:
            tier = "D-fallback"
        rec["tier"] = tier
        records.append(rec)

    # Pivot: tier × depth
    pivot_tier_depth = defaultdict(lambda: Counter())
    for r in records:
        pivot_tier_depth[r["tier"]][r["depth"]] += 1

    # Pivot: tier × value_bucket
    pivot_tier_value = defaultdict(lambda: Counter())
    for r in records:
        pivot_tier_value[r["tier"]][r["value_bucket"]] += 1

    # Count by current tier
    tier_counts = Counter(r["tier"] for r in records)
    total = len(records)

    # Identify the "State-Pension-quality" quality level in our Tier A
    state_pension = ext.get("entries", {}).get("State Pension", {})
    gold_stats_count = len(state_pension.get("key_stats") or [])
    gold_has_legal = bool(state_pension.get("legal_basis"))
    gold_has_notes = bool(state_pension.get("notes"))
    gold_sources = len(state_pension.get("sources") or [])

    # Count Tier A entries meeting the "gold" bar
    gold_entries = []
    for k, e in ext.get("entries", {}).items():
        stats_count = len(e.get("key_stats") or [])
        has_legal = bool(e.get("legal_basis"))
        has_notes = bool(e.get("notes"))
        sources_count = len(e.get("sources") or [])
        gold = (stats_count >= 8 and has_legal and has_notes and sources_count >= 3)
        gold_entries.append({
            "key": k,
            "stats_count": stats_count,
            "has_legal": has_legal,
            "has_notes": has_notes,
            "sources_count": sources_count,
            "meets_gold": gold,
        })
    n_gold = sum(1 for g in gold_entries if g["meets_gold"])

    # Output
    report = {
        "generated": "2026-04-20",
        "total_nodes": total,
        "tier_counts": dict(tier_counts),
        "pivot_tier_depth": {k: dict(v) for k, v in pivot_tier_depth.items()},
        "pivot_tier_value": {k: dict(v) for k, v in pivot_tier_value.items()},
        "gold_standard": {
            "reference": "State Pension",
            "required_stats": 8,
            "required_legal_basis": True,
            "required_notes": True,
            "required_sources": 3,
            "tier_a_entries_meeting_bar": n_gold,
            "tier_a_total": len(gold_entries),
        },
        "per_node_records": records,  # heavy — can skip if too big
    }

    # Save but drop per_node_records to keep file readable
    small = {k: v for k, v in report.items() if k != "per_node_records"}
    OUT.write_text(json.dumps(small, indent=2, ensure_ascii=False), encoding="utf-8")

    # Human report
    print("=" * 72)
    print(f"UK TREE NODE BREAKDOWN — {report['generated']}")
    print("=" * 72)
    print(f"Total nodes: {total:,}")
    print()
    print("Coverage by tier:")
    for tier in sorted(tier_counts.keys()):
        c = tier_counts[tier]
        print(f"  {tier:30s} {c:5,}  ({c/total*100:5.1f}%)")
    print()

    print("Gold-standard (State-Pension-level) quality bar:")
    print(f"  Required: >=8 key_stats + legal_basis + notes + >=3 sources")
    print(f"  Tier A entries meeting bar: {n_gold}/{len(gold_entries)}")
    if len(gold_entries) - n_gold > 0:
        print(f"  Tier A entries BELOW bar ({len(gold_entries) - n_gold}):")
        for g in gold_entries:
            if not g["meets_gold"]:
                gaps = []
                if g["stats_count"] < 8: gaps.append(f"stats={g['stats_count']}")
                if not g["has_legal"]: gaps.append("no legal_basis")
                if not g["has_notes"]: gaps.append("no notes")
                if g["sources_count"] < 3: gaps.append(f"sources={g['sources_count']}")
                print(f"    - {g['key']:50s}  ({', '.join(gaps)})")
    print()

    print("Pivot: tier x depth (clicks concentrate at depths 1-3):")
    depths = sorted({d for v in pivot_tier_depth.values() for d in v})
    head = "  " + "Tier".ljust(30) + "".join(f"d{d:<4}" for d in depths)
    print(head)
    for tier in sorted(pivot_tier_depth.keys()):
        row = "  " + tier.ljust(30)
        for d in depths:
            c = pivot_tier_depth[tier].get(d, 0)
            row += f"{c:<5,}"
        print(row)
    print()

    print("Pivot: tier x value bucket (biggest nodes = most impact):")
    vals = [b[1] for b in VALUE_BUCKETS]
    head = "  " + "Tier".ljust(30) + "".join(f"{v[:10]:<12}" for v in vals)
    print(head)
    for tier in sorted(pivot_tier_value.keys()):
        row = "  " + tier.ljust(30)
        for v in vals:
            c = pivot_tier_value[tier].get(v, 0)
            row += f"{c:<12,}"
        print(row)
    print()

    # Priority buckets: biggest + shallowest nodes without Tier A
    print("PRIORITY: biggest nodes NOT in Tier A (ordered by value):")
    not_a = [r for r in records if not r["tier"].startswith("A") and r["depth"] > 0]
    not_a.sort(key=lambda r: -r["value"])
    for r in not_a[:40]:
        print(f"  £{r['value_B']:7.2f}B  d{r['depth']}  [{r['tier']:25s}]  {r['name'][:60]}")
    print()
    print(f"Full breakdown written to: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    main()
