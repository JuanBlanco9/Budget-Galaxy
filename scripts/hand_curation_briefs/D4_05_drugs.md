# Cluster D4_05 Drugs costs (NHS Trusts)

Scope: 191 trust drug-cost sub-lines · total £10.76B

## Task

Each depth-4 "Drug Costs" sub-line under a specific NHS Trust needs a hand-curated Tier A entry that is TAILOR-MADE per-entity. NO generic template fallback. NO shared content.

```python
NEW = {
    "Drug Costs — Royal Cornwall Hospitals NHS Trust": {
        "aliases": [{"name": "Drug Costs", "parent": "Royal Cornwall Hospitals NHS Trust"}],
        "description": "2-3 sentences: trust-specific drug-spend context (formulary posture · high-cost drugs share · biosimilar uptake · specialty mix)",
        "beneficiaries": "Patients served by the trust's pharmacy-dispensed and ward-administered drugs",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · Health and Care Act 2022 (drug commissioning) · NICE TAs (funding mandate) · specific commissioning context",
        "key_stats": [...],  # 6-10 trust-specific stats
        "notes": "2-4 sentences: trust-specific drug-spend drivers (cancer drugs growth · high-cost devices · homecare insourcing · PbR reimbursement mix)",
        "sources": [...],  # 2-3 URLs
        "related": ["<trust name>", "Clinical Supplies & Drugs — <trust>"]
    }
}
```

## Rules
- Em-dash separator ` — ` (U+2014 with spaces) in composite keys
- Scoped alias parent = TRUST NAME exactly
- Every source with working URL (trust annual report · NHS Digital · NHS England · manufacturer-specific refs if relevant)
- 6-10 key_stats per entry, trust-specific
- Drug-spend narrative should reflect:
  * Oncology share (MHRA-licensed new tumour agents growing ~8-12%/yr)
  * High-cost drugs list (HCDs commissioned directly by ICB/specialised commissioning, not in trust tariff)
  * Biosimilar penetration (adalimumab · rituximab · trastuzumab switches)
  * Cancer Drugs Fund (£340M 2024-25 national · not in trust Drug Costs)
  * Homecare medicines (direct-to-patient, impacting trust bill)
- Each entry's `notes` must include specific operational context (which specialties drive spend · any recent shortage · procurement consortium)

## Output
Write your file as `scripts/D4_05_drugs_<batch>.py` where <batch> is A / B / C / D (depending which brief slice the agent handled) — with a single `NEW = { ... }` direct dict literal. No `if __name__ == '__main__'` block.

## Trust-specific anchors (reference these in narratives)

Category spread of this brief:
- **NHS Acute Trusts**: 118 trusts
- **NHS Mental Health Trusts**: 42 trusts
- **NHS Specialist Trusts**: 15 trusts
- **NHS Community Trusts**: 13 trusts
- **NHS Ambulance Trusts**: 3 trusts

## Sub-lines in this cluster

### Drug Costs — University Hospitals Birmingham NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals Birmingham NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £349.63M

### Drug Costs — Guy's & St Thomas' NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Guy's & St Thomas' NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £340.08M

### Drug Costs — The Leeds Teaching Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: The Leeds Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £301.55M

### Drug Costs — Manchester University NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Manchester University NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £297.90M

### Drug Costs — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £277.70M

### Drug Costs — University College London Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: University College London Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £266.54M

### Drug Costs — Royal Free London NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Royal Free London NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £262.04M

### Drug Costs — Sheffield Teaching Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Sheffield Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £240.90M

### Drug Costs — Barts Health NHS Trust
  sub-line type: Drug Costs
  parent trust: Barts Health NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £229.06M

### Drug Costs — King’s College Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: King’s College Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £222.78M

### Drug Costs — Oxford University Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Oxford University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £206.88M

### Drug Costs — Cambridge University Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Cambridge University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £206.34M

### Drug Costs — Northern Care Alliance NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Northern Care Alliance NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £205.51M

### Drug Costs — University Hospital Southampton NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: University Hospital Southampton NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £195.37M

### Drug Costs — Nottingham University Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: Nottingham University Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £192.75M

### Drug Costs — University Hospitals Bristol and Weston NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals Bristol and Weston NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £183.21M

### Drug Costs — Imperial College Healthcare NHS Trust
  sub-line type: Drug Costs
  parent trust: Imperial College Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £161.47M

### Drug Costs — University Hospitals of Leicester NHS Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals of Leicester NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £152.81M

### Drug Costs — University Hospitals Sussex NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals Sussex NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £151.10M

