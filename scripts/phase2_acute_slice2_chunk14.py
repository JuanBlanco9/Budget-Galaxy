# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 14 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    'Transport (business + patient) — Cambridge University Hospitals NHS Foundation Trust': {
        'aliases': [
            {'name': 'Transport (business + patient)', 'parent': 'Cambridge University Hospitals NHS Foundation Trust'}
        ],
        'description': "CUH's £6.03M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across Addenbrooke's Hospital + Rosie Hospital on the Cambridge Biomedical Campus, plus tertiary-referral PTS into the trust from across East of England. The trust hosts the East of England Major Trauma Centre, regional neurosurgery, transplantation (kidney, liver, multivisceral), specialist paediatrics and the National Institute for Health Research BioResource — all driving substantial inter-hospital PTS demand from referring district general hospitals.",
        'beneficiaries': "c. 12,500 WTE staff serving a c. 580,000 Cambridge & Peterborough catchment plus tertiary specialty referrals across East of England (c. 6.5M tertiary catchment); c. 140,000 ED attendances/yr at Addenbrooke's ED; c. 100,000 admissions/yr; East of England Major Trauma Centre.",
        'legal_basis': 'DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17',
        'key_stats': [
            {'label': 'Transport (business + patient) 2024-25', 'value': '£6.03M'},
            {'label': 'Trust scale', 'value': "Two-site academic acute (Addenbrooke's + Rosie) on Cambridge Biomedical Campus; c. 12,500 WTE"},
            {'label': 'Major Trauma Centre', 'value': "East of England MTC at Addenbrooke's — drives inter-hospital trauma transfer PTS from referring DGHs across East of England"},
            {'label': 'Tertiary referrals', 'value': 'Transplantation (kidney, liver, multivisceral, small bowel), neurosurgery, specialist paediatrics — substantial cross-region PTS'},
            {'label': 'PTS provider mix', 'value': 'East of England Ambulance Service NHS Trust + accredited NEPTS contractors (e.g. EMED Group / ERS Medical) — re-tendered via Cambridgeshire & Peterborough ICS'},
            {'label': 'Staff mileage rate', 'value': 'NHS AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter'},
            {'label': 'Pool fleet (IFRS 16)', 'value': 'Right-of-use depreciation + interest on leased pool vehicles for AHPs + research-cohort transport'},
            {'label': 'Industrial action 2023-24 effect', 'value': '44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site transfers + locum mileage'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.5M → 2023-24 c. £5.5M → 2024-25 £6.03M — fuel CPI + activity recovery + tertiary-referral growth'},
            {'label': 'Delivery body', 'value': 'Trust E&F + Travel team + EEAST PTS + accredited NEPTS contractors'},
            {'label': 'Policy owner', 'value': 'DHSC + NHSE Provider Finance + NHSE NEPTS framework + Cambridgeshire & Peterborough ICB'},
            {'label': 'Evaluation evidence', 'value': 'NHSE NEPTS Eligibility Framework 2022 review; CQC inspection RGT; Trust ARA disclosure'}
        ],
        'notes': "CUH's transport line is structurally elevated by the trust's tertiary-referral pattern — Addenbrooke's hosts the East of England Major Trauma Centre, the regional transplantation hub (kidney, liver, small bowel, multivisceral) and specialist paediatric services, generating continuous inter-hospital PTS demand from referring DGHs across Norfolk, Suffolk, Cambridgeshire, Hertfordshire, Bedfordshire and Essex. The 2022 NHSE NEPTS Eligibility Framework reshaped commissioning; Cambridgeshire & Peterborough ICS led the most recent NEPTS re-tender. Industrial action 2023-24 added ad-hoc inter-site transfer demand. April 2025 NIC step-up feeds through PTS-contractor pass-through; CPI fuel pressure remains the dominant unit-cost driver.",
        'sources': [
            {'publisher': 'Cambridge University Hospitals NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.cuh.nhs.uk/about-us/who-we-are/our-publications/'},
            {'publisher': 'NHS England', 'title': 'Non-Emergency Patient Transport Services Eligibility Framework 2022', 'url': 'https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/'},
            {'publisher': 'East of England Ambulance Service NHS Trust', 'title': 'Annual Report 2023-24', 'url': 'https://www.eastamb.nhs.uk/about-us/our-publications.htm'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'Cambridge University Hospitals provider profile (RGT)', 'url': 'https://www.cqc.org.uk/provider/RGT'}
        ],
        'related': ['Cambridge University Hospitals NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'East of England Ambulance Service NHS Trust', 'Transport (business + patient) — Imperial College Healthcare NHS Trust', 'Department of Health and Social Care']
    },
    'Establishment costs — Royal Surrey NHS Foundation Trust': {
        'aliases': [
            {'name': 'Establishment costs', 'parent': 'Royal Surrey NHS Foundation Trust'}
        ],
        'description': "Royal Surrey's £6.00M establishment costs line covers postage, telephony, IT subscriptions, training, professional fees, advertising, courier services, conference fees, agency-recruitment fees and other below-the-line operational running costs across the single-site Guildford acute footprint. The trust hosts the Royal Surrey County Hospital plus integrated specialist services (St Luke's Cancer Centre regional radiotherapy + the Surrey Research Park clinical-trials interface) — driving above-peer training, IT-subscription and professional-fees baseline.",
        'beneficiaries': "c. 4,500 WTE staff serving a c. 350,000 west Surrey catchment plus c. 1.0M tertiary cancer-radiotherapy catchment via St Luke's; c. 90,000 ED attendances/yr; c. 50,000 admissions/yr; St Luke's Cancer Centre serves regional Surrey & Sussex radiotherapy demand.",
        'legal_basis': 'DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25',
        'key_stats': [
            {'label': 'Establishment costs 2024-25', 'value': '£6.00M'},
            {'label': 'Trust scale', 'value': "Single-site DGH (Royal Surrey County Hospital, Guildford) + St Luke's Cancer Centre; c. 4,500 WTE"},
            {'label': 'Composition', 'value': 'Postage + telephony + IT subscriptions + training + professional fees + advertising + agency-recruitment fees + conference fees + courier'},
            {'label': "St Luke's Cancer Centre", 'value': 'Regional radiotherapy hub for Surrey & Sussex — drives radiotherapy IT-subscription + training baseline'},
            {'label': 'FD EPR context', 'value': "Cerner Millennium EPR shared with Ashford & St Peter's via Surrey Safe Care programme — drives training + change-management establishment cost"},
            {'label': 'Industrial action 2023-24 effect', 'value': '44 days junior-doctor + 10 days consultant strikes drove agency-recruitment + locum-fee establishment lift'},
            {'label': 'April 2025 NIC + CPI', 'value': 'Apr 2025 NIC pass-through on agency + professional services + sustained CPI on subscriptions feed forward unit-cost pressure'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.5M → 2023-24 £5.5M → 2024-25 £6.00M — sustained CPI + EPR training + agency-recruitment uplift'},
            {'label': 'Delivery body', 'value': 'Trust Finance + Procurement + HR Workforce-Resourcing teams'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + Surrey Heartlands ICB'},
            {'label': 'Evaluation evidence', 'value': 'Model Hospital establishment-cost benchmarks; CQC inspection RA2; Trust ARA disclosure'},
            {'label': 'Predecessor / successor', 'value': 'Predecessor: pre-Surrey Safe Care separate IT-subscription baseline · Successor: NHSE FD EPR convergence + Surrey Heartlands ICS shared back-office'}
        ],
        'notes': "Royal Surrey's establishment-costs line is shaped by the trust's hosting of St Luke's Cancer Centre (regional radiotherapy hub for Surrey & Sussex) and the Surrey Safe Care Cerner Millennium EPR programme shared with Ashford & St Peter's — both lift training, IT-subscription and professional-fees baselines above pure single-site DGH peers. Industrial action 2023-24 drove agency-recruitment fee uplift through repeated locum mobilisation across acute medicine and surgical rotas. The April 2025 NIC step-up flows through agency-staffing and professional-services pass-through; CPI on subscriptions and training continues to feed forward. Surrey Heartlands ICS shared back-office and NHSE Frontline Digitisation EPR convergence shape the medium-term path.",
        'sources': [
            {'publisher': 'Royal Surrey NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.royalsurrey.nhs.uk/about-us/our-publications/'},
            {'publisher': 'NHS England', 'title': 'Frontline Digitisation programme', 'url': 'https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'Royal Surrey provider profile (RA2)', 'url': 'https://www.cqc.org.uk/provider/RA2'},
            {'publisher': 'NHS England', 'title': 'New Hospital Programme — reset and revised schedule (2025)', 'url': 'https://www.gov.uk/government/publications/new-hospital-programme-update'}
        ],
        'related': ['Royal Surrey NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Establishment costs — Cambridge University Hospitals NHS Foundation Trust', "Ashford and St Peter's Hospitals NHS Foundation Trust", 'NHS England']
    },
    'Business rates — Oxford University Hospitals NHS Foundation Trust': {
        'aliases': [
            {'name': 'Business rates', 'parent': 'Oxford University Hospitals NHS Foundation Trust'}
        ],
        'description': "OUH's £5.96M business rates line covers non-domestic rates payable across the four-site footprint — the John Radcliffe Hospital, Churchill Hospital, Nuffield Orthopaedic Centre and Horton General Hospital — under the 2023 rating list operated by the Valuation Office Agency. The trust hosts regional and national specialist services (Major Trauma Centre, transplantation, cancer, cardiac, paediatrics) on a substantial estate footprint. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 and the 2026 revaluation set the medium-term rate-multiplier path.",
        'beneficiaries': 'c. 13,000 WTE staff serving a c. 700,000 Oxfordshire catchment plus tertiary specialty referrals across Thames Valley & Wessex (c. 3.0M tertiary catchment); c. 175,000 ED attendances/yr (John Radcliffe + Horton EDs); c. 100,000 admissions/yr; Thames Valley Major Trauma Centre at the John Radcliffe.',
        'legal_basis': 'Local Government Finance Act 1988 (Schedule 6 — Non-Domestic Rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006',
        'key_stats': [
            {'label': 'Business rates 2024-25', 'value': '£5.96M'},
            {'label': 'Trust scale', 'value': 'Four-site academic acute (John Radcliffe + Churchill + NOC + Horton General); c. 13,000 WTE'},
            {'label': 'Major Trauma Centre', 'value': 'Thames Valley MTC at John Radcliffe — drives high-value emergency-care estate footprint subject to NDR'},
            {'label': 'Tertiary specialist estate', 'value': 'Churchill cancer + Nuffield Orthopaedic + JR transplantation + cardiac — substantial high-RV specialist footprint'},
            {'label': 'VOA 2023 rating list', 'value': 'Antecedent valuation date 1 April 2021; rating list took effect 1 April 2023; next revaluation 2026'},
            {'label': 'Multiplier 2024-25', 'value': 'Standard multiplier 54.6p; small business multiplier 49.9p (England)'},
            {'label': 'NDR Act 2024 effect', 'value': 'Multipliers reform — divergent multipliers for high-value (RV ≥ £500k) vs standard properties from 2025-26 onwards'},
            {'label': 'Rating list challenge route', 'value': 'Check-Challenge-Appeal via VOA — trust E&F monitors valuations across all four sites'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £5.0M → 2023-24 £5.6M → 2024-25 £5.96M — RV uplift from 2023 list + multiplier'},
            {'label': 'Delivery body', 'value': 'Valuation Office Agency (HMRC ALB) + billing authorities (Oxford City + Cherwell + South Oxfordshire) + trust E&F'},
            {'label': 'Policy owner', 'value': 'MHCLG (NDR policy) + HMT (multiplier) + DHSC + Buckinghamshire, Oxfordshire & Berkshire West ICB'},
            {'label': 'Evaluation evidence', 'value': 'VOA rating list disclosures; HMT 2023 NDR consultation; Trust ARA'}
        ],
        'notes': "OUH's business rates line is shaped by the trust's substantial four-site academic-acute footprint — the John Radcliffe (Major Trauma Centre, transplantation, neurosciences), the Churchill (cancer + radiotherapy), the Nuffield Orthopaedic and the Horton General — generating high aggregate rateable value across the 2023 VOA rating list. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces divergent multipliers for high-value (RV ≥ £500k) and standard properties from 2025-26, with material implications for the trust's largest sites. The 2026 revaluation (AVD 1 April 2024) will reset the rating list across the estate. NHS providers do not receive empty/charitable relief on operational acute estate, so the line tracks RV × multiplier directly.",
        'sources': [
            {'publisher': 'Oxford University Hospitals NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.ouh.nhs.uk/about/publications/'},
            {'publisher': 'Valuation Office Agency', 'title': '2023 rating list and revaluation guidance', 'url': 'https://www.gov.uk/government/organisations/valuation-office-agency'},
            {'publisher': 'HM Treasury', 'title': 'Non-Domestic Rating (Multipliers and Private Finance) Act 2024', 'url': 'https://www.legislation.gov.uk/ukpga/2024/30/contents'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'OUH provider profile (RTH)', 'url': 'https://www.cqc.org.uk/provider/RTH'}
        ],
        'related': ['Oxford University Hospitals NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Valuation Office Agency', 'NHS Property Services', 'Business rates — Sheffield Teaching Hospitals NHS Foundation Trust']
    },
    'Amortisation — Royal Free London NHS Foundation Trust': {
        'aliases': [
            {'name': 'Amortisation', 'parent': 'Royal Free London NHS Foundation Trust'}
        ],
        'description': "Royal Free London's £5.96M amortisation line covers the systematic write-down of intangible assets — predominantly the trust's EPR software (Cerner Millennium / shared instance with Barnet & Chase Farm), licensed clinical applications, capitalised software development costs and other intangibles — over their assessed useful economic lives under IAS 38 and DHSC GAM ch.5. The trust runs a three-site major-acute estate (Royal Free, Barnet, Chase Farm) plus the Hadley Wood satellite, and is in active group-model formation with North Middlesex University Hospital under NCL ICS.",
        'beneficiaries': 'c. 11,000 WTE staff serving a c. 1.6M North Central London catchment; c. 280,000 ED attendances/yr (Royal Free + Barnet EDs); c. 165,000 admissions/yr; tertiary services include hepatology + transplantation + amyloidosis (national centre) at Royal Free site.',
        'legal_basis': 'IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 (intangibles) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022',
        'key_stats': [
            {'label': 'Amortisation 2024-25', 'value': '£5.96M'},
            {'label': 'Trust scale', 'value': 'Three-site acute (Royal Free + Barnet + Chase Farm) + Hadley Wood; c. 11,000 WTE'},
            {'label': 'Composition', 'value': 'EPR software amortisation + licensed clinical applications + capitalised software development + other intangibles'},
            {'label': 'EPR context', 'value': 'Cerner Millennium shared instance across RFL group sites — capitalised software amortising under IAS 38 over 5-10 year UEL'},
            {'label': 'FD EPR programme', 'value': 'NHSE Frontline Digitisation EPR programme funding underpins capitalisation; subsequent amortisation cycles feed forward'},
            {'label': 'National amyloidosis centre', 'value': 'Specialist clinical-application amortisation interface for national amyloidosis service'},
            {'label': 'IAS 38 useful life assumption', 'value': 'Software typically 5-10 years UEL (trust accounting policy); reviewed annually'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.5M → 2023-24 £5.5M → 2024-25 £5.96M — sustained capitalised-software amortisation cycle'},
            {'label': 'NCL group model', 'value': 'Active group-model transaction with North Middlesex University Hospital — shared EPR + back-office consolidation in scope'},
            {'label': 'Delivery body', 'value': 'Trust Finance + Digital teams + NCL ICS Digital Transformation'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + NHSE FD EPR + North Central London ICB'},
            {'label': 'Evaluation evidence', 'value': 'NHSE FD EPR programme evaluation; CQC inspection RAL; Trust ARA intangibles disclosure'}
        ],
        'notes': "Royal Free London's amortisation line is shaped by the trust's group-model architecture — the 2014 acquisition of Barnet & Chase Farm Hospitals consolidated intangible registers, and the active North Middlesex University Hospital transaction will further consolidate the NCL group footprint. The shared Cerner Millennium EPR instance dominates the line, with capitalised software development under IAS 38 amortising over 5-10 year UEL per trust accounting policy. NHSE Frontline Digitisation EPR programme funding underpins ongoing capitalisation — subsequent amortisation feeds the line forward as further FD investment lands. National amyloidosis centre and hepatology/transplantation specialist application interfaces add complexity.",
        'sources': [
            {'publisher': 'Royal Free London NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.royalfree.nhs.uk/about-us/corporate-information/annual-report-and-accounts/'},
            {'publisher': 'NHS England', 'title': 'Frontline Digitisation programme', 'url': 'https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25 (chapter 5 — intangibles)', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'Royal Free London provider profile (RAL)', 'url': 'https://www.cqc.org.uk/provider/RAL'},
            {'publisher': 'NHS England', 'title': 'North Central London ICS group-model transaction (Royal Free + North Mid)', 'url': 'https://www.england.nhs.uk/london/our-work/north-central-london/'}
        ],
        'related': ['Royal Free London NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'North Middlesex University Hospital NHS Trust', 'Amortisation — Kingston Hospital NHS Foundation Trust', 'NHS England']
    },
    'Establishment costs — County Durham and Darlington NHS Foundation Trust': {
        'aliases': [
            {'name': 'Establishment costs', 'parent': 'County Durham and Darlington NHS Foundation Trust'}
        ],
        'description': "CDDFT's £5.95M establishment costs line covers postage, telephony, IT subscriptions, training, professional fees, advertising, agency-recruitment fees, conference fees and courier services across the multi-site trust footprint — University Hospital of North Durham (UHND), Darlington Memorial Hospital, Bishop Auckland Hospital plus several community-hospital sites across County Durham and the Tees Valley. The Carillion 2018 collapse novated FM contracts on UHND PFI, with consequential establishment-cost churn carried forward.",
        'beneficiaries': 'c. 7,500 WTE staff serving a c. 650,000 County Durham + Darlington catchment; c. 200,000 ED attendances/yr (UHND + Darlington EDs); c. 95,000 admissions/yr; integrated community hospital sites across Bishop Auckland, Chester-le-Street, Sedgefield, Shotley Bridge, Weardale.',
        'legal_basis': 'DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25',
        'key_stats': [
            {'label': 'Establishment costs 2024-25', 'value': '£5.95M'},
            {'label': 'Trust scale', 'value': 'Multi-site (UHND + Darlington Memorial + Bishop Auckland + community hospitals); c. 7,500 WTE'},
            {'label': 'Composition', 'value': 'Postage + telephony + IT subscriptions + training + professional fees + advertising + agency-recruitment fees + courier'},
            {'label': 'Carillion 2018 effect', 'value': 'UHND PFI FM contracts novated post-Carillion January 2018 collapse — consequential legal/professional fees carried forward'},
            {'label': 'FD EPR context', 'value': 'Oracle Health (Cerner Millennium) EPR rollout — drives training + change-management establishment cost'},
            {'label': 'Multi-site community footprint', 'value': 'Community hospitals + integrated community services drive courier + telephony establishment baseline above acute-only peers'},
            {'label': 'Industrial action 2023-24 effect', 'value': '44 days junior-doctor + 10 days consultant strikes drove agency-recruitment fee uplift'},
            {'label': 'April 2025 NIC + CPI', 'value': 'Apr 2025 NIC pass-through on agency + sustained CPI on subscriptions feed forward unit-cost pressure'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.5M → 2023-24 £5.5M → 2024-25 £5.95M — CPI + EPR + agency-recruitment uplift'},
            {'label': 'Delivery body', 'value': 'Trust Finance + Procurement + HR Workforce-Resourcing teams'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + County Durham & Tees Valley ICB (NENC ICS)'},
            {'label': 'Evaluation evidence', 'value': 'Model Hospital establishment-cost benchmarks; NAO Carillion report; CQC inspection RXP; Trust ARA disclosure'}
        ],
        'notes': "CDDFT's establishment-costs line reflects the multi-site footprint across County Durham and Darlington — UHND, Darlington Memorial, Bishop Auckland and a network of community hospitals — driving baseline courier, telephony and training cost above pure single-site acute peers. The 2018 Carillion collapse novated UHND PFI FM contracts (UHND was a 2001-signed PFI), with consequential legal/professional fees carried forward through subsequent contract management. Industrial action 2023-24 lifted agency-recruitment fees as the trust mobilised repeated locum cohorts. The April 2025 employer-NIC step-up flows through agency-staffing pass-through; CPI on IT subscriptions and training continues to feed forward.",
        'sources': [
            {'publisher': 'County Durham and Darlington NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.cddft.nhs.uk/about-us/publications/annual-report-and-accounts.aspx'},
            {'publisher': 'National Audit Office', 'title': "Investigation into the rescue of Carillion's PFI hospital contracts", 'url': 'https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/'},
            {'publisher': 'NHS England', 'title': 'Frontline Digitisation programme', 'url': 'https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'CDDFT provider profile (RXP)', 'url': 'https://www.cqc.org.uk/provider/RXP'}
        ],
        'related': ['County Durham and Darlington NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Establishment costs — Royal Surrey NHS Foundation Trust', 'PFI / LIFT charges — County Durham and Darlington NHS Foundation Trust', 'NHS England']
    },
    'Business rates — King’s College Hospital NHS Foundation Trust': {
        'aliases': [
            {'name': 'Business rates', 'parent': 'King’s College Hospital NHS Foundation Trust'}
        ],
        'description': "KCH's £5.94M business rates line covers non-domestic rates payable across the trust's two-site major-acute footprint — the Denmark Hill site in south-east London (King's College Hospital flagship) and the Princess Royal University Hospital in Orpington — under the 2023 VOA rating list. The trust hosts the South East London Major Trauma Centre, regional liver transplantation, neuroscience, fetal medicine and haematology services on a high-RV estate. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 sets the 2025-26 multiplier path.",
        'beneficiaries': 'c. 13,500 WTE staff serving a c. 700,000 south-east London + Bromley catchment plus tertiary specialty referrals across South East England; c. 235,000 ED attendances/yr (Denmark Hill + PRUH EDs); c. 130,000 admissions/yr; SEL Major Trauma Centre at Denmark Hill.',
        'legal_basis': 'Local Government Finance Act 1988 (Schedule 6 — Non-Domestic Rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006',
        'key_stats': [
            {'label': 'Business rates 2024-25', 'value': '£5.94M'},
            {'label': 'Trust scale', 'value': 'Two-site major-acute (Denmark Hill + Princess Royal University Hospital, Orpington); c. 13,500 WTE'},
            {'label': 'Major Trauma Centre', 'value': 'South East London MTC at Denmark Hill — drives high-RV emergency-care estate'},
            {'label': 'Tertiary specialist estate', 'value': 'Liver transplantation + neuroscience + fetal medicine + haematology — substantial specialist-services footprint'},
            {'label': 'VOA 2023 rating list', 'value': 'AVD 1 April 2021; rating list took effect 1 April 2023; next revaluation 2026'},
            {'label': 'Multiplier 2024-25', 'value': 'Standard multiplier 54.6p; small business multiplier 49.9p (England)'},
            {'label': 'NDR Act 2024 effect', 'value': 'Divergent multipliers for high-value (RV ≥ £500k) vs standard properties from 2025-26 — material for Denmark Hill flagship'},
            {'label': 'Billing authorities', 'value': 'London Borough of Lambeth (Denmark Hill) + London Borough of Bromley (PRUH)'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £5.0M → 2023-24 £5.6M → 2024-25 £5.94M — RV uplift from 2023 list + multiplier'},
            {'label': 'Delivery body', 'value': 'Valuation Office Agency (HMRC ALB) + Lambeth + Bromley billing authorities + trust E&F'},
            {'label': 'Policy owner', 'value': 'MHCLG (NDR policy) + HMT (multiplier) + DHSC + South East London ICB'},
            {'label': 'Evaluation evidence', 'value': 'VOA rating list disclosures; HMT 2023 NDR consultation; CQC inspection RJZ; Trust ARA'}
        ],
        'notes': "KCH's business-rates line is shaped by the trust's two-site major-acute footprint across two London billing authorities (Lambeth at Denmark Hill, Bromley at PRUH). Denmark Hill carries the Major Trauma Centre, liver transplantation, neuroscience and high-acuity emergency-care estate; PRUH provides DGH services for Bromley and parts of Kent. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces divergent multipliers for high-value (RV ≥ £500k) and standard properties from 2025-26 — material for the Denmark Hill flagship's high RV. The 2026 revaluation (AVD 1 April 2024) will reset the rating list. NHS providers do not receive empty/charitable relief on operational acute estate, so the line tracks RV × multiplier directly.",
        'sources': [
            {'publisher': "King's College Hospital NHS Foundation Trust", 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.kch.nhs.uk/about/corporate/annual-reports/'},
            {'publisher': 'Valuation Office Agency', 'title': '2023 rating list and revaluation guidance', 'url': 'https://www.gov.uk/government/organisations/valuation-office-agency'},
            {'publisher': 'HM Treasury', 'title': 'Non-Domestic Rating (Multipliers and Private Finance) Act 2024', 'url': 'https://www.legislation.gov.uk/ukpga/2024/30/contents'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': "King's College Hospital provider profile (RJZ)", 'url': 'https://www.cqc.org.uk/provider/RJZ'}
        ],
        'related': ['King’s College Hospital NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Valuation Office Agency', 'Business rates — Oxford University Hospitals NHS Foundation Trust', 'Establishment costs — King’s College Hospital NHS Foundation Trust']
    },
    'Business rates — University Hospitals of Derby and Burton NHS Foundation Trust': {
        'aliases': [
            {'name': 'Business rates', 'parent': 'University Hospitals of Derby and Burton NHS Foundation Trust'}
        ],
        'description': "UHDB's £5.82M business rates line covers non-domestic rates payable across the multi-site footprint following the 2018 acquisition of Burton Hospitals — the Royal Derby Hospital (Royal Derby + London Road Community Hospital sites), Queen's Hospital Burton, Samuel Johnson Community Hospital (Lichfield), Sir Robert Peel Community Hospital (Tamworth) — under the 2023 VOA rating list. Cross-county footprint spans Derbyshire and Staffordshire billing authorities, with the NDR Act 2024 setting forward multiplier path.",
        'beneficiaries': "c. 13,000 WTE staff serving a c. 1.0M Derby + Burton + south-east Staffordshire catchment; c. 250,000 ED attendances/yr (Royal Derby + Queen's Burton EDs); c. 145,000 admissions/yr; multi-county DGH footprint with community-hospital satellites at Lichfield + Tamworth.",
        'legal_basis': 'Local Government Finance Act 1988 (Schedule 6 — Non-Domestic Rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006',
        'key_stats': [
            {'label': 'Business rates 2024-25', 'value': '£5.82M'},
            {'label': 'Trust scale', 'value': "Multi-site (Royal Derby + Queen's Burton + Lichfield + Tamworth + London Road Community); c. 13,000 WTE"},
            {'label': 'Cross-county estate', 'value': 'Derbyshire (Derby City + Lichfield) + Staffordshire (East Staffs + Lichfield + Tamworth) billing authorities'},
            {'label': 'VOA 2023 rating list', 'value': 'AVD 1 April 2021; rating list took effect 1 April 2023; next revaluation 2026'},
            {'label': 'Multiplier 2024-25', 'value': 'Standard multiplier 54.6p; small business multiplier 49.9p (England)'},
            {'label': 'NDR Act 2024 effect', 'value': 'Divergent multipliers for high-value (RV ≥ £500k) vs standard properties from 2025-26'},
            {'label': '2018 acquisition', 'value': 'UHDB created by 1 July 2018 acquisition of Burton Hospitals NHS FT by Derby Teaching Hospitals NHS FT — consolidated rating registers'},
            {'label': 'Royal Derby PFI context', 'value': 'Royal Derby Hospital is PFI-built (signed 2003, opened 2009) — RV reflects new-build estate; NDR sits separately from PFI unitary charge'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.9M → 2023-24 £5.5M → 2024-25 £5.82M — RV uplift from 2023 list + multiplier'},
            {'label': 'Delivery body', 'value': 'Valuation Office Agency (HMRC ALB) + multiple billing authorities + trust E&F'},
            {'label': 'Policy owner', 'value': 'MHCLG (NDR policy) + HMT (multiplier) + DHSC + Derby & Derbyshire ICB + Staffordshire & Stoke-on-Trent ICB'},
            {'label': 'Evaluation evidence', 'value': 'VOA rating list disclosures; HMT 2023 NDR consultation; CQC inspection RTG; Trust ARA'}
        ],
        'notes': "UHDB's business-rates line is shaped by the trust's cross-county footprint following the 2018 acquisition of Burton Hospitals NHS FT by Derby Teaching Hospitals NHS FT — operating across Derby City, East Staffordshire, Lichfield and Tamworth billing authorities, each issuing separate NDR demands. The Royal Derby Hospital is PFI-built (signed 2003, opened 2009 by Skanska/Innisfree consortium) — its NDR sits separately from the PFI unitary charge but reflects new-build estate RV. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces divergent multipliers for high-value (RV ≥ £500k) and standard properties from 2025-26, with implications for the Royal Derby flagship. The 2026 revaluation (AVD 1 April 2024) will reset the rating list.",
        'sources': [
            {'publisher': 'University Hospitals of Derby and Burton NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.uhdb.nhs.uk/annual-report-and-accounts'},
            {'publisher': 'Valuation Office Agency', 'title': '2023 rating list and revaluation guidance', 'url': 'https://www.gov.uk/government/organisations/valuation-office-agency'},
            {'publisher': 'HM Treasury', 'title': 'Non-Domestic Rating (Multipliers and Private Finance) Act 2024', 'url': 'https://www.legislation.gov.uk/ukpga/2024/30/contents'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'UHDB provider profile (RTG)', 'url': 'https://www.cqc.org.uk/provider/RTG'}
        ],
        'related': ['University Hospitals of Derby and Burton NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Valuation Office Agency', 'Business rates — Oxford University Hospitals NHS Foundation Trust', 'Business rates — King’s College Hospital NHS Foundation Trust']
    },
    'Establishment costs — Norfolk and Norwich University Hospitals NHS Foundation Trust': {
        'aliases': [
            {'name': 'Establishment costs', 'parent': 'Norfolk and Norwich University Hospitals NHS Foundation Trust'}
        ],
        'description': "NNUH's £5.77M establishment costs line covers postage, telephony, IT subscriptions, training, professional fees, advertising, agency-recruitment fees, conference fees and courier services across the single-site Norwich Research Park (NRP) acute footprint. The trust runs the Norfolk and Norwich University Hospital — opened 2001 as a PFI build, one of the NHS's first-wave PFI deals — plus the Cromer Hospital satellite. Norwich Research Park interface drives elevated training, IT-subscription and professional-fees baseline relative to standalone DGH peers.",
        'beneficiaries': 'c. 11,000 WTE staff serving a c. 1.0M Norfolk catchment plus tertiary referrals from north Suffolk & north Cambridgeshire; c. 165,000 ED attendances/yr at NNUH ED; c. 110,000 admissions/yr; major regional teaching hospital with University of East Anglia clinical school interface.',
        'legal_basis': 'DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25',
        'key_stats': [
            {'label': 'Establishment costs 2024-25', 'value': '£5.77M'},
            {'label': 'Trust scale', 'value': 'Single major-acute (NNUH) + Cromer Hospital satellite; c. 11,000 WTE'},
            {'label': 'Composition', 'value': 'Postage + telephony + IT subscriptions + training + professional fees + advertising + agency-recruitment fees + courier'},
            {'label': 'Norwich Research Park interface', 'value': 'UEA clinical school + Quadram Institute + research-cohort training/professional-fees baseline above standalone DGH peers'},
            {'label': 'PFI estate context', 'value': 'NNUH is PFI-built (signed 1998, opened 2001 — Octagon Healthcare consortium) — establishment costs reflect modern-build IT-infrastructure baseline'},
            {'label': 'FD EPR context', 'value': 'EPR rollout under NHSE FD programme — drives training + change-management establishment cost'},
            {'label': 'Industrial action 2023-24 effect', 'value': '44 days junior-doctor + 10 days consultant strikes drove agency-recruitment fee uplift'},
            {'label': 'April 2025 NIC + CPI', 'value': 'Apr 2025 NIC pass-through on agency + sustained CPI on subscriptions feed forward unit-cost pressure'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.5M → 2023-24 £5.3M → 2024-25 £5.77M — CPI + EPR + agency-recruitment uplift'},
            {'label': 'Delivery body', 'value': 'Trust Finance + Procurement + HR Workforce-Resourcing teams'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + Norfolk & Waveney ICB'},
            {'label': 'Evaluation evidence', 'value': 'Model Hospital establishment-cost benchmarks; CQC inspection RM1; Trust ARA disclosure'}
        ],
        'notes': "NNUH's establishment-costs line is shaped by the trust's single-site major-acute footprint and Norwich Research Park interface — UEA clinical school, Quadram Institute and life-science research generate elevated training, IT-subscription and professional-fees baseline relative to comparable single-site DGH peers. The PFI build (Octagon Healthcare consortium, opened 2001) was one of the NHS's first-wave PFI deals; establishment costs reflect modern IT-infrastructure baseline (separate from the PFI/LIFT charges line which captures unitary charge). Industrial action 2023-24 lifted agency-recruitment fees through repeated locum mobilisation.",
        'sources': [
            {'publisher': 'Norfolk and Norwich University Hospitals NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.nnuh.nhs.uk/about-us/our-publications/annual-reports/'},
            {'publisher': 'NHS England', 'title': 'Frontline Digitisation programme', 'url': 'https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/'},
            {'publisher': 'National Audit Office', 'title': 'PFI and PF2 (HC 718, 2018)', 'url': 'https://www.nao.org.uk/reports/pfi-and-pf2/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'NNUH provider profile (RM1)', 'url': 'https://www.cqc.org.uk/provider/RM1'}
        ],
        'related': ['Norfolk and Norwich University Hospitals NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Establishment costs — Royal Surrey NHS Foundation Trust', 'Establishment costs — County Durham and Darlington NHS Foundation Trust', 'NHS England']
    },
    'PFI / LIFT charges — Walsall Healthcare NHS Trust': {
        'aliases': [
            {'name': 'PFI / LIFT charges', 'parent': 'Walsall Healthcare NHS Trust'}
        ],
        'description': "Walsall Healthcare's £5.74M PFI/LIFT charge reflects unitary-charge pass-through on the Manor Hospital PFI redevelopment (signed 2007, operational from 2010) plus residual LIFT-scheme primary-care premises across Walsall, with SPV Skanska Innisfree and post-Carillion FM novation churn from the 2018 collapse. The trust runs the single-site Manor Hospital (Walsall) plus integrated community services across Walsall — the IFRS 16 2022 transition reshaped the headline figure but not the underlying obligation.",
        'beneficiaries': 'c. 4,500 WTE staff serving a c. 285,000 Walsall catchment; c. 130,000 ED attendances/yr at Manor Hospital ED; c. 60,000 admissions/yr; integrated community services across Walsall PCT-legacy footprint (district nursing, community-paediatric, community-adult).',
        'legal_basis': 'IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition for service-concession components) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022',
        'key_stats': [
            {'label': 'PFI / LIFT charges 2024-25', 'value': '£5.74M'},
            {'label': 'PFI vehicle', 'value': 'Manor Hospital PFI signed 2007, operational from 2010; SPV Skanska Innisfree consortium'},
            {'label': 'Contract end date', 'value': 'c. 2040 (30-year operational concession from 2010)'},
            {'label': 'Carillion 2018 effect', 'value': 'Carillion (subcontracted FM elements) Jan 2018 collapse → FM contract novation churn carried forward'},
            {'label': 'Estate covered', 'value': 'Manor Hospital (single-site DGH, c. 550 beds) + residual LIFT primary-care premises across Walsall'},
            {'label': 'Unitary charge composition', 'value': 'Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM'},
            {'label': 'Indexation mechanism', 'value': 'RPI-linked annual uplift on indexed soft-FM components'},
            {'label': 'Funding trajectory', 'value': 'Mature PFI; £5.74M figure represents accounted PFI/LIFT-line element after IFRS 16 split'},
            {'label': 'Integrated community context', 'value': 'Trust integrated Walsall community services from Walsall PCT in 2011 — LIFT primary-care premises tail integrated into trust footprint'},
            {'label': 'Delivery body', 'value': 'Skanska Innisfree SPV + post-Carillion FM contractors + Community Health Partnerships (LIFT) + trust E&F'},
            {'label': 'Policy owner', 'value': 'DHSC + HM Treasury PFI guidance + NHSE Provider Finance + Black Country ICB'},
            {'label': 'Evaluation evidence', 'value': 'NAO PFI 2018 + Carillion 2018 reports; CQC inspection RBK; Trust ARA disclosure'}
        ],
        'notes': "Walsall Healthcare's Manor Hospital PFI was signed in 2007 under the second wave of NHS PFI deals, with operational commencement in 2010 — the SPV is Skanska Innisfree, with Carillion subcontracted on FM elements pre-2018. The January 2018 Carillion collapse triggered FM contract novation churn carried forward through subsequent contract management. The trust's 2011 integration of Walsall PCT community services brought residual LIFT primary-care premises into the trust footprint, contributing the small LIFT element of this combined line. RPI-linked indexation on soft-FM continues to lift cost even as senior debt amortises down. The IFRS 16 2022 transition and DHSC GAM ch.7 split reshaped the headline figure; hand-back planning ahead of c.",
        'sources': [
            {'publisher': 'Walsall Healthcare NHS Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.walsallhealthcare.nhs.uk/about-us/publications/annual-report-accounts/'},
            {'publisher': 'National Audit Office', 'title': 'PFI and PF2 (HC 718, 2018)', 'url': 'https://www.nao.org.uk/reports/pfi-and-pf2/'},
            {'publisher': 'National Audit Office', 'title': "Investigation into the rescue of Carillion's PFI hospital contracts", 'url': 'https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'Walsall Healthcare provider profile (RBK)', 'url': 'https://www.cqc.org.uk/provider/RBK'}
        ],
        'related': ['Walsall Healthcare NHS Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust', 'PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust', 'Department of Health and Social Care']
    },
    'Establishment costs — Northumbria Healthcare NHS Foundation Trust': {
        'aliases': [
            {'name': 'Establishment costs', 'parent': 'Northumbria Healthcare NHS Foundation Trust'}
        ],
        'description': "Northumbria Healthcare's £5.73M establishment costs line covers postage, telephony, IT subscriptions, training, professional fees, advertising, agency-recruitment fees, conference fees and courier services across the multi-site footprint — the Northumbria Specialist Emergency Care Hospital (Cramlington, opened 2015 as the UK's first purpose-built specialist emergency hospital), Wansbeck General, North Tyneside General, Hexham General, plus integrated community-hospital network across Northumberland and North Tyneside. NHSPS-leased and trust-owned mix shapes baseline.",
        'beneficiaries': "c. 11,000 WTE staff serving a c. 500,000 Northumberland + North Tyneside catchment; c. 250,000 ED attendances/yr (Northumbria Specialist Emergency Care Hospital + walk-in centres); c. 110,000 admissions/yr; integrated acute + community across one of England's largest geographies by trust footprint.",
        'legal_basis': 'DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25',
        'key_stats': [
            {'label': 'Establishment costs 2024-25', 'value': '£5.73M'},
            {'label': 'Trust scale', 'value': 'Multi-site (NSECH Cramlington + Wansbeck + North Tyneside + Hexham + community hospitals); c. 11,000 WTE'},
            {'label': 'Composition', 'value': 'Postage + telephony + IT subscriptions + training + professional fees + advertising + agency-recruitment fees + courier'},
            {'label': 'NSECH Cramlington context', 'value': "UK's first purpose-built specialist emergency hospital (opened 2015) — dedicated emergency-care model drives training + IT-subscription baseline"},
            {'label': 'Geography premium', 'value': "Multi-site footprint across one of England's largest trust geographies — drives courier + telephony establishment baseline above urban single-site peers"},
            {'label': 'FD EPR context', 'value': 'EPR rollout under NHSE FD programme — drives training + change-management establishment cost'},
            {'label': 'Industrial action 2023-24 effect', 'value': '44 days junior-doctor + 10 days consultant strikes drove agency-recruitment fee uplift'},
            {'label': 'April 2025 NIC + CPI', 'value': 'Apr 2025 NIC pass-through on agency + sustained CPI on subscriptions feed forward unit-cost pressure'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.5M → 2023-24 £5.3M → 2024-25 £5.73M — CPI + EPR + agency-recruitment uplift'},
            {'label': 'Delivery body', 'value': 'Trust Finance + Procurement + HR Workforce-Resourcing teams + Northumbria Healthcare Facilities Management subsidiary (NHFM)'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + North East and North Cumbria ICB'},
            {'label': 'Evaluation evidence', 'value': 'Model Hospital establishment-cost benchmarks; CQC inspection RTF (Outstanding 2019); Trust ARA disclosure'}
        ],
        'notes': "Northumbria Healthcare's establishment-costs line is shaped by the multi-site geography across Northumberland and North Tyneside — one of England's largest trust footprints — driving baseline courier, telephony and training cost above urban single-site peers. The 2015 opening of the Northumbria Specialist Emergency Care Hospital at Cramlington (the UK's first purpose-built specialist emergency hospital) reshaped the dedicated emergency-care model and lifted training and IT-subscription baselines as staff were rotated through the new model. The trust's wholly-owned subsidiary Northumbria Healthcare Facilities Management (NHFM) handles in-house FM, separate from this line. Industrial action 2023-24 lifted agency-recruitment fees.",
        'sources': [
            {'publisher': 'Northumbria Healthcare NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.northumbria.nhs.uk/about-us/news-and-publications/publications/'},
            {'publisher': 'NHS England', 'title': 'Frontline Digitisation programme', 'url': 'https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'Northumbria Healthcare provider profile (RTF)', 'url': 'https://www.cqc.org.uk/provider/RTF'},
            {'publisher': "King's Fund", 'title': 'Northumbria specialist emergency care model — case study', 'url': 'https://www.kingsfund.org.uk/insight-and-analysis'}
        ],
        'related': ['Northumbria Healthcare NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Establishment costs — County Durham and Darlington NHS Foundation Trust', 'Establishment costs — Norfolk and Norwich University Hospitals NHS Foundation Trust', 'NHS England']
    },
    'Establishment costs — East And North Hertfordshire NHS Trust': {
        'aliases': [
            {'name': 'Establishment costs', 'parent': 'East And North Hertfordshire NHS Trust'}
        ],
        'description': "ENHT's £5.67M establishment costs line covers postage, telephony, IT subscriptions, training, professional fees, advertising, agency-recruitment fees, conference fees and courier services across the multi-site footprint — Lister Hospital (Stevenage, main acute), New QEII Hospital (Welwyn Garden City), Hertford County Hospital plus the Mount Vernon Cancer Centre satellite at Northwood. The trust hosts the Mount Vernon Cancer Centre regional cancer service, contributing tertiary-referral training and professional-fees baseline above pure DGH peers.",
        'beneficiaries': 'c. 6,500 WTE staff serving a c. 600,000 east and north Hertfordshire catchment plus tertiary cancer referrals from across north-west London + Beds & Herts via Mount Vernon (c. 2.0M tertiary cancer catchment); c. 130,000 ED attendances/yr at Lister ED; c. 75,000 admissions/yr.',
        'legal_basis': 'DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25',
        'key_stats': [
            {'label': 'Establishment costs 2024-25', 'value': '£5.67M'},
            {'label': 'Trust scale', 'value': 'Multi-site (Lister + New QEII + Hertford County + Mount Vernon Cancer Centre); c. 6,500 WTE'},
            {'label': 'Composition', 'value': 'Postage + telephony + IT subscriptions + training + professional fees + advertising + agency-recruitment fees + courier'},
            {'label': 'Mount Vernon Cancer Centre', 'value': 'Regional cancer hub for north-west London + Beds & Herts — drives radiotherapy + cancer-IT subscription + training baseline'},
            {'label': 'Mount Vernon transfer review', 'value': 'Active service-redesign reviews (Mount Vernon transferred from East & North Herts NHS Trust to potential alternative provider 2024-25) — drives transition + professional-fees baseline'},
            {'label': 'FD EPR context', 'value': 'EPR rollout under NHSE FD programme — drives training + change-management establishment cost'},
            {'label': 'Industrial action 2023-24 effect', 'value': '44 days junior-doctor + 10 days consultant strikes drove agency-recruitment fee uplift'},
            {'label': 'April 2025 NIC + CPI', 'value': 'Apr 2025 NIC pass-through on agency + sustained CPI on subscriptions feed forward unit-cost pressure'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.5M → 2023-24 £5.2M → 2024-25 £5.67M — CPI + EPR + Mount Vernon transition uplift'},
            {'label': 'Delivery body', 'value': 'Trust Finance + Procurement + HR Workforce-Resourcing teams'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + Hertfordshire & West Essex ICB'},
            {'label': 'Evaluation evidence', 'value': 'NHSE Mount Vernon Cancer Centre review; CQC inspection RWH; Trust ARA disclosure'}
        ],
        'notes': "ENHT's establishment-costs line is shaped by the multi-site footprint across east and north Hertfordshire and the Mount Vernon Cancer Centre satellite at Northwood — a regional cancer hub serving north-west London and Beds & Herts that drives radiotherapy and cancer-IT subscription baselines above pure DGH peers. Active NHSE-led service-redesign reviews considering the future of Mount Vernon's hosting (potential transfer from ENHT to alternative provider 2024-25 onwards) drive elevated professional-fees baseline through transition planning, legal/advisory and change-management activity. The Lister Hospital expansion programme and the New QEII Hospital opening (2015) reshaped the trust's site footprint over the past decade. Industrial action 2023-24 lifted agency-recruitment fees.",
        'sources': [
            {'publisher': 'East and North Hertfordshire NHS Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.enherts-tr.nhs.uk/about-us/publications/annual-report/'},
            {'publisher': 'NHS England', 'title': 'Mount Vernon Cancer Centre review', 'url': 'https://www.england.nhs.uk/london/our-work/mount-vernon-cancer-centre/'},
            {'publisher': 'NHS England', 'title': 'Frontline Digitisation programme', 'url': 'https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'ENHT provider profile (RWH)', 'url': 'https://www.cqc.org.uk/provider/RWH'}
        ],
        'related': ['East And North Hertfordshire NHS Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Establishment costs — Norfolk and Norwich University Hospitals NHS Foundation Trust', 'Establishment costs — Northumbria Healthcare NHS Foundation Trust', 'NHS England']
    },
    'General supplies & services — Mersey and West Lancashire Teaching Hospitals NHS Trust': {
        'aliases': [
            {'name': 'General supplies & services', 'parent': 'Mersey and West Lancashire Teaching Hospitals NHS Trust'}
        ],
        'description': "MWL's £5.65M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the trust's multi-site footprint following the July 2023 merger of St Helens & Knowsley Teaching Hospitals NHS Trust with Southport & Ormskirk Hospital NHS Trust. The trust runs Whiston Hospital (St Helens), St Helens Hospital, Southport District General Hospital, Ormskirk District General Hospital and the Newton Community Hospital — generating large multi-site non-clinical consumables baseline.",
        'beneficiaries': 'c. 9,000 WTE staff serving a c. 600,000 St Helens, Knowsley, Southport, Ormskirk, West Lancashire catchment; c. 230,000 ED attendances/yr (Whiston + Southport EDs); c. 100,000 admissions/yr; multi-site DGH footprint across Cheshire & Merseyside ICS and Lancashire & South Cumbria ICS boundary.',
        'legal_basis': 'DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25',
        'key_stats': [
            {'label': 'General supplies & services 2024-25', 'value': '£5.65M'},
            {'label': 'Trust scale', 'value': 'Multi-site (Whiston + St Helens + Southport + Ormskirk + Newton Community); c. 9,000 WTE'},
            {'label': '2023 merger context', 'value': 'Merger of St Helens & Knowsley Teaching Hospitals + Southport & Ormskirk Hospital effective 1 July 2023 — first full year of merged consumables baseline 2023-24'},
            {'label': 'Cross-ICS footprint', 'value': 'Sites span Cheshire & Merseyside ICS (Whiston/St Helens) + Lancashire & South Cumbria ICS (Southport/Ormskirk) — divergent procurement-collaborative interfaces'},
            {'label': 'Procurement route', 'value': 'NHS Supply Chain national framework + trust-direct contracts + dual ICS procurement collaboratives'},
            {'label': 'April 2025 NIC + CPI uplift', 'value': 'Apr 2025 employer-NIC step-up + sustained non-clinical CPI feed forward unit-cost pressure'},
            {'label': 'Industrial action 2023-24 effect', 'value': '44 days junior-doctor + 10 days consultant strikes drove agency backfill + cancellation-related re-stocking churn'},
            {'label': 'Whiston Hospital PFI context', 'value': 'Whiston Hospital is PFI-built (signed 2005, opened 2010) — modern-build hotel-services standards lift non-clinical consumables baseline'},
            {'label': 'Funding trajectory', 'value': '2022-23 pre-merger separate baselines → 2023-24 first merged year c. £5.2M → 2024-25 £5.65M'},
            {'label': 'Delivery body', 'value': 'Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + dual ICS procurement collaboratives'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + Cheshire & Merseyside ICB + Lancashire & South Cumbria ICB'},
            {'label': 'Evaluation evidence', 'value': 'Model Hospital benchmarks; NHSE merger business case; CQC inspection R0A; Trust ARA 2023-24'}
        ],
        'notes': "MWL's general supplies & services baseline reflects the July 2023 merger of St Helens & Knowsley Teaching Hospitals (CQC Outstanding) with the financially-challenged Southport & Ormskirk Hospital — 2023-24 was the first full year of merged operations and consumables baseline. The cross-ICS footprint (Cheshire & Merseyside hosting Whiston/St Helens; Lancashire & South Cumbria hosting Southport/Ormskirk) creates divergent procurement-collaborative interfaces and complicates ICS-level scaling. Whiston Hospital is PFI-built (2010 opening), with modern hotel-services standards lifting baseline non-clinical consumables vs older sites. Industrial action 2023-24 drove agency backfill and cancellation-related re-stocking churn.",
        'sources': [
            {'publisher': 'Mersey and West Lancashire Teaching Hospitals NHS Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.merseywestlancs.nhs.uk/about/publications/'},
            {'publisher': 'NHS England', 'title': 'Mersey and West Lancashire Teaching Hospitals NHS Trust merger business case (2023)', 'url': 'https://www.england.nhs.uk/north-west/'},
            {'publisher': 'NHS Supply Chain', 'title': 'Annual Report 2023-24', 'url': 'https://www.supplychain.nhs.uk/about-us/our-publications/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'MWL provider profile (R0A)', 'url': 'https://www.cqc.org.uk/provider/R0A'}
        ],
        'related': ['Mersey and West Lancashire Teaching Hospitals NHS Trust', 'Clinical Supplies & Drugs', 'NHS Acute Trusts', 'NHS Supply Chain', 'General supplies & services — Liverpool University Hospitals NHS Foundation Trust', 'Department of Health and Social Care']
    },
    'Establishment costs — University Hospitals of North Midlands NHS Trust': {
        'aliases': [
            {'name': 'Establishment costs', 'parent': 'University Hospitals of North Midlands NHS Trust'}
        ],
        'description': "UHNM's £5.59M establishment costs line covers postage, telephony, IT subscriptions, training, professional fees, advertising, agency-recruitment fees, conference fees and courier services across the two-site major-acute footprint — the Royal Stoke University Hospital (Stoke-on-Trent, regional Major Trauma Centre) and the County Hospital (Stafford). The trust hosts the West Midlands North Major Trauma Centre, regional cardiothoracic, neurosciences and renal services, driving above-peer training and IT-subscription baseline.",
        'beneficiaries': 'c. 11,500 WTE staff serving a c. 900,000 Staffordshire + Shropshire catchment plus tertiary specialty referrals from across the West Midlands North; c. 220,000 ED attendances/yr (Royal Stoke + County EDs); c. 130,000 admissions/yr; West Midlands North MTC at Royal Stoke.',
        'legal_basis': 'DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25',
        'key_stats': [
            {'label': 'Establishment costs 2024-25', 'value': '£5.59M'},
            {'label': 'Trust scale', 'value': 'Two-site major-acute (Royal Stoke + County Hospital, Stafford); c. 11,500 WTE'},
            {'label': 'Composition', 'value': 'Postage + telephony + IT subscriptions + training + professional fees + advertising + agency-recruitment fees + courier'},
            {'label': 'Major Trauma Centre', 'value': 'West Midlands North MTC at Royal Stoke — drives high-volume training + tertiary-referral establishment baseline'},
            {'label': 'Tertiary specialist services', 'value': 'Cardiothoracic + neurosciences + renal + specialist paediatrics — substantial tertiary-referral training + IT-subscription baseline'},
            {'label': 'FD EPR context', 'value': 'EPR rollout under NHSE FD programme — drives training + change-management establishment cost'},
            {'label': 'Industrial action 2023-24 effect', 'value': '44 days junior-doctor + 10 days consultant strikes drove agency-recruitment fee uplift'},
            {'label': 'April 2025 NIC + CPI', 'value': 'Apr 2025 NIC pass-through on agency + sustained CPI on subscriptions feed forward unit-cost pressure'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.5M → 2023-24 £5.2M → 2024-25 £5.59M — CPI + EPR + agency-recruitment uplift'},
            {'label': 'Delivery body', 'value': 'Trust Finance + Procurement + HR Workforce-Resourcing teams'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + Staffordshire & Stoke-on-Trent ICB'},
            {'label': 'Evaluation evidence', 'value': 'Model Hospital establishment-cost benchmarks; CQC inspection RJE; Trust ARA disclosure'}
        ],
        'notes': "UHNM's establishment-costs line is shaped by the two-site major-acute footprint (Royal Stoke + County Hospital Stafford) and the West Midlands North Major Trauma Centre at Royal Stoke — driving high-volume training, tertiary-referral and IT-subscription baseline above pure DGH peers. The 2014 dissolution of Mid Staffordshire NHS FT (post-Francis Inquiry) brought the County Hospital site into the merged UHNM footprint. Industrial action 2023-24 lifted agency-recruitment fees through repeated locum mobilisation across acute medicine and surgical rotas. The April 2025 employer-NIC step-up flows through agency-staffing pass-through; CPI on IT subscriptions and training continues to feed forward.",
        'sources': [
            {'publisher': 'University Hospitals of North Midlands NHS Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.uhnm.nhs.uk/about-us/publications-policies-and-procedures/'},
            {'publisher': 'NHS England', 'title': 'Frontline Digitisation programme', 'url': 'https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'UHNM provider profile (RJE)', 'url': 'https://www.cqc.org.uk/provider/RJE'},
            {'publisher': 'NHS England', 'title': 'RAAC remediation programme — affected sites', 'url': 'https://www.england.nhs.uk/estates/raac/'}
        ],
        'related': ['University Hospitals of North Midlands NHS Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Establishment costs — East And North Hertfordshire NHS Trust', 'Business rates — University Hospitals of North Midlands NHS Trust', 'NHS England']
    },
    'Business rates — University Hospitals of North Midlands NHS Trust': {
        'aliases': [
            {'name': 'Business rates', 'parent': 'University Hospitals of North Midlands NHS Trust'}
        ],
        'description': "UHNM's £5.55M business rates line covers non-domestic rates payable across the two-site major-acute footprint — the Royal Stoke University Hospital (Stoke-on-Trent) and the County Hospital (Stafford) — under the 2023 VOA rating list operated through Stoke-on-Trent City Council and Stafford Borough Council billing authorities. The trust hosts the West Midlands North Major Trauma Centre, regional cardiothoracic, neurosciences and renal services on a substantial high-RV estate. NDR Act 2024 sets forward multiplier path.",
        'beneficiaries': 'c. 11,500 WTE staff serving a c. 900,000 Staffordshire + Shropshire catchment plus tertiary specialty referrals across West Midlands North (c. 3.0M tertiary catchment); c. 220,000 ED attendances/yr (Royal Stoke + County EDs); c. 130,000 admissions/yr; WMN MTC at Royal Stoke.',
        'legal_basis': 'Local Government Finance Act 1988 (Schedule 6 — Non-Domestic Rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006',
        'key_stats': [
            {'label': 'Business rates 2024-25', 'value': '£5.55M'},
            {'label': 'Trust scale', 'value': 'Two-site major-acute (Royal Stoke + County Hospital, Stafford); c. 11,500 WTE'},
            {'label': 'Major Trauma Centre', 'value': 'West Midlands North MTC at Royal Stoke — drives high-RV emergency-care + tertiary specialist estate'},
            {'label': 'Tertiary specialist estate', 'value': 'Cardiothoracic + neurosciences + renal + specialist paediatrics — substantial high-RV specialist footprint'},
            {'label': 'VOA 2023 rating list', 'value': 'AVD 1 April 2021; rating list took effect 1 April 2023; next revaluation 2026'},
            {'label': 'Multiplier 2024-25', 'value': 'Standard multiplier 54.6p; small business multiplier 49.9p (England)'},
            {'label': 'NDR Act 2024 effect', 'value': 'Divergent multipliers for high-value (RV ≥ £500k) vs standard properties from 2025-26 — material for Royal Stoke flagship'},
            {'label': 'Billing authorities', 'value': 'Stoke-on-Trent City Council (Royal Stoke) + Stafford Borough Council (County Hospital)'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.7M → 2023-24 £5.2M → 2024-25 £5.55M — RV uplift from 2023 list + multiplier'},
            {'label': 'Delivery body', 'value': 'Valuation Office Agency (HMRC ALB) + Stoke-on-Trent + Stafford billing authorities + trust E&F'},
            {'label': 'Policy owner', 'value': 'MHCLG (NDR policy) + HMT (multiplier) + DHSC + Staffordshire & Stoke-on-Trent ICB'},
            {'label': 'Evaluation evidence', 'value': 'VOA rating list disclosures; HMT 2023 NDR consultation; CQC inspection RJE; Trust ARA'}
        ],
        'notes': "UHNM's business-rates line is shaped by the trust's two-site major-acute footprint and Major Trauma Centre status at Royal Stoke — driving high aggregate rateable value across the 2023 VOA rating list. The Royal Stoke is partly PFI-built (Skanska Innisfree consortium); its NDR sits separately from the PFI unitary charge but reflects new-build estate RV. The 2014 dissolution of Mid Staffordshire NHS FT (post-Francis Inquiry) brought the County Hospital Stafford site into the merged trust's rating register. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces divergent multipliers for high-value (RV ≥ £500k) and standard properties from 2025-26, with material implications for the Royal Stoke flagship.",
        'sources': [
            {'publisher': 'University Hospitals of North Midlands NHS Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.uhnm.nhs.uk/about-us/publications-policies-and-procedures/'},
            {'publisher': 'Valuation Office Agency', 'title': '2023 rating list and revaluation guidance', 'url': 'https://www.gov.uk/government/organisations/valuation-office-agency'},
            {'publisher': 'HM Treasury', 'title': 'Non-Domestic Rating (Multipliers and Private Finance) Act 2024', 'url': 'https://www.legislation.gov.uk/ukpga/2024/30/contents'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'UHNM provider profile (RJE)', 'url': 'https://www.cqc.org.uk/provider/RJE'}
        ],
        'related': ['University Hospitals of North Midlands NHS Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Valuation Office Agency', 'Business rates — Oxford University Hospitals NHS Foundation Trust', 'Establishment costs — University Hospitals of North Midlands NHS Trust']
    },
    'Establishment costs — York and Scarborough Teaching Hospitals NHS Foundation Trust': {
        'aliases': [
            {'name': 'Establishment costs', 'parent': 'York and Scarborough Teaching Hospitals NHS Foundation Trust'}
        ],
        'description': "York & Scarborough's £5.53M establishment costs line covers postage, telephony, IT subscriptions, training, professional fees, advertising, agency-recruitment fees, conference fees and courier services across the multi-site footprint — York Hospital (main acute), Scarborough Hospital, Bridlington Hospital, Selby War Memorial Hospital plus integrated community services across North Yorkshire. The wide rural geography drives elevated courier and telephony establishment baseline relative to compact urban single-site peers.",
        'beneficiaries': "c. 8,500 WTE staff serving a c. 800,000 York, North Yorkshire + East Riding catchment; c. 175,000 ED attendances/yr (York + Scarborough EDs); c. 95,000 admissions/yr; integrated community services across one of England's largest geographies including coastal Scarborough/Bridlington and rural Selby/Easingwold.",
        'legal_basis': 'DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25',
        'key_stats': [
            {'label': 'Establishment costs 2024-25', 'value': '£5.53M'},
            {'label': 'Trust scale', 'value': 'Multi-site (York + Scarborough + Bridlington + Selby + community services); c. 8,500 WTE'},
            {'label': 'Composition', 'value': 'Postage + telephony + IT subscriptions + training + professional fees + advertising + agency-recruitment fees + courier'},
            {'label': 'Geography premium', 'value': 'Wide rural North Yorkshire + East Riding footprint — drives courier + telephony establishment baseline above urban single-site peers'},
            {'label': 'Scarborough remoteness', 'value': 'Scarborough acute site + coastal/rural community footprint drives separate IT-subscription + training cohort baseline'},
            {'label': 'FD EPR context', 'value': 'EPR rollout under NHSE FD programme (CPP York-Scarborough joint instance) — drives training + change-management establishment cost'},
            {'label': 'Industrial action 2023-24 effect', 'value': '44 days junior-doctor + 10 days consultant strikes drove agency-recruitment fee uplift; remote rota sustainability challenge'},
            {'label': 'April 2025 NIC + CPI', 'value': 'Apr 2025 NIC pass-through on agency + sustained CPI on subscriptions feed forward unit-cost pressure'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.5M → 2023-24 £5.1M → 2024-25 £5.53M — CPI + EPR + agency-recruitment uplift'},
            {'label': 'Delivery body', 'value': 'Trust Finance + Procurement + HR Workforce-Resourcing teams'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + Humber and North Yorkshire ICB'},
            {'label': 'Evaluation evidence', 'value': 'Model Hospital establishment-cost benchmarks; CQC inspection RCB; Trust ARA disclosure'}
        ],
        'notes': "York & Scarborough's establishment-costs line is shaped by the multi-site rural footprint across North Yorkshire and East Riding — one of England's largest trust geographies — driving baseline courier, telephony and training costs above urban single-site peers. The 2012 acquisition of Scarborough & North East Yorkshire Healthcare NHS Trust by York Teaching Hospital NHS FT consolidated the multi-site footprint, with Scarborough's coastal remoteness driving distinct IT-subscription and training cohort baselines. Industrial action 2023-24 lifted agency-recruitment fees, exacerbated by the chronic challenge of remote-rota recruitment at Scarborough/Bridlington sites.",
        'sources': [
            {'publisher': 'York and Scarborough Teaching Hospitals NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.yorkhospitals.nhs.uk/about-us/our-publications/'},
            {'publisher': 'NHS England', 'title': 'Frontline Digitisation programme', 'url': 'https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'York & Scarborough provider profile (RCB)', 'url': 'https://www.cqc.org.uk/provider/RCB'},
            {'publisher': 'Nuffield Trust', 'title': 'Rural healthcare workforce challenges', 'url': 'https://www.nuffieldtrust.org.uk/research/'}
        ],
        'related': ['York and Scarborough Teaching Hospitals NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Establishment costs — Northumbria Healthcare NHS Foundation Trust', 'Establishment costs — University Hospitals of North Midlands NHS Trust', 'NHS England']
    },
    'Business rates — Sheffield Teaching Hospitals NHS Foundation Trust': {
        'aliases': [
            {'name': 'Business rates', 'parent': 'Sheffield Teaching Hospitals NHS Foundation Trust'}
        ],
        'description': "STH's £5.53M business rates line covers non-domestic rates payable across the trust's multi-site footprint — the Royal Hallamshire Hospital, Northern General Hospital, Weston Park Hospital (cancer), Charles Clifford Dental Hospital, Jessop Wing (maternity) — under the 2023 VOA rating list operated through Sheffield City Council billing authority. The trust hosts the South Yorkshire Major Trauma Centre at Northern General, regional cancer services at Weston Park, and substantial tertiary specialty estate. NDR Act 2024 sets forward multiplier path.",
        'beneficiaries': 'c. 18,500 WTE staff serving a c. 600,000 Sheffield catchment plus tertiary specialty referrals across South Yorkshire + North Midlands (c. 2.0M tertiary catchment); c. 175,000 ED attendances/yr (Northern General + Hallamshire EDs); c. 165,000 admissions/yr; SY MTC at Northern General.',
        'legal_basis': 'Local Government Finance Act 1988 (Schedule 6 — Non-Domestic Rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006',
        'key_stats': [
            {'label': 'Business rates 2024-25', 'value': '£5.53M'},
            {'label': 'Trust scale', 'value': 'Multi-site (Royal Hallamshire + Northern General + Weston Park + Charles Clifford + Jessop Wing); c. 18,500 WTE'},
            {'label': 'Major Trauma Centre', 'value': 'South Yorkshire MTC at Northern General — drives high-RV emergency-care estate'},
            {'label': 'Tertiary specialist estate', 'value': 'Weston Park Cancer + neurosciences + cardiothoracic + dental (Charles Clifford) + transplantation — substantial high-RV specialist footprint'},
            {'label': 'VOA 2023 rating list', 'value': 'AVD 1 April 2021; rating list took effect 1 April 2023; next revaluation 2026'},
            {'label': 'Multiplier 2024-25', 'value': 'Standard multiplier 54.6p; small business multiplier 49.9p (England)'},
            {'label': 'NDR Act 2024 effect', 'value': 'Divergent multipliers for high-value (RV ≥ £500k) vs standard properties from 2025-26 — material for Northern General + Hallamshire flagships'},
            {'label': 'Billing authority', 'value': 'Sheffield City Council — single billing authority across all city-centre trust sites'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.7M → 2023-24 £5.2M → 2024-25 £5.53M — RV uplift from 2023 list + multiplier'},
            {'label': 'Delivery body', 'value': 'Valuation Office Agency (HMRC ALB) + Sheffield City Council billing authority + trust E&F'},
            {'label': 'Policy owner', 'value': 'MHCLG (NDR policy) + HMT (multiplier) + DHSC + South Yorkshire ICB'},
            {'label': 'Evaluation evidence', 'value': 'VOA rating list disclosures; HMT 2023 NDR consultation; CQC inspection RHQ; Trust ARA'}
        ],
        'notes': "STH's business-rates line is shaped by the trust's substantial multi-site academic-acute footprint across Sheffield — Royal Hallamshire (city-centre tertiary), Northern General (Major Trauma Centre + cardiothoracic + renal + transplantation), Weston Park (regional cancer hub serving South Yorkshire and North Midlands), Charles Clifford Dental Hospital and the Jessop Wing maternity unit. All sites fall within Sheffield City Council billing authority, simplifying NDR administration relative to multi-authority peer trusts. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces divergent multipliers for high-value (RV ≥ £500k) and standard properties from 2025-26, with material implications for the Northern General and Hallamshire flagships.",
        'sources': [
            {'publisher': 'Sheffield Teaching Hospitals NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.sth.nhs.uk/about-us/key-publications/annual-report'},
            {'publisher': 'Valuation Office Agency', 'title': '2023 rating list and revaluation guidance', 'url': 'https://www.gov.uk/government/organisations/valuation-office-agency'},
            {'publisher': 'HM Treasury', 'title': 'Non-Domestic Rating (Multipliers and Private Finance) Act 2024', 'url': 'https://www.legislation.gov.uk/ukpga/2024/30/contents'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'Sheffield Teaching Hospitals provider profile (RHQ)', 'url': 'https://www.cqc.org.uk/provider/RHQ'}
        ],
        'related': ['Sheffield Teaching Hospitals NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Valuation Office Agency', 'Business rates — Oxford University Hospitals NHS Foundation Trust', 'Business rates — King’s College Hospital NHS Foundation Trust']
    },
    'Amortisation — Kingston Hospital NHS Foundation Trust': {
        'aliases': [
            {'name': 'Amortisation', 'parent': 'Kingston Hospital NHS Foundation Trust'}
        ],
        'description': "Kingston Hospital's £5.49M amortisation line covers the systematic write-down of intangible assets — predominantly EPR software (Cerner Millennium under SWL ICS shared instance), licensed clinical applications, capitalised software development and other intangibles — over their assessed useful economic lives under IAS 38 and DHSC GAM ch.5. The trust runs the single-site Kingston Hospital, with active group-model arrangements across Kingston + Hounslow & Richmond Community Healthcare and chair-in-common with Epsom & St Helier under SWL ICS planning.",
        'beneficiaries': 'c. 4,000 WTE staff serving a c. 350,000 Kingston, Richmond and Wandsworth catchment; c. 110,000 ED attendances/yr at Kingston ED; c. 45,000 admissions/yr; large maternity service (c. 5,500 deliveries/yr — among largest in SWL).',
        'legal_basis': 'IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 (intangibles) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022',
        'key_stats': [
            {'label': 'Amortisation 2024-25', 'value': '£5.49M'},
            {'label': 'Trust scale', 'value': 'Single-site DGH (Kingston Hospital, Kingston upon Thames); c. 4,000 WTE'},
            {'label': 'Composition', 'value': 'EPR software amortisation + licensed clinical applications + capitalised software development + other intangibles'},
            {'label': 'EPR context', 'value': 'Cerner Millennium EPR shared SWL instance — capitalised software amortising under IAS 38 over 5-10 year UEL'},
            {'label': 'FD EPR programme', 'value': 'NHSE Frontline Digitisation EPR programme funding underpins capitalisation; subsequent amortisation cycles feed forward'},
            {'label': 'SWL ICS group model', 'value': 'Active group-model arrangement with Hounslow & Richmond Community Healthcare; chair-in-common with Epsom & St Helier — shared digital systems amortise across federated footprint'},
            {'label': 'Maternity service', 'value': 'Large maternity (c. 5,500 deliveries/yr) drives maternity-specific clinical-application amortisation'},
            {'label': 'IAS 38 useful life assumption', 'value': 'Software typically 5-10 years UEL (trust accounting policy); reviewed annually'},
            {'label': 'Funding trajectory', 'value': '2021-22 c. £4.0M → 2023-24 £5.0M → 2024-25 £5.49M — sustained capitalised-software amortisation cycle'},
            {'label': 'Delivery body', 'value': 'Trust Finance + Digital teams + SWL ICS Digital Transformation'},
            {'label': 'Policy owner', 'value': 'NHSE Provider Finance + DHSC + NHSE FD EPR + South West London ICB'},
            {'label': 'Evaluation evidence', 'value': 'NHSE FD EPR programme evaluation; CQC inspection RAX (Outstanding 2018, 2023); Trust ARA intangibles disclosure'}
        ],
        'notes': "Kingston Hospital's amortisation line is shaped by the trust's single-site footprint and SWL ICS shared digital architecture — Cerner Millennium EPR is operated as a shared SWL instance, with capitalised software amortising under IAS 38 over 5-10 year UEL per trust accounting policy. NHSE Frontline Digitisation EPR programme funding underpins ongoing capitalisation, with subsequent amortisation feeding the line forward as further FD investment lands. The trust's group-model arrangement with Hounslow & Richmond Community Healthcare (active) and chair-in-common with Epsom & St Helier University Hospitals NHS Trust under SWL ICS planning shape medium-term consolidation of digital systems and the intangible asset register.",
        'sources': [
            {'publisher': 'Kingston Hospital NHS Foundation Trust', 'title': 'Annual Report and Accounts 2023-24', 'url': 'https://www.kingstonhospital.nhs.uk/about-us/our-publications/'},
            {'publisher': 'NHS England', 'title': 'Frontline Digitisation programme', 'url': 'https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/'},
            {'publisher': 'Department of Health and Social Care', 'title': 'Group Accounting Manual 2024-25 (chapter 5 — intangibles)', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
            {'publisher': 'Care Quality Commission', 'title': 'Kingston Hospital provider profile (RAX) — Outstanding', 'url': 'https://www.cqc.org.uk/provider/RAX'},
            {'publisher': 'NHS England', 'title': 'South West London ICS digital strategy', 'url': 'https://www.southwestlondon.icb.nhs.uk/'}
        ],
        'related': ['Kingston Hospital NHS Foundation Trust', 'Premises & Infrastructure', 'NHS Acute Trusts', 'Amortisation — Royal Free London NHS Foundation Trust', 'Social security & levy — Kingston Hospital NHS Foundation Trust', 'NHS England']
    }
}
