# -*- coding: utf-8 -*-
"""Phase2 SCamb chunk07 — 17 hand-curated entries (NHS Specialist + Community + Ambulance orphan sub-lines)."""

NEW = {
    "Establishment costs — Leeds Community Healthcare NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Leeds Community Healthcare NHS Trust"}],
        "description": "Establishment costs (printing, stationery, postage, phones, courier, office consumables) at Leeds Community Healthcare (LCH) — the city-wide community provider running district nursing, neighbourhood teams, school nursing, dental, MSK and the Leeds Sexual Health Service. With ~3,000 WTE distributed across 70+ community sites, the overhead carries pooled-mobile, lone-worker safety devices, and patient-letter postage at scale. The line totalled £3.76M in 2023-24 audited accounts and sits inside the Premises & Infrastructure parent in the orphan map.",
        "beneficiaries": "~3,000 WTE clinical and admin staff across roughly 70 community bases; downstream ~750k patient contacts/year across Leeds (pop. 822k).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses recognition) · IAS 1 Presentation of Financial Statements · NHS Act 2006 s.30 (NHS trust functions) · Health and Care Act 2022 (ICB-trust relationship)",
        "key_stats": [
            "Sub-line value 2023-24: £3,758,592 (audited ARA)",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Community (1 of 18 in scope)",
            "Trust HQ: Stockdale House, Headingley, Leeds LS6",
            "Workforce: ~3,000 WTE (2023-24)",
            "Annual contacts: ~750k community patient contacts",
            "Commissioner: NHS West Yorkshire ICB",
            "CQC overall rating: Good (last inspection 2023)",
            "Estate: ~70 sites, mostly NHSPS-leased",
            "Annual income 2023-24: ~£196M"
        ],
        "notes": "LCH is the lead provider for Leeds neighbourhood teams under the Three Shifts ‘out-of-hospital’ push, so establishment overhead has crept up with hybrid working (laptops, virtual MDTs) but stationery/postage are falling as the trust digitises GP-LCH referrals via SystmOne. The 2023-24 NIC/inflation pressure squeezed non-pay budgets while the trust absorbed a ~5% Agenda for Change uplift. Looking forward, the April 2025 employer NIC step-up to 15% (£5k threshold) will hit corporate overhead allocations indirectly. Predecessor: pre-2011 PCT-provider arm of NHS Leeds; successor direction is further pooled corporate services with Leeds Teaching Hospitals NHS Trust under the West Yorkshire ICS.",
        "sources": [
            {"publisher": "Leeds Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedscommunityhealthcare.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Consolidated NHS Provider Accounts 2023-24", "url": "https://www.england.nhs.uk/publication/consolidated-nhs-provider-accounts-2023-24/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Leeds Community Healthcare NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RY2"},
            {"publisher": "NHS West Yorkshire ICB", "title": "Joint Forward Plan 2024-29", "url": "https://www.wypartnership.co.uk/our-priorities/joint-forward-plan"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHS Three Shifts — community-out-of-hospital programme",
            "Leeds Community Healthcare NHS Trust",
            "Establishment costs — Birmingham Community Healthcare NHS Foundation Trust",
            "Establishment costs — Sussex Community NHS Foundation Trust"
        ]
    },
    "General supplies & services — West Midlands Ambulance Service University NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "West Midlands Ambulance Service University NHS Foundation Trust"}],
        "description": "Non-clinical and consumable supplies (uniforms, PPE, cleaning chemicals for Make Ready Centres, response-bag stock, vehicle prep consumables) for WMAS — the regional 999/111 provider serving 5.9M people across the West Midlands, Staffordshire, Shropshire, Hereford & Worcester and Coventry & Warwickshire. The line captures non-pharma stock not coded as Drugs costs, plus the high-volume hub-and-spoke Make Ready Centre cleaning pipeline. It totalled £3.67M in 2023-24 inside the Clinical Supplies & Drugs orphan parent.",
        "beneficiaries": "~5.9M residents across 5 sub-regions; ~1.2M emergency incidents handled annually with ~4,500 WTE operating from 15 hubs and ~90 community ambulance stations.",
        "legal_basis": "DHSC GAM 2024-25 (operating expenses) · IAS 2 Inventories (interaction with consumables held) · NHS Act 2006 · NHS Supply Chain Framework agreements",
        "key_stats": [
            "Sub-line value 2023-24: £3,666,000",
            "Parent orphan line: Clinical Supplies & Drugs",
            "Trust category: Ambulance (1 of 10)",
            "Population served: ~5.9M (West Midlands region)",
            "Incidents 2023-24: ~1.2M emergency incidents",
            "Make Ready Hubs: 15",
            "Ambulance community stations: ~90",
            "Workforce: ~6,500 staff (incl. ~4,500 frontline)",
            "Trust income 2023-24: ~£426M",
            "CQC overall rating: Requires Improvement (May 2023)"
        ],
        "notes": "WMAS pioneered the Make Ready Centre model in England — vehicles cleaned, restocked and serviced centrally so paramedics start each shift with a ready ambulance, which concentrates non-clinical supply spend in this line rather than at station level. 2023-24 saw cost pressure from PPE recovery (post-COVID stock run-down), Cat-1 8-min handover delays adding kit churn, and inflation on cleaning chemicals. Industrial action 2022-23 (GMB/Unison paramedics) drove backfill but mostly hit the Staff Costs side. The CQC Requires Improvement rating in 2023 added remedial spend on documentation/training kit. NHS Supply Chain remains the dominant counterparty.",
        "sources": [
            {"publisher": "West Midlands Ambulance Service University NHSFT", "title": "Annual Report and Accounts 2023-24", "url": "https://wmas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Ambulance quality indicators (AQI) 2023-24", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "WMAS inspection report May 2023", "url": "https://www.cqc.org.uk/provider/RYA"},
            {"publisher": "NHS Supply Chain", "title": "Framework agreements catalogue", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": [
            "Clinical Supplies & Drugs — NHS Trust sector",
            "NHS Supply Chain — DHSC ALB",
            "West Midlands Ambulance Service University NHS Foundation Trust",
            "General supplies & services — North East Ambulance Service NHS Foundation Trust",
            "General supplies & services — North West Ambulance Service NHS Trust"
        ]
    },
    "Business rates — The Royal Marsden NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Royal Marsden NHS Foundation Trust"}],
        "description": "Non-domestic rates (NDR) paid to LB Kensington & Chelsea (Chelsea hospital, Fulham Road) and LB Sutton (Sutton hospital + Oak Cancer Centre) by The Royal Marsden — England's flagship specialist cancer centre. NHS hospitals are NOT exempt from business rates (unlike charities, which get 80%); the trust pays full NDR on its rateable value across both London sites. The line totalled £3.59M in 2023-24, sitting in the Premises & Infrastructure orphan parent.",
        "beneficiaries": "Patients across the supra-regional cancer catchment (~60,000 patients/year, ~5M referral catchment via NHSE Specialised Commissioning); ~4,500 WTE staff across two London sites.",
        "legal_basis": "Local Government Finance Act 1988 Sch 6 (rateable value) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 revaluation · DHSC GAM 2024-25",
        "key_stats": [
            "Sub-line value 2023-24: £3,592,787",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Specialist (cancer)",
            "Sites: Chelsea (SW3) + Sutton (SM2) + Oak Cancer Centre (opened 2023)",
            "Patients/year: ~60,000",
            "WTE: ~4,500",
            "Annual income 2023-24: ~£625M (incl. private patient income)",
            "Commissioner: NHSE Specialised Commissioning",
            "Status: NHS Foundation Trust (since 2004)",
            "Billing authorities: LB Kensington & Chelsea, LB Sutton",
            "VOA 2023 revaluation effective: 1 Apr 2023"
        ],
        "notes": "The 2023 VOA revaluation (using 1 Apr 2021 antecedent valuation date) re-set rateable values across both Marsden sites, and the Oak Cancer Centre at Sutton — opened June 2023 — added a new high-value listing. The Non-Domestic Rating Act 2024 introduced separate multipliers and is recalibrating large-property liabilities from 2025-26, which the trust has flagged as a forward pressure. Unlike charity hospices, NHS trusts get no mandatory rate relief, so this is a pure cash-out line to the two billing authorities. Drivers ahead: Sutton site cyclotron extension; Chelsea estate optimisation; potential reform of public-sector NDR under the Treasury 2024-25 review.",
        "sources": [
            {"publisher": "The Royal Marsden NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalmarsden.nhs.uk/about-royal-marsden/corporate-information/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (Royal Marsden listings)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/15/contents"},
            {"publisher": "NHS England", "title": "Specialised Commissioning — Cancer", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHSE Specialised Commissioning",
            "The Royal Marsden NHS Foundation Trust",
            "Business rates — Alder Hey Children's NHS Foundation Trust",
            "Business rates — Great Ormond Street Hospital for Children NHS Foundation Trust"
        ]
    },
    "Establishment costs — Bridgewater Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Bridgewater Community Healthcare NHS Foundation Trust"}],
        "description": "Establishment overhead (postage, printing, telephony, stationery, courier) at Bridgewater — the NW England community provider covering Halton, Warrington, St Helens, Wigan and parts of Cheshire. With district nursing, school nursing, community dental and 0-19 health visiting delivered across ~70 community sites and clinicians' homes, the line carries patient-letter postage, lone-worker telephony and franking. It totalled £3.53M in 2023-24 within the Premises & Infrastructure orphan parent.",
        "beneficiaries": "~1.0M residents across Halton, Warrington, St Helens, Wigan and Trafford 0-19; ~2,000 WTE staff and >1.5M patient contacts/year.",
        "legal_basis": "DHSC GAM 2024-25 · IAS 1 Presentation of Financial Statements · NHS Act 2006 s.30 · Health and Care Act 2022",
        "key_stats": [
            "Sub-line value 2023-24: £3,531,000",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Community (1 of 18)",
            "HQ: Spencer House, Newton-le-Willows",
            "Population covered: ~1.0M",
            "WTE: ~2,000",
            "Patient contacts/year: ~1.5M+",
            "Sites: ~70 community bases",
            "Annual income 2023-24: ~£139M",
            "Commissioner: NHS Cheshire & Merseyside ICB / NHS Greater Manchester ICB",
            "CQC overall rating: Good (2022)"
        ],
        "notes": "Bridgewater's geographically split footprint (Cheshire & Merseyside ICS + Greater Manchester ICS) means duplicated admin overhead vs a single-ICS provider; postage and franking remain heavy because much of the cohort is paediatric/older-adult (paper-letter expectation). The trust digitised its 0-19 records onto SystmOne in 2022-23 which is gradually pulling print/postage down. Industrial-action backfill 2023-24 hit the Pay line, not Establishment. Forward pressures: April 2025 employer NIC step-up plus Three Shifts community lift growing the 0-19 caseload. Predecessor: Cheshire/Halton/Warrington PCT-provider arms 2011 reorganisation.",
        "sources": [
            {"publisher": "Bridgewater Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bridgewater.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Consolidated NHS Provider Accounts 2023-24", "url": "https://www.england.nhs.uk/publication/consolidated-nhs-provider-accounts-2023-24/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bridgewater Community Healthcare NHS FT inspection reports", "url": "https://www.cqc.org.uk/provider/RY2BR"},
            {"publisher": "NHS Cheshire & Merseyside ICB", "title": "Joint Forward Plan 2024-29", "url": "https://www.cheshireandmerseyside.nhs.uk/"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHS Three Shifts — community-out-of-hospital programme",
            "Bridgewater Community Healthcare NHS Foundation Trust",
            "Establishment costs — Solent NHS Trust",
            "Establishment costs — Leeds Community Healthcare NHS Trust"
        ]
    },
    "Establishment costs — Solent NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Solent NHS Trust"}],
        "description": "Establishment overhead (postage, printing, telephony, stationery, courier, office consumables) at Solent NHS Trust — the integrated community + mental-health provider for Portsmouth, Southampton and parts of Hampshire & Isle of Wight. The line spans patient-letter postage for ~1M+ contacts, lone-worker telephony for community nurses, and franking across primary care/community/MH services. It totalled £3.52M in 2023-24 inside the Premises & Infrastructure orphan parent.",
        "beneficiaries": "~1.3M residents across Portsmouth, Southampton and parts of Hampshire/IoW; ~3,500 WTE delivering ~1.4M community + MH patient contacts/year.",
        "legal_basis": "DHSC GAM 2024-25 · IAS 1 Presentation of Financial Statements · NHS Act 2006 s.30 · Health and Care Act 2022 (integrated commissioning)",
        "key_stats": [
            "Sub-line value 2023-24: £3,524,000",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Community (integrated with MH)",
            "HQ: Highpoint Venue, Bursledon Road, Southampton",
            "Population covered: ~1.3M",
            "WTE: ~3,500",
            "Annual contacts: ~1.4M",
            "Sites: ~50 community bases",
            "Annual income 2023-24: ~£245M",
            "Commissioner: NHS Hampshire & IoW ICB",
            "CQC overall rating: Good (2023)",
            "Status: NHS Trust (not FT) — has been on the FT pipeline"
        ],
        "notes": "Solent's blended community + mental-health caseload concentrates more comms volume than a pure community trust because of MH appointment letters, CPA paperwork and DBT/CMHT outreach. Hampshire & IoW ICB's 2023-24 financial recovery plan flagged corporate-services rationalisation across Solent + Southern Health, which could trim postage/print over 2025-27. April 2025 NIC step-up will hit allocated overhead. Predecessor: pre-2011 Solent Healthcare PCT-provider arm; ongoing strategic review of community + MH provider footprint in HIOW could reshape the establishment baseline.",
        "sources": [
            {"publisher": "Solent NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.solent.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Consolidated NHS Provider Accounts 2023-24", "url": "https://www.england.nhs.uk/publication/consolidated-nhs-provider-accounts-2023-24/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Solent NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/R1C"},
            {"publisher": "NHS Hampshire & Isle of Wight ICB", "title": "Joint Forward Plan 2024-29", "url": "https://www.hantsiowhealthandcare.org.uk/"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHS Three Shifts — community-out-of-hospital programme",
            "Solent NHS Trust",
            "Establishment costs — Sussex Community NHS Foundation Trust",
            "Establishment costs — Bridgewater Community Healthcare NHS Foundation Trust"
        ]
    },
    "Transport (business + patient) — Sussex Community NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Sussex Community NHS Foundation Trust"}],
        "description": "Business mileage (AMAP) for district nurses + community physios + 0-19 health visitors plus patient transport (PTS) sub-contracts, fleet lease and pool-car running for SCFT — the community provider serving Brighton & Hove, East Sussex and West Sussex. With the largest geography of any English community trust, vehicle-mile spend is a structural driver: rural West Sussex and the Downs add range, and the 2024-25 patient-transport contract reset hit costs. The line totalled £3.50M in 2023-24 inside Premises & Infrastructure.",
        "beneficiaries": "~1.7M residents across Sussex; ~5,000 WTE; ~3M community patient contacts/year delivered largely in patient homes.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework (2022 refresh) · Agenda for Change s.17 + HMRC AMAP rates · IFRS 16 Leases (pool fleet) · Highway Act 1980 (lone-worker safety)",
        "key_stats": [
            "Sub-line value 2023-24: £3,498,000",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Community",
            "HQ: Brighton General Hospital",
            "Population covered: ~1.7M (Sussex)",
            "WTE: ~5,000",
            "Annual contacts: ~3M (community)",
            "Sites: ~70 community bases",
            "Annual income 2023-24: ~£260M",
            "Commissioner: NHS Sussex ICB",
            "CQC overall rating: Good (2023)",
            "AMAP rate (HMRC): 45p/mile first 10,000mi; 25p thereafter"
        ],
        "notes": "Sussex's east-west spread (Hastings to Chichester, ~80 miles) makes business mileage structurally higher than London or single-city community trusts. The 2024 NHSE PTS eligibility refresh tightened patient transport access, partially shifting demand to volunteer/charity transport, but capacity gaps in rural West Sussex still attract trust-funded discretionary moves. Industrial action 2023 didn't directly hit Transport. Forward: April 2025 NIC step-up plus HMRC AMAP rate review (frozen at 45p since 2011) is a slow-burn pressure. Predecessor: 2011 PCT-provider arms merged. Successor direction: Three Shifts community lift adds caseload and miles.",
        "sources": [
            {"publisher": "Sussex Community NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sussexcommunity.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Non-emergency patient transport services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "HMRC", "title": "Approved mileage allowance payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Sussex ICB", "title": "Joint Forward Plan 2024-29", "url": "https://www.sussex.ics.nhs.uk/"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHSE NEPTS Eligibility Framework",
            "Sussex Community NHS Foundation Trust",
            "Transport (business + patient) — Gloucestershire Health and Care NHS Foundation Trust",
            "Transport (business + patient) — Kent Community Health NHS Foundation Trust"
        ]
    },
    "Transport (business + patient) — The Royal Marsden NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Royal Marsden NHS Foundation Trust"}],
        "description": "Inter-site shuttle (Chelsea ↔ Sutton ~14 miles) for staff, samples and chemo-pharmacy stock, plus patient transport for radiotherapy fractionation patients moving between sites and home, plus AMAP business mileage for outreach clinics. As a supra-regional cancer centre with twin sites and a ~5M referral catchment via NHSE Specialised Commissioning, daily inter-campus logistics is a structural cost. The line totalled £3.47M in 2023-24 inside Premises & Infrastructure.",
        "beneficiaries": "~60,000 cancer patients/year (NHS + private); ~5M referral catchment via NHSE Specialised Commissioning; ~4,500 WTE across two campuses.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility · Agenda for Change s.17 + HMRC AMAP · IFRS 16 Leases (shuttle/pool fleet) · NHSE Specialised Commissioning specifications",
        "key_stats": [
            "Sub-line value 2023-24: £3,469,644",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Specialist (cancer)",
            "Sites: Chelsea SW3 + Sutton SM2 + Oak Cancer Centre",
            "Inter-site distance: ~14 miles (M25/M3)",
            "Patients/year: ~60,000",
            "WTE: ~4,500",
            "Annual income 2023-24: ~£625M",
            "Commissioner: NHSE Specialised Commissioning",
            "Radiotherapy fractions/year: ~110,000",
            "Specialist transport vendor: NSL/private courier mix"
        ],
        "notes": "The Marsden's twin-site model means every chemo-pharmacy aseptic prep batch made at one site can require courier to the other, and same-day radiotherapy patients commonly travel daily for ~6 weeks (4-week courses common at Sutton) — driving patient transport volumes. The 2023 opening of the Oak Cancer Centre (£70M philanthropic build) shifted some footfall to Sutton, slightly redistributing patient-transport demand. Forward pressures: AMAP rates frozen since 2011; HMRC review pending; April 2025 NIC step-up. Predecessor: pre-Specialised Commissioning patient-transport tariff was bundled in cancer best-practice tariff; current direction is whole-pathway PTS contracts with London ICBs.",
        "sources": [
            {"publisher": "The Royal Marsden NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalmarsden.nhs.uk/about-royal-marsden/corporate-information/annual-reports"},
            {"publisher": "NHS England", "title": "Non-emergency patient transport services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "NHS England", "title": "Specialised Commissioning — Cancer", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "HMRC", "title": "Approved mileage allowance payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHSE Specialised Commissioning",
            "The Royal Marsden NHS Foundation Trust",
            "Business rates — The Royal Marsden NHS Foundation Trust",
            "Transport (business + patient) — Moorfields Eye Hospital NHS Foundation Trust"
        ]
    },
    "Business rates — Alder Hey Children's NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Alder Hey Children's NHS Foundation Trust"}],
        "description": "Non-domestic rates paid to Liverpool City Council for Alder Hey — England's largest children's hospital — covering the £237M New Alder Hey in the Park hospital (opened 2015, IFRIC 12 PFI), the legacy outpatient block, the Catkin Centre (mental health, opened 2022) and the Sunflower House CAMHS unit. Rateable value reset under the 2023 VOA revaluation (1 Apr 2021 AVD). The line totalled £3.42M in 2023-24 inside the Premises & Infrastructure orphan parent.",
        "beneficiaries": "~330,000 patient attendances/year (children & young people up to 16, plus some young-adult specialised services); supra-regional NW England catchment via NHSE Specialised Commissioning paediatric specs.",
        "legal_basis": "Local Government Finance Act 1988 Sch 6 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · VOA 2023 revaluation · DHSC GAM 2024-25 · IFRIC 12 (PFI estate)",
        "key_stats": [
            "Sub-line value 2023-24: £3,416,000",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Specialist (paediatric)",
            "Site: West Derby, Liverpool L12",
            "Patient attendances/year: ~330,000",
            "PFI: New Alder Hey (£237M build, 30-yr concession from 2015)",
            "Catchment: NW England + supra-regional",
            "Annual income 2023-24: ~£446M",
            "Commissioner: NHSE Specialised Commissioning + NHS Cheshire & Merseyside ICB",
            "Status: NHS Foundation Trust",
            "Billing authority: Liverpool City Council",
            "VOA 2023 revaluation: effective 1 Apr 2023"
        ],
        "notes": "NHS hospitals get no mandatory NDR relief, so the New Alder Hey high-spec PFI estate (built 2015) carries a substantial rateable value. The 2023 VOA revaluation, plus the 2022 opening of the Catkin Centre (CAMHS), pushed the line up. The Non-Domestic Rating Act 2024 introduces split multipliers from 2025-26 with a higher rate for high-RV properties — a forward pressure flagged in the trust's 2024-25 financial plan. Predecessor: pre-2015 rateable value was on the legacy 1914 hospital site; successor direction is the Catkin/Sunflower CAMHS expansion plus possible Treasury reform of public-sector NDR.",
        "sources": [
            {"publisher": "Alder Hey Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.alderhey.nhs.uk/about/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (Alder Hey listings)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/15/contents"},
            {"publisher": "NHS England", "title": "Specialised Commissioning — Paediatric services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHSE Specialised Commissioning",
            "Alder Hey Children's NHS Foundation Trust",
            "Business rates — The Royal Marsden NHS Foundation Trust",
            "PFI / LIFT charges — Alder Hey Children's NHS Foundation Trust"
        ]
    },
    "General supplies & services — North East Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "North East Ambulance Service NHS Foundation Trust"}],
        "description": "Non-pharmaceutical consumables (uniforms, PPE, cleaning chemicals, vehicle prep stock, response-bag kit, station consumables) for NEAS — the regional 999/111 provider for the North East and North Cumbria, serving ~2.7M residents from Berwick to Tees Valley. The Make Ready Centre model concentrates non-clinical stock in central hubs. The line totalled £3.40M in 2023-24 inside the Clinical Supplies & Drugs orphan parent.",
        "beneficiaries": "~2.7M residents across Northumberland, Tyne & Wear, Durham and the Tees Valley + North Cumbria; ~620,000 emergency incidents/year handled by ~3,000 WTE.",
        "legal_basis": "DHSC GAM 2024-25 · IAS 2 Inventories · NHS Act 2006 · NHS Supply Chain Framework agreements",
        "key_stats": [
            "Sub-line value 2023-24: £3,396,000",
            "Parent orphan line: Clinical Supplies & Drugs",
            "Trust category: Ambulance (1 of 10)",
            "HQ: Bernicia House, Newcastle",
            "Population served: ~2.7M",
            "Incidents 2023-24: ~620,000",
            "Workforce: ~3,000 staff",
            "Trust income 2023-24: ~£190M",
            "Commissioner: NHS North East & North Cumbria ICB",
            "CQC overall rating: Requires Improvement (Aug 2022)",
            "Make Ready Centres: 5 hubs"
        ],
        "notes": "NEAS spent 2022-24 under heightened scrutiny following the 2022 Sky News reporting of incident-data concerns and the resulting CQC well-led downgrade — corrective spend included consumables for documentation, training kit and re-papered processes. Industrial action 2022-23 (paramedics) drove backfill but mostly hit pay. Cost pressure 2023-24: PPE legacy stock run-down + cleaning-chemical inflation + Cat-1 8-min handover kit churn. Forward: new leadership team 2023-25 driving estate consolidation, plus April 2025 NIC step-up. Predecessor: 2006 merger of Tees, East & North Yorkshire Ambulance Service NHS Trust + Northumbria Ambulance Service NHS Trust.",
        "sources": [
            {"publisher": "North East Ambulance Service NHSFT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.neas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Ambulance quality indicators 2023-24", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "NEAS inspection report 2022", "url": "https://www.cqc.org.uk/provider/RX6"},
            {"publisher": "NHS Supply Chain", "title": "Framework agreements catalogue", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": [
            "Clinical Supplies & Drugs — NHS Trust sector",
            "NHS Supply Chain — DHSC ALB",
            "North East Ambulance Service NHS Foundation Trust",
            "General supplies & services — West Midlands Ambulance Service University NHS Foundation Trust",
            "General supplies & services — North West Ambulance Service NHS Trust"
        ]
    },
    "Transport (business + patient) — Moorfields Eye Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Moorfields Eye Hospital NHS Foundation Trust"}],
        "description": "Inter-site logistics across Moorfields' hub-and-spoke network — City Road flagship plus ~30 satellite sites in NE/NW/SW/SE London, Croydon, Bedford, Watford, Ealing — for staff, surgical kit, drug stocks and patient transport between theatre/clinic flow. Moorfields runs the biggest ophthalmic outreach footprint in England, so business mileage + pool fleet + courier are structural costs. The line totalled £3.34M in 2023-24 inside Premises & Infrastructure.",
        "beneficiaries": "~750,000 patient attendances/year (largest single ophthalmic centre in Europe); supra-regional referral catchment via NHSE Specialised Commissioning + ~30 outreach sites.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility · Agenda for Change s.17 + HMRC AMAP · IFRS 16 Leases (pool fleet) · NHSE Specialised Commissioning specs",
        "key_stats": [
            "Sub-line value 2023-24: £3,336,000",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Specialist (ophthalmic)",
            "Flagship: 162 City Road, EC1V 2PD (since 1899)",
            "Outreach sites: ~30 (London + South East + East)",
            "Attendances/year: ~750,000",
            "WTE: ~2,500",
            "Annual income 2023-24: ~£269M",
            "Commissioner: NHSE Specialised Commissioning",
            "Status: NHS Foundation Trust",
            "Major capital project: Oriel — new flagship at St Pancras (target ~2027)"
        ],
        "notes": "Moorfields pioneered ophthalmic networked care: outreach clinics across London + SE England feed back to City Road for vitreoretinal/oncology theatres, so daily inter-site shuttle of staff, surgical instruments, vitreous specimens and intraocular drugs is core operational logistics. The Oriel project (relocation to a new joint UCL/Moorfields site at St Pancras targeted ~2027) is reshaping forward planning. Industrial action 2023 didn't hit Transport. Forward pressures: AMAP frozen since 2011; April 2025 NIC step-up. Predecessor: pre-2007 outreach was less developed; current direction is to consolidate the London hub at Oriel and refresh the satellite network.",
        "sources": [
            {"publisher": "Moorfields Eye Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.moorfields.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "NHS England", "title": "NEPTS eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "NHS England", "title": "Specialised Commissioning — Specialised Ophthalmology", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Oriel project", "title": "Oriel: A new home for Moorfields and the UCL Institute of Ophthalmology", "url": "https://oriel-london.org.uk/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHSE Specialised Commissioning",
            "Moorfields Eye Hospital NHS Foundation Trust",
            "Transport (business + patient) — The Royal Marsden NHS Foundation Trust",
            "Transport (business + patient) — Great Ormond Street Hospital for Children NHS Foundation Trust"
        ]
    },
    "Establishment costs — Birmingham Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Birmingham Community Healthcare NHS Foundation Trust"}],
        "description": "Establishment overhead (postage, printing, telephony, stationery, courier, office consumables) at BCHC — the lead community provider for Birmingham (pop. ~1.15M), running adult & children's community services, dental, learning disability inpatient, and specialist rehab (West Midlands Rehabilitation Centre, Moseley Hall Hospital). The line carries patient-letter postage, lone-worker telephony, and franking across ~80 community sites. It totalled £3.33M in 2023-24 inside the Premises & Infrastructure orphan parent.",
        "beneficiaries": "~1.15M Birmingham residents + super-regional dental & LD specialist beneficiaries; ~5,500 WTE across ~80 sites; ~1.6M community contacts/year.",
        "legal_basis": "DHSC GAM 2024-25 · IAS 1 Presentation of Financial Statements · NHS Act 2006 s.30 · Health and Care Act 2022",
        "key_stats": [
            "Sub-line value 2023-24: £3,333,000",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Community + specialist rehab",
            "HQ: Priestley Wharf, Aston, Birmingham",
            "Population covered: ~1.15M (Birmingham core) + super-regional",
            "WTE: ~5,500",
            "Annual contacts: ~1.6M",
            "Sites: ~80 community bases incl. Moseley Hall + WMRC",
            "Annual income 2023-24: ~£294M",
            "Commissioner: NHS Birmingham & Solihull ICB",
            "CQC overall rating: Good (2023)",
            "Inpatient beds: ~340 (Moseley Hall + community)"
        ],
        "notes": "BCHC's blended community + specialist-rehab + LD-inpatient mix means more comms volume than a pure community trust — CPA letters, MDT documentation, statutory LD review packs all push postage and printing. Birmingham & Solihull ICB's 2023-24 financial recovery plan is consolidating corporate services across BCHC + BSMHFT, which should trim duplicative overhead 2025-27. Industrial action 2023 hit pay, not Establishment. Forward: April 2025 NIC step-up; Three Shifts community lift adds caseload. Predecessor: 2010 PCT split — BCHC took the provider arm of NHS Birmingham East & North + South Birmingham + HoB.",
        "sources": [
            {"publisher": "Birmingham Community Healthcare NHSFT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bhamcommunity.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Consolidated NHS Provider Accounts 2023-24", "url": "https://www.england.nhs.uk/publication/consolidated-nhs-provider-accounts-2023-24/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "BCHC inspection reports", "url": "https://www.cqc.org.uk/provider/RYW"},
            {"publisher": "NHS Birmingham & Solihull ICB", "title": "Joint Forward Plan 2024-29", "url": "https://www.birminghamsolihull.icb.nhs.uk/"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHS Three Shifts — community-out-of-hospital programme",
            "Birmingham Community Healthcare NHS Foundation Trust",
            "Establishment costs — Leeds Community Healthcare NHS Trust",
            "Establishment costs — Sussex Community NHS Foundation Trust"
        ]
    },
    "General supplies & services — North West Ambulance Service NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "North West Ambulance Service NHS Trust"}],
        "description": "Non-pharma consumables, uniforms, PPE, cleaning chemicals, response-bag stock and station consumables for NWAS — the regional 999/111 provider for Cumbria, Lancashire, Greater Manchester, Merseyside and Cheshire. Largest geography of any English ambulance service (~5,400 sq mi reach), serving ~7M residents. The line totalled £3.31M in 2023-24 inside the Clinical Supplies & Drugs orphan parent.",
        "beneficiaries": "~7M residents across the North West; ~1.4M emergency incidents/year + 5.5M+ NHS 111 calls handled by ~7,000 WTE.",
        "legal_basis": "DHSC GAM 2024-25 · IAS 2 Inventories · NHS Act 2006 · NHS Supply Chain Framework agreements",
        "key_stats": [
            "Sub-line value 2023-24: £3,305,000",
            "Parent orphan line: Clinical Supplies & Drugs",
            "Trust category: Ambulance (1 of 10)",
            "HQ: Ladybridge Hall, Bolton",
            "Population served: ~7M",
            "Geography: Cumbria + Lancashire + GM + Merseyside + Cheshire",
            "Incidents 2023-24: ~1.4M",
            "111 calls 2023-24: ~5.5M",
            "Workforce: ~7,000 WTE",
            "Trust income 2023-24: ~£521M",
            "CQC overall rating: Good (Aug 2024)",
            "Make Ready Centres: 5 hubs"
        ],
        "notes": "NWAS handled the third-largest 999 demand in England behind LAS and SECAmb-equivalent in 2023-24 and runs the largest 111 footprint of any single trust. Cumbria's rural reach and the Greater Manchester urban core create a mixed cost profile: rural fleet has heavier vehicle-prep stock per km, urban hubs higher consumable churn. The 2023 ambulance industrial action hit pay; PPE legacy run-down + cleaning chemical inflation drove the GS&S line up 2022-24. CQC well-led upgraded to Good in 2024 (from Requires Improvement 2020). Forward: April 2025 NIC step-up plus fleet electrification pilot.",
        "sources": [
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwas.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Ambulance quality indicators 2023-24", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "NWAS inspection report 2024", "url": "https://www.cqc.org.uk/provider/RX7"},
            {"publisher": "NHS Supply Chain", "title": "Framework agreements catalogue", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": [
            "Clinical Supplies & Drugs — NHS Trust sector",
            "NHS Supply Chain — DHSC ALB",
            "North West Ambulance Service NHS Trust",
            "General supplies & services — North East Ambulance Service NHS Foundation Trust",
            "General supplies & services — West Midlands Ambulance Service University NHS Foundation Trust"
        ]
    },
    "Business rates — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "London Ambulance Service NHS Trust"}],
        "description": "Non-domestic rates paid to ~30 London billing authorities for LAS — the only England ambulance trust serving a single core city, covering Greater London (pop. ~9M). Estate spans the HQ at 220 Waterloo Road, ~70 ambulance stations, the Bow Make Ready Centre, the Deptford fleet workshops and the Emergency Operations Centres at Waterloo + Bow. London's high rateable values + the 2023 VOA revaluation push the total. The line totalled £3.28M in 2023-24 inside Premises & Infrastructure.",
        "beneficiaries": "~9M Greater London residents; ~2.0M emergency incidents and ~2.0M NHS 111 calls/year handled by ~9,000 WTE.",
        "legal_basis": "Local Government Finance Act 1988 Sch 6 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · VOA 2023 revaluation · DHSC GAM 2024-25 · GLA Act 1999 (London context)",
        "key_stats": [
            "Sub-line value 2023-24: £3,276,000",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Ambulance (1 of 10)",
            "Population served: ~9M (Greater London)",
            "Stations + sites: ~70",
            "Make Ready Centres: Bow + Deptford",
            "EOCs: Waterloo + Bow",
            "Incidents 2023-24: ~2.0M",
            "Workforce: ~9,000 WTE (largest UK ambulance trust by HC)",
            "Trust income 2023-24: ~£619M",
            "Billing authorities: ~30 London boroughs + Corporation of London",
            "CQC overall rating: Good (Apr 2024)"
        ],
        "notes": "London's central rateable values (Waterloo HQ adjacent to South Bank) and dispersed station footprint across all 32 boroughs mean LAS pays NDR to more billing authorities than any other ambulance trust. The 2023 VOA revaluation reset post-pandemic values; the Non-Domestic Rating Act 2024 split-multiplier reform is a forward pressure for London-heavy estate. CQC upgraded LAS to Good (well-led) in April 2024 after the 2022 demand surge. Industrial action 2022-23 didn't directly hit Business Rates. Predecessor: rates baseline reset on each revaluation cycle (2017, 2023, next 2026); strategic direction is fewer larger Make Ready hubs.",
        "sources": [
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/15/contents"},
            {"publisher": "Care Quality Commission", "title": "LAS inspection report April 2024", "url": "https://www.cqc.org.uk/provider/RRU"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHS England — Ambulance Services Programme",
            "London Ambulance Service NHS Trust",
            "Business rates — The Royal Marsden NHS Foundation Trust",
            "Business rates — Alder Hey Children's NHS Foundation Trust"
        ]
    },
    "Amortisation — Central London Community Healthcare NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Central London Community Healthcare NHS Trust"}],
        "description": "Amortisation of intangible assets (mostly capitalised software — SystmOne contract licences, RiO mental-health record system, Microsoft 365 enterprise agreement, plus internally developed clinical workflow apps) at CLCH — the largest English community trust, covering 11 inner & west London boroughs. Software-heavy because community providers run on shared electronic patient record platforms. The line totalled £3.22M in 2023-24 inside Premises & Infrastructure.",
        "beneficiaries": "~2M residents across 11 London boroughs (Westminster, K&C, Camden, H&F, Wandsworth, Merton, Brent, Ealing, Harrow, Hounslow, Barnet); ~3,500 WTE delivering ~3M contacts/year.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC GAM 2024-25 ch.5 (intangible-asset amortisation) · NHS Act 2006 · IFRS 3 (any acquired intangibles)",
        "key_stats": [
            "Sub-line value 2023-24: £3,220,000",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Community (largest in England)",
            "HQ: Parsons Green, Fulham",
            "Boroughs covered: 11 (inner + west London)",
            "Population covered: ~2M",
            "WTE: ~3,500",
            "Annual contacts: ~3M",
            "Annual income 2023-24: ~£303M",
            "Commissioner: NHS NW London ICB + NHS NC London ICB + NHS SW London ICB",
            "CQC overall rating: Good (2023)",
            "Major EPR: SystmOne (TPP)"
        ],
        "notes": "CLCH's 11-borough footprint means it spans three London ICBs and consequently maintains parallel software contracts and integration overhead — driving capitalised intangible asset balances above peer community trusts. The 2022 IFRS 16 transition shifted some IT contracts between Lease and Amortisation classifications. Forward: the NHSE Federated Data Platform (Palantir-built, awarded 2023) and the SCW LCRES roll-out will recapitalise software stacks 2025-27. Predecessor: the 2011 PCT-provider-arm spin-out created the trust; successor direction is integrated tri-ICB digital tooling under Three Shifts.",
        "sources": [
            {"publisher": "Central London Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://clch.nhs.uk/about-us/publications"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (intangibles ch.5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Federated Data Platform programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-through-data/federated-data-platform/"},
            {"publisher": "Care Quality Commission", "title": "CLCH inspection reports", "url": "https://www.cqc.org.uk/provider/RYX"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHSE Federated Data Platform",
            "Central London Community Healthcare NHS Trust",
            "Amortisation — Sussex Community NHS Foundation Trust",
            "Lease expenditure — Central London Community Healthcare NHS Trust"
        ]
    },
    "General supplies & services — Derbyshire Community Health Services NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Derbyshire Community Health Services NHS Foundation Trust"}],
        "description": "Non-pharma consumables and supplies (incontinence pads, dressings stock not coded as drugs, district-nursing wound-care, MSK equipment, school-nursing kit, community-clinic consumables) at DCHS — a county-wide community provider for Derbyshire serving ~1M residents from Buxton to High Peak via 11 community hospitals + ~50 clinics. The line totalled £3.13M in 2023-24 inside the Clinical Supplies & Drugs orphan parent.",
        "beneficiaries": "~1.05M Derbyshire residents (excluding Derby City core acute) across the county; ~4,200 WTE delivering ~2.4M community contacts/year.",
        "legal_basis": "DHSC GAM 2024-25 · IAS 2 Inventories · NHS Act 2006 · NHS Supply Chain Framework agreements",
        "key_stats": [
            "Sub-line value 2023-24: £3,133,000",
            "Parent orphan line: Clinical Supplies & Drugs",
            "Trust category: Community (1 of 18)",
            "HQ: Walton Hospital, Chesterfield",
            "Population covered: ~1.05M",
            "Community hospitals: 11",
            "Clinics + community bases: ~50",
            "WTE: ~4,200",
            "Annual contacts: ~2.4M",
            "Annual income 2023-24: ~£199M",
            "Commissioner: NHS Derby & Derbyshire ICB",
            "CQC overall rating: Outstanding (2019, last full inspection)"
        ],
        "notes": "DCHS is one of only two community trusts CQC-rated Outstanding (since 2019). Its 11 community hospitals carry inpatient consumables not seen at non-bedded community trusts — wound-care, continence, mobility kit. Stock pressure 2022-24 came from PPE legacy run-down and inflation on dressings + incontinence products via NHS Supply Chain. Forward: April 2025 NIC step-up plus Three Shifts community lift growing intermediate-care caseload + bed days. Predecessor: 2011 PCT-provider arm of NHS Derbyshire County. Successor direction: deeper integration with University Hospitals of Derby & Burton + Derbyshire Healthcare under the ICS provider collaborative.",
        "sources": [
            {"publisher": "Derbyshire Community Health Services NHSFT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchs.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "DCHS inspection report 2019 (Outstanding)", "url": "https://www.cqc.org.uk/provider/RY8"},
            {"publisher": "NHS Supply Chain", "title": "Framework agreements catalogue", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Derby & Derbyshire ICB", "title": "Joint Forward Plan 2024-29", "url": "https://www.derbyandderbyshireccg.nhs.uk/"}
        ],
        "related": [
            "Clinical Supplies & Drugs — NHS Trust sector",
            "NHS Supply Chain — DHSC ALB",
            "Derbyshire Community Health Services NHS Foundation Trust",
            "General supplies & services — Sussex Community NHS Foundation Trust",
            "General supplies & services — Norfolk Community Health and Care NHS Trust"
        ]
    },
    "Transport (business + patient) — Gloucestershire Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Gloucestershire Health and Care NHS Foundation Trust"}],
        "description": "Business mileage (AMAP) for district nurses + community physios + 0-19 health visitors + community mental-health teams, plus patient-transport for older-people inpatient flow at the seven community hospitals (Cirencester, Tewkesbury, Stroud, Vale, Dilke, Lydney, North Cotswolds), and pool-fleet running. GHC is the integrated community + mental-health provider for Gloucestershire (pop. ~650k). The line totalled £2.97M in 2023-24 inside Premises & Infrastructure.",
        "beneficiaries": "~650,000 Gloucestershire residents (rural Cotswolds + Forest of Dean + Severn Vale + Stroud); ~5,000 WTE; ~1.4M community + MH contacts/year.",
        "legal_basis": "NHS Act 2006 · NHSE NEPTS Eligibility Framework · Agenda for Change s.17 + HMRC AMAP · IFRS 16 Leases · NHSE Mental Health Investment Standard",
        "key_stats": [
            "Sub-line value 2023-24: £2,970,386",
            "Parent orphan line: Premises & Infrastructure",
            "Trust category: Community + MH integrated",
            "HQ: Edward Jenner Court, Brockworth",
            "Population covered: ~650,000",
            "Community hospitals: 7 (Cirencester, Tewkesbury, Stroud, Vale, Dilke, Lydney, North Cotswolds)",
            "WTE: ~5,000",
            "Annual contacts: ~1.4M (community + MH)",
            "Annual income 2023-24: ~£250M",
            "Commissioner: NHS Gloucestershire ICB",
            "CQC overall rating: Good (2023)",
            "AMAP rate (HMRC): 45p/mile first 10,000mi"
        ],
        "notes": "The Cotswolds + Forest of Dean rural geography (~1,000 sq mi) means GHC clinicians log heavy business mileage — visiting older-people in remote Forest villages adds cost vs urban community trusts. The 2022 GHC merger created a single integrated provider, which centralised pool-car management but didn't reduce miles. Industrial action 2023 didn't hit Transport. Forward: AMAP frozen since 2011; Three Shifts community lift adds mileage; April 2025 NIC step-up. Predecessor: 2019 merger of Gloucestershire Care Services NHS Trust + 2gether NHS Foundation Trust to create the integrated GHC provider.",
        "sources": [
            {"publisher": "Gloucestershire Health and Care NHSFT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ghc.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-emergency patient transport services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "HMRC", "title": "Approved mileage allowance payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Gloucestershire ICB", "title": "Joint Forward Plan 2024-29", "url": "https://www.nhsglos.nhs.uk/"}
        ],
        "related": [
            "Premises & Infrastructure — NHS Trust sector",
            "NHSE NEPTS Eligibility Framework",
            "Gloucestershire Health and Care NHS Foundation Trust",
            "Transport (business + patient) — Sussex Community NHS Foundation Trust",
            "Transport (business + patient) — Kent Community Health NHS Foundation Trust"
        ]
    },
    "General supplies & services — Sussex Community NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Sussex Community NHS Foundation Trust"}],
        "description": "Non-pharma consumables and supplies (incontinence pads, dressings stock not coded as drugs, district-nursing wound-care, MSK community equipment, school-nursing kit, sexual-health clinic consumables) at SCFT — the community provider for Brighton & Hove, East Sussex, West Sussex, with the largest geographic footprint of any English community trust. The line totalled £2.96M in 2023-24 inside the Clinical Supplies & Drugs orphan parent.",
        "beneficiaries": "~1.7M Sussex residents (Brighton & Hove + East Sussex + West Sussex); ~5,000 WTE delivering ~3M community contacts/year mostly in patient homes.",
        "legal_basis": "DHSC GAM 2024-25 · IAS 2 Inventories · NHS Act 2006 · NHS Supply Chain Framework agreements · Health and Care Act 2022",
        "key_stats": [
            "Sub-line value 2023-24: £2,964,000",
            "Parent orphan line: Clinical Supplies & Drugs",
            "Trust category: Community",
            "HQ: Brighton General Hospital",
            "Population covered: ~1.7M (Sussex)",
            "Geography spread: ~80 miles east-west (Hastings to Chichester)",
            "WTE: ~5,000",
            "Annual contacts: ~3M",
            "Sites: ~70 community bases",
            "Annual income 2023-24: ~£260M",
            "Commissioner: NHS Sussex ICB",
            "CQC overall rating: Good (2023)"
        ],
        "notes": "SCFT's east-west geographic spread structurally inflates pooled stock-holding because supplies must be staged across multiple distribution points (Brighton, Hastings, Chichester). PPE legacy run-down 2022-23 + dressings inflation drove cost growth. Industrial action 2023 hit pay, not supplies. Forward: April 2025 NIC step-up plus Three Shifts community lift growing district-nursing caseload — pulls dressings, continence and MSK consumables. Predecessor: 2008 PCT-provider arm of NHS West Sussex + NHS East Sussex Downs & Weald + NHS Hastings & Rother combined under SCFT 2011. Successor direction: Sussex ICS provider collaborative integration with University Hospitals Sussex.",
        "sources": [
            {"publisher": "Sussex Community NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sussexcommunity.nhs.uk/about-us/publications"},
            {"publisher": "NHS Supply Chain", "title": "Framework agreements catalogue", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "SCFT inspection reports", "url": "https://www.cqc.org.uk/provider/RDR"},
            {"publisher": "NHS Sussex ICB", "title": "Joint Forward Plan 2024-29", "url": "https://www.sussex.ics.nhs.uk/"}
        ],
        "related": [
            "Clinical Supplies & Drugs — NHS Trust sector",
            "NHS Supply Chain — DHSC ALB",
            "Sussex Community NHS Foundation Trust",
            "General supplies & services — Derbyshire Community Health Services NHS Foundation Trust",
            "Transport (business + patient) — Sussex Community NHS Foundation Trust"
        ]
    },
}
