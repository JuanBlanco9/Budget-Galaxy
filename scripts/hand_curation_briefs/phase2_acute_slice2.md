# Cluster Phase2_Acute_slice2 — NHS Acute Trust orphan sub-lines (long-tail)

Scope: 791 orphan depth-5 sub-lines under NHS Acute Trusts not yet covered · total £4.12B

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
"<sub-line> — <Acute trust>": {
    "aliases": [{"name": "<sub-line>", "parent": "<Acute trust>"}],
    "description": "3-5 sentences, 250-600 chars · trust-specific (sub-line driver + trust specialty mix + ICS group context)",
    "beneficiaries": "1-2 sentences with CONCRETE N (sites · ED attendances · elective admissions · WTE)",
    "legal_basis": "<sub-line-type-specific> · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 · applicable IAS/IFRS",
    "key_stats": [...],  # 8-12 trust-specific
    "notes": "3-5 sentences, 300-800 chars trust-specific drivers + recent context",
    "sources": [...],  # 4-6 dicts {publisher, title, url} https://
    "related": [...]   # 3-6 cross-links (incl. parent line + relevant policy programme + peer trust + Premises (other) — <trust> cross-ref)
}
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
- `sources` MUST be list of dicts {publisher, title, url} https://
- 8-12 stats · 4-6 sources · 3-6 related · 3-5 sentence notes (300-800) · 3-5 sentence description (250-600)
- All 6 PROGRAMME dimensions present
- NO boilerplate placeholders
- Watchdog-safe incremental Edit (skeleton + per-entry inserts)

## Sub-lines in this cluster

### General supplies & services — Liverpool University Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £28.16M

### General supplies & services — North Middlesex University Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £27.99M

### PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £27.75M

### PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £27.56M

### Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £26.58M

### Social security & levy — Great Western Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £26.39M

### Transport (business + patient) — Imperial College Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £26.27M

### Social security & levy — Whittington Health NHS Trust
  parent line: Staff Costs
  value: £25.95M

### Social security & levy — Kingston Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £25.53M

### Social security & levy — South Warwickshire NHS Foundation Trust
  parent line: Staff Costs
  value: £25.27M

### General supplies & services — Worcestershire Acute Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £24.94M

### Social security & levy — West Suffolk NHS Foundation Trust
  parent line: Staff Costs
  value: £24.92M

### Social security & levy — Kettering General Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £24.91M

### Social security & levy — Stockport NHS Foundation Trust
  parent line: Staff Costs
  value: £24.83M

### General supplies & services — East Suffolk and North Essex NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £24.62M

### Social security & levy — Dartford and Gravesham NHS Trust
  parent line: Staff Costs
  value: £24.55M

### Social security & levy — Walsall Healthcare NHS Trust
  parent line: Staff Costs
  value: £24.49M

### General supplies & services — Bradford Teaching Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £24.23M

### General supplies & services — East Kent Hospitals University NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £23.94M

### Social security & levy — The Hillingdon Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £23.79M

### General supplies & services — Barts Health NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £23.50M

### PFI / LIFT charges — County Durham and Darlington NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £23.39M

### Social security & levy — Mid Cheshire Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £23.35M

### Social security & levy — Milton Keynes University Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £23.00M

### Establishment costs — Cambridge University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £22.63M

### Social security & levy — Countess of Chester Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £22.47M

### Social security & levy — North Tees and Hartlepool NHS Foundation Trust
  parent line: Staff Costs
  value: £22.16M

### Social security & levy — Gateshead Health NHS Foundation Trust
  parent line: Staff Costs
  value: £22.03M

### PFI / LIFT charges — University Hospitals Birmingham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £21.13M

### General supplies & services — Cambridge University Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £21.08M

### PFI / LIFT charges — The Mid Yorkshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £21.04M

### Social security & levy — Chesterfield Royal Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £20.90M

### Social security & levy — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £20.44M

### Establishment costs — University Hospitals Bristol and Weston NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £20.39M

### Social security & levy — Harrogate and District NHS Foundation Trust
  parent line: Staff Costs
  value: £20.38M

### Social security & levy — Tameside and Glossop Integrated Care NHS Foundation Trust
  parent line: Staff Costs
  value: £20.08M

### Transport (business + patient) — Guy's & St Thomas' NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £20.04M

### Social security & levy — Isle of Wight NHS Trust
  parent line: Staff Costs
  value: £19.74M

### Social security & levy — The Princess Alexandra Hospital NHS Trust
  parent line: Staff Costs
  value: £19.57M

### Business rates — Barts Health NHS Trust
  parent line: Premises & Infrastructure
  value: £19.52M

### Transport (business + patient) — Royal Free London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £19.51M

### PFI / LIFT charges — Chelsea and Westminster Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £19.47M

### Social security & levy — The Rotherham NHS Foundation Trust
  parent line: Staff Costs
  value: £19.41M

### General supplies & services — Imperial College Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £19.30M

### General supplies & services — Royal Cornwall Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £19.25M

### Social security & levy — James Paget University Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £19.18M

### Social security & levy — Salisbury NHS Foundation Trust
  parent line: Staff Costs
  value: £19.17M

### Social security & levy — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  parent line: Staff Costs
  value: £19.11M

### Establishment costs — South Warwickshire NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £19.01M

### Establishment costs — University Hospitals Birmingham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £18.42M

### General supplies & services — Hull University Teaching Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £18.31M

### Establishment costs — Royal Devon University Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £18.31M

### PFI / LIFT charges — North Cumbria Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £18.28M

### General supplies & services — West Hertfordshire Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £18.10M

### Establishment costs — Bedfordshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £17.78M

### Transport (business + patient) — Barts Health NHS Trust
  parent line: Premises & Infrastructure
  value: £17.64M

### Social security & levy — Barnsley Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £17.59M

### General supplies & services — University Hospitals of Leicester NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £17.59M

### Social security & levy — Wye Valley NHS Trust
  parent line: Staff Costs
  value: £17.45M

### General supplies & services — Mid and South Essex NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £17.37M

### PFI / LIFT charges — Calderdale and Huddersfield NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £17.27M

### General supplies & services — Royal Devon University Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £17.05M

### Establishment costs — Mid and South Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £17.01M

### Social security & levy — Airedale NHS Foundation Trust
  parent line: Staff Costs
  value: £16.93M

### Establishment costs — King’s College Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £16.69M

### Establishment costs — Manchester University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £16.64M

### PFI / LIFT charges — Great Western Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £16.44M

### Social security & levy — Dorset County Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £16.36M

### Establishment costs — Great Western Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £16.17M

### Establishment costs — Somerset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £15.72M

### General supplies & services — Homerton Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £15.60M

