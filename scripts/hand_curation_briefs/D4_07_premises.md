# Cluster D4_07 Premises (other) — NHS Trust depth-5 sub-lines

Scope: 206 NHS trust 'Premises (other)' sub-lines · total £4.63B

## What 'Premises (other)' covers

Every NHS provider trust has a 'Premises' line in its accounts capturing estate
operating costs OUTSIDE the depreciation/amortisation lines. 'Premises (other)'
is the residual within Premises — building maintenance, hard FM contracts,
soft FM (cleaning, catering insourced), grounds maintenance, water + sewerage,
refuse, fire safety contracts, security, pest control, parking management,
sustainability/Net Zero retrofit operational costs.

## Key 2024-25 context anchors

- **NHS Net Zero (DHSC)** target for direct emissions 2040 has driven LED
  retrofit, heat-pump installations, BMS upgrades — visible in Premises (other)
  for trusts mid-program.
- **RAAC concrete crisis** (Reinforced Autoclaved Aerated Concrete): 27 trusts
  affected per HSSIB Sep 2023, with Premises (other) inflated by mitigation
  works (props, decant, monitoring).
- **NHP (New Hospital Programme) Reset** announced 20 Jan 2025 by Streeting:
  some trusts had budgeted for new builds, now decant/temporary works extending.
- **Industrial action 2023-24** had MINOR Premises (other) impact (security
  + extra catering for picket-line management).
- **PFI unitary charges are NOT in Premises (other)** — separate D4_11 line.
- **Business rates are NOT in Premises (other)** — separate D4_13 line.
- **Energy contracts (NHS Crown Commercial Service)** — most trusts on RM6011
  framework; price spikes 2022-23 partial pass-through to 2024-25 budgets.
- **Construction inflation 2024-25** ~5-7% on hard FM contracts.

## Specialty mix anchors by category

- **Acute Trusts** (~75% of clusters here): multi-site means heavier estate
  load — large hospitals + community sites + ambulances + warehouses.
- **Specialist** (cancer / cardiac / orthopaedic): single-site typically,
  but specialty equipment power demands inflate utilities.
- **Mental Health**: section 136 suites + PICU + ECT room conditions key;
  RAAC affected several MH estates (Edenfield, Tees Esk).
- **Community**: clinic estate + some inpatient (community hospitals).
- **Ambulance**: ambulance stations, HART bases, training centres,
  vehicle workshops + fuel costs.

## Schema per entry

```python
"Premises (other) — <trust>": {
    "aliases": [{"name": "Premises (other)", "parent": "<trust>"}],
    "description": "2-3 sentences trust-specific (estate footprint, key sites, hard/soft FM contract holder, sustainability stage)",
    "beneficiaries": "Patients + staff at trust sites — be specific (5 hospitals · X ambulance stations · Y community clinics)",
    "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
    "key_stats": [
        {"label": "Premises (other) 2024-25", "value": "£<exact from brief>M"},
        {"label": "Share of trust total opex", "value": "c. X%"},
        {"label": "Estate scale", "value": "e.g. '5 hospital sites + 12 community sites · X m² floorspace'"},
        {"label": "Hard FM contract", "value": "Holder + contract end date if known"},
        {"label": "Soft FM model", "value": "Insourced/outsourced + provider"},
        {"label": "RAAC status", "value": "if applicable"},
        {"label": "NHP scheme status", "value": "if applicable"},
        {"label": "Net Zero milestone", "value": "e.g. 'BMS upgrade 60% complete'"},
        {"label": "YoY change", "value": "c. +X% (driver)"},
        {"label": "Peer benchmark", "value": "vs trust-category median"}
    ],  # 6-10 trust-specific
    "notes": "2-4 sentences trust-specific drivers (estate consolidation, RAAC mitigation, energy contract renewals, FM contract bidding cycles, decarbonisation grant funding)",
    "sources": [...],  # 2-3 with https:// URLs (trust AR, NHS ERIC, NHSE provider finance, CQC inspection)
    "related": ["<trust>", "<parent line>"]
}
```

## Category spread of this brief

- **NHS Acute Trusts**: 118 trusts
- **NHS Mental Health Trusts**: 45 trusts
- **NHS Community Trusts**: 18 trusts
- **NHS Specialist Trusts**: 15 trusts
- **NHS Ambulance Trusts**: 10 trusts

