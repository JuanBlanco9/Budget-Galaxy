"""Build Phase 2 NHS Acute slice 2 brief.

Slice 1 (132 top-£) was hand-curated in waves prior. Slice 2 covers the
remaining ~1,019 Acute Trust orphans — long-tail by £ but still
trust-specific narratives needed (PROGRAMME archetype).
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
    if name == 'NHS Acute Trusts':
        for t in (n.get('children') or []):
            tname = t.get('name', '')
            if 'Trust' in tname or 'Health Board' in tname:
                results.append((t, chain + [name]))
    for c in (n.get('children') or []):
        results.extend(find_target_subtree(c, chain + [name]))
    return results

trust_subtrees = find_target_subtree(tree)
print(f'NHS Acute Trusts: {len(trust_subtrees)}')

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

print(f'Acute slice 2 orphans: {len(orphans)}')
print(f'Total £: £{sum(o["value"] for o in orphans)/1e9:.2f}B')
by_subline = Counter(o['sub_line'] for o in orphans)
print('\nTop sub-line types:')
for n, c in by_subline.most_common(15):
    total = sum(o['value'] for o in orphans if o['sub_line']==n)/1e9
    print(f'  {c:4d}  £{total:>5.2f}B  {n}')

# Sort by £ desc
orphans.sort(key=lambda x: -x['value'])

brief_path = Path('scripts/hand_curation_briefs/phase2_acute_slice2.md')
brief_path.write_text(f"""# Cluster Phase2_Acute_slice2 — NHS Acute Trust orphan sub-lines (long-tail)

Scope: {len(orphans)} orphan depth-5 sub-lines under NHS Acute Trusts not yet covered · total £{sum(o['value'] for o in orphans)/1e9:.2f}B

## Archetype: PROGRAMME (per docs/archetype_briefs.md)

Required dimensions per entry: Delivery body · Policy owner · Beneficiary count · Funding trajectory · Evaluation evidence · Predecessor/successor

## Sub-line types in slice 2

Mix of operational lines: Establishment costs · Transport · General supplies & services · Lease · Amortisation · Business rates · Inventories · Termination · Other & adjustments · plus residual PFI/LIFT charges · Impairments tail.

## Key 2024-25 Acute trust context

- **NHS England Operating Plan 2024-25**: 76% A&E 4-hour standard, 92% RTT 18-week (paused), £6.6B productivity assumption
- **Industrial action 2023-24**: junior doctors 11 strikes (44 days), consultants 7 strikes (10 days) — heavy on Acute trusts (vs MH/community lower direct impact). Backfill agency + locum cost feeds Establishment + Transport
- **Frontline Digitisation EPR rollout**: Cerner / Oracle Health / Epic / SystemC adoption — drives Amortisation (capitalised intangible) and Establishment (training/change-mgmt)
- **NHSPS rent dispute** (2018-2024 ongoing): community-clinic Acute trusts in arrears
- **April 2025 employer NIC step-up** (15%, £5k threshold) — Social security & levy pressure
- **NHP cohort + Reset Jan 2025**: trusts in original 40-hospitals programme had baseline impairment and lease assumptions; deferral changes 2025-30 trajectory
- **RAAC Sep 2023 HSSIB list**: 27 trusts — concrete-plank failure drives premises + impairment + transport (decant) lines
- **Carillion 2018 collapse + Engie/Equans/Sodexo novations**: ongoing FM contract churn at PFI Acute trusts (NBT Brunel, Royal Liverpool, MMUH SWBH, Wye Valley)

## Schema per entry (PROGRAMME contract floors)

```python
"<sub-line> — <Acute trust>": {{
    "aliases": [{{"name": "<sub-line>", "parent": "<Acute trust>"}}],
    "description": "3-5 sentences, 250-600 chars · trust-specific (sub-line driver + trust specialty mix + ICS group context)",
    "beneficiaries": "1-2 sentences with CONCRETE N (sites · ED attendances · elective admissions · WTE)",
    "legal_basis": "<sub-line-type-specific> · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 · applicable IAS/IFRS",
    "key_stats": [...],  # 8-12 trust-specific
    "notes": "3-5 sentences, 300-800 chars trust-specific drivers + recent context",
    "sources": [...],  # 4-6 dicts {{publisher, title, url}} https://
    "related": [...]   # 3-6 cross-links (incl. parent line + relevant policy programme + peer trust + Premises (other) — <trust> cross-ref)
}}
```

## Sub-line specific legal_basis

- **Establishment costs**: GAM operating expenses · IAS 1 Presentation of Financial Statements · NHS Act 2006
- **Transport (business + patient)**: NHS Act 2006 · NHSE Patient Transport Services Eligibility · AfC Section 17 + AMAP · IFRS 16 (pool fleet)
- **General supplies & services**: GAM operating expenses · IAS 2 Inventories (interaction)
- **Business rates**: Local Government Finance Act 1988 (Sch 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024
- **Amortisation**: IAS 38 Intangible Assets · DHSC GAM ch.5
- **Lease expenditure**: IFRS 16 Leases · DHSC GAM ch.7 · Landlord and Tenant Act 1954
- **Inventories**: IAS 2 · DHSC GAM
- **Termination & post-employment**: IAS 19 · NHS Pension Scheme regs · Public Sector Exit Payments Regs 2020
- **PFI / LIFT charges**: IFRIC 12 Service Concession Arrangements · IFRS 16 (post-2022) · DHSC PFI guidance
- **Impairments residual**: IAS 36 · DHSC GAM ch.4 (cross-ref existing D4_08 entries — slice2 is residuals only)

## PROGRAMME dimensions per entry

1. **Delivery body**: trust dept (E&F · Procurement · Pharmacy · IT) + external contractor (Sodexo · Equans · Cerner · Oracle Health · Epic · SystemC · NHS Supply Chain · NHSPS)
2. **Policy owner**: NHSE Provider Finance · DHSC · NHS Resolution (CNST) · NHS Supply Chain · NHS Property Services
3. **Beneficiary count**: concrete N (sites · ED attendances · elective admissions · WTE staff)
4. **Funding trajectory**: 3-5 year £ trend (industrial action 2023-24 backfill spike · Frontline Digitisation amort cycle · IFRS 16 jump 2022 · NHP Reset deferral)
5. **Evaluation evidence**: NAO Acute reports · CQC inspections · NHSE Operational Plan returns · Carter Lord review legacy · Model Hospital
6. **Predecessor/successor**: prior contract / merger / scheme · current vehicle · planned NHP rebuild or Reset deferral

## Hard rules
- Em-dash ` — ` (U+2014)
- Scoped alias parent = EXACT trust name from JSON
- `sources` MUST be list of dicts {{publisher, title, url}} https://
- 8-12 stats · 4-6 sources · 3-6 related · 3-5 sentence notes (300-800) · 3-5 sentence description (250-600)
- All 6 PROGRAMME dimensions present
- NO boilerplate placeholders
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
    label = f'phase2_acute_slice2_chunk{(i//CHUNK)+1:02d}'
    p = Path(f'scripts/hand_curation_briefs/{label}.json')
    p.write_text(json.dumps(chunk, ensure_ascii=False, indent=2), encoding='utf-8')
    if (i//CHUNK)+1 <= 3 or (i//CHUNK)+1 >= len(orphans)//CHUNK:
        print(f'  {label}: {len(chunk)} entries')

print(f'\nTotal chunks: {(len(orphans)+CHUNK-1)//CHUNK}')