### Drug Costs — Royal Devon University Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Royal Devon University Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £126.54M

### Drug Costs — Hull University Teaching Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: Hull University Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £124.27M

### Drug Costs — Mid and South Essex NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Mid and South Essex NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £123.80M

### Drug Costs — University Hospitals of North Midlands NHS Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals of North Midlands NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £122.92M

### Drug Costs — The Christie NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Christie NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £121.96M

### Drug Costs — Portsmouth Hospitals University NHS Trust
  sub-line type: Drug Costs
  parent trust: Portsmouth Hospitals University NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £121.43M

### Drug Costs — University Hospitals of Derby and Burton NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals of Derby and Burton NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £117.53M

### Drug Costs — The Royal Marsden NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Royal Marsden NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £115.77M

### Drug Costs — Great Ormond Street Hospital for Children NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Great Ormond Street Hospital for Children NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £111.52M

### Drug Costs — Norfolk and Norwich University Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Norfolk and Norwich University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £107.63M

### Drug Costs — Liverpool University Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Liverpool University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £107.19M

### Drug Costs — The Clatterbridge Cancer Centre NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Clatterbridge Cancer Centre NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £106.53M

### Drug Costs — St George's University Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: St George's University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £100.84M

### Drug Costs — University Hospitals Plymouth NHS Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals Plymouth NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £98.93M

### Drug Costs — Gloucestershire Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Gloucestershire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £97.40M

### Drug Costs — South Tees Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: South Tees Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £95.75M

### Drug Costs — East Kent Hospitals University NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: East Kent Hospitals University NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £95.37M

### Drug Costs — Frimley Health NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Frimley Health NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £94.52M

### Drug Costs — East Suffolk and North Essex NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: East Suffolk and North Essex NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £92.84M

### Drug Costs — London North West University Healthcare NHS Trust
  sub-line type: Drug Costs
  parent trust: London North West University Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £85.47M

### Drug Costs — Chelsea and Westminster Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Chelsea and Westminster Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £84.93M

### Drug Costs — Somerset NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Somerset NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £84.91M

### Drug Costs — University Hospitals Coventry And Warwickshire NHS Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals Coventry And Warwickshire NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £82.38M

### Drug Costs — University Hospitals Dorset NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals Dorset NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £80.98M

### Drug Costs — The Royal Wolverhampton NHS Trust
  sub-line type: Drug Costs
  parent trust: The Royal Wolverhampton NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £77.94M

### Drug Costs — Royal Cornwall Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: Royal Cornwall Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £77.25M

### Drug Costs — Lancashire Teaching Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Lancashire Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £75.06M

### Drug Costs — North Bristol NHS Trust
  sub-line type: Drug Costs
  parent trust: North Bristol NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £74.94M

### Drug Costs — East And North Hertfordshire NHS Trust
  sub-line type: Drug Costs
  parent trust: East And North Hertfordshire NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £73.59M

### Drug Costs — Maidstone And Tunbridge Wells NHS Trust
  sub-line type: Drug Costs
  parent trust: Maidstone And Tunbridge Wells NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £73.01M

### Drug Costs — York and Scarborough Teaching Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: York and Scarborough Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £72.89M

### Drug Costs — United Lincolnshire Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: United Lincolnshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £71.20M

### Drug Costs — Bedfordshire Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Bedfordshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £70.59M

### Drug Costs — Royal Surrey NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Royal Surrey NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £67.01M

### Drug Costs — Royal Berkshire NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Royal Berkshire NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £65.23M

### Drug Costs — Worcestershire Acute Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: Worcestershire Acute Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £63.35M

### Drug Costs — South Tyneside and Sunderland NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: South Tyneside and Sunderland NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £63.10M

### Drug Costs — Hampshire Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Hampshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £62.67M

### Drug Costs — East Sussex Healthcare NHS Trust
  sub-line type: Drug Costs
  parent trust: East Sussex Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £60.68M

### Drug Costs — North West Anglia NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: North West Anglia NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £60.65M

### Drug Costs — Blackpool Teaching Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Blackpool Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £56.76M

### Drug Costs — The Shrewsbury and Telford Hospital NHS Trust
  sub-line type: Drug Costs
  parent trust: The Shrewsbury and Telford Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £56.29M

### Drug Costs — Royal United Hospitals Bath NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Royal United Hospitals Bath NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £56.10M

### Drug Costs — Buckinghamshire Healthcare NHS Trust
  sub-line type: Drug Costs
  parent trust: Buckinghamshire Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £55.43M

