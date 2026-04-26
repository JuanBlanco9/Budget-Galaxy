"""Build Phase 2 NHS Mental Health slice 2 brief.

Slice 1 (200 entries top-£) was hand-curated in waves 1-3. Slice 2 covers the
remaining ~285 MH orphans — lower-£ sub-lines like Business rates, Amortisation,
Lease, Inventories, Termination, mostly < £5M each.
"""
import json
import re
import sys
from pathlib import Path
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(50000)

with open('data/uk/node_enrichment_extended.json', encoding='utf-8') as f: ext = json.load(f)
with open('data/uk/uk_budget_tree_2024.json', encoding='utf-8') as f: tree = json.load(f)
keys = set(ext['entries'].keys())

aliases_scoped = defaultdict(set)
for k, e in ext['entries'].items():
    for a in (e.get('aliases') or []):
        if isinstance(a, dict) and a.get('name') and a.get('parent'):
            aliases_scoped[(a['name'], a['parent'])].add(k)

def find_target_subtree(n, chain=[]):
    results = []
    name = n.get('name', '')
    if name == 'NHS Mental Health Trusts':
        for t in (n.get('children') or []):
            tname = t.get('name', '')
            if 'Trust' in tname or 'Health Board' in tname:
                results.append((t, chain + [name]))
    for c in (n.get('children') or []):
        results.extend(find_target_subtree(c, chain + [name]))
    return results

trust_subtrees = find_target_subtree(tree)
print(f'NHS MH Trusts: {len(trust_subtrees)}')

orphans = []
def walk_node(n, trust_name, chain):
    name = n.get('name', '')
    v = n.get('value') or 0
    if name and v > 1e5:
        composite = f'{name} — {trust_name}'
        if composite not in keys and (name, trust_name) not in aliases_scoped:
            orphans.append({
                'trust': trust_name,
                'sub_line': name,
                'value': v,
                'parent_line': chain[-1] if chain else '',
            })
    for c in (n.get('children') or []):
        walk_node(c, trust_name, chain + [name])

for trust_node, chain in trust_subtrees:
    tname = trust_node.get('name', '')
    for child in (trust_node.get('children') or []):
        walk_node(child, tname, chain + [trust_node.get('name', '')])

print(f'Slice 2 MH orphans: {len(orphans)}')
print(f'Total £: £{sum(o["value"] for o in orphans)/1e9:.2f}B')
by_subline = Counter(o['sub_line'] for o in orphans)
print('Top sub-lines in slice 2:')
for n, c in by_subline.most_common(15):
    total = sum(o['value'] for o in orphans if o['sub_line']==n)/1e9
    print(f'  {c:4d}  £{total:>5.2f}B  {n}')

# Sort by £ desc, save
orphans.sort(key=lambda x: -x['value'])

brief_path = Path('scripts/hand_curation_briefs/phase2_mh_slice2.md')
brief_path.write_text(f"""# Cluster Phase2_MH_slice2 — NHS Mental Health Trust orphan sub-lines (lower-£ tail)

Scope: {len(orphans)} orphan depth-5 sub-lines under NHS MH Trusts that weren't covered by slice 1 (top-£ 200) · total £{sum(o['value'] for o in orphans)/1e9:.2f}B

## Archetype: PROGRAMME (per docs/archetype_briefs.md)

Required dimensions per entry: Delivery body · Policy owner · Beneficiary count · Funding trajectory · Evaluation evidence · Predecessor/successor

## Sub-line types in slice 2 (mostly < £5M each)

These are the residual MH orphan sub-lines: Business rates, Amortisation, Lease, Inventories, Termination & post-employment, Other & adjustments.

## What each sub-line covers (to drive trust-specific narratives)

- **Business rates** — VOA-set rateable value × 49.9p UBR (2024-25 small/standard) on each occupied site. NHS MH trusts rated as "Other" hereditaments unless charitable exemption applies.
- **Amortisation** — Intangible asset depreciation (mainly software, capitalised training, EPR rollouts under Frontline Digitisation programme).
- **Lease expenditure** — IFRS 16 right-of-use asset opex post-2022 transition. NHSPS-leased clinic estate dominates for MH community sites.
- **Inventories written down** — Stock writedowns (drugs near expiry, ward consumables, PPE legacy).
- **Termination & post-employment** — One-off severance + exit pay (NHS Pension Scheme employer element + senior-staff exit packages).
- **Other & adjustments** — Cleanup line for prior-year corrections, AME reclassifications.

## Schema per entry (PROGRAMME contract floors)

```python
"<sub-line> — <MH trust>": {{
    "aliases": [{{"name": "<sub-line>", "parent": "<MH trust>"}}],
    "description": "3-5 sentences, 250-600 chars · trust-specific (sub-line-type-specific drivers, with the trust's specialty mix as anchor)",
    "beneficiaries": "1-2 sentences with CONCRETE N (sites for business rates · users on rolled-out EPR for amortisation · etc)",
    "legal_basis": "[sub-line-type-specific] · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 + applicable IAS/IFRS",
    "key_stats": [...],  # 8-12 trust-specific
    "notes": "3-5 sentences, 300-800 chars · trust-specific drivers + recent context",
    "sources": [...],  # 4-6 dicts {{publisher, title, url}} https://
    "related": [...]   # 3-6 cross-links (incl. parent line + relevant policy programme + peer trust)
}}
```

## Sub-line specific legal_basis

- Business rates: Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006
- Amortisation: IAS 38 Intangible Assets · DHSC GAM 2024-25 ch.5 · NHS Act 2006
- Lease: IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954
- Inventories: IAS 2 Inventories · DHSC GAM 2024-25
- Termination: IAS 19 Employee Benefits · NHS Pension Scheme regulations · Public Sector Exit Payments Regulations 2020
- Other & adjustments: General GAM disclosure rules

## Anchors
- Frontline Digitisation EPR rollouts (amortisation driver post-2023)
- IFRS 16 transition 2022 (lease line jump)
- Edenfield Panorama, Lampard Inquiry, Whorlton Hall — relevant for termination + inventories context where trusts incurred remediation costs
- NHSPS dispute on community-clinic rates (lease + business rates interaction)
- April 2025 employer NIC step-up affecting NHS Pension Scheme employer element on termination

## Hard rules
- Em-dash ` — ` (U+2014)
- Scoped alias parent = EXACT trust name from JSON
- `sources` MUST be list of dicts {{publisher, title, url}} https://
- 8-12 stats · 4-6 sources · 3-6 related · 3-5 sentence notes (300-800) · 3-5 sentence description (250-600)
- All 6 PROGRAMME dimensions present
- Watchdog-safe incremental Edit (skeleton + per-entry inserts)

## Sub-lines in this cluster

""", encoding='utf-8')
with brief_path.open('a', encoding='utf-8') as f:
    for r in orphans:
        f.write(f"### {r['sub_line']} — {r['trust']}\n  parent line: {r['parent_line']}\n  value: £{r['value']/1e6:.2f}M\n\n")

print(f'Wrote {brief_path}')

# Split into chunks of 17
CHUNK = 17
for i in range(0, len(orphans), CHUNK):
    chunk = orphans[i:i+CHUNK]
    label = f'phase2_mh_slice2_chunk{(i//CHUNK)+1:02d}'
    p = Path(f'scripts/hand_curation_briefs/{label}.json')
    p.write_text(json.dumps(chunk, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  {label}: {len(chunk)} entries')
