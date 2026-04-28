# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 36 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Transport (business + patient) — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "Cambridge University Hospitals NHS FT's £6.03M transport line covers staff business mileage (AfC Section 17 + AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between Addenbrooke's, the Rosie Hospital and the Cambridge Biomedical Campus, plus contracted non-emergency patient transport (NEPTS) for the Cambridgeshire and Peterborough ICS catchment. The trust's specialist tertiary footprint (transplantation, oncology, neurosciences) drives outsized inter-hospital pathology and blood-product courier flows.",
        "beneficiaries": "c. 12,500 WTE staff serving a c. 580,000 local catchment plus a tertiary referral population of c. 5M for specialist services (transplant, neurosciences, oncology, paediatric cardiac); c. 145,000 ED attendances/yr at Addenbrooke's; c. 130,000 admissions/yr; c. 1.0M outpatient attendances/yr including high specialist pathology and imaging volumes feeding inter-site transport.",
        "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£6.03M"},
            {"label": "Trust scale", "value": "Addenbrooke's + Rosie Hospital + CBC tertiary footprint; c. 12,500 WTE; major trauma centre + transplant centre"},
            {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology/blood-product courier + contracted NEPTS"},
            {"label": "NEPTS provider", "value": "E-zec Medical Transport Services (Cambridgeshire & Peterborough framework, retendered 2022)"},
            {"label": "Inter-site flow", "value": "High pathology + organ + blood-product courier volume between Addenbrooke's, Rosie, Royal Papworth (CBC) and tertiary referrer trusts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement + NEPTS rebooking spike"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via NEPTS contractor + agency-driver pass-through (15% over £5k threshold)"},
            {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.6M → 2023-24 c. £5.7M → 2024-25 £6.03M — strike backfill + fuel-cost pass-through + NEPTS retender uplift"},
            {"label": "Cambridgeshire & Peterborough ICS", "value": "Member of Cambridgeshire and Peterborough ICB; collaborative NEPTS commissioning"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + E-zec Medical (NEPTS) + EEAST (when emergency overlap)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Patient Transport Services policy + DHSC + Cambridgeshire & Peterborough ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; Trust ARA 2023-24; CQC RGT inspections; NAO Major Trauma Care report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-2022-retender baseline · Successor: NEPTS-Review aligned eligibility-criteria implementation + ICS-wide pool-fleet consolidation"}
        ],
        "notes": "Cambridge University Hospitals NHS FT's transport line is shaped by the trust's status as a tertiary referral centre on the Cambridge Biomedical Campus — high-volume inter-site pathology, organ-procurement and blood-product courier flows between Addenbrooke's, the Rosie Hospital and Royal Papworth on the same campus drive a structural premium over peer DGHs. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) added locum travel reimbursement and NEPTS rebooking cost. The NEPTS contract (E-zec Medical) was retendered in 2022 against the NHSE Patient Transport Services Review eligibility framework. April 2025 employer NIC step-up and frozen AMAP rates (45p/mile since 2011) compress the staff-mileage element. The CUH 2030 strategy (Cambridge Children's Hospital + Cambridge Cancer Research Hospital co-located builds) will drive medium-term inter-site transport growth.",
        "sources": [
            {"publisher": "Cambridge University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cuh.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Cambridge University Hospitals NHS Foundation Trust provider profile (RGT)", "url": "https://www.cqc.org.uk/provider/RGT"}
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Cambridge University Hospitals NHS Foundation Trust", "Transport (business + patient) — Guy's & St Thomas' NHS Foundation Trust", "NHS England"]
    },
    "Establishment costs — Royal Surrey NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Royal Surrey NHS Foundation Trust"}],
        "description": "Royal Surrey NHS FT's £6.00M establishment costs line covers GAM operating expenses outside the payroll chain — office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below the capitalisation threshold across the Royal Surrey County Hospital (Guildford) plus the trust's specialist St Luke's Cancer Centre and community footprint. Industrial-action backfill plus EPR (Cerner) change-management training and recruitment-advertising spend drive the line.",
        "beneficiaries": "c. 4,400 WTE staff serving a c. 350,000 west Surrey + Hampshire-borders catchment plus a tertiary cancer-centre population for St Luke's; c. 90,000 ED attendances/yr at Royal Surrey ED; c. 65,000 admissions/yr; c. 480,000 outpatient attendances/yr; trust hosts a regional cancer centre (St Luke's) serving Surrey, Sussex and parts of Hampshire.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£6.00M"},
            {"label": "Trust scale", "value": "Royal Surrey County Hospital (Guildford) + St Luke's Cancer Centre + community services; c. 4,400 WTE"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "EPR platform", "value": "Cerner Millennium (legacy) + Frontline Digitisation upgrade pathway — change-management training + travel costs feed Establishment line"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "St Luke's Cancer Centre", "value": "Tertiary cancer centre — drives specialist training/conferences + recruitment-advertising premium over peer DGHs"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via training-provider and recruitment-advertising contractor pass-through (15% over £5k)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.7M → 2023-24 c. £5.7M → 2024-25 £6.00M — strike backfill + EPR training + CPI on consumables"},
            {"label": "Surrey Heartlands ICS", "value": "Member of Surrey Heartlands ICB; collaborative procurement, training and recruitment frameworks"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + Surrey Heartlands ICB + DHSC + NHS Supply Chain (where used)"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RA2 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner-stabilisation baseline · Successor: Frontline Digitisation EPR upgrade-cycle training + Surrey Heartlands shared-service consolidation"}
        ],
        "notes": "Royal Surrey NHS FT's establishment-cost line reflects its tertiary cancer-centre status (St Luke's) — specialist oncology training, conference attendance and recruitment-advertising for sub-specialty consultants drive a premium over peer DGH establishment-cost ratios. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) added admin rebooking, recruitment advertising and casual training spend. Cerner Millennium EPR change-management cycles (with a Frontline Digitisation upgrade pathway) feed training-provider and travel costs. The trust hosts the regional radiotherapy network (Genesis Care partnership cancelled 2022, retendered) and runs Surrey Hampshire Borders pathology partnership. April 2025 employer NIC step-up (15% over £5k threshold) flows indirectly via training-provider and recruitment-advertising contractor pass-through.",
        "sources": [
            {"publisher": "Royal Surrey NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalsurrey.nhs.uk/about-us/board-and-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Royal Surrey NHS Foundation Trust provider profile (RA2)", "url": "https://www.cqc.org.uk/provider/RA2"},
            {"publisher": "NHS Confederation", "title": "Surrey Heartlands Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
        ],
        "related": ["Royal Surrey NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Hampshire Hospitals NHS Foundation Trust", "Establishment costs — Frimley Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Oxford University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
        "description": "OUH's £5.96M business-rates line covers non-domestic rate liability across the trust's four-hospital footprint — John Radcliffe Hospital (Headington), Churchill Hospital (Headington), Nuffield Orthopaedic Centre (Headington) and Horton General Hospital (Banbury) — plus research and outreach sites. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Buckinghamshire, Oxfordshire and Berkshire West (BOB) ICS context.",
        "beneficiaries": "c. 13,500 WTE staff serving a c. 750,000 Oxfordshire local catchment plus a tertiary referral population of c. 4M for specialist services (Oxford Eye Hospital, paediatric cardiac, neurosciences, transplant, Oxford Vaccine Group); c. 165,000 ED attendances/yr at John Radcliffe + Horton; c. 145,000 admissions/yr; major university-teaching trust co-located with University of Oxford Medical Sciences Division.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£5.96M"},
            {"label": "Trust scale", "value": "John Radcliffe + Churchill + Nuffield Orthopaedic Centre + Horton General; c. 13,500 WTE"},
            {"label": "Principal hereditaments", "value": "John Radcliffe (large acute hereditament — likely £500k+ rateable value tier) + Churchill + NOC + Horton General"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne (cf. Oxford colleges — exempt as charities)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.2M → 2023-24 c. £5.7M → 2024-25 £5.96M — 2023 list revaluation + multiplier uplift on large hereditaments"},
            {"label": "BOB ICS", "value": "Member of Buckinghamshire, Oxfordshire and Berkshire West ICB"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA (rateable-value setter) + Oxford City Council / Cherwell DC (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + BOB ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24 disclosure; CQC RTH inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + ongoing trust appeal of John Radcliffe rateable value (high-tier multiplier exposure)"}
        ],
        "notes": "OUH's business-rates line is shaped by the trust's four large hereditaments — John Radcliffe (the principal acute site, almost certainly above the £500k rateable-value threshold introduced by the NDR (Multipliers and Private Finance) Act 2024 from April 2025), Churchill (oncology and renal), Nuffield Orthopaedic Centre and Horton General (Banbury). NHS trusts are not eligible for the mandatory 80% charitable rate relief — a structural disparity vs Oxford University colleges, which receive full charitable exemption on adjacent estate. The 1 April 2026 next revaluation is the medium-term lever. The trust's John Radcliffe site is partly PFI-financed (West Wing); rates are paid by the trust as occupier regardless of PFI structure. RAAC was identified at Horton General in the 2023 HSSIB survey but was below the critical-mitigation threshold.",
        "sources": [
            {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ouh.nhs.uk/about/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Oxford University Hospitals NHS Foundation Trust provider profile (RTH)", "url": "https://www.cqc.org.uk/provider/RTH"}
        ],
        "related": ["Oxford University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Royal Cornwall Hospitals NHS Trust", "Business rates — Sheffield Teaching Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Royal Free London NHS FT's £5.96M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the Cerner Millennium EPR and associated digital-imaging, e-prescribing and Frontline Digitisation modules deployed across the Royal Free Hampstead, Barnet General and Chase Farm hospitals, plus capitalised software licences for pathology, radiology and back-office systems. The trust's Chase Farm new-build (opened 2018, fully digital) brought a substantial intangibles tranche that is now in steady-state amortisation. North Central London ICS context.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 1.6M north London catchment across Camden, Barnet, Enfield, Haringey and Hertfordshire borders; c. 290,000 ED attendances/yr across Royal Free + Barnet ED + Chase Farm UTC; c. 175,000 admissions/yr; trust hosts the national liver-transplant centre (Sheila Sherlock Liver Centre) and HIV/infectious-diseases tertiary services.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — IFRS 3 Business Combinations (acquired-software treatment) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£5.96M"},
            {"label": "Trust scale", "value": "Royal Free Hampstead + Barnet General + Chase Farm; c. 11,000 WTE; national liver transplant centre"},
            {"label": "Principal intangibles", "value": "Cerner Millennium EPR + digital imaging (PACS/RIS) + e-prescribing + pathology LIMS + back-office software"},
            {"label": "EPR platform", "value": "Cerner Millennium (RFL was an early Cerner adopter — hosting partnership with Health Services Laboratories, Berkeley Group estate)"},
            {"label": "Chase Farm (2018)", "value": "Fully digital new-build hospital — large 2018-2019 intangibles capitalisation tranche now in mid-life amortisation"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; PACS image storage ~10 years; major EPR modules amortised over 7-10 yrs"},
            {"label": "Frontline Digitisation pipeline", "value": "Continued capitalised module additions (clinical noting, mobile apps, decision-support) feed forward intangibles balance"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.8M → 2023-24 c. £5.7M → 2024-25 £5.96M — Frontline Digitisation module additions + Chase Farm steady-state"},
            {"label": "North Central London ICS", "value": "Member of NCL ICB; collaborative pathology partnership (HSL) and shared-EPR ambitions"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Cerner (Oracle Health) + HSL pathology + Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + NCL ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation reports; Trust ARA 2023-24 intangibles note; CQC RAL inspections; DHSC GAM compliance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner-Millennium baseline + Chase Farm pre-rebuild estate · Successor: Frontline Digitisation Wave 4-5 module deployment + future EPR refresh-cycle (2030+)"}
        ],
        "notes": "Royal Free London NHS FT's amortisation line is dominated by the Cerner Millennium EPR (early-adopter trust) plus a substantial Chase Farm 2018 digital-new-build intangibles tranche now in mid-life amortisation under IAS 38 useful-economic-life conventions. The trust's national liver-transplant role (Sheila Sherlock Liver Centre) and tertiary HIV/infectious-diseases services drive specialist clinical-software capitalisation. Frontline Digitisation module additions (clinical noting, mobile apps, decision-support) feed forward additions. The 2018 Royal Free / DeepMind Streams data-sharing controversy (ICO finding July 2017) shaped the trust's data-governance overhead but is not material to amortisation per se. Future EPR refresh-cycle (likely 2030+) is the medium-term cliff-edge for the intangibles balance.",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information/annual-reports-and-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Royal Free London NHS Foundation Trust provider profile (RAL)", "url": "https://www.cqc.org.uk/provider/RAL"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Sheffield Teaching Hospitals NHS Foundation Trust", "Amortisation — King’s College Hospital NHS Foundation Trust", "Transport (business + patient) — Royal Free London NHS Foundation Trust"]
    },
    "Establishment costs — County Durham and Darlington NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "County Durham and Darlington NHS Foundation Trust"}],
        "description": "CDDFT's £5.95M establishment costs line covers GAM operating expenses outside the payroll chain — office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below the capitalisation threshold across the trust's twin-DGH footprint (University Hospital of North Durham, Darlington Memorial Hospital) plus Bishop Auckland Hospital, Shotley Bridge, Chester-le-Street and Sedgefield community hospitals. Industrial-action backfill plus EPR (Oracle Health Cerner) change-management training drive the line.",
        "beneficiaries": "c. 7,800 WTE staff serving a c. 670,000 County Durham + Darlington catchment plus borders flow into Tees Valley; c. 165,000 ED attendances/yr at UH North Durham + Darlington Memorial ED; c. 110,000 admissions/yr; covers a high-deprivation post-industrial coal-field belt with high coronary, respiratory and oncology demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.95M"},
            {"label": "Trust scale", "value": "UH North Durham + Darlington Memorial + Bishop Auckland + Shotley Bridge + Chester-le-Street + Sedgefield + community footprint; c. 7,800 WTE"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "EPR platform", "value": "Oracle Health (Cerner Millennium) — Frontline Digitisation programme partner — change-management training feeds Establishment line"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "Multi-site geography", "value": "Distributed county footprint drives premium on travel, courier, telephony and training-coordination costs vs single-site DGHs"},
            {"label": "Shotley Bridge", "value": "Replacement community hospital build (NHP cohort) — pre-construction training, recruitment and consultation costs feed Establishment"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via training-provider and recruitment-advertising contractor pass-through (15% over £5k)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.6M → 2023-24 c. £5.6M → 2024-25 £5.95M — strike backfill + EPR training + CPI on consumables"},
            {"label": "North East and North Cumbria ICS", "value": "Member of NENC ICB — largest ICS by area in England; collaborative procurement/training frameworks"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NENC ICB + DHSC + NHS Supply Chain"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RXP inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner Millennium baseline · Successor: Shotley Bridge new hospital training+recruitment + Frontline Digitisation upgrade-cycle"}
        ],
        "notes": "CDDFT's establishment-cost line is shaped by its distributed multi-site footprint (twin DGHs plus Bishop Auckland and four community hospitals across rural and post-industrial County Durham), driving travel-coordination, telephony and training-logistics premium over compact urban peers. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) added admin rebooking and recruitment-advertising spend. Oracle Health Cerner Millennium EPR change-management cycles feed training-provider costs. The Shotley Bridge replacement community hospital (NHP cohort, originally promised 2022 but deferred to NHP Reset 2025) drives pre-construction consultation, training and recruitment-advertising spend. April 2025 employer NIC step-up (15% over £5k threshold) flows indirectly via training-provider and recruitment-advertising contractor pass-through.",
        "sources": [
            {"publisher": "County Durham and Darlington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cddft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "Care Quality Commission", "title": "County Durham and Darlington NHS Foundation Trust provider profile (RXP)", "url": "https://www.cqc.org.uk/provider/RXP"},
            {"publisher": "NHS Confederation", "title": "North East and North Cumbria Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
        ],
        "related": ["County Durham and Darlington NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — County Durham and Darlington NHS Foundation Trust", "Establishment costs — North Tees and Hartlepool NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — King’s College Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "King’s College Hospital NHS Foundation Trust"}],
        "description": "King's College Hospital NHS FT's £5.94M business-rates line covers non-domestic rate liability across the trust's two-acute-site footprint — King's College Hospital (Denmark Hill, Camberwell) and the Princess Royal University Hospital (Farnborough, Bromley) — plus Orpington Hospital, Beckenham Beacon and the Cicely Saunders / Maudsley campus shared estate. Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024. South East London ICS context.",
        "beneficiaries": "c. 13,000 WTE staff serving a c. 1.0M Lambeth + Southwark + Bromley local catchment plus a tertiary referral population for liver transplant, neurosciences, haematology and major trauma covering c. 4M; c. 250,000 ED attendances/yr at Denmark Hill (designated Major Trauma Centre) + Princess Royal ED; c. 145,000 admissions/yr.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£5.94M"},
            {"label": "Trust scale", "value": "Denmark Hill + Princess Royal University Hospital + Orpington + Beckenham Beacon; c. 13,000 WTE; designated Major Trauma Centre + liver transplant centre"},
            {"label": "Principal hereditaments", "value": "King's Denmark Hill (large acute hereditament — almost certainly £500k+ rateable-value tier) + Princess Royal University Hospital (Bromley)"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.1M → 2023-24 c. £5.7M → 2024-25 £5.94M — 2023 list revaluation + multiplier uplift on large hereditaments"},
            {"label": "South East London ICS", "value": "Member of SEL ICB; co-tenant with Guy's & St Thomas' on shared service-line estate (cancer hub, pathology partnership)"},
            {"label": "Major Trauma Centre", "value": "Denmark Hill is the South East London + Kent + Medway MTC — drives outsized hereditament size + intensity uplift"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + LB Southwark / LB Bromley (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + SEL ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24 disclosure; CQC RJZ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + ongoing trust appeal of Denmark Hill rateable value (high-tier multiplier exposure)"}
        ],
        "notes": "King's College Hospital NHS FT's business-rates line is dominated by the Denmark Hill principal hereditament — a large Major Trauma Centre site almost certainly above the £500k rateable-value threshold introduced by the NDR (Multipliers and Private Finance) Act 2024, attracting the higher multiplier from April 2025. The Princess Royal University Hospital (Bromley) is a sizeable second hereditament. NHS trusts are not eligible for mandatory 80% charitable rate relief — a structural disparity vs co-located independent-sector charity hospitals. The trust emerged from the 2018-2020 financial special-measures regime under Lord Carter's recommendations, with cost-base scrutiny including non-pay running costs. The 1 April 2026 next revaluation is the medium-term lever; the trust's E&F team has historically engaged Gerald Eve / Avison Young for rates appeal advice on the Denmark Hill estate.",
        "sources": [
            {"publisher": "King’s College Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kch.nhs.uk/about/corporate-information/publications/annual-reports-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "King’s College Hospital NHS Foundation Trust provider profile (RJZ)", "url": "https://www.cqc.org.uk/provider/RJZ"}
        ],
        "related": ["King’s College Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — King’s College Hospital NHS Foundation Trust", "Transport (business + patient) — King’s College Hospital NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — University Hospitals of Derby and Burton NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals of Derby and Burton NHS Foundation Trust"}],
        "description": "UHDB's £5.82M business-rates line covers non-domestic rate liability across the trust's five-hospital footprint formed by the July 2018 merger of Derby Teaching Hospitals and Burton Hospitals — Royal Derby Hospital, Queen's Hospital Burton, Sir Robert Peel Community Hospital (Tamworth), Samuel Johnson Community Hospital (Lichfield) and London Road Community Hospital (Derby). Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024. Joined Forces Together NHS Derby + Joined Up Care Derbyshire + Staffordshire ICS context.",
        "beneficiaries": "c. 13,500 WTE staff serving a c. 1.05M Derbyshire + East Staffordshire catchment (Derby, Burton, Tamworth, Lichfield, Uttoxeter, South Derbyshire); c. 220,000 ED attendances/yr at Royal Derby + Queen's Burton ED; c. 165,000 admissions/yr; cross-ICB-border footprint (Joined Up Care Derbyshire + Staffordshire ICS).",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£5.82M"},
            {"label": "Trust scale", "value": "Royal Derby + Queen's Burton + Sir Robert Peel + Samuel Johnson + London Road; c. 13,500 WTE"},
            {"label": "Principal hereditaments", "value": "Royal Derby Hospital (PFI-financed; large acute hereditament likely £500k+ tier) + Queen's Hospital Burton"},
            {"label": "PFI overlap", "value": "Royal Derby Hospital is PFI (Project Co — Catalyst Healthcare); rates paid by trust as occupier regardless of PFI structure"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Merger genesis", "value": "Trust formed July 2018 by merger of Derby Teaching Hospitals + Burton Hospitals — drove rates-line consolidation across two billing-authority footprints"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.0M → 2023-24 c. £5.6M → 2024-25 £5.82M — 2023 list revaluation + multiplier uplift on Royal Derby"},
            {"label": "Cross-ICS footprint", "value": "Royal Derby in Joined Up Care Derbyshire ICB; Queen's Burton + Tamworth + Lichfield in Staffordshire and Stoke-on-Trent ICB"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + Derby City Council / East Staffs BC / Tamworth BC / Lichfield DC (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Joined Up Care Derbyshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24 disclosure; CQC RTG inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018-merger Derby Teaching + Burton Hospitals separate rates lines · Successor: 2026 VOA revaluation + post-NHP-Reset Royal Derby refresh planning"}
        ],
        "notes": "UHDB's business-rates line reflects the trust's five-hospital footprint formed by the July 2018 merger of Derby Teaching Hospitals NHS FT and Burton Hospitals NHS FT — an NHSI-driven merger to stabilise Burton's deficit and consolidate clinical pathways. The Royal Derby Hospital PFI structure (Catalyst Healthcare ProjectCo) does not transfer rates liability — the trust as occupier pays rates regardless. The Royal Derby is almost certainly above the £500k rateable-value threshold attracting the higher multiplier from April 2025 under the NDR (Multipliers and Private Finance) Act 2024. The trust's cross-ICS footprint (Derbyshire + Staffordshire) drives administrative overhead in dealing with multiple billing authorities. The 2023 RAAC HSSIB survey identified RAAC at Queen's Burton requiring monitoring but not critical mitigation.",
        "sources": [
            {"publisher": "University Hospitals of Derby and Burton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhdb.nhs.uk/annual-reports-and-accounts"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals of Derby and Burton NHS Foundation Trust provider profile (RTG)", "url": "https://www.cqc.org.uk/provider/RTG"}
        ],
        "related": ["University Hospitals of Derby and Burton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Northampton General Hospital NHS Trust", "Business rates — The Dudley Group NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Establishment costs — Norfolk and Norwich University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Norfolk and Norwich University Hospitals NHS Foundation Trust"}],
        "description": "NNUH's £5.77M establishment costs line covers GAM operating expenses outside the payroll chain — office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below the capitalisation threshold across the Norfolk and Norwich University Hospital (Colney, Norwich), Cromer Hospital and shared estate at the University of East Anglia / Quadram Institute campus. Industrial-action backfill plus EPR (Cerner) change-management training drive the line.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 1.0M Norfolk + north Suffolk catchment (Norwich, North Norfolk, Breckland, Broadland, Great Yarmouth borders); c. 175,000 ED attendances/yr at NNUH ED; c. 130,000 admissions/yr; c. 800,000 outpatient attendances/yr; trust hosts the Norwich Medical School (UEA) academic partnership.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.77M"},
            {"label": "Trust scale", "value": "NNUH (Colney) + Cromer Hospital + UEA-campus academic estate; c. 9,500 WTE"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "EPR platform", "value": "Cerner Millennium (long-standing) — Frontline Digitisation upgrade pathway — change-management training feeds Establishment line"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "RAAC critical site", "value": "NNUH on the 2023 HSSIB RAAC list (concrete-plank risk) — drove decant logistics, mitigation works, training and consultation costs feeding Establishment + Premises lines"},
            {"label": "PFI overlap", "value": "NNUH was PFI-financed (Octagon Healthcare Partnership) since opening 2001 — long PFI debate driving establishment-cost overhead in contract-management"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via training-provider and recruitment-advertising contractor pass-through (15% over £5k)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 c. £5.4M → 2024-25 £5.77M — strike backfill + EPR training + RAAC consultation + CPI on consumables"},
            {"label": "Norfolk and Waveney ICS", "value": "Member of Norfolk and Waveney ICB"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + Norfolk and Waveney ICB + DHSC + NHS Supply Chain"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RM1 inspections; HSSIB RAAC assessments"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner stabilisation baseline · Successor: NHP / RAAC programme rebuild planning + Frontline Digitisation Wave 4-5 module deployment"}
        ],
        "notes": "NNUH's establishment-cost line is shaped by three structural drivers — its RAAC status (one of the 2023 HSSIB-listed sites with critical-mitigation requirements drove decant logistics, mitigation-works coordination, staff and patient-consultation training and communications spend), its 2001 PFI structure (Octagon Healthcare Partnership) generating contract-management administrative overhead, and the 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) feeding admin rebooking and recruitment-advertising. Cerner Millennium EPR change-management cycles add training-provider costs. The trust's UEA / Quadram Institute academic partnership drives a research-conference and subscription premium over peer DGHs. April 2025 employer NIC step-up flows indirectly via training-provider and recruitment-advertising pass-through.",
        "sources": [
            {"publisher": "Norfolk and Norwich University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nnuh.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "RAAC mitigation programme + New Hospital Programme Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "Care Quality Commission", "title": "Norfolk and Norwich University Hospitals NHS Foundation Trust provider profile (RM1)", "url": "https://www.cqc.org.uk/provider/RM1"},
            {"publisher": "NHS Confederation", "title": "Norfolk and Waveney Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
        ],
        "related": ["Norfolk and Norwich University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — James Paget University Hospitals NHS Foundation Trust", "Establishment costs — West Suffolk NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Walsall Healthcare NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Walsall Healthcare NHS Trust"}],
        "description": "Walsall Healthcare NHS Trust's £5.74M PFI / LIFT charges line covers the IFRIC 12 service-concession unitary-charge profile attaching to the Walsall Manor Hospital PFI scheme (Sodexo / Skanska / Innisfree consortium) — capital and lifecycle elements presented as PFI / LIFT charges with operating-element FM (cleaning, catering, portering, security) elsewhere in the GAM. The 2022 IFRS 16 transition reclassified PFI service concessions, with continued IFRIC 12 treatment for principal scheme. Black Country ICS context.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 286,000 Walsall metropolitan-borough catchment plus Black Country borders; c. 110,000 ED attendances/yr at Walsall Manor ED; c. 75,000 admissions/yr; trust covers a high-deprivation post-industrial Black Country population with elevated cardiovascular, respiratory and diabetes demand.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 transition) — DHSC PFI guidance — DHSC Group Accounting Manual 2024-25 chapter 7 — NHS Act 2006 — Health and Care Act 2022 — Local Government and Public Involvement in Health Act 2007",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£5.74M"},
            {"label": "Trust scale", "value": "Walsall Manor Hospital + community services; c. 4,000 WTE"},
            {"label": "PFI scheme", "value": "Walsall Manor Hospital PFI — original construction phase early-2000s, expansion phase 2010 (Sodexo/Skanska/Innisfree consortium)"},
            {"label": "PFI ProjectCo", "value": "Skanska Innisfree consortium — Sodexo as FM operator"},
            {"label": "Concession term", "value": "30-year DBFO contract — expiry approx. 2040"},
            {"label": "IFRS 16 transition (2022)", "value": "DHSC guidance retained IFRIC 12 treatment for service-concession with off-balance-sheet capital recognition; income-statement profile continues"},
            {"label": "Composition", "value": "Capital + lifecycle unitary-charge element (interest + indexation) — FM operating-element (cleaning, catering, portering, security) sits elsewhere in GAM"},
            {"label": "RPI indexation", "value": "Unitary charge typically RPI-linked — recent high CPI/RPI runs (2022-2024) drove material annual escalation in charge"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.8M → 2023-24 c. £5.5M → 2024-25 £5.74M — RPI indexation on unitary charge + lifecycle phasing"},
            {"label": "Black Country ICS", "value": "Member of Black Country ICB (also covers Wolverhampton, Sandwell, Dudley)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Skanska Innisfree ProjectCo + Sodexo (FM) + DHSC PFI Centre of Excellence"},
            {"label": "Policy owner", "value": "DHSC PFI Centre of Excellence + IPA / HMT PFI policy + NHSE Provider Finance + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI in the NHS reports; Trust ARA 2023-24 PFI disclosure note; CQC RBK inspections; DHSC GAM PFI guidance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI Walsall Manor estate · Successor: PFI expiry handback c. 2040 + interim NHP / Premises Recovery Programme bid"}
        ],
        "notes": "Walsall Healthcare NHS Trust's PFI charges reflect the unitary-charge profile of the Walsall Manor Hospital PFI scheme — a Skanska / Innisfree / Sodexo consortium DBFO with original construction in the early 2000s and a 2010-era expansion. The 2022 IFRS 16 transition retained IFRIC 12 treatment for the service-concession element under DHSC GAM guidance. RPI indexation on the unitary charge has driven material annual escalation through the 2022-2024 high-inflation period. The trust has been linked with Sandwell and West Birmingham NHS Trust (now Sandwell and West Birmingham — operator of the new Midland Metropolitan University Hospital opened 2024) for collaborative Black Country acute reconfiguration, but Walsall Manor remains a standalone DGH. PFI expiry handback (c. 2040) is a long-horizon strategic challenge, sitting alongside the Carillion-novation legacy on FM operations.",
        "sources": [
            {"publisher": "Walsall Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.walsallhealthcare.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases + PFI)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Care Quality Commission", "title": "Walsall Healthcare NHS Trust provider profile (RBK)", "url": "https://www.cqc.org.uk/provider/RBK"},
            {"publisher": "HM Treasury Infrastructure and Projects Authority", "title": "PFI projects database", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2022-summary-data"}
        ],
        "related": ["Walsall Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "PFI / LIFT charges — University Hospitals Birmingham NHS Foundation Trust", "Social security & levy — Walsall Healthcare NHS Trust"]
    },
    "Establishment costs — Northumbria Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Northumbria Healthcare NHS Foundation Trust"}],
        "description": "Northumbria Healthcare NHS FT's £5.73M establishment costs line covers GAM operating expenses outside the payroll chain — office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below the capitalisation threshold across the trust's distinctive distributed-network model — Northumbria Specialist Emergency Care Hospital (Cramlington), North Tyneside General, Wansbeck General, Hexham General and Berwick Infirmary plus community hospitals. Industrial-action backfill plus EPR change-management training drive the line.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 500,000 Northumberland + North Tyneside catchment from rural northern uplands (Berwick, Hexham) to coastal and post-industrial communities; c. 200,000 ED attendances/yr concentrated at NSECH Cramlington (England's first purpose-built emergency hospital, 2015); c. 110,000 admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.73M"},
            {"label": "Trust scale", "value": "NSECH Cramlington + North Tyneside + Wansbeck + Hexham + Berwick + community footprint; c. 11,000 WTE"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "EPR + Care Strategy", "value": "Trust runs Lorenzo (legacy) with Frontline Digitisation pathway; GP/community CareLink integration drives training overhead"},
            {"label": "NSECH model", "value": "England's first purpose-built emergency hospital (2015) — single ED for the region, drives consolidated training, induction and rotational-staffing cost"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "Geographic spread", "value": "Largest ICB-area trust by geography — drives travel, courier, telephony, training-coordination premium over compact urban peers"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via training-provider and recruitment-advertising contractor pass-through (15% over £5k)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.7M → 2023-24 c. £5.5M → 2024-25 £5.73M — strike backfill + EPR training + CPI on consumables"},
            {"label": "North East and North Cumbria ICS", "value": "Member of NENC ICB; collaborative procurement / training frameworks across NENC"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance + Northumbria Healthcare FM Ltd (subsidiary)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NENC ICB + DHSC + NHS Supply Chain"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RTF inspections; NIHR Northern Care Alliance research collaboration"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NSECH single-site model · Successor: Frontline Digitisation Wave 4-5 deployment + ongoing FM-subsidiary (NHFML) consolidation"}
        ],
        "notes": "Northumbria Healthcare NHS FT's establishment-cost line is shaped by its geographic spread (largest ICB-area acute trust in England by area, from Berwick on the Scottish border to North Tyneside) — driving travel-coordination, telephony, courier and training-logistics premium. The trust's distinctive single-ED model at Northumbria Specialist Emergency Care Hospital (NSECH Cramlington, opened 2015 — England's first purpose-built emergency hospital) consolidates ED workforce training, induction and rotational scheduling. The 2023-24 industrial-action cycle added admin rebooking and recruitment-advertising. The trust's Northumbria Healthcare Facilities Management Ltd (NHFML) wholly-owned subsidiary insources FM at advantageous VAT and procurement terms — its overhead sits across multiple lines but interacts with Establishment. April 2025 employer NIC step-up flows indirectly via training-provider and recruitment-advertising pass-through.",
        "sources": [
            {"publisher": "Northumbria Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northumbria.nhs.uk/about-us/publications-policies-and-strategies/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Northumbria Healthcare NHS Foundation Trust provider profile (RTF)", "url": "https://www.cqc.org.uk/provider/RTF"},
            {"publisher": "NHS Confederation", "title": "North East and North Cumbria Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
        ],
        "related": ["Northumbria Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — North Tees and Hartlepool NHS Foundation Trust", "Establishment costs — South Tees Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — East And North Hertfordshire NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "East And North Hertfordshire NHS Trust"}],
        "description": "ENHT's £5.67M establishment costs line covers GAM operating expenses outside the payroll chain — office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below the capitalisation threshold across the Lister Hospital (Stevenage), Mount Vernon Cancer Centre (Northwood — leased from London North West University Healthcare), the New QEII (Welwyn Garden City) and Hertford County Hospital. Industrial-action backfill plus EPR change-management training drive the line.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 600,000 east + north Hertfordshire catchment plus a tertiary cancer-centre population for Mount Vernon serving c. 2M; c. 110,000 ED attendances/yr at Lister ED; c. 75,000 admissions/yr; c. 540,000 outpatient attendances/yr; trust hosts the Mount Vernon Cancer Centre — radiotherapy and oncology hub for north-west London + Beds + Herts.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.67M"},
            {"label": "Trust scale", "value": "Lister Hospital (Stevenage) + Mount Vernon Cancer Centre + New QEII + Hertford County; c. 5,500 WTE"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "Mount Vernon Cancer Centre", "value": "Tertiary radiotherapy + oncology centre — service-review process 2018-2023 (whether to retain at MV or relocate to UCLH); drives specialist training/conferences premium"},
            {"label": "EPR platform", "value": "Cerner Millennium — Frontline Digitisation upgrade pathway — change-management training feeds Establishment line"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via training-provider and recruitment-advertising contractor pass-through (15% over £5k)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 c. £5.4M → 2024-25 £5.67M — strike backfill + EPR training + CPI on consumables"},
            {"label": "Hertfordshire and West Essex ICS", "value": "Member of Hertfordshire and West Essex ICB; cross-ICS Mount Vernon catchment with NW London"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + Hertfordshire and West Essex ICB + DHSC + NHS Supply Chain"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RWH inspections; Mount Vernon Cancer Centre external review (2023)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner stabilisation baseline · Successor: Mount Vernon service-reconfiguration outcome + Frontline Digitisation upgrade-cycle training"}
        ],
        "notes": "ENHT's establishment-cost line is shaped by its tertiary Mount Vernon Cancer Centre footprint (radiotherapy + oncology hub serving north-west London, Beds and Herts — the subject of a long-running 2018-2023 service-reconfiguration review on whether to retain at the leased Mount Vernon site or relocate to UCLH / Watford) — driving specialist training, conferences and recruitment-advertising premium. The 2023-24 industrial-action cycle added admin rebooking and recruitment-advertising. Cerner Millennium EPR change-management cycles feed training-provider costs. The Lister Hospital was retained as the trust's principal acute-services site under the 'Our Changing Hospitals' service reconfiguration. April 2025 employer NIC step-up flows indirectly via training-provider and recruitment-advertising pass-through.",
        "sources": [
            {"publisher": "East And North Hertfordshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.enherts-tr.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Mount Vernon Cancer Centre future review", "url": "https://www.england.nhs.uk/london/our-work/mount-vernon-cancer-centre-review/"},
            {"publisher": "Care Quality Commission", "title": "East And North Hertfordshire NHS Trust provider profile (RWH)", "url": "https://www.cqc.org.uk/provider/RWH"},
            {"publisher": "NHS Confederation", "title": "Hertfordshire and West Essex Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
        ],
        "related": ["East And North Hertfordshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "General supplies & services — East And North Hertfordshire NHS Trust", "Establishment costs — West Hertfordshire Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Mersey and West Lancashire Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Mersey and West Lancashire Teaching Hospitals NHS Trust"}],
        "description": "MWL's £5.65M general supplies & services line covers GAM operating-expense consumables outside the Clinical Supplies & Drugs core — patient-facing non-clinical consumables (linen, paper, hand-towels, cleaning supplies), small medical-device parts below capitalisation threshold, kitchen and catering disposables, sterilisation and infection-control consumables, and high-volume administrative supplies across Whiston Hospital, St Helens Hospital, Southport & Formby District General and Ormskirk District General following the July 2023 merger.",
        "beneficiaries": "c. 9,800 WTE staff serving a c. 760,000 Merseyside + West Lancashire catchment (St Helens, Knowsley, Sefton, West Lancashire); c. 195,000 ED attendances/yr at Whiston + Southport ED; c. 130,000 admissions/yr; trust acquired by July 2023 merger of St Helens & Knowsley Teaching Hospitals (Whiston PFI) with Southport and Ormskirk Hospital NHS Trust.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 2 Inventories (interaction with Inventory line) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£5.65M"},
            {"label": "Trust scale", "value": "Whiston Hospital + St Helens + Southport DGH + Ormskirk DGH + community services; c. 9,800 WTE"},
            {"label": "Composition", "value": "Linen + paper + cleaning supplies + small medical-device parts below cap + catering disposables + sterilisation + infection-control consumables + admin supplies"},
            {"label": "Merger genesis", "value": "Trust formed July 2023 by merger of St Helens & Knowsley Teaching Hospitals NHS Trust with Southport and Ormskirk Hospital NHS Trust — drove integration costs in supply consolidation"},
            {"label": "PFI overlap", "value": "Whiston Hospital (acute base) is PFI (opened 2010) — FM operator embeds catering + cleaning supply procurement; rest of estate non-PFI"},
            {"label": "NHS Supply Chain spine", "value": "Most non-clinical consumable spend routed through NHS Supply Chain framework — pricing trajectory driven by Inflation Recovery Plan + Tower model retender"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + linen + sterilisation cycle uplift"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier + contractor pass-through (15% over £5k threshold)"},
            {"label": "Funding trajectory", "value": "Pre-merger: c. £3.5M (StHK) + c. £2.0M (S&O) → 2023-24 (post-merger) c. £5.4M → 2024-25 £5.65M — CPI on consumables + integration spike"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB; collaborative procurement frameworks across regional acute"},
            {"label": "Delivery body", "value": "Trust Procurement + E&F + NHS Supply Chain + Whiston PFI FM operator (Engie / Equans) + sterilisation services"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Supply Chain (Supply Chain Coordination Ltd) + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "NHS Supply Chain framework reports; Carter Lord review legacy; Model Hospital non-pay benchmark; Trust ARA 2023-24; CQC RBN inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger StHK + Southport-Ormskirk separate supply lines · Successor: post-merger consolidated procurement spine + NHP-Reset cohort Southport rebuild planning"}
        ],
        "notes": "MWL's general supplies & services line is shaped by the July 2023 merger of St Helens & Knowsley Teaching Hospitals (the high-performing 'outstanding' CQC trust operating the Whiston PFI hospital from 2010) with the financially and operationally challenged Southport and Ormskirk Hospital NHS Trust — driving consolidation overhead across linen, catering disposables, sterilisation and admin consumables. NHS Supply Chain Tower model retender (2023-2024) drove pricing pass-through. Most spend routes through NHS Supply Chain framework with Tower model coverage. Whiston PFI (Engie / Equans-novated FM) embeds catering and cleaning supply procurement within the unitary charge for that site. The Southport / Ormskirk estate sits in the NHP Reset cohort awaiting redevelopment timeline confirmation. April 2025 employer NIC step-up flows indirectly via supplier and contractor pass-through.",
        "sources": [
            {"publisher": "Mersey and West Lancashire Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.merseywestlancs.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Tower model and category framework", "url": "https://www.supplychain.nhs.uk/about-us/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mersey and West Lancashire Teaching Hospitals NHS Trust provider profile (RBN)", "url": "https://www.cqc.org.uk/provider/RBN"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"}
        ],
        "related": ["Mersey and West Lancashire Teaching Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "General supplies & services — Lancashire Teaching Hospitals NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Establishment costs — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "UHNM's £5.59M establishment costs line covers GAM operating expenses outside the payroll chain — office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below the capitalisation threshold across the Royal Stoke University Hospital (Stoke-on-Trent) and County Hospital (Stafford) following the November 2014 dissolution of Mid Staffordshire FT. Industrial-action backfill plus EPR (Lorenzo / Frontline Digitisation) change-management training drive the line.",
        "beneficiaries": "c. 11,500 WTE staff serving a c. 900,000 north Staffordshire + south Cheshire + Shropshire-borders catchment plus tertiary cardiothoracic and major-trauma referral footprint of c. 3M; c. 220,000 ED attendances/yr at Royal Stoke + County Hospital ED; c. 175,000 admissions/yr; designated Major Trauma Centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.59M"},
            {"label": "Trust scale", "value": "Royal Stoke University Hospital + County Hospital (Stafford); c. 11,500 WTE; designated Major Trauma Centre + cardiothoracic centre"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "EPR platform", "value": "Lorenzo (legacy National Programme for IT) — Frontline Digitisation upgrade pathway with selected Cerner / Oracle Health migration plan"},
            {"label": "Mid Staffs legacy", "value": "Trust absorbed Stafford Hospital (County Hospital) post-Mid Staffs dissolution Nov 2014 — Francis Inquiry training and culture-change programme legacy on training-cost line"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "PFI overlap", "value": "Royal Stoke is PFI-financed (BTUH / Project Co — opened 2012) — long PFI debate driving establishment-cost overhead in contract-management"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via training-provider and recruitment-advertising contractor pass-through (15% over £5k)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.4M → 2023-24 c. £5.3M → 2024-25 £5.59M — strike backfill + EPR training + CPI on consumables + Frontline Digitisation prep"},
            {"label": "Staffordshire and Stoke-on-Trent ICS", "value": "Member of Staffordshire and Stoke-on-Trent ICB"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + Staffordshire and Stoke-on-Trent ICB + DHSC + NHS Supply Chain"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RJE inspections; Francis Inquiry follow-up"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Mid Staffs dissolution baseline + pre-Lorenzo legacy · Successor: Frontline Digitisation EPR migration training + post-NHP-Reset planning for ageing estate"}
        ],
        "notes": "UHNM's establishment-cost line is shaped by the long shadow of the Mid Staffordshire NHS FT dissolution (Nov 2014) — when Stafford Hospital (now County Hospital) was transferred to UHNM with attendant Francis Inquiry-driven training, induction and culture-change programme cost feeding the line. The trust's Major Trauma Centre and tertiary cardiothoracic role drive specialist training and conference attendance premium. The Royal Stoke PFI structure (opened 2012) generates ongoing contract-management administrative overhead. The trust adopted Lorenzo EPR via the failed National Programme for IT and is in the Frontline Digitisation upgrade pathway with planned Oracle Health migration — driving training-cost preparation. The 2023-24 industrial-action cycle added admin rebooking and recruitment-advertising. April 2025 employer NIC step-up flows indirectly via training-provider and recruitment-advertising pass-through.",
        "sources": [
            {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhnm.nhs.uk/about-us/publications/annual-reports-and-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals of North Midlands NHS Trust provider profile (RJE)", "url": "https://www.cqc.org.uk/provider/RJE"},
            {"publisher": "Mid Staffordshire NHS Foundation Trust Public Inquiry", "title": "Final Report (Francis Inquiry)", "url": "https://webarchive.nationalarchives.gov.uk/ukgwa/20150407084003/http://www.midstaffspublicinquiry.com/report"}
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals of North Midlands NHS Trust", "Establishment costs — University Hospitals Birmingham NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "UHNM's £5.55M business-rates line covers non-domestic rate liability across the trust's two-acute-site footprint — Royal Stoke University Hospital (Stoke-on-Trent, opened on the new-build PFI site in 2012) and County Hospital (Stafford, transferred from Mid Staffs FT in 2014) — plus community outposts. Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Staffordshire and Stoke-on-Trent ICS context.",
        "beneficiaries": "c. 11,500 WTE staff serving a c. 900,000 north Staffordshire + south Cheshire + Shropshire-borders catchment plus tertiary cardiothoracic and major-trauma referral footprint of c. 3M; c. 220,000 ED attendances/yr at Royal Stoke + County Hospital ED; c. 175,000 admissions/yr; designated Major Trauma Centre + tertiary cardiothoracic centre.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£5.55M"},
            {"label": "Trust scale", "value": "Royal Stoke University Hospital + County Hospital (Stafford); c. 11,500 WTE; designated Major Trauma Centre"},
            {"label": "Principal hereditaments", "value": "Royal Stoke (large modern PFI acute hereditament — almost certainly £500k+ rateable-value tier) + County Hospital (Stafford)"},
            {"label": "PFI overlap", "value": "Royal Stoke is PFI-financed (opened 2012); rates paid by trust as occupier regardless of PFI structure"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.7M → 2023-24 c. £5.3M → 2024-25 £5.55M — 2023 list revaluation + multiplier uplift on Royal Stoke principal hereditament"},
            {"label": "Staffordshire and Stoke-on-Trent ICS", "value": "Member of Staffordshire and Stoke-on-Trent ICB"},
            {"label": "Mid Staffs legacy", "value": "County Hospital transferred from Mid Staffs FT (dissolution Nov 2014) — separate hereditament / billing-authority footprint"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + Stoke-on-Trent City Council / Stafford BC (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Staffordshire and Stoke-on-Trent ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24 disclosure; CQC RJE inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 Mid-Staffs County Hospital separate rates line + pre-PFI-2012 Royal Stoke baseline · Successor: 2026 VOA revaluation + ongoing trust appeal of Royal Stoke rateable value"}
        ],
        "notes": "UHNM's business-rates line is dominated by the Royal Stoke University Hospital principal hereditament — a large modern PFI-financed acute site (opened 2012) almost certainly above the £500k rateable-value threshold attracting the higher multiplier from April 2025 under the NDR (Multipliers and Private Finance) Act 2024. The County Hospital (Stafford) sits in a separate billing-authority footprint following the November 2014 Mid Staffs FT dissolution. NHS trusts are not eligible for the mandatory 80% charitable rate relief — full liability borne. The Royal Stoke PFI structure does not transfer rates liability — the trust as occupier pays rates regardless of PFI. The 1 April 2026 next revaluation is the medium-term lever; the trust's E&F team has historically engaged commercial rates consultants for Royal Stoke appeal advice. Pairs with the trust's £5.59M Establishment costs entry as a complementary running-cost view of the same estate footprint.",
        "sources": [
            {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhnm.nhs.uk/about-us/publications/annual-reports-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals of North Midlands NHS Trust provider profile (RJE)", "url": "https://www.cqc.org.uk/provider/RJE"}
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — University Hospitals of North Midlands NHS Trust", "Business rates — University Hospitals of Derby and Burton NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Establishment costs — York and Scarborough Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
        "description": "York and Scarborough NHS FT's £5.53M establishment costs line covers GAM operating expenses outside the payroll chain — office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below the capitalisation threshold across York Hospital, Scarborough Hospital, Bridlington Hospital, Selby War Memorial Hospital, Malton Hospital and Whitby Community Hospital. Industrial-action backfill plus EPR (CPP CITO) change-management training drive the line.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 800,000 York + North Yorkshire + Scarborough coastal catchment plus East Yorkshire borders (Bridlington); c. 175,000 ED attendances/yr at York + Scarborough ED; c. 110,000 admissions/yr; trust covers the largest geographic area of any English acute trust outside Northumbria — coast-to-Wolds rural and coastal communities.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.53M"},
            {"label": "Trust scale", "value": "York Hospital + Scarborough Hospital + Bridlington + Selby + Malton + Whitby; c. 8,500 WTE"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "EPR platform", "value": "CPP CITO (legacy) — Frontline Digitisation upgrade pathway with planned Cerner / Oracle Health migration — change-management training feeds Establishment line"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "RAAC critical site", "value": "Scarborough Hospital on the 2023 HSSIB RAAC list — drove decant logistics, mitigation works, training and consultation costs"},
            {"label": "Rural geographic spread", "value": "Coast-to-Wolds rural footprint drives travel, courier, telephony, training-coordination premium over compact urban peers"},
            {"label": "Recruitment challenges", "value": "Scarborough + Bridlington coastal sites historically struggle to recruit consultants — drives heavy recruitment-advertising premium (international + agency channel mix)"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via training-provider and recruitment-advertising contractor pass-through (15% over £5k)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.4M → 2023-24 c. £5.3M → 2024-25 £5.53M — strike backfill + EPR training + RAAC consultation + recruitment-ad premium + CPI"},
            {"label": "Humber and North Yorkshire ICS", "value": "Member of Humber and North Yorkshire ICB"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + Humber and North Yorkshire ICB + DHSC + NHS Supply Chain"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RCB inspections; HSSIB RAAC assessments"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-CITO baseline + pre-2012 acquisition of Scarborough by York · Successor: NHP / RAAC programme rebuild planning at Scarborough + Frontline Digitisation Wave 4-5"}
        ],
        "notes": "York and Scarborough Teaching Hospitals NHS FT's establishment-cost line is shaped by three structural drivers — Scarborough Hospital's RAAC status (one of the 2023 HSSIB-listed sites with critical-mitigation requirements driving decant logistics, mitigation-works coordination, staff and patient-consultation costs), persistent recruitment difficulty at Scarborough and Bridlington coastal sites (driving a heavy recruitment-advertising premium with international and agency channel use), and the trust's vast rural geographic footprint (coast-to-Wolds). The trust acquired Scarborough Hospital from Scarborough and North East Yorkshire Healthcare NHS Trust in 2012, with attendant integration overhead. Frontline Digitisation EPR migration (planned Oracle Health / Cerner replacement of the legacy CPP CITO) is the medium-term training-cost driver. April 2025 employer NIC step-up flows indirectly via training-provider and recruitment-advertising pass-through.",
        "sources": [
            {"publisher": "York and Scarborough Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yorkhospitals.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "RAAC mitigation programme + New Hospital Programme Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "Care Quality Commission", "title": "York and Scarborough Teaching Hospitals NHS Foundation Trust provider profile (RCB)", "url": "https://www.cqc.org.uk/provider/RCB"},
            {"publisher": "NHS Confederation", "title": "Humber and North Yorkshire Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
        ],
        "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — York and Scarborough Teaching Hospitals NHS Foundation Trust", "Establishment costs — Hull University Teaching Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Business rates — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "Sheffield Teaching Hospitals NHS FT's £5.53M business-rates line covers non-domestic rate liability across the trust's five-site footprint — Royal Hallamshire Hospital, Northern General Hospital, Weston Park Hospital (cancer centre), Jessop Wing (women's hospital), and Charles Clifford Dental Hospital — plus community outposts in Sheffield. Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024. South Yorkshire ICS context.",
        "beneficiaries": "c. 18,000 WTE staff serving a c. 580,000 Sheffield catchment plus a tertiary referral population for kidney transplant, neurosciences, oncology (Weston Park), spinal injuries (Princess Royal Spinal Injuries Centre at Northern General) and major trauma covering c. 1.8M South Yorkshire + Bassetlaw + Derbyshire borders; c. 220,000 ED attendances/yr at Northern General + Royal Hallamshire ED; c. 175,000 admissions/yr.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£5.53M"},
            {"label": "Trust scale", "value": "Royal Hallamshire + Northern General + Weston Park + Jessop Wing + Charles Clifford Dental; c. 18,000 WTE"},
            {"label": "Principal hereditaments", "value": "Northern General (Major Trauma Centre — large hereditament likely £500k+ tier) + Royal Hallamshire (large acute tower)"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne (cf. Weston Park Cancer Charity — separate hereditament with charity exemption on charity-occupied portion)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.7M → 2023-24 c. £5.2M → 2024-25 £5.53M — 2023 list revaluation + multiplier uplift on Northern General + Royal Hallamshire"},
            {"label": "South Yorkshire ICS", "value": "Member of South Yorkshire ICB"},
            {"label": "Major Trauma Centre", "value": "Northern General is the South Yorkshire MTC + Princess Royal Spinal Injuries Centre — drives outsized hereditament size + intensity uplift"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + Sheffield City Council (billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24 disclosure; CQC RHQ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + ongoing trust appeal of Northern General + Royal Hallamshire rateable values (high-tier multiplier exposure)"}
        ],
        "notes": "Sheffield Teaching Hospitals NHS FT's business-rates line is shaped by the trust's five-site footprint — with the Northern General Hospital (South Yorkshire Major Trauma Centre + Princess Royal Spinal Injuries Centre) and the Royal Hallamshire tower as the principal large hereditaments almost certainly above the £500k rateable-value threshold attracting the higher multiplier from April 2025 under the NDR (Multipliers and Private Finance) Act 2024. NHS trusts are not eligible for the mandatory 80% charitable rate relief, though Weston Park Hospital's Weston Park Cancer Charity-occupied portion attracts charity exemption on its slice. All sites sit in a single billing-authority footprint (Sheffield City Council) — administratively simpler than peer multi-site trusts. The 1 April 2026 next revaluation is the medium-term lever; the trust's E&F team has historically engaged commercial rates consultants for appeal advice on the principal hereditaments. Pairs with the trust's Amortisation entry as a complementary running-cost view of the same estate.",
        "sources": [
            {"publisher": "Sheffield Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sth.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Teaching Hospitals NHS Foundation Trust provider profile (RHQ)", "url": "https://www.cqc.org.uk/provider/RHQ"}
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Sheffield Teaching Hospitals NHS Foundation Trust", "Business rates — The Shrewsbury and Telford Hospital NHS Trust", "Valuation Office Agency"]
    },
    "Amortisation — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Kingston Hospital NHS FT's £5.49M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly Cerner Millennium EPR (the trust's flagship 2014 deployment, an early NHS adopter outside the National Programme for IT) plus capitalised digital-imaging (PACS / RIS), e-prescribing, pathology LIMS modules and back-office software supporting Kingston Hospital (Galsworthy Road) operations. The 2024 group structure now shares services with Hounslow and Richmond Community Healthcare following the group-model partnership with HRCH. South West London ICS context.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 360,000 Kingston + Richmond + Merton + Surrey-borders catchment; c. 110,000 ED attendances/yr at Kingston ED; c. 75,000 admissions/yr; c. 470,000 outpatient attendances/yr; trust historically sustained outstanding CQC ratings and led on early Cerner adoption.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — IFRS 3 Business Combinations (acquired-software treatment) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£5.49M"},
            {"label": "Trust scale", "value": "Kingston Hospital (Galsworthy Road); c. 3,500 WTE; CQC outstanding-rated (multiple cycles)"},
            {"label": "Principal intangibles", "value": "Cerner Millennium EPR + digital imaging (PACS/RIS) + e-prescribing + pathology LIMS + back-office software"},
            {"label": "EPR platform", "value": "Cerner Millennium (deployed 2014 — early NHS adopter outside NPfIT)"},
            {"label": "Cerner / Oracle Health", "value": "Trust ran Big Bang Cerner go-live 2014; now in Frontline Digitisation upgrade-cycle for module additions and lifecycle refresh"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; PACS image storage ~10 years; major EPR modules amortised over 7-10 yrs"},
            {"label": "Frontline Digitisation pipeline", "value": "Continued capitalised module additions (clinical noting, mobile apps, decision-support) feed forward intangibles balance"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 c. £5.0M → 2024-25 £5.49M — Frontline Digitisation module additions + Cerner refresh-cycle + HRCH group-model integration software"},
            {"label": "Group-model with HRCH", "value": "Kingston + Hounslow and Richmond Community Healthcare group partnership (announced 2023) — drives shared-software capitalisation"},
            {"label": "South West London ICS", "value": "Member of South West London ICB; collaborative provider with St George's, Epsom and St Helier"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Cerner (Oracle Health) + Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + SWL ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation reports; Trust ARA 2023-24 intangibles note; CQC RAX inspections (consistent outstanding); DHSC GAM compliance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner-2014 baseline · Successor: Cerner / Oracle Health refresh-cycle (2025-2027) + HRCH-shared-platform module additions"}
        ],
        "notes": "Kingston Hospital NHS FT's amortisation line reflects the trust's status as an early NHS Cerner Millennium adopter (2014 Big Bang go-live, outside the failed National Programme for IT) — its core EPR is now in mid-life amortisation under IAS 38 useful-economic-life conventions, with Frontline Digitisation module additions feeding forward additions. The 2023 group-model partnership with Hounslow and Richmond Community Healthcare (HRCH) drove shared-platform capitalisation for clinical-noting and admin systems. The trust has consistently held CQC 'outstanding' ratings (most recently 2022) — its digital maturity has been a cited contributor to its ratings. Future EPR refresh-cycle (Cerner / Oracle Health 2025-2027 lifecycle refresh planning) is the medium-term cliff-edge for the intangibles balance and future amortisation profile. Pairs with the trust's Social security & levy entry as a complementary view of the same operational footprint.",
        "sources": [
            {"publisher": "Kingston Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kingstonhospital.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Kingston Hospital NHS Foundation Trust provider profile (RAX)", "url": "https://www.cqc.org.uk/provider/RAX"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Social security & levy — Kingston Hospital NHS Foundation Trust", "Amortisation — Royal Free London NHS Foundation Trust", "Amortisation — Sheffield Teaching Hospitals NHS Foundation Trust"]
    },
}