### Drug Costs — East Lancashire Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: East Lancashire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £55.34M

### Drug Costs — North Cumbria Integrated Care NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: North Cumbria Integrated Care NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £54.09M

### Drug Costs — County Durham and Darlington NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: County Durham and Darlington NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £53.99M

### Drug Costs — Bradford Teaching Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Bradford Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £53.76M

### Drug Costs — The Mid Yorkshire Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: The Mid Yorkshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £52.61M

### Drug Costs — Royal Papworth Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Royal Papworth Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £52.08M

### Drug Costs — Oxford Health NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Oxford Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £52.06M

### Drug Costs — Alder Hey Children's NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Alder Hey Children's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £51.66M

### Drug Costs — Lewisham and Greenwich NHS Trust
  sub-line type: Drug Costs
  parent trust: Lewisham and Greenwich NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £49.46M

### Drug Costs — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £48.50M

### Drug Costs — The Dudley Group NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Dudley Group NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £47.26M

### Drug Costs — Calderdale and Huddersfield NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Calderdale and Huddersfield NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £45.82M

### Drug Costs — Torbay and South Devon NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Torbay and South Devon NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £45.03M

### Drug Costs — Great Western Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Great Western Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £44.68M

### Drug Costs — Sandwell And West Birmingham Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: Sandwell And West Birmingham Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £42.88M

### Drug Costs — South Warwickshire NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: South Warwickshire NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £42.87M

### Drug Costs — Moorfields Eye Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Moorfields Eye Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £42.56M

### Drug Costs — Northumbria Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Northumbria Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £42.38M

### Drug Costs — Northampton General Hospital NHS Trust
  sub-line type: Drug Costs
  parent trust: Northampton General Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £40.20M

### Drug Costs — University Hospitals of Morecambe Bay NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: University Hospitals of Morecambe Bay NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £40.17M

### Drug Costs — Medway NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Medway NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £39.76M

### Drug Costs — Mersey and West Lancashire Teaching Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: Mersey and West Lancashire Teaching Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £38.79M

### Drug Costs — Northern Lincolnshire and Goole NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Northern Lincolnshire and Goole NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £37.95M

### Drug Costs — Epsom and St Helier University Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: Epsom and St Helier University Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £35.24M

### Drug Costs — Surrey And Sussex Healthcare NHS Trust
  sub-line type: Drug Costs
  parent trust: Surrey And Sussex Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £34.86M

### Drug Costs — Kettering General Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Kettering General Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £34.51M

### Drug Costs — Sheffield Children's NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Sheffield Children's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £34.12M

### Drug Costs — Liverpool Heart and Chest Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Liverpool Heart and Chest Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £33.46M

### Drug Costs — Milton Keynes University Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Milton Keynes University Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £32.71M

### Drug Costs — Salisbury NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Salisbury NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £32.09M

### Drug Costs — Wrightington, Wigan and Leigh NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Wrightington, Wigan and Leigh NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £31.66M

### Drug Costs — Wye Valley NHS Trust
  sub-line type: Drug Costs
  parent trust: Wye Valley NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £30.59M

### Drug Costs — Sherwood Forest Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Sherwood Forest Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £30.39M

### Drug Costs — Dartford and Gravesham NHS Trust
  sub-line type: Drug Costs
  parent trust: Dartford and Gravesham NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £30.05M

### Drug Costs — The Walton Centre NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Walton Centre NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £29.97M

### Drug Costs — Wirral University Teaching Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Wirral University Teaching Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £29.91M

### Drug Costs — Chesterfield Royal Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Chesterfield Royal Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £29.44M

### Drug Costs — West Hertfordshire Hospitals NHS Trust
  sub-line type: Drug Costs
  parent trust: West Hertfordshire Hospitals NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £29.35M

### Drug Costs — Ashford and St Peter's Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Ashford and St Peter's Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £29.01M

### Drug Costs — Kingston Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Kingston Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £29.00M

### Drug Costs — North Middlesex University Hospital NHS Trust
  sub-line type: Drug Costs
  parent trust: North Middlesex University Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £28.32M

### Drug Costs — West Suffolk NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: West Suffolk NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £28.29M

### Drug Costs — Central and North West London NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Central and North West London NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £27.76M

### Drug Costs — North Tees and Hartlepool NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: North Tees and Hartlepool NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £27.29M

### Drug Costs — Bolton NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Bolton NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £27.27M

### Drug Costs — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £26.59M

### Drug Costs — Countess of Chester Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Countess of Chester Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £26.49M

### Drug Costs — The Princess Alexandra Hospital NHS Trust
  sub-line type: Drug Costs
  parent trust: The Princess Alexandra Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £26.26M

