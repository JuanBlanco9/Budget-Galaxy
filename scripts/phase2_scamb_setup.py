"""Build Phase 2 Specialist + Community + Ambulance unified brief.

Combines the 3 remaining NHS provider categories that haven't been audited:
  - Specialist:  100 orphans · £0.37B (15 trusts)
  - Community:   130 orphans · £0.52B (18 trusts)
  - Ambulance:    77 orphans · £0.72B (10 trusts)
  Total:         307 orphans · £1.61B (43 trusts)

Sub-line types are the same operational mix as Acute slice 2 — Establishment,
Transport, Supplies, Business rates, Amortisation, Lease, Inventories, S&L,
Termination, PFI/LIFT residuals, Impairments tail. Briefs reusable.
"""
import json
import sys
from pathlib import Path
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(50000)

# Load all 3 orphan files, tag with category, merge
all_orphans = []
for cat, label in [('specialist','Specialist'), ('community','Community'), ('ambulance','Ambulance')]:
    arr = json.load(open(f'data/uk/factcheck/phase2_{cat}_orphans.json', encoding='utf-8'))
    for o in arr:
        o['category'] = label
    all_orphans.extend(arr)

# Sort by £ desc
all_orphans.sort(key=lambda x: -x['value'])
print(f'Total orphans across 3 categories: {len(all_orphans)}')
print(f'Total £: £{sum(o["value"] for o in all_orphans)/1e9:.2f}B')

