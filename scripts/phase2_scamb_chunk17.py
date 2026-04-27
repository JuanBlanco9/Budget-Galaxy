# -*- coding: utf-8 -*-
# Phase 2 SCamb — chunk 17 (17 NHS Specialist/Community/Ambulance Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "RJAH's £0.32M amortisation charge represents the systematic write-down of intangible assets — predominantly capitalised software licences and software development under IAS 38, including the Trust's electronic patient record stack, theatre-management/scheduling software supporting elective orthopaedic flow at Gobowen, the Midlands & North West Spinal Service registry, and capitalised development on imaging-PACS and the Trust's data platform. The amortisation line is small and stable, reflecting RJAH's specialist single-site model with limited proprietary digital estate beyond clinical-system licences.",
        "beneficiaries": "Tertiary orthopaedic and spinal centre serving a c. 3M Shropshire, Mid-Wales and West Midlands referral catchment from a single 167-bed campus at Gobowen near Oswestry; runs c. 7,500 elective inpatient + day-case episodes/yr and the Midlands Centre for Spinal Injuries with c. 1,800 WTE.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.32M"},
            {"label": "Trust profile", "value": "Specialist orthopaedic + spinal tertiary centre — single Gobowen campus, near Oswestry, Shropshire"},
            {"label": "Catchment", "value": "c. 3M referral catchment — Shropshire, Mid + North Wales, West Midlands; supra-regional spinal injuries"},
            {"label": "Estate", "value": "Single 167-bed campus + Midlands Centre for Spinal Injuries + Veterans' Orthopaedic Service"},
            {"label": "Annual activity", "value": "c. 7,500 elective inpatient + day-case episodes/yr; c. 75,000 outpatient attendances; c. 200 spinal-injury admissions"},
            {"label": "Workforce", "value": "c. 1,800 WTE — orthopaedic surgeons, AHPs, theatre teams, spinal nursing"},
            {"label": "Intangibles class", "value": "EPR licences (Lorenzo / SystmOne / TPP), theatre-scheduling software, PACS, capitalised data-platform development, spinal registry"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; long-life clinical EPRs straight-lined over service life"},
            {"label": "Delivery body", "value": "RJAH IT/Digital + Shropshire, Telford & Wrekin ICB digital programme + EPR/PACS vendors"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (spinal injuries + complex spine) + Shropshire ICB + DHSC + NHSE Frontline Digitisation"},
            {"label": "Funding trajectory", "value": "Stable around £0.3M; modest growth as Frontline Digitisation capital crystallises into in-service intangibles + theatre-flow software"},
            {"label": "Evaluation evidence", "value": "RJAH ARA; CQC provider profile (RL1) — rated Good/Outstanding; National Joint Registry data; GIRFT orthopaedic benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy paper + early-2010s clinical systems · Successor: Frontline Digitisation 2025-30 EPR uplift + GIRFT-driven theatre productivity software"}
        ],
        "notes": "RJAH is one of England's specialist orthopaedic tertiary centres alongside RNOH Stanmore and the Royal Orthopaedic Hospital Birmingham, serving a supra-regional Shropshire/Welsh-Marches/West-Midlands catchment from its 1922-founded Gobowen campus. Amortisation is small in absolute terms because the Trust's intangibles base is dominated by software licences and capitalised development (theatre scheduling, PACS, the spinal registry) rather than large self-developed platforms. Drivers include NHSE Frontline Digitisation capital flowing through to in-service software, GIRFT orthopaedic productivity initiatives requiring theatre-flow tooling, and the long-cycle nature of the National Joint Registry submissions. The line is unlikely to grow materially absent a step-change in EPR strategy.",
        "sources": [
            {"publisher": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rjah.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "RJAH Orthopaedic Hospital NHS Foundation Trust provider profile (RL1)", "url": "https://www.cqc.org.uk/provider/RL1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Getting It Right First Time (GIRFT)", "title": "Orthopaedic and spinal national reports", "url": "https://gettingitrightfirsttime.co.uk/"}
        ],
        "related": ["The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Amortisation — The Walton Centre NHS Foundation Trust", "Amortisation — The Royal Orthopaedic Hospital NHS Foundation Trust", "NHS England"]
    },
    "Lease expenditure — Derbyshire Community Health Services NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Derbyshire Community Health Services NHS Foundation Trust"}],
        "description": "DCHS's £0.32M residual lease expenditure line covers IFRS 16 right-of-use leases that fall below the on-balance-sheet recognition threshold or are short-term — including small satellite-clinic rooms, shared GP-practice consulting space, low-value office lets, photocopier/MFD agreements, and pool-fleet vehicle leases for the district-nursing and community-physio workforce. The bulk of DCHS premises are NHSPS-leased community hospitals and clinics under a separate sub-let mechanism, so this line captures the de-minimis tail rather than the main estate cost.",
        "beneficiaries": "DCHS provides community nursing, community hospitals, MSK, podiatry, sexual health and children's services across the c. 1.05M population of Derbyshire; runs c. 11 community hospitals (incl. Walton, Whitworth, Newholme, Babington, Cavendish, Heanor, Buxton); c. 4,500 WTE.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.32M"},
            {"label": "Trust profile", "value": "Standalone community FT serving whole of Derbyshire (excl. acute services delivered by UHDB and Chesterfield Royal)"},
            {"label": "Footprint", "value": "c. 11 community hospitals + c. 80 health centres, clinics, GP-shared sites; mostly NHSPS-leased"},
            {"label": "Population served", "value": "c. 1.05M Derbyshire residents"},
            {"label": "Annual activity", "value": "c. 2.5M community contacts/yr; c. 16,000 community-hospital admissions; c. 70,000 MSK referrals"},
            {"label": "Workforce", "value": "c. 4,500 WTE — district nurses, AHPs, community physios, podiatrists, school nurses, HVs"},
            {"label": "Lease composition", "value": "GP-shared rooms, photocopier/MFD, satellite-clinic short lets, pool-fleet vehicles below IFRS 16 capitalisation threshold"},
            {"label": "IFRS 16 driver", "value": "April 2022 transition put main NHSPS estate on balance sheet; this residual line is the post-transition tail (short-term + low-value exemptions)"},
            {"label": "Delivery body", "value": "DCHS Estates & Facilities + NHS Property Services (main estate) + commercial leasing (vehicles + MFD)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Joined Up Care Derbyshire ICB + NHSPS"},
            {"label": "Funding trajectory", "value": "Stable c. £0.3M; Three Shifts (Darzi Sep 2024) may grow community-clinic footprint; April 2025 employer-NIC step-up flows indirect via supplier overhead"},
            {"label": "Evaluation evidence", "value": "DCHS ARA; CQC provider profile (RY8) — rated Outstanding (one of the highest-rated community trusts); ERIC 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 PCT-provider arm leases · Successor: Three Shifts community uplift + NHSPS estate optimisation"}
        ],
        "notes": "DCHS is one of the few standalone community foundation trusts and has historically been rated Outstanding by CQC, giving it relative stability of estate. Its main premises footprint sits inside NHSPS-leased community hospitals and clinics whose costs flow through Premises rather than this line, so the £0.32M lease expenditure is a residual capturing IFRS 16 short-term + low-value exemptions plus equipment leases. Drivers include the IFRS 16 April 2022 step-change (main estate jumped on balance sheet), the Three Shifts community direction (Darzi Sep 2024) potentially growing satellite-clinic space, and ongoing NHSPS estate-optimisation moves that may consolidate or relocate sub-let arrangements.",
        "sources": [
            {"publisher": "Derbyshire Community Health Services NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchs.nhs.uk/about-us/corporate-publications"},
            {"publisher": "Care Quality Commission", "title": "DCHS NHS Foundation Trust provider profile (RY8)", "url": "https://www.cqc.org.uk/provider/RY8"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "NHS Property Services", "title": "Community estate and lease arrangements", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Derbyshire Community Health Services NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Hertfordshire Community NHS Trust", "Lease expenditure — Gloucestershire Health and Care NHS Foundation Trust", "NHS Property Services"]
    },
    "Lease expenditure — Hertfordshire Community NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Hertfordshire Community NHS Trust"}],
        "description": "HCT's £0.32M residual lease expenditure covers IFRS 16 short-term and low-value-exemption leases plus equipment agreements — small satellite-clinic rooms in shared GP and council premises, photocopier/MFD contracts, and pool-fleet leases supporting the district-nursing and children's-services workforce across Hertfordshire and West Essex. The bulk of HCT's main community-hospital and clinic estate (Welwyn QEII, Hemel Hempstead, Cheshunt) sits in NHSPS-leased premises whose cost flows through the Premises line rather than this residual.",
        "beneficiaries": "HCT serves a c. 1.2M Hertfordshire and parts of West Essex population delivering c. 2.0M community contacts/yr through district nursing, children's services (incl. school nursing, HVs), MSK, community paediatrics; c. 2,800 WTE across c. 50+ sites incl. community hospitals at Hemel Hempstead, Welwyn Garden City, Cheshunt and Bishop's Stortford.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.32M"},
            {"label": "Trust profile", "value": "Standalone community trust covering Hertfordshire + parts of West Essex"},
            {"label": "Footprint", "value": "c. 50+ sites — community hospitals at Hemel Hempstead, Welwyn QEII, Cheshunt, Bishop's Stortford + clinics + children's centres"},
            {"label": "Population served", "value": "c. 1.2M residents (Hertfordshire core) + West Essex children's commission"},
            {"label": "Annual activity", "value": "c. 2.0M community contacts/yr (district nursing + children's + MSK + community paediatrics)"},
            {"label": "Workforce", "value": "c. 2,800 WTE — district nurses, school nurses, HVs, MSK physios, community paediatricians"},
            {"label": "Lease composition", "value": "Photocopier/MFD, GP-shared satellite rooms, pool-fleet vehicles, short-term clinic lets — IFRS 16 short-term/low-value tail"},
            {"label": "IFRS 16 driver", "value": "April 2022 transition put main NHSPS estate on balance sheet; this residual sits below capitalisation threshold"},
            {"label": "Delivery body", "value": "HCT Estates & Facilities + NHS Property Services (main estate) + commercial leasing for fleet + MFD"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hertfordshire & West Essex ICB + NHSPS"},
            {"label": "Funding trajectory", "value": "Stable c. £0.3M; Three Shifts (Darzi Sep 2024) may grow satellite-clinic footprint; West Essex children's contract expansion historic driver"},
            {"label": "Evaluation evidence", "value": "HCT ARA; CQC provider profile (RY4) — rated Good; NHSE community-services dataset (CSDS); ERIC 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2010 Herts PCT-provider arm leases · Successor: Three Shifts community uplift + NHSPS estate optimisation"}
        ],
        "notes": "HCT is one of two community trusts serving the Hertfordshire footprint (alongside Hertfordshire Partnership University NHSFT for mental health) and holds the West Essex children's services contract. The £0.32M lease line is small because main premises sit on NHSPS leases captured in the Premises line; this is the IFRS 16 residual covering low-value/short-term exemptions plus equipment + pool-fleet vehicles. Drivers include the IFRS 16 April 2022 transition pulling main estate onto balance sheet, the West Essex children's contract historic expansion, the Three Shifts (Sep 2024) community direction of travel, and ongoing photocopier/MFD refresh cycles. Trajectory is broadly flat but sensitive to satellite-clinic demand growth.",
        "sources": [
            {"publisher": "Hertfordshire Community NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hct.nhs.uk/about-us/publications-and-reports/"},
            {"publisher": "Care Quality Commission", "title": "Hertfordshire Community NHS Trust provider profile (RY4)", "url": "https://www.cqc.org.uk/provider/RY4"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "NHS Property Services", "title": "Community estate and lease arrangements", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Hertfordshire Community NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Derbyshire Community Health Services NHS Foundation Trust", "Lease expenditure — Gloucestershire Health and Care NHS Foundation Trust", "NHS Property Services"]
    },
    "Transport (business + patient) — Hounslow and Richmond Community Healthcare NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Hounslow and Richmond Community Healthcare NHS Trust"}],
        "description": "HRCH's £0.32M transport line covers business mileage paid to community staff under AfC Section 17 + AMAP rates plus patient transport for community-based services across Hounslow and Richmond — district nurses driving between patients' homes, health visitors moving between Sure Start centres and child clinics, MSK community physios visiting outpatient sites, and end-of-life palliative-care community teams. London traffic congestion + ULEZ + paid parking inflate per-visit travel time even on relatively short geographic distances.",
        "beneficiaries": "Serves c. 480,000 residents of Hounslow and Richmond upon Thames (NW + SW outer London) delivering c. 850,000 community contacts/yr via district nursing, HVs, school nursing, community paediatrics and MSK; c. 1,300 WTE across c. 30 community sites + clinics + Sure Start hubs.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility · AfC Section 17 (business mileage) + HMRC AMAP rates · IFRS 16 (pool fleet) · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£0.32M"},
            {"label": "Trust profile", "value": "Outer-London community trust serving Hounslow + Richmond; mostly community-nursing / children's services / MSK"},
            {"label": "Population served", "value": "c. 480,000 (Hounslow c. 290k + Richmond c. 195k)"},
            {"label": "Annual activity", "value": "c. 850,000 community contacts/yr; district-nursing visits, HV contacts, school-nursing assessments"},
            {"label": "Workforce", "value": "c. 1,300 WTE — district nurses, HVs, school nurses, MSK physios, community paediatricians"},
            {"label": "Estate", "value": "c. 30 sites — community hospitals (Teddington Memorial), polyclinics, Sure Start hubs, GP-shared rooms"},
            {"label": "Mileage rate", "value": "AfC Section 17: 56p/mile up to 3,500 miles then 20p; HMRC AMAP 45p/25p reference"},
            {"label": "London driver", "value": "ULEZ + emissions zone vehicle compliance + paid parking + congestion increases per-visit travel cost"},
            {"label": "Delivery body", "value": "HRCH workforce (own cars, claim mileage) + small pool fleet + commercial fleet leasing"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NW London ICB + SW London ICB (joint) + NHSE Net Zero (fleet electrification)"},
            {"label": "Funding trajectory", "value": "c. £0.3M stable; April 2025 employer-NIC step-up indirect; ULEZ extension Aug 2023 + fleet electrification policy a long-cycle pressure"},
            {"label": "Evaluation evidence", "value": "HRCH ARA; CQC provider profile (RY9) — rated Outstanding; ERIC 2023-24; NHSE community-services dataset"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Hounslow/Richmond PCT-provider arm transport · Successor: NHSE Net Zero EV-fleet 2030 plan + Three Shifts community uplift"}
        ],
        "notes": "HRCH is a small outer-London community trust covering two boroughs (Hounslow and Richmond) which sit in different ICBs (NW + SW London), giving it a complex commissioning landscape. Transport is dominated by AfC Section 17 mileage claimed by district nurses and HVs using their own vehicles, with a small pool fleet for shared assets. London-specific cost pressures include the ULEZ extension (Aug 2023), high parking + congestion costs, and the medium-term shift to EV fleet under NHSE Net Zero. The line is small but politically sensitive given it directly funds workforce travel — material to staff retention. Three Shifts (Darzi Sep 2024) may grow visit volume.",
        "sources": [
            {"publisher": "Hounslow and Richmond Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hrch.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "HRCH NHS Trust provider profile (RY9)", "url": "https://www.cqc.org.uk/provider/RY9"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — reimbursement of travel costs", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "NHS England", "title": "Delivering a 'Net Zero' National Health Service", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"},
            {"publisher": "Transport for London", "title": "Ultra Low Emission Zone (ULEZ)", "url": "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone"},
            {"publisher": "HM Revenue and Customs", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"}
        ],
        "related": ["Hounslow and Richmond Community Healthcare NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Transport (business + patient) — Central London Community Healthcare NHS Trust", "Transport (business + patient) — Sussex Community NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Bridgewater Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Bridgewater Community Healthcare NHS Foundation Trust"}],
        "description": "Bridgewater's £0.29M business-rates line is non-domestic rates payable on the Trust's directly-occupied community estate across Halton, St Helens and Warrington — community hospitals, clinics, walk-in centres, dental access centres, Sure Start sites and HQ — calculated by the Valuation Office Agency under the Local Government Finance Act 1988 (Sch 6) using the rateable value × the small-business or standard multiplier. NHS trusts pay the full mandatory rate without charity relief (England), in contrast to council-occupied or charity-occupied premises.",
        "beneficiaries": "Serves c. 360,000 residents of Halton, St Helens and Warrington (plus pockets of Wigan/Bolton via specialist services); delivers c. 850,000 community contacts/yr through c. 1,800 WTE district nurses, HVs, school nurses, AHPs, MSK physios across c. 60 community sites.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 Revaluation · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.29M"},
            {"label": "Footprint", "value": "Halton, St Helens, Warrington (+ specialist services into Wigan/Bolton)"},
            {"label": "Estate", "value": "c. 60 community sites — community hospitals, clinics, dental access centres, walk-in centres, Sure Start hubs"},
            {"label": "Population served", "value": "c. 360,000 residents in core boroughs"},
            {"label": "Annual activity", "value": "c. 850,000 community contacts/yr"},
            {"label": "Workforce", "value": "c. 1,800 WTE — district nurses, HVs, school nurses, AHPs, MSK community physios"},
            {"label": "Multiplier (24-25)", "value": "Standard non-domestic multiplier 54.6p/£ (England); small-business 49.9p/£; revaluation effective 1 April 2023"},
            {"label": "Charity relief", "value": "NHS trusts do NOT receive 80% mandatory charity relief (unlike many council/charity occupiers); pay full assessed liability"},
            {"label": "Delivery body", "value": "Valuation Office Agency (assessment) + 3 billing authorities (Halton, St Helens, Warrington councils) + Bridgewater Estates"},
            {"label": "Policy owner", "value": "DHSC + DLUHC/MHCLG (rates policy) + HM Treasury + Cheshire & Merseyside ICB"},
            {"label": "Funding trajectory", "value": "Revaluation 2023 step-change; multiplier indexed to CPI capped; future revaluations every 3 years (2026 next)"},
            {"label": "Evaluation evidence", "value": "Bridgewater ARA; CQC provider profile (RY2) — rated Good; ERIC 2023-24 estate footprint"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 revaluation valuations · Successor: 2026 revaluation + Non-Domestic Rating (Multipliers and Private Finance) Act 2024 reforms"}
        ],
        "notes": "Business rates on NHS estate are a contested public-finance flow: trusts pay full mandatory rates (no charity relief in England) to local councils, who keep a share under business-rates retention. Bridgewater's £0.29M reflects its directly-occupied community estate (NHSPS-leased premises pay rates separately via NHSPS rather than this line). Drivers include the 1 April 2023 VOA revaluation (which generally moved community-property rateable values modestly upward in the North West), the Non-Domestic Rating Act 2024 multiplier reforms, and the upcoming 2026 revaluation. Local political pressure occasionally surfaces for NHS rate relief but this has not been enacted in England.",
        "sources": [
            {"publisher": "Bridgewater Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bridgewater.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Bridgewater Community Healthcare NHS Foundation Trust provider profile (RY2)", "url": "https://www.cqc.org.uk/provider/RY2"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government (legislation.gov.uk)", "title": "Local Government Finance Act 1988", "url": "https://www.legislation.gov.uk/ukpga/1988/41/contents"},
            {"publisher": "UK Government (legislation.gov.uk)", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/29/contents"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Bridgewater Community Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Shropshire Community Health NHS Trust", "Business rates — Lincolnshire Community Health Services NHS Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Queen Victoria Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Queen Victoria Hospital NHS Foundation Trust"}],
        "description": "QVH's £0.29M transport line covers business mileage paid under AfC Section 17 + AMAP rates to clinicians and outreach staff travelling between East Grinstead and the Trust's outreach clinics across Sussex, Surrey, Kent and South London (incl. Crawley, Brighton, Tunbridge Wells, Maidstone, Ashford, Croydon outreach), plus a small pool fleet and limited patient-transport for the supra-regional reconstructive-surgery and burns referral catchment. QVH is a small specialist trust so the absolute line is modest but disproportionately important for outreach delivery.",
        "beneficiaries": "QVH at East Grinstead is a tertiary specialist centre for reconstructive plastic surgery, burns, corneal/eye services and head-and-neck cancer; serves a c. 4M South East England catchment (Sussex, Surrey, Kent, South London); c. 1,200 WTE; c. 80,000 outpatient attendances + c. 6,000 inpatient/day-case episodes/yr.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility · AfC Section 17 + HMRC AMAP rates · IFRS 16 (pool fleet) · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£0.29M"},
            {"label": "Trust profile", "value": "Specialist tertiary trust — reconstructive plastic surgery, burns, corneal/eye, head-and-neck cancer; East Grinstead, West Sussex"},
            {"label": "Catchment", "value": "c. 4M South East England — Sussex, Surrey, Kent, South London (plus national/international referrals for some specialties)"},
            {"label": "Annual activity", "value": "c. 80,000 outpatient attendances; c. 6,000 inpatient/day-case episodes/yr"},
            {"label": "Workforce", "value": "c. 1,200 WTE — plastic surgeons, ophthalmologists, head-and-neck surgeons, ITU + theatre teams"},
            {"label": "Outreach footprint", "value": "Outreach clinics at Crawley, Brighton, Tunbridge Wells, Maidstone, Ashford + South London/Croydon"},
            {"label": "Mileage rate", "value": "AfC Section 17: 56p/mile up to 3,500 then 20p; HMRC AMAP 45p/25p reference"},
            {"label": "Heritage", "value": "WWII Guinea Pig Club — McIndoe burns reconstruction unit; long-standing supra-regional reputation"},
            {"label": "Delivery body", "value": "QVH workforce (own cars + claims) + small pool fleet + commercial fleet leasing"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (burns + reconstructive + head-and-neck) + NHSE Net Zero + DHSC + Sussex ICB"},
            {"label": "Funding trajectory", "value": "Stable around £0.25-0.30M; April 2025 employer-NIC step-up indirect; outreach-clinic expansion under ICS networks may grow line"},
            {"label": "Evaluation evidence", "value": "QVH ARA; CQC provider profile (RPC) — rated Outstanding; British Burn Association data; specialised commissioning service spec"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy outreach-mileage arrangements pre-2010 · Successor: NHSE Net Zero EV-fleet 2030 + ICS-network outreach reconfiguration"}
        ],
        "notes": "QVH is unusual among NHS trusts for its supra-regional reach despite being a small organisation — its outreach-clinic model is core to making tertiary specialist surgery accessible across the South East, which makes business-mileage to peripheral clinics a structural cost rather than a discretionary one. The £0.29M is modest in absolute terms but materially supports c. 80,000 outpatient attendances/yr by allowing surgeons to travel rather than every patient travelling to East Grinstead. Drivers include AfC Section 17 mileage rates, NHSE Net Zero pressure to electrify fleet, ICS-network outreach growth, and the post-pandemic recovery of plastic-surgery elective demand. Politically sensitive given staff retention link.",
        "sources": [
            {"publisher": "Queen Victoria Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qvh.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "Queen Victoria Hospital NHS Foundation Trust provider profile (RPC)", "url": "https://www.cqc.org.uk/provider/RPC"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — reimbursement of travel costs", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "NHS England", "title": "Specialised commissioning — burns and reconstructive surgery service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS England", "title": "Delivering a 'Net Zero' National Health Service", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"},
            {"publisher": "HM Revenue and Customs", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"}
        ],
        "related": ["Queen Victoria Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — The Walton Centre NHS Foundation Trust", "Transport (business + patient) — Liverpool Heart and Chest Hospital NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Bridgewater Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Bridgewater Community Healthcare NHS Foundation Trust"}],
        "description": "Bridgewater's £0.29M transport line covers business mileage paid to community staff under AfC Section 17 + AMAP rates plus pool-fleet vehicle leases for the district-nursing, health-visiting, school-nursing and MSK-community-physio workforce travelling between patients' homes and clinics across Halton, St Helens and Warrington. Community trusts run high mileage per WTE because care is delivered in patients' homes rather than central hospital sites, making this line structural to operations.",
        "beneficiaries": "Serves c. 360,000 residents across Halton, St Helens and Warrington (plus pockets of Wigan/Bolton via specialist services); c. 1,800 WTE deliver c. 850,000 community contacts/yr from c. 60 community sites; high per-WTE business mileage characteristic of community-trust model.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility · AfC Section 17 + HMRC AMAP rates · IFRS 16 (pool fleet) · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£0.29M"},
            {"label": "Trust profile", "value": "Standalone community FT — district nursing, HVs, school nursing, MSK community physio, dental access, end-of-life community"},
            {"label": "Footprint", "value": "Halton, St Helens, Warrington (+ specialist services into Wigan/Bolton)"},
            {"label": "Population served", "value": "c. 360,000 residents in core boroughs"},
            {"label": "Annual activity", "value": "c. 850,000 community contacts/yr (district nursing + HVs + school nursing + MSK)"},
            {"label": "Workforce", "value": "c. 1,800 WTE — district nurses, HVs, school nurses, AHPs, MSK physios"},
            {"label": "Mileage rate", "value": "AfC Section 17: 56p/mile up to 3,500 miles then 20p; HMRC AMAP 45p/25p reference"},
            {"label": "Travel pattern", "value": "Home-to-home district-nursing rounds + clinic outreach + school visits — high per-WTE mileage typical of community-trust model"},
            {"label": "Delivery body", "value": "Bridgewater workforce (own cars, claim mileage) + small pool fleet + commercial fleet leasing"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire & Merseyside ICB + NHSE Net Zero (fleet electrification)"},
            {"label": "Funding trajectory", "value": "Stable around £0.25-0.30M; April 2025 employer-NIC step-up indirect via supplier overhead; Three Shifts (Darzi Sep 2024) likely to grow line as activity shifts to community"},
            {"label": "Evaluation evidence", "value": "Bridgewater ARA; CQC provider profile (RY2) — rated Good; ERIC 2023-24; NHSE community-services dataset (CSDS)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-provider arm transport · Successor: NHSE Net Zero EV-fleet 2030 + Three Shifts community uplift"}
        ],
        "notes": "Community trusts have a structurally different transport profile from acute hospitals: care is delivered in patients' homes, so business mileage and pool-fleet leases are core operational costs not discretionary. Bridgewater's £0.29M reflects c. 1,800 WTE largely claiming AfC Section 17 mileage in their own cars, with a smaller pool fleet for shared assets like community-equipment delivery. Drivers include the AfC Section 17 mileage rate (last reviewed 2024 with no inflation uplift), NHSE Net Zero fleet-electrification pressure, the Three Shifts community direction (Darzi Sep 2024) which structurally grows visit volume, and the high cost of fleet vehicle leasing post-IFRS 16. Politically sensitive given staff retention.",
        "sources": [
            {"publisher": "Bridgewater Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bridgewater.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Bridgewater Community Healthcare NHS Foundation Trust provider profile (RY2)", "url": "https://www.cqc.org.uk/provider/RY2"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — reimbursement of travel costs", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "NHS England", "title": "Delivering a 'Net Zero' National Health Service", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "HM Revenue and Customs", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"}
        ],
        "related": ["Bridgewater Community Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Transport (business + patient) — Hounslow and Richmond Community Healthcare NHS Trust", "Transport (business + patient) — Sussex Community NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — Norfolk Community Health and Care NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Norfolk Community Health and Care NHS Trust"}],
        "description": "NCH&C's £0.29M amortisation charge represents systematic write-down of intangible assets under IAS 38 — predominantly software licences and capitalised software development covering the Trust's community electronic patient record stack (SystmOne / Rio for community services), capitalised development on the Norfolk & Waveney shared-care record, mobile working platforms enabling district nurses' caseload management on the move, and licence costs for the Trust's clinical-system suite supporting community-hospital and out-of-hospital workflows.",
        "beneficiaries": "NCH&C provides community nursing, community hospitals, end-of-life care, MSK and rehabilitation across the c. 1.0M Norfolk population; runs community hospitals at Norwich (Norwich Community), North Walsham, Cromer, Dereham, Swaffham, Kelling Hospital + minor injury units; c. 2,500 WTE.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.29M"},
            {"label": "Trust profile", "value": "Standalone community trust serving Norfolk; runs community hospitals + MIU + community nursing"},
            {"label": "Footprint", "value": "Whole of Norfolk; community hospitals at Norwich, North Walsham, Cromer, Dereham, Swaffham, Kelling + MIUs + clinics"},
            {"label": "Population served", "value": "c. 1.0M Norfolk residents"},
            {"label": "Annual activity", "value": "c. 1.5M community contacts/yr; community-hospital bed-days; MIU attendances; end-of-life and rehab caseload"},
            {"label": "Workforce", "value": "c. 2,500 WTE — district nurses, community matrons, AHPs, community physios, end-of-life teams"},
            {"label": "Intangibles class", "value": "EPR licences (SystmOne / Rio), capitalised software development (mobile working + ICS shared-care), clinical-system suite licences"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; long-life clinical EPR straight-lined over service life"},
            {"label": "Delivery body", "value": "NCH&C IT/Digital + Norfolk & Waveney ICB digital programme + EPR vendors (TPP / Servelec / Civica)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Norfolk & Waveney ICB + NHSE Frontline Digitisation"},
            {"label": "Funding trajectory", "value": "Stable around £0.25-0.30M; modest growth as Frontline Digitisation capital matures into in-service intangibles"},
            {"label": "Evaluation evidence", "value": "NCH&C ARA; CQC provider profile (RY3) — rated Outstanding; NHSE community-services dataset (CSDS); digital maturity assessment"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-provider arm clinical systems · Successor: Norfolk & Waveney shared-care record + Frontline Digitisation 2025-30"}
        ],
        "notes": "NCH&C is one of England's CQC-Outstanding community trusts and runs an unusually broad community-hospital footprint for a community-only provider, giving it a relatively complex digital-systems estate. Amortisation is small and steady at c. £0.29M and reflects the long-tail of software licences plus capitalised development for mobile-working platforms and shared-care-record contributions. Drivers include NHSE Frontline Digitisation capital flowing through to in-service intangibles, the Norfolk & Waveney ICS shared-care record build-out, and the Three Shifts community direction (Darzi Sep 2024) which intensifies the case for digital-enabled out-of-hospital care delivery. Trajectory is modest growth.",
        "sources": [
            {"publisher": "Norfolk Community Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.norfolkcommunityhealthandcare.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Norfolk Community Health and Care NHS Trust provider profile (RY3)", "url": "https://www.cqc.org.uk/provider/RY3"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Norfolk & Waveney ICB", "title": "Integrated Care System publications", "url": "https://improvinglivesnw.org.uk/"}
        ],
        "related": ["Norfolk Community Health and Care NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Sussex Community NHS Foundation Trust", "Amortisation — Central London Community Healthcare NHS Trust", "NHS England"]
    },
    "Amortisation — The Walton Centre NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Walton Centre NHS Foundation Trust"}],
        "description": "The Walton Centre's £0.27M amortisation charge represents systematic write-down of intangible assets under IAS 38 — predominantly software licences and capitalised software development covering the Trust's electronic patient record, neuroscience-specific imaging-PACS integration, the Cheshire & Merseyside neurosciences network platform, capitalised development on neurology-trial platforms and research data systems, and operational software supporting neurosurgery scheduling. As a single-specialty tertiary neurosciences centre, intangibles are concentrated in clinical-system licences rather than enterprise software.",
        "beneficiaries": "The Walton Centre at Aintree, Liverpool is the only standalone neurology + neurosurgery NHS trust in England; serves a c. 3.5M Cheshire, Merseyside, Lancashire, Isle of Man and parts of N Wales referral catchment; c. 1,800 WTE delivering neurology, neurosurgery, neurorehab, neuropsychology and pain services with c. 14,000 inpatient/day-case episodes/yr.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.27M"},
            {"label": "Trust profile", "value": "Only standalone neurology + neurosurgery NHS Trust in England; Aintree, Liverpool campus + outreach"},
            {"label": "Catchment", "value": "c. 3.5M referral catchment — Cheshire, Merseyside, Lancashire, Isle of Man, parts of N Wales"},
            {"label": "Annual activity", "value": "c. 14,000 inpatient/day-case episodes; c. 60,000+ outpatient attendances; c. 4,000 neurosurgical procedures"},
            {"label": "Workforce", "value": "c. 1,800 WTE — neurosurgeons, neurologists, AHPs, neuro-rehab teams, ITU"},
            {"label": "Intangibles class", "value": "EPR licences, neuroscience-PACS integration, neurology-trial platform development, surgical-scheduling software"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; long-life specialist clinical platforms straight-lined over service life"},
            {"label": "Delivery body", "value": "Walton Centre IT/Digital + Cheshire & Merseyside ICB digital programme + EPR/PACS vendors"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (neurosciences network) + Cheshire & Merseyside ICB + DHSC + NHSE Frontline Digitisation"},
            {"label": "Funding trajectory", "value": "Stable around £0.25-0.30M; modest growth as Frontline Digitisation capital crystallises + neurosciences-network capital flows"},
            {"label": "Evaluation evidence", "value": "Walton Centre ARA; CQC provider profile (RET) — rated Outstanding; NHSE neurosciences operational delivery network reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1992 Walton Hospital legacy systems · Successor: Frontline Digitisation 2025-30 EPR uplift + neuro-imaging AI integration"}
        ],
        "notes": "The Walton Centre is unique in England — the only standalone NHS Foundation Trust dedicated solely to neurology and neurosurgery. Its intangibles base is small and concentrated in clinical-system licences, neuroscience-imaging integration with PACS, and capitalised development supporting the supra-regional Cheshire & Merseyside neurosciences operational delivery network. Drivers include NHSE Frontline Digitisation capital flowing through to in-service intangibles, integration of AI-enabled imaging tools into the neuro-radiology workflow, and ongoing investment in neurology-clinical-trial platforms. The line is unlikely to grow materially absent a step-change in EPR/PACS strategy.",
        "sources": [
            {"publisher": "The Walton Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thewaltoncentre.nhs.uk/about-us/publications.htm"},
            {"publisher": "Care Quality Commission", "title": "The Walton Centre NHS Foundation Trust provider profile (RET)", "url": "https://www.cqc.org.uk/provider/RET"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — neurosciences service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["The Walton Centre NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Amortisation — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "Amortisation — The Royal Marsden NHS Foundation Trust", "NHS England"]
    },
    "Lease expenditure — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "RJAH's £0.27M residual lease expenditure covers IFRS 16 short-term and low-value-exemption leases plus equipment agreements — small outreach-clinic rooms used for orthopaedic and spinal outpatient outreach across Shropshire, Mid-Wales and the West Midlands, photocopier/MFD contracts, and pool-fleet vehicles supporting consultant outreach travel. The Trust's main 167-bed Gobowen campus is owned freehold so doesn't generate a lease cost; this line captures only the de-minimis tail.",
        "beneficiaries": "Tertiary orthopaedic and spinal centre serving a c. 3M Shropshire, Mid-Wales and West Midlands referral catchment from a single Gobowen campus + outreach; c. 7,500 elective inpatient/day-case episodes/yr + c. 75,000 outpatient attendances + Midlands Centre for Spinal Injuries; c. 1,800 WTE.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.27M"},
            {"label": "Trust profile", "value": "Specialist orthopaedic + spinal tertiary centre — single Gobowen campus near Oswestry; freehold main estate"},
            {"label": "Catchment", "value": "c. 3M referral catchment — Shropshire, Mid + N Wales, West Midlands; supra-regional spinal injuries"},
            {"label": "Estate", "value": "Single 167-bed Gobowen campus (freehold) + small outreach clinic rooms in DGHs and community settings"},
            {"label": "Annual activity", "value": "c. 7,500 elective inpatient + day-case episodes; c. 75,000 outpatient attendances"},
            {"label": "Workforce", "value": "c. 1,800 WTE — orthopaedic surgeons, AHPs, theatre teams, spinal-injury nursing"},
            {"label": "Lease composition", "value": "Outreach clinic rooms in partner DGHs, photocopier/MFD, pool-fleet vehicles for consultant outreach — IFRS 16 short-term/low-value tail"},
            {"label": "IFRS 16 driver", "value": "April 2022 transition — main estate is freehold so no big balance-sheet jump; this residual is short-term + low-value exemption tail"},
            {"label": "Delivery body", "value": "RJAH Estates & Facilities + commercial leasing (vehicles + MFD) + outreach-host DGH facilities"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (spinal injuries + complex spine) + Shropshire ICB + DHSC + NHSPS"},
            {"label": "Funding trajectory", "value": "Stable c. £0.25-0.30M; minimal growth pressure absent change in outreach-clinic strategy"},
            {"label": "Evaluation evidence", "value": "RJAH ARA; CQC provider profile (RL1) — rated Good/Outstanding; ERIC 2023-24 estate footprint"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease P&L · Successor: Three Shifts may grow community-orthopaedic outreach footprint marginally"}
        ],
        "notes": "RJAH is unusual among tertiary specialist trusts in owning its main campus freehold (founded as the Florence Treloar orthopaedic hospital and substantially developed pre-NHS), giving it relative structural stability and a small lease line. The £0.27M reflects the IFRS 16 residual tail covering outreach-clinic rooms, equipment leases, and pool-fleet vehicles. Drivers include the post-IFRS 16 short-term/low-value classification regime, GIRFT-driven orthopaedic productivity work that could expand outreach-clinic strategy modestly, and the fixed nature of the Welsh-Marches catchment. Politically the Welsh-side referrals make Welsh Government a co-payer but commissioning sits with Shropshire ICB.",
        "sources": [
            {"publisher": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rjah.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "RJAH Orthopaedic Hospital NHS Foundation Trust provider profile (RL1)", "url": "https://www.cqc.org.uk/provider/RL1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "Getting It Right First Time (GIRFT)", "title": "Orthopaedic and spinal national reports", "url": "https://gettingitrightfirsttime.co.uk/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — spinal services service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Lease expenditure — The Royal Orthopaedic Hospital NHS Foundation Trust", "Lease expenditure — The Walton Centre NHS Foundation Trust", "NHS Property Services"]
    },
    "Termination & post-employment — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "London Ambulance Service NHS Trust"}],
        "description": "LAS's £0.27M termination & post-employment line covers IAS 19 termination benefits and post-employment costs accrued during 2024-25 — voluntary and compulsory severance payments to leavers under the Public Sector Exit Payments Regulations 2020 (£95k cap), redundancy provisions linked to back-office restructuring, ill-health early retirement contributions, and Mutually Agreed Resignation Scheme (MARS) settlements where used. The line excludes the ongoing NHS Pension Scheme employer contributions (which sit elsewhere in staff costs).",
        "beneficiaries": "LAS is the world's busiest single-payer ambulance service, serving Greater London's c. 9.0M residents + commuters; c. 8,000 WTE paramedics, EMTs, call-handlers, dispatchers; c. 2.0M emergency calls + c. 1.2M incidents/yr; c. 70 ambulance stations + 2 emergency operations centres (Waterloo + Bow).",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme regulations · Public Sector Exit Payments Regulations 2020 (£95k cap) · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.27M"},
            {"label": "Trust profile", "value": "London regional ambulance service — Cat 1/2 emergency response + 111 IUC integration"},
            {"label": "Population served", "value": "c. 9.0M Greater London residents + c. 1M+ commuters"},
            {"label": "Annual activity", "value": "c. 2.0M emergency 999 calls; c. 1.2M ambulance incidents; c. 80,000 Cat-1 (life-threatening) calls"},
            {"label": "Workforce", "value": "c. 8,000 WTE — paramedics, EMTs, call-handlers, dispatchers, support"},
            {"label": "Estate", "value": "c. 70 ambulance stations + 2 EOCs (Waterloo HQ + Bow); Make Ready Centres"},
            {"label": "Termination scope", "value": "Voluntary/compulsory severance, redundancy provisions, ill-health early retirement contributions, MARS settlements"},
            {"label": "Public-sector cap", "value": "Public Sector Exit Payments Regulations 2020 — £95k cap on aggregate exit payments per individual"},
            {"label": "Delivery body", "value": "LAS HR + NHS Pensions Agency (BSA) + NHS Resolution (occasional injury benefit interaction)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury + NHSE Provider Finance + NHS Business Services Authority (Pensions)"},
            {"label": "Funding trajectory", "value": "Variable year-on-year — driven by restructuring decisions; backfill from 2023-24 industrial action settlements + post-pandemic operational reset"},
            {"label": "Evaluation evidence", "value": "LAS ARA; CQC provider profile (RRU); NHSE ambulance ARP performance dashboard; NAO ambulance system reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 uncapped exit payments · Successor: Cat-2 mean-response-time renewed focus + paramedic-progression workforce strategy"}
        ],
        "notes": "Termination & post-employment is a volatile line that swings year on year with restructuring decisions and ill-health retirement volume. LAS's £0.27M is modest in the context of c. 8,000 WTE and reflects a relatively quiet year for restructuring — much smaller than years when major back-office reorganisations or operational reconfiguration drove higher exit-payment provisions. Drivers include the Public Sector Exit Payments Regulations 2020 £95k cap (which constrains individual settlements), the post-pandemic London operational reset, and the legacy of 2023-24 paramedic industrial action which has shifted some staff retention dynamics. Politically scrutinised under PAC + NAO oversight given exit-payment sensitivities.",
        "sources": [
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "London Ambulance Service NHS Trust provider profile (RRU)", "url": "https://www.cqc.org.uk/provider/RRU"},
            {"publisher": "UK Government (legislation.gov.uk)", "title": "Public Sector Exit Payments Regulations 2020", "url": "https://www.legislation.gov.uk/uksi/2020/1122/contents/made"},
            {"publisher": "IFRS Foundation", "title": "IAS 19 Employee Benefits", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-19-employee-benefits/"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
            {"publisher": "National Audit Office", "title": "NHS ambulance services", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"}
        ],
        "related": ["London Ambulance Service NHS Trust", "Staff Costs", "NHS Ambulance Trusts", "Termination & post-employment — Yorkshire Ambulance Service NHS Trust", "Termination & post-employment — Norfolk Community Health and Care NHS Trust", "NHS Business Services Authority"]
    },
    "Lease expenditure — Gloucestershire Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Gloucestershire Health and Care NHS Foundation Trust"}],
        "description": "GHC's £0.26M residual lease expenditure covers IFRS 16 short-term and low-value-exemption leases plus equipment agreements — small satellite-clinic rooms, GP-shared rooms, photocopier/MFD contracts, and pool-fleet vehicles supporting the combined community + mental health workforce across Gloucestershire. The bulk of GHC's main estate (community hospitals at Cirencester, Stroud, Tewkesbury, Dilke, Lydney, North Cotswolds, Vale + mental health inpatient units) sits in NHSPS-leased premises whose cost flows through the Premises line.",
        "beneficiaries": "GHC is a combined community + mental health trust formed 2019 by the merger of 2gether NHSFT and Gloucestershire Care Services; serves c. 670,000 Gloucestershire residents from c. 70 sites including community hospitals + mental health inpatient units; delivers c. 1.6M community + mental health contacts/yr via c. 5,500 WTE.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 (operational interaction)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.26M"},
            {"label": "Trust profile", "value": "Combined community + mental health FT (formed 2019 by merger of 2gether NHSFT + Gloucestershire Care Services)"},
            {"label": "Footprint", "value": "Whole of Gloucestershire; c. 70 sites incl. community hospitals + mental health inpatient units + clinics + CMHTs"},
            {"label": "Population served", "value": "c. 670,000 Gloucestershire residents"},
            {"label": "Annual activity", "value": "c. 1.6M community + mental health contacts/yr; community hospital bed-days; CAMHS, IAPT/Talking Therapies, ED, LD"},
            {"label": "Workforce", "value": "c. 5,500 WTE — district nurses, community physios, MH nurses, psychiatrists, psychologists"},
            {"label": "Lease composition", "value": "GP-shared rooms, photocopier/MFD, satellite-clinic short lets, pool-fleet vehicles below IFRS 16 capitalisation threshold"},
            {"label": "IFRS 16 driver", "value": "April 2022 transition put main NHSPS estate on balance sheet; this residual is short-term + low-value exemption tail"},
            {"label": "Delivery body", "value": "GHC Estates & Facilities + NHS Property Services (main estate) + commercial leasing for fleet + MFD"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + One Gloucestershire ICB + NHSPS"},
            {"label": "Funding trajectory", "value": "Stable c. £0.25M; Three Shifts (Darzi Sep 2024) may grow community-clinic footprint; mental health investment standard pressure"},
            {"label": "Evaluation evidence", "value": "GHC ARA; CQC provider profile (RTQ); ERIC 2023-24 estate footprint; Mental Health Act monitoring"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate 2gether + GCS leases · Successor: Three Shifts community uplift + NHSPS estate optimisation"}
        ],
        "notes": "GHC's combined community-and-mental-health remit gives it a more complex estate than a pure community trust — mental health inpatient units, CMHTs, IAPT/Talking Therapies premises, community hospitals and traditional community-clinic rooms all need different lease arrangements. The £0.26M reflects the IFRS 16 residual after main estate moved on balance sheet in April 2022. Drivers include the IFRS 16 transition baseline, the Three Shifts community direction (Darzi Sep 2024) which may grow satellite-clinic footprint, the mental health investment standard which drives capital into MH community spaces, and ongoing NHSPS estate-optimisation reviews. Trajectory is broadly flat.",
        "sources": [
            {"publisher": "Gloucestershire Health and Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ghc.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Gloucestershire Health and Care NHS Foundation Trust provider profile (RTQ)", "url": "https://www.cqc.org.uk/provider/RTQ"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "NHS Property Services", "title": "Community estate and lease arrangements", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Gloucestershire Health and Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Derbyshire Community Health Services NHS Foundation Trust", "Lease expenditure — Hertfordshire Community NHS Trust", "NHS Property Services"]
    },
    "Transport (business + patient) — Liverpool Women's NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Liverpool Women's NHS Foundation Trust"}],
        "description": "Liverpool Women's £0.25M transport line covers business mileage paid to clinicians and outreach staff under AfC Section 17 + AMAP rates plus patient transport activity, including the supra-regional Cheshire & Merseyside Neonatal Transport Service (transferring sick babies between Level-3 NICU at LWH and partner hospitals), gynaecology and antenatal outreach travel, and pool-fleet vehicles for inter-site working between Crown Street and outreach clinics. The neonatal-transport flow is operationally critical even at modest absolute spend.",
        "beneficiaries": "England's only standalone women's hospital alongside Birmingham Women's; serves a c. 1.5M Cheshire & Merseyside catchment for tertiary obstetrics and gynaecology with c. 8,200 deliveries/yr, the Hewitt Fertility Centre (c. 4,000 cycles/yr), Level-3 NICU (c. 1,000 admissions/yr) and the Cheshire & Merseyside Neonatal Transport Service; c. 1,500 WTE on Crown Street + outreach.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility · AfC Section 17 + HMRC AMAP rates · IFRS 16 (pool fleet) · Health and Care Act 2022 · NHSE neonatal critical care service spec",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£0.25M"},
            {"label": "Trust profile", "value": "Standalone tertiary women's & neonatal hospital — only one of two in England (Crown Street, Liverpool L8)"},
            {"label": "Catchment", "value": "c. 1.5M Cheshire & Merseyside; tertiary obstetric + Level-3 NICU + gynae-oncology + fertility"},
            {"label": "Annual activity", "value": "c. 8,200 deliveries/yr; c. 1,000 NICU admissions; c. 50,000 outpatient attendances; Hewitt Fertility c. 4,000 cycles/yr"},
            {"label": "Workforce", "value": "c. 1,500 WTE — c. 230 medical + c. 700 nursing/midwifery + AHPs"},
            {"label": "Neonatal transport", "value": "Cheshire & Merseyside Neonatal Transport Service (CMNTS) — operates ambulance + neonatal-cot transfers from LWH NICU"},
            {"label": "Mileage rate", "value": "AfC Section 17: 56p/mile up to 3,500 then 20p; HMRC AMAP 45p/25p reference"},
            {"label": "Estate flow", "value": "Crown Street main hospital + Aintree-area outreach + community gynae clinics — pool fleet bridges sites"},
            {"label": "Delivery body", "value": "LWH workforce (own cars + claims) + small pool fleet + CMNTS specialist neonatal transport ambulance"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (Level-3 NICU + gynae-oncology) + Cheshire & Merseyside ICB + NWAS (transport partner) + DHSC"},
            {"label": "Funding trajectory", "value": "Stable c. £0.25M; April 2025 employer-NIC step-up indirect; long-deferred Liverpool Women's relocation business case could change line materially"},
            {"label": "Evaluation evidence", "value": "LWH ARA; CQC provider profile (REP); NHSE perinatal mortality reviews; HFEA Hewitt Fertility benchmarks; CMNTS performance data"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy outreach-mileage arrangements · Successor: NHSE Net Zero EV-fleet 2030 + Liverpool Women's relocation/co-location strategic outline case"}
        ],
        "notes": "Liverpool Women's transport profile is unusual — modest in absolute terms but operationally critical because of the supra-regional Cheshire & Merseyside Neonatal Transport Service which moves sick babies between LWH's Level-3 NICU and partner hospitals across the region. The £0.25M includes both routine business mileage and the specialist neonatal-cot/ambulance transport activity (some delivered in partnership with NWAS). Drivers include the CMNTS commissioning footprint, AfC Section 17 mileage rates, NHSE Net Zero pressure to electrify fleet, and the long-deferred LWH relocation/co-location business case. Politically sensitive given the unique standalone-women's-hospital status.",
        "sources": [
            {"publisher": "Liverpool Women's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.liverpoolwomens.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "Liverpool Women's NHS Foundation Trust provider profile (REP)", "url": "https://www.cqc.org.uk/provider/REP"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — reimbursement of travel costs", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "NHS England", "title": "Specialised commissioning — neonatal critical care service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS England", "title": "Delivering a 'Net Zero' National Health Service", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"},
            {"publisher": "HM Revenue and Customs", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"}
        ],
        "related": ["Liverpool Women's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — Great Ormond Street Hospital for Children NHS Foundation Trust", "Transport (business + patient) — Alder Hey Children's NHS Foundation Trust", "NHS England"]
    },
    "Termination & post-employment — Norfolk Community Health and Care NHS Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Norfolk Community Health and Care NHS Trust"}],
        "description": "NCH&C's £0.25M termination & post-employment line covers IAS 19 termination benefits and post-employment costs accrued during 2024-25 — voluntary and compulsory severance under the Public Sector Exit Payments Regulations 2020 £95k cap, redundancy provisions linked to back-office and pathway redesign, ill-health early retirement contributions, and Mutually Agreed Resignation Scheme (MARS) settlements where used. The line excludes ongoing NHS Pension Scheme employer contributions (which sit elsewhere in staff costs).",
        "beneficiaries": "NCH&C provides community nursing, community hospitals, end-of-life and rehabilitation services across the c. 1.0M Norfolk population; runs community hospitals at Norwich, North Walsham, Cromer, Dereham, Swaffham, Kelling + MIUs; c. 2,500 WTE delivering c. 1.5M community contacts/yr.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme regulations · Public Sector Exit Payments Regulations 2020 (£95k cap) · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.25M"},
            {"label": "Trust profile", "value": "Standalone community trust serving Norfolk; community hospitals + MIU + community nursing"},
            {"label": "Footprint", "value": "Whole of Norfolk; community hospitals at Norwich, North Walsham, Cromer, Dereham, Swaffham, Kelling"},
            {"label": "Population served", "value": "c. 1.0M Norfolk residents"},
            {"label": "Annual activity", "value": "c. 1.5M community contacts/yr; community-hospital bed-days; MIU attendances"},
            {"label": "Workforce", "value": "c. 2,500 WTE — district nurses, AHPs, community physios, community matrons, end-of-life teams"},
            {"label": "Termination scope", "value": "Voluntary/compulsory severance, redundancy provisions for pathway redesign, ill-health early retirement, MARS settlements"},
            {"label": "Public-sector cap", "value": "Public Sector Exit Payments Regulations 2020 — £95k cap on aggregate exit payments per individual"},
            {"label": "Delivery body", "value": "NCH&C HR + NHS Pensions Agency (NHSBSA) + NHS Resolution"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury + NHSE Provider Finance + NHS Business Services Authority + Norfolk & Waveney ICB"},
            {"label": "Funding trajectory", "value": "Variable year-on-year — driven by restructuring decisions; some exposure to ICS provider-collaborative reconfiguration; April 2025 employer-NIC step-up indirect"},
            {"label": "Evaluation evidence", "value": "NCH&C ARA; CQC provider profile (RY3) — rated Outstanding; ERIC 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 uncapped exit payments · Successor: ICS provider-collaborative integration with Norfolk acute providers"}
        ],
        "notes": "Termination & post-employment costs are inherently lumpy at community trusts of NCH&C's size — a single restructuring round can swing the line up or down by hundreds of thousands. The £0.25M reflects a moderate year of voluntary/compulsory severance plus ill-health retirement contributions. Drivers include the Public Sector Exit Payments Regulations 2020 £95k cap (constraining individual settlements), Norfolk & Waveney ICS provider-collaborative integration with the acute providers (which can drive back-office consolidation), and ongoing pathway-redesign work tying into the Three Shifts community direction (Darzi Sep 2024). Under PAC + NAO scrutiny on exit-payment governance.",
        "sources": [
            {"publisher": "Norfolk Community Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.norfolkcommunityhealthandcare.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Norfolk Community Health and Care NHS Trust provider profile (RY3)", "url": "https://www.cqc.org.uk/provider/RY3"},
            {"publisher": "UK Government (legislation.gov.uk)", "title": "Public Sector Exit Payments Regulations 2020", "url": "https://www.legislation.gov.uk/uksi/2020/1122/contents/made"},
            {"publisher": "IFRS Foundation", "title": "IAS 19 Employee Benefits", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-19-employee-benefits/"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Norfolk Community Health and Care NHS Trust", "Staff Costs", "NHS Community Trusts", "Termination & post-employment — Derbyshire Community Health Services NHS Foundation Trust", "Termination & post-employment — London Ambulance Service NHS Trust", "NHS Business Services Authority"]
    },
    "Business rates — Shropshire Community Health NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Shropshire Community Health NHS Trust"}],
        "description": "Shropshire Community's £0.24M business-rates line is non-domestic rates payable on the Trust's directly-occupied community estate across Shropshire and Telford & Wrekin — community hospitals at Bridgnorth, Whitchurch, Bishop's Castle, Ludlow + clinics, child development centres, podiatry sites and HQ — calculated by the Valuation Office Agency under the Local Government Finance Act 1988 (Sch 6) using rateable value × the appropriate multiplier. NHS trusts pay the full mandatory rate without charity relief in England.",
        "beneficiaries": "Provides community nursing, community hospitals, MIUs, MSK, podiatry, school nursing and community paediatrics across the c. 500,000 population of Shropshire, Telford & Wrekin; community hospitals at Bridgnorth, Whitchurch, Bishop's Castle, Ludlow + MIUs; c. 1,800 WTE.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 Revaluation · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.24M"},
            {"label": "Trust profile", "value": "Standalone community trust covering Shropshire + Telford & Wrekin"},
            {"label": "Footprint", "value": "Community hospitals at Bridgnorth, Whitchurch, Bishop's Castle, Ludlow + MIUs + clinics + child development centres"},
            {"label": "Population served", "value": "c. 500,000 (Shropshire c. 325k + Telford & Wrekin c. 180k)"},
            {"label": "Annual activity", "value": "c. 800,000 community contacts/yr; community-hospital bed-days; MIU attendances"},
            {"label": "Workforce", "value": "c. 1,800 WTE — district nurses, community matrons, AHPs, podiatrists, school nurses"},
            {"label": "Multiplier (24-25)", "value": "Standard non-domestic multiplier 54.6p/£ (England); small-business 49.9p/£; revaluation effective 1 April 2023"},
            {"label": "Charity relief", "value": "NHS trusts do NOT receive 80% mandatory charity relief; pay full assessed liability"},
            {"label": "Delivery body", "value": "Valuation Office Agency (assessment) + 2 billing authorities (Shropshire Council + Telford & Wrekin Council) + Trust Estates"},
            {"label": "Policy owner", "value": "DHSC + DLUHC/MHCLG (rates policy) + HM Treasury + Shropshire, Telford & Wrekin ICB"},
            {"label": "Funding trajectory", "value": "Revaluation 2023 step-change; multiplier indexed to CPI capped; 2026 revaluation upcoming"},
            {"label": "Evaluation evidence", "value": "Shropshire Community ARA; CQC provider profile (RY6); ERIC 2023-24 estate footprint"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 revaluation valuations · Successor: 2026 revaluation + Non-Domestic Rating Act 2024 reforms"}
        ],
        "notes": "Shropshire Community runs a relatively rural and dispersed estate of community hospitals and clinics, which means a meaningful directly-occupied footprint and therefore a non-trivial business-rates line. The £0.24M reflects rates on directly-occupied premises (NHSPS-leased premises pay rates separately via NHSPS). Drivers include the 1 April 2023 VOA revaluation (which generally moved rural Shropshire community-property rateable values modestly upward), the Non-Domestic Rating Act 2024 multiplier reforms, the upcoming 2026 revaluation, and ongoing local-government funding pressure on Shropshire Council which retains a share. Politically the Welsh-border catchment adds complexity for cross-border patients.",
        "sources": [
            {"publisher": "Shropshire Community Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.shropscommunityhealth.nhs.uk/about-us/publications"},
            {"publisher": "Care Quality Commission", "title": "Shropshire Community Health NHS Trust provider profile (RY6)", "url": "https://www.cqc.org.uk/provider/RY6"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government (legislation.gov.uk)", "title": "Local Government Finance Act 1988", "url": "https://www.legislation.gov.uk/ukpga/1988/41/contents"},
            {"publisher": "UK Government (legislation.gov.uk)", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/29/contents"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Shropshire Community Health NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Bridgewater Community Healthcare NHS Foundation Trust", "Business rates — Lincolnshire Community Health Services NHS Trust", "Valuation Office Agency"]
    },
    "Other & adjustments — The Royal Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "The Royal Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "ROH's £0.24M 'other & adjustments' line sits inside Staff Costs and captures residual employee-cost adjustments that don't fit cleanly into salaries, social security, pensions or termination — items such as apprenticeship-levy adjustments, pension reconciliation true-ups, NHS Pension Scheme contracted-out reconciliations, accruals/reversals for prior-period payroll items, and small ad-hoc workforce charges (recognition awards, long-service, restructuring residuals). The line is small but recurring and reflects the housekeeping side of NHS payroll accounting under IAS 19.",
        "beneficiaries": "ROH at Northfield, Birmingham is one of England's three specialist orthopaedic tertiary centres alongside RNOH Stanmore and RJAH Gobowen; serves a c. 5M+ West Midlands and supra-regional referral catchment for primary + revision joint replacement, oncology, paediatric and complex spine; c. 1,400 WTE; c. 6,500 elective inpatient/day-case episodes/yr.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme regulations · Apprenticeship Levy (Finance Act 2016) · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Other & adjustments 2024-25", "value": "£0.24M"},
            {"label": "Trust profile", "value": "Specialist orthopaedic tertiary centre — Northfield, Birmingham; primary + revision joint replacement, oncology, paediatric, complex spine"},
            {"label": "Catchment", "value": "c. 5M+ West Midlands referral catchment + supra-regional revision/oncology referrals"},
            {"label": "Annual activity", "value": "c. 6,500 elective inpatient/day-case episodes/yr; c. 50,000 outpatient attendances; high revision-arthroplasty share"},
            {"label": "Workforce", "value": "c. 1,400 WTE — orthopaedic surgeons, AHPs, theatre teams, oncology multidisciplinary team"},
            {"label": "Adjustment scope", "value": "Apprenticeship-levy true-up, pension reconciliation, prior-period payroll accruals, recognition + long-service awards"},
            {"label": "Apprenticeship levy", "value": "0.5% of paybill above £3M threshold (Finance Act 2016) — paid via PAYE; reconciliation runs through this line"},
            {"label": "Delivery body", "value": "ROH HR + Payroll + NHS Pensions Agency (NHSBSA) + HMRC apprenticeship-levy account"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury + NHSE Provider Finance + NHS Business Services Authority + NHSE Specialised Commissioning"},
            {"label": "Funding trajectory", "value": "Stable c. £0.2M; April 2025 employer-NIC step-up to 15% / £5k threshold flows through here partially via reconciliation"},
            {"label": "Evaluation evidence", "value": "ROH ARA; CQC provider profile (RRJ); National Joint Registry (NJR) data; GIRFT orthopaedic benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 paybill (no levy) · Successor: April 2025 employer-NIC step-up + ongoing GIRFT productivity workforce planning"}
        ],
        "notes": "ROH is one of the three remaining standalone NHS specialist orthopaedic centres (alongside RNOH Stanmore and RJAH Gobowen) and runs a high revision-arthroplasty case-mix that demands a relatively complex workforce composition. The 'other & adjustments' line is small and largely housekeeping — apprenticeship-levy reconciliation, pension true-ups under the McCloud remedy, and prior-period payroll accruals/reversals. Drivers include the post-2017 apprenticeship-levy regime, NHS Pension Scheme regulatory changes, the McCloud pensions remedy implementation 2023-25, and the April 2025 employer-NIC step-up to 15% / £5k threshold which will flow through reconciliation in this line.",
        "sources": [
            {"publisher": "The Royal Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.roh.nhs.uk/about-us/publications"},
            {"publisher": "Care Quality Commission", "title": "The Royal Orthopaedic Hospital NHS Foundation Trust provider profile (RRJ)", "url": "https://www.cqc.org.uk/provider/RRJ"},
            {"publisher": "IFRS Foundation", "title": "IAS 19 Employee Benefits", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-19-employee-benefits/"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme — McCloud remedy", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
            {"publisher": "HM Revenue and Customs", "title": "Apprenticeship levy", "url": "https://www.gov.uk/guidance/pay-apprenticeship-levy"},
            {"publisher": "Getting It Right First Time (GIRFT)", "title": "Orthopaedic national reports", "url": "https://gettingitrightfirsttime.co.uk/"}
        ],
        "related": ["The Royal Orthopaedic Hospital NHS Foundation Trust", "Staff Costs", "NHS Specialist Trusts", "Other & adjustments — The Clatterbridge Cancer Centre NHS Foundation Trust", "Other & adjustments — Cambridgeshire Community Services NHS Trust", "NHS Business Services Authority"]
    },
    "Business rates — Lincolnshire Community Health Services NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Lincolnshire Community Health Services NHS Trust"}],
        "description": "LCHS's £0.23M business-rates line is non-domestic rates payable on the Trust's directly-occupied community estate across the Lincolnshire footprint — community hospitals (Skegness, Louth, Spalding, Gainsborough, Stamford, Johnson), MIUs, clinics, podiatry sites and HQ — calculated by the Valuation Office Agency under the Local Government Finance Act 1988 (Sch 6) using rateable value × the appropriate multiplier. NHS trusts pay the full mandatory rate without charity relief in England, even on rural and dispersed community estates.",
        "beneficiaries": "LCHS provides community nursing, community hospitals, MIUs (incl. as the route into urgent care across rural coastal Lincolnshire), MSK, podiatry, school nursing and community paediatrics across the c. 770,000 Lincolnshire population; community hospitals at Skegness, Louth, Spalding, Gainsborough, Stamford, Johnson + MIUs; c. 2,200 WTE.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 Revaluation · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.23M (£226,864)"},
            {"label": "Trust profile", "value": "Standalone community trust covering Lincolnshire (rural + coastal); MIUs + community hospitals + community nursing"},
            {"label": "Footprint", "value": "Community hospitals at Skegness, Louth, Spalding, Gainsborough, Stamford, Johnson (Spalding) + MIUs + clinics"},
            {"label": "Population served", "value": "c. 770,000 Lincolnshire residents (England's fourth-largest county by area)"},
            {"label": "Annual activity", "value": "c. 1.2M community contacts/yr; community-hospital bed-days; c. 200,000 MIU attendances"},
            {"label": "Workforce", "value": "c. 2,200 WTE — district nurses, community matrons, AHPs, MIU nurses, community paediatricians"},
            {"label": "Multiplier (24-25)", "value": "Standard non-domestic multiplier 54.6p/£ (England); small-business 49.9p/£; revaluation effective 1 April 2023"},
            {"label": "Charity relief", "value": "NHS trusts do NOT receive 80% mandatory charity relief; pay full assessed liability"},
            {"label": "Delivery body", "value": "Valuation Office Agency (assessment) + Lincolnshire billing authorities (7 district councils + County) + LCHS Estates"},
            {"label": "Policy owner", "value": "DHSC + DLUHC/MHCLG (rates policy) + HM Treasury + Lincolnshire ICB"},
            {"label": "Funding trajectory", "value": "Revaluation 2023 step-change (rural Lincolnshire generally modest movement); multiplier indexed CPI capped; 2026 revaluation upcoming"},
            {"label": "Evaluation evidence", "value": "LCHS ARA; CQC provider profile (RY5); ERIC 2023-24 estate footprint; NHSE community-services dataset"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 revaluation valuations · Successor: 2026 revaluation + Non-Domestic Rating Act 2024 reforms + LCHS-Lincolnshire Partnership group strategy"}
        ],
        "notes": "Lincolnshire is England's fourth-largest county by area and one of the most rural and coastal regions, giving LCHS an unusually dispersed estate with multiple small community hospitals and MIUs that act as the route into urgent care for coastal towns far from the main acute providers. The £0.23M business-rates line reflects this dispersed directly-occupied footprint — NHSPS-leased premises pay rates separately via NHSPS. Drivers include the 1 April 2023 VOA revaluation, the Non-Domestic Rating Act 2024 multiplier reforms, the upcoming 2026 revaluation, and the strategic LCHS + Lincolnshire Partnership NHSFT group structure that may eventually lead to estate consolidation. Politically the rural-coastal access agenda makes any rates-driven site-closure debate sensitive.",
        "sources": [
            {"publisher": "Lincolnshire Community Health Services NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lincolnshirecommunityhealthservices.nhs.uk/about-us/publications"},
            {"publisher": "Care Quality Commission", "title": "Lincolnshire Community Health Services NHS Trust provider profile (RY5)", "url": "https://www.cqc.org.uk/provider/RY5"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government (legislation.gov.uk)", "title": "Local Government Finance Act 1988", "url": "https://www.legislation.gov.uk/ukpga/1988/41/contents"},
            {"publisher": "UK Government (legislation.gov.uk)", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/29/contents"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Lincolnshire Community Health Services NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Bridgewater Community Healthcare NHS Foundation Trust", "Business rates — Shropshire Community Health NHS Trust", "Valuation Office Agency"]
    },
}
