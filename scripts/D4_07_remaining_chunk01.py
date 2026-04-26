# -*- coding: utf-8 -*-
# D4_07 Premises (other) — remaining chunk 01 (17 NHS trusts)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Premises (other) — Harrogate and District NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Harrogate and District NHS Foundation Trust"}],
        "description": "Premises operating costs across HDFT — Harrogate District Hospital (the principal acute on the Lancaster Park Road site) plus a substantial out-of-area community estate including Ripon Community Hospital, plus the trust's children's-and-school nursing community footprint extending into Gateshead, Sunderland, County Durham, North Yorkshire and Darlington. Estates & Facilities is the delivery body, with NHSE as policy owner. Spend reflects an unusually wide community footprint relative to the small acute base.",
        "beneficiaries": "Around 600,000 patients across Harrogate, the wider Yorkshire Dales, and contracted children's-services populations in the north-east; ~5,000 staff working across the acute site and 100+ community locations.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment) · Health and Safety at Work Act 1974 · Mental Capacity Act 2005 (DoLS environmental duties)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.79M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute (Harrogate DH ~330 beds) + Ripon Community Hospital + 100+ community/school sites across 5 LAs"},
            {"label": "Hard FM model", "value": "In-house Estates & Facilities · no acute PFI"},
            {"label": "Soft FM model", "value": "Insourced cleaning + catering · partial outsourced security"},
            {"label": "Funding trajectory", "value": "2022-23 c. £11.0M → 2023-24 c. £11.9M → 2024-25 £12.79M (c. +7% YoY · energy + community-estate uplift)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · capital pursued through STP / regional bids"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-decarbonisation feasibility at Harrogate DH · LED rollout multi-site"},
            {"label": "Community premium", "value": "0-19 children's-services contract drives non-NHS-owned property costs (LA buildings, schools)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 Harrogate & District plus pre-2018 0-19 contract take-on · Successor: estate strategy 2025-30 in development"},
            {"label": "Peer benchmark", "value": "Above small-acute median per m² (community-estate spread)"}
        ],
        "notes": "HDFT's premises spend is structurally unusual because the trust delivers 0-19 children's services well beyond its acute catchment — pulling cleaning, soft-FM, water-hygiene and statutory-compliance costs across non-NHS-owned property (LA buildings and schools) into Premises (other). The 2024-25 uplift reflects RM6011 energy reset and 5-7% hard-FM construction inflation. CQC Reg 15 compliance across the wide community estate is a recurring inspection theme. Without an NHP slot, the trust is reliant on PSDS, ERIC backlog allocations and ICB capital for asset renewal at Harrogate DH.",
        "sources": [
            {"publisher": "Harrogate and District NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hdft.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "NHS England", "title": "NHS provider finance and operational performance 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Care Quality Commission", "title": "HDFT provider profile (RCD)", "url": "https://www.cqc.org.uk/provider/RCD"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Harrogate and District NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — York and Scarborough Teaching Hospitals NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — West London NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "West London NHS Trust"}],
        "description": "Mental-health and forensic premises operating costs across West London NHS Trust's estate — most notably Broadmoor Hospital (high-secure forensic, national-tier; new 2019 build) plus St Bernard's Hospital (Southall, with West London Forensic Service medium-secure), Lakeside Mental Health Unit (West Middlesex), and community sites across Ealing, Hounslow and Hammersmith & Fulham. Estates & Facilities delivers; NHSE specialised commissioning owns high-secure policy.",
        "beneficiaries": "Around 800,000 west-London residents for local services plus ~200 high-secure Broadmoor patients (national catchment) and ~300 medium/low-secure forensic places; c. 4,500 staff including high-security perimeter operations.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.4 high-secure designation) · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · HM Prison Service-equivalent security standards for high-secure",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.72M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "1 high-secure (Broadmoor ~210 beds) + St Bernard's medium-secure complex + Lakeside MHU + 30+ community sites"},
            {"label": "Hard FM model", "value": "In-house Estates with security-cleared specialist sub-contractors"},
            {"label": "High-secure perimeter", "value": "Broadmoor Cat-A-equivalent perimeter, CCTV, airlocks, secure ducting · drives premium per-m² cost"},
            {"label": "Funding trajectory", "value": "2022-23 c. £11.5M → 2023-24 c. £12.0M → 2024-25 £12.72M (c. +6% YoY · new-Broadmoor commissioning costs + energy)"},
            {"label": "Broadmoor 2019 rebuild", "value": "Replacement Victorian Broadmoor opened 2019 · old buildings still on site, decommissioning + listed-building obligations"},
            {"label": "Net Zero milestone", "value": "BMS upgrade across new Broadmoor; St Bernard's PSDS heat-pump feasibility"},
            {"label": "MH-specific", "value": "s.136 suite + PICU + ECT room + ligature-resistant fittings drive premises cost"},
            {"label": "Predecessor / successor", "value": "Predecessor: West London Mental Health Trust (renamed 2019) · Successor: estate strategy aligned to North West London ICS forensic plan"},
            {"label": "Evaluation evidence", "value": "CQC inspection 2023 noted environment progress at new Broadmoor; ongoing focus on St Bernard's 19th-century blocks"},
            {"label": "Peer benchmark", "value": "Far above MH-trust median per m² (high-secure premium · listed estate at St Bernard's)"}
        ],
        "notes": "West London's Premises (other) line is structurally elevated by its national high-secure responsibility: the new Broadmoor (commissioned 2019) brought higher operating-cost-per-m² than older blocks because of intensive BMS, security-system maintenance, and clinical airlock servicing — but enabled decant of the listed Victorian estate, which still carries holding costs. St Bernard's Southall's Victorian asylum buildings are listed, constraining decarbonisation options under PSDS. The trust's medium-secure West London Forensic Service expansion and Lakeside ageing-block pressures both feed the 2024-25 uplift alongside the RM6011 energy reset.",
        "sources": [
            {"publisher": "West London NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.westlondon.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "High Secure Hospitals Service Specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-c/c02/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "West London NHS Trust provider profile (RKL)", "url": "https://www.cqc.org.uk/provider/RKL"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["West London NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Premises (other) — South London and Maudsley NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Oxleas NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Oxleas NHS Foundation Trust"}],
        "description": "Mental-health, learning-disability and community-services premises costs across Oxleas's south-east-London estate — Oxleas House (Queen Elizabeth Hospital Woolwich co-location), Green Parks House (Princess Royal University Hospital, Bromley), Memorial Hospital Shooters Hill, plus Bracton Centre (medium-secure forensic) and Atlas House. Estate also includes prison-healthcare delivery footprint at HMP Belmarsh, Isis, Thameside and Rochester. Estates & Facilities is delivery body; NHSE + HMPPS share commissioning.",
        "beneficiaries": "Around 1.7M residents of Bexley, Bromley and Greenwich for community + MH services, plus ~600,000 across Kent prison-healthcare contracts; c. 4,000 patients in active MH caseloads; c. 4,500 staff.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · HMPPS prison-healthcare service spec · Mental Capacity Act 2005",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.62M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "Oxleas House + Green Parks House + Bracton (medium-secure) + Memorial + 80+ community clinics + prison-healthcare footprint at 4 prisons"},
            {"label": "Hard FM model", "value": "In-house Estates · co-tenanted hard-FM with LGT and KCH at QEH and PRUH respectively"},
            {"label": "Forensic perimeter", "value": "Bracton Centre medium-secure walls, CCTV, ligature-resistant fittings"},
            {"label": "Funding trajectory", "value": "2022-23 c. £11.4M → 2023-24 c. £11.9M → 2024-25 £12.62M (c. +6% YoY · energy + Bracton refurb)"},
            {"label": "Co-location", "value": "Inpatient MH co-located in acute-trust sites · shared-service estate cost recharges"},
            {"label": "Prison healthcare", "value": "Property obligations at HMP Belmarsh, Isis, Thameside, Rochester · MoJ-NHS landlord interface"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Memorial; LED rollout multi-site"},
            {"label": "Predecessor / successor", "value": "Predecessor: Oxleas NHS Trust (FT 2006) · Successor: South East London ICS estate strategy with LGT and SLAM partner trusts"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection rated trust Outstanding; environment praised but Bracton ageing fabric noted"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH-trust per m² (forensic premium offset by co-tenanted soft-FM efficiency)"}
        ],
        "notes": "Oxleas's premises spend is unusual in three ways: it co-tenants its main inpatient blocks inside acute-trust sites (Lewisham & Greenwich and KCH), generating shared-service estate-cost recharges rather than freehold operating spend; it operates a medium-secure forensic centre (Bracton); and it carries the property interface for NHS-delivered prison healthcare across four major south-east London prisons, where the landlord is HMPPS. The 2024-25 uplift reflects RM6011 energy reset, 5-7% hard-FM inflation and ongoing Bracton refurbishment costs.",
        "sources": [
            {"publisher": "Oxleas NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.oxleas.nhs.uk/about-us/key-documents/"},
            {"publisher": "NHS England", "title": "Health and Justice Service Specification", "url": "https://www.england.nhs.uk/commissioning/health-just/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "Oxleas NHS Foundation Trust provider profile (RPG)", "url": "https://www.cqc.org.uk/provider/RPG"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Oxleas NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Premises (other) — South London and Maudsley NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Norfolk and Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Norfolk and Suffolk NHS Foundation Trust"}],
        "description": "Mental-health and LD premises operating costs across NSFT's two-county estate — Hellesdon Hospital (Norwich, principal MH inpatient site), Northgate Hospital (Great Yarmouth), Wedgwood House (Bury St Edmunds, on West Suffolk Hospital site), Carlton Court (Lowestoft), plus over 50 community clinics. The trust has been in CQC special measures or 'requires improvement' multiple times since 2014, with environment one of the recurring issues driving estate spend.",
        "beneficiaries": "Around 1.7M residents of Norfolk and Suffolk; c. 4,000 staff; recent MH inquiry 'unexpected deaths' review (Strachan, Grant Thornton) has placed estate safety under sharp scrutiny.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · CQC Reg 12 (safe care, ligature)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.47M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Hellesdon (principal) + Northgate + Wedgwood + Carlton + 50+ community sites across two counties"},
            {"label": "Hard FM model", "value": "In-house Estates · Wedgwood House co-tenanted with WSFT"},
            {"label": "MH-specific", "value": "Ligature-resistant retrofit programme post-2019 inquiries · s.136 places of safety · PICU at Hellesdon"},
            {"label": "Funding trajectory", "value": "2022-23 c. £10.7M → 2023-24 c. £11.6M → 2024-25 £12.47M (c. +7-8% YoY · ligature-retrofit + energy)"},
            {"label": "Evaluation evidence", "value": "Grant Thornton 'unexpected deaths' independent review 2023 · CQC 2024 inspection environment-related findings"},
            {"label": "Net Zero milestone", "value": "PSDS heat-decarbonisation feasibility at Hellesdon · LED rollout"},
            {"label": "Estate strategy", "value": "Refresh 2024 prioritises ligature reduction + dormitory eradication"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2012 merger of Norfolk and Waveney MH FT with Suffolk MH Partnership · Successor: estate strategy aligned to Norfolk and Waveney + Suffolk and North East Essex ICSs"},
            {"label": "Dormitory programme", "value": "MH dormitory eradication capital flowing through trust capital programme; revenue impacts in this line"},
            {"label": "Peer benchmark", "value": "Above MH-trust per m² (estate age + retrofit programme)"}
        ],
        "notes": "NSFT's premises spend has been driven up materially by ongoing ligature-reduction retrofit and dormitory-elimination work flowing through both capital and operating lines, in response to the Strachan/Grant Thornton 'unexpected deaths' review and successive CQC inspections. The 2024-25 uplift reflects this safety-driven retrofit on top of the standard RM6011 energy reset and 5-7% hard-FM inflation. The trust's geography (rural Norfolk + Suffolk) drives high travel and small-site overheads in the community footprint.",
        "sources": [
            {"publisher": "Norfolk and Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nsft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Grant Thornton", "title": "Independent review of NSFT unexpected deaths (2023)", "url": "https://www.nsft.nhs.uk/independent-review/"},
            {"publisher": "Care Quality Commission", "title": "NSFT provider profile (RMY)", "url": "https://www.cqc.org.uk/provider/RMY"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Norfolk and Suffolk NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Premises (other) — Cambridgeshire and Peterborough NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Pennine Care NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Pennine Care NHS Foundation Trust"}],
        "description": "Mental-health and CAMHS premises operating costs across Pennine Care's east Greater Manchester estate — Tameside General co-located inpatient unit, Royal Oldham Hospital co-located Park House (the wholly-decommissioned Edenfield successor build was a separate Greater Manchester MH FT site), plus the trust's main Birch Hill Hospital (Rochdale) wards and over 70 community sites across Bury, Heywood/Middleton/Rochdale, Oldham, Stockport and Tameside. CAMHS Tier 4 inpatient at Hope Unit (Tameside).",
        "beneficiaries": "Around 1.4M residents across five east-Greater Manchester boroughs; c. 3,500 staff; the trust separated forensic services to Greater Manchester Mental Health FT in 2017, leaving a community + adult-acute + CAMHS estate.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · CQC Reg 12",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.45M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Birch Hill (Rochdale) + co-located Park House Oldham + Tameside MHU + Hope CAMHS + 70+ community sites"},
            {"label": "Hard FM model", "value": "Mixed — co-tenancy with Northern Care Alliance at Royal Oldham + Tameside · in-house at Birch Hill"},
            {"label": "MH-specific", "value": "s.136 suite · PICU · ligature-resistant retrofit ongoing post 2017-22 incidents"},
            {"label": "Funding trajectory", "value": "2022-23 c. £11.5M → 2023-24 c. £12.0M → 2024-25 £12.45M (c. +4-5% YoY · energy + retrofit)"},
            {"label": "CAMHS estate", "value": "Hope Unit Tameside national-tier CAMHS · environment historically scrutinised by CQC"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Birch Hill · LED multi-site"},
            {"label": "Estate consolidation", "value": "Post-2017 forensic transfer to GMMH simplified estate; ongoing dormitory-elimination capital"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 Pennine Care including forensic · Successor: ongoing GM ICS estate alignment with NCA and GMMH"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection environment findings at Hope Unit; estate-strategy refresh underway"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH-trust per m² (community-spread offsets)"}
        ],
        "notes": "Pennine Care's premises cost reflects a community-heavy MH estate spread across five GM boroughs, with co-tenancy in NCA acute sites generating shared-service recharges rather than freehold operating costs at major inpatient locations. The 2017 forensic transfer to GMMH simplified the estate but left ongoing CAMHS Tier 4 environmental obligations. Recent retrofit cycles (ligature, dormitory elimination, CAMHS environment) drive the 2024-25 uplift alongside RM6011 energy reset and 5-7% hard-FM inflation.",
        "sources": [
            {"publisher": "Pennine Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.penninecare.nhs.uk/about/our-publications"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "Pennine Care NHS Foundation Trust provider profile (RT2)", "url": "https://www.cqc.org.uk/provider/RT2"},
            {"publisher": "NHS England", "title": "Mental health dormitory eradication programme", "url": "https://www.england.nhs.uk/mental-health/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Pennine Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Premises (other) — Greater Manchester Mental Health NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Countess of Chester Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
        "description": "Premises operating costs at COCH — Countess of Chester Hospital (the principal acute, opened 1984) plus Ellesmere Port Hospital (intermediate care) and the Tarporley War Memorial community hospital. Estates & Facilities is the delivery body. The trust has been the subject of intense national scrutiny following the Lucy Letby case and the Thirlwall Inquiry — with neonatal-unit facilities and ward design under direct review.",
        "beneficiaries": "Around 600,000 patients across western Cheshire and Deeside; c. 5,000 staff; the trust's neonatal unit serves a wider regional catchment for higher-acuity care.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Inquiries Act 2005 (Thirlwall Inquiry context)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.43M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "1 acute (~600 beds) + Ellesmere Port intermediate + Tarporley WMH"},
            {"label": "Hard FM model", "value": "In-house Estates · no acute PFI"},
            {"label": "Estate vintage", "value": "1984 build envelope · ageing MEP at multiple ward levels"},
            {"label": "Neonatal context", "value": "Thirlwall Inquiry-related reviews of physical environment + CCTV + access controls flowing through estate spend"},
            {"label": "Funding trajectory", "value": "2022-23 c. £11.0M → 2023-24 c. £11.7M → 2024-25 £12.43M (c. +6% YoY · energy + neonatal-related works)"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump feasibility · LED rollout"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · capital recovery via ICB and ERIC backlog allocations"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1984 'Chester Royal Infirmary' city-centre site · Successor: estate strategy 2025-30 in development under Cheshire & Merseyside ICS"},
            {"label": "Evaluation evidence", "value": "CQC 2023-24 inspections, Thirlwall Inquiry live (interim findings due 2025)"},
            {"label": "Peer benchmark", "value": "Mid-range vs north-west single-site acutes per m²"}
        ],
        "notes": "COCH's Premises (other) line carries a unique driver — the Thirlwall Inquiry into the Lucy Letby case has triggered detailed scrutiny of neonatal-unit physical layout, CCTV, access controls, drug-storage security and ward sightlines, with physical works flowing through both capital and operating budgets. Standard 1984-build MEP renewal pressures sit alongside this safety-driven retrofit. The 2024-25 uplift reflects RM6011 energy reset and 5-7% hard-FM inflation on top of inquiry-related works.",
        "sources": [
            {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.coch.nhs.uk/about-us/publications/"},
            {"publisher": "Thirlwall Inquiry", "title": "Inquiry into events at the Countess of Chester Hospital", "url": "https://thirlwall.public-inquiry.uk/"},
            {"publisher": "Care Quality Commission", "title": "COCH provider profile (RJR)", "url": "https://www.cqc.org.uk/provider/RJR"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Countess of Chester Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Mid Cheshire Hospitals NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Airedale NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Airedale NHS Foundation Trust"}],
        "description": "Premises operating costs at Airedale — Airedale General Hospital (Steeton, near Keighley), one of the most-RAAC-affected hospitals in England (almost the entire structure built with the planks), plus a community-services estate across Airedale, Wharfedale and Craven, and the trust's national tele-health hub Digital Care Hub. Estates & Facilities is delivery body; estate has been a national focus since RAAC concrete crisis Sep 2023.",
        "beneficiaries": "Around 200,000 acute catchment plus a wider community population; c. 3,000 staff; the Digital Care Hub serves national tele-health contracts, adding additional 24/7 facilities-resilience demand.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Construction (Design and Management) Regulations 2015 (RAAC works)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.30M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute (Airedale GH) ~325 beds · community estate · Digital Care Hub"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist RAAC contractors"},
            {"label": "RAAC status", "value": "Almost entirety of acute hospital RAAC-built (HSSIB Sep 2023 priority list) · the 'whole-hospital RAAC' case"},
            {"label": "NHP scheme status", "value": "Airedale in NHP 2030 cohort for whole-hospital replacement; NHP Reset Jan 2025 reaffirmed RAAC trusts but timeline slipped"},
            {"label": "Funding trajectory", "value": "2022-23 c. £10.0M → 2023-24 c. £11.5M → 2024-25 £12.30M (c. +7-8% YoY · RAAC props, monitoring, decant)"},
            {"label": "RAAC operational impact", "value": "Continuous structural-monitoring + props + decant rooms · capital and operating spend"},
            {"label": "Net Zero milestone", "value": "Constrained by RAAC structural envelope · interim LED + BMS only"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1970 Airedale GH RAAC build · Successor: NHP 2030 replacement (single-stage scheme)"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC alert Sep 2023 · NAO 2023 NHP report · PAC NHP scrutiny 2024"},
            {"label": "Peer benchmark", "value": "Materially above acute-trust per m² (RAAC mitigation premium)"}
        ],
        "notes": "Airedale is the archetypal 'whole-hospital RAAC' trust — the Steeton building was constructed using RAAC planks throughout, leading to ongoing structural monitoring, propping, decant and ward closures that flow continuously through Premises (other). The NHP Reset Jan 2025 reaffirmed that RAAC trusts would be prioritised but slipped delivery timelines, extending the operating-cost burden of mitigation. Decarbonisation work is constrained by the structural envelope's poor condition.",
        "sources": [
            {"publisher": "Airedale NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.airedale-trust.nhs.uk/about-us/publications/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in the NHS — patient safety investigation", "url": "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/"},
            {"publisher": "DHSC", "title": "New Hospital Programme update Jan 2025 (Reset)", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "Airedale provider profile (RCF)", "url": "https://www.cqc.org.uk/provider/RCF"}
        ],
        "related": ["Airedale NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "New Hospital Programme", "Premises (other) — Bradford Teaching Hospitals NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Walsall Healthcare NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Walsall Healthcare NHS Trust"}],
        "description": "Premises operating costs at Walsall Healthcare — Walsall Manor Hospital (the principal acute, with a 2010 PFI new-build wing alongside legacy estate) plus community sites including community-nursing bases and adult services across Walsall borough. The trust operates a group model with The Royal Wolverhampton NHS Trust under Black Country Provider Collaborative arrangements.",
        "beneficiaries": "Around 270,000 patients across Walsall plus shared specialty pathways with Wolverhampton; c. 4,000 staff working from Manor Hospital and community sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.16M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "1 acute (Walsall Manor ~550 beds) + 8 community sites + Pleck Health Centre etc."},
            {"label": "Hard FM model", "value": "PFI envelope at Manor new-build · in-house Estates on legacy + community"},
            {"label": "PFI footprint", "value": "Walsall Manor 2010 PFI (Skanska / Innisfree) — unitary charge in D4_11; non-PFI sites + variations here"},
            {"label": "Funding trajectory", "value": "2022-23 c. £11.0M → 2023-24 c. £11.5M → 2024-25 £12.16M (c. +5-6% YoY · energy + PFI variations)"},
            {"label": "Group working", "value": "RWT-WHC group model · shared estate-strategy emerging across Black Country"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Manor non-PFI estate · LED rollout"},
            {"label": "Backlog", "value": "Pre-PFI Manor blocks carry residual high-risk backlog · ongoing replacement"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Walsall Hospitals NHS Trust · Successor: WHC-RWT group integration progressing"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection · ICS-level capital prioritisation"},
            {"label": "Peer benchmark", "value": "Below acute median per m² (PFI absorbs hard FM at the new-build core)"}
        ],
        "notes": "Walsall's premises spend reflects a mixed estate model — the 2010 PFI new-build absorbs hard FM into the unitary charge (D4_11), while pre-PFI legacy blocks and community estate are in-house Estates and bear the full energy and 5-7% hard-FM inflation. The emerging group-working with RWT (Black Country Provider Collaborative) has begun yielding shared estate roles. The 2024-25 uplift reflects RM6011 energy reset and ongoing PFI variations as service patterns evolve.",
        "sources": [
            {"publisher": "Walsall Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.walsallhealthcare.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Care Quality Commission", "title": "Walsall Healthcare provider profile (RBK)", "url": "https://www.cqc.org.uk/provider/RBK"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Walsall Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — The Royal Wolverhampton NHS Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — East Cheshire NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "East Cheshire NHS Trust"}],
        "description": "Premises operating costs across East Cheshire's small-acute and community estate — Macclesfield District General Hospital (the principal acute, ageing 1980s build), Congleton War Memorial Hospital, Knutsford and District Community Hospital, plus community-team bases across rural east Cheshire. ECT is one of the smaller English acute trusts and has been in long-running discussions over service sustainability with neighbouring trusts.",
        "beneficiaries": "Around 200,000 patients across east Cheshire and the High Peak fringe; c. 2,800 staff; the trust's small scale + rural geography drives high relative estate cost.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£11.85M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "1 acute (Macclesfield DGH ~250 beds) + Congleton WMH + Knutsford + community bases"},
            {"label": "Hard FM model", "value": "In-house Estates · no acute PFI"},
            {"label": "Macclesfield vintage", "value": "1980s build · backlog maintenance + MEP refresh pressure"},
            {"label": "Funding trajectory", "value": "2022-23 c. £10.5M → 2023-24 c. £11.2M → 2024-25 £11.85M (c. +6% YoY · energy + backlog refresh)"},
            {"label": "Service sustainability", "value": "Long-running East Cheshire / Mid Cheshire / MFT discussions on acute-service consolidation"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Macclesfield · LED rollout"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · capital recovery via ERIC backlog and ICS prioritisation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 Cheshire and Wirral PCT split · Successor: ICS-led service-sustainability review live"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection · NHSE finance-distress regime engagement"},
            {"label": "Peer benchmark", "value": "Materially above small-acute median per patient (sub-scale fixed-cost overhead)"}
        ],
        "notes": "East Cheshire's premises cost is structurally elevated in percentage terms by the trust's small operating scale — fixed estate overhead (statutory compliance, BMS, water hygiene, security) is spread across a low revenue base. Macclesfield DGH backlog and the persistent service-sustainability discussion with Mid Cheshire / MFT both shape capital prioritisation. The 2024-25 uplift reflects RM6011 energy reset and 5-7% hard-FM inflation on top of routine backlog refresh.",
        "sources": [
            {"publisher": "East Cheshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastcheshire.nhs.uk/About-The-Trust/publications.htm"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "East Cheshire NHS Trust provider profile (RJN)", "url": "https://www.cqc.org.uk/provider/RJN"},
            {"publisher": "NHS England", "title": "NHS provider finance and operational performance 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["East Cheshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Mid Cheshire Hospitals NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Cornwall Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Cornwall Partnership NHS Foundation Trust"}],
        "description": "Mental-health, learning-disability and community-services premises operating costs across CFT's all-Cornwall + Isles of Scilly estate — Bodmin Hospital (principal MH inpatient site, including Garner Ward and Fletcher Ward), Longreach House (Redruth, MH inpatient), Camborne Redruth Community Hospital, Bodmin Community, plus 60+ community team bases. CFT delivers community services across NHSPS-leased clinics across one of England's largest geographic single-county footprints.",
        "beneficiaries": "Around 570,000 residents of Cornwall and the Isles of Scilly; c. 4,000 staff; rural geography drives travel and small-site overhead premium.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£11.67M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "Bodmin Hospital + Longreach + 4-5 community hospitals + 60+ NHSPS-leased community sites"},
            {"label": "Hard FM model", "value": "In-house Estates plus NHSPS recharges on leased community sites"},
            {"label": "MH-specific", "value": "s.136 suite at Bodmin · PICU · ligature-resistant retrofit ongoing"},
            {"label": "NHSPS lease cost", "value": "Significant share of community estate is NHS Property Services — MOU rents flow through this line"},
            {"label": "Funding trajectory", "value": "2022-23 c. £10.5M → 2023-24 c. £11.0M → 2024-25 £11.67M (c. +6% YoY · NHSPS uplifts + energy)"},
            {"label": "Geographic premium", "value": "All-Cornwall coverage drives extreme dispersion; Isles of Scilly logistics premium"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Bodmin · LED rollout"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2008 demerger of Cornwall services from Cornwall Partnership PCT · Successor: One Cornwall ICS estate strategy with Royal Cornwall and Adult Social Care"},
            {"label": "Evaluation evidence", "value": "CQC 2024 inspection environment findings; estate-strategy refresh underway"},
            {"label": "Peer benchmark", "value": "Above MH-trust per inpatient bed (community-hospital + NHSPS leasehold mix)"}
        ],
        "notes": "Cornwall Partnership's Premises (other) line is shaped by the very large NHSPS leasehold estate it operates from for community-team bases across the county — annual MOU rent uplifts drive a structural premium not seen in trusts that own freehold. Add the all-Cornwall geography, Bodmin MH backlog and ligature-retrofit cycle, and the 2024-25 uplift reflects all three pressures alongside RM6011 energy reset. Isles of Scilly logistics adds a small but visible cost.",
        "sources": [
            {"publisher": "Cornwall Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cornwallft.nhs.uk/publications/"},
            {"publisher": "NHS Property Services", "title": "Annual report and tenant relationships", "url": "https://www.property.nhs.uk/about-us/"},
            {"publisher": "Care Quality Commission", "title": "Cornwall Partnership provider profile (RJ8)", "url": "https://www.cqc.org.uk/provider/RJ8"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Cornwall Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Premises (other) — Royal Cornwall Hospitals NHS Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Sheffield Children's NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Sheffield Children's NHS Foundation Trust"}],
        "description": "Premises operating costs at Sheffield Children's — the principal Western Bank hospital (Sheffield) including the 2021-opened Sterling Park outpatient + clinical research wing, plus the Centenary Wing (extended 2022) and the Becton Centre for Children and Young People (Tier 4 CAMHS, Sevenairs Road, Beighton). One of England's two dedicated standalone children's NHS foundation trusts. Estates & Facilities is delivery body; NHSE specialised commissioning is policy owner for tertiary services.",
        "beneficiaries": "Patients aged 0-18 across South Yorkshire, North Derbyshire and beyond — c. 320,000 attendances/yr. Tertiary specialties (paediatric oncology, neurosciences, cardiac, metabolic) draw national referrals. c. 4,000 staff.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Children Act 1989 (safeguarding-by-design environmental duties) · Mental Health Act 1983 (Becton CAMHS)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£11.48M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Western Bank principal site (Sterling + Centenary + listed historic block) + Becton Centre CAMHS Tier 4 + outpatient outreach"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contractors (paediatric-imaging-grade clean rooms, oncology HEPA)"},
            {"label": "Listed buildings", "value": "Historic Western Bank block listed Grade II — constrains decarbonisation options"},
            {"label": "Recent capital", "value": "Sterling Park 2021 opened (£40M) + Centenary Wing extension 2022; both feeding 2024-25 commissioning + lifecycle costs"},
            {"label": "Funding trajectory", "value": "2022-23 c. £9.8M → 2023-24 c. £10.7M → 2024-25 £11.48M (c. +7% YoY · new-wing commissioning + energy)"},
            {"label": "CAMHS estate", "value": "Becton Centre Tier 4 inpatient · ligature-resistant + safeguarding-by-design fittings"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Western Bank · LED rollout · constrained by listed envelope"},
            {"label": "Specialty power demand", "value": "Paediatric oncology HEPA + MRI/CT diagnostics drives utilities premium"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FT Sheffield Children's NHS Trust · Successor: estate masterplan 2025-30 in development"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection rating Good · NHSE specialised-commissioning environmental standards reviews"},
            {"label": "Peer benchmark", "value": "Above specialist median per m² (paediatric specialty utilities + listed envelope)"}
        ],
        "notes": "Sheffield Children's Premises (other) line is shaped by the recent commissioning of two major new wings (Sterling Park 2021, Centenary 2022) which have raised lifecycle and BMS costs, layered on top of the listed historic Western Bank block which constrains decarbonisation. Tier 4 CAMHS at Becton drives specialised safeguarding-by-design fittings. The 2024-25 uplift reflects new-wing operating costs, RM6011 energy reset and 5-7% hard-FM inflation.",
        "sources": [
            {"publisher": "Sheffield Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sheffieldchildrens.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Children's provider profile (RCU)", "url": "https://www.cqc.org.uk/provider/RCU"},
            {"publisher": "NHS England", "title": "Specialised commissioning service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Sheffield Children's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Department of Health and Social Care", "Premises (other) — Great Ormond Street Hospital for Children NHS Foundation Trust", "Premises (other) — Alder Hey Children's NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Coventry and Warwickshire Partnership NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Coventry and Warwickshire Partnership NHS Trust"}],
        "description": "Mental-health, learning-disability and community-services premises operating costs across CWPT's Coventry + Warwickshire estate — Caludon Centre (Coventry, principal MH inpatient on the UHCW campus), Brooklands Hospital (Birmingham, learning-disability inpatient), Manor Court (Nuneaton, MH inpatient), plus Hospital of St Cross Rugby co-tenanted MH unit, and 70+ community sites. Estates & Facilities delivers; NHSE + Coventry & Warwickshire ICB are commissioners.",
        "beneficiaries": "Around 1.0M residents of Coventry and Warwickshire; c. 4,500 staff; LD inpatient catchment extends well beyond the ICB into the West Midlands.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Mental Capacity Act 2005 (DoLS / LD environments) · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£11.24M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Caludon Centre (UHCW campus) + Brooklands LD + Manor Court + Hospital of St Cross MH unit + 70+ community sites"},
            {"label": "Hard FM model", "value": "Caludon co-tenanted with UHCW estate · Brooklands in-house · community NHSPS leasehold mix"},
            {"label": "MH-specific", "value": "s.136 places of safety · PICU at Caludon · LD ligature + DoLS-compliant fittings at Brooklands"},
            {"label": "Funding trajectory", "value": "2022-23 c. £10.0M → 2023-24 c. £10.6M → 2024-25 £11.24M (c. +6% YoY · NHSPS uplift + energy)"},
            {"label": "Brooklands LD context", "value": "National-tier LD beds · Transforming Care alignment to reduce inpatient footprint generates estate-rationalisation cost"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Brooklands · LED rollout multi-site"},
            {"label": "NHSPS leasehold", "value": "Substantial community estate held under NHSPS lease — annual MOU rent uplifts hit this line"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 'Coventry and Warwickshire Partnership Trust' minus pre-merger CWPT-CWHPT consolidation · Successor: ICS-led estate-rationalisation"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection rated Good with environment improvement requirements"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH-trust per m² (LD inpatient + co-tenancy partly offsetting)"}
        ],
        "notes": "CWPT's Premises (other) line carries an unusual driver in the Brooklands learning-disability inpatient estate — Transforming Care policy direction reduces LD inpatient footprint over time, generating estate-rationalisation costs alongside ongoing DoLS-compliant fitting upgrades. Caludon's co-tenancy on the UHCW campus generates shared-service estate recharges. The 2024-25 uplift reflects RM6011 energy reset, NHSPS rent uplifts on community estate, and 5-7% hard-FM inflation.",
        "sources": [
            {"publisher": "Coventry and Warwickshire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.covwarkpt.nhs.uk/publications"},
            {"publisher": "NHS England", "title": "Building the right support / Transforming Care for LD", "url": "https://www.england.nhs.uk/learning-disabilities/care/"},
            {"publisher": "Care Quality Commission", "title": "CWPT provider profile (RYG)", "url": "https://www.cqc.org.uk/provider/RYG"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Coventry and Warwickshire Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Premises (other) — University Hospitals Coventry And Warwickshire NHS Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — West Midlands Ambulance Service University NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "West Midlands Ambulance Service University NHS Foundation Trust"}],
        "description": "Premises operating costs across WMAS's regional ambulance estate — the trust's Brierley Hill HQ, the Tollgate (Stafford) regional control centre, plus the network of 14 'Hub' make-ready depots and 70+ Community Ambulance Stations across Staffordshire, Shropshire, Black Country, West Midlands metro, Birmingham, Coventry & Warwickshire, Hereford & Worcester. Includes HART (Hazardous Area Response Team) base, Air Ambulance bases, fleet workshops and fuel infrastructure.",
        "beneficiaries": "Around 5.7M residents of the West Midlands region — the largest English ambulance catchment by population; c. 6,500 staff including 5,500+ frontline.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Civil Contingencies Act 2004 (Cat 1 responder estate) · NHS Estates Code · CQC Reg 15 · COMAH (fuel storage) · Hazardous Substances Regs",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£11.21M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "Brierley Hill HQ + Tollgate EOC + 14 Hubs + 70+ Community Ambulance Stations + HART base + workshops"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts · 'Hub-and-CAS' delivery model"},
            {"label": "Hub-and-CAS model", "value": "Make-ready Hubs replaced traditional stations from 2010s · operating model continues to drive estate consolidation"},
            {"label": "Fleet support", "value": "Workshops + bulk fuel + EV charging infrastructure rollout"},
            {"label": "Funding trajectory", "value": "2022-23 c. £10.0M → 2023-24 c. £10.6M → 2024-25 £11.21M (c. +6% YoY · energy + EV-charging buildout)"},
            {"label": "Net Zero milestone", "value": "Vehicle decarbonisation programme · ZEV-1 first electric DCAs piloting · charging-point capital impacting opex"},
            {"label": "HART resilience", "value": "Cat 1 responder estate · backup power, training estate, decontamination"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2006 merger of West Midlands, Staffordshire and Hereford & Worcester ambulance trusts · Successor: continued Hub consolidation + EV transition"},
            {"label": "Evaluation evidence", "value": "CQC 2023 — only ambulance trust rated Outstanding · estate management cited as strength"},
            {"label": "Peer benchmark", "value": "Below ambulance-trust median per emergency call (Hub model efficiency)"}
        ],
        "notes": "WMAS's Premises (other) line is shaped by its pioneering Hub-and-CAS model — make-ready depots replaced traditional ambulance stations, lowering long-run operating cost per call but requiring ongoing capital and operating support for 14 Hub sites. The EV-DCA transition is starting to add charging-point installation and electrical-supply upgrade costs into this line. Cat 1 responder resilience (backup power, decontamination, HART base) drives a non-trivial fixed overhead. The 2024-25 uplift reflects energy reset and EV-rollout buildout.",
        "sources": [
            {"publisher": "West Midlands Ambulance Service University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://wmas.nhs.uk/about-us/our-trust/key-publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "WMAS provider profile (RYA)", "url": "https://www.cqc.org.uk/provider/RYA"},
            {"publisher": "NHS England", "title": "Greener NHS — ambulance fleet decarbonisation", "url": "https://www.england.nhs.uk/greenernhs/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["West Midlands Ambulance Service University NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Department of Health and Social Care", "Premises (other) — North West Ambulance Service NHS Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Sussex Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Sussex Partnership NHS Foundation Trust"}],
        "description": "Mental-health, CAMHS and substance-misuse premises operating costs across SPFT's Sussex + Hampshire + Surrey footprint — Mill View Hospital (Hove, principal MH inpatient), Langley Green Hospital (Crawley), Hellingly Centre (medium-secure forensic, Hailsham), Chalkhill Adolescent Inpatient Unit (Hellingly), Department of Psychiatry on the Princess Royal Hospital site (Haywards Heath), plus 80+ community sites across two ICBs.",
        "beneficiaries": "Around 1.7M residents of Sussex plus specialist CAMHS + perinatal + forensic catchments extending to Surrey and Hampshire; c. 4,800 staff.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · CQC Reg 12",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£11.04M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "Mill View + Langley Green + Hellingly Centre + Chalkhill + acute-co-located DOP + 80+ community sites across 2 ICBs"},
            {"label": "Hard FM model", "value": "In-house Estates · NHSPS leasehold mix on community sites"},
            {"label": "MH-specific", "value": "s.136 places of safety · PICU · medium-secure perimeter at Hellingly · CAMHS T4"},
            {"label": "Funding trajectory", "value": "2022-23 c. £10.0M → 2023-24 c. £10.5M → 2024-25 £11.04M (c. +5-6% YoY · NHSPS uplift + energy + dormitory works)"},
            {"label": "Dormitory programme", "value": "Mill View dormitory eradication capital · operating cost during decant"},
            {"label": "Cross-ICB footprint", "value": "Operates across Sussex ICB + Frimley ICB + Surrey Heartlands ICB · estate-strategy coordination challenge"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Mill View · LED multi-site"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2006 Sussex Partnership FT formation from East/West Sussex MH trusts · Successor: ICS-aligned estate strategy refresh"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection rated Good · Hellingly forensic environment specific reviews"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH-trust per inpatient bed (forensic premium offsetting community efficiency)"}
        ],
        "notes": "SPFT's premises spend is shaped by a heterogenous estate spanning adult acute MH, CAMHS Tier 4, medium-secure forensic and a wide community footprint across three ICB geographies — generating a complex cross-ICB estate-strategy coordination overhead. Dormitory eradication at Mill View has been a multi-year capital programme with associated decant operating costs. The 2024-25 uplift reflects RM6011 energy reset, NHSPS rent uplifts on community estate, and 5-7% hard-FM inflation.",
        "sources": [
            {"publisher": "Sussex Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sussexpartnership.nhs.uk/our-publications"},
            {"publisher": "NHS England", "title": "Mental health dormitory eradication programme", "url": "https://www.england.nhs.uk/mental-health/"},
            {"publisher": "Care Quality Commission", "title": "Sussex Partnership provider profile (RX2)", "url": "https://www.cqc.org.uk/provider/RX2"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Sussex Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Premises (other) — University Hospitals Sussex NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "Premises operating costs across YAS — the Wakefield headquarters, two Emergency Operations Centres (EOCs at Wakefield and York), 60+ ambulance stations spread across West, South, North and East Yorkshire and the Humber, plus HART base, training facilities, fleet workshops and the Patient Transport Service depot estate. YAS also operates NHS 111 Yorkshire and adds tele-triage facility cost on top.",
        "beneficiaries": "Around 5.5M residents across Yorkshire and Humber; c. 6,500 staff; one of the most-rural ambulance footprints in England (Yorkshire Dales, North Yorkshire Moors).",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Civil Contingencies Act 2004 · NHS Estates Code · CQC Reg 15 · COMAH (fuel) · Hazardous Substances Regs",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£10.84M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "Wakefield HQ + 2 EOCs (Wakefield + York) + 60+ stations + HART base + workshops + PTS depots"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts"},
            {"label": "Rural premium", "value": "Yorkshire Dales + Moors drive remote-station resilience cost (heating, generators, snow access)"},
            {"label": "111 estate", "value": "Tele-triage facility cost on top of 999 EOC footprint"},
            {"label": "Funding trajectory", "value": "2022-23 c. £9.6M → 2023-24 c. £10.2M → 2024-25 £10.84M (c. +6% YoY · energy + EV-charging buildout)"},
            {"label": "Net Zero milestone", "value": "EV-DCA pilot · charging-point rollout at multiple stations · roof-PV programme starting"},
            {"label": "Backlog", "value": "Significant share of station estate predates 2006 trust formation; Salix-funded refurb at risk-priority sites"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2006 merger of South, West, North & East and Tees ambulance services · Successor: continued station consolidation + EV transition"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection · NAO 2024 ambulance services review"},
            {"label": "Peer benchmark", "value": "Above ambulance-trust median per station (rural dispersion)"}
        ],
        "notes": "YAS's Premises (other) line is shaped by one of the most geographically dispersed and rural ambulance footprints in England — the Yorkshire Dales and North York Moors stations carry winter-resilience and small-site fixed-cost overheads that exceed urban peer trusts. Old pre-2006 station fabric still dominates the portfolio, with rolling Salix-funded refurbishment. The EV-DCA and roof-PV programmes are starting to flow into capital and operating spend. The 2024-25 uplift reflects energy reset and EV-rollout buildout.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/yas-publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "YAS provider profile (RX8)", "url": "https://www.cqc.org.uk/provider/RX8"},
            {"publisher": "National Audit Office", "title": "NHS ambulance services (2024)", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Yorkshire Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Department of Health and Social Care", "Premises (other) — North West Ambulance Service NHS Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Gloucestershire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Gloucestershire Hospitals NHS Foundation Trust"}],
        "description": "Premises operating costs at GHFT — Gloucestershire Royal Hospital (Gloucester) and Cheltenham General Hospital, the trust's two acute sites operating under the long-running 'Centre of Excellence' service-reconfiguration programme that splits emergency surgery and women & children's between the two. Plus a small community / outpatient outreach footprint. Estates & Facilities is delivery body.",
        "beneficiaries": "Around 650,000 patients across Gloucestershire; c. 8,000 staff; the 'one trust, two sites' reconfiguration drives ongoing decant and ward-level estate change.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£10.68M"},
            {"label": "Share of trust total opex", "value": "c. 1.5%"},
            {"label": "Estate scale", "value": "2 acute hospitals (Gloucestershire Royal ~700 beds + Cheltenham General ~430 beds) + outpatient outreach"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Service reconfiguration", "value": "Centre of Excellence programme — emergency surgery centralised at Gloucester, planned at Cheltenham · ongoing decant"},
            {"label": "Estate vintage", "value": "Cheltenham General late-Victorian + 20th-century blocks · Gloucestershire Royal 1970s-onwards"},
            {"label": "Funding trajectory", "value": "2022-23 c. £9.4M → 2023-24 c. £10.0M → 2024-25 £10.68M (c. +7% YoY · energy + decant + Cheltenham backlog)"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Gloucester · LED multi-site · Cheltenham listed-block constraints"},
            {"label": "Backlog", "value": "Cheltenham General has high backlog ranking on NHS ERIC return"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2002 merger of Gloucester and Cheltenham acute trusts · Successor: 'One Gloucestershire' ICS estate strategy"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection · NHSE provider-finance focus on capital-deficit position"},
            {"label": "Peer benchmark", "value": "Below acute median per m² (low % of opex reflects high non-premises clinical spend)"}
        ],
        "notes": "GHFT's Premises (other) line is unusually low as a share of opex compared with peer two-site acute trusts, reflecting a high clinical-spend ratio rather than estate efficiency. Cheltenham General's backlog ranking is among the highest in the south-west on NHS ERIC returns, with listed-block constraints limiting decarbonisation. The Centre of Excellence reconfiguration generates ongoing decant cost as services move between sites. The 2024-25 uplift reflects RM6011 energy reset and 5-7% hard-FM inflation.",
        "sources": [
            {"publisher": "Gloucestershire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gloshospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "GHFT provider profile (RTE)", "url": "https://www.cqc.org.uk/provider/RTE"},
            {"publisher": "NHS England", "title": "NHS provider finance and operational performance 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Gloucestershire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Gloucestershire Health and Care NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
    "Premises (other) — Barnsley Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Barnsley Hospital NHS Foundation Trust"}],
        "description": "Premises operating costs at Barnsley Hospital — a single-site acute trust with the 1970s tower-block Barnsley General Hospital, plus the new Tickhill Road Education Centre and a small community-outreach footprint. Operating under the South Yorkshire Working Together provider partnership with Sheffield Teaching, Doncaster & Bassetlaw, Rotherham and The Mid Yorkshire — driving shared estate-services dialogue. Estates & Facilities is delivery body.",
        "beneficiaries": "Around 240,000 patients across Barnsley borough; c. 3,500 staff; small-acute scale drives high relative fixed-cost overhead.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£10.34M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute (Barnsley General ~400 beds) · single-site · plus Education Centre + outreach clinics"},
            {"label": "Hard FM model", "value": "In-house Estates · no acute PFI"},
            {"label": "Estate vintage", "value": "1977 main tower + multiple later additions · ageing MEP"},
            {"label": "Backlog", "value": "Significant high-risk backlog reported on NHS ERIC return · ward-block lift and electrical refurb pressure"},
            {"label": "Funding trajectory", "value": "2022-23 c. £9.0M → 2023-24 c. £9.7M → 2024-25 £10.34M (c. +7% YoY · backlog refresh + energy)"},
            {"label": "South Yorkshire Working Together", "value": "Provider partnership with STH/DBTH/RDFT/MYHT · shared estate-services emerging"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility · LED rollout"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · capital recovery via ICB and ERIC backlog"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1977 'Beckett Hospital' + 'Mount Vernon' Barnsley estates · Successor: ICS-aligned strategy under SYB ICB and provider partnership"},
            {"label": "Evaluation evidence", "value": "CQC 2023 inspection · NAO Tackling the NHS backlog of care 2024 (relevant context)"},
            {"label": "Peer benchmark", "value": "Above small-acute median per m² (1977 tower-block MEP overhead)"}
        ],
        "notes": "Barnsley's premises spend is shaped by the ageing 1977 tower-block estate, where lift, electrical and HVAC refresh has been a persistent backlog focus on NHS ERIC returns. The trust has no PFI, so all hard FM, soft FM, utilities and lifecycle costs flow through this line. The South Yorkshire Working Together partnership is opening up shared-estate service possibilities but slow. The 2024-25 uplift reflects RM6011 energy reset, 5-7% hard-FM inflation and accelerated backlog refresh.",
        "sources": [
            {"publisher": "Barnsley Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.barnsleyhospital.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "Barnsley Hospital provider profile (RFF)", "url": "https://www.cqc.org.uk/provider/RFF"},
            {"publisher": "National Audit Office", "title": "Tackling the elective backlog (2024)", "url": "https://www.nao.org.uk/reports/managing-nhs-backlogs-and-waiting-times-in-england/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Barnsley Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Department of Health and Social Care", "Premises (other) — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Premises (other) — Sheffield Teaching Hospitals NHS Foundation Trust", "GF.07 Health (COFOG)"]
    },
}
