# -*- coding: utf-8 -*-
# D4_07 Premises (other) — chunk 05 (20 NHS trusts)
# Hand-curated trust-specific enrichment entries.

NEW = {
    "Premises (other) — University Hospitals Bristol and Weston NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals Bristol and Weston NHS Foundation Trust"}],
        "description": "Premises running costs across UHBW's two-city estate, formed by the 2020 merger of UH Bristol and Weston Area Health — Bristol Royal Infirmary, Bristol Royal Hospital for Children, St Michael's (maternity), Bristol Heart Institute, Bristol Haematology and Oncology Centre, Bristol Dental Hospital, Bristol Eye Hospital and the South Bristol Community Hospital, plus Weston General Hospital. The Bristol acute campus is a dense vertically-stacked specialty estate; Weston is a 1980s coastal DGH.",
        "beneficiaries": "500,000+ Bristol catchment plus regional tertiary referrals (cardiac, paediatric, haem-onc, ophthalmology, dental) plus 220,000+ at Weston — coastal North Somerset.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£20.18M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "8 specialty hospitals on Bristol campus + Weston General + South Bristol Community"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Vertical campus", "value": "BRI tower + linked specialty buildings · complex vertical-transport (lift) and shared-services cost"},
            {"label": "Weston coastal", "value": "Saline-air corrosion premium on hard FM at Weston General"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Weston · LED rollout multi-site · BNSSG decarbonisation programme"},
            {"label": "YoY change", "value": "c. +5-7% (energy + post-merger estate-rationalisation)"},
            {"label": "Peer benchmark", "value": "Below acute-teaching median per m² (vertical campus efficient on footprint)"}
        ],
        "notes": "UHBW's Premises (other) line is moderated by the dense vertically-stacked Bristol specialty campus (efficient footprint per bed) but inflated at Weston by coastal corrosion and 1980s build vintage. Post-merger estate-rationalisation continues to drive decant and minor works captured here. Bristol's BHOC and Heart Institute carry specialty-equipment power and HVAC loads above general-acute averages.",
        "sources": [
            {"publisher": "University Hospitals Bristol and Weston NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhbw.nhs.uk/p/about-us/publications-and-policies"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["University Hospitals Bristol and Weston NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Mid Cheshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Mid Cheshire Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across MCHFT — Leighton Hospital (Crewe, the principal acute, a 1972-vintage RAAC-affected site with national prominence in the concrete crisis), Victoria Infirmary Northwich, and Elmhurst Intermediate Care Centre Winsford. Leighton is one of the most-RAAC-exposed acute hospitals in England, dominating estate spend.",
        "beneficiaries": "440,000+ patients across Cheshire East and Cheshire West — A&E, maternity and acute medicine at Leighton, intermediate care at Victoria and Elmhurst.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£20.16M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "1 acute (Leighton) + 1 community hospital + Elmhurst ICU"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "RAAC status", "value": "Leighton Hospital — among most-extensively RAAC-affected NHS acute estates · HSSIB-listed · NHP cohort"},
            {"label": "NHP scheme status", "value": "Leighton replacement promoted into accelerated NHP wave 2024 due to RAAC severity"},
            {"label": "RAAC mitigation cost", "value": "Significant ongoing props, fail-safe steel, monitoring, decant"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + BMS works at Leighton · constrained by RAAC"},
            {"label": "YoY change", "value": "c. +8-10% (RAAC mitigation dominant driver)"},
            {"label": "Peer benchmark", "value": "Well above acute median per m² (RAAC operating burden)"}
        ],
        "notes": "MCHFT's Premises (other) line is dominated by ongoing RAAC mitigation at Leighton — one of the most-exposed concrete-frame estates in NHS England, with extensive temporary props, fail-safe steel, and area-by-area decant works. The trust was promoted into the accelerated NHP wave for full replacement, but until that delivers, operating spend is structurally elevated. Capital investment in any non-RAAC scheme is constrained while the structural emergency continues.",
        "sources": [
            {"publisher": "Mid Cheshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mcht.nhs.uk/about-us/publications"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in the NHS — investigation report", "url": "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/"},
            {"publisher": "GOV.UK / DHSC", "title": "New Hospital Programme update January 2025", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"}
        ],
        "related": ["Mid Cheshire Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Epsom and St Helier University Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Epsom and St Helier University Hospitals NHS Trust"}],
        "description": "Premises running costs across Epsom and St Helier — Epsom Hospital (Surrey) and St Helier Hospital (Carshalton, a 1938-built listed/protected estate widely regarded as the most-dated acute hospital in England). Both are NHP cohort sites with the planned Sutton Specialist Emergency Care Hospital intended to consolidate acute services; NHP Reset Jan 2025 deferred the scheme. Operating in GESH group with St George's.",
        "beneficiaries": "490,000+ patients across south-west London and Surrey — A&E, maternity and acute medicine split between sites pending reconfiguration.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£19.98M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "2 acute hospitals + Sutton Hospital site + community estate"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "St Helier", "value": "1938-vintage estate · widely cited as oldest functioning acute in NHS England · severe backlog"},
            {"label": "NHP scheme status", "value": "Sutton Specialist Emergency Care Hospital deferred under Reset Jan 2025"},
            {"label": "GESH group", "value": "Operating in group with St George's · shared estate strategy emerging"},
            {"label": "Net Zero milestone", "value": "Limited investment pending NHP outcome · PSDS-funded LED at Epsom"},
            {"label": "YoY change", "value": "c. +6-8% (extending operating life of pre-NHP estate)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (St Helier age + backlog)"}
        ],
        "notes": "ESTH carries one of the most-acute estate-condition challenges in NHS England — St Helier's 1938 fabric was scheduled for replacement at Sutton, and the NHP Reset has indefinitely extended its operating life. Backlog maintenance is structurally embedded in this line because capital is held back pending NHP clarity. GESH group formation with St George's may yield shared FM efficiencies but the Estate's age dominates near-term operating cost.",
        "sources": [
            {"publisher": "Epsom and St Helier University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.epsom-sthelier.nhs.uk/our-publications"},
            {"publisher": "GOV.UK / DHSC", "title": "New Hospital Programme update January 2025", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Epsom and St Helier University Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Salisbury NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Salisbury NHS Foundation Trust"}],
        "description": "Premises running costs at Salisbury District Hospital — a single-site acute teaching hospital in Wiltshire, host to specialty national-referral services including the Wessex Spinal Centre, Wessex Regional Genetics Laboratory, the Duke of Cornwall Spinal Treatment Centre and the Burns Centre, plus general acute. The single-site model concentrates estate spend on one campus.",
        "beneficiaries": "270,000+ Wiltshire/south-west catchment plus national tertiary referrals (spinal injury, burns, plastics, genetics).",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£19.62M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "1 acute campus (~470 beds) · large rural-style site with multiple specialty wings"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Specialty estate", "value": "Wessex Spinal Centre · Burns Centre · Genetics Lab · Plastic Surgery · power and HVAC premium"},
            {"label": "Estate age", "value": "Mix of 1990s redevelopment + earlier wings · backlog moderate"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat decarbonisation feasibility · LED rollout"},
            {"label": "YoY change", "value": "c. +5% (energy + 5-7% hard-FM inflation)"},
            {"label": "Peer benchmark", "value": "Above small-acute median per m² (specialty equipment loads)"}
        ],
        "notes": "Salisbury's premises cost is structurally elevated by its specialty national-referral mix — spinal-injury and burns rehabilitation drive 24/7 environmental controls and specialised ward HVAC well beyond general-acute norms. The single-site model concentrates resilience cost (one set of standby generators, one oxygen plant) but limits decant flexibility. RM6011 energy reset feeds the YoY uplift.",
        "sources": [
            {"publisher": "Salisbury NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.salisbury.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Salisbury NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "Premises running costs across WAHT's three-acute-site estate — Worcestershire Royal Hospital (Worcester, a 2002 PFI build), the Alexandra Hospital (Redditch, 1980s) and Kidderminster Hospital and Treatment Centre (1970s, downgraded from full A&E). The Worcester PFI absorbs much hard FM into D4_11; the Alexandra and Kidderminster are operated under in-house Estates with backlog pressure.",
        "beneficiaries": "580,000+ patients across Worcestershire — major emergency at Worcester, urgent + planned at the Alexandra, planned + minor injuries at Kidderminster.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£19.54M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "3 acute hospitals · mixed PFI + in-house"},
            {"label": "Hard FM model", "value": "Worcester PFI envelope · Alexandra + Kidderminster in-house Estates"},
            {"label": "PFI footprint", "value": "Worcestershire Royal PFI (Catalyst Healthcare Worcester) — unitary charge in D4_11"},
            {"label": "Alexandra estate", "value": "1980s build · ongoing backlog and ward-block refresh pressure"},
            {"label": "Reconfiguration", "value": "Future of Acute Hospital Services Worcestershire (FoAHSW) — long-running"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at the Alexandra · LED multi-site"},
            {"label": "YoY change", "value": "c. +5-7% (energy + Alexandra backlog)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers per m²"}
        ],
        "notes": "WAHT's Premises (other) line is shaped by a mixed PFI/in-house estate split — Worcester PFI carries hard FM into D4_11 while the Alexandra and Kidderminster carry the bulk of operating spend captured here. The long-running FoAHSW reconfiguration debate has constrained capital, leaving operating-line spend to absorb backlog. Without an NHP slot, the Alexandra in particular faces persistent operating-cost pressure.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.worcsacute.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Chelsea and Westminster Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
        "description": "Premises running costs across ChelWest — Chelsea and Westminster Hospital (Fulham Road, a 1993 build with co-located retail mall and atrium) and West Middlesex University Hospital (Isleworth), plus the trust's HIV/sexual-health network (56 Dean Street, John Hunter Clinic, West London CASH). ChelWest is one of the largest HIV/GU service-providers in Europe.",
        "beneficiaries": "1M+ catchment across central, west and south-west London — A&E, maternity at both sites, plus national-leading HIV/sexual-health services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£19.53M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "2 acute hospitals + 4 community/sexual-health clinic sites in central + west London"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Atrium estate", "value": "Chelsea and Westminster's atrium + retail mall · unique mixed-use estate"},
            {"label": "West Middlesex", "value": "Acquired 2015 · estate integration and refresh continuing"},
            {"label": "Specialty clinics", "value": "56 Dean Street (Soho) · John Hunter Clinic · GU service estate cost"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at West Mid · LED multi-site"},
            {"label": "YoY change", "value": "c. +5-7% (London energy + central-London soft FM)"},
            {"label": "Peer benchmark", "value": "Mid-range vs London acute peers per m²"}
        ],
        "notes": "ChelWest's premises cost is shaped by central-London soft-FM premiums (cleaning and security cost more in zone-1/2), the unusual mixed-use atrium estate at the Chelsea site (with retail tenants and shared-services complexity), and a satellite GU/HIV estate that adds central-London property running cost. The 2015 West Middlesex acquisition continues to drive estate-integration spend.",
        "sources": [
            {"publisher": "Chelsea and Westminster Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chelwest.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Kettering General Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Kettering General Hospital NHS Foundation Trust"}],
        "description": "Premises running costs at Kettering General Hospital — a single-site acute serving north Northamptonshire, originally built 1897 with extensive subsequent additions. KGH is in the NHP cohort with a planned redevelopment, and the estate carries documented backlog and modernisation pressure. Recently joined the University Hospitals of Northamptonshire group with Northampton General.",
        "beneficiaries": "350,000+ patients across Kettering, Corby and north Northamptonshire — A&E, maternity, acute medicine and surgery.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£19.40M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "1 acute campus (1897 origin + many subsequent additions) + community sites"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Estate age", "value": "Multi-vintage from 1897 to 2010s · documented backlog pressure"},
            {"label": "NHP scheme status", "value": "Kettering redevelopment in NHP cohort · Reset Jan 2025 deferred timeline"},
            {"label": "UHN group", "value": "Operating in UHN group with Northampton General · shared estate strategy emerging"},
            {"label": "Net Zero milestone", "value": "PSDS heat works · LED rollout · constrained pending NHP outcome"},
            {"label": "YoY change", "value": "c. +6% (extending operating life pre-NHP)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (estate age + multi-vintage)"}
        ],
        "notes": "KGH's Premises (other) line is structurally inflated by the multi-vintage estate (parts dating to 1897) and the NHP Reset's deferral of redevelopment, which has extended operating life of fabric scheduled for replacement. Documented backlog maintenance feeds the operating line directly. UHN group formation with Northampton General offers some shared FM and estate-strategy efficiency over time.",
        "sources": [
            {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/publications"},
            {"publisher": "GOV.UK / DHSC", "title": "New Hospital Programme update January 2025", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Kettering General Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Royal United Hospitals Bath NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal United Hospitals Bath NHS Foundation Trust"}],
        "description": "Premises running costs at the Royal United Hospital Bath — a single-site ~750-bed acute on the western edge of Bath, with mixed mid-20th-century and recent build (Dyson Cancer Centre opened 2024). The trust also operates at Paulton Memorial Hospital and Sulis Hospital (acquired private hospital, now NHS-operated for elective recovery).",
        "beneficiaries": "500,000+ patients across Bath, north-east Somerset and west Wiltshire — A&E, maternity, regional cancer care at the new Dyson Centre, plus elective recovery at Sulis.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£19.18M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute (RUH Bath) + Sulis Hospital + Paulton Memorial + clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Dyson Cancer Centre", "value": "Opened 2024 · operating-cost step-up in 2024-25 line"},
            {"label": "Sulis Hospital", "value": "Acquired private elective hospital · unique NHS estate-management case"},
            {"label": "Estate age", "value": "Mid-20th-century base + 2000s additions + 2024 Dyson · mixed vintage"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump works at RUH · Dyson built to high BREEAM standard"},
            {"label": "YoY change", "value": "c. +6% (Dyson opening + energy reset)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers per m²"}
        ],
        "notes": "RUH Bath's Premises (other) line stepped up in 2024-25 with the opening of the Dyson Cancer Centre — new utilities, FM contracts and HVAC loads come on stream even before activity reaches steady state. The trust's acquisition of Sulis Hospital (a former private acute) is a structurally unusual NHS estate case requiring distinct FM and compliance handling. RM6011 energy reset compounds the YoY uplift.",
        "sources": [
            {"publisher": "Royal United Hospitals Bath NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ruh.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Royal United Hospitals Bath NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Chesterfield Royal Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Chesterfield Royal Hospital NHS Foundation Trust"}],
        "description": "Premises running costs at Chesterfield Royal Hospital — a single-site ~530-bed acute opened 1984 in Calow, north-east Derbyshire, with subsequent additions including the 2010s Hartington Wing. The trust also runs Royal Primary Care (a wholly-owned subsidiary GP estate) and a network of community clinics, plus Helping You Health (DHU joint venture).",
        "beneficiaries": "400,000+ patients across north Derbyshire and parts of north-east Derbyshire — A&E, maternity, acute medicine and surgery.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£19.03M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "1 acute (Chesterfield Royal) + Royal Primary Care GP estate + community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates plus subsidiary FM (DBS Facilities Services Ltd)"},
            {"label": "Subsidiary FM", "value": "DBS Facilities Services Ltd (wholly-owned NHS sub-co · runs hard + soft FM)"},
            {"label": "Royal Primary Care", "value": "Wholly-owned GP-estate subsidiary · adds primary-care premises cost to trust line"},
            {"label": "Estate age", "value": "1984 build + Hartington Wing (2010s) · backlog moderate"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + BMS works · heat decarbonisation feasibility"},
            {"label": "YoY change", "value": "c. +5-6% (energy + GP-estate uplift)"},
            {"label": "Peer benchmark", "value": "Above small-acute median per m² (subsidiary structure adds visible spend)"}
        ],
        "notes": "Chesterfield Royal's Premises (other) line is structurally unusual because of the trust's wholly-owned subsidiary model — DBS Facilities Services delivers hard and soft FM in-group, and Royal Primary Care brings GP estate inside the trust's premises envelope. This makes per-m² spend look elevated versus peers but reflects vertical integration rather than inefficiency. Salix and PSDS grants are recurring funding sources for decarbonisation works.",
        "sources": [
            {"publisher": "Chesterfield Royal Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chesterfieldroyal.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Chesterfield Royal Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals of Morecambe Bay NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals of Morecambe Bay NHS Foundation Trust"}],
        "description": "Premises running costs across UHMB's three-acute-site estate — Royal Lancaster Infirmary (Lancaster), Furness General Hospital (Barrow-in-Furness, peninsula geography) and Westmorland General Hospital (Kendal, smaller acute) — plus Queen Victoria Hospital Morecambe and a community footprint. UHMB's geography is among the most-stretched in NHS England, with the Furness peninsula adding logistic complexity.",
        "beneficiaries": "365,000+ patients across north Lancashire, south Cumbria and parts of North Yorkshire — A&E + maternity at Lancaster and Furness, planned and rehabilitation at Westmorland.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.91M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "3 acute + 1 community hospital · stretched coastal/peninsula geography"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Furness peninsula", "value": "Geographic isolation drives resilience cost · higher-than-peer travel and supply-chain"},
            {"label": "Estate age", "value": "Royal Lancaster + Furness General both 1980s · backlog pressure"},
            {"label": "Coastal exposure", "value": "Furness + Lancaster coastal · saline-air corrosion premium on hard FM"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Lancaster · LED multi-site"},
            {"label": "YoY change", "value": "c. +6-7% (rural/peninsula premium + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (geographic dispersion + estate age)"}
        ],
        "notes": "UHMB's premises spend is structurally inflated by geographic dispersion (the Furness peninsula adds resilience and supply-chain cost beyond peer norms) and by 1980s estate vintage at the two main acutes. The post-Kirkup-2015 maternity reform investment programme has been a recurring estate-improvement theme. Without an NHP slot, capital recovery for backlog falls disproportionately on operating spend captured here.",
        "sources": [
            {"publisher": "University Hospitals of Morecambe Bay NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhmb.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["University Hospitals of Morecambe Bay NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Hampshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across HHFT's three-site acute estate — Royal Hampshire County Hospital (Winchester), Basingstoke and North Hampshire Hospital, and Andover War Memorial Hospital. HHFT is in the NHP cohort with the planned Hampshire Hospitals scheme (single new acute on a Basingstoke-area site, consolidating Winchester and Basingstoke); NHP Reset Jan 2025 deferred the timeline.",
        "beneficiaries": "600,000+ patients across north + mid Hampshire — A&E + maternity at Winchester and Basingstoke, planned and minor injuries at Andover. Basingstoke also hosts the national Pseudomyxoma Peritonei Centre.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.87M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "3 acute hospitals · multi-site geography across north Hampshire"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "NHP scheme status", "value": "Hampshire Hospitals scheme (consolidation of Winchester + Basingstoke) deferred under Reset"},
            {"label": "Basingstoke", "value": "Hosts national Pseudomyxoma Peritonei Centre · specialty HVAC/lab loads"},
            {"label": "Estate age", "value": "Both main acutes 1970s-80s + RHCH historic core · backlog pressure"},
            {"label": "Net Zero milestone", "value": "PSDS heat works · LED rollout · constrained pending NHP outcome"},
            {"label": "YoY change", "value": "c. +6% (extending operating life of pre-NHP estate)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (multi-site + estate age)"}
        ],
        "notes": "HHFT's Premises (other) line is shaped by the NHP Reset deferral, which has extended operating life of two ageing acute estates (Winchester and Basingstoke) that were scheduled for consolidation. Backlog maintenance is structurally captured here while capital is held back. Basingstoke's national pseudomyxoma centre adds specialty laboratory and HVAC operating cost above general-acute averages.",
        "sources": [
            {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hampshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "GOV.UK / DHSC", "title": "New Hospital Programme update January 2025", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Hampshire Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Bedfordshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Bedfordshire Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs at Bedfordshire Hospitals — formed in April 2020 from the merger of Bedford Hospital and Luton and Dunstable University Hospital. The trust runs Bedford Hospital and the L&D, plus satellite clinics. The L&D is one of the busiest A&Es in the East of England; both estates have multi-decade build vintages.",
        "beneficiaries": "700,000+ patients across Bedford, Luton, Dunstable and the surrounding Beds/Herts/Bucks border — A&E, maternity, acute medicine across two sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.87M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "2 acute hospitals (Bedford + L&D) + community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "L&D", "value": "Among busiest A&E departments in East of England · 1939 origin + many additions"},
            {"label": "Bedford Hospital", "value": "Multi-decade vintage · backlog and refurbishment pressure"},
            {"label": "Merger context", "value": "April 2020 merger · ongoing post-merger estate-rationalisation captured here"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at L&D · LED rollout multi-site"},
            {"label": "YoY change", "value": "c. +5-6% (energy + post-merger consolidation)"},
            {"label": "Peer benchmark", "value": "Mid-range vs East of England acute peers per m²"}
        ],
        "notes": "Bedfordshire Hospitals' Premises (other) line continues to reflect post-2020-merger estate-integration spend (FM contract harmonisation, BMS migration, asset-management system unification). The L&D's multi-decade vintage and high A&E throughput drive elevated soft-FM (cleaning frequency) and utility costs. RM6011 energy reset feeds the YoY uplift; backlog pressure is documented in NHS ERIC returns.",
        "sources": [
            {"publisher": "Bedfordshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bedfordshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Bedfordshire Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust"}],
        "description": "Mental-health and learning-disability premises operating costs across CNTW's very large geographic estate — St Nicholas Hospital (Newcastle), St George's Park Hospital (Morpeth), Hopewood Park (Sunderland, opened 2014), Walkergate Park (neuro-rehab) and the Carleton Clinic (Carlisle), plus a network of 60+ community sites stretching from the Scottish border to Tyne and Wear. One of England's largest MH trusts by geography.",
        "beneficiaries": "1.7M residents across Cumbria, Northumberland, Newcastle, North Tyneside, Gateshead, South Tyneside and Sunderland — adult acute MH, CAMHS, learning disability, neuro-rehab, secure forensic services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.80M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "5+ MH inpatient hospitals + 60+ community sites · stretches Scottish border to Sunderland"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "MH-specific", "value": "s.136 places of safety · PICU · forensic medium-secure · CAMHS Tier 4 · LD inpatient utilities"},
            {"label": "Hopewood Park", "value": "Modern (2014) build · efficient operating cost"},
            {"label": "Carleton Clinic", "value": "Cumbria MH inpatient site · rural-resilience cost premium"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump works at multiple sites · LED rollout"},
            {"label": "YoY change", "value": "c. +5-6% (energy + dispersed-estate uplift)"},
            {"label": "Peer benchmark", "value": "Above MH median per inpatient bed (geographic dispersion)"}
        ],
        "notes": "CNTW's Premises (other) line is structurally inflated by one of NHS England's largest MH-trust geographies (Cumbria to Sunderland), with the Carleton Clinic in Carlisle adding rural-resilience cost above urban MH peers. The forensic medium-secure estate carries higher security and HVAC operating cost than general adult acute MH. Hopewood Park's modern fabric provides some operating-cost mitigation.",
        "sources": [
            {"publisher": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cntw.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Maidstone And Tunbridge Wells NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Maidstone And Tunbridge Wells NHS Trust"}],
        "description": "Premises running costs at MTW — Maidstone Hospital and Tunbridge Wells Hospital at Pembury (a 2011 PFI new-build replacing the legacy Kent and Sussex Hospital). The Pembury PFI bundles much hard FM into the unitary charge (D4_11), so Premises (other) is dominated by Maidstone, satellite estate and PFI variations.",
        "beneficiaries": "590,000+ patients across west Kent and parts of East Sussex — A&E + maternity at Pembury, planned care + Kent Cancer Centre at Maidstone.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.77M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "2 acute hospitals + Kent Cancer Centre + community clinics"},
            {"label": "Hard FM model", "value": "Pembury PFI envelope · Maidstone in-house Estates"},
            {"label": "PFI footprint", "value": "Pembury PFI (Project Co — Equion/Bouygues) — unitary charge in D4_11"},
            {"label": "Maidstone estate", "value": "1980s build · Kent Cancer Centre LINAC bunkers · specialty utility loads"},
            {"label": "Kent Cancer Centre", "value": "Regional cancer with LINAC bunkers · 24/7 utility resilience driver"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Maidstone · PFI-led BMS at Pembury"},
            {"label": "YoY change", "value": "c. +5% (energy + PFI variations)"},
            {"label": "Peer benchmark", "value": "Below acute median per m² (Pembury PFI absorbs hard FM)"}
        ],
        "notes": "MTW's Premises (other) line is moderated by the Pembury PFI which carries hard FM, soft FM and lifecycle into the unitary charge (D4_11), leaving operating spend concentrated on Maidstone and the Kent Cancer Centre. Cancer-centre LINAC bunkers and specialty equipment drive elevated utility resilience cost. PFI variations as service patterns evolve at Pembury feed into this line at the trust-borne margin.",
        "sources": [
            {"publisher": "Maidstone and Tunbridge Wells NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mtw.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"}
        ],
        "related": ["Maidstone And Tunbridge Wells NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Essex Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Essex Partnership University NHS Foundation Trust"}],
        "description": "Mental-health and community premises operating costs across EPUT's very large Essex estate — major MH inpatient sites at the Linden Centre (Chelmsford), Basildon Mental Health Unit, Rochford Hospital, plus community-hospital estate (Brentwood Community Hospital, Halstead, Saffron Walden, etc.) and 100+ community clinics. EPUT is under sustained scrutiny following the Lampard Inquiry into Essex MH deaths and has had estate condition cited as a contributing concern.",
        "beneficiaries": "1.8M residents of Essex plus parts of Bedfordshire and Suffolk — adult acute MH, CAMHS, learning disability, community physical-health, community hospital inpatients.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.62M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Multiple MH inpatient sites + 6+ community hospitals + 100+ community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "MH-specific", "value": "s.136 places of safety · PICU · CAMHS Tier 4 · ligature-risk environmental works"},
            {"label": "Lampard Inquiry context", "value": "Statutory inquiry into Essex MH deaths · estate / ligature concerns cited"},
            {"label": "Linden Centre", "value": "Subject of inquest findings · ongoing environmental refurbishment programme"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at multiple community hospitals · LED rollout"},
            {"label": "YoY change", "value": "c. +6-7% (Lampard-driven environmental works + energy)"},
            {"label": "Peer benchmark", "value": "Above MH median per inpatient bed (community-hospital estate + ligature works)"}
        ],
        "notes": "EPUT's Premises (other) line is structurally elevated by ongoing ligature-risk and ward-environment refurbishment driven by inquest findings and the Lampard Inquiry into Essex MH deaths. The trust's unusual mix of MH inpatient + community-hospital estate adds operating cost above pure-MH peers. Capital recovery for environmental works falls partly on operating spend captured here.",
        "sources": [
            {"publisher": "Essex Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://eput.nhs.uk/about-us/publications/"},
            {"publisher": "Lampard Inquiry", "title": "Independent inquiry into deaths in mental health units in Essex", "url": "https://lampardinquiry.org.uk/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Essex Partnership University NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs at ASPH — St Peter's Hospital (Chertsey, the principal acute, with 1990s-2000s build) and Ashford Hospital (Ashford, Surrey — smaller-acute and elective focus). The two-site model splits A&E (St Peter's only) from elective and ambulatory (Ashford), shaping site-specific operating costs. Operating in close partnership with Royal Surrey via the Surrey Heartlands ICS.",
        "beneficiaries": "410,000+ patients across north-west Surrey, Spelthorne and parts of Hounslow — A&E + maternity at St Peter's, planned care + ambulatory at Ashford.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.55M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 acute hospitals (St Peter's + Ashford) + community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "St Peter's", "value": "Principal acute · 1990s-2000s build · A&E + maternity"},
            {"label": "Ashford", "value": "Elective + ambulatory focus · Heathrow proximity (noise/airspace planning context)"},
            {"label": "ICS partnership", "value": "Surrey Heartlands ICS · cross-trust estate strategy with Royal Surrey emerging"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at St Peter's · LED rollout"},
            {"label": "YoY change", "value": "c. +5-7% (energy + 5-7% hard-FM inflation)"},
            {"label": "Peer benchmark", "value": "Mid-range vs south-east acute peers per m²"}
        ],
        "notes": "ASPH's Premises (other) line reflects a relatively modern St Peter's estate with moderate backlog, plus the unusual Heathrow-adjacent Ashford site whose airspace and noise planning context affects retrofit options. Surrey Heartlands ICS partnership is starting to drive shared estate-strategy work with Royal Surrey. RM6011 energy reset and 5-7% hard-FM inflation feed the YoY uplift.",
        "sources": [
            {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ashfordstpeters.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Barnet, Enfield And Haringey Mental Health NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Barnet, Enfield And Haringey Mental Health NHS Trust"}],
        "description": "Mental-health premises operating costs across BEH-MHT's north-London estate — Chase Farm (St Michael's Wing MH inpatient unit), the Bracton Centre forensic services partnership, plus St Ann's Hospital (Haringey, where the new MH inpatient block opened in the 2010s) and a network of community MH clinics. BEH operates closely with Camden and Islington and other north-London MH providers under the North London MH Partnership.",
        "beneficiaries": "1.2M residents of Barnet, Enfield and Haringey — adult acute MH, older-people's MH, forensic services, eating disorders.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.43M"},
            {"label": "Share of trust total opex", "value": "c. 7%"},
            {"label": "Estate scale", "value": "MH inpatient sites at St Ann's Haringey + Chase Farm + community clinics across N. London"},
            {"label": "Hard FM model", "value": "In-house Estates plus shared services with co-located acute trusts"},
            {"label": "MH-specific", "value": "s.136 places of safety · PICU · forensic mid-secure · ligature works"},
            {"label": "St Ann's", "value": "New MH inpatient block · efficient operating cost · former site partly redeveloped for housing"},
            {"label": "Co-location", "value": "Chase Farm shared with Royal Free's Chase Farm Hospital · shared utilities/services"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + BMS works at St Ann's · heat decarbonisation feasibility"},
            {"label": "YoY change", "value": "c. +5-6% (London energy reset + soft FM)"},
            {"label": "Peer benchmark", "value": "Above MH median % opex (small trust + London soft-FM premium)"}
        ],
        "notes": "BEH-MHT's Premises (other) line carries a high share of total opex because the trust is comparatively small — fixed estate and shared-services costs spread across a smaller revenue base. Co-location at Chase Farm with Royal Free creates shared-services complexity (utilities apportionment, joint FM contracts) that flows through this line. The North London MH Partnership is driving cross-trust estate-rationalisation discussions.",
        "sources": [
            {"publisher": "Barnet, Enfield and Haringey Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.beh-mht.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "CQC", "title": "Provider profile — Barnet, Enfield and Haringey MHT", "url": "https://www.cqc.org.uk/provider/RRP"}
        ],
        "related": ["Barnet, Enfield And Haringey Mental Health NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Royal Surrey NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal Surrey NHS Foundation Trust"}],
        "description": "Premises running costs at Royal Surrey County Hospital (Guildford) — a single-site ~520-bed acute hospital with co-located St Luke's Cancer Centre (regional radiotherapy and oncology). The trust is partnered with University of Surrey (the next-door School of Veterinary Medicine and Faculty of Health Sciences). Operating in close partnership with Ashford and St Peter's via Surrey Heartlands ICS.",
        "beneficiaries": "330,000+ patients across Guildford, Waverley and the surrounding south-west Surrey area — A&E, maternity, acute medicine and St Luke's regional cancer services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.29M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute (RSCH ~520 beds) + St Luke's Cancer Centre + community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "St Luke's Cancer Centre", "value": "Regional radiotherapy · LINAC bunkers · 24/7 utility resilience driver"},
            {"label": "University partnership", "value": "Co-location with University of Surrey campus · shared research-facility infrastructure"},
            {"label": "Estate age", "value": "Mid-1980s base + later additions · backlog moderate"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works · LED rollout · partnership with University on decarbonisation"},
            {"label": "YoY change", "value": "c. +5-6% (energy + 5-7% hard-FM inflation)"},
            {"label": "Peer benchmark", "value": "Mid-range vs south-east acute peers per m²"}
        ],
        "notes": "RSCH's Premises (other) line is shaped by St Luke's Cancer Centre's specialty utility loads (LINAC bunkers require continuous cooling and shielded power) and the University of Surrey co-location which adds shared-services complexity. The trust is among the more-mature Salix / PSDS grant recipients. Surrey Heartlands ICS partnership with Ashford and St Peter's is starting to drive cross-trust estate strategy.",
        "sources": [
            {"publisher": "Royal Surrey NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalsurrey.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Royal Surrey NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Northern Lincolnshire and Goole NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Northern Lincolnshire and Goole NHS Foundation Trust"}],
        "description": "Premises running costs across NLAG's three-acute estate — Diana, Princess of Wales Hospital (Grimsby), Scunthorpe General Hospital, and Goole and District Hospital. NLAG is in formal group working with Hull University Teaching Hospitals (Humber Health Partnership) which has begun consolidating estate strategy and FM. Both Grimsby and Scunthorpe are NHP cohort sites with redevelopment plans deferred under Reset.",
        "beneficiaries": "400,000+ patients across northern Lincolnshire and East Riding — A&E + maternity at Grimsby and Scunthorpe, planned care + community at Goole.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.06M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "3 acute hospitals + community clinics · cross-Humber footprint"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Humber Health Partnership", "value": "Group working with Hull University Teaching Hospitals · shared estate strategy"},
            {"label": "NHP scheme status", "value": "Grimsby + Scunthorpe in NHP cohort · Reset Jan 2025 deferred timelines"},
            {"label": "Coastal exposure", "value": "Grimsby coastal · saline-air corrosion premium on hard FM"},
            {"label": "Estate age", "value": "Both main acutes 1980s-90s · backlog pressure"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Scunthorpe · LED rollout multi-site"},
            {"label": "YoY change", "value": "c. +6-7% (extending operating life pre-NHP + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (estate age + dispersion)"}
        ],
        "notes": "NLAG's Premises (other) line is structurally elevated by NHP Reset deferrals at both main acutes, Grimsby's coastal exposure, and the multi-site geography across northern Lincs into East Riding. Humber Health Partnership group-working with Hull is starting to drive shared FM and estate-strategy efficiency, but the dominant driver remains extending operating life of fabric scheduled for replacement.",
        "sources": [
            {"publisher": "Northern Lincolnshire and Goole NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nlg.nhs.uk/about/publications/"},
            {"publisher": "GOV.UK / DHSC", "title": "New Hospital Programme update January 2025", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Northern Lincolnshire and Goole NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — South East Coast Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "South East Coast Ambulance Service NHS Foundation Trust"}],
        "description": "Premises running costs across SECAmb's ambulance estate — 110 Make Ready Centres, ambulance stations and community response posts across Kent, Surrey, Sussex and parts of Hampshire, plus HART (Hazardous Area Response Team) bases, Emergency Operations Centres at Coxheath (Kent) and Crawley (Sussex), training centres and vehicle workshops. Ambulance estates differ from acute trust estates — vehicle-fleet logistics, fuel, and 24/7 EOC resilience dominate operating cost.",
        "beneficiaries": "4.7M residents of Kent, Surrey, Sussex and parts of north-east Hampshire — 999 emergency response, NHS 111, HCP transfers, plus event medical cover.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.02M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "110+ ambulance stations + Make Ready Centres + 2 EOCs (Coxheath + Crawley) + HART bases + workshops"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts · ambulance-specific fleet logistics"},
            {"label": "Make Ready Centres", "value": "Centralised vehicle preparation + restocking model · operating-cost concentration vs traditional stations"},
            {"label": "EOC resilience", "value": "Coxheath + Crawley dual EOC · 24/7 power and comms-resilience driver"},
            {"label": "HART bases", "value": "Specialist hazardous-area response teams · CBRN equipment + training estate"},
            {"label": "Fleet workshops", "value": "Vehicle servicing in-house at multiple sites · workshop utilities + fuel"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at Make Ready Centres · EV-charger rollout (zero-emission ambulance trial)"},
            {"label": "YoY change", "value": "c. +5-6% (energy reset + EV-charger infrastructure)"},
            {"label": "Peer benchmark", "value": "Mid-range vs other ambulance trusts per station"}
        ],
        "notes": "SECAmb's Premises (other) line is unlike acute-trust estates — dominated by 110+ small operational sites (stations, response posts, Make Ready Centres) plus two EOCs whose 24/7 power and comms-resilience requirements drive utility cost. The trust is investing in EV-charger infrastructure ahead of zero-emission ambulance fleet trials, which is starting to feed into operating spend. CQC inspection improvement plan and call-handling reform have estate implications at the EOCs.",
        "sources": [
            {"publisher": "South East Coast Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.secamb.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) — Ambulance Trusts", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "NHS England", "title": "Greener NHS — zero-emission ambulance programme", "url": "https://www.england.nhs.uk/greenernhs/"}
        ],
        "related": ["South East Coast Ambulance Service NHS Foundation Trust", "Premises & Infrastructure"]
    },
}