## Hard rules
- Em-dash ` — ` (U+2014 with spaces) in composite keys
- Scoped alias parent = EXACT trust name (from brief JSON)
- Every source URL `https://`
- 6-10 key_stats per entry, trust-specific
- 2-4 sentence notes, trust-specific (NOT generic NHS-wide)

## Output

Each agent writes `scripts/D4_07_premises_<batch>.py` with `NEW = { ... }` direct dict literal. NO `__main__`, imports, or file mutation.

## Sub-lines in this cluster

### Premises (other) — Guy's & St Thomas' NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Guy's & St Thomas' NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £173.83M

### Premises (other) — University College London Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: University College London Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £127.82M

### Premises (other) — Barts Health NHS Trust
  sub-line type: Premises (other)
  parent trust: Barts Health NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £95.00M

### Premises (other) — Cambridge University Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Cambridge University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £88.51M

### Premises (other) — University Hospitals Birmingham NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals Birmingham NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £73.94M

### Premises (other) — The Leeds Teaching Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: The Leeds Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £62.91M

### Premises (other) — Frimley Health NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Frimley Health NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £62.50M

### Premises (other) — Imperial College Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: Imperial College Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £61.59M

### Premises (other) — Northern Care Alliance NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Northern Care Alliance NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £61.12M

### Premises (other) — University Hospitals of Leicester NHS Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals of Leicester NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £59.90M

### Premises (other) — Nottingham University Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: Nottingham University Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £59.56M

### Premises (other) — King’s College Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: King’s College Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £57.07M

### Premises (other) — University Hospital Southampton NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: University Hospital Southampton NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £54.48M

### Premises (other) — Mid and South Essex NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Mid and South Essex NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £53.07M

### Premises (other) — Liverpool University Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Liverpool University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £50.34M

### Premises (other) — Northumbria Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Northumbria Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £50.33M

### Premises (other) — Manchester University NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Manchester University NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £47.71M

### Premises (other) — University Hospitals Sussex NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals Sussex NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £47.42M

### Premises (other) — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £47.34M

### Premises (other) — Central and North West London NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Central and North West London NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £47.20M

### Premises (other) — Oxford University Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Oxford University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £46.88M

### Premises (other) — East Suffolk and North Essex NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: East Suffolk and North Essex NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £46.28M

### Premises (other) — Sheffield Teaching Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Sheffield Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £45.95M

### Premises (other) — Royal Free London NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Royal Free London NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £44.11M

### Premises (other) — North Bristol NHS Trust
  sub-line type: Premises (other)
  parent trust: North Bristol NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £40.73M

### Premises (other) — Lancashire Teaching Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Lancashire Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £40.42M

### Premises (other) — Mersey Care NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Mersey Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £39.75M

### Premises (other) — Lewisham and Greenwich NHS Trust
  sub-line type: Premises (other)
  parent trust: Lewisham and Greenwich NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £38.22M

### Premises (other) — Royal Berkshire NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Royal Berkshire NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £38.15M

### Premises (other) — Great Ormond Street Hospital for Children NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Great Ormond Street Hospital for Children NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £34.39M

### Premises (other) — Mersey and West Lancashire Teaching Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: Mersey and West Lancashire Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £34.15M

### Premises (other) — Lancashire and South Cumbria NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Lancashire and South Cumbria NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £33.43M

### Premises (other) — Buckinghamshire Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: Buckinghamshire Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £33.13M

### Premises (other) — Kingston Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Kingston Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £32.75M

### Premises (other) — Hull University Teaching Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: Hull University Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £32.29M

### Premises (other) — The Shrewsbury and Telford Hospital NHS Trust
  sub-line type: Premises (other)
  parent trust: The Shrewsbury and Telford Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £31.89M

### Premises (other) — North East London NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: North East London NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £31.00M

### Premises (other) — Sandwell And West Birmingham Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: Sandwell And West Birmingham Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £30.86M

### Premises (other) — The Royal Wolverhampton NHS Trust
  sub-line type: Premises (other)
  parent trust: The Royal Wolverhampton NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £30.28M

### Premises (other) — University Hospitals Dorset NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals Dorset NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £29.94M

### Premises (other) — South London and Maudsley NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: South London and Maudsley NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £29.72M

