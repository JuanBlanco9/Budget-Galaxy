# Cluster Phase2_MH_slice2 — NHS Mental Health Trust orphan sub-lines (lower-£ tail)

Scope: 239 orphan depth-5 sub-lines under NHS MH Trusts that weren't covered by slice 1 (top-£ 200) · total £0.30B

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
"<sub-line> — <MH trust>": {
    "aliases": [{"name": "<sub-line>", "parent": "<MH trust>"}],
    "description": "3-5 sentences, 250-600 chars · trust-specific (sub-line-type-specific drivers, with the trust's specialty mix as anchor)",
    "beneficiaries": "1-2 sentences with CONCRETE N (sites for business rates · users on rolled-out EPR for amortisation · etc)",
    "legal_basis": "[sub-line-type-specific] · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 + applicable IAS/IFRS",
    "key_stats": [...],  # 8-12 trust-specific
    "notes": "3-5 sentences, 300-800 chars · trust-specific drivers + recent context",
    "sources": [...],  # 4-6 dicts {publisher, title, url} https://
    "related": [...]   # 3-6 cross-links (incl. parent line + relevant policy programme + peer trust)
}
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
- `sources` MUST be list of dicts {publisher, title, url} https://
- 8-12 stats · 4-6 sources · 3-6 related · 3-5 sentence notes (300-800) · 3-5 sentence description (250-600)
- All 6 PROGRAMME dimensions present
- Watchdog-safe incremental Edit (skeleton + per-entry inserts)

## Sub-lines in this cluster

### Business rates — Central and North West London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.32M

### Establishment costs — Bradford District Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.23M

### Transport (business + patient) — Greater Manchester Mental Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.23M

### Lease expenditure — Mersey Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.19M

### Transport (business + patient) — Norfolk and Suffolk NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.16M

### Transport (business + patient) — Leicestershire Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £3.12M

### Establishment costs — Berkshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.07M

### Establishment costs — Tavistock and Portman NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.05M

### PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.02M

### Transport (business + patient) — Coventry and Warwickshire Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £2.99M

### Establishment costs — Surrey and Borders Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.98M

### Establishment costs — Leeds and York Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.96M

### PFI / LIFT charges — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.96M

### Establishment costs — Kent and Medway NHS and Social Care Partnership Trust
  parent line: Premises & Infrastructure
  value: £2.96M

### Transport (business + patient) — Cambridgeshire and Peterborough NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.95M

### Business rates — Mersey Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.85M

### Establishment costs — Devon Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £2.83M

### Establishment costs — South London and Maudsley NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.81M

### General supplies & services — Sheffield Health and Social Care NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.77M

### Transport (business + patient) — Derbyshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.76M

### Establishment costs — Dorset Healthcare University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.75M

### Transport (business + patient) — Surrey and Borders Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.74M

### General supplies & services — Leeds and York Partnership NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.73M

### Establishment costs — Essex Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.70M

### Lease expenditure — Oxford Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.70M

### Transport (business + patient) — Rotherham Doncaster and South Humber NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.68M

### Transport (business + patient) — Pennine Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.66M

### PFI / LIFT charges — Cambridgeshire and Peterborough NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.64M

### Amortisation — Oxford Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.63M

### Establishment costs — Avon and Wiltshire Mental Health Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £2.62M

### Impairments net of reversals — Leeds and York Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.54M

### Amortisation — Mersey Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.49M

### PFI / LIFT charges — Avon and Wiltshire Mental Health Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £2.48M

### Business rates — Surrey and Borders Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.38M

### Amortisation — Essex Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.37M

### General supplies & services — Devon Partnership NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £2.36M

### Establishment costs — Black Country Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.35M

### Establishment costs — North East London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.34M

### General supplies & services — Rotherham Doncaster and South Humber NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.32M

### Business rates — Southern Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.28M

### Transport (business + patient) — South London and Maudsley NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.23M

### Business rates — West London NHS Trust
  parent line: Premises & Infrastructure
  value: £2.19M

### Transport (business + patient) — Barnet, Enfield And Haringey Mental Health NHS Trust
  parent line: Premises & Infrastructure
  value: £2.17M

### Business rates — Tees, Esk and Wear Valleys NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.17M

### Business rates — Midlands Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.14M

### Impairments net of reversals — South London and Maudsley NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.13M

### Establishment costs — Rotherham Doncaster and South Humber NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.12M

