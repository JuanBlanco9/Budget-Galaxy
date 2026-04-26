# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 03 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Social security & levy — Harrogate and District NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Harrogate and District NHS Foundation Trust"}],
        "description": "Harrogate and District's £20.38M social-security & levy line covers employer NICs (13.8% above secondary threshold in 2024-25) plus the Apprenticeship Levy (0.5% on paybill above £3M) on the trust's c. 4,000-WTE paybill. The trust's combined acute (Harrogate District Hospital, c. 350 beds) + community-services footprint across North Yorkshire — including school-nursing and 0-19 children's services — drives a paybill mix weighted toward Bands 5-7 nursing and AHP grades, with consultant medical staff a smaller share than urban teaching trusts.",
        "beneficiaries": "c. 4,000 WTE substantive staff (medical, nursing, AHP, scientific, admin, estates) plus contracted bank/agency cover; serves a registered acute catchment c. 160,000 across Harrogate, Knaresborough, Ripon and rural North Yorkshire, plus c. 1.5M reach via community children's services across Yorkshire and the Humber.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016 Pt 6) · IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£20.38M"},
            {"label": "Workforce scale", "value": "c. 4,000 WTE substantive + contracted bank/agency"},
            {"label": "Composition", "value": "Employer NIC (13.8% above secondary threshold) + Apprenticeship Levy (0.5% on paybill > £3M) + Class 1A on benefits"},
            {"label": "April 2025 NIC step-up", "value": "Employer rate to 15% + secondary threshold drop £9,100 → £5,000 — DHSC partial reimbursement via NHSE allocation; net residual remains material"},
            {"label": "Industrial action 2023-24 backfill", "value": "Junior doctor + consultant strikes drove agency-medical NIC layer; agency/bank now subject to off-payroll IR35 employer NIC"},
            {"label": "Apprenticeship Levy use", "value": "Levy drawdown into nursing-associate, registered-nurse-degree-apprenticeship + AHP routes per NHSE workforce plan"},
            {"label": "Community-services paybill mix", "value": "0-19 children's services + school nursing + community paediatrics broaden the Band-5/6 nursing layer beyond pure-acute peers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M (paybill recovery) → 2024-25 £20.38M; forward step-up Apr 2025"},
            {"label": "Delivery body", "value": "Trust Finance + HR + ESR payroll; HMRC PAYE collection; NHS Business Services Authority pension element parallel"},
            {"label": "Policy owner", "value": "HMT (NIC + Levy policy) + HMRC (collection) + DHSC + NHSE Workforce + Humber and North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 remuneration + workforce report; NHSE Long Term Workforce Plan 2023; CQC 'Good' rating 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 Apprenticeship Levy regime · Successor: April 2025 NIC reform + LTWP 2023 expansion"}
        ],
        "notes": "Harrogate's social-security line tracks paybill mix more than headline workforce growth — the trust's combined acute + community remit (Yorkshire-wide 0-19 children's services and school nursing) carries a broader Band-5/6 nursing layer than a pure-acute peer of similar size. The 2023-24 industrial action wave pushed agency-medical cover above plan, layering employer-NIC on agency invoices subject to IR35 off-payroll rules. The April 2025 employer-NIC step-up raises forward cost; DHSC partial reimbursement via NHSE softens but does not neutralise impact, and contracted-out FM remains unreimbursed. Apprenticeship Levy drawdown is increasingly directed at nursing-associate and RNDA pipelines per LTWP.",
        "sources": [
            {"publisher": "Harrogate and District NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hdft.nhs.uk/about/annual-report-accounts/"},
            {"publisher": "HM Revenue & Customs", "title": "Employer NIC + Apprenticeship Levy guidance 2024-25", "url": "https://www.gov.uk/guidance/pay-apprenticeship-levy"},
            {"publisher": "NHS England", "title": "Long Term Workforce Plan 2023", "url": "https://www.england.nhs.uk/publication/nhs-long-term-workforce-plan/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Harrogate and District NHS FT provider profile (RCD)", "url": "https://www.cqc.org.uk/provider/RCD"}
        ],
        "related": ["Harrogate and District NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "NHS England Long Term Workforce Plan", "Social security & levy — Tameside and Glossop Integrated Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Social security & levy — Tameside and Glossop Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Tameside and Glossop Integrated Care NHS Foundation Trust"}],
        "description": "Tameside and Glossop's £20.08M social-security & levy line covers employer NICs (13.8%) and the Apprenticeship Levy on a c. 4,200-WTE paybill anchored at Tameside Hospital (c. 450 beds, Ashton-under-Lyne) plus an integrated community-services arm covering Tameside borough and Glossopdale (Derbyshire). The trust's integrated-care model — among the earliest Section 75 partnerships with Tameside MBC adult social care — broadens the Band-3/4 support-worker and AHP paybill layer above pure-acute peers, lifting employer NIC against a base bed-count of similar size.",
        "beneficiaries": "c. 4,200 WTE substantive staff plus contracted bank/agency; serves a registered catchment c. 250,000 across Tameside (Ashton, Hyde, Stalybridge, Denton, Audenshaw, Droylsden, Mossley) plus Glossop and Hadfield in Derbyshire; integrated-care perimeter includes c. 200 social-care colleagues seconded under S.75.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016 Pt 6) · IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 (Section 75 partnership powers) · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£20.08M"},
            {"label": "Workforce scale", "value": "c. 4,200 WTE substantive + integrated S.75 social-care secondees"},
            {"label": "Composition", "value": "Employer NIC (13.8% above secondary threshold) + Apprenticeship Levy (0.5% on paybill > £3M) + Class 1A"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15% + threshold £9,100 → £5,000 — DHSC partial reimbursement via NHSE allocation"},
            {"label": "Industrial action 2023-24 backfill", "value": "Junior doctor + consultant strikes drove agency-medical NIC layer; bank/agency activity peaked Q3 2023-24"},
            {"label": "Integrated-care paybill mix", "value": "Section 75 partnership with Tameside MBC adult social care broadens Band-3/4 support-worker layer beyond acute peers"},
            {"label": "Apprenticeship Levy use", "value": "Drawdown into RNDA + nursing-associate + AHP apprenticeship routes; Greater Manchester levy-pooling explored under GM ICS"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M → 2024-25 £20.08M; Apr 2025 forward uplift"},
            {"label": "Delivery body", "value": "Trust Finance + HR + ESR payroll; HMRC PAYE; NHSBSA pension element parallel"},
            {"label": "Policy owner", "value": "HMT (NIC + Levy) + HMRC (collection) + DHSC + NHSE Workforce + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 remuneration report; NHSE LTWP 2023; CQC inspection 2024"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 Apprenticeship Levy + 2017 trust integration with Tameside community services · Successor: Apr 2025 NIC reform + LTWP expansion"}
        ],
        "notes": "Tameside and Glossop's social-security line reflects an integrated-care trust where the Section 75 partnership with Tameside MBC adult social care extends the paybill into the Band-3/4 support-worker domain not normally captured at pure-acute peers. Industrial-action backfill in 2023-24 added an agency-medical layer on top of routine bank cover, with employer-NIC applying via IR35 off-payroll rules to limited-company locums. The April 2025 employer-NIC step-up raises forward cost meaningfully; DHSC partial reimbursement via NHSE softens the impact but the contracted-FM perimeter (Mitie estates, catering) is not reimbursed. The trust sits within the Greater Manchester ICS, which has explored levy-pooling and shared apprenticeship pipelines across the conurbation.",
        "sources": [
            {"publisher": "Tameside and Glossop Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.tamesidehospital.nhs.uk/about-us/annual-reports.htm"},
            {"publisher": "HM Revenue & Customs", "title": "Employer NIC + Apprenticeship Levy guidance 2024-25", "url": "https://www.gov.uk/guidance/pay-apprenticeship-levy"},
            {"publisher": "NHS England", "title": "Long Term Workforce Plan 2023", "url": "https://www.england.nhs.uk/publication/nhs-long-term-workforce-plan/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Tameside and Glossop NHS FT provider profile (RMP)", "url": "https://www.cqc.org.uk/provider/RMP"}
        ],
        "related": ["Tameside and Glossop Integrated Care NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "NHS England Long Term Workforce Plan", "Social security & levy — Harrogate and District NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Guy's & St Thomas' NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Guy's & St Thomas' NHS Foundation Trust"}],
        "description": "GSTT's £20.04M transport line covers staff business mileage, the trust pool fleet (right-of-use under IFRS 16), inter-site clinical-courier runs between Guy's, St Thomas', Royal Brompton and Harefield, and patient-transport contracts for non-emergency conveyance — a structurally elevated line driven by a multi-site Central London + outer-London (Harefield) footprint and the 2021 incorporation of the Royal Brompton & Harefield specialist heart-and-lung sites into the GSTT group. Specimen-courier traffic for tertiary cardiothoracic and renal services is a material sub-component.",
        "beneficiaries": "c. 24,000 WTE workforce across Guy's (Southwark), St Thomas' (Lambeth), Royal Brompton (Chelsea) and Harefield (Hillingdon); serves c. 2.5M Lambeth + Southwark population plus a national tertiary cardiothoracic, renal-transplant and complex-paediatric catchment; c. 1M outpatient attendances per year.",
        "legal_basis": "NHS Act 2006 · NHS England Patient Transport Services Eligibility Criteria · Agenda for Change Section 17 · HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£20.04M"},
            {"label": "Site footprint", "value": "Guy's (Southwark) + St Thomas' (Lambeth) + Evelina London + Royal Brompton (Chelsea) + Harefield (Hillingdon)"},
            {"label": "Royal Brompton + Harefield merger", "value": "Feb 2021 RBH integration added national cardiothoracic + cystic-fibrosis activity + Harefield outer-London site — meaningful inter-site transport baseline added"},
            {"label": "Specimen + clinical-courier", "value": "Tertiary cardiothoracic, renal-transplant + complex-paediatric pathways drive sustained inter-site specimen traffic plus pharmacy redistribution"},
            {"label": "PTS contractor", "value": "Patient-transport via contracted PTS providers (London-region tendered) plus LAS s.136 / inter-hospital ambulance"},
            {"label": "ULEZ + congestion charge", "value": "TfL ULEZ + Congestion Charge zone covers Guy's, St Thomas', Brompton — fleet renewal accelerated to comply; staff-mileage premium in zone"},
            {"label": "Pool fleet IFRS 16", "value": "ROU asset + lease liability per IFRS 16 — depreciation + interest split since 2022 transition"},
            {"label": "Industrial action 2023-24", "value": "Junior doctor + consultant strikes raised inter-site agency-medical mileage + courier shifts"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £18M (post-RBH merger) → 2024-25 £20.04M — sustained CPI fuel + multi-site uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Travel team + contracted PTS provider + LAS for emergency conveyance"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South East London ICB + NW London ICB (Harefield); TfL for road-charging interaction"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate GSTT + RBH transport regimes · Successor: GSTT-RBH integrated fleet + EV transition + ULEZ-compliant pool"}
        ],
        "notes": "GSTT's transport line is structurally elevated by a multi-site Central + outer-London estate that became more complex with the February 2021 incorporation of Royal Brompton & Harefield — Harefield in particular adds a Hillingdon-based outer-London leg with substantial inter-site clinical-courier and patient-transfer traffic for cardiothoracic and ECMO pathways. Specimen and pharmacy redistribution between the four core sites is sustained by tertiary cardiothoracic, renal-transplant and paediatric activity. TfL ULEZ and Congestion Charge covering Guy's, St Thomas' and Brompton accelerated fleet electrification. Industrial action 2023-24 drove inter-site agency-medical mileage above plan; CPI fuel pressure remains dominant.",
        "sources": [
            {"publisher": "Guy's and St Thomas' NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.guysandstthomas.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Eligibility Criteria for Patient Transport Services (NEPTS)", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-criteria/"},
            {"publisher": "Transport for London", "title": "ULEZ + Congestion Charge zone", "url": "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Guy's and St Thomas' NHS FT provider profile (RJ1)", "url": "https://www.cqc.org.uk/provider/RJ1"}
        ],
        "related": ["Guy's & St Thomas' NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "London Ambulance Service NHS Trust", "Transport (business + patient) — Royal Free London NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Social security & levy — Isle of Wight NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Isle of Wight NHS Trust"}],
        "description": "Isle of Wight NHS Trust's £19.74M social-security & levy line covers employer NICs (13.8%) and Apprenticeship Levy on a c. 3,200-WTE paybill across England's only fully integrated acute + community + mental-health + ambulance trust on a single offshore site (St Mary's Hospital, Newport). The structurally diverse paybill — including a contained ambulance-paramedic cadre, MH inpatient rosters and a community-services workforce — broadens the employer-NIC base materially relative to a pure-acute peer of similar size, with the offshore-recruitment premium adding shift-allowance NIC.",
        "beneficiaries": "c. 3,200 WTE substantive staff plus contracted bank/agency cover; serves the Isle of Wight resident population c. 140,000 plus c. 1.6M annual visitors; integrated remit covers acute (St Mary's, c. 246 beds), community, mental-health and the IOW ambulance + 999 / NEPTS service.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016 Pt 6) · IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£19.74M"},
            {"label": "Workforce scale", "value": "c. 3,200 WTE substantive across acute + community + MH + ambulance"},
            {"label": "Composition", "value": "Employer NIC (13.8% above secondary threshold) + Apprenticeship Levy (0.5% on paybill > £3M) + Class 1A on benefits"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15% + threshold £9,100 → £5,000 — DHSC partial reimbursement via NHSE allocation"},
            {"label": "Integrated-trust paybill mix", "value": "Acute + community + MH + ambulance combined — England's only single-county integrated trust of this scope; broadens NIC base"},
            {"label": "Offshore-recruitment premium", "value": "Persistent vacancy + agency premium drives shift-allowance NIC layer above mainland-trust peers"},
            {"label": "Industrial action 2023-24 backfill", "value": "Junior doctor + consultant strikes drove agency-medical NIC layer; bank/agency through Solent ferry adds logistics complication"},
            {"label": "NHSE oversight context", "value": "Trust under NHSE Recovery Support Programme since 2017; financial sustainability + workforce plan central to recovery trajectory"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M → 2024-25 £19.74M; Apr 2025 forward uplift"},
            {"label": "Delivery body", "value": "Trust Finance + HR + ESR payroll; HMRC PAYE; NHSBSA pension element parallel; Hampshire Hospitals + Portsmouth tertiary partnership for clinical posts"},
            {"label": "Policy owner", "value": "HMT (NIC + Levy) + HMRC (collection) + DHSC + NHSE Workforce + Hampshire and Isle of Wight ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 financial regime · Successor: NHSE Recovery Support Programme + Hampshire-IOW ICS partnership + Apr 2025 NIC reform"}
        ],
        "notes": "Isle of Wight's social-security line reflects the unusual structural footprint of England's only fully integrated single-county trust covering acute, community, MH and ambulance on one offshore site. The combined remit broadens the employer-NIC base across a wider grade and specialty mix than a pure-acute peer of comparable headcount, and the persistent offshore-recruitment premium drives shift-allowance and agency-cover layers above mainland norms. The trust has been under NHSE Recovery Support Programme oversight since 2017, with workforce sustainability central to recovery. The April 2025 employer-NIC step-up materially raises forward cost; ferry-logistics premium on agency cover is unreimbursed.",
        "sources": [
            {"publisher": "Isle of Wight NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.iow.nhs.uk/About-Us/publications.htm"},
            {"publisher": "HM Revenue & Customs", "title": "Employer NIC + Apprenticeship Levy guidance 2024-25", "url": "https://www.gov.uk/guidance/pay-apprenticeship-levy"},
            {"publisher": "NHS England", "title": "Long Term Workforce Plan 2023 + Recovery Support Programme", "url": "https://www.england.nhs.uk/publication/nhs-long-term-workforce-plan/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Isle of Wight NHS Trust provider profile (R1F)", "url": "https://www.cqc.org.uk/provider/R1F"}
        ],
        "related": ["Isle of Wight NHS Trust", "Staff Costs", "NHS Acute Trusts", "NHS England Long Term Workforce Plan", "Social security & levy — Harrogate and District NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Social security & levy — The Princess Alexandra Hospital NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "The Princess Alexandra Hospital NHS Trust"}],
        "description": "Princess Alexandra Hospital Trust's £19.58M social-security & levy line covers employer NICs (13.8%) and Apprenticeship Levy on a c. 3,500-WTE paybill at the trust's Harlow base — a small DGH (c. 414 beds) with an ageing 1960s estate already prioritised under the New Hospital Programme for full rebuild on a new Kao Park site. RAAC presence in plant rooms and ageing infrastructure have driven elevated agency-medical and bank-nursing cover during 2023-24, layering employer NIC on top of the substantive paybill.",
        "beneficiaries": "c. 3,500 WTE substantive staff plus contracted bank/agency; serves a registered catchment c. 350,000 across Harlow, Epping Forest, Uttlesford and parts of East Hertfordshire; c. 100,000 ED attendances and c. 30,000 elective + non-elective admissions per year.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016 Pt 6) · IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£19.58M"},
            {"label": "Workforce scale", "value": "c. 3,500 WTE substantive + contracted bank/agency cover"},
            {"label": "Composition", "value": "Employer NIC (13.8% above secondary threshold) + Apprenticeship Levy (0.5% on paybill > £3M) + Class 1A"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15% + threshold £9,100 → £5,000 — DHSC partial reimbursement via NHSE allocation"},
            {"label": "NHP cohort + Reset Jan 2025", "value": "Trust in original NHP 40-hospitals programme for full Kao Park rebuild — Reset Jan 2025 deferred construction beyond 2030; agency premium tied to estate quality persists"},
            {"label": "RAAC + estate context", "value": "RAAC plank presence in non-clinical plant rooms; ageing 1960s estate drives premium cover for fragile ward stock + temporary decant"},
            {"label": "Industrial action 2023-24 backfill", "value": "Junior doctor + consultant strikes drove agency-medical NIC layer with IR35 off-payroll application"},
            {"label": "Apprenticeship Levy use", "value": "Drawdown into RNDA + nursing-associate routes; East of England LWAB pipeline coordination"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M → 2024-25 £19.58M; Apr 2025 forward uplift"},
            {"label": "Delivery body", "value": "Trust Finance + HR + ESR payroll; HMRC PAYE; NHSBSA pension element parallel"},
            {"label": "Policy owner", "value": "HMT (NIC + Levy) + HMRC + DHSC + NHSE Workforce + Hertfordshire and West Essex ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NHP cohort estate baseline · Successor: Apr 2025 NIC reform + NHP Kao Park rebuild post-2030"}
        ],
        "notes": "Princess Alexandra Hospital's social-security line is shaped less by headcount growth than by the pay-mix consequences of the trust's estate condition — RAAC plank presence and a 1960s building stock drive a premium for agency-medical and bank-nursing cover that pushes employer-NIC above what a comparable-size DGH on a modern site would carry. The trust's inclusion in the NHP original 40-hospitals cohort for full Kao Park rebuild was confirmed at Reset January 2025 but deferred beyond 2030, sustaining the cover-premium for the medium term. Industrial action 2023-24 added an agency-medical NIC layer subject to IR35. The April 2025 employer-NIC step-up materially raises forward cost.",
        "sources": [
            {"publisher": "The Princess Alexandra Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.pah.nhs.uk/our-publications"},
            {"publisher": "HM Revenue & Customs", "title": "Employer NIC + Apprenticeship Levy guidance 2024-25", "url": "https://www.gov.uk/guidance/pay-apprenticeship-levy"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Plan for Implementation (Reset January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "NHS England", "title": "Long Term Workforce Plan 2023", "url": "https://www.england.nhs.uk/publication/nhs-long-term-workforce-plan/"},
            {"publisher": "Care Quality Commission", "title": "Princess Alexandra Hospital provider profile (RQW)", "url": "https://www.cqc.org.uk/provider/RQW"}
        ],
        "related": ["The Princess Alexandra Hospital NHS Trust", "Staff Costs", "NHS Acute Trusts", "New Hospital Programme", "Social security & levy — Harrogate and District NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Barts Health NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Barts Health NHS Trust"}],
        "description": "Barts Health's £19.52M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's five-site East-and-Central-London estate — Royal London Hospital (Whitechapel, c. 845 beds), St Bartholomew's (Smithfield, specialist cardiac + cancer), Whipps Cross (Leytonstone, c. 460 beds, NHP rebuild cohort), Newham (Plaistow, c. 305 beds) and Mile End. The estate combines the brand-new Royal London PFI tower (2012) and St Bart's PFI (2010) with the ageing Victorian Whipps Cross — driving a wide RV range across hereditaments.",
        "beneficiaries": "England's largest NHS Trust by turnover and the second-largest by paybill, serving a registered catchment c. 2.5M across Tower Hamlets, Newham, Waltham Forest, the City of London and tertiary regional flows for cardiac, cancer and renal services; c. 18,000 WTE staff occupying c. 30+ rated hereditaments.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 · NHS Property Services occupier-rules",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£19.52M"},
            {"label": "Hereditament count", "value": "c. 30+ occupied sites — 5 main hospitals + outpatient + community + admin estate"},
            {"label": "Major rated sites", "value": "Royal London (Whitechapel) + St Bartholomew's (Smithfield) + Whipps Cross (Leytonstone) + Newham (Plaistow) + Mile End"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Billing authorities", "value": "Tower Hamlets LBC (Royal London + Mile End) + City of London Corp (St Bart's) + Waltham Forest LBC (Whipps Cross) + Newham LBC + Hackney LBC; charitable exemption not applicable"},
            {"label": "VOA 2023 revaluation impact", "value": "Material upward rebase on Smithfield + Whitechapel hereditaments tracking Central + East London commercial RV recovery"},
            {"label": "Whipps Cross NHP rebuild", "value": "Whipps Cross in NHP 40-hospitals programme; Reset Jan 2025 confirmed funding to mid-construction; future RV will rebase on new build at completion"},
            {"label": "PFI estate interaction", "value": "Royal London + St Bart's held under 2006 PFI (Skanska Innisfree consortium, Engie/Equans FM) — rates payable by occupier (trust), not SPV"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2024-25 £19.52M — sustained Central London RV uplift + new-build coming on-stream"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 5 billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance + NE London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023 3-year cycle + Whipps Cross NHP rebuild rebase"}
        ],
        "notes": "Barts Health's business-rates line is the largest in the acute-trust sector, reflecting the scale and Central London location of the estate. The Royal London (Whitechapel) and St Bartholomew's (Smithfield) PFI towers carry premium per-m² RV consistent with their City-fringe and East-London locations, while Whipps Cross's Victorian fabric still generates meaningful rates pending NHP rebuild. The 2023 VOA revaluation rebased Central + East London hereditaments upward; the Autumn Statement 2023 UBR freeze gave a one-year reprieve, and the 2026 revaluation under NDRA 2023 is expected to push the line further. Whipps Cross NHP rebuild was confirmed at Reset January 2025 — on completion the new asset will rebase RV substantially.",
        "sources": [
            {"publisher": "Barts Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bartshealth.nhs.uk/our-annual-report"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Plan for Implementation (Reset January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Care Quality Commission", "title": "Barts Health NHS Trust provider profile (R1H)", "url": "https://www.cqc.org.uk/provider/R1H"}
        ],
        "related": ["Barts Health NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Valuation Office Agency", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Royal Free London's £19.51M transport line covers staff business mileage, the trust pool fleet (right-of-use under IFRS 16), inter-site clinical-courier runs across the Royal Free (Hampstead), Barnet and Chase Farm (Enfield) sites, and patient-transport contracts for non-emergency conveyance. The trust's hub-and-spoke design — with major specialty consolidation at the Hampstead hub (HIV, hepatology, renal-transplant, infectious diseases) — drives sustained inter-site movement of patients, specimens and medical staff across four boroughs.",
        "beneficiaries": "c. 13,000 WTE workforce across the Royal Free (Hampstead, c. 850 beds), Barnet (c. 460 beds) and Chase Farm (Enfield, planned-care hub, opened 2018); serves a registered catchment c. 1.6M across Camden, Barnet, Enfield, Haringey and tertiary regional flows for renal transplantation, HIV, hepatology and infectious diseases.",
        "legal_basis": "NHS Act 2006 · NHS England Patient Transport Services Eligibility Criteria · Agenda for Change Section 17 · HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£19.51M"},
            {"label": "Site footprint", "value": "Royal Free (Hampstead) + Barnet (Wellhouse Lane) + Chase Farm (Enfield, planned-care hub) + community-clinic estate"},
            {"label": "Hub-and-spoke design", "value": "Major-specialty consolidation at Hampstead (HIV, hepatology, renal-transplant, infectious diseases) drives inter-site patient + specimen flow"},
            {"label": "Chase Farm 2018 rebuild", "value": "New planned-care hub opened 2018 — paperless digital design + dedicated planned-care flow added inter-site logistics layer"},
            {"label": "PTS contractor", "value": "Patient-transport via contracted PTS providers (London region tendered) plus LAS for emergency + s.136 conveyance"},
            {"label": "ULEZ", "value": "TfL ULEZ covers all three sites — fleet renewal accelerated to comply; staff-mileage premium in zone"},
            {"label": "Pool fleet IFRS 16", "value": "ROU asset + lease liability per IFRS 16 — depreciation + interest split since 2022 transition"},
            {"label": "Industrial action 2023-24", "value": "Junior doctor + consultant strikes raised inter-site agency-medical mileage + courier shifts"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M → 2024-25 £19.51M — CPI fuel + multi-site uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Travel team + contracted PTS provider + London Ambulance Service"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NC London ICB; TfL for road-charging interaction"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 Chase Farm legacy site · Successor: integrated RFL Group fleet + EV transition + ULEZ-compliant pool"}
        ],
        "notes": "Royal Free London's transport line reflects a hub-and-spoke clinical model where major-specialty consolidation at the Hampstead site for HIV, hepatology, renal transplantation and infectious diseases drives sustained inter-site patient, specimen and medical-staff movement to and from Barnet and Chase Farm. The 2018 Chase Farm planned-care rebuild — Royal Free's flagship paperless digital site — added a dedicated planned-care flow that increased inter-site logistics. The TfL ULEZ now covers all three main sites, accelerating fleet electrification and adding a per-mile premium for non-compliant vehicles. Industrial action 2023-24 drove additional inter-site agency-medical mileage; CPI fuel pressure remains the dominant cost driver, partially offset by hybrid + EV pool transition.",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information-publications/"},
            {"publisher": "NHS England", "title": "Eligibility Criteria for Patient Transport Services (NEPTS)", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-criteria/"},
            {"publisher": "Transport for London", "title": "ULEZ + Congestion Charge zone", "url": "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Free London NHS FT provider profile (RAL)", "url": "https://www.cqc.org.uk/provider/RAL"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "London Ambulance Service NHS Trust", "Transport (business + patient) — Guy's & St Thomas' NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Chelsea and Westminster Hospital NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
        "description": "Chelsea and Westminster's £19.47M PFI / LIFT line reflects the unitary-charge pass-through on the trust's Chelsea & Westminster Hospital site (Fulham Road, opened 1993 — among the earliest NHS hospital PFIs) plus subsequent service-concession works. The line covers the debt-service component, hard-FM lifecycle and soft-FM bundle (cleaning, security, portering, catering) under the contract. The trust also operates West Middlesex University Hospital (acquired 2015), which carries its own historic FM / lifecycle arrangements outside this PFI charge.",
        "beneficiaries": "c. 7,500 WTE workforce across Chelsea and Westminster Hospital (Fulham Road, c. 430 beds) and West Middlesex (Isleworth, c. 380 beds); serves a registered catchment c. 1.5M across Kensington & Chelsea, Hammersmith & Fulham, Hounslow, Richmond, Wandsworth and Westminster; c. 1M outpatient attendances and c. 130,000 ED attendances.",
        "legal_basis": "IFRS 16 Leases (post-2022 transition for finance-lease + service-concession components) · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · DHSC PFI guidance · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£19.47M"},
            {"label": "PFI vehicle", "value": "Chelsea and Westminster Hospital PFI — original 1993 build (first-generation NHS PFI), with subsequent variations + lifecycle works"},
            {"label": "Estate covered", "value": "Chelsea and Westminster Hospital (Fulham Road) main building + plant + service-concession components"},
            {"label": "Unitary charge composition", "value": "Debt-service + hard-FM lifecycle (building maintenance, M&E plant) + soft-FM bundle (cleaning, security, portering, catering)"},
            {"label": "Contract duration profile", "value": "First-generation PFI signed early 1990s — contract approaching hand-back later this decade; trust + ICS preparing transition planning"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession asset on-balance-sheet under IFRIC 12; lease component re-evaluated under IFRS 16 ch.7 GAM since 2022"},
            {"label": "Lifecycle indexation + WMUH boundary", "value": "Annual RPI / CPI indexation per contract; West Middlesex (acquired Sep 2015) carries separate FM history outside this PFI charge"},
            {"label": "Funding trajectory", "value": "2020-21 c. £15M → 2022-23 c. £17M → 2024-25 £19.47M — sustained CPI / RPI uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + PFI SPV + FM contractor (historic Engie / now Equans variants on first-generation PFIs)"},
            {"label": "Policy owner", "value": "DHSC PFI guidance + IPA Operational PFI Centre of Excellence + NHSE Provider Finance + NW London ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI / PF2 review 2018 + ongoing IPA hand-back guidance; trust ARA 2023-24 disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI early-1990s NHS Estates capital model · Successor: PFI hand-back transition + post-contract estate planning"}
        ],
        "notes": "Chelsea and Westminster's PFI line is a first-generation NHS PFI — the Fulham Road hospital opened 1993 was among the earliest privately financed NHS hospital builds, predating the formal PFI policy framework's later standardisation. CPI / RPI indexation drives steady cost growth on top of fixed debt-service and hard-FM lifecycle components. The contract is among the earliest in the NHS PFI hand-back wave, with trust and NW London ICB scoping transition arrangements; the IPA Operational PFI Centre of Excellence has issued sector-wide hand-back guidance to manage the cliff-edge. West Middlesex University Hospital (acquired September 2015) has its own historic FM and lifecycle arrangements outside this PFI charge.",
        "sources": [
            {"publisher": "Chelsea and Westminster Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chelwest.nhs.uk/about-us/publications"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 review 2018", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Infrastructure and Projects Authority", "title": "Operational PFI hand-back guidance", "url": "https://www.gov.uk/government/collections/operational-pfi-contracts"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Chelsea and Westminster NHS FT provider profile (RQM)", "url": "https://www.cqc.org.uk/provider/RQM"}
        ],
        "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Infrastructure and Projects Authority", "PFI / LIFT charges — Mersey Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Social security & levy — The Rotherham NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "The Rotherham NHS Foundation Trust"}],
        "description": "Rotherham FT's £19.41M social-security & levy line covers employer NICs (13.8%) and the Apprenticeship Levy on a c. 4,400-WTE paybill at Rotherham General Hospital (Moorgate Road, c. 480 beds) plus the trust's community-services arm covering the borough of Rotherham. The trust's combined acute + community model — incorporating district-nursing, community-MSK, community-paediatrics and adult therapies — broadens the Band-3/4 support-worker and Band-5/6 nursing layer above pure-acute peers, lifting employer NIC against the substantive paybill.",
        "beneficiaries": "c. 4,400 WTE substantive staff plus contracted bank/agency cover; serves a registered catchment c. 265,000 across Rotherham borough and adjacent South Yorkshire postcodes; integrated remit covers acute hospital + community-services for the resident population; tertiary flow into Sheffield Teaching for major-specialty.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016 Pt 6) · IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£19.41M"},
            {"label": "Workforce scale", "value": "c. 4,400 WTE substantive across acute + community"},
            {"label": "Composition", "value": "Employer NIC (13.8% above secondary threshold) + Apprenticeship Levy (0.5% on paybill > £3M) + Class 1A"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15% + threshold £9,100 → £5,000 — DHSC partial reimbursement via NHSE allocation"},
            {"label": "Combined acute + community paybill", "value": "District-nursing + community-MSK + community-paediatrics broaden Band-3/4 + Band-5/6 nursing layer beyond pure-acute peers"},
            {"label": "Industrial action 2023-24 backfill", "value": "Junior doctor + consultant strikes drove agency-medical NIC layer; bank/agency activity peaked Q3 2023-24"},
            {"label": "Apprenticeship Levy + ICS context", "value": "Drawdown into RNDA + nursing-associate routes; South Yorkshire ICS levy-pooling explored, workforce planning aligned with Sheffield Teaching tertiary partnership"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M → 2024-25 £19.41M; Apr 2025 forward uplift"},
            {"label": "Delivery body", "value": "Trust Finance + HR + ESR payroll; HMRC PAYE; NHSBSA pension element parallel"},
            {"label": "Policy owner", "value": "HMT (NIC + Levy) + HMRC (collection) + DHSC + NHSE Workforce + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 remuneration report; NHSE LTWP 2023; CQC inspection 2024"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 Apprenticeship Levy + 2014 trust integration with Rotherham community services · Successor: Apr 2025 NIC reform + South Yorkshire ICS workforce strategy"}
        ],
        "notes": "Rotherham's social-security line reflects a combined acute + community trust where district-nursing, community-MSK and community-paediatrics extend the paybill into Band-3/4 and Band-5/6 grades not normally captured at pure-acute peers, broadening the employer-NIC base. Industrial action in 2023-24 added an agency-medical layer subject to IR35 off-payroll rules. The trust sits within the South Yorkshire ICS alongside Sheffield Teaching, which provides the major-specialty tertiary partnership; ICS-level workforce planning is now driving levy-pooling experimentation. The April 2025 employer-NIC step-up materially raises forward cost; DHSC partial reimbursement via NHSE softens the impact, but contracted-out functions such as FM and catering remain unreimbursed at the trust boundary.",
        "sources": [
            {"publisher": "The Rotherham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.therotherhamft.nhs.uk/About_Us/Annual_Reports/"},
            {"publisher": "HM Revenue & Customs", "title": "Employer NIC + Apprenticeship Levy guidance 2024-25", "url": "https://www.gov.uk/guidance/pay-apprenticeship-levy"},
            {"publisher": "NHS England", "title": "Long Term Workforce Plan 2023", "url": "https://www.england.nhs.uk/publication/nhs-long-term-workforce-plan/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Rotherham NHS FT provider profile (RFR)", "url": "https://www.cqc.org.uk/provider/RFR"}
        ],
        "related": ["The Rotherham NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "NHS England Long Term Workforce Plan", "Social security & levy — Harrogate and District NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Imperial College Healthcare NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Imperial College Healthcare NHS Trust"}],
        "description": "Imperial College Healthcare's £19.30M general supplies & services line covers non-clinical consumables, ward provisions, household goods, laundry materials and small operational equipment across the trust's five hospital sites — Charing Cross, Hammersmith, St Mary's (Paddington, NHP cohort), Queen Charlotte's & Chelsea and Western Eye. The trust's tertiary academic-medical-centre status alongside Imperial College London drives a complex consumables mix layered onto a high-volume acute baseline, with Procurement Act 2023 transition reshaping framework architecture from February 2025.",
        "beneficiaries": "c. 14,000 WTE workforce across five Central + West London sites; serves a registered catchment c. 1.7M across NW London plus tertiary regional and national flows for cardiac, vascular, renal-transplant, neonatal and major trauma at the St Mary's Major Trauma Centre; c. 1.2M outpatient attendances per year.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (consumables procurement, transitional) · Procurement Act 2023 (in force 24 Feb 2025)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£19.30M"},
            {"label": "Site footprint generating consumption", "value": "Charing Cross + Hammersmith + St Mary's + Queen Charlotte's & Chelsea + Western Eye"},
            {"label": "Bed-stock", "value": "c. 1,400 inpatient beds across 5 sites; c. 280,000 ED + UTC attendances per year"},
            {"label": "Composition", "value": "Non-clinical consumables + ward provisions + household goods + laundry materials + small operational equipment + minor catering provisions"},
            {"label": "AMC + tertiary driver", "value": "Imperial College AMC partnership + tertiary cardiac, vascular, renal-transplant, neonatal + Major Trauma Centre at St Mary's drive specialist consumables layer"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (majority) + Crown Commercial Service category contracts + minor local spot-buy + AMC research-aligned procurement"},
            {"label": "Procurement Act 2023 transition", "value": "New regime live 24 Feb 2025 — central digital platform + transparency obligations replace PCR 2015"},
            {"label": "St Mary's NHP rebuild", "value": "St Mary's Paddington in NHP 40-hospitals programme; Reset Jan 2025 confirmed funding to construction beyond 2030 — supply lines reshape on completion"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M → 2024-25 £19.30M — supplies CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + Estates & Facilities + AMC research-procurement coordination"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NW London ICB + NHS Supply Chain governance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 fragmented spot-buy regime · Successor: NHS Supply Chain Future Operating Model + Procurement Act 2023 + St Mary's NHP rebuild"}
        ],
        "notes": "Imperial College Healthcare's general supplies line reflects the consumables footprint of one of the largest NHS academic medical centres — five Central + West London sites operating tertiary cardiac, vascular, renal-transplant, neonatal and major-trauma services alongside high-volume acute activity at St Mary's. AMC partnership with Imperial College London adds a research-aligned procurement layer overlaying NHS Supply Chain category buys. The Procurement Act 2023 came into force 24 February 2025, replacing PCR 2015; the trust is mid-transition. St Mary's Paddington remains in the NHP cohort with funding confirmed to construction at Reset January 2025 — supply lines will reshape materially on completion.",
        "sources": [
            {"publisher": "Imperial College Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.imperial.nhs.uk/about-us/annual-reports"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Plan for Implementation (Reset January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Care Quality Commission", "title": "Imperial College Healthcare NHS Trust provider profile (RYJ)", "url": "https://www.cqc.org.uk/provider/RYJ"}
        ],
        "related": ["Imperial College Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "New Hospital Programme", "Department of Health and Social Care"]
    },
    "General supplies & services — Royal Cornwall Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Royal Cornwall Hospitals NHS Trust"}],
        "description": "Royal Cornwall's £19.25M general supplies & services line covers non-clinical consumables, ward provisions, household goods, laundry materials and small operational equipment across the trust's three sites — the Royal Cornwall Hospital (Truro, c. 720 beds), West Cornwall Hospital (Penzance) and St Michael's Hospital (Hayle). The peripheral Cornwall geography drives a logistics premium on framework deliveries from the NHS Supply Chain Bridgwater RDC and a higher minimum-order tail than urban acute peers, with Procurement Act 2023 transition reshaping framework architecture from February 2025.",
        "beneficiaries": "c. 6,000 WTE workforce across three sites covering Cornwall and the Isles of Scilly; serves the resident population c. 570,000 plus seasonal visitor surge; tertiary outflow to Plymouth (Derriford) and Bristol (UHBW) for specialist services; c. 95,000 ED attendances and c. 35,000 elective + non-elective admissions per year.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (transitional) · Procurement Act 2023 (in force 24 Feb 2025)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£19.25M"},
            {"label": "Site footprint generating consumption", "value": "Royal Cornwall Hospital (Truro) + West Cornwall Hospital (Penzance) + St Michael's Hospital (Hayle)"},
            {"label": "Bed-stock", "value": "c. 800 inpatient beds across three sites"},
            {"label": "Composition", "value": "Non-clinical consumables + ward provisions + household goods + laundry materials + small operational equipment"},
            {"label": "Peripheral-geography premium", "value": "Cornwall location drives logistics premium on framework deliveries; NHS Supply Chain Bridgwater RDC serves SW England"},
            {"label": "Seasonal surge driver", "value": "Summer visitor influx adds c. 200,000 transient population — ED-pathway consumables peak Q2-Q3"},
            {"label": "Procurement route + Procurement Act 2023", "value": "NHS Supply Chain framework majority + CCS category contracts + minor spot-buy; Procurement Act 2023 live 24 Feb 2025 replaces PCR 2015"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M → 2024-25 £19.25M — supplies CPI + post-pandemic activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + Estates & Facilities teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cornwall and Isles of Scilly ICB + NHS Supply Chain governance"},
            {"label": "Evaluation evidence", "value": "NHS Supply Chain framework data; Trust ARA 2023-24 disclosure; CQC inspection 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 fragmented spot-buy regime · Successor: NHS Supply Chain Future Operating Model + Procurement Act 2023"}
        ],
        "notes": "Royal Cornwall's general supplies line is structurally elevated by the peripheral Cornwall geography — the Bridgwater NHS Supply Chain regional distribution centre serves the South West, but the last-mile run from Bridgwater to Truro and onward to Penzance and Hayle adds a logistics premium not present at urban acute peers. The summer visitor surge across Cornwall drives a Q2-Q3 ED-pathway consumables peak, with a transient population uplift of c. 200,000 lifting per-bed consumption above resident-only modelling. The Procurement Act 2023 came into force 24 February 2025, replacing PCR 2015 with a central digital platform and stronger transparency obligations. CPI on supplies remains the dominant cost driver post-pandemic; activity recovery has restored consumption above 2019-20 baseline.",
        "sources": [
            {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalcornwall.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model + regional distribution centres", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Cornwall Hospitals NHS Trust provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"}
        ],
        "related": ["Royal Cornwall Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Imperial College Healthcare NHS Trust", "Department of Health and Social Care"]
    },
    "Social security & levy — James Paget University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "James Paget University Hospitals NHS Foundation Trust"}],
        "description": "James Paget's £19.18M social-security & levy line covers employer NICs (13.8%) and Apprenticeship Levy on a c. 3,200-WTE paybill at the James Paget University Hospital (Gorleston-on-Sea, c. 500 beds). The trust is in the New Hospital Programme original 40-hospitals cohort for full rebuild and is among the most acute RAAC-affected Acute trusts on the September 2023 HSSIB list, with extensive concrete-plank presence driving elevated agency cover and decant-related shift premiums that layer additional employer NIC on the substantive paybill.",
        "beneficiaries": "c. 3,200 WTE substantive staff plus contracted bank/agency cover; serves a registered catchment c. 230,000 across Great Yarmouth, Waveney + adjacent East Norfolk + North Suffolk coastal communities; c. 65,000 ED attendances and c. 28,000 elective + non-elective admissions per year.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016 Pt 6) · IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£19.18M"},
            {"label": "Workforce scale", "value": "c. 3,200 WTE substantive + contracted bank/agency"},
            {"label": "Composition", "value": "Employer NIC (13.8% above secondary threshold) + Apprenticeship Levy (0.5% on paybill > £3M) + Class 1A"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15% + threshold £9,100 → £5,000 — DHSC partial reimbursement via NHSE allocation"},
            {"label": "RAAC + NHP context", "value": "Trust on Sep 2023 HSSIB RAAC list with extensive plank presence; in NHP 40-hospitals cohort for full rebuild — Reset Jan 2025 confirmed funding to construction"},
            {"label": "Decant-related premium", "value": "RAAC-affected ward closures + temporary structures drive shift-allowance + agency NIC layer above non-RAAC peers"},
            {"label": "Industrial action + recruitment premium", "value": "2023-24 strikes drove agency-medical NIC layer (IR35 off-payroll); persistent vacancy + agency premium across Great Yarmouth + Waveney coastal labour market"},
            {"label": "Funding trajectory", "value": "2020-21 c. £13M → 2022-23 c. £16M → 2024-25 £19.18M; Apr 2025 forward uplift"},
            {"label": "Delivery body", "value": "Trust Finance + HR + ESR payroll; HMRC PAYE; NHSBSA pension element parallel"},
            {"label": "Policy owner", "value": "HMT (NIC + Levy) + HMRC (collection) + DHSC + NHSE Workforce + Norfolk and Waveney ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 remuneration report; HSSIB RAAC report Sep 2023; NAO RAAC review 2024"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC-discovery baseline · Successor: NHP rebuild + Apr 2025 NIC reform"}
        ],
        "notes": "James Paget's social-security line carries a structural premium driven by the trust's RAAC and rebuild context — the September 2023 HSSIB list confirmed extensive concrete-plank presence, and inclusion in the NHP 40-hospitals cohort for full rebuild was reaffirmed at Reset January 2025 with funding to construction. Decant arrangements, temporary structures and ward-closure cycles drive shift-allowance and agency cover above non-RAAC peers, layering additional employer-NIC on a workforce already exposed to a coastal-labour-market recruitment premium across Great Yarmouth and Waveney. Industrial action 2023-24 added an agency-medical NIC layer subject to IR35. The April 2025 NIC step-up materially raises forward cost.",
        "sources": [
            {"publisher": "James Paget University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.jpaget.nhs.uk/about-us/publications/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC investigation Sep 2023", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Plan for Implementation (Reset January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "HM Revenue & Customs", "title": "Employer NIC + Apprenticeship Levy guidance 2024-25", "url": "https://www.gov.uk/guidance/pay-apprenticeship-levy"},
            {"publisher": "Care Quality Commission", "title": "James Paget University Hospitals NHS FT provider profile (RGP)", "url": "https://www.cqc.org.uk/provider/RGP"}
        ],
        "related": ["James Paget University Hospitals NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "New Hospital Programme", "Social security & levy — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Social security & levy — Salisbury NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Salisbury NHS Foundation Trust"}],
        "description": "Salisbury FT's £19.17M social-security & levy line covers employer NICs (13.8%) and Apprenticeship Levy on a c. 4,300-WTE paybill at Salisbury District Hospital (Odstock) — a DGH plus host of two regional specialist services: the Wessex Spinal Cord Injuries Centre and the Duke of Cornwall Spinal Treatment Centre, plus the Burns Unit and Plastic Surgery service. The specialist-cadre paybill mix — including high-grade rehabilitation and burns specialists — adds an upper-Band layer that lifts employer NIC against the substantive workforce profile.",
        "beneficiaries": "c. 4,300 WTE substantive staff plus contracted bank/agency cover; serves a registered acute catchment c. 270,000 across South Wiltshire, parts of Hampshire and Dorset, plus regional specialist catchment for spinal cord injuries (Wessex), burns and plastic surgery extending across central southern England.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016 Pt 6) · IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£19.17M"},
            {"label": "Workforce scale", "value": "c. 4,300 WTE substantive + contracted bank/agency"},
            {"label": "Composition", "value": "Employer NIC (13.8% above secondary threshold) + Apprenticeship Levy (0.5% on paybill > £3M) + Class 1A"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15% + threshold £9,100 → £5,000 — DHSC partial reimbursement via NHSE allocation"},
            {"label": "Specialist-cadre paybill mix", "value": "Wessex Spinal Cord Injuries Centre + Burns + Plastic Surgery specialists add upper-Band layer beyond pure-DGH peer"},
            {"label": "Industrial action 2023-24 backfill", "value": "Junior doctor + consultant strikes drove agency-medical NIC layer; specialist-cover continuity priorities sustained agency premium"},
            {"label": "Apprenticeship Levy + ICS context", "value": "Levy drawdown into RNDA + nursing-associate routes + specialist-rehab pathway development under Wessex regional partnership; trust within BSW ICS aligned with Great Western + RUH"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M → 2024-25 £19.17M; Apr 2025 forward uplift"},
            {"label": "Delivery body", "value": "Trust Finance + HR + ESR payroll; HMRC PAYE; NHSBSA pension element parallel"},
            {"label": "Policy owner", "value": "HMT (NIC + Levy) + HMRC (collection) + DHSC + NHSE Workforce + BSW ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 remuneration report; NHSE LTWP 2023; CQC inspection 2023"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 Apprenticeship Levy regime · Successor: Apr 2025 NIC reform + LTWP expansion + BSW ICS workforce strategy"}
        ],
        "notes": "Salisbury's social-security line reflects a DGH that hosts disproportionately specialist services — the Wessex Spinal Cord Injuries Centre and the Duke of Cornwall Spinal Treatment Centre, the regional Burns Unit and Plastic Surgery service all draw an upper-Band consultant and specialist-AHP cadre that lifts the employer-NIC base above what a pure DGH of similar size would carry. Industrial action 2023-24 added an agency-medical NIC layer with continuity priorities for specialist services sustaining elevated agency cover. Apprenticeship Levy drawdown is increasingly directed at specialist-rehabilitation pathways under the Wessex regional partnership. The April 2025 NIC step-up raises forward cost; specialist-cadre premium remains structurally embedded.",
        "sources": [
            {"publisher": "Salisbury NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.salisbury.nhs.uk/about-us/about-the-trust/publications/"},
            {"publisher": "HM Revenue & Customs", "title": "Employer NIC + Apprenticeship Levy guidance 2024-25", "url": "https://www.gov.uk/guidance/pay-apprenticeship-levy"},
            {"publisher": "NHS England", "title": "Long Term Workforce Plan 2023", "url": "https://www.england.nhs.uk/publication/nhs-long-term-workforce-plan/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Salisbury NHS FT provider profile (RNZ)", "url": "https://www.cqc.org.uk/provider/RNZ"}
        ],
        "related": ["Salisbury NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "NHS England Long Term Workforce Plan", "Social security & levy — Harrogate and District NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Social security & levy — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Queen Elizabeth Hospital King's Lynn NHS Foundation Trust"}],
        "description": "QEH King's Lynn's £19.12M social-security & levy line covers employer NICs (13.8%) and Apprenticeship Levy on a c. 3,400-WTE paybill at the Queen Elizabeth Hospital (King's Lynn, c. 510 beds). The trust is among the most acutely RAAC-affected hospitals in England — extensive concrete-plank presence drove a sustained ward-by-ward fail-safe propping programme — and is in the New Hospital Programme original cohort for full rebuild, with the resultant decant + agency premium driving employer NIC above non-RAAC peer baselines.",
        "beneficiaries": "c. 3,400 WTE substantive staff plus contracted bank/agency cover; serves a registered catchment c. 250,000 across West Norfolk, North Cambridgeshire, South Lincolnshire and Eastern Norfolk fenland; c. 75,000 ED attendances and c. 30,000 elective + non-elective admissions per year.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016 Pt 6) · IAS 19 Employee Benefits · Public Sector Exit Payments Regulations 2020 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£19.12M"},
            {"label": "Workforce scale", "value": "c. 3,400 WTE substantive + contracted bank/agency"},
            {"label": "Composition", "value": "Employer NIC (13.8% above secondary threshold) + Apprenticeship Levy (0.5% on paybill > £3M) + Class 1A"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15% + threshold £9,100 → £5,000 — DHSC partial reimbursement via NHSE allocation"},
            {"label": "RAAC + NHP context", "value": "Among most RAAC-affected acute trusts on Sep 2023 HSSIB list — extensive ward-by-ward propping; in NHP 40-hospitals cohort confirmed to construction at Reset Jan 2025"},
            {"label": "Decant-related premium", "value": "RAAC-affected ward closures + temporary structures + propping operations drive shift-allowance + agency NIC layer"},
            {"label": "Industrial action + recruitment premium", "value": "2023-24 strikes drove agency-medical NIC layer (IR35 off-payroll); persistent vacancy across West Norfolk + East Cambridgeshire fenland labour market sustains agency premium"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £17M → 2024-25 £19.12M; Apr 2025 forward uplift"},
            {"label": "Delivery body", "value": "Trust Finance + HR + ESR payroll; HMRC PAYE; NHSBSA pension element parallel"},
            {"label": "Policy owner", "value": "HMT (NIC + Levy) + HMRC + DHSC + NHSE Workforce + Norfolk and Waveney ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 remuneration report; HSSIB RAAC investigation Sep 2023; NAO RAAC review 2024"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC-discovery baseline · Successor: NHP rebuild + Apr 2025 NIC reform"}
        ],
        "notes": "QEH King's Lynn's social-security line is among the most acutely RAAC-shaped in the sector — the trust hosts one of the most extensive concrete-plank presences identified on the September 2023 HSSIB list, and ward-by-ward fail-safe propping has driven sustained shift-allowance and agency cover that layers additional employer-NIC on an already-stretched paybill. The trust's place in the NHP 40-hospitals cohort was reaffirmed at Reset January 2025 with funding to construction, locking in the medium-term rebuild path. The fenland labour-market context across West Norfolk and East Cambridgeshire sustains a recruitment-premium compounding RAAC-driven cover need. The April 2025 NIC step-up raises forward cost; RAAC + recruitment premia remain structurally elevated.",
        "sources": [
            {"publisher": "Queen Elizabeth Hospital King's Lynn NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qehkl.nhs.uk/about-us/our-publications/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC investigation Sep 2023", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Plan for Implementation (Reset January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "HM Revenue & Customs", "title": "Employer NIC + Apprenticeship Levy guidance 2024-25", "url": "https://www.gov.uk/guidance/pay-apprenticeship-levy"},
            {"publisher": "Care Quality Commission", "title": "QEH King's Lynn NHS FT provider profile (RCX)", "url": "https://www.cqc.org.uk/provider/RCX"}
        ],
        "related": ["Queen Elizabeth Hospital King's Lynn NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "New Hospital Programme", "Social security & levy — James Paget University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — South Warwickshire NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "South Warwickshire NHS Foundation Trust"}],
        "description": "South Warwickshire's £19.01M establishment costs line covers postage, telephony, IT consumables, training, recruitment, advertising, courier, printing, hospitality, subscriptions and professional fees on a combined acute + community footprint anchored at Warwick Hospital and extending across community-services bases in Stratford-upon-Avon, Leamington Spa, Rugby, Nuneaton and Coventry post-2024 expansion. The trust's accelerating-merger trajectory with Wye Valley NHS Trust (proposed group model 2024) drives elevated change-management, legal and integration costs.",
        "beneficiaries": "c. 5,500 WTE substantive workforce across acute + community sites; serves a registered acute catchment c. 290,000 across Warwick, Stratford and South Warwickshire plus community-services reach to c. 600,000 across Coventry, Rugby, Nuneaton and adjacent areas under Coventry & Warwickshire community contracts.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (transitional) · Procurement Act 2023 (in force 24 Feb 2025)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£19.01M"},
            {"label": "Workforce scale", "value": "c. 5,500 WTE across acute + community"},
            {"label": "Composition", "value": "Postage + telephony + IT consumables + training + recruitment + advertising + courier + printing + hospitality + subscriptions + professional fees + legal"},
            {"label": "Combined acute + community driver", "value": "Multi-site community estate across South Warwickshire + Coventry expansion drives postal + courier + telephony + training cost layer above pure-acute peers"},
            {"label": "Wye Valley group-model context", "value": "Proposed 2024 group/integration with Wye Valley NHS Trust under shared chief executive — drives elevated legal, change-management, due-diligence, integration cost"},
            {"label": "FD EPR + industrial action", "value": "Frontline Digitisation training + cutover prep generates IT-consumable + training spend; 2023-24 strikes drove agency advertising + recruitment-spend + legal cost"},
            {"label": "Procurement Act 2023 transition", "value": "New regime live 24 Feb 2025 — central digital platform + transparency obligations replace PCR 2015"},
            {"label": "Funding trajectory", "value": "2020-21 c. £14M → 2022-23 c. £16M → 2024-25 £19.01M — uplift driven by FD EPR + Wye Valley integration + post-pandemic recovery"},
            {"label": "Delivery body", "value": "Trust Corporate Services + IT + Workforce + Estates + procurement teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Coventry and Warwickshire ICB; NHSE FD programme oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; NHSE FD programme assurance; CQC 'Outstanding' rating context (community)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Wye Valley-integration baseline · Successor: SWFT-Wye Valley group + Procurement Act 2023 + FD EPR full deployment"}
        ],
        "notes": "South Warwickshire's establishment costs line reflects a trust in active strategic transition — the proposed 2024 group/integration with Wye Valley NHS Trust under a shared chief executive drives elevated legal, change-management, due-diligence and integration costs, layered on routine corporate-overhead recovery post-pandemic. The combined acute + community footprint, with community-services contracts extending into Coventry, Rugby and Nuneaton, supports a multi-site postal, courier, telephony and training cost layer above pure-acute peers. Frontline Digitisation EPR rollout adds training, change-management and IT-consumable cost. The Procurement Act 2023 came into force 24 February 2025, adding transition-period legal-advice spend.",
        "sources": [
            {"publisher": "South Warwickshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swft.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Warwickshire NHS FT provider profile (RJC)", "url": "https://www.cqc.org.uk/provider/RJC"}
        ],
        "related": ["South Warwickshire NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Wye Valley NHS Trust", "Establishment costs — University Hospitals Birmingham NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — University Hospitals Birmingham NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospitals Birmingham NHS Foundation Trust"}],
        "description": "UHB's £18.42M establishment costs line covers postage, telephony, IT consumables, training, recruitment, advertising, courier, printing, hospitality, subscriptions, professional fees and legal across England's largest NHS trust by paybill — Queen Elizabeth Hospital Birmingham (Edgbaston, c. 1,215 beds), Heartlands (Bordesley Green), Good Hope (Sutton Coldfield) and Solihull post-2018 merger with HEFT. Sustained governance scrutiny since the 2022 Bewick Review and a continuing leadership-renewal cycle drive elevated legal, recruitment and external-advice costs.",
        "beneficiaries": "c. 22,000 WTE substantive workforce across four hospital sites; serves a registered catchment c. 2.2M across Birmingham, Solihull, North Warwickshire plus tertiary regional and national flows for liver and cardiac transplantation, major trauma, military Critical Care, and complex burns at the QEHB Royal Centre for Defence Medicine.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (transitional) · Procurement Act 2023 (in force 24 Feb 2025)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£18.42M"},
            {"label": "Workforce scale", "value": "c. 22,000 WTE across four hospital sites"},
            {"label": "Composition", "value": "Postage + telephony + IT consumables + training + recruitment + advertising + courier + printing + hospitality + subscriptions + professional fees + legal"},
            {"label": "Bewick Review context", "value": "2022 independent review (Prof Mike Bewick) into UHB culture + governance — drove sustained legal, governance-review + remediation cost; rolling action plan oversight by NHSE"},
            {"label": "2018 HEFT merger legacy", "value": "Heart of England integration — sustained corporate-services consolidation costs; legacy site infrastructure churn at Heartlands + Solihull"},
            {"label": "FD EPR + industrial action", "value": "Oracle Health (Cerner) Millennium EPR — long-running programme drives training + change-management + IT-consumable line; 2023-24 strikes drove AMC-scale agency advertising + recruitment + legal cost"},
            {"label": "Procurement Act 2023 transition", "value": "New regime live 24 Feb 2025 — central digital platform + transparency obligations replace PCR 2015"},
            {"label": "Funding trajectory", "value": "2020-21 c. £15M → 2022-23 c. £17M → 2024-25 £18.42M — uplift driven by Bewick remediation + FD EPR + post-pandemic recovery"},
            {"label": "Delivery body", "value": "Trust Corporate Services + IT + Workforce + Estates + procurement teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Birmingham and Solihull ICB; NHSE FD programme + governance oversight"},
            {"label": "Evaluation evidence", "value": "Bewick Reviews 2022-2023; NHSE rolling oversight; trust ARA 2023-24 disclosure; CQC inspections 2023-2024"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 UHB / HEFT separate trusts · Successor: post-Bewick governance + Procurement Act 2023 + FD EPR full deployment"}
        ],
        "notes": "UHB's establishment costs line carries a structural premium driven by the post-2022 Bewick Review remediation programme — the independent governance and culture review (Prof Mike Bewick) drove a sustained legal, governance-advice and external-review cost layer, with NHSE rolling oversight extending the remediation cycle through 2023-2024. Layered on this is continuing legacy cost from the 2018 HEFT merger consolidation, the Oracle Health Millennium EPR programme generating training and change-management cost, and AMC-scale 2023-24 industrial-action recruitment activity. The Procurement Act 2023 came into force 24 February 2025, adding transition-period legal-advice spend.",
        "sources": [
            {"publisher": "University Hospitals Birmingham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhb.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Bewick Review of UHB + rolling oversight", "url": "https://www.england.nhs.uk/midlands/2022/03/24/independent-review-into-the-leadership-and-governance-of-university-hospitals-birmingham-nhs-foundation-trust/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Birmingham NHS FT provider profile (RRK)", "url": "https://www.cqc.org.uk/provider/RRK"}
        ],
        "related": ["University Hospitals Birmingham NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "NHS England", "Establishment costs — South Warwickshire NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Hull University Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Hull University Teaching Hospitals NHS Trust"}],
        "description": "Hull UTH's £18.31M general supplies & services line covers non-clinical consumables, ward provisions, household goods, laundry materials and small operational equipment across the trust's two main sites — Hull Royal Infirmary (c. 700 beds, major trauma + tertiary) and Castle Hill (Cottingham, oncology + cardiothoracic + planned-care). The trust's tertiary remit for cardiothoracic, vascular, neurosurgery and oncology layered onto a high-volume DGH baseline drives a complex consumables mix, with Procurement Act 2023 transition reshaping framework architecture from February 2025.",
        "beneficiaries": "c. 11,000 WTE workforce across HRI (city centre tower) and Castle Hill (Cottingham); serves a registered catchment c. 600,000 across Hull, the East Riding of Yorkshire and Northern Lincolnshire (via tertiary outflow) plus regional flows for cardiothoracic, vascular and major trauma; c. 145,000 ED attendances per year.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 (transitional) · Procurement Act 2023 (in force 24 Feb 2025)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£18.31M"},
            {"label": "Site footprint generating consumption", "value": "Hull Royal Infirmary (city centre, major trauma) + Castle Hill Hospital (Cottingham, oncology + cardiothoracic + planned-care)"},
            {"label": "Bed-stock", "value": "c. 1,000 inpatient beds across two sites"},
            {"label": "Composition", "value": "Non-clinical consumables + ward provisions + household goods + laundry materials + small operational equipment + minor catering provisions"},
            {"label": "Tertiary + DGH + Castle Hill PFI", "value": "Cardiothoracic + vascular + neurosurgery + oncology tertiary layer overlays high-volume DGH + major-trauma baseline; Castle Hill Queen's Centre PFI (2008) ringfences soft-FM but supplies pass through trust"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (majority) + Crown Commercial Service category contracts + minor local spot-buy"},
            {"label": "Procurement Act 2023 transition", "value": "New regime live 24 Feb 2025 — central digital platform + transparency obligations replace PCR 2015"},
            {"label": "Funding trajectory", "value": "2020-21 c. £13M → 2022-23 c. £16M → 2024-25 £18.31M — supplies CPI + activity recovery + tertiary growth"},
            {"label": "Delivery body", "value": "Trust Procurement + Estates & Facilities teams + Castle Hill PFI SPV interface for soft-FM coordination"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Humber and North Yorkshire ICB + NHS Supply Chain governance"},
            {"label": "Evaluation evidence", "value": "NHS Supply Chain framework data; Trust ARA 2023-24 disclosure; CQC inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 fragmented spot-buy regime · Successor: NHS Supply Chain Future Operating Model + Procurement Act 2023"}
        ],
        "notes": "Hull UTH's general supplies line reflects a tertiary teaching trust where cardiothoracic, vascular, neurosurgery and oncology specialty layers overlay a high-volume DGH and major-trauma baseline. The Queen's Centre for Oncology + Haematology PFI build at Castle Hill (2008) ringfences soft-FM through the SPV, but supplies and consumables continue to pass through the trust procurement perimeter. Humber and North Yorkshire ICS provides the regional planning context, with tertiary inflow from Northern Lincolnshire. The Procurement Act 2023 came into force 24 February 2025, replacing PCR 2015. CPI on supplies remains the dominant cost driver; tertiary-activity growth has lifted consumption above 2019-20 baseline.",
        "sources": [
            {"publisher": "Hull University Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hey.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Hull University Teaching Hospitals NHS Trust provider profile (RWA)", "url": "https://www.cqc.org.uk/provider/RWA"}
        ],
        "related": ["Hull University Teaching Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Imperial College Healthcare NHS Trust", "Department of Health and Social Care"]
    },
}
