# Tier A depth-4 enrichment: Drugs costs sub-lines for NHS trusts (Batch B, 48 entries)
# Each entry is tailor-made to the trust's specialty mix, HCD footprint, and 2024-25 context.

NEW = {
    "Drugs costs — Guy's & St Thomas' NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Guy's & St Thomas' NHS Foundation Trust"}],
        "description": "Drug expenditure for GSTT, one of England's largest acute-teaching groups (Guy's, St Thomas', Evelina, Royal Brompton & Harefield), anchored by the Cancer Centre at Guy's, adult and paediatric cardiothoracic transplant services, HIV/GUM (Harrison Wing) and cystic fibrosis. HCD-heavy mix reflects bevacizumab/pembrolizumab/trastuzumab pipelines, CFTR modulators (Kaftrio/Symkevi) and transplant immunosuppression.",
        "beneficiaries": "~3.2M Lambeth/Southwark residents plus national specialist cardiothoracic, paediatric cardiology, HIV and CF catchments.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHS England Specialised Commissioning (Section 7A) for HCDs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£340.08M"},
            {"label": "Share of trust opex", "value": "~13-14%"},
            {"label": "Oncology/haematology share", "value": "~38% (Guy's Cancer Centre)"},
            {"label": "HCDs pass-through", "value": "~70% (ICB/NHSE-commissioned)"},
            {"label": "Biosimilar switches live", "value": "adalimumab, rituximab, trastuzumab, bevacizumab"},
            {"label": "CF modulator spend (Kaftrio/Symkevi)", "value": "Material via Royal Brompton adult CF service"},
            {"label": "YoY growth", "value": "~+9% (new immuno-oncology indications + CDF exits)"},
            {"label": "Pharmacy WTE (group)", "value": "~650 (GSTT Pharmacy incl. aseptics at Guy's)"},
            {"label": "Procurement consortium", "value": "NHS London Procurement Partnership + CMU framework"},
            {"label": "Homecare medicines value", "value": ">£120M channelled via Sciensus/Polar Speed/HealthNet"}
        ],
        "notes": "2024-25 drug bill driven by Evelina paediatric cardiac/ECMO drugs, Royal Brompton CFTR modulators (Vertex), and Guy's Cancer immuno-oncology (Keytruda/Opdivo) combinations. VPAG rebate transition (15.3% headline) partially offsets pembrolizumab/nivolumab volume growth. Industrial-action knock-on deferred elective chemo pushed Q1-Q2 spend forwards. Biosimilar trastuzumab and bevacizumab switches (Q3 2024) offered ~£4-6M in-year savings. Sizable homecare channel for immunology/HIV ARTs reduces on-site dispensing but remains on the trust P&L.",
        "sources": [
            {"publisher": "Guy's and St Thomas' NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.guysandstthomas.nhs.uk/about-us/corporate-publications"},
            {"publisher": "NHS England", "title": "National Cost Collection for the NHS 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "DHSC", "title": "Voluntary Scheme for Branded Medicines Pricing, Access and Growth (VPAG) 2024", "url": "https://www.gov.uk/government/publications/the-2024-voluntary-scheme-for-branded-medicines-pricing-access-and-growth"}
        ],
        "related": ["Guy's & St Thomas' NHS Foundation Trust", "Clinical Supplies & Drugs — Guy's & St Thomas' NHS Foundation Trust"]
    },
    "Drugs costs — University College London Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University College London Hospitals NHS Foundation Trust"}],
        "description": "Drug expenditure for UCLH, a central-London teaching trust hosting UCH Macmillan Cancer Centre, the National Hospital for Neurology & Neurosurgery (Queen Square), UCLH Proton Beam Centre, and specialist HIV, haematology and rare-disease services. Spend is dominated by CAR-T (Kymriah/Yescarta), bispecifics, MS DMTs (ocrelizumab, natalizumab) and orphan neurology drugs.",
        "beneficiaries": "Local Camden/central-London population plus tertiary national neurology, haemato-oncology, proton beam therapy and infectious-disease referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£266.54M"},
            {"label": "Share of trust opex", "value": "~16-17%"},
            {"label": "Oncology + haematology share", "value": "~45% (Macmillan Cancer Centre + UCLH CAR-T centre)"},
            {"label": "Neurology DMT share", "value": "~18% (Queen Square MS/neuro-immunology)"},
            {"label": "HCD pass-through share", "value": "~72% NHSE-commissioned"},
            {"label": "CAR-T cases commissioned", "value": "Adult lymphoma + ALL hub site"},
            {"label": "Biosimilar penetration", "value": "adalimumab >95%, rituximab >90%, trastuzumab >90%"},
            {"label": "YoY growth", "value": "~+11% (CAR-T volume + new NICE TAs)"},
            {"label": "Homecare channel", "value": "HIV ARTs + MS DMTs material via homecare providers"}
        ],
        "notes": "UCLH is a national CAR-T delivery hub (NHSE-commissioned, pass-through at list) — volume growth and bispecifics (epcoritamab, glofitamab) underpin double-digit growth. Queen Square neurology drives ocrelizumab/natalizumab/inebilizumab spend. Proton Beam service brings ancillary supportive drugs but not therapy itself. VPAG rebate (~15.3%) partially credits back to DHSC, not trust. Industrial action (2023-24) delayed some haematology regimens; rebased Q2 2024-25.",
        "sources": [
            {"publisher": "University College London Hospitals NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.uclh.nhs.uk/about-us/who-we-are/corporate-publications"},
            {"publisher": "NHS England", "title": "Commissioning CAR-T cell therapy", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/blood-and-infection-group-f/f01/"},
            {"publisher": "NICE", "title": "Technology appraisal guidance", "url": "https://www.nice.org.uk/guidance/published?ngt=Technology%20appraisal%20guidance"}
        ],
        "related": ["University College London Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — University College London Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — King’s College Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "King’s College Hospital NHS Foundation Trust"}],
        "description": "Drug expenditure for King's, a major south-London teaching trust (Denmark Hill, Princess Royal Orpington) hosting the UK's largest liver transplant programme, the King's Haemato-Oncology centre, neurosciences (major trauma), and a large HIV service. Spend is weighted to transplant immunosuppression, haemato-oncology (AML/MM/lymphoma) and anti-virals.",
        "beneficiaries": "~700,000 Lambeth/Southwark/Bromley residents plus national liver transplant and haemato-oncology referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning (liver transplant, haem-onc HCDs) · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£222.78M"},
            {"label": "Share of trust opex", "value": "~13%"},
            {"label": "Haemato-oncology + solid-tumour share", "value": "~40%"},
            {"label": "Transplant immunosuppression", "value": "Material (largest UK liver programme)"},
            {"label": "HCDs commissioned (NHSE/ICB)", "value": "~68%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, bevacizumab, trastuzumab"},
            {"label": "YoY growth", "value": "~+8%"},
            {"label": "Pharmacy WTE", "value": "~380 across Denmark Hill / PRUH"},
            {"label": "Procurement framework", "value": "LPP + CMU"}
        ],
        "notes": "CAR-T and bispecifics in lymphoma/MM underpin haemato-oncology growth alongside King's myeloma CAR-T activity. Liver transplant volumes (~250/yr) drive tacrolimus/MMF/everolimus + antiviral prophylaxis spend. HIV service on Caldecot Centre shifts most ART cost to homecare but remains on trust P&L. Industrial action (2023-24) compressed some elective chemo into Q3-Q4 2024-25. Viekirax/Epclusa HCV cure regimens tail off; replaced by long-acting injectable ART uptake. VPAG transition lowers rebate yield for trust (rebate credited centrally).",
        "sources": [
            {"publisher": "King's College Hospital NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.kch.nhs.uk/about/corporate/annual-report-and-accounts/"},
            {"publisher": "NHS Blood and Transplant", "title": "Annual Activity Report – Liver transplantation 2023-24", "url": "https://www.odt.nhs.uk/statistics-and-reports/annual-activity-report/"},
            {"publisher": "NHS England", "title": "Specialised Commissioning – HCDs list", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/"}
        ],
        "related": ["King’s College Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — King’s College Hospital NHS Foundation Trust"]
    },
    "Drugs costs — University Hospital Southampton NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University Hospital Southampton NHS Foundation Trust"}],
        "description": "Drug expenditure for UHS, Wessex's tertiary acute centre hosting the regional cardiac, neurosciences, paediatric and adult cancer services, plus the Wessex Genomic Medicine Centre. Oncology SACT, immunosuppressants for cardiac transplant, cystic fibrosis modulators and paediatric rare-disease drugs drive spend.",
        "beneficiaries": "~1.9M Hampshire / IoW / Wessex residents plus tertiary cardiac, paediatric oncology, neurosciences referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£195.37M"},
            {"label": "Share of trust opex", "value": "~15%"},
            {"label": "Oncology/haematology share", "value": "~40%"},
            {"label": "HCDs commissioned by NHSE/ICB", "value": "~68%"},
            {"label": "CF modulator spend (Kaftrio/Symkevi)", "value": "Regional CF centre – material line"},
            {"label": "Biosimilar switches live", "value": "adalimumab >95%, rituximab >90%, trastuzumab, bevacizumab"},
            {"label": "YoY growth", "value": "~+9%"},
            {"label": "Pharmacy WTE", "value": "~260"},
            {"label": "Procurement consortium", "value": "NHS South Central Pharmacy Procurement + CMU"}
        ],
        "notes": "Southampton is a NICE-mandated CAR-T referral pathway site and runs the Wessex CF adult centre (Vertex CFTR modulators). 2024-25 growth reflects adjuvant durvalumab/osimertinib expansion and paediatric oncology CAR-T pathway. Industrial action reduced some day-case chemo in 2023-24 with rebound in 2024-25. GLP-1 (semaglutide/tirzepatide) weight-management pathways are community-commissioned and sit largely off trust drugs bill. Bevacizumab biosimilar (from Q3 2024) offering ~2-3% in-year saving on line.",
        "sources": [
            {"publisher": "University Hospital Southampton NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.uhs.nhs.uk/about-us/our-publications/annual-report-and-accounts"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "Cystic Fibrosis Trust", "title": "UK CF Registry Annual Data Report 2023", "url": "https://www.cysticfibrosis.org.uk/the-work-we-do/uk-cf-registry"}
        ],
        "related": ["University Hospital Southampton NHS Foundation Trust", "Clinical Supplies & Drugs — University Hospital Southampton NHS Foundation Trust"]
    },
    "Drugs costs — University Hospitals of Leicester NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University Hospitals of Leicester NHS Trust"}],
        "description": "Drug expenditure for UHL, a three-hospital (LRI, Glenfield, LGH) teaching trust serving Leicester, Leicestershire & Rutland. Host of the East Midlands Congenital Heart Centre and renal transplant unit; spend skewed to cardiology (Glenfield), renal immunosuppression, oncology SACT (Osborne Building) and respiratory biologics.",
        "beneficiaries": "~1.1M Leicester/Leicestershire/Rutland residents plus east-Midlands tertiary cardiac, renal, ECMO referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£152.81M"},
            {"label": "Share of trust opex", "value": "~11%"},
            {"label": "Oncology share", "value": "~34%"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~62%"},
            {"label": "Renal transplant immunosuppression", "value": "Tacrolimus/MMF – material recurring spend"},
            {"label": "Biosimilar live switches", "value": "adalimumab, infliximab, rituximab, trastuzumab"},
            {"label": "YoY growth", "value": "~+7%"},
            {"label": "Pharmacy WTE", "value": "~220"},
            {"label": "Procurement framework", "value": "NoE CPC + CMU"}
        ],
        "notes": "Spend mix atypical because Glenfield hosts ECMO, cardiothoracic and the East-Midlands Congenital Heart Centre — drives inotrope, pulmonary hypertension (bosentan/macitentan) and anticoagulation volume. Respiratory biologics (mepolizumab, benralizumab, dupilumab) growing double-digit on severe asthma pathway. Osborne Building chemo day-unit drives adjuvant immuno-oncology. Industrial action delayed some elective oncology 2023-24. GLP-1 diabetes (semaglutide) supply constraints eased late 2024-25.",
        "sources": [
            {"publisher": "University Hospitals of Leicester NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.leicestershospitals.nhs.uk/aboutus/our-news-publications/corporate-publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Specialised Commissioning – HCDs", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/"},
            {"publisher": "NICE", "title": "Severe asthma biologics – TAs", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/respiratory-conditions/asthma"}
        ],
        "related": ["University Hospitals of Leicester NHS Trust", "Clinical Supplies & Drugs — University Hospitals of Leicester NHS Trust"]
    },
    "Drugs costs — Mid and South Essex NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Mid and South Essex NHS Foundation Trust"}],
        "description": "Drug expenditure for MSEFT, a three-hospital acute trust (Basildon, Broomfield, Southend) formed 2020 serving ~1.2M Essex residents. Essex Cardiothoracic Centre (Basildon) and the regional plastics/burns unit (St Andrew's, Broomfield) shape the spend profile, with oncology now consolidated post-merger.",
        "beneficiaries": "~1.2M mid/south Essex residents; tertiary cardiothoracic and burns/plastics referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£123.80M"},
            {"label": "Share of trust opex", "value": "~8%"},
            {"label": "Oncology SACT share", "value": "~32%"},
            {"label": "Cardiothoracic drugs share", "value": "~12% (Essex Cardiothoracic Centre)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~60%"},
            {"label": "Biosimilar penetration", "value": "adalimumab >95%, trastuzumab ~85%, rituximab ~90%"},
            {"label": "YoY growth", "value": "~+8% (post-merger consolidation + new TAs)"},
            {"label": "Pharmacy WTE", "value": "~180 across three sites"},
            {"label": "Procurement framework", "value": "EAHSN + CMU"}
        ],
        "notes": "Post-merger formulary harmonisation delivered modest savings but adjuvant checkpoint inhibitors (pembrolizumab, atezolizumab) and new CDK4/6 TAs (ribociclib, abemaciclib) pushed oncology spend up. Essex Cardiothoracic Centre drives ticagrelor, anticoagulants and post-CABG regimens. Broomfield burns unit uses high-value dressings and specialist antifungals (isavuconazole). GLP-1 supply shortages through 2023-24 eased in 2024-25. VPAG rebate transition reduced notional net-price savings relative to VPAS in prior year.",
        "sources": [
            {"publisher": "Mid and South Essex NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.mse.nhs.uk/publications"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NICE", "title": "Technology appraisal guidance", "url": "https://www.nice.org.uk/guidance"}
        ],
        "related": ["Mid and South Essex NHS Foundation Trust", "Clinical Supplies & Drugs — Mid and South Essex NHS Foundation Trust"]
    },
    "Drugs costs — University Hospitals of Derby and Burton NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University Hospitals of Derby and Burton NHS Foundation Trust"}],
        "description": "Drug expenditure for UHDB, a five-site integrated acute/community trust (Royal Derby, Queen's Burton, plus three community hospitals) serving ~1.1M southern Derbyshire / east Staffordshire residents. Regional vascular and renal dialysis spend sit alongside oncology SACT at the Royal Derby Cancer Centre.",
        "beneficiaries": "~1.1M southern Derbyshire / east Staffordshire residents; regional renal dialysis and vascular referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£117.53M"},
            {"label": "Share of trust opex", "value": "~10%"},
            {"label": "Oncology share", "value": "~32% (Royal Derby Cancer Centre)"},
            {"label": "Renal/dialysis-related drugs", "value": "Material (iron sucrose, ESAs, phosphate binders)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~60%"},
            {"label": "Biosimilar live switches", "value": "adalimumab >95%, rituximab, trastuzumab, bevacizumab"},
            {"label": "YoY growth", "value": "~+7%"},
            {"label": "Pharmacy WTE", "value": "~170 across Derby + Burton"},
            {"label": "Procurement framework", "value": "NoE CPC + CMU"}
        ],
        "notes": "Oncology growth driven by new adjuvant/neoadjuvant TAs and CDK4/6 in breast cancer. Renal service at Royal Derby supports ~800 HD/PD patients, generating steady ESA/iron/phosphate-binder volume. Vascular service uses high-cost sartans/DOAC pathways. Industrial-action impact (2023-24) deferred elective chemo, rebased in 2024-25. GLP-1 diabetes pathway normalised in H2 2024-25 after national shortages.",
        "sources": [
            {"publisher": "University Hospitals of Derby and Burton NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.uhdb.nhs.uk/annual-reports/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "UK Renal Registry", "title": "Annual Report 2023", "url": "https://ukkidney.org/audit-research/annual-report"}
        ],
        "related": ["University Hospitals of Derby and Burton NHS Foundation Trust", "Clinical Supplies & Drugs — University Hospitals of Derby and Burton NHS Foundation Trust"]
    },
    "Drugs costs — Liverpool University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Liverpool University Hospitals NHS Foundation Trust"}],
        "description": "Drug expenditure for LUHFT, the merged acute trust (Royal Liverpool, Aintree, Broadgreen) serving central Merseyside. Host of the regional renal transplant service at Royal Liverpool and tertiary hepatobiliary, head & neck oncology and infectious diseases. Oncology spend largely routed via adjacent Clatterbridge Cancer Centre but trust carries inpatient SACT and supportive care.",
        "beneficiaries": "~750,000 Liverpool/Knowsley/Sefton residents; tertiary renal transplant, head & neck, hepatobiliary cohorts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£107.19M"},
            {"label": "Share of trust opex", "value": "~8%"},
            {"label": "Inpatient oncology/SACT share", "value": "~22% (most outpatient SACT via Clatterbridge)"},
            {"label": "Renal transplant immunosuppression", "value": "Material (~120 transplants/yr)"},
            {"label": "Infectious diseases / HIV drugs", "value": "Material via Royal Liverpool ID unit"},
            {"label": "Biosimilar penetration", "value": "adalimumab >95%, infliximab, rituximab"},
            {"label": "YoY growth", "value": "~+6%"},
            {"label": "Pharmacy WTE", "value": "~200"},
            {"label": "Procurement framework", "value": "NW Pharmacy Procurement + CMU"}
        ],
        "notes": "Drug-spend share lower than peers because the adjacent Clatterbridge Cancer Centre carries bulk outpatient SACT. LUHFT retains inpatient oncology, renal transplant immunosuppression, and regional ID (antiretrovirals, hepatitis antivirals). New Royal Liverpool opened 2022 — drug logistics modernised, EPMA reduces waste. Industrial action delayed some elective activity 2023-24. GLP-1 diabetes volumes normalised H2 2024-25.",
        "sources": [
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.liverpoolft.nhs.uk/about-us/annual-reports-and-accounts/"},
            {"publisher": "NHS Blood and Transplant", "title": "Annual Activity Report 2023-24", "url": "https://www.odt.nhs.uk/statistics-and-reports/annual-activity-report/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"}
        ],
        "related": ["Liverpool University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Liverpool University Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — Gloucestershire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Gloucestershire Hospitals NHS Foundation Trust"}],
        "description": "Drug expenditure for GHFT, a two-site acute trust (Gloucestershire Royal, Cheltenham General) serving ~650,000 residents. Cheltenham General hosts the regional oncology centre, driving a larger-than-average SACT share relative to trust size.",
        "beneficiaries": "~650,000 Gloucestershire residents plus sub-regional oncology referrals (Cheltenham Oncology Centre).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£97.40M"},
            {"label": "Share of trust opex", "value": "~12%"},
            {"label": "Oncology SACT share", "value": "~42% (Cheltenham Oncology Centre)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~65%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, trastuzumab, rituximab, bevacizumab"},
            {"label": "Respiratory biologics share", "value": "Material (regional severe-asthma hub)"},
            {"label": "YoY growth", "value": "~+8%"},
            {"label": "Pharmacy WTE", "value": "~130"},
            {"label": "Procurement framework", "value": "SW Pharmacy Procurement + CMU"}
        ],
        "notes": "Cheltenham Oncology Centre lifts drugs-to-opex ratio above acute-trust average. 2024-25 growth from adjuvant IO combinations (pembrolizumab/atezolizumab), HER2+ breast extensions and new lung TAs. Bevacizumab biosimilar (Q3 2024) saved ~£1.5M in-year. Severe asthma pathway (benralizumab/mepolizumab/dupilumab) consistently grows ~10%+. GLP-1 (Wegovy) weight-management rollout largely community-commissioned in Gloucestershire ICB, not trust line.",
        "sources": [
            {"publisher": "Gloucestershire Hospitals NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.gloshospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NICE", "title": "TA published list", "url": "https://www.nice.org.uk/guidance/published?ngt=Technology%20appraisal%20guidance"}
        ],
        "related": ["Gloucestershire Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Gloucestershire Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "Drug expenditure for ESNEFT, a two-hospital trust (Ipswich, Colchester) plus community services serving ~1M residents across east Suffolk and north Essex. Colchester hosts a regional cancer centre; Ipswich the stroke unit and acute medicine base.",
        "beneficiaries": "~1M east-Suffolk / north-Essex residents including integrated community services.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£92.84M"},
            {"label": "Share of trust opex", "value": "~9%"},
            {"label": "Oncology SACT share", "value": "~36% (Colchester Cancer Centre)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~62%"},
            {"label": "Biosimilar penetration", "value": "adalimumab >95%, infliximab, rituximab, trastuzumab"},
            {"label": "Stroke thrombolysis / anticoagulation", "value": "Material line (Ipswich hyper-acute stroke)"},
            {"label": "YoY growth", "value": "~+7%"},
            {"label": "Pharmacy WTE", "value": "~140 across two sites"},
            {"label": "Procurement framework", "value": "EoE Pharmacy Procurement + CMU"}
        ],
        "notes": "Colchester SACT unit drives outpatient IO/CDK4/6 growth. Ipswich hyper-acute stroke unit consumes alteplase/tenecteplase and regular DOAC/anticoagulation volume. Community integration (community nursing, hospital-at-home) repatriates some homecare medicines bill. Industrial action (2023-24) deferred some elective chemo into 2024-25. GLP-1 diabetes volumes normalised through year.",
        "sources": [
            {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.esneft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "Sentinel Stroke National Audit Programme", "title": "SSNAP Annual Report", "url": "https://www.strokeaudit.org/results/Clinical-audit/National-Results.aspx"}
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Clinical Supplies & Drugs — East Suffolk and North Essex NHS Foundation Trust"]
    },
    "Drugs costs — University Hospitals Coventry And Warwickshire NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
        "description": "Drug expenditure for UHCW, a two-site teaching trust (University Hospital Coventry, Hospital of St Cross Rugby) serving ~1M Coventry & Warwickshire residents. Regional renal transplant centre (Coventry), Arden Cancer Centre, and a busy stem-cell transplant programme shape spend.",
        "beneficiaries": "~1M Coventry & Warwickshire residents; regional renal transplant, haematology SCT cohorts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£82.38M"},
            {"label": "Share of trust opex", "value": "~9%"},
            {"label": "Oncology + haematology share", "value": "~40% (Arden Cancer Centre + SCT)"},
            {"label": "Renal transplant drugs", "value": "Material – ~120 transplants/yr"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~63%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab, bevacizumab"},
            {"label": "YoY growth", "value": "~+8%"},
            {"label": "Pharmacy WTE", "value": "~150"},
            {"label": "Procurement framework", "value": "West Midlands Pharmacy Procurement + CMU"}
        ],
        "notes": "Allogeneic and autologous SCT activity supports consistent antifungal (isavuconazole/posaconazole) and anti-viral (letermovir) spend. Arden Cancer Centre driving double-digit growth on adjuvant checkpoint inhibitors. Renal transplant immunosuppression stable but impacted by basiliximab/belatacept pathway variation. Industrial action rippled into 2024-25 via deferred chemo. GLP-1 normalised H2 2024-25.",
        "sources": [
            {"publisher": "University Hospitals Coventry and Warwickshire NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.uhcw.nhs.uk/about-us/trust-documents/"},
            {"publisher": "NHS Blood and Transplant", "title": "Renal transplant activity 2023-24", "url": "https://www.odt.nhs.uk/statistics-and-reports/annual-activity-report/"},
            {"publisher": "NHS England", "title": "Specialised Commissioning – HCDs", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/"}
        ],
        "related": ["University Hospitals Coventry And Warwickshire NHS Trust", "Clinical Supplies & Drugs — University Hospitals Coventry And Warwickshire NHS Trust"]
    },
    "Drugs costs — Lancashire Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Lancashire Teaching Hospitals NHS Foundation Trust"}],
        "description": "Drug expenditure for LTHTr, a two-site teaching trust (Royal Preston, Chorley & South Ribble) serving ~390,000 local plus ~1.5M tertiary Lancashire & South Cumbria residents. Royal Preston hosts the Rosemere Cancer Centre, Lancashire Major Trauma Centre and the regional neurosciences unit.",
        "beneficiaries": "Local ~390k plus ~1.5M tertiary Lancashire & South Cumbria residents (neurosciences, oncology, major trauma).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£75.06M"},
            {"label": "Share of trust opex", "value": "~10%"},
            {"label": "Oncology SACT share", "value": "~40% (Rosemere Cancer Centre)"},
            {"label": "Neurology DMT share", "value": "~9% (regional MS service)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~64%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab, bevacizumab"},
            {"label": "YoY growth", "value": "~+8%"},
            {"label": "Pharmacy WTE", "value": "~130"},
            {"label": "Procurement framework", "value": "NW Pharmacy Procurement + CMU"}
        ],
        "notes": "Rosemere Cancer Centre widening treatment of adjuvant IO (pembrolizumab, atezolizumab) and CDK4/6 drives oncology line. Regional neurosciences lifts MS DMTs (ocrelizumab, cladribine) and epilepsy new agents (cenobamate). Major Trauma Centre uses high volumes of prothrombin complex concentrates and tranexamic acid. Industrial action backlog impact most visible Q4 2023-24 / Q1 2024-25. GLP-1 diabetes supply normalised mid-year.",
        "sources": [
            {"publisher": "Lancashire Teaching Hospitals NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.lancsteachinghospitals.nhs.uk/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NICE", "title": "MS DMT guidance", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/neurological-conditions/multiple-sclerosis"}
        ],
        "related": ["Lancashire Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Lancashire Teaching Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — York and Scarborough Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
        "description": "Drug expenditure for YSTHFT, a multi-site acute trust (York, Scarborough plus Bridlington, Malton, Selby) serving ~800,000 North Yorkshire residents. Rural geography with long supply chains; Scarborough serves coastal catchment requiring robust formulary distribution.",
        "beneficiaries": "~800,000 North Yorkshire residents including coastal Scarborough/Whitby and rural communities.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£72.89M"},
            {"label": "Share of trust opex", "value": "~8%"},
            {"label": "Oncology share", "value": "~32% (links to Leeds Cancer Centre)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~58%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab, bevacizumab"},
            {"label": "Geriatric medicines share", "value": "Elevated due to older demographic"},
            {"label": "YoY growth", "value": "~+6%"},
            {"label": "Pharmacy WTE", "value": "~110 across sites"},
            {"label": "Procurement framework", "value": "Yorkshire Pharmacy Procurement + CMU"}
        ],
        "notes": "Rural, older-skewed population elevates polypharmacy and community respiratory/COPD drug spend. Some complex SACT referred to Leeds Cancer Centre, limiting local HCD growth. Scarborough pharmacy manages coastal distribution; 2024-25 ePMA roll-out improving adherence/waste control. Industrial action disproportionately affected Scarborough workforce. GLP-1 diabetes normalised H2 2024-25.",
        "sources": [
            {"publisher": "York and Scarborough Teaching Hospitals NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.yorkhospitals.nhs.uk/about-us/publications-performance-and-membership/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NHS Digital", "title": "Prescribing Cost Analysis", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis"}
        ],
        "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — York and Scarborough Teaching Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — Royal Berkshire NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Royal Berkshire NHS Foundation Trust"}],
        "description": "Drug expenditure for RBFT, a single-site acute DGH in Reading serving ~500,000 Berkshire residents. Host of a significant oncology day-case unit, regional vascular service and a growing ambulatory care hub; busy IVF service also contributes fertility-drug volume.",
        "beneficiaries": "~500,000 Berkshire (Reading, Wokingham, West Berks, South Oxon) residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£65.23M"},
            {"label": "Share of trust opex", "value": "~10%"},
            {"label": "Oncology SACT share", "value": "~38%"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~62%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab, bevacizumab"},
            {"label": "Fertility drugs (IVF)", "value": "Modest line - Berkshire NHS IVF pathway"},
            {"label": "YoY growth", "value": "~+8%"},
            {"label": "Pharmacy WTE", "value": "~100"},
            {"label": "Procurement framework", "value": "NHS South Central Pharmacy Procurement + CMU"}
        ],
        "notes": "Oncology growth from adjuvant IO, HER2+ extensions and CDK4/6. Vascular service drives DOAC/antiplatelet regimens. Trust exploring site redevelopment for new hospital (business case); aseptic compounding capacity a live design issue. Industrial action deferred some elective activity 2023-24. GLP-1 diabetes normalised H2 2024-25; weight-management Wegovy path commissioned via Berks West ICB.",
        "sources": [
            {"publisher": "Royal Berkshire NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.royalberkshire.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NICE", "title": "Technology appraisals – oncology", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/cancer"}
        ],
        "related": ["Royal Berkshire NHS Foundation Trust", "Clinical Supplies & Drugs — Royal Berkshire NHS Foundation Trust"]
    },
    "Drugs costs — East Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "East Sussex Healthcare NHS Trust"}],
        "description": "Drug expenditure for ESHT, a combined acute / community trust with two main hospitals (Conquest Hastings, Eastbourne DGH) plus community services. Serves ~525,000 residents of East Sussex — older demographic with high respiratory, cardiovascular and oncology demand.",
        "beneficiaries": "~525,000 East Sussex residents; integrated community and acute services.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£60.68M"},
            {"label": "Share of trust opex", "value": "~9%"},
            {"label": "Oncology SACT share", "value": "~34%"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~60%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab, bevacizumab"},
            {"label": "Respiratory/COPD spend", "value": "Elevated – older demography"},
            {"label": "YoY growth", "value": "~+7%"},
            {"label": "Pharmacy WTE", "value": "~90 across two sites"},
            {"label": "Procurement framework", "value": "South Coast Pharmacy Procurement + CMU"}
        ],
        "notes": "Older demographic drives higher-than-average anticoagulant, anti-dementia and respiratory-inhaler spend. Oncology day-units at both Conquest and Eastbourne deliver adjuvant regimens locally; complex cases referred to Brighton. Wound-care and district-nurse-administered drug costs visible in community line. Industrial-action impact moderate. GLP-1 diabetes stabilised late 2024-25.",
        "sources": [
            {"publisher": "East Sussex Healthcare NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.esht.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Digital", "title": "Prescribing Cost Analysis", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"}
        ],
        "related": ["East Sussex Healthcare NHS Trust", "Clinical Supplies & Drugs — East Sussex Healthcare NHS Trust"]
    },
    "Drugs costs — Royal United Hospitals Bath NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Royal United Hospitals Bath NHS Foundation Trust"}],
        "description": "Drug expenditure for RUH Bath, a single-site acute DGH serving ~500,000 BANES and north-east Somerset residents. Hosts the regional Royal National Hospital for Rheumatic Diseases (RNHRD) and dedicated oncology/haematology day-unit; rheumatology biologics and axial spondyloarthritis pathways are disproportionately material.",
        "beneficiaries": "~500,000 BANES / NE Somerset / W Wiltshire residents plus national RNHRD rheumatology referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£56.10M"},
            {"label": "Share of trust opex", "value": "~10%"},
            {"label": "Rheumatology biologics share", "value": "Elevated – RNHRD legacy service"},
            {"label": "Oncology SACT share", "value": "~30%"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~58%"},
            {"label": "Biosimilar penetration", "value": "adalimumab >95%, infliximab >90%, rituximab, trastuzumab"},
            {"label": "YoY growth", "value": "~+7%"},
            {"label": "Pharmacy WTE", "value": "~90"},
            {"label": "Procurement framework", "value": "SW Pharmacy Procurement + CMU"}
        ],
        "notes": "RNHRD integration (moved into RUH 2019) gives rheumatology an outsized biologics footprint — JAK inhibitors (upadacitinib, tofacitinib, baricitinib) and IL-17/IL-23 inhibitors (secukinumab, risankizumab) grow year-on-year. Adalimumab biosimilar switching near-complete. Oncology day-unit adjuvant IO and breast CDK4/6. Industrial action deferred some elective chemo into 2024-25. GLP-1 diabetes normalised mid-year.",
        "sources": [
            {"publisher": "Royal United Hospitals Bath NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.ruh.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NICE", "title": "Rheumatology TAs", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/musculoskeletal-conditions/arthritis"}
        ],
        "related": ["Royal United Hospitals Bath NHS Foundation Trust", "Clinical Supplies & Drugs — Royal United Hospitals Bath NHS Foundation Trust"]
    },
    "Drugs costs — County Durham and Darlington NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "County Durham and Darlington NHS Foundation Trust"}],
        "description": "Drug expenditure for CDDFT, a multi-site acute / community trust (University Hospital of North Durham, Darlington Memorial, Bishop Auckland plus community sites) serving ~650,000 County Durham and Darlington residents. Significant community services footprint including district nursing drug administration.",
        "beneficiaries": "~650,000 County Durham / Darlington residents plus integrated community services.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£53.99M"},
            {"label": "Share of trust opex", "value": "~8%"},
            {"label": "Oncology share", "value": "~30% (links to Newcastle Cancer Centre)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~58%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab"},
            {"label": "Community medicines spend", "value": "Material via community nursing"},
            {"label": "YoY growth", "value": "~+6%"},
            {"label": "Pharmacy WTE", "value": "~100 across sites"},
            {"label": "Procurement framework", "value": "NoE CPC + CMU"}
        ],
        "notes": "Complex SACT often referred to Newcastle or James Cook (South Tees); CDDFT carries adjuvant regimens and supportive care. Community nursing uses material volumes of insulin, anticoagulants and wound-care drugs. Bishop Auckland ambulatory activity and integrated community pharmacist roles reduce admissions but not the drugs line. Industrial action affected elective activity 2023-24. GLP-1 diabetes normalised 2024-25.",
        "sources": [
            {"publisher": "County Durham and Darlington NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.cddft.nhs.uk/about-us/publications.aspx"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NHS Digital", "title": "Prescribing Cost Analysis", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis"}
        ],
        "related": ["County Durham and Darlington NHS Foundation Trust", "Clinical Supplies & Drugs — County Durham and Darlington NHS Foundation Trust"]
    },
    "Drugs costs — Oxford Health NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Oxford Health NHS Foundation Trust"}],
        "description": "Drug expenditure for Oxford Health, a mental health / community / specialist trust serving Oxfordshire, Buckinghamshire and parts of Wiltshire, Swindon & BaNES. Hosts the NHSE-commissioned Highly Specialist Eating Disorders service and national CAMHS work; drug line is disproportionately high among MH trusts due to specialist community / forensic prescribing.",
        "beneficiaries": "~2M Oxfordshire / Buckinghamshire / Swindon / BaNES / Wiltshire residents; specialist forensic, CAMHS, eating disorders cohorts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£52.06M"},
            {"label": "Share of trust opex", "value": "~8-9% (unusually high for an MH trust)"},
            {"label": "Clozapine service", "value": "Material monitoring-and-supply volume"},
            {"label": "LAI antipsychotics share", "value": "Growing (paliperidone palmitate, aripiprazole LAI)"},
            {"label": "Dementia drugs", "value": "Donepezil, memantine recurring"},
            {"label": "Forensic/secure services drug line", "value": "Elevated (high-complexity caseload)"},
            {"label": "YoY growth", "value": "~+5%"},
            {"label": "Pharmacy WTE", "value": "~70"},
            {"label": "Procurement framework", "value": "NHS South Central Pharmacy Procurement + CMU"}
        ],
        "notes": "Elevated MH-trust drug spend reflects forensic inpatient units (Littlemore, Thames House), complex clozapine caseload, CAMHS prescribing and inclusion of community physical-health prescribing in integrated teams. Long-acting injectable antipsychotics adoption rising with 6-monthly paliperidone. Children's sleep/ADHD lines (melatonin, lisdexamfetamine, guanfacine) grew double-digit. VPAG rebate applies to few MH-relevant branded drugs; GLP-1 weight-management rollout affects MH metabolic-monitoring pathway only indirectly.",
        "sources": [
            {"publisher": "Oxford Health NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.oxfordhealth.nhs.uk/about-us/corporate/annual-report/"},
            {"publisher": "NICE", "title": "Mental health TAs and guidelines", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/mental-health-and-behavioural-conditions"},
            {"publisher": "NHS England", "title": "Specialised mental health commissioning", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/mental-health-group-c/"}
        ],
        "related": ["Oxford Health NHS Foundation Trust", "Clinical Supplies & Drugs — Oxford Health NHS Foundation Trust"]
    },
    "Drugs costs — The Dudley Group NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Dudley Group NHS Foundation Trust"}],
        "description": "Drug expenditure for Dudley Group, a mainly single-site acute trust (Russells Hall, plus Corbett Outpatients and Guest Hospital) serving ~450,000 Dudley borough and surrounding Black Country residents. Complex oncology referred into University Hospitals Birmingham; local SACT day-unit handles adjuvant and mid-complexity regimens.",
        "beneficiaries": "~450,000 Dudley and Black Country residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£47.26M"},
            {"label": "Share of trust opex", "value": "~9%"},
            {"label": "Oncology SACT share", "value": "~30%"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~58%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab, bevacizumab"},
            {"label": "Diabetes / metabolic share", "value": "Material (high local prevalence)"},
            {"label": "YoY growth", "value": "~+7%"},
            {"label": "Pharmacy WTE", "value": "~80"},
            {"label": "Procurement framework", "value": "West Midlands Pharmacy Procurement + CMU"}
        ],
        "notes": "High local diabetes prevalence and deprivation skews spend toward GLP-1, SGLT-2 and insulins; 2023-24 semaglutide/ozempic shortages created supply challenges which eased 2024-25. Adjuvant IO (pembrolizumab) and HER2 pathway growth via Black Country cancer alliance. Industrial-action impact moderate; recovery plan delivered by Q3 2024-25.",
        "sources": [
            {"publisher": "The Dudley Group NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://dgft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NHS Digital", "title": "Prescribing Cost Analysis", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis"}
        ],
        "related": ["The Dudley Group NHS Foundation Trust", "Clinical Supplies & Drugs — The Dudley Group NHS Foundation Trust"]
    },
    "Drugs costs — Sandwell And West Birmingham Hospitals NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Sandwell And West Birmingham Hospitals NHS Trust"}],
        "description": "Drug expenditure for SWBH, an acute trust (Sandwell General, City Hospital, new Midland Metropolitan University Hospital opened 2024) serving ~530,000 Sandwell and west-Birmingham residents in a highly deprived catchment. Opening of the Midland Met in late 2024 reconfigured acute pathways.",
        "beneficiaries": "~530,000 Sandwell and west-Birmingham residents with high deprivation and diabetes prevalence.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£42.89M"},
            {"label": "Share of trust opex", "value": "~7%"},
            {"label": "Oncology share", "value": "~26% (complex tertiary referred to UHB/QEHB)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~55%"},
            {"label": "Diabetes/metabolic drugs", "value": "Elevated (T2DM prevalence)"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab"},
            {"label": "YoY growth", "value": "~+7%"},
            {"label": "Pharmacy WTE", "value": "~90 now consolidated at Midland Met"},
            {"label": "Procurement framework", "value": "West Midlands Pharmacy Procurement + CMU"}
        ],
        "notes": "Midland Metropolitan University Hospital opening (late 2024) consolidated services from Sandwell and City — aseptic unit rationalised to single site, expected medium-term savings on unit-dose manufacture. High diabetes/CKD prevalence drives SGLT-2, GLP-1 and iron/ESA spend. Complex oncology referred to UHB reducing HCD footprint relative to population. Industrial action layered onto move preparation.",
        "sources": [
            {"publisher": "Sandwell and West Birmingham Hospitals NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.swbh.nhs.uk/about-us/publications-and-reports/"},
            {"publisher": "NHS England", "title": "Midland Metropolitan University Hospital opening 2024", "url": "https://www.england.nhs.uk/2024/10/midland-metropolitan-university-hospital-opens/"},
            {"publisher": "NHS Digital", "title": "Prescribing Cost Analysis", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis"}
        ],
        "related": ["Sandwell And West Birmingham Hospitals NHS Trust", "Clinical Supplies & Drugs — Sandwell And West Birmingham Hospitals NHS Trust"]
    },
    "Drugs costs — Northampton General Hospital NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Northampton General Hospital NHS Trust"}],
        "description": "Drug expenditure for NGH, a single-site acute DGH serving ~380,000 Northampton and south-Northamptonshire residents. Hosts the Northamptonshire Cancer Centre providing SACT and radiotherapy for the county; operates a group model with Kettering General Hospital.",
        "beneficiaries": "~380,000 Northampton and south-Northants residents plus county oncology referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£40.20M"},
            {"label": "Share of trust opex", "value": "~9%"},
            {"label": "Oncology SACT share", "value": "~38% (Northamptonshire Cancer Centre)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~62%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab, bevacizumab"},
            {"label": "Group-model procurement with KGH", "value": "Shared chief pharmacist function"},
            {"label": "YoY growth", "value": "~+8%"},
            {"label": "Pharmacy WTE", "value": "~80"},
            {"label": "Procurement framework", "value": "EoE Pharmacy Procurement + CMU"}
        ],
        "notes": "Northamptonshire Cancer Centre concentrates HCD spend — adjuvant IO, CDK4/6 and new lung TAs dominate growth. Group model with Kettering enables joint formulary and shared aseptic workload. Bevacizumab biosimilar savings realised from Q3 2024. Industrial action (2023-24) deferred elective chemo volume. GLP-1 diabetes normalised late 2024-25.",
        "sources": [
            {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.northamptongeneral.nhs.uk/AboutUs/CorporatePublications/AnnualReport/AnnualReport.aspx"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "University Hospitals of Northamptonshire Group", "title": "Group plan", "url": "https://www.uhn-group.nhs.uk/"}
        ],
        "related": ["Northampton General Hospital NHS Trust", "Clinical Supplies & Drugs — Northampton General Hospital NHS Trust"]
    },
    "Drugs costs — Northern Lincolnshire and Goole NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Northern Lincolnshire and Goole NHS Foundation Trust"}],
        "description": "Drug expenditure for NLaG, a multi-site acute trust (Diana Princess of Wales Grimsby, Scunthorpe General, Goole) serving ~400,000 northern-Lincolnshire residents. Operates a group model with Hull University Teaching Hospitals; complex SACT is referred to Hull Queen's Centre.",
        "beneficiaries": "~400,000 northern-Lincolnshire / east-Yorkshire residents including rural Goole catchment.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£37.95M"},
            {"label": "Share of trust opex", "value": "~8%"},
            {"label": "Oncology share", "value": "~28% (complex cases to Hull Queen's Centre)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~55%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab"},
            {"label": "Group model with HUTH", "value": "Shared formulary under Humber Acute Services"},
            {"label": "YoY growth", "value": "~+6%"},
            {"label": "Pharmacy WTE", "value": "~80 across three sites"},
            {"label": "Procurement framework", "value": "Yorkshire Pharmacy Procurement + CMU"}
        ],
        "notes": "Rural, coastal catchment with older demography drives higher inhaler / DOAC / diabetes drug volumes. Complex SACT mostly delivered at Hull Queen's Centre so HCD footprint relatively modest. Group-model formulary with Hull enables shared procurement leverage. Industrial action exacerbated pre-existing workforce constraints; backlog recovery ongoing. GLP-1 diabetes normalised late 2024-25.",
        "sources": [
            {"publisher": "Northern Lincolnshire and Goole NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.nlg.nhs.uk/about/corporate-documents/annual-reports/"},
            {"publisher": "NHS England", "title": "Humber Acute Services Review", "url": "https://humberandnorthyorkshire.org.uk/our-work/humber-acute-services-review/"},
            {"publisher": "NHS Digital", "title": "Prescribing Cost Analysis", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis"}
        ],
        "related": ["Northern Lincolnshire and Goole NHS Foundation Trust", "Clinical Supplies & Drugs — Northern Lincolnshire and Goole NHS Foundation Trust"]
    },
    "Drugs costs — Sheffield Children's NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Sheffield Children's NHS Foundation Trust"}],
        "description": "Drug expenditure for Sheffield Children's, a specialist paediatric trust providing regional acute paediatrics, national specialised services (paediatric neurology, metabolic, bone & joint surgery) plus CAMHS and community. HCD line weighted to paediatric oncology, rare-disease enzyme replacement therapies and paediatric biologics.",
        "beneficiaries": "Sheffield city children plus national/regional specialist paediatric referrals (metabolic, neurology, bone/joint).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning (paediatric HCDs) · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£34.12M"},
            {"label": "Share of trust opex", "value": "~14% (unusually high for paediatric-only trust)"},
            {"label": "Paediatric oncology / haemato-oncology share", "value": "~35%"},
            {"label": "Rare-disease / ERT share", "value": "Material (Batten, MPS, Pompe, SMA nusinersen/onasemnogene)"},
            {"label": "HCDs NHSE-commissioned", "value": "~75% (paediatric specialised)"},
            {"label": "Paediatric biologics (IBD, JIA, asthma)", "value": "Growing adalimumab / tocilizumab / mepolizumab"},
            {"label": "YoY growth", "value": "~+9%"},
            {"label": "Pharmacy WTE", "value": "~60"},
            {"label": "Procurement framework", "value": "Yorkshire Pharmacy Procurement + CMU"}
        ],
        "notes": "Paediatric ATMPs (Zolgensma/onasemnogene, Kymriah/tisagenlecleucel) and enzyme-replacement therapies (alglucosidase alfa, velaglucerase) drive disproportionately high drugs-to-opex ratio. Most funded via NHSE Specialised Commissioning pass-through. 2024-25 includes voretigene neparvovec (ophthalmic gene therapy) referrals. Industrial action less impactful given paediatric urgent pathways. GLP-1 not material; paediatric obesity pathway separate.",
        "sources": [
            {"publisher": "Sheffield Children's NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.sheffieldchildrens.nhs.uk/about-us/annual-reports-and-accounts/"},
            {"publisher": "NHS England", "title": "Highly Specialised Services – paediatrics", "url": "https://www.england.nhs.uk/commissioning/highly-spec-services/"},
            {"publisher": "NICE", "title": "Highly Specialised Technologies", "url": "https://www.nice.org.uk/about/what-we-do/our-programmes/nice-guidance/nice-highly-specialised-technologies-guidance"}
        ],
        "related": ["Sheffield Children's NHS Foundation Trust", "Clinical Supplies & Drugs — Sheffield Children's NHS Foundation Trust"]
    },
    "Drugs costs — Wrightington, Wigan and Leigh NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Wrightington, Wigan and Leigh NHS Foundation Trust"}],
        "description": "Drug expenditure for WWL, a three-site acute trust (Royal Albert Edward Infirmary Wigan, Leigh Infirmary, Wrightington Hospital) serving ~320,000 Wigan borough residents. Wrightington is a nationally recognised elective orthopaedic centre; Wigan provides acute/emergency and a modest SACT unit.",
        "beneficiaries": "~320,000 Wigan borough residents plus national Wrightington orthopaedic elective referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£31.66M"},
            {"label": "Share of trust opex", "value": "~8%"},
            {"label": "Oncology share", "value": "~25% (most complex to Christie)"},
            {"label": "Orthopaedic VTE prophylaxis", "value": "Material – Wrightington high elective volume"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~50%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab"},
            {"label": "YoY growth", "value": "~+6%"},
            {"label": "Pharmacy WTE", "value": "~60"},
            {"label": "Procurement framework", "value": "NW Pharmacy Procurement + CMU"}
        ],
        "notes": "Wrightington's elective-orthopaedics profile (hip/knee historic centre) means disproportionate anticoagulant / VTE-prophylaxis and periprosthetic antibiotic spend. Complex oncology routed to The Christie so HCD footprint lower than peer-size trusts. Industrial action less disruptive for the elective-heavy site (consultant resilience). GLP-1 diabetes pathway stabilised.",
        "sources": [
            {"publisher": "Wrightington, Wigan and Leigh NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.wwl.nhs.uk/annual-report-and-accounts"},
            {"publisher": "National Joint Registry", "title": "Annual Report 2024", "url": "https://www.njrcentre.org.uk/njr-annual-report/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"}
        ],
        "related": ["Wrightington, Wigan and Leigh NHS Foundation Trust", "Clinical Supplies & Drugs — Wrightington, Wigan and Leigh NHS Foundation Trust"]
    },
    "Drugs costs — The Walton Centre NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Walton Centre NHS Foundation Trust"}],
        "description": "Drug expenditure for The Walton Centre, England's only dedicated neurology & neurosurgery specialist trust (Liverpool), serving ~3.5M Cheshire, Merseyside, Lancashire, Isle of Man & North Wales population. Spend heavily weighted to MS DMTs, neuromuscular (SMA/DMD) agents, migraine CGRP inhibitors and epilepsy new molecules.",
        "beneficiaries": "~3.5M north-west & North Wales neurology/neurosurgery catchment; tertiary referrals UK-wide.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning (neurosciences HCDs) · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£29.97M"},
            {"label": "Share of trust opex", "value": "~15% (elevated – specialist neurosciences)"},
            {"label": "MS DMT share", "value": "~35% (ocrelizumab, natalizumab, cladribine, ofatumumab)"},
            {"label": "SMA / neuromuscular share", "value": "Material (nusinersen, risdiplam)"},
            {"label": "HCDs NHSE-commissioned", "value": "~80% (neurosciences pass-through)"},
            {"label": "Migraine CGRP biologics share", "value": "Growing (fremanezumab, galcanezumab, erenumab)"},
            {"label": "Epilepsy new agents", "value": "Cenobamate, brivaracetam, perampanel"},
            {"label": "YoY growth", "value": "~+10%"},
            {"label": "Pharmacy WTE", "value": "~35"}
        ],
        "notes": "As a mono-specialty neurosciences trust Walton's drug line is disproportionately large and HCD-dominated. MS DMT pipeline (ocrelizumab, ofatumumab sub-cut, cladribine, natalizumab including biosimilar entry Q4 2024-25) and SMA therapies (nusinersen quarterly, risdiplam daily oral) drive ongoing ~10% growth. Epilepsy new molecules (cenobamate) rolling out post-NICE TA. Industrial action moderate impact given elective/specialist model. VPAG rebate mostly credited centrally (DHSC).",
        "sources": [
            {"publisher": "The Walton Centre NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.thewaltoncentre.nhs.uk/62/publications.html"},
            {"publisher": "NHS England", "title": "Specialised Commissioning – Neurosciences", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d04/"},
            {"publisher": "NICE", "title": "MS DMT and neuromuscular TAs", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/neurological-conditions"}
        ],
        "related": ["The Walton Centre NHS Foundation Trust", "Clinical Supplies & Drugs — The Walton Centre NHS Foundation Trust"]
    },
    "Drugs costs — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "Drug expenditure for ASPH, a two-site acute DGH (Ashford, St Peter's Chertsey) serving ~410,000 north-west Surrey residents. Offers SACT at St Peter's, the regional bariatric surgery service and the trust-wide maternity hub at Chertsey.",
        "beneficiaries": "~410,000 north-west Surrey residents plus regional bariatric referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£29.01M"},
            {"label": "Share of trust opex", "value": "~7%"},
            {"label": "Oncology SACT share", "value": "~28% (complex cases to Royal Surrey / Royal Marsden)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~56%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab"},
            {"label": "Bariatric / metabolic drug pathway", "value": "Material line"},
            {"label": "YoY growth", "value": "~+6%"},
            {"label": "Pharmacy WTE", "value": "~60"},
            {"label": "Procurement framework", "value": "NHS London Procurement Partnership + CMU"}
        ],
        "notes": "Proximity to Royal Surrey (Guildford) and Royal Marsden moderates complex-oncology HCD exposure. Bariatric surgery service generates post-op vitamin/mineral prophylaxis volume plus some GLP-1 pre-op pathway spend. Industrial action deferred some elective chemo 2023-24. GLP-1 diabetes/weight-management access constrained by national supply through 2024-25.",
        "sources": [
            {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.ashfordstpeters.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NICE", "title": "Bariatric & obesity guidance", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/diabetes-and-other-endocrinal--nutritional-and-metabolic-conditions/obesity"}
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Ashford and St Peter's Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — Central and North West London NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Central and North West London NHS Foundation Trust"}],
        "description": "Drug expenditure for CNWL, a large mental health / community / addictions trust serving ~2M residents across Westminster, Brent, Harrow, Hillingdon, Kensington & Chelsea, Milton Keynes and parts of Camden. Runs national addictions services and HMP healthcare in several estates; drugs line spans psychiatric, substance-misuse and community physical-health prescribing.",
        "beneficiaries": "~2M residents across central / NW London and Milton Keynes; national addictions and offender-health cohorts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · Misuse of Drugs Act 1971 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£27.76M"},
            {"label": "Share of trust opex", "value": "~4%"},
            {"label": "Addiction / OST line (methadone, buprenorphine)", "value": "Material (national addictions portfolio)"},
            {"label": "Long-acting buprenorphine (Buvidal) share", "value": "Growing – prison and community"},
            {"label": "Clozapine and LAI antipsychotics", "value": "Large recurring volume"},
            {"label": "Offender health prescribing", "value": "Significant (HMP Bronzefield, Brixton and others)"},
            {"label": "YoY growth", "value": "~+5%"},
            {"label": "Pharmacy WTE", "value": "~80"},
            {"label": "Procurement framework", "value": "NHS London Procurement Partnership + CMU"}
        ],
        "notes": "CNWL's mix is atypical: large opioid-substitution therapy (OST) portfolio (methadone oral, buprenorphine s/l, long-acting Buvidal) plus HMP healthcare means addictions and secure-environment prescribing is materially embedded. MH line also covers LAI antipsychotics and clozapine monitoring for severe/enduring caseload. Milton Keynes community services contribute district-nurse administered drugs. VPAG impact limited (few branded MH drugs in scope).",
        "sources": [
            {"publisher": "Central and North West London NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.cnwl.nhs.uk/about-us/publications"},
            {"publisher": "OHID", "title": "Adult substance misuse treatment statistics", "url": "https://www.gov.uk/government/collections/substance-misuse-treatment-for-adults-statistics"},
            {"publisher": "NICE", "title": "Drug misuse and dependence – opioid substitution", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/mental-health-and-behavioural-conditions/drug-misuse"}
        ],
        "related": ["Central and North West London NHS Foundation Trust", "Clinical Supplies & Drugs — Central and North West London NHS Foundation Trust"]
    },
    "Drugs costs — Countess of Chester Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
        "description": "Drug expenditure for COCH, a single-site acute DGH serving ~330,000 Chester, West Cheshire and parts of North Wales residents. Provides SACT day-unit and cross-border (Welsh) oncology flows via contractual agreement; complex cases referred to The Clatterbridge Cancer Centre.",
        "beneficiaries": "~330,000 west Cheshire residents plus North Wales cross-border flows.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024 · cross-border NHS Wales agreements",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£26.49M"},
            {"label": "Share of trust opex", "value": "~8%"},
            {"label": "Oncology SACT share", "value": "~30% (complex to Clatterbridge)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~55%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab"},
            {"label": "Cross-border (Wales) drug cost share", "value": "Material – recharged via LTA with BCUHB"},
            {"label": "YoY growth", "value": "~+6%"},
            {"label": "Pharmacy WTE", "value": "~60"},
            {"label": "Procurement framework", "value": "NW Pharmacy Procurement + CMU"}
        ],
        "notes": "Cross-border activity with NHS Wales (Betsi Cadwaladr UHB) means some drug cost is recharged via long-term agreements. Complex oncology deferred to adjacent Clatterbridge site. Maternity improvement programme continues post-Lucy Letby / Kirkup Inquiry; medicines-governance reviews in neonatal remain a focus. Industrial action moderate impact. GLP-1 diabetes normalised.",
        "sources": [
            {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.coch.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "Welsh Government / BCUHB", "title": "Cross-border healthcare agreements", "url": "https://bcuhb.nhs.wales/"}
        ],
        "related": ["Countess of Chester Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Countess of Chester Hospital NHS Foundation Trust"]
    },
    "Drugs costs — James Paget University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "James Paget University Hospitals NHS Foundation Trust"}],
        "description": "Drug expenditure for JPUH, a single-site acute DGH in Gorleston serving ~230,000 Great Yarmouth, Waveney and north-east Suffolk residents. Older demographic with significant ophthalmology and cardio-respiratory demand; complex SACT referred to Norfolk & Norwich.",
        "beneficiaries": "~230,000 Great Yarmouth / Waveney / NE Suffolk residents (older demographic).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£25.17M"},
            {"label": "Share of trust opex", "value": "~9%"},
            {"label": "Oncology SACT share", "value": "~26% (complex referred to NNUH)"},
            {"label": "Intravitreal anti-VEGF (AMD/DME)", "value": "Material – ageing population (aflibercept, ranibizumab, biosimilars)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~55%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, ranibizumab, aflibercept biosimilar (Q4 2024)"},
            {"label": "YoY growth", "value": "~+7%"},
            {"label": "Pharmacy WTE", "value": "~50"},
            {"label": "Procurement framework", "value": "EoE Pharmacy Procurement + CMU"}
        ],
        "notes": "Very elderly catchment drives high ophthalmology intravitreal anti-VEGF volume — aflibercept biosimilar entry (Q3-Q4 2024) and ranibizumab biosimilars expected to trim ~£0.8-1.2M in full year. COPD/inhaler spend elevated. Hospital proposed rebuild under New Hospital Programme affects long-term aseptic capacity planning. Industrial action moderate impact. GLP-1 normalised.",
        "sources": [
            {"publisher": "James Paget University Hospitals NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.jpaget.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Commissioning – intravitreal anti-VEGF", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/"},
            {"publisher": "NICE", "title": "AMD / DME TAs", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/eye-conditions"}
        ],
        "related": ["James Paget University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — James Paget University Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — Harrogate and District NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Harrogate and District NHS Foundation Trust"}],
        "description": "Drug expenditure for HDFT, a combined acute / community trust serving ~160,000 Harrogate-district residents plus extensive community services across North Yorkshire and beyond (including the nationally contracted 0-19 children's public health service in several areas). Local SACT day-unit feeds into Leeds Cancer Centre for complex work.",
        "beneficiaries": "~160,000 Harrogate-district residents plus wider North Yorkshire children's/community contracts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£22.67M"},
            {"label": "Share of trust opex", "value": "~6%"},
            {"label": "Oncology share", "value": "~25% (complex to Leeds Cancer Centre)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~50%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab"},
            {"label": "Community medicines (wound care, insulin)", "value": "Material via community nursing"},
            {"label": "YoY growth", "value": "~+5%"},
            {"label": "Pharmacy WTE", "value": "~45"},
            {"label": "Procurement framework", "value": "Yorkshire Pharmacy Procurement + CMU"}
        ],
        "notes": "Smaller-scale acute plus large community footprint means community-nurse-administered drugs and school-based immunisation programmes show up alongside acute SACT. Complex oncology routed to Leeds; HCD share modest. Industrial action less disruptive given elective-moderate mix. Winter viral immunisation and community COPD pathways shape variable seasonal spend.",
        "sources": [
            {"publisher": "Harrogate and District NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.hdft.nhs.uk/about-us/trust-reports/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NHS Digital", "title": "Prescribing Cost Analysis", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis"}
        ],
        "related": ["Harrogate and District NHS Foundation Trust", "Clinical Supplies & Drugs — Harrogate and District NHS Foundation Trust"]
    },
    "Drugs costs — Isle of Wight NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Isle of Wight NHS Trust"}],
        "description": "Drug expenditure for IoW NHS Trust, the UK's only integrated acute / community / mental health / ambulance trust on a single island site (St Mary's, Newport) serving ~140,000 residents plus summer visitors. Cross-Solent logistics add complexity; supply resilience with Solent partner trusts is essential.",
        "beneficiaries": "~140,000 Isle of Wight residents plus seasonal visitors (acute, MH, community and ambulance services).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · Ambulance Services Regulations · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£21.06M"},
            {"label": "Share of trust opex", "value": "~7%"},
            {"label": "Acute + MH + ambulance blended line", "value": "Unique integrated mix"},
            {"label": "Oncology share", "value": "~22% (complex to Portsmouth/Southampton)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~48%"},
            {"label": "Ambulance paramedic drug kit", "value": "Material – geography-driven prehospital stock"},
            {"label": "YoY growth", "value": "~+5%"},
            {"label": "Pharmacy WTE", "value": "~40"},
            {"label": "Procurement framework", "value": "NHS South Central Pharmacy Procurement + CMU"}
        ],
        "notes": "Unique organisational model (acute + MH + community + ambulance) gives a blended drugs line with modest HCD share; complex oncology referred across the Solent. Prehospital/paramedic kit plus island stock-resilience overheads add logistic cost. UHS (Southampton) partnership provides clinical support for advanced therapies. Industrial action disproportionately difficult for single-site island workforce. GLP-1 diabetes normalised late 2024-25.",
        "sources": [
            {"publisher": "Isle of Wight NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.iow.nhs.uk/about-us/publications/annual-reports-and-accounts/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NHSE / Hampshire & IoW ICB", "title": "Integrated care commissioning", "url": "https://www.hantsiowhealthandcare.org.uk/"}
        ],
        "related": ["Isle of Wight NHS Trust", "Clinical Supplies & Drugs — Isle of Wight NHS Trust"]
    },
    "Drugs costs — George Eliot Hospital NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "George Eliot Hospital NHS Trust"}],
        "description": "Drug expenditure for GEH, a single-site acute DGH in Nuneaton serving ~300,000 north-Warwickshire, south-west Leicestershire and north Coventry residents. Provides core acute services with SACT day-unit; complex oncology referred to UHCW (Coventry) or UHB (Birmingham).",
        "beneficiaries": "~300,000 Nuneaton / north-Warwickshire / SW Leicestershire residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£17.92M"},
            {"label": "Share of trust opex", "value": "~7%"},
            {"label": "Oncology SACT share", "value": "~24% (complex to UHCW / UHB)"},
            {"label": "HCDs NHSE/ICB-commissioned", "value": "~50%"},
            {"label": "Biosimilar live switches", "value": "adalimumab, rituximab, trastuzumab"},
            {"label": "Diabetes/CV spend", "value": "Elevated – local prevalence"},
            {"label": "YoY growth", "value": "~+6%"},
            {"label": "Pharmacy WTE", "value": "~40"},
            {"label": "Procurement framework", "value": "West Midlands Pharmacy Procurement + CMU"}
        ],
        "notes": "Small acute footprint with moderate SACT unit; complex HCDs referred to UHCW so oncology share lower than teaching-hospital peers. Local population health drives diabetes, CVD and respiratory-inhaler spend. Industrial action moderate impact. GLP-1 supply challenges affected diabetes 2023-24; rebased 2024-25.",
        "sources": [
            {"publisher": "George Eliot Hospital NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.geh.nhs.uk/about-us/trust-publications/"},
            {"publisher": "NHS England", "title": "National Cost Collection 2023-24", "url": "https://www.england.nhs.uk/costing-in-the-nhs/national-cost-collection/"},
            {"publisher": "NHS Digital", "title": "Prescribing Cost Analysis", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis"}
        ],
        "related": ["George Eliot Hospital NHS Trust", "Clinical Supplies & Drugs — George Eliot Hospital NHS Trust"]
    },
    "Drugs costs — Birmingham Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Birmingham Community Healthcare NHS Foundation Trust"}],
        "description": "Drug expenditure for BCHC, a community trust serving ~1.1M Birmingham residents across community nursing, specialist children's community services, dental and rehabilitation. Drugs line dominated by district-nurse administered injectables, community IV antibiotic / anticoagulant programmes, and specialist paediatric community medicines.",
        "beneficiaries": "~1.1M Birmingham residents; community nursing, specialist children's services, dental, inclusion health.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£11.23M"},
            {"label": "Share of trust opex", "value": "~4%"},
            {"label": "OPAT / community IV antibiotics", "value": "Material line (hospital-at-home schemes)"},
            {"label": "Wound-care dressings / topicals", "value": "Material (district nursing)"},
            {"label": "Paediatric community specialist drugs", "value": "Notable niche line"},
            {"label": "Anticoagulant administration", "value": "Enoxaparin / DOACs in community"},
            {"label": "Dental sedation / local anaesthetics", "value": "Regular run-rate"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Pharmacy WTE", "value": "~25"}
        ],
        "notes": "Community drug spend is structurally lower than acute trusts but highly labour-linked: OPAT, IV iron clinics, community palliative care syringe drivers, and specialist community paediatric prescribing. Growth in hospital-at-home / virtual wards with Birmingham & Solihull ICB shifts some acute-like drug spend into BCHC line. GLP-1 not a community-trust line (primary-care commissioned).",
        "sources": [
            {"publisher": "Birmingham Community Healthcare NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.bhamcommunity.nhs.uk/about-us/corporate-information/"},
            {"publisher": "NHS England", "title": "Virtual wards and hospital-at-home", "url": "https://www.england.nhs.uk/virtual-wards/"},
            {"publisher": "NHS Digital", "title": "Prescribing Cost Analysis", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/prescription-cost-analysis"}
        ],
        "related": ["Birmingham Community Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs — Birmingham Community Healthcare NHS Foundation Trust"]
    },
    "Drugs costs — South London and Maudsley NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "South London and Maudsley NHS Foundation Trust"}],
        "description": "Drug expenditure for SLaM, one of Europe's largest mental health trusts, covering Lambeth, Southwark, Lewisham and Croydon plus national/specialist services (National Psychosis Unit, National Affective Disorders Service, Behavioural & Developmental Psychiatry). Drug line dominated by antipsychotics (clozapine, LAIs), mood stabilisers and specialist pharmacy-led services.",
        "beneficiaries": "~1.3M south-London residents plus national specialist psychosis/affective/neurodevelopmental cohorts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£8.60M"},
            {"label": "Share of trust opex", "value": "~1-1.5%"},
            {"label": "Clozapine service", "value": "Large national-reference cohort at Maudsley"},
            {"label": "LAI antipsychotics", "value": "Growing (paliperidone palmitate 6-month, aripiprazole LAI)"},
            {"label": "Mood stabilisers (lithium, valproate, lamotrigine)", "value": "Recurring"},
            {"label": "ADHD (lisdexamfetamine, guanfacine, atomoxetine)", "value": "Growing – adult ADHD pathway"},
            {"label": "Esketamine (Spravato) service", "value": "NICE-approved TRD pathway – niche but high-unit-cost"},
            {"label": "YoY growth", "value": "~+5%"},
            {"label": "Pharmacy WTE", "value": "~60"}
        ],
        "notes": "MH drug-to-opex ratio low but absolute mix unusual: the Maudsley hosts one of the largest clozapine caseloads globally (plus the Clozapine Handbook/TDM service) and runs specialist esketamine for treatment-resistant depression. Adult ADHD demand and LAI antipsychotic uptake drive growth. Very little VPAG exposure (most MH drugs off-patent). GLP-1 pathway for metabolic monitoring of antipsychotic-induced weight gain growing but commissioned primarily via primary care.",
        "sources": [
            {"publisher": "South London and Maudsley NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://slam.nhs.uk/about-us/our-publications"},
            {"publisher": "NICE", "title": "Psychosis and schizophrenia TAs/guidelines", "url": "https://www.nice.org.uk/guidance/cg178"},
            {"publisher": "NHS England", "title": "Specialised mental health commissioning", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/mental-health-group-c/"}
        ],
        "related": ["South London and Maudsley NHS Foundation Trust", "Clinical Supplies & Drugs — South London and Maudsley NHS Foundation Trust"]
    },
    "Drugs costs — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust"}],
        "description": "Drug expenditure for CNTW, a large north-east mental health / disability / neurorehabilitation trust serving ~1.7M residents across Cumbria, Northumberland, Newcastle, North Tyneside, Gateshead, South Tyneside and Sunderland. Runs secure/forensic, CAMHS, neurorehabilitation and national specialist services.",
        "beneficiaries": "~1.7M North East / Cumbria residents; forensic, neurorehab, CAMHS and specialist MH cohorts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£7.33M"},
            {"label": "Share of trust opex", "value": "~1.5%"},
            {"label": "Forensic/secure inpatient prescribing", "value": "Significant share (high/medium secure)"},
            {"label": "Clozapine caseload", "value": "Large regional"},
            {"label": "LAI antipsychotics", "value": "Growing"},
            {"label": "Neurorehab spasticity (botulinum, baclofen pumps)", "value": "Material niche line"},
            {"label": "CAMHS specialist prescribing", "value": "Growing ADHD / LD pathways"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Pharmacy WTE", "value": "~55"}
        ],
        "notes": "Wide geography (Cumbria to Sunderland) and full range of MH services — including high-secure at Hadrian (partner site) and medium-secure — drive complex polypharmacy. Neurorehabilitation unit uses botulinum toxin for spasticity, baclofen pumps and other specialist agents. CAMHS ADHD demand growing strongly. GLP-1 impact limited (primary-care commissioned).",
        "sources": [
            {"publisher": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.cntw.nhs.uk/about/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Specialised mental health – secure services", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/mental-health-group-c/"},
            {"publisher": "NICE", "title": "Mental health guidance", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/mental-health-and-behavioural-conditions"}
        ],
        "related": ["Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Clinical Supplies & Drugs — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust"]
    },
    "Drugs costs — Mersey Care NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Mersey Care NHS Foundation Trust"}],
        "description": "Drug expenditure for Mersey Care, a large mental health / learning disability / community trust serving Liverpool, Sefton, Knowsley, Warrington and St Helens. Hosts high-secure services at Ashworth Hospital and a broad community mental health / addictions / LD footprint.",
        "beneficiaries": "~1.5M Merseyside / Warrington / St Helens residents; national high-secure forensic cohort (Ashworth).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · Misuse of Drugs Act 1971 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£6.61M"},
            {"label": "Share of trust opex", "value": "~1%"},
            {"label": "Ashworth high-secure share", "value": "Materially elevated – complex forensic polypharmacy"},
            {"label": "Clozapine caseload", "value": "Large regional"},
            {"label": "Addictions / OST (methadone, buprenorphine)", "value": "Material community line"},
            {"label": "LD community drug-optimisation (STOMP programme)", "value": "Active de-prescribing agenda"},
            {"label": "LAI antipsychotics", "value": "Growing"},
            {"label": "YoY growth", "value": "~+3%"},
            {"label": "Pharmacy WTE", "value": "~50"}
        ],
        "notes": "Ashworth (high-secure) hosts one of three UK high-secure hospitals — atypical polypharmacy and higher per-patient drug cost. Addictions portfolio via community contracts adds OST volume. STOMP (stopping over-medication of people with learning disabilities) programme actively reduces LD inpatient antipsychotic burden, partially offsetting growth. VPAG largely immaterial (off-patent MH generics). GLP-1 not material.",
        "sources": [
            {"publisher": "Mersey Care NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.merseycare.nhs.uk/about-us/our-performance/annual-reports-accounts"},
            {"publisher": "NHS England", "title": "STOMP – Stopping Over-Medication of People with Learning Disabilities", "url": "https://www.england.nhs.uk/learning-disabilities/improving-health/stomp/"},
            {"publisher": "OHID", "title": "Adult substance misuse treatment statistics", "url": "https://www.gov.uk/government/collections/substance-misuse-treatment-for-adults-statistics"}
        ],
        "related": ["Mersey Care NHS Foundation Trust", "Clinical Supplies & Drugs — Mersey Care NHS Foundation Trust"]
    },
    "Drugs costs — Sussex Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Sussex Partnership NHS Foundation Trust"}],
        "description": "Drug expenditure for Sussex Partnership, a mental health / LD / CAMHS / forensic trust serving East Sussex, West Sussex and Brighton & Hove plus parts of Hampshire. Runs the regional secure (medium-secure) service and specialist perinatal MH services.",
        "beneficiaries": "~1.7M Sussex (East, West, B&H) residents plus parts of Hampshire; secure and perinatal MH cohorts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£6.00M"},
            {"label": "Share of trust opex", "value": "~1.2%"},
            {"label": "Forensic/secure inpatient share", "value": "Elevated complex polypharmacy"},
            {"label": "Clozapine caseload", "value": "Substantial"},
            {"label": "LAI antipsychotics", "value": "Growing paliperidone/aripiprazole LAI"},
            {"label": "Perinatal MH prescribing", "value": "Sertraline, quetiapine tailored pathway"},
            {"label": "CAMHS ADHD (lisdexamfetamine)", "value": "Double-digit growth"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Pharmacy WTE", "value": "~40"}
        ],
        "notes": "Medium-secure service drives relatively higher per-patient cost. Perinatal MH unit requires carefully formulated prescribing (lactation-safe agents). Adult ADHD titration demand sustained. MH trust GLP-1 impact via metabolic-monitoring pathway for antipsychotic-induced weight gain, mostly commissioned in primary care. VPAG rebate largely non-material given generic MH portfolio.",
        "sources": [
            {"publisher": "Sussex Partnership NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.sussexpartnership.nhs.uk/our-publications"},
            {"publisher": "NHS England", "title": "Specialised mental health – secure services", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/mental-health-group-c/"},
            {"publisher": "NICE", "title": "Antenatal and postnatal mental health", "url": "https://www.nice.org.uk/guidance/cg192"}
        ],
        "related": ["Sussex Partnership NHS Foundation Trust", "Clinical Supplies & Drugs — Sussex Partnership NHS Foundation Trust"]
    },
    "Drugs costs — Black Country Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Black Country Healthcare NHS Foundation Trust"}],
        "description": "Drug expenditure for BCHFT, a mental health / LD / CAMHS trust serving ~1.2M Sandwell, Wolverhampton, Dudley and Walsall residents. Integrated MH provider for the Black Country ICB footprint with growing community MH transformation programme.",
        "beneficiaries": "~1.2M Black Country (Sandwell, Wolverhampton, Dudley, Walsall) residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£4.70M"},
            {"label": "Share of trust opex", "value": "~1%"},
            {"label": "Clozapine monitoring service", "value": "Regional hub"},
            {"label": "LAI antipsychotic share", "value": "Growing"},
            {"label": "ADHD titration demand", "value": "High – rapidly growing"},
            {"label": "Community MH transformation drugs", "value": "Neighbourhood-team prescribing"},
            {"label": "LD STOMP impact", "value": "Ongoing de-prescribing"},
            {"label": "YoY growth", "value": "~+3%"},
            {"label": "Pharmacy WTE", "value": "~25"}
        ],
        "notes": "Newer trust (formed 2020 via merger) with ongoing formulary harmonisation yielding modest savings. High local ADHD demand creates bottleneck on lisdexamfetamine titration (also subject to national supply constraint 2023-24). LD STOMP programme reduces antipsychotic polypharmacy. GLP-1 impact is indirect (metabolic screening in MH pathway).",
        "sources": [
            {"publisher": "Black Country Healthcare NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.blackcountryhealthcare.nhs.uk/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "ADHD medication supply disruption", "url": "https://www.england.nhs.uk/supply-disruption-alerts/"},
            {"publisher": "NICE", "title": "ADHD NG87", "url": "https://www.nice.org.uk/guidance/ng87"}
        ],
        "related": ["Black Country Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs — Black Country Healthcare NHS Foundation Trust"]
    },
    "Drugs costs — Kent Community Health NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Kent Community Health NHS Foundation Trust"}],
        "description": "Drug expenditure for KCHFT, a community trust serving ~1.8M Kent and Medway residents through district nursing, minor injury units, specialist community paediatrics, long-term condition nursing and HMP healthcare. Drugs line is dominated by district-nurse administered injectables, community IV programmes and minor-injury stock.",
        "beneficiaries": "~1.8M Kent and Medway residents; community nursing, specialist paediatrics, MIUs, offender health.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£4.42M"},
            {"label": "Share of trust opex", "value": "~1.3%"},
            {"label": "OPAT / community IV antibiotics", "value": "Material"},
            {"label": "Wound-care consumables adjacency", "value": "Significant community nursing run-rate"},
            {"label": "Anticoagulants (LMWH, DOACs)", "value": "Material (hospital-at-home)"},
            {"label": "Prison healthcare prescribing", "value": "Ten HMPs + OST"},
            {"label": "Virtual wards drug contribution", "value": "Growing"},
            {"label": "YoY growth", "value": "~+5%"},
            {"label": "Pharmacy WTE", "value": "~20"}
        ],
        "notes": "Large HMP healthcare portfolio adds OST (methadone, buprenorphine, long-acting Buvidal) and secure-environment prescribing. Kent & Medway virtual wards partnership increases community IV antibiotic and diuretic therapy volumes. Very low HCD exposure.",
        "sources": [
            {"publisher": "Kent Community Health NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.kentcht.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Virtual wards", "url": "https://www.england.nhs.uk/virtual-wards/"},
            {"publisher": "OHID", "title": "Adult substance misuse treatment statistics", "url": "https://www.gov.uk/government/collections/substance-misuse-treatment-for-adults-statistics"}
        ],
        "related": ["Kent Community Health NHS Foundation Trust", "Clinical Supplies & Drugs — Kent Community Health NHS Foundation Trust"]
    },
    "Drugs costs — Leicestershire Partnership NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Leicestershire Partnership NHS Trust"}],
        "description": "Drug expenditure for LPT, a combined mental health / LD / community trust serving ~1.1M Leicester, Leicestershire & Rutland residents. Runs adult MH, CAMHS, LD, community nursing and specialist community paediatrics.",
        "beneficiaries": "~1.1M Leicester, Leicestershire and Rutland residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£4.20M"},
            {"label": "Share of trust opex", "value": "~0.9%"},
            {"label": "MH antipsychotics (LAIs + clozapine)", "value": "Core line"},
            {"label": "CAMHS ADHD growth", "value": "Double-digit"},
            {"label": "Community nursing medicines (wounds, anticoags)", "value": "Material"},
            {"label": "LD STOMP activity", "value": "Active de-prescribing"},
            {"label": "Perinatal MH prescribing", "value": "Tailored pathway"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Pharmacy WTE", "value": "~25"}
        ],
        "notes": "Combined MH + LD + community footprint makes drug line a blended mix of psychotropics, wound-care / community nursing and CAMHS specialist prescribing. Lisdexamfetamine supply constraints rippled through 2023-24 and early 2024-25. GLP-1 not material at trust; related to metabolic monitoring for SMI.",
        "sources": [
            {"publisher": "Leicestershire Partnership NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.leicspart.nhs.uk/about/corporate-information/"},
            {"publisher": "NHS England", "title": "Community mental health framework", "url": "https://www.england.nhs.uk/mental-health/adults/cmhs/"},
            {"publisher": "NICE", "title": "ADHD NG87", "url": "https://www.nice.org.uk/guidance/ng87"}
        ],
        "related": ["Leicestershire Partnership NHS Trust", "Clinical Supplies & Drugs — Leicestershire Partnership NHS Trust"]
    },
    "Drugs costs — Liverpool Women's NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Liverpool Women's NHS Foundation Trust"}],
        "description": "Drug expenditure for LWFT, a specialist women's / neonatal trust in Liverpool — one of very few dedicated women's hospitals in Europe. Spend weighted to maternity obstetrics, neonatal intensive care (surfactant, caffeine citrate), gynae-oncology and IVF services (Hewitt Fertility Centre).",
        "beneficiaries": "Regional Merseyside/Cheshire obstetric, gynae, neonatal and fertility cohorts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning (neonatal, gynae-onc) · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£3.92M"},
            {"label": "Share of trust opex", "value": "~3%"},
            {"label": "Neonatal intensive care drugs", "value": "Surfactant (poractant), caffeine citrate, ibuprofen IV"},
            {"label": "Obstetric anaesthesia / oxytocics", "value": "Oxytocin, carboprost, misoprostol – core line"},
            {"label": "Gynae-oncology SACT share", "value": "PARP inhibitors (olaparib, niraparib) growing"},
            {"label": "IVF / fertility drugs (Hewitt Centre)", "value": "Gonadotropins – modest trust-billed line"},
            {"label": "HCDs NHSE-commissioned", "value": "~55%"},
            {"label": "YoY growth", "value": "~+6%"},
            {"label": "Pharmacy WTE", "value": "~20"}
        ],
        "notes": "Specialty trust with unusual profile: neonatal intensive-care drugs (surfactant is high-unit-cost), obstetric emergencies (uterotonics, magnesium sulfate, anti-D immunoglobulin) and gynae-oncology (PARP inhibitors) all on one small footprint. CAR-T / rare-disease HCDs absent. Cytotec / oxytocin supply stable through 2024-25. GLP-1 not material. VPAG partial impact on PARPi spend.",
        "sources": [
            {"publisher": "Liverpool Women's NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.liverpoolwomens.nhs.uk/about-us/corporate-publications/"},
            {"publisher": "NHS England", "title": "Neonatal critical care – specialised commissioning", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-e/e08/"},
            {"publisher": "NICE", "title": "Gynae-oncology TAs (PARPi)", "url": "https://www.nice.org.uk/guidance/conditions-and-diseases/cancer/ovarian-cancer"}
        ],
        "related": ["Liverpool Women's NHS Foundation Trust", "Clinical Supplies & Drugs — Liverpool Women's NHS Foundation Trust"]
    },
    "Drugs costs — Lincolnshire Community Health Services NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Lincolnshire Community Health Services NHS Trust"}],
        "description": "Drug expenditure for LCHS, a community trust serving ~780,000 Lincolnshire residents across district nursing, specialist community nursing (TB, diabetes), urgent treatment centres and children's community services. Large rural geography; MIU/UTC medicine stocks are a key operational element.",
        "beneficiaries": "~780,000 Lincolnshire residents across one of England's largest rural county footprints.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£3.66M"},
            {"label": "Share of trust opex", "value": "~2%"},
            {"label": "UTC/MIU medicines stock", "value": "Dispersed rural sites – logistic overhead"},
            {"label": "District nursing injectables", "value": "LMWH, insulin, palliative"},
            {"label": "Community IV antibiotics (OPAT)", "value": "Growing"},
            {"label": "TB service (RIPE regimen)", "value": "Specialist community line"},
            {"label": "Palliative syringe drivers", "value": "Diamorphine, midazolam, haloperidol, levomepromazine"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Pharmacy WTE", "value": "~15"}
        ],
        "notes": "Rural geography drives disproportionate logistic cost per unit dispensed; multi-site UTC stocks require tight waste control. Palliative community prescribing is a meaningful share. GLP-1 and HCD exposure minimal (primary-care and acute respectively). Community virtual-ward expansion with ULHT adding IV antibiotic and diuretic volumes.",
        "sources": [
            {"publisher": "Lincolnshire Community Health Services NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.lincolnshirecommunityhealthservices.nhs.uk/about-us/corporate-publications"},
            {"publisher": "NHS England", "title": "Virtual wards", "url": "https://www.england.nhs.uk/virtual-wards/"},
            {"publisher": "NICE", "title": "Tuberculosis NG33", "url": "https://www.nice.org.uk/guidance/ng33"}
        ],
        "related": ["Lincolnshire Community Health Services NHS Trust", "Clinical Supplies & Drugs — Lincolnshire Community Health Services NHS Trust"]
    },
    "Drugs costs — Camden and Islington NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Camden and Islington NHS Foundation Trust"}],
        "description": "Drug expenditure for C&I, a mental health / MH community trust serving ~500,000 Camden and Islington residents. In 2024 merged with Barnet, Enfield and Haringey MH Trust to form North London Mental Health Partnership; accounts for 2024-25 reflect the transitional period.",
        "beneficiaries": "~500,000 Camden and Islington residents; transitioning into North London Mental Health Partnership.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£2.79M"},
            {"label": "Share of trust opex", "value": "~1%"},
            {"label": "Clozapine caseload", "value": "Central-London reference cohort"},
            {"label": "LAI antipsychotics share", "value": "Growing (paliperidone 6-monthly)"},
            {"label": "Perinatal MH prescribing", "value": "Specialist pathway (MBU links)"},
            {"label": "ADHD adult titration", "value": "Large growing caseload"},
            {"label": "Mood stabilisers (lithium, valproate, lamotrigine)", "value": "Recurring"},
            {"label": "Merger transition", "value": "Oct 2024 → North London MH Partnership"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Pharmacy WTE", "value": "~18"}
        ],
        "notes": "2024-25 is the transitional year into the North London Mental Health Partnership (formed with BEH-MHT). Formulary harmonisation and merged procurement expected to yield savings in 2025-26 onward. Dense urban MH population with high ADHD and psychosis demand — lisdexamfetamine supply constraint (2023-24) impacted titration waiting times. VPAG/GLP-1 impact minimal.",
        "sources": [
            {"publisher": "Camden and Islington NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.candi.nhs.uk/our-trust/publications-and-reports"},
            {"publisher": "North London Mental Health Partnership", "title": "Partnership information", "url": "https://www.northlondonmentalhealth.nhs.uk/"},
            {"publisher": "NICE", "title": "ADHD NG87", "url": "https://www.nice.org.uk/guidance/ng87"}
        ],
        "related": ["Camden and Islington NHS Foundation Trust", "Clinical Supplies & Drugs — Camden and Islington NHS Foundation Trust"]
    },
    "Drugs costs — Bridgewater Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Bridgewater Community Healthcare NHS Foundation Trust"}],
        "description": "Drug expenditure for Bridgewater Community, a community trust serving ~570,000 residents across Halton, Warrington, St Helens and parts of Trafford. Delivers district nursing, community paediatrics, dental, sexual health and 0-19 services; small but essential drugs line.",
        "beneficiaries": "~570,000 residents across Halton, Warrington, St Helens and Trafford.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£2.42M"},
            {"label": "Share of trust opex", "value": "~1.5%"},
            {"label": "Community IV antibiotics (OPAT)", "value": "Growing via virtual-ward partnership"},
            {"label": "District-nurse injectables (LMWH, insulin)", "value": "Core line"},
            {"label": "Sexual health contraceptives / STI", "value": "Material line (LARC, antivirals)"},
            {"label": "Community dental LA / sedation", "value": "Recurring"},
            {"label": "0-19 immunisations stock", "value": "Managed through programme"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Pharmacy WTE", "value": "~8"}
        ],
        "notes": "Sexual-health service across Halton drives LARC and HIV PrEP/contraception volume. 0-19 children's services stock vaccines via national programme (not all on trust P&L). Small pharmacy function relies on NHSE-framework procurement. HCD exposure nil. GLP-1 not material.",
        "sources": [
            {"publisher": "Bridgewater Community Healthcare NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.bridgewater.nhs.uk/about-us/corporate-publications/"},
            {"publisher": "NHS England", "title": "Virtual wards", "url": "https://www.england.nhs.uk/virtual-wards/"},
            {"publisher": "UKHSA", "title": "Sexual health commissioning guidance", "url": "https://www.gov.uk/government/publications/sexual-and-reproductive-health-services-statutory-guidance"}
        ],
        "related": ["Bridgewater Community Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs — Bridgewater Community Healthcare NHS Foundation Trust"]
    },
    "Drugs costs — South West London and St George's Mental Health NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "South West London and St George's Mental Health NHS Trust"}],
        "description": "Drug expenditure for SWLSTG, a mental health trust serving ~1.1M residents across Kingston, Merton, Richmond, Sutton and Wandsworth. Runs adult MH, CAMHS, eating disorders (Springfield), older adult MH and specialist national service for deafness & mental health.",
        "beneficiaries": "~1.1M SW London residents plus national specialist deaf MH and national eating-disorders cohorts.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£2.35M"},
            {"label": "Share of trust opex", "value": "~0.8%"},
            {"label": "Clozapine caseload", "value": "Large regional"},
            {"label": "LAI antipsychotics share", "value": "Growing"},
            {"label": "CAMHS ADHD growth", "value": "Double-digit"},
            {"label": "Eating disorders (Springfield) prescribing", "value": "Fluoxetine, olanzapine low-dose, re-feeding supplements"},
            {"label": "Older adult MH (dementia agents)", "value": "Donepezil, memantine recurring"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Pharmacy WTE", "value": "~18"}
        ],
        "notes": "Springfield Hospital redevelopment (new unit opened 2023) reshapes logistics but not total drugs bill. Eating-disorders specialist unit generates limited pharmacotherapy spend but disproportionate supplementary-feed line. ADHD titration demand continues to grow. VPAG impact minimal.",
        "sources": [
            {"publisher": "South West London and St George's Mental Health NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.swlstg.nhs.uk/about-us/corporate-information"},
            {"publisher": "NICE", "title": "Eating disorders NG69", "url": "https://www.nice.org.uk/guidance/ng69"},
            {"publisher": "NHS England", "title": "Specialised mental health commissioning", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/mental-health-group-c/"}
        ],
        "related": ["South West London and St George's Mental Health NHS Trust", "Clinical Supplies & Drugs — South West London and St George's Mental Health NHS Trust"]
    },
    "Drugs costs — North West Ambulance Service NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "North West Ambulance Service NHS Trust"}],
        "description": "Drug expenditure for NWAS, the ambulance trust for Cumbria, Lancashire, Greater Manchester, Merseyside & Cheshire serving ~7M residents. Drugs line covers paramedic prehospital kit (analgesia, thrombolysis candidates, cardiac arrest, naloxone, IV fluids) and HART / specialist resources.",
        "beneficiaries": "~7M NW England residents; prehospital emergency care across urban and rural geography.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Ambulance Services Regulations · Human Medicines Regulations 2012 (paramedic exemptions) · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£1.97M"},
            {"label": "Share of trust opex", "value": "~0.4%"},
            {"label": "Paramedic PGD drug portfolio", "value": "Morphine, midazolam, IV tranexamic acid, amiodarone, adrenaline"},
            {"label": "Naloxone (opioid overdose) kits", "value": "Expanded distribution programme"},
            {"label": "IV fluids (0.9% NaCl, Hartmann's)", "value": "Core bulk stock"},
            {"label": "Oxygen (medicinal gas)", "value": "Significant recurring supply"},
            {"label": "HART / specialist unit drugs", "value": "CBRN/HAZMAT reserves"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Procurement framework", "value": "NHS Supply Chain + CMU + AACE"}
        ],
        "notes": "Unusually small drug line relative to trust opex — prehospital stock is dominated by generics (morphine, midazolam, adrenaline) and IV fluids. Naloxone distribution programme (community take-home post-opioid overdose) rising. Supply resilience across a 7M-population footprint drives logistic cost. No HCD or VPAG exposure of note.",
        "sources": [
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.nwas.nhs.uk/about-us/our-publications/"},
            {"publisher": "Association of Ambulance Chief Executives (AACE)", "title": "UK Ambulance Services Clinical Practice Guidelines 2024", "url": "https://aace.org.uk/clinical-practice-guidelines/"},
            {"publisher": "NHS England", "title": "Naloxone – national take-home programme", "url": "https://www.england.nhs.uk/"}
        ],
        "related": ["North West Ambulance Service NHS Trust", "Clinical Supplies & Drugs — North West Ambulance Service NHS Trust"]
    },
    "Drugs costs — East of England Ambulance Service NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "East of England Ambulance Service NHS Trust"}],
        "description": "Drug expenditure for EEAST, the ambulance trust for Bedfordshire, Cambridgeshire, Essex, Hertfordshire, Norfolk and Suffolk serving ~6.2M residents. Drugs line dominated by prehospital paramedic kit, with a mixed rural-urban geography posing stock-distribution and expiry-management challenges.",
        "beneficiaries": "~6.2M East of England residents across mixed urban/rural catchments.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Ambulance Services Regulations · Human Medicines Regulations 2012 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£1.64M"},
            {"label": "Share of trust opex", "value": "~0.3%"},
            {"label": "Paramedic PGD drug portfolio", "value": "Morphine, midazolam, amiodarone, adrenaline, ondansetron"},
            {"label": "IV fluids and crystalloids", "value": "Major bulk line"},
            {"label": "Medicinal oxygen", "value": "Recurring supply"},
            {"label": "Naloxone take-home kits", "value": "Expanded regional programme"},
            {"label": "HART / HEMS drug kits", "value": "Specialist small line"},
            {"label": "YoY growth", "value": "~+4%"},
            {"label": "Procurement framework", "value": "NHS Supply Chain + CMU + AACE"}
        ],
        "notes": "Rural distribution (Norfolk/Suffolk) drives higher logistic cost per unit than urban-dominant peers. Shared HEMS operation (Magpas / EAAA) influences advanced analgesia and RSI drug footprint. No HCDs. Generic-dominated mix insulates from VPAG rebate dynamics.",
        "sources": [
            {"publisher": "East of England Ambulance Service NHS Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.eastamb.nhs.uk/about-us/board-papers-and-publications/"},
            {"publisher": "AACE", "title": "UK Ambulance Services Clinical Practice Guidelines 2024", "url": "https://aace.org.uk/clinical-practice-guidelines/"},
            {"publisher": "NHS England", "title": "Ambulance services commissioning", "url": "https://www.england.nhs.uk/urgent-emergency-care/"}
        ],
        "related": ["East of England Ambulance Service NHS Trust", "Clinical Supplies & Drugs — East of England Ambulance Service NHS Trust"]
    },
    "Drugs costs — Bradford District Care NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Bradford District Care NHS Foundation Trust"}],
        "description": "Drug expenditure for BDCFT, an integrated mental health / community / LD trust serving ~540,000 Bradford District and Craven residents. Provides adult MH, CAMHS, LD, community nursing and a growing perinatal MH service.",
        "beneficiaries": "~540,000 Bradford District and Craven residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · NICE TAs · VPAG 2024",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£1.31M"},
            {"label": "Share of trust opex", "value": "~0.6%"},
            {"label": "Clozapine caseload", "value": "Meaningful local cohort"},
            {"label": "LAI antipsychotic growth", "value": "Moderate"},
            {"label": "ADHD titration demand", "value": "Growing; supply constraints eased 2024-25"},
            {"label": "Community IV antibiotics (OPAT)", "value": "Growing via virtual-ward partnership"},
            {"label": "Perinatal MH pathway", "value": "Tailored prescribing"},
            {"label": "YoY growth", "value": "~+3%"},
            {"label": "Pharmacy WTE", "value": "~12"}
        ],
        "notes": "Small integrated trust with blended drug line across MH, LD and community. Perinatal MH service growing (Bradford District has one of the highest birth-rates in the region). Virtual-ward partnership with Bradford Teaching Hospitals adds community IV antibiotic and diuretic volume. HCD and VPAG exposure minimal.",
        "sources": [
            {"publisher": "Bradford District Care NHS Foundation Trust", "title": "Annual Report & Accounts 2024-25", "url": "https://www.bdct.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Community mental health framework", "url": "https://www.england.nhs.uk/mental-health/adults/cmhs/"},
            {"publisher": "NICE", "title": "Antenatal and postnatal mental health CG192", "url": "https://www.nice.org.uk/guidance/cg192"}
        ],
        "related": ["Bradford District Care NHS Foundation Trust", "Clinical Supplies & Drugs — Bradford District Care NHS Foundation Trust"]
    }
}
