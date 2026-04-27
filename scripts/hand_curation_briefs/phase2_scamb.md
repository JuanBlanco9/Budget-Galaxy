# Cluster Phase2_SCamb — NHS Specialist + Community + Ambulance Trust orphan sub-lines

Scope: 307 orphan depth-5 sub-lines under NHS Specialist (100), Community (130), Ambulance (77) Trusts · total £1.61B

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
"<sub-line> — <trust>": {
    "aliases": [{"name": "<sub-line>", "parent": "<trust>"}],
    "description": "3-5 sentences, 250-600 chars · trust-specific (sub-line driver + trust specialty mix)",
    "beneficiaries": "1-2 sentences with CONCRETE N (sites · referral catchment · WTE)",
    "legal_basis": "<sub-line-type-specific> · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 · applicable IAS/IFRS",
    "key_stats": [...],  # 8-12 trust-specific
    "notes": "3-5 sentences, 300-800 chars · trust-specific drivers + recent context",
    "sources": [...],  # 4-6 dicts {publisher, title, url} https://
    "related": [...]   # 3-6 cross-links (incl. parent line + relevant policy programme + peer trust)
}
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
- `sources` MUST be list of dicts {publisher, title, url} https://
- 8-12 stats · 4-6 sources · 3-6 related · 3-5 sentence notes (300-800) · 3-5 sentence description (250-600)
- All 6 PROGRAMME dimensions present
- NO boilerplate placeholders
- Watchdog-safe incremental Edit (skeleton + per-entry inserts)

## Sub-lines in this cluster (sorted by £ desc, with category tag)

### [Ambulance] Transport (business + patient) — North West Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £59.19M

### [Ambulance] Transport (business + patient) — South Western Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £53.66M

### [Ambulance] Social security & levy — London Ambulance Service NHS Trust
  parent line: Staff Costs
  value: £46.84M

### [Ambulance] Transport (business + patient) — East of England Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £45.29M

### [Ambulance] General supplies & services — London Ambulance Service NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £42.19M

### [Community] General supplies & services — Central London Community Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £36.92M

### [Ambulance] Transport (business + patient) — East Midlands Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £34.79M

### [Ambulance] Transport (business + patient) — Yorkshire Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £28.11M

### [Ambulance] Transport (business + patient) — West Midlands Ambulance Service University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £27.51M

### [Ambulance] Social security & levy — Yorkshire Ambulance Service NHS Trust
  parent line: Staff Costs
  value: £25.91M

### [Ambulance] Social security & levy — West Midlands Ambulance Service University NHS Foundation Trust
  parent line: Staff Costs
  value: £25.80M

### [Community] Social security & levy — Central London Community Healthcare NHS Trust
  parent line: Staff Costs
  value: £25.70M

### [Ambulance] Social security & levy — South Western Ambulance Service NHS Foundation Trust
  parent line: Staff Costs
  value: £24.02M

### [Ambulance] Transport (business + patient) — London Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £22.60M

### [Community] Social security & levy — Birmingham Community Healthcare NHS Foundation Trust
  parent line: Staff Costs
  value: £21.15M

### [Community] Social security & levy — Northamptonshire Healthcare NHS Foundation Trust
  parent line: Staff Costs
  value: £20.59M

### [Ambulance] Social security & levy — South East Coast Ambulance Service NHS Foundation Trust
  parent line: Staff Costs
  value: £20.48M

### [Community] Social security & levy — Sussex Community NHS Foundation Trust
  parent line: Staff Costs
  value: £20.23M

### [Specialist] Social security & levy — Alder Hey Children's NHS Foundation Trust
  parent line: Staff Costs
  value: £20.11M

### [Ambulance] Social security & levy — South Central Ambulance Service NHS Foundation Trust
  parent line: Staff Costs
  value: £18.83M

### [Ambulance] Social security & levy — East Midlands Ambulance Service NHS Trust
  parent line: Staff Costs
  value: £18.30M

