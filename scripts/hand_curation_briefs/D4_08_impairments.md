# Cluster D4_08 Impairments net of reversals — NHS Trust depth-4

Scope: 125 NHS trust 'Impairments net of reversals' sub-lines · total £0.86B

## Archetype: PROGRAMME (per docs/archetype_briefs.md)

Required dimensions per entry: Delivery body · Policy owner · Beneficiary count · Funding trajectory · Evaluation evidence · Predecessor/successor

## What 'Impairments net of reversals' covers

Non-cash accounting writedowns of trust capital assets, primarily driven by:
- **Modern Equivalent Asset (MEA) revaluation** — annual DHSC valuation reassessment of NHS estate (5-year cycle for buildings, indexed via VOA in interim years). Negative deltas hit this line.
- **Net realisable value impairment** — when a building's market value drops below carrying value (e.g. listed-buildings becoming non-functional, RAAC-affected sites awaiting decant)
- **Reversals** — write-up if value recovers (rare for NHS estate)

Treatment per IAS 36 (Impairment of Assets) + DHSC Group Accounting Manual 2024-25 Chapter 4.

## Key 2024-25 context anchors

- **RAAC crisis impairments** — trusts with concrete-plank failures (HSSIB list Sep 2023) booked impairment when remedial cost > MEA-DRC value. Examples: Frimley Park, Whipps Cross, Hinchingbrooke, Royal Devon NDDH, Mid Cheshire, Princess Alexandra.
- **NHP Reset Jan 2025** — trusts in original NHP cohort had carrying values held against expected new build; Reset deferral triggered impairment review on existing structures (Imperial St Mary's, Leeds, Hull, Bedfordshire).
- **MEA-DRC revaluation cycle** — 5-yearly full revaluation due 2024-25 for many trusts (last full 2019-20). Indexation in interim years uses VOA. Results vary by region (London inflation higher than rural).
- **Listed-building constraints** — heritage estate (RUH Bath WHS, QVH McIndoe, Tavistock) often impaired when modernisation cost exceeds MEA.
- **Coastal salt-corrosion** — impairment risk at coastal trusts (Blackpool, Pilgrim Boston, Conquest, Eastbourne, Margate ESHT).

## Schema per entry (PROGRAMME contract floors)

```python
"Impairments net of reversals — <trust>": {
    "aliases": [{"name": "Impairments net of reversals", "parent": "<trust>"}],
    "description": "3-5 sentences, 250-600 chars · trust-specific impairment driver (RAAC / NHP / heritage / coastal / merger transition / specialty equipment)",
    "beneficiaries": "1-2 sentences · concrete N (sites with assets impaired, m² affected, replacement-vs-impair decision)",
    "legal_basis": "IAS 36 Impairment of Assets · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
    "key_stats": [...],  # 8-12 trust-specific (£ this year, 5-year trend, MEA-DRC vs market, RAAC scope, NHP status, valuation cycle phase, peer comparison)
    "notes": "3-5 sentences, 300-800 chars · trust-specific drivers + recent context (RAAC mitigation, NHP Reset deferral cost, valuation cycle, listed-building constraints)",
    "sources": [...],  # 4-6 dicts {publisher, title, url} https://
    "related": [...]   # 3-6 cross-links: trust + Premises (other) cross-ref + RAAC affected peers + NHP cohort + parent line
}
```

## PROGRAMME dimensions (must hit each entry)
1. **Delivery body**: trust Estates & Facilities · external valuer (often Cushman & Wakefield, JLL, GVA for NHS)
2. **Policy owner**: DHSC + NHSE Provider Finance · IAS 36 / DHSC GAM oversight
3. **Beneficiary count**: concrete N (assets impaired, m², replacement timeline)
4. **Funding trajectory**: 3-5 year impairment trend (volatile · spike years vs base years)
5. **Evaluation evidence**: NAO Estate report · HSSIB RAAC alert · CQC infrastructure findings · DHSC ARA disclosure
6. **Predecessor/successor**: prior valuation cycle outcome · current write-down · planned NHP rebuild or retain-and-refurbish

## Specialty mix per category
- **Acute** (~118 trusts in scope): biggest impairments by £ · multi-site MEA volatility · RAAC + NHP exposure
- **Specialist**: lower volume, but big impairments when single-site equipment becomes obsolete (PBT cyclotron, MRI replacement cycles)
- **Mental Health**: heritage + listed building impairments · forensic-secure perimeter constraints
- **Community**: smaller values · NHSPS-leased estate so impairments lower (NHSPS holds the asset)
- **Ambulance**: vehicle fleet impairments · station refresh cycle

## Category spread of this brief

- **NHS Acute Trusts**: 81 trusts
- **NHS Mental Health Trusts**: 16 trusts
- **NHS Community Trusts**: 13 trusts
- **NHS Specialist Trusts**: 8 trusts
- **NHS Ambulance Trusts**: 7 trusts

## Hard rules
- Em-dash ` — ` (U+2014)
- Scoped alias parent = EXACT trust name
- Sources = list of dicts with `https://` URLs
- 8-12 stats · 4-6 sources · 3-6 related · 3-5 sentence notes/desc
- All 6 PROGRAMME dimensions present
- Watchdog-safe incremental Edit (skeleton + per-entry inserts)

## Sub-lines in this cluster

### Impairments net of reversals — Worcestershire Acute Hospitals NHS Trust
  parent trust: Worcestershire Acute Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £28.60M

### Impairments net of reversals — Barts Health NHS Trust
  parent trust: Barts Health NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £26.17M

### Impairments net of reversals — Northern Care Alliance NHS Foundation Trust
  parent trust: Northern Care Alliance NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £25.86M

### Impairments net of reversals — South Tees Hospitals NHS Foundation Trust
  parent trust: South Tees Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £25.38M

### Impairments net of reversals — Maidstone And Tunbridge Wells NHS Trust
  parent trust: Maidstone And Tunbridge Wells NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £25.37M

### Impairments net of reversals — University Hospitals Coventry And Warwickshire NHS Trust
  parent trust: University Hospitals Coventry And Warwickshire NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £24.90M

### Impairments net of reversals — Nottingham University Hospitals NHS Trust
  parent trust: Nottingham University Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £23.90M

### Impairments net of reversals — Airedale NHS Foundation Trust
  parent trust: Airedale NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £22.61M

### Impairments net of reversals — King’s College Hospital NHS Foundation Trust
  parent trust: King’s College Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £21.13M

### Impairments net of reversals — James Paget University Hospitals NHS Foundation Trust
  parent trust: James Paget University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £20.89M

### Impairments net of reversals — East Lancashire Hospitals NHS Trust
  parent trust: East Lancashire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £19.39M

### Impairments net of reversals — Gloucestershire Hospitals NHS Foundation Trust
  parent trust: Gloucestershire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £19.19M

### Impairments net of reversals — Northern Lincolnshire and Goole NHS Foundation Trust
  parent trust: Northern Lincolnshire and Goole NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £17.63M

### Impairments net of reversals — Solent NHS Trust
  parent trust: Solent NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £16.54M

### Impairments net of reversals — South East Coast Ambulance Service NHS Foundation Trust
  parent trust: South East Coast Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £15.44M

### Impairments net of reversals — York and Scarborough Teaching Hospitals NHS Foundation Trust
  parent trust: York and Scarborough Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £15.11M

### Impairments net of reversals — The Dudley Group NHS Foundation Trust
  parent trust: The Dudley Group NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £15.03M

### Impairments net of reversals — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  parent trust: The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £15.02M

### Impairments net of reversals — Hull University Teaching Hospitals NHS Trust
  parent trust: Hull University Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £14.76M

### Impairments net of reversals — Dartford and Gravesham NHS Trust
  parent trust: Dartford and Gravesham NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £14.50M

### Impairments net of reversals — County Durham and Darlington NHS Foundation Trust
  parent trust: County Durham and Darlington NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £14.12M

### Impairments net of reversals — Blackpool Teaching Hospitals NHS Foundation Trust
  parent trust: Blackpool Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £12.70M

### Impairments net of reversals — University Hospitals of Morecambe Bay NHS Foundation Trust
  parent trust: University Hospitals of Morecambe Bay NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £12.67M

### Impairments net of reversals — Bedfordshire Hospitals NHS Foundation Trust
  parent trust: Bedfordshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £12.64M

### Impairments net of reversals — Alder Hey Children's NHS Foundation Trust
  parent trust: Alder Hey Children's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £12.39M

### Impairments net of reversals — University Hospitals of Leicester NHS Trust
  parent trust: University Hospitals of Leicester NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £12.22M

### Impairments net of reversals — The Royal Marsden NHS Foundation Trust
  parent trust: The Royal Marsden NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £11.74M

### Impairments net of reversals — Bradford Teaching Hospitals NHS Foundation Trust
  parent trust: Bradford Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £11.51M

### Impairments net of reversals — Liverpool Heart and Chest Hospital NHS Foundation Trust
  parent trust: Liverpool Heart and Chest Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £11.50M

### Impairments net of reversals — University Hospitals Plymouth NHS Trust
  parent trust: University Hospitals Plymouth NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £11.47M

### Impairments net of reversals — Bolton NHS Foundation Trust
  parent trust: Bolton NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £11.39M

### Impairments net of reversals — East Suffolk and North Essex NHS Foundation Trust
  parent trust: East Suffolk and North Essex NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £11.15M

### Impairments net of reversals — Wirral University Teaching Hospital NHS Foundation Trust
  parent trust: Wirral University Teaching Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £10.41M

### Impairments net of reversals — Derbyshire Community Health Services NHS Foundation Trust
  parent trust: Derbyshire Community Health Services NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £9.92M

### Impairments net of reversals — Royal Cornwall Hospitals NHS Trust
  parent trust: Royal Cornwall Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £9.65M

### Impairments net of reversals — Chesterfield Royal Hospital NHS Foundation Trust
  parent trust: Chesterfield Royal Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £9.38M

### Impairments net of reversals — Whittington Health NHS Trust
  parent trust: Whittington Health NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £9.26M

### Impairments net of reversals — South Tyneside and Sunderland NHS Foundation Trust
  parent trust: South Tyneside and Sunderland NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £8.94M

### Impairments net of reversals — Calderdale and Huddersfield NHS Foundation Trust
  parent trust: Calderdale and Huddersfield NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £8.74M

### Impairments net of reversals — Lewisham and Greenwich NHS Trust
  parent trust: Lewisham and Greenwich NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £8.63M

### Impairments net of reversals — North Bristol NHS Trust
  parent trust: North Bristol NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £8.41M

### Impairments net of reversals — University College London Hospitals NHS Foundation Trust
  parent trust: University College London Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £7.95M

### Impairments net of reversals — Sheffield Teaching Hospitals NHS Foundation Trust
  parent trust: Sheffield Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £7.91M

### Impairments net of reversals — Great Ormond Street Hospital for Children NHS Foundation Trust
  parent trust: Great Ormond Street Hospital for Children NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £7.81M

### Impairments net of reversals — Epsom and St Helier University Hospitals NHS Trust
  parent trust: Epsom and St Helier University Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £7.73M

### Impairments net of reversals — Sussex Community NHS Foundation Trust
  parent trust: Sussex Community NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £7.37M

### Impairments net of reversals — University Hospitals of North Midlands NHS Trust
  parent trust: University Hospitals of North Midlands NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £7.03M

### Impairments net of reversals — University Hospital Southampton NHS Foundation Trust
  parent trust: University Hospital Southampton NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £6.80M

### Impairments net of reversals — Kettering General Hospital NHS Foundation Trust
  parent trust: Kettering General Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £6.75M

### Impairments net of reversals — United Lincolnshire Hospitals NHS Trust
  parent trust: United Lincolnshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £6.58M

### Impairments net of reversals — Isle of Wight NHS Trust
  parent trust: Isle of Wight NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £6.44M

### Impairments net of reversals — North Tees and Hartlepool NHS Foundation Trust
  parent trust: North Tees and Hartlepool NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £6.14M

### Impairments net of reversals — Kingston Hospital NHS Foundation Trust
  parent trust: Kingston Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £5.92M

### Impairments net of reversals — Buckinghamshire Healthcare NHS Trust
  parent trust: Buckinghamshire Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £5.75M

### Impairments net of reversals — South Central Ambulance Service NHS Foundation Trust
  parent trust: South Central Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £5.56M

### Impairments net of reversals — East Sussex Healthcare NHS Trust
  parent trust: East Sussex Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £5.37M

### Impairments net of reversals — Wrightington, Wigan and Leigh NHS Foundation Trust
  parent trust: Wrightington, Wigan and Leigh NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £5.32M

### Impairments net of reversals — Royal Berkshire NHS Foundation Trust
  parent trust: Royal Berkshire NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £5.06M

### Impairments net of reversals — Hampshire Hospitals NHS Foundation Trust
  parent trust: Hampshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £4.52M

### Impairments net of reversals — Ashford and St Peter's Hospitals NHS Foundation Trust
  parent trust: Ashford and St Peter's Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £4.46M

### Impairments net of reversals — The Shrewsbury and Telford Hospital NHS Trust
  parent trust: The Shrewsbury and Telford Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £3.76M

### Impairments net of reversals — North West Ambulance Service NHS Trust
  parent trust: North West Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £3.66M

### Impairments net of reversals — Stockport NHS Foundation Trust
  parent trust: Stockport NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £3.41M

### Impairments net of reversals — London North West University Healthcare NHS Trust
  parent trust: London North West University Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £3.38M

### Impairments net of reversals — Surrey And Sussex Healthcare NHS Trust
  parent trust: Surrey And Sussex Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £3.36M

### Impairments net of reversals — East Cheshire NHS Trust
  parent trust: East Cheshire NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £3.34M

### Impairments net of reversals — Coventry and Warwickshire Partnership NHS Trust
  parent trust: Coventry and Warwickshire Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £3.29M

### Impairments net of reversals — Southern Health NHS Foundation Trust
  parent trust: Southern Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £3.29M

### Impairments net of reversals — Royal National Orthopaedic Hospital NHS Trust
  parent trust: Royal National Orthopaedic Hospital NHS Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £3.29M

### Impairments net of reversals — Royal Devon University Healthcare NHS Foundation Trust
  parent trust: Royal Devon University Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £3.08M

### Impairments net of reversals — Walsall Healthcare NHS Trust
  parent trust: Walsall Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.96M

### Impairments net of reversals — East And North Hertfordshire NHS Trust
  parent trust: East And North Hertfordshire NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.95M

### Impairments net of reversals — The Princess Alexandra Hospital NHS Trust
  parent trust: The Princess Alexandra Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.93M

### Impairments net of reversals — The Rotherham NHS Foundation Trust
  parent trust: The Rotherham NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.61M

### Impairments net of reversals — Leeds and York Partnership NHS Foundation Trust
  parent trust: Leeds and York Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £2.54M

### Impairments net of reversals — Harrogate and District NHS Foundation Trust
  parent trust: Harrogate and District NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.52M

### Impairments net of reversals — Sheffield Children's NHS Foundation Trust
  parent trust: Sheffield Children's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £2.50M

### Impairments net of reversals — Royal United Hospitals Bath NHS Foundation Trust
  parent trust: Royal United Hospitals Bath NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.50M

### Impairments net of reversals — The Hillingdon Hospitals NHS Foundation Trust
  parent trust: The Hillingdon Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.20M

### Impairments net of reversals — South London and Maudsley NHS Foundation Trust
  parent trust: South London and Maudsley NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £2.13M

### Impairments net of reversals — Dorset County Hospital NHS Foundation Trust
  parent trust: Dorset County Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.02M

### Impairments net of reversals — Royal Free London NHS Foundation Trust
  parent trust: Royal Free London NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.02M

### Impairments net of reversals — Northamptonshire Healthcare NHS Foundation Trust
  parent trust: Northamptonshire Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £2.00M

### Impairments net of reversals — Hertfordshire Partnership University NHS Foundation Trust
  parent trust: Hertfordshire Partnership University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £1.91M

### Impairments net of reversals — Barnsley Hospital NHS Foundation Trust
  parent trust: Barnsley Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £1.86M

### Impairments net of reversals — North East London NHS Foundation Trust
  parent trust: North East London NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £1.86M

### Impairments net of reversals — South Western Ambulance Service NHS Foundation Trust
  parent trust: South Western Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £1.86M

### Impairments net of reversals — South Warwickshire NHS Foundation Trust
  parent trust: South Warwickshire NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £1.82M

### Impairments net of reversals — Bradford District Care NHS Foundation Trust
  parent trust: Bradford District Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £1.81M

### Impairments net of reversals — North Middlesex University Hospital NHS Trust
  parent trust: North Middlesex University Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £1.76M

### Impairments net of reversals — Herefordshire and Worcestershire Health and Care NHS Trust
  parent trust: Herefordshire and Worcestershire Health and Care NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £1.74M

### Impairments net of reversals — University Hospitals of Derby and Burton NHS Foundation Trust
  parent trust: University Hospitals of Derby and Burton NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £1.66M

### Impairments net of reversals — Countess of Chester Hospital NHS Foundation Trust
  parent trust: Countess of Chester Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £1.50M

### Impairments net of reversals — Derbyshire Healthcare NHS Foundation Trust
  parent trust: Derbyshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £1.49M

### Impairments net of reversals — Wirral Community Health and Care NHS Foundation Trust
  parent trust: Wirral Community Health and Care NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £1.46M

### Impairments net of reversals — Birmingham Community Healthcare NHS Foundation Trust
  parent trust: Birmingham Community Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £1.43M

### Impairments net of reversals — Portsmouth Hospitals University NHS Trust
  parent trust: Portsmouth Hospitals University NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £1.32M

### Impairments net of reversals — North East Ambulance Service NHS Foundation Trust
  parent trust: North East Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £1.31M

### Impairments net of reversals — Cornwall Partnership NHS Foundation Trust
  parent trust: Cornwall Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £1.13M

### Impairments net of reversals — Great Western Hospitals NHS Foundation Trust
  parent trust: Great Western Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £1.08M

### Impairments net of reversals — Barnet, Enfield And Haringey Mental Health NHS Trust
  parent trust: Barnet, Enfield And Haringey Mental Health NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £0.99M

### Impairments net of reversals — Nottinghamshire Healthcare NHS Foundation Trust
  parent trust: Nottinghamshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £0.92M

### Impairments net of reversals — Sherwood Forest Hospitals NHS Foundation Trust
  parent trust: Sherwood Forest Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £0.85M

### Impairments net of reversals — Bridgewater Community Healthcare NHS Foundation Trust
  parent trust: Bridgewater Community Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £0.79M

### Impairments net of reversals — East Midlands Ambulance Service NHS Trust
  parent trust: East Midlands Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £0.78M

### Impairments net of reversals — London Ambulance Service NHS Trust
  parent trust: London Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £0.68M

### Impairments net of reversals — Salisbury NHS Foundation Trust
  parent trust: Salisbury NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £0.67M

### Impairments net of reversals — Gateshead Health NHS Foundation Trust
  parent trust: Gateshead Health NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £0.67M

### Impairments net of reversals — Devon Partnership NHS Trust
  parent trust: Devon Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £0.56M

### Impairments net of reversals — Birmingham and Solihull Mental Health NHS Foundation Trust
  parent trust: Birmingham and Solihull Mental Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £0.54M

### Impairments net of reversals — Queen Victoria Hospital NHS Foundation Trust
  parent trust: Queen Victoria Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £0.51M

### Impairments net of reversals — Shropshire Community Health NHS Trust
  parent trust: Shropshire Community Health NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £0.50M

### Impairments net of reversals — George Eliot Hospital NHS Trust
  parent trust: George Eliot Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £0.48M

### Impairments net of reversals — The Royal Wolverhampton NHS Trust
  parent trust: The Royal Wolverhampton NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £0.43M

### Impairments net of reversals — Tameside and Glossop Integrated Care NHS Foundation Trust
  parent trust: Tameside and Glossop Integrated Care NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £0.42M

### Impairments net of reversals — Kent Community Health NHS Foundation Trust
  parent trust: Kent Community Health NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £0.39M

### Impairments net of reversals — The Royal Orthopaedic Hospital NHS Foundation Trust
  parent trust: The Royal Orthopaedic Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £0.35M

### Impairments net of reversals — Gloucestershire Health and Care NHS Foundation Trust
  parent trust: Gloucestershire Health and Care NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £0.28M

### Impairments net of reversals — Norfolk Community Health and Care NHS Trust
  parent trust: Norfolk Community Health and Care NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £0.26M

### Impairments net of reversals — Cheshire and Wirral Partnership NHS Foundation Trust
  parent trust: Cheshire and Wirral Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £0.24M

### Impairments net of reversals — Hertfordshire Community NHS Trust
  parent trust: Hertfordshire Community NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £0.23M

### Impairments net of reversals — Dorset Healthcare University NHS Foundation Trust
  parent trust: Dorset Healthcare University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £0.21M

### Impairments net of reversals — Medway NHS Foundation Trust
  parent trust: Medway NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £0.17M

### Impairments net of reversals — Royal Surrey NHS Foundation Trust
  parent trust: Royal Surrey NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £0.11M

### Impairments net of reversals — Dudley Integrated Health and Care NHS Trust
  parent trust: Dudley Integrated Health and Care NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £0.10M

