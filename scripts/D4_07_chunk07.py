# -*- coding: utf-8 -*-
# D4_07 Premises (other) — chunk 07 (20 NHS trusts)
# Hand-curated trust-specific enrichment entries.

NEW = {
    "Premises (other) — North Tees and Hartlepool NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "North Tees and Hartlepool NHS Foundation Trust"}],
        "description": "Premises running costs across NTHFT's two-acute estate — University Hospital of North Tees (Stockton-on-Tees, the principal acute) and University Hospital of Hartlepool (a smaller-acute / planned-care site post the long-running North Tees & Hartlepool reconfiguration). Spend is shaped by ageing 1960s-70s build at North Tees and the unusually long 'Momentum' new-hospital saga.",
        "beneficiaries": "400,000+ patients across Stockton, Hartlepool and East Durham — major emergency + maternity at North Tees, planned care + diagnostics at Hartlepool.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.08M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 acute hospitals + community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "North Tees estate", "value": "1968 build · among the oldest fully-operational acute estates in England · backlog pressure"},
            {"label": "NHP scheme status", "value": "North Tees replacement long-promised (Momentum); deferred under NHP Reset Jan 2025"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at North Tees · LED rollout multi-site"},
            {"label": "YoY change", "value": "c. +6-8% (energy + ageing-fabric backlog)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (estate age)"}
        ],
        "notes": "NTHFT carries one of NHS England's longest-standing 'replacement-promised' estate stories — University Hospital of North Tees has been earmarked for replacement repeatedly since 2007 and the NHP Reset has deferred it again, extending operating life of plant and fabric originally built in 1968. The Hartlepool site's reconfiguration to planned care has shifted utility-load patterns. Backlog maintenance is a recurring board theme.",
        "sources": [
            {"publisher": "North Tees and Hartlepool NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nth.nhs.uk/about/publications/"},
            {"publisher": "DHSC / NHP", "title": "New Hospital Programme update (Reset)", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["North Tees and Hartlepool NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Sussex Community NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Sussex Community NHS Foundation Trust"}],
        "description": "Community-trust premises running costs across SCFT's dispersed Sussex footprint — community hospitals (Crawley, Lewes Victoria, Bognor War Memorial, Salvington Lodge, Brighton General campus), Crowborough birthing centre, plus a very large clinic estate operating from leased and NHS Property Services-owned buildings across West Sussex and Brighton & Hove.",
        "beneficiaries": "1.6M residents of Brighton & Hove, West Sussex and parts of East Sussex — community nursing, intermediate-care beds, children's services, MSK and rehabilitation.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.03M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "5+ community hospitals + 100+ clinic and base sites · large mix of NHSPS leases"},
            {"label": "Hard FM model", "value": "In-house Estates + NHSPS service-charges where landlord"},
            {"label": "Community-trust profile", "value": "Estate dominated by small leased clinics and intermediate-care beds"},
            {"label": "Crawley + Bognor", "value": "Community hospitals with intermediate-care wards · ageing fabric"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump and LED works at community hospitals"},
            {"label": "YoY change", "value": "c. +5-7% (NHSPS service-charge uplift + energy)"},
            {"label": "Peer benchmark", "value": "Mid-range vs community-trust peers per site"}
        ],
        "notes": "SCFT's premises spend is shaped by an unusually fragmented community estate — the trust is a major occupier of NHS Property Services and Community Health Partnerships buildings, so a material share of this line is service-charge pass-through rather than direct hard FM. Service-charge uplifts at NHSPS in 2024-25 (well above general inflation) feed directly into this line. Community-hospital backlog is a board concern.",
        "sources": [
            {"publisher": "Sussex Community NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sussexcommunity.nhs.uk/about-us/publications"},
            {"publisher": "NHS Property Services", "title": "Service charges and rent guidance", "url": "https://www.property.nhs.uk/our-services/managing-property/service-charges/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Sussex Community NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — South Western Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "South Western Ambulance Service NHS Foundation Trust"}],
        "description": "Ambulance-trust premises running costs across SWASFT's vast south-west footprint — 96 ambulance stations from Cornwall to Wiltshire, two emergency operations centres (St Leonards and Exeter), HART and SORT bases, vehicle preparation hubs and training centres. Among NHS England's most geographically-dispersed estates with material rural fuel and travel costs feeding through.",
        "beneficiaries": "5.5M residents across Cornwall, Devon, Dorset, Somerset, Wiltshire, Bristol, Bath & North East Somerset, Gloucestershire and the Isles of Scilly — 999 emergency response and 111 integrated urgent care.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.86M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "96 ambulance stations + 2 EOCs + HART/SORT bases + vehicle prep hubs + training centres"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts"},
            {"label": "Geographic spread", "value": "Largest English ambulance-trust footprint by area · 10,000+ sq miles"},
            {"label": "Make-Ready model", "value": "Centralised vehicle prep hubs reduce station-level workshop load"},
            {"label": "Net Zero milestone", "value": "EV charging infrastructure rollout at stations · PSDS heat-pump trials"},
            {"label": "YoY change", "value": "c. +5-7% (energy + EV charging capex moving to opex)"},
            {"label": "Peer benchmark", "value": "Mid-range vs ambulance peers; high per-station given rural dispersion"}
        ],
        "notes": "SWASFT's premises cost is shaped by NHS England's largest ambulance-trust geographic footprint, the move to centralised Make-Ready hubs (which shifts cost between line items), and the leading-edge rollout of EV charging infrastructure as the fleet electrifies. The two-EOC resilient model (St Leonards + Exeter) drives elevated power, HVAC and security spend on those sites. Rural station fabric is largely 1970s-1990s vintage with backlog pressure.",
        "sources": [
            {"publisher": "South Western Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swast.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Ambulance services estates and fleet strategy", "url": "https://www.england.nhs.uk/ambulance-services/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["South Western Ambulance Service NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Medway NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Medway NHS Foundation Trust"}],
        "description": "Premises running costs at Medway — Medway Maritime Hospital (Gillingham), the principal acute site for the Medway towns, on a single campus alongside Kent and Medway NHS and Social Care Partnership Trust occupants. Spend is shaped by the 1990s-vintage main hospital block, ongoing emergency-department reconfiguration, and the trust's continuous improvement journey out of historical CQC special measures.",
        "beneficiaries": "424,000+ patients across the Medway towns and Swale — major emergency, maternity and acute services at Medway Maritime.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.81M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "1 acute site (Medway Maritime ~580 beds) + clinic outposts"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Estate vintage", "value": "Main block 1990s with successive ED + ward additions · backlog pressure"},
            {"label": "Co-location", "value": "Shared campus with KMPT (mental health) — shared estate cost recoveries"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility · LED rollout main building"},
            {"label": "YoY change", "value": "c. +5-7% (energy + ED reconfiguration decant)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers per m²"}
        ],
        "notes": "Medway's single-site model concentrates premises spend on Maritime, with no PFI absorbing hard FM. Continuous emergency-department and AMU reconfiguration — driven by recovery from historical CQC concerns — generates rolling decant and refurbishment cost. Shared-campus arrangements with KMPT yield modest cost recoveries. RM6011 energy reset is the main 2024-25 cost driver.",
        "sources": [
            {"publisher": "Medway NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.medway.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Provider finance returns 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Medway NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Princess Alexandra Hospital NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Princess Alexandra Hospital NHS Trust"}],
        "description": "Premises running costs at PAH — The Princess Alexandra Hospital (Harlow, Essex), a 1965-vintage acute estate with confirmed RAAC and one of the most-publicised structural-condition cases in NHS England. The Premises (other) line carries unusually high RAAC mitigation and props/monitoring cost relative to trust scale.",
        "beneficiaries": "350,000+ patients across west Essex and east Hertfordshire — emergency, maternity and acute services at Harlow.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.79M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "1 acute hospital (PAH Harlow ~414 beds) + outpatient outposts"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "RAAC status", "value": "Confirmed RAAC throughout main block (HSSIB Sep 2023) · among most-affected trusts"},
            {"label": "NHP scheme status", "value": "PAH replacement in original NHP cohort with confirmed funding · Reset Jan 2025 reaffirmed but timeline uncertain"},
            {"label": "Decant strategy", "value": "Continuous structural monitoring + ward-level decant + temporary clinical accommodation"},
            {"label": "Net Zero milestone", "value": "Constrained by RAAC priority; new-build will deliver Net Zero"},
            {"label": "YoY change", "value": "c. +8-10% (RAAC mitigation + energy)"},
            {"label": "Peer benchmark", "value": "Significantly above acute median per m² (RAAC mitigation premium)"}
        ],
        "notes": "PAH carries one of the highest RAAC-mitigation operating burdens in NHS England relative to trust size — virtually the entire main hospital block is RAAC-constructed and requires continuous structural surveillance, props installation and clinical decant. The new PAH replacement remains in the NHP cohort but the Reset has not yet given a fixed delivery date, meaning every additional year of operating life pushes more cost into this line.",
        "sources": [
            {"publisher": "The Princess Alexandra Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.pah.nhs.uk/about-us/publications"},
            {"publisher": "HSSIB", "title": "RAAC in the NHS — investigation report", "url": "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/"},
            {"publisher": "DHSC / NHP", "title": "New Hospital Programme update (Reset)", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"}
        ],
        "related": ["The Princess Alexandra Hospital NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Cambridgeshire and Peterborough NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Cambridgeshire and Peterborough NHS Foundation Trust"}],
        "description": "Mental-health and community premises operating costs across CPFT's Cambridgeshire and Peterborough estate — Fulbourn Hospital (Cambridge), Cavell Centre (Peterborough), plus inpatient and community sites including the Mulberry Ward (CAMHS), Phoenix Centre (eating disorders), and a wide community-clinic estate. The trust co-locates substantially with Cambridge University Hospitals on the Cambridge Biomedical Campus.",
        "beneficiaries": "1M residents of Cambridgeshire and Peterborough — adult acute MH inpatients, CAMHS, eating disorders, older-people's MH, learning disabilities and community physical-health.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.69M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "Fulbourn + Cavell + 50+ community sites"},
            {"label": "Hard FM model", "value": "In-house Estates · CUH shared services on Cambridge campus"},
            {"label": "MH-specific", "value": "s.136 suites at Fulbourn + Cavell · PICU · Phoenix eating-disorders unit"},
            {"label": "Fulbourn site", "value": "Historic asylum estate (1858 origin) · Victorian fabric coexists with new Adult MH units"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Fulbourn · LED rollout community"},
            {"label": "YoY change", "value": "c. +5-6% (energy + Fulbourn fabric upkeep)"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH peer median per inpatient bed"}
        ],
        "notes": "CPFT's premises spend is shaped by the historic Fulbourn estate — Victorian asylum buildings sit alongside modern inpatient blocks, with the trust managing ligature-risk environment upgrades and ward refurbishment in parallel. Cambridge Biomedical Campus co-location with CUH brings shared estate-services arrangements but also exposure to CUH energy procurement. The Cavell Centre in Peterborough is a 2010s purpose-built MH facility with lower per-m² operating cost.",
        "sources": [
            {"publisher": "Cambridgeshire and Peterborough NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cpft.nhs.uk/about-us/publications.htm"},
            {"publisher": "CQC", "title": "CPFT inspection reports (provider RT1)", "url": "https://www.cqc.org.uk/provider/RT1"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Cambridgeshire and Peterborough NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Dorset Healthcare University NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Dorset Healthcare University NHS Foundation Trust"}],
        "description": "Mental-health and community premises operating costs across Dorset Healthcare's countywide estate — St Ann's Hospital (Poole, the principal MH inpatient site), Forston Clinic (Charminster), Alderney Hospital, plus Bridport, Blandford, Sherborne, Shaftesbury, Swanage, Wareham and Wimborne community hospitals. The integrated MH + community model creates one of the largest combined-trust estates in southern England.",
        "beneficiaries": "850,000+ residents of Dorset, Bournemouth, Christchurch and Poole — adult acute MH, CAMHS, older-people's MH, learning disabilities, plus community physical-health and community-hospital inpatients.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.51M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "3 MH inpatient hospitals + 7 community hospitals + 100+ clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts"},
            {"label": "MH-specific", "value": "s.136 suite at St Ann's · PICU · CAMHS Pebble Lodge"},
            {"label": "Coastal exposure", "value": "Poole, Bournemouth, Swanage, Bridport sites carry saline-air corrosion premium"},
            {"label": "Community-hospital network", "value": "7 small acute/rehab sites · rural winter resilience cost"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump rollout at community hospitals · LED multi-site"},
            {"label": "YoY change", "value": "c. +5-7% (coastal premium + energy)"},
            {"label": "Peer benchmark", "value": "Above MH median per inpatient bed (community-hospital footprint)"}
        ],
        "notes": "Dorset Healthcare's premises cost is driven by an unusual combined MH + community-hospital model with seven community hospitals adding small-site overhead, plus extensive coastal exposure across Poole, Bournemouth and Purbeck which lifts hard-FM cost. St Ann's is the focus of MH inpatient capital strategy. The 2024-25 uplift reflects energy reset and substantial PSDS-funded heat-pump rollouts at community sites moving from capex to opex.",
        "sources": [
            {"publisher": "Dorset HealthCare University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dorsethealthcare.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Provider finance returns 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Dorset Healthcare University NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Southern Health NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Southern Health NHS Foundation Trust"}],
        "description": "Mental-health and community premises operating costs across Southern Health's Hampshire estate — Antelope House (Southampton), Melbury Lodge (Winchester), Parklands (Basingstoke), Tatchbury Mount (New Forest), Ravenswood House (medium-secure), Western Community Hospital, plus Lymington, Romsey, Andover and other community hospitals. The trust has rebuilt its premises governance after the 2015 Mazars review.",
        "beneficiaries": "1.4M residents of Hampshire — adult acute MH, CAMHS, older-people's MH, learning disabilities, secure services, plus community physical-health.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.32M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "5+ MH inpatient hospitals + 4 community hospitals + Ravenswood medium-secure"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · medium-secure (Ravenswood) · LD inpatient utilities"},
            {"label": "Estate vintage", "value": "Mix of Victorian asylum legacy (Tatchbury Mount) and modern purpose-build"},
            {"label": "Governance context", "value": "Post Mazars 2015 review — premises safety / ligature programme institutionalised"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump rollout · LED community programme"},
            {"label": "YoY change", "value": "c. +5-6% (energy + ligature/environmental upgrade programme)"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH peer median per inpatient bed"}
        ],
        "notes": "Southern Health's premises spend has been structurally elevated since the 2015 Mazars review by an institutionalised ligature-risk and environmental-safety upgrade programme that runs continuously across all inpatient units. The trust's combined MH + community + medium-secure portfolio creates an unusually mixed estate. Tatchbury Mount's Victorian legacy buildings carry above-average hard-FM cost.",
        "sources": [
            {"publisher": "Southern Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southernhealth.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Mazars review and Southern Health response", "url": "https://www.england.nhs.uk/2015/12/mazars-investigation/"},
            {"publisher": "CQC", "title": "Southern Health inspection reports (provider RW1)", "url": "https://www.cqc.org.uk/provider/RW1"}
        ],
        "related": ["Southern Health NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Isle of Wight NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Isle of Wight NHS Trust"}],
        "description": "Premises running costs at the Isle of Wight NHS Trust — uniquely the only fully integrated acute + community + mental health + ambulance trust in NHS England. The estate centres on St Mary's Hospital (Newport), with Sevenacres MH unit, ambulance stations across the island, and community clinics. Spend is shaped by island isolation, single-site dependency, and resilience requirements with no acute back-up.",
        "beneficiaries": "140,000 island residents + ~3M annual visitors — emergency, maternity, acute, MH, ambulance and community services with no off-island fallback for time-critical care.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.21M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "1 acute (St Mary's) + Sevenacres MH unit + 4 ambulance stations + community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with on-island sub-contracts (limited supplier market)"},
            {"label": "Integrated-trust profile", "value": "Only fully integrated acute+community+MH+ambulance trust in NHSE"},
            {"label": "Island premium", "value": "Logistics + ferry costs add 5-10% to materials and contractor mobilisation"},
            {"label": "Resilience requirements", "value": "No mainland fallback drives elevated standby-power, oxygen-plant, water resilience"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at St Mary's · LED rollout"},
            {"label": "YoY change", "value": "c. +6-8% (island premium + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (island isolation premium)"}
        ],
        "notes": "The Isle of Wight is unique in NHS England — no other trust runs all four service streams (acute, community, MH, ambulance) on a single estate footprint with no off-island fallback. Island isolation lifts every cost: contractor mobilisation across the Solent, materials logistics, and the requirement that St Mary's stand alone for major emergencies all drive premises (other) above mainland equivalents. Recovery from historical CQC concerns continues to underwrite estate investment.",
        "sources": [
            {"publisher": "Isle of Wight NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.iow.nhs.uk/about-us/publications"},
            {"publisher": "CQC", "title": "Isle of Wight NHS Trust inspection reports (provider R1F)", "url": "https://www.cqc.org.uk/provider/R1F"},
            {"publisher": "NHS England", "title": "Provider finance returns 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Isle of Wight NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Rotherham NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Rotherham NHS Foundation Trust"}],
        "description": "Premises running costs at TRFT — Rotherham Hospital (Moorgate, the principal acute) plus a network of community clinics including Breathing Space, Rotherham Community Health Centre, and Maltby/Wath/Rawmarsh sites. Spend is shaped by the single-acute-site model and the trust's combined acute + community service portfolio.",
        "beneficiaries": "265,000+ residents of Rotherham — emergency, maternity, planned care, community physical-health and breathing-disease services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.16M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute (Rotherham Hospital ~440 beds) + Breathing Space + community sites"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Integrated-trust profile", "value": "Acute + community combined trust · estate spans both portfolios"},
            {"label": "Estate vintage", "value": "Main hospital 1970s tower + later additions · backlog pressure"},
            {"label": "Breathing Space", "value": "Specialist purpose-build COPD centre · low operating cost per m²"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Rotherham Hospital · LED rollout"},
            {"label": "YoY change", "value": "c. +5-7% (energy + ageing fabric)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers per m²"}
        ],
        "notes": "TRFT operates a relatively contained single-acute-site estate without the multi-site dispersion that lifts comparable trusts. The 1970s tower remains the principal building with continuous ward and theatre refurbishment generating backlog and decant cost. The Breathing Space respiratory centre is a notable specialist build with lower operating cost. RM6011 energy reset is the main 2024-25 cost driver alongside hard-FM contract inflation.",
        "sources": [
            {"publisher": "The Rotherham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.therotherhamft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Provider finance returns 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["The Rotherham NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — South Central Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "South Central Ambulance Service NHS Foundation Trust"}],
        "description": "Ambulance-trust premises running costs across SCAS's Thames-Valley and central-south footprint — ~70 ambulance stations and ambulance resource centres across Hampshire, Berkshire, Buckinghamshire and Oxfordshire, two emergency operations centres (Bicester and Otterbourne), a HART base, vehicle preparation hubs and training centres. The trust also runs NHS 111 with associated estate.",
        "beneficiaries": "7M+ residents across Hampshire, Berkshire, Buckinghamshire and Oxfordshire — 999 emergency response, 111 integrated urgent care and patient transport.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.14M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "~70 ambulance stations + 2 EOCs + HART base + 111 contact centres"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts"},
            {"label": "EOC resilience", "value": "Bicester + Otterbourne dual-site model · power and HVAC redundancy"},
            {"label": "Make-Ready model", "value": "Centralised vehicle prep hubs reducing station workshop load"},
            {"label": "111 estate", "value": "Contact-centre overhead in addition to ambulance stations"},
            {"label": "Net Zero milestone", "value": "EV charging rollout at stations · PSDS heat-pump trials"},
            {"label": "YoY change", "value": "c. +5-7% (energy + EV charging capex moving to opex)"},
            {"label": "Peer benchmark", "value": "Mid-range vs ambulance peers per station"}
        ],
        "notes": "SCAS combines ambulance station estate with significant 111 contact-centre overhead, which other ambulance trusts often house separately. The dual EOC resilience model at Bicester and Otterbourne drives elevated power and HVAC spend. Recent organisational rebuild post-2022 CQC inspection has emphasised estate condition as part of governance recovery. Fleet electrification is generating new charging-infrastructure operating cost.",
        "sources": [
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.scas.nhs.uk/about-us/publications/"},
            {"publisher": "CQC", "title": "SCAS inspection reports (provider RYE)", "url": "https://www.cqc.org.uk/provider/RYE"},
            {"publisher": "NHS England", "title": "Ambulance services estates and fleet strategy", "url": "https://www.england.nhs.uk/ambulance-services/"}
        ],
        "related": ["South Central Ambulance Service NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — North West Anglia NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "North West Anglia NHS Foundation Trust"}],
        "description": "Premises running costs across NWAFT's three-acute estate post the 2017 merger — Peterborough City Hospital (a 2010-vintage PFI single-site rebuild), Hinchingbrooke Hospital (Huntingdon, RAAC-affected and an NHP cohort site) and Stamford and Rutland Hospital. The Peterborough PFI absorbs hard FM into D4_11, while RAAC mitigation at Hinchingbrooke drives Premises (other) cost.",
        "beneficiaries": "850,000+ patients across Peterborough, Huntingdonshire, Cambridgeshire fringes and Rutland — emergency, maternity and acute services at Peterborough + Hinchingbrooke; planned care + rehabilitation at Stamford.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.03M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "3 acute hospitals (Peterborough + Hinchingbrooke + Stamford)"},
            {"label": "Hard FM model", "value": "Peterborough PFI envelope · Hinchingbrooke + Stamford in-house Estates"},
            {"label": "PFI footprint", "value": "Peterborough City PFI (Project Co — Equitix/Brookfield) — unitary charge in D4_11"},
            {"label": "RAAC status", "value": "Hinchingbrooke confirmed RAAC throughout (HSSIB Sep 2023) · among most-affected"},
            {"label": "NHP scheme status", "value": "Hinchingbrooke replacement in NHP cohort · Reset Jan 2025 reaffirmed but timeline uncertain"},
            {"label": "Net Zero milestone", "value": "Constrained at Hinchingbrooke by RAAC priority; PSDS works at Stamford"},
            {"label": "YoY change", "value": "c. +7-9% (RAAC + energy + PFI variations)"},
            {"label": "Peer benchmark", "value": "Mixed — Peterborough below median (PFI), Hinchingbrooke above (RAAC)"}
        ],
        "notes": "NWAFT has the unusual combination of a major acute PFI (Peterborough) and one of NHS England's most-RAAC-affected acute estates (Hinchingbrooke), creating a bifurcated cost profile. RAAC mitigation at Hinchingbrooke continues to inflate Premises (other) with structural surveys, props and decant. The NHP Reset reaffirmed Hinchingbrooke replacement but timeline remains uncertain, extending high operating cost.",
        "sources": [
            {"publisher": "North West Anglia NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwangliaft.nhs.uk/about-us/publications/"},
            {"publisher": "HSSIB", "title": "RAAC in the NHS — investigation report", "url": "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/"},
            {"publisher": "DHSC / NHP", "title": "New Hospital Programme update (Reset)", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"}
        ],
        "related": ["North West Anglia NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Kent and Medway NHS and Social Care Partnership Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Kent and Medway NHS and Social Care Partnership Trust"}],
        "description": "Mental-health premises operating costs across KMPT's countywide Kent estate — Priority House (Maidstone), Littlebrook Hospital (Dartford), Medway Maritime co-located MH unit (Gillingham), St Martin's Hospital (Canterbury), plus regional inpatient and community sites. Estate spend is shaped by ageing former-asylum buildings, ongoing dormitory-elimination capital programme and rolling ligature-risk upgrades.",
        "beneficiaries": "1.9M residents of Kent and Medway — adult acute MH, CAMHS, older-people's MH, learning disabilities and forensic services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.02M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "5+ MH inpatient hospitals + 50+ community clinic sites"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · forensic services · LD inpatient utilities"},
            {"label": "St Martin's Canterbury", "value": "Former Victorian asylum estate · listed-building hard-FM premium"},
            {"label": "Dormitory elimination", "value": "Capital programme to convert dorm wards to single rooms · ongoing"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Priority House and Littlebrook · LED community"},
            {"label": "YoY change", "value": "c. +5-7% (energy + ligature programme)"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH peer median per inpatient bed"}
        ],
        "notes": "KMPT's premises spend is structurally elevated by historic ex-asylum estate at St Martin's Canterbury, the ongoing national dormitory-elimination capital programme converting multi-bed wards to single rooms (with associated decant), and the ligature-risk environmental upgrade programme that has institutionalised in MH-trust estates post-2015. Co-location with Medway Maritime brings shared estate-services arrangements.",
        "sources": [
            {"publisher": "Kent and Medway NHS and Social Care Partnership Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kmpt.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Dormitory elimination capital programme", "url": "https://www.england.nhs.uk/mental-health/case-studies/dormitory-elimination/"},
            {"publisher": "CQC", "title": "KMPT inspection reports (provider RXY)", "url": "https://www.cqc.org.uk/provider/RXY"}
        ],
        "related": ["Kent and Medway NHS and Social Care Partnership Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Clatterbridge Cancer Centre NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Clatterbridge Cancer Centre NHS Foundation Trust"}],
        "description": "Specialist-cancer premises operating costs across CCC's three-site estate — the new 11-storey Clatterbridge Cancer Centre Liverpool (opened 2020 on the Royal Liverpool campus), the original Clatterbridge site at Bebington (Wirral, with proton therapy and radiotherapy), and Aintree satellite. Spend is shaped by linear-accelerator HVAC, radiotherapy bunker conditioning, and the unusual proton-therapy plant.",
        "beneficiaries": "2.4M Cheshire-and-Merseyside catchment + national proton-therapy referrals — radiotherapy, chemotherapy, brachytherapy and tertiary cancer surgery.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · IRMER 2017 (radiotherapy environmental controls)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£13.70M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "3 sites — Liverpool tower (2020) + Wirral campus + Aintree satellite"},
            {"label": "Hard FM model", "value": "In-house Estates · shared-services with Royal Liverpool on Liverpool site"},
            {"label": "Radiotherapy load", "value": "Multiple LINACs · radiotherapy bunkers drive heavy HVAC + power demand"},
            {"label": "Proton therapy", "value": "One of only 2 NHS proton-therapy centres (with UCLH) · cyclotron utilities premium"},
            {"label": "Liverpool tower", "value": "11-storey clinical tower 2020 · modern but high-spec MEP"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at Wirral site · LED rollout"},
            {"label": "YoY change", "value": "c. +5-6% (energy + radiotherapy plant maintenance)"},
            {"label": "Peer benchmark", "value": "Above specialist median per m² (radiotherapy + proton plant)"}
        ],
        "notes": "Clatterbridge is one of only two NHS proton-therapy providers (with UCLH), giving it a uniquely high specialist-equipment utility load — cyclotron cooling, beamline conditioning, and shielded-bunker HVAC all feed into Premises (other). The 2020 Liverpool tower added significant high-spec floor area on a shared campus with the Royal Liverpool, with associated shared-services cost. RM6011 energy reset is the primary 2024-25 driver.",
        "sources": [
            {"publisher": "The Clatterbridge Cancer Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.clatterbridgecc.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Proton beam therapy services specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-b/b01/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme awards", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["The Clatterbridge Cancer Centre NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Alder Hey Children's NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Alder Hey Children's NHS Foundation Trust"}],
        "description": "Specialist-children's premises operating costs at Alder Hey — the 'Alder Hey in the Park' main hospital (opened 2015 on a single Springfield Park site, replacing the historic 1914 hospital), plus the Catkin Centre / Sunflower House mental-health and community children's facility (opened 2023). The estate is among NHS England's most modern but carries specialist paediatric utility loads.",
        "beneficiaries": "330,000+ children annually — quaternary paediatric surgery, cardiology, oncology, neuroscience, plus paediatric MH at Catkin/Sunflower for north-west and national referrals.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£13.65M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Main hospital (2015) + Catkin/Sunflower MH centre (2023) + Springfield Park grounds"},
            {"label": "Hard FM model", "value": "In-house Estates · main hospital under residual life-cycle agreement"},
            {"label": "Build vintage", "value": "2015 main hospital — among newest acute estates in NHS England"},
            {"label": "Paediatric specialty", "value": "Quaternary paediatric services drive specialist HVAC, isolation and play-space requirements"},
            {"label": "Catkin/Sunflower 2023", "value": "Purpose-built children's MH and community centre · added operating footprint"},
            {"label": "Net Zero milestone", "value": "Modern build achieves BREEAM Excellent baseline · LED + BMS optimisation"},
            {"label": "YoY change", "value": "c. +5-7% (energy + Catkin/Sunflower full-year operating cost)"},
            {"label": "Peer benchmark", "value": "Below specialist median per m² (modern build) but above per inpatient (paediatric specialty)"}
        ],
        "notes": "Alder Hey's premises spend reflects an unusually modern estate by NHS standards — the 2015 main hospital was a complete site-replacement to BREEAM Excellent — but paediatric specialty drives elevated specific-area requirements (play space, parent accommodation, theatre HVAC). The 2023 opening of the Catkin Centre / Sunflower House for children's MH added a full year of operating cost in 2024-25, contributing to YoY uplift alongside RM6011 energy reset.",
        "sources": [
            {"publisher": "Alder Hey Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://alderhey.nhs.uk/about-us/publications"},
            {"publisher": "Alder Hey", "title": "Catkin and Sunflower mental-health centre", "url": "https://alderhey.nhs.uk/about-us/our-locations/catkin-and-sunflower"},
            {"publisher": "NHS England", "title": "Provider finance returns 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Alder Hey Children's NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Northamptonshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Northamptonshire Healthcare NHS Foundation Trust"}],
        "description": "Combined community + mental-health premises operating costs across NHFT's countywide Northamptonshire estate — Berrywood Hospital (Northampton, MH), St Mary's Hospital (Kettering), Isebrook Hospital, plus Corby Community Hospital, Danetre Hospital (Daventry), Nene Park and an extensive community-clinic estate. NHFT operates as one of the largest combined community + MH trusts in the East Midlands.",
        "beneficiaries": "775,000+ residents of Northamptonshire — adult acute MH, CAMHS, learning disabilities, older-people's MH plus community physical-health and community-hospital inpatients.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£13.28M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 MH inpatient hospitals + 4 community hospitals + 80+ clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts · NHSPS service-charges where landlord"},
            {"label": "MH-specific", "value": "Berrywood s.136 + PICU · Isebrook LD · CAMHS estate"},
            {"label": "Combined model", "value": "MH + community + LD service portfolio · diverse estate types"},
            {"label": "CQC Outstanding 2019", "value": "Estate-management governance recognised — premises spend reflects sustained programme"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump rollout community hospitals · LED multi-site"},
            {"label": "YoY change", "value": "c. +5-7% (NHSPS service-charge uplift + energy)"},
            {"label": "Peer benchmark", "value": "Mid-range vs combined-trust peers per site"}
        ],
        "notes": "NHFT's combined community + MH model creates a diverse estate where Premises (other) absorbs hard FM, soft FM and NHSPS service charges across two main MH hospitals, four community hospitals, and a large clinic footprint. The trust's CQC Outstanding rating (2019, 2023) is partly underpinned by a sustained estate-environment programme. NHSPS service-charge uplifts in 2024-25 are a notable cost driver alongside RM6011 energy reset.",
        "sources": [
            {"publisher": "Northamptonshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nhft.nhs.uk/about-us/publications/"},
            {"publisher": "CQC", "title": "NHFT inspection reports (provider RP1)", "url": "https://www.cqc.org.uk/provider/RP1"},
            {"publisher": "NHS Property Services", "title": "Service charges and rent guidance", "url": "https://www.property.nhs.uk/our-services/managing-property/service-charges/"}
        ],
        "related": ["Northamptonshire Healthcare NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Hillingdon Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Hillingdon Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs at THH — Hillingdon Hospital (Uxbridge, the principal acute, with confirmed RAAC and a substantial NHP-funded redevelopment under way) and Mount Vernon Hospital (Northwood, sharing campus with the Mount Vernon Cancer Centre operated by East and North Herts NHS Trust). The Hillingdon site is an active NHP build-on-occupied-site programme, generating decant and temporary-works cost.",
        "beneficiaries": "350,000+ residents of Hillingdon plus Heathrow workforce — emergency, maternity, paediatrics and acute services at Hillingdon; planned care + outpatients at Mount Vernon.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£13.27M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 sites — Hillingdon Hospital + Mount Vernon Hospital campus"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "RAAC status", "value": "Hillingdon main block confirmed RAAC (HSSIB Sep 2023) · ongoing mitigation"},
            {"label": "NHP scheme status", "value": "New Hillingdon Hospital — Phase 1 enabling on site · Reset Jan 2025 reaffirmed"},
            {"label": "Build-on-occupied-site", "value": "Phased construction generating live decant + temporary clinical works"},
            {"label": "Net Zero milestone", "value": "New build to Net Zero standard · interim PSDS works at Mount Vernon"},
            {"label": "YoY change", "value": "c. +7-9% (RAAC + new-build decant + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (RAAC + active redevelopment)"}
        ],
        "notes": "Hillingdon is among the most-active NHP construction sites in 2024-25, with new-hospital enabling works generating live decant, temporary-works and parallel-running costs that hit Premises (other). The confirmed RAAC throughout the existing main block requires ongoing structural surveillance until clinical migration to the new build. Mount Vernon's shared-campus arrangement with East and North Herts (cancer centre) brings cost-recovery complexities.",
        "sources": [
            {"publisher": "The Hillingdon Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thh.nhs.uk/about-us/publications"},
            {"publisher": "HSSIB", "title": "RAAC in the NHS — investigation report", "url": "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/"},
            {"publisher": "DHSC / NHP", "title": "New Hospital Programme update (Reset)", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"}
        ],
        "related": ["The Hillingdon Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Midlands Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Midlands Partnership NHS Foundation Trust"}],
        "description": "Combined MH + community premises operating costs across MPFT's Staffordshire and Shropshire estate — St George's Hospital (Stafford, MH inpatient), Redwoods Centre (Shrewsbury), plus Cannock Chase Hospital, County Hospital Stafford community wards, Haywood Hospital and many community sites. MPFT also operates services in Telford & Wrekin and parts of the wider Midlands, creating a dispersed footprint.",
        "beneficiaries": "1.5M residents of Staffordshire, Shropshire and beyond — adult acute MH, CAMHS, learning disabilities, secure services, plus community physical-health.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£13.22M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "5+ MH inpatient sites + 4 community hospitals + 100+ clinic sites across two counties"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts · NHSPS service-charges across community estate"},
            {"label": "MH-specific", "value": "St George's s.136 + PICU · Redwoods s.136 · LD inpatient utilities"},
            {"label": "Geographic spread", "value": "Staffordshire + Shropshire + parts of West Midlands · two-county footprint"},
            {"label": "Combined model", "value": "MH + community + LD + secure services portfolio"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at St George's and Redwoods · LED community programme"},
            {"label": "YoY change", "value": "c. +5-7% (energy + dispersed-estate uplift)"},
            {"label": "Peer benchmark", "value": "Mid-range vs combined-trust peers per site"}
        ],
        "notes": "MPFT's premises spend is shaped by an unusually dispersed two-county geography (Staffordshire + Shropshire) and a combined MH + community + LD service portfolio, generating estate-management complexity. The trust is subject to ongoing reorganisation discussions with neighbouring providers which has held back some estate-rationalisation decisions. NHSPS service-charge uplifts feed materially into this line via the community-clinic estate.",
        "sources": [
            {"publisher": "Midlands Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mpft.nhs.uk/about-us/our-publications"},
            {"publisher": "CQC", "title": "MPFT inspection reports (provider RRE)", "url": "https://www.cqc.org.uk/provider/RRE"},
            {"publisher": "NHS Property Services", "title": "Service charges and rent guidance", "url": "https://www.property.nhs.uk/our-services/managing-property/service-charges/"}
        ],
        "related": ["Midlands Partnership NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — East Midlands Ambulance Service NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "East Midlands Ambulance Service NHS Trust"}],
        "description": "Ambulance-trust premises running costs across EMAS's six-county footprint — ambulance stations across Derbyshire, Nottinghamshire, Lincolnshire, Leicestershire, Rutland and Northamptonshire, two emergency operations centres (Lincoln and Nottingham), HART base, fleet-preparation hubs and training centres. EMAS has been working through estate-rationalisation under its 'Being the Best' transformation programme.",
        "beneficiaries": "4.8M residents across the East Midlands — 999 emergency response and patient transport.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£13.14M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "60+ ambulance stations + 2 EOCs + HART base + Make-Ready hubs"},
            {"label": "Hard FM model", "value": "In-house Estates with regional sub-contracts"},
            {"label": "EOC resilience", "value": "Lincoln + Nottingham dual-EOC model · power and HVAC redundancy"},
            {"label": "Make-Ready model", "value": "Centralised vehicle prep hubs · station footprint reducing"},
            {"label": "Estate rationalisation", "value": "'Being the Best' transformation reshaping station portfolio"},
            {"label": "Net Zero milestone", "value": "EV charging rollout at hub sites · PSDS heat-pump trials"},
            {"label": "YoY change", "value": "c. +5-7% (energy + EV charging infrastructure)"},
            {"label": "Peer benchmark", "value": "Mid-range vs ambulance peers per station"}
        ],
        "notes": "EMAS's premises spend reflects a transitional estate as 'Being the Best' shifts from traditional small ambulance stations toward fewer, larger Make-Ready hubs supported by community ambulance posts. Lincolnshire's geography (the largest county by area in the EMAS footprint) drives elevated dispersion. EV charging infrastructure rollout is moving from capex to opex as fleets electrify, contributing to YoY uplift alongside RM6011 energy reset.",
        "sources": [
            {"publisher": "East Midlands Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.emas.nhs.uk/about-us/publications/"},
            {"publisher": "CQC", "title": "EMAS inspection reports (provider RX9)", "url": "https://www.cqc.org.uk/provider/RX9"},
            {"publisher": "NHS England", "title": "Ambulance services estates and fleet strategy", "url": "https://www.england.nhs.uk/ambulance-services/"}
        ],
        "related": ["East Midlands Ambulance Service NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Cambridgeshire Community Services NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Cambridgeshire Community Services NHS Trust"}],
        "description": "Community-trust premises operating costs across CCS's three-area footprint — Cambridgeshire children's, Luton children's and Peterborough/Norfolk adult community services. Estate is dominated by leased and NHSPS-owned community clinics, school-nursing bases, health-visiting bases, and 0-19 services premises rather than inpatient facilities. CCS was rated CQC Outstanding 2018 and 2023.",
        "beneficiaries": "1.5M+ residents across Cambridgeshire (children's), Luton (children's) and parts of Peterborough/Norfolk (adult community) — health visiting, school nursing, MSK, podiatry, child development.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£13.06M"},
            {"label": "Share of trust total opex", "value": "c. 8%"},
            {"label": "Estate scale", "value": "100+ community clinic and base sites · primarily leased / NHSPS"},
            {"label": "Hard FM model", "value": "Mixed in-house Estates + NHSPS service-charges + landlord arrangements"},
            {"label": "Geographic spread", "value": "Three contracts — Cambridgeshire + Luton + Peterborough/Norfolk · cross-border"},
            {"label": "Service mix", "value": "Largely outpatient/clinic-based · low inpatient utility load"},
            {"label": "CQC Outstanding", "value": "2018 and 2023 ratings · estate-environment is part of governance story"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at owned sites · LED across leased estate where landlord agrees"},
            {"label": "YoY change", "value": "c. +6-8% (NHSPS service-charge uplift + energy)"},
            {"label": "Peer benchmark", "value": "High-ratio per opex (community-clinic estate dominant)"}
        ],
        "notes": "CCS's Premises (other) line is unusual in being a comparatively high share of total opex — community trusts that don't own inpatient infrastructure carry their estate cost almost entirely in this line as clinic rents, NHSPS service charges, and small-site hard FM. NHSPS service-charge uplifts in 2024-25 (above general inflation) feed disproportionately into this line. The cross-county contract footprint adds management overhead.",
        "sources": [
            {"publisher": "Cambridgeshire Community Services NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cambscommunityservices.nhs.uk/about-us/publications"},
            {"publisher": "CQC", "title": "CCS inspection reports (provider RYV)", "url": "https://www.cqc.org.uk/provider/RYV"},
            {"publisher": "NHS Property Services", "title": "Service charges and rent guidance", "url": "https://www.property.nhs.uk/our-services/managing-property/service-charges/"}
        ],
        "related": ["Cambridgeshire Community Services NHS Trust", "Premises & Infrastructure"]
    },
}