### General supplies & services — East And North Hertfordshire NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £15.58M

### Establishment costs — South Tees Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £15.51M

### General supplies & services — University Hospitals Dorset NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £15.06M

### PFI / LIFT charges — Wye Valley NHS Trust
  parent line: Premises & Infrastructure
  value: £14.78M

### General supplies & services — University Hospitals Bristol and Weston NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £14.74M

### Transport (business + patient) — King’s College Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £14.12M

### General supplies & services — Manchester University NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £14.11M

### General supplies & services — The Royal Wolverhampton NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £14.06M

### Lease expenditure — Northern Care Alliance NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £13.95M

### General supplies & services — South Warwickshire NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £13.77M

### Establishment costs — Liverpool University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £13.70M

### Establishment costs — University College London Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £13.46M

### Social security & levy — George Eliot Hospital NHS Trust
  parent line: Staff Costs
  value: £13.46M

### General supplies & services — Lancashire Teaching Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £13.43M

### Transport (business + patient) — University College London Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £13.38M

### General supplies & services — Frimley Health NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £13.29M

### Establishment costs — North West Anglia NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £13.17M

### Establishment costs — Hampshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £12.82M

### General supplies & services — North Bristol NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £12.79M

### PFI / LIFT charges — Lewisham and Greenwich NHS Trust
  parent line: Premises & Infrastructure
  value: £12.75M

### General supplies & services — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £12.71M

### General supplies & services — University Hospitals Sussex NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £12.69M

### General supplies & services — Nottingham University Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £12.56M

### General supplies & services — Sandwell And West Birmingham Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £12.55M

### Establishment costs — St George's University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £12.48M

### General supplies & services — Guy's & St Thomas' NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £12.47M

### Establishment costs — Oxford University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £12.38M

### General supplies & services — Epsom and St Helier University Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £12.25M

### Social security & levy — East Cheshire NHS Trust
  parent line: Staff Costs
  value: £12.24M

### General supplies & services — Northumbria Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £12.20M

### General supplies & services — Medway NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £11.92M

### Establishment costs — Blackpool Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £11.73M

### Amortisation — Northern Care Alliance NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £11.70M

### General supplies & services — United Lincolnshire Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £11.55M

### Transport (business + patient) — London North West University Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £11.52M

### PFI / LIFT charges — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £11.46M

### Establishment costs — University Hospitals Coventry And Warwickshire NHS Trust
  parent line: Premises & Infrastructure
  value: £11.43M

### General supplies & services — Chesterfield Royal Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £11.42M

### Establishment costs — Northern Care Alliance NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £11.42M

### Establishment costs — Whittington Health NHS Trust
  parent line: Premises & Infrastructure
  value: £11.41M

### Establishment costs — Nottingham University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £11.19M

### General supplies & services — Blackpool Teaching Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £11.13M

### Transport (business + patient) — Manchester University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £11.12M

### Transport (business + patient) — St George's University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £11.05M

### Lease expenditure — Manchester University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £10.94M

### PFI / LIFT charges — North Middlesex University Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £10.85M

### Business rates — University Hospitals Birmingham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £10.72M

### Business rates — University College London Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £10.43M

### Establishment costs — Frimley Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £10.24M

### General supplies & services — York and Scarborough Teaching Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £10.15M

### Establishment costs — The Shrewsbury and Telford Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £9.96M

### General supplies & services — Sheffield Teaching Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £9.91M

### General supplies & services — Oxford University Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £9.90M

### Establishment costs — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £9.81M

### General supplies & services — The Leeds Teaching Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £9.72M

### Establishment costs — Barts Health NHS Trust
  parent line: Premises & Infrastructure
  value: £9.68M

### General supplies & services — East Cheshire NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £9.67M

### Establishment costs — Imperial College Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £9.59M

### Establishment costs — Kingston Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £9.44M

### PFI / LIFT charges — Liverpool University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £9.42M

### General supplies & services — Royal United Hospitals Bath NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £9.40M

### Establishment costs — Mersey and West Lancashire Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £9.39M

### General supplies & services — University College London Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £9.34M

### Amortisation — Royal Berkshire NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £9.33M

### Establishment costs — West Suffolk NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £9.22M

### PFI / LIFT charges — The Leeds Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £9.13M

### Business rates — University Hospitals Sussex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £9.08M

### Transport (business + patient) — University Hospitals of Leicester NHS Trust
  parent line: Premises & Infrastructure
  value: £9.04M

### Amortisation — Guy's & St Thomas' NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £8.94M

### General supplies & services — East Lancashire Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £8.91M

### Amortisation — Royal Devon University Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £8.71M

### Establishment costs — University Hospitals Sussex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £8.65M

### General supplies & services — University Hospitals of North Midlands NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £8.59M

### General supplies & services — East Sussex Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £8.49M

### General supplies & services — University Hospitals Plymouth NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £8.45M

### Establishment costs — University Hospitals of Leicester NHS Trust
  parent line: Premises & Infrastructure
  value: £8.44M

### Establishment costs — North Bristol NHS Trust
  parent line: Premises & Infrastructure
  value: £8.41M

### Termination & post-employment — Guy's & St Thomas' NHS Foundation Trust
  parent line: Staff Costs
  value: £8.37M

### PFI / LIFT charges — Northern Care Alliance NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £8.37M

### Establishment costs — Sheffield Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £8.36M

### Establishment costs — United Lincolnshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £8.31M

### Establishment costs — Worcestershire Acute Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £8.31M

### General supplies & services — Whittington Health NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £8.15M

### Establishment costs — University Hospital Southampton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £8.07M

### Transport (business + patient) — Oxford University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £8.04M

### PFI / LIFT charges — North Bristol NHS Trust
  parent line: Premises & Infrastructure
  value: £7.88M

### Establishment costs — Royal Free London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.84M

### Establishment costs — East Lancashire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £7.83M

### General supplies & services — The Mid Yorkshire Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £7.83M

### Lease expenditure — University Hospitals of Leicester NHS Trust
  parent line: Premises & Infrastructure
  value: £7.76M

### Establishment costs — University Hospitals of Morecambe Bay NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.75M

### Establishment costs — East Suffolk and North Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.65M

### Establishment costs — Lewisham and Greenwich NHS Trust
  parent line: Premises & Infrastructure
  value: £7.64M

### General supplies & services — North West Anglia NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £7.61M

### Establishment costs — The Royal Wolverhampton NHS Trust
  parent line: Premises & Infrastructure
  value: £7.58M

### Amortisation — Somerset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.58M

### Amortisation — South Tees Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.48M

### Establishment costs — London North West University Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £7.38M

### Establishment costs — Hull University Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £7.31M

### General supplies & services — Hampshire Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £7.30M