### Premises (other) — University Hospitals of Derby and Burton NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals of Derby and Burton NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £28.81M

### Premises (other) — Calderdale and Huddersfield NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Calderdale and Huddersfield NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £28.76M

### Premises (other) — East Kent Hospitals University NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: East Kent Hospitals University NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £28.74M

### Premises (other) — Dartford and Gravesham NHS Trust
  sub-line type: Premises (other)
  parent trust: Dartford and Gravesham NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £28.70M

### Premises (other) — East Lancashire Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: East Lancashire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £28.04M

### Premises (other) — South Tyneside and Sunderland NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: South Tyneside and Sunderland NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £27.76M

### Premises (other) — University Hospitals of North Midlands NHS Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals of North Midlands NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £27.74M

### Premises (other) — University Hospitals Coventry And Warwickshire NHS Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals Coventry And Warwickshire NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £27.67M

### Premises (other) — Royal Devon University Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Royal Devon University Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £27.33M

### Premises (other) — University Hospitals Plymouth NHS Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals Plymouth NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £27.25M

### Premises (other) — St George's University Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: St George's University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £27.21M

### Premises (other) — Norfolk and Norwich University Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Norfolk and Norwich University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £26.91M

### Premises (other) — United Lincolnshire Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: United Lincolnshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £26.80M

### Premises (other) — South Tees Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: South Tees Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £26.71M

### Premises (other) — County Durham and Darlington NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: County Durham and Darlington NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £26.21M

### Premises (other) — York and Scarborough Teaching Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: York and Scarborough Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £25.74M

### Premises (other) — Leicestershire Partnership NHS Trust
  sub-line type: Premises (other)
  parent trust: Leicestershire Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £25.72M

### Premises (other) — East Sussex Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: East Sussex Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £25.70M

### Premises (other) — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £24.43M

### Premises (other) — Wirral University Teaching Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Wirral University Teaching Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £24.04M

### Premises (other) — East And North Hertfordshire NHS Trust
  sub-line type: Premises (other)
  parent trust: East And North Hertfordshire NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £23.79M

### Premises (other) — Torbay and South Devon NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Torbay and South Devon NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £23.58M

### Premises (other) — Nottinghamshire Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Nottinghamshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £23.38M

### Premises (other) — Tees, Esk and Wear Valleys NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Tees, Esk and Wear Valleys NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £23.34M

### Premises (other) — Whittington Health NHS Trust
  sub-line type: Premises (other)
  parent trust: Whittington Health NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £22.95M

### Premises (other) — Bolton NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Bolton NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £22.64M

### Premises (other) — Somerset NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Somerset NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £22.59M

### Premises (other) — Solent NHS Trust
  sub-line type: Premises (other)
  parent trust: Solent NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £22.30M

### Premises (other) — Milton Keynes University Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Milton Keynes University Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £22.29M

### Premises (other) — North Cumbria Integrated Care NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: North Cumbria Integrated Care NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £22.28M

### Premises (other) — Birmingham Community Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Birmingham Community Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £22.16M

### Premises (other) — Wrightington, Wigan and Leigh NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Wrightington, Wigan and Leigh NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £22.10M

### Premises (other) — West Hertfordshire Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: West Hertfordshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £21.94M

### Premises (other) — The Royal Marsden NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Royal Marsden NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £21.89M

### Premises (other) — Blackpool Teaching Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Blackpool Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £21.45M

### Premises (other) — Sherwood Forest Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Sherwood Forest Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £20.68M

### Premises (other) — The Christie NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Christie NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £20.67M

### Premises (other) — London North West University Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: London North West University Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £20.52M

### Premises (other) — North West Ambulance Service NHS Trust
  sub-line type: Premises (other)
  parent trust: North West Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £20.27M

### Premises (other) — University Hospitals Bristol and Weston NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals Bristol and Weston NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £20.18M

### Premises (other) — Mid Cheshire Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Mid Cheshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £20.16M

### Premises (other) — Epsom and St Helier University Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: Epsom and St Helier University Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £19.98M

### Premises (other) — Salisbury NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Salisbury NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £19.62M

### Premises (other) — Worcestershire Acute Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: Worcestershire Acute Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £19.54M

### Premises (other) — Chelsea and Westminster Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Chelsea and Westminster Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £19.53M