# Brief
brief_path = Path('scripts/hand_curation_briefs/phase2_scamb.md')
brief_path.write_text(f"""# Cluster Phase2_SCamb — NHS Specialist + Community + Ambulance Trust orphan sub-lines

Scope: {len(all_orphans)} orphan depth-5 sub-lines under NHS Specialist (100), Community (130), Ambulance (77) Trusts · total £{sum(o['value'] for o in all_orphans)/1e9:.2f}B

## Archetype: PROGRAMME (per docs/archetype_briefs.md)

Required dimensions per entry: Delivery body · Policy owner · Beneficiary count · Funding trajectory · Evaluation evidence · Predecessor/successor

## Sub-line types in this cluster

Same operational mix as Acute slice 2: Establishment costs · Transport (business + patient) · General supplies & services · Business rates · Amortisation · Lease expenditure · Social security & levy · Inventories written down · Termination & post-employment · PFI / LIFT charges · Drugs costs · Other & adjustments.

## Trust-category-specific context (vs Acute)

### NHS Specialist Trusts (15 trusts in scope · £0.37B orphans)
Single-condition or organ-specific tertiary referral centres: Moorfields (eye), GOSH (paediatric), Royal Marsden (cancer), Royal Brompton & Harefield (heart/lung), Christie (cancer), Walton (neuro), RNOH Stanmore (orthopaedic), Liverpool Heart & Chest, Papworth (heart/lung absorbed by CUH), Birmingham Children's, Sheffield Children's, Royal Orthopaedic Birmingham, Tavistock & Portman (gender — wound down 2024), QVH East Grinstead (reconstructive). Drivers different from Acute:
- **Specialised commissioning** via NHSE Specialised Commissioning (vs ICB local)
- **Cyclotron + linac depreciation** (Christie, Royal Marsden) — high amortisation
- **Listed-building constraints** (RNOH 1922 buildings, RBHT Royal Brompton listed) — premises mix
- **Supra-regional referral catchments** — not population-coterminous

### NHS Community Trusts (18 trusts in scope · £0.52B orphans)
Provide community nursing, district nursing, health visiting, school nursing, end-of-life community care, MSK community physio. Different cost mix:
- **Workforce-heavy** — Social security & levy is dominant (mostly nurses + AHPs in clients' homes)
- **Vehicle fleet** — district-nursing cars, MSK community-physio mobile units → big Transport line
- **NHSPS-leased estate** dominates premises (vs Acute hospital owned estate) — but flow appears in Lease, not Premises
- **Out-of-hospital direction of travel** (Darzi report Sep 2024 · Three Shifts) → growth capex but flat opex
- Examples: Bridgewater, Central London Community Healthcare, Hertfordshire Community, Leicestershire Partnership, Lincolnshire Community, Solent, Sussex Community, Wirral Community

### NHS Ambulance Trusts (10 trusts in scope · £0.72B orphans)
The 10 regional ambulance services (LAS, NWAS, EMAS, EEAST, SWAST, SCAS, SECAmb, NEAS, WMAS, YAS). Cost mix totally different:
- **Transport** is the BIGGEST line — fleet replacement + fuel + AMAP + Cat-1/Cat-2 dispatch
- **Estate** is small (ambulance stations, hub & spoke model), lots leased from NHSPS
- **Industrial action 2023-24** — paramedics struck, GMB+Unison heavy. Backfill agency cost
- **Make Ready Centres** — prep vehicles, big cleaning supplies line
- **CFR programme** — Community First Responder volunteer scheme
- **Cat-1 8-min standard** — RRV motorbikes, bicycles in central London → small fleet diversification
- **Air Ambulance** — partner charity (HEMS) but lease-based aircraft
- Examples: London Ambulance Service · NWAS (North West) · EMAS (East Midlands) · EEAST (East of England) · SWAST (South Western) · SCAS (South Central) · SECAmb (South East Coast) · NEAS (North East) · WMAS (West Midlands) · YAS (Yorkshire)

## Schema per entry (PROGRAMME contract floors)

```python
"<sub-line> — <trust>": {{
    "aliases": [{{"name": "<sub-line>", "parent": "<trust>"}}],
    "description": "3-5 sentences, 250-600 chars · trust-specific (sub-line driver + trust specialty mix)",
    "beneficiaries": "1-2 sentences with CONCRETE N (sites · referral catchment · WTE)",
    "legal_basis": "<sub-line-type-specific> · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 · applicable IAS/IFRS",
    "key_stats": [...],  # 8-12 trust-specific
    "notes": "3-5 sentences, 300-800 chars · trust-specific drivers + recent context",
    "sources": [...],  # 4-6 dicts {{publisher, title, url}} https://
    "related": [...]   # 3-6 cross-links (incl. parent line + relevant policy programme + peer trust)
}}
```

## Sub-line specific legal_basis (same as Acute slice 2)

- **Establishment costs**: GAM operating expenses · IAS 1 · NHS Act 2006
- **Transport (business + patient)**: NHS Act 2006 · NHSE Patient Transport Services Eligibility · AfC s.17 + AMAP · IFRS 16 (pool fleet)
- **General supplies & services**: GAM operating expenses · IAS 2 (interaction)
- **Business rates**: Local Government Finance Act 1988 (Sch 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024
- **Amortisation**: IAS 38 Intangible Assets · DHSC GAM ch.5
- **Lease expenditure**: IFRS 16 Leases · DHSC GAM ch.7 · Landlord and Tenant Act 1954
- **Social security & levy**: SSCBA 1992 · Health and Social Care Levy (repealed 2022, NIC reverted) · April 2025 employer NIC step-up to 15% / £5k threshold
- **Inventories written down**: IAS 2 · DHSC GAM
- **Termination & post-employment**: IAS 19 · NHS Pension Scheme regs · Public Sector Exit Payments Regs 2020
- **PFI / LIFT charges**: IFRIC 12 · IFRS 16 (post-2022) · DHSC PFI guidance
- **Drugs costs**: NHS Act 2006 (Drug Tariff) · Branded Medicines Pricing Scheme

## PROGRAMME dimensions per entry (must hit each)

1. **Delivery body**: trust dept (E&F · Procurement · Pharmacy · IT · Fleet) + external (NHSPS · NHS Supply Chain · Sodexo · Equans · OCS · Cerner / Oracle Health / Epic / SystemC)
2. **Policy owner**: NHSE Provider Finance / Specialised Commissioning · DHSC · NHS Resolution (CNST) · NHS Supply Chain · NHS Property Services
3. **Beneficiary count**: concrete N (sites · annual attendances or call-outs · referrals · WTE staff)
4. **Funding trajectory**: 3-5 year £ trend (industrial action backfill · IFRS 16 jump 2022 · Three Shifts policy · April 2025 NIC step-up)
5. **Evaluation evidence**: NAO reports · CQC inspections · NHSE Operational Plan returns · trust ARA · Model Hospital · ORH benchmarks (ambulance)
6. **Predecessor/successor**: prior contract · current vehicle · planned reform (e.g. Tavistock GIDS closure 2024 · Three Shifts community lift · ambulance fleet electrification)

## Hard rules
- Em-dash ` — ` (U+2014)
- Scoped alias parent = EXACT trust name from JSON
- `sources` MUST be list of dicts {{publisher, title, url}} https://
- 8-12 stats · 4-6 sources · 3-6 related · 3-5 sentence notes (300-800) · 3-5 sentence description (250-600)
- All 6 PROGRAMME dimensions present
- NO boilerplate placeholders
- Watchdog-safe incremental Edit (skeleton + per-entry inserts)

## Sub-lines in this cluster (sorted by £ desc, with category tag)

""", encoding='utf-8')
with brief_path.open('a', encoding='utf-8') as f:
    for r in all_orphans:
        f.write(f"### [{r['category']}] {r['sub_line']} — {r['trust']}\n  parent line: {r['parent_line']}\n  value: £{r['value']/1e6:.2f}M\n\n")

print(f'Wrote {brief_path}')

# Split into chunks of 17
CHUNK = 17
n_chunks = (len(all_orphans) + CHUNK - 1) // CHUNK
for i in range(0, len(all_orphans), CHUNK):
    chunk = all_orphans[i:i+CHUNK]
    label = f'phase2_scamb_chunk{(i//CHUNK)+1:02d}'
    p = Path(f'scripts/hand_curation_briefs/{label}.json')
    p.write_text(json.dumps(chunk, ensure_ascii=False, indent=2), encoding='utf-8')

print(f'Total chunks of {CHUNK}: {n_chunks}')
print(f'Wave 1 = chunks 1-4 (~{min(4*CHUNK, len(all_orphans))} entries)')
print(f'Wave 2 = chunks 5-8')
print(f'Wave 3 = chunks 9-12')
print(f'Wave 4 = chunks 13-16')
print(f'Wave 5 = chunks 17-{n_chunks}')
