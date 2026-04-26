# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 05 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "General supplies & services — Bradford District Care NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Bradford District Care NHS Foundation Trust"}],
        "description": "Bradford District Care's £1.77M general supplies & services line covers non-drug clinical and non-clinical consumables — ward bedding, single-use clinical kit, PPE, dressings, sharps boxes, infection-control cleaning consumables and CAMHS therapy materials — across Lynfield Mount Hospital, Airedale Centre for Mental Health and the trust's c. 60+ community sites. It excludes drugs (separately disclosed) but captures most ward-running consumables for a high-throughput community + acute-MH provider.",
        "beneficiaries": "Consumables consumed by c. 3,500 substantive WTE staff supporting c. 700,000 residents of Bradford, Airedale, Wharfedale and Craven across acute MH wards, CAMHS, IAPT (NHS Talking Therapies), district-nursing, health-visiting and school-nursing services.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 · Health and Social Care Act 2008 (Hygiene Code)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£1.77M"},
            {"label": "Composition", "value": "Bedding + ward consumables + PPE + dressings + sharps + cleaning consumables + CAMHS therapy materials"},
            {"label": "Site footprint", "value": "Lynfield Mount Hospital + Airedale CMH + c. 60 community sites (district-nursing, CAMHS, IAPT)"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework (majority) + local contracts for specialist therapy + CAMHS materials"},
            {"label": "PPE legacy unwind", "value": "2020-22 COVID-era PPE inventory drawn down; ward consumables now back to BAU run-rate"},
            {"label": "Headcount served", "value": "c. 3,500 substantive WTE"},
            {"label": "Population served", "value": "c. 700,000 across Bradford district + Airedale + Craven + Wharfedale"},
            {"label": "Funding trajectory", "value": "2020-21 PPE-inflated peak → 2022-23 normalisation → 2024-25 £1.77M tracking activity + CPI"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Infection Prevention & Control teams; NHS Supply Chain (national)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + West Yorkshire ICB · IAS 2 + GAM disclosure"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; NHSE Model Hospital consumables benchmarking"},
            {"label": "Predecessor / successor", "value": "Predecessor: COVID-era PPE-inflated supplies line · Successor: Frontline Digitisation EPR + procurement-rationalisation under WY ICB"}
        ],
        "notes": "Bradford District Care's general supplies line normalised after the COVID-era PPE peak (2020-21 ran at multiples of BAU), with 2024-25 reflecting steady-state ward and community consumables. The trust's combined MH + community + CAMHS + district-nursing remit means the line has to fund a wider mix than MH-only peers — district-nursing dressings and infection-control consumables sit alongside ward-running kit at Lynfield Mount. NHS Supply Chain provides the bulk via national framework, with West Yorkshire ICB pursuing further procurement rationalisation. The CAMHS service generates atypical therapy-material spend (sensory, art-therapy, play-therapy) not seen on adult MH wards.",
        "sources": [
            {"publisher": "Bradford District Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bdct.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Clinical consumables framework + Model Hospital data", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS England", "title": "Model Hospital — community + mental health benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bradford District Care NHS FT provider profile (RT5)", "url": "https://www.cqc.org.uk/provider/RT5"}
        ],
        "related": ["Bradford District Care NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "NHS Supply Chain", "General supplies & services — Cheshire and Wirral Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Lincolnshire Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Lincolnshire Partnership NHS Foundation Trust"}],
        "description": "Lincolnshire Partnership's £1.76M establishment line covers stationery, postage, telephony, mobile devices, printing and courier across Peter Hodgkinson Centre (Lincoln), Hartsholme (Lincoln), Witham Court (Lincoln), Ash Villa (Sleaford), Manthorpe Centre (Grantham) and the trust's geographically dispersed community-MH bases serving Lincolnshire's largely rural footprint. Postage and courier sit higher than urban-MH peers because of the catchment geography across England's fourth-largest county.",
        "beneficiaries": "c. 2,800 staff serving c. 770,000 residents across Lincolnshire (England's 4th largest ceremonial county at c. 6,950 km²); covers acute MH inpatients, CAMHS, IAPT, perinatal MH, eating-disorder service, and learning-disability community-MH across c. 40 sites.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.76M"},
            {"label": "Site footprint", "value": "Peter Hodgkinson Centre + Hartsholme + Witham Court + Ash Villa (Sleaford) + Manthorpe (Grantham) + c. 35 community bases"},
            {"label": "Catchment area", "value": "c. 6,950 km² across Lincolnshire — England's 4th largest ceremonial county"},
            {"label": "Headcount served", "value": "c. 2,800 substantive WTE"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying"},
            {"label": "Rural-geography premium", "value": "Postage + courier per WTE elevated vs urban-MH peers due to dispersed community-MH footprint"},
            {"label": "Mobile-device estate", "value": "Sustained laptop + smartphone rollout for community-MH + CAMHS staff working across Lincolnshire"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (stationery + IT consumables) + Crown Commercial Service telephony + local courier contracts"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.3M → 2024-25 £1.76M — uplift tracking community mobile-working + CPI + telephony rebasing"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Lincolnshire ICB · DHSC GAM disclosure rules"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paper-heavy admin model · Successor: Lincolnshire ICS shared-services + Frontline Digitisation EPR"}
        ],
        "notes": "Lincolnshire Partnership's establishment line is structurally elevated by the rural-geography premium — Lincolnshire is England's 4th-largest ceremonial county and the trust serves dispersed populations from Mablethorpe to Stamford, generating per-WTE postage, courier and mobile-device costs above urban-MH peers. Sustained investment since 2020 in laptops, smartphones and MiFi for community staff has pushed the device estate higher; the Lincolnshire ICS is exploring shared-services consolidation but progress is slowed by the system's predominantly rural and non-foundation provider mix. The Frontline Digitisation EPR programme (Rio replacement) is the medium-term lever to flatten print and postage but will raise licensing.",
        "sources": [
            {"publisher": "Lincolnshire Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lpft.nhs.uk/about-us/publications-and-policies/annual-reports"},
            {"publisher": "NHS England", "title": "Model Hospital — mental health benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Lincolnshire Partnership NHS FT provider profile (RP7)", "url": "https://www.cqc.org.uk/provider/RP7"},
            {"publisher": "Lincolnshire ICB", "title": "Integrated care strategy + estates review", "url": "https://lincolnshire.icb.nhs.uk/"}
        ],
        "related": ["Lincolnshire Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Norfolk and Suffolk NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Transport (business + patient) — West London NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "West London NHS Trust"}],
        "description": "West London NHS Trust's £1.73M transport line covers staff business mileage and contracted patient transfers between Broadmoor Hospital (high-secure, Crowthorne), the West London Forensic Service (medium/low-secure), St Bernard's Hospital site (Southall), the Lakeside MH Unit and dozens of community bases across Ealing, Hammersmith & Fulham and Hounslow. Broadmoor's high-secure regime drives an unusual share of escorted-transfer cost — every off-site movement requires accredited secure-transport with multiple escorts.",
        "beneficiaries": "c. 4,500 staff serving c. 850,000 residents across Ealing, Hammersmith & Fulham and Hounslow plus a national high-secure cohort of c. 200 patients at Broadmoor Hospital; secure-services catchment includes London + South of England.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance + secure-transfer) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.73M"},
            {"label": "Site footprint generating transfers", "value": "Broadmoor Hospital (high-secure) + St Bernard's + Lakeside MHU + community bases across 3 W London boroughs"},
            {"label": "Broadmoor escorted-transfer premium", "value": "Every off-site movement (court, healthcare, family) requires accredited secure-transport with multi-escort cordon"},
            {"label": "Bed-stock generating transfers", "value": "c. 200 high-secure beds (Broadmoor) + medium/low-secure forensic + acute MH"},
            {"label": "MHA conveyance share", "value": "s.136 + s.135 contracted via LAS + private secure-transport providers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "Pool car + lease fleet", "value": "Crown Commercial Service vehicle framework; ULEZ + Mayor's Net Zero adding EV transition pressure"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.2M → 2024-25 £1.73M — uplift driven by post-pandemic activity recovery + secure-transfer cost inflation + ULEZ"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS + secure-transport contracted with LAS + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Specialised Commissioning (high-secure) + NW London ICB + Frimley ICB (Broadmoor)"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports; HMPPS / NHSE high-secure standards; Mazars-style transparency in NHSE specialist commissioning"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 Broadmoor old-build secure-transport regime · Successor: NHSE specialised-commissioning consolidated secure-transport framework + EV transition"}
        ],
        "notes": "West London NHS Trust's transport line is dominated by Broadmoor Hospital — England's oldest high-secure psychiatric institution, where every off-site patient movement (NHS healthcare, court appearance, family contact) requires accredited secure-transport with a multi-staff escort cordon, generating per-journey costs many multiples of standard PTS. The 2019 Broadmoor new-build relocation reduced some intra-site transfer cost but the high-secure regime persists. Beyond Broadmoor, the trust's W London community footprint generates routine AMHP and crisis-team mileage; ULEZ and Mayor's Net Zero have added EV-transition cost pressure. NHSE specialised commissioning is moving toward consolidated secure-transport frameworks across the high-secure estate (Broadmoor, Ashworth, Rampton).",
        "sources": [
            {"publisher": "West London NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.westlondon.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England Specialised Commissioning", "title": "High-secure mental health services policy", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Care Quality Commission", "title": "West London NHS Trust provider profile (RKL)", "url": "https://www.cqc.org.uk/provider/RKL"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "London Ambulance Service NHS Trust", "title": "PTS contract data + s.136 conveyance protocols", "url": "https://www.londonambulance.nhs.uk/"}
        ],
        "related": ["West London NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Mental Health Act 1983", "Transport (business + patient) — Greater Manchester Mental Health NHS Foundation Trust", "NHS England Specialised Commissioning"]
    },
    "Lease expenditure — Essex Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Essex Partnership University NHS Foundation Trust"}],
        "description": "EPUT's £1.73M lease line covers IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio includes NHSPS-leased community-MH clinics across Essex, CHP LIFT-vehicle leases, and ancillary leased space adjacent to Rochford, Basildon and Linden Centre (Chelmsford). The Lampard Inquiry into Essex MH deaths (2014-2023) is the trust's defining context — leased estate has been under sustained scrutiny as part of the inquiry's remit.",
        "beneficiaries": "c. 5,500 staff serving c. 2.5M residents across Essex (Mid Essex, North East Essex, South East Essex, West Essex, Bedfordshire, Luton, Suffolk where applicable); c. 80+ leased community-MH clinics + ancillary spaces.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.73M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability"},
            {"label": "Leased site count", "value": "c. 80+ NHSPS + CHP-LIFT premises across Essex (community-MH, IAPT, CAMHS, perinatal)"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service charge — feeds annual lease volatility"},
            {"label": "Lampard Inquiry context", "value": "Statutory inquiry into Essex MH deaths (2000-2023) — placed estate condition + community footprint under sustained scrutiny"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.9M → 2022-23 c. £1.5M ROU first year → 2024-25 £1.73M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Mid and South Essex ICB + Suffolk and North East Essex ICB · IFRS 16 / GAM ch.7 oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: Lampard Inquiry recommendations + Essex ICS estate consolidation"}
        ],
        "notes": "EPUT's lease line carries the IFRS 16 transition step-up (2022 reclassification of operating leases on-balance-sheet) plus the structural uplift from a community-MH footprint spanning all of Essex and parts of Bedfordshire and Suffolk. The Lampard Inquiry — the statutory inquiry into c. 2,000 mental-health deaths under EPUT and predecessor trusts 2000-2023 — has placed the trust's leased estate, ward conditions and community-clinic accessibility under sustained public scrutiny. The NHSPS / MH-trust market-rent dispute affects EPUT particularly because of the dispersed community-clinic footprint. Mid and South Essex ICB is exploring estate rationalisation but progress is constrained by the inquiry timeline and remediation programme.",
        "sources": [
            {"publisher": "Essex Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://eput.nhs.uk/about-us/publications-and-policies/"},
            {"publisher": "Lampard Inquiry", "title": "Independent Inquiry into Mental Health Deaths in Essex (terms of reference + reports)", "url": "https://lampardinquiry.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "EPUT inspection reports (RWN)", "url": "https://www.cqc.org.uk/provider/RWN"}
        ],
        "related": ["Essex Partnership University NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Mersey Care NHS Foundation Trust", "Lampard Inquiry"]
    },
    "General supplies & services — Cheshire and Wirral Partnership NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Cheshire and Wirral Partnership NHS Foundation Trust"}],
        "description": "CWP's £1.72M general supplies & services line covers ward-running consumables, PPE, dressings, sharps, infection-control cleaning consumables and CAMHS therapy materials across Bowmere Hospital (Chester), Springview (Wirral), Soss Moss Hospital (LD), Millbrook (Macclesfield) and the trust's community-MH bases across Cheshire West, Cheshire East, Wirral and Trafford. The combined MH + LD specialist remit drives a diverse consumables mix.",
        "beneficiaries": "c. 3,400 staff serving c. 1.0M residents across Cheshire West, Cheshire East, Wirral plus specialist LD service; c. 250 inpatient MH + LD beds plus dispersed community-MH and CAMHS sites.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 · Health and Social Care Act 2008 (Hygiene Code)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£1.72M"},
            {"label": "Composition", "value": "Bedding + ward consumables + PPE + dressings + sharps + cleaning consumables + CAMHS + LD therapy materials"},
            {"label": "Site footprint", "value": "Bowmere Hospital + Springview + Soss Moss (LD) + Millbrook + community bases"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework (majority) + local contracts for LD + CAMHS specialist materials"},
            {"label": "PPE legacy unwind", "value": "2020-22 COVID-era PPE drawn down; ward consumables now back to BAU"},
            {"label": "Headcount served", "value": "c. 3,400 substantive WTE"},
            {"label": "Population served", "value": "c. 1.0M across Cheshire + Wirral + LD specialist catchment"},
            {"label": "LD specialist driver", "value": "Soss Moss Hospital + LD community service generates atypical consumables (specialist seating, communication aids, sensory)"},
            {"label": "Funding trajectory", "value": "2020-21 PPE-inflated peak → 2022-23 normalisation → 2024-25 £1.72M tracking activity + CPI"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IPC teams; NHS Supply Chain (national)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cheshire and Merseyside ICB · IAS 2 + GAM disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: COVID-era PPE-inflated baseline · Successor: Cheshire & Merseyside ICS procurement consolidation"}
        ],
        "notes": "CWP's general supplies line carries an unusual LD-specialist footprint — Soss Moss Hospital and the trust's wider LD community service generate consumables atypical of MH-only providers (specialist seating, communication aids, sensory equipment, swallowing supplies). The line normalised after the COVID-era PPE peak and now reflects steady-state ward + community consumables. Cheshire and Merseyside ICS is pursuing procurement consolidation across MH + acute providers; CWP benefits from NHS Supply Chain national volumes for the bulk but retains local contracts for specialist LD therapy materials and CAMHS sensory kit. Frontline Digitisation EPR rollout will further drive procurement-data integration.",
        "sources": [
            {"publisher": "Cheshire and Wirral Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cwp.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS Supply Chain", "title": "Clinical consumables framework + Model Hospital data", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS England", "title": "Model Hospital — mental health benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Cheshire and Wirral Partnership NHS FT provider profile (RXA)", "url": "https://www.cqc.org.uk/provider/RXA"}
        ],
        "related": ["Cheshire and Wirral Partnership NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "NHS Supply Chain", "General supplies & services — Bradford District Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Mersey Care NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Mersey Care NHS Foundation Trust"}],
        "description": "Mersey Care's £1.71M transport line covers staff business mileage and inter-site patient transfers across Ashworth Hospital (high-secure), the Whalley Edenfield-equivalent secure-services site, Rowan View medium-secure (Maghull, opened 2023), Clock View (Liverpool), Hollins Park (Warrington) and dozens of community-MH + physical-health bases across Liverpool, Sefton, Knowsley, St Helens, Halton and Warrington. Ashworth's high-secure regime drives escorted-transfer cost for off-site movements.",
        "beneficiaries": "c. 9,000 staff serving c. 1.5M residents across Liverpool City Region; high-secure men's service at Ashworth Hospital is a national specialist resource for c. 200 patients; community + physical-health remit adds district-nursing mileage on top of MH crisis-team travel.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance + secure-transfer) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.71M"},
            {"label": "Site footprint generating transfers", "value": "Ashworth Hospital (high-secure) + Rowan View MSU (146 beds, Maghull, 2023) + Clock View + Hollins Park + community bases"},
            {"label": "Ashworth escorted-transfer premium", "value": "Off-site movements (court, healthcare) require accredited secure-transport with multi-staff cordon"},
            {"label": "Bed-stock generating transfers", "value": "c. 200 high-secure (Ashworth) + 146 medium-secure (Rowan View) + acute MH + community"},
            {"label": "MHA conveyance share", "value": "s.136 + s.135 contracted via NWAS + private secure-transport providers"},
            {"label": "Combined remit driver", "value": "MH + LD + community physical-health → district-nursing mileage adds to MH crisis-team travel base"},
            {"label": "Liverpool City Region context", "value": "Mayoral combined authority transport pooling discussions; Clean Air Zone in Liverpool city centre"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.0M → 2024-25 £1.71M — uplift driven by Rowan View opening 2023 + post-pandemic recovery + fuel CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with NWAS + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Specialised Commissioning (Ashworth high-secure) + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports; NHSE high-secure standards; Liverpool City Region transport strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 MSU footprint · Successor: NHSE specialised-commissioning consolidated secure-transport framework + EV transition"}
        ],
        "notes": "Mersey Care's transport line is structurally elevated by the Ashworth Hospital high-secure regime — every off-site movement (NHS healthcare, court appearances, family contact) requires accredited secure-transport with a multi-staff escort cordon. The 2023 opening of Rowan View medium-secure unit at Maghull (146 beds) added inter-site transfer volumes between the secure estate and community step-down sites. Beyond secure services, the trust's combined MH + LD + community physical-health remit means district-nursing and community-physical-health teams add to the staff-mileage base. Liverpool City Region's mayoral transport pooling discussions and the Liverpool Clean Air Zone are medium-term levers; EV transition is constrained by the secure-transport accreditation requirements.",
        "sources": [
            {"publisher": "Mersey Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.merseycare.nhs.uk/about-us/our-publications/annual-report-and-accounts"},
            {"publisher": "NHS England Specialised Commissioning", "title": "High-secure mental health services policy", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Care Quality Commission", "title": "Mersey Care NHS FT provider profile (RW4)", "url": "https://www.cqc.org.uk/provider/RW4"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "North West Ambulance Service NHS Trust", "title": "PTS contract data + s.136 conveyance protocols", "url": "https://www.nwas.nhs.uk/"}
        ],
        "related": ["Mersey Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Mental Health Act 1983", "Transport (business + patient) — Greater Manchester Mental Health NHS Foundation Trust", "NHS England Specialised Commissioning"]
    },
    "General supplies & services — Pennine Care NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Pennine Care NHS Foundation Trust"}],
        "description": "Pennine Care's £1.70M general supplies & services line covers ward consumables, PPE, dressings, sharps, infection-control cleaning consumables and CAMHS therapy materials across the Tameside, Stockport, Bury, Oldham and Rochdale community-MH footprint plus inpatient wards at Birch Hill (Rochdale), Hyde, Tameside and Stockport. The trust is a community-MH-only provider (since 2020 LCO transfers) so the line skews toward community + crisis consumables rather than acute-ward kit.",
        "beneficiaries": "c. 3,500 staff serving c. 1.3M residents across the 5 Greater Manchester boroughs (Tameside, Stockport, Bury, Oldham, Rochdale); CAMHS, IAPT (NHS Talking Therapies), perinatal MH, eating-disorder + community adult MH service.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 · Health and Social Care Act 2008 (Hygiene Code)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£1.70M"},
            {"label": "Composition", "value": "Bedding + ward consumables + PPE + dressings + sharps + cleaning + CAMHS therapy materials"},
            {"label": "Site footprint", "value": "Birch Hill (Rochdale) + Hyde + Tameside + Stockport + community bases across 5 GM boroughs"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework (majority) + GM Health & Social Care Partnership consolidated procurement"},
            {"label": "PPE legacy unwind", "value": "2020-22 COVID-era PPE drawn down; ward consumables back to BAU"},
            {"label": "Headcount served", "value": "c. 3,500 substantive WTE"},
            {"label": "Population served", "value": "c. 1.3M across 5 GM boroughs"},
            {"label": "Community-only model", "value": "Since 2020 LCO transfers, trust is community-MH-only — no acute-physical-health ward consumables; CAMHS + crisis-team mix dominates"},
            {"label": "Funding trajectory", "value": "2020-21 PPE-inflated peak → 2022-23 normalisation → 2024-25 £1.70M tracking activity + CPI"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IPC teams; NHS Supply Chain (national) + GM HSCP regional"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Greater Manchester ICB · IAS 2 + GAM disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 LCO acute-physical-health consumables included · Successor: GM ICS procurement consolidation + Frontline Digitisation EPR"}
        ],
        "notes": "Pennine Care's general supplies line reflects its community-MH-only footprint since the 2020 Local Care Organisation transfers, when acute-physical-health functions in Tameside, Stockport, Bury, Oldham and Rochdale moved out — leaving consumables skewed toward community + crisis + CAMHS use rather than acute-ward kit. The line normalised after the COVID-era PPE peak. GM Health & Social Care Partnership (and now GM ICB) drive procurement consolidation across MH + acute providers, giving Pennine Care access to GM-scale volumes on top of NHS Supply Chain national framework. CAMHS therapy materials (sensory, art, play) are an atypical component of the line.",
        "sources": [
            {"publisher": "Pennine Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.penninecare.nhs.uk/aboutus/publications-policies"},
            {"publisher": "NHS Supply Chain", "title": "Clinical consumables framework + Model Hospital data", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Greater Manchester Integrated Care", "title": "Health and Social Care Partnership procurement", "url": "https://www.gmintegratedcare.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Pennine Care NHS FT provider profile (RT2)", "url": "https://www.cqc.org.uk/provider/RT2"}
        ],
        "related": ["Pennine Care NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "NHS Supply Chain", "General supplies & services — Cheshire and Wirral Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Birmingham and Solihull Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Birmingham and Solihull Mental Health NHS Foundation Trust"}],
        "description": "BSMHFT's £1.70M amortisation line covers depreciation of capitalised intangibles — primarily the Rio EPR + supporting clinical software, capitalised training, e-prescribing modules and licensed-software stack used by the trust's c. 4,000 staff. The Frontline Digitisation programme funded EPR upgrades since 2023, increasing capitalised intangible balances and feeding the amortisation line. BSMHFT's footprint includes the Reaside Clinic medium-secure forensic service, Ardenleigh forensic CAMHS and Birmingham + Solihull community-MH bases.",
        "beneficiaries": "c. 4,000 staff using the EPR + capitalised software stack across Reaside Clinic, Ardenleigh, the Zinnia Centre, Oleaster (Edgbaston), Mary Seacole House and dozens of community-MH sites; serves c. 1.3M residents of Birmingham and Solihull plus regional secure-services catchment.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation funding programme",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.70M"},
            {"label": "Composition", "value": "EPR (Rio) + clinical-software + e-prescribing + licensed software amortisation"},
            {"label": "Frontline Digitisation context", "value": "Programme funded EPR + digital-maturity uplift 2023-25 — capitalised intangible balances stepped up"},
            {"label": "Useful-life range", "value": "Software 3-5 years (typical) per IAS 38 + DHSC GAM ch.5"},
            {"label": "Site footprint", "value": "Reaside Clinic (medium-secure) + Ardenleigh (forensic CAMHS) + Zinnia + Oleaster + Mary Seacole + community bases"},
            {"label": "Headcount served", "value": "c. 4,000 substantive WTE"},
            {"label": "Population served", "value": "c. 1.3M Birmingham + Solihull plus regional secure-services catchment"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.9M → 2024-25 £1.70M — uplift driven by Frontline Digitisation EPR + e-prescribing capitalisation"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams; NHSE Frontline Digitisation Programme funding"},
            {"label": "Policy owner", "value": "DHSC + NHSE Digital Transformation + Birmingham and Solihull ICB · IAS 38 / GAM ch.5"},
            {"label": "Evaluation evidence", "value": "NHSE digital maturity assessment; Frontline Digitisation milestone reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD EPR baseline · Successor: federated-data-platform + AI clinical-decision-support amortisation post-2026"}
        ],
        "notes": "BSMHFT's amortisation line reflects the Frontline Digitisation programme's impact on the trust's capitalised intangibles balance — Rio EPR upgrades, e-prescribing modules and digital-maturity uplift since 2023 have been capitalised and now flow through amortisation over 3-5 year useful lives. The trust runs Reaside Clinic and Ardenleigh forensic services that require additional security-focused EPR modules. Birmingham and Solihull ICB's digital strategy and the regional NHS Confederation's data programme will drive further capitalised intangibles over 2025-27, sustaining the amortisation trajectory. The federated data platform rollout and AI clinical-decision-support modules are expected to drive the next step-up.",
        "sources": [
            {"publisher": "Birmingham and Solihull Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bsmhft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme — mental health trusts", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "Care Quality Commission", "title": "BSMHFT provider profile (RXT)", "url": "https://www.cqc.org.uk/provider/RXT"}
        ],
        "related": ["Birmingham and Solihull Mental Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Frontline Digitisation programme", "Amortisation — Oxford Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Oxleas NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Oxleas NHS Foundation Trust"}],
        "description": "Oxleas's £1.66M lease line covers IFRS 16 right-of-use depreciation + interest on the leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHSPS-leased community-MH clinics and physical-health bases across Bexley, Bromley and Greenwich plus prison healthcare ancillary leased space (Oxleas runs healthcare in HMP Belmarsh, HMP Isis, HMP Thameside, HMP Wandsworth and other London prisons). The combined MH + community + prison-healthcare remit drives an unusually diverse leased footprint.",
        "beneficiaries": "c. 4,500 staff serving c. 800,000 residents across Bexley, Bromley and Greenwich plus prison-healthcare populations across multiple London prisons; c. 70+ leased community-MH + physical-health + prison-ancillary premises.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Health and Social Care Act 2012 (prison healthcare commissioning)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.66M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability"},
            {"label": "Leased site count", "value": "c. 70+ NHSPS + private + prison-ancillary premises"},
            {"label": "Prison-healthcare contracts", "value": "HMP Belmarsh, HMP Isis, HMP Thameside, HMP Wandsworth + others — generates ancillary leased space"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords + HMPPS"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service charge"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; prison-healthcare contract terms tied to NHSE commissioning cycles"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.8M → 2022-23 c. £1.4M ROU first year → 2024-25 £1.66M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT + HMPPS for prison-healthcare estate"},
            {"label": "Policy owner", "value": "DHSC + NHSE Health and Justice Commissioning + South East London ICB · IFRS 16 / GAM ch.7"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: SE London ICS estate consolidation + NHSE prison-healthcare recommissioning"}
        ],
        "notes": "Oxleas's lease line carries the IFRS 16 transition step-up plus the unusual structural overlay from prison healthcare — Oxleas is one of England's largest prison-healthcare providers, running services across HMP Belmarsh, HMP Isis, HMP Thameside, HMP Wandsworth and others, generating ancillary leased space (training, administration, custodial-staff facilities) outside the core HMPPS-owned secure estate. The NHSPS / MH-trust market-rent dispute affects Oxleas's community-MH clinic footprint across Bexley, Bromley and Greenwich. SE London ICS estate consolidation is the medium-term lever; NHSE Health and Justice prison-healthcare recommissioning cycles drive lease-term volatility on the prison-ancillary portfolio.",
        "sources": [
            {"publisher": "Oxleas NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://oxleas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England Health and Justice", "title": "Prison healthcare commissioning policy", "url": "https://www.england.nhs.uk/commissioning/health-just/"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Oxleas NHS FT provider profile (RPG)", "url": "https://www.cqc.org.uk/provider/RPG"}
        ],
        "related": ["Oxleas NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Mersey Care NHS Foundation Trust", "NHS England Health and Justice"]
    },
    "Business rates — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust"}],
        "description": "CNTW's £1.64M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on a geographically vast estate covering Northumberland, Tyne and Wear, North Cumbria and parts of County Durham. Major hereditaments include St Nicholas Hospital (Newcastle), Hopewood Park (Sunderland), St George's Park (Morpeth), the Hadrian Clinic and dozens of community-MH and CAMHS bases across one of England's largest geographical MH-trust catchments.",
        "beneficiaries": "Approximately 90+ occupied hereditaments across Northumberland, Newcastle, North Tyneside, South Tyneside, Sunderland, Gateshead, North Cumbria + County Durham; serves c. 1.7M residents plus regional secure-services + neuro-rehabilitation specialist catchment.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.64M"},
            {"label": "Hereditament count", "value": "c. 90+ occupied sites across CNTW footprint"},
            {"label": "Geographic spread", "value": "Northumberland + Newcastle + North Tyneside + South Tyneside + Sunderland + Gateshead + N Cumbria + Co Durham"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "VOA 2023 revaluation impact", "value": "North East commercial RVs broadly stable post-pandemic; CNTW liability roughly unchanged"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Specialist services driving RV", "value": "Hopewood Park (Hopewood House MSU) + Hadrian Clinic + neuro-rehabilitation services drive higher per-m² RV than community-MH average"},
            {"label": "NHSPS interaction", "value": "Significant share of community-clinic estate held via NHSPS lease; rates pass through to trust as occupier"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Valuation Office Agency + multiple billing authorities (Newcastle CC, Northumberland CC, Sunderland CC, etc.)"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.3M → 2024-25 £1.64M; tracks frozen UBR + new-site additions + post-pandemic activity"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "CNTW carries a substantial business-rates bill structured by an unusually wide geographic estate — one of England's largest MH-trust footprints by area, spanning Northumberland's rural north, the Tyneside conurbation, Sunderland and Gateshead, plus North Cumbria and parts of County Durham. The Autumn Statement 2023 UBR freeze gave a one-year reprieve and the North East commercial RV base has remained relatively stable through the 2023 revaluation, but the 2026 revaluation cycle (under NDRA 2023) is the next inflection point. NHSPS-leased community clinics across the footprint pass rates through to CNTW. Specialist secure and neuro-rehabilitation services at Hopewood Park and the Hadrian Clinic carry higher per-m² rateable values than typical community-MH bases.",
        "sources": [
            {"publisher": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cntw.nhs.uk/about/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "CNTW provider profile (RX4)", "url": "https://www.cqc.org.uk/provider/RX4"}
        ],
        "related": ["Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Central and North West London NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Nottinghamshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Nottinghamshire Healthcare NHS Foundation Trust"}],
        "description": "Nottinghamshire Healthcare's £1.63M transport line covers staff business mileage and contracted patient transfers across Rampton Hospital (high-secure, Retford), the Wells Road Centre, Highbury Hospital, Millbrook (Sutton-in-Ashfield), the Wathwood Hospital MSU, and dozens of community-MH and forensic bases. Rampton's high-secure regime drives an unusual share of escorted-transfer cost. The Valdo Calocane Nottingham attacks (Jan 2023) and subsequent CQC enforcement + independent inquiry have placed transport governance under scrutiny.",
        "beneficiaries": "c. 9,000 staff serving c. 1.2M residents across Nottinghamshire plus Rampton's c. 350 high-secure patients drawn from a national catchment; Wathwood Hospital MSU + community-MH + CAMHS + forensic outreach generate routine staff mileage.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance + secure-transfer) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.63M"},
            {"label": "Site footprint generating transfers", "value": "Rampton Hospital (high-secure) + Wathwood MSU + Highbury + Wells Road + Millbrook + community bases"},
            {"label": "Rampton escorted-transfer premium", "value": "Off-site movements (court, healthcare, family) require accredited secure-transport with multi-staff cordon"},
            {"label": "Bed-stock generating transfers", "value": "c. 350 high-secure (Rampton) + medium-secure (Wathwood) + acute MH + community"},
            {"label": "MHA conveyance share", "value": "s.136 + s.135 contracted via EMAS + private secure-transport providers"},
            {"label": "Calocane attacks context", "value": "Jan 2023 Nottingham attacks → CQC inspection findings → external review travel + remediation programme"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.1M → 2024-25 £1.63M — uplift driven by post-pandemic recovery + Calocane remediation + secure-transfer cost inflation"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS + secure-transport contracted with EMAS + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Specialised Commissioning (Rampton high-secure) + Nottingham and Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports; NHSE high-secure standards; independent inquiry into the Nottingham attacks (ongoing)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 Calocane baseline · Successor: NHSE specialised-commissioning consolidated secure-transport + inquiry-led reforms"}
        ],
        "notes": "Nottinghamshire Healthcare's transport line is structurally elevated by the Rampton Hospital high-secure regime (one of England's three high-secure psychiatric hospitals alongside Broadmoor and Ashworth) and overlaid by the operational impact of the Valdo Calocane Nottingham attacks (June 2023, three killed), which led to CQC enforcement, multiple external reviews, the Nottingham attacks independent inquiry (announced 2024) and a sustained programme of remediation travel. Rampton's high-secure escorted-transfer protocol and Wathwood MSU's medium-secure regime drive per-journey costs many multiples of standard PTS. EMAS handles most s.136 conveyance under the East Midlands all-age PTS framework. The independent inquiry's recommendations are expected to drive further governance + transport-protocol changes.",
        "sources": [
            {"publisher": "Nottinghamshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nottinghamshirehealthcare.nhs.uk/publications"},
            {"publisher": "NHS England Specialised Commissioning", "title": "High-secure mental health services policy", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Care Quality Commission", "title": "Nottinghamshire Healthcare provider profile (RHA)", "url": "https://www.cqc.org.uk/provider/RHA"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Nottingham Attacks Independent Inquiry", "title": "Inquiry terms of reference + interim updates", "url": "https://www.gov.uk/government/news/nottingham-attacks-independent-inquiry"}
        ],
        "related": ["Nottinghamshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Mental Health Act 1983", "Transport (business + patient) — Greater Manchester Mental Health NHS Foundation Trust", "NHS England Specialised Commissioning"]
    },
    "Transport (business + patient) — Oxleas NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Oxleas NHS Foundation Trust"}],
        "description": "Oxleas's £1.63M transport line covers staff business mileage and contracted patient transfers across Green Parks House (Bromley), Oxleas House (Greenwich), the Bracton Centre medium-secure forensic unit (Dartford), Memorial Hospital and dozens of community bases plus prison-healthcare travel to HMP Belmarsh, HMP Isis, HMP Thameside and HMP Wandsworth. The combined MH + community physical-health + prison-healthcare remit creates an unusually broad mileage base — district-nursing visits sit alongside MH crisis-team travel and inter-prison healthcare clinician movements.",
        "beneficiaries": "c. 4,500 staff serving c. 800,000 residents across Bexley, Bromley and Greenwich plus prison-healthcare populations across multiple London prisons; Bracton Centre (medium-secure forensic) draws regional catchment; community-physical-health adds district-nursing mileage.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments · Health and Social Care Act 2012 (prison healthcare commissioning)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.63M"},
            {"label": "Site footprint generating transfers", "value": "Green Parks House + Oxleas House + Bracton Centre MSU (Dartford) + Memorial Hospital + community + prison sites"},
            {"label": "Combined remit driver", "value": "MH + community physical-health + prison-healthcare → district-nursing + clinician inter-prison travel adds to MH base"},
            {"label": "Bracton Centre medium-secure", "value": "Forensic MSU at Dartford generates inter-site escorted transfers"},
            {"label": "Prison-healthcare transport", "value": "Clinicians travel daily to HMP Belmarsh, HMP Isis, HMP Thameside, HMP Wandsworth + others — contracted clinician movements"},
            {"label": "MHA conveyance share", "value": "s.136 + s.135 contracted via LAS + private secure-transport providers"},
            {"label": "ULEZ + EV pressure", "value": "Mayor's ULEZ + Net Zero adding fleet-transition cost; partial EV adoption progressing"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.0M → 2024-25 £1.63M — uplift driven by post-pandemic recovery + ULEZ + prison-healthcare contract expansion"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with LAS + accredited secure-transport providers + HMPPS-coordinated prison-clinician access"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Health and Justice + South East London ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports; NHSE Health and Justice prison-healthcare standards"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ULEZ vehicle baseline · Successor: SE London ICS shared-fleet pooling + EV transition + prison-healthcare recommissioning"}
        ],
        "notes": "Oxleas's transport line is structurally elevated by an unusually diverse remit — alongside community-MH crisis teams across Bexley, Bromley and Greenwich, the trust runs district-nursing across the same boroughs and operates one of England's largest prison-healthcare portfolios, sending clinicians daily into HMP Belmarsh, HMP Isis, HMP Thameside, HMP Wandsworth and other London prisons. Each remit generates distinct mileage signatures. The Bracton Centre forensic MSU at Dartford adds escorted-transfer cost. ULEZ and Mayor's Net Zero are accelerating fleet EV transition; SE London ICS is exploring shared-fleet pooling across acute + MH providers. NHSE Health and Justice prison-healthcare recommissioning cycles drive contract-volume volatility.",
        "sources": [
            {"publisher": "Oxleas NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://oxleas.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England Health and Justice", "title": "Prison healthcare commissioning policy", "url": "https://www.england.nhs.uk/commissioning/health-just/"},
            {"publisher": "Care Quality Commission", "title": "Oxleas NHS FT provider profile (RPG)", "url": "https://www.cqc.org.uk/provider/RPG"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "London Ambulance Service NHS Trust", "title": "PTS contract data + s.136 conveyance protocols", "url": "https://www.londonambulance.nhs.uk/"}
        ],
        "related": ["Oxleas NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Mental Health Act 1983", "Transport (business + patient) — West London NHS Trust", "NHS England Health and Justice"]
    },
    "Transport (business + patient) — Cheshire and Wirral Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Cheshire and Wirral Partnership NHS Foundation Trust"}],
        "description": "CWP's £1.62M transport line covers staff business mileage and inter-site patient transfers across Bowmere Hospital (Chester), Springview (Wirral), Soss Moss Hospital (LD specialist, Nether Alderley), Millbrook (Macclesfield) and dozens of community-MH + LD bases across Cheshire West, Cheshire East, Wirral and parts of Trafford. The combined MH + LD specialist remit drives unusual transport requirements — LD service users often need adapted-vehicle transport for outpatient appointments + day-service access.",
        "beneficiaries": "c. 3,400 staff serving c. 1.0M residents across Cheshire + Wirral plus regional LD specialist catchment; rural Cheshire footprint generates higher per-WTE mileage than urban-MH peers; Soss Moss Hospital LD inpatients drive adapted-transport need.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments · Equality Act 2010 (LD adapted-transport)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.62M"},
            {"label": "Site footprint", "value": "Bowmere Hospital + Springview + Soss Moss (LD) + Millbrook + community bases"},
            {"label": "Catchment area", "value": "Cheshire West, Cheshire East, Wirral + Trafford community elements"},
            {"label": "LD adapted-transport driver", "value": "Soss Moss + LD community service requires adapted-vehicle transport for outpatient + day-service access"},
            {"label": "Rural Cheshire premium", "value": "Per-WTE community mileage elevated vs urban-MH peers; rural Cheshire postcodes drive longer journeys"},
            {"label": "MHA conveyance share", "value": "s.136 + s.135 contracted via NWAS + private secure-transport providers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.1M → 2024-25 £1.62M — uplift driven by post-pandemic recovery + fuel CPI + LD adapted-transport CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with NWAS + accredited LD-adapted + secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports; NHSE LD service standards (Whorlton Hall + Mazars context); CWP Quality Account 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate-LD-trust transport baseline · Successor: Cheshire & Merseyside ICS shared-fleet + EV transition"}
        ],
        "notes": "CWP's transport line is structurally elevated by the LD specialist remit — Soss Moss Hospital and the trust's LD community service require adapted-vehicle transport for outpatient and day-service access, generating per-journey costs above standard MH transport. The Equality Act 2010 reasonable-adjustment duty drives adapted-transport contracting beyond what MH-only providers face. Rural Cheshire's geography adds a per-WTE mileage premium for community staff. NHSE LD service standards (post-Whorlton Hall + Mazars context) have raised expectations on safe transport for LD inpatients during transfers. Cheshire & Merseyside ICS shared-fleet exploration and EV transition are the medium-term levers.",
        "sources": [
            {"publisher": "Cheshire and Wirral Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cwp.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "CWP provider profile (RXA)", "url": "https://www.cqc.org.uk/provider/RXA"},
            {"publisher": "NHS England", "title": "Learning Disability service standards + Building the Right Support", "url": "https://www.england.nhs.uk/learning-disabilities/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "North West Ambulance Service NHS Trust", "title": "PTS contract data + s.136 conveyance protocols", "url": "https://www.nwas.nhs.uk/"}
        ],
        "related": ["Cheshire and Wirral Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Mental Health Act 1983", "Transport (business + patient) — Leicestershire Partnership NHS Trust", "NHS England Specialised Commissioning"]
    },
    "Lease expenditure — Black Country Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Black Country Healthcare NHS Foundation Trust"}],
        "description": "BCHFT's £1.62M lease line covers IFRS 16 right-of-use depreciation + interest on the leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHSPS-leased community-MH clinics across Dudley, Sandwell, Walsall and Wolverhampton plus CHP LIFT-vehicle leases and ancillary leased space adjacent to Penn Hospital (Wolverhampton), Dorothy Pattison Hospital (Walsall), Bushey Fields (Dudley) and Hallam Street (Sandwell). The 2020 BCHFT formation (merger of Black Country Partnership and Dudley & Walsall MH) consolidated a fragmented leased estate.",
        "beneficiaries": "c. 3,500 staff serving c. 1.2M residents across the 4 Black Country boroughs (Dudley, Sandwell, Walsall, Wolverhampton); c. 60+ leased community-MH + CAMHS + LD premises.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.62M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability"},
            {"label": "Leased site count", "value": "c. 60+ NHSPS + CHP-LIFT premises across the 4 Black Country boroughs"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "2020 merger context", "value": "BCHFT formed 2020 from Black Country Partnership + Dudley & Walsall MH — consolidated fragmented leased estate"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service charge"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community-clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.8M → 2022-23 c. £1.4M ROU first year → 2024-25 £1.62M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Black Country ICB · IFRS 16 / GAM ch.7 oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense + pre-merger split-trust portfolios · Successor: Black Country ICS estate consolidation"}
        ],
        "notes": "BCHFT's lease line carries the IFRS 16 transition step-up and the legacy of a 2020 merger that brought together two distinct leased-estate portfolios from Black Country Partnership (Sandwell + Wolverhampton focus) and Dudley & Walsall MH. Estate rationalisation is a continuing post-merger workstream. The NHSPS / MH-trust market-rent dispute affects BCHFT's geographically dispersed community-MH footprint across the 4 Black Country boroughs. Black Country ICB is exploring estate consolidation across MH + acute providers (Sandwell & West Birmingham, Royal Wolverhampton, Dudley Group). The Penn Hospital site itself is owned, but ancillary administrative + training space sits in leased premises.",
        "sources": [
            {"publisher": "Black Country Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.blackcountryhealthcare.nhs.uk/about-us/publications-and-corporate-information"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "BCHFT provider profile (RYK)", "url": "https://www.cqc.org.uk/provider/RYK"}
        ],
        "related": ["Black Country Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Mersey Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Leicestershire Partnership NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Leicestershire Partnership NHS Trust"}],
        "description": "LPT's £1.60M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's combined MH + community + LD estate across Leicester, Leicestershire and Rutland. Major hereditaments include Bradgate Mental Health Unit (Glenfield), Evington Centre, Agnes Unit, Bennion Centre and dozens of community + district-nursing bases. Combined-remit trusts carry larger hereditament counts than MH-only peers because community-physical-health bases add to the rateable footprint.",
        "beneficiaries": "Approximately 70+ occupied hereditaments across Leicester city, Leicestershire and Rutland; serves c. 1.1M residents through combined MH + community physical-health + LD service.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.60M"},
            {"label": "Hereditament count", "value": "c. 70+ occupied sites across LLR footprint (acute MH, community, district-nursing bases, CAMHS, LD)"},
            {"label": "Geographic spread", "value": "Leicester city, Leicestershire (Hinckley, Loughborough, Melton, Market Harborough), Rutland"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "VOA 2023 revaluation impact", "value": "East Midlands commercial RVs broadly stable post-pandemic"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS trusts are not registered charities under Charities Act 2011"},
            {"label": "Combined-remit driver", "value": "MH + community physical-health + LD remit raises hereditament count vs MH-only peers"},
            {"label": "NHSPS interaction", "value": "Significant share of community-clinic estate held via NHSPS lease; rates pass through to trust as occupier"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Valuation Office Agency + Leicester CC, Leicestershire CC + Rutland CC billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.3M → 2024-25 £1.60M; tracks frozen UBR + new-site additions + post-pandemic activity"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "LPT's business-rates bill is structured by the trust's combined MH + community physical-health + LD remit, which inflates the hereditament count above MH-only peers — district-nursing bases, school-nursing clinics and LD community premises all add rateable footprint. The Autumn Statement 2023 UBR freeze gave a one-year reprieve and East Midlands commercial RVs are broadly stable through the 2023 revaluation, but the 2026 revaluation cycle is the next inflection point. NHSPS-leased community clinics across LLR pass rates through to LPT. The 2018 merger that brought community-physical-health into LPT's remit explains the elevated hereditament base relative to historic MH-only baseline.",
        "sources": [
            {"publisher": "Leicestershire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicspart.nhs.uk/about/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Leicestershire Partnership NHS Trust provider profile (RT5)", "url": "https://www.cqc.org.uk/provider/RT5"}
        ],
        "related": ["Leicestershire Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — South West London and St George's Mental Health NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "South West London and St George's Mental Health NHS Trust"}],
        "description": "SWLSTG's £1.56M amortisation line covers depreciation of capitalised intangibles — primarily the Rio EPR + supporting clinical software, e-prescribing modules, capitalised training and licensed-software stack used by the trust's c. 2,800 staff across Springfield University Hospital (Tooting), Tolworth Hospital, the new Trinity (Tooting) and Shaftesbury Park (Tooting) developments, plus community-MH bases across Wandsworth, Merton, Sutton, Kingston and Richmond. The Springfield Hospital redevelopment (2022-2024) drove a major step-up in capitalised assets and supporting intangibles.",
        "beneficiaries": "c. 2,800 staff using EPR + capitalised software stack across Springfield, Tolworth + community bases; serves c. 1.0M residents across SW London (Wandsworth, Merton, Sutton, Kingston, Richmond) plus regional specialist services (eating disorders, perinatal, OCD).",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation funding programme",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.56M"},
            {"label": "Composition", "value": "EPR (Rio) + clinical-software + e-prescribing + licensed software amortisation"},
            {"label": "Springfield redevelopment context", "value": "2022-2024 Springfield University Hospital redevelopment + new Trinity / Shaftesbury Park MH wards drove capitalised intangibles step-up"},
            {"label": "Frontline Digitisation context", "value": "Programme funded EPR + digital-maturity uplift since 2023"},
            {"label": "Useful-life range", "value": "Software 3-5 years per IAS 38 + DHSC GAM ch.5"},
            {"label": "Site footprint", "value": "Springfield University Hospital (Tooting) + Tolworth + Trinity + Shaftesbury Park + community bases across 5 SW London boroughs"},
            {"label": "Headcount served", "value": "c. 2,800 substantive WTE"},
            {"label": "Population served", "value": "c. 1.0M across 5 SW London boroughs + regional specialist catchment"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.7M → 2024-25 £1.56M — uplift driven by Springfield redevelopment + Frontline Digitisation EPR + e-prescribing"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams; NHSE Frontline Digitisation Programme funding"},
            {"label": "Policy owner", "value": "DHSC + NHSE Digital Transformation + South West London ICB · IAS 38 / GAM ch.5"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Springfield redevelopment baseline · Successor: federated-data-platform + digital-maturity-level-3 amortisation post-2026"}
        ],
        "notes": "SWLSTG's amortisation line carries the legacy of the £150M+ Springfield University Hospital redevelopment (2022-24), which delivered new MH wards (Trinity, Shaftesbury Park) and consolidated the Tooting estate — capitalised supporting intangibles (software licences, capitalised digital-training, EPR migrations) flow through amortisation over 3-5 year useful lives. The Frontline Digitisation programme has funded EPR upgrades and digital-maturity uplift since 2023, sustaining the amortisation trajectory. SWL ICB's digital strategy and SWLSTG's specialist remit (eating disorders, perinatal MH, OCD) drive ongoing capitalised intangibles in clinical-decision-support and outcomes-data platforms. Federated data platform and AI clinical-decision-support modules are expected to drive the next step-up.",
        "sources": [
            {"publisher": "South West London and St George's Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swlstg.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme — mental health trusts", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "Care Quality Commission", "title": "SWLSTG provider profile (RQY)", "url": "https://www.cqc.org.uk/provider/RQY"}
        ],
        "related": ["South West London and St George's Mental Health NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Frontline Digitisation programme", "Amortisation — Birmingham and Solihull Mental Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
}