### [Ambulance] Transport (business + patient) — South Central Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £18.11M

### [Community] Social security & levy — Gloucestershire Health and Care NHS Foundation Trust
  parent line: Staff Costs
  value: £18.03M

### [Community] Social security & levy — Kent Community Health NHS Foundation Trust
  parent line: Staff Costs
  value: £17.99M

### [Specialist] Social security & levy — Sheffield Children's NHS Foundation Trust
  parent line: Staff Costs
  value: £17.85M

### [Community] Lease expenditure — Central London Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £17.73M

### [Specialist] Social security & levy — The Christie NHS Foundation Trust
  parent line: Staff Costs
  value: £17.66M

### [Ambulance] Transport (business + patient) — South East Coast Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £16.70M

### [Specialist] General supplies & services — Moorfields Eye Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £16.59M

### [Community] Social security & levy — Herefordshire and Worcestershire Health and Care NHS Trust
  parent line: Staff Costs
  value: £16.47M

### [Community] Social security & levy — Solent NHS Trust
  parent line: Staff Costs
  value: £16.34M

### [Ambulance] Transport (business + patient) — North East Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £14.73M

### [Ambulance] Establishment costs — London Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £14.51M

### [Specialist] Social security & levy — Moorfields Eye Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £14.22M

### [Community] General supplies & services — Norfolk Community Health and Care NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £13.89M

### [Community] Social security & levy — Derbyshire Community Health Services NHS Foundation Trust
  parent line: Staff Costs
  value: £13.64M

### [Community] Social security & levy — Leeds Community Healthcare NHS Trust
  parent line: Staff Costs
  value: £13.29M

### [Ambulance] Social security & levy — North East Ambulance Service NHS Foundation Trust
  parent line: Staff Costs
  value: £12.93M

### [Ambulance] Establishment costs — North West Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £12.82M

### [Specialist] Social security & levy — Royal Papworth Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £11.89M

### [Ambulance] Establishment costs — East of England Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £11.62M

### [Specialist] General supplies & services — The Royal Marsden NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £11.58M

### [Community] Social security & levy — Cambridgeshire Community Services NHS Trust
  parent line: Staff Costs
  value: £10.25M

### [Specialist] Social security & levy — Royal National Orthopaedic Hospital NHS Trust
  parent line: Staff Costs
  value: £10.21M

### [Community] Establishment costs — Kent Community Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £10.12M

### [Specialist] General supplies & services — The Christie NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £9.98M

### [Specialist] General supplies & services — Liverpool Heart and Chest Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £9.81M

### [Specialist] Establishment costs — The Christie NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £9.68M

### [Specialist] PFI / LIFT charges — Royal Papworth Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £9.67M

### [Specialist] Social security & levy — Liverpool Heart and Chest Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £9.50M

### [Specialist] General supplies & services — Royal National Orthopaedic Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £9.42M

### [Community] Social security & levy — Norfolk Community Health and Care NHS Trust
  parent line: Staff Costs
  value: £9.32M

### [Specialist] Establishment costs — Moorfields Eye Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £8.88M

### [Community] Social security & levy — Lincolnshire Community Health Services NHS Trust
  parent line: Staff Costs
  value: £8.77M

### [Specialist] Social security & levy — The Clatterbridge Cancer Centre NHS Foundation Trust
  parent line: Staff Costs
  value: £8.71M

### [Specialist] Social security & levy — Liverpool Women's NHS Foundation Trust
  parent line: Staff Costs
  value: £8.56M

### [Specialist] General supplies & services — Great Ormond Street Hospital for Children NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £8.51M

### [Community] Social security & levy — Hertfordshire Community NHS Trust
  parent line: Staff Costs
  value: £8.39M

### [Ambulance] Establishment costs — North East Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £8.26M

### [Specialist] Social security & levy — The Walton Centre NHS Foundation Trust
  parent line: Staff Costs
  value: £7.90M

