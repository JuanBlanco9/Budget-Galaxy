# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 11 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "General supplies & services — Hampshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
        "description": "Hampshire Hospitals' £7.30M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor below-threshold equipment across the three-site Royal Hampshire County Hospital (Winchester) + Basingstoke and North Hampshire + Andover War Memorial estate. The trust serves the central + north Hampshire catchment in the Hampshire & Isle of Wight ICS, with Basingstoke hosting nationally significant peritoneal-malignancy and HPB tertiary services that lift non-clinical baselines above peer DGH groups.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 600,000 central + north Hampshire catchment (Winchester, Basingstoke, Andover, Alton, Test Valley); c. 145,000 ED attendances/yr (Winchester + Basingstoke EDs); c. 70,000 elective + day-case admissions/yr; nationally commissioned peritoneal malignancy / HPB / complex colorectal at Basingstoke.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£7.30M"},
            {"label": "Trust scale", "value": "Three-site acute (Winchester + Basingstoke + Andover); c. 6,500 WTE; c. 600,000 catchment"},
            {"label": "ED throughput", "value": "c. 145,000 attendances/yr (Winchester RHCH + Basingstoke EDs combined)"},
            {"label": "Elective + day-case", "value": "c. 70,000 admissions/yr"},
            {"label": "Specialist tertiary lift", "value": "Basingstoke nationally commissioned peritoneal malignancy / HPB / complex colorectal — elevates non-clinical consumable baseline above DGH peer"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Hampshire & IoW ICS collaborative + trust-direct contracts"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + sustained non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.8M → 2023-24 c. £6.7M → 2024-25 £7.30M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Hampshire & IoW ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHSE Operational Plan returns; Trust ARA 2023-24; CQC inspection RN5"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 separate Winchester + Basingstoke trusts (merged Jan 2012) · Successor: New Hospital Programme cohort (Basingstoke) — Jan 2025 Reset deferred to post-2030 wave"}
        ],
        "notes": "Hampshire Hospitals formed via the January 2012 merger of Winchester & Eastleigh and Basingstoke & North Hampshire trusts, and its non-clinical consumables baseline reflects three-site operations plus Basingstoke's nationally commissioned peritoneal-malignancy and HPB tertiary services that elevate consumable demand above peer DGH groups. The trust sits in the original New Hospital Programme cohort for a Basingstoke rebuild — the January 2025 NHP Reset deferred this scheme into the post-2030 wave, sustaining the existing estate's operational consumable profile longer than originally planned. Industrial action 2023-24 drove agency-backfill churn; April 2025 NIC step-up and CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hampshirehospitals.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Hampshire Hospitals provider profile (RN5)", "url": "https://www.cqc.org.uk/provider/RN5"}
        ],
        "related": ["Hampshire Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "New Hospital Programme", "General supplies & services — Royal Berkshire NHS Foundation Trust"]
    },
    "Business rates — Guy's & St Thomas' NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Guy's & St Thomas' NHS Foundation Trust"}],
        "description": "GSTT's £7.29M business-rates line covers non-domestic rates payable on the central-London estate spanning St Thomas' Hospital (Westminster), Guy's Hospital (Southwark), Evelina London Children's Hospital, the Royal Brompton + Harefield (post-Feb 2021 merger), community-clinic estate and central support sites. The high rateable values of central-London Lambeth/Southwark sites and Royal Brompton's South Kensington footprint drive a rates baseline materially above peer Acute trusts, with the 2023 Valuation Office Agency revaluation and post-2024 multiplier reform reshaping the trajectory.",
        "beneficiaries": "c. 24,000 WTE staff serving a c. 800,000 Lambeth + Southwark + Lewisham core catchment plus national specialist referrals; c. 240,000 ED attendances/yr (St Thomas' ED); c. 200,000 elective + day-case admissions/yr; Royal Brompton + Harefield national cardiothoracic/respiratory + Evelina paediatric.",
        "legal_basis": "Local Government Finance Act 1988 Schedule 6 (non-domestic rating valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Local Government Finance Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£7.29M"},
            {"label": "Trust scale", "value": "c. 24,000 WTE — UK's largest acute trust by turnover; central-London + national specialist estate"},
            {"label": "Estate covered", "value": "St Thomas' (Lambeth) + Guy's (Southwark) + Evelina + Royal Brompton (Kensington) + Harefield (Hillingdon) + community + corporate"},
            {"label": "VOA 2023 revaluation", "value": "April 2023 list took effect — central-London hereditaments revalued, transitional relief tapered through 2024-25"},
            {"label": "Multiplier reform 2024", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduced lower multiplier for retail/hospitality and higher for £500k+ rateable-value properties from 2026-27 — large-acute trusts in higher-multiplier band"},
            {"label": "Royal Brompton merger Feb 2021", "value": "Royal Brompton & Harefield NHS FT merged into GSTT 1 Feb 2021 — added South Kensington + Hillingdon hereditaments to rates base"},
            {"label": "NHS Charitable status", "value": "NHS bodies pay full business rates — no charitable mandatory relief unlike charity-sector peers"},
            {"label": "Funding trajectory", "value": "Pre-merger c. £5.5M (2020-21) → post-Brompton merger £6.5M (2022-23) → 2024-25 £7.29M (VOA 2023 effects + multiplier indexation)"},
            {"label": "Delivery body", "value": "Trust E&F + Lambeth / Southwark / Westminster / Hillingdon / RB Kensington & Chelsea billing authorities + Valuation Office Agency"},
            {"label": "Policy owner", "value": "MHCLG (multiplier policy) + HM Treasury + DHSC + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "VOA 2023 list publication + revaluation impact assessment; NAO/IFS NDR commentary; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate Royal Brompton & Harefield rates base · Successor: 2026-27 multiplier-reform band split + 2028 revaluation cycle"}
        ],
        "notes": "GSTT's business-rates line reflects the cumulative effect of the February 2021 merger with Royal Brompton & Harefield NHS FT — adding South Kensington and Hillingdon hereditaments — combined with the April 2023 Valuation Office Agency revaluation that lifted central-London rateable values. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a higher multiplier band from 2026-27 for properties with rateable value above £500,000, into which large acute-trust hereditaments fall, signalling further upward pressure. NHS bodies pay full non-domestic rates without charitable mandatory relief, so the trust remains exposed to the full multiplier and revaluation cycle through 2028.",
        "sources": [
            {"publisher": "Guy's and St Thomas' NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.guysandstthomas.nhs.uk/about-us/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "Business rates revaluation 2023", "url": "https://www.gov.uk/government/collections/non-domestic-rating-2023-revaluation"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/39"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: NDR multipliers 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-revaluation-2023-information"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Guy's & St Thomas' NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Barts Health NHS Trust", "Valuation Office Agency", "Transport (business + patient) — Guy's & St Thomas' NHS Foundation Trust"]
    },
    "Transport (business + patient) — Nottingham University Hospitals NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Nottingham University Hospitals NHS Trust"}],
        "description": "NUH's £7.21M transport line covers business mileage reimbursement under AfC Section 17 + AMAP, lease and pool-vehicle fleet (IFRS 16), patient transport services contracted under NHSE PTS Eligibility, and inter-site shuttles between QMC, City Hospital and Ropewalk House. The trust is one of England's largest acute trusts and a major regional tertiary centre (East Midlands trauma, neuro, cardiac), driving inter-site clinical movement and PTS volume above peer single-site DGHs in the Nottingham & Nottinghamshire ICS.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 2.5M East Midlands tertiary catchment; c. 220,000 ED attendances/yr (QMC ED — Major Trauma Centre); c. 130,000 elective + day-case admissions/yr; PTS volume c. 200,000 patient journeys/yr commissioned via NCL/EMAS-area providers.",
        "legal_basis": "NHS Act 2006 · Health and Care Act 2022 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change Section 17 (mileage allowances) · HMRC AMAP rates · IFRS 16 Leases · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£7.21M"},
            {"label": "Trust scale", "value": "c. 17,000 WTE; c. 2.5M tertiary catchment; QMC + City Hospital + Ropewalk House"},
            {"label": "Major Trauma Centre", "value": "QMC houses East Midlands MTC — drives inter-site transfers + helicopter handover + PTS volume"},
            {"label": "Inter-site shuttles", "value": "Routine clinical + corporate shuttle between QMC + City Hospital — multi-mile inter-site travel sustained on operational baseline"},
            {"label": "PTS provider", "value": "Patient Transport Services contracted to regional PTS provider (East Midlands Ambulance Service / EMAS group + commercial cohort)"},
            {"label": "AfC Section 17 / AMAP", "value": "Business mileage reimbursed at AfC reserve rate under Section 17 + HMRC AMAP framework (45p/mile first 10k)"},
            {"label": "IFRS 16 effect", "value": "Pool fleet + lease vehicles brought on-balance-sheet from 2022-23 transition — inflates transport line vs pre-IFRS 16 baseline"},
            {"label": "Funding trajectory", "value": "Pre-IFRS 16 c. £5.5M → IFRS 16 transition 2022-23 step-up → 2024-25 £7.21M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Procurement + EMAS-area PTS provider + NHSE East Midlands commissioning"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Nottingham & Nottinghamshire ICB + NHSE PTS policy"},
            {"label": "Evaluation evidence", "value": "NHSE PTS Review 2021-22; CQC inspection RX1; Trust ARA 2023-24; NHSE Major Trauma annual review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 expensed-only fleet · Successor: NHP Reset cohort planning could consolidate QMC + City sites long-term, reducing inter-site shuttle baseline"}
        ],
        "notes": "NUH's transport baseline reflects the multi-site East Midlands tertiary footprint — QMC's Major Trauma Centre status and the routine clinical and corporate shuttle traffic between QMC and City Hospital sustain inter-site travel demand above peer DGHs. The April 2022 IFRS 16 transition stepped pool fleet and lease vehicles onto the balance sheet, lifting the transport line's headline figure. Industrial action 2023-24 drove additional inter-site cover travel and locum mileage claims. Patient transport services are commissioned via the EMAS-area provider cohort under NHSE eligibility criteria reviewed in 2021-22; the NHP Reset cohort planning offers the medium-term lever for site consolidation that could reduce inter-site shuttle baseline.",
        "sources": [
            {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nuh.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — Mileage allowances", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NUH provider profile (RX1)", "url": "https://www.cqc.org.uk/provider/RX1"}
        ],
        "related": ["Nottingham University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Transport (business + patient) — Royal Free London NHS Foundation Trust", "New Hospital Programme"]
    },
    "General supplies & services — Surrey And Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Surrey And Sussex Healthcare NHS Trust"}],
        "description": "SASH's £7.21M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor below-threshold equipment at the single-site East Surrey Hospital (Redhill) plus a community-clinic footprint. The trust serves the east Surrey + west Sussex border catchment in the Surrey Heartlands ICS, having moved from CQC 'requires improvement' to 'outstanding' across the 2010s — a turnaround case-study repeatedly cited by NHSE/CQC.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 535,000 east Surrey, north-east West Sussex and south-east Surrey catchment (Redhill, Reigate, Crawley, Horley, Caterham); c. 130,000 ED attendances/yr (East Surrey Hospital ED); c. 60,000 elective + day-case admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£7.21M"},
            {"label": "Trust scale", "value": "Single-site (East Surrey Hospital, Redhill); c. 4,000 WTE; c. 535,000 catchment"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr at East Surrey ED"},
            {"label": "Elective + day-case", "value": "c. 60,000 admissions/yr"},
            {"label": "CQC turnaround case-study", "value": "Moved from 'requires improvement' (2014) → 'outstanding' (2018) — repeatedly cited NHSE/CQC turnaround template"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Surrey Heartlands ICS collaborative + trust-direct contracts"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.5M → 2023-24 c. £6.7M → 2024-25 £7.21M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Surrey Heartlands ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHSE Operational Plan returns; CQC inspection 2018 'Outstanding' (RTP); Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1998 separate East Surrey + Crawley/Horsham trusts · Successor: Surrey Heartlands collaborative procurement scaling"}
        ],
        "notes": "SASH operates a single-site model centred on East Surrey Hospital, with non-clinical consumables baseline reflecting steady c. 130,000 ED attendances/yr and c. 60,000 elective admissions/yr across a Surrey/Sussex border catchment. The trust's well-documented CQC turnaround from 'requires improvement' in 2014 to 'outstanding' in 2018 — a frequently cited NHSE template — was supported by tightened procurement and supplies discipline alongside cultural and clinical-governance reform. NHS Supply Chain remains dominant, with Surrey Heartlands ICS collaborative scaling as the medium-term lever; industrial action 2023-24 drove cancellation re-stocking churn, and April 2025 NIC step-up plus CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Surrey and Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.surreyandsussex.nhs.uk/about-us/annual-report-and-accounts/"},
            {"publisher": "Care Quality Commission", "title": "Surrey and Sussex Healthcare provider profile (RTP)", "url": "https://www.cqc.org.uk/provider/RTP"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital", "url": "https://model.nhs.uk/"}
        ],
        "related": ["Surrey And Sussex Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Hampshire Hospitals NHS Foundation Trust", "Care Quality Commission"]
    },
    "General supplies & services — University Hospitals of Morecambe Bay NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "University Hospitals of Morecambe Bay NHS Foundation Trust"}],
        "description": "UHMB's £7.20M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor below-threshold equipment across the Royal Lancaster Infirmary + Furness General (Barrow-in-Furness) + Westmorland General (Kendal) three-site rural-coastal estate. The trust's Cumbria + North Lancashire footprint — geographically the most dispersed acute trust in England — sustains a high site-services overhead, with the legacy Morecambe Bay Investigation (Kirkup 2015) shaping ongoing assurance and procurement governance.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 365,000 Cumbria + North Lancashire catchment across c. 1,000 sq miles; c. 110,000 ED attendances/yr (RLI + FGH EDs); c. 50,000 elective + day-case admissions/yr; rural-coastal access constraints.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£7.20M"},
            {"label": "Trust scale", "value": "Three-site rural-coastal acute (RLI + FGH + Westmorland); c. 6,000 WTE; c. 365,000 catchment over c. 1,000 sq miles"},
            {"label": "ED throughput", "value": "c. 110,000 attendances/yr (Royal Lancaster + Furness General EDs)"},
            {"label": "Geographic dispersion premium", "value": "Most dispersed acute footprint in England — drives multi-site supplies overhead + transport-of-goods baseline"},
            {"label": "Morecambe Bay legacy", "value": "Kirkup 2015 Morecambe Bay Investigation shapes ongoing governance + procurement assurance regime"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Lancashire & South Cumbria + North East and North Cumbria ICS collaboratives + trust-direct"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.6M → 2023-24 c. £6.7M → 2024-25 £7.20M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Lancashire & South Cumbria ICS collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lancashire & South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Kirkup 2015 Morecambe Bay Investigation report; CQC inspection RTX; Model Hospital; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1998 separate Lancaster + Furness + Westmorland trusts · Successor: ICS collaborative procurement scaling"}
        ],
        "notes": "UHMB operates the most geographically dispersed acute footprint in England — Royal Lancaster Infirmary, Furness General (Barrow-in-Furness, c. 50 miles north-west) and Westmorland General (Kendal) — sustaining a multi-site non-clinical consumables baseline and goods-transport overhead above peer DGH groups. The Kirkup 2015 Morecambe Bay Investigation into maternity failings continues to shape the trust's governance and procurement assurance regime. NHS Supply Chain remains dominant, with Lancashire & South Cumbria ICS collaborative scaling as the medium-term lever. Industrial action 2023-24 drove cancellation re-stocking churn; April 2025 NIC step-up and CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "University Hospitals of Morecambe Bay NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhmb.nhs.uk/about/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Morecambe Bay Investigation (Kirkup 2015)", "url": "https://www.gov.uk/government/publications/morecambe-bay-investigation-report"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHMB provider profile (RTX)", "url": "https://www.cqc.org.uk/provider/RTX"}
        ],
        "related": ["University Hospitals of Morecambe Bay NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Hampshire Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Royal Berkshire NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Royal Berkshire NHS Foundation Trust"}],
        "description": "Royal Berkshire's £7.18M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor below-threshold equipment at the single-site Royal Berkshire Hospital (London Road, Reading) plus a community-clinic footprint. The trust is in the New Hospital Programme cohort for a Reading rebuild — the January 2025 NHP Reset deferred this scheme into the post-2030 wave, keeping the legacy Victorian estate operational longer with sustained non-clinical consumable demand under Buckinghamshire, Oxfordshire and Berkshire West (BOB) ICS.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 600,000 Reading + west Berkshire + south Oxfordshire catchment; c. 130,000 ED attendances/yr (Royal Berkshire ED); c. 70,000 elective + day-case admissions/yr; tertiary-cohort burns + plastics services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£7.18M"},
            {"label": "Trust scale", "value": "Single-site (Royal Berkshire Hospital, Reading); c. 5,500 WTE; c. 600,000 catchment"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr at RBH ED"},
            {"label": "Elective + day-case", "value": "c. 70,000 admissions/yr"},
            {"label": "NHP cohort + Jan 2025 Reset", "value": "Royal Berkshire in original 40-hospital NHP cohort for full rebuild — Jan 2025 NHP Reset deferred to post-2030 wave"},
            {"label": "Estate age", "value": "Victorian-era core hospital (founded 1839) — high backlog maintenance + estate-services consumable demand"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + BOB ICS collaborative + trust-direct contracts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.6M → 2023-24 c. £6.7M → 2024-25 £7.18M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + BOB ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + BOB ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHP review 2023; NHSE NHP Reset Jan 2025; CQC inspection RHW; Model Hospital; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: stand-alone Royal Berkshire Hospital pre-FT · Successor: post-2030 NHP rebuild scheme — eventual estate transition"}
        ],
        "notes": "Royal Berkshire's non-clinical consumables baseline reflects its single-site Reading footprint and the sustained operational demand on the Victorian-era core estate (founded 1839) that drives elevated estate-services and hotel-services consumable use. The trust was placed in the original 40-hospital New Hospital Programme cohort for a Reading rebuild — the January 2025 NHP Reset deferred this scheme into the post-2030 wave, sustaining the existing estate's operational consumable profile longer than originally planned and putting backlog-maintenance pressure on the supplies line. NHS Supply Chain remains dominant via BOB ICS collaborative; April 2025 NIC step-up and CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Royal Berkshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalberkshire.nhs.uk/about-us/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Royal Berkshire provider profile (RHW)", "url": "https://www.cqc.org.uk/provider/RHW"}
        ],
        "related": ["Royal Berkshire NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "New Hospital Programme", "NHS Supply Chain", "General supplies & services — Hampshire Hospitals NHS Foundation Trust"]
    },
    "PFI / LIFT charges — Mid and South Essex NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Mid and South Essex NHS Foundation Trust"}],
        "description": "MSE's £7.13M PFI/LIFT charge covers residual unitary-charge pass-through on the Orsett Hospital and Basildon-area LIFT estate plus retained PFI obligations inherited from the legacy Basildon, Mid Essex and Southend trusts merged in April 2020. The line covers debt service, lifecycle hard-FM and indexed soft-FM components across smaller PFI/LIFT-funded community and acute support buildings within the MSE footprint serving south Essex under Mid and South Essex ICS.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 1.2M Mid + South Essex catchment; c. 320,000 ED attendances/yr (Basildon + Broomfield + Southend EDs combined); c. 130,000 elective + day-case admissions/yr; PFI/LIFT estate covers smaller acute support + community-clinic buildings.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · LIFT Programme regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£7.13M"},
            {"label": "Trust formation", "value": "MSE FT formed 1 Apr 2020 via merger of Basildon & Thurrock + Mid Essex Hospital Services + Southend University Hospital — three legacy PFI/LIFT obligations consolidated"},
            {"label": "Estate covered", "value": "Smaller PFI/LIFT-funded community + acute support buildings inherited from legacy trusts (incl. Orsett-area LIFT cohort)"},
            {"label": "Carillion 2018 effect", "value": "Carillion Jan 2018 collapse + Engie/Equans novation on FM subcontracts at certain inherited PFI sites"},
            {"label": "Hand-back planning", "value": "Earlier-vintage LIFT/PFI deals approaching IPA/HMT PFI Hand-Back unit engagement window"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM"},
            {"label": "IFRS 16 effect", "value": "Service-concession components reclassified through IFRS 16 transition (2022) — DHSC GAM ch.7 split affects headline figure"},
            {"label": "Funding trajectory", "value": "Post-merger consolidated line £6.5-7.5M range as RPI uplift offsets debt-service amortisation"},
            {"label": "Delivery body", "value": "Inherited SPVs + Engie / Equans / Sodexo-cohort FM (post-Carillion novations) + trust E&F"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI/LIFT guidance + NHSE Provider Finance + Mid and South Essex ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI hand-back report 2020; NAO Carillion investigation 2018; CQC inspection R5G; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate Basildon + Mid Essex + Southend PFI/LIFT lines · Successor: PFI/LIFT contract expiry hand-backs across late 2020s/2030s"}
        ],
        "notes": "MSE FT formed via the April 2020 merger of three south Essex acute trusts — Basildon & Thurrock, Mid Essex and Southend — consolidating three legacy PFI/LIFT obligations into a single consolidated line covering smaller acute-support and community-clinic LIFT-funded buildings (including Orsett-area cohort) rather than a flagship hospital PFI. Carillion's January 2018 collapse triggered FM contract novations to Engie/Equans across inherited subcontracts. RPI indexation continues to lift soft-FM components even as debt-service amortises down. Earlier-vintage LIFT/PFI deals are approaching the IPA/HMT PFI Hand-Back unit engagement window, with NAO's 2020 hand-back report shaping governance.",
        "sources": [
            {"publisher": "Mid and South Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mse.nhs.uk/about-us/publications-policies-and-reports"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mid and South Essex provider profile (R5G)", "url": "https://www.cqc.org.uk/provider/R5G"}
        ],
        "related": ["Mid and South Essex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — The Hillingdon Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "The Hillingdon Hospitals NHS Foundation Trust"}],
        "description": "Hillingdon's £7.09M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the Hillingdon Hospital + Mount Vernon site footprint serving outer-west London. The trust is in the original New Hospital Programme cohort for a Hillingdon rebuild — January 2025 NHP Reset placed Hillingdon in the priority Wave 1 cohort given the 2017 fire damage and condemned 1960s towerblock — meaning establishment-line activity is shaped by transition planning into the new build under North West London ICS.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 320,000 Hillingdon catchment (Uxbridge, Ruislip, Hayes, Heathrow boundary); c. 100,000 ED attendances/yr (Hillingdon ED — serves Heathrow); c. 50,000 elective + day-case admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.09M"},
            {"label": "Trust scale", "value": "Two-site (Hillingdon Hospital + Mount Vernon); c. 3,500 WTE; c. 320,000 catchment"},
            {"label": "ED throughput", "value": "c. 100,000 attendances/yr — serves Heathrow Airport boundary, includes airport-related casework"},
            {"label": "NHP Wave 1 priority", "value": "Hillingdon Hospital placed in NHP Reset Wave 1 (Jan 2025) — Wave 1 priority due to 2017 fire damage + condemned 1960s tower; new build targeted by 2030"},
            {"label": "2017 fire", "value": "Major 2017 fire in main hospital block accelerated rebuild case + drove establishment overhead through transition planning"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme (Cerner/Oracle Health cohort) drives training + change-management establishment lift"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC step-up on training + corporate-services payroll feed forward"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.5M → 2023-24 c. £6.5M → 2024-25 £7.09M — NHP transition-planning + EPR programme uplift"},
            {"label": "Delivery body", "value": "Trust corporate services + HR + Comms + IT + NHP project team + procurement"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North West London ICB + DHSC NHP project board"},
            {"label": "Evaluation evidence", "value": "NAO NHP review 2023; NHSE NHP Reset Jan 2025 Wave 1 listing; CQC inspection RAS; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: stand-alone Hillingdon Hospital + Mount Vernon (pre-FT) · Successor: NHP Wave 1 new build by 2030 + post-build operational baseline"}
        ],
        "notes": "Hillingdon's establishment-line costs reflect the trust's preparation for the New Hospital Programme rebuild — placed in the priority Wave 1 cohort under the January 2025 NHP Reset following the 2017 fire damage and the condemned 1960s tower block deemed unfit for continued long-term operation. NHP transition-planning sustains corporate-services, training and project overhead above peer DGH baselines. The Frontline Digitisation EPR programme (Cerner/Oracle Health cohort) drives training and change-management uplift, and industrial action 2023-24 pushed up agency, locum and recruitment-advertising activity. April 2025 NIC step-up feeds forward training and corporate-services payroll cost into 2025-26.",
        "sources": [
            {"publisher": "The Hillingdon Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thh.nhs.uk/about/publications/annualreports.php"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Reset January 2025 (Wave 1 priority)", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Hillingdon Hospitals provider profile (RAS)", "url": "https://www.cqc.org.uk/provider/RAS"}
        ],
        "related": ["The Hillingdon Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Frontline Digitisation Programme", "Establishment costs — University Hospitals Plymouth NHS Trust"]
    },
    "Establishment costs — University Hospitals Plymouth NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospitals Plymouth NHS Trust"}],
        "description": "UHP's £7.07M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions at the single-site Derriford Hospital + community-clinic footprint serving Plymouth, west Devon and east Cornwall. As the South West peninsula's tertiary centre (Major Trauma, neuro, cardiac), UHP carries a regional corporate-services overhead disproportionate to its ED catchment, reinforced by the Frontline Digitisation EPR rollout under Devon ICS.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 450,000 Plymouth + west Devon + east Cornwall + South West naval-services catchment plus tertiary referrals; c. 110,000 ED attendances/yr (Derriford ED — South West Major Trauma Centre); c. 75,000 elective + day-case admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.07M"},
            {"label": "Trust scale", "value": "Single-site Derriford Hospital + community footprint; c. 9,500 WTE; c. 450,000 catchment + tertiary referrals"},
            {"label": "Major Trauma Centre", "value": "Derriford houses South West Peninsula MTC — drives regional corporate-services + training overhead"},
            {"label": "Naval-services catchment", "value": "Plymouth Royal Naval base + Devonport — military-services interface adds occupational-health + corporate liaison"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme drives training + change-management establishment lift"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC step-up on training + corporate-services payroll feed forward"},
            {"label": "CQC engagement", "value": "Sustained CQC engagement drives quality-improvement + governance overhead reflected in establishment baseline"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.5M → 2023-24 c. £6.6M → 2024-25 £7.07M"},
            {"label": "Delivery body", "value": "Trust corporate services + HR + Comms + IT + EPR project team + Procurement"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Devon ICB + NHSE South West"},
            {"label": "Evaluation evidence", "value": "CQC inspection REF; NHSE Major Trauma annual review; NHSE Frontline Digitisation; Model Hospital; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 Plymouth Hospitals NHS Trust · Successor: post-EPR steady-state corporate-services baseline + South West Peninsula tertiary integration"}
        ],
        "notes": "UHP's establishment-line baseline reflects its role as the South West Peninsula's tertiary centre and Major Trauma Centre at Derriford Hospital, sustaining a regional corporate-services overhead disproportionate to its catchment ED throughput. The Frontline Digitisation EPR rollout drives training and change-management lift, and the trust's military-services interface with Plymouth's Royal Naval base and Devonport adds an occupational-health and corporate-liaison overhead absent at peer DGHs. Industrial action 2023-24 pushed up agency, locum and recruitment-advertising activity; April 2025 NIC step-up feeds forward training and corporate-services payroll cost into 2025-26 alongside sustained CQC engagement.",
        "sources": [
            {"publisher": "University Hospitals Plymouth NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.plymouthhospitals.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Frontline Digitisation Programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Plymouth provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Major Trauma Centres Annual Review", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d15/"}
        ],
        "related": ["University Hospitals Plymouth NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Establishment costs — The Hillingdon Hospitals NHS Foundation Trust", "Establishment costs — Royal Devon University Healthcare NHS Foundation Trust"]
    },
    "Establishment costs — East Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "East Sussex Healthcare NHS Trust"}],
        "description": "ESHT's £7.05M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the Conquest Hospital (Hastings) + Eastbourne DGH + Bexhill + community-clinic footprint serving east Sussex. The trust runs a paired-acute model with both Conquest and Eastbourne providing emergency services, with an extensive community-clinic estate inherited via the legacy 2011 transfer of community services into ESHT — sustaining corporate-services overhead under Sussex ICS.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 525,000 east Sussex catchment (Hastings, Eastbourne, Bexhill, Rye); c. 145,000 ED attendances/yr (Conquest + Eastbourne EDs combined); c. 65,000 elective + day-case admissions/yr; large community-services footprint.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.05M"},
            {"label": "Trust scale", "value": "Two-site acute (Conquest + Eastbourne) + community footprint; c. 6,000 WTE; c. 525,000 catchment"},
            {"label": "Paired-acute model", "value": "Conquest (Hastings) + Eastbourne DGH both retain emergency + acute services — twin-site corporate overhead"},
            {"label": "Community services 2011", "value": "Sussex community services transferred into ESHT in 2011 — added community-clinic footprint + corporate-services overhead"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme drives training + change-management establishment lift"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC step-up on training + corporate-services payroll feed forward"},
            {"label": "CQC history", "value": "Long-running CQC engagement through 2010s — Special Measures 2015 → out of SM 2017 → ongoing 'good' rating; quality-governance overhead embedded in establishment baseline"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.5M → 2023-24 c. £6.6M → 2024-25 £7.05M"},
            {"label": "Delivery body", "value": "Trust corporate services + HR + Comms + IT + Procurement"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Sussex ICB + NHSE South East"},
            {"label": "Evaluation evidence", "value": "CQC inspection RXC; NHSE Operational Plan returns; Model Hospital; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate East Sussex Hospitals + Sussex community services · Successor: Sussex ICS shared corporate-services scaling"}
        ],
        "notes": "ESHT operates a paired-acute model with both Conquest Hospital (Hastings) and Eastbourne DGH retaining emergency and acute services across the east Sussex catchment, sustaining a twin-site corporate-services overhead. The 2011 transfer of Sussex community services into ESHT added a community-clinic footprint and corporate-services overhead embedded in the establishment baseline. The trust's CQC engagement history — Special Measures in 2015, out by 2017, and ongoing 'good' rating — left a quality-governance overhead embedded in establishment activity. Frontline Digitisation EPR drives training and change-management lift; industrial action 2023-24 pushed agency and recruitment-advertising spend; April 2025 NIC step-up feeds forward into 2025-26.",
        "sources": [
            {"publisher": "East Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esht.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "East Sussex Healthcare provider profile (RXC)", "url": "https://www.cqc.org.uk/provider/RXC"},
            {"publisher": "NHS England", "title": "Frontline Digitisation Programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Operational Planning Guidance 2024-25", "url": "https://www.england.nhs.uk/operational-planning-and-contracting/"}
        ],
        "related": ["East Sussex Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Establishment costs — University Hospitals Plymouth NHS Trust", "Establishment costs — Buckinghamshire Healthcare NHS Trust"]
    },
    "Establishment costs — Buckinghamshire Healthcare NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Buckinghamshire Healthcare NHS Trust"}],
        "description": "BHT's £7.02M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the Stoke Mandeville (Aylesbury) + Wycombe + Amersham + community-services footprint. The trust hosts the National Spinal Injuries Centre at Stoke Mandeville (founded by Sir Ludwig Guttmann 1944) — a nationally commissioned tertiary service that lifts corporate-services overhead above peer DGH baselines, plus community-services responsibility for Buckinghamshire under BOB ICS.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 540,000 Buckinghamshire catchment plus national NSIC referrals; c. 110,000 ED attendances/yr (Stoke Mandeville + Wycombe EDs); c. 55,000 elective + day-case admissions/yr; nationally commissioned spinal-injuries service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.02M"},
            {"label": "Trust scale", "value": "Stoke Mandeville (Aylesbury) + Wycombe + Amersham + community; c. 6,500 WTE; c. 540,000 catchment"},
            {"label": "National Spinal Injuries Centre", "value": "Founded 1944 by Sir Ludwig Guttmann at Stoke Mandeville — nationally commissioned tertiary service lifting corporate overhead"},
            {"label": "Community services transfer", "value": "Buckinghamshire community-services responsibility consolidated into BHT — adds corporate + training overhead"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme drives training + change-management establishment lift"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC step-up on training + corporate-services payroll feed forward"},
            {"label": "Wycombe stroke unit", "value": "Wycombe hyperacute stroke + cardiac centre — specialist tertiary lift on training + corporate-services overhead"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.5M → 2023-24 c. £6.6M → 2024-25 £7.02M"},
            {"label": "Delivery body", "value": "Trust corporate services + HR + Comms + IT + Procurement + NSIC"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + BOB ICB + NHSE Specialised Commissioning (NSIC)"},
            {"label": "Evaluation evidence", "value": "CQC inspection RXQ; NHSE Specialised Commissioning NSIC review; Model Hospital; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 stand-alone hospitals + community-services trust · Successor: BOB ICS shared-services scaling"}
        ],
        "notes": "Buckinghamshire Healthcare's establishment-line baseline reflects the multi-site Stoke Mandeville + Wycombe + Amersham acute footprint plus the corporate-services overhead absorbed when Buckinghamshire community services consolidated into the trust. The National Spinal Injuries Centre at Stoke Mandeville — founded by Sir Ludwig Guttmann in 1944 and a frequently cited Paralympic-movement origin — is a nationally commissioned tertiary service that elevates training, governance and corporate-liaison overhead above peer DGH baselines, alongside the Wycombe hyperacute stroke and cardiac specialist services. Frontline Digitisation EPR drives further training and change-management lift; industrial action 2023-24 pushed agency and recruitment spend; April 2025 NIC step-up feeds forward.",
        "sources": [
            {"publisher": "Buckinghamshire Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.buckshealthcare.nhs.uk/about-us/publications-and-reports/annual-reports/"},
            {"publisher": "NHS England", "title": "National Spinal Injuries Centre — specialised commissioning", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Care Quality Commission", "title": "Buckinghamshire Healthcare provider profile (RXQ)", "url": "https://www.cqc.org.uk/provider/RXQ"},
            {"publisher": "NHS England", "title": "Frontline Digitisation Programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Buckinghamshire Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Establishment costs — East Sussex Healthcare NHS Trust", "Establishment costs — Royal Devon University Healthcare NHS Foundation Trust"]
    },
    "General supplies & services — Wirral University Teaching Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Wirral University Teaching Hospital NHS Foundation Trust"}],
        "description": "WUTH's £6.97M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor below-threshold equipment across the Arrowe Park (Birkenhead) + Clatterbridge + Wirral community-clinic estate. The trust serves the Wirral peninsula in the Cheshire & Merseyside ICS, with a paired-site model anchored at Arrowe Park — non-clinical consumables baseline reflects steady DGH activity plus the corporate-services overhead of Clatterbridge co-location with The Clatterbridge Cancer Centre.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 320,000 Wirral peninsula catchment; c. 130,000 ED attendances/yr (Arrowe Park ED — single ED on Wirral); c. 60,000 elective + day-case admissions/yr; community-clinic footprint across Wirral.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£6.97M"},
            {"label": "Trust scale", "value": "Arrowe Park (Birkenhead) + Clatterbridge + community; c. 6,000 WTE; c. 320,000 Wirral catchment"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr at Arrowe Park ED — single ED serving Wirral peninsula"},
            {"label": "Elective + day-case", "value": "c. 60,000 admissions/yr"},
            {"label": "Clatterbridge co-location", "value": "Clatterbridge site shared with The Clatterbridge Cancer Centre NHS FT — joint estate-services + corporate-liaison consumable overhead"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Cheshire & Merseyside ICS collaborative + trust-direct contracts"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.4M → 2023-24 c. £6.5M → 2024-25 £6.97M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Cheshire & Merseyside ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHSE Operational Plan returns; CQC inspection RBL; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FT Wirral Hospital NHS Trust · Successor: Cheshire & Merseyside ICS collaborative procurement scaling"}
        ],
        "notes": "WUTH's non-clinical consumables baseline reflects single-ED operations at Arrowe Park serving the Wirral peninsula plus the Clatterbridge site shared with The Clatterbridge Cancer Centre NHS FT, which produces a joint estate-services and corporate-liaison consumable overhead absent at peer single-site DGHs. The trust's geographic isolation on the peninsula concentrates non-clinical demand on the supplies line. NHS Supply Chain remains dominant with Cheshire & Merseyside ICS collaborative scaling as the medium-term lever; industrial action 2023-24 drove cancellation re-stocking churn, and April 2025 NIC step-up plus sustained CPI on non-clinical inputs feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Wirral University Teaching Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wuth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Wirral University Teaching Hospital provider profile (RBL)", "url": "https://www.cqc.org.uk/provider/RBL"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Operational Planning Guidance 2024-25", "url": "https://www.england.nhs.uk/operational-planning-and-contracting/"}
        ],
        "related": ["Wirral University Teaching Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "The Clatterbridge Cancer Centre NHS Foundation Trust"]
    },
    "Establishment costs — Royal United Hospitals Bath NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Royal United Hospitals Bath NHS Foundation Trust"}],
        "description": "RUH Bath's £6.95M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions at the single-site Royal United Hospital (Combe Park, Bath) plus a community-clinic footprint serving Bath and North East Somerset, west Wiltshire and Mendip. The trust hosts a Dyson Cancer Centre (opened May 2024) and the RNHRD-linked rheumatology service — sustaining corporate-services and training overhead under BSW (Bath, Swindon and Wiltshire) ICS.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 500,000 Bath + west Wiltshire + Mendip catchment; c. 90,000 ED attendances/yr (RUH Bath ED); c. 60,000 elective + day-case admissions/yr; rheumatology + cancer specialty mix.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£6.95M"},
            {"label": "Trust scale", "value": "Single-site (RUH Combe Park) + community footprint; c. 5,000 WTE; c. 500,000 catchment"},
            {"label": "Dyson Cancer Centre", "value": "New Dyson Cancer Centre opened May 2024 — uplift in training, change-management + corporate-services activity"},
            {"label": "RNHRD rheumatology", "value": "Royal National Hospital for Rheumatic Diseases services transferred into RUH (2015) — specialty corporate overhead"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme (Cerner/Oracle Health cohort) drives training + change-management establishment lift"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC step-up on training + corporate-services payroll feed forward"},
            {"label": "Quartz House admin estate", "value": "Quartz House non-clinical admin block contributes to corporate-services overhead"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.4M → 2023-24 c. £6.5M → 2024-25 £6.95M (Dyson Cancer Centre uplift)"},
            {"label": "Delivery body", "value": "Trust corporate services + HR + Comms + IT + Procurement + Cancer Centre project team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + BSW ICB + NHSE Specialised Commissioning"},
            {"label": "Evaluation evidence", "value": "CQC inspection RD1; NHSE Cancer Alliance review; Model Hospital; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 RUH stand-alone + RNHRD as separate trust · Successor: Dyson Cancer Centre operational steady-state + BSW ICS shared services"}
        ],
        "notes": "RUH Bath's establishment-line baseline reflects the single-site Royal United Hospital footprint plus the corporate-services lift from the new Dyson Cancer Centre, which opened May 2024 and is sustaining transitional training, change-management and corporate-liaison overhead through 2024-25. The 2015 transfer of the Royal National Hospital for Rheumatic Diseases into RUH consolidated rheumatology specialty corporate overhead. Frontline Digitisation EPR rollout drives further training and change-management lift; industrial action 2023-24 pushed agency, locum and recruitment-advertising spend; April 2025 NIC step-up feeds forward training and corporate-services payroll cost into 2025-26.",
        "sources": [
            {"publisher": "Royal United Hospitals Bath NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ruh.nhs.uk/about/publications/annual_reports.asp"},
            {"publisher": "Royal United Hospitals Bath NHS Foundation Trust", "title": "Dyson Cancer Centre opening — May 2024", "url": "https://www.ruh.nhs.uk/dyson-cancer-centre/"},
            {"publisher": "Care Quality Commission", "title": "RUH Bath provider profile (RD1)", "url": "https://www.cqc.org.uk/provider/RD1"},
            {"publisher": "NHS England", "title": "Frontline Digitisation Programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Royal United Hospitals Bath NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Establishment costs — University Hospitals Plymouth NHS Trust", "Establishment costs — Buckinghamshire Healthcare NHS Trust"]
    },
    "Transport (business + patient) — University Hospitals Bristol and Weston NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospitals Bristol and Weston NHS Foundation Trust"}],
        "description": "UHBW's £6.87M transport line covers business mileage reimbursement under AfC Section 17 + AMAP, lease and pool-vehicle fleet (IFRS 16), patient transport services contracted under NHSE PTS Eligibility, and inter-site clinical movement between the central Bristol estate (BRI, Bristol Royal Hospital for Children, Bristol Eye, Bristol Heart Institute, St Michael's, Bristol Haematology and Oncology) and Weston General. The trust's geographically split footprint — Bristol c. 25 miles north of Weston-super-Mare — drives substantial inter-site movement under BNSSG ICS.",
        "beneficiaries": "c. 13,000 WTE staff serving a c. 1.6M BNSSG + South West tertiary catchment; c. 200,000 ED attendances/yr (BRI + BRHC + Weston EDs combined); c. 110,000 elective + day-case admissions/yr; nationally commissioned paediatric tertiary + cardiac.",
        "legal_basis": "NHS Act 2006 · Health and Care Act 2022 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change Section 17 (mileage allowances) · HMRC AMAP rates · IFRS 16 Leases · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£6.87M"},
            {"label": "Trust scale", "value": "c. 13,000 WTE; central Bristol cluster + Weston General; c. 1.6M BNSSG catchment + tertiary"},
            {"label": "Bristol-Weston split", "value": "Central Bristol cluster c. 25 miles north of Weston General — major inter-site clinical movement baseline"},
            {"label": "Weston merger Apr 2020", "value": "Weston Area Health NHS Trust merged into UHB to form UHBW 1 Apr 2020 — added inter-site travel obligation"},
            {"label": "Specialist tertiary lift", "value": "Bristol Royal Hospital for Children + Bristol Heart Institute + paediatric cardiac — drives specialist patient transport under specialised commissioning"},
            {"label": "AfC Section 17 / AMAP", "value": "Business mileage reimbursed at AfC reserve rate under Section 17 + HMRC AMAP framework (45p/mile first 10k)"},
            {"label": "IFRS 16 effect", "value": "Pool fleet + lease vehicles brought on-balance-sheet from 2022-23 transition — inflates transport line vs pre-IFRS 16 baseline"},
            {"label": "Funding trajectory", "value": "Pre-merger c. £4.5M → post-Weston merger 2020-21 c. £5.5M → IFRS 16 transition + Bristol-Weston pathway development → 2024-25 £6.87M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Procurement + regional PTS provider + NHSE specialised commissioning"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + BNSSG ICB + NHSE PTS policy"},
            {"label": "Evaluation evidence", "value": "NHSE PTS Review 2021-22; CQC inspection RA7; NHSE specialised commissioning paediatric review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate UHB + Weston Area transport baselines · Successor: BNSSG ICS pathway consolidation + post-IFRS 16 steady state"}
        ],
        "notes": "UHBW's transport baseline reflects the geographically split footprint created by the April 2020 merger of UHB with Weston Area Health NHS Trust — central Bristol's specialist cluster (BRI + BRHC + BHI + Bristol Eye + St Michael's) sits c. 25 miles north of Weston General, sustaining substantial inter-site clinical movement and specialist patient-transport demand under BNSSG ICS. The April 2022 IFRS 16 transition stepped pool fleet and lease vehicles onto the balance sheet. Specialised commissioning paediatric and cardiac referrals drive PTS volume. Industrial action 2023-24 pushed inter-site cover travel and locum mileage claims; the Bristol-Weston pathway-development work continues to shape transport patterns.",
        "sources": [
            {"publisher": "University Hospitals Bristol and Weston NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhbw.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — Mileage allowances", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "Care Quality Commission", "title": "UHBW provider profile (RA7)", "url": "https://www.cqc.org.uk/provider/RA7"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["University Hospitals Bristol and Weston NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Nottingham University Hospitals NHS Trust", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Transport (business + patient) — Royal Free London NHS Foundation Trust"]
    },
    "General supplies & services — North Tees and Hartlepool NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "North Tees and Hartlepool NHS Foundation Trust"}],
        "description": "NTH's £6.86M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor below-threshold equipment across the University Hospital of North Tees (Stockton) + University Hospital of Hartlepool + community-clinic estate. The trust serves the Stockton + Hartlepool catchment in the North East and North Cumbria ICS, and is in the New Hospital Programme cohort for a long-promised Wynyard rebuild — Jan 2025 NHP Reset retained but deferred — sustaining the existing two-site operational consumable profile.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 400,000 Stockton + Hartlepool + east Durham catchment; c. 110,000 ED attendances/yr (UHNT ED); c. 55,000 elective + day-case admissions/yr; community-clinic footprint.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£6.86M"},
            {"label": "Trust scale", "value": "Two-site (UHNT Stockton + UHH Hartlepool); c. 5,500 WTE; c. 400,000 catchment"},
            {"label": "ED throughput", "value": "c. 110,000 attendances/yr — single ED at UHNT (UHH downgraded historically)"},
            {"label": "Elective + day-case", "value": "c. 55,000 admissions/yr split across both sites"},
            {"label": "NHP Wynyard rebuild", "value": "Long-promised Wynyard new-build scheme in NHP cohort — Jan 2025 Reset retained but deferred to later wave"},
            {"label": "Hartlepool downgrade legacy", "value": "Hartlepool ED downgraded c. 2011 — political controversy reshaped catchment + sustained two-site operational footprint"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + NENC ICS collaborative + trust-direct contracts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.4M → 2023-24 c. £6.4M → 2024-25 £6.86M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + NENC ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHP review 2023; NHSE NHP Reset Jan 2025; CQC inspection RVW; Model Hospital; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1999 separate Stockton + Hartlepool trusts · Successor: NHP Wynyard rebuild post-Reset deferral"}
        ],
        "notes": "NTH operates a two-site model — University Hospital of North Tees (Stockton) and University Hospital of Hartlepool — with steady non-clinical consumables baseline reflecting the legacy Hartlepool ED downgrade c. 2011 (a politically charged moment in the north-east) that concentrated emergency throughput at UHNT while sustaining elective and outpatient activity at Hartlepool. The long-promised Wynyard rebuild — placed in the NHP cohort but deferred at the January 2025 Reset — keeps the two-site consumable profile in place longer than originally planned. NHS Supply Chain remains dominant via NENC ICS collaborative; industrial action 2023-24 drove cancellation re-stocking churn; April 2025 NIC step-up and CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "North Tees and Hartlepool NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nth.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "North Tees and Hartlepool provider profile (RVW)", "url": "https://www.cqc.org.uk/provider/RVW"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["North Tees and Hartlepool NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "New Hospital Programme", "General supplies & services — Hampshire Hospitals NHS Foundation Trust"]
    },
    "Establishment costs — Epsom and St Helier University Hospitals NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Epsom and St Helier University Hospitals NHS Trust"}],
        "description": "Epsom and St Helier's £6.81M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising and minor IT/software subscriptions across the Epsom (Surrey) + St Helier (Sutton/Carshalton) acute estate. The trust hosts the South West London Elective Orthopaedic Centre at Epsom and operates renal services across south London, and is in the New Hospital Programme cohort for the long-debated Sutton Specialist Emergency Care Hospital — Jan 2025 NHP Reset retained the scheme — driving sustained transition-planning corporate overhead under SWL ICS.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 490,000 south west London + Surrey catchment (Sutton, Merton, Surrey Downs); c. 175,000 ED attendances/yr (Epsom + St Helier EDs); c. 75,000 elective + day-case admissions/yr; SWLEOC + south-London renal services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£6.81M"},
            {"label": "Trust scale", "value": "Two-site (Epsom + St Helier); c. 5,500 WTE; c. 490,000 catchment"},
            {"label": "Sutton SECH new build", "value": "Specialist Emergency Care Hospital (Sutton) in NHP cohort — Jan 2025 Reset retained scheme; transition planning sustains establishment overhead"},
            {"label": "Estate condition", "value": "St Helier 1930s-era estate — high backlog maintenance + RAAC mitigation profile shapes corporate-services activity"},
            {"label": "SWLEOC", "value": "South West London Elective Orthopaedic Centre at Epsom — partnership with Croydon, Kingston, St George's; specialty corporate liaison"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme drives training + change-management establishment lift"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC step-up on training + corporate-services payroll feed forward"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.3M → 2023-24 c. £6.4M → 2024-25 £6.81M (NHP transition + EPR uplift)"},
            {"label": "Delivery body", "value": "Trust corporate services + HR + Comms + IT + Procurement + NHP Sutton SECH project team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South West London ICB + DHSC NHP project board"},
            {"label": "Evaluation evidence", "value": "NAO NHP review 2023; NHSE NHP Reset Jan 2025; CQC inspection RVR; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1999 separate Epsom + St Helier trusts · Successor: Sutton SECH new-build delivery + reconfigured site model"}
        ],
        "notes": "Epsom and St Helier's establishment-line baseline reflects the trust's two-site operations across south west London and Surrey, sustained transition-planning overhead from the long-debated Specialist Emergency Care Hospital at Sutton — placed in the NHP cohort and retained at the January 2025 Reset — and the corporate-services lift from hosting the SWLEOC partnership at Epsom. The 1930s-era St Helier estate carries elevated backlog maintenance and a RAAC mitigation profile that shapes corporate-services and project-management activity. Frontline Digitisation EPR drives training and change-management lift; industrial action 2023-24 pushed agency, locum and recruitment-advertising spend; April 2025 NIC step-up feeds forward into 2025-26.",
        "sources": [
            {"publisher": "Epsom and St Helier University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.epsom-sthelier.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "Epsom and St Helier provider profile (RVR)", "url": "https://www.cqc.org.uk/provider/RVR"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Epsom and St Helier University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Frontline Digitisation Programme", "Establishment costs — The Hillingdon Hospitals NHS Foundation Trust"]
    },
    "General supplies & services — The Shrewsbury and Telford Hospital NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
        "description": "SaTH's £6.79M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor below-threshold equipment across the Royal Shrewsbury Hospital + Princess Royal Hospital (Telford) two-site estate. The trust serves Shropshire, Telford & Wrekin and mid Wales catchments under Shropshire, Telford and Wrekin ICS, with a non-clinical baseline shaped by the legacy 'Future Fit' / Hospitals Transformation Programme reconfiguration debate and the Ockenden Review (Mar 2022) governance overhead.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 500,000 Shropshire + Telford & Wrekin + mid Wales catchment; c. 130,000 ED attendances/yr (RSH + PRH EDs combined); c. 60,000 elective + day-case admissions/yr; cross-border Welsh patients via Powys Teaching Health Board pathways.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£6.79M"},
            {"label": "Trust scale", "value": "Two-site (Royal Shrewsbury + Princess Royal Telford); c. 6,500 WTE; c. 500,000 catchment"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr (RSH + PRH EDs combined)"},
            {"label": "Cross-border Welsh activity", "value": "Cross-border patient flows from Powys Teaching Health Board (no DGH in Powys) — drives consumable demand vs same-population English peer"},
            {"label": "Hospitals Transformation Programme", "value": "Long-debated Future Fit / HTP reconfiguration (RSH emergency, PRH elective + women's-children) — implementation in NHP-adjacent cohort, drives transitional non-clinical demand"},
            {"label": "Ockenden Review legacy", "value": "Final Ockenden Report (Mar 2022) into maternity failings — sustained governance + assurance overhead embedded in supplies + corporate procurement"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + STW ICS collaborative + trust-direct contracts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.3M → 2023-24 c. £6.4M → 2024-25 £6.79M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + STW ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Shropshire, Telford and Wrekin ICB"},
            {"label": "Evaluation evidence", "value": "Ockenden Final Report (Mar 2022); CQC inspection RXW; NHSE Operational Plan returns; Model Hospital; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2003 separate Royal Shrewsbury + Princess Royal trusts · Successor: HTP / Future Fit site reconfiguration (RSH emergency + PRH elective)"}
        ],
        "notes": "SaTH's non-clinical consumables baseline reflects two-site operations across Royal Shrewsbury Hospital and Princess Royal Telford, plus the elevated cross-border Welsh patient flow from Powys Teaching Health Board (Powys has no DGH of its own). The trust's long-debated Hospitals Transformation Programme — formerly Future Fit — proposes splitting RSH as the emergency centre and PRH as the elective + women's & children's centre, sustaining transitional non-clinical demand as planning continues. The Ockenden Final Report (March 2022) into maternity failings left a sustained governance and assurance overhead embedded in procurement and supplies. NHS Supply Chain remains dominant via STW ICS collaborative; April 2025 NIC step-up and CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "The Shrewsbury and Telford Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sath.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Ockenden Final Report — March 2022", "url": "https://www.gov.uk/government/publications/final-report-of-the-ockenden-review"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "SaTH provider profile (RXW)", "url": "https://www.cqc.org.uk/provider/RXW"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Hampshire Hospitals NHS Foundation Trust", "General supplies & services — North Tees and Hartlepool NHS Foundation Trust"]
    },
}