### Business rates — Guy's & St Thomas' NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.29M

### Transport (business + patient) — Nottingham University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £7.21M

### General supplies & services — Surrey And Sussex Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £7.21M

### General supplies & services — University Hospitals of Morecambe Bay NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £7.20M

### General supplies & services — Royal Berkshire NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £7.18M

### PFI / LIFT charges — Mid and South Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.13M

### Establishment costs — The Hillingdon Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £7.09M

### Establishment costs — University Hospitals Plymouth NHS Trust
  parent line: Premises & Infrastructure
  value: £7.07M

### Establishment costs — East Sussex Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £7.05M

### Establishment costs — Buckinghamshire Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £7.01M

### General supplies & services — Wirral University Teaching Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £6.97M

### Establishment costs — Royal United Hospitals Bath NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.95M

### Transport (business + patient) — University Hospitals Bristol and Weston NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.87M

### General supplies & services — North Tees and Hartlepool NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £6.86M

### Establishment costs — Epsom and St Helier University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £6.81M

### General supplies & services — The Shrewsbury and Telford Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £6.79M

### General supplies & services — South Tyneside and Sunderland NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £6.79M

### General supplies & services — Maidstone And Tunbridge Wells NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £6.78M

### Business rates — Liverpool University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.73M

### Transport (business + patient) — University Hospitals Birmingham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.68M

### Amortisation — Chelsea and Westminster Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.66M

### Amortisation — Nottingham University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £6.65M

### Transport (business + patient) — Royal Devon University Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.64M

### Amortisation — Mid and South Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.63M

### Establishment costs — Homerton Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.62M

### General supplies & services — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £6.61M

### Transport (business + patient) — The Leeds Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £6.59M

### Establishment costs — The Mid Yorkshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £6.56M

### Business rates — North Bristol NHS Trust
  parent line: Premises & Infrastructure
  value: £6.54M

### General supplies & services — Torbay and South Devon NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £6.54M

### Lease expenditure — The Shrewsbury and Telford Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £6.52M

### Establishment costs — The Leeds Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £6.47M

### Transport (business + patient) — Northumbria Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.46M

### Business rates — Imperial College Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £6.42M

### Establishment costs — Portsmouth Hospitals University NHS Trust
  parent line: Premises & Infrastructure
  value: £6.42M

### General supplies & services — Northern Lincolnshire and Goole NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £6.40M

### General supplies & services — The Princess Alexandra Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £6.40M

### PFI / LIFT charges — Maidstone And Tunbridge Wells NHS Trust
  parent line: Premises & Infrastructure
  value: £6.37M

### Amortisation — St George's University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.33M

### Business rates — Mid and South Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.33M

### Establishment costs — South Tyneside and Sunderland NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.27M

### General supplies & services — Ashford and St Peter's Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £6.27M

### General supplies & services — Northern Care Alliance NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £6.25M

### Amortisation — Imperial College Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £6.23M

### General supplies & services — University Hospitals Coventry And Warwickshire NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £6.20M

### Business rates — Northern Care Alliance NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.20M

### Amortisation — West Suffolk NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.13M

### General supplies & services — Milton Keynes University Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £6.12M

### Establishment costs — North Cumbria Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.10M

### Transport (business + patient) — University Hospitals of North Midlands NHS Trust
  parent line: Premises & Infrastructure
  value: £6.08M

### Transport (business + patient) — Cambridge University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.03M

### Establishment costs — Royal Surrey NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £6.00M

### Business rates — Oxford University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.96M

### Amortisation — Royal Free London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.96M

### Establishment costs — County Durham and Darlington NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.95M

### Business rates — King’s College Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.94M

### Business rates — University Hospitals of Derby and Burton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.82M

### Establishment costs — Norfolk and Norwich University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.77M

### PFI / LIFT charges — Walsall Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £5.74M

### Establishment costs — Northumbria Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.73M

### Establishment costs — East And North Hertfordshire NHS Trust
  parent line: Premises & Infrastructure
  value: £5.67M

### General supplies & services — Mersey and West Lancashire Teaching Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £5.65M

### Establishment costs — University Hospitals of North Midlands NHS Trust
  parent line: Premises & Infrastructure
  value: £5.59M

### Business rates — University Hospitals of North Midlands NHS Trust
  parent line: Premises & Infrastructure
  value: £5.55M

### Establishment costs — York and Scarborough Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.53M

### Business rates — Sheffield Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.53M

### Amortisation — Kingston Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.49M

### Establishment costs — Salisbury NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.48M

### Transport (business + patient) — East Kent Hospitals University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.45M

### Transport (business + patient) — North Cumbria Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.42M

### Business rates — County Durham and Darlington NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.40M

### Business rates — North West Anglia NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.39M

### General supplies & services — The Rotherham NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £5.38M

### Establishment costs — Surrey And Sussex Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £5.37M

### PFI / LIFT charges — Kingston Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.31M

### General supplies & services — Wrightington, Wigan and Leigh NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £5.30M

### Business rates — Somerset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.26M

### Establishment costs — East Kent Hospitals University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.24M

### Business rates — London North West University Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £5.22M

### Transport (business + patient) — Frimley Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.22M

### General supplies & services — Barnsley Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £5.21M

### Establishment costs — Walsall Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £5.20M

### Amortisation — Cambridge University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.19M

### General supplies & services — Northampton General Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £5.14M

### Amortisation — University Hospitals of Leicester NHS Trust
  parent line: Premises & Infrastructure
  value: £5.11M

### Establishment costs — Wye Valley NHS Trust
  parent line: Premises & Infrastructure
  value: £5.07M

### Transport (business + patient) — East Suffolk and North Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.05M

### Establishment costs — Lancashire Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.03M

### Transport (business + patient) — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.02M

### Transport (business + patient) — South Tees Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £5.01M

### Business rates — Mersey and West Lancashire Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £5.00M

### Business rates — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.98M

### Business rates — Maidstone And Tunbridge Wells NHS Trust
  parent line: Premises & Infrastructure
  value: £4.98M

### Business rates — Nottingham University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £4.97M

### Termination & post-employment — King’s College Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £4.96M

### Establishment costs — North Tees and Hartlepool NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.94M

### Amortisation — University Hospitals of North Midlands NHS Trust
  parent line: Premises & Infrastructure
  value: £4.88M

### General supplies & services — Mid Cheshire Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.87M

### General supplies & services — Kingston Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.85M

### Amortisation — University Hospitals Dorset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.83M

### Establishment costs — Royal Cornwall Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £4.82M

### Establishment costs — University Hospitals of Derby and Burton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.80M

### Business rates — Cambridge University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.79M

### General supplies & services — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.79M

### General supplies & services — Walsall Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £4.71M

### General supplies & services — Countess of Chester Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.71M

