# -*- coding: utf-8 -*-
# Phase 2 SCamb — chunk 18 (17 NHS Specialist/Community/Ambulance Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Lease expenditure — The Walton Centre NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "The Walton Centre NHS Foundation Trust"}],
        "description": "The Walton Centre's £0.19M lease expenditure line covers IFRS 16-recognised operating-lease charges on small ancillary leased space, equipment leases (e.g. office printer/MFD fleet, small clinical-equipment leases) and any short-life property leases at the Lower Lane, Fazakerley site or satellite outreach clinics. Walton is England's only standalone neurology and neurosurgery specialist trust, with a tightly-bounded estate centred on the Sid Watkins Building and main hospital block, so leased footprint is small versus larger acute trusts.",
        "beneficiaries": "Supports the c. 3.4M-population Cheshire & Mersey neuroscience catchment plus tertiary referrals from across North Wales, Isle of Man and the North West; trust runs c. 130 inpatient beds and c. 1,800 WTE staff across one main site and outreach clinics in c. 20 hospitals across the network.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.19M (£191k)"},
            {"label": "Trust profile", "value": "England's only standalone neurology + neurosurgery specialist trust"},
            {"label": "Main site", "value": "Lower Lane, Fazakerley, Liverpool — co-located with Aintree University Hospital"},
            {"label": "Bed base", "value": "c. 130 inpatient neuroscience beds + Cheshire & Merseyside Rehabilitation Centre beds"},
            {"label": "Workforce", "value": "c. 1,800 WTE staff (consultants, neurosurgeons, nursing, AHPs)"},
            {"label": "Catchment", "value": "c. 3.4M Cheshire & Merseyside resident population + tertiary referrals from N Wales, IoM, Lancashire"},
            {"label": "Outreach footprint", "value": "Outreach neurology + neurosurgery clinics at c. 20 partner hospitals across the network"},
            {"label": "Lease scope", "value": "Office equipment (MFD print fleet), small clinical-equipment leases, ancillary leased rooms in partner hospitals for outreach clinics"},
            {"label": "IFRS 16 transition", "value": "April 2022 IFRS 16 adoption brought most operating leases onto balance sheet — residual P&L line is short-life + low-value-asset exemptions"},
            {"label": "Funding trajectory", "value": "Stable c. £180-200k since IFRS 16 transition (2022); pre-2022 line was higher under IAS 17 operating-lease treatment"},
            {"label": "Delivery body", "value": "Walton Centre Estates & Facilities + Procurement; counterparties include HSCNI/NHSPS for any partner-hospital outreach space"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (specialist neurosciences D04 service line) + DHSC + NHS Resolution"},
            {"label": "Evaluation evidence", "value": "Walton Centre Annual Report and Accounts; CQC inspection reports (Outstanding rated); Model Hospital benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2009 Walton Hospital Trust + Cheshire neurosciences merger · Successor: ongoing Sid Watkins Building expansion + Cheshire & Merseyside neurosciences network growth"}
        ],
        "notes": "Walton Centre is one of the smallest specialist trusts by turnover but commands a uniquely focused remit as the only standalone neuro trust in England. Its leased footprint is intentionally minimal — the trust is a single-campus operation co-located with Aintree on the Lower Lane site, which keeps the operating-lease line low. Most of the residual £191k post-IFRS 16 reflects small-asset and short-life carve-outs (printer fleet, low-value clinical-equipment leases, outreach-clinic peppercorn rentals at partner trusts). The April 2022 IFRS 16 transition reshaped the historical line by capitalising operating leases as right-of-use assets — this P&L line therefore covers exemptions only.",
        "sources": [
            {"publisher": "The Walton Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thewaltoncentre.nhs.uk/238/about-us.html"},
            {"publisher": "Care Quality Commission", "title": "The Walton Centre provider profile (RET)", "url": "https://www.cqc.org.uk/provider/RET"},
            {"publisher": "NHS England", "title": "Specialised commissioning — Neurosciences (D04)", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury / FRAB", "title": "IFRS 16 application in central government and NHS", "url": "https://www.gov.uk/government/publications/financial-reporting-advisory-board-frab"}
        ],
        "related": ["The Walton Centre NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Lease expenditure — The Royal Orthopaedic Hospital NHS Foundation Trust", "Amortisation — The Walton Centre NHS Foundation Trust", "NHS Property Services"]
    },
    "Amortisation — Lincolnshire Community Health Services NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Lincolnshire Community Health Services NHS Trust"}],
        "description": "LCHS's £0.19M amortisation line is the IAS 38 charge against intangible assets — primarily clinical and corporate software (SystmOne EPR licences, RiO mental-health overlap, Oracle finance ledger, ESR HR/payroll local configurations) and software-development capitalisation. Lincolnshire Community runs district nursing, school nursing, MIUs and community hospitals across one of England's largest rural counties, so amortisation reflects mostly the EPR + roster software stack plus any internally-generated digital-tools capitalisation under DHSC GAM rules.",
        "beneficiaries": "Serves a c. 770,000 resident population across Lincolnshire (one of England's largest counties by area at 6,959 km²) including Boston, Skegness, Lincoln, Grantham and Stamford rural communities; runs c. 8 community hospitals (e.g. Louth County, Skegness, Spalding, Gainsborough) plus Minor Injuries Units and c. 2,400 WTE community-nursing staff.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 chapter 5 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.19M (£186,247)"},
            {"label": "Trust scope", "value": "Community health services + community hospitals + 0-19 Healthy Child Programme across Lincolnshire"},
            {"label": "Geographic footprint", "value": "Lincolnshire — 6,959 km² (4th-largest English county by area); Boston/Skegness coastal + Wolds + Fens"},
            {"label": "Population served", "value": "c. 770,000 residents across c. 7 District Council areas + Lincolnshire ICB footprint"},
            {"label": "Community hospitals", "value": "c. 8 community hospitals (Louth, Skegness, Spalding, Gainsborough, Stamford, John Coupland Hospital etc.)"},
            {"label": "Workforce", "value": "c. 2,400 WTE — predominantly district nurses, health visitors, community physios, MIU clinicians"},
            {"label": "Asset scope", "value": "Software intangibles — SystmOne community module, ESR, Oracle finance, internally-generated patient-app capitalisation"},
            {"label": "EPR system", "value": "TPP SystmOne community module — primary clinical record (shared with Lincolnshire GP federation)"},
            {"label": "Funding trajectory", "value": "Stable c. £150-200k as software useful-economic-life amortises over 3-5 years; growth depends on Three Shifts digital capex"},
            {"label": "Delivery body", "value": "LCHS IT/Digital + Finance + ULHT/NHSPS estate partners; software vendors include TPP SystmOne, Oracle, IBM Cognos"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation programme + DHSC + Lincolnshire ICB"},
            {"label": "Evaluation evidence", "value": "LCHS Annual Report; CQC community provider profile; NHSE Operational Plan returns; What Good Looks Like digital maturity"},
            {"label": "Predecessor / successor", "value": "Predecessor: Lincolnshire PCT community arm pre-2011 TCS · Successor: Three Shifts community-digital lift + EPR convergence with Lincolnshire ICB Single Patient Record"}
        ],
        "notes": "LCHS is among England's most rural community trusts, operating across a county that exceeds the size of several London-region trust catchments combined. Its amortisation line is comparatively small versus larger urban community trusts because the trust's intangibles base is dominated by SystmOne community-module licences (shared with primary care) and incremental software-capitalisation rather than bespoke clinical-system development. The Three Shifts policy direction (Darzi report, Sep 2024) and NHSE Frontline Digitisation programme are likely to lift capitalised software spend over the medium term as community providers adopt shared digital platforms. April 2025 NIC step-up does not directly affect this line but compresses overall trust capex headroom.",
        "sources": [
            {"publisher": "Lincolnshire Community Health Services NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lincolnshirecommunityhealthservices.nhs.uk/about-us/who-we-are/board-papers-and-publications"},
            {"publisher": "Care Quality Commission", "title": "LCHS provider profile (RY5)", "url": "https://www.cqc.org.uk/provider/RY5"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Lincolnshire Community Health Services NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Hertfordshire Community NHS Trust", "Amortisation — Wirral Community Health and Care NHS Foundation Trust", "NHS England Frontline Digitisation"]
    },
    "PFI / LIFT charges — Sussex Community NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Sussex Community NHS Foundation Trust"}],
        "description": "Sussex Community's £0.18M PFI / LIFT charges line covers the unitary-charge service-element on LIFT (Local Improvement Finance Trust) primary-care and community-health buildings used by the trust across East and West Sussex. LIFT was the New Labour-era community-estate vehicle (Community Health Partnerships parent) for renewing GP surgeries, walk-in centres and community clinics on long PPP leases — Sussex Community occupies space in a small number of LIFT-financed buildings rather than holding direct PFI debt.",
        "beneficiaries": "Supports the c. 1.7M-population East + West Sussex catchment served by Sussex Community NHS FT; trust runs district nursing, school nursing, MSK community physiotherapy, end-of-life care and 3 community hospitals (Crowborough, Lewes Victoria, Uckfield) with c. 4,500 WTE staff across c. 70 sites.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition) · DHSC PFI/LIFT guidance · Local Improvement Finance Trust (LIFT) framework (Community Health Partnerships) · NHS Act 2006",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.18M (£180,000)"},
            {"label": "Trust scope", "value": "Community provider — district nursing, MSK physio, school nursing, EoL care, community hospitals across Sussex"},
            {"label": "LIFT operator", "value": "Community Health Partnerships (CHP) — DHSC-owned property company with majority stake in regional LIFTcos"},
            {"label": "Geographic footprint", "value": "East Sussex + West Sussex — c. 3,800 km² coastal + Downs"},
            {"label": "Population served", "value": "c. 1.7M residents (East Sussex + West Sussex + Brighton & Hove community-service overlap)"},
            {"label": "Community hospitals", "value": "Crowborough War Memorial, Lewes Victoria, Uckfield (community)"},
            {"label": "Workforce", "value": "c. 4,500 WTE community-health staff"},
            {"label": "PFI/LIFT scope", "value": "Service-charge component (FM, lifecycle, soft FM) on LIFT-financed clinic/community-hospital buildings; capital element flows via lease-recognition under IFRS 16"},
            {"label": "IFRS 16 transition", "value": "April 2022 transition reclassified some LIFT lease-financed elements to balance-sheet right-of-use assets"},
            {"label": "Funding trajectory", "value": "Stable c. £170-190k as LIFT contracts run through their c. 25-30 year tail"},
            {"label": "Delivery body", "value": "Sussex Community Estates & Facilities + Community Health Partnerships LIFTco regional vehicles + private-sector FM operators"},
            {"label": "Policy owner", "value": "DHSC Estates and Facilities + Community Health Partnerships + Sussex ICB"},
            {"label": "Evaluation evidence", "value": "Sussex Community ARA; CHP annual report; NAO PFI in healthcare reports; Model Hospital estate benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2003 NHS direct-construction model · Successor: Three Shifts community estate refresh + LIFT contract expiry handover from c. 2030 onwards"}
        ],
        "notes": "Sussex Community's PFI/LIFT line is small versus large acute-trust PFI debts because the trust occupies LIFT-financed clinic and community-hospital space rather than carrying any major PFI hospital build itself. LIFT is a different beast from acute-hospital PFI: the regional LIFTco (jointly owned by Community Health Partnerships and a private-sector partner) builds and owns clinic / community-hospital buildings, with NHS tenants paying a unitary charge that includes finance + lifecycle + FM. The April 2022 IFRS 16 transition reclassified the lease-financed element to balance-sheet right-of-use assets, leaving this P&L line covering the service-charge (FM, lifecycle, soft services) component. Most LIFT contracts have c. 25-30 year tails running into the early 2030s.",
        "sources": [
            {"publisher": "Sussex Community NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sussexcommunity.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "Community Health Partnerships", "title": "Annual Report and Accounts (LIFT portfolio)", "url": "https://communityhealthpartnerships.co.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — PFI/LIFT", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sussex Community NHS FT provider profile (RDR)", "url": "https://www.cqc.org.uk/provider/RDR"}
        ],
        "related": ["Sussex Community NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "PFI / LIFT charges — Northamptonshire Healthcare NHS Foundation Trust", "PFI / LIFT charges — Birmingham Community Healthcare NHS Foundation Trust", "Community Health Partnerships"]
    },
    "Transport (business + patient) — Wirral Community Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Wirral Community Health and Care NHS Foundation Trust"}],
        "description": "Wirral Community Health & Care's £0.18M transport line covers AMAP staff mileage for district nurses, health visitors, school nurses and MSK community physios driving across the Wirral peninsula plus Cheshire West & Chester catchment, pool-car fleet running costs and any IFRS 16 lease-recognised vehicle leases. Workforce is dispersed across patient homes, schools, GP-attached community-clinic rooms and care homes — driving substantial AMAP exposure even though the geographic footprint is compact compared to a county community trust.",
        "beneficiaries": "Serves a c. 320,000-population Wirral peninsula catchment plus Cheshire West & Chester 0-19 services; trust runs district nursing, health visiting, school nursing, MSK community physiotherapy and end-of-life care with c. 1,500 WTE staff visiting patients in c. 138,000 households + c. 60 schools.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments (45p first 10,000 / 25p thereafter) · IFRS 16 Leases (pool fleet) · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.18M (£177,499)"},
            {"label": "Trust scope", "value": "Community provider — DN, HV, school nursing, MSK physio, EoL care across Wirral + CWAC 0-19"},
            {"label": "Geographic footprint", "value": "Wirral peninsula c. 157 km² + Cheshire West & Chester 0-19 service overlap"},
            {"label": "Population served", "value": "c. 320,000 Wirral residents + 0-19 service for CWAC"},
            {"label": "Workforce", "value": "c. 1,500 WTE — predominantly community-facing nurses + AHPs"},
            {"label": "Visit volume", "value": "c. 138,000 Wirral households served by district nursing + HV; c. 60 schools served by school nursing"},
            {"label": "Cost driver — AMAP mileage", "value": "HMRC AMAP rates 45p / 25p — staff personal-vehicle mileage dominates this line for community providers"},
            {"label": "Pool fleet", "value": "Small electric + ICE pool-car fleet; some shared-use with Cheshire & Wirral Partnership mental-health trust"},
            {"label": "PTS scope", "value": "PTS not directly provided — NWAS/EMED group runs Cheshire/Mersey PTS contract"},
            {"label": "Funding trajectory", "value": "Stable c. £170-180k as AMAP rates have not been uprated since 2011 despite fuel inflation; growth tied to caseload"},
            {"label": "Delivery body", "value": "WCHC Fleet & Logistics + HR/Payroll for AMAP claims; pool-fleet operators include NHS Fleet Solutions"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care + Cheshire & Merseyside ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "WCHC Annual Report; CQC inspection (Outstanding rated); Model Hospital community benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: Wirral PCT community arm pre-2011 TCS · Successor: Three Shifts community-care lift + EV pool-fleet transition under NHSE Net Zero 2032"}
        ],
        "notes": "Wirral Community Health & Care is a small-footprint but high-density community trust — the Wirral peninsula's c. 157 km² packs c. 320,000 residents, so the per-mile cost-of-care differs from rural Lincolnshire or Norfolk community trusts. The £177k transport line is dominated by AMAP staff-mileage reimbursement at the HMRC 45p/25p rate (frozen since 2011 despite c. 50% cumulative DERV/petrol inflation) plus pool-car running costs. The trust earned an Outstanding CQC rating overall in 2018 and remains one of the smaller standalone community FTs. Three Shifts (Darzi, Sep 2024) shifts care closer to home and is expected to grow community workforce and consequently mileage exposure.",
        "sources": [
            {"publisher": "Wirral Community Health and Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wchc.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Wirral Community Health and Care provider profile (RY7)", "url": "https://www.cqc.org.uk/provider/RY7"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — Reimbursement of travel costs", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "Lord Darzi", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Wirral Community Health and Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Transport (business + patient) — Hertfordshire Community NHS Trust", "Transport (business + patient) — Sussex Community NHS Foundation Trust", "Amortisation — Wirral Community Health and Care NHS Foundation Trust"]
    },
    "Inventories written down — Royal National Orthopaedic Hospital NHS Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Royal National Orthopaedic Hospital NHS Trust"}],
        "description": "RNOH Stanmore's £0.17M inventories-written-down line is the IAS 2 charge for orthopaedic implants, prosthetics, surgical-supplies and theatre-disposables that have passed sell-by, become obsolete (e.g. superseded implant generations following NICE guidance change), been damaged or otherwise written off the inventory ledger. RNOH is England's largest orthopaedic specialist trust running revision joint surgery, spinal surgery, sarcoma orthopaedics and complex paediatric orthopaedics — implant SKU heterogeneity is unusually high and write-downs reflect that diversity.",
        "beneficiaries": "RNOH serves national-level tertiary orthopaedic referrals from across England (c. 56M population reach for revision joint surgery, sarcoma, spinal cord injury, complex paeds); runs c. 220 inpatient beds across the Stanmore site plus the central London outpatient unit; c. 2,000 WTE clinical staff; performs c. 6,000 inpatient orthopaedic procedures/yr.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · NHS Supply Chain orthopaedic category framework · MHRA medical-device regulations",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.17M (£171,000)"},
            {"label": "Trust profile", "value": "England's largest specialist orthopaedic trust — Stanmore main campus + Bolsover Street outpatient + spinal cord injury centre"},
            {"label": "Bed base", "value": "c. 220 inpatient beds (Stanmore main + spinal injury centre)"},
            {"label": "Workforce", "value": "c. 2,000 WTE staff including world-leading orthopaedic surgeons"},
            {"label": "Catchment", "value": "National tertiary referrals — revision joints, sarcoma orthopaedics, spinal cord injury, complex paeds"},
            {"label": "Procedure volume", "value": "c. 6,000 inpatient orthopaedic procedures/yr; high-volume revision-arthroplasty workload"},
            {"label": "Inventory drivers", "value": "Implant heterogeneity (multiple manufacturers — Stryker, Smith+Nephew, Zimmer Biomet, DePuy Synthes); revision-specific stock; sarcoma custom implants"},
            {"label": "Write-down causes", "value": "NICE guidance change displacing implant generation; expiry; damage; product recall (rare)"},
            {"label": "Site constraint", "value": "1922 listed-buildings constraint at Stanmore — Stanmore Hospital Redevelopment Programme partial completion"},
            {"label": "Funding trajectory", "value": "Stable c. £150-200k; spike in years with major implant-generation displacement"},
            {"label": "Delivery body", "value": "RNOH Procurement + Theatres + Pharmacy + Sterile Services; counterparties include NHS Supply Chain orthopaedic tower + direct OEM contracts"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (D14 specialised orthopaedics + D15 spinal services) + DHSC + NHS Supply Chain"},
            {"label": "Evaluation evidence", "value": "RNOH Annual Report; CQC provider profile; National Joint Registry (NJR) outcomes; Getting It Right First Time (GIRFT) orthopaedic benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1907-founded Royal National Orthopaedic Hospital (Stanmore site since 1922) · Successor: Stanmore Hospital Redevelopment Programme phase 2 + national orthopaedic-network role"}
        ],
        "notes": "RNOH Stanmore is the largest orthopaedic specialist trust in England and one of the largest in Europe, with a national tertiary referral base for revision joint surgery, primary bone tumour (sarcoma) and spinal cord injury. The £171k inventories-written-down line reflects the unusually high implant-SKU heterogeneity that complex revision orthopaedics requires — multiple manufacturers, multiple generations, custom-fabricated sarcoma implants and bespoke spinal hardware. NICE Health Technology Appraisal updates (e.g. on hip resurfacing, on cementless arthroplasty for older patients) periodically displace older implant generations and drive write-down spikes. The 1922 listed-buildings constraint at Stanmore is being addressed via the Stanmore Hospital Redevelopment Programme.",
        "sources": [
            {"publisher": "Royal National Orthopaedic Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rnoh.nhs.uk/about-us/who-we-are/key-publications"},
            {"publisher": "Care Quality Commission", "title": "RNOH provider profile (RAN)", "url": "https://www.cqc.org.uk/provider/RAN"},
            {"publisher": "National Joint Registry", "title": "NJR Annual Report — implant outcomes", "url": "https://reports.njrcentre.org.uk/"},
            {"publisher": "Getting It Right First Time", "title": "GIRFT Orthopaedics National Specialty Report", "url": "https://gettingitrightfirsttime.co.uk/surgical_specialties/orthopaedic-surgery/"},
            {"publisher": "NHS Supply Chain", "title": "Orthopaedic category framework", "url": "https://www.supplychain.nhs.uk/categories/orthopaedics/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Royal National Orthopaedic Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Specialist Trusts", "Inventories written down — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "Inventories written down — Great Ormond Street Hospital for Children NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Amortisation — Hertfordshire Community NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Hertfordshire Community NHS Trust"}],
        "description": "HCT's £0.17M amortisation line is the IAS 38 charge against intangible assets — primarily clinical software (SystmOne community module, Liquidlogic, Oracle finance, ESR), software licences and any internally-generated software-development capitalisation amortising over a 3-5 year useful economic life. HCT delivers community nursing, children's services (0-19), MIUs and MSK community physio across the Hertfordshire and West Essex ICS footprint, so amortisation tracks the EPR + roster + finance digital stack rather than any physical-asset capital programme.",
        "beneficiaries": "Serves a c. 1.2M-population Hertfordshire catchment plus West Essex children's services overlap; runs c. 4 community hospitals (Cheshunt, Herts and Essex, Potters Bar, Queen Victoria Memorial), Children's Therapies and Universal Children's Services with c. 3,000 WTE staff visiting c. 200,000 patients/yr in homes and community clinics.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.17M (£169,000)"},
            {"label": "Trust scope", "value": "Community nursing + 0-19 Healthy Child Programme + MIUs + MSK physio + EoL care across Hertfordshire"},
            {"label": "Geographic footprint", "value": "Hertfordshire 1,643 km² + West Essex children's services overlap"},
            {"label": "Population served", "value": "c. 1.2M Hertfordshire residents + West Essex 0-19 service"},
            {"label": "Community hospitals", "value": "Cheshunt, Herts and Essex, Potters Bar, Queen Victoria Memorial — community-bed footprint"},
            {"label": "Workforce", "value": "c. 3,000 WTE community-health staff"},
            {"label": "Patient volume", "value": "c. 200,000 patients/yr across community + 0-19 services"},
            {"label": "Asset scope", "value": "Software intangibles — SystmOne, Liquidlogic children's case-management, ESR, Oracle ledger"},
            {"label": "EPR system", "value": "TPP SystmOne community module + Liquidlogic for 0-19 children's services"},
            {"label": "Funding trajectory", "value": "Stable c. £160-180k as software UEL amortises; growth tied to Three Shifts digital capex"},
            {"label": "Delivery body", "value": "HCT IT/Digital + Finance; vendors include TPP SystmOne, Liquidlogic, Oracle, IBM Cognos"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation + Hertfordshire & West Essex ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "HCT Annual Report; CQC provider profile; What Good Looks Like digital maturity assessments"},
            {"label": "Predecessor / successor", "value": "Predecessor: Hertfordshire PCT community arm pre-2011 TCS · Successor: Three Shifts community-digital lift + Single Patient Record convergence under HWE ICB"}
        ],
        "notes": "Hertfordshire Community NHS Trust is one of England's mid-size standalone community trusts, distinguished by the integrated 0-19 Healthy Child Programme delivered jointly with West Essex. The £169k amortisation reflects an IT-asset book dominated by SystmOne community-module licences, Liquidlogic children's case-management software, ESR HR/payroll and the Oracle finance ledger. Three Shifts policy direction (Darzi, Sep 2024) and NHSE Frontline Digitisation are likely to lift capitalised software spend over the medium term as community providers adopt shared digital platforms — particularly the Hertfordshire & West Essex Single Patient Record initiative under the ICB.",
        "sources": [
            {"publisher": "Hertfordshire Community NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hct.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Hertfordshire Community NHS Trust provider profile (RY4)", "url": "https://www.cqc.org.uk/provider/RY4"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Hertfordshire Community NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Lincolnshire Community Health Services NHS Trust", "Amortisation — Wirral Community Health and Care NHS Foundation Trust", "Transport (business + patient) — Hertfordshire Community NHS Trust"]
    },
    "Inventories written down — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "RJAH Oswestry's £0.16M inventories-written-down line is the IAS 2 charge for orthopaedic implants, prosthetics and surgical-supplies stock that has expired, become obsolete (e.g. NICE guidance change, manufacturer switch), been damaged or otherwise written off the inventory ledger. RJAH is a specialist orthopaedic trust running primary and revision joint surgery, paediatric orthopaedics, spinal surgery, sports medicine and the Midlands Centre for Spinal Injuries — implant heterogeneity drives write-down exposure even on a smaller scale than RNOH Stanmore.",
        "beneficiaries": "Serves the Welsh-borders + Shropshire + Cheshire orthopaedic catchment plus tertiary referrals from across the Midlands and North Wales (c. 5M reach for spinal injury); runs c. 200 inpatient beds across the rural Oswestry campus; c. 1,500 WTE clinical staff; performs c. 5,000 inpatient orthopaedic procedures/yr.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · NHS Supply Chain orthopaedic category framework · MHRA medical-device regulations",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.16M (£164,000)"},
            {"label": "Trust profile", "value": "Specialist orthopaedic trust — Oswestry rural campus + Midlands Centre for Spinal Injuries (MCSI)"},
            {"label": "Bed base", "value": "c. 200 inpatient beds across Oswestry main + spinal-injuries centre"},
            {"label": "Workforce", "value": "c. 1,500 WTE clinical staff"},
            {"label": "Catchment", "value": "Welsh borders + Shropshire + Cheshire + tertiary referrals from Midlands + North Wales"},
            {"label": "Procedure volume", "value": "c. 5,000 inpatient orthopaedic procedures/yr; revision and complex case mix"},
            {"label": "Inventory drivers", "value": "Implant heterogeneity (Stryker, Smith+Nephew, Zimmer Biomet, DePuy Synthes, Corin); spinal hardware; sports-medicine consumables"},
            {"label": "Write-down causes", "value": "NICE guidance change, expiry, damage, supplier consolidation, manufacturer recall"},
            {"label": "MCSI", "value": "Midlands Centre for Spinal Injuries — one of c. 11 UK SCI centres; specialised commissioning under NHSE D15"},
            {"label": "Funding trajectory", "value": "Stable c. £150-170k; spike in years with major NICE TA-driven implant displacement"},
            {"label": "Delivery body", "value": "RJAH Procurement + Theatres + Pharmacy; counterparties include NHS Supply Chain orthopaedic tower + direct OEM contracts"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (D14 specialised orthopaedics + D15 spinal services) + DHSC + NHS Supply Chain"},
            {"label": "Evaluation evidence", "value": "RJAH Annual Report; CQC provider profile; National Joint Registry outcomes; GIRFT orthopaedic benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: Robert Jones (1888) + Agnes Hunt (1900) founders' legacy hospital · Successor: ongoing Oswestry estate-renewal capital programme + national orthopaedic-network role"}
        ],
        "notes": "RJAH Oswestry is one of England's two standalone specialist orthopaedic trusts (with RNOH Stanmore) and one of the 11 UK Spinal Cord Injury Centres via the Midlands Centre for Spinal Injuries. The £164k inventories-written-down line reflects implant SKU heterogeneity across primary + revision joint surgery, paediatric orthopaedics and spinal hardware. NICE Health Technology Appraisal updates and supplier-consolidation events periodically displace older implant generations and drive write-down spikes. Despite its rural Oswestry location, RJAH commands tertiary referrals from across the Midlands and North Wales for complex orthopaedic and spinal-injury work.",
        "sources": [
            {"publisher": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rjah.nhs.uk/about-us/publications/annual-reports.aspx"},
            {"publisher": "Care Quality Commission", "title": "RJAH provider profile (RL1)", "url": "https://www.cqc.org.uk/provider/RL1"},
            {"publisher": "National Joint Registry", "title": "NJR Annual Report — implant outcomes", "url": "https://reports.njrcentre.org.uk/"},
            {"publisher": "Getting It Right First Time", "title": "GIRFT Orthopaedics National Specialty Report", "url": "https://gettingitrightfirsttime.co.uk/surgical_specialties/orthopaedic-surgery/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — Spinal services (D15)", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Specialist Trusts", "Inventories written down — Royal National Orthopaedic Hospital NHS Trust", "Inventories written down — Great Ormond Street Hospital for Children NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Other & adjustments — The Clatterbridge Cancer Centre NHS Foundation Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "The Clatterbridge Cancer Centre NHS Foundation Trust"}],
        "description": "Clatterbridge's £0.16M Staff Costs 'Other & adjustments' line is the residual catch-all in the IAS 19 staff-costs note covering recharges between trusts (e.g. SLA-based oncologist loans to/from neighbouring acute trusts), payroll reclassifications, accruals adjustments, prior-year corrections, IFRS 16 sub-let mileage and other minor staff-cost adjustments not captured under salaries, NIC, pension or termination headers. Clatterbridge is England's largest standalone cancer specialist trust running radiotherapy, systemic anti-cancer therapy (SACT) and a regional proton-beam pilot.",
        "beneficiaries": "Serves a c. 2.4M Cheshire & Merseyside cancer-treatment catchment plus tertiary referrals from across the North West for proton-beam therapy (one of two UK NHS PBT centres alongside The Christie); runs c. 110 inpatient beds across the new Liverpool Cancer Centre + Wirral campus + satellite radiotherapy hubs; c. 2,200 WTE clinical staff treating c. 33,000 patients/yr.",
        "legal_basis": "IAS 19 Employee Benefits · DHSC Group Accounting Manual 2024-25 staff-costs note · NHS Act 2006 · Health and Care Act 2022 · NHS Pension Scheme Regulations",
        "key_stats": [
            {"label": "Other & adjustments (Staff Costs) 2024-25", "value": "£0.16M (£155,257)"},
            {"label": "Trust profile", "value": "England's largest standalone cancer specialist trust — radiotherapy + SACT + one of two UK NHS proton-beam centres"},
            {"label": "Main sites", "value": "Liverpool Cancer Centre (opened 2020), Wirral Clatterbridge campus, Aintree + Halton + Macclesfield satellite radiotherapy hubs"},
            {"label": "Bed base", "value": "c. 110 inpatient cancer beds across Liverpool + Wirral campuses"},
            {"label": "Workforce", "value": "c. 2,200 WTE clinical + corporate staff"},
            {"label": "Patient volume", "value": "c. 33,000 cancer patients treated/yr (radiotherapy + SACT + brachytherapy)"},
            {"label": "Catchment", "value": "c. 2.4M Cheshire & Merseyside residents + tertiary PBT referrals nationally"},
            {"label": "Recharge complexity", "value": "Joint clinical posts with Liverpool University Hospitals + Wirral University Teaching Hospital; SLA-based oncologist time"},
            {"label": "Adjustment scope", "value": "Inter-trust SLA recharges, prior-year payroll corrections, IFRS 16 immaterial adjustments, accrual true-ups"},
            {"label": "Funding trajectory", "value": "Volatile c. £100-200k year-on-year depending on inter-trust recharge volume + prior-year corrections"},
            {"label": "Delivery body", "value": "Clatterbridge Finance + HR + Payroll (NHS SBS); inter-trust counterparties include LUFT, WUTH, Aintree"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (B01 chemotherapy + B02 radiotherapy + B03 PBT) + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Clatterbridge Annual Report; CQC provider profile (Outstanding); NHSE Cancer Dashboard; National Cancer Audit Programme"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1958-founded Clatterbridge Hospital + 2020 Liverpool Cancer Centre opening · Successor: ongoing PBT capacity expansion + Cheshire & Merseyside cancer-network consolidation"}
        ],
        "notes": "Clatterbridge is England's largest standalone cancer specialist trust and one of only two UK NHS proton-beam therapy centres (alongside The Christie). The 2020 opening of the new Liverpool Cancer Centre on the Royal Liverpool Hospital campus added a second major site to the historical Wirral Clatterbridge base, increasing inter-trust SLA complexity for joint oncology posts shared with Liverpool University Hospitals and Wirral University Teaching Hospital. The £155k 'Other & adjustments' line catches the residue of these inter-trust recharge flows plus prior-year corrections and minor IFRS 16 staff-cost reclassifications. This line is structurally volatile year-to-year.",
        "sources": [
            {"publisher": "The Clatterbridge Cancer Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.clatterbridgecc.nhs.uk/about-us/publications/annual-report"},
            {"publisher": "Care Quality Commission", "title": "Clatterbridge provider profile (REN)", "url": "https://www.cqc.org.uk/provider/REN"},
            {"publisher": "NHS England", "title": "Specialised commissioning — Cancer (B01-B03)", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS England", "title": "Cancer Dashboard and Operational Standards", "url": "https://www.england.nhs.uk/cancer/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — Staff Costs", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Clatterbridge Cancer Centre NHS Foundation Trust", "Staff Costs", "NHS Specialist Trusts", "Other & adjustments — South Western Ambulance Service NHS Foundation Trust", "Social security & levy — The Clatterbridge Cancer Centre NHS Foundation Trust", "Amortisation — The Clatterbridge Cancer Centre NHS Foundation Trust"]
    },
    "Termination & post-employment — The Walton Centre NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "The Walton Centre NHS Foundation Trust"}],
        "description": "Walton Centre's £0.15M termination & post-employment line is the IAS 19 charge for redundancy payments, voluntary-severance settlements (e.g. Mutually Agreed Resignation Scheme), pay-in-lieu of notice and post-employment benefit movements (excluding NHS Pension Scheme regular contributions which sit in Social security & levy / Pensions). For a c. 1,800-WTE single-campus specialist neurology trust, this line is small and reflects modest annual restructuring activity governed by the NHS Pension Scheme regulations and Public Sector Exit Payments Regulations 2020.",
        "beneficiaries": "Funds exit settlements affecting a small number of staff per year out of c. 1,800 WTE Walton Centre workforce; serves the c. 3.4M-population Cheshire & Merseyside neuroscience catchment via consultants, neurosurgeons, neurology nurses and AHPs based at Lower Lane Fazakerley.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2015 · Public Sector Exit Payments Regulations 2020 · Restriction of Public Sector Exit Payments Regulations 2020 (£95k cap, since revoked) · DHSC GAM 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.15M (£153,000)"},
            {"label": "Trust profile", "value": "England's only standalone neurology + neurosurgery specialist trust"},
            {"label": "Workforce baseline", "value": "c. 1,800 WTE staff"},
            {"label": "Main site", "value": "Lower Lane, Fazakerley, Liverpool — co-located with Aintree University Hospital"},
            {"label": "Catchment", "value": "c. 3.4M Cheshire & Merseyside resident population + tertiary referrals from N Wales, IoM, Lancs"},
            {"label": "Termination scope", "value": "Voluntary redundancy, MARS settlements, payment in lieu of notice, contractual termination payments"},
            {"label": "Post-employment", "value": "Movements in NHS Pension early-retirement provisions, ill-health retirement top-ups (employer share)"},
            {"label": "Exit-pay regulation", "value": "Public Sector Exit Payments Regs 2020 (£95k cap) revoked Feb 2021 following legal challenge; HM Treasury guidance still applies"},
            {"label": "Funding trajectory", "value": "Volatile c. £50-200k year-on-year depending on restructuring activity; spike years align with service redesign"},
            {"label": "Delivery body", "value": "Walton Centre HR + Finance + NHS Pensions Agency; counterparty NHS Business Services Authority"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (exit-pay framework) + NHSE Workforce + NHS Pensions Agency"},
            {"label": "Evaluation evidence", "value": "Walton Centre Annual Report (note 8 staff costs); NAO Public Sector Exit Payments report; ONS workforce statistics"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2020 PSEP £95k cap (revoked Feb 2021) · Successor: HM Treasury exit-pay reform consultation pending"}
        ],
        "notes": "Walton Centre's termination line is small in cash terms but is a closely-watched accounting area given the political sensitivity of NHS exit packages. The 2020 Public Sector Exit Payments Regulations introduced a £95k cap that was revoked in February 2021 following judicial review and union legal challenge — HM Treasury guidance still applies to exit packages above £95k requiring approval, and the NHS Confederation publishes annual exit-payment data per ARA. Walton's small c. 1,800 WTE workforce means restructuring activity is modest and year-on-year volatility is structural rather than indicative of strategic change.",
        "sources": [
            {"publisher": "The Walton Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24 (Note 8 Staff Costs)", "url": "https://www.thewaltoncentre.nhs.uk/238/about-us.html"},
            {"publisher": "HM Treasury", "title": "Public Sector Exit Payments — guidance", "url": "https://www.gov.uk/government/publications/exit-payments-guidance-for-the-public-sector"},
            {"publisher": "National Audit Office", "title": "Investigation into government's actions on Public Sector Exit Payments", "url": "https://www.nao.org.uk/"},
            {"publisher": "NHS Business Services Authority — NHS Pensions", "title": "NHS Pension Scheme Regulations and ill-health retirement", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Walton Centre NHS Foundation Trust", "Staff Costs", "NHS Specialist Trusts", "Termination & post-employment — Derbyshire Community Health Services NHS Foundation Trust", "Social security & levy — The Walton Centre NHS Foundation Trust", "NHS Business Services Authority"]
    },
    "Amortisation — The Christie NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Christie NHS Foundation Trust"}],
        "description": "The Christie's £0.15M amortisation line is the IAS 38 charge against intangible assets — primarily clinical software (Aria oncology information system, ESR HR/payroll, Oracle finance, Mosaiq radiotherapy planning) and internally-generated software-development capitalisation. The Christie is the largest single-site cancer centre in Europe and one of two UK NHS proton-beam therapy hosts (alongside Clatterbridge Liverpool); intangibles capitalisation reflects oncology-specific clinical IT plus the Christie Charity-funded research-systems estate.",
        "beneficiaries": "Serves a c. 3.2M Greater Manchester + Cheshire cancer-treatment catchment plus tertiary referrals from across the North West and nationally for proton-beam therapy + CAR-T cell therapy + advanced radiotherapy techniques; runs c. 240 inpatient beds across the Withington (Manchester) main site; c. 3,500 WTE staff treating c. 60,000 patients/yr.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.15M (£148,970)"},
            {"label": "Trust profile", "value": "Largest single-site cancer centre in Europe; one of two UK NHS proton-beam therapy centres (alongside UCLH/Clatterbridge group)"},
            {"label": "Main site", "value": "Withington, Manchester — Christie Hospital main campus + Christie at Macclesfield + Christie at Salford radiotherapy hubs"},
            {"label": "Bed base", "value": "c. 240 inpatient cancer beds at Withington"},
            {"label": "Workforce", "value": "c. 3,500 WTE clinical + corporate staff"},
            {"label": "Patient volume", "value": "c. 60,000 cancer patients treated/yr (radiotherapy + SACT + brachytherapy + PBT + CAR-T)"},
            {"label": "Catchment", "value": "c. 3.2M Greater Manchester + East Cheshire + tertiary referrals nationally"},
            {"label": "Asset scope", "value": "Software intangibles — Aria oncology info system, Mosaiq radiotherapy planning, ESR, Oracle finance, internally-developed research software"},
            {"label": "EPR/Oncology IT", "value": "Aria (Varian) + Mosaiq (Elekta) for radiotherapy + chemotherapy management; bespoke research analytics under Christie Charity funding"},
            {"label": "Funding trajectory", "value": "Stable c. £130-170k as software UEL amortises over 3-5 years; growth tied to Frontline Digitisation capex"},
            {"label": "Delivery body", "value": "Christie IT/Digital + Finance; vendors include Varian, Elekta, Oracle, IBM, Christie Charity research-systems team"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (B01-B03 cancer + B03 PBT) + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Christie Annual Report; CQC provider profile (Outstanding); NHSE Cancer Dashboard; NCRAS national cancer outcomes"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1901-founded Christie Hospital + Holt Radium Institute · Successor: ongoing Christie Charity-funded research expansion + PBT-2 capacity"}
        ],
        "notes": "The Christie's amortisation line tracks an IT-asset book heavily oriented towards oncology-specific clinical systems — Varian Aria oncology information system + Elekta Mosaiq radiotherapy planning + bespoke research-analytics software funded in part by The Christie Charity (one of England's largest hospital charities). The Christie is structurally distinguished from other specialist trusts by the depth of charity-funded research infrastructure that flows through both capital and operating budgets. Frontline Digitisation programme funding is expected to lift capitalised software spend medium-term as the trust converges with Greater Manchester ICB shared digital infrastructure.",
        "sources": [
            {"publisher": "The Christie NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.christie.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "The Christie provider profile (RBV)", "url": "https://www.cqc.org.uk/provider/RBV"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — Cancer (B01-B03)", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Christie NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Amortisation — The Royal Marsden NHS Foundation Trust", "Amortisation — The Clatterbridge Cancer Centre NHS Foundation Trust", "Social security & levy — The Christie NHS Foundation Trust"]
    },
    "Inventories written down — South Western Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "South Western Ambulance Service NHS Foundation Trust"}],
        "description": "SWASFT's £0.15M inventories-written-down line is the IAS 2 charge for ambulance consumables — single-use airway/ventilation kit, dressings, IV cannulae and giving sets, bandages, pre-filled emergency drug syringes, defibrillator pads, vehicle-fit oxygen consumables and PPE — that have expired, been damaged or otherwise written off the inventory ledger. Across c. 950 emergency vehicles operating from c. 90 stations and Make Ready Centres across the South West, expiry-driven write-downs are a structural cost.",
        "beneficiaries": "Serves a c. 5.5M-resident South West catchment plus c. 23M annual visitor-days summer surge across Cornwall, Devon, Dorset, Somerset, Wiltshire, Bristol, Gloucestershire and the Isles of Scilly; SWASFT responds to c. 1.0M 999 calls/yr with c. 5,000 WTE staff including c. 3,500 frontline paramedics + EMTs.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · MHRA medical-device regulations · NHS Supply Chain ambulance category · JRCALC clinical guidelines",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.15M (£146,000)"},
            {"label": "Trust profile", "value": "Regional ambulance trust covering largest English geographic ambulance footprint"},
            {"label": "Geographic footprint", "value": "c. 25,000 km² — c. 20% of England's land area"},
            {"label": "Fleet scale", "value": "c. 950 emergency vehicles across c. 90 stations + Make Ready Centres"},
            {"label": "999 call volume", "value": "c. 1.0M emergency calls/yr"},
            {"label": "Population + tourist spike", "value": "c. 5.5M residents + c. 23M visitor-days/yr summer surge"},
            {"label": "Workforce", "value": "c. 5,000 WTE; c. 3,500 frontline clinicians"},
            {"label": "Inventory drivers", "value": "Single-use airway kit, IV consumables, dressings, defib pads, pre-filled drug syringes, oxygen consumables, PPE"},
            {"label": "Write-down causes", "value": "Expiry (vehicle-stocked drugs/consumables turn over slowly outside Cat-1 hot zones), damage (vehicle accidents), JRCALC guideline change"},
            {"label": "Make Ready Centre rotation", "value": "MRC vehicle prep model rotates consumables across the fleet to manage expiry exposure"},
            {"label": "Funding trajectory", "value": "Stable c. £140-160k; pandemic-era PPE expiry drove higher write-downs 2022-23"},
            {"label": "Delivery body", "value": "SWASFT Procurement + Make Ready Centres + clinical leads; counterparty NHS Supply Chain ambulance category framework"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care + DHSC + South West ICBs + JRCALC"},
            {"label": "Evaluation evidence", "value": "SWASFT Annual Report; AACE benchmarking; NAO Ambulance Services report; ORH benchmarking"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 Westcountry + Avon ambulance services + 2013 GWAS merger · Successor: ongoing JRCALC formulary updates + drug-pack standardisation"}
        ],
        "notes": "Ambulance consumables write-down is structurally driven by the tension between Cat-1 readiness (every vehicle must carry a full drug + consumables pack at all times) and slow per-vehicle turnover outside hot dispatch zones. SWASFT's geographic spread across rural South West means many station-stocked drug packs sit at lower turnover than urban LAS or NWAS hot vehicles, raising expiry exposure. The Make Ready Centre model partially mitigates by rotating stock across the fleet. Pandemic-era PPE expiry (2020-22 stockpile turn-over) drove an elevated write-down 2022-23 that has since normalised. JRCALC clinical guideline updates periodically retire drug formularies and drive write-down spikes.",
        "sources": [
            {"publisher": "South Western Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swast.nhs.uk/about-us/freedom-of-information/publications/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "SWASFT provider profile (RYF)", "url": "https://www.cqc.org.uk/provider/RYF"},
            {"publisher": "Joint Royal Colleges Ambulance Liaison Committee", "title": "JRCALC Clinical Practice Guidelines", "url": "https://aace.org.uk/clinical-practice-guidelines/"},
            {"publisher": "NHS Supply Chain", "title": "Ambulance category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["South Western Ambulance Service NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Ambulance Trusts", "Other & adjustments — South Western Ambulance Service NHS Foundation Trust", "General supplies & services — South Western Ambulance Service NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Other & adjustments — South Western Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "South Western Ambulance Service NHS Foundation Trust"}],
        "description": "SWASFT's £0.14M Staff Costs 'Other & adjustments' line is the residual catch-all in the IAS 19 staff-costs note covering inter-trust SLA recharges (e.g. cross-border ambulance support with NEAS for Scilly transfers, with WAST for Welsh-borders), prior-year payroll corrections, accruals adjustments, IFRS 16 immaterial reclassifications and other minor staff-cost items not captured under salaries, NIC, pension or termination headers. SWASFT's c. 5,000-WTE rural ambulance workforce generates a small year-end residue of these adjustments.",
        "beneficiaries": "Affects the c. 5,000 WTE SWASFT workforce + cross-border SLA partners (Welsh Ambulance Service Trust, Devon Air Ambulance, Cornwall Air Ambulance, Dorset & Somerset Air Ambulance via HEMS partnership); operational service reaches c. 5.5M residents + c. 23M visitor-days/yr seasonal surge across the South West.",
        "legal_basis": "IAS 19 Employee Benefits · DHSC Group Accounting Manual 2024-25 staff-costs note · NHS Act 2006 · NHS Pension Scheme Regulations · Health and Care Act 2022",
        "key_stats": [
            {"label": "Other & adjustments (Staff Costs) 2024-25", "value": "£0.14M (£142,000)"},
            {"label": "Trust profile", "value": "Regional ambulance trust — largest English geographic ambulance footprint"},
            {"label": "Workforce", "value": "c. 5,000 WTE; c. 3,500 frontline clinicians"},
            {"label": "Population + tourist spike", "value": "c. 5.5M residents + c. 23M visitor-days/yr summer surge"},
            {"label": "999 call volume", "value": "c. 1.0M emergency calls/yr"},
            {"label": "Cross-border SLAs", "value": "Welsh Ambulance Service Trust (Welsh-borders), Cornwall Air Ambulance + Devon Air Ambulance + Dorset & Somerset Air Ambulance (HEMS partnerships), NHSE 111 South West"},
            {"label": "Adjustment scope", "value": "Inter-trust SLA recharges, prior-year payroll corrections, accrual true-ups, IFRS 16 staff-cost reclassifications, IoS-specific transfers"},
            {"label": "111 service", "value": "SWASFT operates the South West NHS 111 contract — staff-cost interface with the ambulance service line"},
            {"label": "Funding trajectory", "value": "Volatile c. £100-200k year-on-year depending on inter-trust recharge volume + prior-year corrections"},
            {"label": "Delivery body", "value": "SWASFT Finance + HR + Payroll (NHS SBS); inter-trust counterparties WAST, NEAS, NHSE 111 SW"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care + DHSC + South West ICBs (Cornwall + IoS · Devon · Dorset · Somerset · BNSSG · BSW · Glos)"},
            {"label": "Evaluation evidence", "value": "SWASFT Annual Report (Note 8); AACE benchmarking; CQC inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2013 GWAS merger absorbing Avon + Glos + Wilts · Successor: ongoing 111 + 999 integration model + cross-border SLA simplification"}
        ],
        "notes": "SWASFT operates the South West NHS 111 contract alongside the 999 ambulance service, which adds inter-line staff-cost reclassifications between the 111 cost centre and ambulance staff cost centre at year-end. The £142k 'Other & adjustments' line catches these inter-line and inter-trust SLA recharge residues plus prior-year payroll corrections and IFRS 16 immaterial reclassifications. The 2013 merger that absorbed Great Western Ambulance Service (Avon, Gloucestershire, Wiltshire) into SWASFT consolidated payroll but kept some legacy SLA arrangements live. This line is structurally volatile year-to-year.",
        "sources": [
            {"publisher": "South Western Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24 (Note 8 Staff Costs)", "url": "https://www.swast.nhs.uk/about-us/freedom-of-information/publications/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "SWASFT provider profile (RYF)", "url": "https://www.cqc.org.uk/provider/RYF"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report and ambulance benchmarking", "url": "https://aace.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — Staff Costs", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["South Western Ambulance Service NHS Foundation Trust", "Staff Costs", "NHS Ambulance Trusts", "Inventories written down — South Western Ambulance Service NHS Foundation Trust", "Social security & levy — South Western Ambulance Service NHS Foundation Trust", "Other & adjustments — The Clatterbridge Cancer Centre NHS Foundation Trust"]
    },
    "Amortisation — Wirral Community Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Wirral Community Health and Care NHS Foundation Trust"}],
        "description": "WCHC's £0.14M amortisation line is the IAS 38 charge against intangible assets — primarily clinical software (TPP SystmOne community module, ESR HR/payroll, Oracle finance) and any internally-generated software-development capitalisation amortising over a 3-5 year useful economic life. WCHC delivers district nursing, school nursing, MSK community physiotherapy and 0-19 services across the Wirral peninsula plus Cheshire West & Chester children's overlap, so amortisation tracks the EPR + roster + finance digital stack.",
        "beneficiaries": "Serves a c. 320,000-resident Wirral peninsula catchment plus Cheshire West & Chester 0-19 service overlap; runs district nursing, health visiting, school nursing, MSK community physio and end-of-life care with c. 1,500 WTE staff visiting c. 138,000 households + c. 60 schools.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.14M (£138,365)"},
            {"label": "Trust scope", "value": "Community provider — DN, HV, school nursing, MSK physio, EoL care across Wirral + CWAC 0-19"},
            {"label": "Geographic footprint", "value": "Wirral peninsula c. 157 km² + CWAC 0-19 service overlap"},
            {"label": "Population served", "value": "c. 320,000 Wirral residents + 0-19 service for CWAC"},
            {"label": "Workforce", "value": "c. 1,500 WTE — predominantly community-facing nurses + AHPs"},
            {"label": "Visit volume", "value": "c. 138,000 Wirral households + c. 60 schools served"},
            {"label": "Asset scope", "value": "Software intangibles — SystmOne community module, ESR, Oracle finance, internally-developed digital tools"},
            {"label": "EPR system", "value": "TPP SystmOne community module — primary clinical record (shared with Wirral GP federation)"},
            {"label": "Funding trajectory", "value": "Stable c. £130-150k as software UEL amortises; growth tied to Cheshire & Mersey ICB digital convergence + Three Shifts capex"},
            {"label": "Delivery body", "value": "WCHC IT/Digital + Finance; vendors include TPP SystmOne, Oracle, IBM Cognos"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation + Cheshire & Merseyside ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "WCHC Annual Report; CQC provider profile (Outstanding); What Good Looks Like digital maturity"},
            {"label": "Predecessor / successor", "value": "Predecessor: Wirral PCT community arm pre-2011 TCS · Successor: Three Shifts community-digital lift + Cheshire & Mersey ICB Single Patient Record"}
        ],
        "notes": "WCHC's amortisation line tracks an IT-asset book dominated by SystmOne community-module licences (shared with Wirral primary care), ESR HR/payroll, the Oracle finance ledger and small internally-developed digital tools. WCHC earned an Outstanding CQC rating overall in 2018 — one of relatively few community trusts to do so. Three Shifts policy direction (Darzi report, Sep 2024) and NHSE Frontline Digitisation are likely to lift capitalised software spend medium-term as the trust converges with the Cheshire & Merseyside ICB Single Patient Record initiative. April 2025 NIC step-up does not directly affect this line but compresses overall trust capex headroom.",
        "sources": [
            {"publisher": "Wirral Community Health and Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wchc.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "WCHC provider profile (RY7)", "url": "https://www.cqc.org.uk/provider/RY7"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Wirral Community Health and Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Hertfordshire Community NHS Trust", "Amortisation — Lincolnshire Community Health Services NHS Trust", "Transport (business + patient) — Wirral Community Health and Care NHS Foundation Trust"]
    },
    "Other & adjustments — Cambridgeshire Community Services NHS Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "Cambridgeshire Community Services NHS Trust"}],
        "description": "CCS's £0.14M Staff Costs 'Other & adjustments' line is the residual catch-all in the IAS 19 staff-costs note covering inter-trust SLA recharges, prior-year payroll corrections, accruals adjustments, IFRS 16 immaterial reclassifications and other minor staff-cost items not captured under salaries, NIC, pension or termination headers. CCS delivers community nursing, children's services, public health and dental services across Cambridgeshire, Peterborough, Bedfordshire, Luton, Norfolk, Suffolk and Hertfordshire — multi-county footprint generates structural inter-trust recharge complexity.",
        "beneficiaries": "Serves community + children's services across c. 2.5M residents in Cambridgeshire + Peterborough + Beds + Luton + parts of Norfolk + Suffolk + Herts; runs c. 4,000 WTE staff delivering district nursing, health visiting, school nursing, public health nursing, dental services, looked-after children services and prison healthcare.",
        "legal_basis": "IAS 19 Employee Benefits · DHSC Group Accounting Manual 2024-25 staff-costs note · NHS Act 2006 · NHS Pension Scheme Regulations · Health and Care Act 2022",
        "key_stats": [
            {"label": "Other & adjustments (Staff Costs) 2024-25", "value": "£0.14M (£137,000)"},
            {"label": "Trust scope", "value": "Multi-county community + children's + public health + dental + prison-healthcare provider"},
            {"label": "Geographic footprint", "value": "Cambridgeshire + Peterborough + Beds + Luton + parts of Norfolk + Suffolk + Herts"},
            {"label": "Population served", "value": "c. 2.5M aggregated catchment across multiple ICBs"},
            {"label": "Workforce", "value": "c. 4,000 WTE community + children's + dental + prison-health staff"},
            {"label": "Service breadth", "value": "DN, HV, school nursing, 0-19 Healthy Child Programme, dental services, public health nursing, prison healthcare"},
            {"label": "Multi-ICB complexity", "value": "Contracts with multiple ICBs (BLMK · CPICB · Norfolk & Waveney · Suffolk & NE Essex · Herts & W Essex) drive SLA recharge volume"},
            {"label": "Adjustment scope", "value": "Inter-ICB SLA recharges, prior-year payroll corrections, accrual true-ups, IFRS 16 staff-cost reclassifications"},
            {"label": "Funding trajectory", "value": "Volatile c. £100-180k year-on-year depending on inter-ICB recharge volume + prior-year corrections"},
            {"label": "Delivery body", "value": "CCS Finance + HR + Payroll (NHS SBS); inter-trust counterparties Cambridgeshire & Peterborough NHSFT, Hinchingbrooke, Bedfordshire Hospitals NHSFT"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + multiple ICBs (BLMK, CPICB, Norfolk & Waveney etc.)"},
            {"label": "Evaluation evidence", "value": "CCS Annual Report (Note 8); CQC provider profile; NHSE Operational Plan returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: Cambridgeshire PCT community arm pre-2011 TCS · Successor: Three Shifts community-care lift + multi-ICB SLA simplification"}
        ],
        "notes": "CCS is one of England's most geographically-distributed community trusts, delivering services across multiple counties and ICB footprints. This multi-ICB structure drives unusual SLA-recharge complexity at year-end, with inter-trust and inter-ICB payroll reconciliations flowing through this 'Other & adjustments' line alongside prior-year corrections and IFRS 16 immaterial reclassifications. CCS also operates HMP Peterborough and HMP Whitemoor prison healthcare, which adds another distinct staff-cost cohort with separate commissioning. The line is structurally volatile year-to-year and reflects the trust's atypical multi-ICB footprint.",
        "sources": [
            {"publisher": "Cambridgeshire Community Services NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cambscommunityservices.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "CCS provider profile (RYV)", "url": "https://www.cqc.org.uk/provider/RYV"},
            {"publisher": "NHS England", "title": "Operational Planning and Contracting Guidance", "url": "https://www.england.nhs.uk/publication/operational-planning-and-contracting-guidance/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — Staff Costs", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Cambridgeshire Community Services NHS Trust", "Staff Costs", "NHS Community Trusts", "Other & adjustments — Central London Community Healthcare NHS Trust", "Other & adjustments — Bridgewater Community Healthcare NHS Foundation Trust", "Social security & levy — Cambridgeshire Community Services NHS Trust"]
    },
    "Other & adjustments — Central London Community Healthcare NHS Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "Central London Community Healthcare NHS Trust"}],
        "description": "CLCH's £0.13M Staff Costs 'Other & adjustments' line is the residual catch-all in the IAS 19 staff-costs note covering inter-trust SLA recharges, prior-year payroll corrections, accruals adjustments, IFRS 16 immaterial reclassifications and other minor staff-cost items. CLCH is one of England's largest community trusts by revenue, delivering district nursing, health visiting, MSK community physio, MIUs and walk-in centres across central, north and west London plus Hertfordshire — multi-borough London weighting and ICB footprint complexity drive structural year-end adjustments.",
        "beneficiaries": "Serves community + walk-in services across c. 2M residents in Westminster, Kensington & Chelsea, Hammersmith & Fulham, Brent, Barnet, Wandsworth, Merton plus Hertfordshire children's services; runs c. 3,500 WTE staff including district nurses, health visitors, school nurses, MSK physios + MIU clinicians.",
        "legal_basis": "IAS 19 Employee Benefits · DHSC Group Accounting Manual 2024-25 staff-costs note · NHS Act 2006 · NHS Pension Scheme Regulations · Health and Care Act 2022",
        "key_stats": [
            {"label": "Other & adjustments (Staff Costs) 2024-25", "value": "£0.13M (£131,000)"},
            {"label": "Trust scope", "value": "Multi-borough London community provider — DN, HV, school nursing, MSK physio, MIUs, walk-in centres"},
            {"label": "Geographic footprint", "value": "Inner + Outer London (W&C, K&C, H&F, Brent, Barnet, Wandsworth, Merton) + Herts children's overlap"},
            {"label": "Population served", "value": "c. 2M residents across c. 7 London boroughs + Herts children's services"},
            {"label": "Workforce", "value": "c. 3,500 WTE community-health staff + MIU clinicians"},
            {"label": "London weighting", "value": "HCA Inner London + Outer London supplements lift base pay-bill — flows through staff-cost adjustments"},
            {"label": "Multi-ICB complexity", "value": "NW London ICB + NC London ICB + SW London ICB + Herts & W Essex ICB contracts"},
            {"label": "Adjustment scope", "value": "Inter-trust SLA recharges, prior-year payroll corrections, accrual true-ups, IFRS 16 staff-cost reclassifications"},
            {"label": "Funding trajectory", "value": "Volatile c. £100-180k year-on-year depending on inter-ICB recharge volume + prior-year corrections"},
            {"label": "Delivery body", "value": "CLCH Finance + HR + Payroll (NHS SBS); inter-trust counterparties Imperial, CNWL, RBKC GP federation"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + multiple London ICBs (NWL, NCL, SWL) + HWE ICB"},
            {"label": "Evaluation evidence", "value": "CLCH Annual Report (Note 8); CQC provider profile; NHSE Operational Plan returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2011 TCS-era merger of multiple London PCT community arms · Successor: Three Shifts community-care lift + ICB SLA simplification"}
        ],
        "notes": "CLCH is one of England's largest community trusts by revenue and is unusual for spanning multiple London ICB footprints (NW London, NC London, SW London) plus an out-of-region Hertfordshire children's services contract. This multi-ICB London-weighted structure drives unusual SLA-recharge and payroll-adjustment volume at year-end. The £131k 'Other & adjustments' line catches these inter-ICB and inter-trust payroll reconciliations alongside prior-year corrections and IFRS 16 immaterial reclassifications. CLCH was created through the 2011 Transforming Community Services consolidation of multiple London PCT community arms.",
        "sources": [
            {"publisher": "Central London Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://clch.nhs.uk/about-us/our-publications"},
            {"publisher": "Care Quality Commission", "title": "CLCH provider profile (RYX)", "url": "https://www.cqc.org.uk/provider/RYX"},
            {"publisher": "NHS England", "title": "Operational Planning and Contracting Guidance", "url": "https://www.england.nhs.uk/publication/operational-planning-and-contracting-guidance/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — Staff Costs", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Central London Community Healthcare NHS Trust", "Staff Costs", "NHS Community Trusts", "Other & adjustments — Cambridgeshire Community Services NHS Trust", "Other & adjustments — Bridgewater Community Healthcare NHS Foundation Trust", "Social security & levy — Central London Community Healthcare NHS Trust"]
    },
    "Other & adjustments — Bridgewater Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "Bridgewater Community Healthcare NHS Foundation Trust"}],
        "description": "Bridgewater's £0.12M Staff Costs 'Other & adjustments' line is the residual catch-all in the IAS 19 staff-costs note covering inter-trust SLA recharges, prior-year payroll corrections, accruals adjustments, IFRS 16 immaterial reclassifications and minor staff-cost items not captured elsewhere. Bridgewater delivers community nursing, dental services, MSK community physio and 0-19 services across Halton, Warrington, St Helens, parts of Cheshire and Wigan — multi-Place footprint within Cheshire & Merseyside ICB plus Greater Manchester ICB drives structural inter-trust recharge volume.",
        "beneficiaries": "Serves community + dental + 0-19 services across c. 1M residents in Halton, Warrington, St Helens, parts of Cheshire and Wigan; runs c. 1,800 WTE staff including district nurses, health visitors, school nurses, dental nurses + MSK physios.",
        "legal_basis": "IAS 19 Employee Benefits · DHSC Group Accounting Manual 2024-25 staff-costs note · NHS Act 2006 · NHS Pension Scheme Regulations · Health and Care Act 2022",
        "key_stats": [
            {"label": "Other & adjustments (Staff Costs) 2024-25", "value": "£0.12M (£117,000)"},
            {"label": "Trust scope", "value": "Multi-Place community + dental + 0-19 + MSK physio provider across NW England"},
            {"label": "Geographic footprint", "value": "Halton, Warrington, St Helens, parts of Cheshire, Wigan — straddles Cheshire & Merseyside ICB + GM ICB"},
            {"label": "Population served", "value": "c. 1M aggregated catchment across multiple Places"},
            {"label": "Workforce", "value": "c. 1,800 WTE — community nurses + dental nurses + AHPs + 0-19 staff"},
            {"label": "Service breadth", "value": "DN, HV, school nursing, 0-19 Healthy Child Programme, dental services, MSK community physio, public health nursing"},
            {"label": "Multi-ICB complexity", "value": "Cheshire & Merseyside ICB (Halton, Warrington, St Helens) + GM ICB (Wigan) contracts drive SLA recharge volume"},
            {"label": "Adjustment scope", "value": "Inter-Place SLA recharges, prior-year payroll corrections, accrual true-ups, IFRS 16 staff-cost reclassifications"},
            {"label": "Funding trajectory", "value": "Volatile c. £80-150k year-on-year depending on inter-Place recharge volume + prior-year corrections"},
            {"label": "Delivery body", "value": "Bridgewater Finance + HR + Payroll (NHS SBS); inter-trust counterparties Mersey Care, WWL, St Helens & Knowsley"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + Cheshire & Merseyside ICB + GM ICB"},
            {"label": "Evaluation evidence", "value": "Bridgewater Annual Report (Note 8); CQC provider profile; NHSE Operational Plan returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2011 TCS-era merger of NW PCT community arms · Successor: Three Shifts community-care lift + Cheshire & Mersey ICB SLA simplification"}
        ],
        "notes": "Bridgewater is structurally distinguished by its straddle of the Cheshire & Merseyside ICB / Greater Manchester ICB boundary, with services in Halton, Warrington, St Helens (C&M) plus Wigan (GM). This multi-ICB structure drives inter-Place SLA-recharge complexity at year-end alongside the conventional prior-year payroll corrections and IFRS 16 immaterial reclassifications captured in this 'Other & adjustments' line. Bridgewater also delivers high-volume dental services across the North West, adding another distinct staff-cost cohort with its own NHSE Dental contract terms. The line is structurally volatile year-to-year.",
        "sources": [
            {"publisher": "Bridgewater Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bridgewater.nhs.uk/about-us/news-and-publications/publications/"},
            {"publisher": "Care Quality Commission", "title": "Bridgewater provider profile (RY2)", "url": "https://www.cqc.org.uk/provider/RY2"},
            {"publisher": "NHS England", "title": "Operational Planning and Contracting Guidance", "url": "https://www.england.nhs.uk/publication/operational-planning-and-contracting-guidance/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — Staff Costs", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Bridgewater Community Healthcare NHS Foundation Trust", "Staff Costs", "NHS Community Trusts", "Other & adjustments — Central London Community Healthcare NHS Trust", "Other & adjustments — Cambridgeshire Community Services NHS Trust", "Social security & levy — Bridgewater Community Healthcare NHS Foundation Trust"]
    },
    "Transport (business + patient) — The Royal Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Royal Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "ROH Birmingham's £0.12M transport line covers AMAP staff mileage, pool-car running costs, vehicle leasing under IFRS 16, patient-transport-services interface costs and minor consumables (tyres, fuel, breakdown recovery) for the Bristol Road, Northfield, Birmingham campus. ROH is one of England's specialist orthopaedic trusts, delivering primary and revision joint surgery, paediatric orthopaedics, sarcoma orthopaedics, sports medicine and complex spinal work — single-campus footprint keeps the transport line small versus geographically-distributed acute trusts.",
        "beneficiaries": "Serves the West Midlands orthopaedic catchment plus tertiary referrals from across the Midlands and beyond (c. 6M reach for sarcoma orthopaedics + complex revision); runs c. 130 inpatient beds across the Bristol Road site; c. 1,200 WTE clinical staff; performs c. 4,500 inpatient orthopaedic procedures/yr.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.12M (£115,000)"},
            {"label": "Trust profile", "value": "Specialist orthopaedic trust — Bristol Road, Northfield, Birmingham single-campus"},
            {"label": "Bed base", "value": "c. 130 inpatient orthopaedic beds"},
            {"label": "Workforce", "value": "c. 1,200 WTE clinical staff"},
            {"label": "Catchment", "value": "West Midlands orthopaedic catchment + tertiary referrals from Midlands + nationally for sarcoma orthopaedics"},
            {"label": "Procedure volume", "value": "c. 4,500 inpatient orthopaedic procedures/yr; complex revision + sarcoma case mix"},
            {"label": "Cost driver — AMAP mileage", "value": "Modest staff personal-vehicle mileage; pool-car running for outreach + cross-site clinics"},
            {"label": "Pool fleet", "value": "Small pool-car fleet for outreach clinics + inter-hospital transfers"},
            {"label": "PTS scope", "value": "PTS not directly operated — West Midlands PTS contract is run by EMED Group / WMAS"},
            {"label": "IFRS 16 transition", "value": "April 2022 adoption brought leased pool-fleet onto balance sheet — residual P&L line covers running costs + AMAP"},
            {"label": "Funding trajectory", "value": "Stable c. £100-130k as AMAP rates frozen since 2011; growth tied to outreach activity volume"},
            {"label": "Delivery body", "value": "ROH Fleet & Logistics + HR/Payroll for AMAP claims; pool-fleet operators include NHS Fleet Solutions"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (D14 specialised orthopaedics) + DHSC + Birmingham & Solihull ICB"},
            {"label": "Evaluation evidence", "value": "ROH Annual Report; CQC provider profile; National Joint Registry outcomes; GIRFT orthopaedic benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: Royal Cripples' Hospital (1817 founder) → Royal Orthopaedic Hospital (1925 site move) · Successor: ongoing Bristol Road site renewal capital programme"}
        ],
        "notes": "ROH Birmingham is one of England's three specialist orthopaedic trusts (with RNOH Stanmore and RJAH Oswestry). The £115k transport line is among the smallest of any specialist trust because the trust operates from a single Bristol Road, Northfield campus with limited outreach activity — most patients travel to ROH rather than ROH staff travelling out. The line covers AMAP staff mileage at the HMRC 45p/25p rate (frozen since 2011 despite c. 50% cumulative fuel inflation) plus pool-car running for outreach clinics + inter-hospital transfers. The 2022 IFRS 16 transition brought leased pool-fleet onto the balance sheet at higher recognised charge.",
        "sources": [
            {"publisher": "The Royal Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.roh.nhs.uk/about-us/board-publications"},
            {"publisher": "Care Quality Commission", "title": "ROH provider profile (RRJ)", "url": "https://www.cqc.org.uk/provider/RRJ"},
            {"publisher": "National Joint Registry", "title": "NJR Annual Report — implant outcomes", "url": "https://reports.njrcentre.org.uk/"},
            {"publisher": "Getting It Right First Time", "title": "GIRFT Orthopaedics National Specialty Report", "url": "https://gettingitrightfirsttime.co.uk/surgical_specialties/orthopaedic-surgery/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Royal Orthopaedic Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — Royal National Orthopaedic Hospital NHS Trust", "Transport (business + patient) — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "Other & adjustments — The Royal Orthopaedic Hospital NHS Foundation Trust"]
    },
}
