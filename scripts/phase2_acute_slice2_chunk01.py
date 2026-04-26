# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 01 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "General supplies & services — Liverpool University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Liverpool University Hospitals NHS Foundation Trust"}],
        "description": "LUHFT's £28.16M general supplies & services line covers non-clinical consumables, office supplies, linen, catering provisions, hotel-services materials, IT consumables and minor-equipment expensed below the trust's c. £5k capitalisation threshold across the merged Royal Liverpool + Aintree + Broadgreen estate. The trust runs the new Royal Liverpool University Hospital (opened Oct 2022 after Carillion-collapse rescue), Aintree University Hospital, Broadgreen and a community-clinic footprint in the Cheshire & Merseyside ICS — driving high-volume non-clinical consumables baseline.",
        "beneficiaries": "c. 13,500 WTE staff serving a registered c. 1.5M Cheshire & Merseyside catchment; c. 250,000 ED attendances/yr across Royal Liverpool + Aintree EDs (two of the highest-volume EDs in Northwest England); c. 130,000 elective + day-case admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£28.16M"},
            {"label": "Trust scale", "value": "Three-site acute (Royal Liverpool + Aintree + Broadgreen) post-2019 merger, c. 13,500 WTE"},
            {"label": "ED throughput", "value": "c. 250,000 ED attendances/yr (Royal + Aintree combined — among highest Northwest)"},
            {"label": "Elective + day-case", "value": "c. 130,000 admissions/yr"},
            {"label": "New Royal context", "value": "New Royal Liverpool University Hospital opened Oct 2022 after Carillion 2018 collapse + Laing O'Rourke completion — first full year of operational consumable baseline 2023-24"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Cheshire & Merseyside ICS regional collaboration"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + sustained non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency backfill + cancellation-related re-stocking churn"},
            {"label": "Funding trajectory", "value": "2021-22 pre-merger-operational c. £22M → 2022-23 New Royal opening £25M → 2024-25 £28.16M"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + Cheshire & Merseyside ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NAO Carillion + New Royal completion reports; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate Royal Liverpool + Aintree non-clinical baselines · Successor: full-merger consolidated procurement + ICS collaborative scaling"}
        ],
        "notes": "LUHFT's general supplies & services baseline reflects the post-2019 merger of Royal Liverpool & Broadgreen with Aintree, and the October 2022 opening of the new Royal Liverpool University Hospital — completion by Laing O'Rourke after Carillion's January 2018 insolvency abandoned the original PFI build. The new Royal's larger footprint and modern hotel-services standards lifted non-clinical consumables baseline above the legacy site. Industrial action 2023-24 drove additional churn through cancellation re-stocking and agency-backfill use. NHS Supply Chain remains dominant, with Cheshire & Merseyside ICS collaborative scaling as the medium-term lever; April 2025 NIC step-up and CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.liverpoolft.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LUHFT provider profile (REM)", "url": "https://www.cqc.org.uk/provider/REM"}
        ],
        "related": ["Liverpool University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Barts Health NHS Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — North Middlesex University Hospital NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "North Middlesex University Hospital NHS Trust"}],
        "description": "North Middlesex's £27.99M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment at the single-site Edmonton DGH serving north-east London. The trust is in active merger transaction with Royal Free London NHS FT (transaction completion targeted 2024-25 onwards under the North Central London ICS group model), and its high-deprivation Enfield/Haringey catchment drives elevated A&E throughput and emergency-care consumable demand.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 350,000 Enfield and Haringey catchment with very high IMD deprivation; c. 200,000 ED attendances/yr (one of London's busiest single-site EDs); c. 65,000 admissions/yr; large maternity unit (c. 4,500 deliveries/yr).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£27.99M"},
            {"label": "Trust scale", "value": "Single-site DGH (Sterling Way, Edmonton); c. 3,500 WTE"},
            {"label": "ED throughput", "value": "c. 200,000 attendances/yr — among London's busiest single-site EDs"},
            {"label": "Catchment deprivation", "value": "Enfield + Haringey — high IMD deprivation, drives emergency-care + maternity volume"},
            {"label": "Royal Free merger context", "value": "Transaction with Royal Free London NHS FT progressing 2023-25; targets group-model integration under North Central London ICS"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + NCL ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation-related churn + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £22M → 2023-24 £25M → 2024-25 £27.99M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + NCL ICS procurement collaborative + (post-merger) Royal Free Group functions"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection 2023 (RAP); NHSE NCL ICS group-model business case; Model Hospital benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: stand-alone trust pre-merger · Successor: Royal Free London Group consolidated procurement post-transaction"}
        ],
        "notes": "North Middlesex serves one of London's most deprived catchments across Enfield and Haringey, sustaining ED attendance volumes that rank among the busiest single-site EDs in the capital and a c. 4,500-delivery maternity service — both of which drive non-clinical consumables baseline above peer single-site DGHs. The active merger transaction with Royal Free London NHS FT, progressing towards group-model integration under North Central London ICS, reshapes the medium-term procurement vehicle as Royal Free Group functions absorb local procurement scaling. Industrial action 2023-24 drove agency-backfill consumable churn; April 2025 NIC step-up and sustained CPI on non-clinical inputs feed forward unit-cost pressure ahead of the merger consolidation.",
        "sources": [
            {"publisher": "North Middlesex University Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northmid.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "North Central London ICS group-model transaction (Royal Free + North Mid)", "url": "https://www.england.nhs.uk/london/our-work/north-central-london/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "North Middlesex provider profile (RAP)", "url": "https://www.cqc.org.uk/provider/RAP"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["North Middlesex University Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Royal Free London NHS Foundation Trust", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "NHS Supply Chain"]
    },
    "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Sherwood Forest Hospitals NHS Foundation Trust"}],
        "description": "Sherwood Forest's £27.75M PFI charge reflects the unitary-charge pass-through on the King's Mill Hospital PFI (signed 2005, operational 2011) — one of the most expensive PFI deals per bed in the NHS, repeatedly flagged by NAO/PAC. The contract was originally with Skanska Innisfree consortium with hard-FM by Skanska and soft-FM through subcontractors, and runs to 2043. The line covers debt service, lifecycle (hard-FM major-maintenance) and indexed soft-FM components across King's Mill, Newark and Mansfield Community Hospital sites.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 420,000 Mid Nottinghamshire catchment (Mansfield, Newark, Sherwood); c. 130,000 ED attendances/yr at King's Mill ED; c. 60,000 admissions/yr; PFI estate covers main King's Mill DGH + Newark Hospital + Mansfield Community Hospital.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition for service-concession components) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£27.75M"},
            {"label": "PFI vehicle", "value": "King's Mill PFI signed 2005, operational 2011; SPV Healthcare Support (Newark) Ltd / SF SPV — Skanska Innisfree consortium"},
            {"label": "Contract end date", "value": "c. 2043 (38-year operational concession)"},
            {"label": "PAC/NAO scrutiny", "value": "Sherwood Forest King's Mill cited by NAO/PAC as one of highest-cost-per-bed PFI deals in NHS; 2014 contract reset to ease affordability pressure"},
            {"label": "Estate covered", "value": "King's Mill Hospital (main DGH, c. 460 beds) + Newark Hospital + Mansfield Community Hospital"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM (cleaning, catering, portering)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed components per concession agreement"},
            {"label": "Funding trajectory", "value": "Annual unitary charge c. £40-50M total whole-PFI; £27.75M figure represents accounted PFI/LIFT-line element after IFRS 16 split"},
            {"label": "Delivery body", "value": "SPV (Healthcare Support) + Skanska (hard-FM) + soft-FM subcontractor cohort + trust E&F oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + NHSE Provider Finance + Nottingham & Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back report 2020; PAC PFI hearings; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI King's Mill estate (1980s buildings) · Successor: 2043 hand-back + post-PFI public-sector ownership transition"}
        ],
        "notes": "Sherwood Forest's King's Mill PFI is one of the NHS's most cited cautionary PFI tales — NAO and PAC scrutiny in the 2010s flagged the 2005-signed deal's unitary charge as among the highest cost-per-bed, prompting a 2014 contract reset to ease the trust's affordability position. The contract runs to 2043, with RPI-linked uplifts on indexed soft-FM components driving cost growth and lifecycle hard-FM cycles producing year-on-year volatility. The IFRS 16 2022 transition and DHSC GAM ch.7 split reshaped the headline figure but not the underlying obligation. Hand-back planning ahead of 2043 is the medium-term question, with HMT/IPA guidance shaping the path.",
        "sources": [
            {"publisher": "Sherwood Forest Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sfh-tr.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sherwood Forest Hospitals provider profile (RK5)", "url": "https://www.cqc.org.uk/provider/RK5"}
        ],
        "related": ["Sherwood Forest Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "PFI / LIFT charges — University Hospitals Birmingham NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "Worcestershire Acute's £27.56M PFI charge covers the unitary-charge pass-through on the Worcestershire Royal Hospital PFI (signed 1999, operational 2002), with SPV Catalyst Healthcare (Worcester) and post-Carillion-collapse FM novation to Engie/Equans for hard-FM and soft-FM. The 30-year concession runs to 2032, putting the trust in the active hand-back planning window for one of the NHS's first-wave PFI builds. The line covers debt service, lifecycle and indexed FM components for the main Worcester site.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 600,000 Worcestershire catchment (Worcester, Redditch, Bromsgrove, Kidderminster); c. 180,000 ED attendances/yr (Worcester + Redditch Alexandra EDs combined); c. 80,000 admissions/yr; PFI estate covers main Worcestershire Royal Hospital site.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£27.56M"},
            {"label": "PFI vehicle", "value": "Worcestershire Royal PFI signed 1999, operational Feb 2002; SPV Catalyst Healthcare (Worcester) Ltd"},
            {"label": "Contract end date", "value": "c. 2032 (30-year concession from 2002 operational date)"},
            {"label": "Carillion 2018 effect", "value": "Carillion (original FM contractor on some PFI subcontracts) Jan 2018 collapse → Engie/Equans novation; ongoing FM contract churn"},
            {"label": "Hand-back planning window", "value": "c. 7-8 years to expiry — IPA / HMT PFI Hand-Back unit engagement underway sector-wide"},
            {"label": "Estate covered", "value": "Worcestershire Royal Hospital (Worcester) — main acute site (c. 670 beds)"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed FM components"},
            {"label": "Funding trajectory", "value": "Mature PFI; annual line £25-28M range as RPI uplift continues vs declining debt-service balance"},
            {"label": "Delivery body", "value": "Catalyst Healthcare SPV + Engie / Equans (post-Carillion FM) + trust E&F"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + NHSE Provider Finance + Herefordshire & Worcestershire ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI hand-back review 2020; CQC inspection RWP 2022-2024; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI Worcester Royal Infirmary city-centre site · Successor: 2032 hand-back to public-sector + post-PFI estate ownership"}
        ],
        "notes": "Worcestershire Royal is one of the NHS's first-wave 1999-signed PFI deals, putting Worcestershire Acute Hospitals in the active hand-back planning window seven to eight years from 2032 expiry. Carillion's January 2018 collapse triggered FM contract novations to Engie/Equans on subcontracted FM elements, adding contract-management complexity layered on the existing Catalyst Healthcare SPV structure. RPI indexation continues to lift soft-FM components even as debt-service balance amortises down. The IPA/HMT PFI Hand-Back unit's NAO-recommended cross-government engagement is shaping trust hand-back governance — NAO's 2020 'Managing PFI assets and services as contracts end' report flagged Worcestershire as among trusts in the early-expiry cohort needing structured preparation.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.worcsacute.nhs.uk/about-us/key-publications/annual-reports"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Infrastructure and Projects Authority", "title": "PFI Hand-Back Resource Centre", "url": "https://www.gov.uk/government/collections/pfi-and-pf2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Worcestershire Acute provider profile (RWP)", "url": "https://www.cqc.org.uk/provider/RWP"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "General supplies & services — Worcestershire Acute Hospitals NHS Trust", "Infrastructure and Projects Authority"]
    },
    "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "ASPH's £26.58M social security & levy line covers employer National Insurance contributions plus the Apprenticeship Levy on the trust's c. 4,500-WTE pay bill across the two-site Ashford Hospital + St Peter's Hospital footprint serving north-west Surrey. The line scales directly with substantive headcount and overtime/agency. The April 2025 employer-NIC step-up (rate to 15%, threshold reduced to £5,000) feeds forward as a structural cost increase, on top of 2023-24 industrial-action backfill that elevated overtime-related employer-NIC.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 410,000 north-west Surrey catchment (Runnymede, Spelthorne, Surrey Heath, Woking); c. 130,000 ED attendances/yr (St Peter's main ED + Ashford Walk-in); c. 65,000 admissions/yr; large maternity unit at St Peter's.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · Income Tax (Earnings and Pensions) Act 2003 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£26.58M"},
            {"label": "Trust scale", "value": "Two-site DGH (St Peter's, Chertsey + Ashford); c. 4,500 WTE"},
            {"label": "ED throughput", "value": "c. 130,000 ED attendances/yr (St Peter's main + Ashford Walk-in)"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000 (Apr 2025) — material forward-cost increase, partially offset by NHSE NIC funding"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency + overtime backfill, lifting NIC base"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M annual allowance — c. £1.5M-£2M/yr at this trust scale"},
            {"label": "Funding trajectory", "value": "2021-22 c. £22M → 2024-25 £26.58M; 2025-26 forward jump from NIC reform"},
            {"label": "Delivery body", "value": "Trust HR + Payroll team + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy policy) + DHSC + NHSE Workforce + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "NHSE workforce return; OBR Economic and Fiscal Outlook (NIC effect); Trust ARA workforce disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 pre-Apprenticeship Levy regime · Successor: post-Apr 2025 NIC step-up baseline"}
        ],
        "notes": "ASPH's social security & levy line scales tightly with the c. 4,500-WTE substantive pay bill, with the Apprenticeship Levy adding c. £1.5-2M/yr on top of employer NIC. Industrial action across 2023-24 — 44 days of junior-doctor strikes plus 10 days of consultant strikes — drove additional agency-locum backfill and overtime that elevated the employer-NIC base, particularly across emergency-medicine and surgical rotas. The April 2025 employer-NIC step-up (rate to 15.0%, secondary threshold reduced to £5,000) is the dominant forward-cost driver, with NHSE-issued partial NIC compensation flowing through ICB allocation; net residual pressure feeds the trust's 2025-26 productivity assumption. Surrey Heartlands ICS group-level workforce planning shapes the medium-term path.",
        "sources": [
            {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ashfordstpeters.nhs.uk/annual-reports"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Office for Budget Responsibility", "title": "Economic and Fiscal Outlook (employer NIC effect)", "url": "https://obr.uk/efo/economic-and-fiscal-outlook/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "ASPH provider profile (RTK)", "url": "https://www.cqc.org.uk/provider/RTK"}
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Social security & levy — Kingston Hospital NHS Foundation Trust", "Apprenticeship Levy", "HM Revenue and Customs"]
    },
    "Social security & levy — Great Western Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Great Western Hospitals NHS Foundation Trust"}],
        "description": "GWH's £26.39M social security & levy line covers employer NIC plus the Apprenticeship Levy on the trust's c. 5,500-WTE pay bill. The trust runs the Great Western Hospital in Swindon (PFI-built, opened 2002) plus integrated community services across Wiltshire and Bath & North East Somerset (BSW ICS). The April 2025 NIC step-up is the dominant forward driver, layered on 2023-24 industrial-action backfill and the trust's integrated acute + community workforce profile.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 350,000 Swindon catchment plus c. 1.0M for community services across Wiltshire and BaNES; c. 110,000 ED attendances/yr at Great Western ED; c. 60,000 admissions/yr; integrated community workforce (district nursing + community-paediatric).",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£26.39M"},
            {"label": "Trust scale", "value": "Single acute site (Great Western, Swindon) + integrated Wiltshire + BaNES community services; c. 5,500 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation flowing through BSW ICB"},
            {"label": "ED throughput", "value": "c. 110,000 attendances/yr"},
            {"label": "Integrated community workforce", "value": "Acute trust integrated with Wiltshire community services (district nursing, community paediatric, sexual health) — broadens NIC base vs acute-only peers"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove agency + overtime backfill, lifting NIC base"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.5-2M/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £22M → 2023-24 £25M → 2024-25 £26.39M; 2025-26 forward step-up from NIC reform"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + Bath, Swindon and Wiltshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE workforce returns; OBR EFO NIC line; Trust ARA workforce remuneration report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 pre-Apprenticeship Levy regime · Successor: post-Apr 2025 NIC baseline"}
        ],
        "notes": "GWH's pay-bill profile is broadened by its integrated acute + community model — the trust runs Wiltshire and BaNES community services (district nursing, community-paediatric, sexual-health, school-nursing) alongside the Swindon acute site, so the employer-NIC base is wider than for acute-only peers of similar bed count. Industrial action 2023-24 drove additional agency and overtime backfill on the acute-medicine and surgical rotas. The April 2025 employer-NIC step-up to 15% with the threshold drop to £5,000 is the dominant forward-cost driver; partial NHSE NIC compensation flows through Bath, Swindon and Wiltshire ICB allocation, leaving residual pressure to feed the trust's 2025-26 efficiency assumption. The Apprenticeship Levy adds c. £1.5-2M/yr on top.",
        "sources": [
            {"publisher": "Great Western Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gwh.nhs.uk/about-us/key-publications/"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Office for Budget Responsibility", "title": "Economic and Fiscal Outlook", "url": "https://obr.uk/efo/economic-and-fiscal-outlook/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Great Western Hospitals provider profile (RN3)", "url": "https://www.cqc.org.uk/provider/RN3"}
        ],
        "related": ["Great Western Hospitals NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "Apprenticeship Levy", "HM Revenue and Customs"]
    },
    "Transport (business + patient) — Imperial College Healthcare NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Imperial College Healthcare NHS Trust"}],
        "description": "Imperial's £26.27M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's five-site footprint (Charing Cross, Hammersmith, St Mary's, Queen Charlotte's & Chelsea, Western Eye). Inter-site clinical transfers between Charing Cross neuroscience, Hammersmith cardiac/renal and St Mary's major-trauma generate substantial PTS demand, with London Ambulance Service and accredited PTS contractors as primary carriers. The line also covers AHP and community-team mileage across the NW London ICS catchment.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 2.0M north-west London catchment plus tertiary specialty referrals national/international; c. 350,000 ED attendances/yr (St Mary's, Charing Cross, Hammersmith); c. 200,000 admissions/yr; St Mary's is one of London's four Major Trauma Centres.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£26.27M"},
            {"label": "Trust scale", "value": "Five-site academic acute (St Mary's + Charing Cross + Hammersmith + Queen Charlotte's + Western Eye); c. 14,000 WTE"},
            {"label": "Major Trauma Centre", "value": "St Mary's = one of London's four MTCs — drives inter-site major-trauma transfer demand"},
            {"label": "Tertiary referrals", "value": "Hammersmith cardiac/renal + Charing Cross neuroscience + Imperial cancer — substantial inter-hospital + inter-trust PTS"},
            {"label": "PTS provider mix", "value": "London Ambulance Service NHS Trust (LAS) + accredited NEPTS contractors (e.g. ERS Medical / G4S subcontractors) — re-tendered via NWL ICS"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for AHPs + community teams"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £20M → 2023-24 £24M → 2024-25 £26.27M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + LAS PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + North West London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC inspection RYJ; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2007 separate Hammersmith + St Mary's NHS Trust transport baselines · Successor: NWL ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "Imperial's transport line is structurally elevated by the trust's five-site academic footprint and tertiary referral pattern — Major Trauma Centre status at St Mary's drives inter-hospital trauma transfers; Hammersmith's national cardiac and renal services and Charing Cross neuroscience generate continuous patient transfer between sites and from referring trusts across NW London. The 2007 merger consolidating Hammersmith Hospitals with St Mary's baselined the current footprint. Industrial action 2023-24 added ad-hoc transfer demand and locum mileage. April 2025 NIC step-up affects PTS-contractor pass-through; CPI fuel pressure remains the dominant driver. NWL ICS shared-fleet pooling and EV transition are the medium-term levers.",
        "sources": [
            {"publisher": "Imperial College Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.imperial.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Imperial College Healthcare provider profile (RYJ)", "url": "https://www.cqc.org.uk/provider/RYJ"}
        ],
        "related": ["Imperial College Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "London Ambulance Service NHS Trust", "Transport (business + patient) — Lancashire and South Cumbria NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Social security & levy — Whittington Health NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Whittington Health NHS Trust"}],
        "description": "Whittington Health's £25.95M social security & levy line covers employer NIC and Apprenticeship Levy on the integrated acute + community workforce of c. 4,500 WTE. The trust runs the Whittington Hospital (Archway, north London) plus integrated community services across Islington and Haringey — district nursing, school-nursing, community-paediatric and HIV services. The April 2025 NIC step-up is the dominant forward-cost driver layered on the broad community-team NIC base and 2023-24 industrial-action backfill.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 500,000 Islington + Haringey catchment; c. 90,000 ED attendances/yr at Whittington ED; c. 35,000 admissions/yr; community caseload c. 200,000 individuals/yr across district-nursing + community-paediatric + sexual-health.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£25.95M"},
            {"label": "Trust scale", "value": "Single acute site (Whittington, Archway) + Islington + Haringey integrated community services; c. 4,500 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation via NCL ICB"},
            {"label": "Catchment deprivation", "value": "Islington + Haringey — high IMD deprivation; broad community workforce footprint"},
            {"label": "Integrated community workforce", "value": "District nursing + school-nursing + community-paediatric + HIV services + sexual-health — broadens NIC base"},
            {"label": "ED throughput", "value": "c. 90,000 attendances/yr — relatively small acute footprint vs broad community workforce"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove backfill, lifting NIC base"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.5M/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £21M → 2023-24 £24M → 2024-25 £25.95M; 2025-26 forward step-up from NIC reform"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE workforce returns; OBR EFO NIC line; CQC inspection RKE; Trust ARA workforce disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate acute + PCT community baselines · Successor: post-Apr 2025 NIC baseline + NCL ICS workforce planning"}
        ],
        "notes": "Whittington Health's pay-bill profile reflects the 2011 integration of Whittington Hospital with Islington and Haringey PCT community services — making it one of the early integrated acute + community trusts. The community workforce (district nursing, school-nursing, community-paediatric, HIV, sexual-health) broadens the employer-NIC base relative to acute-only peers of similar acute footprint. Industrial action 2023-24 drove additional backfill on the small acute site. The April 2025 employer-NIC step-up is the dominant forward driver — partial NHSE NIC compensation flows through NCL ICB allocation. Whittington sits within North Central London ICS alongside Royal Free Group, UCLH and North Middlesex (under merger), shaping medium-term workforce-cost planning.",
        "sources": [
            {"publisher": "Whittington Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whittington.nhs.uk/default.asp?c=21091"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Office for Budget Responsibility", "title": "Economic and Fiscal Outlook", "url": "https://obr.uk/efo/economic-and-fiscal-outlook/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Whittington Health provider profile (RKE)", "url": "https://www.cqc.org.uk/provider/RKE"}
        ],
        "related": ["Whittington Health NHS Trust", "Staff Costs", "NHS Acute Trusts", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "Apprenticeship Levy", "HM Revenue and Customs"]
    },
    "Social security & levy — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Kingston Hospital's £25.53M social security & levy line covers employer NIC and Apprenticeship Levy on the c. 4,000-WTE workforce serving south-west London. The trust is in active group-model arrangements with Hounslow & Richmond Community Healthcare and shares a chair-in-common with Epsom and St Helier University Hospitals NHS Trust under SWL ICS planning. April 2025 NIC step-up is the dominant forward-cost driver, layered on 2023-24 industrial-action backfill.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 350,000 Kingston, Richmond and Wandsworth catchment; c. 110,000 ED attendances/yr at Kingston ED; c. 45,000 admissions/yr; large maternity service (c. 5,500 deliveries/yr — among largest in SWL).",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£25.53M"},
            {"label": "Trust scale", "value": "Single-site DGH (Kingston Hospital, Galsworthy Road); c. 4,000 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation via SWL ICB"},
            {"label": "ED throughput", "value": "c. 110,000 attendances/yr"},
            {"label": "Maternity scale", "value": "c. 5,500 deliveries/yr — among the largest maternity services in south-west London"},
            {"label": "Group-model context", "value": "Group arrangements with Hounslow & Richmond Community Healthcare; chair-in-common with Epsom and St Helier under SWL ICS"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency backfill, lifting NIC base"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.3-1.6M/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £21M → 2023-24 £24M → 2024-25 £25.53M; 2025-26 forward step-up"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + South West London ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection RAX (Outstanding-rated); NHSE workforce returns; OBR EFO NIC line"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 pre-Apprenticeship Levy regime · Successor: post-Apr 2025 NIC baseline + SWL ICS group-model consolidation"}
        ],
        "notes": "Kingston Hospital's pay-bill profile is dominated by its large maternity service (c. 5,500 deliveries/yr — among SWL's largest) and c. 110,000-attendance ED, plus the chair-in-common arrangement with Epsom and St Helier University Hospitals NHS Trust which shapes shared-back-office workforce planning under South West London ICS. Industrial action 2023-24 drove additional agency-locum backfill on the acute-medicine and emergency-medicine rotas. The April 2025 employer-NIC step-up is the dominant forward-cost driver; partial NHSE NIC compensation flows through SWL ICB allocation. Group-model consolidation with Epsom & St Helier is an ongoing strategic question shaping medium-term workforce cost.",
        "sources": [
            {"publisher": "Kingston Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kingstonhospital.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Office for Budget Responsibility", "title": "Economic and Fiscal Outlook", "url": "https://obr.uk/efo/economic-and-fiscal-outlook/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Kingston Hospital provider profile (RAX) — Outstanding rated", "url": "https://www.cqc.org.uk/provider/RAX"}
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "Epsom and St Helier University Hospitals NHS Trust", "HM Revenue and Customs"]
    },
    "Social security & levy — South Warwickshire NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "South Warwickshire NHS Foundation Trust"}],
        "description": "South Warwickshire University NHS FT's £25.27M social security & levy line covers employer NIC and Apprenticeship Levy on c. 4,500-WTE integrated acute + community workforce. The trust runs Warwick Hospital and integrated community services across south Warwickshire, having completed merger with Wye Valley NHS Trust in 2024-25 to form South Warwickshire University NHS FT — extending the workforce footprint into Herefordshire. April 2025 NIC step-up dominates the forward-cost picture.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 280,000 south Warwickshire catchment plus extended Herefordshire footprint post-merger with Wye Valley; c. 75,000 ED attendances/yr at Warwick Hospital ED; c. 35,000 admissions/yr; integrated community-team workforce.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£25.27M"},
            {"label": "Trust scale", "value": "Warwick Hospital + integrated south Warwickshire community services; post-2024 merger extending into Herefordshire (Wye Valley); c. 4,500 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation"},
            {"label": "Wye Valley merger", "value": "Apr 2024 acquisition completion → unified South Warwickshire University NHS FT; absorbs Wye Valley workforce + Carillion-novated Hereford PFI FM context"},
            {"label": "Integrated community workforce", "value": "District nursing + community-paediatric + therapies — broadens NIC base"},
            {"label": "ED throughput", "value": "c. 75,000 attendances/yr at Warwick + Hereford post-merger c. 60,000"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove agency-locum backfill"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.3-1.6M/yr pre-merger"},
            {"label": "Funding trajectory", "value": "2021-22 c. £20M → 2023-24 £23M → 2024-25 £25.27M; 2025-26 forward jump from NIC + Wye Valley merger"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + Coventry & Warwickshire ICB + (post-merger) Herefordshire & Worcestershire ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection RJC; NHSE workforce returns; Trust ARA workforce remuneration disclosure; merger transaction business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger SWFT acute + community workforce · Successor: post-Apr 2024 unified SWUFT including Wye Valley + post-Apr 2025 NIC baseline"}
        ],
        "notes": "South Warwickshire's NIC line reflects an integrated acute + community workforce (district nursing, community-paediatric, therapies) covering south Warwickshire. The April 2024 acquisition of Wye Valley NHS Trust to form South Warwickshire University NHS FT — one of NHSE's flagship 2024 group-model transactions — extends the workforce footprint into Herefordshire and brings a Carillion-novated Hereford PFI estate into trust scope. Industrial action 2023-24 drove backfill at Warwick. The April 2025 employer-NIC step-up combines with first-full-year post-merger workforce consolidation as the dominant 2025-26 driver; partial NHSE NIC compensation flows via the two ICBs covering the trust's catchment.",
        "sources": [
            {"publisher": "South Warwickshire University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swft.nhs.uk/about-us/our-publications/annual-report-and-accounts"},
            {"publisher": "NHS England", "title": "Wye Valley + South Warwickshire group-model transaction", "url": "https://www.england.nhs.uk/midlands/"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Warwickshire provider profile (RJC)", "url": "https://www.cqc.org.uk/provider/RJC"}
        ],
        "related": ["South Warwickshire NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Wye Valley NHS Trust", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "HM Revenue and Customs"]
    },
    "General supplies & services — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "Worcestershire Acute's £24.94M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials and minor expensed equipment across the trust's Worcestershire Royal Hospital (PFI), Alexandra Hospital Redditch and Kidderminster Hospital + Treatment Centre footprint. The trust's PFI hard-FM/soft-FM regime under Catalyst Healthcare SPV (with Carillion-collapse-driven Engie/Equans novations) shapes how non-clinical supplies are procured at Worcester relative to direct trust procurement at Alexandra and Kidderminster.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 600,000 Worcestershire catchment (Worcester, Redditch, Bromsgrove, Kidderminster); c. 180,000 ED attendances/yr (Worcester + Redditch Alexandra EDs combined); c. 80,000 admissions/yr; multi-site DGH spread across Worcestershire.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · IFRIC 12 (PFI consumables interaction)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£24.94M"},
            {"label": "Trust scale", "value": "Three-site DGH (Worcestershire Royal + Alexandra Redditch + Kidderminster); c. 6,500 WTE"},
            {"label": "ED throughput", "value": "c. 180,000 attendances/yr (Worcester main ED + Redditch Alexandra ED)"},
            {"label": "PFI procurement interaction", "value": "Worcester Royal soft-FM under Catalyst Healthcare SPV + Engie/Equans (post-Carillion); separate trust-direct procurement for Alexandra + Kidderminster non-clinical supplies"},
            {"label": "Carillion 2018 effect", "value": "Carillion Jan 2018 collapse → Engie/Equans novation on FM subcontracts → consumables sub-contracting churn at Worcester"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Herefordshire & Worcestershire ICS collaborative"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency backfill + cancellation-related re-stocking"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + sustained non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £19M → 2023-24 £22M → 2024-25 £24.94M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Catalyst PFI SPV + Engie / Equans soft-FM (Worcester) + H&W ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Herefordshire & Worcestershire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NAO Carillion + PFI reports; Trust ARA disclosure; CQC RWP inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 pre-PFI Worcester Royal procurement + 2010s reconfiguration · Successor: 2032 PFI hand-back + post-PFI direct-trust procurement consolidation"}
        ],
        "notes": "Worcestershire Acute's general supplies & services line reflects the multi-site DGH footprint plus the dual procurement model where Worcester Royal sits within the Catalyst Healthcare PFI SPV soft-FM envelope (with Engie/Equans novations after Carillion's January 2018 insolvency on parts of the subcontract chain), while Alexandra Redditch and Kidderminster operate under direct-trust procurement. The 2025 Procurement Act regime is reshaping framework call-off patterns. Industrial action 2023-24 drove cancellation-related re-stocking and agency-backfill consumable use. April 2025 NIC step-up and sustained non-clinical CPI continue to feed forward unit-cost pressure. The 2032 PFI expiry will eventually consolidate procurement under direct-trust control across all three sites.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.worcsacute.nhs.uk/about-us/key-publications/annual-reports"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Worcestershire Acute provider profile (RWP)", "url": "https://www.cqc.org.uk/provider/RWP"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Social security & levy — West Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "West Suffolk NHS Foundation Trust"}],
        "description": "West Suffolk NHS FT's £24.92M social security & levy line covers employer NIC and Apprenticeship Levy on the c. 4,500-WTE workforce at the Bury St Edmunds DGH. The trust is one of the original NHP cohort (40 hospitals programme) trusts where the Jan 2025 NHP Reset deferred the planned new West Suffolk Hospital build (RAAC-affected) into the next financing cycle — keeping the existing workforce baseline intact through 2025-26 with NIC step-up as the dominant forward driver.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 280,000 west Suffolk catchment (Bury St Edmunds, Newmarket, Haverhill, Sudbury); c. 75,000 ED attendances/yr at West Suffolk Hospital ED; c. 35,000 admissions/yr; large maternity unit + community footprint extending into rural west Suffolk.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£24.92M"},
            {"label": "Trust scale", "value": "Single-site DGH (West Suffolk Hospital, Bury St Edmunds); c. 4,500 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation via Suffolk & North East Essex ICB"},
            {"label": "RAAC + NHP context", "value": "West Suffolk Hospital on Sep 2023 HSSIB RAAC list (27 trusts); original NHP cohort; Jan 2025 NHP Reset deferred new build into next cycle — keeps existing workforce baseline"},
            {"label": "ED throughput", "value": "c. 75,000 attendances/yr"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove agency-locum backfill, lifting NIC base"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.3-1.6M/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £20M → 2023-24 £23M → 2024-25 £24.92M; 2025-26 forward step-up from NIC reform"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + Suffolk & North East Essex ICB"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC report Sep 2023; NHP Reset announcement Jan 2025; CQC RGR inspection; NHSE workforce returns; OBR EFO NIC line"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 pre-Apprenticeship Levy regime · Successor: post-Apr 2025 NIC baseline + post-NHP-Reset workforce planning towards eventual rebuild"}
        ],
        "notes": "West Suffolk's pay-bill profile is shaped by its single-DGH model and its place in the Sep 2023 HSSIB RAAC cohort — the existing hospital's reinforced autoclaved aerated concrete planks have driven structural mitigation and decant planning, with the original New Hospital Programme commitment to a replacement build deferred under the January 2025 NHP Reset into the next financing window. That deferral preserves the current workforce baseline rather than forcing accelerated transition. Industrial action 2023-24 added agency-locum NIC base. The April 2025 employer-NIC step-up is the dominant 2025-26 forward-cost driver, with partial NHSE compensation flowing through Suffolk & North East Essex ICB.",
        "sources": [
            {"publisher": "West Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wsh.nhs.uk/About-us/Publications.aspx"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Reinforced autoclaved aerated concrete (RAAC) in NHS hospitals", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Care Quality Commission", "title": "West Suffolk provider profile (RGR)", "url": "https://www.cqc.org.uk/provider/RGR"}
        ],
        "related": ["West Suffolk NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "New Hospital Programme", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "HM Revenue and Customs"]
    },
    "Social security & levy — Kettering General Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Kettering General Hospital NHS Foundation Trust"}],
        "description": "Kettering General Hospital NHS FT's £24.91M social security & levy line covers employer NIC and Apprenticeship Levy on the c. 4,500-WTE workforce serving north Northamptonshire. The trust shares a chair-in-common with Northampton General under the University Hospitals of Northamptonshire group model. Kettering is in the original NHP cohort with a planned new-build deferred under Jan 2025 NHP Reset, keeping the workforce baseline at the existing site through 2025-26 with NIC step-up dominating forward-cost picture.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 360,000 north Northamptonshire catchment (Kettering, Corby, Wellingborough, Rushden); c. 90,000 ED attendances/yr; c. 50,000 admissions/yr; large maternity unit + Foundation Group functions shared with Northampton General.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£24.91M"},
            {"label": "Trust scale", "value": "Single-site DGH (Kettering General Hospital); c. 4,500 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "Group-model context", "value": "University Hospitals of Northamptonshire group with Northampton General — chair-in-common since 2021; shared corporate functions"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation via Northants ICB"},
            {"label": "NHP context", "value": "Original NHP cohort; Jan 2025 NHP Reset deferred new build — workforce remains at existing site"},
            {"label": "ED throughput", "value": "c. 90,000 attendances/yr"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove agency-locum backfill"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.3-1.6M/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £20M → 2023-24 £23M → 2024-25 £24.91M; 2025-26 forward step-up"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + UHN Group functions + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "CQC RNQ inspection; NHSE workforce returns; UHN group business case; OBR EFO NIC line"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 stand-alone Kettering General · Successor: post-Apr 2025 NIC baseline + UHN Group functions consolidation + post-NHP-Reset rebuild"}
        ],
        "notes": "Kettering General Hospital's pay-bill profile is shaped by its membership of the University Hospitals of Northamptonshire group with Northampton General — the chair-in-common arrangement since 2021 has driven shared corporate-functions consolidation, including elements of HR, payroll and finance back-office that affect the NIC reporting boundary. The trust's place in the original New Hospital Programme cohort, with the Jan 2025 NHP Reset deferring the planned rebuild, preserves the current workforce baseline. Industrial action 2023-24 drove agency-locum backfill on acute-medicine and surgical rotas. The April 2025 employer-NIC step-up is the dominant 2025-26 forward driver; partial NHSE NIC compensation flows through Northamptonshire ICB.",
        "sources": [
            {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/our-publications"},
            {"publisher": "University Hospitals of Northamptonshire NHS Group", "title": "Group business case + chair-in-common arrangements", "url": "https://www.uhn.nhs.uk/"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Kettering General Hospital provider profile (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"}
        ],
        "related": ["Kettering General Hospital NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Northampton General Hospital NHS Trust", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "Social security & levy — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Stockport NHS FT's £24.83M social security & levy line covers employer NIC and Apprenticeship Levy on the c. 4,500-WTE workforce at Stepping Hill Hospital. The trust serves the borough of Stockport within Greater Manchester ICS, runs the only acute ED for the borough, and operates extensive integrated community services across Stockport. April 2025 NIC step-up dominates the forward-cost picture, layered on industrial-action backfill 2023-24 and ongoing financial-recovery context.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 290,000 Stockport borough catchment; c. 110,000 ED attendances/yr at Stepping Hill ED; c. 50,000 admissions/yr; integrated community services across Stockport adding c. 800-1,000 community-team WTE.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£24.83M"},
            {"label": "Trust scale", "value": "Single acute site (Stepping Hill, Stockport) + integrated Stockport community services; c. 4,500 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation via Greater Manchester ICB"},
            {"label": "ED throughput", "value": "c. 110,000 attendances/yr — sole acute ED for Stockport borough"},
            {"label": "Integrated community workforce", "value": "Adult community nursing + therapies + community paediatric — broadens NIC base"},
            {"label": "Financial recovery context", "value": "Trust in NHSE Recovery Support Programme historically; persistent operational deficit shapes workforce + agency NIC base"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency-locum backfill at Stepping Hill"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.3-1.6M/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £20M → 2023-24 £23M → 2024-25 £24.83M; 2025-26 forward step-up"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "CQC RWJ inspection; NHSE Recovery Support Programme reviews; OBR EFO NIC line"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate acute + Stockport PCT community baselines · Successor: post-Apr 2025 NIC baseline + GM ICS workforce planning"}
        ],
        "notes": "Stockport NHS FT's pay-bill profile reflects integrated acute + community workforce — the trust runs Stepping Hill Hospital alongside the borough's adult-community-nursing, therapies and community-paediatric teams, broadening the employer-NIC base relative to acute-only peers. Industrial action 2023-24 drove agency-locum backfill at Stepping Hill, particularly in emergency medicine and acute medicine. The trust has experienced persistent operational deficit pressure, shaping its workforce-cost trajectory under NHSE Provider Finance oversight. The April 2025 employer-NIC step-up is the dominant 2025-26 forward driver, with partial NHSE compensation flowing through Greater Manchester ICB allocation under the GM mayoral devolution health envelope.",
        "sources": [
            {"publisher": "Stockport NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stockport.nhs.uk/about-us/our-publications/"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Office for Budget Responsibility", "title": "Economic and Fiscal Outlook", "url": "https://obr.uk/efo/economic-and-fiscal-outlook/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Stockport NHS FT provider profile (RWJ)", "url": "https://www.cqc.org.uk/provider/RWJ"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Greater Manchester Integrated Care Board", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "HM Revenue and Customs"]
    },
    "General supplies & services — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "ESNEFT's £24.62M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials and minor expensed equipment across the trust's two-DGH footprint — Ipswich Hospital and Colchester Hospital — formed by the 2018 merger of Ipswich Hospital NHS Trust with Colchester Hospital University NHS FT. The trust runs one of England's largest cross-boundary acute footprints (east Suffolk + north Essex) and a substantial integrated community workforce.",
        "beneficiaries": "c. 12,000 WTE staff serving a c. 1.0M cross-boundary east Suffolk + north Essex catchment; c. 220,000 ED attendances/yr (Ipswich + Colchester EDs combined); c. 100,000 admissions/yr; integrated community workforce across both counties.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£24.62M"},
            {"label": "Trust scale", "value": "Two-DGH (Ipswich + Colchester) post-2018 merger + integrated east Suffolk + north Essex community services; c. 12,000 WTE"},
            {"label": "ED throughput", "value": "c. 220,000 attendances/yr (Ipswich + Colchester combined)"},
            {"label": "2018 merger context", "value": "Ipswich Hospital NHS Trust + Colchester Hospital University NHS FT merged Jul 2018 forming ESNEFT — consolidated procurement post-merger"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Suffolk & North East Essex ICS collaborative"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency backfill + cancellation-related re-stocking churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + sustained non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Cross-county integrated community", "value": "ESNEFT runs community services across east Suffolk + north Essex — broadens consumables consumption profile"},
            {"label": "Funding trajectory", "value": "2020-21 post-merger c. £19M → 2023-24 £22M → 2024-25 £24.62M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + SNEE ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Suffolk & North East Essex ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC RDE inspection (Outstanding-rated); Trust ARA disclosure; merger benefits-realisation review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Ipswich + Colchester non-clinical baselines · Successor: SNEE ICS collaborative procurement scaling"}
        ],
        "notes": "ESNEFT was created in July 2018 by merger of Ipswich Hospital NHS Trust with Colchester Hospital University NHS FT, forming one of England's largest cross-boundary acute trusts spanning east Suffolk and north Essex. The merger consolidated post-2018 non-clinical procurement, with subsequent integration of community services adding consumables consumption breadth. Industrial action 2023-24 drove cancellation-related re-stocking and agency-backfill consumable use. The Procurement Act 2023 regime is reshaping framework call-off patterns. CQC rated ESNEFT 'Outstanding' overall, providing evaluation evidence on operational consistency. April 2025 NIC step-up and sustained CPI on non-clinical inputs feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "ESNEFT provider profile (RDE) — Outstanding rated", "url": "https://www.cqc.org.uk/provider/RDE"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Suffolk and North East Essex ICB", "title": "ICS estate and procurement strategy", "url": "https://suffolkandnortheastessex.icb.nhs.uk/"}
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "NHS Supply Chain", "Department of Health and Social Care"]
    },
    "Social security & levy — Dartford and Gravesham NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Dartford and Gravesham NHS Trust"}],
        "description": "Dartford and Gravesham's £24.55M social security & levy line covers employer NIC and Apprenticeship Levy on the c. 4,500-WTE workforce at Darent Valley Hospital — one of the NHS's earliest large operational PFIs (signed 1997, opened 2000). The trust serves north Kent and operates one of the few non-FT acute trusts in the south-east. April 2025 NIC step-up dominates forward-cost picture, layered on industrial-action backfill 2023-24.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 500,000 north Kent catchment (Dartford, Gravesham, Bexley, Swanley); c. 130,000 ED attendances/yr at Darent Valley ED; c. 60,000 admissions/yr; large maternity service (c. 4,500 deliveries/yr).",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£24.55M"},
            {"label": "Trust scale", "value": "Single PFI-built acute (Darent Valley Hospital); c. 4,500 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation via Kent & Medway ICB"},
            {"label": "PFI context", "value": "Darent Valley PFI — one of NHS's earliest large operational PFIs (signed 1997, opened 2000); shapes hard-FM/soft-FM workforce boundary (some FM staff are SPV-employed not trust-employed, reducing trust-direct NIC base)"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr"},
            {"label": "Maternity scale", "value": "c. 4,500 deliveries/yr"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove agency-locum backfill"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.3-1.6M/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £20M → 2023-24 £23M → 2024-25 £24.55M; 2025-26 forward step-up from NIC reform"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + Kent & Medway ICB"},
            {"label": "Evaluation evidence", "value": "CQC RN7 inspection; NHSE workforce returns; OBR EFO NIC line"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 pre-Apprenticeship Levy regime · Successor: post-Apr 2025 NIC baseline + 2030+ PFI hand-back planning"}
        ],
        "notes": "Dartford and Gravesham operates Darent Valley Hospital under one of the NHS's earliest large PFI deals — signed 1997 and opened 2000 — meaning the trust is in mid-stage hand-back planning ahead of expiry around 2030, with the IPA/HMT PFI Hand-Back unit's recommended structured engagement underway. The PFI structure shifts some hard-FM/soft-FM staff onto SPV employment rather than trust-direct, marginally narrowing the trust's NIC base relative to non-PFI peers of similar scale. Industrial action 2023-24 drove agency-locum backfill on acute medicine and emergency medicine. The April 2025 employer-NIC step-up is the dominant 2025-26 forward driver; partial NHSE NIC compensation flows through Kent & Medway ICB.",
        "sources": [
            {"publisher": "Dartford and Gravesham NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dvh.nhs.uk/about-us/publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Dartford and Gravesham provider profile (RN7)", "url": "https://www.cqc.org.uk/provider/RN7"}
        ],
        "related": ["Dartford and Gravesham NHS Trust", "Staff Costs", "NHS Acute Trusts", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "Infrastructure and Projects Authority", "HM Revenue and Customs"]
    },
    "Social security & levy — Walsall Healthcare NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Walsall Healthcare NHS Trust"}],
        "description": "Walsall Healthcare NHS Trust's £24.49M social security & levy line covers employer NIC and Apprenticeship Levy on the c. 4,500-WTE integrated acute + community workforce at Walsall Manor Hospital plus Walsall borough community services. The trust is in active group-model integration with Royal Wolverhampton NHS Trust under the Black Country Provider Collaborative — chair-in-common since 2020, shared corporate functions developing. April 2025 NIC step-up dominates forward-cost picture.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 285,000 Walsall borough catchment; c. 110,000 ED attendances/yr at Walsall Manor ED; c. 50,000 admissions/yr; integrated borough-wide community services (district nursing + therapies + community-paediatric + sexual-health).",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£24.49M"},
            {"label": "Trust scale", "value": "Single acute site (Walsall Manor Hospital) + integrated Walsall community services; c. 4,500 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation via Black Country ICB"},
            {"label": "Group-model context", "value": "Royal Wolverhampton + Walsall Healthcare chair-in-common since 2020 → Black Country Provider Collaborative; shared corporate functions developing"},
            {"label": "Catchment deprivation", "value": "Walsall borough — high IMD deprivation; broad community workforce footprint"},
            {"label": "Integrated community workforce", "value": "District nursing + therapies + community-paediatric + sexual-health — broadens NIC base"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove agency-locum backfill"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.3-1.6M/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £20M → 2023-24 £23M → 2024-25 £24.49M; 2025-26 forward step-up"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + (developing) Black Country Provider Collaborative shared functions + NHSBSA + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "CQC RBK inspection; NHSE workforce returns; Black Country group-model business case; OBR EFO NIC line"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate acute + Walsall PCT community baselines · Successor: post-Apr 2025 NIC + ongoing Black Country group-model integration with Royal Wolverhampton"}
        ],
        "notes": "Walsall Healthcare's pay-bill profile reflects integrated acute + community workforce alongside the developing group-model relationship with Royal Wolverhampton NHS Trust under the Black Country Provider Collaborative — chair-in-common since 2020 has shaped shared back-office and corporate-functions consolidation. The Walsall borough catchment carries high IMD deprivation, sustaining ED and community-team activity. Industrial action 2023-24 drove agency-locum backfill on acute medicine and surgical rotas. The April 2025 employer-NIC step-up is the dominant 2025-26 forward driver, with partial NHSE compensation flowing through Black Country ICB allocation under West Midlands Combined Authority context. Group-model maturation will progressively reshape the workforce-cost reporting boundary.",
        "sources": [
            {"publisher": "Walsall Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.walsallhealthcare.nhs.uk/about-us/publications/"},
            {"publisher": "Black Country ICB", "title": "Black Country Provider Collaborative + group-model arrangements", "url": "https://blackcountry.icb.nhs.uk/"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Walsall Healthcare provider profile (RBK)", "url": "https://www.cqc.org.uk/provider/RBK"}
        ],
        "related": ["Walsall Healthcare NHS Trust", "Staff Costs", "NHS Acute Trusts", "The Royal Wolverhampton NHS Trust", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "HM Revenue and Customs"]
    },
}