### General supplies & services — Norfolk and Norwich University Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.70M

### Amortisation — United Lincolnshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £4.68M

### Transport (business + patient) — Royal Cornwall Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £4.68M

### General supplies & services — Calderdale and Huddersfield NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.67M

### Business rates — University Hospitals of Leicester NHS Trust
  parent line: Premises & Infrastructure
  value: £4.65M

### Establishment costs — Northern Lincolnshire and Goole NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.63M

### General supplies & services — North Cumbria Integrated Care NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.63M

### Transport (business + patient) — Lewisham and Greenwich NHS Trust
  parent line: Premises & Infrastructure
  value: £4.61M

### PFI / LIFT charges — Tameside and Glossop Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.59M

### Amortisation — Frimley Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.58M

### Establishment costs — Gateshead Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.57M

### Business rates — Northumbria Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.57M

### General supplies & services — Stockport NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.54M

### Transport (business + patient) — Norfolk and Norwich University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.50M

### Amortisation — East Lancashire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £4.49M

### Business rates — Chelsea and Westminster Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.49M

### PFI / LIFT charges — Somerset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.48M

### General supplies & services — Salisbury NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.44M

### Transport (business + patient) — Epsom and St Helier University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £4.44M

### Lease expenditure — Countess of Chester Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.44M

### Amortisation — University Hospital Southampton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.43M

### Amortisation — Wye Valley NHS Trust
  parent line: Premises & Infrastructure
  value: £4.38M

### Establishment costs — University Hospitals Dorset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.37M

### Business rates — University Hospitals Coventry And Warwickshire NHS Trust
  parent line: Premises & Infrastructure
  value: £4.33M

### General supplies & services — West Suffolk NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.30M

### General supplies & services — Kettering General Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.28M

### Amortisation — London North West University Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £4.25M

### Transport (business + patient) — University Hospitals Sussex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.23M

### Business rates — Lewisham and Greenwich NHS Trust
  parent line: Premises & Infrastructure
  value: £4.23M

### General supplies & services — Bolton NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.21M

### General supplies & services — County Durham and Darlington NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.19M

### Amortisation — Gloucestershire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.16M

### General supplies & services — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.16M

### Establishment costs — Sandwell And West Birmingham Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £4.15M

### General supplies & services — South Tees Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.13M

### Transport (business + patient) — Maidstone And Tunbridge Wells NHS Trust
  parent line: Premises & Infrastructure
  value: £4.12M

### General supplies & services — King’s College Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.12M

### Transport (business + patient) — Liverpool University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.10M

### Social security & levy — Southport And Ormskirk Hospital NHS Trust
  parent line: Staff Costs
  value: £4.10M

### Amortisation — Lewisham and Greenwich NHS Trust
  parent line: Premises & Infrastructure
  value: £4.09M

### Establishment costs — Chelsea and Westminster Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.07M

### Amortisation — Homerton Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.07M

### Amortisation — Liverpool University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £4.05M

### General supplies & services — James Paget University Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £4.03M

### Establishment costs — Isle of Wight NHS Trust
  parent line: Premises & Infrastructure
  value: £4.02M

### Transport (business + patient) — The Rotherham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.99M

### Establishment costs — Sherwood Forest Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.94M

### Transport (business + patient) — Royal Berkshire NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.94M

### Establishment costs — Royal Berkshire NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.91M

### Establishment costs — Northampton General Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £3.89M

### Transport (business + patient) — Torbay and South Devon NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.88M

### Business rates — Portsmouth Hospitals University NHS Trust
  parent line: Premises & Infrastructure
  value: £3.82M

### Business rates — University Hospitals Bristol and Weston NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.79M

### General supplies & services — Sherwood Forest Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £3.79M

### Amortisation — Portsmouth Hospitals University NHS Trust
  parent line: Premises & Infrastructure
  value: £3.78M

### Amortisation — University Hospitals Bristol and Weston NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.70M

### Lease expenditure — London North West University Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £3.70M

### Transport (business + patient) — Chelsea and Westminster Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.69M

### Transport (business + patient) — North Middlesex University Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £3.67M

### Business rates — Sherwood Forest Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.67M

### General supplies & services — Portsmouth Hospitals University NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £3.64M

### Business rates — Norfolk and Norwich University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.62M

### Establishment costs — Wrightington, Wigan and Leigh NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.62M

### Business rates — East Lancashire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £3.61M

### Business rates — University Hospitals Plymouth NHS Trust
  parent line: Premises & Infrastructure
  value: £3.59M

### Business rates — Gloucestershire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.59M

### Business rates — The Mid Yorkshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £3.59M

### Amortisation — North Bristol NHS Trust
  parent line: Premises & Infrastructure
  value: £3.58M

### Establishment costs — Bolton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.58M

### Establishment costs — Calderdale and Huddersfield NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.56M

### Establishment costs — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.56M

### Transport (business + patient) — Hampshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.50M

### Lease expenditure — Bedfordshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.50M

### Transport (business + patient) — University Hospitals of Morecambe Bay NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.48M

### General supplies & services — Tameside and Glossop Integrated Care NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £3.45M

### Transport (business + patient) — North West Anglia NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.44M

### Establishment costs — Ashford and St Peter's Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.44M

### Transport (business + patient) — York and Scarborough Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.41M

### Amortisation — University Hospitals Birmingham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.40M

### Amortisation — Milton Keynes University Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.38M

### Business rates — East Kent Hospitals University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.36M

### Business rates — Frimley Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.35M

### Business rates — East Suffolk and North Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.35M

### Establishment costs — Bradford Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.30M

### Amortisation — East And North Hertfordshire NHS Trust
  parent line: Premises & Infrastructure
  value: £3.28M

### Transport (business + patient) — Northern Lincolnshire and Goole NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.27M

### Establishment costs — Kettering General Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.25M

### Business rates — North Middlesex University Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £3.24M

### Amortisation — University College London Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.23M

### Transport (business + patient) — North Bristol NHS Trust
  parent line: Premises & Infrastructure
  value: £3.23M

### Amortisation — Royal Cornwall Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £3.20M

### General supplies & services — George Eliot Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £3.20M

### PFI / LIFT charges — London North West University Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £3.19M

### Amortisation — Ashford and St Peter's Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.19M

### Transport (business + patient) — Sheffield Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.17M

### Amortisation — Northumbria Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.16M

### Amortisation — Blackpool Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.16M

### Establishment costs — Torbay and South Devon NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.15M

### Business rates — South Tees Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.12M

### Amortisation — The Shrewsbury and Telford Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £3.12M

### Business rates — University Hospital Southampton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.11M

### Transport (business + patient) — Lancashire Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.11M

### Amortisation — University Hospitals Sussex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.11M

