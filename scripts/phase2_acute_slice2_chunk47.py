# -*- coding: utf-8 -*-
"""Phase 2 Acute slice 2 — chunk 47 (final partial chunk, 9 entries).

Hand-curated NEW dict to merge into data/uk/node_enrichment_extended.json.
Composite key: "<sub-line> — <trust>" (em-dash U+2014).
"""

NEW = {}

NEW["Inventories written down — Torbay and South Devon NHS Foundation Trust"] = {
    "aliases": [
        {"name": "Inventories written down", "parent": "Torbay and South Devon NHS Foundation Trust"}
    ],
    "description": "Torbay and South Devon NHSFT's £0.127M inventories-written-down line captures the IAS 2 charge for stock written off below cost across the integrated care organisation — chiefly expired pharmaceuticals at Torbay Hospital pharmacy, expired surgical consumables across general/orthopaedic/ophthalmic/ENT theatres, obsolete community-equipment store items (the trust's adult social-care integration brings unusually large equipment-store stock), and time-expired emergency-department/HDU consumables. The integrated health-and-care model raises stockholding breadth vs a pure acute trust.",
    "beneficiaries": "Serves c. 286,000 residents of Torbay and South Devon (Paignton, Brixham, Torquay, Totnes, Dartmouth) plus the South Devon coastal-tourist surge; c. 6,500 WTE staff; Torbay Hospital DGH (c. 320 beds) plus community hospitals at Brixham, Dawlish, Newton Abbot, Paignton, Totnes; integrated adult social care (the trust is a Section 75 ICO).",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Care Act 2014 (Section 75 ICO partnership) · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.127M"},
        {"label": "Trust profile", "value": "Integrated DGH + community hospitals + adult social care (Section 75 ICO)"},
        {"label": "Catchment", "value": "c. 286,000 residents Torbay + South Devon + tourist surge"},
        {"label": "Workforce", "value": "c. 6,500 WTE"},
        {"label": "Estate", "value": "Torbay Hospital DGH (c. 320 beds) + 5 community hospitals"},
        {"label": "Stock profile", "value": "Pharmacy expired drugs + theatre consumables + community-equipment store + ED/HDU kit"},
        {"label": "Write-down driver", "value": "Expired pharmacy stock + ICO community-equipment-store obsolescence + tourist-surge over-stocking"},
        {"label": "Procurement route", "value": "NHS Supply Chain + RDE Group joint contracts + community-equipment specific procurement"},
        {"label": "Funding trajectory", "value": "Stable; ICO community-equipment-store remains structural driver"},
        {"label": "Delivery body", "value": "Trust Pharmacy + Procurement + Theatres + Community Equipment Service"},
        {"label": "Policy owner", "value": "DHSC + NHSE South West + Devon ICB + Torbay Council (S75 partner)"},
        {"label": "Evaluation evidence", "value": "Trust ARA; CQC RA9 (Requires Improvement Sept 2023); Devon ICS financial recovery plan"}
    ],
    "notes": "Torbay and South Devon NHSFT is the original Section 75 integrated care organisation pioneer (formed 2015 from merger of Torbay Hospital and Torbay & Southern Devon Health & Care Trust) and integrates adult social-care commissioning with NHS provision — uniquely raising the breadth of inventory beyond pure acute pharmaceuticals to include community-equipment loan stores. The trust's CQC rating dropped to Requires Improvement (Sept 2023) and it sits within Devon ICS which has been in formal financial recovery — driving tighter inventory management and write-down scrutiny. The 2024-25 figure (£0.127M) is modest in absolute terms but reflects ongoing pressure on community-equipment obsolescence and pharmacy expiry control.",
    "sources": [
        {"publisher": "Torbay and South Devon NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.torbayandsouthdevon.nhs.uk/about-us/our-publications/annual-reports/"},
        {"publisher": "CQC", "title": "Torbay and South Devon NHSFT provider inspection (RA9)", "url": "https://www.cqc.org.uk/provider/RA9"},
        {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Devon ICS financial recovery / NHS Oversight Framework", "url": "https://www.england.nhs.uk/publication/nhs-oversight-framework/"},
        {"publisher": "NHS Supply Chain", "title": "NHS Supply Chain — annual report", "url": "https://www.supplychain.nhs.uk/"}
    ],
    "related": [
        "Torbay and South Devon NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain"
    ]
}

