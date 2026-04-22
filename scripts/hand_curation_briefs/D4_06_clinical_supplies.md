# Cluster D4_06 Clinical supplies & services (NHS Trusts)

Scope: 196 trust clinical-supplies sub-lines · total £9.43B

## Task

Each depth-4 "Clinical supplies & services" sub-line under a specific NHS Trust needs a hand-curated Tier A entry that is TAILOR-MADE per-entity. NO generic template. NO shared content.

## Scope (what clinical supplies & services covers)
- Surgical supplies (sutures · meshes · prostheses · single-use instruments)
- Diagnostic reagents (pathology · histopathology · POC tests)
- Blood products (NHSBT invoiced per bag)
- Oxygen and medical gases (BOC contract)
- Dressings / wound-care (procured via NHS Supply Chain Medical category)
- Theatre packs / custom procedure packs
- Radiology contrast media
- Consumables for devices (pacemaker leads · hip stems · knee trays · CGM sensors)
- NOT drugs (those are D4_05, separate line)
- NOT premises / IT (separate lines)

## Key context 2024-25
- **NHS Supply Chain** delivers 80%+ via category management (Medical, FFD - Food/Facilities, ORCA)
- **High-cost devices** (HCDs) commissioning split — some devices pass through trust ClinSupp, others ICB-commissioned
- **VAT** on clinical supplies: UK VAT refund for NHS (since 1984) — zero-rate via RCS reclaim — usually NOT visible in trust Drug/ClinSupp gross
- **Industrial action 2023-24**: elective cancellations reduced theatre-consumable spend (partial rebound 2024-25)
- **CNST** (Clinical Negligence Scheme for Trusts) is NOT Clinical supplies — that's NHS Resolution premium, separate
- **Sustainability (DHSC Net Zero)**: pressure to switch from single-use to reusable instruments impacting post-2024 procurement strategy

## Schema per entry
```python
"Clinical supplies & services — <trust>": {
    "aliases": [{"name": "Clinical supplies & services", "parent": "<trust>"}],
    "description": "2-3 sentences trust-specific clinical supplies (surgical volume · specialty mix · consumable-heavy specialties)",
    "beneficiaries": "Patients undergoing procedures / diagnostics / treatment at trust sites",
    "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions for the Supply of Goods and Services",
    "key_stats": [
        {"label": "Clinical supplies & services 2024-25", "value": "£<exact from brief>M"},
        {"label": "Share of trust total opex", "value": "c. X%"},
        {"label": "Activity anchor", "value": "e.g. 'c.140k elective admissions/yr'"},
        {"label": "Biggest sub-category", "value": "e.g. 'Orthopaedic implants ~20% (hip/knee/trauma)'"},
        {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct ~20%"},
        {"label": "YoY change", "value": "c. +X% nominal"},
        {"label": "Peer benchmark", "value": "£/elective or per bed-day vs peer"},
        {"label": "Theatre activity", "value": "N theatres · M sessions/yr"}
    ],  # 6-10 trust-specific stats
    "notes": "2-4 sentences trust-specific drivers (high-volume specialties like orthopaedics · cardiology · vascular · radiotherapy devices · infection-control pressures · CCRW robotic surgery scaling · contract renegotiation dates · supply-chain incidents 2024-25)",
    "sources": [...],  # 2-3 with https:// URLs
    "related": ["<trust>", "Drugs costs — <trust>"]
}
```

## Specialty-mix anchors by category
- **Acute Trusts**: ~12-18% of trust opex · driven by surgery volume · orthopaedic implants · cardiology stents · vascular grafts
- **Specialist Trusts** (cancer / cardiac / orthopaedic): higher share 20-25% · prostheses · specialty devices · robot consumables
- **Mental Health Trusts**: LOW (1-3%) · mostly restraint devices · ward diagnostics · PPE
- **Community Trusts**: LOW-MEDIUM (3-6%) · wound-care · continence · catheters · home respiratory
- **Ambulance Trusts**: MEDIUM · defibrillator consumables · trauma packs · O2 cylinders · stretchers

## Category spread of this brief
- **NHS Acute Trusts**: 118 trusts
- **NHS Mental Health Trusts**: 35 trusts
- **NHS Community Trusts**: 18 trusts
- **NHS Specialist Trusts**: 15 trusts
- **NHS Ambulance Trusts**: 10 trusts