### General supplies & services — Wye Valley NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £3.10M

### Establishment costs — Dartford and Gravesham NHS Trust
  parent line: Premises & Infrastructure
  value: £3.10M

### Transport (business + patient) — Mid and South Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.10M

### Transport (business + patient) — Blackpool Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.08M

### Establishment costs — Harrogate and District NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.04M

### Transport (business + patient) — University Hospitals of Derby and Burton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.03M

### Establishment costs — The Dudley Group NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.02M

### Business rates — South Tyneside and Sunderland NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £3.00M

### Amortisation — The Princess Alexandra Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £3.00M

### Transport (business + patient) — The Royal Wolverhampton NHS Trust
  parent line: Premises & Infrastructure
  value: £2.99M

### Business rates — University Hospitals Dorset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.99M

### Business rates — The Royal Wolverhampton NHS Trust
  parent line: Premises & Infrastructure
  value: £2.99M

### Transport (business + patient) — University Hospital Southampton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.98M

### Transport (business + patient) — Bedfordshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.96M

### Transport (business + patient) — The Mid Yorkshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.96M

### Transport (business + patient) — Gloucestershire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.95M

### Business rates — St George's University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.94M

### General supplies & services — The Hillingdon Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.90M

### Establishment costs — Countess of Chester Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.89M

### Business rates — York and Scarborough Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.88M

### Amortisation — Salisbury NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.88M

### General supplies & services — Gateshead Health NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.88M

### Transport (business + patient) — County Durham and Darlington NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.85M

### Transport (business + patient) — Isle of Wight NHS Trust
  parent line: Premises & Infrastructure
  value: £2.85M

### Establishment costs — Maidstone And Tunbridge Wells NHS Trust
  parent line: Premises & Infrastructure
  value: £2.83M

### Business rates — Hull University Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.82M

### General supplies & services — Great Western Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.80M

### General supplies & services — Airedale NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.79M

### Transport (business + patient) — Buckinghamshire Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £2.79M

### Transport (business + patient) — South Warwickshire NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.78M

### Transport (business + patient) — The Hillingdon Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.77M

### Amortisation — University Hospitals of Derby and Burton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.75M

### PFI / LIFT charges — Cambridge University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.75M

### Transport (business + patient) — Whittington Health NHS Trust
  parent line: Premises & Infrastructure
  value: £2.73M

### General supplies & services — Dorset County Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.73M

### Termination & post-employment — Northern Care Alliance NHS Foundation Trust
  parent line: Staff Costs
  value: £2.73M

### Business rates — Bedfordshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.73M

### Establishment costs — Mid Cheshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.73M

### Business rates — Lancashire Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.72M

### General supplies & services — Isle of Wight NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £2.71M

### PFI / LIFT charges — The Royal Wolverhampton NHS Trust
  parent line: Premises & Infrastructure
  value: £2.71M

### Business rates — Royal Devon University Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.69M

### Amortisation — Whittington Health NHS Trust
  parent line: Premises & Infrastructure
  value: £2.67M

### Amortisation — Kettering General Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.65M

### Amortisation — Bradford Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.64M

### Lease expenditure — University Hospitals Birmingham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.64M

### Establishment costs — The Princess Alexandra Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £2.63M

### Establishment costs — The Rotherham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.63M

### Lease expenditure — Guy's & St Thomas' NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.61M

### Lease expenditure — North Bristol NHS Trust
  parent line: Premises & Infrastructure
  value: £2.60M

### Establishment costs — West Hertfordshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.60M

### Business rates — Walsall Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £2.59M

### Amortisation — Isle of Wight NHS Trust
  parent line: Premises & Infrastructure
  value: £2.57M

### Amortisation — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.56M

### Business rates — Blackpool Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.56M

### Amortisation — Manchester University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.55M

### Business rates — United Lincolnshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.54M

### Amortisation — Torbay and South Devon NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.53M

### Amortisation — Royal United Hospitals Bath NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.52M

### Establishment costs — Tameside and Glossop Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.52M

### PFI / LIFT charges — Hull University Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.51M

### Establishment costs — East Cheshire NHS Trust
  parent line: Premises & Infrastructure
  value: £2.50M

### Establishment costs — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.50M

### PFI / LIFT charges — Dartford and Gravesham NHS Trust
  parent line: Premises & Infrastructure
  value: £2.49M

### Establishment costs — North Middlesex University Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £2.47M

### Establishment costs — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.46M

### Transport (business + patient) — Mersey and West Lancashire Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.46M

### Business rates — Buckinghamshire Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £2.45M

### Amortisation — Oxford University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.44M

### Establishment costs — Wirral University Teaching Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.44M

### Transport (business + patient) — Hull University Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.44M

### Business rates — Torbay and South Devon NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.41M

### Amortisation — Maidstone And Tunbridge Wells NHS Trust
  parent line: Premises & Infrastructure
  value: £2.39M

### Business rates — Northern Lincolnshire and Goole NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.38M

### Amortisation — Lancashire Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.36M

### Transport (business + patient) — Portsmouth Hospitals University NHS Trust
  parent line: Premises & Infrastructure
  value: £2.35M

### Amortisation — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.33M

### Business rates — Epsom and St Helier University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.33M

### Transport (business + patient) — West Suffolk NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.31M

### Transport (business + patient) — University Hospitals Coventry And Warwickshire NHS Trust
  parent line: Premises & Infrastructure
  value: £2.31M

### PFI / LIFT charges — Nottingham University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.29M

### Transport (business + patient) — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.28M

### PFI / LIFT charges — Gloucestershire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.26M

### Lease expenditure — Lancashire Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.26M

### Business rates — Hampshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.25M

### Transport (business + patient) — Northern Care Alliance NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.23M

### Amortisation — East Suffolk and North Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.23M

### Amortisation — Royal Surrey NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.23M

### Business rates — Whittington Health NHS Trust
  parent line: Premises & Infrastructure
  value: £2.23M

### Transport (business + patient) — Wrightington, Wigan and Leigh NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.22M

### Establishment costs — James Paget University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.21M

### Establishment costs — George Eliot Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £2.19M

### Business rates — The Leeds Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.19M

### Establishment costs — Medway NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.17M

### Transport (business + patient) — Harrogate and District NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.17M

### Transport (business + patient) — Homerton Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.16M

### Amortisation — King’s College Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.16M

### Transport (business + patient) — Somerset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.15M

### Amortisation — Hull University Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.15M

### PFI / LIFT charges — East Lancashire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.15M

### Transport (business + patient) — Mid Cheshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.13M

### Transport (business + patient) — Salisbury NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.12M

### Business rates — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.11M

### Establishment costs — Dorset County Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.09M