### Drug Costs — Walsall Healthcare NHS Trust
  sub-line type: Drug Costs
  parent trust: Walsall Healthcare NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £25.82M

### Drug Costs — Dorset County Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Dorset County Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £25.56M

### Drug Costs — James Paget University Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: James Paget University Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £25.17M

### Drug Costs — Mid Cheshire Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Mid Cheshire Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £24.23M

### Drug Costs — Stockport NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Stockport NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £23.03M

### Drug Costs — Gateshead Health NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Gateshead Health NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £22.73M

### Drug Costs — Harrogate and District NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Harrogate and District NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £22.67M

### Drug Costs — The Rotherham NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Rotherham NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £22.45M

### Drug Costs — The Hillingdon Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Hillingdon Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £21.35M

### Drug Costs — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Warrington and Halton Teaching Hospitals NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £21.24M

### Drug Costs — Isle of Wight NHS Trust
  sub-line type: Drug Costs
  parent trust: Isle of Wight NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £21.06M

### Drug Costs — Homerton Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Homerton Healthcare NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £20.52M

### Drug Costs — Barnsley Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Barnsley Hospital NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £19.87M

### Drug Costs — Midlands Partnership NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Midlands Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £18.77M

### Drug Costs — George Eliot Hospital NHS Trust
  sub-line type: Drug Costs
  parent trust: George Eliot Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £17.92M

### Drug Costs — Airedale NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Airedale NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £17.88M

### Drug Costs — Whittington Health NHS Trust
  sub-line type: Drug Costs
  parent trust: Whittington Health NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £16.47M

### Drug Costs — Oxleas NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Oxleas NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £14.63M

### Drug Costs — Birmingham Community Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Birmingham Community Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £11.23M

### Drug Costs — Tameside and Glossop Integrated Care NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Tameside and Glossop Integrated Care NHS Foundation Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £10.22M

### Drug Costs — Solent NHS Trust
  sub-line type: Drug Costs
  parent trust: Solent NHS Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £10.11M

### Drug Costs — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £9.69M

### Drug Costs — South London and Maudsley NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: South London and Maudsley NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £8.60M

### Drug Costs — East Cheshire NHS Trust
  sub-line type: Drug Costs
  parent trust: East Cheshire NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £8.48M

### Drug Costs — Cambridgeshire Community Services NHS Trust
  sub-line type: Drug Costs
  parent trust: Cambridgeshire Community Services NHS Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £8.02M

### Drug Costs — Coventry and Warwickshire Partnership NHS Trust
  sub-line type: Drug Costs
  parent trust: Coventry and Warwickshire Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £7.45M

### Drug Costs — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £7.33M

### Drug Costs — Birmingham and Solihull Mental Health NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Birmingham and Solihull Mental Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £7.23M

### Drug Costs — Northamptonshire Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Northamptonshire Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £6.82M

### Drug Costs — Nottinghamshire Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Nottinghamshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £6.69M

### Drug Costs — Mersey Care NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Mersey Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £6.61M

### Drug Costs — Lancashire and South Cumbria NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Lancashire and South Cumbria NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £6.57M

### Drug Costs — Dorset Healthcare University NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Dorset Healthcare University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £6.48M

### Drug Costs — Berkshire Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Berkshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £6.40M

### Drug Costs — Sussex Partnership NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Sussex Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £6.00M

### Drug Costs — Greater Manchester Mental Health NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Greater Manchester Mental Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £5.66M

### Drug Costs — Essex Partnership University NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Essex Partnership University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £5.37M

### Drug Costs — Tees, Esk and Wear Valleys NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Tees, Esk and Wear Valleys NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £5.32M

### Drug Costs — Black Country Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Black Country Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.70M

### Drug Costs — North East London NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: North East London NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.63M

### Drug Costs — West London NHS Trust
  sub-line type: Drug Costs
  parent trust: West London NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.52M

### Drug Costs — Gloucestershire Health and Care NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Gloucestershire Health and Care NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.51M

### Drug Costs — Kent Community Health NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Kent Community Health NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.42M

### Drug Costs — Royal National Orthopaedic Hospital NHS Trust
  sub-line type: Drug Costs
  parent trust: Royal National Orthopaedic Hospital NHS Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.40M

### Drug Costs — Derbyshire Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Derbyshire Healthcare NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.37M

### Drug Costs — Southern Health NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Southern Health NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.28M

### Drug Costs — Leicestershire Partnership NHS Trust
  sub-line type: Drug Costs
  parent trust: Leicestershire Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.20M