## Rules
- Em-dash ` — ` (U+2014 with spaces) in composite keys
- Scoped alias parent = EXACT trust name (from brief JSON)
- Every source with https:// URL
- Use £ value from the brief JSON as anchor
- 6-10 key_stats per entry
- Trust-specific notes, NOT generic NHS-wide

## Output
Write `scripts/D4_06_clinical_<batch>.py` with `NEW = { ... }` direct dict literal.

## Sub-lines in this cluster

### Clinical supplies & services — Guy's & St Thomas' NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Guy's & St Thomas' NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £367.73M

### Clinical supplies & services — Manchester University NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Manchester University NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £262.71M

### Clinical supplies & services — University Hospitals Birmingham NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals Birmingham NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £221.28M

### Clinical supplies & services — Barts Health NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Barts Health NHS Trust
  trust category: NHS Acute Trusts
  value: £211.53M

### Clinical supplies & services — The Leeds Teaching Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: The Leeds Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £205.86M

### Clinical supplies & services — Cambridge University Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Cambridge University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £199.88M

### Clinical supplies & services — Nottingham University Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Nottingham University Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £183.46M

### Clinical supplies & services — Oxford University Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Oxford University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £177.77M

### Clinical supplies & services — University Hospitals of Leicester NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals of Leicester NHS Trust
  trust category: NHS Acute Trusts
  value: £166.49M

### Clinical supplies & services — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £165.13M

### Clinical supplies & services — Imperial College Healthcare NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Imperial College Healthcare NHS Trust
  trust category: NHS Acute Trusts
  value: £163.90M

### Clinical supplies & services — University Hospitals Sussex NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals Sussex NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £135.41M

### Clinical supplies & services — Sheffield Teaching Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Sheffield Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £134.82M

### Clinical supplies & services — St George's University Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: St George's University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £132.36M

### Clinical supplies & services — University Hospital Southampton NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospital Southampton NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £130.60M

### Clinical supplies & services — University College London Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: University College London Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £130.01M

### Clinical supplies & services — King’s College Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: King’s College Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £122.49M

### Clinical supplies & services — Mid and South Essex NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Mid and South Essex NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £117.63M

### Clinical supplies & services — University Hospitals of North Midlands NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals of North Midlands NHS Trust
  trust category: NHS Acute Trusts
  value: £116.13M

### Clinical supplies & services — University Hospitals Bristol and Weston NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals Bristol and Weston NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £110.71M

### Clinical supplies & services — East Kent Hospitals University NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: East Kent Hospitals University NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £107.30M

### Clinical supplies & services — South Tees Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: South Tees Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £107.06M

### Clinical supplies & services — Northern Care Alliance NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Northern Care Alliance NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £104.07M

### Clinical supplies & services — Liverpool University Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Liverpool University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £103.12M

### Clinical supplies & services — The Royal Wolverhampton NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: The Royal Wolverhampton NHS Trust
  trust category: NHS Acute Trusts
  value: £102.86M

### Clinical supplies & services — East Suffolk and North Essex NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: East Suffolk and North Essex NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £97.63M

### Clinical supplies & services — University Hospitals Coventry And Warwickshire NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals Coventry And Warwickshire NHS Trust
  trust category: NHS Acute Trusts
  value: £97.28M

### Clinical supplies & services — Chelsea and Westminster Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Chelsea and Westminster Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £95.59M

### Clinical supplies & services — Norfolk and Norwich University Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Norfolk and Norwich University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £94.70M

### Clinical supplies & services — North Bristol NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: North Bristol NHS Trust
  trust category: NHS Acute Trusts
  value: £94.30M

### Clinical supplies & services — University Hospitals Plymouth NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals Plymouth NHS Trust
  trust category: NHS Acute Trusts
  value: £88.96M

### Clinical supplies & services — Royal Free London NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Royal Free London NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £88.23M

### Clinical supplies & services — Royal Devon University Healthcare NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Royal Devon University Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £87.63M

### Clinical supplies & services — London North West University Healthcare NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: London North West University Healthcare NHS Trust
  trust category: NHS Acute Trusts
  value: £87.50M

### Clinical supplies & services — Frimley Health NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Frimley Health NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £86.35M

### Clinical supplies & services — York and Scarborough Teaching Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: York and Scarborough Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £82.02M

### Clinical supplies & services — Hull University Teaching Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Hull University Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £80.96M

### Clinical supplies & services — University Hospitals of Derby and Burton NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals of Derby and Burton NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £79.03M

### Clinical supplies & services — United Lincolnshire Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: United Lincolnshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £74.10M