### PFI / LIFT charges — Sandwell And West Birmingham Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.07M

### Business rates — Calderdale and Huddersfield NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.06M

### Amortisation — Northampton General Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £2.04M

### Business rates — Worcestershire Acute Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £2.03M

### Amortisation — Chesterfield Royal Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.03M

### Amortisation — Wirral University Teaching Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.02M

### General supplies & services — The Dudley Group NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £2.02M

### Business rates — South Warwickshire NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.01M

### Transport (business + patient) — South Tyneside and Sunderland NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.00M

### Amortisation — Bolton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £2.00M

### Amortisation — York and Scarborough Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.99M

### Business rates — The Shrewsbury and Telford Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £1.99M

### Business rates — Royal Berkshire NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.97M

### Business rates — Dartford and Gravesham NHS Trust
  parent line: Premises & Infrastructure
  value: £1.97M

### Lease expenditure — Royal Free London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.97M

### Business rates — Royal Surrey NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.96M

### Transport (business + patient) — United Lincolnshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.95M

### Amortisation — Great Western Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.95M

### Amortisation — University Hospitals Plymouth NHS Trust
  parent line: Premises & Infrastructure
  value: £1.95M

### Transport (business + patient) — Great Western Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.94M

### Business rates — Bradford Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.94M

### Transport (business + patient) — Calderdale and Huddersfield NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.93M

### Business rates — North Cumbria Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.93M

### Business rates — Great Western Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.93M

### Business rates — Milton Keynes University Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.92M

### Establishment costs — Milton Keynes University Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.91M

### General supplies & services — Buckinghamshire Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £1.90M

### Establishment costs — Chesterfield Royal Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.90M

### Transport (business + patient) — East Lancashire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.89M

### Transport (business + patient) — Kingston Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.88M

### Amortisation — The Mid Yorkshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.88M

### Transport (business + patient) — Walsall Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £1.86M

### Transport (business + patient) — Royal Surrey NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.85M

### Amortisation — Surrey And Sussex Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £1.85M

### Amortisation — Stockport NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.85M

### Business rates — Chesterfield Royal Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.83M

### PFI / LIFT charges — Guy's & St Thomas' NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.83M

### Business rates — Homerton Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.83M

### Transport (business + patient) — Medway NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.81M

### Amortisation — Mersey and West Lancashire Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.80M

### Amortisation — The Leeds Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.77M

### Amortisation — South Tyneside and Sunderland NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.77M

### Amortisation — Sherwood Forest Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.77M

### Establishment costs — Stockport NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.76M

### Business rates — Surrey And Sussex Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £1.76M

### Business rates — East Sussex Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £1.75M

### Business rates — Royal Cornwall Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.74M

### Lease expenditure — West Suffolk NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.72M

### Establishment costs — Barnsley Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.72M

### Business rates — Gateshead Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.70M

### PFI / LIFT charges — Stockport NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.70M

### Business rates — Northampton General Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £1.69M

### Amortisation — The Dudley Group NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.69M

### Amortisation — Worcestershire Acute Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.67M

### Amortisation — East Kent Hospitals University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.67M

### Transport (business + patient) — Worcestershire Acute Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.67M

### Lease expenditure — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.67M

### Business rates — The Dudley Group NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.67M

### Amortisation — Sheffield Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.65M

### Transport (business + patient) — Gateshead Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.64M

### Lease expenditure — Sherwood Forest Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.63M

### Establishment costs — Gloucestershire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.63M

### Business rates — Kettering General Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.62M

### Business rates — Bolton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.61M

### Business rates — Kingston Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.60M

### Transport (business + patient) — East And North Hertfordshire NHS Trust
  parent line: Premises & Infrastructure
  value: £1.59M

### Transport (business + patient) — Ashford and St Peter's Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.58M

### Amortisation — Barnsley Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.58M

### Lease expenditure — Royal Devon University Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.58M

### Business rates — Wrightington, Wigan and Leigh NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.57M

### Business rates — Salisbury NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.57M

### Transport (business + patient) — Bolton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.56M

### Termination & post-employment — Liverpool University Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £1.55M

### Amortisation — Hampshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.54M

### Business rates — Wirral University Teaching Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.53M

### Transport (business + patient) — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.52M

### Business rates — North Tees and Hartlepool NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.52M

### Lease expenditure — Cambridge University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.52M

### Business rates — Stockport NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.49M

### Transport (business + patient) — Stockport NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.49M

### Amortisation — The Royal Wolverhampton NHS Trust
  parent line: Premises & Infrastructure
  value: £1.48M

### Business rates — Mid Cheshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.48M

### General supplies & services — Harrogate and District NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.48M

### Transport (business + patient) — Barnsley Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.46M

### Transport (business + patient) — Sandwell And West Birmingham Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.46M

### Transport (business + patient) — University Hospitals Dorset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.45M

### Business rates — Dorset County Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.41M

### Business rates — Wye Valley NHS Trust
  parent line: Premises & Infrastructure
  value: £1.41M

### Lease expenditure — Mid Cheshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.41M

### Inventories written down — Nottingham University Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £1.39M

### PFI / LIFT charges — University Hospitals Sussex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.38M

### Transport (business + patient) — East Sussex Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £1.37M

### Transport (business + patient) — Royal United Hospitals Bath NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.37M

### Business rates — University Hospitals of Morecambe Bay NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.36M

### Amortisation — North Middlesex University Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £1.36M

### Business rates — Royal Free London NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.33M

### Amortisation — West Hertfordshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.33M

### Lease expenditure — King’s College Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.32M

### PFI / LIFT charges — Bedfordshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.30M

### PFI / LIFT charges — Torbay and South Devon NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.30M

### Business rates — The Rotherham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.29M

### Business rates — The Hillingdon Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.29M

### PFI / LIFT charges — Salisbury NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.29M

### Amortisation — Calderdale and Huddersfield NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.28M

### Amortisation — North Cumbria Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.27M

### Amortisation — The Rotherham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.27M

### Amortisation — The Hillingdon Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.25M

### Establishment costs — Airedale NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.24M

### Inventories written down — Guy's & St Thomas' NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £1.24M

### General supplies & services — Dartford and Gravesham NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £1.22M

### Transport (business + patient) — Wirral University Teaching Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.20M

### Lease expenditure — Somerset NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.20M

### Business rates — Isle of Wight NHS Trust
  parent line: Premises & Infrastructure
  value: £1.18M

### PFI / LIFT charges — St George's University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.16M

### Amortisation — University Hospitals Coventry And Warwickshire NHS Trust
  parent line: Premises & Infrastructure
  value: £1.15M

### Business rates — Harrogate and District NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.10M

### Amortisation — James Paget University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.09M

### Transport (business + patient) — Surrey And Sussex Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £1.08M