NEW["Termination & post-employment — Royal Cornwall Hospitals NHS Trust"] = {
    "aliases": [
        {"name": "Termination & post-employment", "parent": "Royal Cornwall Hospitals NHS Trust"}
    ],
    "description": "Royal Cornwall Hospitals NHS Trust's £0.127M termination and post-employment cost line captures IAS 19/IAS 26 charges for staff exits — Mutually Agreed Resignation Scheme (MARS) settlements, voluntary redundancies, contractual notice payments and ill-health early retirement employer contributions to the NHS Pension Scheme — across the trust's geographically isolated DGH at Treliske (Truro) plus West Cornwall Hospital (Penzance) and St Michael's (Hayle). Recruitment fragility in peripheral peninsular geography materially shapes turnover and exit cost composition.",
    "beneficiaries": "Serves c. 540,000 residents of Cornwall and the Isles of Scilly (England's most peripheral mainland health economy) plus c. 5M tourist visits/yr; c. 5,400 WTE staff; Royal Cornwall Hospital Treliske (c. 750 beds, sole DGH for Cornwall), West Cornwall Hospital (Penzance), St Michael's Hayle (eye unit + day-case), maternity at Treliske + Penzance.",
    "legal_basis": "IAS 19 Employee Benefits · IAS 26 Retirement Benefit Plans · DHSC Group Accounting Manual 2024-25 · NHS Pension Scheme Regulations 2015 · Employment Rights Act 1996 · NHS Act 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.127M"},
        {"label": "Trust profile", "value": "Sole DGH for Cornwall + IoS — England's most peripheral mainland acute trust"},
        {"label": "Catchment", "value": "c. 540,000 residents + c. 5M tourist visits/yr"},
        {"label": "Workforce", "value": "c. 5,400 WTE"},
        {"label": "Estate", "value": "Treliske DGH (c. 750 beds) + West Cornwall Hospital Penzance + St Michael's Hayle"},
        {"label": "Cost composition", "value": "MARS settlements + voluntary redundancy + contractual notice + ill-health early retirement employer contributions"},
        {"label": "Turnover driver", "value": "Peninsular recruitment fragility; high cost of living in coastal Cornwall vs nurse pay; consultant retention pressure"},
        {"label": "YoY trend", "value": "Modest absolute level; reflects targeted exits not bulk restructure"},
        {"label": "Pension scheme", "value": "NHS Pension Scheme (1995/2008/2015 sections) — McCloud remedy ongoing"},
        {"label": "Recent context", "value": "Trust placed in NHSE Recovery Support Programme (NOSEG segment 4) for finance + quality"},
        {"label": "Workforce evaluation", "value": "NHS Staff Survey results below national median on engagement and retention"},
        {"label": "Policy owner", "value": "DHSC + NHSE South West + Cornwall and IoS ICB + NHS Business Services Authority (Pensions)"}
    ],
    "notes": "Royal Cornwall Hospitals' termination/post-employment line reflects the structural workforce fragility of being England's most geographically isolated mainland acute trust — high reliance on locum and agency consultants, persistent vacancy gaps in emergency medicine, paediatrics and obstetrics, and recruitment competition from Plymouth/Devon-side trusts. The trust has been in NHSE's Recovery Support Programme (NOSEG segment 4) covering both finance and CQC quality concerns since the maternity-care report fallout; this raises termination-cost activity around senior clinical and managerial exits. The McCloud remedy (Public Service Pensions and Judicial Offices Act 2022) continues to add complexity to post-employment accounting across the NHS Pension Scheme and contributes to the IAS 19 charge variability.",
    "sources": [
        {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.royalcornwall.nhs.uk/about-us/publications/"},
        {"publisher": "CQC", "title": "Royal Cornwall Hospitals NHS Trust inspection (REF)", "url": "https://www.cqc.org.uk/provider/REF"},
        {"publisher": "NHS England", "title": "NHS Oversight Framework — Recovery Support Programme", "url": "https://www.england.nhs.uk/publication/nhs-oversight-framework/"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme — McCloud remedy guidance", "url": "https://www.nhsbsa.nhs.uk/member-hub/mccloud-remedy"},
        {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
    ],
    "related": [
        "Royal Cornwall Hospitals NHS Trust",
        "Staff Costs",
        "NHS Pension Scheme"
    ]
}

NEW["Termination & post-employment — Blackpool Teaching Hospitals NHS Foundation Trust"] = {
    "aliases": [
        {"name": "Termination & post-employment", "parent": "Blackpool Teaching Hospitals NHS Foundation Trust"}
    ],
    "description": "Blackpool Teaching Hospitals NHSFT's £0.123M termination and post-employment cost line captures IAS 19/IAS 26 charges for staff exits — MARS settlements, voluntary redundancies, contractual notice payments and ill-health early retirement employer pension contributions — across Blackpool Victoria Hospital DGH, the Lancashire Cardiac Centre (regional tertiary heart centre serving 1.6M Lancashire and South Cumbria population) and community hospitals at Clifton (Lytham St Annes), Fleetwood and Bispham. The deeply deprived Fylde-coast catchment shapes workforce-stability dynamics.",
    "beneficiaries": "Serves c. 330,000 Fylde Coast residents (Blackpool Unitary, Wyre, Fylde) plus c. 1.6M tertiary cardiac catchment across Lancashire and South Cumbria; c. 7,800 WTE staff; Blackpool Victoria Hospital (c. 700 beds), Lancashire Cardiac Centre, c. 5 community hospital sites; maternity, ED, stroke unit, oncology, hyper-acute stroke at the Vic.",
    "legal_basis": "IAS 19 Employee Benefits · IAS 26 Retirement Benefit Plans · DHSC Group Accounting Manual 2024-25 · NHS Pension Scheme Regulations 2015 · Employment Rights Act 1996 · NHS Act 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.123M"},
        {"label": "Trust profile", "value": "Fylde-coast DGH + Lancashire Cardiac Centre (regional tertiary)"},
        {"label": "Catchment", "value": "c. 330,000 Fylde Coast residents + c. 1.6M tertiary cardiac catchment"},
        {"label": "Workforce", "value": "c. 7,800 WTE"},
        {"label": "Estate", "value": "Blackpool Victoria Hospital (c. 700 beds) + Lancashire Cardiac Centre + community hospitals"},
        {"label": "Cost composition", "value": "MARS + voluntary redundancy + contractual notice + ill-health early retirement"},
        {"label": "Turnover driver", "value": "Deprivation-related health pressure on workforce; consultant retention competition with Manchester/Liverpool/Preston tertiary centres"},
        {"label": "YoY trend", "value": "Modest absolute level; reflects targeted exits"},
        {"label": "Pension scheme", "value": "NHS Pension Scheme (1995/2008/2015 sections) — McCloud remedy ongoing"},
        {"label": "Recent context", "value": "Trust holds tertiary cardiac surgery role; CQC ratings mixed (Requires Improvement maternity)"},
        {"label": "Catchment deprivation", "value": "Blackpool ranks among most deprived English LAs (IMD 2019 — Blackpool top decile)"},
        {"label": "Policy owner", "value": "DHSC + NHSE North West + Lancashire and South Cumbria ICB + NHS BSA (Pensions)"}
    ],
    "notes": "Blackpool Teaching Hospitals' termination/post-employment line is shaped by the trust's dual identity — a Fylde-coast DGH serving England's most deprived seaside town (Blackpool consistently ranks in the top decile of the Index of Multiple Deprivation) alongside the Lancashire Cardiac Centre's regional tertiary role. Workforce retention pressure is structural: nursing and medical recruitment competes with Preston, Manchester and Liverpool tertiary centres, while the deprivation-related health load on the workforce raises ill-health early retirement claims. The McCloud remedy under the Public Service Pensions and Judicial Offices Act 2022 continues to add IAS 19 charge variability across the NHS Pension Scheme, and the trust's CQC profile (Requires Improvement on maternity post-2024 inspection) drives targeted clinical-leadership exits.",
    "sources": [
        {"publisher": "Blackpool Teaching Hospitals NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.bfwh.nhs.uk/about-the-trust/publications/"},
        {"publisher": "CQC", "title": "Blackpool Teaching Hospitals NHSFT inspection (RXL)", "url": "https://www.cqc.org.uk/provider/RXL"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme — McCloud remedy guidance", "url": "https://www.nhsbsa.nhs.uk/member-hub/mccloud-remedy"},
        {"publisher": "MHCLG", "title": "Index of Multiple Deprivation 2019", "url": "https://www.gov.uk/government/statistics/english-indices-of-deprivation-2019"},
        {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
    ],
    "related": [
        "Blackpool Teaching Hospitals NHS Foundation Trust",
        "Staff Costs",
        "NHS Pension Scheme"
    ]
}

NEW["Inventories written down — University Hospitals of Morecambe Bay NHS Foundation Trust"] = {
    "aliases": [
        {"name": "Inventories written down", "parent": "University Hospitals of Morecambe Bay NHS Foundation Trust"}
    ],
    "description": "University Hospitals of Morecambe Bay NHSFT's £0.113M inventories-written-down line captures the IAS 2 charge for stock written off below cost across the trust's three-DGH footprint — chiefly expired pharmaceuticals (Royal Lancaster Infirmary, Furness General, Westmorland General pharmacies), expired surgical and obstetric consumables across general/orthopaedic/paediatric/maternity theatres, time-expired ED/HDU consumables, and obsolete bespoke implant stock. The geographically dispersed three-site model raises stockholding redundancy.",
    "beneficiaries": "Serves c. 365,000 residents of North Lancashire, South Cumbria and the Furness Peninsula (Lancaster, Morecambe, Barrow-in-Furness, Kendal, Ulverston) plus Lake District tourist load; c. 6,800 WTE staff; Royal Lancaster Infirmary (c. 480 beds, main DGH), Furness General (c. 270 beds, Barrow), Westmorland General (Kendal, day-case + community), maternity at RLI + Furness General.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.113M"},
        {"label": "Trust profile", "value": "Three-DGH model spanning North Lancs + South Cumbria + Furness Peninsula"},
        {"label": "Catchment", "value": "c. 365,000 residents + Lake District tourist load"},
        {"label": "Workforce", "value": "c. 6,800 WTE"},
        {"label": "Estate", "value": "Royal Lancaster Infirmary + Furness General + Westmorland General"},
        {"label": "Stock profile", "value": "Pharmacy expired drugs + theatre consumables + maternity kit + ED/HDU consumables + bespoke implants"},
        {"label": "Write-down driver", "value": "Three-site stockholding redundancy + geographic dispersal + tourist-surge over-stocking"},
        {"label": "Procurement route", "value": "NHS Supply Chain + manufacturer agreements + NW collaborative procurement"},
        {"label": "Funding trajectory", "value": "Stable; three-site dispersal sustains structural write-down baseline"},
        {"label": "Delivery body", "value": "Trust Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Recent context", "value": "Trust historically scarred by Morecambe Bay Investigation (Kirkup 2015) — driving sustained governance/quality scrutiny"},
        {"label": "Policy owner", "value": "DHSC + NHSE North West + Lancashire and South Cumbria ICB"}
    ],
    "notes": "University Hospitals of Morecambe Bay NHSFT's inventories-written-down line is structurally elevated by its three-site DGH model spanning a geographically dispersed catchment (Lancaster, Barrow, Kendal) which sustains stockholding redundancy across pharmacy, theatres and maternity. The trust carries the long institutional shadow of the Morecambe Bay Investigation (Bill Kirkup, 2015) into preventable maternity deaths at Furness General — driving sustained CQC and NHSE governance scrutiny that raises stock-control formality. The trust sits within Lancashire and South Cumbria ICS where financial recovery pressure has driven tighter inventory management, but the absolute write-down level (£0.113M) reflects sound stock control given the multi-site dispersal.",
    "sources": [
        {"publisher": "University Hospitals of Morecambe Bay NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.uhmb.nhs.uk/about-us/publications-policies-and-procedures"},
        {"publisher": "CQC", "title": "UHMB NHSFT provider inspection (RTX)", "url": "https://www.cqc.org.uk/provider/RTX"},
        {"publisher": "DHSC", "title": "The Morecambe Bay Investigation (Kirkup Report 2015)", "url": "https://www.gov.uk/government/publications/morecambe-bay-investigation-report"},
        {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "NHS Supply Chain — annual report", "url": "https://www.supplychain.nhs.uk/"}
    ],
    "related": [
        "University Hospitals of Morecambe Bay NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain"
    ]
}

