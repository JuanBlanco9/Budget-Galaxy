# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 08 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Establishment costs — Frimley Health NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Frimley Health NHS Foundation Trust"}],
        "description": "Frimley Health's £10.24M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the Frimley Park + Wexham Park + Heatherwood three-site combine. The trust formed via the Oct 2014 acquisition of Heatherwood and Wexham Park, and operates the new Heatherwood elective hub (opened Mar 2022) — sustaining a multi-site corporate-services overhead in Frimley Health & Care ICS at the Surrey/Berkshire/Hampshire boundary.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 900,000 catchment across north-east Hampshire, west Surrey and south Buckinghamshire / Berkshire; c. 230,000 ED attendances/yr (Frimley Park + Wexham Park EDs combined); c. 130,000 elective + day-case admissions/yr (Heatherwood the dedicated cold-site elective hub).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£10.24M"},
            {"label": "Trust scale", "value": "c. 9,500 WTE across Frimley Park + Wexham Park + Heatherwood; c. 900,000 catchment across three counties"},
            {"label": "2014 acquisition", "value": "Heatherwood and Wexham Park acquired by Frimley Park 1 Oct 2014 — first NHS FT acquisition of failing trust under Health and Social Care Act 2012 regime"},
            {"label": "New Heatherwood elective hub", "value": "Opened Mar 2022 — purpose-built cold-site elective surgical hub; training + change-mgmt feed establishment baseline through opening cycle"},
            {"label": "Composition", "value": "Telecoms + postage + printing + training + courses + recruitment-advertising + minor IT/software subs + professional fees + agency-recruitment commission"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike action drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Trust runs Epic EPR (live since 2019) — established change-mgmt baseline; ongoing optimisation + interoperability spend"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate rise raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £8.5M → 2022-23 (Heatherwood opening) £9.5M → 2024-25 £10.24M — sustained tri-site overhead + recruitment churn"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications corporate functions + EPR programme office + NHS Resolution"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Frimley Health & Care ICB; cross-ICB working with BOB + Hampshire & IoW"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 separate Frimley Park + Heatherwood/Wexham Park establishment baselines · Successor: ICS-shared corporate-services pooling + Epic optimisation phase"}
        ],
        "notes": "Frimley Health's establishment line reflects the cumulative overhead of running three acute sites that span three ICSs (Frimley, BOB, Hampshire & IoW) — multi-system commissioner interfaces multiply professional-fee and contracting overhead vs single-ICS peers. The Oct 2014 acquisition of Heatherwood and Wexham Park was the first FT-led rescue of a failing trust under the Health and Social Care Act 2012 regime, leaving residual harmonisation cost. The Mar 2022 Heatherwood elective hub opening drove a step-up in training and change-mgmt spend through 2022-24. Industrial action 2023-24 layered rota-restructuring and recruitment-advertising costs; Apr 2025 NIC step-up raises forward professional-fee cost.",
        "sources": [
            {"publisher": "Frimley Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.fhft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Frimley Health NHS FT provider profile (RDU)", "url": "https://www.cqc.org.uk/provider/RDU"},
            {"publisher": "NHS England", "title": "Operating framework 2024-25 + provider planning guidance", "url": "https://www.england.nhs.uk/publication/2024-25-priorities-and-operational-planning-guidance/"}
        ],
        "related": ["Frimley Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Establishment costs — Royal Devon University Healthcare NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "General supplies & services — York and Scarborough Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
        "description": "York and Scarborough's £10.15M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies and minor expensed equipment across York Hospital, Scarborough Hospital, Bridlington Hospital and a footprint of community hospitals (Selby, Malton, Whitby, Easingwold, Archways). The trust's c. 7,500 km² catchment across North Yorkshire — among the largest acute geographies in England — multiplies inbound logistics cost on the supplies baseline.",
        "beneficiaries": "c. 9,000 WTE staff serving c. 800,000 residents across York, Scarborough, Ryedale, the East Riding coastal strip and rural North Yorkshire over c. 7,500 km²; c. 195,000 ED attendances/yr (York + Scarborough EDs combined); c. 100,000 elective + day-case admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£10.15M"},
            {"label": "Trust scale", "value": "c. 9,000 WTE across York + Scarborough + Bridlington + 5 community hospitals; c. 800,000 catchment"},
            {"label": "Geographic multiplier", "value": "c. 7,500 km² catchment — among largest English acute footprints; rural-coastal logistics overhead on inbound consumables"},
            {"label": "Site model", "value": "York Hospital (main DGH, c. 700 beds) + Scarborough Hospital (coastal DGH) + Bridlington + community hospitals"},
            {"label": "NHP cohort context", "value": "Scarborough Hospital in original 40-hospital New Hospital Programme cohort; Jan 2025 NHP Reset rephased delivery — backlog patching consumables remain elevated pre-rebuild"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Humber and North Yorkshire ICS regional collaboration + minor local spot-buy for rural community sites"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn + agency backfill consumable use"},
            {"label": "Procurement Act 2023 + Apr 2025 NIC", "value": "New regime live Oct 2024; Apr 2025 employer-NIC step-up feeds forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £8M → 2022-23 £9M → 2024-25 £10.15M — sustained CPI + activity recovery + condition-driven patching at Scarborough"},
            {"label": "Delivery body + policy owner", "value": "Trust Procurement + Estates + NHS Supply Chain + HNY ICS collaborative; NHSE Provider Finance + DHSC + HNY ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RCB 2023-2024; NHP business case Scarborough; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 York Teaching Hospitals + 2012 Scarborough acquisition baselines · Successor: NHP-Reset Scarborough rebuild + ICS-collaborative procurement scaling"}
        ],
        "notes": "York and Scarborough's supplies line is shaped by its outsized rural-coastal North Yorkshire geography — c. 7,500 km² adds inbound-logistics cost on inbound consumables that single-DGH peers do not carry. Scarborough Hospital's New Hospital Programme cohort status, rephased rather than cancelled at the Jan 2025 NHP Reset, leaves backlog-patching consumables elevated through the rebuild lead-in. The Humber and North Yorkshire ICS collaborative procurement function and NHS Supply Chain dominate framework spend; Procurement Act 2023 implementation from Oct 2024 reshapes architecture, and Apr 2025 employer-NIC pass-through feeds forward unit-cost. Industrial action 2023-24 layered cancellation re-stocking and agency-backfill consumable churn through the year.",
        "sources": [
            {"publisher": "York and Scarborough Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yorkhospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24 + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme + Jan 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-review"},
            {"publisher": "Care Quality Commission", "title": "York and Scarborough provider profile (RCB)", "url": "https://www.cqc.org.uk/provider/RCB"}
        ],
        "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "New Hospital Programme", "General supplies & services — West Hertfordshire Hospitals NHS Trust"]
    },
    "Establishment costs — The Shrewsbury and Telford Hospital NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
        "description": "SaTH's £9.96M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the Royal Shrewsbury Hospital + Princess Royal Hospital Telford two-site footprint. The trust carries elevated establishment cost driven by the Ockenden Report (Mar 2022) implementation programme — sustained governance, training, professional-fee and recruitment-advertising spend on maternity reform — alongside the Hospitals Transformation Programme reconfiguration in development.",
        "beneficiaries": "c. 6,500 WTE staff serving c. 500,000 residents across Shropshire, Telford & Wrekin, and parts of mid-Wales; c. 145,000 ED attendances/yr (Royal Shrewsbury + Princess Royal EDs combined); c. 65,000 elective + day-case admissions/yr; c. 4,200 deliveries/yr (post-Ockenden specialist intake-restricted maternity).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£9.96M"},
            {"label": "Trust scale", "value": "c. 6,500 WTE across Royal Shrewsbury + Princess Royal Telford; c. 500,000 catchment incl. mid-Wales cross-border flow"},
            {"label": "Ockenden Report context", "value": "Mar 2022 Ockenden Final Report on SaTH maternity — c. 200 recommendations driving sustained governance, training, recruitment-advertising spend on midwifery + obstetric improvement"},
            {"label": "Hospitals Transformation Programme", "value": "SaTH HTP reconfiguration of Royal Shrewsbury + Princess Royal in pre-construction; programme office + business-case professional-fee spend feeds establishment line"},
            {"label": "Composition", "value": "Telecoms + postage + printing + training + courses + recruitment-advertising + minor IT/software subs + professional fees + agency-recruitment commission"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + recruitment-advertising churn"},
            {"label": "Frontline Digitisation EPR", "value": "Trust on FD-funded EPR rollout pathway — training + change-mgmt feed line"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate rise raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7M → 2022-23 (post-Ockenden) £8.8M → 2024-25 £9.96M — sustained Ockenden + HTP overhead"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications corporate functions + Ockenden Improvement Plan office + HTP programme office"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Shropshire, Telford and Wrekin ICB + NHSE Maternity Transformation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Ockenden 2019 baseline · Successor: HTP reconfiguration completion + ICS-shared corporate-services pooling"}
        ],
        "notes": "SaTH's establishment line is structurally inflated by the Ockenden Report (March 2022 Final Report) implementation programme — c. 200 recommendations on maternity governance, midwifery training, obstetric staffing and family-engagement that the trust must evidence delivery against, with NHSE and CQC monitoring sustaining a heavy professional-fee, training and recruitment-advertising baseline. The Hospitals Transformation Programme reconfiguration of Royal Shrewsbury and Princess Royal is in business-case development, layering programme-office cost. Industrial action 2023-24 added rota-restructuring and recruitment cost; Apr 2025 NIC step-up raises forward professional-fee and retainer cost. STW ICB shared-corporate-services pooling is the medium-term lever.",
        "sources": [
            {"publisher": "The Shrewsbury and Telford Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sath.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Ockenden Review — Final Report (Mar 2022)", "url": "https://www.gov.uk/government/publications/final-report-of-the-ockenden-review"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "SaTH provider profile (RXW)", "url": "https://www.cqc.org.uk/provider/RXW"}
        ],
        "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Establishment costs — Frimley Health NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "General supplies & services — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "Sheffield Teaching Hospitals' £9.91M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the Royal Hallamshire, Northern General, Weston Park (cancer), Jessop Wing (women's), and Charles Clifford Dental hospital sites. As one of England's largest teaching trusts and a tertiary referral centre for South Yorkshire and parts of Derbyshire/Lincolnshire, the multi-site academic footprint sustains a wide non-clinical consumables baseline.",
        "beneficiaries": "c. 19,000 WTE staff serving a c. 640,000 Sheffield primary catchment plus c. 2.0M South Yorkshire / North Derbyshire / North Lincolnshire / Bassetlaw tertiary catchment; c. 195,000 ED attendances/yr at Northern General (also South Yorkshire MTC); c. 175,000 elective + day-case admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£9.91M"},
            {"label": "Trust scale", "value": "c. 19,000 WTE across 5 specialist hospitals; one of England's largest teaching acute trusts"},
            {"label": "Major Trauma Centre", "value": "Northern General Hospital — South Yorkshire MTC; drives high non-clinical consumables baseline on emergency floors"},
            {"label": "Tertiary specialty mix", "value": "Weston Park cancer centre + Jessop Wing women's + Charles Clifford Dental — specialist hotel-services consumables across distinct catering + linen profiles"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + South Yorkshire ICS regional collaboration + trust-direct contracts"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn + agency backfill consumable use"},
            {"label": "Procurement Act 2023 + Apr 2025 NIC", "value": "New regime live Oct 2024; Apr 2025 employer-NIC step-up feeds forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7.5M → 2022-23 £8.8M → 2024-25 £9.91M — sustained CPI + activity recovery; relatively contained vs trust scale due to mature procurement function"},
            {"label": "Delivery body + policy owner", "value": "Trust Procurement + Estates + NHS Supply Chain + SY ICS collaborative; NHSE Provider Finance + DHSC + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RHQ 2022-2024; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2001 separate Sheffield acute trusts · Successor: South Yorkshire ICS collaborative procurement scaling + Sheffield Children's joint working"},
            {"label": "Academic context", "value": "University of Sheffield Medical School partnership — research-grade consumables segregation; NIHR BRC + CRF activity"}
        ],
        "notes": "Sheffield Teaching Hospitals' supplies line reflects breadth of specialist site portfolio — Northern General's MTC and emergency floor, Royal Hallamshire's tertiary medicine, Weston Park cancer centre, Jessop Wing women's and Charles Clifford Dental produce a wider non-clinical consumables profile than any single-site DGH. Mature in-house procurement and NHS Supply Chain integration keep unit-cost contained. South Yorkshire ICS collaborative procurement and University of Sheffield partnership shape category strategy. Industrial action 2023-24 layered cancellation re-stocking churn; Procurement Act 2023 (Oct 2024) reshapes architecture; Apr 2025 NIC pass-through is the dominant near-term unit-cost driver.",
        "sources": [
            {"publisher": "Sheffield Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24 + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Operating framework 2024-25 + provider planning guidance", "url": "https://www.england.nhs.uk/publication/2024-25-priorities-and-operational-planning-guidance/"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Teaching Hospitals provider profile (RHQ)", "url": "https://www.cqc.org.uk/provider/RHQ"}
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — York and Scarborough Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Oxford University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
        "description": "Oxford University Hospitals' £9.90M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the John Radcliffe, Churchill, Nuffield Orthopaedic Centre and Horton General (Banbury) sites. As a tertiary academic centre with national specialist services (transplant, neurosciences, cardiac, paediatric ECMO) and the University of Oxford partnership, the line carries an elevated non-clinical consumables profile shaped by research-grade requirements and four-site logistics.",
        "beneficiaries": "c. 14,500 WTE staff serving c. 700,000 Oxfordshire primary catchment plus c. 2.5M Thames Valley + national tertiary referrals; c. 175,000 ED attendances/yr (John Radcliffe MTC + Horton); c. 130,000 elective + day-case admissions/yr (NOC orthopaedic + Churchill cancer concentrations).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£9.90M"},
            {"label": "Trust scale", "value": "c. 14,500 WTE across John Radcliffe + Churchill + NOC + Horton; tertiary academic centre"},
            {"label": "Major Trauma Centre", "value": "John Radcliffe — Thames Valley MTC; drives high non-clinical consumables on emergency floors"},
            {"label": "Tertiary specialty mix", "value": "Transplantation + cardiac + neurosciences (JR) + cancer (Churchill) + orthopaedics (NOC) — specialist hotel-services profile"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + BOB ICS regional collaboration + trust-direct + research-procurement gateway with University of Oxford"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn + agency backfill consumable use"},
            {"label": "Procurement Act 2023 + Apr 2025 NIC", "value": "New regime live Oct 2024; Apr 2025 employer-NIC step-up feeds forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7.5M → 2022-23 £8.5M → 2024-25 £9.90M — sustained CPI + activity recovery"},
            {"label": "Academic + research context", "value": "University of Oxford partnership; NIHR BRC; Pandemic Preparedness research footprint — research-grade consumable segregation"},
            {"label": "Delivery body + policy owner", "value": "Trust Procurement + Estates + NHS Supply Chain + BOB ICS collaborative; NHSE Provider Finance + DHSC + BOB ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RTH 2022-2024; Trust ARA; NIHR BRC reporting"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2007 Oxford Radcliffe + Nuffield Orthopaedic + 2011 Horton acquisitions · Successor: BOB ICS collaborative procurement + Oxford research-procurement gateway scaling"}
        ],
        "notes": "OUH's supplies line reflects four-site academic-tertiary breadth — JR's MTC and transplant/cardiac/neurosciences floors, Churchill's cancer concentration, NOC's orthopaedic specialty and Horton's Banbury DGH role each carry distinct hotel-services and consumables profiles. The University of Oxford partnership and NIHR BRC drive a research-grade procurement gateway segregating commercial-trial consumables. Industrial action 2023-24 layered cancellation re-stocking churn through high-acuity floors. BOB ICS collaborative procurement and NHS Supply Chain dominate framework spend; Procurement Act 2023 (live Oct 2024) reshapes architecture; Apr 2025 employer-NIC pass-through is the dominant near-term unit-cost driver.",
        "sources": [
            {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ouh.nhs.uk/about/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24 + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Oxford University Hospitals provider profile (RTH)", "url": "https://www.cqc.org.uk/provider/RTH"},
            {"publisher": "National Institute for Health and Care Research", "title": "Oxford Biomedical Research Centre", "url": "https://oxfordbrc.nihr.ac.uk/"}
        ],
        "related": ["Oxford University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Sheffield Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — The Newcastle Upon Tyne Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust"}],
        "description": "Newcastle Hospitals' £9.81M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the Royal Victoria Infirmary + Freeman Hospital + Great North Children's + community footprint. As one of the UK's leading academic medical centres, with national specialist services (cardiothoracic, transplant, paediatrics, neurosciences) and a Newcastle University partnership, the trust's professional-fee, training and recruitment-advertising baseline runs above peer DGHs.",
        "beneficiaries": "c. 16,000 WTE staff serving c. 800,000 Newcastle + Gateshead primary catchment plus c. 3.0M North East and Cumbria tertiary; c. 220,000 ED attendances/yr (RVI MTC + Great North Children's ED); c. 150,000 elective + day-case admissions/yr; national transplant + cardiothoracic flows.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£9.81M"},
            {"label": "Trust scale", "value": "c. 16,000 WTE across RVI + Freeman + Great North Children's + community sites; tertiary academic centre"},
            {"label": "Major Trauma Centre", "value": "Royal Victoria Infirmary — North East MTC; drives critical-care + emergency-medicine recruitment churn"},
            {"label": "National specialist services", "value": "Cardiothoracic transplant (Freeman) + paediatric BMT + neurosciences + Institute of Transplantation — concentrated specialist recruitment + training spend"},
            {"label": "Composition", "value": "Telecoms + postage + printing + training + courses + recruitment-advertising + minor IT/software subs + professional fees + agency-recruitment commission"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Trust on EPR rollout (Cerner Millennium / Oracle Health migration) — training + change-mgmt feed line"},
            {"label": "Newcastle University partnership", "value": "Joint clinical-academic posts + NIHR BRC — research-led recruitment overhead + professional-fee profile"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate rise raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7.5M → 2022-23 £8.8M → 2024-25 £9.81M — sustained academic + tertiary recruitment overhead"},
            {"label": "Delivery body + policy owner", "value": "Trust Finance + HR + IT + Communications + EPR programme office + Newcastle University joint office; NHSE Provider Finance + DHSC + NENC ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1998 Newcastle General + RVI + Freeman separate baselines · Successor: NENC ICS shared-corporate-services pooling + EPR optimisation phase"}
        ],
        "notes": "Newcastle Hospitals' establishment line reflects its position as one of the UK's leading academic medical centres — recruitment + retention advertising for cardiothoracic-transplant, paediatric-BMT, neurosciences and other national-specialist roles runs at a level peer DGHs do not approach. The Newcastle University partnership, NIHR BRC and Institute of Transplantation drive joint-academic professional-fee and training spend. Industrial action 2023-24 layered rota-restructuring on the academic-recruitment baseline. The Cerner Millennium / Oracle Health EPR migration sustains training and change-management spend. Apr 2025 NIC step-up raises forward professional-fee cost; NENC ICS shared-corporate-services pooling is the medium-term lever.",
        "sources": [
            {"publisher": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.newcastle-hospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Newcastle Hospitals provider profile (RTD)", "url": "https://www.cqc.org.uk/provider/RTD"},
            {"publisher": "National Institute for Health and Care Research", "title": "Newcastle Biomedical Research Centre", "url": "https://newcastlebrc.nihr.ac.uk/"}
        ],
        "related": ["The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Establishment costs — The Shrewsbury and Telford Hospital NHS Trust", "Frontline Digitisation programme"]
    },
    "General supplies & services — The Leeds Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Leeds Teaching Hospitals NHS Trust"}],
        "description": "LTHT's £9.72M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the Leeds General Infirmary, St James's University Hospital, Leeds Children's Hospital, Wharfedale Hospital and Chapel Allerton sites. As one of England's largest teaching trusts and West Yorkshire's tertiary referral centre, the multi-site academic footprint and Hospitals of the Future redevelopment programme shape a sustained non-clinical consumables baseline.",
        "beneficiaries": "c. 20,000 WTE staff serving c. 800,000 Leeds primary catchment plus c. 5.4M Yorkshire and Humber tertiary referrals; c. 240,000 ED attendances/yr (LGI MTC + St James's + Leeds Children's); c. 175,000 elective + day-case admissions/yr; national specialist transplant + paediatric flows.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£9.72M"},
            {"label": "Trust scale", "value": "c. 20,000 WTE across LGI + St James's + Leeds Children's + Wharfedale + Chapel Allerton; one of England's largest teaching trusts"},
            {"label": "Major Trauma Centre", "value": "Leeds General Infirmary — West Yorkshire MTC; drives high non-clinical consumables baseline on emergency floors"},
            {"label": "Tertiary specialty mix", "value": "Cardiac + transplant + paediatric (Leeds Children's) + cancer (St James's) — distinct hotel-services consumable profiles"},
            {"label": "Hospitals of the Future redevelopment", "value": "LGI redevelopment in NHP cohort; Jan 2025 Reset rephased delivery — backlog patching consumables remain elevated pre-rebuild"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + West Yorkshire ICS regional collaboration + trust-direct contracts"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn + agency backfill consumable use"},
            {"label": "Procurement Act 2023 + Apr 2025 NIC", "value": "New regime live Oct 2024; Apr 2025 employer-NIC step-up feeds forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7.5M → 2022-23 £8.7M → 2024-25 £9.72M — sustained CPI + activity recovery"},
            {"label": "Delivery body + policy owner", "value": "Trust Procurement + Estates + NHS Supply Chain + WY ICS collaborative; NHSE Provider Finance + DHSC + WY ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RR8 2022-2024; NHP business case LGI; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1998 separate Leeds General + St James's baselines · Successor: NHP Hospitals of the Future LGI rebuild + WY ICS collaborative procurement scaling"}
        ],
        "notes": "LTHT's supplies line reflects breadth of academic-tertiary site portfolio — LGI's MTC and emergency floor, St James's cancer concentration, Leeds Children's national paediatric flows and Wharfedale + Chapel Allerton specialty roles each carry distinct non-clinical consumable profiles. The Hospitals of the Future redevelopment programme (LGI rebuild in NHP cohort, rephased at Jan 2025 NHP Reset) leaves backlog-patching consumables elevated through the rebuild lead-in. West Yorkshire ICS collaborative procurement and NHS Supply Chain dominate framework spend; Procurement Act 2023 (live Oct 2024) reshapes architecture; industrial action 2023-24 layered cancellation re-stocking churn; Apr 2025 NIC pass-through is the dominant near-term unit-cost driver.",
        "sources": [
            {"publisher": "The Leeds Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24 + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS England", "title": "New Hospital Programme + Jan 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-review"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Leeds Teaching Hospitals provider profile (RR8)", "url": "https://www.cqc.org.uk/provider/RR8"}
        ],
        "related": ["The Leeds Teaching Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "New Hospital Programme", "General supplies & services — Oxford University Hospitals NHS Foundation Trust"]
    },
    "Establishment costs — Barts Health NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Barts Health NHS Trust"}],
        "description": "Barts Health's £9.68M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across The Royal London, St Bartholomew's, Whipps Cross, Newham and Mile End sites. Barts Health is the largest NHS trust in England by turnover and headcount, formed by the 2012 merger of three predecessor trusts, with the Royal London PFI (operational 2012) and active Whipps Cross redevelopment in the New Hospital Programme — sustaining a heavy multi-site corporate-services overhead.",
        "beneficiaries": "c. 19,000 WTE staff serving c. 2.5M east London residents (Tower Hamlets, Newham, Waltham Forest, City of London) plus tertiary cardiac (Barts Heart Centre); c. 460,000 ED attendances/yr across The Royal London, Whipps Cross, Newham; c. 200,000 elective + day-case admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£9.68M"},
            {"label": "Trust scale", "value": "Largest English NHS trust by turnover/headcount; c. 19,000 WTE across 5 sites; c. 2.5M east-London catchment"},
            {"label": "2012 merger context", "value": "Barts Health formed Apr 2012 via merger of Barts and the London + Newham + Whipps Cross — historic corporate-services consolidation overhead"},
            {"label": "Royal London PFI", "value": "Royal London + St Bartholomew's PFI (Skanska Innisfree consortium, operational 2012) — ongoing FM contract management overhead feeds professional fees"},
            {"label": "Whipps Cross NHP redevelopment", "value": "Whipps Cross in NHP cohort; Jan 2025 NHP Reset rephased delivery — programme-office professional-fee + business-case spend feeds line"},
            {"label": "Composition", "value": "Telecoms + postage + printing + training + courses + recruitment-advertising + minor IT/software subs + professional fees + agency-recruitment commission"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Trust on Cerner / Oracle Health EPR — training + change-mgmt feed line; convergence-optimisation phase"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate rise raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7.5M → 2022-23 £8.7M → 2024-25 £9.68M — sustained merger + Whipps Cross programme overhead"},
            {"label": "Delivery body + policy owner", "value": "Trust Finance + HR + IT + Communications + EPR programme office + Whipps Cross NHP team; NHSE Provider Finance + DHSC + NEL ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 Barts and the London + Newham + Whipps Cross separate baselines · Successor: NEL ICS shared-corporate-services pooling + Whipps Cross rebuild post-NHP Reset"}
        ],
        "notes": "Barts Health's establishment line reflects scale of England's largest NHS trust — 5-site east-London footprint serving high-deprivation catchments including Tower Hamlets and Newham, with three EDs accounting for c. 460,000 attendances/yr. The Royal London PFI (operational 2012) brings ongoing FM-contract-management professional-fee overhead. Whipps Cross's NHP cohort redevelopment, rephased rather than cancelled at the Jan 2025 NHP Reset, sustains business-case and programme-office spend. Industrial action 2023-24 layered rota-restructuring on the merger-residual baseline; Apr 2025 NIC step-up raises forward professional-fee cost; NEL ICS shared-corporate-services pooling is the medium-term lever.",
        "sources": [
            {"publisher": "Barts Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bartshealth.nhs.uk/annual-report"},
            {"publisher": "NHS England", "title": "New Hospital Programme + Jan 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-review"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Barts Health provider profile (R1H)", "url": "https://www.cqc.org.uk/provider/R1H"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"}
        ],
        "related": ["Barts Health NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Establishment costs — The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "General supplies & services — East Cheshire NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "East Cheshire NHS Trust"}],
        "description": "East Cheshire's £9.67M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across Macclesfield District General Hospital + community-hospital footprint (Knutsford, Congleton) and integrated community services across east Cheshire. The trust operates as one of England's smaller acute trusts, serving an affluent but geographically dispersed catchment, with sustained NHSE merger speculation and Cheshire & Merseyside ICS strategic-sustainability discussions framing the medium-term path.",
        "beneficiaries": "c. 2,800 WTE staff serving c. 200,000 east Cheshire residents (Macclesfield, Congleton, Knutsford, Wilmslow, Poynton); c. 65,000 ED attendances/yr at Macclesfield ED; c. 35,000 elective + day-case admissions/yr; integrated community-hospital + district nursing footprint.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£9.67M"},
            {"label": "Trust scale", "value": "c. 2,800 WTE across Macclesfield DGH + community hospitals (Knutsford, Congleton); among England's smaller acute trusts"},
            {"label": "Integrated community model", "value": "Acute + community-hospital + district nursing combine — broader non-clinical consumables base than acute-only peers of similar headcount"},
            {"label": "Strategic sustainability context", "value": "Long-running C&M ICS strategic-sustainability discussions on East Cheshire's small-acute viability; Manchester FT clinical-service pathway dependencies"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Cheshire & Merseyside ICS regional collaboration + minor local spot-buy"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn + agency backfill consumable use"},
            {"label": "Procurement Act 2023 + Apr 2025 NIC", "value": "New regime live Oct 2024; Apr 2025 employer-NIC step-up feeds forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7.5M → 2022-23 £8.8M → 2024-25 £9.67M — high relative supplies cost reflecting fixed-cost base on small WTE denominator"},
            {"label": "Delivery body + policy owner", "value": "Trust Procurement + Estates + NHS Supply Chain + C&M ICS collaborative; NHSE Provider Finance + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RJN 2022-2024; Trust ARA"},
            {"label": "Catchment profile", "value": "Affluent but dispersed east-Cheshire catchment — sustained per-capita supplies baseline shaped by community-hospital + district-nursing reach"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2010 Eastern Cheshire PCT acute services baseline · Successor: ongoing C&M ICS sustainability review + collaborative procurement scaling"}
        ],
        "notes": "East Cheshire's supplies line carries a high relative cost-per-WTE because the trust's small acute scale spreads fixed inbound-logistics and minimum-order overhead across c. 2,800 WTE — one of the smaller English acute trusts. The integrated community-hospital and district-nursing combine broadens the non-clinical consumables base relative to acute-only DGHs. C&M ICS strategic-sustainability discussions on small-acute viability and clinical-pathway dependencies on Manchester FT shape the medium-term operating model. Industrial action 2023-24 layered cancellation re-stocking churn; Procurement Act 2023 (live Oct 2024) reshapes architecture; Apr 2025 employer-NIC pass-through feeds forward unit-cost.",
        "sources": [
            {"publisher": "East Cheshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastcheshire.nhs.uk/About-The-Trust/publications.htm"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24 + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "East Cheshire NHS Trust provider profile (RJN)", "url": "https://www.cqc.org.uk/provider/RJN"},
            {"publisher": "NHS England", "title": "Operating framework 2024-25 + provider planning guidance", "url": "https://www.england.nhs.uk/publication/2024-25-priorities-and-operational-planning-guidance/"}
        ],
        "related": ["East Cheshire NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Imperial College Healthcare NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Imperial College Healthcare NHS Trust"}],
        "description": "Imperial's £9.59M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the St Mary's, Charing Cross, Hammersmith, Queen Charlotte's & Chelsea, and Western Eye sites. Imperial is one of England's largest academic acute trusts, formed Oct 2007 by Hammersmith + St Mary's merger, with five sites in NHP-cohort redevelopment, an Imperial College London partnership and tertiary specialty mix that sustain heavy professional-fee, training and recruitment overhead.",
        "beneficiaries": "c. 14,000 WTE staff serving c. 2.0M north-west London residents plus tertiary cardiac (Hammersmith), neurosciences (Charing Cross) and major-trauma (St Mary's) referrals; c. 350,000 ED attendances/yr (St Mary's MTC, Charing Cross, Hammersmith); c. 200,000 elective + day-case admissions/yr; c. 8,000 deliveries/yr (Queen Charlotte's tertiary maternity).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£9.59M"},
            {"label": "Trust scale", "value": "c. 14,000 WTE across 5 sites; c. 2.0M NW-London catchment + national specialist flows"},
            {"label": "2007 merger context", "value": "Imperial formed Oct 2007 via Hammersmith + St Mary's merger — created England's first academic-health-science centre"},
            {"label": "Major Trauma Centre + NHP", "value": "St Mary's — one of London's four MTCs; in NHP cohort with Charing Cross + Hammersmith; Jan 2025 NHP Reset rephased delivery"},
            {"label": "Imperial College London partnership", "value": "Imperial College AHSC + NIHR BRC — joint clinical-academic posts + research-led recruitment overhead"},
            {"label": "Composition", "value": "Telecoms + postage + printing + training + courses + recruitment-advertising + minor IT/software subs + professional fees + agency-recruitment commission"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Trust on Cerner / Oracle Health EPR pathway — training + change-mgmt feed line; convergence-optimisation phase"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate rise raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7.5M → 2022-23 £8.7M → 2024-25 £9.59M — sustained NHP + academic recruitment overhead"},
            {"label": "Delivery body + policy owner", "value": "Trust Finance + HR + IT + Communications + EPR programme office + Imperial College joint office + NHP team; NHSE Provider Finance + DHSC + NWL ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2007 separate Hammersmith + St Mary's establishment baselines · Successor: NWL ICS shared-corporate-services + NHP-Reset St Mary's redevelopment"}
        ],
        "notes": "Imperial's establishment line reflects the overhead of running five academic acute sites with national specialist services — St Mary's MTC, Hammersmith cardiac, Charing Cross neurosciences and Queen Charlotte's tertiary maternity each carry distinct recruitment + training profiles. The Imperial College London AHSC and NIHR BRC drive joint clinical-academic professional-fee spend. The NHP cohort redevelopment of St Mary's + Charing Cross + Hammersmith, rephased at Jan 2025 NHP Reset, sustains business-case and programme-office spend. Industrial action 2023-24 layered rota-restructuring; Apr 2025 NIC step-up raises forward professional-fee cost; NWL ICS shared-corporate-services pooling is the medium-term lever.",
        "sources": [
            {"publisher": "Imperial College Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.imperial.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "New Hospital Programme + Jan 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-review"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Imperial College Healthcare provider profile (RYJ)", "url": "https://www.cqc.org.uk/provider/RYJ"},
            {"publisher": "National Institute for Health and Care Research", "title": "Imperial Biomedical Research Centre", "url": "https://imperialbrc.nihr.ac.uk/"}
        ],
        "related": ["Imperial College Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Establishment costs — Barts Health NHS Trust", "New Hospital Programme"]
    },
    "Establishment costs — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Kingston's £9.44M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the single-site Kingston Hospital and the integrated community services (Hounslow + Richmond Community Healthcare partnership). Following the formation of the Kingston and Richmond NHS Foundation Trust group in late 2024 (acquisition of Hounslow & Richmond Community Healthcare), the trust's corporate-services baseline is in active integration phase, sustaining elevated professional-fee and harmonisation spend.",
        "beneficiaries": "c. 4,500 WTE staff serving c. 350,000 Kingston, Richmond and Hounslow residents; c. 110,000 ED attendances/yr at Kingston ED; c. 60,000 elective + day-case admissions/yr; c. 6,000 deliveries/yr at Kingston maternity (one of London's larger maternity units).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£9.44M"},
            {"label": "Trust scale", "value": "c. 4,500 WTE across Kingston Hospital + integrated Hounslow + Richmond community footprint; c. 350,000 catchment"},
            {"label": "2024 group formation", "value": "Kingston and Richmond NHS Foundation Trust group formed late 2024 via acquisition of Hounslow & Richmond Community Healthcare NHS Trust — corporate-services integration cost"},
            {"label": "Maternity scale", "value": "c. 6,000 deliveries/yr — among London's larger maternity units; sustained recruitment + training spend on midwifery + obstetric workforce"},
            {"label": "Composition", "value": "Telecoms + postage + printing + training + courses + recruitment-advertising + minor IT/software subs + professional fees + agency-recruitment commission"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Trust on Epic EPR (Apollo programme with Royal Surrey + Ashford & St Peter's collaboration) — training + change-mgmt feed line"},
            {"label": "Apollo EPR collaboration", "value": "Joint Epic implementation with Royal Surrey + Ashford & St Peter's — shared training + governance overhead"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate rise raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7M → 2022-23 £8.5M → 2024-25 £9.44M — sustained acute-community integration overhead + Apollo EPR rollout"},
            {"label": "Delivery body + policy owner", "value": "Trust Finance + HR + IT + Communications + EPR programme office + group-formation programme team; NHSE Provider Finance + DHSC + South West London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2024 stand-alone Kingston Hospital establishment baseline · Successor: full Kingston + Richmond group integration + Apollo EPR optimisation phase"}
        ],
        "notes": "Kingston Hospital's establishment line reflects the cumulative overhead of the late-2024 Kingston and Richmond NHS Foundation Trust group formation — acquiring Hounslow & Richmond Community Healthcare NHS Trust drove a step-up in corporate-services harmonisation spend through 2024-25 with continued integration cost forward. The Apollo Epic EPR programme — joint implementation with Royal Surrey and Ashford & St Peter's — sustains training, change-mgmt and governance overhead. The trust's c. 6,000-delivery maternity service is among London's larger units and adds recruitment + retention pressure on midwifery + obstetric workforce. Industrial action 2023-24 layered rota-restructuring; Apr 2025 NIC step-up raises forward professional-fee cost.",
        "sources": [
            {"publisher": "Kingston Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kingstonhospital.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Kingston Hospital provider profile (RAX)", "url": "https://www.cqc.org.uk/provider/RAX"},
            {"publisher": "NHS England", "title": "Operating framework 2024-25 + provider planning guidance", "url": "https://www.england.nhs.uk/publication/2024-25-priorities-and-operational-planning-guidance/"}
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Establishment costs — Imperial College Healthcare NHS Trust", "Frontline Digitisation programme"]
    },
    "PFI / LIFT charges — Liverpool University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Liverpool University Hospitals NHS Foundation Trust"}],
        "description": "LUHFT's £9.42M PFI / LIFT charges line is shaped not by a conventional PFI hospital but by the legacy of the Carillion 2018 collapse — the original Royal Liverpool University Hospital PFI (with Carillion as constructor and FM contractor) was abandoned, with the new hospital ultimately completed by Laing O'Rourke and opening Oct 2022 outside the original PFI vehicle. The line covers residual LIFT/community-clinic service-concession arrangements across the Cheshire & Merseyside footprint plus tail of legacy PFI/IFRIC 12 obligations on smaller estate components.",
        "beneficiaries": "c. 13,500 WTE staff serving a registered c. 1.5M Cheshire & Merseyside catchment; c. 250,000 ED attendances/yr across Royal Liverpool + Aintree EDs; c. 130,000 elective + day-case admissions/yr; PFI/LIFT-line covers community-clinic LIFT estate + minor service-concession components.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition) · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£9.42M"},
            {"label": "Carillion 2018 effect", "value": "Original Royal Liverpool PFI abandoned post-Carillion Jan 2018 collapse; rescue completion by Laing O'Rourke outside original PFI vehicle — atypical for an Acute trust this scale"},
            {"label": "New Royal Liverpool", "value": "Opened Oct 2022 — capital asset on trust balance sheet (not via PFI SPV); main Premises & Infrastructure depreciation rather than PFI line"},
            {"label": "LIFT residual scope", "value": "Community-clinic LIFT estate across Cheshire & Merseyside footprint; smaller service-concession components"},
            {"label": "IFRIC 12 + IFRS 16 treatment", "value": "Residual service-concession assets on-balance-sheet under IFRIC 12; lease element re-evaluated under IFRS 16 ch.7 GAM 2022 transition"},
            {"label": "RPI / CPI indexation", "value": "Annual indexation per concession terms — drives modest year-on-year line movement"},
            {"label": "NAO Carillion review", "value": "NAO 2020 Investigation into the rescue of Carillion's PFI hospital contracts — Royal Liverpool one of two hospitals (with Midland Met) requiring rescue"},
            {"label": "Funding trajectory", "value": "2021-22 c. £7M → 2024-25 £9.42M — modest growth on residual concession indexation; minor LIFT additions"},
            {"label": "Delivery body + policy owner", "value": "Trust Estates + LIFT vehicles + service-concession SPVs; DHSC + HM Treasury PFI guidance + NHSE Provider Finance + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "NAO Carillion rescue 2020; NAO Managing PFI assets and services as contracts end 2020; Trust ARA disclosure"},
            {"label": "Cf. peer trusts", "value": "Unlike Sherwood Forest or Worcestershire, LUHFT has no major hospital-PFI unitary charge — reflects the Carillion abandonment outcome"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Carillion-collapse 2018 PFI baseline assumption · Successor: post-2022 New Royal in trust ownership; LIFT-only residual concession line forward"}
        ],
        "notes": "LUHFT's PFI/LIFT charges line is unusual for a major acute teaching trust — the Carillion 2018 collapse abandoned the original Royal Liverpool PFI, and Laing O'Rourke's rescue completion delivered the new hospital outside any PFI vehicle, putting the asset on the trust balance sheet rather than under a unitary-charge concession. The residual line therefore covers community-clinic LIFT estate and minor service-concession components across the Cheshire & Merseyside footprint, with IFRIC 12 plus IFRS 16 ch.7 treatment per DHSC GAM 2024-25. NAO's 2020 'Investigation into the rescue of Carillion's PFI hospital contracts' (HC 1056) documented the rescue path. Year-on-year movement is dominated by RPI/CPI indexation on residual concessions.",
        "sources": [
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.liverpoolft.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts (HC 1056, 2020)", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LUHFT provider profile (REM)", "url": "https://www.cqc.org.uk/provider/REM"}
        ],
        "related": ["Liverpool University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Royal United Hospitals Bath NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Royal United Hospitals Bath NHS Foundation Trust"}],
        "description": "RUH Bath's £9.40M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the Royal United Hospital site (Combe Park, Bath) and integrated outpatient + community footprint. The trust's elevated baseline reflects the Dyson Cancer Centre opening (Apr 2024), the Sulis Hospital Bath subsidiary (acquired Jan 2021 from Circle), and an ageing 1930s-era estate with substantial RAAC remediation programme — all driving operational consumable churn alongside redevelopment patching.",
        "beneficiaries": "c. 5,500 WTE staff serving c. 500,000 BaNES, Wiltshire, north Somerset and west Wiltshire residents; c. 95,000 ED attendances/yr at RUH Bath ED; c. 65,000 elective + day-case admissions/yr (RUH + Sulis Hospital combined).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£9.40M"},
            {"label": "Trust scale", "value": "c. 5,500 WTE across Royal United Hospital + integrated community + Sulis Hospital subsidiary; c. 500,000 catchment"},
            {"label": "Dyson Cancer Centre", "value": "New Dyson Cancer Centre opened Apr 2024 — purpose-built integrated cancer centre; new hotel-services + non-clinical consumable baseline"},
            {"label": "Sulis Hospital subsidiary", "value": "Sulis Hospital Bath acquired Jan 2021 from Circle Health — wholly-owned subsidiary providing elective + insourcing capacity; consolidated into trust supplies baseline"},
            {"label": "RAAC remediation", "value": "RUH has confirmed RAAC presence in parts of estate (HSSIB list); remediation programme drives backlog patching consumables"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Bath, Swindon and Wiltshire ICS regional collaboration + minor local spot-buy"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn + agency backfill consumable use"},
            {"label": "Procurement Act 2023 + Apr 2025 NIC", "value": "New regime live Oct 2024; Apr 2025 employer-NIC step-up feeds forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7M → 2022-23 £8.3M → 2024-25 £9.40M — sustained CPI + Sulis consolidation + Dyson Cancer Centre opening"},
            {"label": "Delivery body + policy owner", "value": "Trust Procurement + Estates + NHS Supply Chain + BSW ICS collaborative; NHSE Provider Finance + DHSC + Bath, Swindon and Wiltshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RD1 2022-2024; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 RUH-only baseline (without Sulis) · Successor: full Sulis + Dyson integration + BSW ICS collaborative procurement scaling"}
        ],
        "notes": "RUH Bath's supplies line reflects three concurrent step-ups — the Apr 2024 Dyson Cancer Centre opening (purpose-built integrated cancer facility added a new hotel-services and non-clinical consumables baseline), the Jan 2021 Sulis Hospital acquisition from Circle (wholly-owned subsidiary consolidating elective insourcing supplies into trust accounts), and an ongoing RAAC remediation programme (RUH on HSSIB confirmed list) driving estate-patching consumables. Industrial action 2023-24 layered cancellation re-stocking churn. BSW ICS collaborative procurement and NHS Supply Chain dominate framework spend; Procurement Act 2023 (live Oct 2024) reshapes architecture; Apr 2025 NIC pass-through is the dominant near-term unit-cost driver.",
        "sources": [
            {"publisher": "Royal United Hospitals Bath NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ruh.nhs.uk/about/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24 + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS estates investigation", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "Royal United Hospitals Bath provider profile (RD1)", "url": "https://www.cqc.org.uk/provider/RD1"}
        ],
        "related": ["Royal United Hospitals Bath NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Sheffield Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Mersey and West Lancashire Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Mersey and West Lancashire Teaching Hospitals NHS Trust"}],
        "description": "MWL's £9.39M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the Whiston, St Helens, Southport, Ormskirk, Newton and community-clinic footprint. The trust formed 1 Jul 2023 via merger of Southport & Ormskirk and St Helens & Knowsley Teaching Hospitals — one of NHSE's flagship 2023 acute reconfigurations — sustaining a heavy first-full-year-merger establishment baseline through 2024-25 driven by corporate-services harmonisation and recruitment churn.",
        "beneficiaries": "c. 9,500 WTE staff across Whiston Hospital + St Helens + Southport + Ormskirk + Newton sites serving c. 600,000 Cheshire & Merseyside + Lancashire residents; c. 230,000 ED attendances/yr (Whiston + Southport EDs combined); c. 110,000 elective + day-case admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£9,392,774"},
            {"label": "Trust scale", "value": "c. 9,500 WTE across 5 sites across two ICSs (C&M + Lancashire and South Cumbria); c. 600,000 catchment"},
            {"label": "2023 merger context", "value": "MWL formed 1 Jul 2023 via Southport & Ormskirk + St Helens & Knowsley merger — flagship NHSE 2023 acute reconfiguration"},
            {"label": "Cross-ICB working", "value": "Footprint spans C&M ICS (Knowsley + St Helens + Halton flow) + Lancashire and South Cumbria ICS (Southport + Ormskirk) — multi-ICB commissioning interfaces"},
            {"label": "Composition", "value": "Telecoms + postage + printing + training + courses + recruitment-advertising + minor IT/software subs + professional fees + agency-recruitment commission"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend layered on merger overhead"},
            {"label": "Frontline Digitisation EPR", "value": "Trust on Cerner / Oracle Health EPR convergence pathway across pre-merger separate instances — training + change-mgmt feed line"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate rise raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2022-23 pre-merger combined c. £7M → 2023-24 first-merged £8.5M → 2024-25 £9.39M — first-full-year merger overhead"},
            {"label": "Delivery body + policy owner", "value": "Trust Finance + HR + IT + Communications + EPR programme office + merger-integration team; NHSE Provider Finance + DHSC + C&M + LSC ICBs"},
            {"label": "Evaluation evidence", "value": "NHSE 2023 acute-reconfiguration business case; CQC inspection R0A 2024; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: separate Southport & Ormskirk + St Helens & Knowsley establishment baselines pre-Jul 2023 · Successor: cross-ICS shared-corporate-services pooling + EPR single-instance convergence"}
        ],
        "notes": "MWL's establishment line carries the cumulative cost of the 1 Jul 2023 Southport & Ormskirk + St Helens & Knowsley merger overhead through its first full operational year — 2024-25 captures peak harmonisation spend on HR, Finance, IT, governance and Cerner/Oracle Health EPR convergence between pre-merger separate instances. The cross-ICS footprint (Cheshire & Merseyside plus Lancashire and South Cumbria) multiplies commissioner-interface professional-fee overhead vs single-ICS peers. Industrial action 2023-24 layered rota-restructuring on merger overhead. Apr 2025 NIC step-up raises forward professional-fee cost; cross-ICS shared-corporate-services pooling and EPR single-instance convergence are the medium-term levers.",
        "sources": [
            {"publisher": "Mersey and West Lancashire Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.merseywestlancs.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mersey and West Lancashire provider profile (R0A)", "url": "https://www.cqc.org.uk/provider/R0A"},
            {"publisher": "NHS England", "title": "Operating framework 2024-25 + provider planning guidance", "url": "https://www.england.nhs.uk/publication/2024-25-priorities-and-operational-planning-guidance/"}
        ],
        "related": ["Mersey and West Lancashire Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Establishment costs — Kingston Hospital NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "General supplies & services — University College London Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "University College London Hospitals NHS Foundation Trust"}],
        "description": "UCLH's £9.34M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the Euston Road campus (UCH, NHNN, EGA, Macmillan, Westmoreland Street) and Grafton Way Building (Proton Beam Therapy + cancer haematology, opened 2021). UCLH is a tertiary academic centre with an outsized national specialist footprint — neurosciences (NHNN), cancer (Macmillan + PBT), nuclear medicine and infection — sustaining a research-grade non-clinical consumables baseline.",
        "beneficiaries": "c. 12,000 WTE staff serving c. 350,000 central-London primary catchment plus national tertiary referrals (NHNN, Macmillan, PBT); c. 130,000 ED attendances/yr at UCH ED; c. 130,000 elective + day-case admissions/yr; PBT national service (c. 750 patients/yr at full operation).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£9,342,847"},
            {"label": "Trust scale", "value": "c. 12,000 WTE across UCH + NHNN + EGA + Macmillan + Grafton Way + Westmoreland Street; tertiary academic centre"},
            {"label": "National specialist services", "value": "NHNN Queen Square (neurosciences) + Macmillan Cancer Centre + Grafton Way PBT + EGA women's + UCLH at Westmoreland Street ENT — national tertiary flows"},
            {"label": "Grafton Way Building", "value": "Opened 2021 — Proton Beam Therapy national service + cancer haematology; new hotel-services + non-clinical consumable baseline post-opening"},
            {"label": "UCL partnership", "value": "UCL Partners academic-health-science centre + NIHR BRC — research-grade procurement gateway segregating commercial-trial consumables"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + NCL ICS regional collaboration + trust-direct + research-procurement gateway"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn + agency backfill consumable use"},
            {"label": "Procurement Act 2023 + Apr 2025 NIC", "value": "New regime live Oct 2024; Apr 2025 employer-NIC step-up feeds forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2020-21 c. £7M (pre-Grafton-stable) → 2022-23 £8.5M (Grafton + cancer cohort recovery) → 2024-25 £9.34M"},
            {"label": "Delivery body + policy owner", "value": "Trust Procurement + Estates + NHS Supply Chain + NCL ICS collaborative + UCL Partners research-procurement gateway; NHSE Provider Finance + DHSC + NCL ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RRV 2022-2024; Trust ARA; NIHR BRC reporting"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2005 separate UCH + NHNN + EGA baselines · Successor: NCL ICS collaborative procurement scaling + research-procurement gateway expansion"}
        ],
        "notes": "UCLH's supplies line reflects national-tertiary-specialist breadth — NHNN Queen Square neurosciences, Macmillan Cancer Centre, Grafton Way PBT and EGA women's services each carry distinct hotel-services profiles, with the Grafton Way Building opening in 2021 adding a new baseline for the PBT national service and cancer haematology. The UCL Partners AHSC and NIHR BRC drive a research-procurement gateway. Industrial action 2023-24 layered cancellation re-stocking churn through oncology and neurosciences floors. NCL ICS collaborative procurement and NHS Supply Chain dominate framework spend; Procurement Act 2023 (Oct 2024) reshapes architecture; Apr 2025 NIC pass-through feeds forward unit-cost.",
        "sources": [
            {"publisher": "University College London Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uclh.nhs.uk/about-us/publications"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24 + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UCLH provider profile (RRV)", "url": "https://www.cqc.org.uk/provider/RRV"},
            {"publisher": "National Institute for Health and Care Research", "title": "UCLH Biomedical Research Centre", "url": "https://www.uclhospitals.brc.nihr.ac.uk/"}
        ],
        "related": ["University College London Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Oxford University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Royal Berkshire NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Royal Berkshire NHS Foundation Trust"}],
        "description": "Royal Berkshire's £9.33M amortisation line is the systematic write-down of intangible assets — predominantly capitalised Electronic Patient Record software (Epic implementation), other clinical and corporate software, software development costs and intellectual-property licences — under IAS 38 + DHSC GAM ch.5. The line carries a step-up reflecting the trust's Epic EPR programme (joint Apollo implementation with Kingston, Royal Surrey and Ashford & St Peter's), one of the larger Frontline Digitisation funded EPR rollouts going through capitalisation-then-amortisation cycle.",
        "beneficiaries": "c. 5,500 WTE staff serving c. 600,000 west-Berkshire residents (Reading, Wokingham, West Berkshire, parts of South Oxfordshire) at the single-site Royal Berkshire Hospital (London Road, Reading); c. 130,000 ED attendances/yr at RBH ED; c. 65,000 elective + day-case admissions/yr.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 (Property, Plant and Equipment + Intangibles) · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation programme funding terms",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£9.33M"},
            {"label": "Trust scale", "value": "Single-site DGH (Royal Berkshire Hospital, Reading); c. 5,500 WTE; c. 600,000 catchment"},
            {"label": "Apollo Epic EPR", "value": "Joint Epic implementation with Kingston + Royal Surrey + Ashford & St Peter's — capitalised intangible drives sustained amortisation cycle"},
            {"label": "Frontline Digitisation funding", "value": "NHSE Frontline Digitisation programme co-funded EPR capitalisation; cycle drives 5-10 year amortisation post go-live"},
            {"label": "Composition", "value": "EPR software + clinical-system licences + corporate-system software + capitalised software-development costs + IP licences"},
            {"label": "IAS 38 treatment", "value": "Intangible assets amortised on straight-line basis over useful economic life (typically 5-10 years for software)"},
            {"label": "DHSC GAM ch.5", "value": "Per chapter 5 — intangible assets recognised at cost less accumulated amortisation + impairment; useful-life assessment annual"},
            {"label": "NHP cohort context", "value": "Royal Berkshire in original NHP cohort — Reading rebuild rephased at Jan 2025 NHP Reset; wider capital sequencing affects asset-mix amortisation profile"},
            {"label": "Funding trajectory", "value": "2020-21 c. £6M → 2022-23 £8M (Apollo EPR capitalisation) → 2024-25 £9.33M — steady-state amortisation post Apollo go-live"},
            {"label": "Delivery body + policy owner", "value": "Trust Finance + IT + EPR programme office + Epic UK; NHSE Frontline Digitisation + DHSC + Buckinghamshire, Oxfordshire and Berkshire West ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; CQC inspection RHW 2022-2024; Trust ARA disclosure of intangibles note"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Apollo Cerner Millennium amortisation tail · Successor: post-Apollo Epic single-instance amortisation full-cycle + NHP-Reset Reading rebuild capital implications"}
        ],
        "notes": "Royal Berkshire's amortisation line is dominated by the capitalised intangible of the Apollo Epic EPR programme — a joint implementation with Kingston, Royal Surrey and Ashford & St Peter's that brought four trusts onto a shared Epic instance, with capitalised software and configuration costs amortised straight-line over useful economic life under IAS 38 + DHSC GAM ch.5. NHSE Frontline Digitisation co-financed capitalisation. The trust's NHP cohort status (Reading rebuild rephased at Jan 2025 NHP Reset) shapes the medium-term capital-asset profile — when the new hospital is built, PP&E depreciation will dwarf intangibles amortisation, but for now the line remains EPR-dominated.",
        "sources": [
            {"publisher": "Royal Berkshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalberkshire.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Property, Plant and Equipment + Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme + Jan 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-review"},
            {"publisher": "Care Quality Commission", "title": "Royal Berkshire NHS FT provider profile (RHW)", "url": "https://www.cqc.org.uk/provider/RHW"}
        ],
        "related": ["Royal Berkshire NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation programme", "New Hospital Programme", "Establishment costs — Kingston Hospital NHS Foundation Trust"]
    },
    "Establishment costs — West Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "West Suffolk NHS Foundation Trust"}],
        "description": "West Suffolk's £9.22M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the West Suffolk Hospital (Bury St Edmunds) site and integrated community footprint. The baseline is shaped by NHP cohort status — West Suffolk Hospital is full RAAC construction where Jan 2025 NHP Reset reaffirmed rebuild necessity, sustaining heavy programme-office, professional-fee and business-case spend.",
        "beneficiaries": "c. 4,500 WTE staff serving c. 280,000 west-Suffolk residents (Bury St Edmunds, Newmarket, Sudbury, Stowmarket, Thetford); c. 90,000 ED attendances/yr at West Suffolk ED; c. 50,000 elective + day-case admissions/yr; integrated community-services footprint.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£9.22M"},
            {"label": "Trust scale", "value": "c. 4,500 WTE across West Suffolk Hospital + integrated community services; c. 280,000 catchment"},
            {"label": "RAAC + NHP context", "value": "West Suffolk Hospital in HSSIB Sep 2023 RAAC list — full RAAC-construction main hospital; NHP cohort priority rebuild reaffirmed at Jan 2025 NHP Reset"},
            {"label": "RAAC programme overhead", "value": "Sustained programme-office + structural-engineering professional-fee + monitoring-survey spend feeds establishment line ahead of decant + rebuild"},
            {"label": "Composition", "value": "Telecoms + postage + printing + training + courses + recruitment-advertising + minor IT/software subs + professional fees + agency-recruitment commission"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR + ICS group", "value": "Cerner / Oracle Health EPR (joint with East Suffolk and North Essex) — training + change-mgmt feed line; SNEE ICS shared corporate-services exploration"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate rise raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £6.5M → 2022-23 £8M (RAAC programme step-up) → 2024-25 £9.22M — sustained NHP + RAAC monitoring overhead"},
            {"label": "Delivery body + policy owner", "value": "Trust Finance + HR + IT + Communications + EPR programme office + RAAC + NHP team; NHSE Provider Finance + DHSC + SNEE ICB + NHSE NHP team"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC investigation; NAO Aug 2024 Resilience of the NHS hospital estate; CQC inspection RGR 2022-2024; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC-programme 2020 baseline · Successor: post-NHP rebuild + SNEE ICS shared-corporate-services pooling"}
        ],
        "notes": "West Suffolk's establishment line carries the disproportionate overhead of its NHP cohort RAAC-rebuild status — the main West Suffolk Hospital is full RAAC construction (per HSSIB Sep 2023 list) and was reaffirmed at Jan 2025 NHP Reset as a priority rebuild, sustaining structural-engineering professional fees, monitoring-survey spend, business-case development and decant-planning programme-office cost above peer DGH baselines. Industrial action 2023-24 layered rota-restructuring on the RAAC overhead. Cerner/Oracle Health EPR shared with East Suffolk and North Essex sustains training spend; SNEE ICS shared-corporate-services exploration is the medium-term lever. NAO's Aug 2024 'Resilience of the NHS hospital estate' (HC 145) cited West Suffolk as among priority RAAC-rebuild cases.",
        "sources": [
            {"publisher": "West Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wsh.nhs.uk/About-us/Trust-publications/Annual-reports.aspx"},
            {"publisher": "National Audit Office", "title": "Resilience of the NHS hospital estate (HC 145, Aug 2024)", "url": "https://www.nao.org.uk/reports/resilience-of-the-nhs-hospital-estate/"},
            {"publisher": "NHS England", "title": "New Hospital Programme + Jan 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-review"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "West Suffolk NHS FT provider profile (RGR)", "url": "https://www.cqc.org.uk/provider/RGR"}
        ],
        "related": ["West Suffolk NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Establishment costs — Mersey and West Lancashire Teaching Hospitals NHS Trust", "Department of Health and Social Care"]
    },
}