### [Ambulance] Establishment costs — East Midlands Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £7.73M

### [Specialist] Social security & levy — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £7.67M

### [Ambulance] Lease expenditure — South Central Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.61M

### [Community] General supplies & services — Leeds Community Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £7.28M

### [Community] Establishment costs — Herefordshire and Worcestershire Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £7.13M

### [Ambulance] Establishment costs — West Midlands Ambulance Service University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.01M

### [Community] General supplies & services — Hertfordshire Community NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £7.00M

### [Community] Social security & levy — Hounslow and Richmond Community Healthcare NHS Trust
  parent line: Staff Costs
  value: £6.28M

### [Community] Social security & levy — Wirral Community Health and Care NHS Foundation Trust
  parent line: Staff Costs
  value: £6.18M

### [Ambulance] Establishment costs — South East Coast Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.04M

### [Specialist] Social security & levy — The Royal Orthopaedic Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £5.99M

### [Specialist] Social security & levy — Queen Victoria Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £5.97M

### [Specialist] Transport (business + patient) — Great Ormond Street Hospital for Children NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.85M

### [Ambulance] Establishment costs — South Central Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.70M

### [Community] General supplies & services — Birmingham Community Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £5.64M

### [Ambulance] Lease expenditure — West Midlands Ambulance Service University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.61M

### [Community] Social security & levy — Shropshire Community Health NHS Trust
  parent line: Staff Costs
  value: £5.60M

### [Community] General supplies & services — Lincolnshire Community Health Services NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £5.53M

### [Community] Social security & levy — Bridgewater Community Healthcare NHS Foundation Trust
  parent line: Staff Costs
  value: £5.45M

### [Community] Establishment costs — Hertfordshire Community NHS Trust
  parent line: Premises & Infrastructure
  value: £5.38M

### [Specialist] PFI / LIFT charges — Alder Hey Children's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.10M

### [Ambulance] Establishment costs — Yorkshire Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £4.90M

### [Specialist] Business rates — Great Ormond Street Hospital for Children NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.69M

### [Community] Transport (business + patient) — Kent Community Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.50M

### [Specialist] General supplies & services — The Clatterbridge Cancer Centre NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.49M

### [Community] Termination & post-employment — Derbyshire Community Health Services NHS Foundation Trust
  parent line: Staff Costs
  value: £4.47M

### [Specialist] Establishment costs — The Royal Marsden NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.36M

### [Specialist] General supplies & services — The Walton Centre NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.34M

### [Community] Establishment costs — Gloucestershire Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.34M

### [Specialist] Transport (business + patient) — Royal National Orthopaedic Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £4.31M

### [Specialist] Amortisation — Alder Hey Children's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.24M

### [Community] General supplies & services — Gloucestershire Health and Care NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.22M

### [Ambulance] General supplies & services — East of England Ambulance Service NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £4.19M

### [Specialist] Establishment costs — Great Ormond Street Hospital for Children NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.18M

### [Specialist] General supplies & services — Liverpool Women's NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.14M

### [Ambulance] Establishment costs — South Western Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.03M

### [Specialist] Amortisation — Great Ormond Street Hospital for Children NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.03M

### [Community] General supplies & services — Herefordshire and Worcestershire Health and Care NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £3.94M

### [Ambulance] General supplies & services — South East Coast Ambulance Service NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £3.93M

### [Community] Transport (business + patient) — Northamptonshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.92M

### [Specialist] Amortisation — The Royal Marsden NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.87M

### [Community] Transport (business + patient) — Derbyshire Community Health Services NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.85M

### [Community] Establishment costs — Leeds Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £3.76M

### [Ambulance] General supplies & services — West Midlands Ambulance Service University NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £3.67M

### [Specialist] Business rates — The Royal Marsden NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.59M

### [Community] Establishment costs — Bridgewater Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.53M