NEW["Lease expenditure — Sandwell And West Birmingham Hospitals NHS Trust"] = {
    "aliases": [
        {"name": "Lease expenditure", "parent": "Sandwell And West Birmingham Hospitals NHS Trust"}
    ],
    "description": "Operating lease expenditure (post-IFRS 16) at Sandwell and West Birmingham Hospitals NHS Trust — covering short-life leased clinical and admin space ahead of and during transition to the new Midland Metropolitan University Hospital (MMUH) at Smethwick which opened October 2024, vehicle fleet operating leases, and minor equipment leases. The trust's recent estate consolidation from Sandwell General + Birmingham City Hospital onto the new MMUH site sustains a transitional lease footprint covering decant, retained-services and outpatient hubs.",
    "beneficiaries": "Serves c. 530,000 residents of Sandwell, west Birmingham (Ladywood, Soho, Smethwick) and parts of Dudley; c. 7,000 WTE staff; Midland Metropolitan University Hospital MMUH (c. 740 beds, opened Oct 2024) plus retained outpatient/diagnostic activity at Sandwell General + Birmingham City sites in transition + Rowley Regis Community Hospital + Leasowes Intermediate Care Centre.",
    "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · IFRS 16 (as adapted by FReM/GAM) · Health and Care Act 2022 · Care Act 2014 · NHS Standard Contract",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.112M"},
        {"label": "Trust profile", "value": "Major DGH provider with new MMUH (Smethwick, opened Oct 2024)"},
        {"label": "Catchment", "value": "c. 530,000 residents Sandwell + west Birmingham"},
        {"label": "Workforce", "value": "c. 7,000 WTE"},
        {"label": "Estate", "value": "MMUH (740 beds, opened Oct 2024) + retained Sandwell + City sites in transition + Rowley Regis + Leasowes"},
        {"label": "Coverage", "value": "Short-life and low-value leases excluded from RoU under GAM treatment"},
        {"label": "Specific driver", "value": "Transitional decant + retained-service space + vehicle fleet + minor equipment during MMUH ramp-up"},
        {"label": "YoY change", "value": "Transitioning down as MMUH absorbs activity from legacy sites"},
        {"label": "Recent context", "value": "MMUH opening (Oct 2024) was 8 years late vs original 2018 ISD — Carillion collapse 2018 + remediation"},
        {"label": "PFI exposure", "value": "MMUH delivered via revised post-Carillion construction contract (not PFI)"},
        {"label": "Cost growth", "value": "MMUH outturn cost c. £988M vs original £350M baseline (NAO scrutiny)"},
        {"label": "Policy owner", "value": "DHSC + NHSE Midlands + Black Country ICB + IPA / NAO oversight"}
    ],
    "notes": "Sandwell and West Birmingham's lease line sits at a transitional moment — the long-delayed Midland Metropolitan University Hospital (MMUH) at Smethwick finally opened to patients in October 2024 after Carillion's 2018 collapse halted construction at c. 70% completion and triggered a £988M outturn vs original £350M baseline (a NAO-scrutinised cost overrun). Operating leases cover transitional decant space, retained outpatient/diagnostic activity at the legacy Sandwell General and Birmingham City Hospital sites, and the vehicle fleet supporting community services. The lease line will continue to step down as MMUH absorbs the full activity envelope and legacy sites are released. The trust forms part of Black Country ICS and is a key delivery partner for the ICB's deprivation-targeted population health priorities.",
    "sources": [
        {"publisher": "Sandwell and West Birmingham Hospitals NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.swbh.nhs.uk/about-us/publications/"},
        {"publisher": "NAO", "title": "Investigation: the collapse of Carillion (HC 1002, 2018)", "url": "https://www.nao.org.uk/reports/investigation-the-collapse-of-carillion/"},
        {"publisher": "CQC", "title": "Sandwell and West Birmingham Hospitals NHS Trust inspection (RXK)", "url": "https://www.cqc.org.uk/provider/RXK"},
        {"publisher": "HM Treasury", "title": "FReM / GAM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "Infrastructure and Projects Authority", "title": "Government Major Projects Portfolio — MMUH entry", "url": "https://www.gov.uk/government/collections/government-major-projects-portfolio-data"}
    ],
    "related": [
        "Sandwell And West Birmingham Hospitals NHS Trust",
        "Premises & Infrastructure",
        "Carillion collapse"
    ]
}

