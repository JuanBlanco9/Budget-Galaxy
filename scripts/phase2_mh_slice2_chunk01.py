# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 01 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Establishment costs — Bradford District Care NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Bradford District Care NHS Foundation Trust"}],
        "description": "Establishment costs at Bradford District Care covers stationery, postage, telephones, mobile devices, printing, courier and the residual office-running cost across the trust's mental-health, community and CAMHS services. The £3.23M 2024-25 line is large because Bradford operates a high site-count community + MH model — Lynfield Mount Hospital, Airedale Centre for Mental Health (Steeton), and dozens of community clinics — each requiring local establishment infrastructure beyond the consolidated HQ.",
        "beneficiaries": "c. 3,500 staff working across Lynfield Mount Hospital (acute MH), Airedale CMH, plus c. 60+ community sites covering health visiting, school nursing, CAMHS, IAPT (now NHS Talking Therapies) and adult community services for c. 700,000 residents of Bradford, Airedale, Wharfedale and Craven.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (consumables procurement)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.23M"},
            {"label": "Site footprint driving line", "value": "Lynfield Mount Hospital + Airedale CMH + c. 60 community sites across Bradford district + Craven"},
            {"label": "Headcount served", "value": "c. 3,500 substantive WTE staff"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephones + mobile-device estate + photocopying"},
            {"label": "Mobile-device estate", "value": "Sustained increase from c. 2020 community-mobile-working programme — laptops, smartphones, MiFi for district-nursing"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (stationery + IT consumables) + local contracts for postage and courier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.4M → 2024-25 £3.23M — sustained growth tracking community-mobile-working rollout and CPI"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT Estates teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE provider-finance + West Yorkshire ICB · DHSC GAM disclosure rules"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; NHSE Model Hospital benchmarking shows MH community trusts running 1.5-2.0% of turnover on establishment"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paper-heavy office model · Successor: digital-first community workflow under Frontline Digitisation EPR (Rio replacement)"}
        ],
        "notes": "Bradford District Care's establishment line sits high relative to peers because of the sheer geographic spread and site count required by the trust's community-led service model — health visiting, school nursing and district nursing across rural Craven and Wharfedale generate higher per-staff postage, courier and mobile-device cost than urban-concentrated MH trusts. The line has grown faster than CPI since 2020 as community-mobile-working expanded post-COVID, with each district nurse now equipped with laptop + smartphone. The Frontline Digitisation EPR rollout (Rio replacement, programmed 2025-27) is expected to reduce printing and postage but raise mobile-device and licensing recurring cost, leaving net establishment expenditure broadly flat in real terms.",
        "sources": [
            {"publisher": "Bradford District Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bdct.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Model Hospital — community + mental health benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "Office consumables and stationery framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Bradford District Care NHS FT provider profile (RT5)", "url": "https://www.cqc.org.uk/provider/RT5"}
        ],
        "related": ["Bradford District Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Berkshire Healthcare NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Business rates — Central and North West London NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Central and North West London NHS Foundation Trust"}],
        "description": "CNWL's £3.32M 2024-25 business-rates charge reflects an unusually large dispersed estate of 150+ sites across central + NW London, Milton Keynes and Hillingdon — including St Charles (Ladbroke Grove), Park Royal Centre, the Gordon Hospital legacy and dozens of CAMHS + community clinics. VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) drive the line; NHS FTs do not get charitable exemption. London RV concentration inflates the per-turnover charge.",
        "beneficiaries": "Approximately 150+ occupied hereditaments (acute mental-health wards, community clinics, CAMHS sites, addictions and offender-health bases) across 8 London boroughs plus Milton Keynes; serves a registered catchment population of c. 2.0M plus national specialist services (Eating Disorders, Gender Identity Clinic).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.32M (largest MH-trust business-rates line in slice 2)"},
            {"label": "Hereditament count", "value": "c. 150+ occupied sites across CNWL footprint (acute, community, CAMHS, addictions, GIC)"},
            {"label": "Geographic spread", "value": "Westminster, Kensington & Chelsea, Brent, Harrow, Hillingdon, Camden, Milton Keynes, plus national specialist sites"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "London RV premium", "value": "Westminster + RBKC postcodes carry 2-3× national-average rateable value per m²"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "VOA 2023 revaluation impact", "value": "London commercial RVs rebased downward post-pandemic; partial mitigation of CNWL liability"},
            {"label": "NHSPS interaction", "value": "Significant share of community clinic estate held via NHS Property Services lease; rates passed through to trust as occupier"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Valuation Office Agency (rateable value) + 8 billing authorities (Westminster CC, RBKC, Brent, Harrow, Hillingdon, Camden, Milton Keynes)"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Funding trajectory", "value": "Sustained upward 2020-21 c. £2.6M → 2024-25 £3.32M; tracks frozen UBR + new-site additions (Gordon Hospital handback offset by community expansion)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "CNWL carries the largest MH-trust business-rates bill in this slice because of its London-heavy estate and the sheer count of hereditaments — more occupied addresses than most acute trusts despite being a community/MH provider. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but London commercial RVs remain elevated and the 2026 revaluation (3-year cycle under NDRA 2023) is expected to rebase upward. The 2023 Gordon Hospital closure reduced one ward hereditament but community + CAMHS expansion added smaller sites. NHSPS-leased community clinics pass rates through to CNWL, complicating the NHSPS service-charge recharge boundary.",
        "sources": [
            {"publisher": "Central and North West London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cnwl.nhs.uk/about/who-we-are/board-papers-and-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Central and North West London NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Mersey Care NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "Transport (business + patient) — Greater Manchester Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Greater Manchester Mental Health NHS Foundation Trust"}],
        "description": "GMMH's £3.23M transport line covers staff business mileage (community visits, AMHP rotas, crisis-team home assessments) and inter-site patient transfers between Prestwich Hospital, the Edenfield Centre (high/medium-secure), Park House (North Manchester General), Laureate House (Wythenshawe) and Trafford community sites, plus contracted PTS for s.136 conveyance and MHA-detained transfers. The Edenfield Panorama exposé (Sep 2022) and subsequent CQC enforcement expanded chaperoned-transfer requirements + external-assessment travel.",
        "beneficiaries": "c. 6,500 staff making community visits across Manchester, Salford, Trafford and Bolton; c. 1,300 inpatient bed-stock generating regular inter-site transfers; serves a registered population c. 1.4M; secure-services catchment extends across NW England.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance + transfer) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments (AMAP)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.23M"},
            {"label": "Site footprint generating transfers", "value": "Prestwich Hospital + Edenfield Centre + Park House + Laureate House + Trafford community"},
            {"label": "Bed-stock generating inter-site transfers", "value": "c. 1,300 inpatient beds across acute MH, PICU, low/medium/high-secure"},
            {"label": "Edenfield Panorama uplift", "value": "Sep 2022 BBC Panorama exposé → CQC enforcement → expanded external-assessment travel + chaperoned-transfer requirements"},
            {"label": "MHA conveyance share", "value": "s.136 + s.135 detained-patient conveyance contracted via NWAS + private secure-transport providers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles, 25p thereafter"},
            {"label": "Pool car + lease-vehicle fleet", "value": "Salary-sacrifice + Crown Commercial Service vehicle framework — gradual EV transition under GM Clean Air Zone"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.2M → 2024-25 £3.23M — uplift driven by post-pandemic community visit recovery + Edenfield remediation + fuel-cost CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel & Transport team; contracted patient-transfer services with NWAS + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + GM ICB · MHA conveyance policy under DHSC + Home Office"},
            {"label": "Evaluation evidence", "value": "CQC special-measures exit 2024 included transport + chaperoning standards; Edenfield independent review 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Edenfield 2022 transfer regime · Successor: GM ICS shared-transport pooling under review + EV transition"}
        ],
        "notes": "GMMH's transport line is structurally elevated by the Edenfield Centre — the high/medium-secure women's service whose 2022 Panorama exposé led to CQC enforcement, ward closures and a sustained programme of external-clinical-review visits, multi-agency safeguarding reviews and independently-chaperoned patient transfers. Each high-secure transfer requires accredited secure-transport, escorted by trained staff; per-journey costs run multiples of standard PTS. Beyond Edenfield, the trust's geographic spread across four boroughs and its regional secure-services catchment generate routine inter-site transfers and AMHP rota mileage. The GM Clean Air Zone and ICS shared-transport pooling are the medium-term levers; the EV transition will raise capital cost upfront before yielding mileage savings.",
        "sources": [
            {"publisher": "Greater Manchester Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gmmh.nhs.uk/annual-report"},
            {"publisher": "Care Quality Commission", "title": "GMMH Edenfield Centre inspection reports + enforcement", "url": "https://www.cqc.org.uk/provider/RXV"},
            {"publisher": "BBC Panorama", "title": "Undercover Hospital Abuse Scandal (Edenfield Centre)", "url": "https://www.bbc.co.uk/news/uk-england-manchester-63076418"},
            {"publisher": "NHS England", "title": "Patient transport services and MHA conveyance policy", "url": "https://www.england.nhs.uk/urgent-emergency-care/nhs-111/integrated-urgent-care/patient-transport/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Greater Manchester Mental Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Norfolk and Suffolk NHS Foundation Trust", "Mental Health Act 1983"]
    },
    "Lease expenditure — Mersey Care NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Mersey Care NHS Foundation Trust"}],
        "description": "Mersey Care's £3.19M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services and CHP LIFT-vehicle leases for community-MH clinics across Liverpool, Sefton, Knowsley, St Helens, Halton and Warrington, plus Ashworth Hospital ancillary leased space and Life Rooms recovery-college sites. The Rowan View medium-secure unit (Maghull, 2023) added a step-up in NHSPS-leased footprint.",
        "beneficiaries": "c. 9,000 staff and a registered catchment c. 1.5M across Liverpool City Region; high-secure men's service at Ashworth Hospital is a national specialist resource serving c. 200 patients; community-MH and physical-health community sites c. 80+ leased premises.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£3.19M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with corresponding depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 80+ NHSPS + CHP-LIFT premises plus Life Rooms recovery-college sites + ancillary Ashworth space"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Rowan View 2023 step-up", "value": "Medium-secure unit at Maghull (146 beds) opened 2023 — added NHSPS-leased ancillary footprint"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £1.6M operating lease → 2022-23 c. £2.7M ROU first year → 2024-25 £3.19M (Rowan View + uplifts)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cheshire & Merseyside ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + ICS estate consolidation"}
        ],
        "notes": "Mersey Care's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet, and has continued to grow as the Rowan View medium-secure unit added leased ancillary space and as NHSPS pursued market-rent uplifts on community clinics. The NHSPS / mental-health-trust dispute over service-charge methodology and market-rent rebasing is a sector-wide friction point — Mersey Care's geographically-dispersed community footprint exposes it more than acute-only peers. Ashworth Hospital itself is owned, but training, support and visitor-services functions sit in leased ancillary space. The Life Rooms recovery-college model also operates from leased non-clinical sites, including library and community-hub partnerships.",
        "sources": [
            {"publisher": "Mersey Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.merseycare.nhs.uk/about-us/our-publications/annual-report-and-accounts"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "HM Treasury", "title": "Public Expenditure System (PES) discount rates", "url": "https://www.gov.uk/government/publications/public-spending-statistics-release-schedule"}
        ],
        "related": ["Mersey Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Oxford Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Norfolk and Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Norfolk and Suffolk NHS Foundation Trust"}],
        "description": "NSFT's £3.16M transport line is structurally elevated by the rural geography of Norfolk and Suffolk — long community-team mileage between Norwich (Hellesdon Hospital), Great Yarmouth (Northgate), King's Lynn (Chatterton House), Ipswich (Woodlands) and rural CMHT bases — combined with a sustained inquest and remediation cycle following the unexpected-deaths governance crisis (Niche reports 2014-2023) that drove additional inter-site assessments and crisis-team home visits. CQC special-measures (in and out repeatedly since 2015) have required external clinical-review travel.",
        "beneficiaries": "c. 3,800 staff covering a registered population c. 1.7M across Norfolk and Suffolk; 4 acute MH inpatient sites + c. 50 community bases; rural footprint c. 5,500 km² gives England's sparsest MH-trust catchment density.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.16M"},
            {"label": "Catchment area", "value": "c. 5,500 km² across Norfolk + Suffolk — among England's sparsest MH-trust footprints"},
            {"label": "Site footprint", "value": "Hellesdon (Norwich) + Northgate (Yarmouth) + Chatterton House (King's Lynn) + Woodlands (Ipswich) + c. 50 community bases"},
            {"label": "Niche reports remediation", "value": "Niche unexpected-deaths reviews 2014-2023 drove sustained crisis-team home-visit + inquest-related travel"},
            {"label": "CQC special-measures cycle", "value": "Repeatedly in / out of special measures 2015-2023 — external review visits added to transport line"},
            {"label": "MHA conveyance share", "value": "s.136 + s.135 detained-patient conveyance contracted via EEAST + private secure-transport providers"},
            {"label": "Rural mileage premium", "value": "Per-WTE community mileage 2-3× urban-trust peers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.4M → 2024-25 £3.16M — uplift driven by post-pandemic in-person assessment recovery + fuel CPI + remediation travel"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with East of England Ambulance Service Trust + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Norfolk and Waveney ICB + Suffolk and North East Essex ICB · MHA conveyance under DHSC + Home Office"},
            {"label": "Evaluation evidence", "value": "Niche reports series; CQC inspection reports 2015-2024; HSSIB MH safety review 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 unitary acute-MH transport baseline · Successor: ICS shared-fleet pooling under Norfolk & Waveney ICB"}
        ],
        "notes": "NSFT's transport line is inseparable from its governance history: the trust's repeated cycles in and out of CQC special measures (2015, 2017, 2018, 2023) and the Niche unexpected-deaths review series have generated sustained external-review travel, inquest-attendance mileage and additional crisis-team home visits as community caseloads were rebuilt. Layered on top is the structural rural-geography premium — Norfolk and Suffolk together cover c. 5,500 km² with one of England's sparsest MH-trust population densities, meaning per-WTE community mileage runs 2-3× urban peers. EEAST contracts handle most s.136 conveyance, but secure-transfer requirements between Hellesdon, Northgate and Woodlands generate recurring inter-site movements. ICS shared-fleet pooling is the medium-term lever.",
        "sources": [
            {"publisher": "Norfolk and Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nsft.nhs.uk/publications/"},
            {"publisher": "Care Quality Commission", "title": "NSFT inspection reports + special-measures history (RMY)", "url": "https://www.cqc.org.uk/provider/RMY"},
            {"publisher": "NHS England", "title": "Niche unexpected-deaths reviews — NSFT series", "url": "https://www.england.nhs.uk/east-of-england/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Mental health investigations 2023-24", "url": "https://www.hssib.org.uk/"}
        ],
        "related": ["Norfolk and Suffolk NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Greater Manchester Mental Health NHS Foundation Trust", "Mental Health Act 1983"]
    },
    "Transport (business + patient) — Leicestershire Partnership NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Leicestershire Partnership NHS Trust"}],
        "description": "LPT's £3.12M transport line covers business mileage for community-MH, LD, district-nursing and CAMHS teams across Leicester, Leicestershire and Rutland, plus inter-site transfers between Bradgate Mental Health Unit (Glenfield), the Evington Centre, the Agnes Unit and Bennion Centre. The combined MH + community + LD remit creates a high district-nursing mileage component on top of standard MH crisis-team travel; CQC enforcement on community-MH waits since 2022 added external-assessment travel.",
        "beneficiaries": "c. 5,500 staff serving c. 1.1M residents across Leicester city, Leicestershire and Rutland; c. 250 inpatient MH + LD beds; combined MH + community-physical-health remit gives a higher staff-mileage base than MH-only peers.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.12M"},
            {"label": "Catchment area", "value": "Leicester, Leicestershire and Rutland — c. 1.1M residents"},
            {"label": "Site footprint", "value": "Bradgate MHU (Glenfield) + Evington Centre + Agnes Unit + Bennion Centre + community bases"},
            {"label": "Combined remit driver", "value": "MH + community physical-health + LD trust → higher district-nursing mileage on top of MH crisis-team travel"},
            {"label": "CQC enforcement context", "value": "2022-23 inspection identified community-MH access risks → CQC Section 31 conditions → external review travel"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance contracted via EMAS + private secure-transport for MHA-detained transfers"},
            {"label": "Staff mileage rate + fleet", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles; mix of pool cars (CCS framework), lease vehicles + staff-private; partial EV transition under Leicester Clean Air Zone planning"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.5M → 2024-25 £3.12M — uplift driven by post-pandemic visit recovery + fuel CPI + community-MH remediation"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with EMAS + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Leicester, Leicestershire and Rutland ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports 2022-2024 (RT5); LLR ICS estate + travel review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate-trust LD/community split · Successor: LLR ICS shared-fleet + EV transition"}
        ],
        "notes": "LPT's transport line is structurally elevated by the integrated MH + community + LD remit — the same trust runs district-nursing across Leicestershire and Rutland alongside MH crisis teams and learning-disability community services, generating a much larger mileage base than MH-only providers of similar size. CQC's 2022-23 finding of community-MH access risks led to Section 31 conditions and a remediation programme that increased external-clinical-review travel and crisis-home-visit volumes. EMAS handles most s.136 conveyance under the LLR all-age PTS contract. The LLR ICS is exploring shared-fleet pooling and EV transition under Leicester's Clean Air Zone proposals — partial EV adoption is the medium-term lever to flatten fuel-cost growth.",
        "sources": [
            {"publisher": "Leicestershire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicspart.nhs.uk/about/publications/"},
            {"publisher": "Care Quality Commission", "title": "Leicestershire Partnership NHS Trust provider profile (RT5)", "url": "https://www.cqc.org.uk/provider/RT5"},
            {"publisher": "Leicester, Leicestershire and Rutland ICB", "title": "ICS estate and travel review 2024", "url": "https://leicesterleicestershireandrutland.icb.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "East Midlands Ambulance Service NHS Trust", "title": "PTS contract data", "url": "https://www.emas.nhs.uk/"}
        ],
        "related": ["Leicestershire Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Coventry and Warwickshire Partnership NHS Trust", "Mental Health Act 1983"]
    },
    "Establishment costs — Berkshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Berkshire Healthcare NHS Foundation Trust"}],
        "description": "Berkshire Healthcare's £3.07M establishment line covers stationery, postage, telephony, mobile devices, printing and courier across Prospect Park Hospital (Reading), Wokingham Community Hospital, Bracknell Healthspace, Upton Hospital (Slough), West Berkshire Community Hospital and dozens of community-MH + physical-health bases. The combined MH + community remit across all 6 Berkshire unitary authorities generates a high site count; CQC 'Outstanding' rating reflects mobile-working investment that drives device + connectivity cost.",
        "beneficiaries": "c. 4,500 staff supporting c. 900,000 residents across Reading, Slough, Bracknell Forest, Windsor and Maidenhead, West Berkshire and Wokingham; combined MH + community + CAMHS service across 100+ sites including hospitals, community hospitals, GP-co-located teams and CAMHS clinics.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.07M"},
            {"label": "Site footprint", "value": "Prospect Park Hospital + Wokingham CH + Bracknell Healthspace + Upton + West Berks CH + 100+ community bases"},
            {"label": "Headcount served", "value": "c. 4,500 substantive WTE"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying + minor office consumables"},
            {"label": "CQC Outstanding context", "value": "Trust rated 'Outstanding' overall by CQC since 2019 — sustained investment in mobile-working tools"},
            {"label": "Mobile-device estate", "value": "Substantial laptop + smartphone + MiFi rollout for community staff; supports remote working post-2020"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + Crown Commercial Service telephony framework"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.3M → 2024-25 £3.07M — sustained growth tracking community-mobile-working + CPI"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Buckinghamshire, Oxfordshire and Berkshire West ICB / Frimley ICB"},
            {"label": "Evaluation evidence", "value": "CQC 'Outstanding' rating sustained 2019-2024; NHSE Model Hospital benchmarking shows sector-typical establishment ratio"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 paper-heavy clinical workflow · Successor: Frontline Digitisation EPR rollout (Rio replacement) reducing print + postage but raising licensing"}
        ],
        "notes": "Berkshire Healthcare carries one of the highest establishment lines among MH community trusts of its size, reflecting both the geographic spread across all 6 Berkshire unitary authorities and the deliberate investment in mobile-working infrastructure that underpins its CQC 'Outstanding' rating. The trust's combined MH + community + CAMHS + LD remit means establishment cost has to support district-nursing visits, school-nursing rounds, CAMHS home assessments and adult-MH crisis teams — all device-and-connectivity-intensive. The Frontline Digitisation EPR rollout (Rio system replacement, programmed mid-2020s) is expected to compress printing and postage but raise licensing and connectivity, leaving net establishment broadly flat in real terms.",
        "sources": [
            {"publisher": "Berkshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.berkshirehealthcare.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Berkshire Healthcare NHS FT provider profile (RWX)", "url": "https://www.cqc.org.uk/provider/RWX"},
            {"publisher": "NHS England", "title": "Model Hospital — community + MH benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "Office consumables and stationery framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Berkshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Bradford District Care NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Establishment costs — Tavistock and Portman NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Tavistock and Portman NHS Foundation Trust"}],
        "description": "Tavistock and Portman is England's specialist national psychotherapy + training trust at the Tavistock Centre (Belsize Lane) and Portman Clinic, with an education-heavy model — postgraduate training in psychoanalytic, child + adolescent, and forensic psychotherapy. Its £3.05M establishment line is large relative to turnover because of academic publishing, library, course-materials and faculty-office estate on top of clinical overhead. The April 2024 closure of GIDS reshaped the cost base.",
        "beneficiaries": "c. 800 staff plus c. 600 trainees on accredited postgraduate clinical-training programmes; serves a national specialist clinical caseload (psychotherapy, forensic psychotherapy, child + adolescent therapy) plus academic publication and external-training income across NHS and global partnerships.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Higher Education and Research Act 2017 (training accreditation context) · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.05M (high relative to small £100M-band turnover)"},
            {"label": "Site footprint", "value": "Tavistock Centre (Belsize Lane, Hampstead) + Portman Clinic + training-faculty office and library space"},
            {"label": "Headcount + trainee count served", "value": "c. 800 staff + c. 600 postgraduate trainees on accredited programmes"},
            {"label": "Composition (specialist mix)", "value": "Stationery + printing + postage + library + academic publishing materials + lecture-room consumables + telephony + mobile-device estate"},
            {"label": "Training-trust premium", "value": "Library + publishing + course-materials drive line above pure-clinical-trust peer ratio"},
            {"label": "GIDS closure Apr 2024 impact", "value": "GIDS closure reshaped cost base; new regional NHSE-commissioned services (north + south hubs at GOSH + Maudsley) replace the central pathway"},
            {"label": "Tavistock Press + publications", "value": "Academic press operates Karnac/Routledge co-imprint; printing and distribution tracked in establishment line"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.4M → 2024-25 £3.05M; reshape post-GIDS closure expected to flatten the line"},
            {"label": "Delivery body", "value": "Trust Finance + Library Services + Academic Publishing team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Specialised Commissioning + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "Cass Review 2024 (post-publication context for GIDS closure); CQC inspection 2023; NHSE specialised-commissioning review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2024 GIDS central-service model · Successor: new regional gender services at GOSH (north hub) + Maudsley (south hub) commissioned 2024 onwards"}
        ],
        "notes": "Tavistock and Portman's establishment line carries an unusually large education + publishing component because the trust is England's primary specialist provider of accredited postgraduate training in psychoanalytic and forensic psychotherapy — library, course-materials and faculty-office costs sit alongside clinical overhead. The Apr 2024 closure of GIDS, following the Cass Review, reshaped the cost base: GIDS-attributed overhead transfers to GOSH (north hub) and Maudsley (south hub) under NHSE specialised commissioning. Tavistock Press publications continue at scale. The small turnover base means this line is high as a percentage but modest in absolute terms — characteristic of a specialist-training NHS organisation.",
        "sources": [
            {"publisher": "Tavistock and Portman NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://tavistockandportman.nhs.uk/about-us/governance/annual-reports/"},
            {"publisher": "NHS England", "title": "The Cass Review: independent review of gender identity services for children and young people (Final report)", "url": "https://cass.independent-review.uk/"},
            {"publisher": "Care Quality Commission", "title": "Tavistock and Portman NHS FT provider profile (RNK)", "url": "https://www.cqc.org.uk/provider/RNK"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised commissioning of children + young people gender services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["Tavistock and Portman NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Bradford District Care NHS Foundation Trust", "NHS England Specialised Commissioning"]
    },
    "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Cornwall Partnership NHS Foundation Trust"}],
        "description": "Cornwall Partnership's £3.02M PFI / LIFT charge reflects the trust's occupation of LIFT-procured community-MH and community-physical-health bases across Cornwall and the Isles of Scilly, including Bodmin Hospital ancillary blocks, St Austell, Camborne-Redruth and Penzance community sites built under the Cornwall LIFT vehicle (Community Health Partnerships shareholding + private partners). The line covers the PFI-equivalent unitary charge passed through to the trust as occupier — debt service, FM lifecycle and soft-FM components — for these LIFT premises.",
        "beneficiaries": "c. 4,000 staff serving c. 570,000 residents of Cornwall + Isles of Scilly across MH inpatient, community-MH, CAMHS, learning-disability and community physical-health services; LIFT-procured community estate hosts a substantial share of the trust's outpatient and team-base footprint.",
        "legal_basis": "IFRS 16 Leases (post-2022 transition for finance-lease + service-concession arrangements) · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£3.02M"},
            {"label": "Procurement vehicle", "value": "Cornwall LIFT — Community Health Partnerships shareholding + private investor + Cornwall Council partnership"},
            {"label": "Estate covered", "value": "Bodmin Hospital ancillary blocks + St Austell + Camborne-Redruth + Penzance + smaller community-MH sites"},
            {"label": "Unitary charge composition", "value": "Debt-service component + lifecycle (hard-FM building maintenance) + soft-FM (cleaning, security, catering where contracted)"},
            {"label": "Contract duration profile", "value": "LIFT contracts typically 25-year initial with 5-year extension option; Cornwall LIFT signed mid-2000s — c. 10-15 years remaining"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession assets recognised on-balance-sheet under IFRIC 12; lease-component re-evaluated under IFRS 16 ch.7 GAM"},
            {"label": "Lifecycle indexation", "value": "Annual RPI / CPI indexation per LIFT contract terms — material driver of year-on-year line movement"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.7M → 2024-25 £3.02M — sustained CPI-linked uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Community Health Partnerships + private LIFT investor consortium"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cornwall and Isles of Scilly ICB; LIFT policy oversight at DHSC"},
            {"label": "Evaluation evidence", "value": "NAO LIFT review 2017-18; trust ARA disclosure 2023-24; ICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT mid-2000s NHS-Estates community-clinic model · Successor: end-of-LIFT-contract review + ICS estate consolidation late 2030s"}
        ],
        "notes": "Cornwall Partnership's PFI / LIFT line is dominated by the Cornwall LIFT vehicle, which procured a tranche of community-health bases in the mid-2000s under the Local Improvement Finance Trust model — a service-concession structure where Community Health Partnerships (DHSC majority shareholder) co-invests with private partners and the trust occupies as tenant under a long unitary-charge contract. CPI / RPI indexation each year is the main driver of cost growth, layered on the fixed debt-service and lifecycle components. As contracts approach their 25-year endpoint in the late 2030s, the trust and Cornwall and Isles of Scilly ICB face a strategic choice on hand-back, extension or estate consolidation — a sector-wide LIFT cliff-edge mirroring the better-known PFI hand-back challenge.",
        "sources": [
            {"publisher": "Cornwall Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cornwallft.nhs.uk/about-us/publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Cornwall Partnership NHS FT provider profile (RJ8)", "url": "https://www.cqc.org.uk/provider/RJ8"}
        ],
        "related": ["Cornwall Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Coventry and Warwickshire Partnership NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Coventry and Warwickshire Partnership NHS Trust"}],
        "description": "CWPT's £2.99M transport line covers business mileage for community-MH, CAMHS, LD and physical-health community teams across Coventry, Warwickshire, Solihull and parts of Worcestershire, plus inter-site patient transfers between the Caludon Centre (Coventry, c. 130 acute MH beds), Brooklands (Marston Green, LD inpatient), St Michael's Hospital (Warwick) and St Laurence's House (Rugby). The trust's combined MH + community + LD remit and its hosting of secure-LD services for the West Midlands generates substantial inter-site secure-transfer activity layered on standard community travel.",
        "beneficiaries": "c. 5,200 staff serving c. 1.05M residents of Coventry, Warwickshire and Solihull plus regional secure-LD catchment; combined MH + community + LD trust with secure-LD inpatient hosting at Brooklands.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.99M"},
            {"label": "Catchment area", "value": "Coventry, Warwickshire, Solihull + regional secure-LD catchment c. 1.05M+"},
            {"label": "Site footprint", "value": "Caludon Centre (Coventry) + Brooklands (Marston Green, LD) + St Michael's (Warwick) + St Laurence's (Rugby)"},
            {"label": "Secure-LD transfer driver", "value": "Brooklands Hospital regional secure-LD catchment generates accredited-secure inter-site transfers — multiples of standard PTS unit cost"},
            {"label": "Combined remit driver", "value": "MH + community + LD + CAMHS — district-nursing layer on top of MH crisis-team mileage"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance via WMAS contract + accredited secure-transport providers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.3M → 2024-25 £2.99M — uplift driven by post-pandemic recovery + fuel CPI + secure-LD activity"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with West Midlands Ambulance Service + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Coventry and Warwickshire ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports 2022-2024; Brooklands secure-LD service inspection 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 community-physical-health TUPE in · Successor: ICS shared-fleet pooling under West Midlands ICS"}
        ],
        "notes": "CWPT's transport line carries an unusual secure-LD inter-site-transfer premium because Brooklands Hospital at Marston Green is a regional resource for secure learning-disability inpatient care across the West Midlands — patient transfers in and out require accredited secure-transport, escorted by trained staff, at multiples of standard PTS unit cost. Layered on top is the trust's combined MH + community + LD + CAMHS remit, which generates a high district-nursing and crisis-team mileage base. WMAS handles most s.136 conveyance under the West Midlands MH all-age PTS contract. ICS shared-fleet pooling and partial EV transition are the medium-term levers; sustained post-pandemic in-person assessment recovery + fuel CPI are the dominant near-term cost drivers.",
        "sources": [
            {"publisher": "Coventry and Warwickshire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.covwarkpt.nhs.uk/publications"},
            {"publisher": "Care Quality Commission", "title": "CWPT provider profile (RYG) + Brooklands inspection", "url": "https://www.cqc.org.uk/provider/RYG"},
            {"publisher": "NHS England", "title": "Specialised commissioning of secure LD services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "West Midlands Ambulance Service University NHS Foundation Trust", "title": "PTS contract data", "url": "https://wmas.nhs.uk/"}
        ],
        "related": ["Coventry and Warwickshire Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Leicestershire Partnership NHS Trust", "Mental Health Act 1983"]
    },
    "Establishment costs — Surrey and Borders Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Surrey and Borders Partnership NHS Foundation Trust"}],
        "description": "Surrey and Borders' £2.98M establishment line covers stationery, postage, telephones, mobile devices, printing, courier and residual office-running costs across Farnham Road Hospital (Guildford), Abraham Cowley Unit (Chertsey), Ridgewood Centre (Frimley), plus 60+ community-MH, CAMHS and LD bases serving Surrey, NE Hampshire and parts of West Sussex. The trust's high site count, dispersed across affluent commuter-belt geography with extended community-team travel patterns, drives a higher establishment ratio than urban-concentrated MH trusts.",
        "beneficiaries": "c. 3,200 staff serving c. 1.3M residents of Surrey, NE Hampshire and parts of West Sussex; c. 60+ community + inpatient sites covering MH, CAMHS, LD and addictions; combined remit means district-nursing-style mobile working not relevant but high CMHT visit volumes generate device + connectivity demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.98M"},
            {"label": "Site footprint", "value": "Farnham Road (Guildford) + Abraham Cowley (Chertsey) + Ridgewood (Frimley) + 60+ community sites"},
            {"label": "Headcount served", "value": "c. 3,200 substantive WTE"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying + minor office consumables"},
            {"label": "Geographic dispersion", "value": "Surrey + NE Hampshire + W Sussex commuter-belt — high inter-site travel base"},
            {"label": "Mobile-device estate", "value": "Sustained smartphone + laptop rollout for community-MH crisis teams + CAMHS"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + CCS telephony framework"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.4M → 2024-25 £2.98M — sustained CPI + community-mobile-working uplift"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Surrey Heartlands ICB / Frimley ICB / Sussex ICB"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' rating sustained 2018-2024; NHSE Model Hospital benchmarking"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 paper-heavy clinical workflow · Successor: SystmOne / Rio EPR rollout under Frontline Digitisation reducing print + postage"}
        ],
        "notes": "Surrey and Borders' establishment line reflects the trust's wide commuter-belt footprint — Surrey, NE Hampshire and parts of West Sussex span three ICB jurisdictions and require a high site count for local CMHT and CAMHS access. The mobile-device estate has grown post-2020 as crisis-team and CMHT staff increasingly work remotely with patient-record access on encrypted laptops + smartphones. The Frontline Digitisation EPR rollout (under regional MH digital programme) is expected to reduce printing and postage but raise licensing and connectivity, leaving net establishment broadly flat in real terms after digitisation savings net out against device-fleet growth.",
        "sources": [
            {"publisher": "Surrey and Borders Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sabp.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "Care Quality Commission", "title": "Surrey and Borders Partnership NHS FT provider profile (RXX)", "url": "https://www.cqc.org.uk/provider/RXX"},
            {"publisher": "NHS England", "title": "Model Hospital — community + MH benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "Office consumables and stationery framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Surrey and Borders Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Berkshire Healthcare NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Establishment costs — Leeds and York Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Leeds and York Partnership NHS Foundation Trust"}],
        "description": "LYPFT's £2.96M establishment line covers stationery, postage, telephony, mobile devices, printing and courier across the Becklin Centre (Leeds), Newsam Centre, Mill Lodge (LD inpatient), Bootham Park legacy and York/Selby community sites, plus a clutch of national specialist services including the Yorkshire Centre for Forensic Psychiatry and the National Inpatient Centre for Psychological Medicine. The mix of acute MH + national specialist services drives device + clinical-publication overhead.",
        "beneficiaries": "c. 3,300 staff serving Leeds (c. 815,000 residents) plus York and Selby; national specialist catchment for forensic psychiatry, deafness + MH, perinatal MH and gender services (north-region hub at GOSH partnership); c. 80+ inpatient + community sites.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.96M"},
            {"label": "Site footprint", "value": "Becklin Centre + Newsam Centre + Mill Lodge + Bootham Park (legacy) + York/Selby community + national specialist services"},
            {"label": "Headcount served", "value": "c. 3,300 substantive WTE"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying"},
            {"label": "National specialist services driver", "value": "Yorkshire Centre for Forensic Psychiatry + National Inpatient Centre for Psychological Medicine + Deaf MH services — clinical-publication and patient-information overhead"},
            {"label": "Mobile-device estate", "value": "CMHT + crisis-team + CAMHS smartphone + laptop rollout sustained post-2020"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + CCS telephony framework"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.3M → 2024-25 £2.96M — sustained CPI + community-mobile-working uplift"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + West Yorkshire ICB + NHSE Specialised Commissioning"},
            {"label": "Evaluation evidence", "value": "CQC inspection 2023; NHSE Model Hospital benchmarking; specialised-commissioning service reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 separate Leeds + York legacy structures · Successor: WY ICS digital + Frontline Digitisation EPR rollout"}
        ],
        "notes": "LYPFT's establishment line carries a national-specialist-services overhead component on top of its standard acute-MH + community footprint — the Yorkshire Centre for Forensic Psychiatry (medium-secure provision at Newton Lodge), the National Inpatient Centre for Psychological Medicine (a national tertiary service for severe medically-unexplained symptoms), and Deaf MH services each generate clinical-publication, patient-information and accessible-format printing demand beyond standard MH overhead. Combined with the dispersed Leeds + York + Selby footprint (with its long-distance community-team travel), the establishment line sits structurally above small-trust averages. Frontline Digitisation EPR rollout will compress printing but raise device-licensing recurring cost.",
        "sources": [
            {"publisher": "Leeds and York Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsandyorkpft.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "LYPFT provider profile (RGD)", "url": "https://www.cqc.org.uk/provider/RGD"},
            {"publisher": "NHS England", "title": "Specialised commissioning of forensic psychiatry + national MH services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital — community + MH benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"}
        ],
        "related": ["Leeds and York Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Bradford District Care NHS Foundation Trust", "NHS England Specialised Commissioning"]
    },
    "PFI / LIFT charges — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust"}],
        "description": "CNTW's £2.96M PFI / LIFT charge reflects unitary-charge pass-through on PFI-procured MH inpatient and community estate, principally Hopewood Park Hospital (Sunderland, opened 2014 under PFI replacing Cherry Knowle + Cleadon Park) and St George's Park (Morpeth) ancillary blocks plus LIFT-procured community sites across Northumberland, Tyne and Wear and North Cumbria. The line covers debt service, hard-FM lifecycle and soft-FM components per service-concession arrangements held on-balance-sheet under IFRIC 12.",
        "beneficiaries": "c. 7,000 staff serving c. 1.7M residents across Cumbria, Northumberland, Tyne and Wear; combined MH + LD trust hosting regional secure services + national specialist eating disorders + neurorehabilitation; c. 60+ inpatient + community sites with PFI / LIFT components.",
        "legal_basis": "IFRS 16 Leases · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.96M"},
            {"label": "Major PFI build", "value": "Hopewood Park Hospital (Sunderland) opened 2014 under PFI — replaced Cherry Knowle + Cleadon Park"},
            {"label": "PFI consortium", "value": "Sunderland MH PFI vehicle — concession runs to mid-2040s"},
            {"label": "LIFT vehicle coverage", "value": "Tyne and Wear LIFT + Northumberland LIFT — community-MH bases"},
            {"label": "Estate covered", "value": "Hopewood Park + St George's Park ancillary + LIFT community-MH sites"},
            {"label": "Unitary charge composition", "value": "Debt-service component + lifecycle (hard-FM building maintenance) + soft-FM (cleaning, security, catering)"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession assets recognised on-balance-sheet under IFRIC 12; lease-component re-evaluated under IFRS 16 ch.7 GAM"},
            {"label": "Indexation", "value": "Annual RPI / CPI uplift per concession-contract terms — major year-on-year movement driver"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.7M → 2024-25 £2.96M — sustained CPI-linked uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + PFI consortium + Community Health Partnerships (LIFT) + private LIFT investors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North East and North Cumbria ICB; PFI/LIFT policy oversight at DHSC + IPA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 Cherry Knowle + Cleadon Park acute-MH estate · Successor: PFI hand-back planning mid-2040s + LIFT contract reviews late 2030s"}
        ],
        "notes": "CNTW's PFI / LIFT line is dominated by the 2014 Hopewood Park Hospital PFI in Sunderland — a 100-bed acute-MH replacement scheme that consolidated the previous Cherry Knowle and Cleadon Park sites into a single modern build, with a unitary-charge contract running to the mid-2040s. The LIFT-procured community-MH bases in Northumberland and Tyne and Wear add a secondary layer. Annual CPI / RPI indexation drives the bulk of year-on-year movement; debt-service is fixed but lifecycle and soft-FM index. As the trust looks to the late 2030s, LIFT-contract endpoints will be a strategic decision point for North East and North Cumbria ICB; the Hopewood Park PFI runs longer to mid-2040s, mirroring sector-wide PFI hand-back challenges.",
        "sources": [
            {"publisher": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cntw.nhs.uk/about/publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and contracts", "url": "https://www.nao.org.uk/reports/managing-pfi-assets/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "CNTW NHS FT provider profile (RX4)", "url": "https://www.cqc.org.uk/provider/RX4"}
        ],
        "related": ["Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Kent and Medway NHS and Social Care Partnership Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Kent and Medway NHS and Social Care Partnership Trust"}],
        "description": "KMPT's £2.96M establishment line covers stationery, postage, telephones, mobile devices, printing, courier and residual office-running cost across the Priority House (Maidstone), St Martin's Hospital (Canterbury), Littlebrook Hospital (Dartford), Medway Maritime ancillary (Gillingham) and 50+ community-MH and CAMHS bases serving Kent and Medway. CQC's 2018 'Inadequate' rating and subsequent special-measures exit drove sustained investment in mobile-working and clinical-record infrastructure that underpins device + connectivity establishment cost.",
        "beneficiaries": "c. 3,500 staff serving c. 1.85M residents across Kent and Medway (one of England's largest county-level MH catchments); 4 acute MH inpatient sites + 50+ community bases including CAMHS, perinatal, eating disorders and addictions services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.96M"},
            {"label": "Site footprint", "value": "Priority House (Maidstone) + St Martin's (Canterbury) + Littlebrook (Dartford) + Medway Maritime ancillary + 50+ community bases"},
            {"label": "Headcount served", "value": "c. 3,500 substantive WTE"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying"},
            {"label": "CQC special-measures exit context", "value": "2018 'Inadequate' → 2021 'Requires Improvement' → sustained investment in clinical-record + mobile-working tooling"},
            {"label": "Mobile-device estate", "value": "Crisis-team + CMHT + CAMHS smartphone + laptop rollout sustained post-2020"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + CCS telephony framework"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.3M → 2024-25 £2.96M — sustained CPI + remediation-driven device investment"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection 2022; Niche-led independent reviews on patient deaths 2022-23"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paper-heavy clinical workflow under special-measures · Successor: K&M ICS digital programme + Frontline Digitisation EPR"}
        ],
        "notes": "KMPT's establishment line carries a remediation-driven uplift component: following CQC's 2018 'Inadequate' rating and subsequent special-measures, the trust invested heavily in mobile-working tools, smartphones and clinical-record-access laptops as part of governance remediation — that infrastructure now underpins ongoing establishment cost. The 1.85M-resident catchment across Kent and Medway is one of England's largest county-level MH footprints, requiring dispersed site count and per-staff device fleet. K&M ICS digital programme and Frontline Digitisation EPR rollout are expected to compress printing and postage but raise licensing and connectivity recurring cost, broadly net-flat in real terms after 2026.",
        "sources": [
            {"publisher": "Kent and Medway NHS and Social Care Partnership Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kmpt.nhs.uk/about-us/governance/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "KMPT provider profile (RXY)", "url": "https://www.cqc.org.uk/provider/RXY"},
            {"publisher": "NHS England", "title": "Niche independent reviews — KMPT", "url": "https://www.england.nhs.uk/south-east/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "Office consumables and stationery framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Kent and Medway NHS and Social Care Partnership Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Surrey and Borders Partnership NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Transport (business + patient) — Cambridgeshire and Peterborough NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Cambridgeshire and Peterborough NHS Foundation Trust"}],
        "description": "CPFT's £2.95M transport line covers business mileage for community-MH, CAMHS, LD and addictions teams across Cambridgeshire and Peterborough plus inter-site patient transfers between Fulbourn Hospital (Cambridge), the Cavell Centre (Peterborough, opened 2014 under PFI replacing Edith Cavell Hospital), Hinchingbrooke and Doddington community sites. The combined MH + community + LD remit and the rural fenland geography of the trust footprint generate a high per-WTE community mileage layered on standard MH inter-site movement.",
        "beneficiaries": "c. 4,500 staff serving c. 980,000 residents across Cambridgeshire (including rural fenland) and Peterborough; 2 acute MH inpatient sites + 50+ community bases covering CAMHS, perinatal MH, addictions and learning-disability services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.95M"},
            {"label": "Catchment area", "value": "Cambridgeshire + Peterborough — c. 980,000 residents across c. 3,400 km² including rural fenland"},
            {"label": "Site footprint", "value": "Fulbourn Hospital (Cambridge) + Cavell Centre (Peterborough) + Hinchingbrooke + Doddington community"},
            {"label": "Combined remit driver", "value": "MH + community + CAMHS + LD + addictions — high district + community visit mileage"},
            {"label": "Rural fenland premium", "value": "Per-WTE community mileage 1.5-2.0× urban-trust peers in Cambridgeshire fenland"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance via EEAST + accredited secure-transport for MHA-detained transfers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.3M → 2024-25 £2.95M — uplift driven by post-pandemic visit recovery + fuel CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with East of England Ambulance Service Trust + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cambridgeshire and Peterborough ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection 2023 (RT1); HSSIB MH safety reviews 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 Edith Cavell Hospital + dispersed Peterborough estate · Successor: ICS shared-fleet pooling under C&P ICB"}
        ],
        "notes": "CPFT's transport line is structurally elevated by the rural fenland geography of Cambridgeshire — community-MH and district-services teams cover c. 3,400 km² including some of England's most sparsely populated rural areas, generating per-WTE community mileage well above urban-trust peers. The combined MH + community + CAMHS + LD + addictions remit means a single trust covers the full spectrum of mobile-working clinical activity. EEAST handles most s.136 conveyance under the East of England MH PTS contract. The Cambridge-Peterborough-Hinchingbrooke triangle generates regular inter-site transfers; partial EV transition under the C&P ICB sustainable-travel strategy is the medium-term lever to flatten fuel-cost growth.",
        "sources": [
            {"publisher": "Cambridgeshire and Peterborough NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cpft.nhs.uk/about-us/publications-and-policies"},
            {"publisher": "Care Quality Commission", "title": "CPFT provider profile (RT1)", "url": "https://www.cqc.org.uk/provider/RT1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "East of England Ambulance Service NHS Trust", "title": "PTS contract data", "url": "https://www.eastamb.nhs.uk/"},
            {"publisher": "Cambridgeshire and Peterborough ICB", "title": "ICS estate + sustainable travel strategy", "url": "https://www.cpics.org.uk/"}
        ],
        "related": ["Cambridgeshire and Peterborough NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Norfolk and Suffolk NHS Foundation Trust", "Mental Health Act 1983"]
    },
    "Business rates — Mersey Care NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Mersey Care NHS Foundation Trust"}],
        "description": "Mersey Care's £2.85M business-rates charge reflects the trust's large dispersed estate across Liverpool City Region — including Ashworth Hospital (Maghull, high-secure men's, large rateable footprint), Rowan View medium-secure unit (opened 2023), the Mossley Hill, Broadoak and Hesketh Centre acute MH sites, plus 80+ community-MH and community-physical-health bases across Liverpool, Sefton, Knowsley, St Helens, Halton and Warrington. Liverpool's commercial RV base sits below London but above national average; the high site count drives volume more than per-site value.",
        "beneficiaries": "Approximately 100+ occupied hereditaments (high-secure + medium-secure + acute MH inpatient + community-MH + community-physical-health + addictions + LD bases) across 6 Liverpool City Region authorities; serves c. 1.5M registered population plus c. 200 high-secure men's national catchment patients at Ashworth.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.85M"},
            {"label": "Hereditament count", "value": "c. 100+ occupied sites — Ashworth + Rowan View + acute-MH + community estate"},
            {"label": "Geographic spread", "value": "Liverpool, Sefton (Maghull), Knowsley, St Helens, Halton, Warrington"},
            {"label": "Ashworth high-secure RV", "value": "Large secure-perimeter hospital site at Maghull — single-largest hereditament in trust portfolio"},
            {"label": "Rowan View 2023 add", "value": "146-bed medium-secure unit opened 2023 — added significant RV during 2023 valuation list"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption + VOA 2023 revaluation", "value": "Not applicable (NHS FTs are not charities); Liverpool commercial RVs broadly stable post-2023 revaluation, Rowan View addition drove trust-level uplift"},
            {"label": "NHSPS interaction", "value": "Substantial community estate via NHSPS lease — rates passed through to trust as occupier"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Valuation Office Agency + 6 LCR billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.3M → 2024-25 £2.85M — Rowan View addition + frozen UBR"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under 3-year cycle (NDRA 2023)"}
        ],
        "notes": "Mersey Care's business-rates bill is structurally elevated by Ashworth Hospital — a national high-secure men's facility on a large secure-perimeter site at Maghull whose rateable value is substantial relative to MH-trust norms — and was further uplifted in 2023 by Rowan View, the new 146-bed medium-secure unit which entered the local rating list mid-year. The Liverpool City Region commercial RV base sits below London but above national-average levels, and the trust's c. 100+ hereditament count means volume effects dominate over per-site value. The 2026 revaluation (3-year cycle under NDRA 2023) is expected to capture full-year Rowan View RV impact. NHSPS-leased community clinic rates pass through to Mersey Care as occupier — a recurring service-charge boundary issue.",
        "sources": [
            {"publisher": "Mersey Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.merseycare.nhs.uk/about-us/our-publications/annual-report-and-accounts"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Mersey Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Central and North West London NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "Establishment costs — Devon Partnership NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Devon Partnership NHS Trust"}],
        "description": "Devon Partnership's £2.83M establishment line covers stationery, postage, telephones, mobile devices, printing, courier and residual office-running cost across the Cedars (Exeter), Wonford House (Exeter), the Glenbourne Unit (Plymouth, partner-trust hosted historically), Langdon Hospital (Dawlish — secure services), and 40+ community-MH bases across Devon (excluding Plymouth's commissioned area where Livewell Southwest provides). Devon's rural geography across Dartmoor, Exmoor and the South Hams generates extended community-team travel that drives device + connectivity establishment cost.",
        "beneficiaries": "c. 3,000 staff serving c. 800,000 residents across Devon (excluding Plymouth area); secure-services catchment at Langdon Hospital extends across SW England; combined MH + addictions + secure-services remit with 40+ inpatient + community sites.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.83M"},
            {"label": "Site footprint", "value": "Cedars + Wonford House (Exeter) + Langdon Hospital (Dawlish, secure) + 40+ community-MH bases"},
            {"label": "Headcount served", "value": "c. 3,000 substantive WTE"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying"},
            {"label": "Rural geography driver", "value": "Devon catchment across Dartmoor, Exmoor, South Hams + East Devon — high mobile-device + connectivity demand for community staff"},
            {"label": "Mobile-device estate + secure-services overhead", "value": "Smartphone + laptop + 4G/5G hotspot rollout for rural CMHT; Langdon Dawlish secure unit + Bovey Court low-secure adds specialist patient-information + accessible-format printing"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + CCS telephony framework"},
            {"label": "Funding trajectory", "value": "2020-21 c. £2.2M → 2024-25 £2.83M — sustained CPI + community-mobile-working uplift"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Devon ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection 2023 (RWV); SW peninsula MH provider review 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paper-heavy clinical workflow · Successor: SW peninsula EPR (Frontline Digitisation) reducing print but raising licensing"}
        ],
        "notes": "Devon Partnership's establishment line is shaped by the rural geography of the trust footprint — Dartmoor, Exmoor, South Hams and East Devon community-MH staff need mobile devices, hotspots and connectivity to deliver in-home assessments at distance, and printing + postage demand remains higher than urban-trust peers because patients in rural areas often lack reliable digital access. Langdon Hospital's secure services add specialist patient-information overhead. The Frontline Digitisation EPR rollout under SW peninsula digital programme is expected to compress printing and postage from 2026 but raise licensing and connectivity, leaving net establishment broadly flat in real terms over the medium term.",
        "sources": [
            {"publisher": "Devon Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dpt.nhs.uk/about-us/our-publications"},
            {"publisher": "Care Quality Commission", "title": "Devon Partnership NHS Trust provider profile (RWV)", "url": "https://www.cqc.org.uk/provider/RWV"},
            {"publisher": "NHS England", "title": "Model Hospital — community + MH benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "Office consumables and stationery framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Devon Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Bradford District Care NHS Foundation Trust", "Frontline Digitisation programme"]
    },
}