### Transport (business + patient) — Birmingham and Solihull Mental Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.11M

### PFI / LIFT charges — Essex Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.11M

### Establishment costs — Camden and Islington NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.09M

### Business rates — Nottinghamshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.04M

### Business rates — South London and Maudsley NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.03M

### Business rates — Norfolk and Suffolk NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.01M

### Transport (business + patient) — Berkshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.99M

### Amortisation — Sussex Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.97M

### Business rates — Essex Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.96M

### Business rates — Lancashire and South Cumbria NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.95M

### Establishment costs — Cornwall Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.94M

### Establishment costs — Pennine Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.93M

### Impairments net of reversals — Hertfordshire Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.91M

### Amortisation — Dorset Healthcare University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.90M

### Impairments net of reversals — North East London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.86M

### Impairments net of reversals — Bradford District Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.81M

### Transport (business + patient) — Leeds and York Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.81M

### Business rates — Oxleas NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.80M

### Lease expenditure — Leicestershire Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £1.78M

### Social security & levy — Dudley Integrated Health and Care NHS Trust
  parent line: Staff Costs
  value: £1.77M

### Business rates — Dorset Healthcare University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.77M

### General supplies & services — Bradford District Care NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.77M

### Establishment costs — Lincolnshire Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.76M

### Transport (business + patient) — West London NHS Trust
  parent line: Premises & Infrastructure
  value: £1.73M

### Lease expenditure — Essex Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.73M

### General supplies & services — Cheshire and Wirral Partnership NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.72M

### Transport (business + patient) — Mersey Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.71M

### General supplies & services — Pennine Care NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.70M

### Amortisation — Birmingham and Solihull Mental Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.70M

### Lease expenditure — Oxleas NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.66M

### Business rates — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.64M

### Transport (business + patient) — Nottinghamshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.63M

### Transport (business + patient) — Oxleas NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.63M

### Transport (business + patient) — Cheshire and Wirral Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.62M

### Lease expenditure — Black Country Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.62M

### Business rates — Leicestershire Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £1.60M

### Amortisation — South West London and St George's Mental Health NHS Trust
  parent line: Premises & Infrastructure
  value: £1.56M

### PFI / LIFT charges — Norfolk and Suffolk NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.55M

### PFI / LIFT charges — North East London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.54M

### Business rates — Kent and Medway NHS and Social Care Partnership Trust
  parent line: Premises & Infrastructure
  value: £1.54M

### Transport (business + patient) — Sheffield Health and Social Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.54M

### Amortisation — Black Country Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.54M

### Business rates — South West London and St George's Mental Health NHS Trust
  parent line: Premises & Infrastructure
  value: £1.53M

### Business rates — Oxford Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.52M

### Establishment costs — Cheshire and Wirral Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.51M

### Impairments net of reversals — Derbyshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.49M

### Transport (business + patient) — Black Country Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.46M

### Lease expenditure — Hertfordshire Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.45M

### Amortisation — Greater Manchester Mental Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.40M

### PFI / LIFT charges — Derbyshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.39M

### Establishment costs — Norfolk and Suffolk NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.37M

### Business rates — Cornwall Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.35M

### Amortisation — Leicestershire Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £1.33M

### Business rates — Sussex Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.33M

### Lease expenditure — Lancashire and South Cumbria NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.33M

### Amortisation — Kent and Medway NHS and Social Care Partnership Trust
  parent line: Premises & Infrastructure
  value: £1.32M

### Business rates — Tavistock and Portman NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.30M

### Amortisation — Berkshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.28M

### Transport (business + patient) — South West London and St George's Mental Health NHS Trust
  parent line: Premises & Infrastructure
  value: £1.23M

### Establishment costs — South West London and St George's Mental Health NHS Trust
  parent line: Premises & Infrastructure
  value: £1.22M

### Business rates — Pennine Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.22M

### Business rates — Camden and Islington NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.22M

### PFI / LIFT charges — Pennine Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.20M

### Amortisation — Oxleas NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.20M

### PFI / LIFT charges — Southern Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.19M

### Lease expenditure — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.16M

### Business rates — South West Yorkshire Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.16M

### Transport (business + patient) — North Staffordshire Combined Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £1.14M

### Business rates — Avon and Wiltshire Mental Health Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £1.13M

### Impairments net of reversals — Cornwall Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.13M

### PFI / LIFT charges — Lancashire and South Cumbria NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.12M

