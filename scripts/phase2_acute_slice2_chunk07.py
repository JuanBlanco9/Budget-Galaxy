# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 07 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Establishment costs — Blackpool Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Blackpool Teaching Hospitals NHS Foundation Trust"}],
        "description": "Blackpool Teaching Hospitals' £11.73M establishment costs line covers the GAM operating-expense bucket of office consumables, postage, telephony, training, professional fees, software subscriptions and IT-related running costs across Victoria Hospital Blackpool plus Clifton, Fleetwood and the trust's integrated community-services footprint. As host of the regional Lancashire Cardiac Centre — and serving one of England's most-deprived coastal catchments — the establishment baseline carries elevated training, regulatory and software-subscription weight.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 330,000 Fylde Coast catchment plus tertiary cardiac referrals (Lancashire and South Cumbria ICS); c. 130,000 ED attendances/yr at Victoria Hospital Blackpool ED; c. 60,000 admissions/yr; integrated community-services workforce across Blackpool, Fylde and Wyre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£11.73M"},
            {"label": "Trust scale", "value": "Victoria Hospital Blackpool main acute site + Clifton + Fleetwood + integrated community services; c. 7,500 WTE"},
            {"label": "Catchment deprivation", "value": "Fylde Coast — Blackpool wards rank among England's most deprived (IMD 2019); drives training + safeguarding subscription weight"},
            {"label": "Tertiary cardiac centre", "value": "Lancashire Cardiac Centre (host of regional cardiac surgery + interventional cardiology) — drives professional-society subscriptions + medical training spend"},
            {"label": "Composition", "value": "Office supplies + postage + telephony + IT subscriptions + training + statutory professional fees + recruitment + audit fees"},
            {"label": "Frontline Digitisation EPR", "value": "EPR rollout drives elevated training + change-management establishment weight in implementation cycle"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove extra communication, locum onboarding + recruitment spend through establishment"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + service-CPI feed forward unit-cost pressure on professional fees + subscriptions"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M → 2023-24 £10.5M → 2024-25 £11.73M — sustained CPI + EPR cycle"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT + HR functions + NHS Supply Chain (DHSC ALB) + Lancashire & South Cumbria ICS collaboratives"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RXL; NAO Frontline Digitisation review 2024; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate Blackpool Fylde and Wyre Hospitals NHS Trust + community-services PCT baselines · Successor: post-EPR-stabilisation reduced training cycle + ICS-shared-back-office consolidation"}
        ],
        "notes": "Blackpool Teaching Hospitals' establishment baseline is shaped by the trust's hosting of the regional Lancashire Cardiac Centre and its integrated community-services footprint across one of England's most-deprived coastal catchments — both lifting training, safeguarding, professional-society and software-subscription weight above peer DGHs. Industrial action across 2023-24 elevated locum-onboarding and recruitment spend booked through establishment. Frontline Digitisation EPR work drives implementation-cycle training and change-management cost. The April 2025 employer-NIC step-up and sustained service-CPI feed forward unit-cost pressure on professional fees and subscriptions; Lancashire and South Cumbria ICS shared-back-office plans are the medium-term consolidation lever.",
        "sources": [
            {"publisher": "Blackpool Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bfwh.nhs.uk/about-the-trust/publications/annual-reports-and-accounts/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Blackpool Teaching Hospitals provider profile (RXL)", "url": "https://www.cqc.org.uk/provider/RXL"},
            {"publisher": "National Audit Office", "title": "Progress on Frontline Digitisation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["Blackpool Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "General supplies & services — Blackpool Teaching Hospitals NHS Foundation Trust", "Frontline Digitisation Programme", "Department of Health and Social Care"]
    },
    "Amortisation — Northern Care Alliance NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Northern Care Alliance NHS Foundation Trust"}],
        "description": "Northern Care Alliance's £11.70M amortisation line covers IAS 38 intangible-asset amortisation across capitalised software licences, EPR (electronic patient record) implementation costs and SaaS capitalised customisations under the trust's group-model footprint of Salford Royal, Royal Oldham, Fairfield General and Rochdale Infirmary. The Allscripts Sunrise EPR exemplar legacy at Salford Royal — historically one of NHSE's deemed digital exemplars — plus group-wide convergence work drive a multi-year capitalised intangible amortisation cycle aligned with NHSE Frontline Digitisation funding.",
        "beneficiaries": "c. 21,000 WTE staff serving a c. 1.0M Greater Manchester catchment (Salford, Oldham, Bury, Rochdale); c. 350,000 ED attendances/yr across Salford Royal + Royal Oldham + Fairfield + Rochdale UTC; c. 200,000 admissions/yr; Salford Royal hosts regional neurosciences + major-trauma functions.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · IAS 36 (impairment trigger interaction)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£11.70M"},
            {"label": "Trust scale", "value": "Group-model integrated care organisation: Salford Royal + Royal Oldham + Fairfield General + Rochdale Infirmary; c. 21,000 WTE"},
            {"label": "EPR estate", "value": "Allscripts Sunrise EPR (Salford Royal legacy global digital exemplar) + group-wide convergence + corporate-system capitalised licences"},
            {"label": "Frontline Digitisation funding", "value": "NHSE FD Programme funded EPR convergence + uplift work — capitalised under IAS 38, amortised over useful life (typically 5-10 yrs for software)"},
            {"label": "Composition", "value": "Capitalised software licences + EPR implementation + capitalised SaaS configuration costs (post-IFRIC IFRS Interpretation Committee 2021 clarification)"},
            {"label": "Useful-life policy", "value": "Software typically 3-5 yrs; EPR major implementations 5-10 yrs per trust accounting policy disclosed in ARA"},
            {"label": "April 2024 group reformation", "value": "NCA originally formed 2021 (acquisition of Pennine Acute by Salford Royal Group); ongoing intangible asset alignment across legacy heritage trust ledgers"},
            {"label": "NAO Frontline Digitisation review 2024", "value": "NAO 2024 report on FD programme progress notes capitalisation-cycle effects on trust amortisation lines"},
            {"label": "Funding trajectory", "value": "2021-22 c. £8M (post-NCA-formation baseline) → 2023-24 c. £11M → 2024-25 £11.70M — sustained EPR + corporate SaaS capitalisation cycle"},
            {"label": "Delivery body", "value": "Trust Digital + Finance functions + Allscripts (Altera Digital Health) + NHSE Frontline Digitisation team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation review 2024; Trust ARA 2023-24 intangible-asset note; Model Hospital digital benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate Salford Royal NHS FT + Pennine Acute Hospitals NHS Trust intangibles · Successor: full NCA group-wide EPR convergence + post-FD-stabilisation amortisation tail"}
        ],
        "notes": "Northern Care Alliance's amortisation profile is structurally elevated by the trust's heritage of the Salford Royal Allscripts Sunrise EPR — historically one of NHSE's deemed digital exemplars — and the post-2021 group convergence programme bringing legacy Pennine Acute systems under common architecture. NHSE Frontline Digitisation funding has driven a sustained capitalised-intangible amortisation cycle, with EPR major-implementation useful lives typically 5-10 yrs producing a long tail. The IFRS Interpretations Committee's 2021 SaaS configuration clarification reshaped what trusts can capitalise vs expense. Greater Manchester ICS digital convergence work is the medium-term lever, alongside the post-2024 NHSE Frontline Digitisation pivot to convergence rather than first-deployment funding.",
        "sources": [
            {"publisher": "Northern Care Alliance NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northerncarealliance.nhs.uk/about-us/annual-reports-and-accounts"},
            {"publisher": "National Audit Office", "title": "Progress on Frontline Digitisation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Northern Care Alliance provider profile (R0A)", "url": "https://www.cqc.org.uk/provider/R0A"}
        ],
        "related": ["Northern Care Alliance NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Establishment costs — Northern Care Alliance NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — United Lincolnshire Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "United Lincolnshire Hospitals NHS Trust"}],
        "description": "United Lincolnshire Hospitals' £11.55M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials and minor expensed equipment across Lincoln County Hospital, Pilgrim Hospital Boston, Grantham & District Hospital and County Hospital Louth — a large, geographically dispersed multi-site footprint serving rural Lincolnshire. The trust has been in long-term Recovery Support Programme oversight, and is in active group-arrangement discussions with Northern Lincolnshire & Goole NHS FT under a single shared CEO since 2021.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 770,000 Lincolnshire catchment (one of the largest geographically of any English acute trust); c. 220,000 ED attendances/yr (Lincoln + Pilgrim Boston + Grantham); c. 100,000 admissions/yr; multi-site DGH footprint with rural patient-flow logistics.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£11.55M"},
            {"label": "Trust scale", "value": "Four-site DGH (Lincoln + Pilgrim Boston + Grantham + Louth); c. 8,500 WTE — geographically dispersed across Lincolnshire"},
            {"label": "ED throughput", "value": "c. 220,000 attendances/yr across Lincoln + Pilgrim Boston + Grantham"},
            {"label": "Recovery Support Programme", "value": "Trust in NHSE RSP oversight (segment 4) — finance + quality challenges; intensive support since 2017"},
            {"label": "Group arrangement with NLAG", "value": "Shared CEO with Northern Lincolnshire & Goole NHS FT since 2021; group-model collaboration shaping medium-term procurement consolidation"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Lincolnshire ICS + cross-trust collaboration with NLAG"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill churn at Lincoln + Pilgrim"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M → 2023-24 £10.5M → 2024-25 £11.55M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + Lincolnshire ICS procurement collaborative + NLAG joint working"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lincolnshire ICB + NHSE RSP team"},
            {"label": "Evaluation evidence", "value": "NHSE RSP segmentation reviews; CQC inspection RWD; Model Hospital benchmarks; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2000 separate Lincoln + Boston + Grantham + Louth NHS Trust baselines · Successor: ULHT/NLAG group consolidation + Lincolnshire ICS shared procurement"}
        ],
        "notes": "United Lincolnshire's procurement profile is shaped by the trust's exceptional geographical footprint — covering one of England's largest county catchments with a four-site DGH model that sustains higher distribution and rural-logistics costs than peer compact-footprint trusts. The trust has been in NHSE Recovery Support Programme oversight since 2017 (segment 4), driving intensive financial scrutiny. The 2021 shared-CEO arrangement with Northern Lincolnshire & Goole NHS FT shapes medium-term procurement consolidation under Lincolnshire ICS. Industrial action 2023-24 elevated cancellation re-stocking and agency backfill churn. The April 2025 employer-NIC step-up and sustained non-clinical CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "United Lincolnshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ulh.nhs.uk/about/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "NHS System Oversight Framework segmentation", "url": "https://www.england.nhs.uk/publication/nhs-system-oversight-framework/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "United Lincolnshire Hospitals provider profile (RWD)", "url": "https://www.cqc.org.uk/provider/RWD"}
        ],
        "related": ["United Lincolnshire Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Northern Lincolnshire and Goole NHS Foundation Trust", "NHS Supply Chain", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — London North West University Healthcare NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "London North West University Healthcare NHS Trust"}],
        "description": "London North West's £11.52M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's three-site footprint — Northwick Park (Harrow), Central Middlesex (Park Royal) and Ealing. Inter-site transfers between Northwick Park's tertiary services, Central Middlesex's UCC + elective hub and Ealing's emergency + maternity-step-down flow drive PTS demand, with London Ambulance Service and accredited NEPTS contractors as primary carriers. Community-team mileage across Brent, Harrow and Ealing also flows through this line.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 1.0M north-west London catchment (Brent, Harrow, Ealing); c. 250,000 ED attendances/yr (Northwick Park + Ealing EDs); c. 120,000 admissions/yr; integrated community workforce across the three boroughs.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£11.52M"},
            {"label": "Trust scale", "value": "Three-site acute (Northwick Park + Central Middlesex + Ealing) + integrated community services; c. 9,000 WTE"},
            {"label": "Inter-site transfer pattern", "value": "Northwick Park tertiary services + Central Middlesex elective + UCC + Ealing emergency drive substantial inter-site PTS"},
            {"label": "PTS provider mix", "value": "London Ambulance Service NHS Trust + accredited NEPTS contractors — re-tendered via NWL ICS"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for community + AHP teams"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Ealing maternity closure 2015 legacy", "value": "Post-2015 Ealing maternity closure baked-in transfer flow to Northwick Park labour ward — sustained PTS pattern"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M → 2023-24 £10.5M → 2024-25 £11.52M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + LAS PTS + accredited NEPTS contractors + community-team fleet"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + North West London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC inspection R1K; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 separate North West London Hospitals + Ealing Hospital NHS Trust transport baselines · Successor: NWL ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "London North West's transport line is structurally elevated by the legacy of the 2014 merger — between North West London Hospitals (Northwick Park + Central Middlesex) and Ealing Hospital NHS Trust — plus the post-2015 Ealing maternity closure that baked-in sustained inter-site transfer demand to Northwick Park's labour ward and Central Middlesex's elective hub. Industrial action 2023-24 added ad-hoc transfer demand and locum mileage. The April 2025 NIC step-up affects PTS-contractor pass-through; CPI fuel pressure remains a dominant driver. NWL ICS shared-fleet pooling and EV transition are the medium-term levers, alongside Shaping a Healthier Future legacy-driven flow patterns.",
        "sources": [
            {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lnwh.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "London North West University Healthcare provider profile (R1K)", "url": "https://www.cqc.org.uk/provider/R1K"}
        ],
        "related": ["London North West University Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "London Ambulance Service NHS Trust", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — The Newcastle Upon Tyne Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust"}],
        "description": "Newcastle Hospitals' £11.46M PFI charge reflects the unitary-charge pass-through on the Newcastle Hospitals PFI scheme — originally underpinning major redevelopment at the Royal Victoria Infirmary and Freeman Hospital sites. The contract structure covers debt service, lifecycle hard-FM and indexed soft-FM components, with the trust managing one of the North East's flagship academic acute footprints. The line operates within the trust's broader estate including the new Northern Centre for Cancer Care and tertiary services baseline.",
        "beneficiaries": "c. 16,000 WTE staff serving a c. 800,000 Newcastle and Gateshead catchment plus tertiary referrals across the North East and North Cumbria ICS (population c. 3.1M); c. 280,000 ED attendances/yr (RVI + Freeman); c. 200,000 admissions/yr; major teaching trust with national specialty centres (transplantation, cardiothoracic, neurosciences).",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition for service-concession components) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£11.46M"},
            {"label": "PFI vehicle", "value": "Newcastle Hospitals PFI scheme — debt service + lifecycle + soft-FM unitary-charge pass-through"},
            {"label": "Estate covered", "value": "Royal Victoria Infirmary (RVI) + Freeman Hospital — flagship North East academic acute estate"},
            {"label": "Trust scale", "value": "c. 16,000 WTE; one of England's largest teaching trusts; national specialty centres"},
            {"label": "Tertiary specialty mix", "value": "Solid-organ transplantation + cardiothoracic + neurosciences + paediatric tertiary services drive complex-estate baseline"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM (cleaning, catering, portering)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed FM components per concession agreement"},
            {"label": "IFRS 16 2022 transition", "value": "GAM ch.7 reshaped the headline split between service-concession + lease components; line represents accounted PFI/LIFT element"},
            {"label": "Funding trajectory", "value": "Mature PFI; line tracks RPI on indexed components vs declining debt-service balance"},
            {"label": "Delivery body", "value": "Trust SPV concession partners + hard-FM contractor + soft-FM subcontractors + trust E&F oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + NHSE Provider Finance + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back 2020 reports; Trust ARA disclosure; CQC inspection RTD"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI legacy RVI + Freeman estate · Successor: contract expiry hand-back to public-sector + post-PFI estate ownership transition"}
        ],
        "notes": "Newcastle Hospitals' PFI charge sits within the trust's flagship North East academic acute footprint covering the Royal Victoria Infirmary and Freeman Hospital — Freeman host of UK national solid-organ transplantation and cardiothoracic services. The IFRS 16 2022 transition under DHSC GAM ch.7 reshaped how the trust splits service-concession debt-service components from lease components, reducing the headline PFI/LIFT line below the gross unitary charge. RPI indexation continues to lift soft-FM components even as debt-service balance amortises down. The IPA/HMT PFI Hand-Back unit's NAO-recommended cross-government engagement is shaping trust hand-back governance for the medium-term contract expiry path.",
        "sources": [
            {"publisher": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.newcastle-hospitals.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Infrastructure and Projects Authority", "title": "PFI Hand-Back Resource Centre", "url": "https://www.gov.uk/government/collections/pfi-and-pf2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Newcastle Hospitals provider profile (RTD)", "url": "https://www.cqc.org.uk/provider/RTD"}
        ],
        "related": ["The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — North Middlesex University Hospital NHS Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — University Hospitals Coventry And Warwickshire NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
        "description": "UHCW's £11.43M establishment costs line covers GAM operating expenses — office consumables, postage, telephony, training, professional fees, software subscriptions and IT-running costs — across University Hospital Coventry (PFI, opened 2006) and the Hospital of St Cross Rugby. As a major teaching trust hosting the West Midlands Regional Genetics Service, regional cancer centre and a clinical-research-active footprint with the University of Warwick, the establishment baseline carries elevated training, professional-society subscription and research-administration weight.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 1.0M Coventry & Warwickshire catchment plus tertiary referrals from the West Midlands; c. 200,000 ED attendances/yr at UHC ED; c. 100,000 admissions/yr; major teaching + research-active trust hosting West Midlands Regional Genetics Service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£11.43M"},
            {"label": "Trust scale", "value": "University Hospital Coventry (PFI) + Hospital of St Cross Rugby; c. 9,500 WTE"},
            {"label": "Teaching + research weight", "value": "Major teaching trust + University of Warwick partnership; West Midlands Regional Genetics Service host — drives professional-society subscription + research-admin weight"},
            {"label": "Composition", "value": "Office supplies + postage + telephony + IT subscriptions + training + statutory professional fees + recruitment + audit fees"},
            {"label": "PFI estate context", "value": "UHC opened 2006 under PFI — establishment line interacts with PFI hard-FM helpdesk + soft-FM-driven recharges"},
            {"label": "Frontline Digitisation EPR", "value": "EPR rollout (Cerner Millennium long-standing legacy) drives elevated training + change-management establishment weight"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove extra communication + locum onboarding + recruitment spend"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + service-CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M → 2023-24 £10.5M → 2024-25 £11.43M — sustained CPI + EPR cycle"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT + HR functions + NHS Supply Chain (DHSC ALB) + Coventry & Warwickshire ICS collaboratives"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Coventry and Warwickshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RKB; NAO Frontline Digitisation review 2024; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 separate Coventry + Warwickshire NHS Trust + Walsgrave Hospitals NHS Trust establishment baselines · Successor: ICS-shared-back-office consolidation + post-EPR-stabilisation reduced training cycle"}
        ],
        "notes": "UHCW's establishment baseline reflects its role as a major teaching, research-active and tertiary-referral acute trust hosting the West Midlands Regional Genetics Service and the regional cancer centre, alongside the University of Warwick partnership — all lifting professional-society subscription, training and research-administration weight above peer DGHs. The UHC PFI estate (opened 2006) introduces helpdesk and soft-FM recharge interactions through establishment. Industrial action 2023-24 elevated locum-onboarding and recruitment spend booked through this line. April 2025 employer-NIC step-up and sustained service-CPI feed forward unit-cost pressure; Coventry and Warwickshire ICS shared-back-office plans are the medium-term lever.",
        "sources": [
            {"publisher": "University Hospitals Coventry and Warwickshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhcw.nhs.uk/about-us/key-publications/annual-reports-and-financial-accounts/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHCW provider profile (RKB)", "url": "https://www.cqc.org.uk/provider/RKB"},
            {"publisher": "National Audit Office", "title": "Progress on Frontline Digitisation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["University Hospitals Coventry And Warwickshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Establishment costs — Blackpool Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Chesterfield Royal Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Chesterfield Royal Hospital NHS Foundation Trust"}],
        "description": "Chesterfield Royal's £11.42M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials and minor expensed equipment at the single-site DGH serving north Derbyshire. The trust runs Derbyshire Support and Facilities Services (DSFS) as a wholly-owned subsidiary providing hard-FM, soft-FM and procurement services — an early NHS subsidiary company structure pre-dating the 2018 NHSE moratorium on new subsidiary VAT-driven schemes — shaping how non-clinical supplies are procured and recharged.",
        "beneficiaries": "c. 4,200 WTE staff serving a c. 400,000 north Derbyshire catchment (Chesterfield, Bolsover, North East Derbyshire, parts of Derbyshire Dales and High Peak); c. 100,000 ED attendances/yr; c. 40,000 admissions/yr; single-site DGH with regional renal-dialysis service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£11.42M"},
            {"label": "Trust scale", "value": "Single-site DGH (Calow, Chesterfield); c. 4,200 WTE"},
            {"label": "Wholly-owned subsidiary", "value": "Derbyshire Support and Facilities Services Ltd (DSFS) provides hard-FM + soft-FM + procurement — pre-dates 2018 NHSE moratorium"},
            {"label": "Procurement route", "value": "DSFS subsidiary + NHS Supply Chain national framework + Joined Up Care Derbyshire ICS collaborative"},
            {"label": "ED throughput", "value": "c. 100,000 attendances/yr"},
            {"label": "Regional renal-dialysis", "value": "Hosts regional renal services; drives some clinical-adjacent supplies through general supplies & services"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure (incl. DSFS recharge interaction)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M → 2023-24 £10.5M → 2024-25 £11.42M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "DSFS subsidiary + Trust Procurement + NHS Supply Chain (DHSC ALB) + Joined Up Care Derbyshire ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Joined Up Care Derbyshire ICB + HMRC (subsidiary VAT regime context)"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RFS; Trust ARA 2023-24 disclosure of DSFS recharge"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 in-house FM model · Successor: continued DSFS operational + post-2018 NHSE subsidiary moratorium impact on growth"}
        ],
        "notes": "Chesterfield Royal's procurement profile is structurally distinct from peer single-site DGHs because of its wholly-owned subsidiary Derbyshire Support and Facilities Services (DSFS) — established before the 2018 NHSE moratorium on new VAT-driven subsidiary structures. DSFS provides hard-FM, soft-FM and procurement services, with recharge interactions visible through the trust's general supplies & services line. Industrial action 2023-24 elevated cancellation re-stocking and agency backfill churn. The April 2025 employer-NIC step-up and sustained non-clinical CPI feed forward unit-cost pressure, with the NIC affecting DSFS workforce as well as direct trust staff. Joined Up Care Derbyshire ICS collaborative procurement is the medium-term lever.",
        "sources": [
            {"publisher": "Chesterfield Royal Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chesterfieldroyal.nhs.uk/about-us/publications/annual-report-and-accounts"},
            {"publisher": "NHS England", "title": "Wholly-owned subsidiary guidance + 2018 moratorium", "url": "https://www.england.nhs.uk/financial-accounting-and-reporting/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Chesterfield Royal Hospital provider profile (RFS)", "url": "https://www.cqc.org.uk/provider/RFS"}
        ],
        "related": ["Chesterfield Royal Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Bradford Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Northern Care Alliance NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Northern Care Alliance NHS Foundation Trust"}],
        "description": "Northern Care Alliance's £11.42M establishment costs line covers GAM operating expenses — office consumables, telephony, training, professional fees, software subscriptions and IT — across the group-model footprint of Salford Royal, Royal Oldham, Fairfield General and Rochdale Infirmary. The trust's role as host of regional neurosciences and major trauma at Salford Royal, plus the legacy Allscripts Sunrise EPR exemplar status, drives elevated training, clinical-research-administration and software-subscription weight relative to peer DGHs.",
        "beneficiaries": "c. 21,000 WTE staff serving a c. 1.0M Greater Manchester catchment (Salford, Oldham, Bury, Rochdale); c. 350,000 ED attendances/yr; c. 200,000 admissions/yr; Salford Royal hosts regional neurosciences, major trauma, complex spine — drives tertiary training + research weight.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£11.42M"},
            {"label": "Trust scale", "value": "Group-model integrated care organisation: Salford Royal + Royal Oldham + Fairfield General + Rochdale Infirmary; c. 21,000 WTE"},
            {"label": "Tertiary specialty mix", "value": "Salford Royal regional neurosciences + major trauma + complex spine + intestinal-failure — drives training + research-admin weight"},
            {"label": "Composition", "value": "Office supplies + postage + telephony + IT subscriptions + training + statutory professional fees + recruitment + audit fees"},
            {"label": "EPR exemplar legacy", "value": "Salford Royal historic Allscripts Sunrise digital exemplar — sustained training + change-management cycle through group-wide convergence"},
            {"label": "Group reformation 2021", "value": "NCA formed Apr 2021 (acquisition of Pennine Acute by Salford Royal Group); ongoing back-office establishment consolidation"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove extra communication + locum onboarding + recruitment spend"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + service-CPI feed forward unit-cost pressure on professional fees + subscriptions"},
            {"label": "Funding trajectory", "value": "2021-22 c. £8M (post-NCA-formation baseline) → 2023-24 c. £10.5M → 2024-25 £11.42M"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT + HR functions + NHS Supply Chain + Greater Manchester ICS collaboratives"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greater Manchester ICB + NHSE Frontline Digitisation"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection R0A; NAO Frontline Digitisation review 2024; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate Salford Royal NHS FT + Pennine Acute Hospitals NHS Trust establishment baselines · Successor: full NCA group-wide back-office consolidation + GM ICS shared services"}
        ],
        "notes": "Northern Care Alliance's establishment baseline reflects the post-2021 group-model footprint formed by the acquisition of Pennine Acute Hospitals NHS Trust by Salford Royal Group — with sustained back-office consolidation work shaping training, recruitment and software-subscription spend. Salford Royal's regional neurosciences, major trauma and the historic Allscripts Sunrise digital exemplar status lift research-administration and EPR training weight above peer trusts. Industrial action 2023-24 elevated locum-onboarding and recruitment spend booked through this line. The April 2025 employer-NIC step-up and sustained service-CPI feed forward unit-cost pressure; Greater Manchester ICS shared-back-office plans plus continued group-model convergence are the medium-term levers.",
        "sources": [
            {"publisher": "Northern Care Alliance NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northerncarealliance.nhs.uk/about-us/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Northern Care Alliance provider profile (R0A)", "url": "https://www.cqc.org.uk/provider/R0A"},
            {"publisher": "National Audit Office", "title": "Progress on Frontline Digitisation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["Northern Care Alliance NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Northern Care Alliance NHS Foundation Trust", "Establishment costs — Blackpool Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Whittington Health NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Whittington Health NHS Trust"}],
        "description": "Whittington Health's £11.41M establishment costs line covers GAM operating expenses — office consumables, postage, telephony, training, professional fees, software subscriptions and IT — across the Whittington Hospital acute site (Archway) plus the integrated community-services footprint covering Islington and Haringey. The integrated acute + community model — uncommon among English acute trusts — broadens establishment baseline through community-team training, safeguarding licences and multi-borough professional-fee weight relative to acute-only peers.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 500,000 Islington + Haringey catchment; c. 90,000 ED attendances/yr at Whittington ED; c. 35,000 admissions/yr; community caseload c. 200,000 individuals/yr across district-nursing + community-paediatric + sexual-health.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£11.41M"},
            {"label": "Trust scale", "value": "Single acute site (Whittington, Archway) + Islington + Haringey integrated community services; c. 4,500 WTE"},
            {"label": "Integration model", "value": "Trust formed 2011 by integration of Whittington Hospital with Islington + Haringey PCT community services — early integrated acute + community model"},
            {"label": "Composition", "value": "Office supplies + postage + telephony + IT subscriptions + training + statutory professional fees + recruitment + audit fees + community-team safeguarding subscriptions"},
            {"label": "Catchment deprivation", "value": "Islington + Haringey high IMD deprivation — drives safeguarding subscription + training weight"},
            {"label": "Frontline Digitisation EPR", "value": "EPR rollout drives elevated training + change-management establishment weight in implementation cycle"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove extra communication + locum onboarding + recruitment spend"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + service-CPI feed forward unit-cost pressure on professional fees + subscriptions"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M → 2023-24 £10.5M → 2024-25 £11.41M — sustained CPI + EPR cycle"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT + HR functions + NHS Supply Chain (DHSC ALB) + North Central London ICS collaboratives"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RKE; NAO Frontline Digitisation review 2024; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate Whittington Hospital NHS Trust + PCT community-services baselines · Successor: NCL ICS shared-back-office consolidation + post-EPR-stabilisation training cycle"}
        ],
        "notes": "Whittington Health's establishment baseline is shaped by the trust's 2011-formed integrated acute + community model — one of the early English experiments in vertical integration — broadening baseline through community-team training, safeguarding licences and multi-borough professional-fee weight relative to acute-only peers. Industrial action 2023-24 elevated locum-onboarding and recruitment spend through this line. Frontline Digitisation EPR work drives implementation-cycle training cost. April 2025 employer-NIC step-up and sustained service-CPI feed forward unit-cost pressure; NCL ICS shared-back-office plans (alongside Royal Free Group, UCLH and Royal Free + North Mid merger) are the medium-term lever.",
        "sources": [
            {"publisher": "Whittington Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whittington.nhs.uk/default.asp?c=21091"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Whittington Health provider profile (RKE)", "url": "https://www.cqc.org.uk/provider/RKE"},
            {"publisher": "National Audit Office", "title": "Progress on Frontline Digitisation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["Whittington Health NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Social security & levy — Whittington Health NHS Trust", "Establishment costs — Blackpool Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Nottingham University Hospitals NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Nottingham University Hospitals NHS Trust"}],
        "description": "NUH's £11.19M establishment costs line covers GAM operating expenses — office consumables, telephony, training, professional fees, software subscriptions and IT — across Queen's Medical Centre and Nottingham City Hospital. As a major teaching trust hosting East Midlands Major Trauma Centre, regional cancer services and a research-active footprint with the University of Nottingham, the establishment baseline carries elevated training, professional-society subscription and research-administration weight — alongside ongoing maternity-services-inquiry-related governance and legal cost.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 800,000 Nottingham and South Nottinghamshire catchment plus tertiary referrals across the East Midlands (population c. 4.8M); c. 320,000 ED attendances/yr at QMC + City; c. 200,000 admissions/yr; major teaching trust hosting East Midlands Major Trauma Centre + regional cancer + neurosciences.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£11.19M"},
            {"label": "Trust scale", "value": "Two-site academic acute (Queen's Medical Centre + Nottingham City Hospital); c. 17,000 WTE; one of England's largest teaching trusts"},
            {"label": "Tertiary specialty mix", "value": "East Midlands Major Trauma Centre + regional cancer + neurosciences + paediatrics — drives training + research-admin weight"},
            {"label": "Composition", "value": "Office supplies + postage + telephony + IT subscriptions + training + statutory professional fees + recruitment + audit fees + governance + legal"},
            {"label": "Maternity services inquiry", "value": "Donna Ockenden-led independent review of NUH maternity services (commissioned 2022, ongoing) — drives elevated governance, legal + family-liaison establishment cost"},
            {"label": "Recovery Support Programme + EPR", "value": "NUH in NHSE RSP oversight from 2022 (segment 4); Frontline Digitisation EPR rollout drives elevated training + change-management weight"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove extra communication + locum onboarding + recruitment spend"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + service-CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M → 2023-24 £10.5M → 2024-25 £11.19M — sustained CPI + EPR cycle + governance cost"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT + HR + Governance + Legal functions + NHS Supply Chain + Nottingham & Nottinghamshire ICS collaboratives"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Nottingham and Nottinghamshire ICB + NHSE RSP team"},
            {"label": "Evaluation evidence", "value": "Donna Ockenden review interim findings; CQC inspection RX1; NHSE RSP segmentation reviews; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 separate QMC University Hospital + Nottingham City Hospital baselines · Successor: post-Ockenden + RSP-exit governance settling + ICS-shared-back-office consolidation"}
        ],
        "notes": "NUH's establishment baseline is shaped by the trust's role as a major teaching, research-active and tertiary-referral acute trust hosting East Midlands Major Trauma Centre and regional cancer services — alongside the ongoing Donna Ockenden-led independent review of NUH maternity services (commissioned 2022) which has driven elevated governance, legal and family-liaison spend booked through establishment. The trust has been in NHSE Recovery Support Programme oversight since 2022, intensifying financial scrutiny. Industrial action 2023-24 elevated locum-onboarding and recruitment spend. The April 2025 employer-NIC step-up and sustained service-CPI feed forward unit-cost pressure; Nottingham and Nottinghamshire ICS shared-back-office plans are the medium-term consolidation lever.",
        "sources": [
            {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nuh.nhs.uk/our-publications"},
            {"publisher": "Donna Ockenden", "title": "Independent review of maternity services at NUH", "url": "https://www.ockendenmaternityreview.org.uk/"},
            {"publisher": "NHS England", "title": "NHS System Oversight Framework segmentation", "url": "https://www.england.nhs.uk/publication/nhs-system-oversight-framework/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NUH provider profile (RX1)", "url": "https://www.cqc.org.uk/provider/RX1"}
        ],
        "related": ["Nottingham University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — University Hospitals Coventry And Warwickshire NHS Trust", "Frontline Digitisation Programme", "Department of Health and Social Care"]
    },
    "General supplies & services — Blackpool Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Blackpool Teaching Hospitals NHS Foundation Trust"}],
        "description": "Blackpool Teaching Hospitals' £11.13M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials and minor expensed equipment across Victoria Hospital Blackpool, Clifton Hospital, Fleetwood Hospital and the trust's integrated community-services footprint across the Fylde Coast. The trust's hosting of the regional Lancashire Cardiac Centre — alongside serving one of England's most-deprived coastal catchments — lifts catering, linen and hotel-services baseline above peer single-county DGHs.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 330,000 Fylde Coast catchment plus tertiary cardiac referrals (Lancashire and South Cumbria ICS); c. 130,000 ED attendances/yr at Victoria Hospital Blackpool ED; c. 60,000 admissions/yr; integrated community-services workforce.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£11.13M"},
            {"label": "Trust scale", "value": "Victoria Hospital Blackpool main acute site + Clifton + Fleetwood + integrated community services; c. 7,500 WTE"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr at Victoria Hospital Blackpool"},
            {"label": "Catchment deprivation", "value": "Fylde Coast — Blackpool wards rank among England's most deprived (IMD 2019)"},
            {"label": "Tertiary cardiac centre", "value": "Lancashire Cardiac Centre regional cardiac surgery + interventional cardiology — drives some clinical-adjacent supplies"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Lancashire & South Cumbria ICS procurement collaborative"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M → 2023-24 £10.5M → 2024-25 £11.13M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + Lancashire & South Cumbria ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RXL; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate Blackpool Fylde and Wyre Hospitals NHS Trust + community-services PCT baselines · Successor: ICS procurement collaborative scaling"}
        ],
        "notes": "Blackpool Teaching Hospitals' general supplies & services baseline reflects the trust's hosting of the regional Lancashire Cardiac Centre and its integrated community-services footprint across one of England's most-deprived coastal catchments — both lifting catering, linen and hotel-services baseline above peer single-county DGHs. NHS Supply Chain remains the dominant procurement route, with Lancashire and South Cumbria ICS procurement collaborative scaling as the medium-term lever. Industrial action 2023-24 elevated cancellation re-stocking and agency backfill churn. The April 2025 employer-NIC step-up and sustained non-clinical CPI feed forward unit-cost pressure on consumable inputs.",
        "sources": [
            {"publisher": "Blackpool Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bfwh.nhs.uk/about-the-trust/publications/annual-reports-and-accounts/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Blackpool Teaching Hospitals provider profile (RXL)", "url": "https://www.cqc.org.uk/provider/RXL"},
            {"publisher": "NHS England", "title": "Lancashire and South Cumbria ICS", "url": "https://www.england.nhs.uk/north-west/"}
        ],
        "related": ["Blackpool Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Establishment costs — Blackpool Teaching Hospitals NHS Foundation Trust", "NHS Supply Chain", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Manchester University NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Manchester University NHS Foundation Trust"}],
        "description": "MFT's £11.12M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's nine-site footprint — MRI, Wythenshawe, RMCH, Saint Mary's, Manchester Royal Eye, Trafford, Withington, North Manchester General Hospital and Altrincham. Inter-site transfers between MRI's tertiary services, Wythenshawe's cardiothoracic transplant centre and RMCH's tertiary paediatrics drive PTS demand, with North West Ambulance Service and accredited NEPTS contractors as primary carriers.",
        "beneficiaries": "c. 28,000 WTE staff serving a c. 1.0M Manchester catchment plus tertiary referrals across the North West (population c. 7M); c. 360,000 ED attendances/yr (MRI + Wythenshawe + RMCH + NMGH); c. 220,000 admissions/yr; one of England's largest acute trusts with national specialty centres (paediatrics, cardiothoracic transplant, ophthalmology).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£11.12M"},
            {"label": "Trust scale", "value": "Nine-site academic acute (MRI + Wythenshawe + RMCH + Saint Mary's + Manchester Royal Eye + Trafford + Withington + NMGH + Altrincham); c. 28,000 WTE — one of England's largest"},
            {"label": "Tertiary referral pattern", "value": "Wythenshawe cardiothoracic transplant + RMCH tertiary paediatrics + Manchester Royal Eye + Saint Mary's tertiary maternity drive substantial inter-site + inter-trust PTS"},
            {"label": "PTS provider mix", "value": "North West Ambulance Service NHS Trust + accredited NEPTS contractors — re-tendered via Greater Manchester ICS"},
            {"label": "NMGH acquisition Apr 2021", "value": "Acquisition of North Manchester General Hospital from Pennine Acute (now NCA legacy) extended footprint + transfer flow patterns"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for AHP + community teams"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M (post-NMGH-acquisition) → 2023-24 £10.5M → 2024-25 £11.12M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + NWAS PTS + accredited NEPTS contractors + community-team fleet"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC inspection R0A; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 separate CMFT + UHSM transport baselines; pre-2021 NMGH-Pennine baseline · Successor: GM ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "MFT's transport line is structurally elevated by the trust's nine-site footprint formed through the 2017 merger of Central Manchester Foundation Trust with University Hospital of South Manchester (Wythenshawe), and the April 2021 acquisition of North Manchester General Hospital from Pennine Acute. Tertiary referral patterns — Wythenshawe cardiothoracic transplant, RMCH tertiary paediatrics, Saint Mary's tertiary maternity, Manchester Royal Eye — generate continuous inter-site and inter-trust PTS demand. Industrial action 2023-24 added ad-hoc transfer demand and locum mileage. April 2025 NIC step-up affects PTS-contractor pass-through; CPI fuel pressure remains a dominant driver. Greater Manchester ICS shared-fleet pooling and EV transition are the medium-term levers.",
        "sources": [
            {"publisher": "Manchester University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://mft.nhs.uk/the-trust/annual-reports/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report 2023-24", "url": "https://www.nwas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "MFT provider profile (R0A — note same as NCA, MFT code: RW3)", "url": "https://www.cqc.org.uk/provider/RW3"}
        ],
        "related": ["Manchester University NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Transport (business + patient) — London North West University Healthcare NHS Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "St George's' £11.05M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's St George's Hospital (Tooting) main site plus Queen Mary's Hospital Roehampton — now operating in group arrangement with Epsom and St Helier University Hospitals as the GESH Group since 2021. As one of London's four Major Trauma Centres and a regional cardiothoracic + neurosciences tertiary centre serving south-west London and Surrey, the trust generates substantial inter-hospital trauma + tertiary transfer demand.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 1.3M south-west London catchment plus tertiary referrals across south-west London and Surrey (population c. 3.5M); c. 200,000 ED attendances/yr at St George's main + Queen Mary's MIU; c. 110,000 admissions/yr; St George's = one of London's four Major Trauma Centres + regional cardiothoracic + neurosciences host.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£11.05M"},
            {"label": "Trust scale", "value": "St George's Hospital (Tooting) main acute + Queen Mary's Hospital Roehampton; c. 9,500 WTE"},
            {"label": "Major Trauma Centre", "value": "St George's = one of London's four MTCs — drives inter-hospital major-trauma transfer demand"},
            {"label": "Tertiary specialty mix", "value": "Regional cardiothoracic + neurosciences + tertiary paediatrics — substantial inter-trust PTS"},
            {"label": "GESH Group + PTS provider mix", "value": "Group arrangement with Epsom and St Helier since 2021 (shared CEO + cross-site flow); PTS via LAS + accredited NEPTS contractors re-tendered through SWL ICS"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £9M → 2023-24 £10.5M → 2024-25 £11.05M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + LAS PTS + accredited NEPTS contractors + (cross-group) GESH joint working"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + South West London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC inspection RJ7; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 St George's Healthcare baselines · Successor: GESH Group shared-fleet pooling + SWL ICS EV transition"}
        ],
        "notes": "St George's' transport line is structurally elevated by the trust's status as one of London's four Major Trauma Centres — and its role as a regional cardiothoracic and neurosciences tertiary centre — both generating continuous inter-hospital transfer demand. The 2021 group arrangement with Epsom and St Helier University Hospitals NHS Trust under the GESH Group adds cross-site clinical flow patterns shaping medium-term PTS planning. Industrial action 2023-24 added ad-hoc transfer demand and locum mileage. April 2025 NIC step-up affects PTS-contractor pass-through; CPI fuel pressure remains a dominant driver. SWL ICS shared-fleet pooling and EV transition are the medium-term levers, alongside continued GESH consolidation.",
        "sources": [
            {"publisher": "St George's University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stgeorges.nhs.uk/about/our-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "St George's University Hospitals provider profile (RJ7)", "url": "https://www.cqc.org.uk/provider/RJ7"}
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Epsom and St Helier University Hospitals NHS Trust", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Manchester University NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Manchester University NHS Foundation Trust"}],
        "description": "MFT's £10.94M lease expenditure line covers IFRS 16 right-of-use asset depreciation and lease-liability interest on the trust's leased portfolio — primarily NHS Property Services (NHSPS) leased community-clinic estate, leased medical equipment under managed-service agreements, and pool-fleet leases. Following the IFRS 16 2022 transition under DHSC GAM ch.7, on-balance-sheet treatment moved most operating leases onto the trust's books, lifting this line above pre-2022 operating-lease rental expense baselines.",
        "beneficiaries": "c. 28,000 WTE staff serving a c. 1.0M Manchester catchment plus tertiary referrals; lease estate covers leased community-clinic spaces (incl. NHSPS), medical-equipment managed-service contracts (radiology + pathology + cardiology) and pool-fleet vehicles supporting community + AHP teams.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IAS 36 (right-of-use impairment trigger interaction)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£10.94M"},
            {"label": "Trust scale", "value": "Nine-site academic acute (post-2017 CMFT-UHSM merger + 2021 NMGH acquisition); c. 28,000 WTE"},
            {"label": "Composition", "value": "Right-of-use depreciation (capitalised lease assets) + lease-liability interest expense"},
            {"label": "IFRS 16 transition (2022)", "value": "DHSC GAM ch.7 brought most operating leases on-balance-sheet; lifted line vs pre-2022 operating-lease rental treatment"},
            {"label": "NHSPS leased estate", "value": "Multiple Manchester community-clinic spaces leased from NHS Property Services — long-running 2018-2024 NHSPS rent dispute context"},
            {"label": "Medical-equipment managed services", "value": "Radiology + pathology + cardiology managed-service agreements with substantial embedded lease-of-equipment elements under IFRS 16"},
            {"label": "Pool fleet", "value": "Leased community + AHP-team pool vehicles; right-of-use depreciation + interest"},
            {"label": "NMGH acquisition", "value": "Apr 2021 acquisition of North Manchester General Hospital from Pennine Acute extended trust lease portfolio"},
            {"label": "Funding trajectory", "value": "2021-22 pre-IFRS-16 operating-lease c. £6M → 2022-23 IFRS 16 transition jump c. £9M → 2024-25 £10.94M — sustained lease-portfolio growth"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + Procurement functions + NHS Property Services + Crown Commercial Service framework + medical-equipment OEM lessors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHS Property Services (DHSC ALB) + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHSPS / Property Services review; HMT Financial Reporting Manual IFRS 16 guidance; Trust ARA 2023-24 IFRS 16 disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 operating-lease rental treatment · Successor: ICS-shared-estate consolidation + NHSPS rent settlement + NHP-Reset deferral effects"}
        ],
        "notes": "MFT's lease expenditure line jumped on the IFRS 16 2022 transition under DHSC GAM ch.7 — which brought most operating leases on-balance-sheet via right-of-use depreciation and lease-liability interest, replacing pre-2022 operating-lease rental treatment. The trust's lease portfolio concentrates in NHS Property Services leased community-clinic estate, embedded equipment-lease elements within radiology, pathology and cardiology managed-service agreements, and pool-fleet leases. The long-running 2018-2024 NHSPS rent dispute shapes ongoing recognition. The April 2021 NMGH acquisition extended the lease portfolio; NHP Reset deferral effects on planned modular leases are a medium-term consideration.",
        "sources": [
            {"publisher": "Manchester University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://mft.nhs.uk/the-trust/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24", "url": "https://www.property.nhs.uk/news-publications/publications/"},
            {"publisher": "HM Treasury", "title": "Financial Reporting Manual (FReM) — IFRS 16 application", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
            {"publisher": "Care Quality Commission", "title": "MFT provider profile (RW3)", "url": "https://www.cqc.org.uk/provider/RW3"}
        ],
        "related": ["Manchester University NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Manchester University NHS Foundation Trust", "NHS Property Services", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — North Middlesex University Hospital NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "North Middlesex University Hospital NHS Trust"}],
        "description": "North Middlesex's £10.85M PFI charge reflects the unitary-charge pass-through on the North Middlesex Hospital PFI redevelopment scheme — signed 2006, principal new-build operational from 2010, with SPV Healthcare Support (North Middlesex) and concession FM partners. The contract covers debt service, lifecycle hard-FM and indexed soft-FM components for the Sterling Way Edmonton site. With the trust now in active group-model transaction with Royal Free London NHS FT under the North Central London ICS, ongoing PFI cost management forms part of the integration business case.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 350,000 Enfield and Haringey catchment with very high IMD deprivation; c. 200,000 ED attendances/yr (one of London's busiest single-site EDs); c. 65,000 admissions/yr; PFI estate covers the Sterling Way Edmonton acute site.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition for service-concession components) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£10.85M"},
            {"label": "PFI vehicle", "value": "North Middlesex Hospital PFI signed 2006, new-build operational 2010; SPV Healthcare Support (North Middlesex) Ltd"},
            {"label": "Estate covered", "value": "North Middlesex University Hospital — Sterling Way Edmonton acute site"},
            {"label": "Royal Free merger context", "value": "Active group-model transaction with Royal Free London NHS FT progressing 2023-25 under NCL ICS — PFI cost management part of integration business case"},
            {"label": "Catchment deprivation", "value": "Enfield + Haringey high IMD deprivation; sustained ED + maternity activity drives variable-charge volume sensitivity"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM (cleaning, catering, portering)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed FM components per concession agreement"},
            {"label": "IFRS 16 2022 transition", "value": "GAM ch.7 reshaped headline split between service-concession + lease components"},
            {"label": "Funding trajectory", "value": "Mature PFI; line tracks RPI uplift on indexed components vs declining debt-service balance"},
            {"label": "Delivery body", "value": "Healthcare Support (North Middlesex) SPV + hard-FM contractor + soft-FM subcontractors + trust E&F oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + NHSE Provider Finance + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back 2020 reports; CQC inspection RAP; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI legacy North Middlesex estate (1960s buildings) · Successor: contract expiry hand-back + (post-merger) Royal Free Group consolidated estate management"}
        ],
        "notes": "North Middlesex's PFI charge sits within the trust's redevelopment programme — delivering the new acute building from 2010 onwards under the 2006-signed Healthcare Support (North Middlesex) concession. With the trust now in active group-model transaction with Royal Free London NHS FT under the NCL ICS, ongoing PFI unitary-charge management forms part of the integration business case alongside workforce and procurement consolidation. The IFRS 16 2022 transition under DHSC GAM ch.7 reshaped the headline split between service-concession debt-service components and lease components. RPI indexation continues to lift soft-FM components even as debt-service balance amortises down; sustained high ED + maternity activity drives variable-charge volume sensitivity.",
        "sources": [
            {"publisher": "North Middlesex University Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northmid.nhs.uk/annual-reports"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North Middlesex provider profile (RAP)", "url": "https://www.cqc.org.uk/provider/RAP"}
        ],
        "related": ["North Middlesex University Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "Royal Free London NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — University Hospitals Birmingham NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals Birmingham NHS Foundation Trust"}],
        "description": "UHB's £10.72M business rates line covers non-domestic rates payable to Birmingham, Solihull and Worcestershire billing authorities on the trust's five-site estate — Queen Elizabeth Hospital Birmingham, Heartlands, Good Hope, Solihull and Birmingham Chest Clinic. As one of England's largest acute trusts hosting liver + renal transplantation and the Royal Centre for Defence Medicine, the rateable-value footprint is exceptionally broad. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 reshapes the multiplier structure for NHS estate.",
        "beneficiaries": "c. 22,000 WTE staff serving a c. 2.2M Birmingham and Solihull catchment plus tertiary referrals across the West Midlands and military RCDM national role; c. 400,000 ED attendances/yr (QE + Heartlands + Good Hope EDs); c. 240,000 admissions/yr; one of England's largest acute trusts.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£10.72M"},
            {"label": "Trust scale", "value": "Five-site academic acute (QEHB + Heartlands + Good Hope + Solihull + Birmingham Chest Clinic); c. 22,000 WTE — one of England's largest"},
            {"label": "Tertiary specialty mix", "value": "Liver + renal transplantation + Royal Centre for Defence Medicine + cancer + neurosciences — drives broad, high-rateable-value estate"},
            {"label": "Billing authorities", "value": "Birmingham City Council + Solihull MBC + (parts) Worcestershire — multi-authority assessment"},
            {"label": "VOA 2023 revaluation", "value": "Valuation Office Agency 2023 revaluation effective Apr 2023 reset rateable values; transitional relief mechanism"},
            {"label": "NDR 2024 Act", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduced new multiplier categories effective Apr 2025"},
            {"label": "Mandatory + discretionary relief", "value": "NHS trusts pay full rates (no charitable relief) — unlike NHS charities; mandatory NHS exemption removed by 1990 reforms"},
            {"label": "Historic context", "value": "Heart of England NHS Foundation Trust + UHB merger 2018 created current rating footprint covering Heartlands + Good Hope + Solihull"},
            {"label": "Funding trajectory", "value": "2021-22 c. £8.5M → 2023-24 c. £10M (post-VOA revaluation) → 2024-25 £10.72M — multiplier + revaluation"},
            {"label": "Delivery body", "value": "Trust Estates + Finance functions + Valuation Office Agency (HMRC) + billing local authorities"},
            {"label": "Policy owner", "value": "MHCLG / DLUHC (NDR policy) + HM Treasury (multiplier setting) + DHSC + NHSE Provider Finance + Birmingham and Solihull ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list; NAO local-government finance reviews; Trust ARA 2023-24 estates note"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate UHB + Heart of England NHS FT rating baselines · Successor: post-Apr 2025 NDR 2024 Act multiplier regime"}
        ],
        "notes": "UHB's business rates line is structurally elevated by the breadth of its estate — five major hospital sites across Birmingham and Solihull following the 2018 merger with Heart of England NHS FT which brought Heartlands, Good Hope and Solihull into a unified rating footprint. Hosting liver + renal transplantation and the Royal Centre for Defence Medicine lifts rateable-value baseline above peer DGHs. The VOA 2023 revaluation reset rateable values effective April 2023; the NDR (Multipliers and Private Finance) Act 2024 introduced new multiplier categories effective April 2025. NHS trusts pay full rates with no mandatory charitable relief — unlike NHS charities — making rate management a material finance lever.",
        "sources": [
            {"publisher": "University Hospitals Birmingham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhb.nhs.uk/about-us/publications.htm"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/14/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHB provider profile (RRK)", "url": "https://www.cqc.org.uk/provider/RRK"}
        ],
        "related": ["University Hospitals Birmingham NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University College London Hospitals NHS Foundation Trust", "Valuation Office Agency", "Department of Health and Social Care"]
    },
    "Business rates — University College London Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "University College London Hospitals NHS Foundation Trust"}],
        "description": "UCLH's £10.43M business rates line covers non-domestic rates payable to Camden and (smaller proportion) Westminster billing authorities on the trust's central-London estate — UCH, the National Hospital for Neurology and Neurosurgery (Queen Square), UCH Macmillan Cancer Centre, RNTNE + Eastman Dental and the Grafton Way Building (Proton Beam Therapy). Central-London rateable values drive a high per-bed baseline; the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 reshapes the multiplier structure.",
        "beneficiaries": "c. 12,000 WTE staff serving a c. 2.0M central-London catchment plus national tertiary referrals (neurosciences, paediatric oncology, proton-beam therapy); c. 130,000 ED attendances/yr at UCH ED; c. 130,000 admissions/yr; major teaching trust with national specialty centres including UK's first NHS proton-beam therapy centre.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£10.43M"},
            {"label": "Trust scale", "value": "Central-London academic acute: UCH + National Hospital for Neurology and Neurosurgery (Queen Square) + UCH Macmillan Cancer Centre + RNTNE + Eastman Dental + Grafton Way (PBT); c. 12,000 WTE"},
            {"label": "Central-London rateable values", "value": "Camden + Westminster billing authority rates among the highest in England — drives high per-bed baseline"},
            {"label": "Tertiary specialty mix", "value": "National Hospital for Neurology + Neurosurgery + UCH Cancer Centre + UK's first NHS Proton Beam Therapy centre (Grafton Way Building, opened 2021) — drives high-value specialised estate"},
            {"label": "Billing authorities", "value": "London Borough of Camden + (smaller proportion) Westminster City Council"},
            {"label": "VOA 2023 revaluation", "value": "Valuation Office Agency 2023 revaluation effective Apr 2023 reset rateable values across central London"},
            {"label": "NDR 2024 Act", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduced new multiplier categories effective Apr 2025"},
            {"label": "Proton Beam Therapy estate", "value": "Grafton Way Building (UK's first NHS PBT centre, opened 2021) added high-rateable-value asset to portfolio"},
            {"label": "Funding trajectory", "value": "2021-22 c. £8.5M → 2023-24 c. £10M (post-VOA revaluation + Grafton Way full-yr) → 2024-25 £10.43M"},
            {"label": "Delivery body", "value": "Trust Estates + Finance functions + Valuation Office Agency (HMRC) + Camden + Westminster billing authorities"},
            {"label": "Policy owner", "value": "MHCLG / DLUHC (NDR policy) + HM Treasury (multiplier setting) + DHSC + NHSE Provider Finance + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list; NAO local-government finance reviews; Trust ARA 2023-24 estates note"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2008 separate UCLH legacy hospital baselines · Successor: post-Apr 2025 NDR 2024 Act multiplier regime"}
        ],
        "notes": "UCLH's business rates line is structurally elevated by the central-London location of its estate, where Camden and Westminster rateable values rank among the highest in England — particularly for the National Hospital for Neurology and Neurosurgery at Queen Square, the UCH Macmillan Cancer Centre and the Grafton Way Building hosting the UK's first NHS Proton Beam Therapy centre (opened 2021). The VOA 2023 revaluation reset central-London rateable values effective April 2023; the NDR (Multipliers and Private Finance) Act 2024 introduced new multiplier categories from April 2025. NHS trusts pay full rates with no mandatory charitable relief, making central-London rate management a material finance lever as additional specialised estate comes onstream.",
        "sources": [
            {"publisher": "University College London Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uclh.nhs.uk/about-us/who-we-are/annual-reports-and-financial-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/14/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UCLH provider profile (RRV)", "url": "https://www.cqc.org.uk/provider/RRV"}
        ],
        "related": ["University College London Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals Birmingham NHS Foundation Trust", "Valuation Office Agency", "Department of Health and Social Care"]
    },
}
