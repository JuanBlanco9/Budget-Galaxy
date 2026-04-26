# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 06 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "PFI / LIFT charges — North East London NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "North East London NHS Foundation Trust"}],
        "description": "NELFT's £1.54M PFI / LIFT line covers unitary-charge payments on the trust's LIFT-vehicle community estate across Waltham Forest, Redbridge, Barking & Dagenham and Havering, plus residual PFI commitments on legacy Goodmayes Hospital ancillary blocks. NELFT is the single integrated MH + community + CAMHS provider for outer NE London; LIFT vehicles operated by Community Health Partnerships (CHP) own and lease back primary-care + community clinics, with unitary-charge service-fee paid by the trust as occupier.",
        "beneficiaries": "c. 6,800 staff serving c. 2.0M residents across 7 outer NE London + Essex boroughs; LIFT-financed primary-care + community premises housing CMHTs, CAMHS, district nursing and IAPT; legacy Goodmayes (Ilford) acute-MH inpatient hub.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.6 · NHS Act 2006 · Health and Care Act 2022 · Local Improvement Finance Trust framework (DH 2001) · Private Finance Initiative HMT guidance",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.54M"},
            {"label": "Vehicle type", "value": "Predominantly LIFT (Local Improvement Finance Trust) primary-care + community premises operated by CHP"},
            {"label": "LIFTCo partner", "value": "Community Health Partnerships (CHP) — DHSC-owned LIFT-vehicle holding company"},
            {"label": "Geographic spread", "value": "Waltham Forest, Redbridge, Barking & Dagenham, Havering + Essex boroughs (Brentwood, Basildon, Thurrock for community)"},
            {"label": "Unitary charge composition", "value": "Senior debt service + equity return + facilities-management service fee + lifecycle reserve"},
            {"label": "Concession term profile", "value": "25-year typical LIFT contracts; contracts signed 2004-2010 → expiries 2029-2035"},
            {"label": "Goodmayes context", "value": "Goodmayes Hospital legacy site (Ilford) — minor PFI ancillary residual + dominant freehold"},
            {"label": "IFRIC 12 treatment", "value": "Where LIFT premises meet IFRIC 12 control test, asset + liability on-balance-sheet; service fee bifurcated finance + opex"},
            {"label": "Funding trajectory", "value": "Stable c. £1.5M-£1.6M annual range — RPI-linked unitary-charge inflation offset by amortising debt"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Community Health Partnerships LIFTCo + Capita / Equitix-style equity holders"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NEL ICB · LIFT framework owned by DHSC via CHP"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2004 GP-owned + DHA-owned premises · Successor: LIFT contract expiry 2029-2035 → ICS estate consolidation under NEL ICB"}
        ],
        "notes": "NELFT's PFI/LIFT line is dominated by LIFT-vehicle community premises rather than classic acute-PFI — reflecting the 2000s-era investment in primary-care + community estate across outer NE London under the DH LIFT framework. Unitary charges are RPI-indexed and contract-locked, providing budget certainty but limited flexibility as service models shift towards home-based care. The 2029-2035 LIFT contract-expiry window is the strategic decision point: NEL ICB will need to decide whether to extend, hand back to CHP, or buy out residual contracts. The Goodmayes Hospital site is largely freehold, with only minor ancillary PFI residual. NHS Property Services interactions and CHP service-charge methodology disputes are sector-wide friction points affecting LIFT-occupier trusts.",
        "sources": [
            {"publisher": "North East London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nelft.nhs.uk/about-us-publications-annual-report"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review and portfolio data", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 6 — Service concession arrangements)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 — annual report on contingent liabilities", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2023-summary-data"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and contracts after contract expiry", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-contracts-after-contract-expiry/"}
        ],
        "related": ["North East London NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Kent and Medway NHS and Social Care Partnership Trust": {
        "aliases": [{"name": "Business rates", "parent": "Kent and Medway NHS and Social Care Partnership Trust"}],
        "description": "KMPT's £1.54M 2024-25 business-rates charge reflects VOA-set rateable values × 49.9p / 54.6p UBR multipliers across acute MH inpatient hubs (St Martin's Hospital Canterbury, Priority House Maidstone, Littlebrook Hospital Dartford, A Block Medway Maritime) and c. 50+ community-MH and CAMHS sites across Kent and Medway. NHS FTs and trusts do not qualify for charitable rate relief; the 2023 VOA revaluation rebased Kent commercial RVs and the 2026 antecedent valuation (3-year cycle under NDRA 2023) is in train.",
        "beneficiaries": "Approximately 50+ occupied hereditaments across Canterbury, Maidstone, Dartford, Medway, Ashford, Thanet and rural East Kent; serves a registered population c. 1.9M across Kent county + Medway unitary; specialist forensic, secure and CAMHS services for Kent and Medway ICS.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.54M"},
            {"label": "Hereditament count", "value": "c. 50+ occupied sites — acute MH, community, CAMHS, forensic"},
            {"label": "Major sites driving line", "value": "St Martin's Hospital (Canterbury) + Priority House (Maidstone) + Littlebrook Hospital (Dartford) + A Block (Medway Maritime)"},
            {"label": "Geographic spread", "value": "Kent county + Medway unitary — c. 12 billing authorities (KCC districts + Medway UA)"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs / trusts not registered charities"},
            {"label": "VOA 2023 revaluation impact", "value": "Kent commercial RVs broadly stable post-pandemic; rural RVs slight downward rebase"},
            {"label": "NHSPS interaction", "value": "Significant share of community-clinic estate held via NHSPS lease — rates passed through to KMPT as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.3M → 2024-25 £1.54M — UBR-tracking + minor estate growth"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 13 billing authorities (Kent districts + Medway)"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance + Kent and Medway ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023 3-year cycle"}
        ],
        "notes": "KMPT's business-rates line is structurally driven by the geographic spread across all Kent districts plus Medway unitary — c. 13 separate billing authorities each issuing separate demand notices, multiplying administrative complexity. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase Kent commercial RVs marginally upward as office and warehousing demand recovers. NHSPS-leased community clinics pass rates through to KMPT as occupier, complicating service-charge recharge boundaries — a sector-wide friction. Kent and Medway ICS estate consolidation may eventually reduce hereditament count, but the current trajectory tracks UBR + minor expansion.",
        "sources": [
            {"publisher": "Kent and Medway NHS and Social Care Partnership Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kmpt.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Kent and Medway NHS and Social Care Partnership Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Sussex Partnership NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "Transport (business + patient) — Sheffield Health and Social Care NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Sheffield Health and Social Care NHS Foundation Trust"}],
        "description": "SHSC's £1.54M transport line covers staff business mileage for community-MH, AMHP, crisis-team and learning-disability outreach across Sheffield, plus inter-site patient transfers between the Longley Centre (Northern General), the Michael Carlisle Centre (Nether Edge), Forest Lodge and Forest Close PICUs and dozens of community CMHTs. SHSC is unusual as a city-state MH trust (Sheffield only) with a tight geographic catchment but a high-density urban estate.",
        "beneficiaries": "c. 2,800 staff serving c. 580,000 Sheffield residents; c. 200 inpatient MH + LD beds across Longley, Michael Carlisle, Forest Lodge and Forest Close; concentrated city catchment generates frequent inter-site short-distance transfers rather than rural long-distance mileage.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.54M"},
            {"label": "Catchment area", "value": "Sheffield city only — c. 580,000 residents (single-city trust)"},
            {"label": "Site footprint", "value": "Longley Centre + Michael Carlisle Centre + Forest Lodge PICU + Forest Close + community CMHT bases"},
            {"label": "Mileage profile", "value": "High-frequency short-distance urban transfers; less rural long-distance mileage than peer MH trusts"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance contracted via Yorkshire Ambulance Service (YAS) + private secure-transport"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "Pool car + lease vehicle fleet", "value": "Mix of pool cars (CCS framework) + lease + staff-private; partial EV transition under Sheffield Clean Air Zone"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.1M → 2024-25 £1.54M — uplift from post-pandemic in-person community visit recovery + fuel CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with YAS + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports 2022-2024; SY ICS estate review 2024"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate-trust LD/community split · Successor: SY ICS shared-fleet pooling + Sheffield CAZ EV transition"}
        ],
        "notes": "SHSC's transport line is unusual among MH-trust peers because Sheffield is a single-city catchment — the trust does not bear the rural-mileage premium that drives transport at NSFT or Cornwall Partnership, but its high-density urban estate generates frequent short-distance inter-site transfers, particularly around the Longley / Michael Carlisle / Forest Lodge axis. Sheffield's Clean Air Zone (Class C, live since 2023) is a forcing function for EV transition of pool cars and lease vehicles. YAS handles s.136 conveyance under the South Yorkshire ICS PTS contract. SY ICS shared-fleet pooling (with Sheffield Children's, Sheffield Teaching Hospitals and Rotherham Doncaster & South Humber) is the medium-term efficiency lever.",
        "sources": [
            {"publisher": "Sheffield Health and Social Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.shsc.nhs.uk/about-us/publications-and-strategies/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "SHSC inspection reports + provider profile", "url": "https://www.cqc.org.uk/provider/RXG"},
            {"publisher": "Sheffield City Council", "title": "Clean Air Zone Class C — Sheffield 2023", "url": "https://www.sheffield.gov.uk/clean-air-zone"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Patient transport services contract", "url": "https://www.yas.nhs.uk/patient-transport-service/"}
        ],
        "related": ["Sheffield Health and Social Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Rotherham Doncaster and South Humber NHS Foundation Trust", "Mental Health Act 1983"]
    },
    "Amortisation — Black Country Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Black Country Healthcare NHS Foundation Trust"}],
        "description": "Black Country Healthcare's £1.54M amortisation line is the IAS 38 charge on capitalised intangibles — predominantly clinical-system software (RiO and Oracle modules), the trust's Frontline Digitisation EPR investment, and capitalised licences across Dudley, Sandwell, Walsall and Wolverhampton. The trust was formed by the 2020 merger of Black Country Partnership FT and Dudley & Walsall MH Partnership Trust, which generated significant integration-driven software capitalisation across 2021-2023.",
        "beneficiaries": "c. 4,000 substantive WTE clinical and admin users on capitalised EPR + clinical-system software; serves c. 1.2M residents across Dudley, Sandwell, Walsall and Wolverhampton; underpins community-MH, CAMHS, learning-disability and inpatient care.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation programme (NHSE 2022-2025)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.54M"},
            {"label": "Composition", "value": "Capitalised software (clinical EPR + corporate systems) + capitalised licences + integration-software developed post-merger"},
            {"label": "Frontline Digitisation context", "value": "Trust included in NHSE Frontline Digitisation EPR rollout — capitalisation of EPR-related development + configuration"},
            {"label": "Useful life convention", "value": "Software typically 3-7 years per DHSC GAM 2024-25 ch.5; longer-life major systems 7-10 years"},
            {"label": "Merger context", "value": "Formed 1 April 2020 via merger of Black Country Partnership FT + Dudley & Walsall MH Partnership Trust → integration-driven software capitalisation 2021-2023"},
            {"label": "Capitalisation threshold", "value": "DHSC GAM £5,000 individual or £250,000 grouped for software"},
            {"label": "Funding trajectory", "value": "Sustained upward 2020-21 c. £0.7M → 2024-25 £1.54M — driven by EPR rollout + integration capitalisation"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams; vendor stack includes RiO (Servelec/Access), Oracle"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate (Frontline Digitisation) + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme tracker; trust digital maturity assessment (DMA) reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate-trust software stacks (BCP + DWMHPT) · Successor: ICS-shared EPR under Black Country ICS digital strategy"}
        ],
        "notes": "Black Country Healthcare's amortisation profile is shaped by both the Frontline Digitisation capital injection and the 2020 merger integration: combining two separate trusts generated significant capitalised configuration work as RiO and corporate systems were unified across Dudley, Sandwell, Walsall and Wolverhampton operations. The £1.54M line will continue rising as Frontline Digitisation EPR investments come into amortisation, before levelling out in the late 2020s as initial capitalised tranches reach end-of-life. Useful-life judgement is the key reporting risk — long-lived clinical software is typically amortised over 7-10 years, but rapid Frontline Digitisation refresh cycles may require shorter conventions. Black Country ICS digital strategy is exploring shared EPR procurement to reduce future per-trust capitalisation.",
        "sources": [
            {"publisher": "Black Country Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.blackcountryhealthcare.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme — EPR rollout", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "Care Quality Commission", "title": "Black Country Healthcare NHS FT provider profile", "url": "https://www.cqc.org.uk/provider/RYK"}
        ],
        "related": ["Black Country Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Frontline Digitisation programme", "Amortisation — Greater Manchester Mental Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — South West London and St George's Mental Health NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "South West London and St George's Mental Health NHS Trust"}],
        "description": "SWLSTG's £1.53M business-rates charge reflects VOA-set rateable values × 49.9p / 54.6p UBR multipliers across an estate dominated by Springfield University Hospital (Tooting) — currently mid-redevelopment under the Springfield programme — plus Tolworth Hospital, Queen Mary's (Roehampton) and dispersed community-MH and CAMHS sites across Wandsworth, Merton, Sutton, Kingston and Richmond. Inner-London RV concentration plus the Springfield rebuild generate above-peer rates intensity.",
        "beneficiaries": "Approximately 60+ occupied hereditaments across 5 SW London boroughs; serves a registered population c. 1.1M; Springfield University Hospital is the trust's flagship 5 SW London-borough acute-MH hub plus regional secure + national OCD/eating-disorders services.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.53M"},
            {"label": "Hereditament count", "value": "c. 60+ occupied sites — acute MH, community, CAMHS, secure, specialist"},
            {"label": "Major sites driving line", "value": "Springfield University Hospital (Tooting) + Tolworth Hospital + Queen Mary's (Roehampton)"},
            {"label": "Springfield redevelopment context", "value": "£150M+ rebuild programme — phased completions 2022-2027 reshaping rateable footprint and prompting VOA reassessments"},
            {"label": "Geographic spread", "value": "Wandsworth, Merton, Sutton, Kingston, Richmond — 5 inner-SW London billing authorities"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 under Autumn Statement 2023"},
            {"label": "Inner-London RV premium", "value": "Tooting + Roehampton postcodes carry elevated commercial RVs vs national average"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS trusts not registered charities"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.4M → 2024-25 £1.53M — UBR-tracking + Springfield-rebuild reassessment effects"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 5 billing authorities (Wandsworth, Merton, Sutton, Kingston, Richmond)"},
            {"label": "Policy owner", "value": "DHSC + MHCLG + NHSE Provider Finance + SW London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023 3-year cycle"}
        ],
        "notes": "SWLSTG's business-rates exposure is shaped by the Springfield University Hospital redevelopment — a £150M+ phased rebuild that began delivering completions from 2022 and is progressively replacing Victorian asylum-era buildings with modern inpatient and community facilities. Each phase prompts VOA reassessment of the hereditament, with new-build rateable values typically higher per m² than the legacy fabric being demolished. The 2026 revaluation under NDRA 2023's 3-year cycle will rebase the line again. Inner-SW-London commercial RVs at Tooting and Roehampton remain elevated. NHSPS-leased community clinics pass rates through to SWLSTG as occupier — a sector-wide friction point. The trust's specialist eating-disorders and OCD services occupy ringfenced Springfield space, contributing to overall RV.",
        "sources": [
            {"publisher": "South West London and St George's Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swlstg.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "South West London and St George's Mental Health NHS Trust", "title": "Springfield Hospital redevelopment programme", "url": "https://www.swlstg.nhs.uk/about-us/our-future"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"}
        ],
        "related": ["South West London and St George's Mental Health NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — West London NHS Trust", "NHS Property Services Ltd"]
    },
    "Business rates — Oxford Health NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Oxford Health NHS Foundation Trust"}],
        "description": "Oxford Health's £1.52M 2024-25 business-rates charge reflects VOA-set rateable values × 49.9p / 54.6p UBR multipliers across the Warneford Hospital + Littlemore Mental Health Centre site (Oxford), the Whiteleaf Centre (Aylesbury), Wallingford Community Hospital and a wide community-MH + community-physical-health estate across Oxfordshire, Buckinghamshire, Wiltshire (CAMHS) and BSW. Combined MH + community + CAMHS remit drives a high hereditament count.",
        "beneficiaries": "Approximately 80+ occupied hereditaments across Oxfordshire, Buckinghamshire and partial Wiltshire/Swindon (CAMHS); serves c. 1.9M residents with combined MH + community-physical-health + LD + CAMHS services; Warneford Hospital is the historic Oxford acute-MH hub.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.52M"},
            {"label": "Hereditament count", "value": "c. 80+ occupied sites across MH inpatient, community, CAMHS, community-physical-health, dental"},
            {"label": "Major sites driving line", "value": "Warneford Hospital (Oxford) + Littlemore MHC + Whiteleaf Centre (Aylesbury) + Wallingford CH + community bases"},
            {"label": "Geographic spread", "value": "Oxfordshire + Buckinghamshire + parts of Wiltshire/Swindon (CAMHS) + BSW"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs not registered charities"},
            {"label": "Warneford redevelopment context", "value": "Oxford University Hospitals + Oxford Health Warneford Park rebuild proposal — long-term planning, not yet delivering RV impact"},
            {"label": "VOA 2023 revaluation", "value": "Oxford commercial RVs broadly stable; rural Oxfordshire and Bucks slight downward rebase"},
            {"label": "NHSPS interaction", "value": "Significant share of community-clinic estate held via NHSPS lease — rates passed through to Oxford Health"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.3M → 2024-25 £1.52M — UBR-tracking + minor estate growth"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + multiple billing authorities (Oxford City, Cherwell, West Oxon, South Oxon, Vale of White Horse, Bucks UA, Swindon)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023; Warneford Park rebuild long-term"}
        ],
        "notes": "Oxford Health's business-rates line is structurally elevated by the combined MH + community-physical-health + CAMHS remit across two counties plus Wiltshire CAMHS — a much wider hereditament footprint than MH-only peers of similar size. The Warneford Park rebuild proposal (a joint Oxford Health + Oxford University Hospitals + Oxford University vision for the Warneford site) is in long-term planning and not yet delivering RV impact, but will rebase the line significantly when delivered. NHSPS-leased community clinics across Oxfordshire and Bucks pass rates through to Oxford Health as occupier, complicating service-charge boundaries. The 2026 VOA revaluation under NDRA 2023's 3-year cycle is expected to rebase Oxford commercial RVs marginally upward.",
        "sources": [
            {"publisher": "Oxford Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.oxfordhealth.nhs.uk/about-us/corporate/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Oxford Health NHS Foundation Trust", "title": "Warneford Park redevelopment vision", "url": "https://www.oxfordhealth.nhs.uk/warneford-park/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"}
        ],
        "related": ["Oxford Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Sussex Partnership NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "Establishment costs — Cheshire and Wirral Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Cheshire and Wirral Partnership NHS Foundation Trust"}],
        "description": "CWP's £1.52M establishment line covers stationery, postage, telephony, mobile-device estate, printing and courier across Countess of Chester Health Park (Bowmere Hospital), Springview Wirral, Millbrook Mental Health Unit (Macclesfield), and dozens of community-MH, CAMHS and learning-disability bases across Cheshire and Wirral. Combined MH + LD + community remit across c. 1.0M residents and 80+ sites generates a high site-count establishment base.",
        "beneficiaries": "c. 3,800 staff serving c. 1.0M residents across Cheshire West, Cheshire East and Wirral; combined MH + LD + CAMHS + community service across 80+ sites including hospitals, community hospitals and CAMHS clinics.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.52M"},
            {"label": "Site footprint", "value": "Bowmere (Chester) + Springview (Wirral) + Millbrook (Macclesfield) + 80+ community bases"},
            {"label": "Headcount served", "value": "c. 3,800 substantive WTE staff"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying"},
            {"label": "Mobile-device estate", "value": "Substantial laptop + smartphone rollout post-2020 supporting community-mobile-working"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + Crown Commercial Service telephony framework"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.1M → 2024-25 £1.52M — sustained growth tracking community-mobile-working + CPI"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; NHSE Model Hospital benchmarking"},
            {"label": "CQC context", "value": "CQC Good rating sustained — supports continued mobile-working investment"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paper-heavy clinical workflow · Successor: Frontline Digitisation EPR rollout reducing print + postage but raising licensing"}
        ],
        "notes": "CWP's establishment line tracks the combined MH + LD + community + CAMHS remit across Cheshire and Wirral — a wider hereditament footprint than MH-only peers, generating higher per-staff postage, telephony and mobile-device costs. The trust's geographic spread between Wirral peninsula and rural East Cheshire (Macclesfield, Knutsford) drives sustained mobile-device and connectivity investment, particularly post-2020 as community-mobile-working scaled. The Frontline Digitisation EPR rollout is expected to compress printing and postage but raise licensing recurring cost — net establishment broadly flat in real terms. Cheshire and Merseyside ICB digital strategy is exploring shared procurement to flatten growth.",
        "sources": [
            {"publisher": "Cheshire and Wirral Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cwp.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Model Hospital — community + mental health benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "Office consumables and stationery framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Cheshire and Wirral Partnership NHS FT provider profile", "url": "https://www.cqc.org.uk/provider/RXA"}
        ],
        "related": ["Cheshire and Wirral Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Bradford District Care NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Impairments net of reversals — Derbyshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Derbyshire Healthcare NHS Foundation Trust"}],
        "description": "Derbyshire Healthcare's £1.49M impairments line is a non-cash IAS 36 charge against the trust's owned property, plant and equipment — predominantly the Kingsway Hospital (Derby) acute-MH site, the Radbourne Unit, the Hartington Unit (Chesterfield) and dispersed community-MH bases. NHS trust impairments are largely Modern Equivalent Asset (MEA) revaluation losses arising from the DHSC-mandated annual desktop revaluation cycle, plus condition-driven write-downs where surveys identify backlog maintenance.",
        "beneficiaries": "c. 2,400 staff and c. 1.05M Derbyshire residents using affected estate — Kingsway Hospital (Derby acute MH), Radbourne Unit (acute), Hartington Unit (Chesterfield) and community-MH bases across Derby city, Derbyshire Dales, High Peak and rural Derbyshire.",
        "legal_basis": "IAS 36 Impairment of Assets · IAS 16 Property, Plant and Equipment · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · HM Treasury FReM",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£1.49M"},
            {"label": "Composition", "value": "MEA revaluation losses + condition-driven write-downs on owned estate"},
            {"label": "Major sites in scope", "value": "Kingsway Hospital (Derby) + Radbourne Unit + Hartington Unit (Chesterfield) + community-MH bases"},
            {"label": "Revaluation methodology", "value": "Annual desktop indexation per DHSC GAM 2024-25 ch.4 + 5-yearly full external revaluation by district valuer"},
            {"label": "Modern Equivalent Asset basis", "value": "MEA replaces depreciated-replacement-cost on specialised NHS assets — typically generates downward adjustments where modern build-cost falls below historic carrying value"},
            {"label": "Backlog maintenance context", "value": "ERIC return shows trust backlog — high-risk + significant-risk components feed condition-led write-downs"},
            {"label": "Charge volatility", "value": "Year-to-year volatility driven by BCIS construction-cost indices + survey timing — not operational"},
            {"label": "Funding trajectory", "value": "Volatile — multi-year average c. £1-2M reflects revaluation cycle"},
            {"label": "Delivery body", "value": "Trust Finance + District Valuer Services (Valuation Office Agency)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Joined Up Care Derbyshire ICB"},
            {"label": "Evaluation evidence", "value": "NHS Estates Returns Information Collection (ERIC) annual data; NAO 2020 report on NHS estate"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2009 historic-cost basis · Successor: ICS-shared estate strategy + New Hospital Programme considerations"}
        ],
        "notes": "Derbyshire Healthcare's impairments line is a function of the DHSC-mandated MEA revaluation cycle rather than operational decisions — the annual indexation against BCIS construction-cost movements typically generates revaluation losses on specialised MH inpatient assets where modern build-cost methodology falls below historic carrying value. Kingsway Hospital and the Radbourne Unit are the largest in-scope assets; the Hartington Unit (Chesterfield) handles north Derbyshire acute MH. Backlog maintenance pressure feeds condition-led write-downs on a periodic basis. The line is non-cash and does not affect operational deliverability, but distorts year-on-year financial-position reporting. JU Care Derbyshire ICB estate strategy is exploring rationalisation.",
        "sources": [
            {"publisher": "Derbyshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.derbyshirehealthcareft.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 4 — Property, plant and equipment)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates/estates-returns-information-collection/"},
            {"publisher": "National Audit Office", "title": "NHS backlog maintenance — Spotlight on the NHS estate", "url": "https://www.nao.org.uk/reports/nhs-backlog-maintenance/"},
            {"publisher": "IFRS Foundation", "title": "IAS 36 Impairment of Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-36-impairment-of-assets/"}
        ],
        "related": ["Derbyshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Impairments net of reversals — North East London NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Black Country Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Black Country Healthcare NHS Foundation Trust"}],
        "description": "Black Country Healthcare's £1.46M transport line covers business mileage for community-MH, AMHP, crisis, CAMHS and learning-disability outreach across Dudley, Sandwell, Walsall and Wolverhampton, plus inter-site transfers between Penn Hospital (Wolverhampton), Dorothy Pattison (Walsall), Bushey Fields (Dudley) and Hallam Street (Sandwell). The 2020 trust-merger created a four-borough geography that drives sustained business-mileage volumes.",
        "beneficiaries": "c. 4,000 staff serving c. 1.2M residents across the four Black Country boroughs; c. 250+ inpatient MH + LD beds across Penn, Dorothy Pattison, Bushey Fields and Hallam Street; integrated-care contracts add school-nursing and CAMHS travel.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.46M"},
            {"label": "Catchment area", "value": "Dudley, Sandwell, Walsall, Wolverhampton — c. 1.2M residents"},
            {"label": "Site footprint", "value": "Penn Hospital + Dorothy Pattison + Bushey Fields + Hallam Street + community CMHTs"},
            {"label": "Merger context", "value": "Formed 1 April 2020 via merger — four-borough geography sustains higher inter-site mileage than pre-merger separate-trust footprints"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance contracted via West Midlands Ambulance Service + private secure-transport"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "Pool car + lease vehicle fleet", "value": "Mix of pool cars (CCS framework) + lease + staff-private; partial EV transition under Birmingham + Black Country Clean Air Zone planning"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.0M (legacy two-trust baseline) → 2024-25 £1.46M — uplift driven by post-merger integration + post-pandemic recovery + fuel CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with WMAS + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports 2022-2024; Black Country ICS estate review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate-trust footprints (BCP + DWMHPT) · Successor: BC ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "Black Country Healthcare's transport line is structurally elevated by the four-borough Black Country geography created at the 2020 merger — Dudley, Sandwell, Walsall and Wolverhampton each retain distinct acute-MH inpatient hubs, generating routine inter-site transfers that did not exist when the predecessor trusts operated within their own footprints. The trust's combined MH + community-physical-health + LD remit further widens the mileage base. WMAS handles s.136 conveyance under the West Midlands ICS PTS contract. Birmingham + Black Country Clean Air Zone considerations drive partial EV transition planning. The merger-era integration is now stable; future trajectory tracks fuel CPI plus modest community-recovery uplift.",
        "sources": [
            {"publisher": "Black Country Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.blackcountryhealthcare.nhs.uk/about-us/our-publications"},
            {"publisher": "Care Quality Commission", "title": "Black Country Healthcare NHS FT provider profile", "url": "https://www.cqc.org.uk/provider/RYK"},
            {"publisher": "West Midlands Ambulance Service", "title": "Patient transport services", "url": "https://wmas.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Birmingham City Council", "title": "Clean Air Zone — Birmingham + Black Country planning", "url": "https://www.brumbreathes.co.uk/"}
        ],
        "related": ["Black Country Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Birmingham and Solihull Mental Health NHS Foundation Trust", "Mental Health Act 1983"]
    },
    "Lease expenditure — Hertfordshire Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Hertfordshire Partnership University NHS Foundation Trust"}],
        "description": "HPFT's £1.45M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio includes NHSPS-leased community-MH and CAMHS bases across Hertfordshire and parts of Buckinghamshire, Norfolk and Essex (specialist services), plus contracted supported-living and rehabilitation premises. HPFT's 'University' designation reflects strong R&D ties with University of Hertfordshire, with academic-collaboration leased space contributing.",
        "beneficiaries": "c. 4,000 staff and a registered population c. 1.2M across Hertfordshire, with national specialist learning-disability and CAMHS services for parts of East of England + Buckinghamshire; c. 70+ leased community premises plus academic-collaboration space.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.45M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with corresponding depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 70+ NHSPS + private-landlord premises across Hertfordshire + specialist out-of-area sites"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships LIFT + private landlords"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer LIFT contracts to 25+ years"},
            {"label": "University collaboration context", "value": "R&D ties with University of Hertfordshire — small leased academic-collaboration space contributes"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.8M operating lease → 2022-23 c. £1.2M ROU first year → 2024-25 £1.45M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP + private landlords"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Hertfordshire and West Essex ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + ICS estate consolidation"}
        ],
        "notes": "HPFT's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet and has continued to grow as NHSPS pursued market-rent uplifts on community clinics. The NHSPS / mental-health-trust dispute over service-charge methodology and market-rent rebasing is a sector-wide friction point — HPFT's geographically-dispersed Hertfordshire community footprint exposes it more than acute-only peers. The trust's specialist learning-disability and CAMHS services for parts of East of England plus Buckinghamshire add out-of-area leased premises to the portfolio. University of Hertfordshire R&D collaboration contributes a small academic-leased footprint. Hertfordshire and West Essex ICS estate consolidation is the medium-term lever.",
        "sources": [
            {"publisher": "Hertfordshire Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hpft.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "HM Treasury", "title": "Public Expenditure System (PES) discount rates", "url": "https://www.gov.uk/government/publications/public-spending-statistics-release-schedule"}
        ],
        "related": ["Hertfordshire Partnership University NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Mersey Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Greater Manchester Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Greater Manchester Mental Health NHS Foundation Trust"}],
        "description": "GMMH's £1.40M amortisation line is the IAS 38 charge on capitalised intangibles — predominantly clinical-system software, the trust's Frontline Digitisation EPR investment, and capitalised licences across Prestwich, Edenfield, Park House and Trafford operations. The Edenfield Centre Panorama exposé (2022) and subsequent CQC enforcement drove additional capitalised investment in incident-reporting, electronic-observation and quality-monitoring software embedded in the trust's RiO and supplementary clinical systems.",
        "beneficiaries": "c. 6,500 substantive WTE clinical and admin users on capitalised software; serves c. 1.4M residents of Manchester, Salford, Trafford and Bolton plus regional secure-services catchment across NW England; c. 1,300 inpatient beds underpinned by EPR.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation programme (NHSE 2022-2025)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.40M"},
            {"label": "Composition", "value": "Capitalised software (RiO + supplementary clinical systems) + capitalised licences + integration-software + Edenfield-remediation digital tooling"},
            {"label": "Frontline Digitisation context", "value": "Trust included in NHSE Frontline Digitisation EPR rollout — capitalisation of EPR-related development + configuration"},
            {"label": "Edenfield digital remediation", "value": "Post-2022 Panorama capitalisation of incident-reporting + electronic-observation + quality-monitoring software"},
            {"label": "Useful life convention", "value": "Software typically 3-7 years per DHSC GAM 2024-25 ch.5; longer-life major systems 7-10 years"},
            {"label": "Capitalisation threshold", "value": "DHSC GAM £5,000 individual or £250,000 grouped for software"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.8M → 2024-25 £1.40M — rising as Frontline Digitisation + Edenfield-remediation software comes into amortisation"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams; vendor stack includes RiO (Servelec/Access) + Datix/RLDatix + supplementary specialist tools"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate (Frontline Digitisation) + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme tracker; CQC special-measures exit 2024 referenced digital-quality investment"},
            {"label": "CQC context", "value": "Edenfield Panorama (2022) → CQC enforcement → digital-quality remediation drove software capitalisation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 separate-trust software (post-Manchester acquisition expansion) · Successor: GM ICS shared EPR + AI-augmented clinical-decision tooling"}
        ],
        "notes": "GMMH's amortisation profile is shaped by both the Frontline Digitisation capital injection and the post-Edenfield digital-remediation programme: from late 2022, the trust capitalised significant investment in incident-reporting, electronic-observation, body-worn-camera management, and quality-monitoring software embedded in or adjacent to the RiO clinical system as part of CQC-mandated remediation. The £1.40M line will continue rising as those capitalised tranches come into amortisation, before levelling out in the late 2020s. Useful-life judgement is the key reporting risk — clinical software is typically amortised over 7-10 years, but rapid Frontline Digitisation refresh cycles may require shorter conventions. GM ICS shared EPR procurement is the medium-term efficiency lever.",
        "sources": [
            {"publisher": "Greater Manchester Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gmmh.nhs.uk/annual-report"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme — EPR rollout", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "GMMH Edenfield Centre inspection reports + enforcement", "url": "https://www.cqc.org.uk/provider/RXV"},
            {"publisher": "BBC Panorama", "title": "Undercover Hospital Abuse Scandal (Edenfield Centre)", "url": "https://www.bbc.co.uk/news/uk-england-manchester-63076418"}
        ],
        "related": ["Greater Manchester Mental Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Frontline Digitisation programme", "Amortisation — Black Country Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Derbyshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Derbyshire Healthcare NHS Foundation Trust"}],
        "description": "Derbyshire Healthcare's £1.39M PFI / LIFT line covers unitary-charge payments on the Kingsway Hospital (Derby) PFI scheme — the trust's principal acute-MH inpatient site delivered under a 2009 PFI contract — plus residual LIFT-vehicle community premises across the county. The Kingsway PFI replaced the legacy Pastures Hospital and includes 116 inpatient beds across acute MH, PICU, older-people's MH and rehabilitation wards, with unitary charge covering senior debt, equity return, FM and lifecycle.",
        "beneficiaries": "c. 1,050,000 Derbyshire residents; c. 200 inpatient beds across the trust, with c. 116 at Kingsway PFI; LIFT community premises hosting CMHTs and CAMHS bases across Derby city, Derbyshire Dales, High Peak and rural Derbyshire.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.6 · NHS Act 2006 · Health and Care Act 2022 · Local Improvement Finance Trust framework (DH 2001) · Private Finance Initiative HMT guidance",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.39M"},
            {"label": "Vehicle types", "value": "Kingsway Hospital PFI (acute-MH inpatient) + LIFT community premises"},
            {"label": "Kingsway PFI", "value": "Operational 2009; replaced legacy Pastures Hospital; c. 116 inpatient beds (acute, PICU, older-people, rehab)"},
            {"label": "Concession term", "value": "Typical 30-year PFI term — Kingsway expiry mid-2030s"},
            {"label": "Unitary charge composition", "value": "Senior debt service + equity return + facilities-management service fee + lifecycle reserve"},
            {"label": "RPI indexation", "value": "Unitary charge RPI/CPI-linked per concession agreement"},
            {"label": "IFRIC 12 treatment", "value": "Kingsway capitalised on-balance-sheet under IFRIC 12 control test; service fee bifurcated finance + opex"},
            {"label": "LIFT component", "value": "Community Health Partnerships LIFTCo premises across Derbyshire — CMHT + CAMHS bases"},
            {"label": "Funding trajectory", "value": "Stable c. £1.3M-£1.4M annual range — RPI uplifts offset by amortising debt"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + PFI SPV + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + JU Care Derbyshire ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2009 Pastures Hospital legacy estate · Successor: PFI expiry mid-2030s → handback or refinance decision"}
        ],
        "notes": "Derbyshire Healthcare's PFI line is dominated by the Kingsway Hospital scheme (operational 2009) — a relatively modern PFI build that replaced the legacy Pastures Hospital and consolidated acute MH, PICU, older-people's MH and rehabilitation wards on a single Derby site. The unitary charge is RPI-indexed, providing budget certainty but limited flexibility as service models evolve. The mid-2030s expiry window is the strategic decision point: hand back, extend, or buy out residual contract under NAO-tracked PFI-expiry guidance. Smaller LIFT components add CHP-vehicle community premises to the line. Joined Up Care Derbyshire ICB estate strategy will need to plan post-PFI continuity well in advance of expiry.",
        "sources": [
            {"publisher": "Derbyshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.derbyshirehealthcareft.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 — annual report on contingent liabilities", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2023-summary-data"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 6 — Service concession arrangements)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and contracts after contract expiry", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-contracts-after-contract-expiry/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"}
        ],
        "related": ["Derbyshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Norfolk and Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Norfolk and Suffolk NHS Foundation Trust"}],
        "description": "NSFT's £1.37M establishment line covers stationery, postage, telephony, mobile-device estate, printing and courier across Hellesdon Hospital (Norwich), Northgate (Yarmouth), Chatterton House (King's Lynn), Woodlands (Ipswich) and c. 50 community-MH bases across rural Norfolk and Suffolk. The trust's repeated CQC special-measures cycles (2015-2023) and the Niche unexpected-deaths review series have sustained a high external-correspondence + inquest-related printing volume on top of routine establishment cost.",
        "beneficiaries": "c. 3,800 substantive WTE clinical and admin staff covering c. 1.7M residents across Norfolk and Suffolk; combined acute MH + community + CAMHS + LD remit across 4 acute hubs and c. 50 community bases; rural footprint c. 5,500 km².",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.37M"},
            {"label": "Site footprint", "value": "Hellesdon (Norwich) + Northgate (Yarmouth) + Chatterton House (King's Lynn) + Woodlands (Ipswich) + c. 50 community bases"},
            {"label": "Headcount served", "value": "c. 3,800 substantive WTE"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying + minor office consumables"},
            {"label": "Inquest/governance correspondence", "value": "Niche reports + repeated CQC special-measures cycles drove sustained external correspondence + inquest-related printing"},
            {"label": "Rural mileage / postage premium", "value": "Sparse rural geography drives higher per-staff postage and courier than urban-trust peers"},
            {"label": "Mobile-device estate", "value": "Community-mobile-working investment from c. 2020 — laptops, smartphones, MiFi for crisis + community teams"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + Crown Commercial Service telephony framework"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.0M → 2024-25 £1.37M — sustained growth tracking community-mobile-working + CPI + remediation correspondence"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Norfolk and Waveney ICB + Suffolk and North East Essex ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 separate Norfolk + Suffolk MH trusts · Successor: Frontline Digitisation EPR rollout reducing print + postage"}
        ],
        "notes": "NSFT's establishment line is shaped by both the structural rural-geography premium of the Norfolk + Suffolk catchment and the trust's governance history — sustained inquest, family-liaison and Niche-review correspondence over the 2015-2023 special-measures cycle has kept printing, postage and courier volumes elevated relative to peer trusts of similar size. Mobile-device estate growth post-2020 supports community-team mobile working across rural geography. The Frontline Digitisation EPR rollout is expected to compress printing and postage but raise licensing recurring cost. The two-ICB footprint (Norfolk & Waveney ICB + Suffolk & North East Essex ICB) adds administrative complexity. CQC's improved 2024 rating and stable governance cycle should slowly reduce the inquest-correspondence component.",
        "sources": [
            {"publisher": "Norfolk and Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nsft.nhs.uk/publications/"},
            {"publisher": "NHS England", "title": "Niche unexpected-deaths reviews — NSFT series", "url": "https://www.england.nhs.uk/east-of-england/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NSFT inspection reports + special-measures history (RMY)", "url": "https://www.cqc.org.uk/provider/RMY"},
            {"publisher": "NHS Supply Chain", "title": "Office consumables and stationery framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Norfolk and Suffolk NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Lincolnshire Partnership NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Business rates — Cornwall Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Cornwall Partnership NHS Foundation Trust"}],
        "description": "Cornwall Partnership's £1.35M 2024-25 business-rates charge reflects VOA-set rateable values × 49.9p / 54.6p UBR multipliers across an estate dominated by Bodmin Hospital (Longreach acute-MH unit), the Garden House (St Lawrence's, Bodmin) and a wide community-MH + community-physical-health hereditament footprint covering rural Cornwall and the Isles of Scilly. The combined MH + community-physical-health remit drives a higher hereditament count than MH-only peers.",
        "beneficiaries": "Approximately 70+ occupied hereditaments across Cornwall + Isles of Scilly; serves c. 570,000 residents with combined MH + community-physical-health + LD + CAMHS services; sparse rural geography generates dispersed small-clinic estate.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.35M"},
            {"label": "Hereditament count", "value": "c. 70+ occupied sites — acute MH (Longreach), community hospitals, community clinics, CAMHS"},
            {"label": "Major sites driving line", "value": "Longreach (Bodmin Hospital) + Garden House (St Lawrence's) + community hospitals (Camborne-Redruth, Stratton, etc.)"},
            {"label": "Geographic spread", "value": "Cornwall unitary authority + Isles of Scilly council — dual billing-authority footprint with sparse rural distribution"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs not registered charities"},
            {"label": "VOA 2023 revaluation", "value": "Cornwall commercial RVs broadly stable; many small clinic hereditaments fall under small-multiplier threshold"},
            {"label": "NHSPS interaction", "value": "Significant share of community-clinic estate held via NHSPS lease — rates passed through to Cornwall Partnership as occupier"},
            {"label": "Rural sparsity premium", "value": "Many small dispersed hereditaments rather than fewer-larger sites — marginally higher per-hereditament cost"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.1M → 2024-25 £1.35M — UBR-tracking + minor estate growth"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + Cornwall Council + Council of the Isles of Scilly"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023"}
        ],
        "notes": "Cornwall Partnership's business-rates line reflects the structural reality of NHS provision in a sparse rural geography — many small dispersed community-clinic hereditaments rather than fewer larger sites, multiplying the administrative complexity of rates demand notices even where individual liabilities sit below the small-multiplier threshold. The combined MH + community-physical-health remit (the trust runs community hospitals at Camborne-Redruth, Stratton and elsewhere alongside MH services) widens the hereditament footprint significantly. NHSPS-leased premises pass rates through to the trust as occupier. The 2026 VOA revaluation under NDRA 2023's 3-year cycle is expected to leave Cornwall RVs broadly stable. The Isles of Scilly forms a separate billing-authority interaction.",
        "sources": [
            {"publisher": "Cornwall Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cornwallft.nhs.uk/about/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Cornwall Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Devon Partnership NHS Trust", "NHS Property Services Ltd"]
    },
    "Amortisation — Leicestershire Partnership NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Leicestershire Partnership NHS Trust"}],
        "description": "LPT's £1.33M amortisation line is the IAS 38 charge on capitalised intangibles — predominantly clinical-system software (RiO and SystmOne for the trust's combined MH + community + LD remit), the Frontline Digitisation EPR investment, and capitalised licences across Bradgate Mental Health Unit, Evington Centre, Agnes Unit and Bennion Centre operations. The trust's combined-remit clinical IT estate spans MH crisis records, community-nursing caseloads, CAMHS and learning-disability outreach.",
        "beneficiaries": "c. 5,500 substantive WTE clinical and admin users across Leicester, Leicestershire and Rutland on capitalised software; combined MH + community-physical-health + LD + CAMHS clinical-system stack underpins service delivery for c. 1.1M residents.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation programme (NHSE 2022-2025)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.33M"},
            {"label": "Composition", "value": "Capitalised software (RiO MH + SystmOne community) + capitalised licences + integration software"},
            {"label": "Frontline Digitisation context", "value": "Trust included in NHSE Frontline Digitisation EPR rollout — capitalisation of EPR-related development + configuration"},
            {"label": "Combined remit driver", "value": "MH + community-physical-health + LD + CAMHS → broader software stack than MH-only peers"},
            {"label": "Useful life convention", "value": "Software typically 3-7 years per DHSC GAM 2024-25 ch.5; longer-life major systems 7-10 years"},
            {"label": "Capitalisation threshold", "value": "DHSC GAM £5,000 individual or £250,000 grouped for software"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.7M → 2024-25 £1.33M — rising as Frontline Digitisation tranches come into amortisation"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams; vendor stack includes RiO (Servelec/Access) + TPP SystmOne for community"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate (Frontline Digitisation) + Leicester, Leicestershire and Rutland ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme tracker; LPT digital maturity assessment"},
            {"label": "CQC context", "value": "CQC Section 31 conditions 2022-23 on community-MH waits — drove dashboard + reporting software investment"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate-trust software stacks (Leicestershire MH + community split) · Successor: LLR ICS shared EPR procurement"}
        ],
        "notes": "LPT's amortisation profile is shaped by both the Frontline Digitisation capital injection and the structural complexity of running combined MH + community + LD + CAMHS services on a dual-EPR stack (RiO for MH, SystmOne for community-nursing) — integration software and interfaces are capitalised and amortised. CQC's 2022-23 Section 31 conditions on community-MH waits drove additional investment in performance-dashboard and access-monitoring tooling. The £1.33M line will continue rising as Frontline Digitisation tranches come into amortisation, before levelling out in the late 2020s. LLR ICS digital strategy is exploring shared EPR procurement to reduce future per-trust capitalisation. Useful-life judgement remains the key reporting risk.",
        "sources": [
            {"publisher": "Leicestershire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicspart.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme — EPR rollout", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "Care Quality Commission", "title": "Leicestershire Partnership NHS Trust provider profile", "url": "https://www.cqc.org.uk/provider/RT5"}
        ],
        "related": ["Leicestershire Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Frontline Digitisation programme", "Amortisation — Black Country Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Sussex Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Sussex Partnership NHS Foundation Trust"}],
        "description": "Sussex Partnership's £1.33M 2024-25 business-rates charge reflects VOA-set rateable values × 49.9p / 54.6p UBR multipliers across Mill View Hospital (Hove), Langley Green Hospital (Crawley), Meadowfield Hospital (Worthing), the Department of Psychiatry (Royal Sussex County Hospital, Brighton) and a wide community-MH + CAMHS estate across East Sussex, West Sussex, Brighton & Hove and Hampshire children's services. South-coast commercial RVs and dispersed estate drive the line.",
        "beneficiaries": "Approximately 70+ occupied hereditaments across East Sussex, West Sussex, Brighton & Hove and Hampshire CAMHS catchment; serves c. 1.7M residents with MH + CAMHS + LD specialist services; key acute hubs at Hove, Crawley and Worthing.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.33M"},
            {"label": "Hereditament count", "value": "c. 70+ occupied sites — acute MH, community, CAMHS, eating-disorder specialist"},
            {"label": "Major sites driving line", "value": "Mill View (Hove) + Langley Green (Crawley) + Meadowfield (Worthing) + DoP (RSCH Brighton)"},
            {"label": "Geographic spread", "value": "East Sussex + West Sussex + Brighton & Hove unitary + parts of Hampshire (CAMHS)"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs not registered charities"},
            {"label": "South-coast RV premium", "value": "Brighton + Hove postcodes carry elevated commercial RVs vs national average; coastal-town RVs more variable"},
            {"label": "VOA 2023 revaluation impact", "value": "Sussex commercial RVs broadly stable; Brighton retail downward rebase post-pandemic"},
            {"label": "NHSPS interaction", "value": "Significant share of community-clinic estate held via NHSPS lease — rates passed through to Sussex Partnership"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.1M → 2024-25 £1.33M — UBR-tracking + minor estate growth"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + multiple billing authorities (Brighton & Hove UA, Lewes, Eastbourne, Hastings, Crawley, Horsham, Worthing, Adur, Mid Sussex, Arun, Chichester, etc.)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023 3-year cycle"}
        ],
        "notes": "Sussex Partnership's business-rates line is shaped by the dispersed south-coast estate spanning two counties plus Brighton & Hove unitary, with c. 12 separate billing authorities each issuing demand notices. Brighton + Hove postcodes carry elevated commercial RVs, partially offset by post-pandemic retail rebasing. The trust's specialist eating-disorder, CAMHS and forensic services occupy ringfenced space across Mill View, Langley Green and Meadowfield. NHSPS-leased community clinics pass rates through as occupier — a sector-wide friction. The 2026 VOA revaluation under NDRA 2023's 3-year cycle is expected to leave Sussex commercial RVs broadly stable. Sussex ICS estate consolidation is the medium-term lever to reduce hereditament count.",
        "sources": [
            {"publisher": "Sussex Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sussexpartnership.nhs.uk/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Sussex Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Oxford Health NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    # __ENTRY_17__
}
