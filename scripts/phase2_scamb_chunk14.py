# -*- coding: utf-8 -*-
# Phase 2 SCamb — chunk 14 (17 NHS Specialist/Community/Ambulance Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — Royal Papworth Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Royal Papworth Hospital NHS Foundation Trust"}],
        "description": "Royal Papworth's £0.76M amortisation charge represents the IAS 38 systematic write-down of intangible assets at the UK's leading specialist heart and lung centre, dominated by capitalised software licences for the Epic electronic patient record (gone live as part of the eHospital programme co-deployed with Cambridge University Hospitals), cardiology imaging analysis, ECMO/ventilator integration software, and lung-transplant donor-management systems. The trust relocated to a new build on the Cambridge Biomedical Campus in 2019, which crystallised a substantial software-capitalisation profile that continues to unwind through amortisation.",
        "beneficiaries": "Serves a c. 5M East of England + supra-regional cardiothoracic catchment plus national referrals for transplant, PEA (pulmonary endarterectomy) and ECMO; c. 2,500 WTE staff at the new Cambridge Biomedical Campus building (opened 2019); c. 25,000 admissions/yr including c. 50 heart transplants and c. 50 lung transplants — among the largest UK transplant programmes.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frascati Manual research/development distinction",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.76M"},
            {"label": "Specialty footprint", "value": "UK's leading specialist heart & lung centre — single new-build site on Cambridge Biomedical Campus (relocated from Papworth Everard 2019)"},
            {"label": "Annual activity", "value": "c. 25,000 admissions/yr; c. 50 heart transplants + c. 50 lung transplants/yr (among UK's largest); national PEA service for chronic thromboembolic pulmonary hypertension"},
            {"label": "Workforce", "value": "c. 2,500 WTE; tertiary cardiothoracic surgeons, transplant teams, ECMO specialists, perfusionists"},
            {"label": "Intangibles class", "value": "Predominantly Epic EPR licences (eHospital programme with CUH) + cardiology imaging analysis + transplant donor-management software + capitalised software development"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; Epic EPR straight-line over service life"},
            {"label": "eHospital partnership", "value": "Epic EPR co-deployed with Cambridge University Hospitals NHS Foundation Trust under shared eHospital programme"},
            {"label": "Funding trajectory", "value": "Stable; legacy 2019 new-build software stack continues to unwind; Cambridge Children's Hospital (planned 2026 opening with CUH and CPFT) may bring further capitalisation"},
            {"label": "Delivery body", "value": "Papworth Digital + Estates teams + Epic Systems (EPR vendor) + CUH eHospital shared service"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (cardiothoracic surgery · transplantation · ECMO · PEA) + DHSC + Cambridgeshire & Peterborough ICB"},
            {"label": "Evaluation evidence", "value": "Papworth ARA; CQC inspection (RGM — Outstanding); NHSBT transplant activity report; NHSE Specialised Commissioning service spec"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2019 relocation from Papworth Everard legacy site · Successor: ongoing eHospital roadmap with CUH + Cambridge Children's Hospital co-location"}
        ],
        "notes": "Royal Papworth is one of NHS England's most internationally-known specialist trusts, operating the UK's largest transplant programme by combined heart+lung volume and the only national PEA (pulmonary endarterectomy) service for chronic thromboembolic pulmonary hypertension. The 2019 relocation to Cambridge Biomedical Campus produced a step-up in capitalised software (Epic EPR via the eHospital partnership with CUH, transplant systems, cardiology imaging) which unwinds via this line. The amortisation charge is modest in absolute terms because Papworth is a single-site trust, but the digital intensity of transplant and ECMO care keeps the intangible base material. Cambridge Children's Hospital (jointly with CUH and Cambridgeshire & Peterborough NHS FT, planned 2026) may add further intangible capitalisation.",
        "sources": [
            {"publisher": "Royal Papworth Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://royalpapworth.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "Royal Papworth Hospital provider profile (RGM)", "url": "https://www.cqc.org.uk/provider/RGM"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 5 Property Plant Equipment & Intangibles", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Blood and Transplant", "title": "Annual Report on Cardiothoracic Organ Transplantation", "url": "https://www.odt.nhs.uk/statistics-and-reports/annual-activity-report/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — cardiothoracic services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Cambridge University Hospitals NHS FT", "title": "eHospital programme — Epic EPR shared deployment", "url": "https://www.cuh.nhs.uk/about-us/who-we-are/ehospital/"}
        ],
        "related": ["Royal Papworth Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Amortisation — The Royal Marsden NHS Foundation Trust", "Amortisation — Liverpool Heart and Chest Hospital NHS Foundation Trust", "NHS England"]
    },
    "Lease expenditure — Leeds Community Healthcare NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Leeds Community Healthcare NHS Trust"}],
        "description": "Leeds Community Healthcare's £0.75M lease expenditure represents the IFRS 16 short-term and low-value lease charges (and any residual operating lease costs not capitalised as right-of-use assets) on the trust's portfolio of community-care premises across Leeds. The trust operates community nursing, neighbourhood teams, children's and family services, dental services and community in-patient beds from health centres, family hubs and clinic sites, predominantly held under occupational leases from NHS Property Services (NHSPS), Community Health Partnerships (CHP — LIFT estate), local authority partners and a small number of commercial landlords.",
        "beneficiaries": "Serves the c. 820,000 Leeds population (LS1-LS29 postcodes); operates from c. 80+ community sites including health centres, family hubs, dental clinics and community in-patient units (e.g. Wharfedale Hospital partnership with LTHT); c. 3,200 WTE incl. district nurses, health visitors, neighbourhood teams, school nurses and AHPs.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 (Part II security of tenure) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.75M"},
            {"label": "Estate footprint", "value": "c. 80+ community sites across Leeds; mix of NHSPS-leased health centres, CHP/LIFT clinics, family hubs, school-nursing bases"},
            {"label": "Population served", "value": "c. 820,000 Leeds residents — England's third-largest single-tier authority by population"},
            {"label": "Workforce", "value": "c. 3,200 WTE — district nurses, health visitors, neighbourhood teams, school nurses, AHPs, community paediatrics"},
            {"label": "Lease line scope", "value": "IFRS 16 short-term (<12mo) + low-value (<£5k pa) leases not capitalised as ROU; service charges; residual op-lease tail"},
            {"label": "Principal landlords", "value": "NHS Property Services (NHSPS) + Community Health Partnerships (CHP — LIFT) + Leeds City Council + commercial landlords for clinic space"},
            {"label": "IFRS 16 effect", "value": "Most material multi-year leases recognised as right-of-use assets on balance sheet from FY22; this line captures the residual P&L charge"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr from NHSPS service-charge uprating + CHP rent reviews; Three Shifts community-care policy may grow estate footprint"},
            {"label": "Delivery body", "value": "LCH Estates & Facilities + NHSPS (managing agent for NHS-owned community estate) + CHP for LIFT sites"},
            {"label": "Policy owner", "value": "DHSC + NHSE Estates & Capital + West Yorkshire ICB (host commissioner) + NHSPS"},
            {"label": "Evaluation evidence", "value": "LCH ARA; CQC provider profile (RY2); NHSE Estates Returns Information Collection (ERIC); ICB community estates strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 op-lease accounting (pre-FY22) · Successor: estate consolidation under Three Shifts community-care lift + Leeds Health & Care Plan estate strategy"}
        ],
        "notes": "Community trusts have a fundamentally different premises mix from acute trusts: they rarely own large hospital buildings, instead occupying NHS Property Services and Community Health Partnerships (LIFT) clinics, plus family hubs and council-owned sites. The bulk of multi-year occupational leases sit on the balance sheet as IFRS 16 right-of-use assets from FY22, so the £0.75M residual P&L charge captures short-term, low-value, variable and service-charge components. Drivers include NHSPS service-charge inflation (a long-running tension between trusts and NHSPS), the Three Shifts policy direction towards out-of-hospital care growing the community footprint, and the Leeds Health & Care Plan estates strategy.",
        "sources": [
            {"publisher": "Leeds Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedscommunityhealthcare.nhs.uk/about-us/corporate-information/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Leeds Community Healthcare NHS Trust provider profile (RY2)", "url": "https://www.cqc.org.uk/provider/RY2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual report and financial statements", "url": "https://www.property.nhs.uk/insights-events/annual-reviews/"},
            {"publisher": "Community Health Partnerships", "title": "About LIFT estate", "url": "https://communityhealthpartnerships.co.uk/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Leeds Community Healthcare NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Northamptonshire Healthcare NHS Foundation Trust", "Lease expenditure — Central London Community Healthcare NHS Trust", "NHS Property Services"]
    },
    "Transport (business + patient) — Royal Papworth Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Royal Papworth Hospital NHS Foundation Trust"}],
        "description": "Royal Papworth's £0.75M transport line covers business-mileage reimbursement (HMRC AMAP) for clinical and support staff, leased pool-cars under IFRS 16, transplant retrieval transport (donor heart and lung organs flown or driven from procurement hospitals across the UK and occasionally Europe), patient-transport services for outpatient clinics under NHSE PTS Eligibility, and specialist couriers shifting blood, ECMO consumables and pathology samples between Papworth and partner hospitals on the Cambridge Biomedical Campus and across the East of England referral network.",
        "beneficiaries": "Serves a c. 5M East of England + supra-regional cardiothoracic catchment plus national transplant, PEA and ECMO referrals; c. 2,500 WTE; c. 25,000 admissions/yr including c. 50 heart transplants and c. 50 lung transplants requiring nationwide donor-organ retrieval logistics by NHS Blood and Transplant teams.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Healthcare Travel Costs Scheme (HTCS) · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · Human Tissue Act 2004 (organ transport)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.75M"},
            {"label": "Specialty footprint", "value": "UK's leading specialist heart & lung centre — single new-build site on Cambridge Biomedical Campus (relocated 2019)"},
            {"label": "Annual activity", "value": "c. 25,000 admissions/yr; c. 50 heart + c. 50 lung transplants/yr; national PEA service; UK's largest combined heart-and-lung transplant programme"},
            {"label": "Workforce", "value": "c. 2,500 WTE; tertiary cardiothoracic surgeons, transplant teams, ECMO retrieval team, perfusionists"},
            {"label": "Transplant retrieval driver", "value": "NHSBT National Organ Retrieval Service (NORS) flies donor hearts/lungs to Papworth from procurement hospitals UK-wide; aircraft-charter and specialist couriers"},
            {"label": "ECMO retrieval", "value": "Adult Severe Respiratory Failure (SRF) ECMO commissioned service — Papworth retrieval team mobilises by ambulance/helicopter to refer hospitals across East of England"},
            {"label": "PTS driver", "value": "Outpatient cardiac/respiratory clinics for c. 5M referral catchment; HTCS reimbursement for patients meeting eligibility criteria"},
            {"label": "Funding trajectory", "value": "Stable to slightly rising; IFRS 16 2022 lease re-recognition + AMAP mileage growth + transplant volume; charter-flight cost volatility"},
            {"label": "Delivery body", "value": "Papworth Estates & Facilities + NHSBT NORS for organ retrieval + commercial leasing for pool fleet + air-charter providers (Babcock/2Excel)"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (cardiothoracic transplant · ECMO · PEA) + NHSBT + DHSC + Cambridgeshire & Peterborough ICB"},
            {"label": "Evaluation evidence", "value": "Papworth ARA; CQC inspection (RGM — Outstanding); NHSBT NORS performance reports; NHSE adult SRF ECMO service spec"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 op-lease accounting · Successor: zero-emission pool fleet under NHSE Net Zero 2032 + ongoing transplant volume growth"}
        ],
        "notes": "Papworth's transport line is small in absolute terms because the trust is single-site on the Cambridge Biomedical Campus, but it has unusually concentrated drivers around organ-retrieval logistics. The NHSBT National Organ Retrieval Service flies donor hearts and lungs from procurement hospitals UK-wide and Papworth runs the East of England adult ECMO retrieval service, both of which depend on rapid-response transport (charter aircraft and emergency ambulance transfers). IFRS 16 2022 lease re-recognition reshaped the line by capitalising multi-year pool-fleet leases as right-of-use assets. NHSE Net Zero 2032 fleet electrification is being phased into pool-car renewals; transplant-retrieval aircraft remain charter-based pending sustainable aviation fuel.",
        "sources": [
            {"publisher": "Royal Papworth Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://royalpapworth.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "NHS Blood and Transplant", "title": "National Organ Retrieval Service (NORS)", "url": "https://www.odt.nhs.uk/retrieval/"},
            {"publisher": "NHS England", "title": "Adult Severe Respiratory Failure ECMO service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Care Quality Commission", "title": "Royal Papworth Hospital provider profile (RGM)", "url": "https://www.cqc.org.uk/provider/RGM"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Healthcare Travel Costs Scheme (HTCS)", "url": "https://www.nhs.uk/nhs-services/help-with-health-costs/healthcare-travel-costs-scheme-htcs/"}
        ],
        "related": ["Royal Papworth Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — The Royal Marsden NHS Foundation Trust", "Transport (business + patient) — Liverpool Heart and Chest Hospital NHS Foundation Trust", "NHS Blood and Transplant"]
    },
    "Transport (business + patient) — Alder Hey Children's NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Alder Hey Children's NHS Foundation Trust"}],
        "description": "Alder Hey's £0.75M transport line covers business-mileage reimbursement (HMRC AMAP) for clinical and support staff, leased pool-cars under IFRS 16, the North West and North Wales Paediatric Transport (NWTS) retrieval service operated jointly with Manchester (which moves critically-ill children from district general hospitals to PICU), patient-transport reimbursements under NHSE PTS Eligibility for outpatient clinics, and specialist couriers shifting paediatric pathology, blood and pharmacy items between Alder Hey's main West Derby site, the East Prescot Road outreach and partner DGHs.",
        "beneficiaries": "Serves a c. 7M paediatric supra-regional catchment across Merseyside, Cheshire, Lancashire, parts of North Wales (Welsh-government-commissioned tertiary services) and the Isle of Man; c. 270,000 patient attendances/yr; c. 4,000 WTE; c. 200 PICU beds nationally with NWTS moving c. 1,000 critically-ill children/yr.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Healthcare Travel Costs Scheme (HTCS) · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.75M"},
            {"label": "Specialty footprint", "value": "Tertiary children's hospital — main West Derby (Alder Hey in the Park, opened 2015) + East Prescot Road outpatients/community + 2 satellite/outreach hubs"},
            {"label": "Supra-regional catchment", "value": "c. 7M paediatric population across Merseyside, Cheshire, Lancashire, North Wales (cross-border tertiary), Isle of Man; one of England's six paediatric tertiary centres"},
            {"label": "Annual activity", "value": "c. 270,000 patient attendances/yr; c. 35,000 inpatient admissions; c. 60,000 ED attendances; c. 25,000 surgical procedures"},
            {"label": "Workforce", "value": "c. 4,000 WTE; c. 360 medical staff incl. tertiary paediatric surgeons, neurosurgeons, oncologists"},
            {"label": "NWTS retrieval", "value": "North West & North Wales Paediatric Transport service (joint with Manchester Royal Infirmary) — c. 1,000 critically-ill child transfers/yr to PICU"},
            {"label": "PTS driver", "value": "Outpatient clinics across NW + N Wales drive HTCS reimbursement; long-distance referrals from rural Cumbria + N Wales"},
            {"label": "Funding trajectory", "value": "Rising due to increased PICU volumes post-pandemic + IFRS 16 2022 lease re-recognition + AMAP mileage growth + Net Zero fleet replacement"},
            {"label": "Delivery body", "value": "Alder Hey Estates & Facilities + NWTS partnership with Manchester + leased-fleet supplier (NHS Fleet Solutions / commercial) + specialist paediatric couriers"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (paediatric tertiary services) + Welsh Government (cross-border paediatrics) + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Alder Hey ARA; CQC inspection (RBS); NWTS service review; NHSE paediatric PICU service specification reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 Eaton Road hospital + pre-IFRS-16 op-lease · Successor: zero-emission pool fleet under NHSE Net Zero 2032 + Alder Hey Plus campus expansion"}
        ],
        "notes": "Alder Hey is one of England's six paediatric tertiary centres and runs the North West & North Wales Paediatric Transport (NWTS) service jointly with Manchester Children's, moving c. 1,000 critically-ill children/yr from DGH-level care to PICU at either Alder Hey or Royal Manchester Children's. The transport line is modest in absolute terms because the trust is concentrated on the West Derby campus (Alder Hey in the Park, opened 2015) but the NWTS retrieval, AMAP business mileage for staff working across Cheshire/Lancashire/N Wales, and outpatient PTS reimbursement are the main drivers. IFRS 16 2022 lease re-recognition reshaped the accounting; Net Zero 2032 fleet electrification is being phased into pool-car renewals.",
        "sources": [
            {"publisher": "Alder Hey Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://alderhey.nhs.uk/about/annual-reports"},
            {"publisher": "NWTS — North West & North Wales Paediatric Transport Service", "title": "Service overview", "url": "https://www.nwts.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Alder Hey Children's NHS Foundation Trust provider profile (RBS)", "url": "https://www.cqc.org.uk/provider/RBS"},
            {"publisher": "NHS England", "title": "Specialised commissioning — paediatric services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Healthcare Travel Costs Scheme (HTCS)", "url": "https://www.nhs.uk/nhs-services/help-with-health-costs/healthcare-travel-costs-scheme-htcs/"}
        ],
        "related": ["Alder Hey Children's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — Great Ormond Street Hospital for Children NHS Foundation Trust", "Transport (business + patient) — Sheffield Children's NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — North West Ambulance Service NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "North West Ambulance Service NHS Trust"}],
        "description": "NWAS's £0.73M amortisation charge represents the IAS 38 systematic write-down of intangible assets at the regional ambulance service for England's North West, dominated by capitalised software licences and developments — Computer-Aided Dispatch (CAD), Electronic Patient Care Record (EPCR), the Manchester Triage / NHS Pathways clinical decision support, fleet-management software, and 999/111 call-handling platforms (CleriCall / Salesforce). NWAS is one of England's 10 regional ambulance services, covering c. 7M residents across Cumbria, Lancashire, Greater Manchester, Merseyside and Cheshire from c. 110 ambulance stations.",
        "beneficiaries": "Serves a c. 7M North West population across Cumbria + Lancashire + Greater Manchester + Merseyside + Cheshire; c. 6,500 WTE incl. paramedics, EMTs, ECAs, call handlers and dispatchers; responds to c. 1.5M 999 incidents/yr + handles c. 3M NHS 111 calls/yr (NWAS holds the NW NHS 111 contract).",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frascati Manual research/development distinction",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.73M"},
            {"label": "Service footprint", "value": "10 regional ambulance services in England — NWAS covers c. 7M North West residents across c. 14,000 sq km from c. 110 stations"},
            {"label": "Annual activity", "value": "c. 1.5M 999 incidents/yr; c. 3M NHS 111 calls/yr (NWAS holds NW NHS 111 contract); c. 1.4M patient transports including PTS"},
            {"label": "Workforce", "value": "c. 6,500 WTE — paramedics, EMTs, emergency care assistants, call handlers, dispatchers, fleet engineers, leadership"},
            {"label": "Intangibles class", "value": "CAD (Computer-Aided Dispatch) + EPCR (Electronic Patient Care Record) + NHS Pathways + Manchester Triage + 999/111 telephony platforms + fleet-management systems"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; clinical decision support straight-line over service life"},
            {"label": "Cat-1 8-min standard", "value": "NHSE response standard — Cat-1 mean 7 min, 90th centile 15 min; CAD + EPCR drive performance reporting"},
            {"label": "Funding trajectory", "value": "Stable around £0.7-1M; rising as digital paramedic kits + EPCR upgrades + 999/111 platform refreshes capitalise"},
            {"label": "Delivery body", "value": "NWAS Digital + IT teams + CAD vendor (Cleric Computer Services) + EPCR vendor + NHS Pathways via NHSE"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent & Emergency Care + DHSC + 6 NW ICBs (lead: Greater Manchester)"},
            {"label": "Evaluation evidence", "value": "NWAS ARA; CQC inspection; NHSE Ambulance Quality Indicators (AQIs) monthly; ORH benchmarks; NHSE 111/999 contract review"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy CAD + paper PRF era · Successor: ongoing EPCR roll-out + digital paramedic kit refresh + ambulance fleet electrification under Net Zero 2032"}
        ],
        "notes": "Ambulance services are unusually digital-intensive operations — every 999 call generates a CAD record, every patient encounter generates an EPCR, and the Cat-1 8-minute response standard depends on the Computer-Aided Dispatch software capitalised under IAS 38. NWAS's c. £0.73M amortisation captures the unwind of past software investments including CAD, EPCR, NHS Pathways/Manchester Triage and the 999/111 telephony platforms. Industrial action 2023-24 (paramedics struck under GMB and Unison) drove operational disruption but didn't directly impact amortisation. Forward drivers include the EPCR refresh, digital paramedic kit upgrades and Net Zero 2032 fleet telemetry.",
        "sources": [
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "North West Ambulance Service NHS Trust provider profile (RX7)", "url": "https://www.cqc.org.uk/provider/RX7"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 5 Property Plant Equipment & Intangibles", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "NHS England", "title": "NHS Pathways clinical decision support", "url": "https://digital.nhs.uk/services/nhs-pathways"},
            {"publisher": "NHS England", "title": "Net zero NHS — ambulance fleet decarbonisation", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["North West Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Amortisation — London Ambulance Service NHS Trust", "Amortisation — Yorkshire Ambulance Service NHS Trust", "NHS England"]
    },
    "Amortisation — Solent NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Solent NHS Trust"}],
        "description": "Solent NHS Trust's £0.73M amortisation charge represents the IAS 38 systematic write-down of intangible assets at the community provider for Portsmouth, Southampton and parts of South East Hampshire, predominantly capitalised software licences for the SystmOne (TPP) electronic patient record used across community-nursing, MSK and dental services, plus health-visiting and school-nursing platforms, sexual health (SHL) and prison healthcare IT, and corporate-systems software development.",
        "beneficiaries": "Serves a c. 750,000 Portsmouth + Southampton + SE Hampshire population across community nursing, MSK, dental, sexual health, prison healthcare, mental health (CAMHS) and dental services; c. 3,500 WTE incl. district nurses, health visitors, school nurses, AHPs, dental staff and prison healthcare team.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frascati Manual research/development distinction",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.73M"},
            {"label": "Service footprint", "value": "Community trust covering Portsmouth, Southampton, SE Hampshire — community nursing, MSK, dental, sexual health, prison healthcare, CAMHS"},
            {"label": "Population served", "value": "c. 750,000 across the Portsmouth + Southampton city footprint and SE Hampshire (Havant, Fareham, Gosport)"},
            {"label": "Workforce", "value": "c. 3,500 WTE — district nurses, health visitors, school nurses, AHPs, MSK community physio, dental, prison healthcare team"},
            {"label": "Intangibles class", "value": "Predominantly SystmOne (TPP) EPR licences + sexual-health platform + prison healthcare IT + capitalised software development"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; clinical-system EPR straight-line over service life"},
            {"label": "Distinctive services", "value": "HMP Winchester + IRC Haslar + Isle of Wight prison healthcare contracts; SHL sexual health service brand"},
            {"label": "Funding trajectory", "value": "Stable around £0.7-1M/yr; expected to rise modestly as Three Shifts policy drives community digital investment"},
            {"label": "Delivery body", "value": "Solent Digital + IT teams + EPR vendor (TPP SystmOne) + sexual-health platform vendors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Hampshire & Isle of Wight ICB (host commissioner) + HMPPS for prison healthcare contracts"},
            {"label": "Evaluation evidence", "value": "Solent ARA; CQC provider profile (R1C); NHSE Operational Plan returns; HMIP prison healthcare inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era community + sexual-health systems · Successor: digital-first community-care under Three Shifts policy + EPR refresh"}
        ],
        "notes": "Solent is one of England's larger community trusts and has a distinctive service mix including SHL (sexual health on the south coast — a major brand-led service line) and prison healthcare contracts at HMP Winchester, IRC Haslar and Isle of Wight prisons. The £0.73M amortisation captures the unwind of capitalised software (predominantly SystmOne EPR plus sexual-health and prison healthcare platforms). The Three Shifts policy direction towards out-of-hospital care is expected to grow community digital investment, driving forward-looking software capitalisation. Useful-economic-life judgements typically run 3-7 years for software per DHSC GAM ch.5.",
        "sources": [
            {"publisher": "Solent NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.solent.nhs.uk/about-us/who-we-are/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Solent NHS Trust provider profile (R1C)", "url": "https://www.cqc.org.uk/provider/R1C"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 5 Property Plant Equipment & Intangibles", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "TPP", "title": "SystmOne community module", "url": "https://tpp-uk.com/products/systmone/"},
            {"publisher": "NHS England", "title": "Three Shifts and the Darzi review of NHS performance", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "HM Inspectorate of Prisons", "title": "Prison healthcare inspections", "url": "https://www.justiceinspectorates.gov.uk/hmiprisons/"}
        ],
        "related": ["Solent NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Sussex Community NHS Foundation Trust", "Amortisation — Central London Community Healthcare NHS Trust", "Three Shifts (Darzi 2024)"]
    },
    "General supplies & services — Shropshire Community Health NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Shropshire Community Health NHS Trust"}],
        "description": "Shropshire Community's £0.72M general supplies & services line covers non-drug clinical and consumable purchasing across the trust's c. 60+ community sites in Shropshire, Telford & Wrekin — including district-nursing dressings and wound-care consumables, MSK community-physio supplies, school-nursing immunisation kit, continence products, oxygen and home-nebuliser consumables, and minor IPC PPE. Most procurement flows through NHS Supply Chain commodity routes (catalogues 02 Wound Care, 04 Continence) supplemented by direct local contracts for specialist community-care items.",
        "beneficiaries": "Serves a c. 500,000 Shropshire + Telford & Wrekin population (one of England's most rural footprints with the Welsh border); operates from c. 60+ sites including community hospitals at Bridgnorth, Ludlow, Whitchurch and Bishop's Castle plus health centres and clinic bases; c. 1,800 WTE incl. district nurses, school nurses, health visitors, MSK community physio.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories (interaction) · Public Contracts Regulations 2015 (now Procurement Act 2023) · NHS Supply Chain framework agreements · NHS Act 2006",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£0.72M"},
            {"label": "Estate footprint", "value": "c. 60+ community sites including community hospitals at Bridgnorth, Ludlow, Whitchurch, Bishop's Castle + clinics + school-nursing bases"},
            {"label": "Population served", "value": "c. 500,000 Shropshire + Telford & Wrekin residents — one of England's most rural footprints with substantial Welsh-border patient flows"},
            {"label": "Workforce", "value": "c. 1,800 WTE — district nurses, school nurses, health visitors, AHPs, MSK community physio, community in-patient teams"},
            {"label": "Cost mix", "value": "Wound-care + continence + minor IPC PPE + school-nursing immunisation kit + oxygen + nebuliser consumables + community-hospital consumables"},
            {"label": "Procurement route", "value": "NHS Supply Chain commodity catalogues (02 Wound Care, 04 Continence, 16 Infection Control) + direct local for specialist community items"},
            {"label": "Wound care driver", "value": "Ageing population in rural Shropshire drives complex/chronic wound caseload (Hartmann, Mölnlycke, Smith & Nephew, Coloplast brands)"},
            {"label": "Funding trajectory", "value": "Slowly rising c. 3-5%/yr from clinical-supplies inflation + caseload complexity; offset partially by central NHS Supply Chain leverage"},
            {"label": "Delivery body", "value": "ShropCom Procurement + NHS Supply Chain + community-hospital site teams + local specialist suppliers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Commercial + NHS Supply Chain + Shropshire, Telford & Wrekin ICB"},
            {"label": "Evaluation evidence", "value": "ShropCom ARA; CQC provider profile (RY7); Model Hospital community-supplies benchmark; NHSE Operational Plan returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era community supplies + pre-Supply Chain transformation · Successor: NHS Supply Chain category-tower model + Three Shifts community digital procurement"}
        ],
        "notes": "Community-trust general supplies & services is dominated by wound-care and continence consumables (the bulk of the district-nursing patient encounter) plus IPC PPE and school-nursing immunisation kit. Shropshire Community's £0.72M is modest by community-trust standards because the trust has a smaller workforce than larger community providers (Birmingham, Central London CH) but the rural geography drives some inefficiency in last-mile distribution to community-hospital sites at Bridgnorth, Ludlow, Whitchurch and Bishop's Castle. NHS Supply Chain category-tower model handles the bulk of commodity routes; specialist wound-care (Hartmann, Mölnlycke, Smith & Nephew, Coloplast) is a key cost driver as ageing population complexity grows.",
        "sources": [
            {"publisher": "Shropshire Community Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.shropscommunityhealth.nhs.uk/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "Shropshire Community Health NHS Trust provider profile (RY7)", "url": "https://www.cqc.org.uk/provider/RY7"},
            {"publisher": "NHS Supply Chain", "title": "Category towers — wound care + continence", "url": "https://www.supplychain.nhs.uk/category-tower/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital — community trust benchmarks", "url": "https://model.nhs.uk/"},
            {"publisher": "UK Government", "title": "Procurement Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/54"}
        ],
        "related": ["Shropshire Community Health NHS Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "General supplies & services — Norfolk Community Health and Care NHS Trust", "General supplies & services — Lincolnshire Community Health Services NHS Trust", "NHS Supply Chain"]
    },
    "Drugs costs — Wirral Community Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Wirral Community Health and Care NHS Foundation Trust"}],
        "description": "WCHC's £0.72M drugs costs line covers community-administered medicines purchased by the trust under the Drug Tariff and Branded Medicines Pricing Scheme — predominantly community-nurse administered injectables (anticoagulants, antibiotics, palliative-care medication for end-of-life patients), school-nursing immunisations (HPV, MenACWY, dTaP/IPV), CAMHS prescribing, sexual-health services (PEP, contraceptive injectables, ECP), and stock medicines for community in-patient beds and walk-in centres. Most non-FP10 community drug spend flows through this line.",
        "beneficiaries": "Serves the c. 320,000 Wirral peninsula population; operates community nursing, district nursing, MSK, CAMHS, sexual health, school-nursing immunisation programme covering all Wirral school-age children, and community in-patient beds at St Catherine's; c. 1,400 WTE incl. district nurses, health visitors, school nurses, AHPs and CAMHS staff.",
        "legal_basis": "NHS Act 2006 (Drug Tariff Part VIII) · Branded Medicines Pricing Scheme (statutory replaced by VPAG voluntary scheme 2024) · Human Medicines Regulations 2012 · MHRA · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.72M"},
            {"label": "Service footprint", "value": "Community trust covering Wirral peninsula — district nursing, MSK, CAMHS, sexual health, school nursing, community in-patient at St Catherine's"},
            {"label": "Population served", "value": "c. 320,000 Wirral residents (Birkenhead, Wallasey, West Kirby, Heswall and surrounds)"},
            {"label": "Workforce", "value": "c. 1,400 WTE — district nurses, health visitors, school nurses, AHPs, CAMHS staff, sexual-health team"},
            {"label": "Cost mix", "value": "Community-nurse injectables (LMWH, IV antibiotics, palliative anticipatory meds) + school immunisation programme + CAMHS prescribing + sexual-health (PEP, contraceptives) + stock for community beds"},
            {"label": "School immunisations", "value": "HPV (Years 8-9), MenACWY (Year 9), Td/IPV (Year 9), seasonal flu (children) — high-volume vaccine spend at vaccination season peaks"},
            {"label": "Palliative care driver", "value": "End-of-life community care — anticipatory drugs (morphine, midazolam, glycopyrronium, hyoscine) for dying patients in own homes"},
            {"label": "Funding trajectory", "value": "Modest growth c. 3-5%/yr; vaccine programme volumes drive year-on-year fluctuation; Branded scheme transition (statutory→VPAG voluntary) from 2024"},
            {"label": "Delivery body", "value": "WCHC Pharmacy + Procurement + NHS Supply Chain + UKHSA (vaccines for school programme) + community-pharmacy partnerships"},
            {"label": "Policy owner", "value": "DHSC + NHSE Commercial Medicines + UKHSA (immunisation programme) + Cheshire & Merseyside ICB + NICE"},
            {"label": "Evaluation evidence", "value": "WCHC ARA; CQC provider profile (RYG); UKHSA immunisation coverage data; NHSE Operational Plan returns; ICB commissioning review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era community medicines + pre-VPAG statutory pricing · Successor: VPAG voluntary scheme + ongoing Three Shifts community-care direction"}
        ],
        "notes": "Community drugs costs sit between very-small primary-care FP10 prescribing (which doesn't appear on community trust accounts) and large hospital pharmacy spend — the community trust line captures medicines administered or stocked by the trust rather than dispensed by community pharmacy. WCHC's £0.72M is dominated by community-nurse injectables (palliative-care anticipatory drugs, LMWH for VTE, IV antibiotics under OPAT pathways), the school-immunisation programme (HPV, MenACWY, dTaP/IPV — funded through UKHSA), and sexual-health services. The transition from the statutory Branded Medicines Pricing Scheme to the 2024 VPAG voluntary scheme is the key recent policy driver.",
        "sources": [
            {"publisher": "Wirral Community Health and Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wchc.nhs.uk/about-us/corporate-information/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Wirral Community Health and Care NHS FT provider profile (RYG)", "url": "https://www.cqc.org.uk/provider/RYG"},
            {"publisher": "Department of Health and Social Care", "title": "Voluntary Scheme for Branded Medicines Pricing, Access and Growth (VPAG) 2024", "url": "https://www.gov.uk/government/publications/the-2024-voluntary-scheme-for-branded-medicines-pricing-access-and-growth"},
            {"publisher": "UK Health Security Agency", "title": "Immunisation programme — schools-based delivery", "url": "https://www.gov.uk/government/collections/immunisation"},
            {"publisher": "NHS England", "title": "Drug Tariff", "url": "https://www.nhsbsa.nhs.uk/pharmacies-gp-practices-and-appliance-contractors/drug-tariff"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Wirral Community Health and Care NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "Drugs costs — Leeds Community Healthcare NHS Trust", "Drugs costs — Norfolk Community Health and Care NHS Trust", "UK Health Security Agency"]
    },
    "Lease expenditure — Northamptonshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Northamptonshire Healthcare NHS Foundation Trust"}],
        "description": "NHFT's £0.71M lease expenditure represents the IFRS 16 short-term and low-value lease charges (and any residual operating lease costs not capitalised as right-of-use assets) on the trust's portfolio of community-care and mental-health premises across Northamptonshire. NHFT is unusual in being an integrated mental-health and community-services provider, occupying a mix of NHSPS-leased community sites, mental-health in-patient units (e.g. Berrywood Hospital + St Mary's), CAMHS Tier 4, dental clinics, and child & family hubs across Northampton, Kettering, Corby, Wellingborough and Daventry.",
        "beneficiaries": "Serves the c. 770,000 Northamptonshire population (West Northants + North Northants unitaries from 2021); operates from c. 80+ sites including mental-health in-patient at Berrywood, community hospitals, CAMHS Tier 4 (Sky House), dental, school nursing, district nursing; c. 4,500 WTE incl. mental-health nurses, district nurses, health visitors, AHPs.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.71M"},
            {"label": "Estate footprint", "value": "c. 80+ sites — mental-health in-patient (Berrywood Hospital, St Mary's), community hospitals, CAMHS Tier 4 (Sky House), dental clinics, child/family hubs"},
            {"label": "Population served", "value": "c. 770,000 Northamptonshire residents (West Northants + North Northants unitaries from April 2021)"},
            {"label": "Workforce", "value": "c. 4,500 WTE — mental-health nurses, district nurses, health visitors, AHPs, CAMHS, dental, IAPT/Talking Therapies"},
            {"label": "Lease line scope", "value": "IFRS 16 short-term (<12mo) + low-value (<£5k pa) leases not capitalised as ROU; service charges; residual op-lease tail"},
            {"label": "Principal landlords", "value": "NHS Property Services + Community Health Partnerships (CHP/LIFT) + West Northants Council + North Northants Council + commercial landlords"},
            {"label": "Integrated provider", "value": "NHFT is unusual in combining mental-health + community + dental services — c. 60% mental-health and c. 40% community split by income"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr from NHSPS service-charge uprating + CHP rent reviews + April 2025 NIC step-up flowing through service charges"},
            {"label": "Delivery body", "value": "NHFT Estates & Facilities + NHSPS + CHP for LIFT sites + commercial landlords"},
            {"label": "Policy owner", "value": "DHSC + NHSE Estates & Capital + Northamptonshire ICB + NHSPS + Northants unitaries"},
            {"label": "Evaluation evidence", "value": "NHFT ARA; CQC provider profile (RP1); NHSE Estates Returns Information Collection (ERIC); ICB community + MH estates strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 op-lease accounting · Successor: ongoing estate consolidation under Three Shifts community-care lift + Mental Health 10-year plan + new Northants ICB strategy"}
        ],
        "notes": "Northamptonshire Healthcare is an integrated mental-health and community-services trust — the combination is increasingly common (Sussex Partnership, Hertfordshire Partnership-Community, etc.) and gives the trust a more balanced estate mix than pure community providers. Most multi-year occupational leases sit on the balance sheet as IFRS 16 right-of-use assets from FY22, leaving the £0.71M residual P&L charge for short-term, low-value, variable and service-charge components. NHSPS service-charge inflation, CHP rent reviews and the Mental Health 10-year plan + Three Shifts policy direction all push the line upwards. The 2021 Northants unitary reorganisation (split into West and North Northants) didn't directly affect trust estate but influences ICB strategic planning.",
        "sources": [
            {"publisher": "Northamptonshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nhft.nhs.uk/about-us/our-publications"},
            {"publisher": "Care Quality Commission", "title": "Northamptonshire Healthcare NHS FT provider profile (RP1)", "url": "https://www.cqc.org.uk/provider/RP1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual report and financial statements", "url": "https://www.property.nhs.uk/insights-events/annual-reviews/"},
            {"publisher": "Community Health Partnerships", "title": "About LIFT estate", "url": "https://communityhealthpartnerships.co.uk/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Northamptonshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Leeds Community Healthcare NHS Trust", "Lease expenditure — Central London Community Healthcare NHS Trust", "NHS Property Services"]
    },
    "Lease expenditure — North West Ambulance Service NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "North West Ambulance Service NHS Trust"}],
        "description": "NWAS's £0.70M lease expenditure represents IFRS 16 short-term and low-value lease charges (and residual operating lease costs not capitalised as right-of-use assets) on the trust's portfolio of c. 110 ambulance stations, hub-and-spoke deployment points, Make Ready Centres, regional HQs at Bolton + Liverpool + Cumbria, EOCs (emergency operations centres) and 999/111 call-handling sites. Most multi-year ambulance-station leases (NHSPS, local-authority and commercial landlords) sit on the balance sheet as ROU assets from FY22, leaving the residual P&L charge for short-term and variable components.",
        "beneficiaries": "Serves a c. 7M North West population across Cumbria + Lancashire + Greater Manchester + Merseyside + Cheshire from c. 110 ambulance stations + Make Ready Centres + 3 EOCs (Bolton, Wigan, Carlisle); c. 6,500 WTE; c. 1.5M 999 incidents/yr + c. 3M NHS 111 calls/yr.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.70M"},
            {"label": "Estate footprint", "value": "c. 110 ambulance stations + hub-and-spoke deployment points + Make Ready Centres + 3 EOCs (Bolton, Wigan, Carlisle) + regional HQs"},
            {"label": "Population served", "value": "c. 7M North West residents across c. 14,000 sq km — Cumbria, Lancashire, Greater Manchester, Merseyside, Cheshire"},
            {"label": "Workforce", "value": "c. 6,500 WTE — paramedics, EMTs, ECAs, call handlers, dispatchers, fleet engineers, leadership"},
            {"label": "Lease line scope", "value": "IFRS 16 short-term (<12mo) + low-value (<£5k pa) + service charges; multi-year ambulance station leases on balance sheet as ROU assets"},
            {"label": "Principal landlords", "value": "NHS Property Services + local authorities (police, fire co-location at some sites) + commercial landlords + NHS trusts (co-located at hospital sites)"},
            {"label": "Hub-and-spoke driver", "value": "Cat-1 8-min standard shifts deployment from station-based to dynamic on-road posting; some stations leased on flexible terms"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr from NHSPS service-charge uprating + business-rates pass-through + Make Ready Centre rollout"},
            {"label": "Delivery body", "value": "NWAS Estates & Facilities + NHSPS + local authorities + commercial landlords"},
            {"label": "Policy owner", "value": "DHSC + NHSE Estates & Capital + NHSE Urgent & Emergency Care + 6 NW ICBs (lead: GM ICB)"},
            {"label": "Evaluation evidence", "value": "NWAS ARA; CQC inspection (RX7); NHSE ERIC; NHSE Ambulance Quality Indicators (AQIs); NAO Reducing emergency admissions (Mar 2018)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 op-lease accounting · Successor: Make Ready Centre estate consolidation + ambulance fleet electrification charging infrastructure under Net Zero 2032"}
        ],
        "notes": "Ambulance services have a distinctive estate model — fewer large hospital-style buildings, instead a network of small ambulance stations and standby points plus 2-3 Make Ready Centres per region for vehicle prep and a couple of EOCs for 999/111 dispatch. NWAS's c. £0.70M residual lease P&L charge captures short-term and variable components after FY22 IFRS 16 capitalised the multi-year leases as right-of-use assets. The Cat-1 8-minute response standard is shifting deployment from station-based to dynamic on-road posting, which influences the future estate strategy. Ambulance fleet electrification under Net Zero 2032 will require substantial new charging infrastructure at stations and Make Ready Centres, reshaping the estate over coming years.",
        "sources": [
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "North West Ambulance Service NHS Trust provider profile (RX7)", "url": "https://www.cqc.org.uk/provider/RX7"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual report and financial statements", "url": "https://www.property.nhs.uk/insights-events/annual-reviews/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "NHS England", "title": "NHS Net Zero — ambulance fleet decarbonisation", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["North West Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Lease expenditure — South Central Ambulance Service NHS Foundation Trust", "Lease expenditure — Yorkshire Ambulance Service NHS Trust", "NHS Property Services"]
    },
    "General supplies & services — Hounslow and Richmond Community Healthcare NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Hounslow and Richmond Community Healthcare NHS Trust"}],
        "description": "HRCH's £0.70M general supplies & services line covers non-drug clinical and consumable purchasing across the trust's c. 30+ community sites in the London Boroughs of Hounslow and Richmond upon Thames — including district-nursing dressings and wound-care consumables, MSK community-physio supplies, school-nursing immunisation kit, continence products, Children's CDC consumables, and minor IPC PPE. Most procurement flows through NHS Supply Chain commodity routes supplemented by direct local contracts for specialist items.",
        "beneficiaries": "Serves the c. 480,000 combined Hounslow + Richmond population (LB Hounslow c. 290,000 + LB Richmond c. 195,000); operates from c. 30+ sites including community nursing bases, child development centres, MSK clinics, school-nursing teams; c. 1,200 WTE incl. district nurses, school nurses, health visitors, AHPs, MSK community physio.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories (interaction) · Procurement Act 2023 (replacing PCR 2015) · NHS Supply Chain framework agreements · NHS Act 2006",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£0.70M"},
            {"label": "Estate footprint", "value": "c. 30+ community sites across LB Hounslow + LB Richmond — community nursing bases + MSK + child development + school nursing + sexual health"},
            {"label": "Population served", "value": "c. 480,000 combined Hounslow (c. 290k) + Richmond upon Thames (c. 195k)"},
            {"label": "Workforce", "value": "c. 1,200 WTE — district nurses, school nurses, health visitors, AHPs, MSK community physio, CAMHS"},
            {"label": "Cost mix", "value": "Wound-care + continence + IPC PPE + school-immunisation kit + child-development assessment kit + MSK supplies"},
            {"label": "Procurement route", "value": "NHS Supply Chain commodity catalogues (02 Wound Care, 04 Continence, 16 IPC) + direct local for specialist items"},
            {"label": "ULEZ exposure", "value": "Both Hounslow + Richmond fully within Greater London ULEZ from August 2023 — drives clean fleet upgrades but doesn't directly affect this line"},
            {"label": "Funding trajectory", "value": "Slowly rising c. 3-5%/yr from clinical-supplies inflation + caseload complexity; Three Shifts community direction may drive volume growth"},
            {"label": "Delivery body", "value": "HRCH Procurement + NHS Supply Chain + community-site teams + local specialist suppliers (e.g. wound care)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Commercial + NHS Supply Chain + NW London ICB + SW London ICB (cross-ICB footprint)"},
            {"label": "Evaluation evidence", "value": "HRCH ARA; CQC provider profile (RY9); Model Hospital community-supplies benchmark; NHSE Operational Plan returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era community supplies + pre-Supply Chain transformation · Successor: NHS Supply Chain category-tower model + Three Shifts community digital procurement"}
        ],
        "notes": "HRCH is unusual among community trusts in covering only two London Boroughs with cross-ICB footprint (LB Hounslow falls under NW London ICB, LB Richmond under SW London ICB), making commissioning a complex tri-party arrangement. The £0.70M general supplies line is dominated by wound-care, continence and IPC PPE consumables sourced through NHS Supply Chain category towers. Caseload complexity in an ageing London population (more chronic-wound and continence cases) drives c. 3-5%/yr inflation. The Three Shifts community-care policy direction (Darzi Sep 2024) is expected to grow community trust volumes and consumable demand, partially offset by NHS Supply Chain leverage.",
        "sources": [
            {"publisher": "Hounslow and Richmond Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hrch.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Hounslow and Richmond Community Healthcare provider profile (RY9)", "url": "https://www.cqc.org.uk/provider/RY9"},
            {"publisher": "NHS Supply Chain", "title": "Category towers — wound care + continence", "url": "https://www.supplychain.nhs.uk/category-tower/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital — community trust benchmarks", "url": "https://model.nhs.uk/"},
            {"publisher": "UK Government", "title": "Procurement Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/54"}
        ],
        "related": ["Hounslow and Richmond Community Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "General supplies & services — Central London Community Healthcare NHS Trust", "General supplies & services — Shropshire Community Health NHS Trust", "NHS Supply Chain"]
    },
    "Business rates — North East Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "North East Ambulance Service NHS Foundation Trust"}],
        "description": "NEAS's £0.66M non-domestic-rates (NDR) bill covers business rates payable on the trust's portfolio of c. 60 ambulance stations, the Bernicia House HQ at Newburn (Newcastle), the Cleadon EOC, Make Ready Centres at Hebburn and Russell House, and standby points across the North East and North Cumbria. NDR is paid to the relevant billing authority (Newcastle, Sunderland, Gateshead, South Tyneside, North Tyneside, Northumberland, Durham, Darlington, Stockton, Middlesbrough, Hartlepool, Redcar & Cleveland) under the Local Government Finance Act 1988 multiplier system, with rateable values from the VOA 2023 list.",
        "beneficiaries": "Serves a c. 2.7M population across the North East and North Cumbria (Northumberland, Tyne and Wear, Durham, Tees Valley, parts of Cumbria); c. 2,800 WTE; c. 350,000 999 incidents/yr + NHS 111 contract; c. 60 ambulance stations + 2 Make Ready Centres + 1 EOC at Cleadon.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.66M"},
            {"label": "Estate footprint", "value": "c. 60 ambulance stations + Bernicia House HQ (Newburn) + Cleadon EOC + Make Ready Centres at Hebburn & Russell House + standby points"},
            {"label": "Population served", "value": "c. 2.7M across Northumberland, Tyne & Wear, Durham, Tees Valley, parts of Cumbria"},
            {"label": "Workforce", "value": "c. 2,800 WTE — paramedics, EMTs, ECAs, call handlers, dispatchers, fleet engineers"},
            {"label": "Billing authorities", "value": "12 LAs: Newcastle, Sunderland, Gateshead, South Tyneside, North Tyneside, Northumberland, Durham, Darlington, Stockton, Middlesbrough, Hartlepool, Redcar & Cleveland"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; small-business 49.9p; ambulance estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Recent context", "value": "NEAS subject to CQC re-inspection 2023-24 and HSSIB review following coroner concerns about response times in 2022"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier under Non-Domestic Rating (M&PF) Act 2024"},
            {"label": "Delivery body", "value": "NEAS Estates & Facilities + NHSPS for some leased stations + 12 billing authorities + VOA"},
            {"label": "Policy owner", "value": "MHCLG (formerly DLUHC) + HM Treasury + DHSC + NHSE Urgent & Emergency Care + North East & North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NEAS ARA; CQC provider profile (RXP); NHSE ERIC; HSSIB review; NHSE Ambulance Quality Indicators (AQIs)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 separate Tyne & Wear, Durham, Northumberland services merged into regional NEAS · Successor: 2026 VOA revaluation + Make Ready Centre estate consolidation + electrification charging infrastructure"}
        ],
        "notes": "Ambulance trusts pay full non-domestic rates with no NHS exemption (unlike charities, NHS bodies don't get 80% mandatory relief), so the line tracks the size and rateable value of the c. 60-station estate. NEAS's £0.66M reflects a smaller estate footprint than the larger ambulance trusts (NWAS, LAS, WMAS) — a function of population and geography. Drivers include the VOA 2023 rating list (which generally raised many ambulance-station RVs), the annual multiplier uprating, and the new supplementary multiplier under the Non-Domestic Rating (M&PF) Act 2024. NEAS has been the subject of regulatory scrutiny following coroner concerns about Cat-2 response times in 2022, which doesn't directly affect rates but pressures estate strategy.",
        "sources": [
            {"publisher": "North East Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.neas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "North East Ambulance Service NHS FT provider profile (RXP)", "url": "https://www.cqc.org.uk/provider/RXP"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"}
        ],
        "related": ["North East Ambulance Service NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Business rates — London Ambulance Service NHS Trust", "Business rates — North West Ambulance Service NHS Trust", "Valuation Office Agency"]
    },
    "Business rates — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "RJAH's £0.65M non-domestic-rates (NDR) bill covers business rates payable on the Gobowen specialist orthopaedic hospital site near Oswestry in north Shropshire (close to the Welsh border) — one of England's leading specialist orthopaedic centres performing tertiary spinal surgery, joint replacement, paediatric orthopaedics, sports medicine and prosthetics. NDR is paid to Shropshire Council under the Local Government Finance Act 1988 multiplier system, with rateable value reflecting the c. 165-bed specialist hospital plus on-site research facilities and the Veterans Orthopaedic Centre.",
        "beneficiaries": "Serves a supra-regional + national orthopaedic catchment from West Midlands, North West, North Wales (cross-border tertiary commissioning) and beyond; c. 165 in-patient beds; c. 1,800 WTE; c. 95,000 outpatient attendances/yr; c. 18,000 surgical procedures including major spinal surgery and joint replacement; UK's largest single-site orthopaedic centre.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.65M"},
            {"label": "Estate footprint", "value": "Single Gobowen site near Oswestry, north Shropshire — c. 165 in-patient beds + outpatients + theatres + research facilities + Veterans Orthopaedic Centre"},
            {"label": "Specialty footprint", "value": "Specialist orthopaedic — UK's largest single-site orthopaedic centre; spinal surgery, paediatric orthopaedics, sports medicine, prosthetics"},
            {"label": "Annual activity", "value": "c. 95,000 outpatient attendances/yr; c. 18,000 surgical procedures; supra-regional + national tertiary referrals"},
            {"label": "Workforce", "value": "c. 1,800 WTE — orthopaedic surgeons, anaesthetists, theatres staff, prosthetists, AHPs, research"},
            {"label": "Billing authority", "value": "Shropshire Council (single unitary) — single billing point unlike multi-site trusts"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under NDR Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; small-business 49.9p; specialist orthopaedic estate on standard multiplier (no NHS exemption)"},
            {"label": "Welsh-border commissioning", "value": "Significant cross-border tertiary referrals from north Wales — Welsh Government commissions some service lines"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier under NDR (M&PF) Act 2024"},
            {"label": "Delivery body", "value": "RJAH Estates & Facilities + Shropshire Council (billing authority) + VOA"},
            {"label": "Policy owner", "value": "MHCLG + HM Treasury + DHSC + NHSE Specialised Commissioning (specialist orthopaedics) + Shropshire, Telford & Wrekin ICB + Welsh Government (cross-border)"},
            {"label": "Evaluation evidence", "value": "RJAH ARA; CQC provider profile (RL1); NHSE Specialised Commissioning service spec; ICB performance review"},
            {"label": "Predecessor / successor", "value": "Predecessor: founded 1900 as Baschurch Convalescent Home, now one of England's longest-established orthopaedic centres · Successor: 2026 VOA revaluation + planned site investment under NHSE specialised orthopaedic strategy"}
        ],
        "notes": "RJAH is a unique trust in the English NHS landscape — a single-site specialist orthopaedic hospital in a deeply rural Shropshire location near the Welsh border, founded 1900 and now one of England's leading tertiary orthopaedic centres. Like other NHS trusts it pays full NDR with no exemption. The £0.65M bill reflects the rateable value of the c. 165-bed hospital plus on-site research facilities (the Keele Univ Medical School research partnership) and the dedicated Veterans Orthopaedic Centre. The single billing point (Shropshire Council unitary) simplifies administration compared to multi-site trusts. The 2026 VOA revaluation is the key forward-looking driver under the new 3-year cycle.",
        "sources": [
            {"publisher": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rjah.nhs.uk/about-us/publications"},
            {"publisher": "Care Quality Commission", "title": "RJAH Orthopaedic Hospital NHS FT provider profile (RL1)", "url": "https://www.cqc.org.uk/provider/RL1"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "NHS England", "title": "Specialised commissioning — orthopaedic services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Business rates — Royal National Orthopaedic Hospital NHS Trust", "Business rates — The Royal Orthopaedic Hospital NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Sheffield Children's NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Sheffield Children's NHS Foundation Trust"}],
        "description": "Sheffield Children's £0.63M transport line covers business-mileage reimbursement (HMRC AMAP) for clinical and support staff, leased pool-cars under IFRS 16, the Embrace Yorkshire & Humber Infant and Children's Transport (paediatric retrieval) service operated by the trust, patient-transport reimbursements under NHSE PTS Eligibility for outpatient clinics, and specialist couriers shifting paediatric pathology, blood and pharmacy items between the Western Bank main hospital, Ryegate community/respite site and partner DGHs across Yorkshire & Humber.",
        "beneficiaries": "Serves a c. 5.5M paediatric supra-regional catchment across South Yorkshire, North Derbyshire, Bassetlaw and parts of Lincolnshire (and the wider Yorkshire & Humber via the Embrace retrieval network); c. 280,000 patient attendances/yr; c. 4,000 WTE; one of England's six paediatric tertiary centres.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Healthcare Travel Costs Scheme (HTCS) · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.63M"},
            {"label": "Specialty footprint", "value": "Tertiary children's hospital — Western Bank main site (Sheffield) + Ryegate community/respite + Embrace retrieval base"},
            {"label": "Supra-regional catchment", "value": "c. 5.5M paediatric population across S Yorks, N Derbyshire, Bassetlaw, parts of Lincs; one of England's six paediatric tertiary centres"},
            {"label": "Annual activity", "value": "c. 280,000 patient attendances/yr; c. 18,000 inpatient admissions; c. 50,000 ED attendances; c. 12,000 surgical procedures"},
            {"label": "Workforce", "value": "c. 4,000 WTE; c. 250 medical staff incl. tertiary paediatric surgeons, neurosurgeons, oncologists, dentists"},
            {"label": "Embrace retrieval", "value": "Yorkshire & Humber Infant and Children's Transport service — c. 2,000 critically-ill child transfers/yr to PICU across the region (largest UK paediatric retrieval service)"},
            {"label": "PTS driver", "value": "Outpatient clinics across Y&H drive HTCS reimbursement; long-distance referrals from rural N Yorks + rural Lincs"},
            {"label": "Funding trajectory", "value": "Rising due to Embrace retrieval volume growth + IFRS 16 2022 lease re-recognition + AMAP mileage growth + Net Zero fleet replacement"},
            {"label": "Delivery body", "value": "Sheffield Children's Estates & Facilities + Embrace retrieval team + leased-fleet supplier (NHS Fleet Solutions / commercial) + specialist paediatric couriers"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (paediatric tertiary services + paediatric retrieval) + South Yorkshire ICB + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Sheffield Children's ARA; CQC inspection (RCU); Embrace service review; NHSE paediatric PICU service specification"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 op-lease accounting · Successor: zero-emission pool fleet under NHSE Net Zero 2032 + ongoing Embrace retrieval volume growth"}
        ],
        "notes": "Sheffield Children's runs Embrace, England's largest paediatric retrieval service, moving c. 2,000 critically-ill children/yr from DGH-level care to PICU across Yorkshire & Humber and beyond. The £0.63M transport line is modest in absolute terms because the trust is concentrated on the Western Bank main hospital (with Ryegate community/respite as the only significant satellite) but Embrace retrieval, AMAP business mileage for staff outreach and HTCS patient reimbursement are the main drivers. IFRS 16 2022 lease re-recognition reshaped the accounting; Net Zero 2032 fleet electrification is being phased into pool-car renewals. Embrace's specialist paediatric retrieval ambulances are bespoke vehicles with high replacement cost.",
        "sources": [
            {"publisher": "Sheffield Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sheffieldchildrens.nhs.uk/about-us/our-publications/"},
            {"publisher": "Embrace Yorkshire & Humber Infant and Children's Transport", "title": "Service overview", "url": "https://www.embrace.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Children's NHS Foundation Trust provider profile (RCU)", "url": "https://www.cqc.org.uk/provider/RCU"},
            {"publisher": "NHS England", "title": "Specialised commissioning — paediatric services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Healthcare Travel Costs Scheme (HTCS)", "url": "https://www.nhs.uk/nhs-services/help-with-health-costs/healthcare-travel-costs-scheme-htcs/"}
        ],
        "related": ["Sheffield Children's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — Alder Hey Children's NHS Foundation Trust", "Transport (business + patient) — Great Ormond Street Hospital for Children NHS Foundation Trust", "NHS England"]
    },
    "Lease expenditure — North East Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "North East Ambulance Service NHS Foundation Trust"}],
        "description": "NEAS's £0.62M lease expenditure represents IFRS 16 short-term and low-value lease charges (and residual operating lease costs not capitalised as right-of-use assets) on the trust's portfolio of c. 60 ambulance stations, the Bernicia House HQ at Newburn (Newcastle), the Cleadon EOC (emergency operations centre), Make Ready Centres at Hebburn and Russell House, and standby points across the North East and North Cumbria. Most multi-year ambulance-station leases sit on the balance sheet as ROU assets from FY22, leaving the residual P&L charge for short-term and variable components.",
        "beneficiaries": "Serves a c. 2.7M population across Northumberland, Tyne & Wear, Durham, Tees Valley and parts of Cumbria from c. 60 ambulance stations + 2 Make Ready Centres + the Cleadon EOC; c. 2,800 WTE; c. 350,000 999 incidents/yr; NHS 111 contract holder for North East.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.62M"},
            {"label": "Estate footprint", "value": "c. 60 ambulance stations + Bernicia House HQ (Newburn) + Cleadon EOC + Make Ready Centres at Hebburn & Russell House + standby points"},
            {"label": "Population served", "value": "c. 2.7M across Northumberland, Tyne & Wear, Durham, Tees Valley, parts of Cumbria"},
            {"label": "Workforce", "value": "c. 2,800 WTE — paramedics, EMTs, ECAs, call handlers, dispatchers, fleet engineers"},
            {"label": "Lease line scope", "value": "IFRS 16 short-term (<12mo) + low-value (<£5k pa) + service charges; multi-year ambulance station leases on balance sheet as ROU assets"},
            {"label": "Principal landlords", "value": "NHS Property Services + 12 LAs + commercial landlords + co-located NHS trusts (some hospital-site standby points)"},
            {"label": "Hub-and-spoke driver", "value": "Cat-1 8-min standard shifts deployment from station-based to dynamic on-road posting; some stations leased on flexible terms"},
            {"label": "Recent context", "value": "NEAS subject to CQC re-inspection 2023-24 + HSSIB review following coroner concerns about Cat-2 response times in 2022"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr from NHSPS service-charge uprating + business-rates pass-through + Make Ready Centre rollout"},
            {"label": "Delivery body", "value": "NEAS Estates & Facilities + NHSPS + 12 LAs + commercial landlords"},
            {"label": "Policy owner", "value": "DHSC + NHSE Estates & Capital + NHSE Urgent & Emergency Care + NE & N Cumbria ICB + NHSPS"},
            {"label": "Evaluation evidence", "value": "NEAS ARA; CQC provider profile (RXP); NHSE ERIC; HSSIB review; NHSE Ambulance Quality Indicators (AQIs)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 op-lease accounting · Successor: Make Ready Centre estate consolidation + electrification charging infrastructure under Net Zero 2032"}
        ],
        "notes": "Ambulance services have a distinctive estate model — fewer large hospital-style buildings, instead a network of small ambulance stations and standby points plus 2-3 Make Ready Centres per region for vehicle prep and 1 EOC for 999/111 dispatch. NEAS's c. £0.62M residual lease P&L charge captures short-term and variable components after FY22 IFRS 16 capitalised the multi-year leases as right-of-use assets. The Cat-1 8-minute standard is shifting deployment from station-based to dynamic on-road posting, which influences the future estate strategy. Net Zero 2032 fleet electrification will require substantial new charging infrastructure at stations and Make Ready Centres, reshaping the estate over coming years.",
        "sources": [
            {"publisher": "North East Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.neas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "North East Ambulance Service NHS FT provider profile (RXP)", "url": "https://www.cqc.org.uk/provider/RXP"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual report and financial statements", "url": "https://www.property.nhs.uk/insights-events/annual-reviews/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "NHS England", "title": "NHS Net Zero — ambulance fleet decarbonisation", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["North East Ambulance Service NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Lease expenditure — North West Ambulance Service NHS Trust", "Lease expenditure — South Central Ambulance Service NHS Foundation Trust", "NHS Property Services"]
    },
    "Lease expenditure — South Western Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "South Western Ambulance Service NHS Foundation Trust"}],
        "description": "SWAST's £0.59M lease expenditure represents IFRS 16 short-term and low-value lease charges (and residual operating lease costs not capitalised as right-of-use assets) on the trust's portfolio of c. 95+ ambulance stations and standby points across the largest geographic patch of any English ambulance service — Devon, Cornwall (incl Isles of Scilly), Somerset, Dorset, Wiltshire, Gloucestershire and Bristol. Most multi-year ambulance-station leases sit on the balance sheet as ROU assets from FY22, leaving the residual P&L charge for short-term and variable components.",
        "beneficiaries": "Serves a c. 5.5M population across the South West (Devon, Cornwall, Somerset, Dorset, Wiltshire, Gloucestershire, Bristol, Isles of Scilly) — England's largest geographic ambulance patch by area covering c. 10,000 sq mi; c. 4,500 WTE; c. 1M 999 incidents/yr.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.59M"},
            {"label": "Estate footprint", "value": "c. 95+ ambulance stations + standby points + Make Ready Centres + Clinical Hub at Exeter + EOCs at Exeter + Bristol"},
            {"label": "Population served", "value": "c. 5.5M across Devon, Cornwall (incl Isles of Scilly), Somerset, Dorset, Wiltshire, Gloucestershire, Bristol — c. 10,000 sq mi (largest English ambulance patch by area)"},
            {"label": "Workforce", "value": "c. 4,500 WTE — paramedics, EMTs, ECAs, call handlers, dispatchers, fleet engineers"},
            {"label": "Lease line scope", "value": "IFRS 16 short-term (<12mo) + low-value (<£5k pa) + service charges; multi-year ambulance station leases on balance sheet as ROU assets"},
            {"label": "Principal landlords", "value": "NHS Property Services + LAs (incl unitary authorities — Cornwall, Wilts, BCP, etc.) + commercial landlords + co-located fire/police bases"},
            {"label": "Geographic driver", "value": "Long rural distances + Isles of Scilly islands service + tourism seasonality (peak summer demand) shape estate distribution"},
            {"label": "Hub-and-spoke driver", "value": "Cat-1 8-min standard particularly challenging across rural Devon/Cornwall — drives standby-point flexibility"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr from NHSPS service-charge uprating + business-rates pass-through + Make Ready Centre rollout"},
            {"label": "Delivery body", "value": "SWAST Estates & Facilities + NHSPS + multiple LAs + commercial landlords"},
            {"label": "Policy owner", "value": "DHSC + NHSE Estates & Capital + NHSE Urgent & Emergency Care + 7 SW ICBs (lead: BNSSG ICB) + NHSPS"},
            {"label": "Evaluation evidence", "value": "SWAST ARA; CQC provider profile (RYF); NHSE ERIC; NHSE Ambulance Quality Indicators (AQIs); ORH benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 separate Devon, Cornwall, Somerset, Dorset, Wilts services merged into SWAST + pre-IFRS-16 op-lease · Successor: Make Ready Centre consolidation + electrification charging infrastructure under Net Zero 2032"}
        ],
        "notes": "SWAST covers England's largest geographic ambulance patch by area — c. 10,000 sq mi from the Cotswolds to Land's End plus the Isles of Scilly — which drives a distributed estate of c. 95+ small stations and standby points needed to deliver Cat-1 8-minute response across deeply rural Devon and Cornwall. The £0.59M residual lease P&L charge captures short-term and variable components after FY22 IFRS 16 capitalised the multi-year leases as right-of-use assets. Tourism seasonality (peak summer demand) and the Isles of Scilly island service shape estate strategy. Net Zero 2032 fleet electrification will require substantial new charging infrastructure at stations and Make Ready Centres — particularly challenging across rural areas with weaker grid capacity.",
        "sources": [
            {"publisher": "South Western Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swast.nhs.uk/about/our-publications"},
            {"publisher": "Care Quality Commission", "title": "South Western Ambulance Service NHS FT provider profile (RYF)", "url": "https://www.cqc.org.uk/provider/RYF"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 7 Leases", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual report and financial statements", "url": "https://www.property.nhs.uk/insights-events/annual-reviews/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "NHS England", "title": "NHS Net Zero — ambulance fleet decarbonisation", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["South Western Ambulance Service NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Lease expenditure — North West Ambulance Service NHS Trust", "Lease expenditure — South Central Ambulance Service NHS Foundation Trust", "NHS Property Services"]
    },
    "Drugs costs — South Western Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "South Western Ambulance Service NHS Foundation Trust"}],
        "description": "SWAST's £0.58M drugs costs line covers paramedic-administered emergency medicines carried on c. 600+ frontline ambulances, RRVs and motorbikes across the South West — under the JRCALC (Joint Royal Colleges Ambulance Liaison Committee) clinical practice guidelines. The drug formulary includes opioid analgesics (morphine, fentanyl), TXA (tranexamic acid for major haemorrhage), benzodiazepines for seizures, adrenaline (cardiac arrest + anaphylaxis), aspirin (suspected ACS), GTN (cardiac chest pain), salbutamol/ipratropium nebs (asthma/COPD), naloxone (opioid OD), oxygen, and obstetric drugs (oxytocin, Syntometrine). All purchased under the Drug Tariff and Branded Medicines Pricing Scheme (now VPAG voluntary scheme from 2024).",
        "beneficiaries": "Serves a c. 5.5M population across the South West (Devon, Cornwall, Somerset, Dorset, Wilts, Gloucs, Bristol, Isles of Scilly); c. 600+ frontline emergency vehicles; c. 1M 999 incidents/yr; c. 4,500 WTE incl. paramedics carrying controlled drugs and POMs under PGDs/PSDs.",
        "legal_basis": "NHS Act 2006 (Drug Tariff Part VIII) · Branded Medicines Pricing Scheme (statutory replaced by VPAG voluntary scheme 2024) · Misuse of Drugs Act 1971 + Misuse of Drugs Regulations 2001 (paramedic CD exemption) · Human Medicines Regulations 2012 (POM exemptions for paramedics + PGDs) · MHRA",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.58M"},
            {"label": "Service footprint", "value": "Regional ambulance service for SW England — c. 600+ frontline emergency vehicles + Make Ready Centres + EOCs at Exeter + Bristol"},
            {"label": "Population served", "value": "c. 5.5M across Devon, Cornwall, Somerset, Dorset, Wilts, Gloucs, Bristol, Isles of Scilly"},
            {"label": "Workforce", "value": "c. 4,500 WTE; c. 2,500 paramedics + technicians authorised to administer POMs under HMR 2012 exemptions"},
            {"label": "JRCALC formulary", "value": "Opioid analgesics (morphine, fentanyl) + TXA + benzodiazepines + adrenaline + aspirin + GTN + salbutamol/ipratropium + naloxone + obstetric drugs + oxygen"},
            {"label": "CD handling", "value": "Controlled drugs (morphine, fentanyl) under MDR 2001 — secure CD storage at every Make Ready Centre + audit trail per dose"},
            {"label": "TXA driver", "value": "Tranexamic acid for major haemorrhage — JRCALC adopted post-CRASH-2 trial; drives ambulance trauma drug spend across all regions"},
            {"label": "Funding trajectory", "value": "Modest growth c. 3-5%/yr; volume driven by 999 incident growth + JRCALC formulary expansions; Branded scheme transition (statutory→VPAG) from 2024"},
            {"label": "Delivery body", "value": "SWAST Pharmacy + Procurement + NHS Supply Chain + commercial pharmaceutical wholesalers (AAH, Alliance Healthcare)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Commercial Medicines + JRCALC + NHSE Urgent & Emergency Care + 7 SW ICBs"},
            {"label": "Evaluation evidence", "value": "SWAST ARA; CQC provider profile (RYF); JRCALC clinical guidelines; NHSE Ambulance Quality Indicators (AQIs); CD AO returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 county ambulance services + pre-VPAG statutory pricing · Successor: VPAG voluntary scheme 2024 + ongoing JRCALC formulary expansion (e.g. ketamine, anti-emetics, point-of-care ECMO drugs)"}
        ],
        "notes": "Ambulance trust drugs costs are a low-volume, high-clinical-criticality line — paramedics carry a JRCALC-defined formulary on every frontline vehicle (typically c. 30-50 line items) including controlled drugs (morphine, fentanyl) under the Misuse of Drugs Regulations 2001 paramedic exemption and POMs under the Human Medicines Regulations 2012. SWAST's £0.58M reflects c. 600+ vehicle footprint and c. 1M 999 incidents/yr across the largest geographic ambulance patch in England. Drivers include JRCALC formulary expansions (TXA post-CRASH-2, anti-emetics, ketamine adoption), 999 incident growth, and the 2024 transition from the statutory Branded Medicines Pricing Scheme to the VPAG voluntary scheme. CD compliance under the SI Reg 2001 + MDA 1971 is a major operational overhead.",
        "sources": [
            {"publisher": "South Western Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swast.nhs.uk/about/our-publications"},
            {"publisher": "Joint Royal Colleges Ambulance Liaison Committee", "title": "JRCALC Clinical Practice Guidelines", "url": "https://aace.org.uk/clinical-practice-guidelines/"},
            {"publisher": "Department of Health and Social Care", "title": "Voluntary Scheme for Branded Medicines Pricing, Access and Growth (VPAG) 2024", "url": "https://www.gov.uk/government/publications/the-2024-voluntary-scheme-for-branded-medicines-pricing-access-and-growth"},
            {"publisher": "Care Quality Commission", "title": "South Western Ambulance Service NHS FT provider profile (RYF)", "url": "https://www.cqc.org.uk/provider/RYF"},
            {"publisher": "UK Government", "title": "Misuse of Drugs Regulations 2001 — paramedic CD exemption", "url": "https://www.legislation.gov.uk/uksi/2001/3998/contents"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQIs)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"}
        ],
        "related": ["South Western Ambulance Service NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Ambulance Trusts", "Drugs costs — West Midlands Ambulance Service University NHS Foundation Trust", "Drugs costs — London Ambulance Service NHS Trust", "JRCALC"]
    },
}