### Clinical supplies & services — Portsmouth Hospitals University NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Portsmouth Hospitals University NHS Trust
  trust category: NHS Acute Trusts
  value: £70.61M

### Clinical supplies & services — Lewisham and Greenwich NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Lewisham and Greenwich NHS Trust
  trust category: NHS Acute Trusts
  value: £70.03M

### Clinical supplies & services — University Hospitals Dorset NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals Dorset NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £66.72M

### Clinical supplies & services — Bedfordshire Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Bedfordshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £63.41M

### Clinical supplies & services — Somerset NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Somerset NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £62.65M

### Clinical supplies & services — Gloucestershire Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Gloucestershire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £62.56M

### Clinical supplies & services — South Tyneside and Sunderland NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: South Tyneside and Sunderland NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £62.22M

### Clinical supplies & services — Royal Papworth Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Royal Papworth Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £60.13M

### Clinical supplies & services — Lancashire Teaching Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Lancashire Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £59.45M

### Clinical supplies & services — Epsom and St Helier University Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Epsom and St Helier University Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £58.04M

### Clinical supplies & services — Bradford Teaching Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Bradford Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £57.81M

### Clinical supplies & services — Blackpool Teaching Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Blackpool Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £56.30M

### Clinical supplies & services — The Dudley Group NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Dudley Group NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £56.22M

### Clinical supplies & services — Worcestershire Acute Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Worcestershire Acute Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £55.90M

### Clinical supplies & services — The Mid Yorkshire Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: The Mid Yorkshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £55.86M

### Clinical supplies & services — County Durham and Darlington NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: County Durham and Darlington NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £55.66M

### Clinical supplies & services — The Shrewsbury and Telford Hospital NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: The Shrewsbury and Telford Hospital NHS Trust
  trust category: NHS Acute Trusts
  value: £55.52M

### Clinical supplies & services — The Royal Marsden NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Royal Marsden NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £54.32M

### Clinical supplies & services — Northampton General Hospital NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Northampton General Hospital NHS Trust
  trust category: NHS Acute Trusts
  value: £52.56M

### Clinical supplies & services — Liverpool Heart and Chest Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Liverpool Heart and Chest Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £52.42M

### Clinical supplies & services — Hampshire Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Hampshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £51.90M

### Clinical supplies & services — Royal United Hospitals Bath NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Royal United Hospitals Bath NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £51.70M

### Clinical supplies & services — Mersey and West Lancashire Teaching Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Mersey and West Lancashire Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £51.31M

### Clinical supplies & services — Royal Cornwall Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Royal Cornwall Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £51.19M

### Clinical supplies & services — East Lancashire Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: East Lancashire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £50.77M

### Clinical supplies & services — Royal Berkshire NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Royal Berkshire NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £49.89M

### Clinical supplies & services — Maidstone And Tunbridge Wells NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Maidstone And Tunbridge Wells NHS Trust
  trust category: NHS Acute Trusts
  value: £49.50M

### Clinical supplies & services — East Sussex Healthcare NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: East Sussex Healthcare NHS Trust
  trust category: NHS Acute Trusts
  value: £49.15M

### Clinical supplies & services — Royal Surrey NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Royal Surrey NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £48.78M

### Clinical supplies & services — Northumbria Healthcare NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Northumbria Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £47.85M

### Clinical supplies & services — Great Ormond Street Hospital for Children NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Great Ormond Street Hospital for Children NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £47.08M

### Clinical supplies & services — Northern Lincolnshire and Goole NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Northern Lincolnshire and Goole NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £45.03M

### Clinical supplies & services — Wrightington, Wigan and Leigh NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Wrightington, Wigan and Leigh NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £44.60M

### Clinical supplies & services — Great Western Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Great Western Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £43.93M

### Clinical supplies & services — Wirral University Teaching Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Wirral University Teaching Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £42.87M

### Clinical supplies & services — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £42.14M

### Clinical supplies & services — East And North Hertfordshire NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: East And North Hertfordshire NHS Trust
  trust category: NHS Acute Trusts
  value: £42.13M

### Clinical supplies & services — North Cumbria Integrated Care NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: North Cumbria Integrated Care NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £40.88M

### Clinical supplies & services — Sandwell And West Birmingham Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Sandwell And West Birmingham Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £40.59M

### Clinical supplies & services — Gateshead Health NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Gateshead Health NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £40.22M

### Clinical supplies & services — London Ambulance Service NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: London Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  value: £39.76M

