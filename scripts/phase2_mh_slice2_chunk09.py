# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 09 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Lease expenditure — Pennine Care NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Pennine Care NHS Foundation Trust"}],
        "description": "Pennine Care's £0.92M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across Bury, Oldham, Rochdale, Stockport, Tameside and Glossop, plus Community Health Partnerships LIFT vehicles for primary-care-co-located bases. The trust's community-heavy footprint — c. 50+ leased clinic addresses — keeps the line elevated despite the small headline value.",
        "beneficiaries": "c. 4,000 staff serving c. 1.3M residents across the five Greater Manchester boroughs of Bury, Oldham, Rochdale, Stockport, Tameside (+ Glossop in Derbyshire); leased-estate component includes c. 50+ community-MH, CAMHS, LD and recovery-college bases.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.92M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 50+ NHSPS + CHP-LIFT premises across five GM boroughs + Glossop"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.4M operating lease → 2022-23 c. £0.8M ROU first year → 2024-25 £0.92M (sustained NHSPS uplift)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Greater Manchester ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; Edenfield/Pennine inquiry context for community-estate prioritisation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + GM ICS estate consolidation"}
        ],
        "notes": "Pennine Care's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet, and has continued to grow as NHSPS pursued market-rent uplifts on community clinics. The trust's geographic footprint across five Greater Manchester boroughs plus Glossop creates a high site count for a relatively modest turnover, exposing it to the NHSPS / mental-health-trust service-charge dispute more than acute-only peers. Pennine Care's strategic divestment of community-physical-health services to Northern Care Alliance in 2021 reduced some leased footprint, but core MH and CAMHS community estate remains largely NHSPS-leased. GM ICS estate consolidation is the medium-term lever to flatten cost growth.",
        "sources": [
            {"publisher": "Pennine Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.penninecare.nhs.uk/about-us/our-publications/annual-report-and-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "Pennine Care NHS FT provider profile (RT2)", "url": "https://www.cqc.org.uk/provider/RT2"}
        ],
        "related": ["Pennine Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Mersey Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Mersey Care NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Mersey Care NHS Foundation Trust"}],
        "description": "Mersey Care's £0.91M PFI / LIFT charge reflects the trust's occupation of LIFT-procured community-MH and integrated-care bases across Liverpool City Region under the Liverpool & Sefton LIFT and Knowsley LIFT vehicles (Community Health Partnerships shareholding + private partners + local-authority co-investment). The line covers the unitary-charge pass-through — debt service, FM lifecycle and soft-FM components — for those LIFT premises hosting MH community teams, addictions services and Life Rooms recovery-college sites.",
        "beneficiaries": "c. 9,000 staff and a registered catchment c. 1.5M across Liverpool City Region; LIFT-procured estate hosts community-MH team bases, addictions services and recovery-college (Life Rooms) sites; Ashworth Hospital high-secure men's service uses some LIFT-procured ancillary support space.",
        "legal_basis": "IFRS 16 Leases (post-2022 transition for finance-lease + service-concession arrangements) · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.91M"},
            {"label": "Procurement vehicle", "value": "Liverpool & Sefton LIFT + Knowsley LIFT — CHP shareholding + private investor + LA partnership"},
            {"label": "Estate covered", "value": "Community-MH team bases + addictions services + Life Rooms recovery-college sites + Ashworth ancillary support space"},
            {"label": "Unitary charge composition", "value": "Debt-service component + lifecycle (hard-FM building maintenance) + soft-FM (cleaning, security, catering where contracted)"},
            {"label": "Contract duration profile", "value": "LIFT contracts typically 25-year initial with extension option; Liverpool & Knowsley LIFTs signed mid-2000s — c. 8-12 years remaining"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession assets recognised on-balance-sheet under IFRIC 12; lease-component re-evaluated under IFRS 16 ch.7 GAM"},
            {"label": "Lifecycle indexation", "value": "Annual RPI / CPI indexation per LIFT contract terms — material driver of year-on-year line movement"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.7M → 2024-25 £0.91M — sustained CPI-linked uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Community Health Partnerships + private LIFT investor consortium"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cheshire & Merseyside ICB; LIFT policy oversight at DHSC"},
            {"label": "Evaluation evidence", "value": "NAO LIFT review 2017-18; trust ARA disclosure 2023-24; Cheshire & Merseyside ICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT mid-2000s NHS-Estates community-clinic model · Successor: end-of-LIFT-contract review + ICS estate consolidation early 2030s"}
        ],
        "notes": "Mersey Care's PFI / LIFT line is dominated by the Liverpool & Sefton and Knowsley LIFT vehicles, which procured community-health bases in the mid-2000s under the Local Improvement Finance Trust model — service-concession structures where Community Health Partnerships (DHSC majority shareholder) co-invests with private partners and local-authority partners, and the trust occupies as tenant under unitary-charge contracts. CPI / RPI indexation is the main driver of cost growth, layered on fixed debt-service and lifecycle components. As contracts approach their 25-year endpoint in the early 2030s, the trust and Cheshire & Merseyside ICB face a strategic choice on hand-back, extension or estate consolidation — a sector-wide LIFT cliff-edge mirroring the better-known PFI hand-back challenge.",
        "sources": [
            {"publisher": "Mersey Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.merseycare.nhs.uk/about-us/our-publications/annual-report-and-accounts"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mersey Care NHS FT provider profile (RW4)", "url": "https://www.cqc.org.uk/provider/RW4"}
        ],
        "related": ["Mersey Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Termination & post-employment — Nottinghamshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Nottinghamshire Healthcare NHS Foundation Trust"}],
        "description": "Nottinghamshire Healthcare's £0.91M termination + post-employment line covers one-off severance, contractual notice pay-in-lieu, redundancy and the NHS Pension Scheme employer-element on early-retirement and exit packages across the trust's c. 10,000-staff base. The trust's high-profile governance and capacity context — Rampton Hospital high-secure men's service, the Valdo Calocane homicide-inquiry fallout (2023-24), and the post-pandemic restructuring of community-MH teams — has driven elevated senior-leadership turnover and remediation-related exits.",
        "beneficiaries": "c. 10,000 staff covering Nottinghamshire, Bassetlaw and the national Rampton Hospital high-secure men's service; redundancy + exit-package pool of c. 30-60 individuals per year on average, scaled to remediation cycles and senior-leadership turnover.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme regulations · Public Sector Exit Payments Regulations 2020 (uncapped post-2021 quash) · Employment Rights Act 1996 (s.139 redundancy + s.86 statutory notice) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.91M"},
            {"label": "Headcount + exit-pool context", "value": "c. 10,000 substantive WTE; estimated 30-60 exit packages annually"},
            {"label": "Composition", "value": "Statutory + contractual redundancy + pay-in-lieu of notice + NHS Pension Scheme employer-element on early retirement + senior-staff exit packages"},
            {"label": "Valdo Calocane inquiry context", "value": "Jun 2023 Nottingham attacks → CQC rapid review + s.48 inquiry into trust pathway → senior-leadership turnover + remediation exits"},
            {"label": "Rampton Hospital context", "value": "High-secure men's service → workforce restructuring + retirement-cycle activity feeds termination line"},
            {"label": "April 2025 NIC step-up", "value": "Employer NIC threshold drop + rate rise (Apr 2025) raises NHS Pension Scheme employer-cost on exit packages forward"},
            {"label": "PSE Payments Regs 2020", "value": "Capped exit-payment regs revoked 2021; trust currently operates under HM Treasury non-statutory guidance + NHS England consent rules"},
            {"label": "Funding trajectory", "value": "Variable year-on-year; 2020-21 c. £0.5M → 2023-24 elevated through Calocane response + 2024-25 £0.91M"},
            {"label": "Delivery body", "value": "Trust HR + Finance teams + NHS Business Services Authority (Pensions) + NHSE consent for senior packages"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + HM Treasury (exit-pay guidance) + Notts & Notts ICB"},
            {"label": "Evaluation evidence", "value": "NAO senior-pay + exit reviews; CQC s.48 review report 2024 (Calocane); Trust ARA workforce remuneration report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 capped PSE payments regime · Successor: HMT non-statutory exit-pay guidance + NIC step-up Apr 2025"}
        ],
        "notes": "Nottinghamshire Healthcare's termination line in 2024-25 reflects the cumulative impact of the Valdo Calocane homicide-inquiry fallout — the June 2023 Nottingham attacks, perpetrated by a former service-user, triggered a CQC rapid review and s.48 inquiry into the trust's MH pathway, which in turn drove senior-leadership turnover and remediation-related exits across the community-MH leadership cadre. Layered on top is the routine retirement-cycle activity at Rampton Hospital, where ageing senior nursing and medical staff at the high-secure men's service generate a structural NHS Pension Scheme employer-cost on early retirement. The April 2025 employer-NIC step-up will raise forward NHS Pension Scheme employer-cost on subsequent exit packages.",
        "sources": [
            {"publisher": "Nottinghamshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nottinghamshirehealthcare.nhs.uk/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "Section 48 review of Nottinghamshire Healthcare NHS Foundation Trust (Valdo Calocane)", "url": "https://www.cqc.org.uk/publications/themed-work/section-48-review-nottinghamshire-healthcare-nhs-foundation-trust"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guidance", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
            {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/public-sector-exit-payments-guidance"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Nottinghamshire Healthcare NHS Foundation Trust", "Staff Costs", "NHS Mental Health Trusts", "NHS Pension Scheme", "Termination & post-employment — Southern Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Lancashire and South Cumbria NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Lancashire and South Cumbria NHS Foundation Trust"}],
        "description": "LSCFT's £0.91M transport line covers community-MH, CAMHS and crisis-team mileage plus inter-site patient transfers across one of England's largest geographic MH-trust catchments — Lancashire (urban + coastal + rural), Blackpool, Blackburn with Darwen and South Cumbria (rural Furness + Lake District). Sites include the Harbour (Blackpool), Guild Lodge (Preston, secure), Royal Lancaster Infirmary MH unit and dispersed community bases. The 2018 Lancashire-Cumbria merger consolidated previously separate transport regimes.",
        "beneficiaries": "c. 7,000 staff serving c. 1.8M residents across Lancashire, Blackpool, Blackburn with Darwen + South Cumbria; c. 5,500 km² catchment with substantial rural component (Lake District + Forest of Bowland); secure-MH catchment extends across Northwest England.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.91M"},
            {"label": "Catchment area", "value": "Lancashire + Blackpool + Blackburn + South Cumbria — c. 5,500 km², among England's largest MH-trust footprints"},
            {"label": "Site footprint", "value": "The Harbour (Blackpool, c. 154 beds) + Guild Lodge (Preston, secure) + Royal Lancaster MH unit + dispersed community bases"},
            {"label": "Rural mileage premium", "value": "South Cumbria + rural Lancashire generate per-WTE community mileage 2-3× urban-trust peers"},
            {"label": "2018 merger context", "value": "Lancashire Care + Cumbria Partnership MH services merged 2018-2019 forming LSCFT — consolidated transport baseline + Guild Lodge secure-services activity"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance via NWAS contract + accredited secure-transport providers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.65M → 2024-25 £0.91M — uplift driven by post-pandemic recovery + fuel CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with North West Ambulance Service NHS Trust + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports 2022-2024 (RW5); LSC ICS estate + travel review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Lancashire Care + Cumbria Partnership transport · Successor: LSC ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "LSCFT's transport line is structurally elevated by the geographic spread — the trust's footprint covers c. 5,500 km² from Blackpool's coastal urban core through Preston and Blackburn into rural Lancashire and the Lake District, generating per-WTE community mileage among the highest in the MH-trust sector. The 2018 merger of Lancashire Care with Cumbria Partnership's MH services consolidated transport baselines but retained the underlying rural-mileage premium. Guild Lodge low/medium-secure unit at Whittingham generates inter-site secure-transfer activity. NWAS handles most s.136 conveyance under the Northwest all-age PTS contract. Lancashire and South Cumbria ICS shared-fleet pooling and partial EV transition are the medium-term levers; CPI fuel pressure remains the dominant cost driver.",
        "sources": [
            {"publisher": "Lancashire and South Cumbria NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lscft.nhs.uk/About-Us/publications/"},
            {"publisher": "Care Quality Commission", "title": "LSCFT provider profile (RW5)", "url": "https://www.cqc.org.uk/provider/RW5"},
            {"publisher": "North West Ambulance Service NHS Trust", "title": "PTS contract data", "url": "https://www.nwas.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lancashire and South Cumbria ICB", "title": "ICS estate and travel review", "url": "https://www.lancashireandsouthcumbria.icb.nhs.uk/"}
        ],
        "related": ["Lancashire and South Cumbria NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Norfolk and Suffolk NHS Foundation Trust", "Mental Health Act 1983"]
    },
    "Business rates — Coventry and Warwickshire Partnership NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Coventry and Warwickshire Partnership NHS Trust"}],
        "description": "CWPT's £0.90M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — the Caludon Centre (Coventry, c. 130 acute MH beds), Brooklands Hospital (Marston Green, secure-LD), St Michael's Hospital (Warwick), St Laurence's House (Rugby) and c. 30+ community-MH, CAMHS and LD bases across Coventry, Warwickshire and Solihull. NHS FTs do not get charitable exemption; the line is rebased at each VOA revaluation cycle.",
        "beneficiaries": "Approximately 30+ occupied hereditaments (acute MH wards, secure-LD inpatient, community clinics, CAMHS sites, LD community bases) across Coventry, Warwickshire and Solihull; serves a registered catchment c. 1.05M plus regional secure-LD catchment.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.90M"},
            {"label": "Hereditament count", "value": "c. 30+ occupied sites across Coventry, Warwickshire + Solihull"},
            {"label": "Major rated sites", "value": "Caludon Centre (Coventry) + Brooklands (Marston Green, secure-LD) + St Michael's (Warwick) + St Laurence's (Rugby)"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs / Trusts are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "Coventry City Council + Warwick DC + Stratford-on-Avon DC + Rugby BC + Solihull MBC + Nuneaton & Bedworth BC + North Warwickshire BC"},
            {"label": "VOA 2023 revaluation impact", "value": "Mixed urban / district commercial RV movement post-pandemic; net broadly neutral; Brooklands custom-built secure-LD facility carries higher £/m² RV than community clinics"},
            {"label": "NHSPS interaction", "value": "Some community clinic estate held via NHSPS lease; rates passed through to CWPT as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.75M → 2024-25 £0.90M — tracks frozen UBR + new-site additions"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 7 billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "CWPT's business-rates line is structurally inflated by Brooklands Hospital — the West Midlands regional secure-LD inpatient resource at Marston Green carries an above-average rateable value per m² as a custom-built specialist secure facility. The Caludon Centre (Coventry) acute-MH unit and St Michael's (Warwick) inpatient site each carry meaningful RV alongside dozens of smaller community clinics. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. NHSPS-leased community clinics pass rates through to CWPT under occupier-rule, complicating the NHSPS service-charge recharge boundary that has been a sector-wide friction point.",
        "sources": [
            {"publisher": "Coventry and Warwickshire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.covwarkpt.nhs.uk/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Coventry and Warwickshire Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Central and North West London NHS Foundation Trust", "Valuation Office Agency"]
    },
    "General supplies & services — Berkshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Berkshire Healthcare NHS Foundation Trust"}],
        "description": "Berkshire Healthcare's £0.89M general supplies & services line covers non-clinical consumables, ward provisions, household goods, laundry materials and small operational equipment across Prospect Park Hospital (Reading), Wokingham Community Hospital, Bracknell Healthspace, Upton Hospital (Slough), West Berkshire Community Hospital and 100+ community-MH + physical-health bases. The combined MH + community remit drives a higher-than-pure-MH per-bed and per-clinic supplies cost, particularly for ward consumables and inpatient catering provisions in community-hospital settings.",
        "beneficiaries": "c. 4,500 staff and a registered catchment c. 900,000 across all 6 Berkshire unitary authorities; supplies consumed at c. 250 inpatient MH + community-hospital beds plus 100+ community-MH, CAMHS, IAPT and community-physical-health bases.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (consumables procurement) · Procurement Act 2023 (in force Oct 2024)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£0.89M"},
            {"label": "Site footprint generating consumption", "value": "Prospect Park + Wokingham CH + Bracknell + Upton + West Berks CH + 100+ community bases"},
            {"label": "Bed-stock + clinic count", "value": "c. 250 inpatient MH + community-hospital beds + 100+ community clinic bases"},
            {"label": "Composition", "value": "Non-clinical consumables + ward provisions + household goods + laundry materials + small operational equipment + minor catering provisions"},
            {"label": "Combined MH + community driver", "value": "Inpatient community-hospital beds + district-nursing supplies layer raises consumption above pure-MH peer trusts"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (majority) + Crown Commercial Service category contracts + minor local spot-buy"},
            {"label": "Procurement Act 2023 transition", "value": "New regime live Oct 2024 — central digital platform + transparency obligations replace PCR 2015 process"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.6M → 2024-25 £0.89M — uplift driven by post-pandemic activity recovery + supplies CPI"},
            {"label": "Delivery body", "value": "Trust Procurement + Estates & Facilities teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + BOB ICB / Frimley ICB · NHS Supply Chain governance"},
            {"label": "Evaluation evidence", "value": "NHS Supply Chain framework data; CQC 'Outstanding' inspection 2019-2024; trust ARA disclosure 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 fragmented spot-buy regime · Successor: NHS Supply Chain Future Operating Model + Procurement Act 2023"}
        ],
        "notes": "Berkshire Healthcare's general supplies & services line sits above pure-MH-trust peers because the trust's combined MH + community + community-hospital remit means it consumes ward provisions and household goods at community-hospital inpatient sites (Wokingham, West Berks, Upton) as well as standard MH inpatient consumables at Prospect Park. The trust's CQC 'Outstanding' rating reflects sustained quality investment that includes supply-chain reliability. NHS Supply Chain Future Operating Model and the Procurement Act 2023 transition (in force October 2024) are reshaping the framework architecture but the near-term cost driver remains supplies CPI. Post-pandemic activity recovery has restored consumption levels above 2019-20 baseline.",
        "sources": [
            {"publisher": "Berkshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.berkshirehealthcare.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Care Quality Commission", "title": "Berkshire Healthcare provider profile (RWX)", "url": "https://www.cqc.org.uk/provider/RWX"}
        ],
        "related": ["Berkshire Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "NHS Supply Chain", "General supplies & services — Sheffield Health and Social Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Derbyshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Derbyshire Healthcare NHS Foundation Trust"}],
        "description": "Derbyshire Healthcare's £0.89M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — the Hartington Unit (Chesterfield Royal), Radbourne Unit (Royal Derby Hospital), Audrey House (Ilkeston), Cherry Tree Close (Derby) and c. 25+ community-MH, CAMHS and LD bases across the city of Derby and Derbyshire. NHS FTs do not get charitable exemption; the line is rebased at each VOA revaluation cycle.",
        "beneficiaries": "Approximately 25+ occupied hereditaments (acute MH wards, recovery-house bases, community clinics, CAMHS and LD sites) across Derby and Derbyshire; serves a registered catchment c. 1.05M including rural Peak District + High Peak.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.89M"},
            {"label": "Hereditament count", "value": "c. 25+ occupied sites across Derby + Derbyshire"},
            {"label": "Major rated sites", "value": "Hartington Unit (Chesterfield) + Radbourne Unit (Derby) + Audrey House (Ilkeston) + Cherry Tree Close (Derby) + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "Derby City Council + Derbyshire Dales DC + Chesterfield BC + High Peak BC + Erewash BC + Amber Valley BC + Bolsover DC + NE Derbyshire DC + South Derbyshire DC"},
            {"label": "VOA 2023 revaluation impact", "value": "Mixed urban Derby + Chesterfield premises and rural Peak District community clinics; net broadly neutral for the trust post-pandemic"},
            {"label": "NHSPS interaction", "value": "Some community clinic estate held via NHSPS lease; rates passed through to trust as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.7M → 2024-25 £0.89M — tracks UBR + NHSPS pass-through"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 9 billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "Derbyshire Healthcare's business-rates line reflects a mid-sized MH-trust footprint where the Hartington Unit (co-located on the Chesterfield Royal site) and Radbourne Unit (co-located on Royal Derby Hospital) constitute the two largest hereditaments, while c. 20 smaller community bases generate the residual rates liability. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. The High Peak rural component carries lower per-m² RV than Derby city sites, partially offsetting the cost. NHSPS-leased community clinics pass rates through to the trust as occupier, consistent with the sector-wide service-charge friction.",
        "sources": [
            {"publisher": "Derbyshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.derbyshirehealthcareft.nhs.uk/about-us/board-and-governance/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Derbyshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Nottinghamshire Healthcare NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Cambridgeshire and Peterborough NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Cambridgeshire and Peterborough NHS Foundation Trust"}],
        "description": "CPFT's £0.87M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — Fulbourn Hospital (Cambridge), the Cavell Centre (Peterborough City Hospital site, PFI-procured), Doddington Hospital, Princess of Wales Hospital MH unit (Ely) and c. 30+ community-MH, CAMHS and older-people's MH bases across Cambridgeshire and Peterborough. NHS FTs do not get charitable exemption; the line is rebased at each VOA revaluation cycle.",
        "beneficiaries": "Approximately 30+ occupied hereditaments (acute MH wards, community clinics, CAMHS sites, older-people MH bases) across Cambridge city, Peterborough and rural Fenland + Huntingdonshire; serves a registered catchment c. 880,000.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.87M"},
            {"label": "Hereditament count", "value": "c. 30+ occupied sites across Cambridgeshire + Peterborough"},
            {"label": "Major rated sites", "value": "Fulbourn Hospital (Cambridge) + Cavell Centre (Peterborough, modern PFI-procured MH unit with high £/m² RV) + Doddington Hospital + Princess of Wales (Ely) + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "Cambridge City + Peterborough City + South Cambridgeshire + East Cambridgeshire + Huntingdonshire + Fenland"},
            {"label": "VOA 2023 revaluation impact", "value": "Cambridge city RV movement post-pandemic; rural Fenland modest; net broadly neutral for the trust"},
            {"label": "NHSPS interaction", "value": "Significant share of community clinic estate held via NHSPS lease; rates passed through to trust as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.7M → 2024-25 £0.87M — tracks frozen UBR + new-site additions"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 6 billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "CPFT's business-rates line is shaped by a mix of older-stock acute MH (Fulbourn) and modern PFI-procured (Cavell Centre on the Peterborough City Hospital campus) inpatient sites alongside dispersed community clinics. The Cavell Centre carries a relatively high £/m² rateable value as a custom-built clinical asset, but the underlying PFI unitary-charge sits separately in the trust's PFI / LIFT line. The Autumn Statement 2023 UBR freeze gave a one-year reprieve; the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. NHSPS-leased community clinics pass rates through to CPFT under occupier-rule, consistent with the sector-wide service-charge friction.",
        "sources": [
            {"publisher": "Cambridgeshire and Peterborough NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cpft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Cambridgeshire and Peterborough NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "PFI / LIFT charges — Cambridgeshire and Peterborough NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Devon Partnership NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Devon Partnership NHS Trust"}],
        "description": "Devon Partnership's £0.85M amortisation charge covers the systematic write-down of intangible assets — chiefly capitalised software, EPR licences and digital-clinical-record build cost — over their useful economic life under IAS 38. The line is rising in 2024-25 as the trust's Frontline Digitisation EPR rollout (a 2023-25 programme replacing legacy systems) brings new intangible balances into amortisation, layered on residual amortisation of pre-existing PARIS, RiO and clinical-portal investments.",
        "beneficiaries": "c. 2,800 staff working across the Cygnet Hospital (Exeter), Wonford House Hospital (Exeter), Glenbourne Unit (Plymouth) and dozens of community-MH bases; serves c. 1.2M residents of Devon, Plymouth and Torbay; EPR rollout user-base is the full clinical workforce.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (software procurement)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.85M"},
            {"label": "Composition", "value": "Capitalised software + EPR licences + digital-clinical-record build cost amortised under IAS 38"},
            {"label": "Frontline Digitisation EPR rollout", "value": "2023-25 trust EPR rollout under NHSE Frontline Digitisation programme — adds new intangible balances to amortise"},
            {"label": "Useful-economic-life policy", "value": "Software typically 3-7 years per DHSC GAM 2024-25 ch.5; major EPR systems often 7-10 years"},
            {"label": "Trust ARA disclosure note", "value": "Intangibles note in 2023-24 ARA discloses cost + accumulated amortisation + additions in year"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.5M → 2024-25 £0.85M — uplift driven by Frontline Digitisation additions in flight"},
            {"label": "Delivery body", "value": "Trust Digital Services + Finance + IT Capital teams + NHS England Frontline Digitisation team"},
            {"label": "Policy owner", "value": "DHSC + NHS England Transformation Directorate (Frontline Digitisation) + Devon ICB"},
            {"label": "Capital funding source", "value": "PDC capital allocation + Frontline Digitisation match-funding through NHSE"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme review; trust ARA disclosure 2023-24; CQC inspection 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 PARIS / RiO + smaller systems · Successor: integrated EPR going-concern with phased migration through to 2026"}
        ],
        "notes": "Devon Partnership's amortisation line is rising through the Frontline Digitisation programme period (2023-2026) as new EPR intangible balances come into amortisation, layered on residual amortisation of legacy PARIS, RiO and clinical-portal investments. NHSE's Frontline Digitisation programme provides match-funding through PDC capital, but the resulting intangible balance amortises against the trust's I&E account over 7-10 years per IAS 38. Devon's geography — Exeter + Plymouth + Torbay + rural Devon — meant the EPR rollout had to support a distributed community-team workflow, raising the per-staff licensing and build cost. The line is expected to plateau by 2026-27 once full rollout is complete.",
        "sources": [
            {"publisher": "Devon Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dpt.nhs.uk/about-us/publications/annual-report-accounts"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Devon Partnership NHS Trust provider profile (RWV)", "url": "https://www.cqc.org.uk/provider/RWV"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"}
        ],
        "related": ["Devon Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Frontline Digitisation programme", "Amortisation — Dorset Healthcare University NHS Foundation Trust"]
    },
    "Business rates — Lincolnshire Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Lincolnshire Partnership NHS Foundation Trust"}],
        "description": "LPFT's £0.84M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — Peter Hodgkinson Centre (Lincoln County Hospital site), Hartsholme (Lincoln), Hawthorn House (Boston), Ash Villa (Sleaford) and dozens of community-MH and CAMHS bases across Lincolnshire's rural geography. NHS FTs do not get charitable exemption; the line is rebased at each VOA revaluation cycle.",
        "beneficiaries": "Approximately 25+ occupied hereditaments (acute MH wards, community clinics, CAMHS sites) across Lincolnshire's c. 5,920 km² geography; serves a registered catchment c. 770,000 — England's most rural-skewed mental-health-trust footprint by area-per-resident.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.84M"},
            {"label": "Hereditament count", "value": "c. 25+ occupied sites across Lincolnshire"},
            {"label": "Major rated sites", "value": "Peter Hodgkinson Centre (Lincoln) + Hartsholme (Lincoln) + Hawthorn House (Boston) + Ash Villa (Sleaford) + community bases"},
            {"label": "Rural footprint", "value": "c. 5,920 km² catchment — England's most rural-skewed MH-trust geography; commercial RVs run below national average per m²"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "City of Lincoln + North Kesteven + South Kesteven + Boston + East Lindsey + West Lindsey + South Holland"},
            {"label": "VOA 2023 revaluation + NHSPS interaction", "value": "Modest rural commercial RV movement post-pandemic; significant share of community clinic estate held via NHSPS lease with rates passed through to trust as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.65M → 2024-25 £0.84M — tracks UBR + community-base additions"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 7 billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "LPFT's business-rates line balances a high site count (necessary to provide MH services across Lincolnshire's vast rural geography) against below-national-average per-m² rateable values typical of district commercial markets. The Peter Hodgkinson Centre (co-located on Lincoln County Hospital) is the largest single hereditament, with Hartsholme, Hawthorn House and Ash Villa as the next tier of inpatient sites. The Autumn Statement 2023 UBR freeze gave a one-year reprieve; the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. NHSPS-leased community clinics pass rates through to LPFT under occupier-rule, consistent with the sector-wide service-charge friction.",
        "sources": [
            {"publisher": "Lincolnshire Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lpft.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Lincolnshire Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Norfolk and Suffolk NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Clinical supplies & services — South West London and St George's Mental Health NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "South West London and St George's Mental Health NHS Trust"}],
        "description": "SWLSTG's £0.82M clinical supplies & services line covers consumables specifically attached to clinical activity — needles, syringes, ECT consumables, dressings, infection-control PPE, ward observation supplies and clinical-equipment minor items — across Springfield University Hospital (Tooting), Tolworth Hospital, Queen Mary's Hospital MH unit and 30+ community-MH and CAMHS bases across SW London. Springfield's 2023 redevelopment (new modern wards opened May 2023) reshaped the supply-chain footprint and accelerated single-use clinical-consumables pattern.",
        "beneficiaries": "c. 2,500 staff and a registered catchment c. 1.1M across Wandsworth, Merton, Sutton, Kingston and Richmond; supplies consumed across c. 320 inpatient MH beds (Springfield + Tolworth + Queen Mary's) plus 30+ community bases including the National Deaf Mental Health Service.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (clinical procurement) · Procurement Act 2023 (in force Oct 2024) · Medicines and Medical Devices Act 2021",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£0.82M"},
            {"label": "Site footprint generating consumption", "value": "Springfield (Tooting) + Tolworth + Queen Mary's MH unit + 30+ community bases"},
            {"label": "Bed-stock generating consumption", "value": "c. 320 inpatient MH beds across acute, PICU, older-people MH and forensic"},
            {"label": "Composition", "value": "Needles + syringes + ECT consumables + dressings + infection-control PPE + ward observation supplies + minor clinical equipment"},
            {"label": "Springfield redevelopment + specialist services", "value": "New modern wards opened May 2023 — single-use clinical-consumables pattern increased post-rebuild; National Deaf MH Service + Eating Disorders + Adolescent Forensic add specialist consumables profile"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (majority) + CCS clinical category contracts + minor local spot-buy"},
            {"label": "Procurement Act 2023 transition", "value": "New regime live Oct 2024 — central digital platform + transparency obligations replace PCR 2015"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.55M → 2024-25 £0.82M — uplift driven by post-Springfield-rebuild activity recovery + supplies CPI"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Estates teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South West London ICB · NHS Supply Chain governance"},
            {"label": "Evaluation evidence", "value": "Trust ARA disclosure 2023-24; CQC inspection 2023; Springfield redevelopment evaluation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 older Springfield ward consumables pattern · Successor: NHS Supply Chain Future Operating Model + Procurement Act 2023"}
        ],
        "notes": "SWLSTG's clinical supplies line tracks the 2023 Springfield redevelopment — the trust opened new modern wards on the Tooting site in May 2023, increasing single-use clinical-consumables consumption and ward-observation supplies as the new estate's design favoured single-occupancy en-suite rooms. The trust's specialist national services (the National Deaf Mental Health Service is a flagship, alongside Eating Disorders and Adolescent Forensic) generate a distinct supplies profile with specialist devices and assistive-tech consumables. NHS Supply Chain Future Operating Model and the Procurement Act 2023 transition are reshaping the framework architecture but supplies CPI remains the near-term cost driver.",
        "sources": [
            {"publisher": "South West London and St George's Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swlstg.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model + clinical category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Care Quality Commission", "title": "SWLSTG provider profile (RQY)", "url": "https://www.cqc.org.uk/provider/RQY"}
        ],
        "related": ["South West London and St George's Mental Health NHS Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "NHS Supply Chain", "Clinical supplies & services — Hertfordshire Partnership University NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Oxford Health NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Oxford Health NHS Foundation Trust"}],
        "description": "Oxford Health's £0.82M PFI / LIFT charge reflects the trust's occupation of LIFT-procured community-MH and integrated-care bases across Oxfordshire, Buckinghamshire, Berkshire West and Wiltshire under the Oxfordshire LIFT and adjacent vehicles (Community Health Partnerships shareholding + private partners). The line covers the unitary-charge pass-through — debt service, FM lifecycle and soft-FM components — for those LIFT premises hosting community-MH teams, CAMHS and primary-care-co-located services.",
        "beneficiaries": "c. 7,000 staff serving c. 2.5M residents across Oxfordshire, Buckinghamshire, Berkshire West, Wiltshire and Bath & North East Somerset; LIFT-procured estate hosts community-MH team bases, CAMHS clinics, primary-care-co-located services and addictions sites.",
        "legal_basis": "IFRS 16 Leases (post-2022 transition for finance-lease + service-concession arrangements) · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.82M"},
            {"label": "Procurement vehicle", "value": "Oxfordshire LIFT + adjacent vehicles — CHP shareholding + private investor + LA partnership"},
            {"label": "Estate covered", "value": "Community-MH team bases + CAMHS clinics + primary-care-co-located services + addictions sites"},
            {"label": "Unitary charge composition", "value": "Debt-service component + lifecycle (hard-FM building maintenance) + soft-FM (cleaning, security, catering where contracted)"},
            {"label": "Contract duration profile", "value": "LIFT contracts typically 25-year initial; Oxfordshire LIFT signed mid-2000s — c. 8-12 years remaining"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession assets recognised on-balance-sheet under IFRIC 12; lease-component re-evaluated under IFRS 16 ch.7 GAM"},
            {"label": "Lifecycle indexation", "value": "Annual RPI / CPI indexation per LIFT contract terms — material driver of year-on-year line movement"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.65M → 2024-25 £0.82M — sustained CPI-linked uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Community Health Partnerships + private LIFT investor consortium"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Buckinghamshire, Oxfordshire and Berkshire West ICB; LIFT policy oversight at DHSC"},
            {"label": "Evaluation evidence", "value": "NAO LIFT review 2017-18; trust ARA disclosure 2023-24; BOB ICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT mid-2000s NHS-Estates community-clinic model · Successor: end-of-LIFT-contract review + ICS estate consolidation early 2030s"}
        ],
        "notes": "Oxford Health's PFI / LIFT line is dominated by Oxfordshire LIFT-procured community-health bases from the mid-2000s under the Local Improvement Finance Trust model — service-concession structures where CHP (DHSC majority shareholder) co-invests with private partners, and the trust occupies as tenant. CPI / RPI indexation each year is the main driver of cost growth, layered on fixed debt-service and lifecycle components. As contracts approach their 25-year endpoint in the early 2030s, the trust and BOB ICB face a strategic choice on hand-back, extension or estate consolidation — a sector-wide LIFT cliff-edge mirroring the PFI hand-back challenge. Oxford Health's wider community + MH + dental + sexual-health remit means the LIFT estate is functionally diverse.",
        "sources": [
            {"publisher": "Oxford Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.oxfordhealth.nhs.uk/about-us/corporate-information/publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Oxford Health provider profile (RNU)", "url": "https://www.cqc.org.uk/provider/RNU"}
        ],
        "related": ["Oxford Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Clinical supplies & services — Hertfordshire Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Hertfordshire Partnership University NHS Foundation Trust"}],
        "description": "HPFT's £0.80M clinical supplies & services line covers consumables specifically attached to clinical activity — needles, syringes, ECT consumables, dressings, infection-control PPE and ward observation supplies — across Kingsley Green Hospital (Harper Lane), the Lister Hospital MH unit (Stevenage), Logandene (Hemel Hempstead), Forest House (Radlett, CAMHS) and 30+ community-MH and LD bases across Hertfordshire, Buckinghamshire, Essex and Norfolk. The trust's national specialist services (Tier 4 CAMHS at Forest House, autism + LD specialist services) generate a distinct supplies profile.",
        "beneficiaries": "c. 3,500 staff and a registered catchment c. 1.2M across Hertfordshire plus national specialist Tier 4 CAMHS, autism + LD services; c. 270 inpatient MH + LD + CAMHS beds plus 30+ community bases.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (clinical procurement) · Procurement Act 2023 (in force Oct 2024) · Medicines and Medical Devices Act 2021",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£0.80M"},
            {"label": "Site footprint generating consumption", "value": "Kingsley Green + Lister MH unit + Logandene + Forest House (Tier 4 CAMHS) + 30+ community bases"},
            {"label": "Bed-stock generating consumption", "value": "c. 270 inpatient MH + LD + CAMHS beds"},
            {"label": "Composition", "value": "Needles + syringes + ECT consumables + dressings + infection-control PPE + ward observation supplies + minor clinical equipment"},
            {"label": "Specialist services premium", "value": "Tier 4 CAMHS at Forest House + national autism / LD assessment + treatment service — distinct supplies profile"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (majority) + CCS clinical category contracts + minor local spot-buy"},
            {"label": "Procurement Act 2023 transition", "value": "New regime live Oct 2024 — central digital platform + transparency obligations replace PCR 2015"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.55M → 2024-25 £0.80M — uplift driven by post-pandemic activity recovery + supplies CPI"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Estates teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Hertfordshire and West Essex ICB · NHS Supply Chain governance"},
            {"label": "Evaluation evidence", "value": "Trust ARA disclosure 2023-24; CQC inspection 2023; NHSE specialised commissioning review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 fragmented spot-buy regime · Successor: NHS Supply Chain Future Operating Model + Procurement Act 2023"}
        ],
        "notes": "HPFT's clinical supplies line is shaped by the trust's national specialist services — Tier 4 CAMHS at Forest House (Radlett) and the autism + LD assessment + treatment service generate a distinct supplies pattern that includes specialist devices and assistive-tech consumables, alongside standard MH inpatient consumables at Kingsley Green and the Lister MH unit. The post-pandemic activity recovery has restored consumption above 2019-20 baseline. NHS Supply Chain Future Operating Model and the Procurement Act 2023 transition are reshaping the framework architecture but supplies CPI remains the near-term cost driver. HPFT also incurs supplies cost on national-specialist-services activity commissioned by NHSE Specialised Commissioning, recharged through commissioner contracts.",
        "sources": [
            {"publisher": "Hertfordshire Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hpft.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model + clinical category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Care Quality Commission", "title": "HPFT provider profile (RWR)", "url": "https://www.cqc.org.uk/provider/RWR"}
        ],
        "related": ["Hertfordshire Partnership University NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "NHS Supply Chain", "Clinical supplies & services — South West London and St George's Mental Health NHS Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Cambridgeshire and Peterborough NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Cambridgeshire and Peterborough NHS Foundation Trust"}],
        "description": "CPFT's £0.77M amortisation charge covers the systematic write-down of intangible assets — chiefly capitalised software, EPR licences and digital-clinical-record build cost — over their useful economic life under IAS 38. The line is rising as the trust's Frontline Digitisation EPR rollout (with NHSE-Cambridge University Hospitals shared investment) brings new intangible balances into amortisation, alongside capitalised research-collaboration software developed with the Cambridge academic ecosystem.",
        "beneficiaries": "c. 4,500 staff and a registered catchment c. 880,000 across Cambridgeshire + Peterborough; EPR rollout user-base spans the full clinical workforce across Fulbourn, Cavell Centre, Doddington and community bases; research-collaboration intangibles support the academic-trust university partnership.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (software procurement)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.77M"},
            {"label": "Composition", "value": "Capitalised software + EPR licences + digital-clinical-record build cost + research-collaboration platforms amortised under IAS 38"},
            {"label": "Frontline Digitisation EPR rollout", "value": "Trust EPR programme under NHSE Frontline Digitisation — adds new intangible balances to amortise"},
            {"label": "Useful-economic-life policy", "value": "Software typically 3-7 years per DHSC GAM 2024-25 ch.5; major EPR systems often 7-10 years"},
            {"label": "Cambridge academic ecosystem", "value": "University-of-Cambridge collaboration generates capitalised research-software intangibles alongside clinical EPR"},
            {"label": "Trust ARA disclosure note", "value": "Intangibles note in 2023-24 ARA discloses cost + accumulated amortisation + additions in year"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.45M → 2024-25 £0.77M — uplift driven by Frontline Digitisation additions in flight"},
            {"label": "Delivery body", "value": "Trust Digital Services + Finance + IT Capital teams + NHS England Frontline Digitisation team"},
            {"label": "Policy owner", "value": "DHSC + NHS England Transformation Directorate (Frontline Digitisation) + Cambridgeshire and Peterborough ICB"},
            {"label": "Capital funding source", "value": "PDC capital allocation + Frontline Digitisation match-funding through NHSE"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme review; trust ARA disclosure 2023-24; CQC inspection 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline-Digitisation legacy clinical-record systems · Successor: integrated EPR going-concern with phased migration through to 2026"}
        ],
        "notes": "CPFT's amortisation line is rising through the Frontline Digitisation programme period as new EPR intangible balances come into amortisation. The trust's academic-partnership status with the University of Cambridge adds an unusual research-software intangible component on top of clinical EPR — capitalised platforms supporting clinical research, neuroimaging and informatics-research collaborations amortise alongside operational systems. NHSE's Frontline Digitisation programme provides match-funding through PDC capital, but the resulting intangible balance amortises against the trust's I&E account over 7-10 years per IAS 38. The line is expected to plateau by 2026-27 once full rollout is complete.",
        "sources": [
            {"publisher": "Cambridgeshire and Peterborough NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cpft.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "CPFT provider profile (RT1)", "url": "https://www.cqc.org.uk/provider/RT1"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"}
        ],
        "related": ["Cambridgeshire and Peterborough NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Frontline Digitisation programme", "Amortisation — Devon Partnership NHS Trust"]
    },
    "Transport (business + patient) — Bradford District Care NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Bradford District Care NHS Foundation Trust"}],
        "description": "Bradford District Care's £0.76M transport line covers business mileage for community-MH, district-nursing, school-nursing, health-visiting and CAMHS teams across Bradford, Airedale, Wharfedale and Craven, plus inter-site patient transfers between Lynfield Mount Hospital (Bradford acute MH), Airedale Centre for Mental Health (Steeton) and dozens of community bases. The trust's combined MH + community remit and its rural Craven and Wharfedale catchment generate a high mileage base layered on standard urban-MH crisis-team travel.",
        "beneficiaries": "c. 3,500 staff serving c. 700,000 residents of Bradford metropolitan district + Airedale, Wharfedale and Craven; combined MH + community + CAMHS + LD + community-physical-health remit means a high district-nursing mileage layer.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.76M"},
            {"label": "Catchment area", "value": "Bradford district + Airedale + Wharfedale + Craven — c. 700,000 residents"},
            {"label": "Site footprint", "value": "Lynfield Mount Hospital + Airedale CMH (Steeton) + c. 60+ community bases"},
            {"label": "Combined remit driver", "value": "MH + community + CAMHS + LD + community-physical-health — district-nursing layer on top of MH crisis-team mileage; rural Craven + Wharfedale add Yorkshire Dales fringe mileage premium"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance via Yorkshire Ambulance Service contract + accredited secure-transport providers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "Pool car + lease-vehicle fleet", "value": "Salary-sacrifice + Crown Commercial Service vehicle framework — gradual EV transition under West Yorkshire Clean Air pilots"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.55M → 2024-25 £0.76M — uplift driven by post-pandemic visit recovery + fuel CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with Yorkshire Ambulance Service NHS Trust + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports 2022-2024 (RT5); West Yorkshire ICS estate + travel review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate community + MH transport baselines · Successor: WY ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "Bradford District Care's transport line is structurally elevated by the integrated MH + community + CAMHS + LD + community-physical-health remit — the same trust runs district-nursing, school-nursing and health visiting across Bradford district plus rural Craven and Wharfedale alongside MH crisis teams, generating a much larger mileage base than MH-only providers of similar size. Yorkshire Ambulance Service handles most s.136 conveyance under the West Yorkshire all-age PTS contract. The West Yorkshire ICS is exploring shared-fleet pooling and EV transition under regional Clean Air pilots — partial EV adoption is the medium-term lever to flatten fuel-cost growth.",
        "sources": [
            {"publisher": "Bradford District Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bdct.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "Bradford District Care provider profile (RT5)", "url": "https://www.cqc.org.uk/provider/RT5"},
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "PTS contract data", "url": "https://www.yas.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "West Yorkshire ICB", "title": "ICS estate and travel review", "url": "https://www.wypartnership.co.uk/"}
        ],
        "related": ["Bradford District Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Leicestershire Partnership NHS Trust", "Mental Health Act 1983"]
    },
    "PFI / LIFT charges — Tees, Esk and Wear Valleys NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Tees, Esk and Wear Valleys NHS Foundation Trust"}],
        "description": "TEWV's £0.75M PFI / LIFT charge reflects the trust's occupation of LIFT-procured community-MH and integrated-care bases across Tees Valley, County Durham, North Yorkshire and York under the NE England LIFT vehicles (Community Health Partnerships shareholding + private partners). The line covers the unitary-charge pass-through — debt service, FM lifecycle and soft-FM components — for those LIFT premises hosting community-MH teams, CAMHS and primary-care-co-located services. The 2018 transfer of CAMHS to TEWV consolidated some LIFT footprint.",
        "beneficiaries": "c. 6,500 staff serving c. 2.0M residents across County Durham, Tees Valley, North Yorkshire and the City of York; LIFT-procured estate hosts community-MH team bases, CAMHS clinics, older-people MH bases and primary-care-co-located services.",
        "legal_basis": "IFRS 16 Leases (post-2022 transition for finance-lease + service-concession arrangements) · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.75M"},
            {"label": "Procurement vehicle", "value": "NE England LIFT vehicles — CHP shareholding + private investor + LA partnership"},
            {"label": "Estate covered", "value": "Community-MH team bases + CAMHS clinics + older-people MH bases + primary-care-co-located services"},
            {"label": "Unitary charge composition", "value": "Debt-service component + lifecycle (hard-FM building maintenance) + soft-FM (cleaning, security, catering where contracted)"},
            {"label": "Contract duration profile", "value": "LIFT contracts typically 25-year initial; NE LIFTs signed mid-2000s — c. 8-12 years remaining"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession assets recognised on-balance-sheet under IFRIC 12; lease-component re-evaluated under IFRS 16 ch.7 GAM"},
            {"label": "Lifecycle indexation", "value": "Annual RPI / CPI indexation per LIFT contract terms — material driver of year-on-year line movement"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.6M → 2024-25 £0.75M — sustained CPI-linked uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Community Health Partnerships + private LIFT investor consortium"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North East and North Cumbria ICB + Humber and North Yorkshire ICB; LIFT policy oversight at DHSC"},
            {"label": "Evaluation evidence", "value": "NAO LIFT review 2017-18; trust ARA disclosure 2023-24; West Lane Hospital independent review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT mid-2000s NHS-Estates community-clinic model · Successor: end-of-LIFT-contract review + ICS estate consolidation early 2030s"}
        ],
        "notes": "TEWV's PFI / LIFT line is dominated by mid-2000s NE England LIFT vehicles procured under the Local Improvement Finance Trust model — service-concession structures where Community Health Partnerships (DHSC majority shareholder) co-invests with private partners and the trust occupies as tenant under unitary-charge contracts. CPI / RPI indexation each year is the main driver of cost growth, layered on fixed debt-service and lifecycle components. As contracts approach their 25-year endpoint in the early 2030s, the trust and the two ICBs (NENC + HNY) face a strategic choice on hand-back, extension or estate consolidation. The West Lane Hospital scandal (2019 closure of CAMHS adolescent unit, deaths of three young women) reshaped CAMHS commissioning but the LIFT footprint persists.",
        "sources": [
            {"publisher": "Tees, Esk and Wear Valleys NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.tewv.nhs.uk/about/policies-information/board-papers-and-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "TEWV provider profile (RX3) + West Lane Hospital reports", "url": "https://www.cqc.org.uk/provider/RX3"}
        ],
        "related": ["Tees, Esk and Wear Valleys NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Derbyshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Derbyshire Healthcare NHS Foundation Trust"}],
        "description": "Derbyshire Healthcare's £0.74M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across Derby city and Derbyshire (including the Hartington Unit ancillary space at Chesterfield Royal, Cherry Tree Close at Derby and dispersed Peak District community bases), plus Community Health Partnerships LIFT vehicles for primary-care-co-located premises.",
        "beneficiaries": "c. 2,500 staff serving c. 1.05M residents of Derby + Derbyshire; leased-estate component includes c. 25+ community-MH, CAMHS, LD and recovery-college bases dispersed across urban Derby, Chesterfield and rural Peak District + High Peak.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.74M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 25+ NHSPS + CHP-LIFT premises across urban Derby + Chesterfield + Peak District + High Peak"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.35M operating lease → 2022-23 c. £0.65M ROU first year → 2024-25 £0.74M (sustained NHSPS uplift)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Derby and Derbyshire ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC inspection 2023; Derby and Derbyshire ICS estate review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + Derby and Derbyshire ICS estate consolidation"}
        ],
        "notes": "Derbyshire Healthcare's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet, and has continued to grow as NHSPS pursued market-rent uplifts on community clinics. The trust's geographic footprint across urban Derby and Chesterfield plus rural Peak District and High Peak generates a relatively high site count for a modest turnover, exposing it to the NHSPS / mental-health-trust service-charge dispute. The Hartington and Radbourne Unit primary blocks are co-located on Chesterfield Royal and Royal Derby Hospital sites under host-trust arrangements rather than NHSPS leases, but ancillary clinical space is leased. Derby and Derbyshire ICS estate consolidation is the medium-term lever to flatten cost growth.",
        "sources": [
            {"publisher": "Derbyshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.derbyshirehealthcareft.nhs.uk/about-us/board-and-governance/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "HM Treasury", "title": "Public Expenditure System (PES) discount rates", "url": "https://www.gov.uk/government/publications/public-spending-statistics-release-schedule"}
        ],
        "related": ["Derbyshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Pennine Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
}