### [Community] Establishment costs — Solent NHS Trust
  parent line: Premises & Infrastructure
  value: £3.52M

### [Community] Transport (business + patient) — Sussex Community NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.50M

### [Specialist] Transport (business + patient) — The Royal Marsden NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.47M

### [Specialist] Business rates — Alder Hey Children's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.42M

### [Ambulance] General supplies & services — North East Ambulance Service NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £3.40M

### [Specialist] Transport (business + patient) — Moorfields Eye Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.34M

### [Community] Establishment costs — Birmingham Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.33M

### [Ambulance] General supplies & services — North West Ambulance Service NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £3.31M

### [Ambulance] Business rates — London Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £3.28M

### [Community] Amortisation — Central London Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £3.22M

### [Community] General supplies & services — Derbyshire Community Health Services NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £3.13M

### [Community] Transport (business + patient) — Gloucestershire Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.97M

### [Community] General supplies & services — Sussex Community NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.96M

### [Community] General supplies & services — Northamptonshire Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.96M

### [Community] Establishment costs — Shropshire Community Health NHS Trust
  parent line: Premises & Infrastructure
  value: £2.95M

### [Community] Establishment costs — Central London Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £2.94M

### [Community] Transport (business + patient) — Lincolnshire Community Health Services NHS Trust
  parent line: Premises & Infrastructure
  value: £2.93M

### [Specialist] General supplies & services — Sheffield Children's NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.86M

### [Community] General supplies & services — Cambridgeshire Community Services NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £2.83M

### [Community] Transport (business + patient) — Solent NHS Trust
  parent line: Premises & Infrastructure
  value: £2.80M

### [Ambulance] General supplies & services — South Western Ambulance Service NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.79M

### [Community] Establishment costs — Sussex Community NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.78M

### [Community] Amortisation — Sussex Community NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.78M

### [Community] Transport (business + patient) — Birmingham Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.74M

### [Community] Transport (business + patient) — Herefordshire and Worcestershire Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £2.74M

### [Community] Establishment costs — Northamptonshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.68M

### [Community] Establishment costs — Cambridgeshire Community Services NHS Trust
  parent line: Premises & Infrastructure
  value: £2.64M

### [Ambulance] Amortisation — London Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £2.62M

### [Community] General supplies & services — Solent NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £2.59M

### [Specialist] Establishment costs — Alder Hey Children's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.44M

### [Community] Transport (business + patient) — Norfolk Community Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £2.37M

### [Ambulance] Business rates — South East Coast Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.36M

### [Specialist] General supplies & services — Alder Hey Children's NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.28M

### [Specialist] General supplies & services — Royal Papworth Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.26M

### [Specialist] General supplies & services — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.26M

### [Community] General supplies & services — Wirral Community Health and Care NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.20M

### [Community] Establishment costs — Hounslow and Richmond Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £2.17M

### [Ambulance] Lease expenditure — Yorkshire Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £2.14M

### [Ambulance] Lease expenditure — London Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £2.12M

### [Specialist] Business rates — Royal Papworth Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.12M

### [Ambulance] General supplies & services — South Central Ambulance Service NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.11M

### [Ambulance] Business rates — North West Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £2.11M

### [Specialist] Establishment costs — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.09M

### [Community] Establishment costs — Wirral Community Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.04M

### [Community] Transport (business + patient) — Leeds Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £2.04M

### [Community] Amortisation — Herefordshire and Worcestershire Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £1.98M

### [Ambulance] Amortisation — East of England Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £1.98M

### [Specialist] Establishment costs — Royal Papworth Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.96M

### [Community] Transport (business + patient) — Cambridgeshire Community Services NHS Trust
  parent line: Premises & Infrastructure
  value: £1.95M

### [Community] PFI / LIFT charges — Northamptonshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.90M

### [Specialist] Establishment costs — Sheffield Children's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.85M

### [Community] Establishment costs — Derbyshire Community Health Services NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.84M