### Clinical supplies & services — Buckinghamshire Healthcare NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Buckinghamshire Healthcare NHS Trust
  trust category: NHS Acute Trusts
  value: £39.75M

### Clinical supplies & services — Birmingham Community Healthcare NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Birmingham Community Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  value: £38.99M

### Clinical supplies & services — North Middlesex University Hospital NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: North Middlesex University Hospital NHS Trust
  trust category: NHS Acute Trusts
  value: £38.63M

### Clinical supplies & services — Sherwood Forest Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Sherwood Forest Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £38.58M

### Clinical supplies & services — The Hillingdon Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Hillingdon Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £38.53M

### Clinical supplies & services — University Hospitals of Morecambe Bay NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: University Hospitals of Morecambe Bay NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £38.41M

### Clinical supplies & services — Dartford and Gravesham NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Dartford and Gravesham NHS Trust
  trust category: NHS Acute Trusts
  value: £38.20M

### Clinical supplies & services — Ashford and St Peter's Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Ashford and St Peter's Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £37.67M

### Clinical supplies & services — North West Anglia NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: North West Anglia NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £37.27M

### Clinical supplies & services — Homerton Healthcare NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Homerton Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £36.62M

### Clinical supplies & services — Kingston Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Kingston Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £36.08M

### Clinical supplies & services — Calderdale and Huddersfield NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Calderdale and Huddersfield NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £35.68M

### Clinical supplies & services — West Suffolk NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: West Suffolk NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £35.66M

### Clinical supplies & services — Countess of Chester Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Countess of Chester Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £35.58M

### Clinical supplies & services — Royal National Orthopaedic Hospital NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Royal National Orthopaedic Hospital NHS Trust
  trust category: NHS Specialist Trusts
  value: £35.37M

### Clinical supplies & services — Whittington Health NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Whittington Health NHS Trust
  trust category: NHS Acute Trusts
  value: £35.16M

### Clinical supplies & services — West Hertfordshire Hospitals NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: West Hertfordshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  value: £34.95M

### Clinical supplies & services — Wye Valley NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Wye Valley NHS Trust
  trust category: NHS Acute Trusts
  value: £34.95M

### Clinical supplies & services — Torbay and South Devon NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Torbay and South Devon NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £34.36M

### Clinical supplies & services — South Warwickshire NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: South Warwickshire NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £34.08M

### Clinical supplies & services — Northamptonshire Healthcare NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Northamptonshire Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  value: £33.31M

### Clinical supplies & services — Surrey And Sussex Healthcare NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Surrey And Sussex Healthcare NHS Trust
  trust category: NHS Acute Trusts
  value: £32.71M

### Clinical supplies & services — Hounslow and Richmond Community Healthcare NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Hounslow and Richmond Community Healthcare NHS Trust
  trust category: NHS Community Trusts
  value: £31.93M

### Clinical supplies & services — Medway NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Medway NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £31.76M

### Clinical supplies & services — Bolton NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Bolton NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £30.99M

### Clinical supplies & services — The Christie NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Christie NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £30.23M

### Clinical supplies & services — The Rotherham NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Rotherham NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £30.22M

### Clinical supplies & services — Alder Hey Children's NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Alder Hey Children's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £28.86M

### Clinical supplies & services — Kettering General Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Kettering General Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £28.70M

### Clinical supplies & services — The Walton Centre NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Walton Centre NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £28.65M

### Clinical supplies & services — Harrogate and District NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Harrogate and District NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £28.62M

### Clinical supplies & services — Barnsley Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Barnsley Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £28.53M

### Clinical supplies & services — Leeds Community Healthcare NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Leeds Community Healthcare NHS Trust
  trust category: NHS Community Trusts
  value: £28.18M

### Clinical supplies & services — North Tees and Hartlepool NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: North Tees and Hartlepool NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £27.55M

### Clinical supplies & services — Salisbury NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Salisbury NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £27.00M

### Clinical supplies & services — Oxford Health NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Oxford Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £26.37M

### Clinical supplies & services — Central and North West London NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Central and North West London NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £25.94M

### Clinical supplies & services — Milton Keynes University Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Milton Keynes University Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £25.62M

### Clinical supplies & services — Kent Community Health NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Kent Community Health NHS Foundation Trust
  trust category: NHS Community Trusts
  value: £25.55M

### Clinical supplies & services — Stockport NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Stockport NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £25.12M

### Clinical supplies & services — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Warrington and Halton Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £25.09M

### Clinical supplies & services — James Paget University Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: James Paget University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £24.90M