### Premises (other) — Kettering General Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Kettering General Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £19.40M

### Premises (other) — Royal United Hospitals Bath NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Royal United Hospitals Bath NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £19.18M

### Premises (other) — Chesterfield Royal Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Chesterfield Royal Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £19.03M

### Premises (other) — University Hospitals of Morecambe Bay NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: University Hospitals of Morecambe Bay NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £18.91M

### Premises (other) — Hampshire Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Hampshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £18.87M

### Premises (other) — Bedfordshire Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Bedfordshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £18.87M

### Premises (other) — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £18.80M

### Premises (other) — Maidstone And Tunbridge Wells NHS Trust
  sub-line type: Premises (other)
  parent trust: Maidstone And Tunbridge Wells NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £18.77M

### Premises (other) — Essex Partnership University NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Essex Partnership University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £18.62M

### Premises (other) — Ashford and St Peter's Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Ashford and St Peter's Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £18.55M

### Premises (other) — Barnet, Enfield And Haringey Mental Health NHS Trust
  sub-line type: Premises (other)
  parent trust: Barnet, Enfield And Haringey Mental Health NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £18.43M

### Premises (other) — Royal Surrey NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Royal Surrey NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £18.29M

### Premises (other) — Northern Lincolnshire and Goole NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Northern Lincolnshire and Goole NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £18.06M

### Premises (other) — South East Coast Ambulance Service NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: South East Coast Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £18.02M

### Premises (other) — Surrey And Sussex Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: Surrey And Sussex Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £17.89M

### Premises (other) — Portsmouth Hospitals University NHS Trust
  sub-line type: Premises (other)
  parent trust: Portsmouth Hospitals University NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £17.64M

### Premises (other) — Greater Manchester Mental Health NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Greater Manchester Mental Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £17.31M

### Premises (other) — Birmingham and Solihull Mental Health NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Birmingham and Solihull Mental Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £17.28M

### Premises (other) — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Warrington and Halton Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £17.26M

### Premises (other) — Royal Cornwall Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: Royal Cornwall Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £17.17M

### Premises (other) — Gateshead Health NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Gateshead Health NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £17.16M

### Premises (other) — London Ambulance Service NHS Trust
  sub-line type: Premises (other)
  parent trust: London Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £17.16M

### Premises (other) — Surrey and Borders Partnership NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Surrey and Borders Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £16.92M

### Premises (other) — Berkshire Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Berkshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £16.81M

### Premises (other) — George Eliot Hospital NHS Trust
  sub-line type: Premises (other)
  parent trust: George Eliot Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £16.79M

### Premises (other) — Homerton Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Homerton Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £16.30M

### Premises (other) — Northampton General Hospital NHS Trust
  sub-line type: Premises (other)
  parent trust: Northampton General Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £16.23M

### Premises (other) — South West London and St George's Mental Health NHS Trust
  sub-line type: Premises (other)
  parent trust: South West London and St George's Mental Health NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £15.93M

### Premises (other) — Oxford Health NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Oxford Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £15.76M

### Premises (other) — The Mid Yorkshire Hospitals NHS Trust
  sub-line type: Premises (other)
  parent trust: The Mid Yorkshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £15.76M

### Premises (other) — Avon and Wiltshire Mental Health Partnership NHS Trust
  sub-line type: Premises (other)
  parent trust: Avon and Wiltshire Mental Health Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £15.35M

### Premises (other) — Tameside and Glossop Integrated Care NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Tameside and Glossop Integrated Care NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £15.29M

### Premises (other) — Gloucestershire Health and Care NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Gloucestershire Health and Care NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £15.25M

### Premises (other) — Stockport NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Stockport NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £15.15M

### Premises (other) — North Tees and Hartlepool NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: North Tees and Hartlepool NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £15.08M

### Premises (other) — Sussex Community NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Sussex Community NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £15.03M

### Premises (other) — South Western Ambulance Service NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: South Western Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £14.86M

### Premises (other) — Medway NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Medway NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £14.81M

### Premises (other) — The Princess Alexandra Hospital NHS Trust
  sub-line type: Premises (other)
  parent trust: The Princess Alexandra Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £14.79M

### Premises (other) — Cambridgeshire and Peterborough NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Cambridgeshire and Peterborough NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £14.69M