NEW["Lease expenditure — Medway NHS Foundation Trust"] = {
    "aliases": [
        {"name": "Lease expenditure", "parent": "Medway NHS Foundation Trust"}
    ],
    "description": "Operating lease expenditure (post-IFRS 16) at Medway NHSFT — covering short-life leased clinical and admin space, vehicle fleet operating leases for community-acute services, and minor equipment leases across Medway Maritime Hospital (Gillingham), the trust's main 600-bed acute DGH serving the Medway towns and Swale district of Kent. Operational lease scope is constrained by IFRS 16 GAM treatment which moves most non-low-value leases onto the right-of-use balance sheet rather than this expense line.",
    "beneficiaries": "Serves c. 425,000 residents of Medway (Chatham, Gillingham, Rochester, Strood, Rainham) and Swale (Sittingbourne, Sheppey, Faversham); c. 4,800 WTE staff; Medway Maritime Hospital (c. 600 beds) — sole DGH for the Medway and Swale population — covering ED, maternity, paediatrics, general medicine and surgery, oncology day care.",
    "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · IFRS 16 (as adapted by FReM/GAM) · Health and Care Act 2022 · NHS Standard Contract",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.111M"},
        {"label": "Trust profile", "value": "Sole DGH for Medway + Swale (425k catchment)"},
        {"label": "Catchment", "value": "c. 425,000 residents Medway + Swale"},
        {"label": "Workforce", "value": "c. 4,800 WTE"},
        {"label": "Estate", "value": "Medway Maritime Hospital (c. 600 beds) — Gillingham"},
        {"label": "Coverage", "value": "Short-life and low-value leases excluded from RoU under GAM treatment"},
        {"label": "Specific driver", "value": "Vehicle fleet + minor equipment leases + short-life space"},
        {"label": "YoY change", "value": "Stable; minor lease re-pricing"},
        {"label": "Peer benchmark", "value": "Below DGH median; single-site model limits leased estate"},
        {"label": "Recent context", "value": "Trust has been under sustained CQC + NHSE quality scrutiny — historic Special Measures (2013) and ongoing recovery support"},
        {"label": "Workforce interaction", "value": "Vehicle fleet sustains discharge-flow and intermediate-care links with Medway Council"},
        {"label": "Policy owner", "value": "DHSC + NHSE South East + Kent and Medway ICB"}
    ],
    "notes": "Medway NHSFT's lease line is structurally modest, constrained by the trust's single-site (Medway Maritime Hospital) model and the IFRS 16 GAM treatment which captures most non-low-value leases as right-of-use depreciation rather than operating lease expense. The trust carries a long quality-recovery history — placed in Special Measures in 2013 (one of the original 11 Keogh Review trusts), it spent a decade rebuilding governance and CQC ratings. Despite progress, the trust continues to feature in NHSE oversight escalation and faces structural workforce pressure from being a single-site DGH adjacent to higher-paying London trusts. The trust forms part of Kent and Medway ICS where elective recovery and primary-care access are the dominant population health priorities.",
    "sources": [
        {"publisher": "Medway NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.medway.nhs.uk/about-us/publications/"},
        {"publisher": "CQC", "title": "Medway NHSFT inspection (RPA)", "url": "https://www.cqc.org.uk/provider/RPA"},
        {"publisher": "NHS England", "title": "Keogh Review (2013) — 14 trust mortality review", "url": "https://www.nhs.uk/NHSEngland/bruce-keogh-review/Pages/published-reports.aspx"},
        {"publisher": "HM Treasury", "title": "FReM / GAM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
    ],
    "related": [
        "Medway NHS Foundation Trust",
        "Premises & Infrastructure",
        "Keogh Review"
    ]
}