### [Specialist] Establishment costs — Liverpool Heart and Chest Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.83M

### [Community] Business rates — Gloucestershire Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.80M

### [Ambulance] Lease expenditure — South East Coast Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.76M

### [Ambulance] General supplies & services — Yorkshire Ambulance Service NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £1.75M

### [Ambulance] Business rates — East of England Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £1.73M

### [Specialist] Establishment costs — Royal National Orthopaedic Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £1.72M

### [Ambulance] Business rates — South Western Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.72M

### [Community] Amortisation — Kent Community Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.69M

### [Ambulance] General supplies & services — East Midlands Ambulance Service NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £1.68M

### [Specialist] Amortisation — The Clatterbridge Cancer Centre NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.68M

### [Ambulance] Amortisation — South East Coast Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.67M

### [Ambulance] Business rates — South Central Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.65M

### [Specialist] Establishment costs — The Walton Centre NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.65M

### [Community] Transport (business + patient) — Hertfordshire Community NHS Trust
  parent line: Premises & Infrastructure
  value: £1.63M

### [Community] General supplies & services — Kent Community Health NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.62M

### [Specialist] Establishment costs — The Royal Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.57M

### [Specialist] Business rates — The Clatterbridge Cancer Centre NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.52M

### [Specialist] Establishment costs — The Clatterbridge Cancer Centre NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.44M

### [Community] Business rates — Sussex Community NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.43M

### [Ambulance] Business rates — West Midlands Ambulance Service University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.38M

### [Specialist] Business rates — Moorfields Eye Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.37M

### [Community] Business rates — Cambridgeshire Community Services NHS Trust
  parent line: Premises & Infrastructure
  value: £1.34M

### [Community] Business rates — Herefordshire and Worcestershire Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £1.31M

### [Specialist] Lease expenditure — Great Ormond Street Hospital for Children NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.30M

### [Specialist] Establishment costs — Queen Victoria Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.30M

### [Specialist] Lease expenditure — The Royal Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.29M

### [Specialist] Establishment costs — Liverpool Women's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.29M

### [Community] Business rates — Solent NHS Trust
  parent line: Premises & Infrastructure
  value: £1.22M

### [Specialist] Business rates — The Christie NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.21M

### [Specialist] Transport (business + patient) — The Christie NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.20M

### [Community] Business rates — Derbyshire Community Health Services NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.11M

### [Specialist] Amortisation — Moorfields Eye Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.08M

### [Community] Establishment costs — Lincolnshire Community Health Services NHS Trust
  parent line: Premises & Infrastructure
  value: £1.07M

### [Specialist] Transport (business + patient) — Liverpool Heart and Chest Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.05M

### [Community] Business rates — Hertfordshire Community NHS Trust
  parent line: Premises & Infrastructure
  value: £1.04M

### [Ambulance] Amortisation — Yorkshire Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £1.02M

### [Specialist] General supplies & services — The Royal Orthopaedic Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.02M

### [Specialist] General supplies & services — Queen Victoria Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.01M

### [Community] Drugs costs — Leeds Community Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.99M

### [Ambulance] Drugs costs — West Midlands Ambulance Service University NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.98M

### [Specialist] Amortisation — Liverpool Women's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.98M

### [Community] Establishment costs — Norfolk Community Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £0.98M

### [Community] Transport (business + patient) — Central London Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.98M

### [Ambulance] Business rates — East Midlands Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £0.98M

### [Community] Business rates — Wirral Community Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.98M

### [Community] Drugs costs — Norfolk Community Health and Care NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.97M

### [Specialist] Business rates — Royal National Orthopaedic Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.96M

### [Ambulance] Drugs costs — London Ambulance Service NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.95M

### [Community] Business rates — Kent Community Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.94M

### [Community] PFI / LIFT charges — Birmingham Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.94M

### [Community] Business rates — Central London Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.91M

### [Specialist] Business rates — Sheffield Children's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.90M

### [Community] Lease expenditure — Herefordshire and Worcestershire Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £0.90M