### Premises (other) — Dorset Healthcare University NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Dorset Healthcare University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £14.51M

### Premises (other) — Southern Health NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Southern Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £14.32M

### Premises (other) — Isle of Wight NHS Trust
  sub-line type: Premises (other)
  parent trust: Isle of Wight NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £14.21M

### Premises (other) — The Rotherham NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Rotherham NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £14.16M

### Premises (other) — South Central Ambulance Service NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: South Central Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £14.14M

### Premises (other) — North West Anglia NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: North West Anglia NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £14.03M

### Premises (other) — Kent and Medway NHS and Social Care Partnership Trust
  sub-line type: Premises (other)
  parent trust: Kent and Medway NHS and Social Care Partnership Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £14.02M

### Premises (other) — The Clatterbridge Cancer Centre NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Clatterbridge Cancer Centre NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £13.70M

### Premises (other) — Alder Hey Children's NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Alder Hey Children's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £13.65M

### Premises (other) — Northamptonshire Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Northamptonshire Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £13.28M

### Premises (other) — The Hillingdon Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Hillingdon Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £13.27M

### Premises (other) — Midlands Partnership NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Midlands Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £13.22M

### Premises (other) — East Midlands Ambulance Service NHS Trust
  sub-line type: Premises (other)
  parent trust: East Midlands Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £13.14M

### Premises (other) — Cambridgeshire Community Services NHS Trust
  sub-line type: Premises (other)
  parent trust: Cambridgeshire Community Services NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £13.06M

### Premises (other) — Harrogate and District NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Harrogate and District NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £12.79M

### Premises (other) — West London NHS Trust
  sub-line type: Premises (other)
  parent trust: West London NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £12.72M

### Premises (other) — Oxleas NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Oxleas NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £12.62M

### Premises (other) — Norfolk and Suffolk NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Norfolk and Suffolk NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £12.47M

### Premises (other) — Pennine Care NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Pennine Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £12.45M

### Premises (other) — Countess of Chester Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Countess of Chester Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £12.43M

### Premises (other) — Airedale NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Airedale NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £12.30M

### Premises (other) — Walsall Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: Walsall Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £12.16M

### Premises (other) — East Cheshire NHS Trust
  sub-line type: Premises (other)
  parent trust: East Cheshire NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £11.85M

### Premises (other) — Cornwall Partnership NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Cornwall Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £11.67M

### Premises (other) — Sheffield Children's NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Sheffield Children's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £11.48M

### Premises (other) — Coventry and Warwickshire Partnership NHS Trust
  sub-line type: Premises (other)
  parent trust: Coventry and Warwickshire Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £11.24M

### Premises (other) — West Midlands Ambulance Service University NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: West Midlands Ambulance Service University NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £11.21M

### Premises (other) — Sussex Partnership NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Sussex Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £11.04M

### Premises (other) — Yorkshire Ambulance Service NHS Trust
  sub-line type: Premises (other)
  parent trust: Yorkshire Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £10.84M

### Premises (other) — Gloucestershire Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Gloucestershire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £10.68M

### Premises (other) — Barnsley Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Barnsley Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £10.34M

### Premises (other) — Devon Partnership NHS Trust
  sub-line type: Premises (other)
  parent trust: Devon Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £10.21M

### Premises (other) — Dorset County Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Dorset County Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £9.81M

### Premises (other) — James Paget University Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: James Paget University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £9.61M

### Premises (other) — Bradford Teaching Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Bradford Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £9.58M

### Premises (other) — South Warwickshire NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: South Warwickshire NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £9.47M

### Premises (other) — Lincolnshire Community Health Services NHS Trust
  sub-line type: Premises (other)
  parent trust: Lincolnshire Community Health Services NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £9.38M

### Premises (other) — The Dudley Group NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Dudley Group NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £9.34M

### Premises (other) — Kent Community Health NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Kent Community Health NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £9.26M

### Premises (other) — Royal Papworth Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Royal Papworth Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £9.23M

### Premises (other) — Black Country Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Black Country Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £9.09M

### Premises (other) — Cheshire and Wirral Partnership NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Cheshire and Wirral Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £8.94M

### Premises (other) — Derbyshire Community Health Services NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Derbyshire Community Health Services NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £8.93M

### Premises (other) — Leeds Community Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: Leeds Community Healthcare NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £8.91M

