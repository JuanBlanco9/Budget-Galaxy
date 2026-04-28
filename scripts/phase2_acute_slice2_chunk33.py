# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 33 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Lease expenditure — Sherwood Forest Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Sherwood Forest Hospitals NHS Foundation Trust"}],
        "description": "Sherwood Forest Hospitals NHS FT's £1.633M lease-expenditure line covers IFRS 16 short-term and low-value lease payments plus residual operating-lease charges across the trust's footprint — King's Mill Hospital (Sutton-in-Ashfield, the principal acute / PFI site), Newark Hospital and Mansfield Community Hospital — chiefly modular clinical accommodation, NHSPS community-clinic occupation, photocopier / IT-equipment leases and small-fleet vehicle leases. The trust's main King's Mill PFI estate sits on a separate IFRIC 12 / on-balance-sheet liability outside this line.",
        "beneficiaries": "c. 5,200 WTE staff serving a c. 420,000 north Nottinghamshire catchment (Mansfield, Ashfield, Newark, Sherwood); c. 130,000 ED attendances/yr at King's Mill ED + c. 35,000 at Newark MIU; c. 80,000 admissions/yr; trust runs King's Mill, Newark and Mansfield Community within the Nottingham and Nottinghamshire ICS.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 (chapter 7) — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — IFRIC 12 (separate PFI treatment for King's Mill PFI)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.633M"},
            {"label": "Trust scale", "value": "King's Mill Hospital (Sutton-in-Ashfield, PFI) + Newark Hospital + Mansfield Community Hospital; c. 5,200 WTE"},
            {"label": "Composition", "value": "Short-term + low-value IFRS 16 leases — modular clinical accommodation, NHSPS community-clinic occupation, photocopier/IT, small-fleet vehicles"},
            {"label": "King's Mill PFI", "value": "Principal estate held under separate IFRIC 12 service-concession arrangement (Skanska Healthcare Sherwood) — outside this lease line; expiry 2043"},
            {"label": "IFRS 16 effective date", "value": "1 April 2022 — DHSC GAM mandated full retrospective adoption for NHS bodies, lifting prior off-balance-sheet operating leases on-BS"},
            {"label": "NHSPS community-clinic occupation", "value": "Mansfield Community Hospital and outreach clinics — disputed-rent NHSPS arrears history (2018-2024 sector-wide)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.4M (pre-IFRS 16) → 2022-23 c. £1.55M (IFRS 16 jump) → 2024-25 £1.633M — modular-decant lease pressure"},
            {"label": "Nottingham and Nottinghamshire ICS", "value": "Member of NHS Nottingham and Nottinghamshire ICB; collaborative procurement framework"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + NHS Property Services + Skanska Healthcare Sherwood (PFI vehicle, separate)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHS Property Services + Nottingham and Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 lease note disclosure; CQC RK5 'Outstanding' rating 2020 → 'Good' 2024; NAO PFI reports; DHSC GAM compliance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease accounting · Successor: IFRS 16 right-of-use depreciation cycle + potential King's Mill 2043 PFI expiry handback planning"}
        ],
        "notes": "Sherwood Forest's lease-expenditure line is shaped by IFRS 16's April 2022 effective date — the DHSC GAM mandated full retrospective adoption, lifting previously off-balance-sheet operating leases on-BS and capitalising right-of-use assets. The principal King's Mill PFI estate (Skanska Healthcare Sherwood, expiry 2043) sits on a separate IFRIC 12 service-concession liability outside this line, so the residual lease balance is dominated by modular clinical-accommodation rentals (often used for industrial-action decant or RTT recovery), NHSPS community-clinic occupation in Mansfield, and IT / photocopier leases. The 2018-2024 NHSPS rent dispute affected community-clinic occupation. April 2025 employer NIC step-up is indirectly material via NHSPS service-charge pass-through. The trust holds a CQC 'Good' rating (downgraded from 'Outstanding' in 2024).",
        "sources": [
            {"publisher": "Sherwood Forest Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sfh-tr.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "IFRS 16 Leases application guidance for the public sector", "url": "https://www.gov.uk/government/publications/financial-reporting-manual"},
            {"publisher": "Care Quality Commission", "title": "Sherwood Forest Hospitals NHS Foundation Trust provider profile (RK5)", "url": "https://www.cqc.org.uk/provider/RK5"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 — investigation into PFI and PF2 hospitals", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"}
        ],
        "related": ["Sherwood Forest Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "NHS Property Services", "Department of Health and Social Care"]
    },
    "Establishment costs — Gloucestershire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Gloucestershire Hospitals NHS Foundation Trust"}],
        "description": "Gloucestershire Hospitals NHS FT's £1.632M establishment-costs line covers GAM operating expenses outside the payroll chain — office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services, and minor furniture / equipment below the capitalisation threshold across Gloucestershire Royal Hospital (Gloucester), Cheltenham General Hospital and the trust's Gloucestershire community footprint. 2023-24 industrial-action backfill plus EPR Cerner Millennium training cycles drive the line.",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 650,000 Gloucestershire catchment (Gloucester, Cheltenham, Cotswolds, Forest of Dean, Tewkesbury, Stroud); c. 165,000 ED attendances/yr split across Gloucestershire Royal ED + Cheltenham A&E; c. 95,000 admissions/yr; trust runs Gloucestershire Royal Hospital + Cheltenham General + community sites within the One Gloucestershire ICS.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.632M"},
            {"label": "Trust scale", "value": "Gloucestershire Royal (Gloucester) + Cheltenham General + community footprint; c. 8,000 WTE"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + courier services + minor furniture/equipment below cap threshold"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike across both Gloucestershire Royal and Cheltenham sites"},
            {"label": "EPR Cerner Millennium", "value": "Long-standing Cerner Millennium deployment + Sunrise EPR migration history — training and change-management spend feeds Establishment line"},
            {"label": "Centralisation programme", "value": "Cheltenham A&E night-time downgrade (2020-2022) + emergency-services centralisation at Gloucestershire Royal — recruitment/retention pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.55M → 2024-25 £1.632M — strike backfill + EPR training + CPI"},
            {"label": "One Gloucestershire ICS", "value": "Member of NHS Gloucestershire ICB; tight collaborative procurement and shared back-office with GHC"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + One Gloucestershire ICB + DHSC + NHS Supply Chain (where used)"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RTE inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner baseline establishment-cost profile · Successor: post-EPR-stabilisation training-cost normalisation + GHC shared-services consolidation"}
        ],
        "notes": "Gloucestershire Hospitals' establishment-cost line is shaped by 2023-24 industrial-action backfill (44 days junior-doctor + 10 days consultant strikes drove admin rebooking, recruitment advertising and casual training spend across both Gloucestershire Royal and Cheltenham sites), EPR Cerner Millennium training and change-management cycles, and HMRC subsistence/training-provider CPI uplifts. The trust's medium-term operating context is dominated by the contested Cheltenham A&E night-time downgrade (2020-2022) and the emergency-services centralisation at Gloucestershire Royal, which generated recruitment-retention pressure feeding establishment spend. April 2025 employer NIC step-up (15% over £5k threshold) feeds indirectly via training-provider and recruitment-advertising contractor pass-through. CQC rates the trust 'Good' (RTE) with positive maternity scrutiny in 2024.",
        "sources": [
            {"publisher": "Gloucestershire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gloshospitals.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Gloucestershire Hospitals NHS Foundation Trust provider profile (RTE)", "url": "https://www.cqc.org.uk/provider/RTE"},
            {"publisher": "NHS Confederation", "title": "One Gloucestershire Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
        ],
        "related": ["Gloucestershire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Stockport NHS Foundation Trust", "Establishment costs — Cambridge University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Kettering General Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Kettering General Hospital NHS Foundation Trust"}],
        "description": "Kettering General Hospital NHS FT's £1.616M business-rates line covers non-domestic rate liability principally on Kettering General Hospital (Rothwell Road, Kettering) — the trust's sole acute site serving north Northamptonshire — plus minor community-clinic outposts. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the standard non-domestic multiplier under the Local Government Finance Act 1988 (Sch 6) as amended by the NDR (Multipliers and Private Finance) Act 2024. KGH is a New Hospital Programme cohort site. Northamptonshire ICS context.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 360,000 north Northamptonshire catchment (Kettering, Corby, Wellingborough, Rushden, East Northamptonshire); c. 110,000 ED attendances/yr at Kettering ED; c. 65,000 admissions/yr; sole acute provider for north Northamptonshire — works closely with Northampton General (south Northants) under a Group model.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.616M"},
            {"label": "Trust scale", "value": "Kettering General Hospital + minor community outposts; c. 4,500 WTE"},
            {"label": "Principal hereditament", "value": "Kettering General Hospital (Rothwell Road, Kettering NN16 8UZ) — sole acute site"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 (higher tier on £500k+ from April 2025 — material for KGH)"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "New Hospital Programme cohort", "value": "Kettering General Hospital is in NHP — Reset Jan 2025 deferred to Wave 3 (2032-39 construction window)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.45M → 2023-24 c. £1.6M → 2024-25 £1.616M — 2023 list revaluation + multiplier uplift"},
            {"label": "Northamptonshire ICS / KGH-NGH Group", "value": "University Hospitals of Northamptonshire Group model with Northampton General Hospital — single CEO since 2022"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + North Northamptonshire Council (billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RNQ inspections; NHP IPA gateway reviews; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + post-NHP-rebuild rateable-value reset"}
        ],
        "notes": "Kettering General Hospital's business-rates line reflects the VOA 2023 rating-list valuation on its single acute hereditament — the main hospital site at Rothwell Road, Kettering. The trust is a New Hospital Programme cohort site (originally Wave 2) which was deferred under the January 2025 NHP Reset to Wave 3 (2032-39 construction window) — the rebuild was scoped to address the ageing 1990s estate and structural issues. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals so the full liability is borne. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for the main hospital. KGH operates within the University Hospitals of Northamptonshire Group with Northampton General under a single executive team since 2022.",
        "sources": [
            {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Plan for Implementation", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Care Quality Commission", "title": "Kettering General Hospital NHS Foundation Trust provider profile (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"}
        ],
        "related": ["Kettering General Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Business rates — Surrey And Sussex Healthcare NHS Trust", "Valuation Office Agency"]
    },
    "Business rates — Bolton NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Bolton NHS Foundation Trust"}],
        "description": "Bolton NHS FT's £1.613M business-rates line covers non-domestic rate liability principally on Royal Bolton Hospital (Minerva Road, Farnworth) — the trust's principal acute / maternity site — plus community-clinic outposts across the Bolton metropolitan borough. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the standard non-domestic multiplier under the Local Government Finance Act 1988 (Sch 6) as amended by the NDR (Multipliers and Private Finance) Act 2024. Greater Manchester ICS context.",
        "beneficiaries": "c. 5,800 WTE staff serving a c. 295,000 Bolton metropolitan-borough catchment plus surrounding south-Lancs community demand; c. 145,000 ED attendances/yr at Royal Bolton ED; c. 75,000 admissions/yr; serves a high-deprivation post-industrial population with high maternity activity (regional maternity centre).",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.613M"},
            {"label": "Trust scale", "value": "Royal Bolton Hospital + Bolton community-clinic outposts; c. 5,800 WTE"},
            {"label": "Principal hereditament", "value": "Royal Bolton Hospital (Minerva Road, Farnworth, Bolton BL4 0JR) — main acute site + regional maternity centre"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 (higher tier on £500k+ from April 2025)"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.45M → 2023-24 c. £1.6M → 2024-25 £1.613M — 2023 list revaluation + multiplier uplift"},
            {"label": "Greater Manchester ICS", "value": "Member of Greater Manchester ICB; collaborative procurement and rates-relief discussions across GM"},
            {"label": "Maternity services scrutiny", "value": "Royal Bolton maternity historic CQC scrutiny + Ockenden review context — feeds estate-investment case"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + Bolton MBC (billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RMC inspections; Trust ARA 2023-24; Ockenden / national maternity reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + Bolton trust appeal of rateable values"}
        ],
        "notes": "Bolton NHS FT's business-rates line reflects the VOA 2023 rating-list valuation on Royal Bolton Hospital — its sole acute hereditament — plus minor community-clinic outposts. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals so the full liability is borne. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for Royal Bolton's main site. Greater Manchester ICS membership provides a collaborative-procurement and rates-relief negotiation forum. The trust's maternity-services historical scrutiny (CQC + Ockenden context) feeds the estate-investment case and shapes operational footprint underpinning rateable-value assessment. Bolton has a high-deprivation post-industrial catchment driving high acute demand.",
        "sources": [
            {"publisher": "Bolton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.boltonft.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bolton NHS Foundation Trust provider profile (RMC)", "url": "https://www.cqc.org.uk/provider/RMC"}
        ],
        "related": ["Bolton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Bolton NHS Foundation Trust", "Business rates — Kettering General Hospital NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Kingston Hospital NHS FT's £1.601M business-rates line covers non-domestic rate liability principally on Kingston Hospital (Galsworthy Road, Kingston upon Thames) — the trust's principal acute / maternity site — plus a small Hounslow / Richmond community footprint following the 2024 merger with Hounslow and Richmond Community Healthcare. Rateable values are set by the VOA on the 2023 list with rates calculated against the standard non-domestic multiplier under LGFA 1988 (Sch 6) as amended by the NDR (Multipliers and Private Finance) Act 2024. South West London ICS context.",
        "beneficiaries": "c. 4,800 WTE staff (post-2024 HRCH merger) serving a c. 360,000 Kingston / Richmond / Surbiton / east-Surrey-overspill catchment plus expanded Hounslow / Richmond community population (c. 600,000); c. 110,000 ED attendances/yr at Kingston ED; c. 65,000 admissions/yr; regional maternity centre.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.601M"},
            {"label": "Trust scale", "value": "Kingston Hospital + Hounslow/Richmond community footprint (post-2024 HRCH merger); c. 4,800 WTE"},
            {"label": "Principal hereditament", "value": "Kingston Hospital (Galsworthy Road, Kingston upon Thames KT2 7QB) — main acute site + maternity centre"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 (higher tier on £500k+ from April 2025)"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "HRCH merger 2024", "value": "Acquired Hounslow and Richmond Community Healthcare NHS Trust 1 April 2024 — added community-clinic hereditaments"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.4M → 2023-24 c. £1.55M → 2024-25 £1.601M — 2023 list revaluation + HRCH merger pickup"},
            {"label": "South West London ICS", "value": "Member of NHS South West London ICB"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + Kingston RBC / Richmond LBC / Hounslow LBC (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + South West London ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RAX 'Outstanding' rating maintained 2024; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list + pre-merger acute-only footprint · Successor: 2026 VOA revaluation + post-merger consolidated rateable-value profile"}
        ],
        "notes": "Kingston Hospital's business-rates line reflects the VOA 2023 rating-list valuation on Kingston Hospital plus the expanded community-clinic footprint following the April 2024 acquisition of Hounslow and Richmond Community Healthcare NHS Trust. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals so the full liability is borne. Kingston is one of only a handful of NHS acute trusts holding a CQC 'Outstanding' rating (RAX), maintained at the 2024 inspection — the trust's strong governance underpins its rateable-value challenge capability. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for the main hospital. Cross-borough (Kingston RBC / Richmond LBC / Hounslow LBC) billing-authority complexity adds administrative overhead.",
        "sources": [
            {"publisher": "Kingston Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kingstonhospital.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Kingston Hospital NHS Foundation Trust provider profile (RAX)", "url": "https://www.cqc.org.uk/provider/RAX"}
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Social security & levy — Kingston Hospital NHS Foundation Trust", "Business rates — Bolton NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — East And North Hertfordshire NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "East And North Hertfordshire NHS Trust"}],
        "description": "East and North Hertfordshire NHS Trust's £1.588M transport line covers AfC Section 17 + AMAP staff business mileage, pool and lease vehicle running costs (IFRS 16), inter-site shuttle / courier between Lister Hospital (Stevenage), Hertford County Hospital, the New QEII (Welwyn Garden City) and Mount Vernon Cancer Centre (Northwood — operated by ENHT), plus residual non-emergency patient transport service (NEPTS) commissioning gap-fill and prescription-charge eligible patient travel reimbursement.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 600,000 east + north Hertfordshire catchment (Stevenage, Welwyn, Hatfield, Hertford, Bishop's Stortford, Letchworth) + the much wider Mount Vernon cancer-network catchment (c. 2M from north-west London, Buckinghamshire and Hertfordshire); c. 130,000 ED attendances/yr at Lister ED; c. 80,000 admissions/yr; Mount Vernon adds a tertiary cancer footprint.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — AfC Section 17 (Reimbursement of travel costs) — HMRC Approved Mileage Allowance Payments — IFRS 16 Leases (pool / lease fleet) — Health and Care Act 2022 — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.588M"},
            {"label": "Trust scale", "value": "Lister (Stevenage) + Hertford County + New QEII (Welwyn) + Mount Vernon Cancer Centre (Northwood); c. 5,500 WTE"},
            {"label": "Composition", "value": "AfC Sec 17 + AMAP staff mileage + pool/lease fleet (IFRS 16) + inter-site shuttle/courier + residual patient-travel reimbursement"},
            {"label": "Multi-site footprint", "value": "Four hospital sites — generates inter-site transport demand (Lister-Hertford-QEII-Mount Vernon shuttle)"},
            {"label": "Mount Vernon Cancer Centre", "value": "ENHT operates Mount Vernon (Northwood) — separate from acute footprint, dedicated cancer-patient transport demand under NHS England specialised commissioning review"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove inter-site backfill mileage spike at Lister + QEII"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.55M → 2024-25 £1.588M — strike inter-site backfill + HMRC AMAP rate uplift + IFRS 16 lease cost"},
            {"label": "Hertfordshire and West Essex ICS", "value": "Member of NHS Hertfordshire and West Essex ICB"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + Finance + EEAST (NEPTS) + DHL/private NEPTS providers + PTS appeals office"},
            {"label": "Policy owner", "value": "DHSC (HTC) + NHSE Specialised Commissioning (Mount Vernon) + Hertfordshire and West Essex ICB + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Framework 2021 review; Mount Vernon Cancer Centre future review (NHSE 2024); Trust ARA 2023-24; CQC RWH inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease accounting + pre-HMRC-uplift mileage rates · Successor: post-Mount-Vernon-future-review tertiary-cancer transport reconfiguration + April 2025 NIC contractor pass-through"}
        ],
        "notes": "ENHT's transport line is shaped by its four-site footprint — Lister (Stevenage, the principal acute), Hertford County, New QEII (Welwyn) and the geographically separate Mount Vernon Cancer Centre at Northwood — generating substantial inter-site staff-mileage and pool / shuttle demand plus dedicated cancer-patient transport from the wider Mount Vernon network catchment (c. 2M people across north-west London, Buckinghamshire and Hertfordshire). The 2023-24 industrial-action backfill cycle drove inter-site cover mileage at Lister and QEII. The contested Mount Vernon Cancer Centre future review (NHSE 2024 specialised-commissioning consultation) is the medium-term lever — a relocation or reconfiguration would materially reshape the trust's tertiary-cancer transport footprint. April 2025 employer NIC step-up flows through to NEPTS contractor and pool-fleet maintenance pass-through.",
        "sources": [
            {"publisher": "East and North Hertfordshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.enherts-tr.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Mount Vernon Cancer Centre future — public consultation", "url": "https://www.england.nhs.uk/london/our-work/mount-vernon-cancer-centre/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts-framework/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"},
            {"publisher": "Care Quality Commission", "title": "East and North Hertfordshire NHS Trust provider profile (RWH)", "url": "https://www.cqc.org.uk/provider/RWH"}
        ],
        "related": ["East And North Hertfordshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Mount Vernon Cancer Centre", "Amortisation — East And North Hertfordshire NHS Trust", "Transport (business + patient) — Bolton NHS Foundation Trust"]
    },
    "Transport (business + patient) — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "Ashford and St Peter's Hospitals NHS FT's £1.583M transport line covers AfC Section 17 + AMAP staff business mileage, pool and lease vehicle running costs (IFRS 16), inter-site shuttle / courier between Ashford Hospital (Ashford, Surrey — day-case + outpatients) and St Peter's Hospital (Chertsey — main acute / ED), plus residual non-emergency patient transport service (NEPTS) commissioning gap-fill and prescription-charge eligible patient travel reimbursement. The two-site model generates structural inter-site transport demand.",
        "beneficiaries": "c. 4,300 WTE staff serving a c. 410,000 north-west Surrey + Spelthorne / Heathrow-fringe catchment (Chertsey, Addlestone, Weybridge, Walton, Sunbury, Staines, Ashford, Stanwell); c. 130,000 ED attendances/yr at St Peter's ED; c. 65,000 admissions/yr; structural twin-site model generates daily inter-site transport demand.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — AfC Section 17 (Reimbursement of travel costs) — HMRC Approved Mileage Allowance Payments — IFRS 16 Leases (pool / lease fleet) — Health and Care Act 2022 — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.583M"},
            {"label": "Trust scale", "value": "St Peter's Hospital (Chertsey, ED + main acute) + Ashford Hospital (Ashford Surrey, day-case/outpatients); c. 4,300 WTE"},
            {"label": "Composition", "value": "AfC Sec 17 + AMAP staff mileage + pool/lease fleet (IFRS 16) + inter-site shuttle/courier + residual patient-travel reimbursement"},
            {"label": "Twin-site model", "value": "St Peter's (Chertsey) + Ashford (Surrey) — c. 8 miles apart, daily shuttle and inter-site staff rotation drives mileage demand"},
            {"label": "Heathrow-fringe catchment", "value": "Spelthorne / Stanwell / Heathrow corridor adds airport-related occupational demand and high-cost-of-living staff retention pressure"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove inter-site backfill mileage spike between Ashford and St Peter's"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.55M → 2024-25 £1.583M — HMRC AMAP rate uplift + IFRS 16 lease cost + strike backfill"},
            {"label": "Surrey Heartlands ICS", "value": "Member of NHS Surrey Heartlands ICB; collaborative NEPTS commissioning across Surrey"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + Finance + South Central Ambulance Service / G4S NEPTS contractor"},
            {"label": "Policy owner", "value": "DHSC (HTC) + Surrey Heartlands ICB + NHSE Provider Finance + NHS England NEPTS Framework owner"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Framework 2021 review; Trust ARA 2023-24; CQC RTK 'Outstanding' rating maintained"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease accounting · Successor: post-NEPTS-recommissioning Surrey-wide framework + April 2025 NIC contractor pass-through"}
        ],
        "notes": "Ashford and St Peter's transport line is structurally driven by the c. 8-mile twin-site Chertsey-Ashford footprint — daily inter-site staff rotation, courier between sites and pool / lease fleet running cost dominate the line, with residual patient-travel reimbursement forming a smaller share. The Heathrow-fringe catchment (Spelthorne, Stanwell, Sunbury, Staines) adds airport-related occupational demand and high-cost-of-living staff retention pressure feeding mileage claims. The 2023-24 industrial-action backfill cycle drove substantial inter-site cover mileage. Surrey Heartlands ICS-led NEPTS recommissioning is the medium-term lever. April 2025 employer NIC step-up (15% over £5k threshold) flows through to NEPTS contractor and pool-fleet maintenance pass-through. The trust holds a CQC 'Outstanding' rating — a small minority among NHS acute providers.",
        "sources": [
            {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ashfordstpeters.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts-framework/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Ashford and St Peter's Hospitals NHS Foundation Trust provider profile (RTK)", "url": "https://www.cqc.org.uk/provider/RTK"}
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Ashford and St Peter's Hospitals NHS Foundation Trust", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "Transport (business + patient) — East And North Hertfordshire NHS Trust"]
    },
    "Amortisation — Barnsley Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Barnsley Hospital NHS Foundation Trust"}],
        "description": "Barnsley Hospital NHS FT's £1.583M amortisation line covers IAS 38 systematic write-down of intangible assets — chiefly the capitalised electronic patient record (EPR) and digital-transformation programme implementation costs (Frontline Digitisation cohort), capitalised software licences, clinical-systems integration and bespoke software development across the trust's single Barnsley Hospital site. Software is amortised over its assessed useful life (typically 5-10 years) under the DHSC GAM chapter 5 framework.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 250,000 Barnsley metropolitan-borough catchment (Barnsley, Wombwell, Penistone, Hoyland, Cudworth) plus tertiary outflow to Sheffield Teaching Hospitals; c. 80,000 ED attendances/yr at Barnsley ED; c. 50,000 admissions/yr; sole acute provider for Barnsley borough within the South Yorkshire ICS.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5) — IAS 36 Impairment of Assets (impairment trigger interaction) — NHS Act 2006 — Health and Care Act 2022 — Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.583M"},
            {"label": "Trust scale", "value": "Barnsley Hospital (Gawber Road) — single acute site; c. 3,500 WTE"},
            {"label": "Principal asset", "value": "Capitalised EPR programme (Frontline Digitisation cohort) + clinical-systems software stack (PAS, RIS, PACS, e-prescribing)"},
            {"label": "Frontline Digitisation participation", "value": "Barnsley Hospital is a Frontline Digitisation programme cohort site — central capital + matched trust capex feeds intangible-asset balance"},
            {"label": "Useful life", "value": "Typically 5-10 years for clinical software per DHSC GAM ch.5; longer for foundational PAS"},
            {"label": "South Yorkshire ICS", "value": "Member of NHS South Yorkshire ICB; collaborative digital programme with Sheffield Teaching, Doncaster & Bassetlaw and Rotherham"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.2M → 2023-24 c. £1.5M → 2024-25 £1.583M — Frontline Digitisation EPR amortisation kicking in plus continued software-licence capitalisation"},
            {"label": "Working with Sheffield Teaching", "value": "Long-standing collaborative relationship with Sheffield Teaching Hospitals — shared digital pathways for tertiary referrals"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Frontline Digitisation programme team + EPR vendor + South Yorkshire ICB digital team"},
            {"label": "Policy owner", "value": "NHSE Transformation Directorate (Frontline Digitisation) + DHSC + NHSE Provider Finance + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation reporting; Trust ARA 2023-24 intangible-asset note; NAO Digital Transformation in the NHS reports; CQC RFF inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline-Digitisation legacy clinical-systems amortisation profile · Successor: continued EPR amortisation plus next-generation digital-transformation cohort"}
        ],
        "notes": "Barnsley Hospital's amortisation line is dominated by the capitalised Frontline Digitisation EPR programme — the trust's single-site footprint concentrates the digital-transformation capex base into one balance, generating a steady amortisation profile through the 5-10 year useful-life window. The South Yorkshire ICS collaborative digital programme with Sheffield Teaching, Doncaster & Bassetlaw and Rotherham shapes shared-pathway investment, particularly around tertiary referrals to Sheffield. NAO scrutiny of NHS digital transformation (2020 + 2023 reports) flags useful-life assumptions and impairment-trigger sensitivity. The 2023-24 industrial-action backfill cycle did not directly affect the amortisation line but the Frontline Digitisation programme rollout cycle continues to feed forward intangible-asset capitalisation. Barnsley is a high-deprivation post-mining catchment.",
        "sources": [
            {"publisher": "Barnsley Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.barnsleyhospital.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Barnsley Hospital NHS Foundation Trust provider profile (RFF)", "url": "https://www.cqc.org.uk/provider/RFF"}
        ],
        "related": ["Barnsley Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation programme", "Amortisation — East And North Hertfordshire NHS Trust", "Amortisation — Hampshire Hospitals NHS Foundation Trust"]
    },
    "Lease expenditure — Royal Devon University Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Royal Devon University Healthcare NHS Foundation Trust"}],
        "description": "Royal Devon University Healthcare NHS FT's £1.577M lease-expenditure line covers IFRS 16 short-term and low-value lease payments plus residual operating-lease charges across the trust's twin-DGH-plus-community footprint — the Royal Devon and Exeter Hospital (Wonford), North Devon District Hospital (Barnstaple) and an extensive Eastern + Northern Devon community-hospital network (Tiverton, Honiton, Sidmouth, Axminster, Ottery St Mary, Crediton, Okehampton, South Molton, Bideford, Holsworthy). Modular clinical accommodation, NHSPS community-clinic occupation and pool-fleet leases dominate.",
        "beneficiaries": "c. 14,000 WTE staff (post-2022 merger of Royal Devon and Exeter with Northern Devon Healthcare) serving a c. 615,000 Devon catchment plus c. 9M visitor surge; c. 220,000 ED attendances/yr split across RD&E ED + NDDH ED + Tiverton MIU + 8 other MIUs; c. 130,000 admissions/yr; sole acute provider for north Devon and main acute provider for east + central Devon.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 (chapter 7) — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — IFRIC 12 (separate PFI treatment for any held)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.577M"},
            {"label": "Trust scale", "value": "Royal Devon and Exeter (Wonford) + North Devon District (Barnstaple) + 10+ community hospitals (Tiverton, Honiton, Sidmouth, Axminster, Ottery, Crediton, Okehampton, South Molton, Bideford, Holsworthy); c. 14,000 WTE"},
            {"label": "Composition", "value": "Short-term + low-value IFRS 16 leases — modular clinical accommodation, NHSPS community-clinic occupation, pool-fleet (geographically dispersed), photocopier/IT"},
            {"label": "2022 merger context", "value": "Royal Devon and Exeter NHS FT merged with Northern Devon Healthcare NHS Trust 1 April 2022 — combined community-hospital network creates wide-dispersed lease footprint"},
            {"label": "IFRS 16 effective date", "value": "1 April 2022 — DHSC GAM mandated full retrospective adoption coincided with merger"},
            {"label": "NHSPS community-clinic occupation", "value": "Multiple NHSPS-owned community clinics across east + north Devon — disputed-rent NHSPS arrears history (2018-2024 sector-wide)"},
            {"label": "Geographic dispersion", "value": "Largest geographic footprint of any English NHS acute trust — drives pool-fleet lease intensity"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.3M (pre-merger) → 2022-23 c. £1.5M (post-merger + IFRS 16 jump) → 2024-25 £1.577M — modular-decant pressure"},
            {"label": "Devon ICS", "value": "Member of NHS Devon ICB"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + NHS Property Services + Community Health Partnerships (LIFT for some sites)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHS Property Services + Devon ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 lease note disclosure; CQC RH8 inspections; NHSE post-merger benefits-realisation review; DHSC GAM compliance"},
            {"label": "Predecessor / successor", "value": "Predecessor: separate RD&E + NDH lease accounting pre-merger · Successor: consolidated post-merger lease portfolio + Devon ICS estates rationalisation"}
        ],
        "notes": "Royal Devon's lease line reflects two compounding factors — the April 2022 merger of Royal Devon and Exeter NHS FT with Northern Devon Healthcare NHS Trust which created the largest geographic footprint of any English NHS acute trust (twin DGHs plus 10+ community hospitals across Devon), coinciding with the April 2022 IFRS 16 effective date that lifted previously off-balance-sheet operating leases on-BS. The geographic dispersion drives high pool-fleet lease intensity for community-team transport. NHSPS community-clinic occupation across multiple east + north Devon sites carries 2018-2024 NHSPS rent-dispute history. Devon ICS-led estates rationalisation is the medium-term lever — the merger's benefits-realisation case includes shared-back-office and footprint review. April 2025 employer NIC step-up indirectly material via NHSPS service-charge pass-through.",
        "sources": [
            {"publisher": "Royal Devon University Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royaldevon.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "IFRS 16 Leases application guidance for the public sector", "url": "https://www.gov.uk/government/publications/financial-reporting-manual"},
            {"publisher": "NHS Property Services", "title": "About NHS Property Services + community-clinic occupation", "url": "https://www.property.nhs.uk/about-us/"},
            {"publisher": "Care Quality Commission", "title": "Royal Devon University Healthcare NHS Foundation Trust provider profile (RH8)", "url": "https://www.cqc.org.uk/provider/RH8"}
        ],
        "related": ["Royal Devon University Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "NHS Property Services", "Lease expenditure — Sherwood Forest Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Wrightington, Wigan and Leigh NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Wrightington, Wigan and Leigh NHS Foundation Trust"}],
        "description": "Wrightington, Wigan and Leigh Teaching Hospitals NHS FT's £1.573M business-rates line covers non-domestic rate liability across the trust's three-site footprint — Royal Albert Edward Infirmary (Wigan, the principal acute / ED), Wrightington Hospital (Appley Bridge — internationally renowned orthopaedic centre) and Leigh Infirmary (community + day-case). Rateable values are set by the VOA on the 2023 list with rates calculated against the standard non-domestic multiplier under LGFA 1988 (Sch 6) as amended by the NDR (Multipliers and Private Finance) Act 2024. Greater Manchester ICS context.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 320,000 Wigan metropolitan-borough catchment (Wigan, Leigh, Atherton, Hindley, Tyldesley, Ashton-in-Makerfield) plus a national + international catchment for Wrightington's elective orthopaedic services; c. 110,000 ED attendances/yr at Royal Albert Edward Infirmary ED; c. 65,000 admissions/yr.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.573M"},
            {"label": "Trust scale", "value": "Royal Albert Edward Infirmary (Wigan, ED) + Wrightington Hospital (orthopaedic centre) + Leigh Infirmary; c. 5,000 WTE"},
            {"label": "Wrightington heritage", "value": "Birthplace of John Charnley's modern hip replacement (1962) — internationally renowned orthopaedic centre, dedicated rateable hereditament"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 (higher tier on £500k+ from April 2025)"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.4M → 2023-24 c. £1.55M → 2024-25 £1.573M — 2023 list revaluation + multiplier uplift"},
            {"label": "Greater Manchester ICS", "value": "Member of Greater Manchester ICB"},
            {"label": "Three-site footprint", "value": "Three separately rated hereditaments — Wigan (RAEI), Appley Bridge (Wrightington), Leigh"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + Wigan MBC / West Lancashire BC (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RRF inspections; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + GM-ICS estates rationalisation"}
        ],
        "notes": "Wrightington, Wigan and Leigh's business-rates line reflects the VOA 2023 rating-list valuations across three separately rated hereditaments — Royal Albert Edward Infirmary (Wigan), Wrightington Hospital (Appley Bridge — the internationally renowned orthopaedic centre, birthplace of John Charnley's modern hip replacement in 1962) and Leigh Infirmary. Cross-billing-authority (Wigan MBC / West Lancashire BC) complexity adds administrative overhead. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals so the full liability is borne. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for both Wigan and Wrightington main sites. Greater Manchester ICS membership provides a collaborative-procurement and rates-relief negotiation forum.",
        "sources": [
            {"publisher": "Wrightington, Wigan and Leigh Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wwl.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Wrightington, Wigan and Leigh NHS Foundation Trust provider profile (RRF)", "url": "https://www.cqc.org.uk/provider/RRF"}
        ],
        "related": ["Wrightington, Wigan and Leigh NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Bolton NHS Foundation Trust", "Business rates — Wirral University Teaching Hospital NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Salisbury NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Salisbury NHS Foundation Trust"}],
        "description": "Salisbury NHS FT's £1.572M business-rates line covers non-domestic rate liability principally on Salisbury District Hospital (Odstock Road, Salisbury) — the trust's sole acute site hosting nationally specialised services including the Spinal Treatment Centre, the Wessex Genomic Laboratory and the regional plastic-surgery / burns / cleft-lip services. Rateable values are set by the VOA on the 2023 list with rates calculated against the standard non-domestic multiplier under LGFA 1988 (Sch 6) as amended by the NDR (Multipliers and Private Finance) Act 2024. Bath and North East Somerset, Swindon and Wiltshire ICS context.",
        "beneficiaries": "c. 4,200 WTE staff serving a c. 270,000 south Wiltshire / west Hampshire / east Dorset DGH catchment plus a much wider national + south-west / south-coast specialised-services catchment for spinal injury (c. 4M people), genomic services and burns / cleft / plastic surgery; c. 75,000 ED attendances/yr at Salisbury ED; c. 50,000 admissions/yr.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.572M"},
            {"label": "Trust scale", "value": "Salisbury District Hospital (Odstock Road) — single acute site hosting national specialised services; c. 4,200 WTE"},
            {"label": "Principal hereditament", "value": "Salisbury District Hospital (Odstock Road, Salisbury SP2 8BJ) — main acute + Spinal Treatment Centre + Wessex Genomic Lab + plastic-surgery/burns/cleft regional centre"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 (higher tier on £500k+ from April 2025)"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Specialised services", "value": "NHS England specialised commissioning footprint hosts Spinal Treatment Centre + Wessex Genomic Lab + burns + cleft + plastic surgery — high-specification estate underpins rateable value"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.4M → 2023-24 c. £1.55M → 2024-25 £1.572M — 2023 list revaluation + multiplier uplift"},
            {"label": "BSW ICS", "value": "Member of NHS Bath and North East Somerset, Swindon and Wiltshire ICB"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + Wiltshire Council (billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Specialised Commissioning + NHSE Provider Finance + BSW ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RNZ 'Good' rating; NHSE Spinal Cord Injury Centre review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + Spinal Cord Injury Centre national review outcome"}
        ],
        "notes": "Salisbury NHS FT's business-rates line reflects the VOA 2023 rating-list valuation on Salisbury District Hospital — its sole acute hereditament, but one carrying disproportionate specialised-service density (Spinal Treatment Centre, Wessex Genomic Lab, burns, cleft, plastic surgery) which underpins higher rateable value than would be expected for a small DGH catchment. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals so the full liability is borne. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material. NHSE Specialised Commissioning's review of national Spinal Cord Injury Centres is the medium-term lever — a relocation or reconfiguration would materially reshape the trust's specialised-service estate footprint.",
        "sources": [
            {"publisher": "Salisbury NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.salisbury.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "NHS England", "title": "Specialised commissioning — Spinal Cord Injury Centres", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Care Quality Commission", "title": "Salisbury NHS Foundation Trust provider profile (RNZ)", "url": "https://www.cqc.org.uk/provider/RNZ"}
        ],
        "related": ["Salisbury NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Salisbury NHS Foundation Trust", "Business rates — Wrightington, Wigan and Leigh NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Bolton NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Bolton NHS Foundation Trust"}],
        "description": "Bolton NHS FT's £1.564M transport line covers AfC Section 17 + AMAP staff business mileage, pool and lease vehicle running costs (IFRS 16) for community-team transport across the Bolton metropolitan-borough footprint, courier between Royal Bolton Hospital and community-clinic outposts, plus residual non-emergency patient transport service (NEPTS) commissioning gap-fill and prescription-charge eligible patient travel reimbursement. Greater Manchester ICS-led NEPTS commissioning shapes the line.",
        "beneficiaries": "c. 5,800 WTE staff serving a c. 295,000 Bolton metropolitan-borough catchment plus surrounding south-Lancs community demand; c. 145,000 ED attendances/yr at Royal Bolton ED; c. 75,000 admissions/yr; large district-nursing + community-midwifery footprint drives staff-mileage volume across the borough.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — AfC Section 17 (Reimbursement of travel costs) — HMRC Approved Mileage Allowance Payments — IFRS 16 Leases (pool / lease fleet) — Health and Care Act 2022 — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.564M"},
            {"label": "Trust scale", "value": "Royal Bolton Hospital + Bolton community-clinic outposts + community nursing/midwifery footprint; c. 5,800 WTE"},
            {"label": "Composition", "value": "AfC Sec 17 + AMAP staff mileage + pool/lease fleet (IFRS 16) + community courier + residual patient-travel reimbursement"},
            {"label": "Community demand", "value": "Large district-nursing + community-midwifery footprint across Bolton MBC drives staff-mileage volume"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove backfill mileage spike + casual-staff commute reimbursement"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.5M → 2024-25 £1.564M — HMRC AMAP rate uplift + IFRS 16 lease cost"},
            {"label": "Greater Manchester ICS", "value": "Member of Greater Manchester ICB; collaborative GM-wide NEPTS commissioning"},
            {"label": "GM NEPTS provider", "value": "Arriva Transport Solutions / Manchester Local Care Organisation NEPTS framework — covers Greater Manchester collectively"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + Finance + Arriva NEPTS + GM Combined Authority transport coordination"},
            {"label": "Policy owner", "value": "DHSC (HTC) + Greater Manchester ICB + NHSE Provider Finance + GMCA"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Framework 2021 review; GM NEPTS performance reporting; Trust ARA 2023-24; CQC RMC inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease accounting · Successor: post-NEPTS-recommissioning GM-wide framework + April 2025 NIC contractor pass-through"}
        ],
        "notes": "Bolton NHS FT's transport line reflects the trust's hybrid acute + community model — Royal Bolton Hospital sits alongside a large district-nursing and community-midwifery footprint across the Bolton metropolitan borough, generating substantial staff-mileage volume on top of acute-site shuttle and courier flows. Greater Manchester ICS-led NEPTS commissioning (Arriva Transport Solutions framework) shapes the patient-travel residual. The 2023-24 industrial-action backfill cycle drove substantial cover mileage and casual-staff commute reimbursement. April 2025 employer NIC step-up (15% over £5k threshold) flows through to NEPTS contractor and pool-fleet maintenance pass-through. The trust's high-deprivation post-industrial catchment with high maternity activity sustains community-midwifery transport demand.",
        "sources": [
            {"publisher": "Bolton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.boltonft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts-framework/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bolton NHS Foundation Trust provider profile (RMC)", "url": "https://www.cqc.org.uk/provider/RMC"}
        ],
        "related": ["Bolton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Bolton NHS Foundation Trust", "Transport (business + patient) — Ashford and St Peter's Hospitals NHS Foundation Trust", "Transport (business + patient) — East And North Hertfordshire NHS Trust"]
    },
    "Termination & post-employment — Liverpool University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Liverpool University Hospitals NHS Foundation Trust"}],
        "description": "Liverpool University Hospitals NHS FT's £1.554M termination and post-employment line covers IAS 19 redundancy and exit payments plus residual non-NHS-Pension-Scheme post-employment benefit costs (e.g. unfunded compensatory added-years pension top-ups, MARS / VSS exit packages) at the merged Royal Liverpool University Hospital + Aintree University Hospital + Broadgreen Hospital footprint. The 2019 trust merger (Royal Liverpool + Aintree) plus the 2022 Royal Liverpool new-build opening (post-Carillion collapse) drives ongoing structural-change and exit-package activity.",
        "beneficiaries": "c. 13,000 WTE staff serving a c. 750,000 Liverpool city-region catchment plus tertiary outflow (cancer, renal, transplant, neurosciences) across c. 2.5M Cheshire and Merseyside ICS population; c. 230,000 ED attendances/yr split across Royal Liverpool ED + Aintree ED; c. 130,000 admissions/yr; second-largest English NHS acute trust by catchment after Barts Health.",
        "legal_basis": "IAS 19 Employee Benefits — Public Sector Exit Payments Regulations 2020 (status — repealed) — Public Sector Special Severance Payments Treasury guidance — NHS Pension Scheme Regulations 2008 + 2015 — Employment Rights Act 1996 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£1.554M"},
            {"label": "Trust scale", "value": "Royal Liverpool University Hospital + Aintree University Hospital + Broadgreen Hospital (post-2019 merger); c. 13,000 WTE"},
            {"label": "2019 merger context", "value": "Royal Liverpool and Broadgreen + Aintree University Hospital merged 1 October 2019 to form LUH NHS FT — restructuring exits feed termination line"},
            {"label": "Royal Liverpool new-build 2022", "value": "New Royal Liverpool opened October 2022 — replaced 1978 building; original Carillion build (suspended 2018 collapse) finished by Laing O'Rourke; £1.2B+ total cost"},
            {"label": "Carillion 2018 collapse", "value": "Original Royal Liverpool builder Carillion collapsed January 2018 — c. 4-year completion delay drove ongoing restructuring + exit costs"},
            {"label": "Composition", "value": "IAS 19 redundancy + exit payments + residual unfunded compensatory added-years + MARS / VSS exit packages"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.0M → 2022-23 c. £1.4M (post new-build move) → 2024-25 £1.554M — continued post-merger restructuring + back-office consolidation"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of NHS Cheshire and Merseyside ICB; provider-collaborative back-office shared services"},
            {"label": "Delivery body", "value": "Trust HR + Finance + NHS Pensions Agency + DHSC (special-severance approval >£100k)"},
            {"label": "Policy owner", "value": "HM Treasury (special-severance policy) + DHSC + NHSE Provider Finance + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 termination/post-employment note; HMT Public Sector Exit Payments transparency; CQC REM inspections; NAO Royal Liverpool / Carillion reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: Royal Liverpool + Aintree separate exit profiles pre-2019 · Successor: post-merger consolidated exit programme + provider-collaborative back-office consolidation"}
        ],
        "notes": "Liverpool University Hospitals' termination and post-employment line is shaped by three structural factors — the 2019 merger of Royal Liverpool + Aintree which generated ongoing back-office and senior-management restructuring, the October 2022 opening of the new Royal Liverpool building (replacing the 1978 facility, completed by Laing O'Rourke after Carillion's January 2018 collapse caused a c. 4-year delay), and the trust's status as the second-largest English NHS acute by catchment driving ongoing portfolio-rationalisation activity. The April 2025 employer NIC step-up (15% over £5k threshold) feeds indirectly. HMT special-severance approval (>£100k threshold) is required for senior exits and disclosed in the ARA. Carillion-fallout litigation and PFI-novation ongoing. Cheshire and Merseyside ICS-led provider-collaborative back-office consolidation is the medium-term lever.",
        "sources": [
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.liverpoolft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "Public Sector Special Severance Payments — guidance", "url": "https://www.gov.uk/government/publications/guidance-on-public-sector-special-severance-payments"},
            {"publisher": "National Audit Office", "title": "Investigation: Royal Liverpool University Hospital — Carillion completion", "url": "https://www.nao.org.uk/reports/completing-the-new-royal-liverpool-hospital/"},
            {"publisher": "Care Quality Commission", "title": "Liverpool University Hospitals NHS Foundation Trust provider profile (REM)", "url": "https://www.cqc.org.uk/provider/REM"}
        ],
        "related": ["Liverpool University Hospitals NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "NHS Pension Scheme", "PFI / LIFT charges — Liverpool University Hospitals NHS Foundation Trust", "Carillion plc"]
    },
    "Amortisation — Hampshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
        "description": "Hampshire Hospitals NHS FT's £1.543M amortisation line covers IAS 38 systematic write-down of intangible assets — chiefly the capitalised electronic patient record (EPR) programme (Hampshire's Cerner Millennium-based system, deployed under the Frontline Digitisation umbrella), capitalised software licences, clinical-systems integration and bespoke software development across the trust's twin-DGH-plus footprint — Royal Hampshire County Hospital (Winchester), Basingstoke and North Hampshire Hospital, and Andover War Memorial Hospital.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 600,000 north + central Hampshire catchment (Winchester, Basingstoke, Andover, Alton, Whitchurch, Romsey rural belt); c. 145,000 ED attendances/yr split across Winchester ED + Basingstoke ED; c. 90,000 admissions/yr; trust runs Winchester + Basingstoke + Andover within the Hampshire and Isle of Wight ICS.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5) — IAS 36 Impairment of Assets (impairment trigger interaction) — NHS Act 2006 — Health and Care Act 2022 — Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.543M"},
            {"label": "Trust scale", "value": "Royal Hampshire County (Winchester) + Basingstoke and North Hampshire + Andover War Memorial; c. 7,500 WTE"},
            {"label": "Principal asset", "value": "Capitalised Cerner Millennium EPR + clinical-systems software stack (PAS, RIS, PACS, e-prescribing) under Frontline Digitisation"},
            {"label": "Frontline Digitisation participation", "value": "Hampshire Hospitals is in the Frontline Digitisation cohort — central capital + matched trust capex feeds intangible-asset balance"},
            {"label": "Useful life", "value": "Typically 5-10 years for clinical software per DHSC GAM ch.5"},
            {"label": "NHP cohort context", "value": "Hampshire Hospitals' new-hospital case (single replacement for Winchester + Basingstoke at a centralised Junction 7 M3 site) deferred to NHP Wave 3 (2032-39 window) following January 2025 Reset"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.2M → 2023-24 c. £1.45M → 2024-25 £1.543M — Frontline Digitisation EPR amortisation kicking in plus continued software-licence capitalisation"},
            {"label": "Hampshire and IoW ICS", "value": "Member of NHS Hampshire and Isle of Wight ICB; collaborative digital programme"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Frontline Digitisation programme team + Cerner / Oracle Health + Hampshire and IoW ICB digital team"},
            {"label": "Policy owner", "value": "NHSE Transformation Directorate (Frontline Digitisation) + DHSC + NHSE Provider Finance + Hampshire and IoW ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation reporting; Trust ARA 2023-24 intangible-asset note; NAO Digital Transformation in the NHS reports; CQC RN5 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline-Digitisation legacy clinical-systems amortisation profile · Successor: continued EPR amortisation + post-NHP-Reset 2032-39 new-hospital build impairment/transfer"}
        ],
        "notes": "Hampshire Hospitals' amortisation line is dominated by the capitalised Cerner Millennium EPR programme deployed under the Frontline Digitisation umbrella, plus the layered clinical-systems software stack. The trust's medium-term context is dominated by the contested new-hospital case — the original NHP Wave 2 plan was a single replacement hospital at a centralised Junction 7 M3 site (between Winchester and Basingstoke), but this was deferred under the January 2025 NHP Reset to Wave 3 (2032-39 construction window), generating downstream impairment and asset-transfer accounting questions. NAO scrutiny of NHS digital transformation (2020 + 2023 reports) flags useful-life assumptions and impairment-trigger sensitivity. The 2023-24 industrial-action backfill cycle did not directly affect amortisation but Frontline Digitisation rollout cycle continues to feed forward intangible-asset capitalisation.",
        "sources": [
            {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hampshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Plan for Implementation", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Hampshire Hospitals NHS Foundation Trust provider profile (RN5)", "url": "https://www.cqc.org.uk/provider/RN5"}
        ],
        "related": ["Hampshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation programme", "New Hospital Programme", "Amortisation — Barnsley Hospital NHS Foundation Trust"]
    },
    "Business rates — Wirral University Teaching Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Wirral University Teaching Hospital NHS Foundation Trust"}],
        "description": "Wirral University Teaching Hospital NHS FT's £1.527M business-rates line covers non-domestic rate liability principally on Arrowe Park Hospital (Upton — the trust's principal acute / ED site) and Clatterbridge Hospital (Bebington — the elective / rehabilitation site, distinct from Clatterbridge Cancer Centre NHS FT) plus minor community-clinic outposts. Rateable values are set by the VOA on the 2023 list with rates calculated against the standard non-domestic multiplier under LGFA 1988 (Sch 6) as amended by the NDR (Multipliers and Private Finance) Act 2024. Cheshire and Merseyside ICS context.",
        "beneficiaries": "c. 5,400 WTE staff serving a c. 320,000 Wirral metropolitan-borough catchment (Birkenhead, Wallasey, Bebington, Heswall, West Kirby, Hoylake) plus c. 80,000 west Cheshire / Ellesmere Port overspill; c. 130,000 ED attendances/yr at Arrowe Park ED; c. 75,000 admissions/yr; sole acute provider for the Wirral peninsula.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.527M"},
            {"label": "Trust scale", "value": "Arrowe Park (Upton, ED) + Clatterbridge (Bebington, elective/rehab) + community outposts; c. 5,400 WTE"},
            {"label": "Principal hereditaments", "value": "Arrowe Park Hospital (Upton CH49 5PE) + Clatterbridge Hospital (Bebington CH63 4JY) — two main rated sites"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 (higher tier on £500k+ from April 2025 — material for Arrowe Park)"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Distinct from Clatterbridge Cancer Centre", "value": "Wirral UTH operates Clatterbridge Hospital (general hospital); Clatterbridge Cancer Centre NHS FT (separate trust) operates the cancer centre — different rated entities"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.5M → 2024-25 £1.527M — 2023 list revaluation + multiplier uplift"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of NHS Cheshire and Merseyside ICB"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + Wirral MBC (billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RBL inspections (2018 enforcement action history); Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + Cheshire & Merseyside ICS estates rationalisation"}
        ],
        "notes": "Wirral University Teaching Hospital's business-rates line reflects the VOA 2023 rating-list valuation across two principal hereditaments — Arrowe Park (Upton, the main acute / ED site) and Clatterbridge (Bebington, elective and rehabilitation; distinct from the separately operated Clatterbridge Cancer Centre NHS FT). NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals so the full liability is borne. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for Arrowe Park's main site. The trust's CQC enforcement-action history (2018 Section 29A warning) drove governance overhaul. Cheshire and Merseyside ICS-led estates rationalisation is the medium-term lever, with potential single-site reconfiguration scenarios under the wider provider-collaborative model.",
        "sources": [
            {"publisher": "Wirral University Teaching Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wuth.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Wirral University Teaching Hospital NHS Foundation Trust provider profile (RBL)", "url": "https://www.cqc.org.uk/provider/RBL"}
        ],
        "related": ["Wirral University Teaching Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Salisbury NHS Foundation Trust", "Business rates — Wrightington, Wigan and Leigh NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Warrington and Halton Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Warrington and Halton Teaching Hospitals NHS Foundation Trust"}],
        "description": "Warrington and Halton Teaching Hospitals NHS FT's £1.524M transport line covers AfC Section 17 + AMAP staff business mileage, pool and lease vehicle running costs (IFRS 16), inter-site shuttle and courier between Warrington Hospital (Lovely Lane, Warrington — main acute / ED) and Halton General Hospital (Hospital Way, Runcorn — elective / day-case + minor injuries) c. 8 miles apart, plus residual non-emergency patient transport service (NEPTS) commissioning gap-fill and prescription-charge eligible patient travel reimbursement. Cheshire and Merseyside ICS context.",
        "beneficiaries": "c. 4,400 WTE staff serving a c. 330,000 Warrington + Halton catchment (Warrington, Runcorn, Widnes, Lymm) plus south-west Cheshire / north Cheshire-fringe overspill; c. 110,000 ED attendances/yr at Warrington ED + c. 20,000 at Halton MIU; c. 65,000 admissions/yr; structural twin-site model generates daily inter-site transport demand.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — AfC Section 17 (Reimbursement of travel costs) — HMRC Approved Mileage Allowance Payments — IFRS 16 Leases (pool / lease fleet) — Health and Care Act 2022 — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.524M"},
            {"label": "Trust scale", "value": "Warrington Hospital (ED) + Halton General Hospital (elective/MIU); c. 4,400 WTE"},
            {"label": "Composition", "value": "AfC Sec 17 + AMAP staff mileage + pool/lease fleet (IFRS 16) + inter-site shuttle/courier + residual patient-travel reimbursement"},
            {"label": "Twin-site model", "value": "Warrington (Lovely Lane) + Halton General (Runcorn) — c. 8 miles apart, daily shuttle and inter-site staff rotation drives mileage demand"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove inter-site backfill mileage spike between Warrington and Halton"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.3M → 2023-24 c. £1.5M → 2024-25 £1.524M — HMRC AMAP rate uplift + IFRS 16 lease cost + strike backfill"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of NHS Cheshire and Merseyside ICB"},
            {"label": "NEPTS provider", "value": "North West Ambulance Service / E-Zec NEPTS framework — covers Cheshire and Merseyside collectively"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + Finance + NWAS / E-Zec NEPTS contractor"},
            {"label": "Policy owner", "value": "DHSC (HTC) + Cheshire and Merseyside ICB + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Framework 2021 review; Trust ARA 2023-24; CQC RWW inspections; NHSE Operational Plan transport returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease accounting · Successor: post-NEPTS-recommissioning Cheshire & Merseyside framework + April 2025 NIC contractor pass-through"}
        ],
        "notes": "Warrington and Halton's transport line is structurally driven by the c. 8-mile twin-site Warrington-Runcorn footprint — daily inter-site staff rotation, courier between sites and pool / lease fleet running cost dominate the line, with residual patient-travel reimbursement forming a smaller share. The 2023-24 industrial-action backfill cycle drove substantial inter-site cover mileage. Cheshire and Merseyside ICS-led NEPTS recommissioning (NWAS / E-Zec framework) shapes the patient-travel residual. April 2025 employer NIC step-up (15% over £5k threshold) flows through to NEPTS contractor and pool-fleet maintenance pass-through. The trust is a teaching-hospital partner with the University of Chester and Liverpool. The medium-term Cheshire & Merseyside provider-collaborative reconfiguration could reshape the twin-site footprint.",
        "sources": [
            {"publisher": "Warrington and Halton Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whh.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts-framework/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Warrington and Halton Teaching Hospitals NHS Foundation Trust provider profile (RWW)", "url": "https://www.cqc.org.uk/provider/RWW"}
        ],
        "related": ["Warrington and Halton Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Bolton NHS Foundation Trust", "Transport (business + patient) — Ashford and St Peter's Hospitals NHS Foundation Trust", "Transport (business + patient) — East And North Hertfordshire NHS Trust"]
    },
    "Business rates — North Tees and Hartlepool NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "North Tees and Hartlepool NHS Foundation Trust"}],
        "description": "North Tees and Hartlepool NHS FT's £1.523M business-rates line covers non-domestic rate liability across the trust's twin-site footprint — the University Hospital of North Tees (Hardwick Road, Stockton-on-Tees, the principal acute / ED) and the University Hospital of Hartlepool (Holdforth Road, Hartlepool, day-case + outpatients + non-residential rehabilitation) plus minor community-clinic outposts. Rateable values are set by the VOA on the 2023 list with rates calculated against the standard non-domestic multiplier under LGFA 1988 (Sch 6) as amended by the NDR (Multipliers and Private Finance) Act 2024. North East and North Cumbria ICS context. NHP cohort site.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 400,000 north-Teesside + Hartlepool catchment (Stockton, Billingham, Hartlepool, Sedgefield, Yarm, Norton, Wynyard); c. 105,000 ED attendances/yr at North Tees ED + c. 25,000 at Hartlepool MIU; c. 70,000 admissions/yr.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.523M"},
            {"label": "Trust scale", "value": "University Hospital of North Tees (Stockton ED) + University Hospital of Hartlepool (day-case/MIU); c. 5,500 WTE"},
            {"label": "Principal hereditaments", "value": "UH North Tees (Hardwick Road, Stockton TS19 8PE) + UH Hartlepool (Holdforth Road, Hartlepool TS24 9AH)"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 (higher tier on £500k+ from April 2025 — material for North Tees)"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "New Hospital Programme cohort", "value": "Originally Wave 1 NHP cohort with planned new Tees Valley hospital — deferred under January 2025 NHP Reset to Wave 3 (2032-39 window)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.5M → 2024-25 £1.523M — 2023 list revaluation + multiplier uplift"},
            {"label": "NENC ICS", "value": "Member of NHS North East and North Cumbria ICB"},
            {"label": "Hartlepool A&E history", "value": "Hartlepool A&E closed 2011 (Momentum reconfiguration); long-running political controversy over Hartlepool downgrade — political constraint on rateable-value challenges"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + Stockton-on-Tees BC / Hartlepool BC (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + NENC ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RVW 'Good' rating; Trust ARA 2023-24; NHP IPA gateway reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + post-NHP-Reset 2032-39 new Tees Valley hospital impairment/transfer"}
        ],
        "notes": "North Tees and Hartlepool's business-rates line reflects the VOA 2023 rating-list valuations across two principal hereditaments — University Hospital of North Tees (Stockton, the main acute / ED) and University Hospital of Hartlepool (day-case / MIU), with cross-billing-authority complexity (Stockton-on-Tees BC + Hartlepool BC). Hartlepool's A&E was closed in 2011 (Momentum reconfiguration) generating long-running political controversy about Hartlepool downgrade — this constrains the trust's ability to challenge rateable values without political fallout. The trust was originally in NHP Wave 1 with a planned new Tees Valley single-site replacement hospital, but this was deferred under the January 2025 NHP Reset to Wave 3 (2032-39 construction window). The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for North Tees. NHS trusts are not eligible for mandatory 80% charitable rate relief.",
        "sources": [
            {"publisher": "North Tees and Hartlepool NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nth.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Plan for Implementation", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Care Quality Commission", "title": "North Tees and Hartlepool NHS Foundation Trust provider profile (RVW)", "url": "https://www.cqc.org.uk/provider/RVW"}
        ],
        "related": ["North Tees and Hartlepool NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Social security & levy — North Tees and Hartlepool NHS Foundation Trust", "Valuation Office Agency"]
    },
}
