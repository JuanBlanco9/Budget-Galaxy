# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 45 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {}

NEW["Other & adjustments — Northumbria Healthcare NHS Foundation Trust"] = {
    "aliases": [{"name": "Other & adjustments", "parent": "Northumbria Healthcare NHS Foundation Trust"}],
    "description": "Northumbria Healthcare NHSFT's £0.21M Other & adjustments line is a Staff Costs disclosure cleanup covering prior-year payroll corrections, AME / DEL reclassifications, ESA10-aligned reclassifications, accruals true-ups and immaterial residual employer-cost items below DHSC GAM materiality thresholds. The trust runs a multi-site acute and integrated-community footprint anchored on the Northumbria Specialist Emergency Care Hospital (Cramlington) plus North Tyneside General, Wansbeck General, Hexham, and a wide community estate across Northumberland and North Tyneside.",
    "beneficiaries": "Indirect — adjustments affect net-cost allocation across c. 11,000 substantive WTE serving c. 500,000 residents of Northumberland and North Tyneside; supports the trust's acute, community and adult social-care delivery footprint within the North East and North Cumbria ICB.",
    "legal_basis": "DHSC Group Accounting Manual 2024-25 disclosure rules · ESA10 sector-classification framework · IAS 1 Presentation of Financial Statements · IAS 19 Employee Benefits · NHS Act 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Other & adjustments 2024-25", "value": "£0.21M"},
        {"label": "Composition", "value": "Prior-year payroll corrections + AME / DEL reclassifications + accruals true-ups + immaterial residual employer-cost items"},
        {"label": "ESA10 framework", "value": "European System of Accounts 2010 — sector-classification rules cascading through DHSC GAM"},
        {"label": "Trust scale anchor", "value": "c. 11,000 WTE across Specialist Emergency Care Hospital + 3 general hospitals + 7+ community hospitals"},
        {"label": "Site footprint", "value": "Northumbria Specialist Emergency Care Hospital (Cramlington), North Tyneside General, Wansbeck General, Hexham General + community network"},
        {"label": "DHSC GAM disclosure rule", "value": "Other & adjustments is a permitted catchall for items below materiality thresholds"},
        {"label": "Funding trajectory", "value": "Variable year-on-year per cleanup volume; 2024-25 £0.21M reflects routine cleanup post-Specialist Emergency Care model maturation"},
        {"label": "Delivery body", "value": "Northumbria HR + Finance + NHSE Provider Finance + DHSC consolidation"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North East and North Cumbria (NENC) ICB"},
        {"label": "Beneficiary count", "value": "Indirect — affects net-cost allocation rather than direct-service delivery"},
        {"label": "Evaluation evidence", "value": "Northumbria ARA Note 8 staff-costs disclosure; CQC Outstanding rating; NHSE Operational Plan returns"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-DHSC GAM 2024-25 cleanup categorisation · Successor: continued residual disclosure under standard GAM rules; potential adult-social-care s75 partnership cleanup"}
    ],
    "notes": "Northumbria's Other & adjustments staff-costs line is recurring cleanup covering prior-year payroll corrections, ESA10 reclassifications and immaterial residuals below substantive sub-category materiality. The trust is one of England's largest integrated acute-community-social-care providers (running adult social care under a s75 partnership with Northumberland County Council), and is recognised for its Specialist Emergency Care Hospital model — the first purpose-built emergency-care-only hospital in England (opened 2015). The line is not a substantive policy lever but provides disclosure transparency under DHSC GAM 2024-25. Northumbria has held a CQC Outstanding rating and operates within the NENC ICB.",
    "sources": [
        {"publisher": "Northumbria Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northumbria.nhs.uk/about-us/corporate-information/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "North East and North Cumbria ICB system overview", "url": "https://www.northeastnorthcumbria.nhs.uk/"},
        {"publisher": "Care Quality Commission", "title": "Northumbria Healthcare provider profile (RTF)", "url": "https://www.cqc.org.uk/provider/RTF"},
        {"publisher": "HM Treasury", "title": "FReM 2024-25 ESA10 disclosure framework", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"}
    ],
    "related": [
        "Northumbria Healthcare NHS Foundation Trust",
        "Staff Costs",
        "Department of Health and Social Care",
        "NHS England"
    ]
}

NEW["Amortisation — Buckinghamshire Healthcare NHS Trust"] = {
    "aliases": [{"name": "Amortisation", "parent": "Buckinghamshire Healthcare NHS Trust"}],
    "description": "Buckinghamshire Healthcare NHS Trust's £0.21M amortisation line is the IAS 38 charge against intangible assets — chiefly capitalised software licences, EPR / clinical-system intangible components, and bespoke development costs at Stoke Mandeville Hospital, Wycombe Hospital and Amersham Hospital. The trust hosts the National Spinal Injuries Centre at Stoke Mandeville (largest in Europe) and provides acute and integrated community services across Buckinghamshire within the Bucks, Oxfordshire and Berkshire West (BOB) ICB.",
    "beneficiaries": "Acute inpatients across Stoke Mandeville (general acute + national spinal injuries), Wycombe Hospital (cardiac + minor injuries) and Amersham Hospital (rehab) plus integrated community services across Buckinghamshire (~550,000 pop); c. 6,500 WTE; c. 130,000 ED attendances/yr.",
    "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation programme guidance",
    "key_stats": [
        {"label": "Amortisation 2024-25", "value": "£0.21M"},
        {"label": "Asset class", "value": "Capitalised software (clinical systems, PAS, EPR components, theatre and pharmacy systems, bespoke dev)"},
        {"label": "Useful-life basis", "value": "3-7 years per IAS 38 / DHSC GAM ch.5 — straight-line amortisation"},
        {"label": "Site anchor", "value": "Stoke Mandeville (National Spinal Injuries Centre, ED), Wycombe Hospital, Amersham Hospital"},
        {"label": "EPR context", "value": "Frontline Digitisation programme — Bucks Healthcare in EPR adoption phase across BOB ICB digital convergence"},
        {"label": "Workforce", "value": "c. 6,500 WTE; c. 130,000 ED attendances/yr"},
        {"label": "Funding trajectory", "value": "Rising medium-term as Frontline Digitisation EPR capitalised intangibles enter service and amortise"},
        {"label": "Delivery body", "value": "Bucks Healthcare Digital + Finance + NHSE Frontline Digitisation Team + EPR vendors"},
        {"label": "Policy owner", "value": "NHSE Frontline Digitisation + DHSC + BOB ICB digital programme"},
        {"label": "Evaluation evidence", "value": "Bucks Healthcare ARA intangibles note; NAO Frontline Digitisation reporting; NHSE digital maturity assessment"},
        {"label": "Predecessor / successor", "value": "Predecessor: legacy clinical systems · Successor: post-EPR go-live amortisation step-up + cyber/security software amortisation"}
    ],
    "notes": "Bucks Healthcare's £0.21M amortisation is a small but rising line driven by EPR / digital-system capitalised software entering productive service. The trust is anchored on Stoke Mandeville Hospital and the National Spinal Injuries Centre — the largest spinal injuries centre in Europe and a tertiary referral destination — plus Wycombe Hospital and Amersham. Within BOB ICB the trust is participating in convergence around digital records and shared platforms; capitalised intangibles will scale as Frontline Digitisation projects complete. The line is one of several intangibles charges across the Premises & Infrastructure parent line and reflects standard IAS 38 straight-line amortisation over useful lives of 3-7 years.",
    "sources": [
        {"publisher": "Buckinghamshire Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.buckshealthcare.nhs.uk/about-us/who-we-are/annual-report/"},
        {"publisher": "Care Quality Commission", "title": "Bucks Healthcare provider profile (RXQ)", "url": "https://www.cqc.org.uk/provider/RXQ"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
        {"publisher": "NHS England", "title": "BOB ICB system overview", "url": "https://www.bucksoxonberksw.icb.nhs.uk/"}
    ],
    "related": [
        "Buckinghamshire Healthcare NHS Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Lease expenditure — East Sussex Healthcare NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "East Sussex Healthcare NHS Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at East Sussex Healthcare NHS Trust — covering short-life and low-value leased clinic, office and equipment estate held outside Right-of-Use balances under DHSC GAM treatment, plus operating leases on the trust's vehicle fleet supporting community nursing and integrated-community services across the dispersed East Sussex coastal and rural footprint anchored on Eastbourne DGH and Conquest Hospital (Hastings).",
    "beneficiaries": "Acute inpatients across Eastbourne District General Hospital (~470 beds) and Conquest Hospital, St Leonards (~440 beds), plus community hospital and clinic users across Bexhill, Rye and Uckfield; c. 540,000 East Sussex residents; c. 6,500 WTE; c. 160,000 ED attendances/yr.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.20M"},
        {"label": "Share of trust total opex", "value": "<0.1% of c. £600M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM"},
        {"label": "Site footprint", "value": "Eastbourne DGH, Conquest Hospital (Hastings), Bexhill Hospital, Rye Memorial, Uckfield Community Hospital + community clinics"},
        {"label": "Specific driver", "value": "Equipment hire (theatres, decant) + community-fleet operating leases + temp office leases for integrated-community teams"},
        {"label": "YoY change", "value": "c. +5-7% (lease re-pricing, post-pandemic community-fleet expansion tail)"},
        {"label": "Delivery body", "value": "ESHT Estates & Facilities + Procurement + NHSPS-leased clinics"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Sussex ICB"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift; community-services consolidation across Sussex ICB shapes vehicle-fleet share"},
        {"label": "Evaluation evidence", "value": "ESHT ARA leases disclosure; CQC inspection (RXC); NHSE Operational Plan returns; Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: continued GAM treatment of low-value/short-life items + Carbon Net Zero fleet electrification programme"}
    ],
    "notes": "ESHT's £0.20M lease line is a small recurring operational charge for items outside the IFRS 16 Right-of-Use threshold under DHSC GAM ch.7 — short-life equipment hire, low-value leases and minor fleet items. The trust's two-DGH model (Eastbourne and Conquest) plus integrated community footprint generates a long tail of small leased items across community clinics, vehicle fleet and temporary equipment. The trust operates within Sussex ICB alongside University Hospitals Sussex and Queen Victoria Hospital. Decant activity associated with Eastbourne DGH and Conquest estate refurbishment, plus community-services integration, drives modest year-on-year movement. CQC inspection history has tracked maternity service improvement.",
    "sources": [
        {"publisher": "East Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esht.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "ESHT provider profile (RXC)", "url": "https://www.cqc.org.uk/provider/RXC"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "FReM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "NHS England", "title": "Sussex ICB system overview", "url": "https://www.sussex.ics.nhs.uk/"}
    ],
    "related": [
        "East Sussex Healthcare NHS Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Inventories written down — North Middlesex University Hospital NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "North Middlesex University Hospital NHS Trust"}],
    "description": "North Middlesex University Hospital NHS Trust's £0.19M inventories-written-down line captures the IAS 2 charge for stock written off below net realisable value — chiefly time-expired pharmaceuticals (general acute drugs, anti-infectives, anaesthetic agents), expired theatre consumables and surgical kit, expired wound-care and IV stock, and obsolete bespoke implant inventory at the trust's North Middlesex Hospital site in Edmonton serving Enfield and Haringey populations.",
    "beneficiaries": "Acute inpatients across North Middlesex Hospital (~440 beds — A&E, maternity, paediatrics, general medicine, general surgery) plus integrated community services across Enfield and Haringey (~600,000 pop); c. 165,000 ED attendances/yr (one of London's busiest EDs); c. 3,800 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.19M"},
        {"label": "Site anchor", "value": "North Middlesex Hospital (Edmonton, Sterling Way) — single-site acute"},
        {"label": "Catchment", "value": "Enfield + Haringey + parts of Waltham Forest (~600,000); ED catchment among most deprived in London"},
        {"label": "ED throughput", "value": "c. 165,000 ED attendances/yr (one of London's busiest EDs)"},
        {"label": "Workforce", "value": "c. 3,800 WTE"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary), maternity + theatre consumables, wound-care, IV kits, implants"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + bespoke implant size mix obsolescence"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + London procurement collaboration + direct-to-supplier"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; potential RFL group-model integration savings post-merger discussions"},
        {"label": "Delivery body", "value": "North Mid Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North Central London ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "North Mid ARA inventories note; CQC inspection (RAP); NHSE Operational Plan returns; Model Hospital benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-NCL ICB pharmacy collaboration · Successor: deeper Royal Free London group-model integration (merger plan progressed) + EPR-driven stock visibility"}
    ],
    "notes": "North Middlesex's £0.19M write-down reflects routine IAS 2 NRV adjustment for an acute trust of this scale. The trust serves one of London's most deprived catchments and operates one of England's busiest single-site EDs. NHSE-supported plans for a deeper group-model integration with Royal Free London (NCL ICB) progressed through 2023-25, which is expected to compress duplicated stock and lift bulk-buying scale across pharmacy and procurement. Drivers include drug-price inflation on generic anti-infectives and analgesics, theatre kit obsolescence, and post-pandemic stockpile draw-down tail. Frontline Digitisation EPR rollout and Model Hospital benchmarking shape future trajectory.",
    "sources": [
        {"publisher": "North Middlesex University Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northmid.nhs.uk/annual-report-and-accounts"},
        {"publisher": "Care Quality Commission", "title": "North Middlesex provider profile (RAP)", "url": "https://www.cqc.org.uk/provider/RAP"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "North Central London ICB system overview", "url": "https://www.northcentrallondon.icb.nhs.uk/"}
    ],
    "related": [
        "North Middlesex University Hospital NHS Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "Royal Free London NHS Foundation Trust"
    ]
}

NEW["Lease expenditure — University Hospitals Plymouth NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "University Hospitals Plymouth NHS Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at University Hospitals Plymouth NHS Trust — covering short-life and low-value leased clinic, office and equipment estate held outside Right-of-Use balances under DHSC GAM treatment, plus operating leases on the trust's vehicle fleet supporting acute and tertiary services at Derriford Hospital and a wide referral network across Devon, Cornwall, the Isles of Scilly and the South West peninsula.",
    "beneficiaries": "Acute and tertiary inpatients across Derriford Hospital (~1,050 beds — major trauma centre, vascular, neurosurgery, cardiothoracic, oncology, transplant) plus outreach clinics across the South West peninsula serving c. 2M referral catchment; c. 9,500 WTE; c. 130,000 ED attendances/yr.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.19M"},
        {"label": "Share of trust total opex", "value": "<0.05% of c. £900M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU"},
        {"label": "Site footprint", "value": "Derriford Hospital (Plymouth) + Mount Gould + REI Eye Infirmary + outreach clinics across Devon and Cornwall"},
        {"label": "Specific driver", "value": "Equipment hire (theatres, decant, modular wards), peninsula outreach-clinic leases, vehicle fleet"},
        {"label": "Major Trauma Centre", "value": "Designated South West Peninsula MTC — only acute MTC for c. 2M peninsula population"},
        {"label": "Tertiary services", "value": "Neurosurgery, cardiothoracic, vascular, oncology (incl. proton beam tertiary referrals), renal transplant"},
        {"label": "Delivery body", "value": "UHP Estates & Facilities + Procurement + NHSPS-leased clinics"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Devon ICB"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift; New Hospital Programme (NHP) Reset Jan 2025 deferral lifts ongoing decant and equipment-hire share"},
        {"label": "Evaluation evidence", "value": "UHP ARA leases disclosure; CQC inspection (RK9); NHSE Operational Plan returns; NAO MTC reporting"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: continued GAM treatment + NHP rebuild capex once activated"}
    ],
    "notes": "UHP's £0.19M lease line is a small recurring operational charge for items outside the IFRS 16 Right-of-Use threshold. The trust runs Derriford — the largest acute hospital in the South West peninsula — and is the designated Major Trauma Centre, vascular and neurosurgery centre and tertiary referral anchor for c. 2M people across Devon, Cornwall and the Isles of Scilly. The trust was named in the original New Hospital Programme cohort; the Jan 2025 Reset deferred its rebuild beyond 2030, lifting decant- and equipment-hire-related operational pressure including the lease line. The trust also runs significant peninsula outreach clinics, contributing to a long tail of small estate and fleet leases.",
    "sources": [
        {"publisher": "University Hospitals Plymouth NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.plymouthhospitals.nhs.uk/about-us/our-publications/"},
        {"publisher": "Care Quality Commission", "title": "UHP provider profile (RK9)", "url": "https://www.cqc.org.uk/provider/RK9"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Review (Jan 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
        {"publisher": "NHS England", "title": "Devon ICB system overview", "url": "https://onedevon.org.uk/"}
    ],
    "related": [
        "University Hospitals Plymouth NHS Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Business rates — Ashford and St Peter's Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Business rates", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
    "description": "Ashford and St Peter's Hospitals NHSFT's £0.19M business rates line is the non-domestic rates (NDR) charge against the trust's hereditaments — chiefly Ashford Hospital (Ashford) and St Peter's Hospital (Chertsey) plus satellite estate. The charge is set under the Local Government Finance Act 1988 (Schedule 6) at the small business multiplier × rateable value as determined by the Valuation Office Agency, with revaluation effective from 1 April 2023 and the 2024 Multipliers Act provisions feeding the latest year-on-year movement.",
    "beneficiaries": "Acute inpatients across Ashford Hospital (Ashford, Surrey — day-case + outpatients) and St Peter's Hospital (Chertsey — main acute, ED, maternity, paediatrics, T&O); c. 410,000 catchment across north-west Surrey + south Berkshire; c. 4,200 WTE.",
    "legal_basis": "Local Government Finance Act 1988 Sch 6 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Valuation Office Agency 2023 rating list",
    "key_stats": [
        {"label": "Business rates 2024-25", "value": "£0.19M"},
        {"label": "Multiplier basis", "value": "Standard / small business non-domestic rating multiplier × rateable value (2023 list)"},
        {"label": "VOA revaluation", "value": "Effective 1 April 2023 — 2023 rating list applies through 2026 revaluation"},
        {"label": "2024 Act", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — multiplier reform feeds 2024-25"},
        {"label": "Site footprint", "value": "Ashford Hospital + St Peter's Hospital (Chertsey) + community satellite clinics"},
        {"label": "Catchment", "value": "c. 410,000 across north-west Surrey + south Berkshire"},
        {"label": "Workforce", "value": "c. 4,200 WTE"},
        {"label": "Trust ratepayer status", "value": "NHS trusts pay full business rates without charitable relief — unlike voluntary-aided providers"},
        {"label": "Funding trajectory", "value": "Step-up at 2023 revaluation reflecting Surrey hereditament value uplift; further movement at 2026 revaluation"},
        {"label": "Delivery body", "value": "ASPH Estates + Finance + billing local authorities (Spelthorne BC, Runnymede BC) + VOA"},
        {"label": "Policy owner", "value": "DHSC + DLUHC (now MHCLG) + HM Treasury (multiplier policy) + Surrey Heartlands ICB"},
        {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list · Successor: 2026 revaluation cycle + ongoing 2024 Act multiplier-reform implementation"}
    ],
    "notes": "ASPH's £0.19M business rates line is a recurring statutory charge billed by Spelthorne and Runnymede Borough Councils against the trust's two main hospital sites and satellite community estate at rateable values set in the 2023 VOA rating list. NHS trusts do not benefit from charitable rates relief, so the full liability flows through. The 2023 revaluation lifted hereditament values in much of Surrey, and the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 has reshaped multiplier policy with implications for the 2024-25 charge. The line will step again at the 2026 revaluation cycle. ASPH operates in Surrey Heartlands ICB and is part of an emerging strategic discussion around acute services in north-west Surrey.",
    "sources": [
        {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ashfordstpeters.nhs.uk/about-us"},
        {"publisher": "Valuation Office Agency", "title": "2023 Rating List — non-domestic rates", "url": "https://www.gov.uk/correct-your-business-rates"},
        {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/19/contents"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Surrey Heartlands ICB system overview", "url": "https://www.surreyheartlands.nhs.uk/"}
    ],
    "related": [
        "Ashford and St Peter's Hospitals NHS Foundation Trust",
        "Premises & Infrastructure",
        "Department of Health and Social Care",
        "Ministry of Housing, Communities and Local Government"
    ]
}

NEW["Termination & post-employment — Nottingham University Hospitals NHS Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "Nottingham University Hospitals NHS Trust"}],
    "description": "Nottingham University Hospitals NHS Trust's £0.19M Termination & post-employment line covers IAS 19 charges for severance, MARS-style voluntary exits, contractual notice and redundancy obligations, plus post-employment medical-cover and pension-related residual costs net of NHS Pension Scheme employer recharge. NUH runs Queen's Medical Centre and Nottingham City Hospital — the East Midlands' largest acute teaching trust and Major Trauma Centre.",
    "beneficiaries": "Indirect — exit and post-employment costs affect leaving WTE rather than direct service recipients; trust serves c. 2.5M East Midlands referral catchment across Nottinghamshire, southern Derbyshire and parts of Lincolnshire/Leicestershire; QMC is the regional Major Trauma Centre; c. 17,500 WTE total.",
    "legal_basis": "IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 (revoked Feb 2021 — voluntary cap framework) · NHS Pension Scheme Regulations 2015 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.19M"},
        {"label": "Composition", "value": "Statutory + contractual redundancy + MARS-style voluntary exits + post-employment medical cover + pension residuals"},
        {"label": "Trust scale", "value": "c. 17,500 WTE — one of England's largest acute teaching trusts"},
        {"label": "Site footprint", "value": "Queen's Medical Centre (QMC, Nottingham) + Nottingham City Hospital + Ropewalk House"},
        {"label": "Major Trauma Centre", "value": "East Midlands MTC at QMC — only adult MTC for c. 4.5M peninsula population"},
        {"label": "Tertiary services", "value": "Neurosciences, cardiothoracic, hepatobiliary, oncology, transplantation (kidney + bone marrow), paediatric quaternary"},
        {"label": "Recent context", "value": "CQC inadequate rating (maternity 2023); CEO change 2023; Donna Ockenden review of maternity ongoing"},
        {"label": "Funding trajectory", "value": "Variable; reorg / restructure activity around maternity transformation lifts 2024-25 share; 2025 £5k NIC threshold step-up impacts forward periods"},
        {"label": "Delivery body", "value": "NUH HR + Finance + NHS Business Services Authority (pension recharge) + NHSE Provider Finance"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Nottingham and Nottinghamshire ICB + HM Treasury exit policy"},
        {"label": "Evaluation evidence", "value": "NUH ARA Note 8; NAO Public Sector Exit Payments review; CQC reports; Donna Ockenden NUH maternity review"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 Public Sector Exit Payments cap framework · Successor: continuing IAS 19 disclosure + 2025 employer-NIC threshold cost feed"}
    ],
    "notes": "NUH's £0.19M Termination & post-employment line covers contractual exit obligations, MARS-style voluntary leavers and post-employment residuals at one of England's largest acute teaching trusts. The trust has been the focus of significant reform since the CQC inadequate maternity rating in 2023, the appointment of a new CEO and the ongoing Donna Ockenden review of maternity care; reorganisation activity at scale lifts exit-cost volume, though the line itself remains small relative to trust scale. NUH operates as East Midlands MTC and tertiary teaching anchor across Nottinghamshire, southern Derbyshire and adjacent counties; the April 2025 employer NIC step-up will feed forward-period employer costs.",
    "sources": [
        {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nuh.nhs.uk/annual-report-and-accounts"},
        {"publisher": "Care Quality Commission", "title": "NUH provider profile (RX1)", "url": "https://www.cqc.org.uk/provider/RX1"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Donna Ockenden Review", "title": "Independent Review of Maternity Services at NUH", "url": "https://www.ockendenmaternityreview.org.uk/"},
        {"publisher": "NHS England", "title": "Nottingham and Nottinghamshire ICB system overview", "url": "https://notts.icb.nhs.uk/"}
    ],
    "related": [
        "Nottingham University Hospitals NHS Trust",
        "Staff Costs",
        "NHS Pension Scheme",
        "Department of Health and Social Care"
    ]
}

NEW["Lease expenditure — Ashford and St Peter's Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at Ashford and St Peter's Hospitals NHSFT — covering short-life and low-value leased clinic, office and equipment estate held outside Right-of-Use balances under DHSC GAM treatment, plus operating leases on the trust's vehicle fleet supporting the dual-site Ashford Hospital and St Peter's Hospital (Chertsey) acute and outpatient delivery footprint across north-west Surrey and south Berkshire.",
    "beneficiaries": "Acute inpatients across Ashford Hospital (Ashford — day-case + outpatients) and St Peter's Hospital (Chertsey — main acute, ED, maternity, paediatrics, T&O); c. 410,000 catchment across north-west Surrey + south Berkshire; c. 4,200 WTE; c. 105,000 ED attendances/yr.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.19M"},
        {"label": "Share of trust total opex", "value": "<0.05% of c. £450M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM"},
        {"label": "Site footprint", "value": "Ashford Hospital (Ashford) + St Peter's Hospital (Chertsey) + community/outpatient satellites"},
        {"label": "Specific driver", "value": "Equipment hire (theatres + decant during St Peter's redevelopment) + vehicle fleet + temp office leases"},
        {"label": "YoY change", "value": "c. +5-7% (lease re-pricing tail; decant volume associated with St Peter's redevelopment programme)"},
        {"label": "Delivery body", "value": "ASPH Estates & Facilities + Procurement + NHSPS-leased clinics"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Surrey Heartlands ICB"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift; St Peter's redevelopment programme drives equipment-hire share; NHP cohort interactions"},
        {"label": "Evaluation evidence", "value": "ASPH ARA leases disclosure; CQC inspection (RTK); NHSE Operational Plan returns; Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: continued GAM treatment of low-value/short-life items + Carbon Net Zero fleet electrification"}
    ],
    "notes": "ASPH's £0.19M lease line is a small recurring operational charge for items outside the IFRS 16 Right-of-Use threshold under DHSC GAM ch.7. The trust runs a dual-site model — Ashford Hospital (largely day-case and outpatients) and St Peter's Hospital (the main acute site at Chertsey) — and is exploring a major estate redevelopment programme driving decant and equipment-hire activity. ASPH operates within Surrey Heartlands ICB and is part of strategic discussions around acute service consolidation in north-west Surrey alongside neighbouring trusts. Carbon Net Zero fleet electrification is gradually shifting the vehicle-lease share from ICE to BEV. The line tracks the trust's c. £450M operating cost base.",
    "sources": [
        {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ashfordstpeters.nhs.uk/about-us"},
        {"publisher": "Care Quality Commission", "title": "ASPH provider profile (RTK)", "url": "https://www.cqc.org.uk/provider/RTK"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "FReM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "NHS England", "title": "Surrey Heartlands ICB system overview", "url": "https://www.surreyheartlands.nhs.uk/"}
    ],
    "related": [
        "Ashford and St Peter's Hospitals NHS Foundation Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Inventories written down — Royal Free London NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Royal Free London NHS Foundation Trust"}],
    "description": "Royal Free London NHSFT's £0.18M inventories-written-down line captures the IAS 2 charge for stock written off below net realisable value across the trust's group-model footprint — chiefly time-expired pharmaceuticals (general acute drugs, anti-infectives, anaesthetic agents, biologics, immunosuppressants for transplantation), expired theatre consumables, expired wound-care and IV stock, and obsolete bespoke implant inventory across Royal Free Hospital (Hampstead), Barnet Hospital and Chase Farm Hospital sites.",
    "beneficiaries": "Acute and tertiary inpatients across Royal Free Hospital (~830 beds — liver/renal transplant, HIV, infectious diseases, vascular, hepatobiliary), Barnet Hospital (~440 beds — general acute, ED, maternity), Chase Farm Hospital (elective + day-case); c. 1.6M catchment across north-central and north-west London; c. 11,000 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.18M"},
        {"label": "Site anchor", "value": "Royal Free Hospital (Hampstead) + Barnet Hospital + Chase Farm Hospital + community sites"},
        {"label": "Catchment", "value": "c. 1.6M across north-central and north-west London (Camden, Islington, Barnet, Enfield, Haringey)"},
        {"label": "Workforce", "value": "c. 11,000 WTE"},
        {"label": "Stock profile", "value": "High-value biologics + immunosuppressants (transplant) + anti-infectives + theatre consumables + bespoke implants + HIV/HCV antivirals"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover specialist drugs + immunosuppressant batch obsolescence + theatre kit obsolescence + bespoke implant size mix"},
        {"label": "Group model", "value": "Royal Free London Group — joint procurement and pharmacy with North Mid plans (NHSE-supported integration progressing)"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + London procurement collaboration + direct-to-supplier (specialist + ATMP)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift; group-model integration with North Mid expected to compress write-downs medium-term"},
        {"label": "Delivery body", "value": "Royal Free Group Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North Central London ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "Royal Free ARA inventories note; CQC inspection (RAL); NHSE Operational Plan returns; Model Hospital benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-group-model standalone procurement · Successor: deeper Royal Free London Group + North Middlesex integration + EPR-driven stock visibility"}
    ],
    "notes": "Royal Free London's £0.18M write-down is small relative to the trust's c. £1.6B operating cost base and its complex tertiary-services portfolio. The trust hosts nationally significant transplantation services (liver, kidney) and HIV/infectious diseases, both of which carry low-turnover, high-value drug stock with non-negligible expiry exposure. The Royal Free London Group operating model has been extending toward deeper integration with North Middlesex University Hospital NHS Trust under NHSE-supported group arrangements, expected to lift bulk-buying scale and compress duplicated stock medium term. Frontline Digitisation EPR rollout improves stock visibility and Model Hospital benchmarking drives Carter-style efficiency.",
    "sources": [
        {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information-and-publications"},
        {"publisher": "Care Quality Commission", "title": "Royal Free London provider profile (RAL)", "url": "https://www.cqc.org.uk/provider/RAL"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "North Central London ICB system overview", "url": "https://www.northcentrallondon.icb.nhs.uk/"}
    ],
    "related": [
        "Royal Free London NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "North Middlesex University Hospital NHS Trust"
    ]
}

NEW["Termination & post-employment — University Hospitals Bristol and Weston NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "University Hospitals Bristol and Weston NHS Foundation Trust"}],
    "description": "University Hospitals Bristol and Weston NHSFT's £0.18M Termination & post-employment line covers IAS 19 charges for severance, MARS-style voluntary exits, contractual notice and redundancy obligations, plus post-employment medical-cover and pension-related residual costs net of NHS Pension Scheme employer recharge. UHBW is a tertiary-acute teaching trust formed by the April 2020 merger of UHB with Weston Area Health, running BRI, BRHC, St Michael's, BHI, BEH, BDH and Weston General.",
    "beneficiaries": "Indirect — exit and post-employment costs affect leaving WTE rather than direct service recipients; trust serves c. 1.0M Bristol, North Somerset and South Gloucestershire pop with c. 4M outpatient/inpatient/day-case contacts/yr; c. 14,000 WTE across 9 sites.",
    "legal_basis": "IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 (revoked Feb 2021) · NHS Pension Scheme Regulations 2015 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.18M"},
        {"label": "Composition", "value": "Statutory + contractual redundancy + MARS-style voluntary exits + post-employment medical cover + pension residuals"},
        {"label": "Trust scale", "value": "c. 14,000 WTE across 9 sites"},
        {"label": "Site footprint", "value": "BRI, BRHC, St Michael's, BHI, BEH, BDH, Weston General, South Bristol Community Hospital + satellites"},
        {"label": "Tertiary services", "value": "Paediatric quaternary (BRHC), cardiothoracic (BHI), ophthalmology (BEH), dental (BDH), congenital cardiac"},
        {"label": "Recent context", "value": "Apr 2020 UHB+Weston merger integration tail; CQC reviews of children's cardiac services; consultant-strikes 2023 backfill"},
        {"label": "Funding trajectory", "value": "Variable; integration tail post-Weston merger drives 2020-25 share; 2025 £5k NIC threshold step-up impacts forward periods"},
        {"label": "Delivery body", "value": "UHBW HR + Finance + NHS Business Services Authority (pension recharge) + NHSE Provider Finance"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Bristol, North Somerset and South Gloucestershire (BNSSG) ICB + HM Treasury exit policy"},
        {"label": "Evaluation evidence", "value": "UHBW ARA Note 8; NAO Public Sector Exit Payments review; CQC reports (RA7); ICB integration assessment"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 standalone UHB + Weston exit costs · Successor: post-merger residuals tapering + 2025 employer-NIC threshold cost feed"}
    ],
    "notes": "UHBW's £0.18M Termination & post-employment line covers contractual exit obligations, voluntary leavers and post-employment residuals at a complex 9-site teaching trust formed by the April 2020 merger of UHB with Weston Area Health. The merger integration tail — combining payroll, terms and conditions, and management structures across the original UHB tertiary footprint and Weston General's recovery plan — has elevated exit-cost activity through 2020-25. UHBW operates within BNSSG ICB and is a tertiary specialist anchor for paediatrics (BRHC), cardiothoracic (BHI) and ophthalmology (BEH). The April 2025 employer NIC step-up will lift forward-period employer costs.",
    "sources": [
        {"publisher": "University Hospitals Bristol and Weston NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhbw.nhs.uk/about-us/annual-report-and-accounts"},
        {"publisher": "Care Quality Commission", "title": "UHBW provider profile (RA7)", "url": "https://www.cqc.org.uk/provider/RA7"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guide", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
        {"publisher": "NHS England", "title": "BNSSG ICB system overview", "url": "https://bnssg.icb.nhs.uk/"}
    ],
    "related": [
        "University Hospitals Bristol and Weston NHS Foundation Trust",
        "Staff Costs",
        "NHS Pension Scheme",
        "Department of Health and Social Care"
    ]
}

NEW["Inventories written down — Mid and South Essex NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Mid and South Essex NHS Foundation Trust"}],
    "description": "Mid and South Essex NHSFT's £0.18M inventories-written-down line captures the IAS 2 charge for stock written off below net realisable value across the merged trust's three-site footprint — Basildon University Hospital, Broomfield Hospital (Chelmsford) and Southend University Hospital. Stock comprises time-expired pharmaceuticals (general acute drugs, anti-infectives, anaesthetic agents), expired theatre consumables and surgical kit (incl. cardiothoracic at Basildon), expired wound-care and IV stock, and obsolete bespoke implant inventory.",
    "beneficiaries": "Acute inpatients across Basildon (~530 beds — cardiothoracic centre, ED), Broomfield (~580 beds — burns + plastics tertiary, ED), Southend (~620 beds — ED, cancer); c. 1.2M catchment across mid and south Essex; c. 14,500 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.18M"},
        {"label": "Site anchor", "value": "Basildon University Hospital + Broomfield Hospital (Chelmsford) + Southend University Hospital — formed Apr 2020 by 3-trust merger"},
        {"label": "Catchment", "value": "c. 1.2M across mid + south Essex (Basildon, Brentwood, Castle Point, Chelmsford, Maldon, Rochford, Southend)"},
        {"label": "Workforce", "value": "c. 14,500 WTE"},
        {"label": "Stock profile", "value": "Generic + branded drugs + cardiothoracic implants (Basildon) + burns/plastics consumables (Broomfield) + general theatre + wound-care"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover specialist drugs + cardiothoracic implant size mix + post-merger pharmacy harmonisation tail"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + East of England procurement collaboration + direct-to-supplier (cardiothoracic, burns)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; merger integration tail compressing toward consolidated stock"},
        {"label": "Delivery body", "value": "MSE Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Mid and South Essex ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "MSE ARA inventories note; CQC inspection (RAJ); NHSE Operational Plan returns; Model Hospital procurement benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 standalone Basildon, Broomfield (Mid Essex) and Southend procurement · Successor: NHP rebuild plans (Basildon original cohort) + EPR-driven stock visibility"}
    ],
    "notes": "MSE's £0.18M write-down reflects routine IAS 2 NRV adjustment for an acute trust formed by the April 2020 merger of Basildon and Thurrock, Mid Essex and Southend. The trust hosts the regional cardiothoracic centre at Basildon and the regional burns and plastics unit at Broomfield, both of which carry low-turnover, high-value specialist stock with non-negligible expiry exposure. Post-merger pharmacy harmonisation across the three legacy formularies has been a multi-year exercise. Basildon is in the New Hospital Programme cohort with rebuild scheduling deferred under the Jan 2025 Reset. Frontline Digitisation EPR rollout improves stock visibility.",
    "sources": [
        {"publisher": "Mid and South Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://mse.nhs.uk/about-us/our-publications/"},
        {"publisher": "Care Quality Commission", "title": "MSE provider profile (RAJ)", "url": "https://www.cqc.org.uk/provider/RAJ"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "Mid and South Essex ICB system overview", "url": "https://www.midandsouthessex.ics.nhs.uk/"}
    ],
    "related": [
        "Mid and South Essex NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "New Hospital Programme"
    ]
}

NEW["Termination & post-employment — Northampton General Hospital NHS Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "Northampton General Hospital NHS Trust"}],
    "description": "Northampton General Hospital NHS Trust's £0.18M Termination & post-employment line covers IAS 19 charges for severance, MARS-style voluntary exits, contractual notice and redundancy obligations, plus post-employment medical-cover and pension-related residual costs net of NHS Pension Scheme employer recharge. NGH runs the main Northampton General site as the south Northamptonshire acute and ED anchor and is in a group-model arrangement with Kettering General Hospital under University Hospitals of Northamptonshire (UHN).",
    "beneficiaries": "Indirect — exit and post-employment costs affect leaving WTE rather than direct service recipients; trust serves c. 380,000 south Northamptonshire pop with c. 100,000 ED attendances/yr; c. 5,300 WTE.",
    "legal_basis": "IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 (revoked Feb 2021) · NHS Pension Scheme Regulations 2015 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.18M"},
        {"label": "Composition", "value": "Statutory + contractual redundancy + MARS-style voluntary exits + post-employment medical cover + pension residuals"},
        {"label": "Trust scale", "value": "c. 5,300 WTE"},
        {"label": "Site footprint", "value": "Northampton General Hospital (Cliftonville) + community satellites"},
        {"label": "Group model", "value": "University Hospitals of Northamptonshire (UHN) — single CEO and joint group model with Kettering General Hospital NHSFT"},
        {"label": "Catchment", "value": "c. 380,000 south Northamptonshire (Northampton, South Northants, Daventry)"},
        {"label": "Recent context", "value": "UHN group integration (joint exec since 2021); industrial action 2023-24 backfill agency cost feed; CQC focused inspections"},
        {"label": "Funding trajectory", "value": "Variable; UHN integration tail drives 2022-25 share; 2025 £5k NIC threshold step-up impacts forward periods"},
        {"label": "Delivery body", "value": "NGH HR + Finance + UHN joint exec + NHS Business Services Authority (pension recharge)"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Northamptonshire ICB + HM Treasury exit policy"},
        {"label": "Evaluation evidence", "value": "NGH ARA Note 8; NAO Public Sector Exit Payments review; CQC reports (RNS); UHN group integration assessment"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-UHN standalone NGH exit costs · Successor: deeper UHN consolidation + 2025 employer-NIC threshold cost feed"}
    ],
    "notes": "NGH's £0.18M Termination & post-employment line covers contractual exit obligations, voluntary leavers and post-employment residuals at the south Northamptonshire acute anchor. The trust has been in a group-model arrangement with Kettering General Hospital NHSFT under University Hospitals of Northamptonshire (UHN) since 2021, sharing a single CEO and joint executive — driving integration-related restructure activity that lifts exit-cost volume. Industrial action 2023-24 and the April 2025 employer NIC step-up shape forward-period costs. NGH operates within Northamptonshire ICB and CQC inspections have tracked maternity and emergency-care service improvement.",
    "sources": [
        {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northamptongeneral.nhs.uk/About/Trust-Publications.aspx"},
        {"publisher": "Care Quality Commission", "title": "Northampton General provider profile (RNS)", "url": "https://www.cqc.org.uk/provider/RNS"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guide", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
        {"publisher": "NHS England", "title": "Northamptonshire ICB system overview", "url": "https://www.northamptonshire.icb.nhs.uk/"}
    ],
    "related": [
        "Northampton General Hospital NHS Trust",
        "Staff Costs",
        "Kettering General Hospital NHS Foundation Trust",
        "NHS Pension Scheme"
    ]
}

NEW["Inventories written down — East Suffolk and North Essex NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
    "description": "East Suffolk and North Essex NHSFT's £0.17M inventories-written-down line captures the IAS 2 charge for stock written off below net realisable value across the merged trust's two-DGH footprint — Ipswich Hospital (Suffolk) and Colchester Hospital (Essex). Stock comprises time-expired pharmaceuticals (general acute drugs, anti-infectives, anaesthetic agents), expired theatre consumables and surgical kit, expired wound-care and IV stock, and obsolete bespoke implant inventory.",
    "beneficiaries": "Acute inpatients across Ipswich Hospital (~525 beds — ED, maternity, paediatrics, T&O, oncology) and Colchester Hospital (~700 beds — ED, maternity, T&O, oncology); c. 800,000 catchment across east Suffolk and north Essex (Ipswich, Felixstowe, Woodbridge, Colchester, Clacton, Tendring); c. 11,000 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.17M"},
        {"label": "Site anchor", "value": "Ipswich Hospital + Colchester Hospital — formed July 2018 by merger of Ipswich Hospital NHS Trust + Colchester Hospital University NHSFT"},
        {"label": "Catchment", "value": "c. 800,000 across east Suffolk + north Essex"},
        {"label": "Workforce", "value": "c. 11,000 WTE"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary) + theatre consumables + wound-care + IV kits + implants"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + post-merger pharmacy harmonisation tail"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + East of England procurement collaboration + direct-to-supplier"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; merger integration tail compressing toward consolidated stock"},
        {"label": "Delivery body", "value": "ESNEFT Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Suffolk and North East Essex ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "ESNEFT ARA inventories note; CQC inspection (RDE); NHSE Operational Plan returns; Model Hospital benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 Ipswich Hospital + Colchester procurement · Successor: deeper SNEE ICB pharmacy harmonisation + EPR-driven stock visibility"}
    ],
    "notes": "ESNEFT's £0.17M write-down reflects routine IAS 2 NRV adjustment for an acute trust formed by the July 2018 merger of Ipswich Hospital NHS Trust and Colchester Hospital University NHSFT — one of the earliest large acute-acute mergers under the NHS Long Term Plan provider-collaboration agenda. Post-merger pharmacy harmonisation across the legacy formularies has been a multi-year exercise. The trust operates within the Suffolk and North East Essex ICB and is part of strategic discussions around acute service consolidation across two-DGH systems. Frontline Digitisation EPR rollout improves stock visibility and Model Hospital benchmarking drives Carter-style efficiency.",
    "sources": [
        {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "ESNEFT provider profile (RDE)", "url": "https://www.cqc.org.uk/provider/RDE"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "Suffolk and North East Essex ICB system overview", "url": "https://suffolkandnortheastessex.icb.nhs.uk/"}
    ],
    "related": [
        "East Suffolk and North Essex NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "NHS England"
    ]
}

NEW["Inventories written down — Buckinghamshire Healthcare NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Buckinghamshire Healthcare NHS Trust"}],
    "description": "Buckinghamshire Healthcare NHS Trust's £0.16M inventories-written-down line captures the IAS 2 charge for stock written off below net realisable value across the trust's main acute and specialist sites — Stoke Mandeville Hospital (host to the National Spinal Injuries Centre), Wycombe Hospital and Amersham Hospital. Stock comprises time-expired pharmaceuticals (general acute drugs, anti-infectives, anaesthetic agents, spinal-injury catheterisation supplies), expired theatre consumables, expired wound-care and IV stock, and obsolete bespoke implant inventory.",
    "beneficiaries": "Acute inpatients across Stoke Mandeville (general acute + national spinal injuries — Europe's largest), Wycombe Hospital (cardiac + minor injuries) and Amersham Hospital (rehab) plus integrated community services across Buckinghamshire (~550,000 pop); c. 6,500 WTE; c. 130,000 ED attendances/yr.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.16M"},
        {"label": "Site anchor", "value": "Stoke Mandeville Hospital (incl. National Spinal Injuries Centre) + Wycombe Hospital + Amersham Hospital"},
        {"label": "Catchment", "value": "c. 550,000 Buckinghamshire residents + national spinal-injury referrals"},
        {"label": "Workforce", "value": "c. 6,500 WTE; c. 130,000 ED attendances/yr"},
        {"label": "Stock profile", "value": "Generic + branded drugs + spinal-injury specialist catheterisation/bowel-care + theatre + wound-care + bespoke implants"},
        {"label": "Specialist driver", "value": "National Spinal Injuries Centre carries low-turnover specialist consumables with non-negligible expiry exposure"},
        {"label": "Write-down driver", "value": "Time-expiry of specialist drugs/consumables + theatre kit obsolescence + bespoke implant size-mix"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + Thames Valley collaborative + direct-to-supplier (specialist spinal-injury kit)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; BOB ICB pharmacy collaboration driving medium-term consolidation"},
        {"label": "Delivery body", "value": "Bucks Healthcare Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Bucks, Oxfordshire and Berkshire West (BOB) ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "Bucks Healthcare ARA inventories note; CQC inspection (RXQ); NHSE Operational Plan returns; Model Hospital benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-BOB ICB pharmacy collaboration · Successor: deeper Thames Valley pharmacy harmonisation + EPR-driven stock visibility"}
    ],
    "notes": "Bucks Healthcare's £0.16M write-down reflects routine IAS 2 NRV adjustment for an acute trust of this scale. The trust hosts the National Spinal Injuries Centre at Stoke Mandeville — Europe's largest spinal injuries centre and a tertiary referral destination — which carries a long tail of low-turnover specialist catheterisation, bowel-care, splinting and pressure-relieving stock with non-negligible expiry exposure. Drivers include drug-price inflation on generic anti-infectives and analgesics, theatre kit obsolescence, and ongoing BOB ICB pharmacy harmonisation tail. Frontline Digitisation EPR rollout improves stock visibility and Model Hospital benchmarking drives Carter-style efficiency.",
    "sources": [
        {"publisher": "Buckinghamshire Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.buckshealthcare.nhs.uk/about-us/who-we-are/annual-report/"},
        {"publisher": "Care Quality Commission", "title": "Bucks Healthcare provider profile (RXQ)", "url": "https://www.cqc.org.uk/provider/RXQ"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "BOB ICB system overview", "url": "https://www.bucksoxonberksw.icb.nhs.uk/"}
    ],
    "related": [
        "Buckinghamshire Healthcare NHS Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "NHS England"
    ]
}

NEW["Termination & post-employment — Kettering General Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "Kettering General Hospital NHS Foundation Trust"}],
    "description": "Kettering General Hospital NHSFT's £0.16M Termination & post-employment line covers IAS 19 charges for severance, MARS-style voluntary exits, contractual notice and redundancy obligations, plus post-employment medical-cover and pension-related residual costs net of NHS Pension Scheme employer recharge. KGH runs the main Kettering General Hospital site as the north Northamptonshire acute and ED anchor, in a group-model arrangement with Northampton General Hospital under University Hospitals of Northamptonshire (UHN).",
    "beneficiaries": "Indirect — exit and post-employment costs affect leaving WTE rather than direct service recipients; trust serves c. 320,000 north Northamptonshire pop (Kettering, Corby, Wellingborough, East Northants); c. 4,200 WTE; c. 95,000 ED attendances/yr.",
    "legal_basis": "IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 (revoked Feb 2021) · NHS Pension Scheme Regulations 2015 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.16M"},
        {"label": "Composition", "value": "Statutory + contractual redundancy + MARS-style voluntary exits + post-employment medical cover + pension residuals"},
        {"label": "Trust scale", "value": "c. 4,200 WTE"},
        {"label": "Site footprint", "value": "Kettering General Hospital + Corby Urgent Care Centre + community satellites"},
        {"label": "Group model", "value": "University Hospitals of Northamptonshire (UHN) — single CEO and joint group model with Northampton General Hospital"},
        {"label": "Catchment", "value": "c. 320,000 north Northamptonshire (Kettering, Corby, Wellingborough, East Northants)"},
        {"label": "Recent context", "value": "UHN group integration (joint exec since 2021); industrial action 2023-24 backfill agency cost feed; NHP cohort (Kettering rebuild deferred)"},
        {"label": "Funding trajectory", "value": "Variable; UHN integration tail drives 2022-25 share; 2025 £5k NIC threshold step-up impacts forward periods"},
        {"label": "Delivery body", "value": "KGH HR + Finance + UHN joint exec + NHS Business Services Authority (pension recharge)"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Northamptonshire ICB + HM Treasury exit policy"},
        {"label": "Evaluation evidence", "value": "KGH ARA Note 8; NAO Public Sector Exit Payments review; CQC reports (RNQ); UHN group integration assessment"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-UHN standalone KGH exit costs · Successor: deeper UHN consolidation + 2025 employer-NIC threshold cost feed"}
    ],
    "notes": "KGH's £0.16M Termination & post-employment line covers contractual exit obligations, voluntary leavers and post-employment residuals at the north Northamptonshire acute anchor. The trust has been in a group-model arrangement with Northampton General Hospital under University Hospitals of Northamptonshire (UHN) since 2021, sharing a single CEO and joint executive — driving integration-related restructure activity. Kettering is also part of the New Hospital Programme cohort with rebuild scheduling deferred under the Jan 2025 Reset, lifting decant- and reorganisation-related staffing pressure. Industrial action 2023-24 and the April 2025 employer NIC step-up shape forward-period costs.",
    "sources": [
        {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/our-publications"},
        {"publisher": "Care Quality Commission", "title": "Kettering General provider profile (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Review (Jan 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
        {"publisher": "NHS England", "title": "Northamptonshire ICB system overview", "url": "https://www.northamptonshire.icb.nhs.uk/"}
    ],
    "related": [
        "Kettering General Hospital NHS Foundation Trust",
        "Staff Costs",
        "Northampton General Hospital NHS Trust",
        "NHS Pension Scheme"
    ]
}

NEW["Amortisation — Southport And Ormskirk Hospital NHS Trust"] = {
    "aliases": [{"name": "Amortisation", "parent": "Southport And Ormskirk Hospital NHS Trust"}],
    "description": "Southport And Ormskirk Hospital NHS Trust's £0.16M amortisation line is the IAS 38 charge against intangible assets — chiefly capitalised software licences, EPR / clinical-system intangible components and bespoke development costs at Southport District General Hospital and Ormskirk District General Hospital. The trust is in a transition phase: its acute services are being transferred to Mersey and West Lancashire Teaching Hospitals NHSFT (and women's and children's services to Liverpool Women's / Alder Hey) under reconfiguration plans agreed in 2023-24.",
    "beneficiaries": "Acute inpatients across Southport DGH (~310 beds — ED, T&O, general medicine, general surgery) and Ormskirk DGH (women's and children's, day-case); c. 280,000 catchment across Sefton, West Lancashire and parts of Wigan; c. 3,000 WTE; c. 90,000 ED attendances/yr.",
    "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation programme guidance",
    "key_stats": [
        {"label": "Amortisation 2024-25", "value": "£0.16M"},
        {"label": "Asset class", "value": "Capitalised software (clinical systems, PAS, EPR components, theatre and pharmacy systems, bespoke dev)"},
        {"label": "Useful-life basis", "value": "3-7 years per IAS 38 / DHSC GAM ch.5 — straight-line amortisation"},
        {"label": "Site anchor", "value": "Southport DGH + Ormskirk DGH"},
        {"label": "Reconfiguration context", "value": "Acute services transferring to Mersey and West Lancashire Teaching Hospitals NHSFT; women's/children's to Liverpool Women's / Alder Hey under 2023-24 plans"},
        {"label": "Workforce", "value": "c. 3,000 WTE; c. 90,000 ED attendances/yr"},
        {"label": "Funding trajectory", "value": "Reducing medium-term as services transfer; legacy intangibles continue amortising under DHSC GAM regardless of organisational form"},
        {"label": "Delivery body", "value": "Southport & Ormskirk Digital + Finance + NHSE Frontline Digitisation Team + EPR vendors"},
        {"label": "Policy owner", "value": "NHSE Frontline Digitisation + DHSC + Cheshire and Merseyside ICB + Lancashire and South Cumbria ICB"},
        {"label": "Evaluation evidence", "value": "S&O ARA intangibles note; NAO reconfiguration reporting; CQC inspection (RVY); ICB reconfiguration case"},
        {"label": "Predecessor / successor", "value": "Predecessor: legacy clinical systems · Successor: post-reconfiguration transfer of intangibles to MWL or successor entity; potential trust dissolution"}
    ],
    "notes": "Southport & Ormskirk's £0.16M amortisation is small but reflects the trust's intangible-asset stack (clinical software, capitalised EPR components) at a moment of organisational transition. NHSE-supported plans agreed in 2023-24 will transfer the trust's acute services to Mersey and West Lancashire Teaching Hospitals NHSFT (which runs Whiston Hospital and St Helens Hospital), with women's and children's services moving to Liverpool Women's NHSFT and Alder Hey. Legacy intangibles continue amortising under DHSC GAM regardless of the organisational form change. CQC has rated the trust requires improvement in recent inspections, partly motivating the reconfiguration.",
    "sources": [
        {"publisher": "Southport And Ormskirk Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southportandormskirk.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "Southport & Ormskirk provider profile (RVY)", "url": "https://www.cqc.org.uk/provider/RVY"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Cheshire and Merseyside ICB system overview", "url": "https://www.cheshireandmerseyside.nhs.uk/"},
        {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"}
    ],
    "related": [
        "Southport And Ormskirk Hospital NHS Trust",
        "Premises & Infrastructure",
        "Mersey and West Lancashire Teaching Hospitals NHS Trust",
        "NHS England"
    ]
}

NEW["Inventories written down — Barts Health NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Barts Health NHS Trust"}],
    "description": "Barts Health NHS Trust's £0.16M inventories-written-down line captures the IAS 2 charge for stock written off below net realisable value across the trust's five-site footprint — The Royal London Hospital (Whitechapel), St Bartholomew's Hospital (West Smithfield, Europe's leading specialist cardiac centre), Whipps Cross University Hospital, Newham University Hospital and Mile End Hospital. Stock comprises time-expired pharmaceuticals (general acute drugs, anti-infectives, anaesthetic agents, biologics, cardiac drugs), expired theatre consumables, expired wound-care and IV stock, and obsolete bespoke implant inventory.",
    "beneficiaries": "Acute and tertiary inpatients across Royal London (~990 beds — major trauma centre, helicopter HEMS, neurosciences, paediatric quaternary), St Bart's (cardiac tertiary), Whipps Cross (~440 beds), Newham (~370 beds) and Mile End (rehab); c. 2.5M catchment across north-east London; c. 17,000 WTE — England's largest NHS trust by staff.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.16M"},
        {"label": "Site anchor", "value": "Royal London Hospital (Whitechapel) + St Bartholomew's Hospital + Whipps Cross + Newham + Mile End"},
        {"label": "Catchment", "value": "c. 2.5M across north-east London (Tower Hamlets, Newham, Waltham Forest, Hackney, City)"},
        {"label": "Workforce", "value": "c. 17,000 WTE — England's largest NHS trust by headcount"},
        {"label": "Major Trauma Centre", "value": "Royal London — pan-London Major Trauma System partner; co-located London's Air Ambulance HEMS"},
        {"label": "Tertiary services", "value": "Cardiothoracic (Bart's), neurosciences (Royal London), paediatric quaternary, transplantation"},
        {"label": "Stock profile", "value": "High-value cardiac drugs + biologics + cardiothoracic implants (Bart's) + neurosurgery consumables + general theatre + wound-care"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover specialist drugs + cardiothoracic implant size mix + theatre kit obsolescence"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + London procurement collaboration + direct-to-supplier (cardiac, neurosurgery, ATMP)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; NEL ICB pharmacy collaboration driving consolidation"},
        {"label": "Delivery body", "value": "Barts Health Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East London ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "Barts Health ARA inventories note; CQC inspection (R1H); NHSE Operational Plan returns; Model Hospital benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 Barts and the London + Newham + Whipps Cross merger procurement · Successor: deeper NEL ICB pharmacy harmonisation + Frontline Digitisation EPR-driven stock visibility"}
    ],
    "notes": "Barts Health's £0.16M write-down is small relative to the trust's c. £2.0B operating cost base and its complex tertiary-services portfolio. As England's largest NHS trust by headcount, formed by the 2012 merger of Barts and the London, Newham University Hospital and Whipps Cross University Hospital, it carries low-turnover, high-value specialist stock — particularly cardiac drugs and implants at St Bart's, Europe's leading specialist cardiac centre, and neurosurgery consumables at Royal London. The trust operates within the North East London ICB and Pan-London cardiac-and-MTC networks. NHS Supply Chain and London procurement collaboration drive scale; Frontline Digitisation EPR rollout improves stock visibility.",
    "sources": [
        {"publisher": "Barts Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bartshealth.nhs.uk/annual-reports"},
        {"publisher": "Care Quality Commission", "title": "Barts Health provider profile (R1H)", "url": "https://www.cqc.org.uk/provider/R1H"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "North East London ICB system overview", "url": "https://northeastlondon.icb.nhs.uk/"}
    ],
    "related": [
        "Barts Health NHS Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "NHS England"
    ]
}