### [Specialist] Amortisation — Queen Victoria Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.89M

### [Community] Business rates — Norfolk Community Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £0.89M

### [Community] Drugs costs — Hertfordshire Community NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.88M

### [Ambulance] Lease expenditure — East of England Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £0.87M

### [Community] Business rates — Northamptonshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.86M

### [Community] Lease expenditure — Kent Community Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.85M

### [Ambulance] Lease expenditure — East Midlands Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £0.83M

### [Specialist] Business rates — The Walton Centre NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.82M

### [Community] Business rates — Birmingham Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.82M

### [Ambulance] Business rates — Yorkshire Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £0.80M

### [Specialist] Amortisation — Royal Papworth Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.76M

### [Community] Lease expenditure — Leeds Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.75M

### [Specialist] Transport (business + patient) — Royal Papworth Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.75M

### [Specialist] Transport (business + patient) — Alder Hey Children's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.75M

### [Ambulance] Amortisation — North West Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £0.73M

### [Community] Amortisation — Solent NHS Trust
  parent line: Premises & Infrastructure
  value: £0.73M

### [Community] General supplies & services — Shropshire Community Health NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.72M

### [Community] Drugs costs — Wirral Community Health and Care NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.72M

### [Community] Lease expenditure — Northamptonshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.71M

### [Ambulance] Lease expenditure — North West Ambulance Service NHS Trust
  parent line: Premises & Infrastructure
  value: £0.70M

### [Community] General supplies & services — Hounslow and Richmond Community Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.70M

### [Ambulance] Business rates — North East Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.66M

### [Specialist] Business rates — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.65M

### [Specialist] Transport (business + patient) — Sheffield Children's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.63M

### [Ambulance] Lease expenditure — North East Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.62M

### [Ambulance] Lease expenditure — South Western Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.59M

### [Ambulance] Drugs costs — South Western Ambulance Service NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.58M

### [Ambulance] Drugs costs — East Midlands Ambulance Service NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.57M

### [Specialist] Transport (business + patient) — The Walton Centre NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.57M

### [Ambulance] Drugs costs — North East Ambulance Service NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.57M

### [Community] Amortisation — Birmingham Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.56M

### [Community] Lease expenditure — Norfolk Community Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £0.56M

### [Specialist] Lease expenditure — Moorfields Eye Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.55M

### [Community] Amortisation — Northamptonshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.55M

### [Ambulance] Amortisation — South Central Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.53M

### [Community] Amortisation — Derbyshire Community Health Services NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.52M

### [Community] Business rates — Hounslow and Richmond Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.52M

### [Community] Amortisation — Bridgewater Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.50M

### [Community] Lease expenditure — Lincolnshire Community Health Services NHS Trust
  parent line: Premises & Infrastructure
  value: £0.47M

### [Specialist] Business rates — Liverpool Women's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.47M

### [Community] Lease expenditure — Wirral Community Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.46M

### [Ambulance] Amortisation — West Midlands Ambulance Service University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.46M

### [Specialist] Inventories written down — Great Ormond Street Hospital for Children NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.46M

### [Specialist] Business rates — Liverpool Heart and Chest Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.44M

### [Community] General supplies & services — Bridgewater Community Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.44M

### [Specialist] Lease expenditure — Liverpool Women's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.43M

### [Community] Amortisation — Gloucestershire Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.40M

### [Community] Drugs costs — Hounslow and Richmond Community Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.39M

### [Specialist] Amortisation — The Royal Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.38M

### [Specialist] Business rates — The Royal Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.37M

### [Ambulance] Amortisation — North East Ambulance Service NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.37M

### [Community] Business rates — Leeds Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.37M

### [Community] Termination & post-employment — Kent Community Health NHS Foundation Trust
  parent line: Staff Costs
  value: £0.36M

### [Community] Lease expenditure — Birmingham Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.36M

### [Ambulance] Drugs costs — Yorkshire Ambulance Service NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.35M