### Lease expenditure — Midlands Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.12M

### PFI / LIFT charges — Oxleas NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.11M

### General supplies & services — Derbyshire Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.09M

### Business rates — Birmingham and Solihull Mental Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.09M

### Business rates — Berkshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.06M

### Amortisation — Southern Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.04M

### Business rates — Leeds and York Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.03M

### Business rates — Hertfordshire Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.02M

### PFI / LIFT charges — Sussex Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.00M

### General supplies & services — Lancashire and South Cumbria NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.00M

### Business rates — North East London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.99M

### Impairments net of reversals — Barnet, Enfield And Haringey Mental Health NHS Trust
  parent line: Premises & Infrastructure
  value: £0.99M

### Amortisation — Nottinghamshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.98M

### Drugs costs — Lincolnshire Partnership NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.97M

### Lease expenditure — Dorset Healthcare University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.97M

### Establishment costs — Hertfordshire Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.95M

### Business rates — Black Country Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.94M

### Impairments net of reversals — Nottinghamshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.92M

### Lease expenditure — Pennine Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.92M

### PFI / LIFT charges — Mersey Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.91M

### Termination & post-employment — Nottinghamshire Healthcare NHS Foundation Trust
  parent line: Staff Costs
  value: £0.91M

### Transport (business + patient) — Lancashire and South Cumbria NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.91M

### Business rates — Coventry and Warwickshire Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.90M

### General supplies & services — Berkshire Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.89M

### Business rates — Derbyshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.89M

### Business rates — Cambridgeshire and Peterborough NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.87M

### Amortisation — Devon Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.85M

### Business rates — Lincolnshire Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.84M

### Clinical supplies & services — South West London and St George's Mental Health NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.82M

### PFI / LIFT charges — Oxford Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.82M

### Clinical supplies & services — Hertfordshire Partnership University NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.80M

### Amortisation — Cambridgeshire and Peterborough NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.77M

### Transport (business + patient) — Bradford District Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.76M

### PFI / LIFT charges — Tees, Esk and Wear Valleys NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.75M

### Lease expenditure — Derbyshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.74M

### Amortisation — Derbyshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.74M

### Lease expenditure — Avon and Wiltshire Mental Health Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.73M

### PFI / LIFT charges — Kent and Medway NHS and Social Care Partnership Trust
  parent line: Premises & Infrastructure
  value: £0.73M

### Clinical supplies & services — Surrey and Borders Partnership NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.72M

### Lease expenditure — Kent and Medway NHS and Social Care Partnership Trust
  parent line: Premises & Infrastructure
  value: £0.71M

### Amortisation — Lancashire and South Cumbria NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.71M

### Business rates — Cheshire and Wirral Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.69M

### Lease expenditure — Greater Manchester Mental Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.68M

### Business rates — Sheffield Health and Social Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.68M

### Lease expenditure — Surrey and Borders Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.67M

### Transport (business + patient) — Camden and Islington NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.66M

### Establishment costs — Sheffield Health and Social Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.66M

### Business rates — Barnet, Enfield And Haringey Mental Health NHS Trust
  parent line: Premises & Infrastructure
  value: £0.64M

### Business rates — Greater Manchester Mental Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.63M

### Clinical supplies & services — Tavistock and Portman NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.63M

### Business rates — Devon Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.62M

### Business rates — Rotherham Doncaster and South Humber NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.61M

### Lease expenditure — Birmingham and Solihull Mental Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.61M

### Lease expenditure — West London NHS Trust
  parent line: Premises & Infrastructure
  value: £0.59M

### Impairments net of reversals — Devon Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.56M

### Establishment costs — North Staffordshire Combined Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.56M

### PFI / LIFT charges — Leicestershire Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.55M

### Lease expenditure — Cambridgeshire and Peterborough NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.55M

### Impairments net of reversals — Birmingham and Solihull Mental Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.54M

### Lease expenditure — Cheshire and Wirral Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.54M

### Amortisation — Rotherham Doncaster and South Humber NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.53M

### Business rates — Bradford District Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.52M

### PFI / LIFT charges — Bradford District Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.52M

### Lease expenditure — Coventry and Warwickshire Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.46M

### Lease expenditure — Devon Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.43M

### Termination & post-employment — Southern Health NHS Foundation Trust
  parent line: Staff Costs
  value: £0.43M

### Amortisation — Barnet, Enfield And Haringey Mental Health NHS Trust
  parent line: Premises & Infrastructure
  value: £0.41M

