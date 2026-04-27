# -*- coding: utf-8 -*-
# Phase 2 SCamb — chunk 13 (17 NHS Specialist/Community/Ambulance Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Business rates — Royal National Orthopaedic Hospital NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Royal National Orthopaedic Hospital NHS Trust"}],
        "description": "RNOH's £0.96M non-domestic-rates bill covers business rates payable to the London Borough of Harrow on its main 31-acre Stanmore campus (a Grade II listed 1922 site) plus the satellite outpatient site at Bolsover Street in central London (Westminster City Council). Rates are paid under the Local Government Finance Act 1988 small/large multiplier system, with rateable values from the Valuation Office Agency 2023 rating list. The Stanmore campus dominates the bill given the size of the historic estate, while the outpatient and theatre redevelopment programme is reshaping the rateable footprint.",
        "beneficiaries": "Serves a national tertiary-referral catchment for complex orthopaedics, spinal injury and paediatric musculoskeletal care; c. 200,000 outpatient attendances/yr + c. 8,500 inpatient/day-case episodes; c. 1,500 WTE staff across the 31-acre Stanmore campus + Bolsover Street central London satellite.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.96M"},
            {"label": "Specialty footprint", "value": "National tertiary orthopaedic specialist trust — Stanmore (31 acres, Grade II listed 1922) + Bolsover St central London satellite"},
            {"label": "Annual activity", "value": "c. 200,000 outpatient attendances/yr; c. 8,500 inpatient/day-case episodes; UK's largest spinal cord injury centre (London Spinal Cord Injury Centre)"},
            {"label": "Workforce", "value": "c. 1,500 WTE; tertiary-referral consultant body for complex spinal, sarcoma, paediatric ortho"},
            {"label": "Billing authorities", "value": "London Borough of Harrow (Stanmore main site) + Westminster City Council (Bolsover Street outpatient/theatre site)"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; new Stanmore Building (Phase 1, opened 2024) brings additional rateable value once VOA assesses"},
            {"label": "Delivery body", "value": "RNOH Estates & Facilities + relevant billing authorities (Harrow, Westminster) + Valuation Office Agency"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG + HM Treasury + DHSC + NHSE Specialised Commissioning (specialist orthopaedics)"},
            {"label": "Evaluation evidence", "value": "RNOH ARA 2023-24; CQC provider profile (RAN); NHSE Estates Returns Information Collection (ERIC); NHSE Specialised Commissioning service spec"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 VOA list · Successor: 2026 VOA revaluation + post-2024 Stanmore Building re-assessment + Phase 2 redevelopment (theatres + research wing)"}
        ],
        "notes": "RNOH Stanmore is one of the UK's most distinctive specialist sites — a 31-acre former military convalescent hospital with Grade II listed 1922 buildings — and the rates bill reflects both the campus scale and the listed heritage premium that limits redevelopment options. The new Stanmore Building (Phase 1) opened 2024 brings substantially upgraded ward and theatre capacity, but VOA reassessment will lift the rateable value when the 2026 list is published. RNOH pays full NDR with no NHS charity-style exemption. The Bolsover Street satellite in Westminster carries London-weighted RV reflecting central-zone valuations. Forward drivers are 2026 revaluation, the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 supplementary multiplier, and Phase 2 redevelopment.",
        "sources": [
            {"publisher": "Royal National Orthopaedic Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rnoh.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Royal National Orthopaedic Hospital provider profile (RAN)", "url": "https://www.cqc.org.uk/provider/RAN"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "RNOH", "title": "Stanmore Building redevelopment programme", "url": "https://www.rnoh.nhs.uk/about-us/stanmore-building"}
        ],
        "related": ["Royal National Orthopaedic Hospital NHS Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Business rates — The Royal Marsden NHS Foundation Trust", "Business rates — Sheffield Children's NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Drugs costs — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "London Ambulance Service NHS Trust"}],
        "description": "LAS's £0.95M drugs-costs line covers pre-hospital pharmaceuticals carried on c. 450 frontline emergency ambulances and c. 100 fast-response cars across Greater London — predominantly analgesia (paracetamol, morphine, fentanyl, Entonox), cardiac drugs (aspirin, GTN, adrenaline, amiodarone), anti-emetics (ondansetron, cyclizine), anaphylaxis kits (adrenaline auto-injectors), tranexamic acid for major haemorrhage, naloxone for opioid overdose and oxygen. Procured through NHS Supply Chain frameworks under the Branded Medicines Pricing Scheme and dispensed under PGDs (Patient Group Directions) by paramedics under MHRA Human Medicines Regulations 2012.",
        "beneficiaries": "Serves Greater London's c. 9.0M residents + commuter/visitor population; responds to c. 2.0M calls/yr + c. 1.2M emergency face-to-face responses; c. 9,000 WTE incl. c. 5,500 frontline operational paramedics, technicians and emergency ambulance crew across c. 70 ambulance stations.",
        "legal_basis": "NHS Act 2006 · Human Medicines Regulations 2012 (Patient Group Directions) · Medicines Act 1968 · Misuse of Drugs Act 1971 (CD schedule storage) · NHS Drug Tariff · Branded Medicines Pricing Scheme · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.95M"},
            {"label": "Operational scale", "value": "c. 2.0M calls/yr; c. 1.2M emergency face-to-face responses; c. 450 emergency ambulances + c. 100 fast-response cars + cycle response units"},
            {"label": "Population served", "value": "c. 9.0M Greater London residents + commuters + visitors; UK's largest ambulance trust by call volume"},
            {"label": "Workforce", "value": "c. 9,000 WTE; c. 5,500 frontline paramedics + technicians + emergency ambulance crew across c. 70 stations + 2 EOCs (Waterloo + Bow)"},
            {"label": "Drug categories", "value": "Analgesia (morphine, fentanyl, paracetamol, Entonox); cardiac (adrenaline, amiodarone, GTN); anti-emetic; tranexamic acid; naloxone; oxygen; adrenaline auto-injectors"},
            {"label": "Procurement", "value": "NHS Supply Chain pharmaceutical frameworks + Branded Medicines Pricing Scheme + Drug Tariff"},
            {"label": "Funding trajectory", "value": "Rising — pandemic naloxone expansion + tranexamic acid major-haemorrhage uptake + Cat-1/Cat-2 demand growth + price pressure on generics; small absolute size vs Acute trusts (no IP drugs)"},
            {"label": "Delivery body", "value": "LAS Pharmacy + Make Ready Centres (vehicle resupply) + NHS Supply Chain pharmaceutical category tower"},
            {"label": "Policy owner", "value": "NHSE Ambulance Programme + DHSC + MHRA + Medicines Optimisation team + AACE (Association of Ambulance Chief Executives) JRCALC clinical guidelines"},
            {"label": "Clinical governance", "value": "JRCALC UK Ambulance Services Clinical Practice Guidelines; Patient Group Directions for paramedic administration; CD schedule controlled drugs governance per Misuse of Drugs Act 1971"},
            {"label": "Evaluation evidence", "value": "LAS ARA; CQC inspection (RRU); NHSE ambulance quality indicators (AQIs); NAO ambulance services report 2017; ORH ambulance benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-JRCALC 2019 formulary · Successor: expanded paramedic scope of practice (e.g. specialist paramedic urgent care) + naloxone roll-out + drone-delivered AED/medication trials"}
        ],
        "notes": "Ambulance drugs costs are tiny relative to Acute trusts because pre-hospital pharmacopoeia is narrow (no IP/injectable cancer or biologic drugs) — the line tracks volume of analgesia, cardiac arrest meds and naloxone consumed across c. 1.2M responses. Key drivers are JRCALC guideline updates (e.g. the 2019 expansion of paramedic scope), the post-2020 naloxone roll-out for opioid overdose response, and tranexamic acid uptake for major-haemorrhage trauma calls. CD schedule drugs (morphine, fentanyl) carry storage and audit overhead under Misuse of Drugs Act 1971. NHS Supply Chain pharmaceutical category tower is the principal procurement route. Going forward, expanded paramedic scope and electronic patient care record (ePCR) drug-administration tracking will tighten governance.",
        "sources": [
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/who-we-are/our-publications/"},
            {"publisher": "JRCALC / AACE", "title": "JRCALC Clinical Practice Guidelines (UK Ambulance Services)", "url": "https://aace.org.uk/jrcalc/"},
            {"publisher": "Care Quality Commission", "title": "London Ambulance Service NHS Trust provider profile (RRU)", "url": "https://www.cqc.org.uk/provider/RRU"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "MHRA", "title": "Patient Group Directions: who can use them", "url": "https://www.gov.uk/government/publications/patient-group-directions-pgds"},
            {"publisher": "NHS Supply Chain", "title": "Pharmacy and pharmaceuticals category tower", "url": "https://www.supplychain.nhs.uk/categories/pharmacy/"}
        ],
        "related": ["London Ambulance Service NHS Trust", "Clinical Supplies & Drugs", "NHS Ambulance Trusts", "Drugs costs — West Midlands Ambulance Service University NHS Foundation Trust", "Drugs costs — South Western Ambulance Service NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Business rates — Kent Community Health NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Kent Community Health NHS Foundation Trust"}],
        "description": "KCHFT's £0.94M non-domestic-rates bill covers business rates payable to multiple Kent district councils (Ashford, Canterbury, Dover, Folkestone & Hythe, Maidstone, Swale, Thanet, Tonbridge & Malling, Tunbridge Wells, Sevenoaks, Medway, Gravesham, Dartford) on its portfolio of community hospitals, clinics, neighbourhood-team bases and minor injuries units across Kent and Medway. Rates payable under the Local Government Finance Act 1988 with rateable values from the VOA 2023 rating list. The trust runs minor-injury units, community hospitals at sites including Faversham, Sittingbourne, Tonbridge, Hawkhurst, Sevenoaks, Edenbridge and a long tail of clinic premises.",
        "beneficiaries": "Serves a c. 1.6M Kent + Medway population; operates from c. 70+ owned and leased community sites including community hospitals at Faversham, Hawkhurst, Tonbridge, Sevenoaks, Edenbridge and Sittingbourne; c. 5,200 WTE incl. district nurses, school nurses, health visitors and AHPs covering predominantly rural east + south Kent.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.94M"},
            {"label": "Estate footprint", "value": "c. 70+ sites incl. community hospitals at Faversham, Hawkhurst, Tonbridge, Sevenoaks, Edenbridge, Sittingbourne + clinic + base-station premises"},
            {"label": "Population served", "value": "c. 1.6M Kent + Medway residents"},
            {"label": "Workforce", "value": "c. 5,200 WTE — district nurses, school nurses, health visitors, AHPs, MIU staff"},
            {"label": "Billing authorities", "value": "Multiple Kent districts: Ashford, Canterbury, Dover, Folkestone & Hythe, Maidstone, Swale, Thanet, Tonbridge & Malling, Tunbridge Wells, Sevenoaks, Medway, Gravesham, Dartford"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "KCHFT Estates & Facilities + NHSPS for leased sites + relevant Kent district billing authorities + VOA"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG + HM Treasury + DHSC + Kent & Medway ICB"},
            {"label": "Evaluation evidence", "value": "KCHFT ARA 2023-24; CQC provider profile (RYY); NHSE ERIC annual return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era estate · Successor: 2026 VOA revaluation + estate consolidation under Three Shifts community-care policy + Kent & Medway integrated care strategy"}
        ],
        "notes": "Community trusts pay full NDR with no NHS exemption — the line tracks size and rateable value of the owned/leased footprint. KCHFT's c. £0.94M reflects c. 70+ sites across an unusually large geographic footprint (Kent is England's largest county by area in the Home Counties). The trust's minor-injuries units and community hospital network in east Kent (Hawkhurst, Faversham, Sittingbourne) sit alongside a long tail of clinic premises serving rural communities. Drivers include the VOA 2023 rating list, annual multiplier uprating, and the new supplementary multiplier under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Three Shifts community-care policy may drive selective estate consolidation.",
        "sources": [
            {"publisher": "Kent Community Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kentcht.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Kent Community Health NHS Foundation Trust provider profile (RYY)", "url": "https://www.cqc.org.uk/provider/RYY"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Kent Community Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Norfolk Community Health and Care NHS Trust", "Business rates — Hertfordshire Community NHS Trust", "Valuation Office Agency"]
    },
    "PFI / LIFT charges — Birmingham Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Birmingham Community Healthcare NHS Foundation Trust"}],
        "description": "BCHC's £0.94M PFI/LIFT charges reflect unitary payments to LIFT (Local Improvement Finance Trust) special-purpose companies for community-clinic and primary-care premises across Birmingham — the LIFT model was the principal vehicle for replacing 1990s-era community estate in the 2000s, with Birmingham & Solihull LIFT (now Community Health Partnerships / NHS Property Services successors) holding equity stakes alongside private-sector partners. The line covers service charges, finance charges (post-IFRS 16 typically split between depreciation and interest) and lifecycle/FM charges under the LIFT lease-plus framework for sites such as Sparkhill, Summerfield and other community-clinic LIFT premises.",
        "beneficiaries": "Serves Birmingham's c. 1.15M residents (England's largest local authority area by population); operates from c. 230+ sites including LIFT-procured neighbourhood clinics, district-nursing bases, dental clinics and Moseley Hall + West Heath Hospital (community hospitals); c. 5,400 WTE incl. district nurses, AHPs, dental services, learning disability + children's community services.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 government re-classification) · DHSC PFI/LIFT guidance · Local Improvement Finance Trust framework · NHS Act 2006 · DHSC Group Accounting Manual 2024-25 (ch.7)",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.94M"},
            {"label": "Estate footprint", "value": "c. 230+ sites (community + dental clinics, neighbourhood team bases) incl. LIFT-procured premises across Birmingham + Moseley Hall + West Heath community hospitals"},
            {"label": "Population served", "value": "c. 1.15M Birmingham residents (England's largest LA area by population)"},
            {"label": "Workforce", "value": "c. 5,400 WTE — district nurses, AHPs, school nurses, health visitors, learning disability, dental, children's community services"},
            {"label": "LIFT vehicle", "value": "Birmingham & Solihull LIFT — public-private partnership with NHS / Community Health Partnerships equity + private-sector debt + DBFO arrangement"},
            {"label": "Charge components", "value": "Service charge + finance charge (post-IFRS 16: depreciation + interest split) + lifecycle/FM charge for hard FM (planned + reactive maintenance) and soft FM"},
            {"label": "Funding trajectory", "value": "Stable to slight rise on RPI/CPI uprating; will continue through end of LIFT contract terms (typically 25-30 years from sign-off in mid-2000s) with hand-back milestones"},
            {"label": "Delivery body", "value": "BCHC Estates & Facilities + Birmingham & Solihull LIFTCo + Community Health Partnerships (NHS shareholder) + private-sector partner FM contractor"},
            {"label": "Policy owner", "value": "DHSC PFI/LIFT team + Treasury Operational Efficiency + NHSE + Birmingham & Solihull ICB"},
            {"label": "Evaluation evidence", "value": "BCHC ARA 2023-24; NAO PFI and PF2 reports (HC 718 2017-19); HM Treasury PFI Centre of Best Practice; CQC provider profile (RYW)"},
            {"label": "IFRS 16 transition", "value": "1 Apr 2022 mandatory adoption of IFRS 16 across UK government — LIFT charges previously off-balance-sheet now on-balance-sheet (right-of-use asset + lease liability)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT 1980s/90s community-clinic estate · Successor: post-LIFT contract expiry hand-back to NHS + asset rationalisation under Three Shifts community-care policy + ongoing CHP equity reorganisation"}
        ],
        "notes": "LIFT was the community-care equivalent of PFI used heavily in the 2000s for neighbourhood clinics, GP-and-community-services hubs and dental clinics, with Community Health Partnerships (now part of NHS Property Services group) holding NHS public-sector equity. BCHC's c. £0.94M reflects unitary payments to its Birmingham & Solihull LIFT vehicle for clinics across the city. Post-2022 IFRS 16 transition moved most PFI/LIFT lease elements on-balance-sheet — the line now reflects depreciation + interest + service-charge components rather than the pre-2022 unitary-payment model. Birmingham's PFI/LIFT footprint will hand back to NHS ownership at contract expiry (typically late 2020s/early 2030s) with end-of-contract condition-survey disputes a recurring NAO theme.",
        "sources": [
            {"publisher": "Birmingham Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bhamcommunity.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Birmingham Community Healthcare NHS Foundation Trust provider profile (RYW)", "url": "https://www.cqc.org.uk/provider/RYW"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Community Health Partnerships", "title": "About LIFT", "url": "https://www.communityhealthpartnerships.co.uk/about-us"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "Private finance initiative and private finance 2 projects: 2023 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2023-summary-data"}
        ],
        "related": ["Birmingham Community Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "PFI / LIFT charges — Northamptonshire Healthcare NHS Foundation Trust", "PFI / LIFT charges — Royal Papworth Hospital NHS Foundation Trust", "Community Health Partnerships"]
    },
    "Business rates — Central London Community Healthcare NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Central London Community Healthcare NHS Trust"}],
        "description": "CLCH's £0.91M non-domestic-rates bill covers business rates payable to multiple London boroughs (Westminster, Kensington & Chelsea, Hammersmith & Fulham, Barnet, Brent, Harrow, Hounslow, Ealing) on its portfolio of community clinics, neighbourhood-team bases, walk-in centres and the small inpatient footprint at Athlone House and Edgware Community Hospital site. Central London RVs carry a substantial weighting reflecting West End and inner London commercial valuations, especially Westminster and K&C billing-authority charges. Rates payable under the Local Government Finance Act 1988 with rateable values from the VOA 2023 rating list.",
        "beneficiaries": "Serves a c. 2.0M+ population across north-west and central London; operates from c. 100+ sites including walk-in centres, community clinics, GP-co-located premises and Edgware Community Hospital + St John's Wood + Athlone House; c. 4,200 WTE incl. district nurses, school nurses, health visitors, MSK physio and end-of-life care.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.91M"},
            {"label": "Estate footprint", "value": "c. 100+ sites — walk-in centres, community clinics, neighbourhood team bases, Edgware Community Hospital + St John's Wood + Athlone House inpatient sites"},
            {"label": "Population served", "value": "c. 2.0M+ across NW + central London — Westminster, K&C, H&F, Barnet, Brent, Harrow, Hounslow, Ealing"},
            {"label": "Workforce", "value": "c. 4,200 WTE — district nurses, school nurses, health visitors, MSK physio, end-of-life community team"},
            {"label": "Billing authorities", "value": "Multiple inner + outer London boroughs: Westminster, Kensington & Chelsea, Hammersmith & Fulham, Barnet, Brent, Harrow, Hounslow, Ealing"},
            {"label": "VOA list cycle", "value": "2023 rating list — central-London rateable values particularly high in Westminster + K&C zones"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption); central-London RV premium drives unit cost"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr; central London 2023 VOA list lifted RVs in West End commercial zones; supplements multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "CLCH Estates & Facilities + NHSPS for leased sites (heavy NHSPS exposure for community trusts) + relevant London billing authorities + VOA"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG + HM Treasury + DHSC + NW London ICB + NCL ICB"},
            {"label": "Evaluation evidence", "value": "CLCH ARA 2023-24; CQC provider profile (RYX); NHSE ERIC annual return; NHSPS rent recovery reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era estate · Successor: 2026 VOA revaluation + estate consolidation under Three Shifts community-care policy + NHSPS rationalisation programme"}
        ],
        "notes": "CLCH's central-London geography drives a higher per-site rates bill than provincial community trusts — Westminster and K&C VOA rateable values reflect West End commercial premium. The trust pays full NDR with no NHS exemption. The estate is heavily NHSPS-leased (a feature of community trusts that emerged out of PCTs in 2011), so rate liabilities flow through occupancy charges where NHSPS holds the head lease, but the trust still bears NDR on directly-rated occupations. Drivers include the VOA 2023 rating list (which lifted central-London commercial RVs sharply post-pandemic vacancy normalisation), annual multiplier uprating, the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 supplementary multiplier, and the 2026 VOA revaluation.",
        "sources": [
            {"publisher": "Central London Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://clch.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Central London Community Healthcare NHS Trust provider profile (RYX)", "url": "https://www.cqc.org.uk/provider/RYX"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Central London Community Healthcare NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Hertfordshire Community NHS Trust", "Business rates — Kent Community Health NHS Foundation Trust", "NHS Property Services"]
    },
    "Business rates — Sheffield Children's NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Sheffield Children's NHS Foundation Trust"}],
        "description": "Sheffield Children's NHS FT's £0.90M non-domestic-rates bill covers business rates payable to Sheffield City Council on its main paediatric hospital site at Western Bank (a national-historic-importance Victorian hospital with subsequent additions including the 2016 Wing-redeveloped patient tower) plus Centenary Wing, Ryegate Children's Centre and the satellite community CAMHS sites across South Yorkshire. Rates are paid under the Local Government Finance Act 1988 multiplier system, with rateable values from the VOA 2023 rating list. The newer Acorn Wing/2016 Helipad-Wing capital programme has lifted rateable value over the cycle.",
        "beneficiaries": "Serves a regional paediatric tertiary catchment of c. 2.5M children across South Yorkshire, North Derbyshire, North Nottinghamshire and parts of North Lincolnshire; one of three dedicated children's NHS trusts in England (with GOSH, Alder Hey, Birmingham Children's); c. 280,000 patient contacts/yr; c. 3,800 WTE incl. paediatric specialists and Ryegate community child-disability service.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.90M"},
            {"label": "Specialty footprint", "value": "Standalone paediatric specialist trust — Western Bank main hospital + Acorn Wing/2016 Helipad Wing + Ryegate Children's Centre + community CAMHS sites"},
            {"label": "Annual activity", "value": "c. 280,000 patient contacts/yr; tertiary referral catchment of c. 2.5M children across South Yorkshire + North Derbyshire + North Notts"},
            {"label": "Workforce", "value": "c. 3,800 WTE; one of three dedicated children's NHS trusts in England (with GOSH and Alder Hey)"},
            {"label": "Billing authorities", "value": "Sheffield City Council (primary) + outlying district councils for community CAMHS sites"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; Acorn Wing/2016 Helipad Wing capital additions lifted RV; supplements multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "Sheffield Children's Estates & Facilities + Sheffield City Council billing authority + Valuation Office Agency"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG + HM Treasury + DHSC + NHSE Specialised Commissioning (paediatric specialist services)"},
            {"label": "Evaluation evidence", "value": "Sheffield Children's ARA 2023-24; CQC provider profile (RCU) — Outstanding rating; NHSE ERIC annual return; NHSE Specialised Commissioning paediatric service spec"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 VOA list · Successor: 2026 VOA revaluation + planned ongoing capital programme (theatres, CAMHS Tier 4 expansion) lifting RV"}
        ],
        "notes": "Sheffield Children's is one of only three dedicated children's NHS trusts in England (alongside GOSH and Alder Hey) and the only one outside London/Liverpool serving the north of England's paediatric tertiary catchment. The c. £0.90M rates bill reflects the consolidated Western Bank campus plus the post-2016 Acorn/Helipad Wing addition that brought a helideck and major theatre/wards expansion. NDR is paid in full with no NHS exemption. CAMHS Tier 4 inpatient expansion and ongoing capital additions will continue to lift the rateable footprint at the 2026 VOA revaluation. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 supplementary multiplier will apply to higher-RV occupations.",
        "sources": [
            {"publisher": "Sheffield Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sheffieldchildrens.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Children's NHS Foundation Trust provider profile (RCU)", "url": "https://www.cqc.org.uk/provider/RCU"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised commissioning — paediatric specialist services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["Sheffield Children's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Business rates — Great Ormond Street Hospital for Children NHS Foundation Trust", "Business rates — Alder Hey Children's NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Lease expenditure — Herefordshire and Worcestershire Health and Care NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Herefordshire and Worcestershire Health and Care NHS Trust"}],
        "description": "HWHC's £0.90M lease-expenditure line covers the residual operating-lease element under IFRS 16 — predominantly short-term + low-value lease exemptions plus any remaining service-charge components for vehicle pool fleet (district nursing + community AHP cars), photocopier/print MFD leases and small-item operational equipment. Most premises leases were brought on-balance-sheet at IFRS 16 1 Apr 2022 transition (right-of-use asset + lease liability), so this line is the residual P&L charge for IFRS-16-exempt categories rather than the full premises rental flow.",
        "beneficiaries": "Serves c. 780,000 residents across Herefordshire and Worcestershire (rural counties in the West Midlands); operates from c. 80+ community sites including community hospitals at Ross-on-Wye, Bromsgrove, Evesham, Kidderminster, Malvern, Pershore, Princess of Wales (Bromsgrove), Tenbury and the Hereford CAMHS unit; c. 3,800 WTE incl. district nurses, school nurses, MH practitioners, MSK community physio.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 (ch.7) · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IAS 17 (legacy)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.90M"},
            {"label": "Estate footprint", "value": "c. 80+ sites incl. community hospitals at Ross-on-Wye, Bromsgrove, Evesham, Kidderminster, Malvern, Pershore, Tenbury + Hereford CAMHS unit"},
            {"label": "Population served", "value": "c. 780,000 — Herefordshire (c. 190k) + Worcestershire (c. 590k)"},
            {"label": "Workforce", "value": "c. 3,800 WTE — district nurses, MH practitioners (combined community + MH trust), school nurses, MSK physio"},
            {"label": "Lease composition", "value": "Predominantly IFRS-16-exempt short-term (<12mo) + low-value (<$5k) categories — pool fleet vehicles, MFD print devices, small operational kit"},
            {"label": "Premises lease flow", "value": "Largest premises leases (NHSPS occupation, GP-shared sites, council/community-trust sites) capitalised under IFRS 16 right-of-use + lease liability — flow appears in depreciation/finance cost lines, not here"},
            {"label": "IFRS 16 transition", "value": "1 Apr 2022 mandatory adoption across UK government; transition substantially reduced the operating-lease P&L line"},
            {"label": "Funding trajectory", "value": "Stable to slight rise on RPI; modest sub-£1M reflects substantial premises shift to capitalised leases post-2022 IFRS 16 transition"},
            {"label": "Delivery body", "value": "HWHC Estates & Facilities + NHSPS as principal landlord for clinics + commercial fleet/MFD lease providers"},
            {"label": "Policy owner", "value": "DHSC Finance Manual + HM Treasury Financial Reporting Advisory Board (FRAB) + NHSE Provider Finance + Herefordshire & Worcestershire ICB"},
            {"label": "Evaluation evidence", "value": "HWHC ARA 2023-24; CQC provider profile (R1A); NHSE ERIC annual return; lease commitments note in trust accounts"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease P&L treatment with all premises rentals here · Successor: post-2022 IFRS 16 capitalised + ongoing fleet electrification under NHS Net Zero 2032"}
        ],
        "notes": "Following IFRS 16 mandatory adoption on 1 Apr 2022, most premises leases (NHSPS, GP-shared, council premises) are now on-balance-sheet with depreciation + finance-cost flowing through other lines, leaving this £0.90M residual P&L charge for IFRS-16-exempt short-term and low-value categories. HWHC's geographically-dispersed rural estate across Herefordshire and Worcestershire means a sizeable district-nursing pool-car fleet (mostly leased) plus an MFD/print contract base. Forward drivers include fleet electrification under NHS Net Zero 2032 (charge-points + EV pool cars), and the periodic re-indexation of NHSPS occupation charges under the SLA model. The combined community-and-MH structure of HWHC means the lease portfolio mixes both physical-health and MH service estate.",
        "sources": [
            {"publisher": "Herefordshire and Worcestershire Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hacw.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "Herefordshire and Worcestershire Health and Care NHS Trust provider profile (R1A)", "url": "https://www.cqc.org.uk/provider/R1A"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury / FRAB", "title": "Application of IFRS 16 in central government", "url": "https://www.gov.uk/government/groups/financial-reporting-advisory-board"},
            {"publisher": "NHS Property Services", "title": "About NHSPS", "url": "https://www.property.nhs.uk/about-us/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Herefordshire and Worcestershire Health and Care NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Kent Community Health NHS Foundation Trust", "Lease expenditure — Northamptonshire Healthcare NHS Foundation Trust", "NHS Property Services"]
    },
    "Amortisation — Queen Victoria Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Queen Victoria Hospital NHS Foundation Trust"}],
        "description": "QVH's £0.89M amortisation charge represents the systematic write-down of intangible assets — predominantly software licences (electronic patient record, theatre/scheduling software, specialised reconstructive/burns imaging databases, photographic/clinical-image archives for plastics and reconstructive surgery) and any capitalised software development under IAS 38. QVH at East Grinstead is a tertiary specialist plastics, burns, oculoplastics, corneoplastics and head-and-neck reconstructive trust historically associated with Sir Archibald McIndoe's Guinea Pig Club and one of England's small plastics-and-reconstruction specialist trusts.",
        "beneficiaries": "Serves a tertiary referral catchment of c. 6.5M across Sussex, Surrey, Kent and southern London for complex plastics, burns and reconstructive surgery; one of four English specialist burns/plastics centres; c. 60,000 outpatient attendances + c. 11,000 inpatient/day-case episodes; c. 1,200 WTE incl. specialist plastics/burns/oculoplastics consultants.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frascati Manual research/development distinction",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.89M"},
            {"label": "Specialty footprint", "value": "Tertiary plastics, burns, oculoplastics, corneoplastics, head & neck reconstructive specialist trust at East Grinstead — one of 4 English specialist burns centres"},
            {"label": "Annual activity", "value": "c. 60,000 outpatient attendances/yr; c. 11,000 inpatient/day-case episodes; c. 6.5M tertiary catchment Sussex/Surrey/Kent/S London"},
            {"label": "Workforce", "value": "c. 1,200 WTE incl. specialist plastics + burns + oculoplastics + corneoplastics + maxfax + ENT reconstructive consultants"},
            {"label": "Intangibles class", "value": "Predominantly software licences (EPR, theatre scheduling, specialised reconstructive imaging) + clinical photography/archive systems + capitalised software development under IAS 38"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; clinical-system EPR straight-line over service life"},
            {"label": "Funding trajectory", "value": "Stable around £0.9M/yr; rising slowly with EPR and theatre-scheduling system replacement cycle; small absolute size reflecting compact specialist trust"},
            {"label": "Delivery body", "value": "QVH Digital + Estates teams + EPR / theatre / clinical-photo system providers + NHSE Specialised Commissioning"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (specialist plastics/burns/reconstructive) + DHSC + Sussex ICB host commissioner"},
            {"label": "Evaluation evidence", "value": "QVH ARA 2023-24; CQC provider profile (RPC) — Outstanding rating; NHSE Specialised Commissioning service spec; National Burn Care Standards"},
            {"label": "Heritage", "value": "Founded 1936; Sir Archibald McIndoe pioneering WWII reconstructive surgery (Guinea Pig Club) — historic listed McIndoe Burns Centre buildings"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy paper records + minor IT systems · Successor: planned EPR transition + theatre-scheduling modernisation + ongoing capitalised software replacement"}
        ],
        "notes": "QVH is one of England's specialist plastics/burns/reconstructive surgery centres with a heritage going back to Sir Archibald McIndoe's WWII Guinea Pig Club. Despite its small physical scale, the trust runs a substantial digital footprint for clinical photography, theatre scheduling and specialist plastics/burns imaging archives — these capitalised intangibles drive the £0.89M amortisation line under IAS 38. The specialist nature means costs are concentrated on a narrow set of bespoke clinical systems rather than the broad acute EPR portfolios. Drivers are EPR/theatre-system replacement cycles and useful-economic-life judgements (3-7 years for software) under DHSC GAM ch.5. The trust's small foundation-trust scale (c. 1,200 WTE) means amortisation is a meaningful proportion of intangibles spend.",
        "sources": [
            {"publisher": "Queen Victoria Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qvh.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Queen Victoria Hospital NHS Foundation Trust provider profile (RPC)", "url": "https://www.cqc.org.uk/provider/RPC"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 5 Property Plant Equipment & Intangibles", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised commissioning — specialist plastics, burns and reconstructive services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "British Burn Association", "title": "National Burn Care Standards", "url": "https://www.britishburnassociation.org/standards-and-guidelines/"},
            {"publisher": "Queen Victoria Hospital", "title": "About QVH and the McIndoe Burns Centre legacy", "url": "https://www.qvh.nhs.uk/about-us/our-history/"}
        ],
        "related": ["Queen Victoria Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Amortisation — Moorfields Eye Hospital NHS Foundation Trust", "Amortisation — The Royal Marsden NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Norfolk Community Health and Care NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Norfolk Community Health and Care NHS Trust"}],
        "description": "NCH&C's £0.89M non-domestic-rates bill covers business rates payable to multiple Norfolk district councils (Norwich, Broadland, South Norfolk, Breckland, North Norfolk, Great Yarmouth, King's Lynn & West Norfolk) on its portfolio of community hospitals, neighbourhood-team bases, walk-in centres and clinic premises across one of England's largest geographic-area counties. Rates are payable under the Local Government Finance Act 1988 with rateable values from the VOA 2023 rating list. The community-hospital network includes Cromer, North Walsham, Dereham, Swaffham, Kelling, Benjamin Court and other rural sites.",
        "beneficiaries": "Serves a c. 990,000 Norfolk population; operates from c. 60+ owned and leased community sites including community hospitals at Cromer, North Walsham, Dereham, Swaffham, Kelling, Benjamin Court (Cromer); c. 3,000 WTE incl. district nurses, school nurses, health visitors, MSK community physio and end-of-life community team.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.89M"},
            {"label": "Estate footprint", "value": "c. 60+ sites incl. community hospitals at Cromer, North Walsham, Dereham, Swaffham, Kelling, Benjamin Court + clinic + base-station premises"},
            {"label": "Population served", "value": "c. 990,000 Norfolk residents — predominantly rural with Norwich the only large urban centre"},
            {"label": "Workforce", "value": "c. 3,000 WTE — district nurses, school nurses, health visitors, MSK community physio, end-of-life team"},
            {"label": "Billing authorities", "value": "Multiple Norfolk districts: Norwich, Broadland, South Norfolk, Breckland, North Norfolk, Great Yarmouth, King's Lynn & West Norfolk"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "NCH&C Estates & Facilities + NHSPS for leased sites + relevant Norfolk district billing authorities + VOA"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG + HM Treasury + DHSC + Norfolk & Waveney ICB"},
            {"label": "Evaluation evidence", "value": "NCH&C ARA 2023-24; CQC provider profile (RY3) — Outstanding rating; NHSE ERIC annual return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era estate · Successor: 2026 VOA revaluation + estate consolidation under Three Shifts community-care policy + Norfolk & Waveney integrated care strategy"}
        ],
        "notes": "Norfolk Community Health and Care holds an Outstanding CQC rating and serves one of England's most rural counties through a dispersed estate of c. 60+ sites including community hospitals at Cromer, Dereham, Swaffham and North Walsham. The c. £0.89M rates bill reflects the geographic spread across multiple billing authorities. NHS bodies pay full NDR with no charity-style exemption, so the line is materially driven by the size of the rateable footprint and the VOA-assessed RVs. Drivers include the VOA 2023 rating list, annual multiplier uprating, and the new supplementary multiplier under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. The rural geography means a long tail of low-RV clinic sites alongside the community-hospital RVs.",
        "sources": [
            {"publisher": "Norfolk Community Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.norfolkcommunityhealthandcare.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Norfolk Community Health and Care NHS Trust provider profile (RY3)", "url": "https://www.cqc.org.uk/provider/RY3"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Norfolk Community Health and Care NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Hertfordshire Community NHS Trust", "Business rates — Kent Community Health NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Drugs costs — Hertfordshire Community NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Hertfordshire Community NHS Trust"}],
        "description": "HCT's £0.88M drugs-costs line covers community-administered medicines — predominantly community-nursing-administered injectables (insulin, B12, palliative-care subcut analgesia and anti-emetics via syringe drivers), childhood immunisations under the Greenbook 0-19 schedule, school-nurse vaccination programmes (HPV, Td/IPV, Men ACWY), wound-care products with a drug component, end-of-life-care medications (morphine, midazolam, hyoscine for the just-in-case box) and contraception/sexual-health drugs. Procured through NHS Supply Chain pharmaceutical frameworks under the Branded Medicines Pricing Scheme.",
        "beneficiaries": "Serves c. 1.2M Hertfordshire residents; operates from c. 80+ community sites + service contracts to schools (school nursing across all Hertfordshire LA areas), nurseries (health visiting), care homes and patients' own homes; c. 2,800 WTE incl. district nurses, school nurses, health visitors, community paediatric and end-of-life teams.",
        "legal_basis": "NHS Act 2006 · Human Medicines Regulations 2012 (Patient Group Directions for nurses) · Medicines Act 1968 · Misuse of Drugs Act 1971 (CD storage for end-of-life) · NHS Drug Tariff · Branded Medicines Pricing Scheme · Greenbook (Immunisation against infectious disease) · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.88M"},
            {"label": "Estate + service footprint", "value": "c. 80+ sites + school + nursery + care home + home-visit service contracts across Hertfordshire"},
            {"label": "Population served", "value": "c. 1.2M Hertfordshire residents — 0-19 service for all children + adult community + end-of-life"},
            {"label": "Workforce", "value": "c. 2,800 WTE — district nurses, school nurses, health visitors, community paediatricians, end-of-life nurses"},
            {"label": "Drug categories", "value": "Childhood immunisations (Greenbook); school-age vaccs (HPV/Td-IPV/MenACWY); palliative subcut (morphine, midazolam, hyoscine); insulin/B12 community admin; wound-care; sexual-health/contraception"},
            {"label": "Procurement", "value": "NHS Supply Chain pharmaceutical category tower + Branded Medicines Pricing Scheme + NHSE-commissioned vaccination programmes for schedule vaccines"},
            {"label": "Funding trajectory", "value": "Rising — palliative caseload growth (ageing population) + Three Shifts policy more home-based care + post-pandemic immunisation catch-up programmes"},
            {"label": "Delivery body", "value": "HCT Pharmacy + community-team medicines management + NHS Supply Chain + UKHSA for schedule vaccines"},
            {"label": "Policy owner", "value": "DHSC + NHSE Community Pharmacy/Community Services + Hertfordshire & West Essex ICB + UKHSA (vaccination programmes) + Joint Committee on Vaccination & Immunisation (JCVI)"},
            {"label": "Clinical governance", "value": "PGDs for nurse-led administration; CD schedule controlled drugs governance per Misuse of Drugs Act 1971; Greenbook + JCVI for immunisation schedule"},
            {"label": "Evaluation evidence", "value": "HCT ARA 2023-24; CQC provider profile (RY4); UKHSA immunisation coverage statistics; NHSE community-pharmacy returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: PCT-era community pharmacy fragmented · Successor: Three Shifts policy expansion of community pharmacy + virtual ward drug administration + community palliative growth"}
        ],
        "notes": "Community trusts have a small but distinctive drugs-cost profile dominated by Greenbook childhood + school-age immunisations (substantial volume), end-of-life-care subcut just-in-case medications (controlled drugs governance), community-nurse-administered injectables (insulin, B12) and contraception/sexual-health stock. HCT's c. £0.88M reflects the c. 1.2M Hertfordshire population's needs across all-ages community contact. Three Shifts policy (Darzi report Sep 2024) and the move from acute to community care will raise this line going forward, especially virtual-ward expansion bringing complex drug regimens into the community-nursing portfolio. PGDs under the Human Medicines Regulations 2012 govern nurse-led administration; CD storage and audit per Misuse of Drugs Act 1971 applies to subcut palliative meds.",
        "sources": [
            {"publisher": "Hertfordshire Community NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hct.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "Care Quality Commission", "title": "Hertfordshire Community NHS Trust provider profile (RY4)", "url": "https://www.cqc.org.uk/provider/RY4"},
            {"publisher": "UK Health Security Agency", "title": "Greenbook — Immunisation against infectious disease", "url": "https://www.gov.uk/government/collections/immunisation-against-infectious-disease-the-green-book"},
            {"publisher": "NHS Supply Chain", "title": "Pharmacy and pharmaceuticals category tower", "url": "https://www.supplychain.nhs.uk/categories/pharmacy/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "MHRA", "title": "Patient Group Directions: who can use them", "url": "https://www.gov.uk/government/publications/patient-group-directions-pgds"}
        ],
        "related": ["Hertfordshire Community NHS Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "Drugs costs — Norfolk Community Health and Care NHS Trust", "Drugs costs — Leeds Community Healthcare NHS Trust", "NHS Supply Chain"]
    },
    "Lease expenditure — East of England Ambulance Service NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "East of England Ambulance Service NHS Trust"}],
        "description": "EEAST's £0.87M lease-expenditure line covers IFRS 16 short-term and low-value lease exemptions plus residual operating-lease service-charge components — predominantly satellite ambulance station hot-desk leases, photocopier/MFD leases and small operational equipment hire. EEAST runs c. 130+ ambulance stations and standby points across Bedfordshire, Cambridgeshire, Essex, Hertfordshire, Norfolk and Suffolk; major fleet leases for emergency ambulances and rapid-response cars and the large-station premises were brought on-balance-sheet at IFRS 16 1 Apr 2022 transition (right-of-use asset + lease liability).",
        "beneficiaries": "Serves c. 6.2M East of England residents across Bedfordshire, Cambridgeshire, Essex, Hertfordshire, Norfolk and Suffolk; responds to c. 1.2M calls/yr; operates c. 130+ stations + standby points + 3 EOCs (Bedford, Norwich, Chelmsford); c. 5,300 WTE incl. paramedics, technicians, EOC call-handlers and HART team.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 (ch.7) · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IAS 17 (legacy)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.87M"},
            {"label": "Operational scale", "value": "c. 1.2M calls/yr; c. 130+ stations + standby points + 3 EOCs (Bedford, Norwich, Chelmsford); HART team for hazardous-area response"},
            {"label": "Population served", "value": "c. 6.2M East of England residents — Beds, Cambs, Essex, Herts, Norfolk, Suffolk (largest geographic ambulance trust by area)"},
            {"label": "Workforce", "value": "c. 5,300 WTE — paramedics, technicians, ECPs, EOC staff, HART, ECMO transfer team"},
            {"label": "Lease composition", "value": "Predominantly IFRS-16-exempt short-term + low-value categories — satellite station hot-desk space, MFDs, small operational equipment"},
            {"label": "Premises lease flow", "value": "Major station + EOC + fleet leases capitalised under IFRS 16 right-of-use + lease liability — flow appears in depreciation/finance cost lines, not here"},
            {"label": "IFRS 16 transition", "value": "1 Apr 2022 mandatory adoption — substantially reduced operating-lease P&L line"},
            {"label": "Funding trajectory", "value": "Stable to slight rise on RPI/CPI; residual sub-£1M reflects substantial premises + fleet shift to capitalised leases post-2022"},
            {"label": "Delivery body", "value": "EEAST Estates & Fleet + NHSPS for some leased sites + commercial fleet/MFD lease providers + co-location partners (police/fire stations)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Ambulance Programme + AACE (Association of Ambulance Chief Executives) + East of England regional commissioners"},
            {"label": "Evaluation evidence", "value": "EEAST ARA 2023-24; CQC provider profile (RYC); NAO ambulance services report; ORH benchmarks; AQI returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease P&L · Successor: post-2022 IFRS 16 capitalised + fleet electrification under NHS Net Zero 2032 + planned new-build EOCs"}
        ],
        "notes": "Following IFRS 16 mandatory adoption on 1 Apr 2022, EEAST's major emergency-ambulance fleet leases and station-premises leases were brought on-balance-sheet (right-of-use asset + lease liability), with depreciation + finance cost flowing through other lines. The residual £0.87M on this P&L line reflects IFRS-16-exempt short-term + low-value categories. EEAST is the largest English ambulance trust by geographic area, with a station network spanning six counties and three EOCs. Forward drivers include fleet electrification under NHS Net Zero 2032 (charge-points + EV ambulance trials), planned EOC consolidation, and the wider 'make-ready centre' procurement model that uses centralised hubs to prep ambulances for shift turnaround. EEAST has had repeated CQC and NHSE concerns over performance and culture in recent years — the lease line is small but the wider estate strategy is under review.",
        "sources": [
            {"publisher": "East of England Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastamb.nhs.uk/about-us/our-publications/annual-report-and-accounts.htm"},
            {"publisher": "Care Quality Commission", "title": "East of England Ambulance Service NHS Trust provider profile (RYC)", "url": "https://www.cqc.org.uk/provider/RYC"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "AACE", "title": "Association of Ambulance Chief Executives", "url": "https://aace.org.uk/"},
            {"publisher": "NHS England", "title": "Greener NHS — net zero", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["East of England Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Lease expenditure — East Midlands Ambulance Service NHS Trust", "Lease expenditure — South Central Ambulance Service NHS Foundation Trust", "NHS Property Services"]
    },
    "Business rates — Northamptonshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Northamptonshire Healthcare NHS Foundation Trust"}],
        "description": "NHFT's £0.86M non-domestic-rates bill covers business rates payable to West Northamptonshire and North Northamptonshire unitary councils on the trust's portfolio of community + mental-health sites including St Mary's Hospital Kettering, Berrywood Hospital (Northampton), Welland Centre, Avocet ward sites and a long tail of community-clinic and CMHT bases across Northamptonshire. NHFT is a combined community and mental-health trust serving the whole Northants population. Rates are paid under the Local Government Finance Act 1988 with rateable values from the VOA 2023 rating list.",
        "beneficiaries": "Serves c. 770,000 Northamptonshire residents (West Northants c. 425k + North Northants c. 360k); operates from c. 100+ owned and leased sites including Berrywood (Northampton), St Mary's (Kettering), Welland Centre, plus community clinics, CMHT bases and the secure forensic Welland service; c. 4,300 WTE incl. MH practitioners, district nurses, school nurses, AHPs.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.86M"},
            {"label": "Estate footprint", "value": "c. 100+ sites — Berrywood Hospital (Northampton MH), St Mary's Hospital (Kettering), Welland Centre + community clinics + CMHT bases"},
            {"label": "Population served", "value": "c. 770,000 — West Northants + North Northants unitary council areas"},
            {"label": "Workforce", "value": "c. 4,300 WTE — combined community + MH trust: MH practitioners, district nurses, school nurses, AHPs, learning disability"},
            {"label": "Billing authorities", "value": "West Northamptonshire Council + North Northamptonshire Council (post-2021 unitary reorganisation that abolished county council + districts)"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "NHFT Estates & Facilities + NHSPS for leased sites + West + North Northants billing authorities + VOA"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG + HM Treasury + DHSC + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "NHFT ARA 2023-24; CQC provider profile (RP1) — Outstanding rating; NHSE ERIC annual return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 Northamptonshire CC + 7 districts as billing authorities · Successor: post-2021 two unitaries simplified billing + 2026 VOA revaluation"}
        ],
        "notes": "NHFT is a combined community + mental-health foundation trust serving the whole Northamptonshire footprint, with Berrywood and St Mary's the two largest in-patient mental-health hospitals plus a long tail of community-clinic premises. The c. £0.86M rates bill spans both unitary council billing authorities created at the 2021 Northamptonshire local-government reorganisation (replacing the previous county + 7 district structure). Combined community/MH trusts have a more complex rateable footprint than pure community trusts because of inpatient mental-health sites with higher RVs. Drivers include the VOA 2023 list, annual multiplier uprating, the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 supplementary multiplier, and the 2026 VOA revaluation.",
        "sources": [
            {"publisher": "Northamptonshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nhft.nhs.uk/about-us/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Northamptonshire Healthcare NHS Foundation Trust provider profile (RP1)", "url": "https://www.cqc.org.uk/provider/RP1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Northamptonshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Norfolk Community Health and Care NHS Trust", "Business rates — Hertfordshire Community NHS Trust", "Valuation Office Agency"]
    },
    "Lease expenditure — Kent Community Health NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Kent Community Health NHS Foundation Trust"}],
        "description": "KCHFT's £0.85M lease-expenditure line covers IFRS 16 short-term and low-value lease exemptions plus residual operating-lease service-charge components — predominantly district-nursing pool-fleet vehicles, MFD/print devices, photocopiers and small operational equipment hire. Most premises leases (NHSPS occupations, GP-shared sites, council premises) and the major fleet leases were brought on-balance-sheet at IFRS 16 1 Apr 2022 transition (right-of-use asset + lease liability), so this P&L line is the residual exempt-categories charge rather than the full lease flow.",
        "beneficiaries": "Serves c. 1.6M Kent + Medway residents; operates from c. 70+ sites including community hospitals at Faversham, Hawkhurst, Tonbridge, Sevenoaks, Edenbridge, Sittingbourne; c. 5,200 WTE incl. district nurses, school nurses, health visitors and AHPs running a substantial mobile-fleet operation across rural east + south Kent.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 (ch.7) · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IAS 17 (legacy)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.85M"},
            {"label": "Estate + service footprint", "value": "c. 70+ sites + substantial mobile-fleet operation across rural Kent + Medway"},
            {"label": "Population served", "value": "c. 1.6M Kent + Medway residents"},
            {"label": "Workforce", "value": "c. 5,200 WTE — district nurses, school nurses, health visitors, AHPs, MIU staff"},
            {"label": "Lease composition", "value": "Predominantly IFRS-16-exempt short-term + low-value categories — district-nursing pool-fleet leases, MFDs, photocopiers, small operational kit"},
            {"label": "Premises lease flow", "value": "NHSPS occupations + GP-shared sites + council premises + major fleet leases capitalised under IFRS 16 right-of-use + lease liability — flow appears in depreciation/finance cost lines, not here"},
            {"label": "IFRS 16 transition", "value": "1 Apr 2022 mandatory adoption — substantially reduced operating-lease P&L line"},
            {"label": "Funding trajectory", "value": "Stable to slight rise on RPI/CPI; sub-£1M residual reflecting substantial premises + fleet shift to capitalised leases post-2022"},
            {"label": "Delivery body", "value": "KCHFT Estates & Facilities + Fleet team + NHSPS as principal landlord + commercial fleet/MFD lease providers"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury Financial Reporting Advisory Board (FRAB) + NHSE Provider Finance + Kent & Medway ICB"},
            {"label": "Evaluation evidence", "value": "KCHFT ARA 2023-24; CQC provider profile (RYY); NHSE ERIC annual return; lease commitments note in trust accounts"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease P&L treatment · Successor: post-2022 IFRS 16 capitalised + EV pool-fleet rollout under NHS Net Zero 2032"}
        ],
        "notes": "KCHFT runs a substantial mobile community-services operation across one of England's largest counties, so the underlying fleet + premises footprint is large — but post-1 Apr 2022 IFRS 16 transition the bulk of premises and fleet leases sit on-balance-sheet (right-of-use + lease liability) with depreciation + finance cost flowing through other lines, leaving £0.85M on this residual P&L line. The exempt categories cover short-term hot-desk arrangements, low-value office equipment and short-term vehicle hire. Forward drivers are EV pool-fleet rollout under NHS Net Zero 2032 (charge-points + EV district-nurse cars), periodic re-indexation of NHSPS occupation charges, and the broader Kent & Medway ICB integrated-care strategy reshaping community-services geography.",
        "sources": [
            {"publisher": "Kent Community Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kentcht.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Kent Community Health NHS Foundation Trust provider profile (RYY)", "url": "https://www.cqc.org.uk/provider/RYY"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury / FRAB", "title": "Application of IFRS 16 in central government", "url": "https://www.gov.uk/government/groups/financial-reporting-advisory-board"},
            {"publisher": "NHS Property Services", "title": "About NHSPS", "url": "https://www.property.nhs.uk/about-us/"},
            {"publisher": "NHS England", "title": "Greener NHS — net zero", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["Kent Community Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Herefordshire and Worcestershire Health and Care NHS Trust", "Lease expenditure — Northamptonshire Healthcare NHS Foundation Trust", "NHS Property Services"]
    },
    "Lease expenditure — East Midlands Ambulance Service NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "East Midlands Ambulance Service NHS Trust"}],
        "description": "EMAS's £0.83M lease-expenditure line covers IFRS 16 short-term and low-value lease exemptions plus residual operating-lease service-charge components — predominantly satellite ambulance station hot-desk leases, MFD/print devices and small operational equipment hire. EMAS runs c. 70 ambulance stations + community ambulance stations + 2 EOCs across Derbyshire, Nottinghamshire, Lincolnshire, Leicestershire, Northamptonshire and Rutland. Major emergency-ambulance fleet leases and large-station premises were brought on-balance-sheet at IFRS 16 1 Apr 2022 transition.",
        "beneficiaries": "Serves c. 4.8M East Midlands residents across Derbyshire, Nottinghamshire, Lincolnshire, Leicestershire, Northamptonshire and Rutland; responds to c. 1.0M+ calls/yr; operates c. 70 ambulance stations + community + standby points + 2 EOCs (Nottingham + Lincoln); c. 4,000 WTE incl. paramedics, technicians and EOC call-handlers.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 (ch.7) · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IAS 17 (legacy)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.83M"},
            {"label": "Operational scale", "value": "c. 1.0M+ calls/yr; c. 70 ambulance stations + community + standby points + 2 EOCs (Nottingham + Lincoln)"},
            {"label": "Population served", "value": "c. 4.8M East Midlands residents — Derbyshire, Notts, Lincs, Leics, Northants, Rutland"},
            {"label": "Workforce", "value": "c. 4,000 WTE — paramedics, technicians, ECPs, EOC staff, HART, ECMO transfer team"},
            {"label": "Lease composition", "value": "Predominantly IFRS-16-exempt short-term + low-value categories — satellite station hot-desk space, MFDs, small operational equipment"},
            {"label": "Premises lease flow", "value": "Major station + EOC + emergency-ambulance fleet leases capitalised under IFRS 16 right-of-use + lease liability — flow appears in depreciation/finance cost lines, not here"},
            {"label": "IFRS 16 transition", "value": "1 Apr 2022 mandatory adoption — substantially reduced operating-lease P&L line"},
            {"label": "Funding trajectory", "value": "Stable to slight rise on RPI/CPI; sub-£1M residual reflecting major premises + fleet shift to capitalised leases post-2022"},
            {"label": "Delivery body", "value": "EMAS Estates & Fleet + NHSPS for some leased sites + commercial fleet/MFD lease providers + co-location partners (police/fire stations)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Ambulance Programme + AACE + East Midlands ICBs"},
            {"label": "Evaluation evidence", "value": "EMAS ARA 2023-24; CQC provider profile (RX9); NAO ambulance services report; ORH benchmarks; AQI returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease P&L · Successor: post-2022 IFRS 16 capitalised + EOC consolidation under NHSE ambulance EOC review + fleet electrification under NHS Net Zero 2032"}
        ],
        "notes": "Following IFRS 16 mandatory adoption on 1 Apr 2022, EMAS's major emergency-ambulance fleet leases and station-premises leases were brought on-balance-sheet (right-of-use asset + lease liability), with depreciation + finance cost flowing through other lines. The residual £0.83M reflects IFRS-16-exempt short-term + low-value categories. EMAS spans the geographic East Midlands and operates two EOCs (Nottingham and Lincoln) — the EOC consolidation question and station-network rationalisation are live strategic questions following NHSE's review of ambulance EOC operating models. Forward drivers include fleet electrification under NHS Net Zero 2032 and 'make-ready centre' procurement.",
        "sources": [
            {"publisher": "East Midlands Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.emas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "East Midlands Ambulance Service NHS Trust provider profile (RX9)", "url": "https://www.cqc.org.uk/provider/RX9"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "AACE", "title": "Association of Ambulance Chief Executives", "url": "https://aace.org.uk/"},
            {"publisher": "NHS England", "title": "Greener NHS — net zero", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["East Midlands Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Lease expenditure — East of England Ambulance Service NHS Trust", "Lease expenditure — South Central Ambulance Service NHS Foundation Trust", "NHS Property Services"]
    },
    "Business rates — The Walton Centre NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Walton Centre NHS Foundation Trust"}],
        "description": "The Walton Centre's £0.82M non-domestic-rates bill covers business rates payable to Liverpool City Council on its specialist neurosciences hospital site at Lower Lane, Fazakerley (Liverpool) — the UK's only standalone specialist trust for neurology and neurosurgery. Rates are paid under the Local Government Finance Act 1988 multiplier system, with rateable values from the VOA 2023 rating list. The site includes inpatient neurology + neurosurgery wards, the regional Cheshire & Mersey neuro-rehabilitation unit, theatres, neuro-radiology and the academic-clinical infrastructure shared with University of Liverpool.",
        "beneficiaries": "Serves a tertiary neurosciences catchment of c. 3.5M across Cheshire, Merseyside, Lancashire, North Wales and the Isle of Man; the only standalone NHS specialist neurosciences trust in the UK; c. 92,000 outpatient attendances + c. 9,000 inpatient/day-case episodes; c. 1,600 WTE incl. specialist neurosurgery + neurology + neuro-rehab consultants.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.82M"},
            {"label": "Specialty footprint", "value": "UK's only standalone specialist neurosciences trust — Lower Lane Fazakerley site (Liverpool); neurology + neurosurgery + neuro-rehab"},
            {"label": "Annual activity", "value": "c. 92,000 outpatient attendances/yr; c. 9,000 inpatient/day-case episodes; c. 3.5M tertiary catchment Cheshire/Merseyside/Lancs/N Wales/IoM"},
            {"label": "Workforce", "value": "c. 1,600 WTE incl. specialist neurosurgery + neurology + neuro-rehab consultants + ICU + theatres"},
            {"label": "Billing authorities", "value": "Liverpool City Council (primary)"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "Walton Centre Estates & Facilities + Liverpool City Council billing authority + Valuation Office Agency"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG + HM Treasury + DHSC + NHSE Specialised Commissioning (specialist neurosciences)"},
            {"label": "Evaluation evidence", "value": "Walton Centre ARA 2023-24; CQC provider profile (RET) — Outstanding rating; NHSE Specialised Commissioning service spec; NHSE ERIC annual return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 VOA list · Successor: 2026 VOA revaluation + ongoing Walton Centre redevelopment programme + collaboration with neighbouring Aintree (LUHFT) acute trust"}
        ],
        "notes": "The Walton Centre is the UK's only standalone NHS specialist trust dedicated to neurology, neurosurgery and neuro-rehabilitation, holds an Outstanding CQC rating, and serves a 3.5M-population tertiary catchment from Liverpool's Fazakerley site. The c. £0.82M rates bill reflects a single-billing-authority occupation (Liverpool City Council) with the rateable value driven by the specialist tertiary scale + theatre/ITU intensity. NDR is paid in full with no NHS exemption. The site sits adjacent to Aintree Hospital (Liverpool University Hospitals NHS FT) on the north Liverpool campus and forms part of the wider Liverpool Health Partners academic-clinical network. Drivers include the VOA 2023 list, multiplier uprating, the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 supplementary multiplier, and ongoing capital investment in theatres + neuro-rehab capacity.",
        "sources": [
            {"publisher": "The Walton Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thewaltoncentre.nhs.uk/about-us/publications.htm"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "The Walton Centre NHS Foundation Trust provider profile (RET)", "url": "https://www.cqc.org.uk/provider/RET"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised commissioning — specialist neurosciences", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["The Walton Centre NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Business rates — The Royal Marsden NHS Foundation Trust", "Business rates — Sheffield Children's NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Birmingham Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Birmingham Community Healthcare NHS Foundation Trust"}],
        "description": "BCHC's £0.82M non-domestic-rates bill covers business rates payable principally to Birmingham City Council on the trust's portfolio of community clinics, community hospitals (Moseley Hall, West Heath), neighbourhood-team bases, dental clinics, learning-disability services and children's community sites across England's largest local authority area. Rates are paid under the Local Government Finance Act 1988 multiplier system, with rateable values from the VOA 2023 rating list. Some sites are NHSPS-leased or LIFT-procured (which carries its own service-charge route).",
        "beneficiaries": "Serves Birmingham's c. 1.15M residents (England's largest local authority area by population); operates from c. 230+ sites including LIFT-procured neighbourhood clinics, district-nursing bases, dental clinics and Moseley Hall + West Heath community hospitals; c. 5,400 WTE incl. district nurses, AHPs, dental services, learning disability + children's community services.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.82M"},
            {"label": "Estate footprint", "value": "c. 230+ sites — Moseley Hall + West Heath community hospitals + community + dental clinics + neighbourhood-team bases + LIFT-procured premises"},
            {"label": "Population served", "value": "c. 1.15M Birmingham residents (England's largest local authority area by population)"},
            {"label": "Workforce", "value": "c. 5,400 WTE — district nurses, AHPs, school nurses, health visitors, learning disability, dental, children's community services"},
            {"label": "Billing authorities", "value": "Birmingham City Council (primary)"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "BCHC Estates & Facilities + NHSPS for leased sites + LIFTCo for LIFT-procured premises + Birmingham City Council billing authority + VOA"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG + HM Treasury + DHSC + Birmingham & Solihull ICB"},
            {"label": "Evaluation evidence", "value": "BCHC ARA 2023-24; CQC provider profile (RYW); NHSE ERIC annual return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era estate · Successor: 2026 VOA revaluation + ongoing estate consolidation under Three Shifts community-care policy + Birmingham City Council Section 114 financial-distress context for billing authority"}
        ],
        "notes": "BCHC pays full NDR with no NHS exemption on its c. 230+ Birmingham sites. The c. £0.82M bill reflects Birmingham's large but provincially-priced rateable footprint (lower than central London but with multiple substantial community-clinic and community-hospital occupations). The line interacts with the trust's separate £0.94M PFI/LIFT charges line because LIFT-procured sites typically include service-charge pass-throughs that may pick up rates. Birmingham City Council issued a Section 114 notice in late 2023 reflecting LA financial distress — this affects the billing-authority side rather than the trust's liability but raises questions on local NDR retention and reform. Drivers include VOA 2023 list, multiplier uprating, and the supplementary multiplier under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024.",
        "sources": [
            {"publisher": "Birmingham Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bhamcommunity.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Birmingham Community Healthcare NHS Foundation Trust provider profile (RYW)", "url": "https://www.cqc.org.uk/provider/RYW"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Birmingham Community Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Central London Community Healthcare NHS Trust", "PFI / LIFT charges — Birmingham Community Healthcare NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "YAS's £0.80M non-domestic-rates bill covers business rates payable to multiple Yorkshire local authorities (Leeds, Sheffield, Bradford, Wakefield, York, Kirklees, Calderdale, Doncaster, Rotherham, Barnsley, North Yorkshire) on c. 60 ambulance stations + standby points + 3 EOCs (Wakefield, Rotherham, York), Make Ready Centres and the Ascot Drive HQ in Wakefield. Rates are paid under the Local Government Finance Act 1988 multiplier system, with rateable values from the VOA 2023 rating list. YAS also runs the NHS 111 service for Yorkshire under contract.",
        "beneficiaries": "Serves c. 5.5M Yorkshire residents across West, South, East and North Yorkshire and the Humber; responds to c. 1.0M+ ambulance calls/yr + c. 2.5M+ NHS 111 calls/yr; operates c. 60 ambulance stations + standby points + 3 EOCs (Wakefield, Rotherham, York) + Make Ready Centres; c. 6,500 WTE incl. paramedics, technicians, EOC + 111 staff and PTS team.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.80M"},
            {"label": "Operational scale", "value": "c. 1.0M+ ambulance calls/yr + c. 2.5M+ NHS 111 calls/yr (YAS holds the regional 111 contract); c. 60 stations + Make Ready Centres + 3 EOCs"},
            {"label": "Population served", "value": "c. 5.5M Yorkshire + Humber residents — West, South, East + North Yorkshire"},
            {"label": "Workforce", "value": "c. 6,500 WTE — paramedics, technicians, EOC, 111 call advisors, PTS, HART"},
            {"label": "Billing authorities", "value": "Multiple Yorkshire authorities: Leeds, Sheffield, Bradford, Wakefield, York, Kirklees, Calderdale, Doncaster, Rotherham, Barnsley, North Yorkshire (unitary 2023)"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption); ambulance stations modest RVs vs hospitals"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "YAS Estates + Fleet team + relevant Yorkshire billing authorities + VOA"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG + HM Treasury + DHSC + NHSE Ambulance Programme + Yorkshire ICBs (West, South, North + Humber & North Yorks)"},
            {"label": "Evaluation evidence", "value": "YAS ARA 2023-24; CQC provider profile (RX8); NAO ambulance services report; ORH benchmarks; AQI returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 North Yorks county + districts (now North Yorks unitary from Apr 2023) · Successor: 2026 VOA revaluation + Make Ready Centre estate consolidation + EOC review under NHSE ambulance EOC operating model review"}
        ],
        "notes": "YAS pays full NDR on its c. 60 ambulance stations + standby points + 3 EOCs spread across the Yorkshire footprint. The c. £0.80M bill is modest relative to acute hospitals because ambulance-station RVs are small individually, but the multi-billing-authority spread (especially after North Yorkshire's April 2023 unitary reorganisation) creates administrative complexity. YAS uniquely also runs the NHS 111 contract for Yorkshire (most ambulance trusts don't), so its EOC + call-centre footprint is larger than peers. Make Ready Centre consolidation (centralised vehicle prep hubs replacing decentralised station prep) is reshaping the rateable footprint over the cycle. Drivers include the VOA 2023 list, multiplier uprating, the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 supplementary multiplier, and the 2026 VOA revaluation.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Yorkshire Ambulance Service NHS Trust provider profile (RX8)", "url": "https://www.cqc.org.uk/provider/RX8"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"}
        ],
        "related": ["Yorkshire Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Business rates — London Ambulance Service NHS Trust", "Business rates — North West Ambulance Service NHS Trust", "Valuation Office Agency"]
    },
}