### [Specialist] Transport (business + patient) — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.35M

### [Specialist] Amortisation — Sheffield Children's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.34M

### [Specialist] Business rates — Queen Victoria Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.34M

### [Specialist] Transport (business + patient) — The Clatterbridge Cancer Centre NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.34M

### [Ambulance] Drugs costs — South Central Ambulance Service NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.33M

### [Ambulance] Termination & post-employment — Yorkshire Ambulance Service NHS Trust
  parent line: Staff Costs
  value: £0.33M

### [Specialist] Amortisation — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.32M

### [Community] Lease expenditure — Derbyshire Community Health Services NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.32M

### [Community] Lease expenditure — Hertfordshire Community NHS Trust
  parent line: Premises & Infrastructure
  value: £0.32M

### [Community] Transport (business + patient) — Hounslow and Richmond Community Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.32M

### [Community] Business rates — Bridgewater Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.29M

### [Specialist] Transport (business + patient) — Queen Victoria Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.29M

### [Community] Transport (business + patient) — Bridgewater Community Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.29M

### [Community] Amortisation — Norfolk Community Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £0.29M

### [Specialist] Amortisation — The Walton Centre NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.27M

### [Specialist] Lease expenditure — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.27M

### [Ambulance] Termination & post-employment — London Ambulance Service NHS Trust
  parent line: Staff Costs
  value: £0.27M

### [Community] Lease expenditure — Gloucestershire Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.26M

### [Specialist] Transport (business + patient) — Liverpool Women's NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.25M

### [Community] Termination & post-employment — Norfolk Community Health and Care NHS Trust
  parent line: Staff Costs
  value: £0.25M

### [Community] Business rates — Shropshire Community Health NHS Trust
  parent line: Premises & Infrastructure
  value: £0.24M

### [Specialist] Other & adjustments — The Royal Orthopaedic Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £0.23M

### [Community] Business rates — Lincolnshire Community Health Services NHS Trust
  parent line: Premises & Infrastructure
  value: £0.23M

### [Specialist] Lease expenditure — The Walton Centre NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.19M

### [Community] Amortisation — Lincolnshire Community Health Services NHS Trust
  parent line: Premises & Infrastructure
  value: £0.19M

### [Community] PFI / LIFT charges — Sussex Community NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.18M

### [Community] Transport (business + patient) — Wirral Community Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.18M

### [Specialist] Inventories written down — Royal National Orthopaedic Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.17M

### [Community] Amortisation — Hertfordshire Community NHS Trust
  parent line: Premises & Infrastructure
  value: £0.17M

### [Specialist] Inventories written down — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.16M

### [Specialist] Other & adjustments — The Clatterbridge Cancer Centre NHS Foundation Trust
  parent line: Staff Costs
  value: £0.16M

### [Specialist] Termination & post-employment — The Walton Centre NHS Foundation Trust
  parent line: Staff Costs
  value: £0.15M

### [Specialist] Amortisation — The Christie NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.15M

### [Ambulance] Inventories written down — South Western Ambulance Service NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.15M

### [Ambulance] Other & adjustments — South Western Ambulance Service NHS Foundation Trust
  parent line: Staff Costs
  value: £0.14M

### [Community] Amortisation — Wirral Community Health and Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.14M

### [Community] Other & adjustments — Cambridgeshire Community Services NHS Trust
  parent line: Staff Costs
  value: £0.14M

### [Community] Other & adjustments — Central London Community Healthcare NHS Trust
  parent line: Staff Costs
  value: £0.13M

### [Community] Other & adjustments — Bridgewater Community Healthcare NHS Foundation Trust
  parent line: Staff Costs
  value: £0.12M

### [Specialist] Transport (business + patient) — The Royal Orthopaedic Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.12M

### [Community] Lease expenditure — Shropshire Community Health NHS Trust
  parent line: Premises & Infrastructure
  value: £0.11M