### Lease expenditure — Liverpool University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.08M

### Business rates — Sandwell And West Birmingham Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.08M

### Amortisation — Harrogate and District NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.07M

### Lease expenditure — University College London Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.07M

### PFI / LIFT charges — Sheffield Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.06M

### Amortisation — Mid Cheshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.04M

### Transport (business + patient) — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.03M

### Transport (business + patient) — Tameside and Glossop Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.03M

### Transport (business + patient) — Wye Valley NHS Trust
  parent line: Premises & Infrastructure
  value: £1.03M

### Business rates — West Hertfordshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £1.02M

### Termination & post-employment — Somerset NHS Foundation Trust
  parent line: Staff Costs
  value: £1.01M

### Lease expenditure — University Hospitals of Derby and Burton NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £1.00M

### Transport (business + patient) — Dorset County Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.98M

### Transport (business + patient) — Airedale NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.98M

### Amortisation — Walsall Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.96M

### General supplies & services — Southport And Ormskirk Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.95M

### Business rates — George Eliot Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.94M

### Business rates — West Suffolk NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.94M

### Business rates — The Princess Alexandra Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.94M

### Transport (business + patient) — The Dudley Group NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.93M

### Business rates — Medway NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.92M

### Transport (business + patient) — North Tees and Hartlepool NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.91M

### Amortisation — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.90M

### Amortisation — Wrightington, Wigan and Leigh NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.90M

### Transport (business + patient) — Sherwood Forest Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.89M

### PFI / LIFT charges — East Suffolk and North Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.87M

### Inventories written down — Sheffield Teaching Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.85M

### Inventories written down — University Hospitals Sussex NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.85M

### Amortisation — University Hospitals of Morecambe Bay NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.85M

### Business rates — Barnsley Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.84M

### Amortisation — Countess of Chester Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.84M

### Transport (business + patient) — Kettering General Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.82M

### Amortisation — Tameside and Glossop Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.82M

### Business rates — Tameside and Glossop Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.82M

### Transport (business + patient) — The Shrewsbury and Telford Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.81M

### Amortisation — Northern Lincolnshire and Goole NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.80M

### Lease expenditure — Portsmouth Hospitals University NHS Trust
  parent line: Premises & Infrastructure
  value: £0.79M

### Amortisation — County Durham and Darlington NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.79M

### Lease expenditure — South Tyneside and Sunderland NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.78M

### Business rates — East Cheshire NHS Trust
  parent line: Premises & Infrastructure
  value: £0.77M

### Amortisation — Dorset County Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.76M

### Lease expenditure — East And North Hertfordshire NHS Trust
  parent line: Premises & Infrastructure
  value: £0.76M

### Lease expenditure — East Lancashire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.74M

### Transport (business + patient) — Dartford and Gravesham NHS Trust
  parent line: Premises & Infrastructure
  value: £0.72M

### Amortisation — East Sussex Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.71M

### Business rates — James Paget University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.71M

### Lease expenditure — East Kent Hospitals University NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.71M

### Inventories written down — Imperial College Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.71M

### Business rates — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.70M

### Lease expenditure — Wrightington, Wigan and Leigh NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.69M

### PFI / LIFT charges — The Rotherham NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.69M

### Lease expenditure — The Leeds Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.68M

### Lease expenditure — Isle of Wight NHS Trust
  parent line: Premises & Infrastructure
  value: £0.67M

### Business rates — Countess of Chester Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.67M

### Amortisation — Epsom and St Helier University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.67M

### Inventories written down — Northern Care Alliance NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.66M

### Lease expenditure — Frimley Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.66M

### Lease expenditure — Worcestershire Acute Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.65M

### Lease expenditure — Norfolk and Norwich University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.65M

### Transport (business + patient) — Northampton General Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.64M

### Lease expenditure — Sheffield Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.64M

### Transport (business + patient) — Milton Keynes University Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.62M

### Business rates — Airedale NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.62M

### Lease expenditure — Epsom and St Helier University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.61M

### Transport (business + patient) — Bradford Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.61M

### Inventories written down — Royal Surrey NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.60M

### Lease expenditure — East Cheshire NHS Trust
  parent line: Premises & Infrastructure
  value: £0.60M

### Termination & post-employment — The Leeds Teaching Hospitals NHS Trust
  parent line: Staff Costs
  value: £0.60M

### Lease expenditure — North Tees and Hartlepool NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.60M

### Transport (business + patient) — Chesterfield Royal Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.59M

### Inventories written down — King’s College Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.59M

### Lease expenditure — Calderdale and Huddersfield NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.58M

### Lease expenditure — Chelsea and Westminster Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.56M

### Lease expenditure — York and Scarborough Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.54M

### Inventories written down — University Hospitals of North Midlands NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.53M

### Transport (business + patient) — The Princess Alexandra Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.51M

### Lease expenditure — Wirral University Teaching Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.51M

### Lease expenditure — Gateshead Health NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.49M

### Inventories written down — University Hospitals Plymouth NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.49M

### Lease expenditure — Maidstone And Tunbridge Wells NHS Trust
  parent line: Premises & Infrastructure
  value: £0.49M

### PFI / LIFT charges — The Hillingdon Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.48M

### Inventories written down — University Hospitals Coventry And Warwickshire NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.48M

### Establishment costs — Southport And Ormskirk Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.48M

### Lease expenditure — Mersey and West Lancashire Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.47M

### Inventories written down — Royal Cornwall Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.45M

### Transport (business + patient) — George Eliot Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.44M

### Termination & post-employment — Oxford University Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £0.43M

### PFI / LIFT charges — Southport And Ormskirk Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.42M

### Inventories written down — South Warwickshire NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.41M

### Lease expenditure — Royal Surrey NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.40M

### Lease expenditure — Northampton General Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.40M

### Lease expenditure — Wye Valley NHS Trust
  parent line: Premises & Infrastructure
  value: £0.40M

### Termination & post-employment — Barts Health NHS Trust
  parent line: Staff Costs
  value: £0.39M

### Lease expenditure — Hull University Teaching Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.38M

### Inventories written down — Mid Cheshire Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.38M

### Lease expenditure — Tameside and Glossop Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.38M

### Lease expenditure — Warrington and Halton Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.38M

### Inventories written down — Worcestershire Acute Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.38M

### Business rates — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.37M

### Transport (business + patient) — University Hospitals Plymouth NHS Trust
  parent line: Premises & Infrastructure
  value: £0.37M

### Business rates — Southport And Ormskirk Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.36M

### Amortisation — East Cheshire NHS Trust
  parent line: Premises & Infrastructure
  value: £0.35M

### Lease expenditure — Torbay and South Devon NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.35M