NEW["Amortisation — George Eliot Hospital NHS Trust"] = {
    "aliases": [
        {"name": "Amortisation", "parent": "George Eliot Hospital NHS Trust"}
    ],
    "description": "Amortisation of intangible assets at George Eliot Hospital NHS Trust — capitalised software (PAS, EPR/Lorenzo successor module rollouts, e-rostering, e-prescribing), capitalised licences and intangibles across the trust's single-site small-DGH footprint at Nuneaton serving North Warwickshire, Hinckley & Bosworth and parts of South Leicestershire. As a small DGH (c. 350 beds) the absolute amortisation envelope is modest but the digital-systems share is structurally rising.",
    "beneficiaries": "Serves c. 350,000 residents of North Warwickshire, Nuneaton and Bedworth, Hinckley & Bosworth and parts of South Leicestershire; c. 2,800 WTE staff; George Eliot Hospital (c. 350 beds) — single-site small DGH covering ED, maternity, paediatrics, general medicine, general/orthopaedic surgery, oncology day-case.",
    "legal_basis": "IAS 38 Intangible Assets (as adapted by FReM/GAM) · NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract",
    "key_stats": [
        {"label": "Amortisation 2024-25", "value": "£0.111M"},
        {"label": "Trust profile", "value": "Single-site small DGH (Nuneaton)"},
        {"label": "Catchment", "value": "c. 350,000 residents North Warwickshire + Hinckley & Bosworth + parts of South Leicestershire"},
        {"label": "Workforce", "value": "c. 2,800 WTE"},
        {"label": "Estate", "value": "George Eliot Hospital (c. 350 beds)"},
        {"label": "Asset anchor", "value": "PAS + EPR module rollouts + e-rostering + e-prescribing + capitalised licences"},
        {"label": "Specific driver", "value": "Frontline Digitisation programme capitalisation + EPR refresh + e-prescribing rollout"},
        {"label": "YoY change", "value": "Rising as digital programme assets are capitalised"},
        {"label": "Peer benchmark", "value": "Below small-DGH median; single-site model limits intangible stack"},
        {"label": "Recent context", "value": "Trust merger discussions with University Hospitals Coventry and Warwickshire intermittently revisited"},
        {"label": "Digital programme", "value": "Frontline Digitisation funding routes capitalised software through GEHT"},
        {"label": "Policy owner", "value": "DHSC + NHSE Midlands + Coventry and Warwickshire ICB"}
    ],
    "notes": "George Eliot Hospital NHS Trust's amortisation line is modest in absolute terms, reflecting the trust's small single-site DGH scale (c. 350 beds, c. 2,800 WTE) but is on a structurally rising trajectory as the Frontline Digitisation programme funds capitalised software (EPR module rollouts, e-prescribing, e-rostering) onto the intangible asset register. The trust's merger with University Hospitals Coventry and Warwickshire has been intermittently discussed but not progressed; the trust remains in Coventry and Warwickshire ICS with elective recovery and rural-access challenges as the principal pressures. The IAS 38 amortisation profile is sensitive to the timing of capitalisation cut-overs as Frontline Digitisation modules go live and asset useful-life assumptions are reset.",
    "sources": [
        {"publisher": "George Eliot Hospital NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.geh.nhs.uk/about-us/publications/"},
        {"publisher": "CQC", "title": "George Eliot Hospital NHS Trust inspection (RLT)", "url": "https://www.cqc.org.uk/provider/RLT"},
        {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/"},
        {"publisher": "HM Treasury", "title": "FReM 2024-25 (IAS 38 adaptation)", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
    ],
    "related": [
        "George Eliot Hospital NHS Trust",
        "Premises & Infrastructure",
        "Frontline Digitisation programme"
    ]
}

NEW["Lease expenditure — Kettering General Hospital NHS Foundation Trust"] = {
    "aliases": [
        {"name": "Lease expenditure", "parent": "Kettering General Hospital NHS Foundation Trust"}
    ],
    "description": "Operating lease expenditure (post-IFRS 16) at Kettering General Hospital NHSFT — covering short-life leased clinical and admin space, vehicle fleet operating leases, modular/decant building leases supporting the New Hospital Programme (NHP) cohort site refurbishment and minor equipment leases across the trust's main DGH at Kettering serving North Northamptonshire (Kettering, Corby, Wellingborough, Rushden) plus rural Rutland flow.",
    "beneficiaries": "Serves c. 360,000 residents of North Northamptonshire (Kettering, Corby, Wellingborough, Rushden) and parts of Rutland; c. 4,400 WTE staff; Kettering General Hospital (c. 580 beds) — single-site main DGH covering ED, maternity, paediatrics, general/orthopaedic/vascular surgery, stroke unit and cancer day-case.",
    "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · IFRS 16 (as adapted by FReM/GAM) · Health and Care Act 2022 · NHS Standard Contract · New Hospital Programme governance (HM Treasury / DHSC)",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.110M"},
        {"label": "Trust profile", "value": "Single-site main DGH for North Northamptonshire"},
        {"label": "Catchment", "value": "c. 360,000 residents North Northamptonshire + parts of Rutland"},
        {"label": "Workforce", "value": "c. 4,400 WTE"},
        {"label": "Estate", "value": "Kettering General Hospital (c. 580 beds)"},
        {"label": "Coverage", "value": "Short-life and low-value leases excluded from RoU under GAM treatment"},
        {"label": "Specific driver", "value": "Vehicle fleet + minor equipment + decant/modular leases supporting NHP refurbishment"},
        {"label": "YoY change", "value": "Sensitive to NHP cohort capital programme phasing"},
        {"label": "NHP status", "value": "Trust selected for NHP — refurbishment cohort (post-2025 review revised priority)"},
        {"label": "Recent context", "value": "NHP programme reset (2025) reordered cohorts; Kettering sits in revised pipeline"},
        {"label": "Workforce interaction", "value": "Vehicle fleet sustains discharge-flow + community links"},
        {"label": "Policy owner", "value": "DHSC + NHSE Midlands + Northamptonshire ICB + IPA / NAO oversight"}
    ],
    "notes": "Kettering General Hospital NHSFT's lease line is a small but operationally important component, dominated by vehicle fleet and decant/modular building leases supporting the New Hospital Programme (NHP) refurbishment of the Kettering site. The trust was originally a NHP cohort 4 scheme but the 2025 NHP programme reset (following the new government's review and reprioritisation) reshuffled cohorts and pushed some major capital activity beyond 2030 — this in turn increases the role of operating leases for transitional/decant accommodation in the meantime. The trust forms part of Northamptonshire ICS (jointly with Northampton General — the two trusts operate as a Group with shared executives) and the leased footprint reflects the short-cycle estate workarounds while the main capital scheme is sequenced.",
    "sources": [
        {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.kgh.nhs.uk/our-publications"},
        {"publisher": "CQC", "title": "Kettering General Hospital NHSFT inspection (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"},
        {"publisher": "DHSC", "title": "New Hospital Programme — review and reprioritisation 2025", "url": "https://www.gov.uk/government/collections/new-hospital-programme"},
        {"publisher": "NAO", "title": "New Hospital Programme — progress update", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"},
        {"publisher": "HM Treasury", "title": "FReM / GAM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"}
    ],
    "related": [
        "Kettering General Hospital NHS Foundation Trust",
        "Premises & Infrastructure",
        "New Hospital Programme"
    ]
}

NEW["Lease expenditure — Airedale NHS Foundation Trust"] = {
    "aliases": [
        {"name": "Lease expenditure", "parent": "Airedale NHS Foundation Trust"}
    ],
    "description": "Operating lease expenditure (post-IFRS 16) at Airedale NHSFT — covering short-life leased clinical and admin space, vehicle fleet operating leases for community-acute service links, decant/modular building leases supporting the New Hospital Programme cohort response to RAAC (reinforced autoclaved aerated concrete) structural risk at Airedale General Hospital, and minor equipment leases across the trust's main DGH at Steeton serving the Aire and Wharfe valleys (West Yorkshire and parts of North Yorkshire/East Lancashire).",
    "beneficiaries": "Serves c. 240,000 residents of the Aire, Wharfe, Worth and Calder valleys (Keighley, Ilkley, Skipton, Settle, Bingley, Silsden) plus parts of East Lancashire (Pendle); c. 3,200 WTE staff; Airedale General Hospital Steeton (c. 320 beds) — main DGH covering ED, maternity, general medicine and surgery, stroke unit, plus Skipton General Hospital (community + outpatient).",
    "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · IFRS 16 (as adapted by FReM/GAM) · Health and Care Act 2022 · NHS Standard Contract · New Hospital Programme RAAC governance",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.106M"},
        {"label": "Trust profile", "value": "DGH for Aire and Wharfe valleys + parts of East Lancashire"},
        {"label": "Catchment", "value": "c. 240,000 residents Aire/Wharfe/Worth valleys + Pendle"},
        {"label": "Workforce", "value": "c. 3,200 WTE"},
        {"label": "Estate", "value": "Airedale General Hospital (c. 320 beds, RAAC-affected) + Skipton General"},
        {"label": "Coverage", "value": "Short-life and low-value leases excluded from RoU under GAM treatment"},
        {"label": "Specific driver", "value": "Vehicle fleet + decant/modular leases responding to RAAC programme + minor equipment"},
        {"label": "YoY change", "value": "Rising vs baseline as RAAC mitigation requires temporary leased capacity"},
        {"label": "NHP status", "value": "RAAC priority cohort — full hospital rebuild planned via New Hospital Programme"},
        {"label": "RAAC context", "value": "Airedale was one of original 7 RAAC-affected NHS hospitals (Aug 2023 NHSE survey)"},
        {"label": "Workforce interaction", "value": "Vehicle fleet sustains community + virtual-ward provision (Airedale is a virtual-ward early adopter)"},
        {"label": "Policy owner", "value": "DHSC + NHSE Yorkshire and the Humber + West Yorkshire ICB + IPA / NAO oversight"}
    ],
    "notes": "Airedale NHSFT's lease line is structurally elevated by the trust's status as one of the seven RAAC-affected hospitals identified by NHS England's August 2023 estate-risk survey — Airedale General Hospital was constructed almost entirely from reinforced autoclaved aerated concrete with end-of-life risk requiring full rebuild. The trust is a New Hospital Programme priority cohort (RAAC strand) and operating leases now cover decant accommodation, modular clinical-space hires and continuity-planning estate during the multi-year construction sequence. Beyond RAAC, Airedale is a national virtual-ward early adopter (the Digital Care Hub at Airedale supports remote-monitoring across multiple ICSs) and the leased vehicle fleet sustains the community-acute link. The trust forms part of West Yorkshire ICS where elective recovery, mental-health flow and rural access pressures shape local commissioning priorities.",
    "sources": [
        {"publisher": "Airedale NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.airedale-trust.nhs.uk/about-us/publications/"},
        {"publisher": "CQC", "title": "Airedale NHSFT inspection (RCF)", "url": "https://www.cqc.org.uk/provider/RCF"},
        {"publisher": "DHSC", "title": "New Hospital Programme — RAAC cohort", "url": "https://www.gov.uk/government/collections/new-hospital-programme"},
        {"publisher": "NAO", "title": "Reinforced autoclaved aerated concrete (RAAC) in the NHS", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"},
        {"publisher": "HM Treasury", "title": "FReM / GAM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"}
    ],
    "related": [
        "Airedale NHS Foundation Trust",
        "Premises & Infrastructure",
        "New Hospital Programme",
        "RAAC NHS estate risk"
    ]
}
