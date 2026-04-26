# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 03 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — Essex Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Essex Partnership University NHS Foundation Trust"}],
        "description": "EPUT's £2.37M 2024-25 amortisation charge is dominated by intangible-asset write-down on the Frontline Digitisation EPR rollout (Oracle Health / Cerner Millennium adopted across the trust under the post-Lampard digital programme), capitalised software licences for community-mental-health platforms, and capitalised training. The trust's intangibles base has expanded sharply since 2022 as Lampard Inquiry remediation forced accelerated investment in observation, ligature-monitoring and electronic record digitisation. Amortisation runs straight-line over 5–7 years per DHSC GAM ch.5.",
        "beneficiaries": "Approximately 5,500 staff using the rolled-out EPR across c. 80 inpatient wards and 200+ community sites covering c. 3.5M residents of Essex, Bedfordshire, Luton and parts of Suffolk; c. 12,500 service users active in caseload at any point; capitalised intangibles cover EPR, e-rostering, ligature-asset register and bed-management software.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.37M"},
            {"label": "Intangibles trajectory", "value": "Capitalised intangibles c. £6M (2021-22) → c. £14M (2024-25) post-Frontline Digitisation"},
            {"label": "Useful economic life", "value": "5–7 years straight-line for software licences; 3–5 years for capitalised configuration"},
            {"label": "Frontline Digitisation EPR", "value": "Oracle Health / Cerner Millennium adopted under MH-specific FD funding; Lampard remediation accelerated"},
            {"label": "Capitalised training", "value": "EPR go-live training + ligature-asset register training capitalised under DHSC GAM ch.5 thresholds"},
            {"label": "Delivery body", "value": "Trust Digital Services + NHSE Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate · IAS 38 / DHSC GAM oversight"},
            {"label": "Beneficiary count", "value": "~5,500 staff licensed; c. 12,500 active service users on caseload"},
            {"label": "Funding trajectory", "value": "Charge expected to plateau c. £2.5–3.0M to 2027-28 as FD assets reach mid-cycle"},
            {"label": "Evaluation evidence", "value": "Lampard Inquiry interim findings (2024); CQC 'Requires Improvement' 2023; NHSE FD assurance reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy MOBIUS / RiO records · Successor: Oracle Health convergence + AI-clinical-noting pilots"}
        ],
        "notes": "EPUT's amortisation line is structurally elevated by the Lampard Inquiry context: the trust faced sustained scrutiny over inpatient deaths in north and south Essex services, prompting accelerated digital investment in ligature-asset registers, observation logs and a unified electronic record. The Frontline Digitisation grant accelerated Oracle Health rollout, lifting the intangibles base and feeding straight-line amortisation. The charge will plateau as 2022-24 capitalisations exhaust their economic life mid-cycle. CQC's 2023 'Requires Improvement' rating and the Lampard Inquiry's interim findings reinforce why DHSC permitted accelerated capitalisation rather than expensing.",
        "sources": [
            {"publisher": "Essex Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://eput.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme guidance", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lampard Inquiry", "title": "Independent Inquiry into mental health deaths in Essex", "url": "https://lampardinquiry.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "EPUT provider profile (RHA)", "url": "https://www.cqc.org.uk/provider/RHA"}
        ],
        "related": ["Essex Partnership University NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Amortisation — Mersey Care NHS Foundation Trust", "Lease expenditure — Essex Partnership University NHS Foundation Trust"]
    },
    "General supplies & services — Devon Partnership NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Devon Partnership NHS Trust"}],
        "description": "DPT's £2.36M 2024-25 general supplies & services line covers ward consumables (linen, hygiene, catering disposables, clinical-waste sacks, ligature-safe furnishings replacement) plus stationery and IT consumables across its inpatient mental-health, secure and learning-disability estate. As a relatively small specialist MH trust serving Devon's dispersed geography, the line is sensitive to per-occupied-bed-day consumption and to ligature-mitigation refresh — bedlinen and soft-furnishing replacement programmes have been accelerated since the trust's 2018 NHSE-led intervention on safety culture.",
        "beneficiaries": "Approximately 2,800 staff working across c. 35 inpatient wards (general adult, older adult, secure, LD/autism) and 80+ community sites; serves c. 1.2M residents of Devon (excluding Plymouth); c. 3,300 active service users on caseload; ligature-safe consumables cover c. 600 acute MH beds.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.36M"},
            {"label": "Ward consumables share", "value": "Catering, linen, hygiene, clinical-waste estimated > 60% of line"},
            {"label": "Ligature-safe refresh share", "value": "Bedlinen and soft-furnishings replacement c. 10–15% of line post-2018 intervention"},
            {"label": "Procurement framework", "value": "NHS Supply Chain category towers + Crown Commercial Service frameworks"},
            {"label": "Site count served", "value": "c. 35 inpatient wards + 80+ community / CMHT bases across Devon"},
            {"label": "Delivery body", "value": "Trust procurement + NHS Supply Chain + facilities-management contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Commercial Directorate · NHS Supply Chain mandate"},
            {"label": "Funding trajectory", "value": "Real-terms pressure from CPI and lithium-battery / electronics inflation; line broadly flat 2022-25"},
            {"label": "Evaluation evidence", "value": "NHSE 2018 quality-summit intervention; CQC 'Good' 2023; Edenfield-style risk register reviewed annually"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 fragmented procurement · Successor: NHS Supply Chain category-tower convergence"}
        ],
        "notes": "DPT's general supplies & services line is sensitive to two drivers beyond standard CPI: ligature-mitigation soft-furnishings refresh (post-2018 NHSE-led safety intervention required accelerated replacement of curtains, bedlinen and patient-room furnishings to ligature-resistant equivalents); and the trust's dispersed Devon geography (Wonford House Exeter, Langdon Hospital Dawlish, Cygnet-Devon partnerships, plus rural CMHT bases) which raises last-mile delivery cost and inflates per-occupied-bed-day consumption above urban peers. NHS Supply Chain category-tower migration has begun to compress unit cost but the secure / LD service mix keeps the bedlinen and clinical-waste share elevated.",
        "sources": [
            {"publisher": "Devon Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dpt.nhs.uk/about-us/publications-policies-and-reports"},
            {"publisher": "NHS Supply Chain", "title": "Category towers and procurement framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Devon Partnership NHS Trust provider profile (RWV)", "url": "https://www.cqc.org.uk/provider/RWV"},
            {"publisher": "NHS England", "title": "Mental health inpatient safety improvement programme", "url": "https://www.england.nhs.uk/mental-health/"}
        ],
        "related": ["Devon Partnership NHS Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "Department of Health and Social Care", "General supplies & services — Sheffield Health and Social Care NHS Foundation Trust", "Establishment costs — Devon Partnership NHS Trust"]
    },
    "Establishment costs — Black Country Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Black Country Healthcare NHS Foundation Trust"}],
        "description": "BCHFT's £2.35M 2024-25 establishment costs line covers postage, telephony, mobile devices, courier services, training fees, professional subscriptions and statutory levies (CQC fees, ICO fees) across its mental-health and learning-disability footprint covering Dudley, Sandwell, Walsall and Wolverhampton. The trust was formed in April 2020 by merger of Dudley & Walsall MH and Black Country Partnership; establishment costs reflect post-merger consolidation onto a single mobile/telephony estate plus accelerated Microsoft 365 licensing under N365 NHS-wide deal.",
        "beneficiaries": "Approximately 4,200 staff across c. 30 inpatient wards and 120+ community / CMHT / IAPT bases serving c. 1.2M residents of the Black Country (Dudley, Sandwell, Walsall, Wolverhampton); c. 7,800 active service users; mobile-device estate c. 4,000 smartphones and laptops post-pandemic agile rollout.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.35M"},
            {"label": "Telephony + mobile share", "value": "c. 30–35% of line — c. 4,000 mobile devices on N365 / NHS Mail"},
            {"label": "CQC + ICO statutory fees", "value": "c. £150k combined annual statutory levies"},
            {"label": "Training + subscriptions share", "value": "c. 25% of line — mandatory training, professional registration, CPD"},
            {"label": "Trust formed", "value": "April 2020 — merger of Dudley & Walsall MH + Black Country Partnership"},
            {"label": "Site count served", "value": "c. 30 inpatient wards + 120+ community bases across 4 boroughs"},
            {"label": "Delivery body", "value": "Trust corporate services + N365 NHS-wide licensing + Crown Commercial Service frameworks"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation + ICO / CQC fee-setting"},
            {"label": "Funding trajectory", "value": "Step-up 2020-21 (merger) then plateau; mobile-device refresh cycle 4 years"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; NHSE merger benefits review 2022; Black Country ICS digital strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: separate Dudley & Walsall MH + Black Country Partnership establishment lines · Successor: ICS-shared back-office under review"}
        ],
        "notes": "BCHFT's establishment costs line carries a structural post-merger feature: the April 2020 amalgamation into a single Black Country MH provider required consolidation onto one telephony / mobile estate, one ICO registration, and one CQC fee structure, but retained separate building footprints in 4 boroughs that drive higher per-staff postage and courier cost than a single-borough peer. The pandemic's agile-working acceleration lifted mobile-device count materially. Statutory fees (CQC, ICO) and mandatory training subscriptions are non-discretionary; the discretionary share is concentrated in courier and stationery, where Black Country ICS digital strategy aims to compress paper flow.",
        "sources": [
            {"publisher": "Black Country Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.blackcountryhealthcare.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "BCHFT provider profile (TAJ)", "url": "https://www.cqc.org.uk/provider/TAJ"},
            {"publisher": "NHS England", "title": "N365 NHS-wide Microsoft licensing", "url": "https://digital.nhs.uk/services/nhsmail"},
            {"publisher": "Black Country ICB", "title": "Black Country ICS digital strategy", "url": "https://blackcountry.icb.nhs.uk/"}
        ],
        "related": ["Black Country Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Berkshire Healthcare NHS Foundation Trust", "Lease expenditure — Black Country Healthcare NHS Foundation Trust"]
    },
    "Establishment costs — North East London NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "North East London NHS Foundation Trust"}],
        "description": "NELFT's £2.34M 2024-25 establishment costs cover postage, telephony, mobile-device fleet, courier, training fees, professional subscriptions and statutory levies (CQC, ICO) across a combined MH + community footprint spanning Barking & Dagenham, Havering, Redbridge, Waltham Forest and Essex. The trust integrates community physical-health services with mental-health, so the establishment line is structurally larger per staff than pure-play MH peers — community nursing courier and patient-record postage feed the line.",
        "beneficiaries": "Approximately 7,500 staff across c. 35 inpatient wards (MH + community) and 250+ community / IAPT / district-nursing / CMHT bases serving c. 4.9M residents (combined NEL boroughs + Essex community contracts); mobile-device estate c. 7,000 smartphones and laptops post-pandemic.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.34M"},
            {"label": "Telephony + mobile share", "value": "c. 35% of line — c. 7,000 mobile devices, large agile-working community-nursing fleet"},
            {"label": "Courier + postage share", "value": "Elevated vs MH-only peers due to community physical-health caseload"},
            {"label": "CQC + ICO statutory fees", "value": "c. £180k combined annual statutory levies"},
            {"label": "Site count served", "value": "c. 35 inpatient wards + 250+ community / district / CMHT / IAPT bases"},
            {"label": "Delivery body", "value": "Trust corporate services + N365 NHS-wide licensing + Crown Commercial frameworks"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation + NEL ICB"},
            {"label": "Funding trajectory", "value": "Step-up post-pandemic agile rollout; plateau 2023-24 to 2024-25"},
            {"label": "Beneficiary count", "value": "c. 4.9M residents covered through MH + community contracts"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; NEL ICB digital strategy; Goodmayes Hospital safety reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger NELMHT + community trust establishment lines · Successor: NEL ICB shared back-office under review"}
        ],
        "notes": "NELFT's establishment line carries a structural feature peculiar to integrated MH + community trusts: c. 250 community bases and a large district-nursing / health-visiting workforce inflate mobile-device, courier and postage cost relative to pure-play MH trusts of similar headcount. The Goodmayes Hospital MH inpatient site dominates the inpatient share but the community caseload drives the line. Pandemic-era agile rollout left a sustained mobile-device fleet refresh cycle (c. 4 years). Statutory fees (CQC, ICO) and mandatory training are non-discretionary; the NEL ICB digital strategy aims to consolidate licensing across NEL providers to compress per-seat cost.",
        "sources": [
            {"publisher": "North East London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nelft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NELFT provider profile (RAT)", "url": "https://www.cqc.org.uk/provider/RAT"},
            {"publisher": "NHS England", "title": "N365 NHS-wide Microsoft licensing", "url": "https://digital.nhs.uk/services/nhsmail"},
            {"publisher": "North East London ICB", "title": "NEL ICS digital strategy", "url": "https://northeastlondon.icb.nhs.uk/"}
        ],
        "related": ["North East London NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Impairments net of reversals — North East London NHS Foundation Trust", "PFI / LIFT charges — North East London NHS Foundation Trust"]
    },
    "General supplies & services — Rotherham Doncaster and South Humber NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Rotherham Doncaster and South Humber NHS Foundation Trust"}],
        "description": "RDaSH's £2.32M 2024-25 general supplies & services line covers ward consumables (linen, hygiene, catering, clinical-waste sacks, ligature-safe soft-furnishings refresh) across MH inpatient wards, learning-disability units and CAMHS Tier 4 beds, plus stationery and IT consumables across community sites. The trust's footprint spans Rotherham, Doncaster and North Lincolnshire (South Humber), and the line is sensitive to per-occupied-bed-day consumption plus the ligature-mitigation refresh programme accelerated post-Edenfield (2022 Panorama).",
        "beneficiaries": "Approximately 3,800 staff across c. 25 inpatient wards (MH + LD + CAMHS Tier 4) and 90+ community bases serving c. 1.0M residents of Rotherham, Doncaster and North Lincolnshire; c. 5,500 active service users; ligature-safe consumables cover c. 350 acute MH and LD beds.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.32M"},
            {"label": "Ward consumables share", "value": "Catering, linen, hygiene, clinical-waste estimated > 60% of line"},
            {"label": "Ligature-safe refresh share", "value": "c. 10% of line post-Edenfield-era safety review"},
            {"label": "Procurement framework", "value": "NHS Supply Chain category towers + Crown Commercial Service frameworks"},
            {"label": "Site count served", "value": "c. 25 inpatient wards + 90+ community / CMHT bases across 3 boroughs"},
            {"label": "Delivery body", "value": "Trust procurement + NHS Supply Chain + facilities-management contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Commercial Directorate"},
            {"label": "Funding trajectory", "value": "Real-terms pressure from CPI; line broadly flat 2022-25"},
            {"label": "Beneficiary count", "value": "c. 1.0M catchment; c. 5,500 active caseload"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; NHSE MH inpatient safety improvement programme; SY ICB plan"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 fragmented procurement · Successor: NHS Supply Chain category-tower convergence"}
        ],
        "notes": "RDaSH's general supplies & services line is sensitive to two structural drivers: ligature-mitigation soft-furnishings refresh accelerated after the 2022 Edenfield (GMMH) Panorama exposure prompted system-wide MH inpatient safety review; and the trust's Tier 4 CAMHS provision (Aspen ward at Tickhill Road) raises per-bed consumable consumption above general adult MH wards. The trust spans South Yorkshire and North Lincolnshire ICSs which complicates joint-procurement aggregation. NHS Supply Chain category-tower migration has begun to compress unit cost. Catering, linen and clinical-waste remain the largest sub-shares; the line carries no PPE-legacy writedown post-2023.",
        "sources": [
            {"publisher": "Rotherham Doncaster and South Humber NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rdash.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Category towers and procurement framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "RDaSH provider profile (RXE)", "url": "https://www.cqc.org.uk/provider/RXE"},
            {"publisher": "NHS England", "title": "Mental health inpatient safety improvement programme", "url": "https://www.england.nhs.uk/mental-health/"}
        ],
        "related": ["Rotherham Doncaster and South Humber NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Rotherham Doncaster and South Humber NHS Foundation Trust", "Transport (business + patient) — Rotherham Doncaster and South Humber NHS Foundation Trust"]
    },
    "Business rates — Southern Health NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Southern Health NHS Foundation Trust"}],
        "description": "Southern Health's £2.28M 2024-25 business-rates charge reflects VOA-set rateable values across MH and community sites covering Hampshire and parts of Dorset (Antelope House Southampton, Melbury Lodge Winchester, Parklands Hospital Basingstoke, plus c. 80 community / CMHT / IAPT bases). NHS MH trusts are rated as 'Other' hereditaments under LGFA 1988 Schedule 6 and pay the standard 49.9p UBR multiplier (2024-25); the trust does not benefit from charitable exemption. The 2023 revaluation cycle reset rateable values from a 2021 antecedent valuation date.",
        "beneficiaries": "Approximately 6,000 staff across c. 35 inpatient wards (general adult, older adult, secure, CAMHS, LD) and 80+ community sites serving c. 1.5M residents of Hampshire (excluding Portsmouth) and parts of Dorset; c. 12,000 active service users on caseload.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.28M"},
            {"label": "UBR multiplier 2024-25", "value": "49.9p (small business rate); 54.6p (standard) — applied per hereditament threshold"},
            {"label": "Antecedent valuation date", "value": "1 April 2021 (2023 revaluation list, in force from April 2023)"},
            {"label": "Estimated rateable value base", "value": "c. £4.5M aggregate RV implied by £2.28M charge"},
            {"label": "Hereditament count", "value": "c. 100+ rated entries (inpatient + community sites)"},
            {"label": "Charitable exemption", "value": "Not applied — NHS FTs rated as 'Other' hereditaments"},
            {"label": "Delivery body", "value": "VOA (rateable-value setting) + Hampshire / Dorset billing authorities (collection)"},
            {"label": "Policy owner", "value": "MHCLG / DLUHC + HM Treasury (multiplier)"},
            {"label": "Funding trajectory", "value": "2023 revaluation step; CPI-linked multiplier from 2024-25 (not RPI)"},
            {"label": "Evaluation evidence", "value": "Mazars 2015 inquiry into Southern Health learning-disability deaths; CQC reviews 2018-23"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 revaluation list · Successor: 2026 revaluation cycle (3-yearly)"}
        ],
        "notes": "Southern Health's business-rates line carries the historic context of the Mazars 2015 inquiry into deaths in learning-disability and MH services, which shaped the trust's subsequent estate strategy — including closure of Tatchbury Mount and consolidation onto Antelope House Southampton. The 2023 revaluation cycle (antecedent date April 2021) lifted rateable values modestly across the dispersed Hampshire estate. The trust does not benefit from charitable exemption and pays 'Other' hereditament rates at the 2024-25 standard / small-business multipliers. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 shifted the multiplier uprating from RPI to CPI from April 2024, slightly compressing future growth.",
        "sources": [
            {"publisher": "Southern Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southernhealth.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 non-domestic rating list", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "MHCLG", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/13/contents"},
            {"publisher": "Care Quality Commission", "title": "Southern Health NHS FT provider profile (RW1)", "url": "https://www.cqc.org.uk/provider/RW1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Southern Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Norfolk and Suffolk NHS Foundation Trust", "PFI / LIFT charges — Southern Health NHS Foundation Trust"]
    },
    "Transport (business + patient) — South London and Maudsley NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "South London and Maudsley NHS Foundation Trust"}],
        "description": "SLAM's £2.23M 2024-25 transport line covers business mileage reimbursements (community-MH staff, AMHP visits, home-treatment teams, perinatal liaison), staff travel between Maudsley, Bethlem Royal, Lambeth and Lewisham sites, plus patient transport for inpatient admissions, secure-unit transfers and OAP (out-of-area placement) returns. ULEZ (London-wide from August 2023) materially raised SLAM's compliant-vehicle premium since the trust operates across all four South London boroughs.",
        "beneficiaries": "Approximately 5,000 staff serving c. 1.3M residents of Lambeth, Southwark, Lewisham and Croydon; mileage claimed against c. 4 main sites + 80+ community bases; specialist national services (Bethlem Royal Eating Disorders, National Affective Disorders Service) generate cross-London patient transport.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions (mileage rates) · Mental Health Act 1983 (s.140 conveyance)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.23M"},
            {"label": "AfC mileage rates 2024-25", "value": "59p/mile first 3,500 (standard rate); 24p/mile thereafter (NHS Staff Council)"},
            {"label": "ULEZ exposure", "value": "Trust footprint entirely within ULEZ since Aug 2023 — accelerated lease-fleet electrification"},
            {"label": "Patient transport share", "value": "OAP returns + s.136 conveyance + secure transfers — c. 25–30% of line"},
            {"label": "Specialist national services", "value": "Bethlem Royal Eating Disorders + National Affective Disorders generate cross-region transport"},
            {"label": "Site count served", "value": "4 main sites (Maudsley, Bethlem Royal, Lambeth, Ladywell Lewisham) + 80+ community bases"},
            {"label": "Delivery body", "value": "Trust fleet + LAS / G4S patient-transport contracts + AfC mileage scheme"},
            {"label": "Policy owner", "value": "DHSC + NHSE + GLA / TfL (ULEZ)"},
            {"label": "Funding trajectory", "value": "Step-up post-Aug 2023 ULEZ expansion; CPI inflation; OAP volumes pressure"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; NHSE OAP reduction programme; King's Fund London MH report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ULEZ-expansion fleet · Successor: zero-emission fleet conversion + OAP elimination target"}
        ],
        "notes": "SLAM's transport line is structurally elevated by three London-specific drivers: ULEZ expansion (entire South London footprint subject from Aug 2023, accelerating lease-fleet electrification and lifting compliant-vehicle premium); the trust's specialist national services (Bethlem Royal Eating Disorders Unit, National Affective Disorders) which generate cross-London and inter-region patient transport; and persistent OAP (out-of-area placement) volumes — South London inpatient bed pressure forces transfers to private-sector or distant NHS beds, with return transport billed on this line. The Mental Health Act s.136 conveyance pathway with Met Police (Right Care Right Person rollout) is changing the patient-transport mix.",
        "sources": [
            {"publisher": "South London and Maudsley NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://slam.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Staff Council", "title": "AfC mileage rates 2024-25", "url": "https://www.nhsemployers.org/publications/agenda-change-mileage-allowances"},
            {"publisher": "Transport for London", "title": "Ultra Low Emission Zone expansion Aug 2023", "url": "https://tfl.gov.uk/modes/driving/ulez"},
            {"publisher": "Care Quality Commission", "title": "SLAM provider profile (RV5)", "url": "https://www.cqc.org.uk/provider/RV5"}
        ],
        "related": ["South London and Maudsley NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — South London and Maudsley NHS Foundation Trust", "Business rates — South London and Maudsley NHS Foundation Trust"]
    },
    "Business rates — West London NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "West London NHS Trust"}],
        "description": "West London NHS Trust's £2.19M 2024-25 business-rates charge reflects VOA-set rateable values across its MH and forensic estate, dominated by Broadmoor Hospital (high-secure forensic, Crowthorne) and the Ealing/Hammersmith/Hounslow community-MH footprint. Broadmoor's substantial high-secure rateable value is the largest single hereditament; the trust does not benefit from charitable exemption and pays the standard 49.9p/54.6p UBR multiplier on each occupied site. The 2023 revaluation cycle reset values from a 2021 antecedent.",
        "beneficiaries": "Approximately 4,500 staff across Broadmoor (c. 234 high-secure beds, post-2019 rebuild) plus c. 25 inpatient wards and 60+ community sites serving c. 800,000 residents of Ealing, Hammersmith & Fulham, Hounslow plus a national high-secure patient catchment (Broadmoor).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022 · Criminal Justice Act 2003 (high-secure remit)",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.19M"},
            {"label": "Broadmoor share", "value": "Estimated > 35% of line — single largest hereditament (Crowthorne, Bracknell Forest BC billing)"},
            {"label": "UBR multiplier 2024-25", "value": "49.9p (small business rate); 54.6p (standard) — applied per hereditament threshold"},
            {"label": "Antecedent valuation date", "value": "1 April 2021 (2023 revaluation list)"},
            {"label": "Estimated rateable value base", "value": "c. £4.4M aggregate RV implied by £2.19M charge"},
            {"label": "Charitable exemption", "value": "Not applied — NHS FTs and trusts rated as 'Other'"},
            {"label": "Broadmoor rebuild", "value": "New Broadmoor opened 2019 (replacing 1860s buildings); 234-bed high-secure"},
            {"label": "Delivery body", "value": "VOA + Bracknell Forest / Ealing / Hammersmith & Fulham / Hounslow billing authorities"},
            {"label": "Policy owner", "value": "MHCLG / DLUHC + HM Treasury (multiplier)"},
            {"label": "Funding trajectory", "value": "Broadmoor 2019 rebuild step-change, then plateau; CPI-linked from 2024-25"},
            {"label": "Evaluation evidence", "value": "CQC reviews of Broadmoor 2022-23; HMIP-equivalent NAO scrutiny of high-secure capital"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 Broadmoor Victorian estate · Successor: 2026 revaluation cycle"}
        ],
        "notes": "West London's business-rates line is structurally weighted by Broadmoor — the new high-secure hospital (opened 2019, replacing the 1863 Victorian buildings) carries a substantial rateable value and is billed by Bracknell Forest BC, separately from the Ealing/Hammersmith/Hounslow community estate billed by London-borough authorities. The 2023 revaluation cycle reset rateable values across all hereditaments. The trust does not benefit from charitable exemption. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 shifted multiplier uprating to CPI from April 2024. Broadmoor's high-secure status does not generate a rates discount; functional-equivalent valuation under Schedule 6 captures the substantial built form.",
        "sources": [
            {"publisher": "West London NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.westlondon.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 non-domestic rating list", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "MHCLG", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/13/contents"},
            {"publisher": "Care Quality Commission", "title": "West London NHS Trust provider profile (RKL)", "url": "https://www.cqc.org.uk/provider/RKL"},
            {"publisher": "National Audit Office", "title": "High-secure mental health services capital", "url": "https://www.nao.org.uk/"}
        ],
        "related": ["West London NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — West London NHS Trust", "Lease expenditure — West London NHS Trust"]
    },
    "Transport (business + patient) — Barnet, Enfield And Haringey Mental Health NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Barnet, Enfield And Haringey Mental Health NHS Trust"}],
        "description": "BEH-MHT's £2.17M 2024-25 transport line covers business mileage reimbursements (community-MH staff, AMHP visits, home-treatment teams, perinatal liaison), staff travel between Chase Farm Mental Health Centre, St Ann's Hospital and the c. 40 community sites, plus patient transport for inpatient admissions, secure-unit transfers and OAP returns. ULEZ (London-wide from August 2023) materially raised BEH's compliant-vehicle premium since the trust's North London footprint is entirely within ULEZ.",
        "beneficiaries": "Approximately 3,000 staff serving c. 1.0M residents of Barnet, Enfield and Haringey; mileage claimed across c. 4 inpatient sites + 40+ community bases; St Ann's Hospital Tottenham is being part-disposed for the Haringey Heartlands regeneration scheme, which is reshaping inter-site travel patterns.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions (mileage rates) · Mental Health Act 1983 (s.140 conveyance)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.17M"},
            {"label": "AfC mileage rates 2024-25", "value": "59p/mile first 3,500; 24p/mile thereafter"},
            {"label": "ULEZ exposure", "value": "Trust footprint entirely within ULEZ since Aug 2023 — accelerated lease-fleet electrification"},
            {"label": "Patient transport share", "value": "OAP returns + s.136 conveyance + secure transfers — c. 25% of line"},
            {"label": "St Ann's Haringey Heartlands", "value": "Site part-disposal for housing regeneration; new MH inpatient build on retained portion (c. 2025-26 opening)"},
            {"label": "Site count served", "value": "c. 4 main inpatient sites (St Ann's, Chase Farm MHC, etc) + 40+ community bases"},
            {"label": "Delivery body", "value": "Trust fleet + LAS / G4S patient-transport contracts + AfC mileage scheme"},
            {"label": "Policy owner", "value": "DHSC + NHSE + NCL ICB + GLA / TfL (ULEZ)"},
            {"label": "Funding trajectory", "value": "Step-up post-Aug 2023 ULEZ; further pressure during St Ann's transition"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; NHSE OAP reduction programme; NCL ICB MH plan"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ULEZ-expansion fleet · Successor: zero-emission fleet + new St Ann's inpatient hub"}
        ],
        "notes": "BEH-MHT's transport line is shaped by three drivers: ULEZ expansion (entire North London footprint subject from Aug 2023, lifting the compliant-vehicle premium); the St Ann's Hospital Tottenham regeneration (Haringey Heartlands) which is reshaping the inpatient footprint and during transition raises inter-site travel; and persistent OAP volumes — North London inpatient bed pressure forces transfers to private-sector or distant NHS beds. The trust collaborates with Camden and Islington FT and the proposed North London MH single-provider configuration is in scoping, which would consolidate transport spend over time.",
        "sources": [
            {"publisher": "Barnet, Enfield and Haringey Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.beh-mht.nhs.uk/about/publications.htm"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Staff Council", "title": "AfC mileage rates 2024-25", "url": "https://www.nhsemployers.org/publications/agenda-change-mileage-allowances"},
            {"publisher": "Transport for London", "title": "Ultra Low Emission Zone expansion Aug 2023", "url": "https://tfl.gov.uk/modes/driving/ulez"},
            {"publisher": "Care Quality Commission", "title": "BEH-MHT provider profile (RRP)", "url": "https://www.cqc.org.uk/provider/RRP"}
        ],
        "related": ["Barnet, Enfield And Haringey Mental Health NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Barnet, Enfield And Haringey Mental Health NHS Trust", "Impairments net of reversals — Barnet, Enfield And Haringey Mental Health NHS Trust"]
    },
    "Business rates — Tees, Esk and Wear Valleys NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Tees, Esk and Wear Valleys NHS Foundation Trust"}],
        "description": "TEWV's £2.17M 2024-25 business-rates charge reflects VOA-set rateable values across a large dispersed MH footprint covering County Durham, North Yorkshire, York, Tees Valley and parts of Cumbria — c. 100+ hereditaments including Roseberry Park (Middlesbrough), West Park (Darlington), Foss Park (York) and CMHT bases. NHS FTs are rated as 'Other' hereditaments under LGFA 1988 Schedule 6 and pay the standard 49.9p/54.6p UBR multiplier (2024-25). The trust does not benefit from charitable exemption.",
        "beneficiaries": "Approximately 6,500 staff across c. 50 inpatient wards (general adult, older adult, secure, LD, CAMHS Tier 4) and 100+ community sites serving c. 2.0M residents of County Durham, Tees Valley, North Yorkshire and York; c. 12,000 active service users; one of the largest geographic footprints among English MH trusts.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.17M"},
            {"label": "UBR multiplier 2024-25", "value": "49.9p (small business rate); 54.6p (standard) — applied per hereditament threshold"},
            {"label": "Antecedent valuation date", "value": "1 April 2021 (2023 revaluation list)"},
            {"label": "Estimated rateable value base", "value": "c. £4.3M aggregate RV implied by £2.17M charge"},
            {"label": "Hereditament count", "value": "c. 100+ (largest dispersed MH estate in England by site count)"},
            {"label": "Charitable exemption", "value": "Not applied — NHS FTs rated as 'Other'"},
            {"label": "Major sites", "value": "Roseberry Park Middlesbrough; West Park Darlington; Foss Park York; Lanchester Road Durham"},
            {"label": "Delivery body", "value": "VOA + multiple billing authorities (Durham CC, Stockton, Middlesbrough, NYCC, City of York)"},
            {"label": "Policy owner", "value": "MHCLG / DLUHC + HM Treasury (multiplier)"},
            {"label": "Funding trajectory", "value": "2023 revaluation step; CPI-linked from 2024-25; West Lane Hospital closure 2019 reduced base"},
            {"label": "Evaluation evidence", "value": "CQC inspection 2023 (post-West Lane); HSIB West Lane review; NHSE quality summit 2020"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 list pre-West Lane closure · Successor: 2026 revaluation cycle"}
        ],
        "notes": "TEWV's business-rates line is structurally heavy because of the trust's exceptionally large geographic footprint — covering County Durham, Tees Valley, North Yorkshire and York — and the consequent multiplicity of billing authorities (Durham CC, Stockton, Middlesbrough, North Yorkshire Council, City of York) each levying on separate hereditaments. The closure of West Lane Hospital Middlesbrough in 2019 (following the deaths of three young people and HSIB review) reduced the rateable base; subsequent CAMHS Tier 4 reconfiguration to Foss Park and West Park has shifted the geographic mix. The 2023 revaluation cycle reset values from a 2021 antecedent date.",
        "sources": [
            {"publisher": "Tees, Esk and Wear Valleys NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.tewv.nhs.uk/about-your-care/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 non-domestic rating list", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "MHCLG", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/13/contents"},
            {"publisher": "Care Quality Commission", "title": "TEWV provider profile (RX3)", "url": "https://www.cqc.org.uk/provider/RX3"},
            {"publisher": "Healthcare Safety Investigation Branch", "title": "West Lane Hospital independent review", "url": "https://www.hssib.org.uk/"}
        ],
        "related": ["Tees, Esk and Wear Valleys NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "PFI / LIFT charges — Tees, Esk and Wear Valleys NHS Foundation Trust", "Business rates — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust"]
    },
    "Business rates — Midlands Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Midlands Partnership NHS Foundation Trust"}],
        "description": "MPFT's £2.14M 2024-25 business-rates charge reflects VOA-set rateable values across an integrated MH + community estate covering Staffordshire, Stoke-on-Trent and Shropshire (post-2018 expansion adding Robert Jones and Agnes Hunt-adjacent community services and the South Staffordshire and Shropshire Healthcare merger). The footprint includes St George's Stafford, Brocton Hall and c. 100 community / CMHT / district-nursing bases, all rated as 'Other' hereditaments at standard 49.9p/54.6p multipliers. From October 2024 MPFT merged with Black Country Partnership and others into the new West Midlands MH provider configuration.",
        "beneficiaries": "Approximately 9,000 staff (pre-Oct-2024 reconfiguration baseline) across c. 35 inpatient wards (MH + LD) and 100+ community / district-nursing bases serving c. 1.5M residents of Staffordshire, Stoke and Shropshire; integrated MH + community physical-health caseload c. 16,000 active.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.14M"},
            {"label": "UBR multiplier 2024-25", "value": "49.9p (small business rate); 54.6p (standard) — applied per hereditament threshold"},
            {"label": "Antecedent valuation date", "value": "1 April 2021 (2023 revaluation list)"},
            {"label": "Estimated rateable value base", "value": "c. £4.2M aggregate RV implied by £2.14M charge"},
            {"label": "Hereditament count", "value": "c. 100+ (integrated MH + community footprint)"},
            {"label": "Charitable exemption", "value": "Not applied — NHS FTs rated as 'Other'"},
            {"label": "Major sites", "value": "St George's Stafford; Redwoods Centre Shrewsbury; community / district-nursing bases across Staffs and Shropshire"},
            {"label": "Delivery body", "value": "VOA + multiple billing authorities (Stafford BC, Stoke CC, Shropshire Council, Telford & Wrekin)"},
            {"label": "Policy owner", "value": "MHCLG / DLUHC + HM Treasury (multiplier)"},
            {"label": "Funding trajectory", "value": "2023 revaluation step; CPI-linked from 2024-25; reconfiguration may shift 2025-26 hereditament list"},
            {"label": "Reconfiguration", "value": "Oct 2024 merger into new West Midlands MH provider configuration"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2018 SSSFT + South Staffs and Shropshire Healthcare merger · Successor: post-Oct-2024 merged West Midlands MH provider"}
        ],
        "notes": "MPFT's business-rates line carries a structurally larger profile than pure-play MH peers because the trust integrates community physical-health (district nursing, health visiting) into its footprint, raising hereditament count materially. The 2018 South Staffordshire & Shropshire Healthcare merger expanded the geographic base; the October 2024 merger into a larger West Midlands MH provider configuration will reset the line in 2025-26 reporting. The trust dealt with multiple billing authorities (Stafford BC, Stoke, Shropshire Council, Telford & Wrekin), each levying separately. The Non-Domestic Rating Act 2024 shifted multiplier uprating to CPI from April 2024.",
        "sources": [
            {"publisher": "Midlands Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mpft.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "2023 non-domestic rating list", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "MHCLG", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/13/contents"},
            {"publisher": "Care Quality Commission", "title": "MPFT provider profile (RRE)", "url": "https://www.cqc.org.uk/provider/RRE"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Midlands Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Lease expenditure — Midlands Partnership NHS Foundation Trust", "Amortisation — Midlands Partnership NHS Foundation Trust"]
    },
    "Impairments net of reversals — South London and Maudsley NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "South London and Maudsley NHS Foundation Trust"}],
        "description": "SLAM's £2.14M 2024-25 impairment reflects MEA-DRC revaluation losses across the Maudsley Hospital (Camberwell, mixed Victorian/post-war fabric), Bethlem Royal Hospital (Beckenham), Lambeth Hospital (Landor Road) and Ladywell Lewisham MH unit. The Lambeth Hospital site is on the disposal pathway under SLAM's estates strategy with services migrating to a planned new MH inpatient hub; carrying-value review on Lambeth's ageing fabric drives a material share of the line. Specialty equipment (Bethlem Royal eating disorders / National Affective Disorders) refresh feeds equipment-line writedowns.",
        "beneficiaries": "Approximately 5,000 staff serving c. 1.3M residents of Lambeth, Southwark, Lewisham and Croydon plus a national tertiary catchment for the National Psychosis Unit, National Affective Disorders Service, and Bethlem Royal eating-disorders unit; gross MH estate c. 90,000 m² across 4 main sites + community.",
        "legal_basis": "IAS 36 Impairment of Assets · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£2.14M"},
            {"label": "5-year impairment trend", "value": "2020-21 c. £4M → 2021-22 c. £3M → 2022-23 c. £2.5M → 2023-24 c. £2.2M → 2024-25 £2.14M"},
            {"label": "Estate gross floor area revalued", "value": "c. 90,000 m² across Maudsley + Bethlem Royal + Lambeth + Ladywell"},
            {"label": "MEA-DRC vs market value driver", "value": "Lambeth Hospital ageing fabric on disposal pathway; Bethlem Royal heritage blocks below MEA"},
            {"label": "RAAC scope", "value": "Not on HSSIB confirmed-RAAC list"},
            {"label": "Lambeth disposal pathway", "value": "Lambeth Hospital site on planned disposal; services migrating to new Douglas Bennett-led inpatient hub"},
            {"label": "Specialty driver", "value": "National Psychosis Unit + Bethlem eating disorders + National Affective Disorders — equipment refresh"},
            {"label": "Valuation cycle phase", "value": "5-yearly full revaluation 2024-25; interim VOA indexation"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + external valuer DHSC central panel"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South East London ICB · IAS 36 / DHSC GAM oversight"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; King's Health Partners (academic health sciences) capital reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-disposal-strategy carrying values · Successor: new MH inpatient hub replacing Lambeth (late 2020s)"}
        ],
        "notes": "SLAM's impairment line is structurally smaller than acute peers because much of the trust's tertiary specialty work is housed in Bethlem Royal's heritage estate which is already revalued to a low MEA basis, and the Maudsley's mixed Victorian/post-war fabric has been progressively refurbished. The 2024-25 charge is driven primarily by the Lambeth Hospital disposal pathway — services are migrating away under SLAM's estates strategy, and auditors required carrying-value review of fabric on a wind-down basis. The new replacement inpatient hub (Douglas Bennett-led scheme, late 2020s) sits outside this line. Equipment refresh on national specialty services contributes a smaller equipment-impairment share.",
        "sources": [
            {"publisher": "South London and Maudsley NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://slam.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "NHS provider finance and operational performance 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Care Quality Commission", "title": "SLAM provider profile (RV5)", "url": "https://www.cqc.org.uk/provider/RV5"},
            {"publisher": "South East London ICB", "title": "SEL ICS estates strategy", "url": "https://www.selondonics.org/"}
        ],
        "related": ["South London and Maudsley NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — South London and Maudsley NHS Foundation Trust", "Transport (business + patient) — South London and Maudsley NHS Foundation Trust"]
    },
    "Establishment costs — Rotherham Doncaster and South Humber NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Rotherham Doncaster and South Humber NHS Foundation Trust"}],
        "description": "RDaSH's £2.12M 2024-25 establishment costs cover postage, telephony, mobile devices, courier, training fees, professional subscriptions and statutory levies (CQC, ICO) across MH inpatient wards, learning-disability units, CAMHS Tier 4 and community sites in Rotherham, Doncaster and North Lincolnshire. The trust spans two ICSs (South Yorkshire + Humber & North Yorkshire) which complicates licensing aggregation. Pandemic-era agile rollout left a material mobile-device fleet under N365 NHS-wide licensing.",
        "beneficiaries": "Approximately 3,800 staff across c. 25 inpatient wards (MH + LD + CAMHS Tier 4) and 90+ community / CMHT / IAPT bases serving c. 1.0M residents of Rotherham, Doncaster and North Lincolnshire; mobile-device estate c. 3,500 smartphones and laptops.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.12M"},
            {"label": "Telephony + mobile share", "value": "c. 30–35% of line — c. 3,500 mobile devices on N365 / NHS Mail"},
            {"label": "CQC + ICO statutory fees", "value": "c. £140k combined annual statutory levies"},
            {"label": "Cross-ICS feature", "value": "Footprint spans South Yorkshire ICB + Humber and North Yorkshire ICB — separate digital strategies"},
            {"label": "Training + subscriptions share", "value": "c. 25% of line — mandatory training, professional registration, CPD"},
            {"label": "Site count served", "value": "c. 25 inpatient wards + 90+ community bases across 3 boroughs"},
            {"label": "Delivery body", "value": "Trust corporate services + N365 NHS-wide licensing + Crown Commercial frameworks"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation + ICO / CQC fee-setting"},
            {"label": "Funding trajectory", "value": "Plateau 2023-24 to 2024-25 after pandemic agile step-up"},
            {"label": "Beneficiary count", "value": "c. 1.0M catchment; c. 5,500 active caseload"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; SY ICS digital strategy; HNY ICS digital strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-pandemic establishment baseline · Successor: cross-ICS shared back-office under exploration"}
        ],
        "notes": "RDaSH's establishment line carries a structural cross-ICS feature: the trust operates across South Yorkshire ICB (Rotherham + Doncaster) and Humber & North Yorkshire ICB (North Lincolnshire), each with separate digital strategies and licensing frameworks, which raises duplication on training subscriptions and limits aggregation gains. Pandemic-era agile rollout lifted mobile-device count materially; the c. 4-year refresh cycle keeps the line at plateau. Statutory fees (CQC, ICO) and mandatory training are non-discretionary. The trust's CAMHS Tier 4 provision adds professional-subscription depth (eating-disorder networks, CAMHS national fora) to the line.",
        "sources": [
            {"publisher": "Rotherham Doncaster and South Humber NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rdash.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "RDaSH provider profile (RXE)", "url": "https://www.cqc.org.uk/provider/RXE"},
            {"publisher": "NHS England", "title": "N365 NHS-wide Microsoft licensing", "url": "https://digital.nhs.uk/services/nhsmail"},
            {"publisher": "South Yorkshire ICB", "title": "South Yorkshire ICS digital strategy", "url": "https://syics.co.uk/"}
        ],
        "related": ["Rotherham Doncaster and South Humber NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "General supplies & services — Rotherham Doncaster and South Humber NHS Foundation Trust", "Transport (business + patient) — Rotherham Doncaster and South Humber NHS Foundation Trust"]
    },
    "Transport (business + patient) — Birmingham and Solihull Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Birmingham and Solihull Mental Health NHS Foundation Trust"}],
        "description": "BSMHFT's £2.11M 2024-25 transport line covers business mileage reimbursements (community-MH, AMHP visits, home-treatment teams, perinatal and forensic outreach), staff travel between Reaside Clinic, Ardenleigh, Tamarind Centre, Oleaster and the c. 60 community sites, plus patient transport for inpatient admissions, secure transfers and OAP returns. Birmingham's Clean Air Zone (CAZ, in force from June 2021 — Class D city centre) raised compliant-vehicle premium and accelerated lease-fleet electrification.",
        "beneficiaries": "Approximately 4,200 staff serving c. 1.4M residents of Birmingham and Solihull; mileage claimed across c. 8 main inpatient sites + 60+ community / CMHT / IAPT bases; the trust runs the Reaside medium-secure unit and Ardenleigh CAMHS secure unit which generate cross-region patient transport.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions (mileage rates) · Mental Health Act 1983 (s.140 conveyance)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.11M"},
            {"label": "AfC mileage rates 2024-25", "value": "59p/mile first 3,500; 24p/mile thereafter"},
            {"label": "Birmingham CAZ exposure", "value": "Class D zone live since June 2021 — accelerated lease-fleet electrification, compliant-vehicle premium"},
            {"label": "Patient transport share", "value": "OAP returns + s.136 conveyance + secure transfers — c. 30% of line (Reaside + Ardenleigh secure flow)"},
            {"label": "Forensic outreach", "value": "Reaside medium-secure + Ardenleigh CAMHS secure generate cross-region transport (national catchment)"},
            {"label": "Site count served", "value": "c. 8 inpatient sites + 60+ community / CMHT / IAPT bases"},
            {"label": "Delivery body", "value": "Trust fleet + WMAS / G4S patient-transport contracts + AfC mileage scheme"},
            {"label": "Policy owner", "value": "DHSC + NHSE + Birmingham and Solihull ICB + Birmingham CC (CAZ)"},
            {"label": "Funding trajectory", "value": "Step-up post-2021 CAZ; CPI inflation; OAP volumes pressure"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; NHSE OAP reduction programme; Birmingham CC CAZ impact reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-CAZ fleet · Successor: zero-emission fleet conversion + Ardenleigh CAMHS national flow review"}
        ],
        "notes": "BSMHFT's transport line is shaped by Birmingham's Class D Clean Air Zone (in force since June 2021, the largest Category D CAZ in England), which materially raised the compliant-vehicle premium across the trust's lease-fleet and accelerated electrification. The Reaside Clinic medium-secure unit and Ardenleigh CAMHS secure unit generate national-catchment patient transport (cross-region admissions and discharge transfers). Persistent OAP volumes from BSMHFT's general adult inpatient pressure feed return-transport cost. The s.136 pathway with West Midlands Police under Right Care Right Person rollout is reshaping the patient-transport mix.",
        "sources": [
            {"publisher": "Birmingham and Solihull Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bsmhft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Staff Council", "title": "AfC mileage rates 2024-25", "url": "https://www.nhsemployers.org/publications/agenda-change-mileage-allowances"},
            {"publisher": "Birmingham City Council", "title": "Clean Air Zone (Class D) Birmingham", "url": "https://www.brumbreathes.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "BSMHFT provider profile (RXT)", "url": "https://www.cqc.org.uk/provider/RXT"}
        ],
        "related": ["Birmingham and Solihull Mental Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Amortisation — Birmingham and Solihull Mental Health NHS Foundation Trust", "Business rates — Birmingham and Solihull Mental Health NHS Foundation Trust"]
    },
    "PFI / LIFT charges — Essex Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Essex Partnership University NHS Foundation Trust"}],
        "description": "EPUT's £2.11M 2024-25 PFI / LIFT charges line covers unitary charge service-element payments and LIFT (Local Improvement Finance Trust) lease-equivalents on community-MH primary-care premises across Essex. The trust inherited PFI/LIFT obligations from its predecessor MH and community trusts (North Essex Partnership and South Essex Partnership pre-2017 merger) plus subsequent NEPT-side LIFT primary-care commitments. Unitary charges are split under DHSC GAM ch.7 between IFRS 16 right-of-use depreciation, finance-charge interest and the service element booked here.",
        "beneficiaries": "Approximately 5,500 staff using c. 80 inpatient wards and 200+ community sites covering c. 3.5M residents of Essex, Bedfordshire, Luton and parts of Suffolk; PFI / LIFT footprint covers approximately 12–18 community-MH primary-care bases under LIFT (Essex Local Improvement Finance Trust company structure).",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Private Finance) Act 1997 · Local Improvement Finance Trust regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.11M"},
            {"label": "Charge composition", "value": "Service element (FM, hard FM, soft FM) — capital + interest reported separately under IFRS 16 split"},
            {"label": "LIFT footprint", "value": "c. 12–18 community-MH primary-care bases under Essex LIFT structure"},
            {"label": "Unitary charge index", "value": "RPI-linked under original LIFT contracts (some renegotiated to CPI)"},
            {"label": "Hand-back horizon", "value": "Most LIFT schemes 25-year contracts originating 2004-2010 — hand-back 2029-2035"},
            {"label": "Delivery body", "value": "Essex LIFT company (private-sector-led PPP) + EPUT estates + DHSC GAM oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (PFI / LIFT mandate) + NHSE Provider Finance"},
            {"label": "Beneficiary count", "value": "c. 12,500 active service users; c. 3.5M catchment population"},
            {"label": "Funding trajectory", "value": "RPI/CPI uplift annual; service element broadly flat real-terms"},
            {"label": "Evaluation evidence", "value": "NAO PFI / PF2 hand-back reports; Lampard Inquiry; CQC 'Requires Improvement' 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 NEPT + SEPT separate PFI / LIFT lines · Successor: hand-back 2029-2035 + freehold reversion"}
        ],
        "notes": "EPUT's PFI / LIFT line is dominated by LIFT (Local Improvement Finance Trust) primary-care premises rather than acute PFI — LIFT was the Labour-era primary-care PPP vehicle and Essex has a substantial LIFT footprint hosting community-MH and IAPT-equivalent services. Most LIFT contracts run 25 years from 2004-2010, putting hand-back in 2029-2035 territory; auditors are increasingly scrutinising hand-back-condition reserves. Unitary-charge indexation has been RPI-linked under most original contracts, although some have been renegotiated to CPI following the 2030 RPI alignment policy. The service element booked here covers hard and soft FM; capital + interest are reported separately under the IFRS 16 split.",
        "sources": [
            {"publisher": "Essex Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://eput.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and contracts (2020 + 2023 update)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT programme oversight", "url": "https://communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "EPUT provider profile (RHA)", "url": "https://www.cqc.org.uk/provider/RHA"}
        ],
        "related": ["Essex Partnership University NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Lease expenditure — Essex Partnership University NHS Foundation Trust", "Amortisation — Essex Partnership University NHS Foundation Trust"]
    },
    "Establishment costs — Camden and Islington NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Camden and Islington NHS Foundation Trust"}],
        "description": "C&I's £2.09M 2024-25 establishment costs cover postage, telephony, mobile devices, courier, training fees, professional subscriptions and statutory levies (CQC, ICO) across the trust's MH inpatient and community estate covering Camden and Islington (NCL ICB). The trust is in a strategic merger pathway with Barnet, Enfield and Haringey MHT into a single North London MH provider configuration; establishment costs reflect transition-phase duplication and integration planning. The St Pancras Hospital site is being redeveloped under the Highgate Mental Health Centre Phase 2 strategy.",
        "beneficiaries": "Approximately 2,800 staff serving c. 600,000 residents of Camden and Islington; mobile-device estate c. 2,800 smartphones and laptops; site count covers Highgate MH Centre, St Pancras Hospital (transitional) and c. 30 community / CMHT / IAPT bases.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.09M"},
            {"label": "Telephony + mobile share", "value": "c. 30–35% of line — c. 2,800 mobile devices on N365 / NHS Mail"},
            {"label": "Merger transition", "value": "Strategic merger with BEH-MHT into North London MH single provider — transition-phase duplication"},
            {"label": "CQC + ICO statutory fees", "value": "c. £130k combined annual statutory levies"},
            {"label": "Site count served", "value": "c. 4 main inpatient sites + 30+ community bases"},
            {"label": "St Pancras redevelopment", "value": "Site being redeveloped — Highgate MH Centre Phase 2 strategy reshaping inpatient footprint"},
            {"label": "Delivery body", "value": "Trust corporate services + N365 NHS-wide licensing + Crown Commercial frameworks"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation + NCL ICB + ICO / CQC fee-setting"},
            {"label": "Funding trajectory", "value": "Plateau 2023-24 to 2024-25; merger-driven step-down expected post-integration"},
            {"label": "Beneficiary count", "value": "c. 600,000 catchment; c. 4,500 active caseload"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; NCL ICB MH plan; NHSE provider configuration assurance"},
            {"label": "Predecessor / successor", "value": "Predecessor: standalone C&I FT establishment line · Successor: merged North London MH provider establishment line"}
        ],
        "notes": "C&I's establishment line is shaped by the strategic merger pathway with Barnet, Enfield and Haringey MHT into a single North London MH provider configuration. During transition, duplication of mobile-device fleets, training subscriptions and statutory registrations keeps the line at plateau rather than declining; integration is expected to compress establishment cost over 2025-27. The St Pancras Hospital site redevelopment under the Highgate MH Centre Phase 2 strategy is reshaping the inpatient footprint and during transition raises courier and inter-site postage cost. Statutory fees (CQC, ICO) and mandatory training are non-discretionary; the discretionary share is concentrated in courier, stationery and professional subscriptions.",
        "sources": [
            {"publisher": "Camden and Islington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.candi.nhs.uk/about-us/who-we-are/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "C&I provider profile (RWK)", "url": "https://www.cqc.org.uk/provider/RWK"},
            {"publisher": "NHS England", "title": "N365 NHS-wide Microsoft licensing", "url": "https://digital.nhs.uk/services/nhsmail"},
            {"publisher": "North Central London ICB", "title": "NCL ICS mental-health configuration", "url": "https://nclhealthandcare.org.uk/"}
        ],
        "related": ["Camden and Islington NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Camden and Islington NHS Foundation Trust", "Transport (business + patient) — Camden and Islington NHS Foundation Trust"]
    },
    "Business rates — Nottinghamshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Nottinghamshire Healthcare NHS Foundation Trust"}],
        "description": "Notts Healthcare's £2.04M 2024-25 business-rates charge reflects VOA-set rateable values across MH, learning-disability, forensic and community-physical-health sites in Nottinghamshire — most consequentially Rampton Hospital (high-secure forensic, Retford), Highbury Hospital (Bulwell), Wells Road Centre, Hopewood and c. 90 community bases. Rampton's high-secure footprint is the single largest hereditament. NHS FTs are rated as 'Other' under LGFA 1988 Schedule 6 with no charitable exemption; standard 49.9p/54.6p UBR multipliers apply.",
        "beneficiaries": "Approximately 9,000 staff across c. 50 inpatient wards (MH + LD + forensic + secure CAMHS) plus 90+ community sites serving c. 1.0M residents of Nottinghamshire and a national high-secure catchment via Rampton; c. 12,000 active service users on caseload.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022 · Criminal Justice Act 2003 (high-secure remit)",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.04M"},
            {"label": "Rampton share", "value": "Estimated > 30% of line — high-secure footprint billed by Bassetlaw DC"},
            {"label": "UBR multiplier 2024-25", "value": "49.9p (small business rate); 54.6p (standard) — applied per hereditament threshold"},
            {"label": "Antecedent valuation date", "value": "1 April 2021 (2023 revaluation list)"},
            {"label": "Estimated rateable value base", "value": "c. £4.1M aggregate RV implied by £2.04M charge"},
            {"label": "Hereditament count", "value": "c. 100+ across MH + LD + forensic + community-physical-health footprint"},
            {"label": "Charitable exemption", "value": "Not applied — NHS FTs rated as 'Other'"},
            {"label": "Major sites", "value": "Rampton (Retford); Highbury (Bulwell); Wells Road Centre Mapperley; Hopewood; community bases countywide"},
            {"label": "Delivery body", "value": "VOA + Bassetlaw DC + Nottingham CC + Nottinghamshire CC billing authorities"},
            {"label": "Policy owner", "value": "MHCLG / DLUHC + HM Treasury (multiplier)"},
            {"label": "Funding trajectory", "value": "2023 revaluation step; CPI-linked from 2024-25; Valdo Calocane case scrutiny may reshape capital plans"},
            {"label": "Evaluation evidence", "value": "Independent investigation into Valdo Calocane care 2024; CQC reviews; HMP-equivalent NAO scrutiny of high-secure"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 list pre-Calocane review · Successor: 2026 revaluation cycle + post-Calocane capital response"}
        ],
        "notes": "Notts Healthcare's business-rates line is structurally weighted by Rampton Hospital — one of the three English high-secure hospitals (with Broadmoor and Ashworth) — billed by Bassetlaw DC and carrying a substantial standalone rateable value. The integrated MH + community + forensic footprint generates a high hereditament count (c. 100+) across multiple billing authorities. The independent investigation into the care of Valdo Calocane (2024 NHSE-commissioned review following the Nottingham attacks) sharpened scrutiny of community-MH and forensic capacity; capital plans being reshaped may shift the rateable base in 2025-26. The Non-Domestic Rating Act 2024 shifted multiplier uprating to CPI from April 2024.",
        "sources": [
            {"publisher": "Nottinghamshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nottinghamshirehealthcare.nhs.uk/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "2023 non-domestic rating list", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "MHCLG", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/13/contents"},
            {"publisher": "Care Quality Commission", "title": "Notts Healthcare provider profile (RHA / RHATL)", "url": "https://www.cqc.org.uk/provider/RHA"},
            {"publisher": "NHS England", "title": "Independent investigation into the care of Valdo Calocane", "url": "https://www.england.nhs.uk/long-read/independent-investigation-care-and-treatment-valdo-calocane/"}
        ],
        "related": ["Nottinghamshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Termination & post-employment — Nottinghamshire Healthcare NHS Foundation Trust", "Amortisation — Nottinghamshire Healthcare NHS Foundation Trust"]
    },
}