### Drug Costs — Hertfordshire Partnership University NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Hertfordshire Partnership University NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £4.14M

### Drug Costs — South West Yorkshire Partnership NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: South West Yorkshire Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.98M

### Drug Costs — Surrey and Borders Partnership NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Surrey and Borders Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.92M

### Drug Costs — Liverpool Women's NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Liverpool Women's NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.92M

### Drug Costs — Kent and Medway NHS and Social Care Partnership Trust
  sub-line type: Drug Costs
  parent trust: Kent and Medway NHS and Social Care Partnership Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.77M

### Drug Costs — Avon and Wiltshire Mental Health Partnership NHS Trust
  sub-line type: Drug Costs
  parent trust: Avon and Wiltshire Mental Health Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.76M

### Drug Costs — Barnet, Enfield And Haringey Mental Health NHS Trust
  sub-line type: Drug Costs
  parent trust: Barnet, Enfield And Haringey Mental Health NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.73M

### Drug Costs — Lincolnshire Community Health Services NHS Trust
  sub-line type: Drug Costs
  parent trust: Lincolnshire Community Health Services NHS Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.66M

### Drug Costs — Sussex Community NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Sussex Community NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.63M

### Drug Costs — Norfolk and Suffolk NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Norfolk and Suffolk NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.17M

### Drug Costs — Rotherham Doncaster and South Humber NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Rotherham Doncaster and South Humber NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £3.17M

### Drug Costs — Camden and Islington NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Camden and Islington NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.79M

### Drug Costs — Cornwall Partnership NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Cornwall Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.54M

### Drug Costs — Southport And Ormskirk Hospital NHS Trust
  sub-line type: Drug Costs
  parent trust: Southport And Ormskirk Hospital NHS Trust
  trust category: NHS Acute Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.52M

### Drug Costs — North Staffordshire Combined Healthcare NHS Trust
  sub-line type: Drug Costs
  parent trust: North Staffordshire Combined Healthcare NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.49M

### Drug Costs — Bridgewater Community Healthcare NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Bridgewater Community Healthcare NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.42M

### Drug Costs — Pennine Care NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Pennine Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.41M

### Drug Costs — Herefordshire and Worcestershire Health and Care NHS Trust
  sub-line type: Drug Costs
  parent trust: Herefordshire and Worcestershire Health and Care NHS Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.39M

### Drug Costs — Derbyshire Community Health Services NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Derbyshire Community Health Services NHS Foundation Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.35M

### Drug Costs — South West London and St George's Mental Health NHS Trust
  sub-line type: Drug Costs
  parent trust: South West London and St George's Mental Health NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.35M

### Drug Costs — Leeds and York Partnership NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Leeds and York Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.23M

### Drug Costs — Devon Partnership NHS Trust
  sub-line type: Drug Costs
  parent trust: Devon Partnership NHS Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.21M

### Drug Costs — Cheshire and Wirral Partnership NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Cheshire and Wirral Partnership NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £2.06M

### Drug Costs — North West Ambulance Service NHS Trust
  sub-line type: Drug Costs
  parent trust: North West Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.97M

### Drug Costs — The Royal Orthopaedic Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: The Royal Orthopaedic Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.92M

### Drug Costs — Central London Community Healthcare NHS Trust
  sub-line type: Drug Costs
  parent trust: Central London Community Healthcare NHS Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.79M

### Drug Costs — Shropshire Community Health NHS Trust
  sub-line type: Drug Costs
  parent trust: Shropshire Community Health NHS Trust
  trust category: NHS Community Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.69M

### Drug Costs — East of England Ambulance Service NHS Trust
  sub-line type: Drug Costs
  parent trust: East of England Ambulance Service NHS Trust
  trust category: NHS Ambulance Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.64M

### Drug Costs — South East Coast Ambulance Service NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: South East Coast Ambulance Service NHS Foundation Trust
  trust category: NHS Ambulance Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.50M

### Drug Costs — Queen Victoria Hospital NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Queen Victoria Hospital NHS Foundation Trust
  trust category: NHS Specialist Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.49M

### Drug Costs — Cambridgeshire and Peterborough NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Cambridgeshire and Peterborough NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.42M

### Drug Costs — Bradford District Care NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Bradford District Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.31M

### Drug Costs — Sheffield Health and Social Care NHS Foundation Trust
  sub-line type: Drug Costs
  parent trust: Sheffield Health and Social Care NHS Foundation Trust
  trust category: NHS Mental Health Trusts
  parent line: Clinical Supplies & Drugs
  value: £1.09M