### Clinical supplies & services — Moorfields Eye Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Moorfields Eye Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £24.57M

### Clinical supplies & services — The Princess Alexandra Hospital NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: The Princess Alexandra Hospital NHS Trust
  trust category: NHS Acute Trusts
  value: £22.99M

### Clinical supplies & services — Midlands Partnership NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Midlands Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £22.70M

### Clinical supplies & services — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £22.55M

### Clinical supplies & services — Walsall Healthcare NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Walsall Healthcare NHS Trust
  trust category: NHS Acute Trusts
  value: £22.11M

### Clinical supplies & services — Airedale NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Airedale NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £21.28M

### Clinical supplies & services — Sheffield Children's NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Sheffield Children's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £20.92M

### Clinical supplies & services — Dorset County Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Dorset County Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £20.67M

### Clinical supplies & services — Sussex Partnership NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Sussex Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £20.38M

### Clinical supplies & services — Tameside and Glossop Integrated Care NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Tameside and Glossop Integrated Care NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £19.25M

### Clinical supplies & services — Mersey Care NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Mersey Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £19.05M

### Clinical supplies & services — Isle of Wight NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Isle of Wight NHS Trust
  trust category: NHS Acute Trusts
  value: £18.88M

### Clinical supplies & services — Mid Cheshire Hospitals NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Mid Cheshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £18.01M

### Clinical supplies & services — Central London Community Healthcare NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Central London Community Healthcare NHS Trust
  trust category: NHS Community Trusts
  value: £17.66M

### Clinical supplies & services — Chesterfield Royal Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Chesterfield Royal Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £16.53M

### Clinical supplies & services — East Cheshire NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: East Cheshire NHS Trust
  trust category: NHS Acute Trusts
  value: £15.99M

### Clinical supplies & services — Solent NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Solent NHS Trust
  trust category: NHS Community Trusts
  value: £14.01M

### Clinical supplies & services — Dorset Healthcare University NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Dorset Healthcare University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £12.45M

### Clinical supplies & services — Queen Victoria Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Queen Victoria Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £12.40M

### Clinical supplies & services — Derbyshire Community Health Services NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Derbyshire Community Health Services NHS Foundation Trust
  trust category: NHS Community Trusts
  value: £12.21M

### Clinical supplies & services — Sussex Community NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Sussex Community NHS Foundation Trust
  trust category: NHS Community Trusts
  value: £11.74M

### Clinical supplies & services — George Eliot Hospital NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: George Eliot Hospital NHS Trust
  trust category: NHS Acute Trusts
  value: £11.37M

### Clinical supplies & services — Lincolnshire Community Health Services NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Lincolnshire Community Health Services NHS Trust
  trust category: NHS Community Trusts
  value: £11.31M

### Clinical supplies & services — North East London NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: North East London NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £11.12M

### Clinical supplies & services — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  trust category: NHS Acute Trusts
  value: £10.47M

### Clinical supplies & services — Yorkshire Ambulance Service NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Yorkshire Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  value: £10.03M

### Clinical supplies & services — Gloucestershire Health and Care NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Gloucestershire Health and Care NHS Foundation Trust
  trust category: NHS Community Trusts
  value: £9.79M

### Clinical supplies & services — Southern Health NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Southern Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £9.68M

### Clinical supplies & services — Herefordshire and Worcestershire Health and Care NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Herefordshire and Worcestershire Health and Care NHS Trust
  trust category: NHS Community Trusts
  value: £9.16M

### Clinical supplies & services — Shropshire Community Health NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Shropshire Community Health NHS Trust
  trust category: NHS Community Trusts
  value: £9.01M

### Clinical supplies & services — Coventry and Warwickshire Partnership NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Coventry and Warwickshire Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  value: £8.80M

### Clinical supplies & services — Cambridgeshire Community Services NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Cambridgeshire Community Services NHS Trust
  trust category: NHS Community Trusts
  value: £8.22M

### Clinical supplies & services — Cornwall Partnership NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Cornwall Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £8.13M

### Clinical supplies & services — Norfolk Community Health and Care NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Norfolk Community Health and Care NHS Trust
  trust category: NHS Community Trusts
  value: £7.93M

### Clinical supplies & services — Liverpool Women's NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Liverpool Women's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £7.77M

### Clinical supplies & services — The Clatterbridge Cancer Centre NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Clatterbridge Cancer Centre NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £7.64M