### Termination & post-employment — Royal Surrey NHS Foundation Trust
  parent line: Staff Costs
  value: £0.35M

### Lease expenditure — University Hospitals of North Midlands NHS Trust
  parent line: Premises & Infrastructure
  value: £0.35M

### Inventories written down — South Tyneside and Sunderland NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.33M

### Termination & post-employment — North Bristol NHS Trust
  parent line: Staff Costs
  value: £0.32M

### Transport (business + patient) — West Hertfordshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.32M

### Lease expenditure — United Lincolnshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.32M

### Inventories written down — Chelsea and Westminster Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.31M

### PFI / LIFT charges — Royal Cornwall Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.31M

### Inventories written down — Hampshire Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.31M

### PFI / LIFT charges — Northumbria Healthcare NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.31M

### Inventories written down — The Shrewsbury and Telford Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.30M

### Inventories written down — George Eliot Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.29M

### Inventories written down — South Tees Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.29M

### Inventories written down — University Hospitals Birmingham NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.27M

### Inventories written down — Royal Devon University Healthcare NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.27M

### Termination & post-employment — East Suffolk and North Essex NHS Foundation Trust
  parent line: Staff Costs
  value: £0.27M

### Transport (business + patient) — East Cheshire NHS Trust
  parent line: Premises & Infrastructure
  value: £0.27M

### Lease expenditure — University Hospitals Coventry And Warwickshire NHS Trust
  parent line: Premises & Infrastructure
  value: £0.27M

### Inventories written down — The Newcastle Upon Tyne Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.26M

### Lease expenditure — The Hillingdon Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.26M

### Lease expenditure — Nottingham University Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.26M

### Inventories written down — London North West University Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.26M

### Inventories written down — East And North Hertfordshire NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.26M

### Inventories written down — Northampton General Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.26M

### Inventories written down — Kettering General Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.26M

### Transport (business + patient) — James Paget University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.26M

### Lease expenditure — University Hospitals Bristol and Weston NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.26M

### Other & adjustments — Great Western Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £0.25M

### Inventories written down — Walsall Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.24M

### Lease expenditure — North Cumbria Integrated Care NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.24M

### Inventories written down — Chesterfield Royal Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.24M

### PFI / LIFT charges — Countess of Chester Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.24M

### Lease expenditure — Bradford Teaching Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.24M

### Inventories written down — Wirral University Teaching Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.24M

### Inventories written down — Airedale NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.24M

### Lease expenditure — West Hertfordshire Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.23M

### Inventories written down — Lewisham and Greenwich NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.23M

### Transport (business + patient) — Countess of Chester Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.23M

### Termination & post-employment — Great Western Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £0.23M

### Lease expenditure — East Suffolk and North Essex NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.22M

### Inventories written down — Lancashire Teaching Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.22M

### Termination & post-employment — Dorset County Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £0.22M

### Inventories written down — United Lincolnshire Hospitals NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.21M

### Other & adjustments — Northumbria Healthcare NHS Foundation Trust
  parent line: Staff Costs
  value: £0.21M

### Amortisation — Buckinghamshire Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.20M

### Lease expenditure — East Sussex Healthcare NHS Trust
  parent line: Premises & Infrastructure
  value: £0.20M

### Inventories written down — North Middlesex University Hospital NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.19M

### Lease expenditure — University Hospitals Plymouth NHS Trust
  parent line: Premises & Infrastructure
  value: £0.19M

### Business rates — Ashford and St Peter's Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.19M

### Termination & post-employment — Nottingham University Hospitals NHS Trust
  parent line: Staff Costs
  value: £0.19M

### Lease expenditure — Ashford and St Peter's Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.19M

### Inventories written down — Royal Free London NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.18M

### Termination & post-employment — University Hospitals Bristol and Weston NHS Foundation Trust
  parent line: Staff Costs
  value: £0.18M

### Inventories written down — Mid and South Essex NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.18M

### Termination & post-employment — Northampton General Hospital NHS Trust
  parent line: Staff Costs
  value: £0.17M

### Inventories written down — East Suffolk and North Essex NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.17M

### Inventories written down — Buckinghamshire Healthcare NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.16M

### Termination & post-employment — Kettering General Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £0.16M

### Amortisation — Southport And Ormskirk Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.16M

### Inventories written down — Barts Health NHS Trust
  parent line: Clinical Supplies & Drugs
  value: £0.16M

### Lease expenditure — Oxford University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.16M

### PFI / LIFT charges — Hampshire Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.16M

### Termination & post-employment — West Suffolk NHS Foundation Trust
  parent line: Staff Costs
  value: £0.16M

### Transport (business + patient) — Southport And Ormskirk Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.16M

### Lease expenditure — Great Western Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.15M

### Lease expenditure — North Middlesex University Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.15M

### Inventories written down — Countess of Chester Hospital NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.15M

### PFI / LIFT charges — East And North Hertfordshire NHS Trust
  parent line: Premises & Infrastructure
  value: £0.15M

### Termination & post-employment — Gateshead Health NHS Foundation Trust
  parent line: Staff Costs
  value: £0.14M

### Other & adjustments — Wirral University Teaching Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £0.14M

### Lease expenditure — Royal United Hospitals Bath NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.14M

### Termination & post-employment — University Hospitals Birmingham NHS Foundation Trust
  parent line: Staff Costs
  value: £0.14M

### Termination & post-employment — Barnsley Hospital NHS Foundation Trust
  parent line: Staff Costs
  value: £0.14M

### Lease expenditure — James Paget University Hospitals NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.14M

### Termination & post-employment — University Hospitals Coventry And Warwickshire NHS Trust
  parent line: Staff Costs
  value: £0.14M

### Lease expenditure — Royal Cornwall Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.13M

### Inventories written down — James Paget University Hospitals NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.13M

### Inventories written down — Torbay and South Devon NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.13M

### Termination & post-employment — Royal Cornwall Hospitals NHS Trust
  parent line: Staff Costs
  value: £0.13M

### Termination & post-employment — Blackpool Teaching Hospitals NHS Foundation Trust
  parent line: Staff Costs
  value: £0.12M

### Inventories written down — University Hospitals of Morecambe Bay NHS Foundation Trust
  parent line: Clinical Supplies & Drugs
  value: £0.11M

### Lease expenditure — Sandwell And West Birmingham Hospitals NHS Trust
  parent line: Premises & Infrastructure
  value: £0.11M

### Lease expenditure — Medway NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.11M

### Amortisation — George Eliot Hospital NHS Trust
  parent line: Premises & Infrastructure
  value: £0.11M

### Lease expenditure — Kettering General Hospital NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.11M

### Lease expenditure — Airedale NHS Foundation Trust
  parent line: Premises & Infrastructure
  value: £0.11M

