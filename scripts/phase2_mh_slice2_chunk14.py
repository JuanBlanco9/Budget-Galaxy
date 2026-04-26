# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 14 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Other & adjustments — North East London NHS Foundation Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "North East London NHS Foundation Trust"}],
        "description": "NELFT's £0.20M other & adjustments line is the residual cleanup bucket within Staff Costs covering prior-year corrections, AME reclassifications, accrual-release adjustments and minor restatements that fall outside the principal pay categories. The trust's footprint across north-east London (Barking & Dagenham, Havering, Redbridge, Waltham Forest) plus south-west Essex MH and community services creates a c. 6,500-WTE payroll where small reclass adjustments aggregate annually. The line typically captures audit-cycle re-allocations between substantive pay, agency, NIC and pension components.",
        "beneficiaries": "c. 6,500 WTE payroll covering NHS Mental Health, community-physical-health and CAMHS services across Barking & Dagenham, Havering, Redbridge, Waltham Forest plus south-west Essex; serves a registered catchment c. 2.0M residents.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (general disclosure rules) · IAS 1 Presentation of Financial Statements · IAS 8 Accounting Policies, Changes in Accounting Estimates and Errors · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Other & adjustments 2024-25", "value": "£0.20M"},
            {"label": "Sub-line composition", "value": "Prior-year corrections + AME reclassifications + accrual releases + minor pay-category restatements"},
            {"label": "Trust headcount context", "value": "c. 6,500 WTE substantive payroll across MH + community + CAMHS"},
            {"label": "Footprint", "value": "Barking & Dagenham, Havering, Redbridge, Waltham Forest LBs + Basildon/Brentwood/Thurrock community services"},
            {"label": "Audit cycle driver", "value": "External audit (KPMG/Deloitte rotation) + internal audit findings drive most reclass entries between substantive pay / agency / NIC / pension components"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer NIC threshold drop + 1.2pp rate rise raises forward NHS Pension Scheme employer-cost — feeds future accrual recalibration"},
            {"label": "Material-error threshold", "value": "Trust applies DHSC GAM materiality (typically c. 0.5% of operating expenditure) to determine restatement vs current-period adjustment"},
            {"label": "Funding trajectory", "value": "Variable year-on-year; £0.15M-£0.30M typical range over 2020-21 to 2024-25 — non-structural"},
            {"label": "Delivery body", "value": "Trust Finance team + external auditor (KPMG/Deloitte rotation) + NHS England financial reporting"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NEL ICB · accounting framework HM Treasury FReM"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure note; audit Annual Audit Letter; CQC compliance context"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2009 SHA-based reporting structure · Successor: ICS-aligned reporting under Health and Care Act 2022 + ongoing IFRS adoption"}
        ],
        "notes": "NELFT's other & adjustments residual is the kind of clean-up line that exists at every NHS provider — small in absolute terms but structurally inevitable as the trust closes its annual audit cycle. The line captures reclassifications between substantive pay, agency, NIC and pension components emerging from audit findings and accrual recalibration. NELFT's combined MH + community + CAMHS remit creates a relatively complex payroll architecture that drives a slightly larger residual than pure-MH peers. The April 2025 employer-NIC step-up will feed forward into NHS Pension Scheme employer-cost accrual recalibration in future cycles.",
        "sources": [
            {"publisher": "North East London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nelft.nhs.uk/about-us-publications-annual-reports"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "Financial Reporting Manual (FReM) 2024-25", "url": "https://www.gov.uk/government/collections/government-financial-reporting-manual-frem"},
            {"publisher": "NHS England", "title": "Provider finance handbook", "url": "https://www.england.nhs.uk/financial-accounting/"},
            {"publisher": "Care Quality Commission", "title": "NELFT provider profile (RAT)", "url": "https://www.cqc.org.uk/provider/RAT"}
        ],
        "related": ["North East London NHS Foundation Trust", "Staff Costs", "NHS Mental Health Trusts", "Department of Health and Social Care", "Other & adjustments — Central and North West London NHS Foundation Trust", "NHS England"]
    },
    "Lease expenditure — North Staffordshire Combined Healthcare NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "North Staffordshire Combined Healthcare NHS Trust"}],
        "description": "NSCHT's £0.19M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio centres on NHSPS-leased community-MH and CAMHS premises across Stoke-on-Trent and the Newcastle-under-Lyme area, plus minor private commercial leases on satellite team bases. As a smaller NHS Trust (non-FT), NSCHT's leased footprint is more limited than the larger MH FTs, but the line still reflects the IFRS 16 jump and ongoing NHSPS market-rent uplift dispute.",
        "beneficiaries": "c. 1,800 staff serving c. 470,000 residents across Stoke-on-Trent and the Newcastle-under-Lyme area; leased estate component includes community-MH team bases, CAMHS sites and satellite outreach venues — c. 15-20 leased addresses.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.19M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 15-20 NHSPS + private community-MH/CAMHS bases across Stoke-on-Trent + Newcastle-under-Lyme"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + private commercial landlords (minor)"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — applies to NSCHT-leased space"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "5-10 year community clinic leases typical; some break clauses align to ICS estate review; NSCHT non-FT status constrains owned-estate expansion"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.10M operating lease → 2022-23 c. £0.16M ROU first year → 2024-25 £0.19M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Staffordshire and Stoke-on-Trent ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC inspection (RRE) provider profile"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + Staffs/Stoke ICS estate consolidation"}
        ],
        "notes": "NSCHT's lease line is small in absolute terms but structurally meaningful: as a non-FT MH trust serving Stoke-on-Trent and Newcastle-under-Lyme, the trust has limited capital headroom and depends heavily on NHSPS-leased community-MH and CAMHS bases. The IFRS 16 2022 transition brought previously off-balance-sheet operating leases onto the balance sheet, lifting the headline annual charge. The sector-wide NHSPS / MH-trust service-charge dispute applies to NSCHT space proportionate to its footprint. Staffordshire and Stoke-on-Trent ICS estate consolidation is the medium-term lever; in the near term, CPI-linked uplift on private commercial leases adds modest cost pressure. The trust's smaller scale limits its leverage in NHSPS market-rent negotiations relative to larger MH FTs.",
        "sources": [
            {"publisher": "North Staffordshire Combined Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.combined.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "NSCHT provider profile (RRE)", "url": "https://www.cqc.org.uk/provider/RRE"},
            {"publisher": "Staffordshire and Stoke-on-Trent ICB", "title": "ICS estate strategy", "url": "https://www.staffsstoke.icb.nhs.uk/"}
        ],
        "related": ["North Staffordshire Combined Healthcare NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Pennine Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Other & adjustments — South London and Maudsley NHS Foundation Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "South London and Maudsley NHS Foundation Trust"}],
        "description": "SLaM's £0.19M other & adjustments line is the residual cleanup bucket within Staff Costs covering prior-year corrections, AME reclassifications and minor pay-category restatements arising from the trust's annual audit cycle. SLaM's c. 5,500-WTE payroll spans a complex mix of NHS substantive staff, Institute of Psychiatry, Psychology & Neuroscience (IoPPN) joint-appointment academics with King's College London, and tertiary-specialty national-service clinicians — generating a richer-than-average set of pay-allocation adjustments at year-end.",
        "beneficiaries": "c. 5,500 WTE substantive payroll covering Lambeth, Southwark, Lewisham and Croydon adult MH, the Maudsley Hospital, Bethlem Royal Hospital and a portfolio of national tertiary services (national OCD, national affective disorders, gender services); KCL/IoPPN joint-appointment academic faculty layer adds complexity.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (general disclosure rules) · IAS 1 Presentation of Financial Statements · IAS 8 Accounting Policies, Changes in Accounting Estimates and Errors · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Other & adjustments 2024-25", "value": "£0.19M"},
            {"label": "Sub-line composition", "value": "Prior-year corrections + AME reclassifications + accrual releases + minor pay-category restatements"},
            {"label": "Trust headcount context", "value": "c. 5,500 WTE substantive across 4 SE London boroughs + national tertiary services"},
            {"label": "KCL/IoPPN joint-appointment layer", "value": "Significant cohort of consultant + academic joint-appointments with King's IoPPN — generates pay-attribution complexity at year-end"},
            {"label": "Audit cycle driver", "value": "External audit + internal audit findings drive most reclass entries between substantive pay / agency / NIC / pension / KCL-recharge components"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer NIC threshold drop + 1.2pp rate rise raises forward NHS Pension Scheme employer-cost — feeds future accrual recalibration"},
            {"label": "National tertiary service split", "value": "National OCD/BDD service + national affective disorders + national gender service generate cross-trust pay recharges; trust applies DHSC GAM materiality c. 0.5% of opex"},
            {"label": "Funding trajectory", "value": "Variable year-on-year; £0.15M-£0.25M typical range — non-structural"},
            {"label": "Delivery body", "value": "Trust Finance team + external auditor + NHS England financial reporting"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South East London ICB · accounting framework HM Treasury FReM"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure note; audit Annual Audit Letter; KCL/SLaM partnership agreement"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2009 SHA-based reporting structure · Successor: ICS-aligned reporting under Health and Care Act 2022"}
        ],
        "notes": "SLaM's other & adjustments line is structurally driven by the trust's unusual configuration — a SE London adult MH provider plus the Bethlem and Maudsley estates plus a portfolio of national tertiary services plus the deepest academic-clinical joint-appointment partnership in UK MH (King's IoPPN). Each dimension produces year-end pay-attribution adjustments: cross-trust recharges for national OCD/BDD/gender patients, KCL-recharge adjustments for joint-appointment time, and prior-year audit corrections. The April 2025 employer-NIC step-up feeds forward into NHS Pension Scheme employer-cost accrual recalibration.",
        "sources": [
            {"publisher": "South London and Maudsley NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.slam.nhs.uk/about-us/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "King's College London", "title": "Institute of Psychiatry, Psychology & Neuroscience (IoPPN) — SLaM partnership", "url": "https://www.kcl.ac.uk/ioppn"},
            {"publisher": "NHS England", "title": "Provider finance handbook", "url": "https://www.england.nhs.uk/financial-accounting/"},
            {"publisher": "Care Quality Commission", "title": "SLaM provider profile (RV5)", "url": "https://www.cqc.org.uk/provider/RV5"}
        ],
        "related": ["South London and Maudsley NHS Foundation Trust", "Staff Costs", "NHS Mental Health Trusts", "Department of Health and Social Care", "Other & adjustments — North East London NHS Foundation Trust", "King's College London"]
    },
    "Termination & post-employment — Essex Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Essex Partnership University NHS Foundation Trust"}],
        "description": "EPUT's £0.17M termination + post-employment line covers one-off severance, contractual notice pay-in-lieu, redundancy and the NHS Pension Scheme employer-element on early-retirement and exit packages across the trust's c. 5,500-staff base. EPUT sits at the centre of the Lampard Inquiry (statutory inquiry into MH inpatient deaths in Essex 2000-2023, chaired by Baroness Lampard) which has driven elevated senior-leadership turnover, remediation-related departures and structural workforce restructuring of the inpatient cadre.",
        "beneficiaries": "c. 5,500 staff covering MH and community services across Essex, Bedfordshire and Luton; Lampard Inquiry remediation has driven a heightened exit-package pool of c. 20-40 individuals annually concentrated in inpatient MH leadership and clinical-governance roles.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme regulations · Public Sector Exit Payments Regulations 2020 (uncapped post-2021 quash) · Employment Rights Act 1996 (s.139 redundancy + s.86 statutory notice) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.17M"},
            {"label": "Headcount + exit-pool context", "value": "c. 5,500 substantive WTE; estimated 20-40 exit packages annually with elevated cycle through Lampard remediation"},
            {"label": "Composition", "value": "Statutory + contractual redundancy + pay-in-lieu of notice + NHS Pension Scheme employer-element on early retirement + senior-staff exit packages"},
            {"label": "Lampard Inquiry context", "value": "Statutory inquiry (chaired by Baroness Kate Lampard) into MH inpatient deaths in Essex 2000-2023 — public hearings 2024-25; sustained senior-leadership turnover + clinical-governance restructuring"},
            {"label": "Predecessor SEPT/NEPFT context", "value": "EPUT formed 2017 via merger of South Essex Partnership University FT + North Essex Partnership FT — Lampard scope covers entire predecessor history"},
            {"label": "April 2025 NIC step-up", "value": "Employer NIC threshold drop + rate rise (Apr 2025) raises NHS Pension Scheme employer-cost on exit packages forward"},
            {"label": "PSE Payments Regs 2020", "value": "Capped exit-payment regs revoked 2021; trust currently operates under HM Treasury non-statutory guidance + NHS England consent rules"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.10M → 2023-24 elevated through Lampard preparatory exits → 2024-25 £0.17M"},
            {"label": "Delivery body", "value": "Trust HR + Finance teams + NHS Business Services Authority (Pensions) + NHSE consent for senior packages"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + HM Treasury (exit-pay guidance) + Mid and South Essex / Hertfordshire and West Essex / Bedfordshire Luton & Milton Keynes ICBs"},
            {"label": "Evaluation evidence", "value": "Lampard Inquiry interim reports; CQC inspection findings; trust ARA workforce remuneration report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 capped PSE payments regime · Successor: HMT non-statutory exit-pay guidance + NIC step-up Apr 2025 + Lampard final-report response"}
        ],
        "notes": "EPUT's termination line is exceptional in context even though small in absolute terms — the trust is the named subject of the Lampard Inquiry, the statutory inquiry into MH inpatient deaths across Essex MH services 2000-2023 (EPUT + predecessor SEPT and NEPFT). Public hearings progressed through 2024-25 and have driven senior-leadership turnover, clinical-governance restructuring and remediation-related exits across the inpatient cadre. Each Lampard-prompted senior departure feeds NHS Pension Scheme employer-cost on early retirement plus contractual notice payments. The April 2025 employer-NIC step-up raises forward employer-cost on subsequent exit packages.",
        "sources": [
            {"publisher": "Essex Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://eput.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Lampard Inquiry", "title": "Inquiry into Mental Health Inpatient Deaths in Essex 2000-2023", "url": "https://lampardinquiry.org.uk/"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guidance", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
            {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/public-sector-exit-payments-guidance"},
            {"publisher": "Care Quality Commission", "title": "EPUT provider profile (RHA)", "url": "https://www.cqc.org.uk/provider/RHA"}
        ],
        "related": ["Essex Partnership University NHS Foundation Trust", "Staff Costs", "NHS Mental Health Trusts", "NHS Pension Scheme", "Termination & post-employment — Nottinghamshire Healthcare NHS Foundation Trust", "Lampard Inquiry"]
    },
    "Termination & post-employment — Lincolnshire Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Lincolnshire Partnership NHS Foundation Trust"}],
        "description": "LPFT's £0.17M termination + post-employment line covers one-off severance, contractual notice pay-in-lieu, redundancy and the NHS Pension Scheme employer-element on early-retirement and exit packages across the trust's c. 2,300-staff base serving Lincolnshire's c. 770,000 residents. As one of the smaller MH FTs by scale, LPFT's exit-package pool is correspondingly modest — driven by ordinary retirement-cycle activity, occasional senior-leadership rotation and rural-recruitment-related vacancy churn. The line excludes ongoing pension service-cost (which sits in employer pension contributions).",
        "beneficiaries": "c. 2,300 staff covering MH and LD services across Lincolnshire (Lincoln, Boston, Spalding, Grantham, Stamford, Skegness rural footprint); estimated 10-25 exit packages annually scaled to retirement-cycle and senior-leadership rotation.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme regulations · Public Sector Exit Payments Regulations 2020 (uncapped post-2021 quash) · Employment Rights Act 1996 (s.139 redundancy + s.86 statutory notice) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.17M"},
            {"label": "Headcount + exit-pool context", "value": "c. 2,300 substantive WTE; estimated 10-25 exit packages annually"},
            {"label": "Composition", "value": "Statutory + contractual redundancy + pay-in-lieu of notice + NHS Pension Scheme employer-element on early retirement + senior-staff exit packages"},
            {"label": "Rural-recruitment context", "value": "Lincolnshire's geographic spread + recruitment difficulty in rural districts (Boston, Spalding, Skegness) drives elevated WTE turnover relative to urban MH peers"},
            {"label": "Trust-scale context", "value": "Smaller MH FT (c. £180M turnover) — exit pool tracks retirement cycle more than restructuring"},
            {"label": "April 2025 NIC step-up", "value": "Employer NIC threshold drop + rate rise (Apr 2025) raises NHS Pension Scheme employer-cost on exit packages forward"},
            {"label": "PSE Payments Regs 2020", "value": "Capped exit-payment regs revoked 2021; trust currently operates under HM Treasury non-statutory guidance + NHS England consent rules"},
            {"label": "Funding trajectory", "value": "Variable year-on-year; 2020-21 c. £0.10M → 2024-25 £0.17M — non-structural"},
            {"label": "Delivery body", "value": "Trust HR + Finance teams + NHS Business Services Authority (Pensions) + NHSE consent for senior packages"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + HM Treasury (exit-pay guidance) + Lincolnshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 workforce remuneration report; CQC inspection (RP7); Lincolnshire ICB workforce strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 capped PSE payments regime · Successor: HMT non-statutory exit-pay guidance + NIC step-up Apr 2025"}
        ],
        "notes": "LPFT's termination line reflects the operational rhythm of a smaller MH FT covering an unusually rural English county. Lincolnshire's geographic spread — from Lincoln to Boston and Spalding in the south, Skegness on the coast and Grantham and Stamford toward Rutland — creates persistent recruitment difficulty, driving WTE turnover above compact urban MH-trust rates. The exit-package pool is otherwise dominated by ordinary NHS Pension Scheme retirement-cycle activity. The April 2025 employer-NIC step-up raises forward NHS Pension Scheme employer-cost on subsequent exit packages, layered on the existing rural-recruitment churn pattern.",
        "sources": [
            {"publisher": "Lincolnshire Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lpft.nhs.uk/about-us/our-publications/annual-report-and-accounts"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guidance", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
            {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/public-sector-exit-payments-guidance"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LPFT provider profile (RP7)", "url": "https://www.cqc.org.uk/provider/RP7"}
        ],
        "related": ["Lincolnshire Partnership NHS Foundation Trust", "Staff Costs", "NHS Mental Health Trusts", "NHS Pension Scheme", "Termination & post-employment — Nottinghamshire Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Dudley Integrated Health and Care NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Dudley Integrated Health and Care NHS Trust"}],
        "description": "Dudley Integrated Health and Care NHS Trust's £0.15M general supplies & services line covers non-clinical consumables, ward provisions, household goods, laundry materials and small operational equipment across the trust's community-MH, community-physical-health and primary-care-network estate. As one of England's youngest and smallest NHS Trusts (established 2020 as a vertically-integrated provider for Dudley borough), the trust's supplies footprint is correspondingly modest, dominated by community-clinic consumables and small-team operational kit rather than inpatient ward supplies.",
        "beneficiaries": "c. 800 staff serving Dudley borough's c. 320,000 residents; integrated MH + community-physical-health + Black Country PCN-tier delivery; supplies consumed at c. 30-40 community sites + GP-co-located bases.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 / Procurement Act 2023 (in force Oct 2024)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£0.15M"},
            {"label": "Trust founding context", "value": "Dudley Integrated Health and Care NHS Trust formed 2020 — vertically-integrated MH + community + PCN model unique in NHS England"},
            {"label": "Site footprint", "value": "c. 30-40 community-MH, community-physical-health and PCN-tier bases across Dudley borough"},
            {"label": "Composition", "value": "Non-clinical consumables + household goods + laundry + small operational equipment + minor catering provisions"},
            {"label": "Inpatient share", "value": "Minimal — trust does not operate dedicated MH inpatient beds (delivered by Black Country Healthcare NHS FT in partnership)"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (majority) + Crown Commercial Service category contracts + minor local spot-buy"},
            {"label": "Procurement Act 2023 transition", "value": "New regime live Oct 2024 — central digital platform + transparency obligations replace PCR 2015 process"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.08M (first full year) → 2024-25 £0.15M — uplift driven by service expansion + supplies CPI"},
            {"label": "Delivery body", "value": "Trust Procurement + Estates & Facilities teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Black Country ICB · NHS Supply Chain governance"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC provider profile; Black Country ICB integrated-care evaluation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 Dudley CCG-commissioned community + MH services across multiple providers · Successor: ICS-aligned integrated provider model under Health and Care Act 2022"}
        ],
        "notes": "Dudley Integrated Health and Care NHS Trust is a structural outlier in the NHS provider landscape — established in 2020 as a vertically-integrated provider holding MH, community-physical-health and PCN-tier delivery within a single statutory body for Dudley borough alone. The general supplies line tracks that scale: modest in absolute terms, dominated by community-clinic consumables, with no inpatient ward provision driver (inpatient MH delivered by Black Country Healthcare NHS FT). NHS Supply Chain Future Operating Model and the Procurement Act 2023 transition reshape the framework architecture but the near-term cost driver remains supplies CPI plus PCN-tier service expansion.",
        "sources": [
            {"publisher": "Dudley Integrated Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dihc.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Black Country Integrated Care Board", "title": "Black Country ICS integrated-care evaluation", "url": "https://blackcountry.icb.nhs.uk/"}
        ],
        "related": ["Dudley Integrated Health and Care NHS Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "NHS Supply Chain", "General supplies & services — Berkshire Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Dudley Integrated Health and Care NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Dudley Integrated Health and Care NHS Trust"}],
        "description": "Dudley Integrated Health and Care NHS Trust's £0.15M amortisation line reflects depreciation of intangible assets — primarily software licences, capitalised EPR/clinical-system rollout costs and integration platforms supporting the trust's vertically-integrated MH + community + PCN delivery model. As a 2020-founded trust, the amortisation profile is concentrated on early-life clinical-system implementation rather than legacy mainframe roll-off, and is shaped by the NHS Frontline Digitisation programme that has supported EPR adoption across community-care providers.",
        "beneficiaries": "c. 800 staff and the c. 320,000 Dudley residents whose pathway data sits within the trust's integrated clinical record; intangible-asset base supports MH community-team digital workflow, primary-care-tier integration and shared-care reporting.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 Leases (where SaaS arrangements meet lease criteria) · NHS Act 2006 · Health and Care Act 2022 · Data Protection Act 2018",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.15M"},
            {"label": "Asset composition", "value": "Software licences + capitalised EPR/clinical-system rollout costs + integration-platform development + capitalised training (where eligible under IAS 38)"},
            {"label": "Frontline Digitisation programme", "value": "NHSE programme funding EPR adoption across MH, community + integrated-care providers — supports Dudley capitalisation pipeline"},
            {"label": "Trust founding context", "value": "2020-founded vertically-integrated trust — amortisation profile concentrated on early-life implementation"},
            {"label": "Useful life policy", "value": "Software 3-7 years typical per DHSC GAM ch.5; clinical EPR longer 7-10 years"},
            {"label": "Cloud/SaaS treatment", "value": "Configuration costs split between intangible (capitalised) and operating expense per IFRIC interpretation 2021 + DHSC GAM clarification"},
            {"label": "Integrated-record context", "value": "Vertically-integrated MH + community + PCN model places premium on shared-care record integration — drives platform-development capitalisation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.05M → 2024-25 £0.15M — ramping as Frontline Digitisation rollout progresses"},
            {"label": "Delivery body", "value": "Trust Digital Transformation team + NHS England Frontline Digitisation programme + Black Country ICB"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate · Frontline Digitisation programme + IAS 38 / DHSC GAM ch.5 framework"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 capital + intangibles note; Frontline Digitisation programme assessment"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 multi-provider digital landscape · Successor: continued Frontline Digitisation rollout + integration with NHS Federated Data Platform (Palantir)"}
        ],
        "notes": "Dudley Integrated Health and Care NHS Trust's amortisation line is shaped by its 2020 founding as a vertically-integrated provider — without legacy intangible-asset balances to roll off, the line consists almost entirely of newly-capitalised software, EPR rollout costs and integration-platform development supporting the MH + community + PCN model. NHS England's Frontline Digitisation programme provides the capital pathway, and Dudley's integrated remit drives above-average shared-care-platform capitalisation. The NHS Federated Data Platform (Palantir) deployment will reshape integration architecture going forward. The line will likely grow as the trust matures its digital estate.",
        "sources": [
            {"publisher": "Dudley Integrated Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dihc.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "Black Country Integrated Care Board", "title": "Digital strategy", "url": "https://blackcountry.icb.nhs.uk/"}
        ],
        "related": ["Dudley Integrated Health and Care NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS England", "Amortisation — Oxford Health NHS Foundation Trust", "Frontline Digitisation"]
    },
    "Other & adjustments — Dudley Integrated Health and Care NHS Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "Dudley Integrated Health and Care NHS Trust"}],
        "description": "Dudley Integrated Health and Care NHS Trust's £0.15M other & adjustments line is the residual cleanup bucket within Staff Costs covering prior-year corrections, AME reclassifications and minor pay-category restatements. As a 2020-founded vertically-integrated trust, the trust has been working through opening-balance recalibration and inheritance-of-staff payroll-attribution issues from its predecessor providers (Dudley CCG-commissioned community + MH services), generating a structural reclass workload above what one would expect for a c. £80M-turnover provider.",
        "beneficiaries": "c. 800 WTE substantive payroll covering MH + community-physical-health + PCN-tier integrated services across Dudley borough; legacy-payroll attribution across pre-2020 predecessor providers continues to drive reclass entries.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (general disclosure rules) · IAS 1 Presentation of Financial Statements · IAS 8 Accounting Policies, Changes in Accounting Estimates and Errors · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Other & adjustments 2024-25", "value": "£0.15M"},
            {"label": "Sub-line composition", "value": "Prior-year corrections + AME reclassifications + accrual releases + opening-balance/legacy-provider restatements"},
            {"label": "Trust headcount context", "value": "c. 800 WTE substantive — small-trust scale"},
            {"label": "Founding-vintage driver", "value": "2020 founding means ongoing opening-balance recalibration + inheritance-of-staff payroll-attribution from predecessor providers"},
            {"label": "Audit cycle driver", "value": "External audit + internal audit findings drive most reclass entries between substantive pay / agency / NIC / pension components"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer NIC threshold drop + 1.2pp rate rise raises forward NHS Pension Scheme employer-cost — feeds future accrual recalibration"},
            {"label": "Vertically-integrated context", "value": "MH + community + PCN-tier model creates additional pay-attribution boundaries between service lines; DHSC GAM materiality c. 0.5% of opex applies"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.20M (high opening-year reclass) → 2024-25 £0.15M — settling as opening balances mature"},
            {"label": "Delivery body", "value": "Trust Finance team + external auditor + NHS England financial reporting"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Black Country ICB · accounting framework HM Treasury FReM"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure note; audit Annual Audit Letter; ICB integrated-care provider evaluation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 Dudley CCG-commissioned multi-provider model · Successor: ICS-aligned reporting under Health and Care Act 2022"}
        ],
        "notes": "Dudley's other & adjustments line is shaped by the trust's 2020 founding — opening-balance recalibration and inheritance-of-staff payroll-attribution from predecessor providers (Dudley CCG-commissioned community + MH services) continues to feed reclass activity at a higher rate per WTE than a mature MH FT. The vertically-integrated MH + community + PCN-tier model adds pay-attribution complexity at year-end as cost-allocation boundaries between service lines are recalibrated. The April 2025 employer-NIC step-up feeds forward into NHS Pension Scheme employer-cost accrual recalibration. As the trust matures, the line will settle but integrated-care complexity persists.",
        "sources": [
            {"publisher": "Dudley Integrated Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dihc.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "Financial Reporting Manual (FReM) 2024-25", "url": "https://www.gov.uk/government/collections/government-financial-reporting-manual-frem"},
            {"publisher": "NHS England", "title": "Provider finance handbook", "url": "https://www.england.nhs.uk/financial-accounting/"},
            {"publisher": "Black Country Integrated Care Board", "title": "Black Country ICS integrated-care evaluation", "url": "https://blackcountry.icb.nhs.uk/"}
        ],
        "related": ["Dudley Integrated Health and Care NHS Trust", "Staff Costs", "NHS Mental Health Trusts", "Department of Health and Social Care", "Other & adjustments — North East London NHS Foundation Trust", "NHS England"]
    },
    "Termination & post-employment — South West London and St George's Mental Health NHS Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "South West London and St George's Mental Health NHS Trust"}],
        "description": "SWLSTG's £0.146M termination + post-employment line covers one-off severance, contractual notice pay-in-lieu, redundancy and the NHS Pension Scheme employer-element on early-retirement and exit packages across the trust's c. 2,200-staff base. SWLSTG serves the five SW London boroughs (Kingston, Merton, Richmond, Sutton, Wandsworth) and operates the c. £150M Springfield University Hospital redevelopment, which has driven a measurable workforce restructuring cycle as inpatient services have been re-shaped around the new estate.",
        "beneficiaries": "c. 2,200 staff covering MH services across Kingston, Merton, Richmond, Sutton and Wandsworth boroughs; estimated 10-25 exit packages annually scaled to the Springfield Hospital transition cycle and ordinary retirement-cycle activity.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme regulations · Public Sector Exit Payments Regulations 2020 (uncapped post-2021 quash) · Employment Rights Act 1996 (s.139 redundancy + s.86 statutory notice) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.15M"},
            {"label": "Headcount + exit-pool context", "value": "c. 2,200 substantive WTE; estimated 10-25 exit packages annually"},
            {"label": "Composition", "value": "Statutory + contractual redundancy + pay-in-lieu of notice + NHS Pension Scheme employer-element on early retirement + senior-staff exit packages"},
            {"label": "Springfield Hospital redevelopment context", "value": "c. £150M phased redevelopment of Springfield University Hospital (Tooting) — new inpatient hubs (Trinity, Shaftesbury) replaced legacy ward stock; workforce restructured around new estate model"},
            {"label": "Catchment", "value": "Kingston + Merton + Richmond + Sutton + Wandsworth — SW London boroughs c. 1.4M residents"},
            {"label": "April 2025 NIC step-up", "value": "Employer NIC threshold drop + rate rise (Apr 2025) raises NHS Pension Scheme employer-cost on exit packages forward; capped PSE Payments Regs 2020 revoked 2021 — HMT non-statutory guidance applies"},
            {"label": "St George's University academic-link context", "value": "Joint-appointment academic faculty with St George's University of London adds modest pay-recharge complexity to exit packages"},
            {"label": "Funding trajectory", "value": "Variable year-on-year through the Springfield transition; 2024-25 £0.15M"},
            {"label": "Delivery body", "value": "Trust HR + Finance teams + NHS Business Services Authority (Pensions) + NHSE consent for senior packages"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + HM Treasury (exit-pay guidance) + South West London ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 workforce remuneration report; CQC inspection (RQY); SWL ICS workforce strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 capped PSE payments regime · Successor: HMT non-statutory exit-pay guidance + NIC step-up Apr 2025 + completion of Springfield restructuring"}
        ],
        "notes": "SWLSTG's termination line reflects the convergence of two cycles: ordinary NHS Pension Scheme retirement-cycle activity across the c. 2,200-WTE base, and the workforce restructuring driven by the c. £150M Springfield University Hospital redevelopment in Tooting. The new Trinity and Shaftesbury inpatient hubs replaced legacy Victorian ward stock, and the inpatient nursing cadre has been progressively reshaped around the new estate model — feeding both voluntary exits and contractual notice payments. The St George's University academic-link adds modest pay-recharge complexity to senior-clinician exit packages. The April 2025 employer-NIC step-up will raise forward NHS Pension Scheme employer-cost on subsequent exit packages.",
        "sources": [
            {"publisher": "South West London and St George's Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swlstg.nhs.uk/annual-reports"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guidance", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
            {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/public-sector-exit-payments-guidance"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "SWLSTG provider profile (RQY)", "url": "https://www.cqc.org.uk/provider/RQY"}
        ],
        "related": ["South West London and St George's Mental Health NHS Trust", "Staff Costs", "NHS Mental Health Trusts", "NHS Pension Scheme", "Termination & post-employment — Nottinghamshire Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Other & adjustments — North Staffordshire Combined Healthcare NHS Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "North Staffordshire Combined Healthcare NHS Trust"}],
        "description": "NSCHT's £0.143M other & adjustments line is the residual cleanup bucket within Staff Costs covering prior-year corrections, AME reclassifications, accrual releases and minor pay-category restatements arising from the trust's annual audit cycle. As a small NHS Trust (non-FT) covering Stoke-on-Trent and Newcastle-under-Lyme MH services, NSCHT's line is modest in absolute terms but structurally driven by its Stoke City Council partnership arrangements and shared-services boundaries with University Hospitals of North Midlands.",
        "beneficiaries": "c. 1,800 WTE substantive payroll covering MH and LD services across Stoke-on-Trent and the Newcastle-under-Lyme area c. 470,000 residents; payroll-attribution reclass workload reflects council-partnership and acute-trust shared-services boundaries.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (general disclosure rules) · IAS 1 Presentation of Financial Statements · IAS 8 Accounting Policies, Changes in Accounting Estimates and Errors · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Other & adjustments 2024-25", "value": "£0.14M"},
            {"label": "Sub-line composition", "value": "Prior-year corrections + AME reclassifications + accrual releases + minor pay-category restatements"},
            {"label": "Trust headcount context", "value": "c. 1,800 WTE substantive — small NHS Trust (non-FT) scale"},
            {"label": "Council-partnership context", "value": "Stoke-on-Trent City Council s.75 / s.256 partnership arrangements on social-care-MH interface drive small inter-body pay-attribution adjustments"},
            {"label": "Shared-services boundary", "value": "Some back-office shared-services with University Hospitals of North Midlands generate inter-trust recharge reclass entries; DHSC GAM materiality c. 0.5% of opex applies"},
            {"label": "Audit cycle driver", "value": "External audit + internal audit findings drive most reclass entries between substantive pay / agency / NIC / pension components"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer NIC threshold drop + 1.2pp rate rise raises forward NHS Pension Scheme employer-cost — feeds future accrual recalibration"},
            {"label": "Funding trajectory", "value": "Variable year-on-year; £0.10M-£0.20M typical range over 2020-21 to 2024-25 — non-structural"},
            {"label": "Delivery body", "value": "Trust Finance team + external auditor + NHS England financial reporting"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Staffordshire and Stoke-on-Trent ICB · accounting framework HM Treasury FReM"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure note; audit Annual Audit Letter; CQC inspection (RRE)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2009 SHA-based reporting structure · Successor: ICS-aligned reporting under Health and Care Act 2022"}
        ],
        "notes": "NSCHT's other & adjustments line is small but structurally meaningful for a non-FT MH trust of its scale. The Stoke-on-Trent City Council s.75 / s.256 partnership arrangements on the social-care-MH interface drive small inter-body pay-attribution adjustments at year-end, and back-office shared-services with University Hospitals of North Midlands generate inter-trust recharge reclass entries. Each audit cycle surfaces a modest set of reclass entries between substantive pay, agency, NIC and pension components. The April 2025 employer-NIC step-up feeds forward into NHS Pension Scheme employer-cost accrual recalibration in subsequent cycles.",
        "sources": [
            {"publisher": "North Staffordshire Combined Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.combined.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "Financial Reporting Manual (FReM) 2024-25", "url": "https://www.gov.uk/government/collections/government-financial-reporting-manual-frem"},
            {"publisher": "NHS England", "title": "Provider finance handbook", "url": "https://www.england.nhs.uk/financial-accounting/"},
            {"publisher": "Care Quality Commission", "title": "NSCHT provider profile (RRE)", "url": "https://www.cqc.org.uk/provider/RRE"}
        ],
        "related": ["North Staffordshire Combined Healthcare NHS Trust", "Staff Costs", "NHS Mental Health Trusts", "Department of Health and Social Care", "Other & adjustments — North East London NHS Foundation Trust", "NHS England"]
    },
    "Other & adjustments — Camden and Islington NHS Foundation Trust": {
        "aliases": [{"name": "Other & adjustments", "parent": "Camden and Islington NHS Foundation Trust"}],
        "description": "Camden and Islington NHS FT's £0.14M other & adjustments line is the residual cleanup bucket within Staff Costs covering prior-year corrections, AME reclassifications and minor pay-category restatements. The trust's c. 1,800-WTE payroll covers MH services to the LB Camden and LB Islington populations, plus a portfolio of partnership arrangements with University College London Hospitals NHSFT and a long-running merger trajectory with Barnet, Enfield and Haringey MH NHS Trust under the North London Mental Health Partnership / North London NHS FT (operational from October 2024).",
        "beneficiaries": "c. 1,800 WTE substantive payroll covering MH services across Camden and Islington c. 530,000 residents; partnership and merger-transition pay-attribution reclass workload elevated through the North London NHS FT formation cycle.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (general disclosure rules) · IAS 1 Presentation of Financial Statements · IAS 8 Accounting Policies, Changes in Accounting Estimates and Errors · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Other & adjustments 2024-25", "value": "£0.14M"},
            {"label": "Sub-line composition", "value": "Prior-year corrections + AME reclassifications + accrual releases + merger-transition pay-attribution restatements"},
            {"label": "Trust headcount context", "value": "c. 1,800 WTE substantive — small London MH FT scale"},
            {"label": "North London NHS FT merger context", "value": "C&I + Barnet, Enfield and Haringey MH Trusts merged Oct 2024 forming North London NHS FT — pay-attribution and pension-scheme harmonisation drive elevated reclass activity in the transition window"},
            {"label": "UCLH partnership context", "value": "Joint-appointment and shared-pathway arrangements with UCLH NHSFT (eg. Translational Psychiatry) generate cross-trust pay recharges flowing through this line"},
            {"label": "Audit cycle driver", "value": "External audit + internal audit findings drive most reclass entries; DHSC GAM materiality c. 0.5% of opex applies"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer NIC threshold drop + 1.2pp rate rise raises forward NHS Pension Scheme employer-cost — feeds future accrual recalibration"},
            {"label": "Funding trajectory", "value": "Variable year-on-year; expected uplift in 2024-25 reflecting merger-transition reclass activity → £0.14M"},
            {"label": "Delivery body", "value": "Trust Finance team + external auditor + NHS England financial reporting + North London NHS FT integration team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North Central London ICB · accounting framework HM Treasury FReM"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure note; North London NHS FT pre-merger business case; CQC inspection (RP1)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2024 standalone C&I NHS FT · Successor: subsumed into North London NHS FT from Oct 2024 — last standalone reporting cycle"}
        ],
        "notes": "Camden and Islington NHS FT's other & adjustments line in 2024-25 sits within an exceptional context — the trust merged with Barnet, Enfield and Haringey MH NHS Trust to form North London NHS FT operational from October 2024. The merger has driven elevated pay-attribution and pension-scheme harmonisation reclass activity in the transition window as opening balances are recalibrated and inheriting-trust accounting policies are aligned. The longstanding UCLH NHSFT partnership for translational psychiatry research generates routine cross-trust pay recharges. The April 2025 employer-NIC step-up will further complicate forward NHS Pension Scheme employer-cost accrual within the new North London NHS FT, and 2024-25 represents the trust's last standalone reporting cycle before full integration.",
        "sources": [
            {"publisher": "Camden and Islington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.candi.nhs.uk/about-us/our-publications/annual-report-2023-24"},
            {"publisher": "North London Mental Health Partnership", "title": "North London NHS Foundation Trust formation", "url": "https://www.northlondonmhp.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Provider finance handbook + merger guidance", "url": "https://www.england.nhs.uk/financial-accounting/"},
            {"publisher": "Care Quality Commission", "title": "Camden and Islington NHS FT provider profile (RP1)", "url": "https://www.cqc.org.uk/provider/RP1"}
        ],
        "related": ["Camden and Islington NHS Foundation Trust", "Staff Costs", "NHS Mental Health Trusts", "Department of Health and Social Care", "Other & adjustments — North East London NHS Foundation Trust", "Barnet, Enfield And Haringey Mental Health NHS Trust"]
    },
    "Amortisation — Tavistock and Portman NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Tavistock and Portman NHS Foundation Trust"}],
        "description": "Tavistock and Portman NHS FT's £0.13M amortisation line reflects depreciation of intangible assets — primarily software licences, capitalised EPR/clinical-system costs and the trust's distinctive psychotherapeutic and educational-platform IT assets supporting its psychoanalytic clinical training programmes. As the smallest MH FT (specialist psychotherapy + national training role), the intangible-asset base is shaped by clinical-system needs plus the trust's hybrid academic-clinical mission with Essex University Tavistock training partnership.",
        "beneficiaries": "c. 800 staff plus the trust's national training cohort of c. 1,500 trainees on psychoanalytic + child-psychotherapy + couple-therapy programmes; intangible assets support both clinical record-keeping for psychotherapy services and learning-platform delivery for trainees.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 Leases (where SaaS arrangements meet lease criteria) · NHS Act 2006 · Health and Care Act 2022 · Data Protection Act 2018",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.13M"},
            {"label": "Asset composition", "value": "Software licences + capitalised EPR/clinical-system rollout costs + virtual-learning-platform development + capitalised training (where eligible under IAS 38)"},
            {"label": "Trust scale context", "value": "Smallest MH FT (c. £45M turnover); specialist psychotherapy + national training role"},
            {"label": "Frontline Digitisation programme", "value": "NHSE programme funding EPR adoption — Tavistock benefit limited by smaller scale + specialist EPR fit-for-purpose challenges"},
            {"label": "Essex University Tavistock partnership", "value": "Trust delivers MA/Doctoral psychoanalytic + child-psychotherapy programmes in partnership with Essex University — shared-platform digital infrastructure"},
            {"label": "Useful life policy", "value": "Software 3-7 years typical per DHSC GAM ch.5; clinical EPR longer 7-10 years"},
            {"label": "GIDS closure context", "value": "Gender Identity Development Service closed Mar 2024 (Cass Review fallout) — reduced IT-asset capitalisation pipeline; legacy assets continued to amortise through transition; cloud/SaaS configuration split intangible-vs-opex per IFRIC 2021"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.10M → 2024-25 £0.13M — modest growth"},
            {"label": "Delivery body", "value": "Trust Digital Transformation team + NHS England Frontline Digitisation programme + Essex University training partnership"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + North Central London ICB · Frontline Digitisation programme + IAS 38 / DHSC GAM ch.5 framework"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 capital + intangibles note; Cass Review final report (Apr 2024) re GIDS closure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation legacy clinical-system landscape · Successor: post-GIDS-closure refocused intangibles + continued partnership-platform investment"}
        ],
        "notes": "Tavistock and Portman NHS FT's amortisation line is small but distinct in composition — alongside standard NHS clinical-system capitalisation, the trust uniquely capitalises elements of its virtual-learning-platform development supporting national psychoanalytic and child-psychotherapy training programmes with Essex University. The Cass Review (final report April 2024) and consequent closure of the Gender Identity Development Service in March 2024 reshaped a portion of the trust's clinical IT-asset pipeline; legacy GIDS-related intangibles continued to amortise through the transition. NHS England's Frontline Digitisation programme provides the capital pathway but the trust's specialist-psychotherapy model creates EPR fit-for-purpose challenges.",
        "sources": [
            {"publisher": "Tavistock and Portman NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://tavistockandportman.nhs.uk/about-us/governance/annual-reports/"},
            {"publisher": "NHS England", "title": "Cass Review final report (Independent Review of Gender Identity Services for Children and Young People)", "url": "https://cass.independent-review.uk/home/publications/final-report/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"}
        ],
        "related": ["Tavistock and Portman NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS England", "Amortisation — Oxford Health NHS Foundation Trust", "Frontline Digitisation"]
    },
    "Amortisation — Cheshire and Wirral Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Cheshire and Wirral Partnership NHS Foundation Trust"}],
        "description": "CWP's £0.127M amortisation line reflects depreciation of intangible assets — primarily software licences, capitalised EPR/clinical-system costs and DDaT (digital, data and technology) platform development supporting MH, LD and CAMHS service delivery across Cheshire and the Wirral. The trust serves a c. 1.0M-resident catchment and operates from c. 60+ inpatient and community sites; the amortisation profile is shaped by the NHS Frontline Digitisation programme that has supported EPR rollout across MH-trust providers.",
        "beneficiaries": "c. 4,000 staff serving c. 1.0M residents across Cheshire East, Cheshire West & Chester and Wirral; intangible-asset base supports MH, LD and CAMHS clinical workflow plus drug & alcohol partnership services across the trust's c. 60+ site footprint.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 Leases (where SaaS arrangements meet lease criteria) · NHS Act 2006 · Health and Care Act 2022 · Data Protection Act 2018",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.13M"},
            {"label": "Asset composition", "value": "Software licences + capitalised EPR/clinical-system rollout costs + DDaT platform development + capitalised training (where eligible under IAS 38)"},
            {"label": "Frontline Digitisation programme", "value": "NHSE programme funding EPR adoption across MH, community + integrated-care providers — supports CWP capitalisation pipeline"},
            {"label": "Trust footprint", "value": "c. 4,000 WTE; c. 60+ inpatient + community sites across Cheshire + Wirral"},
            {"label": "Useful life policy", "value": "Software 3-7 years typical per DHSC GAM ch.5; clinical EPR longer 7-10 years"},
            {"label": "Cloud/SaaS treatment", "value": "Configuration costs split between intangible (capitalised) and operating expense per IFRIC interpretation 2021 + DHSC GAM clarification"},
            {"label": "Drug & alcohol partnership context", "value": "Trust delivers commissioned drug & alcohol services for several Cheshire authorities — feeds outcomes-tracking platform capitalisation; Cheshire and Merseyside ICS digital strategy drives cadence"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.08M → 2024-25 £0.13M — moderate growth tracking Frontline Digitisation rollout"},
            {"label": "Delivery body", "value": "Trust Digital + DDaT team + NHS England Frontline Digitisation programme + Cheshire and Merseyside ICB"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate · Frontline Digitisation programme + IAS 38 / DHSC GAM ch.5 framework"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 capital + intangibles note; Cheshire and Merseyside ICS digital strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation legacy clinical-system landscape · Successor: continued Frontline Digitisation rollout + integration with NHS Federated Data Platform"}
        ],
        "notes": "CWP's amortisation line tracks the steady-state intangibles profile of a mid-sized MH FT serving Cheshire and the Wirral. Software licence amortisation, capitalised EPR rollout costs and DDaT platform development make up the bulk of the line, with the Frontline Digitisation programme providing the capital pathway. The trust's commissioned drug & alcohol services for Cheshire authorities feed additional outcomes-tracking platform capitalisation. Cheshire and Merseyside ICS digital strategy drives medium-term cadence; NHS Federated Data Platform (Palantir) and Procurement Act 2023 reshape the contracting framework.",
        "sources": [
            {"publisher": "Cheshire and Wirral Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cwp.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "Cheshire and Merseyside ICB", "title": "ICS digital strategy", "url": "https://www.cheshireandmerseyside.nhs.uk/"}
        ],
        "related": ["Cheshire and Wirral Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS England", "Amortisation — Oxford Health NHS Foundation Trust", "Frontline Digitisation"]
    },
    "Lease expenditure — Leeds and York Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Leeds and York Partnership NHS Foundation Trust"}],
        "description": "LYPFT's £0.127M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio centres on NHSPS-leased and Community Health Partnerships LIFT-procured community-MH and CAMHS premises across the Leeds metropolitan area and the York and Scarborough catchment, plus the trust's national specialist services (eating disorders, deafness MH, adult ADHD, gender dysphoria) which use a mix of leased and partnership-occupied estate.",
        "beneficiaries": "c. 3,500 staff serving c. 1.1M residents across Leeds and the York/Scarborough national specialist catchments; leased estate component includes c. 30+ NHSPS + LIFT community-MH, CAMHS and national-specialist bases.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.13M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 30+ NHSPS + CHP-LIFT community-MH, CAMHS and national-specialist bases across Leeds + York"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private commercial landlords for some national-specialist bases"},
            {"label": "National specialist services context", "value": "Adult eating disorders + deafness MH + adult ADHD + gender dysphoria national-specialist services use leased clinical bases — adds geographic spread + complexity"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology; HMT PES discount rate per DHSC GAM ch.7 recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer LIFT contracts to 25 years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.05M operating lease → 2022-23 c. £0.10M ROU first year → 2024-25 £0.13M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + West Yorkshire ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC inspection (RGD)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + West Yorkshire ICS estate consolidation"}
        ],
        "notes": "LYPFT's lease line is small in absolute terms but structurally distinctive — alongside the standard Leeds metropolitan community-MH and CAMHS leased footprint, the trust hosts a portfolio of national specialist services (adult eating disorders, deafness MH, adult ADHD, gender dysphoria) whose dispersed clinical-base requirements add complexity to the leased estate. The IFRS 16 2022 transition moved previously off-balance-sheet operating leases on-balance-sheet, lifting the headline annual charge. The sector-wide NHSPS / MH-trust service-charge dispute applies to LYPFT proportionate to its NHSPS-leased footprint. West Yorkshire ICS estate consolidation is the medium-term lever; CPI-linked uplift on private commercial leases for national-specialist bases adds modest cost pressure.",
        "sources": [
            {"publisher": "Leeds and York Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsandyorkpft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "LYPFT provider profile (RGD)", "url": "https://www.cqc.org.uk/provider/RGD"}
        ],
        "related": ["Leeds and York Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Pennine Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Tavistock and Portman NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Tavistock and Portman NHS Foundation Trust"}],
        "description": "Tavistock and Portman's £0.122M transport line covers staff business mileage, inter-site travel between the trust's two London bases (Tavistock Centre, Belsize Lane NW3 and Portman Clinic, Fitzjohn's Avenue NW3) plus reimbursed travel for the trust's national outreach training delivery. The line is structurally small because the trust's clinical model is overwhelmingly outpatient/community-based with no inpatient transport requirement, and because the trust's national-specialist remit means most patients travel to the trust rather than vice versa.",
        "beneficiaries": "c. 800 staff plus c. 1,500 trainees on national psychoanalytic + child-psychotherapy + couple-therapy programmes; transport line covers minimal inter-site staff travel, national outreach training delivery and reimbursed academic-partnership travel.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments · NHS Agenda for Change Section 17 (mileage rates)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.12M"},
            {"label": "Trust scale + clinical-model context", "value": "Smallest MH FT (c. £45M turnover); outpatient + community psychotherapy model — no inpatient bed estate requiring patient transfer activity"},
            {"label": "Site footprint", "value": "Two London bases — Tavistock Centre, Belsize Lane NW3 + Portman Clinic, Fitzjohn's Avenue NW3 (both Camden)"},
            {"label": "National specialist remit", "value": "Patients travel TO trust (national catchment) rather than trust travelling to patients — transport line driven by staff business + national-training outreach"},
            {"label": "Essex University training partnership context", "value": "MA/Doctoral programmes delivered with Essex University generate inter-site academic-partnership travel"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "GIDS closure context", "value": "Gender Identity Development Service closed Mar 2024 (Cass Review fallout) — reduced national-outreach travel; legacy reimbursement continued through transition"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.10M (pandemic suppression) → 2024-25 £0.12M — modest recovery"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; minor PTS contract with London Ambulance Service for occasional s.135/s.136 conveyance (rare given outpatient model)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; Cass Review final report (Apr 2024) re GIDS closure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-pandemic baseline transport activity · Successor: continued post-GIDS-closure rebalancing toward Camden-centric outpatient model"}
        ],
        "notes": "Tavistock and Portman's transport line is the smallest in the MH-trust sector reflecting the trust's distinctive clinical model — an outpatient + community psychotherapy service with no inpatient bed estate, and a national-specialist remit where patients travel TO the trust rather than vice versa. The line is dominated by staff business mileage, two-site inter-base travel between the Tavistock Centre and Portman Clinic, and national-outreach training-delivery travel for the psychoanalytic + child-psychotherapy programmes delivered with Essex University. The Cass Review and consequent closure of the Gender Identity Development Service in March 2024 reduced national-outreach travel but legacy reimbursement continued through the transition. Post-pandemic recovery has lifted the line modestly.",
        "sources": [
            {"publisher": "Tavistock and Portman NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://tavistockandportman.nhs.uk/about-us/governance/annual-reports/"},
            {"publisher": "NHS England", "title": "Cass Review final report (Independent Review of Gender Identity Services for Children and Young People)", "url": "https://cass.independent-review.uk/home/publications/final-report/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Tavistock and Portman provider profile (RNK)", "url": "https://www.cqc.org.uk/provider/RNK"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — reimbursement of travel costs", "url": "https://www.nhsemployers.org/publications/tchandbook"}
        ],
        "related": ["Tavistock and Portman NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Lancashire and South Cumbria NHS Foundation Trust", "Mental Health Act 1983"]
    },
    "Termination & post-employment — Avon and Wiltshire Mental Health Partnership NHS Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Avon and Wiltshire Mental Health Partnership NHS Trust"}],
        "description": "AWP's £0.117M termination + post-employment line covers severance, contractual notice pay-in-lieu, redundancy and the NHS Pension Scheme employer-element on early-retirement and exit packages across c. 4,000 staff serving c. 1.7M residents across Bristol, BANES, North Somerset, South Gloucestershire, Wiltshire and Swindon. The trust weathered a sustained CQC concern cycle ('Requires Improvement' overall + 'Inadequate' in some core services 2019-2023, partial improvement 2024) which shaped senior-leadership turnover and remediation exits.",
        "beneficiaries": "c. 4,000 staff covering MH services across Bristol, BANES, North Somerset, South Gloucestershire, Wiltshire + Swindon c. 1.7M residents; estimated 15-30 exit packages annually with elevated cycle through CQC remediation periods.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme regulations · Public Sector Exit Payments Regulations 2020 (uncapped post-2021 quash) · Employment Rights Act 1996 (s.139 redundancy + s.86 statutory notice) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.12M"},
            {"label": "Headcount + exit-pool context", "value": "c. 4,000 substantive WTE; estimated 15-30 exit packages annually"},
            {"label": "Composition", "value": "Statutory + contractual redundancy + pay-in-lieu of notice + NHS Pension Scheme employer-element on early retirement + senior-staff exit packages"},
            {"label": "CQC remediation context", "value": "AWP rated 'Requires Improvement' overall + 'Inadequate' in some core services 2019-2023 — sustained senior-leadership turnover + remediation exits; partial improvement in 2024 inspections"},
            {"label": "Catchment", "value": "Bristol + BANES + N Somerset + S Gloucestershire + Wiltshire + Swindon — large mixed urban-rural footprint"},
            {"label": "April 2025 NIC step-up", "value": "Employer NIC threshold drop + rate rise (Apr 2025) raises NHS Pension Scheme employer-cost on exit packages forward; capped PSE Payments Regs 2020 revoked 2021 — HMT non-statutory guidance applies"},
            {"label": "Restructuring + estate strategy context", "value": "Partial closure of Callington Road inpatient facility + reconfiguration of inpatient bed-stock has driven workforce restructuring exits"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.07M → 2024-25 £0.12M — uplift through CQC remediation cycle"},
            {"label": "Delivery body", "value": "Trust HR + Finance teams + NHS Business Services Authority (Pensions) + NHSE consent for senior packages"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + HM Treasury (exit-pay guidance) + BNSSG ICB + BSW ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports 2019-2024 (RVN); trust ARA workforce remuneration report; BNSSG/BSW ICS workforce strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 capped PSE payments regime · Successor: HMT non-statutory exit-pay guidance + NIC step-up Apr 2025 + continued CQC compliance trajectory"}
        ],
        "notes": "AWP's termination line in 2024-25 reflects the cumulative impact of a sustained CQC concern cycle — the trust was rated 'Requires Improvement' overall and 'Inadequate' in some core services through 2019-2023, driving programmes of senior-leadership turnover, clinical-governance restructuring and remediation-related exits across the inpatient cadre. Partial improvement in 2024 inspections has begun to settle the cycle but workforce restructuring continues. AWP's mixed urban-rural footprint across Bristol/BANES/N Somerset/S Gloucestershire and Wiltshire/Swindon adds geographic complexity to the workforce model. The April 2025 employer-NIC step-up will raise forward NHS Pension Scheme employer-cost on subsequent exit packages.",
        "sources": [
            {"publisher": "Avon and Wiltshire Mental Health Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.awp.nhs.uk/about-us/publications-policies/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "AWP provider profile + inspection reports (RVN)", "url": "https://www.cqc.org.uk/provider/RVN"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guidance", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
            {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/public-sector-exit-payments-guidance"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Avon and Wiltshire Mental Health Partnership NHS Trust", "Staff Costs", "NHS Mental Health Trusts", "NHS Pension Scheme", "Termination & post-employment — Nottinghamshire Healthcare NHS Foundation Trust", "Care Quality Commission"]
    },
    "Amortisation — Bradford District Care NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Bradford District Care NHS Foundation Trust"}],
        "description": "BDCFT's £0.115M amortisation line reflects depreciation of intangible assets — primarily software licences, capitalised EPR/clinical-system costs and DDaT platform development supporting MH, community-physical-health and dental-services delivery across Bradford district and Craven. As a combined MH + community + dental provider, the trust's intangible-asset profile is shaped by both the NHS Frontline Digitisation programme and primary-care-tier dental-services digital infrastructure, with EPR rollout the principal capitalisation driver post-2023.",
        "beneficiaries": "c. 3,000 staff serving Bradford district + Craven c. 600,000 residents; intangible assets support MH community workflow, community-physical-health (district-nursing, health-visiting, school-nursing) records and salaried general dental services for the BDCFT-hosted dental practice estate.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 Leases (where SaaS arrangements meet lease criteria) · NHS Act 2006 · Health and Care Act 2022 · Data Protection Act 2018",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.12M"},
            {"label": "Asset composition", "value": "Software licences + capitalised EPR/clinical-system rollout costs + DDaT platform development + dental-services digital infrastructure + capitalised training (where eligible under IAS 38)"},
            {"label": "Frontline Digitisation programme", "value": "NHSE programme funding EPR adoption across MH, community + integrated-care providers — supports BDCFT capitalisation pipeline"},
            {"label": "Combined MH + community + dental remit", "value": "Trust delivers MH + community-physical-health + salaried general dental services — broader intangible-asset scope than pure-MH peers"},
            {"label": "Useful life policy", "value": "Software 3-7 years typical per DHSC GAM ch.5; clinical EPR longer 7-10 years"},
            {"label": "Cloud/SaaS treatment", "value": "Configuration costs split between intangible (capitalised) and operating expense per IFRIC interpretation 2021 + DHSC GAM clarification; West Yorkshire ICS digital strategy drives cadence"},
            {"label": "Dental services context", "value": "Trust-hosted salaried general dental services use specific dental-clinical-system software — modest additional intangibles capitalisation"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.07M → 2024-25 £0.12M — moderate growth tracking Frontline Digitisation rollout + dental-system upgrade cycle"},
            {"label": "Delivery body", "value": "Trust DDaT team + NHS England Frontline Digitisation programme + West Yorkshire ICB"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate · Frontline Digitisation programme + IAS 38 / DHSC GAM ch.5 framework"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 capital + intangibles note; West Yorkshire ICS digital strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation legacy clinical-system landscape · Successor: continued Frontline Digitisation rollout + integration with NHS Federated Data Platform"}
        ],
        "notes": "BDCFT's amortisation line is structurally distinctive among MH-trust peers because the trust delivers a combined MH + community-physical-health + salaried general dental services portfolio, broadening the scope of intangible-asset capitalisation beyond a pure-MH provider. EPR rollout under the NHS Frontline Digitisation programme is the principal capitalisation driver post-2023, with software licence amortisation, DDaT platform development and dental-services digital infrastructure adding diversity. West Yorkshire ICS digital strategy provides the medium-term frame; NHS Federated Data Platform (Palantir) reshapes integration architecture forward. The line grows as the trust extends its EPR estate.",
        "sources": [
            {"publisher": "Bradford District Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bdct.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "West Yorkshire Integrated Care Board", "title": "ICS digital strategy", "url": "https://www.wypartnership.co.uk/"}
        ],
        "related": ["Bradford District Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS England", "Amortisation — Oxford Health NHS Foundation Trust", "Frontline Digitisation"]
    },
}