### PFI / LIFT charges — Black Country Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.41M

### Business rates — North Staffordshire Combined Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.41M

### Amortisation — Hertfordshire Partnership University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.40M

### Termination & post-employment — Sheffield Health and Social Care NHS Foundation Trust
  parent line: Staff Costs
  value: £0.38M

### Lease expenditure — Central and North West London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.37M

### Amortisation — Sheffield Health and Social Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.35M

### Clinical supplies & services — Derbyshire Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.35M

### Amortisation — Pennine Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.34M

### Establishment costs — Dudley Integrated Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £0.34M

### Lease expenditure — Berkshire Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.33M

### Amortisation — Midlands Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.32M

### Amortisation — North Staffordshire Combined Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.32M

### Clinical supplies & services — Birmingham and Solihull Mental Health NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.32M

### Termination & post-employment — Dudley Integrated Health and Care NHS Trust
  parent line: Staff Costs
  value: £0.31M

### Drugs costs — Tavistock and Portman NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.30M

### Clinical supplies & services — Sheffield Health and Social Care NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.30M

### Clinical supplies & services — Camden and Islington NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.30M

### Amortisation — Leeds and York Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.29M

### Lease expenditure — Sussex Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.29M

### Amortisation — Cornwall Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.28M

### Clinical supplies & services — North Staffordshire Combined Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.27M

### Termination & post-employment — Kent and Medway NHS and Social Care Partnership Trust
  parent line: Staff Costs
  value: £0.27M

### Amortisation — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.26M

### Amortisation — Coventry and Warwickshire Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.26M

### Lease expenditure — Lincolnshire Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.26M

### Amortisation — North East London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.25M

### Amortisation — Avon and Wiltshire Mental Health Partnership NHS Trust
  parent line: Premises & Infrastructure
  value: £0.25M

### Impairments net of reversals — Cheshire and Wirral Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.24M

### Lease expenditure — Sheffield Health and Social Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.22M

### Inventories written down — Barnet, Enfield And Haringey Mental Health NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.22M

### General supplies & services — North Staffordshire Combined Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.22M

### Impairments net of reversals — Dorset Healthcare University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.21M

### Amortisation — South London and Maudsley NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.20M

### Termination & post-employment — Leicestershire Partnership NHS Trust
  parent line: Staff Costs
  value: £0.20M

### Other & adjustments — Central and North West London NHS Foundation Trust
  parent line: Staff Costs
  value: £0.20M

### Other & adjustments — Birmingham and Solihull Mental Health NHS Foundation Trust
  parent line: Staff Costs
  value: £0.20M

### Other & adjustments — North East London NHS Foundation Trust
  parent line: Staff Costs
  value: £0.20M

### Lease expenditure — North Staffordshire Combined Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.19M

### Other & adjustments — South London and Maudsley NHS Foundation Trust
  parent line: Staff Costs
  value: £0.19M

### Termination & post-employment — Essex Partnership University NHS Foundation Trust
  parent line: Staff Costs
  value: £0.17M

### Termination & post-employment — Lincolnshire Partnership NHS Foundation Trust
  parent line: Staff Costs
  value: £0.17M

### General supplies & services — Dudley Integrated Health and Care NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.15M

### Amortisation — Dudley Integrated Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £0.15M

### Other & adjustments — Dudley Integrated Health and Care NHS Trust
  parent line: Staff Costs
  value: £0.15M

### Termination & post-employment — South West London and St George's Mental Health NHS Trust
  parent line: Staff Costs
  value: £0.15M

### Other & adjustments — North Staffordshire Combined Healthcare NHS Trust
  parent line: Staff Costs
  value: £0.14M

### Other & adjustments — Camden and Islington NHS Foundation Trust
  parent line: Staff Costs
  value: £0.14M

### Amortisation — Tavistock and Portman NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.13M

### Amortisation — Cheshire and Wirral Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.13M

### Lease expenditure — Leeds and York Partnership NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.13M

### Transport (business + patient) — Tavistock and Portman NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.12M

### Termination & post-employment — Avon and Wiltshire Mental Health Partnership NHS Trust
  parent line: Staff Costs
  value: £0.12M

### Amortisation — Bradford District Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.12M

### Impairments net of reversals — Dudley Integrated Health and Care NHS Trust
  parent line: Premises & Infrastructure
  value: £0.10M