### Premises (other) — Liverpool Women's NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Liverpool Women's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £8.66M

### Premises (other) — The Walton Centre NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Walton Centre NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £8.62M

### Premises (other) — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £8.56M

### Premises (other) — Royal National Orthopaedic Hospital NHS Trust
  sub-line type: Premises (other)
  parent trust: Royal National Orthopaedic Hospital NHS Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £8.52M

### Premises (other) — Moorfields Eye Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Moorfields Eye Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £8.51M

### Premises (other) — Wye Valley NHS Trust
  sub-line type: Premises (other)
  parent trust: Wye Valley NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £8.10M

### Premises (other) — Shropshire Community Health NHS Trust
  sub-line type: Premises (other)
  parent trust: Shropshire Community Health NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £7.84M

### Premises (other) — South West Yorkshire Partnership NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: South West Yorkshire Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £7.80M

### Premises (other) — Herefordshire and Worcestershire Health and Care NHS Trust
  sub-line type: Premises (other)
  parent trust: Herefordshire and Worcestershire Health and Care NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £7.68M

### Premises (other) — North Middlesex University Hospital NHS Trust
  sub-line type: Premises (other)
  parent trust: North Middlesex University Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £7.67M

### Premises (other) — West Suffolk NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: West Suffolk NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £7.48M

### Premises (other) — Leeds and York Partnership NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Leeds and York Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £7.44M

### Premises (other) — Lincolnshire Partnership NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Lincolnshire Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £6.93M

### Premises (other) — North Staffordshire Combined Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: North Staffordshire Combined Healthcare NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £6.73M

### Premises (other) — Great Western Hospitals NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Great Western Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £6.62M

### Premises (other) — Bradford District Care NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Bradford District Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £6.52M

### Premises (other) — Rotherham Doncaster and South Humber NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Rotherham Doncaster and South Humber NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £6.48M

### Premises (other) — Queen Victoria Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Queen Victoria Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £6.47M

### Premises (other) — Camden and Islington NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Camden and Islington NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £6.35M

### Premises (other) — East of England Ambulance Service NHS Trust
  sub-line type: Premises (other)
  parent trust: East of England Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £6.33M

### Premises (other) — The Royal Orthopaedic Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Royal Orthopaedic Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £6.25M

### Premises (other) — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £6.12M

### Premises (other) — Sheffield Health and Social Care NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Sheffield Health and Social Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £5.92M

### Premises (other) — Hertfordshire Partnership University NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Hertfordshire Partnership University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £5.20M

### Premises (other) — Bridgewater Community Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Bridgewater Community Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £4.27M

### Premises (other) — Liverpool Heart and Chest Hospital NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Liverpool Heart and Chest Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Premises & Infrastructure
  value: £4.14M

### Premises (other) — Derbyshire Healthcare NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Derbyshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £3.82M

### Premises (other) — Wirral Community Health and Care NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Wirral Community Health and Care NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £3.73M

### Premises (other) — Central London Community Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: Central London Community Healthcare NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £3.66M

### Premises (other) — Norfolk Community Health and Care NHS Trust
  sub-line type: Premises (other)
  parent trust: Norfolk Community Health and Care NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £3.53M

### Premises (other) — North East Ambulance Service NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: North East Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Premises & Infrastructure
  value: £3.50M

### Premises (other) — Hertfordshire Community NHS Trust
  sub-line type: Premises (other)
  parent trust: Hertfordshire Community NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £3.24M

### Premises (other) — Hounslow and Richmond Community Healthcare NHS Trust
  sub-line type: Premises (other)
  parent trust: Hounslow and Richmond Community Healthcare NHS Trust
  trust category: NHS Community Trusts
  parent line: Premises & Infrastructure
  value: £3.19M

### Premises (other) — Tavistock and Portman NHS Foundation Trust
  sub-line type: Premises (other)
  parent trust: Tavistock and Portman NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £2.65M

### Premises (other) — Southport And Ormskirk Hospital NHS Trust
  sub-line type: Premises (other)
  parent trust: Southport And Ormskirk Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Premises & Infrastructure
  value: £2.49M

### Premises (other) — Dudley Integrated Health and Care NHS Trust
  sub-line type: Premises (other)
  parent trust: Dudley Integrated Health and Care NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Premises & Infrastructure
  value: £0.17M

