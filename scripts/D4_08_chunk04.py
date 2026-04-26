# -*- coding: utf-8 -*-
# D4_08 Impairments net of reversals — chunk 04 (17 NHS trusts)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Impairments net of reversals — North Tees and Hartlepool NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "North Tees and Hartlepool NHS Foundation Trust"}],
        "description": "Non-cash writedowns booked when MEA-DRC valuations of the trust's two-site estate — University Hospital of North Tees (Stockton, the principal acute, opened 1968) and University Hospital of Hartlepool (now mostly community/elective + day-case after reconfiguration) — fall below carrying value. The trust has been in successive 'new hospital' programmes since the abandoned 2007 Wynyard scheme, leaving carrying values held against rebuild expectations that have repeatedly slipped.",
        "beneficiaries": "Two acute sites covering c. 400,000 residents of Stockton, Hartlepool and east Durham; c. 5,500 staff; impairment hits the I&E reserve rather than cash but constrains capital headroom against the long-running NHP allocation.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£6.14M"},
            {"label": "Driver", "value": "MEA-DRC reassessment of 1968 North Tees envelope · NHP cohort timeline slippage post-Reset Jan 2025"},
            {"label": "Estate scale", "value": "UH North Tees (Stockton) ~580 beds + UH Hartlepool (community/elective)"},
            {"label": "Valuation cycle", "value": "5-yearly full revaluation by external valuer (Cushman & Wakefield panel) with VOA indexation in interim years"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list · pre-RAAC era 1968 concrete frame"},
            {"label": "NHP cohort", "value": "In NHP cohort — successor scheme to abandoned Wynyard · NHP Reset Jan 2025 confirmed but slipped beyond 2030"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £3.5M → 2023-24 c. £4.8M → 2024-25 £6.14M (rising as rebuild defers)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2007 abandoned Wynyard PFI · current: NHP rebuild · interim: backlog-maintenance capital"},
            {"label": "Backlog maintenance", "value": "ERIC 2023-24 high-risk backlog among north-east acutes · drives MEA-DRC haircut"},
            {"label": "Evaluation evidence", "value": "NAO 2023 NHP report flagged Reset cohort exposure · PAC NHP scrutiny 2024"},
            {"label": "Peer benchmark", "value": "Above north-east acute median impairment per bed · 1968 vintage premium"}
        ],
        "notes": "North Tees has been in successive rebuild programmes since the abandoned 2007 Wynyard PFI, and each deferral forces a fresh impairment review against the 1968 Stockton envelope's carrying value. The NHP Reset of January 2025 reaffirmed the trust in the cohort but slipped delivery beyond 2030, prolonging the impairment cycle. Backlog maintenance pressures (ERIC 2023-24 reported high-risk backlog) compound the MEA-DRC haircut. The 2024-25 figure reflects continued estate-condition deterioration ahead of any NHP construction start.",
        "sources": [
            {"publisher": "North Tees and Hartlepool NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nth.nhs.uk/about/publications/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "DHSC", "title": "New Hospital Programme Reset (January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"}
        ],
        "related": ["North Tees and Hartlepool NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — North Tees and Hartlepool NHS Foundation Trust", "Impairments net of reversals — County Durham and Darlington NHS Foundation Trust"]
    },
    "Impairments net of reversals — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Non-cash writedowns on Kingston's single-site Galsworthy Road acute estate (south-west London) when MEA-DRC reassessment falls below carrying value. The Edwardian-era core (Bernard Meade etc.) plus 1970s-80s ward blocks and the Sir William Rous oncology centre present mixed-vintage MEA-DRC exposure, with London Cost Multiplier indexation usually pushing values up but estate condition pulling them down.",
        "beneficiaries": "One acute site serving c. 350,000 residents of Kingston, Richmond, Merton and Wandsworth fringe; c. 4,000 staff; impairment is non-cash but reduces the revaluation reserve available to absorb future writedowns.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£5.92M"},
            {"label": "Driver", "value": "MEA-DRC reassessment on mixed-vintage Galsworthy Road site · London Cost Multiplier interaction"},
            {"label": "Estate scale", "value": "Kingston Hospital ~520 beds · Sir William Rous oncology · Hawks Road birth centre"},
            {"label": "Valuation cycle", "value": "5-yearly full revaluation · interim VOA indexation"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP cohort", "value": "Not in NHP cohort · capital recovery via SW London ICS allocations + ERIC backlog"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £3.0M → 2023-24 c. £4.5M → 2024-25 £5.92M (rising · ageing-block MEA-DRC haircut)"},
            {"label": "Group structure", "value": "Hospital Group with Hounslow & Richmond Community Healthcare since 2024 — first full reval cycle post-merger"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2024 standalone Kingston FT · Successor: integrated Kingston & Richmond NHS FT estate"},
            {"label": "Evaluation evidence", "value": "DHSC ARA disclosure · CQC Outstanding rating maintained 2023"},
            {"label": "Backlog maintenance", "value": "ERIC 2023-24 backlog c. £40M · weighted to high-risk Edwardian core"},
            {"label": "Peer benchmark", "value": "Above SW London single-site median impairment (mixed-vintage estate)"}
        ],
        "notes": "Kingston completed a hospital-group merger with Hounslow & Richmond Community Healthcare in 2024 (becoming Kingston and Richmond NHS FT in 2024-25 reporting), making this the first impairment cycle covering the combined estate. The Edwardian core blocks carry disproportionate MEA-DRC haircut against the modernised oncology and maternity facilities. Without an NHP slot, capital renewal flows through SW London ICS allocations and ERIC backlog bids, leaving impairment as the structural recognition mechanism for the deteriorating ward stock.",
        "sources": [
            {"publisher": "Kingston Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kingstonhospital.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "Kingston Hospital provider profile (RAX)", "url": "https://www.cqc.org.uk/provider/RAX"},
            {"publisher": "NHS England", "title": "Provider mergers and group structures guidance", "url": "https://www.england.nhs.uk/provider-mergers/"}
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Kingston Hospital NHS Foundation Trust", "Impairments net of reversals — Epsom and St Helier University Hospitals NHS Trust"]
    },
    "Impairments net of reversals — Buckinghamshire Healthcare NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Buckinghamshire Healthcare NHS Trust"}],
        "description": "Non-cash impairment of capital assets across Bucks Healthcare's two-acute estate — Stoke Mandeville Hospital (Aylesbury, the National Spinal Injuries Centre site) and Wycombe Hospital (High Wycombe, with the Heart Attack Centre) — plus Amersham Hospital and community sites. Stoke Mandeville carries confirmed RAAC plank exposure on the HSSIB September 2023 list, driving repeated MEA-DRC haircuts against carrying values held in expectation of remediation or rebuild.",
        "beneficiaries": "Two acute sites covering c. 550,000 Buckinghamshire residents plus the National Spinal Injuries Centre's UK-wide referral catchment of c. 2,500 patients/yr; c. 6,500 staff; impairment crystallises the cost gap between deteriorating fabric and a deferred remediation programme.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£5.75M"},
            {"label": "Driver", "value": "Stoke Mandeville RAAC plank impairment + MEA-DRC reassessment of mixed Wycombe estate"},
            {"label": "Estate scale", "value": "Stoke Mandeville (NSIC) ~530 beds + Wycombe Hospital + Amersham Hospital + community sites"},
            {"label": "RAAC status", "value": "Stoke Mandeville on HSSIB Sep 2023 confirmed-RAAC list · plank-mitigation programme ongoing"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "NHP cohort", "value": "Not in NHP RAAC priority sub-cohort · remediation funded via DHSC RAAC programme"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £2.5M → 2023-24 c. £4.0M → 2024-25 £5.75M (rising · post-HSSIB RAAC scope-up)"},
            {"label": "Specialty premium", "value": "National Spinal Injuries Centre · ligature-resistant + accessible-design assets carry specialist MEA-DRC"},
            {"label": "Net realisable value", "value": "Wycombe Cresswell building decommissioning carries NRV haircut"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2008 separate Stoke Mandeville and Wycombe trusts · Successor: BOB ICS estate strategy 2025-30"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC alert Sep 2023 · NAO RAAC report 2023 · DHSC RAAC programme tracking"},
            {"label": "Peer benchmark", "value": "Above acute median impairment (RAAC + spinal-specialty premium)"}
        ],
        "notes": "Stoke Mandeville's RAAC plank exposure has driven up impairments year-on-year as engineering surveys widen the affected scope and remediation timelines defer. The 2024-25 figure includes both RAAC-driven NRV writedowns and standard MEA-DRC cycle reassessment, with the National Spinal Injuries Centre's specialist-asset premium adding complexity to fair-value measurement. Wycombe's older Cresswell building decommissioning compounds the impairment line, and the trust sits outside the priority RAAC sub-cohort within the NHP, leaving remediation reliant on the separate DHSC RAAC programme.",
        "sources": [
            {"publisher": "Buckinghamshire Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.buckshealthcare.nhs.uk/about-us/publications/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC concrete safety alert (September 2023)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "National Audit Office", "title": "Managing the risk of RAAC in NHS estate (2023)", "url": "https://www.nao.org.uk/reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Buckinghamshire Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Buckinghamshire Healthcare NHS Trust", "Impairments net of reversals — Frimley Health NHS Foundation Trust"]
    },
    "Impairments net of reversals — South Central Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "South Central Ambulance Service NHS Foundation Trust"}],
        "description": "Non-cash writedowns dominated by ambulance fleet revaluation — Mercedes Sprinter and Fiat Ducato emergency-conversion stock with carrying values reset against falling residual values — plus ambulance station estate revaluation across Hampshire, Berkshire, Oxfordshire and Buckinghamshire. Unlike acute trusts, ambulance impairment is driven primarily by vehicle MEA-DRC and station-refresh cycles rather than building obsolescence.",
        "beneficiaries": "Fleet of c. 750 vehicles serving c. 7M residents across the four-county SCAS footprint plus NHS 111 contracts; c. 3,800 staff; impairment is non-cash but constrains the capital headroom for the rolling fleet-replacement programme.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£5.56M"},
            {"label": "Driver", "value": "Vehicle fleet MEA-DRC + station revaluation cycle · used-vehicle market price softening"},
            {"label": "Estate scale", "value": "c. 750 emergency + non-emergency vehicles · c. 35 ambulance stations + 5 hubs · Otterbourne HQ"},
            {"label": "Fleet refresh cycle", "value": "DCAs replaced ~7-yr cycle · MEA-DRC pegged to current Sprinter/Ducato conversion list price"},
            {"label": "Station vintage", "value": "Mixed — 1960s-2010s · several Make Ready hubs replacing legacy stations"},
            {"label": "RAAC status", "value": "Not on HSSIB confirmed-RAAC list (no acute building exposure)"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £3.0M → 2023-24 c. £4.5M → 2024-25 £5.56M (rising · used-vehicle softening)"},
            {"label": "NHP cohort", "value": "Not in NHP cohort (acute-only programme)"},
            {"label": "EV transition", "value": "Pilot EV rapid-response cars · ICE fleet impairment risk as 2035 phase-out approaches"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2006 merger Hampshire + Royal Berkshire + Oxfordshire + Bucks ambulance services · Successor: ARP10 fleet standard rollout"},
            {"label": "Evaluation evidence", "value": "DHSC ARA disclosure · CQC inspection findings on response times + fleet readiness"},
            {"label": "Peer benchmark", "value": "Mid-range vs ambulance-trust impairment per vehicle"}
        ],
        "notes": "SCAS's impairment line is structurally different from acute trusts — vehicle MEA-DRC dominates over building writedowns, with the line responding to used-vehicle market softening and emergency-conversion list-price moves rather than to RAAC, NHP or listed-building drivers. The 2024-25 uplift reflects post-pandemic fleet residual softening combined with station-refresh capital flowing to Make Ready hubs. The looming 2035 ICE phase-out creates a forward-looking impairment risk that valuers are starting to factor into MEA-DRC assumptions for late-cycle ICE stock.",
        "sources": [
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.scas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance Response Programme (ARP)", "url": "https://www.england.nhs.uk/urgent-emergency-care/improving-ambulance-services/arp/"},
            {"publisher": "Care Quality Commission", "title": "SCAS provider profile (RYE)", "url": "https://www.cqc.org.uk/provider/RYE"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE national reports", "url": "https://aace.org.uk/"}
        ],
        "related": ["South Central Ambulance Service NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Department of Health and Social Care", "Premises (other) — South Central Ambulance Service NHS Foundation Trust", "Impairments net of reversals — South East Coast Ambulance Service NHS Foundation Trust"]
    },
    "Impairments net of reversals — East Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "East Sussex Healthcare NHS Trust"}],
        "description": "Non-cash writedowns across ESHT's two-acute coastal estate — Conquest Hospital (Hastings, opened 1992) and Eastbourne District General Hospital (1970s build) — plus Bexhill, Rye and Crowborough community hospitals. The coastal exposure of both main sites carries a recognised salt-corrosion premium on cladding, MEP and roofing assets that compresses MEA-DRC reassessment cycles and accelerates impairment crystallisation against carrying values.",
        "beneficiaries": "Two acute sites covering c. 525,000 residents of east Sussex; c. 7,500 staff; impairment is non-cash but signals the gap between fabric condition on a corrosive-coastal estate and the carrying values held against future remediation.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£5.37M"},
            {"label": "Driver", "value": "Coastal salt-corrosion accelerated MEA-DRC haircut on Conquest + Eastbourne DGH"},
            {"label": "Estate scale", "value": "Conquest Hospital (Hastings) + Eastbourne DGH + Bexhill + Rye + Crowborough community"},
            {"label": "Coastal exposure", "value": "Both acutes within 1km of Channel coast · accelerated cladding/roof/MEP corrosion cycles"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation with coastal-site condition adjustment"},
            {"label": "NHP cohort", "value": "Not in NHP cohort · capital recovery via Sussex ICS allocations + ERIC backlog"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £2.8M → 2023-24 c. £4.2M → 2024-25 £5.37M (rising · coastal-corrosion + reconfig review)"},
            {"label": "Service reconfiguration", "value": "'Shaping Our Future' SOF reconfig review pending · creates carrying-value uncertainty on retained vs decommissioned wings"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2011 merger of East Sussex Hospitals + Sussex Community · Successor: Sussex ICS estate strategy"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection environment findings · NHSE Sussex acute review"},
            {"label": "Peer benchmark", "value": "Above south-coast peer median impairment per bed (corrosion premium)"}
        ],
        "notes": "ESHT carries the classic south-coast salt-corrosion impairment profile — Conquest and Eastbourne DGH both sit within a kilometre of the Channel and require shorter cladding/roof/MEP renewal cycles than inland peers, which valuers reflect through condition-adjusted MEA-DRC. The pending 'Shaping Our Future' reconfiguration review (which sites retain which acute services) adds carrying-value uncertainty: any wings flagged for decommissioning are vulnerable to NRV haircut. The 2024-25 figure reflects standard cycle reassessment plus reconfiguration-driven prudence.",
        "sources": [
            {"publisher": "East Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esht.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "ESHT provider profile (RXC)", "url": "https://www.cqc.org.uk/provider/RXC"},
            {"publisher": "NHS Sussex ICB", "title": "Sussex acute services strategy", "url": "https://www.sussex.ics.nhs.uk/"}
        ],
        "related": ["East Sussex Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — East Sussex Healthcare NHS Trust", "Impairments net of reversals — Royal Cornwall Hospitals NHS Trust"]
    },
    "Impairments net of reversals — Wrightington, Wigan and Leigh NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Wrightington, Wigan and Leigh NHS Foundation Trust"}],
        "description": "Non-cash writedowns across WWL's three-site estate — Royal Albert Edward Infirmary (Wigan, the principal acute), Leigh Infirmary (community + day-case) and Wrightington Hospital (the world-renowned John Charnley orthopaedic centre, where the cemented total hip replacement was developed in 1962). Wrightington's specialty heritage estate carries above-typical specialist-asset MEA-DRC, while the Wigan main site faces standard mixed-vintage building reassessment.",
        "beneficiaries": "c. 320,000 acute catchment for Wigan plus a national/international elective orthopaedic referral footprint at Wrightington (c. 6,000 joint replacements/yr); c. 5,000 staff; impairment is non-cash but constrains capital headroom against the trust's elective-recovery + ringfenced-orthopaedic-hub strategy.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£5.32M"},
            {"label": "Driver", "value": "MEA-DRC reassessment of Royal Albert Edward + Wrightington · specialist-asset valuation"},
            {"label": "Estate scale", "value": "Royal Albert Edward Infirmary ~570 beds + Leigh Infirmary + Wrightington Hospital (orthopaedic specialty)"},
            {"label": "Specialist asset", "value": "Wrightington listed as Charnley birthplace · ringfenced elective orthopaedic hub for Greater Manchester"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "NHP cohort", "value": "Not in NHP cohort · capital recovery via GM ICS allocations + national elective hub funding"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £2.5M → 2023-24 c. £4.0M → 2024-25 £5.32M (rising · cycle reassessment)"},
            {"label": "Elective hub designation", "value": "Wrightington designated GM elective surgical hub · MEA-DRC includes ringfenced theatres premium"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1993 trust formation merging Wigan + Wrightington · Successor: GM ICS elective hub strategy"},
            {"label": "Evaluation evidence", "value": "CQC inspection findings · GIRFT orthopaedic benchmarks (Wrightington top-decile) · ERIC backlog reporting"},
            {"label": "Peer benchmark", "value": "Mid-range vs north-west acute median · orthopaedic-specialty premium offsets non-specialty cycle"}
        ],
        "notes": "WWL's impairment line is structurally split between standard mixed-vintage building reassessment at the Royal Albert Edward Infirmary and specialist-asset valuation at Wrightington, where the orthopaedic-specialty ringfenced theatre estate carries above-typical MEA-DRC. The trust's designation as a Greater Manchester elective surgical hub (post-pandemic recovery) has reinforced the carrying value at Wrightington but exposes Wigan-side ageing wards to deeper haircut as backlog maintenance crystallises. The 2024-25 uplift reflects standard cycle reassessment.",
        "sources": [
            {"publisher": "Wrightington, Wigan and Leigh NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wwl.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Getting It Right First Time (GIRFT)", "title": "Orthopaedic GIRFT national report", "url": "https://gettingitrightfirsttime.co.uk/surgical_specialty/orthopaedic-surgery/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "WWL provider profile (RRF)", "url": "https://www.cqc.org.uk/provider/RRF"}
        ],
        "related": ["Wrightington, Wigan and Leigh NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Wrightington, Wigan and Leigh NHS Foundation Trust", "Impairments net of reversals — Bolton NHS Foundation Trust"]
    },
    "Impairments net of reversals — Royal Berkshire NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Royal Berkshire NHS Foundation Trust"}],
        "description": "Non-cash writedowns on the Royal Berkshire Hospital London Road site, Reading — a heritage-listed Victorian core (1839, Grade II listed) plus a 1980s/90s ward block accretion — with the additional complication of being in the New Hospital Programme cohort whose January 2025 Reset slipped delivery beyond the original 2030 commitment. Carrying values held in expectation of replacement face MEA-DRC and NRV haircut as the rebuild defers and the ageing fabric continues to deteriorate.",
        "beneficiaries": "Single major acute site serving c. 600,000 residents of Reading, west Berkshire and south Oxfordshire; c. 6,500 staff; impairment crystallises the carrying-value gap between deferred rebuild and live deterioration.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement · Listed Buildings and Conservation Areas Act 1990",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£5.06M"},
            {"label": "Driver", "value": "NHP Reset Jan 2025 deferral · listed-building Grade II core constraint · MEA-DRC haircut"},
            {"label": "Estate scale", "value": "Royal Berkshire Hospital ~700 beds · Bradbury Centre · West Berkshire Community Hospital · maternity"},
            {"label": "Listed-building constraint", "value": "1839 Grade II listed core blocks limit modernisation options · MEA constrained to 'modern equivalent within heritage envelope'"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP cohort", "value": "In NHP cohort · NHP Reset Jan 2025 confirmed but slipped delivery beyond 2030"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £2.0M → 2023-24 c. £3.5M → 2024-25 £5.06M (rising · NHP Reset crystallisation)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 Royal Berkshire & Battle Hospitals · Successor: NHP rebuild on London Road · Battle site already redeveloped"},
            {"label": "Evaluation evidence", "value": "NAO 2023 NHP report · PAC NHP scrutiny 2024 · DHSC NHP Reset Jan 2025"},
            {"label": "Backlog maintenance", "value": "ERIC 2023-24 high-risk backlog among Thames Valley acutes · listed-building works carry premium"},
            {"label": "Peer benchmark", "value": "Above Thames Valley acute median impairment per bed (heritage + NHP defer)"}
        ],
        "notes": "Royal Berkshire's impairment line is at the intersection of two structural drivers — the Grade II listed Victorian core constrains modernisation options, forcing MEA-DRC into a 'modern equivalent within heritage envelope' framing, and the NHP Reset of January 2025 deferred the planned replacement beyond 2030. Each year of slippage forces a fresh impairment review against carrying values held in expectation of the rebuild. The 2024-25 figure reflects post-Reset crystallisation of that gap, on top of standard cycle reassessment.",
        "sources": [
            {"publisher": "Royal Berkshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalberkshire.nhs.uk/about-us/publications/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "DHSC", "title": "New Hospital Programme Reset (January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Historic England", "title": "Royal Berkshire Hospital listing", "url": "https://historicengland.org.uk/listing/the-list/"}
        ],
        "related": ["Royal Berkshire NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Royal Berkshire NHS Foundation Trust", "Impairments net of reversals — Hampshire Hospitals NHS Foundation Trust"]
    },
    "Impairments net of reversals — Hampshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
        "description": "Non-cash writedowns on HHFT's three-acute estate — Basingstoke and North Hampshire Hospital (1974), Royal Hampshire County Hospital (Winchester, principal acute), and Andover War Memorial Hospital (community/day-case) — alongside an active 'Hampshire Together' service-reconfiguration with planned new-build at Junction 7 of M3 under the NHP. Both NHP confirmation and reconfiguration uncertainty interact with MEA-DRC reassessment.",
        "beneficiaries": "Three sites covering c. 600,000 residents of north and mid Hampshire; c. 9,000 staff; impairment is non-cash but reflects the carrying-value risk on assets earmarked for decommissioning under 'Hampshire Together'.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£4.52M"},
            {"label": "Driver", "value": "Reconfiguration carrying-value review (Hampshire Together) · MEA-DRC cycle on 1974 Basingstoke + Victorian Winchester core"},
            {"label": "Estate scale", "value": "Basingstoke ~450 beds + Royal Hampshire County (Winchester) ~530 beds + Andover WMH"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP cohort", "value": "In NHP cohort — Hampshire Together / Junction 7 site · Reset Jan 2025 confirmed cohort, slipped timeline"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £2.5M → 2023-24 c. £3.5M → 2024-25 £4.52M (rising · reconfig + cycle reassessment)"},
            {"label": "Reconfiguration", "value": "'Hampshire Together' planning: specialty consolidation between sites · creates wing-level NRV uncertainty"},
            {"label": "Listed-building", "value": "Royal Hampshire County Winchester core has heritage constraints"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2012 merger of Basingstoke + Winchester · Successor: NHP Junction 7 new-build (post-2030)"},
            {"label": "Evaluation evidence", "value": "NAO 2023 NHP report · PAC NHP scrutiny 2024 · NHSE Hampshire reconfiguration review"},
            {"label": "Peer benchmark", "value": "Mid-range vs Wessex acute median impairment (NHP-cohort premium)"}
        ],
        "notes": "Hampshire Hospitals' impairment carries a distinct reconfiguration overlay — 'Hampshire Together' is consolidating specialties between Basingstoke and Winchester ahead of the planned NHP new-build at M3 Junction 7, and any wing or specialty unit flagged for decommissioning is exposed to NRV haircut even before construction starts. The NHP Reset of January 2025 confirmed the cohort but slipped delivery, extending the period over which impairment crystallises against the existing fabric. The 2024-25 figure reflects this combined reconfig + cycle reassessment.",
        "sources": [
            {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hampshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "Hampshire Together", "title": "Hampshire Hospitals reconfiguration programme", "url": "https://www.hampshirehospitals.nhs.uk/hampshire-together/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "DHSC", "title": "New Hospital Programme Reset (January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Hampshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Hampshire Hospitals NHS Foundation Trust", "Impairments net of reversals — Royal Berkshire NHS Foundation Trust"]
    },
    "Impairments net of reversals — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "Non-cash writedowns across ASPH's two-site north-west Surrey estate — St Peter's Hospital (Chertsey, the principal acute, mostly 1980s/90s wards on a 1939 wartime emergency hospital footprint) and Ashford Hospital (community + planned-care). The trust sits in the New Hospital Programme cohort, with carrying values held against an expected rebuild that the January 2025 Reset deferred beyond 2030.",
        "beneficiaries": "Two sites covering c. 410,000 residents of north-west Surrey; c. 4,500 staff; impairment crystallises the gap between deteriorating fabric and the deferred NHP rebuild expectation.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£4.46M"},
            {"label": "Driver", "value": "NHP Reset Jan 2025 deferral · MEA-DRC cycle on 1939 emergency-hospital footprint at St Peter's"},
            {"label": "Estate scale", "value": "St Peter's Hospital (Chertsey) ~525 beds + Ashford Hospital (community/planned)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list (pre-RAAC era 1939 build)"},
            {"label": "NHP cohort", "value": "In NHP cohort · Reset Jan 2025 confirmed but slipped beyond 2030"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £2.0M → 2023-24 c. £3.2M → 2024-25 £4.46M (rising · NHP Reset crystallisation)"},
            {"label": "Site history", "value": "St Peter's built 1939 as wartime emergency hospital · structural-age premium on MEA-DRC"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1998 merger of Ashford + St Peter's · Successor: NHP rebuild on Chertsey site (post-2030)"},
            {"label": "Evaluation evidence", "value": "NAO 2023 NHP report · PAC NHP scrutiny 2024 · DHSC NHP Reset Jan 2025"},
            {"label": "Backlog maintenance", "value": "ERIC 2023-24 high-risk backlog reflecting wartime-era fabric"},
            {"label": "Peer benchmark", "value": "Above SE acute median impairment per bed (vintage + NHP defer)"}
        ],
        "notes": "ASPH carries a distinctive structural-age premium on its impairment line — the St Peter's Chertsey site sits on a 1939 wartime emergency-hospital footprint with 1980s/90s ward overlays, generating MEA-DRC haircut as valuers reflect the underlying age of services and structural envelope. The NHP Reset deferred the rebuild beyond 2030, prolonging the period over which impairment crystallises against fabric that the trust expected to replace. ERIC backlog data shows high-risk weighting consistent with this age profile.",
        "sources": [
            {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ashfordstpeters.nhs.uk/about-us/publications"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "DHSC", "title": "New Hospital Programme Reset (January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Ashford and St Peter's Hospitals NHS Foundation Trust", "Impairments net of reversals — Surrey And Sussex Healthcare NHS Trust"]
    },
    "Impairments net of reversals — The Shrewsbury and Telford Hospital NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
        "description": "Non-cash writedowns across SaTH's two-acute Shropshire estate — Royal Shrewsbury Hospital (RSH, 1977 build) and Princess Royal Hospital Telford (PRH, 1989) — the trust at the centre of the Ockenden maternity inquiry. SaTH is in the 'Hospitals Transformation Programme' (HTP) reconfiguration aligned to the New Hospital Programme, with planned specialty consolidation between RSH and PRH that creates wing-level NRV uncertainty alongside standard MEA-DRC cycle reassessment.",
        "beneficiaries": "Two acute sites serving c. 500,000 residents of Shropshire, Telford & Wrekin and mid-Wales; c. 5,500 staff; impairment is non-cash but reflects deteriorating mid-1970s/80s fabric against deferred reconfiguration carrying values.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£3.76M"},
            {"label": "Driver", "value": "Hospitals Transformation Programme reconfiguration carrying-value review · MEA-DRC cycle reassessment"},
            {"label": "Estate scale", "value": "Royal Shrewsbury Hospital ~590 beds + Princess Royal Telford ~415 beds + community sites"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP / HTP cohort", "value": "Hospitals Transformation Programme aligned to NHP · Reset Jan 2025 timeline confirmed but slipped"},
            {"label": "Reconfiguration", "value": "Planned specialty consolidation: emergency at RSH · planned care at PRH (long-debated, judicially reviewed)"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £1.5M → 2023-24 c. £2.8M → 2024-25 £3.76M (rising · HTP carrying-value review)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2003 trust formation · Successor: HTP reconfigured estate (post-2030)"},
            {"label": "Evaluation evidence", "value": "Ockenden Final Report 2022 · CQC Sec 31 · NAO 2023 NHP report · Future Fit programme history"},
            {"label": "Backlog maintenance", "value": "ERIC 2023-24 elevated backlog · maternity-driven environment investment"},
            {"label": "Peer benchmark", "value": "Above west-Midlands acute median impairment (HTP + Ockenden environment cycle)"}
        ],
        "notes": "SaTH's impairment line carries two distinctive overlays — the Hospitals Transformation Programme reconfiguration creates wing-level NRV uncertainty as services are earmarked for one site or the other, and the post-Ockenden environment-investment cycle (ligature-free maternity, secure birthing rooms, bereavement-suite separation) drives capital-and-operating turnover that interacts with carrying values. The 2024-25 figure reflects HTP carrying-value review on top of standard cycle reassessment, with NHP Reset slippage extending the impairment exposure window.",
        "sources": [
            {"publisher": "The Shrewsbury and Telford Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sath.nhs.uk/about-us/publications/"},
            {"publisher": "Ockenden Review", "title": "Final Ockenden Report (2022)", "url": "https://www.gov.uk/government/publications/final-report-of-the-ockenden-review"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — The Shrewsbury and Telford Hospital NHS Trust", "Impairments net of reversals — University Hospitals of North Midlands NHS Trust"]
    },
    "Impairments net of reversals — North West Ambulance Service NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "North West Ambulance Service NHS Trust"}],
        "description": "Non-cash writedowns dominated by ambulance fleet revaluation across NWAS's c. 1,100 vehicle estate — emergency Mercedes Sprinter and Fiat Ducato conversions plus rapid-response cars and PTS minibuses — with MEA-DRC pegged to current conversion list price and used-vehicle residuals. Station estate impairment covers c. 110 stations and Make Ready hubs across Cumbria, Lancashire, Greater Manchester, Merseyside and Cheshire, including legacy fire-shared and Co-responder estate.",
        "beneficiaries": "c. 1,100 vehicles serving c. 7M residents of the North West; c. 7,000 staff; impairment is non-cash but compresses capital headroom against the ARP-driven fleet-replacement cycle and Make Ready hub rollout.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£3.66M"},
            {"label": "Driver", "value": "Vehicle fleet MEA-DRC + station-estate cycle reassessment · used-vehicle market softening"},
            {"label": "Estate scale", "value": "c. 1,100 vehicles · c. 110 stations + Make Ready hubs · HQ at Ladybridge Hall (Bolton)"},
            {"label": "Fleet refresh cycle", "value": "DCAs replaced ~7-yr cycle · MEA-DRC pegged to current conversion list"},
            {"label": "Make Ready rollout", "value": "Centralised vehicle prep hubs replacing legacy station prep · station-NRV crystallisation"},
            {"label": "Co-responder estate", "value": "Legacy fire-shared and Co-responder stations carry mixed-tenure carrying values"},
            {"label": "RAAC status", "value": "Not on HSSIB confirmed-RAAC list"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £2.0M → 2023-24 c. £2.9M → 2024-25 £3.66M (rising · used-vehicle softening + Make Ready)"},
            {"label": "EV transition", "value": "Pilot EV rapid-response · ICE fleet impairment risk on 2035 phase-out trajectory"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2006 merger of Cumbria, Lancashire, GM, Mersey, Cheshire ambulance services · Successor: ARP10 fleet standard"},
            {"label": "Evaluation evidence", "value": "DHSC ARA disclosure · CQC inspection findings on response performance + fleet readiness"},
            {"label": "Peer benchmark", "value": "Above ambulance-trust median impairment per vehicle (Make Ready transition + station NRV)"}
        ],
        "notes": "NWAS's impairment line is shaped by two parallel transitions — Make Ready hub rollout that crystallises NRV haircut on legacy station estate as vehicle-prep activity centralises, and the long-tail ICE fleet revaluation pressure as used-vehicle markets soften and the 2035 phase-out comes into MEA-DRC sightlines. The 2024-25 figure reflects both effects on top of standard cycle reassessment, with mixed-tenure Co-responder and fire-shared stations adding carrying-value complexity that valuers must navigate annually.",
        "sources": [
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance Response Programme (ARP)", "url": "https://www.england.nhs.uk/urgent-emergency-care/improving-ambulance-services/arp/"},
            {"publisher": "Care Quality Commission", "title": "NWAS provider profile (RX7)", "url": "https://www.cqc.org.uk/provider/RX7"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE national reports", "url": "https://aace.org.uk/"}
        ],
        "related": ["North West Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Department of Health and Social Care", "Premises (other) — North West Ambulance Service NHS Trust", "Impairments net of reversals — South Central Ambulance Service NHS Foundation Trust"]
    },
    "Impairments net of reversals — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Non-cash writedowns on Stockport's single-site Stepping Hill Hospital estate — a Victorian-era core (1905 workhouse infirmary origin) overlaid with 1970s-2000s ward and theatre blocks — when MEA-DRC reassessment falls below carrying value. Stepping Hill has carried unusual scrutiny since the 2011 'saline' poisoning case (Victorino Chua) drove access-control and CCTV-related capital and operating works that interact with the building fabric's MEA assessment.",
        "beneficiaries": "Single acute site serving c. 350,000 residents of Stockport, Tameside fringe and High Peak Derbyshire; c. 5,000 staff; impairment is non-cash but flags the gap between ageing fabric and carrying values.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£3.41M"},
            {"label": "Driver", "value": "MEA-DRC reassessment on mixed Victorian + 1970s-2000s estate · backlog-condition haircut"},
            {"label": "Estate scale", "value": "Stepping Hill Hospital ~700 beds · single-site · community footprint"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP cohort", "value": "Not in NHP cohort · capital recovery via GM ICS allocations + ERIC backlog"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £1.5M → 2023-24 c. £2.5M → 2024-25 £3.41M (rising · cycle reassessment)"},
            {"label": "Site history", "value": "1905 workhouse infirmary core · sequential 1970s/80s/2000s overlays"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1993 Stockport DHA · Successor: GM ICS estate strategy"},
            {"label": "Evaluation evidence", "value": "CQC inspection findings · DHSC ARA disclosure · ERIC 2023-24 backlog reporting"},
            {"label": "Backlog maintenance", "value": "ERIC 2023-24 high-risk backlog among GM acutes"},
            {"label": "Peer benchmark", "value": "Mid-range vs GM single-site acute median impairment"}
        ],
        "notes": "Stockport's impairment reflects a textbook mixed-vintage single-site MEA-DRC profile — Victorian workhouse-era core blocks carry deep haircut, 1970s-80s overlays show structural-age decline and only the 2000s wings hold close to indexed carrying values. Without an NHP slot, capital renewal flows through GM ICS allocations and competitive ERIC backlog bids, leaving impairment as the structural recognition mechanism for the deteriorating ward stock. The 2024-25 figure reflects continued cycle reassessment as backlog crystallises.",
        "sources": [
            {"publisher": "Stockport NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stockport.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "Stockport NHS FT provider profile (RWJ)", "url": "https://www.cqc.org.uk/provider/RWJ"},
            {"publisher": "NHS Greater Manchester ICB", "title": "GM ICS estate strategy", "url": "https://gmintegratedcare.org.uk/"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Stockport NHS Foundation Trust", "Impairments net of reversals — Tameside and Glossop Integrated Care NHS Foundation Trust"]
    },
    "Impairments net of reversals — London North West University Healthcare NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "London North West University Healthcare NHS Trust"}],
        "description": "Non-cash writedowns across LNWH's three-site north-west London estate — Northwick Park Hospital (Harrow, principal acute, 1970s build), Central Middlesex Hospital (Park Royal, planned-care after A&E withdrawal), and Ealing Hospital (1970s build). Northwick Park's Brunel-era research provenance (Clinical Research Centre legacy) intersects with carrying-value reassessment, while the Ealing site has been under successive reconfiguration reviews, creating wing-level NRV exposure.",
        "beneficiaries": "Three acute sites covering c. 1M residents of Brent, Harrow and Ealing; c. 9,000 staff; impairment is non-cash but reflects deferred reconfiguration carrying-value crystallisation alongside MEA-DRC cycle reassessment.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£3.38M"},
            {"label": "Driver", "value": "Reconfiguration carrying-value review · MEA-DRC cycle on 1970s Northwick Park + Ealing"},
            {"label": "Estate scale", "value": "Northwick Park ~860 beds + Central Middlesex (planned-care) + Ealing Hospital · St Mark's specialty"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP cohort", "value": "Not in NHP cohort · capital recovery via NW London ICS + national elective hub funding"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · London Cost Multiplier interaction · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £2.0M → 2023-24 c. £2.7M → 2024-25 £3.38M (rising · cycle + reconfig)"},
            {"label": "Reconfiguration", "value": "Shaping a Healthier Future legacy: A&E withdrawal at Central Middlesex 2014 · Ealing inpatient downgrade ongoing"},
            {"label": "St Mark's specialty", "value": "St Mark's Hospital (national bowel-disease specialist) co-located at Northwick Park · specialty-asset MEA-DRC"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2014 merger of Ealing + North West London Hospitals · Successor: NW London ICS estate"},
            {"label": "Evaluation evidence", "value": "CQC inspection findings · NHSE NW London reconfiguration tracking"},
            {"label": "Peer benchmark", "value": "Mid-range vs outer-London acute median impairment (reconfig + Cost Multiplier offset)"}
        ],
        "notes": "LNWH's impairment line is shaped by the long unfinished business of the 'Shaping a Healthier Future' reconfiguration — A&E withdrew from Central Middlesex in 2014 but inpatient downgrade at Ealing has stretched on, creating successive carrying-value reviews on wings flagged for transition. Northwick Park's 1970s envelope plus the co-located St Mark's specialty bowel-disease unit add complexity to MEA-DRC, with the London Cost Multiplier partially offsetting condition-driven haircut. The 2024-25 figure reflects standard cycle reassessment plus reconfiguration prudence.",
        "sources": [
            {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lnwh.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "LNWH provider profile (R1K)", "url": "https://www.cqc.org.uk/provider/R1K"},
            {"publisher": "NHS North West London ICB", "title": "Shaping a Healthier Future legacy", "url": "https://www.nwlondonicb.nhs.uk/"}
        ],
        "related": ["London North West University Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — London North West University Healthcare NHS Trust", "Impairments net of reversals — Imperial College Healthcare NHS Trust"]
    },
    "Impairments net of reversals — Surrey And Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Surrey And Sussex Healthcare NHS Trust"}],
        "description": "Non-cash writedowns on SASH's principal East Surrey Hospital site (Redhill, mid-1980s build, with the Three Bridges PFI maternity wing 2009) plus Crawley Hospital and Caterham Dene community hospital. SASH operates a small acute-PFI overlay on top of an otherwise NHS-owned estate, creating mixed treatment between PFI-on-balance-sheet assets (IFRIC 12) and standard MEA-DRC carrying values for the rest of the estate.",
        "beneficiaries": "Single major acute site at Redhill plus Crawley + Caterham Dene serving c. 535,000 residents of east Surrey, west Sussex and east Hampshire fringe; c. 4,500 staff; impairment is non-cash but reduces revaluation reserve headroom.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement · IFRIC 12 Service Concession Arrangements",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£3.36M"},
            {"label": "Driver", "value": "MEA-DRC reassessment on 1980s East Surrey Hospital · IFRIC 12 PFI residual value review"},
            {"label": "Estate scale", "value": "East Surrey Hospital ~600 beds + Crawley Hospital + Caterham Dene"},
            {"label": "PFI overlay", "value": "Three Bridges PFI maternity wing (2009 unitary charge model) on East Surrey site · IFRIC 12 on balance sheet"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP cohort", "value": "Not in NHP cohort · capital recovery via Sussex/Surrey ICS allocations + ERIC backlog"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £1.8M → 2023-24 c. £2.6M → 2024-25 £3.36M (rising · cycle reassessment)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1998 merger Crawley + East Surrey · Successor: Sussex/Surrey ICS estate strategy"},
            {"label": "Evaluation evidence", "value": "CQC Outstanding rating maintained · DHSC ARA disclosure · ERIC 2023-24"},
            {"label": "Backlog maintenance", "value": "ERIC 2023-24 mid-range backlog · 1980s envelope MEP renewal"},
            {"label": "Peer benchmark", "value": "Mid-range vs SE acute median impairment per bed"}
        ],
        "notes": "SASH's impairment line carries a distinctive PFI overlay — the 2009 Three Bridges maternity wing is on balance sheet under IFRIC 12 and attracts its own residual-value review separate from the rest of the East Surrey estate, where standard MEA-DRC cycle reassessment applies. The 1980s envelope at Redhill is now reaching MEP renewal life-end, with ERIC backlog growth feeding through to MEA-DRC haircut. The trust's CQC Outstanding rating reflects clinical quality but does not insulate the building stock from cycle reassessment.",
        "sources": [
            {"publisher": "Surrey And Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.surreyandsussex.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 data (current contracts)", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2022-summary-data"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "SASH provider profile (RTP)", "url": "https://www.cqc.org.uk/provider/RTP"}
        ],
        "related": ["Surrey And Sussex Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Surrey And Sussex Healthcare NHS Trust", "Impairments net of reversals — Ashford and St Peter's Hospitals NHS Foundation Trust"]
    },
    "Impairments net of reversals — East Cheshire NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "East Cheshire NHS Trust"}],
        "description": "Non-cash writedowns on East Cheshire's small two-site estate — Macclesfield District General Hospital (the principal acute, 1971 build) and Congleton War Memorial Hospital (community), plus a community-services footprint across east Cheshire including Knutsford, Wilmslow and Bollington. The trust has been under successive 'service sustainability' reviews — including a 2018-19 Cheshire and Merseyside review of acute viability — that interact with the carrying value of the 1971 Macclesfield envelope.",
        "beneficiaries": "Single small acute (Macclesfield ~250 beds) plus community sites serving c. 200,000 residents of east Cheshire; c. 2,800 staff; impairment is non-cash but flags the carrying-value gap on a small acute facing repeated sustainability scrutiny.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£3.34M"},
            {"label": "Driver", "value": "MEA-DRC reassessment on 1971 Macclesfield DGH · sustainability-review carrying-value uncertainty"},
            {"label": "Estate scale", "value": "Macclesfield DGH ~250 beds + Congleton War Memorial + community sites"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list (pre-RAAC era 1971 build)"},
            {"label": "NHP cohort", "value": "Not in NHP cohort · capital recovery via C&M ICS allocations + ERIC backlog"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £1.5M → 2023-24 c. £2.4M → 2024-25 £3.34M (rising · cycle + sustainability review)"},
            {"label": "Sustainability reviews", "value": "Repeated C&M ICS reviews of small-acute viability · creates carrying-value uncertainty"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 East Cheshire NHS Trust · Successor: Cheshire & Merseyside ICS estate strategy"},
            {"label": "Evaluation evidence", "value": "CQC inspection findings · ICS sustainability review tracking · DHSC ARA disclosure"},
            {"label": "Backlog maintenance", "value": "ERIC 2023-24 elevated backlog given small-trust capital constraints"},
            {"label": "Peer benchmark", "value": "Above small-acute median impairment (sustainability-review premium)"}
        ],
        "notes": "East Cheshire's impairment is the small-trust archetype — a single 1971 acute envelope at Macclesfield carrying disproportionate condition-driven MEA-DRC haircut, exacerbated by repeated Cheshire & Merseyside ICS sustainability reviews that have at various points raised questions about long-term acute viability. Each review cycle creates carrying-value uncertainty before resolution, and the 2024-25 figure reflects this structural overhang on top of standard cycle reassessment. ERIC backlog data shows elevated risk consistent with small-trust capital constraints.",
        "sources": [
            {"publisher": "East Cheshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastcheshire.nhs.uk/About-The-Trust/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "East Cheshire NHS Trust provider profile (RJN)", "url": "https://www.cqc.org.uk/provider/RJN"},
            {"publisher": "NHS Cheshire and Merseyside ICB", "title": "Cheshire & Merseyside ICS estate strategy", "url": "https://www.cheshireandmerseyside.nhs.uk/"}
        ],
        "related": ["East Cheshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — East Cheshire NHS Trust", "Impairments net of reversals — Mid Cheshire Hospitals NHS Foundation Trust"]
    },
    "Impairments net of reversals — Coventry and Warwickshire Partnership NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Coventry and Warwickshire Partnership NHS Trust"}],
        "description": "Non-cash writedowns across CWPT's mental-health, learning-disability and community-services estate — Caludon Centre (Coventry, principal MH inpatient, co-located with University Hospitals Coventry & Warwickshire), Brooklands Hospital (Marston Green, learning disability), plus community clinics across Coventry, Rugby and Warwickshire. MH and LD impairments are dominated by ligature-resistant retrofit cycles and dormitory-elimination work that interact with carrying values.",
        "beneficiaries": "MH and LD services covering c. 1M residents of Coventry and Warwickshire; c. 4,500 staff; impairment is non-cash but reflects accelerated retrofit cycles in inpatient MH and LD settings.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£3.29M"},
            {"label": "Driver", "value": "MH ligature-retrofit + dormitory-eradication carrying-value review · MEA-DRC on Caludon + Brooklands"},
            {"label": "Estate scale", "value": "Caludon Centre (Coventry) MH inpatient + Brooklands LD + 60+ community clinics"},
            {"label": "MH-specific", "value": "s.136 places of safety · PICU · ligature-resistant fittings · dormitory-elimination ongoing"},
            {"label": "LD-specific", "value": "Brooklands Hospital LD inpatient · post-Winterbourne View / Transforming Care environment standards"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £1.5M → 2023-24 c. £2.4M → 2024-25 £3.29M (rising · retrofit + dormitory programmes)"},
            {"label": "NHP cohort", "value": "Not in NHP cohort (acute-focused programme) · MH dormitory-eradication funded separately"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2006 trust formation · Successor: Coventry & Warwickshire ICS MH estate strategy"},
            {"label": "Evaluation evidence", "value": "CQC inspection environment findings · NHSE MH dormitory-eradication tracking"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH-trust median impairment (LD-Brooklands premium)"}
        ],
        "notes": "CWPT's impairment line is shaped by two sector-specific overlays — ligature-resistant retrofit cycles in MH inpatient settings (Caludon Centre) and post-Winterbourne View / Transforming Care environment standards in LD inpatient settings (Brooklands), both of which crystallise NRV against parts of the estate that fail to meet evolving safety specifications. The MH dormitory-eradication programme adds further carrying-value pressure on legacy multi-bed accommodation. The 2024-25 figure reflects continuation of these retrofit cycles on top of standard MEA-DRC reassessment.",
        "sources": [
            {"publisher": "Coventry and Warwickshire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.covwarkpt.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Mental health dormitory eradication programme", "url": "https://www.england.nhs.uk/mental-health/"},
            {"publisher": "Care Quality Commission", "title": "CWPT provider profile (RYG)", "url": "https://www.cqc.org.uk/provider/RYG"},
            {"publisher": "NHS England", "title": "Building the Right Support / Transforming Care", "url": "https://www.england.nhs.uk/learning-disabilities/care/"}
        ],
        "related": ["Coventry and Warwickshire Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Premises (other) — Coventry and Warwickshire Partnership NHS Trust", "Impairments net of reversals — Birmingham and Solihull Mental Health NHS Foundation Trust"]
    },
    "Impairments net of reversals — Southern Health NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Southern Health NHS Foundation Trust"}],
        "description": "Non-cash writedowns across Southern Health's Hampshire MH and LD estate — Antelope House (Southampton), Melbury Lodge (Winchester), Parklands Hospital (Basingstoke), the Limes secure unit, plus over 100 community sites. Southern Health has been under sustained scrutiny since the 2013 death of Connor Sparrowhawk and the 2015 Mazars review of unexpected deaths, with ligature-elimination, observation-line redesign and ward-environment retrofit cycles flowing through the carrying-value reassessment.",
        "beneficiaries": "MH, LD and community services covering c. 1.4M residents of Hampshire and Isle of Wight; c. 6,000 staff; impairment is non-cash but reflects sustained safety-driven retrofit pressure on MH inpatient stock.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement · CQC Reg 12 (safe care)",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£3.29M"},
            {"label": "Driver", "value": "Ligature-elimination retrofit · dormitory-eradication · MEA-DRC reassessment on heritage MH estate"},
            {"label": "Estate scale", "value": "Antelope House (Southampton) + Melbury Lodge (Winchester) + Parklands (Basingstoke) + Limes secure + 100+ community"},
            {"label": "MH-specific", "value": "s.136 places of safety · PICU · ligature-elimination · post-Mazars 2015 environment review programme"},
            {"label": "Heritage estate", "value": "Some Victorian asylum-era blocks at Parklands (Park Prewett site) carry listed-building constraints"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "Valuation cycle", "value": "5-yearly external valuation · interim VOA indexation"},
            {"label": "3-year impairment trend", "value": "2022-23 c. £1.7M → 2023-24 c. £2.5M → 2024-25 £3.29M (rising · retrofit cycle + dormitory programme)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2011 merger of Hampshire Partnership + Hampshire Community Health · Successor: Hampshire & Isle of Wight ICS MH estate"},
            {"label": "Evaluation evidence", "value": "Mazars review (2015) of unexpected deaths · CQC successive inspections · post-Sparrowhawk reform tracking"},
            {"label": "NHP cohort", "value": "Not in NHP cohort · MH dormitory-eradication funded separately by NHSE"},
            {"label": "Peer benchmark", "value": "Above MH-trust median impairment (heritage + sustained retrofit cycle)"}
        ],
        "notes": "Southern Health's impairment line carries a uniquely sustained safety-driven retrofit profile — the 2015 Mazars review of unexpected deaths and the broader Sparrowhawk-era reforms triggered ligature-elimination and observation-line redesign programmes that continue to crystallise NRV against parts of the inpatient estate that fail evolving environment specifications. Some Park Prewett-era heritage blocks at Parklands constrain modernisation options. The 2024-25 figure reflects continuation of these structural retrofit cycles alongside MH dormitory eradication and standard MEA-DRC reassessment.",
        "sources": [
            {"publisher": "Southern Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southernhealth.nhs.uk/about-us/publications"},
            {"publisher": "Mazars LLP / NHS England", "title": "Independent review into deaths at Southern Health (2015)", "url": "https://www.england.nhs.uk/2015/12/mazars-rep/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Southern Health provider profile (RW1)", "url": "https://www.cqc.org.uk/provider/RW1"},
            {"publisher": "NHS England", "title": "Mental health dormitory eradication programme", "url": "https://www.england.nhs.uk/mental-health/"}
        ],
        "related": ["Southern Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Premises (other) — Southern Health NHS Foundation Trust", "Impairments net of reversals — Hertfordshire Partnership University NHS Foundation Trust"]
    },
}