### Clinical supplies & services — West Midlands Ambulance Service University NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: West Midlands Ambulance Service University NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  value: £7.45M

### Clinical supplies & services — Nottinghamshire Healthcare NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Nottinghamshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £7.36M

### Clinical supplies & services — East of England Ambulance Service NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: East of England Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  value: £7.22M

### Clinical supplies & services — South Western Ambulance Service NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: South Western Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  value: £6.91M

### Clinical supplies & services — Berkshire Healthcare NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Berkshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £6.90M

### Clinical supplies & services — North West Ambulance Service NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: North West Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  value: £6.67M

### Clinical supplies & services — Wirral Community Health and Care NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Wirral Community Health and Care NHS Foundation Trust
  trust category: NHS Community Trusts
  value: £6.58M

### Clinical supplies & services — East Midlands Ambulance Service NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: East Midlands Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  value: £6.56M

### Clinical supplies & services — Oxleas NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Oxleas NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £6.38M

### Clinical supplies & services — Rotherham Doncaster and South Humber NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Rotherham Doncaster and South Humber NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £6.36M

### Clinical supplies & services — Bradford District Care NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Bradford District Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £5.82M

### Clinical supplies & services — Bridgewater Community Healthcare NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Bridgewater Community Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  value: £5.79M

### Clinical supplies & services — Southport And Ormskirk Hospital NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Southport And Ormskirk Hospital NHS Trust
  trust category: NHS Acute Trusts
  value: £5.76M

### Clinical supplies & services — South Central Ambulance Service NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: South Central Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  value: £5.55M

### Clinical supplies & services — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £5.54M

### Clinical supplies & services — Essex Partnership University NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Essex Partnership University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £5.53M

### Clinical supplies & services — Lancashire and South Cumbria NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Lancashire and South Cumbria NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £5.07M

### Clinical supplies & services — Hertfordshire Community NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Hertfordshire Community NHS Trust
  trust category: NHS Community Trusts
  value: £4.93M

### Clinical supplies & services — Greater Manchester Mental Health NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Greater Manchester Mental Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £4.83M

### Clinical supplies & services — Lincolnshire Partnership NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Lincolnshire Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £4.77M

### Clinical supplies & services — Leicestershire Partnership NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Leicestershire Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  value: £4.68M

### Clinical supplies & services — Cambridgeshire and Peterborough NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Cambridgeshire and Peterborough NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £4.66M

### Clinical supplies & services — South West Yorkshire Partnership NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: South West Yorkshire Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £4.46M

### Clinical supplies & services — South East Coast Ambulance Service NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: South East Coast Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  value: £4.40M

### Clinical supplies & services — Tees, Esk and Wear Valleys NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Tees, Esk and Wear Valleys NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £3.58M

### Clinical supplies & services — Kent and Medway NHS and Social Care Partnership Trust
  sub-line type: Clinical supplies & services
  parent trust: Kent and Medway NHS and Social Care Partnership Trust
  trust category: NHS Mental Health Trusts
  value: £3.03M

### Clinical supplies & services — North East Ambulance Service NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: North East Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  value: £2.91M

### Clinical supplies & services — South London and Maudsley NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: South London and Maudsley NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £2.87M

### Clinical supplies & services — Devon Partnership NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Devon Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  value: £2.81M

### Clinical supplies & services — Cheshire and Wirral Partnership NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Cheshire and Wirral Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £2.29M

### Clinical supplies & services — The Royal Orthopaedic Hospital NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: The Royal Orthopaedic Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  value: £2.23M

### Clinical supplies & services — Black Country Healthcare NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Black Country Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £1.67M

### Clinical supplies & services — West London NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: West London NHS Trust
  trust category: NHS Mental Health Trusts
  value: £1.64M

### Clinical supplies & services — Barnet, Enfield And Haringey Mental Health NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Barnet, Enfield And Haringey Mental Health NHS Trust
  trust category: NHS Mental Health Trusts
  value: £1.46M

### Clinical supplies & services — Leeds and York Partnership NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Leeds and York Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £1.29M

### Clinical supplies & services — Norfolk and Suffolk NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Norfolk and Suffolk NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £1.29M

### Clinical supplies & services — Avon and Wiltshire Mental Health Partnership NHS Trust
  sub-line type: Clinical supplies & services
  parent trust: Avon and Wiltshire Mental Health Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  value: £1.22M

### Clinical supplies & services — Pennine Care NHS Foundation Trust
  sub-line type: Clinical supplies & services
  parent trust: Pennine Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  value: £1.16M

