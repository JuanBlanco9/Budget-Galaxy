# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 08 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "PFI / LIFT charges — Oxleas NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Oxleas NHS Foundation Trust"}],
        "description": "Oxleas's £1.11M PFI / LIFT line covers unitary-charge payments on the Greenwich and Bexley LIFT-vehicle community-clinic estate plus residual ancillary PFI obligations. Under IFRIC 12 service-concession accounting, the unitary charge splits between service, finance and asset components. The trust delivers MH, CAMHS, community physical-health and prison healthcare across Bexley, Bromley and Greenwich, and the LIFT estate underpins community-MH and IAPT clinic access.",
        "beneficiaries": "c. 4,300 staff serving c. 800,000 residents across Bexley, Bromley and Greenwich plus prison-healthcare contracts at HMP Belmarsh, Isis and Thameside; LIFT-vehicle clinic estate hosts community-MH, CAMHS, IAPT (NHS Talking Therapies) and physical-health teams.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (where applicable) · DHSC Group Accounting Manual 2024-25 ch.7 + ch.8 · NHS (Local Improvement Finance Trust) framework · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.11M"},
            {"label": "Scheme type", "value": "LIFT (Local Improvement Finance Trust) community-clinic estate — Greenwich + Bexley LIFTCo vehicles"},
            {"label": "Sites covered", "value": "Community-MH + IAPT + CAMHS + physical-health clinics across Bexley, Bromley, Greenwich"},
            {"label": "Unitary charge split", "value": "Service charge (FM, lifecycle, soft services) + finance cost + asset depreciation per IFRIC 12"},
            {"label": "Contract counterparty", "value": "Greenwich LIFTCo + Bexley LIFTCo (CHP-managed strategic partnering boards)"},
            {"label": "Programme owner", "value": "Community Health Partnerships Ltd (CHP) + DHSC + NHSE"},
            {"label": "Funding trajectory", "value": "Broadly flat — unitary charges indexed to RPI/CPI; £1.0-1.2M band sustained 2020-25"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + CHP head-tenant model"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South East London ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI / LIFT reviews; CHP annual review; Public Accounts Committee 2018 PFI value-for-money report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT (early-2000s) directly-owned community clinics · Successor: LIFT contract expiry programme (most schemes expire 2030s) → handback to NHS or re-let"},
            {"label": "Prison-healthcare context", "value": "HMP Belmarsh / Isis / Thameside healthcare delivered by Oxleas; primary-care premises within prison estate sit outside LIFT"}
        ],
        "notes": "Oxleas's PFI / LIFT line is dominated by the Greenwich and Bexley LIFT estate vehicles, which between them house most of the trust's community-MH, IAPT and CAMHS clinics. The unitary charge is indexed annually (RPI/CPI hybrid) and accounted under IFRIC 12 — splitting into service, finance and asset depreciation components, complicating year-on-year comparability when Oxleas refreshes lifecycle works. CHP acts as head-tenant and strategic-partner. The major medium-term risk is LIFT contract expiry across the 2030s, when the trust + ICB must decide between handback, extension or replacement procurement; NAO has flagged sector-wide LIFT-expiry planning as weak. The 2024 Non-Domestic Rating reform interacts with the service-charge component.",
        "sources": [
            {"publisher": "Oxleas NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.oxleas.nhs.uk/about-us/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review and scheme directory", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 8 — Service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018) + LIFT scrutiny", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "HM Treasury", "title": "Private Finance Initiative and Private Finance 2 projects: 2023 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2023-summary-data"}
        ],
        "related": ["Oxleas NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Derbyshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Derbyshire Healthcare NHS Foundation Trust"}],
        "description": "Derbyshire Healthcare's £1.10M general supplies & services line covers non-clinical consumables, ward provisions, hotel-services materials, laundry chemicals, cleaning supplies, kitchen consumables and general equipment across Kingsway Hospital (Derby), the Radbourne Unit (Royal Derby), the Hartington Unit (Chesterfield) and community-MH bases. The MH-only configuration (no integrated physical-health remit) keeps the line modest relative to combined-remit peers; PPE and infection-control consumable costs remain elevated post-pandemic.",
        "beneficiaries": "c. 2,400 staff serving c. 1.05M residents across Derby City and Derbyshire; c. 200 inpatient MH beds across Kingsway, Radbourne and Hartington; community-MH + CAMHS + perinatal + LD coverage across the whole county.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£1.10M"},
            {"label": "Composition", "value": "Hotel-services consumables + laundry + cleaning + kitchen + ward general supplies + minor non-clinical equipment"},
            {"label": "Site footprint", "value": "Kingsway Hospital + Radbourne Unit + Hartington Unit + c. 30 community-MH bases"},
            {"label": "Headcount served", "value": "c. 2,400 substantive WTE"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (hotel services + cleaning + laundry) + local catering and consumables"},
            {"label": "Post-pandemic PPE residual", "value": "Infection-control consumables sustained above 2019 baseline; PPE legacy stocks transitioning to BAU"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.8M → 2024-25 £1.10M — uplift driven by CPI on consumables + sustained infection-control overhead"},
            {"label": "Delivery body", "value": "Trust Procurement + Hotel Services + Estates teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Joined Up Care Derbyshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Model Hospital benchmarking; trust ARA 2023-24 inventory disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 supply baseline · Successor: ICS-pooled procurement under JUCD ICB + NHS Supply Chain reformed CIPS"}
        ],
        "notes": "Derbyshire Healthcare's general supplies & services line stays modest because the trust is MH-only — no integrated district-nursing or physical-health community remit to drive consumable volumes. The post-pandemic PPE / infection-control overhead has stuck above 2019 baselines, mirroring the sector-wide pattern. NHS Supply Chain remains the dominant procurement route under reformed Category Tower governance, but local catering and laundry contracts retain a non-trivial share. The CQC's 2023 'Requires Improvement' rating drove targeted ward-environment improvements (cleaning + repair) that touch this line indirectly. ICS-pooled procurement under Joined Up Care Derbyshire is the medium-term efficiency lever.",
        "sources": [
            {"publisher": "Derbyshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.derbyshirehealthcareft.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "NHS Supply Chain", "title": "Hotel services and cleaning category data", "url": "https://www.supplychain.nhs.uk/categories/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Derbyshire Healthcare NHS FT provider profile (RXM)", "url": "https://www.cqc.org.uk/provider/RXM"},
            {"publisher": "NHS England", "title": "Model Hospital — non-clinical consumables benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"}
        ],
        "related": ["Derbyshire Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "Department of Health and Social Care", "General supplies & services — Sheffield Health and Social Care NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Business rates — Birmingham and Solihull Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Birmingham and Solihull Mental Health NHS Foundation Trust"}],
        "description": "BSMHFT's £1.09M business-rates charge reflects VOA-set rateable values × 49.9p/54.6p UBR on c. 40+ occupied hereditaments — the Reservoir Court hub, Highcroft (Erdington), Oleaster (Edgbaston), Reaside Clinic medium-secure, Tamarind Centre and dozens of community-MH bases across Birmingham and Solihull. NHS FTs do not qualify for charitable exemption, and Birmingham's commercial-RV mix (mixed urban-suburban) keeps the per-site charge moderate relative to inner-London peers.",
        "beneficiaries": "c. 4,200 staff serving c. 1.4M residents of Birmingham and Solihull; the trust runs Reaside Clinic (medium-secure regional service), specialist forensic CAMHS, and the Ardenleigh women's medium-secure unit serving the wider West Midlands.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.09M"},
            {"label": "Hereditament count", "value": "c. 40+ occupied sites across Birmingham + Solihull (acute MH, secure, community, CAMHS)"},
            {"label": "Geographic spread", "value": "Birmingham CC + Solihull MBC billing authorities"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "VOA 2023 revaluation", "value": "Birmingham commercial RVs rebased moderately; rateable values updated 1 Apr 2023 across estate"},
            {"label": "Major sites driving line", "value": "Reservoir Court HQ + Highcroft + Oleaster + Reaside Clinic + Tamarind + Ardenleigh"},
            {"label": "NHSPS interaction", "value": "Significant share of community-MH estate held via NHS Property Services lease; rates passed through to trust"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Valuation Office Agency + Birmingham CC + Solihull MBC billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.9M → 2024-25 £1.09M — modest growth tracking frozen UBR + community estate additions"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation · Successor: 2026 next revaluation under NDRA 2023 (3-year cycle)"}
        ],
        "notes": "BSMHFT's business-rates line reflects an estate concentrated in mid-RV Birmingham locations with significant secure-services footprint (Reaside, Ardenleigh) — secure-unit hereditaments tend to attract above-average rateable values per m² because of the bespoke construction. The 2024 Non-Domestic Rating reform retained the temporary differential between standard and small multipliers, with Autumn Statement 2024 confirming the freeze for retail-hospitality but not the standard NHS hereditament. The 2026 revaluation is the next pinch-point. NHSPS pass-through of rates on community-clinic estate adds annual variability that the trust has limited control over. CQC's 2024 'Good' rating frames a stable estate baseline.",
        "sources": [
            {"publisher": "Birmingham and Solihull Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bsmhft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Birmingham and Solihull Mental Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Central and North West London NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "Business rates — Berkshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Berkshire Healthcare NHS Foundation Trust"}],
        "description": "Berkshire Healthcare's £1.06M business-rates line reflects VOA rateable values × 49.9p/54.6p UBR on c. 100+ occupied hereditaments distributed across all 6 Berkshire unitary authorities — Prospect Park Hospital (Reading), Wokingham Community Hospital, Bracknell Healthspace, Upton Hospital (Slough), West Berkshire Community Hospital and dozens of community-MH + physical-health bases. The combined MH + community + CAMHS + LD remit drives a high site count; commuter-belt Berkshire commercial RVs sit above national average.",
        "beneficiaries": "c. 4,500 staff supporting c. 900,000 residents across Reading, Slough, Bracknell Forest, Windsor and Maidenhead, West Berkshire and Wokingham; combined MH + community + CAMHS + LD service across 100+ sites including hospitals, community hospitals, GP-co-located teams and CAMHS clinics.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.06M"},
            {"label": "Hereditament count", "value": "c. 100+ occupied sites across all 6 Berkshire unitary authorities"},
            {"label": "Billing authorities", "value": "Reading BC + Slough BC + Bracknell Forest + Windsor & Maidenhead + West Berkshire + Wokingham"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Berkshire RV premium", "value": "Reading + Slough + RBWM commercial RVs sit above national-average per m² (commuter-belt)"},
            {"label": "Major sites driving line", "value": "Prospect Park Hospital (Reading) + Wokingham CH + Bracknell Healthspace + Upton + West Berks CH"},
            {"label": "NHSPS interaction", "value": "Substantial community-clinic estate held via NHS Property Services lease — rates passed through to trust as occupier"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Valuation Office Agency + 6 billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG + NHSE Provider Finance + Buckinghamshire, Oxfordshire and Berkshire West ICB / Frimley ICB"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.9M → 2024-25 £1.06M — modest sustained growth tracking site additions + frozen UBR"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation · Successor: 2026 next revaluation under NDRA 2023 (3-year cycle)"}
        ],
        "notes": "Berkshire Healthcare's rates line is shaped by both the multi-authority footprint (six billing authorities to negotiate with) and the structural commuter-belt premium that pushes Reading, Slough and RBWM commercial RVs above national average. The community-physical-health remit means the trust occupies more small NHSPS-leased clinic premises than MH-only peers, generating recurring NHSPS service-charge / rates pass-through volatility. The 2024 Non-Domestic Rating reform did not extend small-multiplier relief to NHS hereditaments, and the 2026 revaluation is expected to rebase Reading and Slough RVs upward post the 2023 antecedent date. CQC 'Outstanding' rating context underpins a stable estate baseline.",
        "sources": [
            {"publisher": "Berkshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.berkshirehealthcare.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Berkshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Birmingham and Solihull Mental Health NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "Amortisation — Southern Health NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Southern Health NHS Foundation Trust"}],
        "description": "Southern Health's £1.04M amortisation line reflects the systematic write-down of intangible assets — primarily software licences, capitalised EPR development cost, capitalised training and minor brand/website assets — across the trust's MH + LD + community-physical-health portfolio in Hampshire. The line stepped up post-2022 as the trust capitalised Frontline Digitisation programme spend on EPR consolidation; useful-life amortisation is set at 3-7 years per DHSC GAM 2024-25.",
        "beneficiaries": "c. 6,000 staff serving c. 1.4M residents across Hampshire (excluding Portsmouth and South-East Hampshire); MH + LD + community-physical-health + specialist-CAMHS coverage; intangibles support clinical record-keeping, e-prescribing and corporate workflow tooling.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.04M"},
            {"label": "Asset class", "value": "Software licences + capitalised EPR development + capitalised training + minor brand/website assets"},
            {"label": "Useful-life policy", "value": "3-7 years per DHSC GAM 2024-25 ch.5 (software typically 3-5; major EPR 5-7)"},
            {"label": "Frontline Digitisation context", "value": "Post-2022 step-up reflecting capitalised EPR consolidation spend under FD programme"},
            {"label": "Amortisation method", "value": "Straight-line over assessed useful life — annual impairment review per IAS 38"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.6M → 2024-25 £1.04M — sustained growth tracking FD capitalisation pipeline"},
            {"label": "Delivery body", "value": "Trust Finance + Digital Services + Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation programme + Hampshire and Isle of Wight ICB"},
            {"label": "Connors-Pope inquiry context", "value": "Trust under sustained scrutiny 2015-onward over unexpected-deaths governance (Mazars 2015, Connor Sparrowhawk inquest); digital-record investment a key remediation lever"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reviews; trust ARA 2023-24 intangibles disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 legacy RiO + paper-hybrid records · Successor: consolidated EPR fully amortised over 5-7 year cycle"},
            {"label": "Context within sub-line", "value": "MH-trust sector amortisation lines typically £0.5-2.0M; Southern Health mid-range reflecting moderate capital programme"}
        ],
        "notes": "Southern Health's amortisation line has grown steadily since 2022 as Frontline Digitisation programme capitalisation flowed through into amortisation under IAS 38. The trust's history — Mazars 2015 review of unexpected deaths, the Connor Sparrowhawk inquest, sustained CQC scrutiny — placed digital clinical-record investment at the centre of its remediation programme, reinforcing capital intangible spend. Useful-life policy aligns to DHSC GAM 2024-25 ch.5: 3-5 years for off-the-shelf software, 5-7 for bespoke EPR development. Annual IAS 38 impairment reviews introduce volatility when modules are deprecated. The medium-term trajectory depends on the FD programme's capitalised-spend pipeline through 2027.",
        "sources": [
            {"publisher": "Southern Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southernhealth.nhs.uk/about/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible Assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme — EPR rollout", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Southern Health NHS FT inspection reports (RW1)", "url": "https://www.cqc.org.uk/provider/RW1"},
            {"publisher": "NHS England", "title": "Mazars Independent Review of Deaths (Southern Health 2015)", "url": "https://www.england.nhs.uk/south/wp-content/uploads/sites/6/2015/12/mazars-rep.pdf"}
        ],
        "related": ["Southern Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Frontline Digitisation programme", "Amortisation — Oxford Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Leeds and York Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Leeds and York Partnership NHS Foundation Trust"}],
        "description": "LYPFT's £1.03M business-rates charge reflects VOA rateable values × 49.9p/54.6p UBR on c. 30+ occupied hereditaments — the Becklin Centre and Mount Hospital (Leeds), the Newsam Centre (Seacroft) housing CAMHS inpatient, the National Inpatient Centre for Psychological Medicine (Leeds), Asket Centre and community-MH bases plus historic York-area sites. NHS FTs do not qualify for charitable exemption; Leeds CC and York CC commercial RVs sit moderately above national average.",
        "beneficiaries": "c. 3,300 staff serving c. 800,000 residents of Leeds plus specialist services drawing nationally — including the National Inpatient Centre for Psychological Medicine (specialist persistent physical-symptoms service); CAMHS inpatient (Mill Lodge, Newsam Centre); perinatal and personality-disorder specialist services.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.03M"},
            {"label": "Hereditament count", "value": "c. 30+ occupied sites across Leeds + York footprints (acute MH, CAMHS, secure, community)"},
            {"label": "Billing authorities", "value": "Leeds CC + City of York Council"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Major sites driving line", "value": "Becklin Centre + Mount Hospital + Newsam Centre + Asket Centre + National Inpatient Centre for Psychological Medicine"},
            {"label": "VOA 2023 revaluation impact", "value": "Leeds + York commercial RVs rebased moderately; rateable values updated 1 Apr 2023 across estate"},
            {"label": "Specialist-services context", "value": "Inpatient Psych Medicine + Mill Lodge CAMHS draw nationally — bespoke construction = above-average RV/m²"},
            {"label": "NHSPS interaction", "value": "Community-clinic estate held via NHSPS lease — rates passed through to trust"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + Leeds CC + City of York Council billing"},
            {"label": "Policy owner", "value": "DHSC + MHCLG + NHSE Provider Finance + West Yorkshire ICB / Humber and North Yorkshire ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation · Successor: 2026 next revaluation under NDRA 2023 (3-year cycle)"}
        ],
        "notes": "LYPFT's rates line is moderate by MH-trust standards but elevated relative to the trust's £400M turnover — driven by the bespoke construction profile of specialist inpatient hereditaments (Newsam Centre CAMHS, the National Inpatient Centre for Psychological Medicine) which attract above-average RV per m² compared to standard ward space. The 2024 Non-Domestic Rating reform did not extend small-multiplier relief to NHS hereditaments, and the 2026 revaluation is the next material pinch-point; Leeds CC commercial RVs are expected to track national rebasing trends. NHSPS pass-through of community-clinic rates remains a recurring source of annual variability. CQC's 2024 'Good' rating frames a stable estate baseline.",
        "sources": [
            {"publisher": "Leeds and York Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsandyorkpft.nhs.uk/about/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Leeds and York Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Berkshire Healthcare NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "Business rates — Hertfordshire Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Hertfordshire Partnership University NHS Foundation Trust"}],
        "description": "HPFT's £1.02M business-rates line reflects VOA rateable values × 49.9p/54.6p UBR on c. 50+ occupied hereditaments — Kingfisher Court (Radlett), Lister Hospital MH ward (Stevenage), the Albany Lodge / Forest House (St Albans), Logandene (Hemel Hempstead), Robertson House and a network of community-MH bases across Hertfordshire, plus specialist-LD services in Norfolk, Essex and North Essex (under contracted provision). Hertfordshire commuter-belt commercial RVs sit moderately above national average.",
        "beneficiaries": "c. 3,500 staff serving c. 1.2M Hertfordshire residents; specialist forensic + LD services extending across the East of England; CAMHS coverage under sub-contract to Hertfordshire Community Trust partnership; eating-disorders specialist regional service.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.02M"},
            {"label": "Hereditament count", "value": "c. 50+ occupied sites across Hertfordshire + cross-border specialist services"},
            {"label": "Billing authorities", "value": "10 Hertfordshire district councils + cross-border billing authorities for specialist sites"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Major sites driving line", "value": "Kingfisher Court + Lister MH + Albany Lodge + Forest House + Logandene + Robertson House"},
            {"label": "Hertfordshire RV premium", "value": "Commuter-belt commercial RVs above national average; St Albans + Watford postcodes carry premium"},
            {"label": "VOA 2023 revaluation", "value": "Hertfordshire commercial RVs rebased; rateable values updated 1 Apr 2023"},
            {"label": "NHSPS interaction", "value": "Substantial community-MH estate held via NHSPS lease — rates passed through"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 10 Herts district billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG + NHSE Provider Finance + Herts and West Essex ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation · Successor: 2026 next revaluation under NDRA 2023"}
        ],
        "notes": "HPFT's rates line is shaped by the multi-district Hertfordshire footprint — ten district billing authorities to negotiate with — and the commuter-belt RV premium that pushes St Albans, Watford and Hertsmere commercial RVs above national average. The Kingfisher Court medium-secure unit and specialist eating-disorders inpatient sites attract above-average RVs because of bespoke construction. NHSPS pass-through of community-clinic rates is the dominant source of annual volatility. The 2024 NDR reform retained the differential between small and standard multipliers without extending relief to NHS hereditaments; the 2026 revaluation will rebase Hertfordshire RVs post the 2023 antecedent date. CQC 'Good' rating context underpins a stable estate baseline.",
        "sources": [
            {"publisher": "Hertfordshire Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hpft.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Hertfordshire Partnership University NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Leeds and York Partnership NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "PFI / LIFT charges — Sussex Partnership NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Sussex Partnership NHS Foundation Trust"}],
        "description": "Sussex Partnership's £1.00M PFI / LIFT line covers unitary-charge payments on the East Sussex and West Sussex LIFTCo community-clinic estate plus residual ancillary PFI obligations. Under IFRIC 12 service-concession accounting, the charge splits between service, finance and asset components. The trust delivers MH, CAMHS, learning-disability and specialist forensic services across Sussex and parts of Hampshire; the LIFT-vehicle estate underpins community-MH and IAPT clinic access.",
        "beneficiaries": "c. 4,800 staff serving c. 1.7M residents across East Sussex, West Sussex and Brighton & Hove plus specialist forensic and Hampshire CAMHS contracts; LIFT-vehicle clinic estate hosts community-MH, CAMHS, NHS Talking Therapies and ancillary services.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (where applicable) · DHSC Group Accounting Manual 2024-25 ch.7 + ch.8 · NHS (Local Improvement Finance Trust) framework · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.00M"},
            {"label": "Scheme type", "value": "LIFT (Local Improvement Finance Trust) community-clinic estate — East + West Sussex LIFTCo vehicles"},
            {"label": "Sites covered", "value": "Community-MH + CAMHS + IAPT clinics across East Sussex, West Sussex and Brighton & Hove"},
            {"label": "Unitary charge split", "value": "Service charge (FM, lifecycle, soft services) + finance cost + asset depreciation per IFRIC 12"},
            {"label": "Contract counterparty", "value": "Sussex LIFTCo vehicles (CHP-managed strategic partnering boards)"},
            {"label": "Programme owner", "value": "Community Health Partnerships Ltd (CHP) + DHSC + NHSE"},
            {"label": "Funding trajectory", "value": "Broadly flat — unitary charges indexed to RPI/CPI; £0.9-1.1M band sustained 2020-25"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + CHP head-tenant model"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Sussex ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI / LIFT reviews; CHP annual review; Public Accounts Committee 2018 PFI value-for-money report"},
            {"label": "Forensic-services context", "value": "The Hellingly Centre medium-secure unit operates outside LIFT (NHS-owned) — LIFT line covers community-clinic estate only"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT directly-owned community clinics · Successor: LIFT contract expiry programme through 2030s → handback or re-let"}
        ],
        "notes": "Sussex Partnership's PFI / LIFT line is dominated by the East and West Sussex LIFT estate, which between them house most of the trust's community-MH, CAMHS and Talking Therapies clinics across the three Sussex authorities. The unitary charge is indexed annually (RPI/CPI hybrid) and accounted under IFRIC 12 — splitting into service, finance and asset depreciation components. Sussex LIFTCos sit under CHP head-tenant governance. The major medium-term risk is LIFT contract expiry across the 2030s, when the trust + Sussex ICB must decide between handback, extension or replacement procurement; NAO has flagged sector-wide LIFT-expiry planning as weak. Service-charge components are also exposed to the NHSPS-style market-rent uplift dynamic.",
        "sources": [
            {"publisher": "Sussex Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sussexpartnership.nhs.uk/our-publications"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review and scheme directory", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 8 — Service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018) + LIFT scrutiny", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "HM Treasury", "title": "Private Finance Initiative and Private Finance 2 projects: 2023 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2023-summary-data"}
        ],
        "related": ["Sussex Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Oxleas NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Lancashire and South Cumbria NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Lancashire and South Cumbria NHS Foundation Trust"}],
        "description": "LSCFT's £1.00M general supplies & services line covers non-clinical consumables, ward provisions, hotel-services materials, laundry chemicals, cleaning supplies, kitchen consumables and general equipment across the Guild Lodge medium-secure unit (Preston), Avondale Unit (Royal Preston), the Harbour (Blackpool), Scarisbrick CMHT, Ridge Lea (Lancaster) and dispersed community-MH bases. The trust's broad MH + LD + autism + CAMHS remit across Lancashire and South Cumbria drives volume; Edenfield-cluster scrutiny on therapeutic environments has raised consumable expectations.",
        "beneficiaries": "c. 7,500 staff serving c. 1.8M residents across Lancashire and South Cumbria; c. 600 inpatient MH + LD + secure beds across Guild Lodge, Avondale, the Harbour, Scarisbrick and Ridge Lea; broad community-MH + CAMHS + perinatal + LD coverage.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£1.00M"},
            {"label": "Composition", "value": "Hotel-services consumables + laundry + cleaning + kitchen + ward general supplies + minor non-clinical equipment"},
            {"label": "Site footprint", "value": "Guild Lodge (medium-secure) + Avondale + The Harbour + Scarisbrick + Ridge Lea + dispersed community-MH bases"},
            {"label": "Headcount served", "value": "c. 7,500 substantive WTE"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (hotel services + cleaning + laundry) + local catering and consumables"},
            {"label": "Edenfield-cluster context", "value": "Sector-wide therapeutic-environment scrutiny post-Edenfield Panorama 2022 raised ward-consumable expectations (linen, single-use)"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.7M → 2024-25 £1.00M — uplift driven by CPI on consumables + sustained infection-control overhead"},
            {"label": "Delivery body", "value": "Trust Procurement + Hotel Services + Estates teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Model Hospital benchmarking; trust ARA 2023-24 inventory disclosure; CQC inspection reports"},
            {"label": "CQC context", "value": "Trust held 'Requires Improvement' rating since 2018; ward-environment + safety improvements drive consumable demand"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 trust merger (Lancashire Care + Cumbria Partnership MH) baseline · Successor: ICS-pooled procurement under LSC ICB + NHS Supply Chain reformed CIPS"}
        ],
        "notes": "LSCFT's general supplies & services line reflects the trust's significant secure-services footprint at Guild Lodge alongside dispersed community-MH provision across one of England's larger MH-trust catchments by area. The trust has held a CQC 'Requires Improvement' rating since 2018, with ward-environment and safety-related consumable spending sustained as part of the remediation programme. Post-Edenfield sector scrutiny has reinforced expectations around single-use linen, infection-control consumables and therapeutic-environment provisioning. NHS Supply Chain dominates procurement under reformed Category Tower governance. ICS-pooled procurement under LSC ICB is the medium-term lever; the planned new MH hospital programme could shift the consumable demand profile from c. 2027.",
        "sources": [
            {"publisher": "Lancashire and South Cumbria NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lscft.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS Supply Chain", "title": "Hotel services and cleaning category data", "url": "https://www.supplychain.nhs.uk/categories/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LSCFT inspection reports + provider profile (RW5)", "url": "https://www.cqc.org.uk/provider/RW5"},
            {"publisher": "NHS England", "title": "Model Hospital — non-clinical consumables benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"}
        ],
        "related": ["Lancashire and South Cumbria NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "Department of Health and Social Care", "General supplies & services — Derbyshire Healthcare NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Business rates — North East London NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "North East London NHS Foundation Trust"}],
        "description": "NELFT's £0.99M business-rates line reflects VOA rateable values × 49.9p/54.6p UBR on c. 80+ occupied hereditaments — Goodmayes Hospital (Ilford), Sunflowers Court (Goodmayes), Brookside CAMHS, the King George Hospital MH ward and dispersed community-MH and physical-health bases across Barking & Dagenham, Havering, Redbridge, Waltham Forest plus services in Essex (Basildon, Brentwood, Thurrock) and Kent. Outer-London billing-authority RVs sit moderately above national average.",
        "beneficiaries": "c. 6,500 staff serving c. 4.0M residents across NE London + parts of Essex and Kent; combined MH + community physical-health + CAMHS remit; Goodmayes is the main acute MH inpatient site; community-physical-health remit spans district nursing, school nursing and adult community services.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.99M"},
            {"label": "Hereditament count", "value": "c. 80+ occupied sites across NE London + Essex + Kent"},
            {"label": "Billing authorities", "value": "LB Redbridge + LB Barking & Dagenham + LB Havering + LB Waltham Forest + Basildon + Brentwood + Thurrock + cross-Kent"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Major sites driving line", "value": "Goodmayes Hospital + Sunflowers Court + Brookside CAMHS + King George MH ward"},
            {"label": "Outer-London RV premium", "value": "LB Redbridge / Havering commercial RVs above national average but below inner-London"},
            {"label": "Combined remit driver", "value": "Community-physical-health remit (district nursing, school nursing) means more small-clinic hereditaments than MH-only peers"},
            {"label": "NHSPS interaction", "value": "Substantial community estate held via NHSPS lease — rates passed through to trust as occupier"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 8+ billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG + NHSE Provider Finance + North East London ICB / Mid and South Essex ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation · Successor: 2026 next revaluation under NDRA 2023"}
        ],
        "notes": "NELFT's rates line is shaped by the geographically vast multi-authority footprint — eight or more billing authorities across NE London, Essex and Kent — and the volume of small community-clinic hereditaments needed to deliver district-nursing, school-nursing and CAMHS alongside core MH services. The cross-border Essex and Kent provision adds billing-authority complexity that pure London-borough-bound trusts avoid. NHSPS pass-through of community-clinic rates is the dominant volatility source. The 2024 NDR reform retained the small-vs-standard multiplier differential without extending relief to NHS hereditaments; the 2026 revaluation will rebase outer-London RVs post the 2023 antecedent date. CQC 'Good' rating context underpins a stable estate baseline.",
        "sources": [
            {"publisher": "North East London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nelft.nhs.uk/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["North East London NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Hertfordshire Partnership University NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "Impairments net of reversals — Barnet, Enfield And Haringey Mental Health NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Barnet, Enfield And Haringey Mental Health NHS Trust"}],
        "description": "BEH-MHT's £0.99M impairment line covers IAS 36 / IFRS 13 land + buildings revaluation losses recognised through I&E, net of any reversals on previously-impaired assets. The trust's estate — Chase Farm MH building (Enfield), St Ann's Hospital (Tottenham), Edgware Community Hospital MH wards, plus community-MH bases — is subject to annual District Valuer revaluation under DHSC GAM 2024-25 ch.4. Impairment volatility reflects North London land-value swings + estate-rationalisation under the trust's planned Camden & Islington merger.",
        "beneficiaries": "c. 1,800 staff serving c. 1.0M residents of Barnet, Enfield and Haringey; c. 250 inpatient MH beds; the trust is mid-way through a planned merger with Camden and Islington NHS FT to form the North London Mental Health Partnership (transition completed 2024-25 financial year).",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS 13 Fair Value Measurement · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IAS 1 Presentation of Financial Statements",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£0.99M"},
            {"label": "Asset class", "value": "Land + buildings (modern equivalent asset valuation under DHSC GAM ch.4)"},
            {"label": "Valuation methodology", "value": "Annual District Valuer Services indexation + 5-year full revaluation cycle"},
            {"label": "Driver of impairment", "value": "North London land-value swings + St Ann's redevelopment land disposal flagged + estate-rationalisation under merger"},
            {"label": "Estate footprint", "value": "Chase Farm MH building (Enfield) + St Ann's Hospital (Tottenham) + Edgware MH wards + community-MH bases"},
            {"label": "Camden + Islington merger", "value": "North London Mental Health Partnership formal merger Oct 2024 — successor trust absorbs estate"},
            {"label": "Reversal vs new impairment split", "value": "Net figure — reversals on previously-impaired land partially offset new-build / refurb cost-vs-MEAV gaps"},
            {"label": "Funding trajectory", "value": "Highly volatile year-on-year — driven by valuation cycle + estate disposal events"},
            {"label": "Delivery body", "value": "Trust Finance + Estates + VOA District Valuer Services"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 PPE note disclosure; DHSC GAM 2024-25 ch.4 guidance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2024 separate BEH-MHT trust valuations · Successor: North London Mental Health Partnership consolidated valuation from 2024-25"}
        ],
        "notes": "BEH-MHT's impairment line is dominated by the cyclical revaluation of its London-located estate — Chase Farm MH building (within the Royal Free Group footprint), the St Ann's Hospital site (which has been the subject of redevelopment and partial land disposal to Catalyst Housing), and Edgware Community Hospital MH wards. Modern Equivalent Asset Valuation (MEAV) under DHSC GAM ch.4 introduces structural volatility because newly-refurbished or built assets typically attract impairment in the first year (build cost > MEAV). The merger with Camden and Islington into the North London Mental Health Partnership (completed October 2024) reframes the estate question: 2024-25 is the last year of stand-alone BEH-MHT accounts, with consolidated successor accounting from 2025-26.",
        "sources": [
            {"publisher": "Barnet, Enfield and Haringey Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.beh-mht.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 4 — PPE)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Valuation Office Agency", "title": "District Valuer Services — NHS revaluations", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "North London Mental Health Partnership", "title": "Merger transition documentation 2024", "url": "https://www.northlondonmentalhealth.nhs.uk/"},
            {"publisher": "NHS England", "title": "Provider valuation framework guidance", "url": "https://www.england.nhs.uk/financial-accounting-and-reporting/"}
        ],
        "related": ["Barnet, Enfield And Haringey Mental Health NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Impairments net of reversals — Leeds and York Partnership NHS Foundation Trust", "Camden and Islington NHS Foundation Trust"]
    },
    "Amortisation — Nottinghamshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Nottinghamshire Healthcare NHS Foundation Trust"}],
        "description": "Nottinghamshire Healthcare's £0.98M amortisation line reflects systematic write-down of intangible assets — software licences, capitalised EPR development cost (Rampton EPR + community Rio replacement), capitalised training and minor brand/website assets — across the trust's MH + LD + forensic + community-physical-health portfolio. The line stepped up post-2022 as Frontline Digitisation programme spend on EPR consolidation flowed into amortisation; useful-life policy is 3-7 years per DHSC GAM 2024-25 ch.5.",
        "beneficiaries": "c. 9,500 staff serving c. 1.1M Nottinghamshire residents plus the Rampton Hospital high-secure national service; intangibles support clinical record-keeping at high-secure (Rampton), medium-secure (Wathwood), low-secure, acute MH (Highbury) and community-physical-health teams.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.98M"},
            {"label": "Asset class", "value": "Software licences + capitalised EPR development + capitalised training + minor brand/website assets"},
            {"label": "Useful-life policy", "value": "3-7 years per DHSC GAM 2024-25 ch.5"},
            {"label": "High-secure context", "value": "Rampton Hospital national high-secure service requires bespoke clinical-record + security system intangibles"},
            {"label": "Frontline Digitisation context", "value": "Post-2022 step-up reflecting capitalised FD programme spend on EPR consolidation"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.5M → 2024-25 £0.98M — sustained growth tracking FD capitalisation pipeline + Rampton-bespoke intangibles"},
            {"label": "Amortisation method", "value": "Straight-line over assessed useful life — annual impairment review per IAS 38"},
            {"label": "Delivery body", "value": "Trust Finance + Digital Services + Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation programme + Nottingham and Nottinghamshire ICB + NHSE Specialised Commissioning (Rampton)"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reviews; trust ARA 2023-24 intangibles disclosure; HSSIB high-secure investigations"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 legacy systems · Successor: consolidated FD-funded EPR fully amortised over 5-7 year cycle"},
            {"label": "Specialist intangibles", "value": "Rampton high-secure system + sex-offender treatment programme materials + DSPD-legacy assets"}
        ],
        "notes": "Nottinghamshire Healthcare's amortisation line is shaped by its dual identity as a regional MH + community provider AND a national high-secure provider at Rampton Hospital — the latter requires bespoke clinical-record, security and case-management intangibles that fall outside generic NHS EPR contracts. Frontline Digitisation programme capitalisation has driven sustained growth in the line since 2022. Useful-life policy aligns to DHSC GAM 2024-25 ch.5, with annual IAS 38 impairment reviews introducing volatility when modules are deprecated. The medium-term trajectory depends on the FD programme's capitalised-spend pipeline and on Rampton-specific digital investment under NHSE Specialised Commissioning. Recent HSSIB and Lampard inquiry context places digital safeguarding at sustained scrutiny.",
        "sources": [
            {"publisher": "Nottinghamshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nottinghamshirehealthcare.nhs.uk/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible Assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme — EPR rollout", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Nottinghamshire Healthcare NHS FT inspection reports (RHA)", "url": "https://www.cqc.org.uk/provider/RHA"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Mental health investigations 2023-24", "url": "https://www.hssib.org.uk/"}
        ],
        "related": ["Nottinghamshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Frontline Digitisation programme", "Amortisation — Southern Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Drugs costs — Lincolnshire Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Lincolnshire Partnership NHS Foundation Trust"}],
        "description": "LPFT's £0.97M drugs cost line covers psychotropic medications dispensed across the trust's MH inpatient and community services in Lincolnshire — antipsychotics (clozapine, olanzapine, risperidone, aripiprazole), mood stabilisers (lithium, sodium valproate), antidepressants (SSRIs, SNRIs), benzodiazepines and depot injectable formulations. The line is shaped by clozapine monitoring volumes (treatment-resistant schizophrenia caseload), depot prescribing for community-MH continuity, and the gradual shift toward long-acting injectables.",
        "beneficiaries": "c. 2,200 staff serving c. 770,000 Lincolnshire residents; c. 250 acute MH + LD + older-people inpatient beds across the Peter Hodgkinson Centre (Lincoln), Hartsholme (Lincoln), Witham Court (Lincoln) and Ash Villa (Sleaford); community-MH + CAMHS coverage county-wide.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · Misuse of Drugs Act 1971 · Human Medicines Regulations 2012 · NHS Act 2006 · Health and Care Act 2022 · MHRA Yellow Card pharmacovigilance",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.97M"},
            {"label": "Composition", "value": "Antipsychotics + mood stabilisers + antidepressants + benzodiazepines + depots + clozapine + ADHD stimulants"},
            {"label": "Site footprint", "value": "Peter Hodgkinson Centre + Hartsholme + Witham Court + Ash Villa + community-MH bases"},
            {"label": "Headcount served", "value": "c. 2,200 substantive WTE supporting c. 770,000 catchment"},
            {"label": "Clozapine monitoring caseload", "value": "Bespoke clozapine-clinic + ZTAS / Clozaril / Denzapine monitoring infrastructure"},
            {"label": "Depot prescribing share", "value": "Sustained share of long-acting injectables (paliperidone, aripiprazole) for community-MH continuity"},
            {"label": "Procurement route", "value": "NHS Supply Chain pharmacy + CMU framework + local hospital pharmacy"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.7M → 2024-25 £0.97M — uplift driven by drug-tariff CPI + caseload + new long-acting formulations"},
            {"label": "Delivery body", "value": "Trust Pharmacy team + ICB Medicines Optimisation"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Lincolnshire ICB · MHRA pharmacovigilance + NICE TA guidance"},
            {"label": "Evaluation evidence", "value": "NICE technology appraisals (TAs) for second-generation antipsychotics; CQC inspection reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: first-generation typical antipsychotic-dominated regime · Successor: continued shift toward long-acting injectables + ADHD-medication community caseload growth"}
        ],
        "notes": "LPFT's drugs cost line is modest relative to peers because the trust serves a single rural-county footprint with no high-secure or specialist tertiary services. The bulk of spend is psychotropics — antipsychotics, mood stabilisers and antidepressants — with clozapine and long-acting injectable depots as the structural high-cost components. NICE technology appraisals and the NHS drug tariff govern unit pricing, with annual CPI-driven uplift. The growing ADHD-medication community caseload and the gradual switch to second-generation long-acting injectables are the medium-term cost drivers; ICB-level Medicines Optimisation is the main lever. CQC's 2023 inspection prompted closer scrutiny of as-PRN prescribing patterns.",
        "sources": [
            {"publisher": "Lincolnshire Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lpft.nhs.uk/about-us/publications/annual-reports-and-accounts"},
            {"publisher": "NHS Business Services Authority", "title": "NHS drug tariff and ePACT data", "url": "https://www.nhsbsa.nhs.uk/pharmacies-gp-practices-and-appliance-contractors/drug-tariff"},
            {"publisher": "National Institute for Health and Care Excellence", "title": "Mental health technology appraisals (TAs)", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/mental-health-and-behavioural-conditions"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Lincolnshire Partnership NHS FT inspection reports (RP7)", "url": "https://www.cqc.org.uk/provider/RP7"}
        ],
        "related": ["Lincolnshire Partnership NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "Department of Health and Social Care", "Drugs costs — Tavistock and Portman NHS Foundation Trust", "NICE technology appraisals"]
    },
    "Lease expenditure — Dorset Healthcare University NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Dorset Healthcare University NHS Foundation Trust"}],
        "description": "Dorset Healthcare's £0.97M lease line reflects IFRS 16 right-of-use asset depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services + CHP LIFT-vehicle leases for community-MH and physical-health clinics across Bournemouth, Christchurch, Poole, Weymouth, Dorchester and rural Dorset, plus St Ann's Hospital (Poole) MH ancillary leased space.",
        "beneficiaries": "c. 5,500 staff serving c. 800,000 Dorset residents through a combined MH + community-physical-health + CAMHS + LD trust; c. 70+ community sites + 4 community hospitals + St Ann's MH inpatient; rural mid-/west-Dorset has higher per-site lease ratio than urban Bournemouth/Poole.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.97M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with corresponding depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 70+ NHSPS + CHP-LIFT premises + ancillary St Ann's space + community-hospital co-location"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Combined remit driver", "value": "MH + community-physical-health + CAMHS + LD trust → high site-count base across rural Dorset"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.5M operating lease → 2022-23 c. £0.8M ROU first year → 2024-25 £0.97M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Dorset ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + Dorset ICS estate consolidation"}
        ],
        "notes": "Dorset Healthcare's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet, and has continued to grow modestly as NHSPS pursued market-rent uplifts on community clinics. The trust's combined MH + community-physical-health remit means it occupies more small NHSPS-leased premises than MH-only peers, exposing it more to NHSPS dispute volatility. Rural mid- and west-Dorset community sites have lower individual rents but higher per-site count, complicating procurement consolidation. The Dorset ICS Clinical Strategy 2023 includes estate-consolidation lines that could rebalance the leased footprint over the 2025-2030 horizon. Dorset's high deprivation/affluence-mix coastal-rural geography sustains this dispersed model.",
        "sources": [
            {"publisher": "Dorset Healthcare University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dorsethealthcare.nhs.uk/about-us/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Dorset Integrated Care Board", "title": "Dorset ICS Clinical Strategy 2023", "url": "https://nhsdorset.nhs.uk/"}
        ],
        "related": ["Dorset Healthcare University NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Mersey Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Hertfordshire Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Hertfordshire Partnership University NHS Foundation Trust"}],
        "description": "HPFT's £0.95M establishment line covers stationery, postage, telephony, mobile-device estate, printing and courier across Kingfisher Court (Radlett), Lister MH ward (Stevenage), Albany Lodge / Forest House (St Albans), Logandene (Hemel Hempstead) and a network of community-MH bases plus specialist forensic + LD services across the East of England. The multi-district Hertfordshire footprint and dispersed community-MH model drive the line; the trust's 'University' designation reflects sustained academic-partnership activity that adds modest establishment overhead.",
        "beneficiaries": "c. 3,500 staff serving c. 1.2M Hertfordshire residents; specialist forensic + LD services extending across the East of England; CAMHS coverage under sub-contract to Hertfordshire Community Trust partnership; eating-disorders specialist regional service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£0.95M"},
            {"label": "Site footprint driving line", "value": "Kingfisher Court + Lister MH + Albany Lodge + Forest House + Logandene + Robertson House + community-MH bases"},
            {"label": "Headcount served", "value": "c. 3,500 substantive WTE"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying"},
            {"label": "Mobile-device estate", "value": "Sustained increase post-2020 community-mobile-working programme — laptops, smartphones for AMHP + community-MH teams"},
            {"label": "University designation", "value": "Academic partnership (e.g. University of Hertfordshire) adds modest research + teaching establishment overhead"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + Crown Commercial Service telephony framework"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.7M → 2024-25 £0.95M — sustained growth tracking community-mobile-working + CPI"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Herts and West Essex ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; NHSE Model Hospital benchmarking shows MH community trusts running 1.5-2.0% of turnover on establishment"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paper-heavy office model · Successor: digital-first community workflow under Frontline Digitisation EPR rollout"}
        ],
        "notes": "HPFT's establishment line is shaped by the multi-district Hertfordshire footprint — ten district authorities across one of England's larger county catchments — and the dispersed community-MH delivery model that supports AMHP rotas, crisis-team home assessments and specialist forensic outreach. The trust's University designation in partnership with the University of Hertfordshire adds a modest academic-overhead component. Frontline Digitisation EPR rollout (Rio replacement, programmed mid-2020s) is expected to compress printing and postage but raise mobile-device, licensing and connectivity costs, leaving net establishment broadly flat in real terms. CQC 'Good' rating context underpins a stable cost baseline.",
        "sources": [
            {"publisher": "Hertfordshire Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hpft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Office consumables and stationery framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS England", "title": "Model Hospital — community + mental health benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "HPFT provider profile (RWR)", "url": "https://www.cqc.org.uk/provider/RWR"}
        ],
        "related": ["Hertfordshire Partnership University NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Berkshire Healthcare NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Business rates — Black Country Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Black Country Healthcare NHS Foundation Trust"}],
        "description": "BCHFT's £0.94M business-rates line reflects VOA rateable values × 49.9p/54.6p UBR on c. 50+ occupied hereditaments — the Penn Hospital (Wolverhampton), the Edward Street Hospital (West Bromwich), Hallam Street (West Bromwich), Bushey Fields Hospital (Dudley), Bloxwich Hospital and dispersed community-MH bases across the four Black Country authorities. Black Country commercial RVs sit below national average — partly mitigating the multi-authority site count.",
        "beneficiaries": "c. 3,500 staff serving c. 1.2M residents across Wolverhampton, Sandwell, Walsall and Dudley (the four Black Country boroughs); MH + LD + CAMHS + perinatal + specialist services; the 2020 reformation of BCHFT consolidated former Black Country Partnership + Dudley & Walsall MH services.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.94M"},
            {"label": "Hereditament count", "value": "c. 50+ occupied sites across the four Black Country authorities"},
            {"label": "Billing authorities", "value": "Wolverhampton CC + Sandwell MBC + Walsall MBC + Dudley MBC"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Black Country RV context", "value": "Commercial RVs below West Midlands average — partial offset to multi-site count"},
            {"label": "Major sites driving line", "value": "Penn Hospital + Edward Street + Hallam Street + Bushey Fields + Bloxwich Hospital"},
            {"label": "VOA 2023 revaluation impact", "value": "Black Country commercial RVs largely unchanged or slightly down post-pandemic; partial mitigation"},
            {"label": "NHSPS interaction", "value": "Significant share of community-MH estate held via NHSPS lease — rates passed through"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 4 Black Country billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG + NHSE Provider Finance + Black Country ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation under separate trust structures · Successor: 2026 next revaluation under NDRA 2023"}
        ],
        "notes": "BCHFT's rates line is moderate by MH-trust standards because Black Country commercial RVs sit below the West Midlands and national averages — a modest structural offset to the trust's multi-authority footprint. The 2020 trust reformation (consolidating former Black Country Partnership and Dudley + Walsall MH services) introduced estate-rationalisation opportunities that are being progressed under the Black Country ICB Estates Strategy. NHSPS pass-through of community-clinic rates remains the dominant volatility source. The 2024 NDR reform retained the small-vs-standard multiplier differential without extending relief to NHS hereditaments; the 2026 revaluation is expected to track national rebasing trends.",
        "sources": [
            {"publisher": "Black Country Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.blackcountryhealthcare.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Black Country Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Birmingham and Solihull Mental Health NHS Foundation Trust", "NHS Property Services Ltd"]
    },
    "Impairments net of reversals — Nottinghamshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Nottinghamshire Healthcare NHS Foundation Trust"}],
        "description": "Nottinghamshire Healthcare's £0.92M impairment line covers IAS 36 / IFRS 13 land + buildings revaluation losses recognised through I&E, net of any reversals on previously-impaired assets. The trust's estate spans Rampton Hospital high-secure (Retford), Wathwood medium-secure, Highbury Hospital (Bulwell), the Wells Road Centre, and dispersed MH + community-physical-health bases. Modern Equivalent Asset Valuation under DHSC GAM ch.4 + the bespoke high-secure construction profile create structural impairment volatility.",
        "beneficiaries": "c. 9,500 staff serving c. 1.1M Nottinghamshire residents plus the Rampton Hospital national high-secure service drawing nationally; estate impairment volatility affects depreciation policy for clinical service planning across MH, LD, forensic and community-physical-health remits.",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS 13 Fair Value Measurement · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IAS 1 Presentation of Financial Statements",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£0.92M"},
            {"label": "Asset class", "value": "Land + buildings (modern equivalent asset valuation under DHSC GAM ch.4)"},
            {"label": "Valuation methodology", "value": "Annual District Valuer Services indexation + 5-year full revaluation cycle"},
            {"label": "Driver of impairment", "value": "Bespoke Rampton high-secure construction (cost > MEAV) + medium-secure Wathwood + new-build vs MEAV gaps"},
            {"label": "Estate footprint", "value": "Rampton + Wathwood + Highbury + Wells Road + dispersed community-MH and community-physical-health bases"},
            {"label": "High-secure context", "value": "Rampton requires bespoke security construction (perimeter, ligature-resistant, observation) attracting impairment vs generic MEAV"},
            {"label": "Reversal vs new impairment split", "value": "Net figure — reversals on indexed land partially offset new-build / refurb cost-vs-MEAV impairment"},
            {"label": "Funding trajectory", "value": "Highly volatile year-on-year — driven by valuation cycle + capital-programme events"},
            {"label": "Delivery body", "value": "Trust Finance + Estates + VOA District Valuer Services"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Nottingham and Nottinghamshire ICB + NHSE Specialised Commissioning (Rampton)"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 PPE note disclosure; DHSC GAM 2024-25 ch.4 guidance; NAO MH estate scrutiny"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 historic-cost basis · Successor: ongoing 5-year revaluation cycle + Rampton capital-programme drives"}
        ],
        "notes": "Nottinghamshire Healthcare's impairment line is structurally elevated by the bespoke construction profile of Rampton Hospital — high-secure perimeter, ligature-resistant fittings, observation infrastructure and security-grade plant — which routinely costs more than the generic Modern Equivalent Asset Valuation used under DHSC GAM ch.4, generating first-year impairment on capital-programme outputs. Wathwood medium-secure and the Highbury acute-MH site add similar but smaller bespoke-construction gaps. Annual DVS indexation + 5-year full revaluation cycle introduce additional cyclical volatility. The line will continue to track Rampton's capital-programme cadence; HSSIB and Lampard inquiry context places sustained scrutiny on high-secure estate adequacy, sustaining capital investment ahead.",
        "sources": [
            {"publisher": "Nottinghamshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nottinghamshirehealthcare.nhs.uk/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 4 — PPE)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Valuation Office Agency", "title": "District Valuer Services — NHS revaluations", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "NHS England", "title": "High-secure mental-health estate framework", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-c/c02/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Mental health investigations 2023-24", "url": "https://www.hssib.org.uk/"}
        ],
        "related": ["Nottinghamshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Impairments net of reversals — Barnet, Enfield And Haringey Mental Health NHS Trust", "Amortisation — Nottinghamshire Healthcare NHS Foundation Trust"]
    },
}
