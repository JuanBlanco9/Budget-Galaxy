# Hand-curated Tier A depth-4 enrichment for NHS trust "Drugs costs" sub-lines (slice C).
# 48 trusts. Keys use em-dash U+2014 with spaces: "Drugs costs — <trust>".

NEW = {
    "Drugs costs — The Leeds Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Leeds Teaching Hospitals NHS Trust"}],
        "description": "Drug spend across Leeds Teaching Hospitals' seven-hospital footprint — St James's (Europe's largest single-site teaching hospital) plus Leeds General Infirmary — where haemato-oncology, solid-tumour chemotherapy, renal transplant immunosuppression and complex paediatric care drive the bill. The trust is a principal treatment centre (PTC) for teenage/young-adult cancer and hosts the Yorkshire Regional Genetics Service, which anchors CAR-T referrals and rare-disease targeted therapies.",
        "beneficiaries": "~1.8M West Yorkshire residents plus regional tertiary referrals (sarcoma, BMT, liver/renal transplant, burns, HIV)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£301.6M"},
            {"label": "Acute beds", "value": "~2,000 across LGI + St James's"},
            {"label": "Staff (WTE)", "value": "~21,000"},
            {"label": "Operating revenue", "value": "£1.88bn (2023-24)"},
            {"label": "Cancer treatment centre", "value": "Leeds Cancer Centre — ~18,000 new cancer diagnoses/yr across Yorkshire"},
            {"label": "BMT / CAR-T", "value": "One of 7 adult CAR-T centres in England (NHS England commissioned)"},
            {"label": "Transplant programme", "value": "Renal + liver + pancreas (~250 kidney transplants/yr)"},
            {"label": "HCD pass-through", "value": "Majority of oncology/haematology drug spend reimbursed via NHS England specialised commissioning HCDs list, not PbR tariff"},
            {"label": "ICB", "value": "West Yorkshire ICB (host commissioner)"}
        ],
        "notes": "Leeds' drug bill is dominated by specialised-commissioning high-cost drugs: daratumumab, venetoclax and bispecific antibodies for myeloma/lymphoma; CAR-T products (axicabtagene, tisagenlecleucel) at c.£280k/dose with full NHS England pass-through; and rising oral targeted-therapy spend (ibrutinib, acalabrutinib biosimilar switch pending). Homecare medicines — notably adalimumab biosimilars for rheumatology/IBD dispensed via Sciensus/Lloyds Clinical — flow through the trust's ledger even though patients never enter a ward. VPAG levy receipts (effective Jan 2024) partially offset branded spend growth but do not apply to biosimilars or generics.",
        "sources": [
            {"publisher": "Leeds Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.leedsth.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "NHS England", "title": "National tariff 2024-25: high-cost drugs list", "year": "2024", "url": "https://www.england.nhs.uk/publication/2024-25-nhs-payment-scheme/"},
            {"publisher": "DHSC", "title": "Voluntary scheme for branded medicines pricing, access and growth (VPAG)", "year": "2024", "url": "https://www.gov.uk/government/publications/the-2024-voluntary-scheme-for-branded-medicines-pricing-access-and-growth"}
        ],
        "related": ["The Leeds Teaching Hospitals NHS Trust", "Clinical Supplies & Drugs — The Leeds Teaching Hospitals NHS Trust"]
    },

    "Drugs costs — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Drug spend across Royal Free London's three-hospital group — Royal Free (Hampstead), Barnet and Chase Farm — where the national liver transplant programme, HIV specialist commissioning, amyloidosis (NHS National Amyloidosis Centre) and renal transplantation generate disproportionate high-cost-drug consumption. One of England's largest HIV outpatient cohorts also lifts antiretroviral spend.",
        "beneficiaries": "~1.6M North London catchment + UK-wide tertiary referrals for amyloidosis, liver transplant and HIV",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£262.0M"},
            {"label": "Operating revenue", "value": "£1.65bn (2023-24)"},
            {"label": "Staff (WTE)", "value": "~10,500"},
            {"label": "Liver transplants", "value": "~150/yr (one of 7 UK adult centres)"},
            {"label": "Renal transplants", "value": "~200/yr"},
            {"label": "HIV service", "value": "~5,000+ patients in Ian Charleson Day Centre cohort"},
            {"label": "National Amyloidosis Centre", "value": "Sole NHS centre — patisiran, vutrisiran, tafamidis"},
            {"label": "ICB", "value": "North Central London ICB"}
        ],
        "notes": "The trust's drug bill is atypically weighted toward pass-through specialised-commissioning drugs: tafamidis (Vyndaqel/Vyndamax) for ATTR cardiac amyloidosis — one of NHS England's highest-unit-cost oral drugs; patisiran and the newer vutrisiran (NICE TA868, 2024) for hereditary ATTR; tacrolimus, mycophenolate and belatacept for transplant cohorts; and a large antiretroviral bill (bictegravir/emtricitabine/tenofovir) with ongoing generic-TAF switches. Biosimilar rituximab and infliximab are fully embedded. Barnet and Chase Farm contribute a more conventional acute drug mix (anaesthesia, antibiotics, cancer chemo).",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information/annual-report-and-accounts/"},
            {"publisher": "NICE", "title": "TA868: Vutrisiran for treating hereditary transthyretin-related amyloidosis", "year": "2023", "url": "https://www.nice.org.uk/guidance/ta868"},
            {"publisher": "NHS England", "title": "Specialised commissioning — liver transplantation service specification", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Clinical Supplies & Drugs — Royal Free London NHS Foundation Trust"]
    },

    "Drugs costs — Oxford University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
        "description": "Drug spend across the John Radcliffe, Churchill, NOC and Horton hospitals — a major academic centre with NIHR BRC status whose drug mix reflects heavy oncology/haematology activity at the Churchill, stem-cell transplant, adult CF service and Thames Valley cardiothoracic work. Early-access and compassionate-use medicines are common given the trust's clinical-trial density.",
        "beneficiaries": "~700k Oxfordshire residents + Thames Valley tertiary (cancer, cardiac, neurosciences, renal)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£206.9M"},
            {"label": "Operating revenue", "value": "£1.62bn (2023-24)"},
            {"label": "Staff (WTE)", "value": "~13,500"},
            {"label": "NIHR BRC funding", "value": "£122M (2022-27) — Oxford BRC"},
            {"label": "Churchill oncology", "value": "Regional cancer centre for Thames Valley (~6,000 new cancers/yr)"},
            {"label": "Clinical trials open", "value": ">1,000 at any time"},
            {"label": "CF service", "value": "Adult centre — Kaftrio/Kalydeco dispensing via homecare"},
            {"label": "ICB", "value": "Buckinghamshire, Oxfordshire and Berkshire West ICB"}
        ],
        "notes": "Oxford's drug bill is disproportionately oncology: the Churchill runs one of England's largest day-unit chemo services, and targeted therapies (osimertinib, pembrolizumab, trastuzumab-deruxtecan) plus CDF-route drugs lift the HCD pass-through line. Homecare elexacaftor/tezacaftor/ivacaftor (Kaftrio, Vertex) for the adult CF cohort is a material line, as are homecare biologics for rheumatology and IBD. The trust was an early adopter of biosimilar bevacizumab (launched Q3 2024) — a multi-million £ annualised saving in colorectal/ovarian cancer.",
        "sources": [
            {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.ouh.nhs.uk/about/publications/annual-reports.aspx"},
            {"publisher": "NHS England", "title": "Commissioning policy: elexacaftor-tezacaftor-ivacaftor (Kaftrio)", "year": "2023", "url": "https://www.england.nhs.uk/publication/clinical-commissioning-policy-elexacaftor-tezacaftor-and-ivacaftor-for-cystic-fibrosis/"},
            {"publisher": "NIHR", "title": "Oxford Biomedical Research Centre", "year": "2024", "url": "https://oxfordbrc.nihr.ac.uk/"}
        ],
        "related": ["Oxford University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Oxford University Hospitals NHS Foundation Trust"]
    },

    "Drugs costs — Nottingham University Hospitals NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Nottingham University Hospitals NHS Trust"}],
        "description": "Drug spend across QMC and Nottingham City Hospital — the East Midlands Major Trauma Centre and a regional cancer/haematology/BMT hub. QMC hosts the East Midlands Children's Hospital and the Nottingham Breast Institute; the City Hospital campus delivers BMT, radiotherapy and specialist respiratory care. The trust remained in NHS Recovery Support Programme (Segment 4) during 2023-24, pressuring formulary discipline.",
        "beneficiaries": "~2.5M population served across Nottinghamshire + East Midlands tertiary (trauma, cancer, renal)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£192.8M"},
            {"label": "Operating revenue", "value": "£1.55bn (2023-24)"},
            {"label": "Staff (WTE)", "value": "~17,500"},
            {"label": "Beds", "value": "~1,700"},
            {"label": "Major Trauma Centre", "value": "East Midlands MTC (adults + paediatrics)"},
            {"label": "Haematology/BMT", "value": "Allogeneic + autologous BMT programme at City Hospital"},
            {"label": "NHS oversight", "value": "NHS Recovery Support Programme (Segment 4) during 2023-24"},
            {"label": "ICB", "value": "Nottingham and Nottinghamshire ICB"}
        ],
        "notes": "Drug-spend drivers at NUH include trauma-related critical care products (tranexamic acid, albumin, fibrinogen concentrate), plus oncology/haematology HCDs (daratumumab, bortezomib, bispecifics entering formulary in 2024). The trust has invested in e-prescribing (EPR go-live ongoing) to tighten missed-dose charging under PbR pass-through, and flagged medicines wastage and off-list usage in its 2023-24 quality report. Industrial action through to July 2024 disrupted elective chemotherapy scheduling, marginally moderating in-year spend.",
        "sources": [
            {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.nuh.nhs.uk/annual-reports/"},
            {"publisher": "NHS England", "title": "NHS Oversight Framework 2023-24 segmentation", "year": "2024", "url": "https://www.england.nhs.uk/publication/nhs-oversight-framework/"},
            {"publisher": "CQC", "title": "Nottingham University Hospitals NHS Trust — inspection reports", "year": "2024", "url": "https://www.cqc.org.uk/provider/RX1"}
        ],
        "related": ["Nottingham University Hospitals NHS Trust", "Clinical Supplies & Drugs — Nottingham University Hospitals NHS Trust"]
    },

    "Drugs costs — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "Drug spend across the merged seven-hospital group (Royal Sussex County, Princess Royal, St Richard's, Worthing, Southlands, Royal Alexandra Children's, Sussex Eye) formed April 2021 from BSUH + Western Sussex. Brighton hosts the Sussex Cancer Centre (regional radiotherapy/chemo) and the HIV service at the Lawson Unit — both material drivers of the HCD pass-through bill.",
        "beneficiaries": "~1.8M Sussex residents + regional tertiary for cancer, cardiology, HIV and major trauma",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£151.1M"},
            {"label": "Operating revenue", "value": "£1.45bn (2023-24)"},
            {"label": "Staff (WTE)", "value": "~13,000"},
            {"label": "Hospitals", "value": "7 sites across Brighton, Worthing, Chichester, Haywards Heath"},
            {"label": "Sussex Cancer Centre", "value": "Regional radiotherapy + SACT chemotherapy hub"},
            {"label": "HIV cohort", "value": "Lawson Unit — one of the largest south-coast HIV services"},
            {"label": "Major Trauma", "value": "Royal Sussex County (Level 1 adult MTC for Sussex)"},
            {"label": "ICB", "value": "Sussex ICB"}
        ],
        "notes": "The merged trust's drug line reflects post-merger formulary harmonisation (Brighton-vs-Worthing biosimilar switch patterns were historically uneven). High-cost oncology at the Sussex Cancer Centre (pembrolizumab, nivolumab, trastuzumab-deruxtecan) and antiretroviral spend at the Lawson Unit dominate; homecare adalimumab biosimilar penetration is near-universal. Trust-level financial pressure (reported deficit in 2023-24) has driven tight stewardship of HCD validation and CQUIN-linked antimicrobial programmes.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.uhsussex.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "HIV drugs — specialised commissioning", "year": "2024", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/blood-and-infection-group-f/"},
            {"publisher": "NHS England", "title": "National tariff 2024-25", "year": "2024", "url": "https://www.england.nhs.uk/publication/2024-25-nhs-payment-scheme/"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Clinical Supplies & Drugs — University Hospitals Sussex NHS Foundation Trust"]
    },

    "Drugs costs — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "Drug spend across Royal Stoke University Hospital and County Hospital (Stafford) — the regional tertiary centre for Staffordshire/North Midlands/mid-Wales, hosting the West Midlands North Major Trauma Centre, regional neurosciences, cardiothoracic surgery and a large renal dialysis programme.",
        "beneficiaries": "~3M across Staffordshire, Shropshire, Cheshire and north Wales for tertiary services; ~900k local catchment",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£122.9M"},
            {"label": "Operating revenue", "value": "£1.05bn (2023-24)"},
            {"label": "Staff (WTE)", "value": "~11,500"},
            {"label": "Beds", "value": "~1,450"},
            {"label": "Major Trauma Centre", "value": "West Midlands North MTC (Royal Stoke)"},
            {"label": "Neurosciences", "value": "Regional centre — MS disease-modifying therapies dispensing"},
            {"label": "Renal", "value": "Regional dialysis + transplant work-up"},
            {"label": "ICB", "value": "Staffordshire and Stoke-on-Trent ICB"}
        ],
        "notes": "Spend drivers include MS disease-modifying therapies (ocrelizumab, ofatumumab, cladribine) under specialised commissioning, solid-tumour oncology (lung, colorectal) and trauma-related blood products. The trust declared material financial pressure in 2023-24 and has focused on biosimilar switch programmes (infliximab, trastuzumab, adalimumab) and homecare provider consolidation to reduce dispensing fees. Industrial action disrupted outpatient infusion capacity across 2023-24.",
        "sources": [
            {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.uhnm.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — multiple sclerosis DMTs", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS Business Services Authority", "title": "Secondary care medicines data (SCMD)", "year": "2024", "url": "https://www.nhsbsa.nhs.uk/access-our-data-products/secondary-care-medicines-data"}
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Clinical Supplies & Drugs — University Hospitals of North Midlands NHS Trust"]
    },

    "Drugs costs — The Royal Marsden NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Royal Marsden NHS Foundation Trust"}],
        "description": "Drug spend at the UK's largest dedicated cancer centre, spanning the Chelsea and Sutton sites (plus Cavendish Square private unit) and partnering with the Institute of Cancer Research. Almost the entire drug bill is oncology/haematology SACT (systemic anti-cancer therapy), immunotherapy, CAR-T and early-phase trial drug — a dramatically different profile from a general acute trust.",
        "beneficiaries": "~60,000 cancer patients per year (NHS and private), plus UK-wide tertiary referrals for rare tumours and early-phase trials",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · Cancer Drugs Fund managed access",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£115.8M"},
            {"label": "Operating revenue", "value": "~£650M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~4,500"},
            {"label": "CAR-T centre", "value": "One of 7 adult CAR-T centres (NHSE commissioned)"},
            {"label": "Clinical trials", "value": ">900 open at any time (~one-third early-phase)"},
            {"label": "NIHR BRC", "value": "Royal Marsden + ICR BRC — one of UK's largest cancer BRCs"},
            {"label": "Sutton + Chelsea", "value": "Two NHS sites + Cavendish Square private unit"},
            {"label": "ICB", "value": "South West London ICB (host) — but specialised commissioning via NHS England"}
        ],
        "notes": "The Royal Marsden's drug bill is an outlier: oncology-only, heavily weighted to HCDs reimbursed by NHS England specialised commissioning at cost (enabling NICE-approved new indications within 3 months of TA). Immune checkpoint inhibitors (pembrolizumab, nivolumab, ipilimumab + LAG-3 relatlimab), antibody-drug conjugates (trastuzumab-deruxtecan, sacituzumab-govitecan), CAR-T products, and a large early-phase trial supply dominate. Private patient income (~25% of revenue) partly cross-subsidises NHS drug costs. Biosimilar bevacizumab (Q3 2024 launch) and aflibercept biosimilar (late 2024) are forecast to release millions in annualised savings from 2024-25.",
        "sources": [
            {"publisher": "The Royal Marsden NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.royalmarsden.nhs.uk/about-royal-marsden/corporate-information/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "Cancer Drugs Fund managed access agreements", "year": "2024", "url": "https://www.england.nhs.uk/cancer/cdf/"},
            {"publisher": "NIHR", "title": "Biomedical Research Centre — Royal Marsden and ICR", "year": "2024", "url": "https://rmicr.nihr.ac.uk/"}
        ],
        "related": ["The Royal Marsden NHS Foundation Trust", "Clinical Supplies & Drugs — The Royal Marsden NHS Foundation Trust"]
    },

    "Drugs costs — The Clatterbridge Cancer Centre NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Clatterbridge Cancer Centre NHS Foundation Trust"}],
        "description": "Drug spend at the regional non-surgical cancer centre for Merseyside, Cheshire, north Wales and Isle of Man — spanning Clatterbridge-Liverpool (new 2020 tower in the Royal Liverpool complex), Wirral and Aintree sites. Virtually all drug spend is oncology SACT/immunotherapy and supportive care. The centre hosts the UK's only operational high-energy proton beam therapy for ocular melanoma (at Clatterbridge Wirral).",
        "beneficiaries": "~2.4M catchment across Merseyside, Cheshire, north Wales and Isle of Man (~32,000 patients/yr)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · Cancer Drugs Fund",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£106.5M"},
            {"label": "Operating revenue", "value": "~£280M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~1,800"},
            {"label": "Patients/year", "value": "~32,000 (largest SACT centre outside London)"},
            {"label": "Proton beam therapy", "value": "UK ocular melanoma centre (Wirral)"},
            {"label": "SACT delivery sites", "value": "Liverpool (Pembroke Place), Wirral, Aintree + satellite clinics"},
            {"label": "HCD share", "value": "Majority of drug spend NHSE-reimbursed via specialised commissioning HCDs list"},
            {"label": "ICB", "value": "Cheshire and Merseyside ICB (host)"}
        ],
        "notes": "As a specialist cancer trust, virtually every pound of drug spend is oncology: checkpoint inhibitors, CDK4/6 inhibitors (palbociclib, abemaciclib, ribociclib), antibody-drug conjugates, and increasing oral targeted therapy volumes via the aseptic unit and homecare. The trust is a reference site for biosimilar adoption (trastuzumab, rituximab, bevacizumab in 2024). Notably, Cancer Drugs Fund spend is NOT in this line — it is centrally commissioned by NHS England (£340M national budget 2024-25) and passed to the trust at cost.",
        "sources": [
            {"publisher": "The Clatterbridge Cancer Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.clatterbridgecc.nhs.uk/about/publications/annual-reports"},
            {"publisher": "NHS England", "title": "Proton beam therapy service specification", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS England", "title": "Cancer Drugs Fund 2024-25", "year": "2024", "url": "https://www.england.nhs.uk/cancer/cdf/"}
        ],
        "related": ["The Clatterbridge Cancer Centre NHS Foundation Trust", "Clinical Supplies & Drugs — The Clatterbridge Cancer Centre NHS Foundation Trust"]
    },

    "Drugs costs — South Tees Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "South Tees Hospitals NHS Foundation Trust"}],
        "description": "Drug spend at James Cook University Hospital (Middlesbrough) and the Friarage (Northallerton) — the tertiary centre for Tees, North Yorkshire and East Cumbria, hosting the North-East Major Trauma Centre (James Cook), regional cardiothoracic surgery, spinal injuries and the North of England Cancer Network for Tees.",
        "beneficiaries": "~1.5M population for tertiary services (cardiothoracic, neuro, spinal) + ~400k local Tees catchment",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£95.8M"},
            {"label": "Operating revenue", "value": "~£880M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~9,500"},
            {"label": "Major Trauma Centre", "value": "Adult + paediatric MTC (James Cook) — one of two NE MTCs"},
            {"label": "Cardiothoracic surgery", "value": "Regional centre serving Tees/N Yorks/E Cumbria"},
            {"label": "Spinal injuries", "value": "Golden Jubilee Spinal Injuries Unit"},
            {"label": "Cancer network", "value": "North East and North Cumbria Cancer Alliance partner"},
            {"label": "ICB", "value": "North East and North Cumbria ICB"}
        ],
        "notes": "Drug spend at South Tees is shaped by trauma/critical-care consumables (blood products, sedatives), cardiothoracic surgery drugs (pulmonary hypertension therapies, anticoagulants) and a growing oncology biologic line. Homecare MS DMTs (ocrelizumab) dispensed via the neurosciences team contribute. The trust reported a material deficit in 2023-24 and has prioritised biosimilar uptake (trastuzumab, rituximab, infliximab biosimilars near-universal) and aseptic production efficiency at the James Cook pharmacy.",
        "sources": [
            {"publisher": "South Tees Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.southtees.nhs.uk/about/publications/annual-report/"},
            {"publisher": "NHS England", "title": "Major Trauma Services — service specification", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d15/"},
            {"publisher": "NHS Business Services Authority", "title": "Secondary care medicines data", "year": "2024", "url": "https://www.nhsbsa.nhs.uk/access-our-data-products/secondary-care-medicines-data"}
        ],
        "related": ["South Tees Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — South Tees Hospitals NHS Foundation Trust"]
    },

    "Drugs costs — London North West University Healthcare NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "London North West University Healthcare NHS Trust"}],
        "description": "Drug spend across Northwick Park, Central Middlesex and Ealing — a large north-west London acute/integrated trust serving Brent, Harrow and Ealing, one of England's most ethnically diverse catchments. Drug mix reflects a high-prevalence type 2 diabetes population, sickle-cell/thalassaemia service, HIV and active elective orthopaedic work at Central Middlesex.",
        "beneficiaries": "~1M residents of Brent, Harrow and Ealing — diverse, high-deprivation catchment",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£85.5M"},
            {"label": "Operating revenue", "value": "~£800M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~8,500"},
            {"label": "Catchment diabetes prevalence", "value": "Brent + Harrow among highest in London"},
            {"label": "Sickle cell service", "value": "Regional specialist haemoglobinopathy centre"},
            {"label": "A&E attendances", "value": "~300k/yr across NPH + Ealing"},
            {"label": "HIV cohort", "value": "Material — Brent and Harrow ICB catchment"},
            {"label": "ICB", "value": "North West London ICB"}
        ],
        "notes": "Drug spend reflects high diabetes prevalence (GLP-1 receptor agonists — semaglutide, dulaglutide — rolled out 2024 under ICB pathways; SGLT2 inhibitors), antiretroviral therapy costs for the HIV cohort, and haemoglobinopathy-related drugs (crizanlizumab, voxelotor under NICE managed access) and chronic transfusion iron chelation (deferasirox). Biosimilar adalimumab/infliximab are embedded. The trust has absorbed meaningful VPAG levy rebates in 2024-25 on branded diabetes drugs, although GLP-1 volume growth is outpacing pricing relief.",
        "sources": [
            {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.lnwh.nhs.uk/annual-reports/"},
            {"publisher": "NICE", "title": "TA875: Crizanlizumab for preventing sickle cell crises (withdrawn 2023)", "year": "2023", "url": "https://www.nice.org.uk/guidance/ta875"},
            {"publisher": "NHS England", "title": "GLP-1 receptor agonist commissioning guidance 2024", "year": "2024", "url": "https://www.england.nhs.uk/long-read/glp-1-receptor-agonists-commissioning/"}
        ],
        "related": ["London North West University Healthcare NHS Trust", "Clinical Supplies & Drugs — London North West University Healthcare NHS Trust"]
    },

    "Drugs costs — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "Drug spend at the merged (Oct 2020) group comprising Royal Bournemouth, Poole and Christchurch hospitals — a large Dorset coastal acute trust with the Dorset Cancer Centre (Poole), regional cardiac surgery and an older-than-average population driving cardiometabolic and oncology drug volumes.",
        "beneficiaries": "~800k Dorset residents (high proportion aged 65+)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£81.0M"},
            {"label": "Operating revenue", "value": "~£830M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~8,500"},
            {"label": "Merger date", "value": "1 October 2020 (Royal Bournemouth + Poole)"},
            {"label": "Dorset Cancer Centre", "value": "Poole Hospital — chemotherapy + radiotherapy hub"},
            {"label": "Cardiac surgery", "value": "Regional centre (Royal Bournemouth)"},
            {"label": "Population aged 65+", "value": "~24% of catchment (vs ~18% England)"},
            {"label": "ICB", "value": "NHS Dorset ICB"}
        ],
        "notes": "An older catchment skews drug spend toward age-related conditions: anti-VEGF injections (aflibercept, ranibizumab; biosimilar aflibercept expected to release material 2024-25 savings), cardiometabolic prescribing, and solid-tumour oncology. The trust is part-way through reconfiguration (major new Critical Treatment Hospital at Bournemouth opening 2025) which is shifting elective/cancer pathways and aseptic production between sites. Biosimilar programme delivery has been strong across rheumatology/IBD biologics.",
        "sources": [
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.uhd.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "NICE", "title": "Biosimilar aflibercept — NHS England commissioning framework", "year": "2024", "url": "https://www.england.nhs.uk/ophthalmology/"},
            {"publisher": "NHS Dorset ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://nhsdorset.nhs.uk/"}
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Clinical Supplies & Drugs — University Hospitals Dorset NHS Foundation Trust"]
    },

    "Drugs costs — North Bristol NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "North Bristol NHS Trust"}],
        "description": "Drug spend at Southmead Hospital — a large PFI-built Brunel building hosting the South West Major Trauma Centre, regional neurosciences, renal (adult transplant), plastics and burns. The drug-cost line is skewed by these tertiary specialties and by a well-developed homecare dispensing programme.",
        "beneficiaries": "~500k local catchment + ~2.5M regional for tertiary services (SW England, S Wales)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£74.9M"},
            {"label": "Operating revenue", "value": "~£830M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~8,500"},
            {"label": "Southmead PFI", "value": "£430M Brunel building (2014)"},
            {"label": "Major Trauma Centre", "value": "South West MTC (adult)"},
            {"label": "Renal transplant", "value": "Regional adult kidney transplant programme"},
            {"label": "Plastics/burns", "value": "SW regional plastics + adult burns unit"},
            {"label": "ICB", "value": "Bristol, North Somerset and South Gloucestershire ICB"}
        ],
        "notes": "Drug spend drivers include MS DMTs and neurology biologics via the regional neurosciences service, transplant immunosuppression, and critical-care drug volumes associated with the MTC. Homecare adalimumab biosimilar (Amgevita/Imraldi/Yuflyma) substitution is near-complete. The trust's PFI capacity constraints periodically push elective chemotherapy pathways, with cancer care largely delivered at UH Bristol & Weston across the city.",
        "sources": [
            {"publisher": "North Bristol NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.nbt.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "NHS England", "title": "Renal transplantation — specialised commissioning", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS Business Services Authority", "title": "Secondary care medicines data", "year": "2024", "url": "https://www.nhsbsa.nhs.uk/access-our-data-products/secondary-care-medicines-data"}
        ],
        "related": ["North Bristol NHS Trust", "Clinical Supplies & Drugs — North Bristol NHS Trust"]
    },

    "Drugs costs — United Lincolnshire Hospitals NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "United Lincolnshire Hospitals NHS Trust"}],
        "description": "Drug spend across Lincoln County, Pilgrim Hospital Boston, Grantham and District, and Louth County — covering a rural, dispersed catchment of ~770k. Lincolnshire has structurally recruitment-challenged specialist services; tertiary oncology and cardiothoracic pathways flow to Nottingham or Sheffield, shaping a drug mix dominated by core acute medicine rather than HCD oncology.",
        "beneficiaries": "~770k Lincolnshire residents across a large rural county",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£71.2M"},
            {"label": "Operating revenue", "value": "~£740M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~7,500"},
            {"label": "Sites", "value": "Lincoln + Boston + Grantham + Louth"},
            {"label": "Catchment", "value": "Rural, dispersed — longest-travel-to-hospital patient mix in E Midlands"},
            {"label": "Tertiary outflow", "value": "Cancer/cardiac/neuro referred to Nottingham/Sheffield"},
            {"label": "NHS oversight", "value": "Historically NHS Recovery Support Programme"},
            {"label": "ICB", "value": "Lincolnshire ICB"}
        ],
        "notes": "ULH's drug spend is weighted toward core acute medicine — antibiotics, anticoagulants, respiratory inhalers, diabetes therapies — and less toward specialised-commissioning HCDs than tertiary peers. Medicines-optimisation priorities include biosimilar switch completion (adalimumab, trastuzumab, rituximab), DOAC vs warfarin stewardship, and reducing missed-dose/antimicrobial waste. Industrial action through 2023-24 delayed elective chemo scheduling; drug-shortage management (e.g. ADHD stimulants) has been a recurring pressure.",
        "sources": [
            {"publisher": "United Lincolnshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.ulh.nhs.uk/about/publications/annual-report/"},
            {"publisher": "NHS Lincolnshire ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://lincolnshire.icb.nhs.uk/"},
            {"publisher": "DHSC", "title": "Medicine supply notifications — ADHD stimulants", "year": "2024", "url": "https://www.gov.uk/drug-safety-update"}
        ],
        "related": ["United Lincolnshire Hospitals NHS Trust", "Clinical Supplies & Drugs — United Lincolnshire Hospitals NHS Trust"]
    },

    "Drugs costs — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "Drug spend across Worcestershire Royal (Worcester), Alexandra (Redditch) and Kidderminster — a mid-sized acute trust whose cancer patients access the Three Counties Cancer Centre at Cheltenham and more complex tertiary work via University Hospitals Birmingham. Drug mix is therefore core-acute weighted with a modest specialist line.",
        "beneficiaries": "~600k Worcestershire residents",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£63.4M"},
            {"label": "Operating revenue", "value": "~£540M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~6,000"},
            {"label": "Sites", "value": "Worcester + Alexandra (Redditch) + Kidderminster"},
            {"label": "Cancer pathway", "value": "SACT locally; complex radio/tertiary cancer outflow to Cheltenham + UHB"},
            {"label": "A&E attendances", "value": "~200k/yr"},
            {"label": "Historical oversight", "value": "Long-standing NHS Recovery Support Programme pressure"},
            {"label": "ICB", "value": "Herefordshire and Worcestershire ICB"}
        ],
        "notes": "Drug spend is dominated by general-acute categories (antibiotics, anticoagulants, inhaled therapies, critical-care sedation), with a smaller HCD oncology line reflecting the trust's referral relationships. Biosimilar switch programmes (adalimumab, infliximab, rituximab) are embedded. Financial pressure and ongoing capital programme (new Emergency Department Worcester) have made medicines-optimisation CIP delivery — homecare rebasing, aseptic efficiency — a recurring theme in board papers.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.worcsacute.nhs.uk/about-us/publications/annual-report-and-accounts"},
            {"publisher": "NHS England", "title": "Biosimilar medicines commissioning framework", "year": "2024", "url": "https://www.england.nhs.uk/medicines-2/biosimilars/"},
            {"publisher": "Herefordshire and Worcestershire ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://herefordshireandworcestershire.icb.nhs.uk/"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Clinical Supplies & Drugs — Worcestershire Acute Hospitals NHS Trust"]
    },

    "Drugs costs — North West Anglia NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "North West Anglia NHS Foundation Trust"}],
        "description": "Drug spend across Peterborough City, Hinchingbrooke (Huntingdon) and Stamford & Rutland — serving north Cambs, west Norfolk fringes and Lincolnshire border. Complex cancer and cardiac work flows to Cambridge University Hospitals; the drug mix is therefore general-acute plus a meaningful SACT outpatient line.",
        "beneficiaries": "~800k residents of north Cambs, Peterborough and neighbouring districts",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£60.6M"},
            {"label": "Operating revenue", "value": "~£560M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~5,500"},
            {"label": "Sites", "value": "Peterborough City + Hinchingbrooke + Stamford"},
            {"label": "Trust creation", "value": "Merged April 2017 (Peterborough + Stamford + Hinchingbrooke)"},
            {"label": "Cancer pathway", "value": "SACT locally; complex cancer outflow to Cambridge (Addenbrooke's)"},
            {"label": "Peterborough PFI", "value": "City Hospital £335M PFI (2010) — continuing unitary charge pressure"},
            {"label": "ICB", "value": "Cambridgeshire and Peterborough ICB"}
        ],
        "notes": "Drug spend profile is general-acute weighted with a growing SACT outpatient chemotherapy volume at Peterborough. The trust's PFI cost base constrains discretionary spend, sharpening focus on biosimilar switch (adalimumab, trastuzumab, rituximab biosimilars near-universal; bevacizumab biosimilar adoption underway since Q3 2024) and homecare rebasing. Cambridge's tertiary specialty split means fewer HCD cost-per-patient outliers than at a regional centre.",
        "sources": [
            {"publisher": "North West Anglia NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.nwangliaft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "National tariff 2024-25", "year": "2024", "url": "https://www.england.nhs.uk/publication/2024-25-nhs-payment-scheme/"},
            {"publisher": "Cambridgeshire and Peterborough ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.cpics.org.uk/"}
        ],
        "related": ["North West Anglia NHS Foundation Trust", "Clinical Supplies & Drugs — North West Anglia NHS Foundation Trust"]
    },

    "Drugs costs — Buckinghamshire Healthcare NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Buckinghamshire Healthcare NHS Trust"}],
        "description": "Drug spend across Stoke Mandeville (Aylesbury), Wycombe and Amersham — a district-general acute/community trust best known for the National Spinal Injuries Centre at Stoke Mandeville (a 1944-founded NHSE-commissioned specialist unit), which gives this trust an atypical drug profile for its size.",
        "beneficiaries": "~550k Bucks residents + UK-wide spinal injuries tertiary referrals",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£55.4M"},
            {"label": "Operating revenue", "value": "~£600M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~6,000"},
            {"label": "National Spinal Injuries Centre", "value": "Stoke Mandeville — UK's original spinal unit (1944)"},
            {"label": "Burns service", "value": "Stoke Mandeville regional burns centre"},
            {"label": "Sites", "value": "Stoke Mandeville + Wycombe + Amersham"},
            {"label": "Cancer outflow", "value": "Specialist oncology flows to Oxford (Churchill)"},
            {"label": "ICB", "value": "Buckinghamshire, Oxfordshire and Berkshire West ICB"}
        ],
        "notes": "Drug spend reflects the dual personality of a district-general plus a nationally commissioned spinal injuries centre: spinal/neuropathic pain pharmacology (gabapentinoids, botulinum toxin for spasticity), long-term catheter/urology drug use, and standard acute-medicine volumes. Biosimilar programme delivery is robust. Specialist oncology outflow to Oxford means HCD pass-through is smaller than at full acute peers.",
        "sources": [
            {"publisher": "Buckinghamshire Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.buckshealthcare.nhs.uk/about-us/publications-2/"},
            {"publisher": "NHS England", "title": "Spinal cord injury service specification", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/"},
            {"publisher": "NHS Business Services Authority", "title": "Secondary care medicines data", "year": "2024", "url": "https://www.nhsbsa.nhs.uk/access-our-data-products/secondary-care-medicines-data"}
        ],
        "related": ["Buckinghamshire Healthcare NHS Trust", "Clinical Supplies & Drugs — Buckinghamshire Healthcare NHS Trust"]
    },

    "Drugs costs — Bradford Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Bradford Teaching Hospitals NHS Foundation Trust"}],
        "description": "Drug spend at Bradford Royal Infirmary and St Luke's — a teaching trust in one of England's most deprived and ethnically diverse cities, with high rates of type 2 diabetes, renal disease and consanguinity-linked paediatric rare-disease burden (reflected in the Born in Bradford cohort).",
        "beneficiaries": "~530k Bradford residents — high-deprivation, ethnically diverse (South Asian heritage majority in-city)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£53.8M"},
            {"label": "Operating revenue", "value": "~£560M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~5,600"},
            {"label": "Diabetes prevalence", "value": "Bradford district — among highest in North"},
            {"label": "Born in Bradford cohort", "value": "30,000+ families followed since 2007 (world-class birth cohort)"},
            {"label": "Renal service", "value": "Regional dialysis"},
            {"label": "A&E attendances", "value": "~200k/yr"},
            {"label": "ICB", "value": "West Yorkshire ICB"}
        ],
        "notes": "Drug spend is shaped by the catchment: high-volume GLP-1 RA and SGLT2 prescribing for type 2 diabetes, DMARDs/biologics for early-onset rheumatic disease, and paediatric rare-disease drugs (some via specialised commissioning pass-through). Biosimilar adoption is embedded. The trust has invested in structured homecare pathways for rheumatology/IBD biologics, moderating administrative cost growth in 2024-25.",
        "sources": [
            {"publisher": "Bradford Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.bradfordhospitals.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Born in Bradford", "title": "Cohort study — Bradford Institute for Health Research", "year": "2024", "url": "https://borninbradford.nhs.uk/"},
            {"publisher": "NHS England", "title": "GLP-1 receptor agonist commissioning guidance 2024", "year": "2024", "url": "https://www.england.nhs.uk/long-read/glp-1-receptor-agonists-commissioning/"}
        ],
        "related": ["Bradford Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Bradford Teaching Hospitals NHS Foundation Trust"]
    },

    "Drugs costs — Alder Hey Children's NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Alder Hey Children's NHS Foundation Trust"}],
        "description": "Drug spend at one of Europe's largest specialist children's hospitals — a Liverpool-based paediatric quaternary centre for North West England, North Wales and the Isle of Man, covering paediatric oncology, cardiac surgery, neurology, rheumatology and a large paediatric ICU. Drug spend per patient is elevated by rare-disease and gene/cell therapy activity.",
        "beneficiaries": "~275,000 paediatric patients per year across the North West, North Wales and Isle of Man",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE specialised commissioning",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£51.7M"},
            {"label": "Operating revenue", "value": "~£380M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,800"},
            {"label": "Patients/year", "value": "~275,000"},
            {"label": "Paediatric oncology", "value": "Principal Treatment Centre (PTC) for North West"},
            {"label": "Cardiac surgery", "value": "Regional paediatric cardiac centre"},
            {"label": "Specialised commissioning", "value": "Most HCD oncology + rare-disease spend reimbursed at cost"},
            {"label": "ICB", "value": "Cheshire and Merseyside ICB (host)"}
        ],
        "notes": "Drug spend at Alder Hey is dominated by paediatric oncology/haematology (vincristine, methotrexate, CAR-T at partner sites), gene/cell therapies (onasemnogene abeparvovec — Zolgensma — and nusinersen/risdiplam for SMA; atidarsagene autotemcel for MLD), and specialist rheumatology biologics. Many of these are ultra-high unit cost and NHSE-commissioned with full pass-through. Paediatric formulations (liquids, unlicensed specials) also inflate unit costs relative to adult peers. Biosimilar adoption where paediatric indications permit.",
        "sources": [
            {"publisher": "Alder Hey Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://alderhey.nhs.uk/about/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Highly specialised services — SMA gene therapy commissioning", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/highly-spec-services/"},
            {"publisher": "NICE", "title": "TA755: Onasemnogene abeparvovec for treating spinal muscular atrophy", "year": "2021", "url": "https://www.nice.org.uk/guidance/ta755"}
        ],
        "related": ["Alder Hey Children's NHS Foundation Trust", "Clinical Supplies & Drugs — Alder Hey Children's NHS Foundation Trust"]
    },

    "Drugs costs — Calderdale and Huddersfield NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
        "description": "Drug spend across Huddersfield Royal Infirmary and Calderdale Royal Hospital (Halifax) — a two-site West Yorkshire acute trust part-way through the long-running Hospital Reconfiguration Programme. Complex cancer and tertiary work flows to Leeds Teaching Hospitals and Bradford; the drug profile is therefore general-acute weighted.",
        "beneficiaries": "~470k residents of Calderdale and Kirklees",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£45.8M"},
            {"label": "Operating revenue", "value": "~£500M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~5,500"},
            {"label": "Sites", "value": "HRI (Huddersfield) + Calderdale Royal (Halifax)"},
            {"label": "A&E attendances", "value": "~190k/yr"},
            {"label": "Cancer outflow", "value": "Complex oncology/BMT via Leeds Teaching Hospitals"},
            {"label": "Reconfiguration", "value": "Hospital Reconfiguration Programme — capital case in development"},
            {"label": "ICB", "value": "West Yorkshire ICB"}
        ],
        "notes": "Drug spend mix is core-acute (antibiotics, anticoagulants, respiratory, diabetes) with a moderate SACT outpatient line for solid-tumour cancers. Biosimilar programmes (adalimumab, infliximab, rituximab, trastuzumab) are embedded with high switch rates. Homecare partner consolidation across Calderdale Huddersfield and neighbouring West Yorkshire trusts is a local CIP theme. VPAG levy receipts partly offset branded inflation, but GLP-1 volume growth is a pressure.",
        "sources": [
            {"publisher": "Calderdale and Huddersfield NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.cht.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "NHS England", "title": "Biosimilar medicines — commissioning framework", "year": "2024", "url": "https://www.england.nhs.uk/medicines-2/biosimilars/"},
            {"publisher": "West Yorkshire ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.wypartnership.co.uk/"}
        ],
        "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Clinical Supplies & Drugs — Calderdale and Huddersfield NHS Foundation Trust"]
    },

    "Drugs costs — South Warwickshire NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "South Warwickshire NHS Foundation Trust"}],
        "description": "Drug spend at Warwick Hospital and associated community services — a smaller district-general integrated trust delivering acute plus community care across south Warwickshire. Tertiary cancer, cardiac and neurosciences referrals flow to University Hospitals Coventry & Warwickshire and Birmingham.",
        "beneficiaries": "~280k residents of Warwick, Stratford, Leamington and surrounding south Warwickshire",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£42.9M"},
            {"label": "Operating revenue", "value": "~£310M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,700"},
            {"label": "Sites", "value": "Warwick Hospital + community clinics"},
            {"label": "Integrated community provider", "value": "Acute + community services in one organisation"},
            {"label": "Cancer pathway", "value": "SACT locally; tertiary flows to UHCW + Birmingham"},
            {"label": "Planned merger", "value": "Merger with George Eliot + Wye Valley proposed (as of 2024)"},
            {"label": "ICB", "value": "Coventry and Warwickshire ICB"}
        ],
        "notes": "Drug spend reflects a mid-sized district-general mix with a moderate SACT outpatient chemo line. Homecare-dispensed biologics (adalimumab biosimilars for rheumatology/IBD) are a material line. The proposed three-way merger (South Warwickshire + George Eliot + Wye Valley, announced 2023-24) is already driving joint formulary and procurement activity. Community prescribing falls to GPs/ICB pharmacy teams and is not captured in this trust drug-spend line.",
        "sources": [
            {"publisher": "South Warwickshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.swft.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "Coventry and Warwickshire ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.happyhealthylives.uk/"},
            {"publisher": "NHS England", "title": "Biosimilar medicines commissioning framework", "year": "2024", "url": "https://www.england.nhs.uk/medicines-2/biosimilars/"}
        ],
        "related": ["South Warwickshire NHS Foundation Trust", "Clinical Supplies & Drugs — South Warwickshire NHS Foundation Trust"]
    },

    "Drugs costs — University Hospitals of Morecambe Bay NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University Hospitals of Morecambe Bay NHS Foundation Trust"}],
        "description": "Drug spend across Royal Lancaster Infirmary, Furness General (Barrow) and Westmorland General (Kendal) — a three-site acute trust covering a dispersed coastal/rural catchment in north Lancashire and south Cumbria. Historically under scrutiny following the Kirkup report into maternity failings (2015); tertiary cancer and neurosciences referrals flow to Preston and Manchester.",
        "beneficiaries": "~365k residents of Lancaster, Barrow, Kendal and southern Lake District",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£40.2M"},
            {"label": "Operating revenue", "value": "~£450M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~5,500"},
            {"label": "Sites", "value": "RLI + Furness General + Westmorland General"},
            {"label": "Catchment", "value": "Dispersed rural/coastal — longest cross-site travel in North West"},
            {"label": "Tertiary outflow", "value": "Cancer/neuro/cardiac to Preston + Manchester"},
            {"label": "Historical oversight", "value": "Post-Kirkup improvement trajectory since 2015"},
            {"label": "ICB", "value": "Lancashire and South Cumbria ICB"}
        ],
        "notes": "Drug spend profile is dominated by general acute-medicine categories; specialist SACT volumes are modest given the tertiary outflow to Preston (Lancashire Teaching Hospitals) and The Christie. Biosimilar uptake (adalimumab, infliximab, trastuzumab, rituximab biosimilars) is high. Drug-shortage mitigation (ADHD stimulants, HRT) has been an operational pressure 2023-24. The trust's geography makes homecare partner service reliability a pharmacy governance priority.",
        "sources": [
            {"publisher": "University Hospitals of Morecambe Bay NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.uhmb.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "DHSC", "title": "Kirkup Review — Morecambe Bay Investigation (2015) and follow-up", "year": "2015", "url": "https://www.gov.uk/government/publications/morecambe-bay-investigation-report"},
            {"publisher": "Lancashire and South Cumbria ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.lancashireandsouthcumbria.icb.nhs.uk/"}
        ],
        "related": ["University Hospitals of Morecambe Bay NHS Foundation Trust", "Clinical Supplies & Drugs — University Hospitals of Morecambe Bay NHS Foundation Trust"]
    },

    "Drugs costs — Epsom and St Helier University Hospitals NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Epsom and St Helier University Hospitals NHS Trust"}],
        "description": "Drug spend across St Helier (Sutton), Epsom and several community hospitals — a two-site south-London acute trust also hosting the South West Thames Regional Renal Unit (on the St Helier site), a nationally significant dialysis/transplant-work-up service whose immunosuppressant and ESA spend materially shapes the overall drug line.",
        "beneficiaries": "~490k residents of Sutton, Merton, Epsom and surrounding areas + SW London renal tertiary referrals",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£35.2M"},
            {"label": "Operating revenue", "value": "~£470M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~5,500"},
            {"label": "Sites", "value": "St Helier (Sutton) + Epsom + community hospitals"},
            {"label": "Renal service", "value": "South West Thames Regional Renal Unit — one of the largest in the UK"},
            {"label": "Future capital", "value": "Sutton Specialist Emergency Care Hospital (New Hospital Programme — delayed)"},
            {"label": "Estate age", "value": "St Helier main building built 1938; significant backlog maintenance"},
            {"label": "ICB", "value": "South West London ICB"}
        ],
        "notes": "Drug spend is atypically weighted to renal medicine: erythropoiesis-stimulating agents (darbepoetin, epoetin biosimilars), iron therapies, calcimimetics (cinacalcet, etelcalcetide) and phosphate binders for the dialysis cohort, plus immunosuppression for transplant recipients. General acute spend otherwise standard. The trust's capital replacement uncertainty means medicines-optimisation CIP remains a recurring theme, with biosimilar switch and homecare consolidation already well progressed.",
        "sources": [
            {"publisher": "Epsom and St Helier University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.epsom-sthelier.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Renal services — specialised commissioning", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-a/a06/"},
            {"publisher": "DHSC", "title": "New Hospital Programme — updated schedule 2023", "year": "2023", "url": "https://www.gov.uk/government/publications/the-new-hospital-programme"}
        ],
        "related": ["Epsom and St Helier University Hospitals NHS Trust", "Clinical Supplies & Drugs — Epsom and St Helier University Hospitals NHS Trust"]
    },

    "Drugs costs — Liverpool Heart and Chest Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Liverpool Heart and Chest Hospital NHS Foundation Trust"}],
        "description": "Drug spend at the specialist cardiothoracic centre serving Merseyside, Cheshire, North Wales and the Isle of Man — one of England's largest heart attack centres and a regional thoracic surgery/lung transplant work-up provider. Drug mix is dominated by cardiovascular, thoracic and pulmonary-hypertension therapies rather than a general acute portfolio.",
        "beneficiaries": "~2.8M catchment across Merseyside, Cheshire, North Wales, Isle of Man (~50,000 patients/yr)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£33.5M"},
            {"label": "Operating revenue", "value": "~£200M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~1,900"},
            {"label": "Cardiac surgery", "value": "~2,000 cardiac operations/yr"},
            {"label": "Thoracic", "value": "Regional thoracic surgery + IPF/pulmonary hypertension clinic"},
            {"label": "PPCI / heart attack centre", "value": "Regional 24/7 primary PCI hub"},
            {"label": "HCD pass-through", "value": "Pulmonary hypertension drugs (bosentan, macitentan, selexipag) under NHSE specialised commissioning"},
            {"label": "ICB", "value": "Cheshire and Merseyside ICB"}
        ],
        "notes": "Drug spend is concentrated in pulmonary hypertension therapies (ambrisentan/macitentan, selexipag, tadalafil, treprostinil), advanced heart-failure medicines (sacubitril/valsartan, dapagliflozin/empagliflozin), antiplatelets/anticoagulants post-PCI, and thoracic-surgery-associated antimicrobials. The PH service is NHSE specialised-commissioning reimbursed at cost. Cardiology-specific biosimilar opportunities are limited — but newer agents (icosapent ethyl, vericiguat) are formulary considerations.",
        "sources": [
            {"publisher": "Liverpool Heart and Chest Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.lhch.nhs.uk/about-us/annual-reports-and-quality-accounts/"},
            {"publisher": "NHS England", "title": "Pulmonary hypertension service specification", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-a/a11/"},
            {"publisher": "NICE", "title": "Heart failure — chronic management guidelines (NG106)", "year": "2018", "url": "https://www.nice.org.uk/guidance/ng106"}
        ],
        "related": ["Liverpool Heart and Chest Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Liverpool Heart and Chest Hospital NHS Foundation Trust"]
    },

    "Drugs costs — Wye Valley NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Wye Valley NHS Trust"}],
        "description": "Drug spend at Hereford County Hospital plus community services — a small rural district-general integrated trust covering Herefordshire, a geographically isolated and demographically older catchment. Complex cancer, cardiac and neuro work flows to Worcester, Birmingham or Cheltenham.",
        "beneficiaries": "~190k residents of Herefordshire — rural, dispersed, older demographic",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£30.6M"},
            {"label": "Operating revenue", "value": "~£250M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,000"},
            {"label": "Sites", "value": "Hereford County Hospital + community hospitals"},
            {"label": "Catchment age 65+", "value": "~24% (vs ~18% England average)"},
            {"label": "Tertiary outflow", "value": "Cancer/cardiac to Worcester, Birmingham, Cheltenham"},
            {"label": "Planned merger", "value": "Proposed merger with South Warwickshire + George Eliot (announced 2023)"},
            {"label": "ICB", "value": "Herefordshire and Worcestershire ICB"}
        ],
        "notes": "Drug spend reflects the catchment: older-age cardiovascular and diabetes prescribing, solid-tumour SACT chemotherapy locally, and a modest homecare biologic line for rheumatology/IBD. Drug-shortage events (ADHD stimulants, HRT, GLP-1 RAs) are especially disruptive given rural homecare logistics. The pending merger with South Warwickshire NHSFT is expected to drive joint procurement and formulary harmonisation by 2025-26.",
        "sources": [
            {"publisher": "Wye Valley NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.wyevalley.nhs.uk/about-us/trust-publications/annual-reports-and-accounts.aspx"},
            {"publisher": "Herefordshire and Worcestershire ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://herefordshireandworcestershire.icb.nhs.uk/"},
            {"publisher": "DHSC", "title": "Medicine supply notifications 2024", "year": "2024", "url": "https://www.gov.uk/drug-safety-update"}
        ],
        "related": ["Wye Valley NHS Trust", "Clinical Supplies & Drugs — Wye Valley NHS Trust"]
    },

    "Drugs costs — Wirral University Teaching Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Wirral University Teaching Hospital NHS Foundation Trust"}],
        "description": "Drug spend at Arrowe Park and Clatterbridge (non-cancer site) — the Wirral's district-general with ~700 beds. Specialist cancer care sits with The Clatterbridge Cancer Centre next door, so Wirral UTH's drug mix is core-acute rather than oncology-weighted.",
        "beneficiaries": "~325k Wirral residents",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£29.9M"},
            {"label": "Operating revenue", "value": "~£390M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~5,000"},
            {"label": "Sites", "value": "Arrowe Park + Clatterbridge non-cancer site"},
            {"label": "Beds", "value": "~700"},
            {"label": "Cancer care", "value": "Delivered adjacent by The Clatterbridge Cancer Centre NHSFT"},
            {"label": "A&E attendances", "value": "~140k/yr"},
            {"label": "ICB", "value": "Cheshire and Merseyside ICB"}
        ],
        "notes": "Drug spend is weighted toward general acute medicine: antibiotics, anticoagulants, critical-care drugs, inhaled respiratory therapies, and diabetes prescribing. Because complex oncology is delivered by a separate trust on an adjacent site, Wirral UTH's HCD pass-through is relatively modest. Biosimilar switch programmes (adalimumab, infliximab) are embedded. Homecare-dispensed rheumatology biologics are routed via regional Cheshire and Merseyside ICB framework contracts.",
        "sources": [
            {"publisher": "Wirral University Teaching Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.wuth.nhs.uk/about-us/publications/annual-reports-and-accounts/"},
            {"publisher": "Cheshire and Merseyside ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.cheshireandmerseyside.nhs.uk/"},
            {"publisher": "NHS England", "title": "Biosimilar medicines commissioning framework", "year": "2024", "url": "https://www.england.nhs.uk/medicines-2/biosimilars/"}
        ],
        "related": ["Wirral University Teaching Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Wirral University Teaching Hospital NHS Foundation Trust"]
    },

    "Drugs costs — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Drug spend at Kingston Hospital — a small-to-mid-size south-west London district-general without tertiary specialties. Complex oncology, cardiac and neurosciences pathways flow to neighbouring St George's and The Royal Marsden. Kingston is a national outlier on maternity volume (high birth rate catchment) and has consistently strong CQC ratings.",
        "beneficiaries": "~320k residents of Kingston, Richmond, Merton and south-west London fringe",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£29.0M"},
            {"label": "Operating revenue", "value": "~£320M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,500"},
            {"label": "CQC rating", "value": "Outstanding — one of few acute trusts rated so"},
            {"label": "Deliveries/year", "value": "~5,500 (high-volume SW London maternity)"},
            {"label": "Tertiary outflow", "value": "Cancer → Marsden; cardiac/neuro → St George's"},
            {"label": "Group model", "value": "Hospital group model with Hounslow & Richmond CHT"},
            {"label": "ICB", "value": "South West London ICB"}
        ],
        "notes": "Drug spend is general-acute weighted: antibiotics, obstetric/anaesthetic agents, standard chemotherapy for locally-delivered solid tumours, and homecare biologics for rheumatology/IBD. Because tertiary oncology and transplant care are delivered elsewhere, HCD pass-through is a smaller share than at neighbouring larger trusts. Maternity-related spend (oxytocin, tranexamic acid, prostaglandins) is disproportionately larger for the trust's size.",
        "sources": [
            {"publisher": "Kingston Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.kingstonhospital.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "CQC", "title": "Kingston Hospital NHS Foundation Trust — inspection reports", "year": "2024", "url": "https://www.cqc.org.uk/provider/RAX"},
            {"publisher": "South West London ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.southwestlondon.icb.nhs.uk/"}
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Kingston Hospital NHS Foundation Trust"]
    },

    "Drugs costs — North Tees and Hartlepool NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "North Tees and Hartlepool NHS Foundation Trust"}],
        "description": "Drug spend across the University Hospital of North Tees (Stockton) and the University Hospital of Hartlepool — a two-site acute trust covering Stockton, Hartlepool and parts of East Durham. Complex cancer, cardiac and neurosciences pathways flow to South Tees (James Cook) and Newcastle.",
        "beneficiaries": "~400k residents of Stockton, Hartlepool and East Durham",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£27.3M"},
            {"label": "Operating revenue", "value": "~£340M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~5,000"},
            {"label": "Sites", "value": "Stockton + Hartlepool"},
            {"label": "A&E attendances", "value": "~140k/yr (Stockton 24/7; Hartlepool urgent care)"},
            {"label": "Tertiary outflow", "value": "Cancer/cardiac/neuro to South Tees + Newcastle"},
            {"label": "Catchment deprivation", "value": "High — Hartlepool among top 20 most deprived LAs"},
            {"label": "ICB", "value": "North East and North Cumbria ICB"}
        ],
        "notes": "Drug spend is dominated by general-acute categories, with solid-tumour SACT delivered locally and complex haematology/radiotherapy referred out. Catchment deprivation drives higher diabetes/COPD/CVD drug volumes than the trust's size alone would predict. Biosimilar uptake across rheumatology/IBD is near-universal. Homecare contract provider performance has been a recurring governance focus in 2023-24 given national Sciensus/Lloyds Clinical disruption.",
        "sources": [
            {"publisher": "North Tees and Hartlepool NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.nth.nhs.uk/about/annual-reports/"},
            {"publisher": "NHS England", "title": "Homecare medicines services — commissioning standards", "year": "2023", "url": "https://www.england.nhs.uk/medicines-2/homecare-medicines-services/"},
            {"publisher": "North East and North Cumbria ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://northeastnorthcumbria.nhs.uk/"}
        ],
        "related": ["North Tees and Hartlepool NHS Foundation Trust", "Clinical Supplies & Drugs — North Tees and Hartlepool NHS Foundation Trust"]
    },

    "Drugs costs — The Princess Alexandra Hospital NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Princess Alexandra Hospital NHS Trust"}],
        "description": "Drug spend at The Princess Alexandra Hospital (Harlow) — a single-site small district-general serving west Essex and east Hertfordshire. Estate age is a known issue (New Hospital Programme candidate); complex cancer, cardiac and specialist work flows to Cambridge University Hospitals, Royal Free and Addenbrooke's.",
        "beneficiaries": "~350k residents of Harlow, Epping Forest, Uttlesford and east Herts fringe",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£26.3M"},
            {"label": "Operating revenue", "value": "~£260M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,500"},
            {"label": "Site", "value": "Princess Alexandra Hospital, Harlow"},
            {"label": "Estate age", "value": "Main building 1965 — under-capacity; New Hospital Programme candidate"},
            {"label": "Tertiary outflow", "value": "Cancer/cardiac/neuro to Cambridge + London"},
            {"label": "A&E attendances", "value": "~130k/yr"},
            {"label": "ICB", "value": "Hertfordshire and West Essex ICB"}
        ],
        "notes": "Drug spend is general-acute weighted with limited HCD pass-through. Biosimilar adoption is mature (adalimumab, infliximab, trastuzumab, rituximab biosimilars near-universal). The trust's capital replacement pipeline (New Hospital Programme — reconfirmed 2023 with revised dates) makes medicines-optimisation CIP a continuous theme. Local GLP-1 RA volume growth has been a notable 2024 pressure.",
        "sources": [
            {"publisher": "The Princess Alexandra Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.pah.nhs.uk/annual-reports/"},
            {"publisher": "DHSC", "title": "New Hospital Programme — updated schedule 2023", "year": "2023", "url": "https://www.gov.uk/government/publications/the-new-hospital-programme"},
            {"publisher": "Hertfordshire and West Essex ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://hertsandwestessex.icb.nhs.uk/"}
        ],
        "related": ["The Princess Alexandra Hospital NHS Trust", "Clinical Supplies & Drugs — The Princess Alexandra Hospital NHS Trust"]
    },

    "Drugs costs — Mid Cheshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Mid Cheshire Hospitals NHS Foundation Trust"}],
        "description": "Drug spend at Leighton Hospital (Crewe) and Victoria Infirmary (Northwich) — a mid-sized Cheshire acute trust. Complex cancer and cardiac pathways flow to Liverpool (Clatterbridge, LHCH) and Manchester (MFT). Leighton is a New Hospital Programme rebuild candidate with substantial RAAC concerns.",
        "beneficiaries": "~320k residents of Crewe, Northwich and south Cheshire",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£24.2M"},
            {"label": "Operating revenue", "value": "~£300M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~4,000"},
            {"label": "Sites", "value": "Leighton (Crewe) + Victoria Infirmary (Northwich)"},
            {"label": "RAAC", "value": "Leighton has extensive RAAC — New Hospital Programme rebuild prioritised"},
            {"label": "Tertiary outflow", "value": "Cancer → Clatterbridge; cardiac → LHCH; complex → MFT"},
            {"label": "A&E attendances", "value": "~100k/yr"},
            {"label": "ICB", "value": "Cheshire and Merseyside ICB"}
        ],
        "notes": "Drug spend is general-acute weighted. Because complex specialist pathways flow off-site, HCD pass-through is modest; biosimilar adoption is mature. RAAC-driven capital uncertainty and estate costs indirectly pressure pharmacy CIP delivery — biosimilar switch completion, homecare rebasing and aseptic efficiency remain the primary medicines-optimisation levers. GLP-1 RA and SGLT2 inhibitor volume growth drove local ICB formulary work in 2024.",
        "sources": [
            {"publisher": "Mid Cheshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.mcht.nhs.uk/about-us/publications/annual-report"},
            {"publisher": "DHSC", "title": "RAAC-affected hospitals — New Hospital Programme prioritisation", "year": "2023", "url": "https://www.gov.uk/government/publications/the-new-hospital-programme"},
            {"publisher": "Cheshire and Merseyside ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.cheshireandmerseyside.nhs.uk/"}
        ],
        "related": ["Mid Cheshire Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Mid Cheshire Hospitals NHS Foundation Trust"]
    },

    "Drugs costs — The Rotherham NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Rotherham NHS Foundation Trust"}],
        "description": "Drug spend at Rotherham Hospital — a single-site district-general plus community services covering the metropolitan borough. Tertiary cancer, cardiac and neurosciences care flows to Sheffield Teaching Hospitals next door.",
        "beneficiaries": "~265k residents of the Metropolitan Borough of Rotherham",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£22.5M"},
            {"label": "Operating revenue", "value": "~£300M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~4,000"},
            {"label": "Site", "value": "Rotherham Hospital (single site) + integrated community services"},
            {"label": "Tertiary outflow", "value": "Most specialist pathways → Sheffield Teaching Hospitals"},
            {"label": "A&E attendances", "value": "~120k/yr"},
            {"label": "Catchment deprivation", "value": "Above-England average (old coalfield communities)"},
            {"label": "ICB", "value": "South Yorkshire ICB"}
        ],
        "notes": "Drug spend is general-acute weighted; specialist oncology and radiotherapy flow to Sheffield. Local SACT outpatient chemo and rheumatology/IBD homecare biologics are the main HCD contributors. Biosimilar programmes (adalimumab, infliximab, rituximab, trastuzumab) are embedded. Community-prescribed drugs are not captured in this trust line — they fall to the South Yorkshire ICB primary-care budget.",
        "sources": [
            {"publisher": "The Rotherham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.therotherhamft.nhs.uk/About_Us/Publications/Annual_Reports/"},
            {"publisher": "South Yorkshire ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://syics.co.uk/"},
            {"publisher": "NHS England", "title": "Biosimilar medicines commissioning framework", "year": "2024", "url": "https://www.england.nhs.uk/medicines-2/biosimilars/"}
        ],
        "related": ["The Rotherham NHS Foundation Trust", "Clinical Supplies & Drugs — The Rotherham NHS Foundation Trust"]
    },

    "Drugs costs — Homerton Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Homerton Healthcare NHS Foundation Trust"}],
        "description": "Drug spend at Homerton Hospital (Hackney) and integrated community services across City & Hackney — a small district-general with nationally significant specialist services in HIV/GU medicine, obstetrics (very high birth volume) and a large neonatal unit. Catchment is one of London's youngest and most ethnically diverse.",
        "beneficiaries": "~300k residents of Hackney and City of London — young, diverse, high-deprivation in places",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£20.5M"},
            {"label": "Operating revenue", "value": "~£380M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~4,000"},
            {"label": "Deliveries/year", "value": "~5,500+ (very high-volume East London maternity)"},
            {"label": "HIV service", "value": "Large HIV outpatient cohort in one of the most affected UK boroughs historically"},
            {"label": "Specialist fertility", "value": "Homerton Fertility Centre — London specialist IVF provider"},
            {"label": "Integrated community", "value": "Community services across City & Hackney"},
            {"label": "ICB", "value": "North East London ICB"}
        ],
        "notes": "Drug spend reflects Homerton's unusual mix: antiretroviral therapy for a substantial HIV cohort (bictegravir/emtricitabine/tenofovir, dolutegravir combinations) is a material HCD line under NHSE specialised commissioning. Maternity drugs (oxytocin, prostaglandins) and neonatal surfactant drive a disproportionate share for the trust's size. Biosimilar adoption mature. Fertility-service drugs (gonadotrophins, progesterone) largely flow through the separate specialist commissioning pathway.",
        "sources": [
            {"publisher": "Homerton Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.homerton.nhs.uk/about-us/publications/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "HIV drugs — specialised commissioning 2024-25", "year": "2024", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/blood-and-infection-group-f/"},
            {"publisher": "North East London ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://northeastlondon.icb.nhs.uk/"}
        ],
        "related": ["Homerton Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs — Homerton Healthcare NHS Foundation Trust"]
    },

    "Drugs costs — Airedale NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Airedale NHS Foundation Trust"}],
        "description": "Drug spend at Airedale General Hospital (Steeton, near Keighley) plus integrated community services — a small district-general serving a mixed urban/rural West Yorkshire catchment. Notable nationally for RAAC concrete issues in the main building (a priority New Hospital Programme rebuild).",
        "beneficiaries": "~200k residents of Craven, Wharfedale, Airedale and South Dales",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£17.9M"},
            {"label": "Operating revenue", "value": "~£220M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,000"},
            {"label": "Site", "value": "Airedale General (Steeton) — substantial RAAC in main fabric"},
            {"label": "New Hospital Programme", "value": "Priority rebuild — one of seven RAAC-confirmed schemes"},
            {"label": "Digital Care Hub", "value": "Pioneering trust-hosted telehealth service"},
            {"label": "Tertiary outflow", "value": "Cancer/cardiac to Bradford + Leeds"},
            {"label": "ICB", "value": "West Yorkshire ICB"}
        ],
        "notes": "Drug spend is general-acute weighted — typical for a ~200k-catchment district-general. Biosimilar programmes mature. The RAAC estate issue does not directly affect drug spend but presses overall financial performance, keeping medicines-optimisation CIP (homecare rebasing, biosimilar switch, aseptic efficiency) firmly on the board agenda. A distinctive feature is the trust's long-established Digital Care Hub (telehealth), which includes remote medicines support for care-home residents.",
        "sources": [
            {"publisher": "Airedale NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.airedale-trust.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "DHSC", "title": "RAAC-affected hospitals — New Hospital Programme prioritisation", "year": "2023", "url": "https://www.gov.uk/government/publications/the-new-hospital-programme"},
            {"publisher": "West Yorkshire ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.wypartnership.co.uk/"}
        ],
        "related": ["Airedale NHS Foundation Trust", "Clinical Supplies & Drugs — Airedale NHS Foundation Trust"]
    },

    "Drugs costs — Tameside and Glossop Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Tameside and Glossop Integrated Care NHS Foundation Trust"}],
        "description": "Drug spend at Tameside General Hospital (Ashton-under-Lyne) plus integrated community services for Tameside and Glossop — a small acute-plus-community provider in Greater Manchester's eastern fringe. Complex cancer and cardiothoracic care flows to Manchester University NHSFT and The Christie.",
        "beneficiaries": "~250k residents of Tameside and Glossop (Derbyshire border)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£10.2M"},
            {"label": "Operating revenue", "value": "~£220M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,000"},
            {"label": "Site", "value": "Tameside General (Ashton-under-Lyne) + community services"},
            {"label": "Integrated model", "value": "Acute + community services in one organisation"},
            {"label": "Tertiary outflow", "value": "Cancer → The Christie; complex → MFT"},
            {"label": "A&E attendances", "value": "~85k/yr"},
            {"label": "ICB", "value": "Greater Manchester ICB (Tameside locality)"}
        ],
        "notes": "Drug spend is small relative to most district-generals in the brief and reflects the trust's limited specialist scope — tertiary oncology, transplant and complex haematology are delivered elsewhere in Greater Manchester. Core lines are general acute (antibiotics, anticoagulants, respiratory, diabetes) plus a modest homecare biologic line for rheumatology/IBD. Biosimilar uptake is high. Greater Manchester's system-wide procurement (one of the earliest mature ICS medicines collaboratives) delivers meaningful per-unit savings.",
        "sources": [
            {"publisher": "Tameside and Glossop Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.tamesidehospital.nhs.uk/about-us/publications.htm"},
            {"publisher": "Greater Manchester ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://gmintegratedcare.org.uk/"},
            {"publisher": "NHS England", "title": "Biosimilar medicines commissioning framework", "year": "2024", "url": "https://www.england.nhs.uk/medicines-2/biosimilars/"}
        ],
        "related": ["Tameside and Glossop Integrated Care NHS Foundation Trust", "Clinical Supplies & Drugs — Tameside and Glossop Integrated Care NHS Foundation Trust"]
    },

    "Drugs costs — East Cheshire NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "East Cheshire NHS Trust"}],
        "description": "Drug spend at Macclesfield District General Hospital plus community services across east Cheshire — a small district-general that is one of the smallest non-specialist acute trusts in England. Complex cancer, cardiac and neurosciences pathways flow to Manchester (Christie, MFT, LHCH).",
        "beneficiaries": "~200k residents of east Cheshire (Macclesfield, Congleton, Knutsford, High Peak fringe)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£8.5M"},
            {"label": "Operating revenue", "value": "~£190M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~2,700"},
            {"label": "Site", "value": "Macclesfield District General + community"},
            {"label": "Organisation scale", "value": "Among smallest non-specialist acute trusts in England"},
            {"label": "Tertiary outflow", "value": "Cancer → Christie; cardiac → LHCH; complex → MFT"},
            {"label": "Planned group arrangement", "value": "Clinical partnerships with MFT discussed since 2023"},
            {"label": "ICB", "value": "Cheshire and Merseyside ICB"}
        ],
        "notes": "Drug spend is unusually small — reflecting the trust's scale and its extensive tertiary outflow to Manchester providers. Core lines are general acute (antibiotics, anticoagulants, respiratory, diabetes) with a modest outpatient SACT volume. Biosimilar switch programmes are mature. The trust's small scale makes individual drug-shortage events (e.g. 2023-24 ADHD stimulants, HRT) proportionately more disruptive than at larger peers.",
        "sources": [
            {"publisher": "East Cheshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.eastcheshire.nhs.uk/About-The-Trust/publications/annual-reports.htm"},
            {"publisher": "Cheshire and Merseyside ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.cheshireandmerseyside.nhs.uk/"},
            {"publisher": "DHSC", "title": "Medicine supply notifications 2024", "year": "2024", "url": "https://www.gov.uk/drug-safety-update"}
        ],
        "related": ["East Cheshire NHS Trust", "Clinical Supplies & Drugs — East Cheshire NHS Trust"]
    },

    "Drugs costs — Birmingham and Solihull Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Birmingham and Solihull Mental Health NHS Foundation Trust"}],
        "description": "Drug spend at one of England's largest specialist mental health trusts — providing adult, older-adult, forensic, secure and addiction services across Birmingham and Solihull (~1.3M catchment). Drug mix is almost entirely psychotropic: antipsychotics, mood stabilisers, antidepressants, depot injections, clozapine (which has extensive monitoring requirements) and opioid-substitution therapy.",
        "beneficiaries": "~1.3M residents of Birmingham and Solihull — one of England's largest MH trust catchments",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£7.2M"},
            {"label": "Operating revenue", "value": "~£290M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~4,000"},
            {"label": "Inpatient beds", "value": "~700 across acute, forensic, secure, older-adult, CAMHS inpatient"},
            {"label": "Catchment", "value": "Birmingham + Solihull (~1.3M people)"},
            {"label": "Drug mix", "value": "Psychotropics only — no HCD oncology, minimal biologics"},
            {"label": "Clozapine service", "value": "Large community + inpatient clozapine monitoring cohort"},
            {"label": "ICB", "value": "Birmingham and Solihull ICB"}
        ],
        "notes": "Drug spend at BSMHFT is a small fraction of trust revenue (~2.5%) — typical for mental health trusts whose cost base is dominated by staff rather than medicines. Key lines include long-acting antipsychotic injections (paliperidone palmitate — Xeplion/Trevicta; aripiprazole LAI — Abilify Maintena), clozapine (with its mandatory haematology monitoring infrastructure), opioid-substitution therapy (methadone, buprenorphine, buprenorphine/naloxone — Suboxone/Espranor) and ADHD stimulants (which faced severe supply disruption in 2023-24). Community prescribing is largely via GPs/ICB, not this line.",
        "sources": [
            {"publisher": "Birmingham and Solihull Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.bsmhft.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NICE", "title": "CG178: Psychosis and schizophrenia in adults — prevention and management", "year": "2014 (updated)", "url": "https://www.nice.org.uk/guidance/cg178"},
            {"publisher": "DHSC", "title": "ADHD stimulant supply notifications 2023-24", "year": "2024", "url": "https://www.gov.uk/drug-safety-update"}
        ],
        "related": ["Birmingham and Solihull Mental Health NHS Foundation Trust", "Clinical Supplies & Drugs — Birmingham and Solihull Mental Health NHS Foundation Trust"]
    },

    "Drugs costs — Lancashire and South Cumbria NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Lancashire and South Cumbria NHS Foundation Trust"}],
        "description": "Drug spend at the mental health and learning disability trust covering Lancashire and South Cumbria — one of the larger geographic MH footprints in England, including the Guild Lodge medium secure unit. Drug mix is psychotropic with LD-specific prescribing and a substantial forensic/secure cohort.",
        "beneficiaries": "~1.8M Lancashire and South Cumbria residents — large, partly rural MH catchment",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£6.6M"},
            {"label": "Operating revenue", "value": "~£380M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~6,500"},
            {"label": "Catchment", "value": "Lancashire + South Cumbria (~1.8M)"},
            {"label": "Guild Lodge", "value": "Medium secure forensic unit (NHSE-commissioned)"},
            {"label": "Drug mix", "value": "Psychotropics + LD/ADHD + opioid substitution"},
            {"label": "CQC history", "value": "Requires Improvement (2023) — improvement trajectory ongoing"},
            {"label": "ICB", "value": "Lancashire and South Cumbria ICB"}
        ],
        "notes": "Drug spend is dominated by LAI antipsychotics, clozapine, SSRIs/SNRIs, mood stabilisers (lithium, valproate under pregnancy-prevention programme), LD-specific prescribing (melatonin, stimulants) and OST. Secure-unit pharmacy has additional controlled-drug infrastructure costs. The trust has managed through industrial action and national stimulant/HRT supply disruption in 2023-24. Drug costs remain a small share of total spend (~1.7%) reflecting the staff-intensive nature of MH care.",
        "sources": [
            {"publisher": "Lancashire and South Cumbria NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.lscft.nhs.uk/about-us/annual-reports/"},
            {"publisher": "NHS England", "title": "Medium secure adult mental health services — service specification", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/mental-health/"},
            {"publisher": "MHRA", "title": "Valproate pregnancy-prevention programme", "year": "2024", "url": "https://www.gov.uk/drug-safety-update/valproate-pregnancy-prevention-programme"}
        ],
        "related": ["Lancashire and South Cumbria NHS Foundation Trust", "Clinical Supplies & Drugs — Lancashire and South Cumbria NHS Foundation Trust"]
    },

    "Drugs costs — Greater Manchester Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Greater Manchester Mental Health NHS Foundation Trust"}],
        "description": "Drug spend at the MH/LD trust serving large parts of Greater Manchester (Manchester, Salford, Trafford, Bolton addictions), plus the Edenfield Centre medium secure service — a specialist unit that has been subject to significant scrutiny (Panorama 2022; ongoing independent review). Drug spend is entirely psychotropic with forensic pharmacy overlay.",
        "beneficiaries": "~1.2M people in Greater Manchester using mental health, LD or addiction services",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£5.7M"},
            {"label": "Operating revenue", "value": "~£410M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~6,500"},
            {"label": "Catchment", "value": "Manchester + Salford + Trafford + Bolton addictions"},
            {"label": "Edenfield Centre", "value": "Medium secure forensic — subject of 2022 Panorama and ongoing independent review"},
            {"label": "Drug mix", "value": "Psychotropics + OST (community drug services) + secure-unit controlled drugs"},
            {"label": "Independent review", "value": "Shoesmith review ongoing (reporting 2024-25)"},
            {"label": "ICB", "value": "Greater Manchester ICB"}
        ],
        "notes": "GMMH's drug spend is largely psychotropic plus a large OST line reflecting its Manchester/Salford addictions contracts (methadone, buprenorphine). Clozapine monitoring service is extensive. Forensic-service controlled-drug governance has intensified since the Edenfield concerns and ongoing independent review — with consequent investment in pharmacy oversight and workforce. Biosimilar opportunities in this setting are limited; the principal CIP levers are formulary adherence, LAI vs oral conversion and OST framework pricing.",
        "sources": [
            {"publisher": "Greater Manchester Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.gmmh.nhs.uk/about-us/annual-reports/"},
            {"publisher": "BBC Panorama", "title": "Undercover Hospital: Patients at Risk", "year": "2022", "url": "https://www.bbc.co.uk/programmes/m001cm5p"},
            {"publisher": "NHS England", "title": "Independent review of Edenfield — terms of reference", "year": "2023", "url": "https://www.england.nhs.uk/"}
        ],
        "related": ["Greater Manchester Mental Health NHS Foundation Trust", "Clinical Supplies & Drugs — Greater Manchester Mental Health NHS Foundation Trust"]
    },

    "Drugs costs — North East London NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "North East London NHS Foundation Trust"}],
        "description": "Drug spend at NELFT — a mental health and community trust delivering MH, LD, CAMHS and community health services across Barking & Dagenham, Havering, Redbridge, Waltham Forest and parts of Essex (Basildon, Brentwood). Drug mix is almost entirely psychotropic + community-nursing-administered drugs.",
        "beneficiaries": "~2M people across 5 North East London boroughs and 2 Essex districts",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£4.6M"},
            {"label": "Operating revenue", "value": "~£490M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~6,500"},
            {"label": "Catchment", "value": "5 NE London boroughs + Essex (Basildon, Brentwood)"},
            {"label": "Scope", "value": "MH + LD + CAMHS + community health (district nursing, health visiting)"},
            {"label": "Drug mix", "value": "Psychotropics + community IV antibiotics + OST"},
            {"label": "CAMHS", "value": "Large service — ADHD stimulant supply was a material 2023-24 challenge"},
            {"label": "ICB", "value": "North East London ICB (+ Mid & South Essex ICB for Essex districts)"}
        ],
        "notes": "NELFT's drug spend includes psychotropics for the MH caseload, ADHD stimulants for the large CAMHS service, OST for community addictions, and community-nurse-administered IV antibiotics (OPAT). The trust was meaningfully affected by the 2023-24 national stimulant supply disruption, requiring brand-switching protocols. Biosimilars are limited in relevance; the main CIP levers are formulary management, LAI uptake and community OPAT efficiency.",
        "sources": [
            {"publisher": "North East London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.nelft.nhs.uk/about-nelft/publications/annual-report/"},
            {"publisher": "DHSC", "title": "ADHD stimulant supply notifications 2023-24", "year": "2024", "url": "https://www.gov.uk/drug-safety-update"},
            {"publisher": "North East London ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://northeastlondon.icb.nhs.uk/"}
        ],
        "related": ["North East London NHS Foundation Trust", "Clinical Supplies & Drugs — North East London NHS Foundation Trust"]
    },

    "Drugs costs — Royal National Orthopaedic Hospital NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Royal National Orthopaedic Hospital NHS Trust"}],
        "description": "Drug spend at the RNOH (Stanmore) — the UK's largest specialist orthopaedic hospital, covering spinal cord injury, bone tumour surgery, paediatric and adult complex orthopaedics, and the London Spinal Cord Injury Centre. Drug mix reflects surgical anaesthesia, post-op analgesia, thromboprophylaxis and sarcoma chemotherapy — not a general acute portfolio.",
        "beneficiaries": "UK-wide tertiary referrals for complex orthopaedic surgery, spinal cord injury and bone sarcoma",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£4.4M"},
            {"label": "Operating revenue", "value": "~£200M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~1,400"},
            {"label": "Site", "value": "Stanmore + Bolsover Street outpatients (relocating)"},
            {"label": "London Spinal Cord Injury Centre", "value": "Large regional SCI rehab unit"},
            {"label": "Sarcoma service", "value": "London Sarcoma Service partnership — complex bone/soft-tissue tumours"},
            {"label": "Drug mix", "value": "Anaesthetic agents, analgesia, LMWH, sarcoma SACT"},
            {"label": "ICB", "value": "North Central London ICB (host)"}
        ],
        "notes": "RNOH's drug bill is modest for a specialist trust because almost all activity is surgical/rehabilitative rather than medical-oncology or long-term infusion-led. Sarcoma SACT (where delivered locally) is the main HCD contributor; the rest is anaesthesia, peri-op antimicrobial prophylaxis, low-molecular-weight heparin thromboprophylaxis and analgesia. Biosimilar opportunities are limited by the drug mix. A new build on the Stanmore site has modernised aseptic dispensing.",
        "sources": [
            {"publisher": "Royal National Orthopaedic Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.rnoh.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "NHS England", "title": "Specialised commissioning — sarcoma service specification", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/"},
            {"publisher": "North Central London ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://northcentrallondon.icb.nhs.uk/"}
        ],
        "related": ["Royal National Orthopaedic Hospital NHS Trust", "Clinical Supplies & Drugs — Royal National Orthopaedic Hospital NHS Trust"]
    },

    "Drugs costs — Hertfordshire Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Hertfordshire Partnership University NHS Foundation Trust"}],
        "description": "Drug spend at HPFT — the mental health and learning disability trust for Hertfordshire, plus Buckinghamshire LD/MH specialist services and specialist services in Norfolk and Essex. Drug mix is entirely psychotropic plus LD-specific prescribing.",
        "beneficiaries": "~1.2M Hertfordshire residents + specialist catchments in Bucks, Norfolk and Essex",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£4.1M"},
            {"label": "Operating revenue", "value": "~£280M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,500"},
            {"label": "Catchment", "value": "Hertfordshire + specialist services in Bucks, Norfolk, Essex"},
            {"label": "CQC rating", "value": "Good/Outstanding — one of few MH trusts consistently Outstanding in specific areas"},
            {"label": "Drug mix", "value": "Psychotropics + LD-specific + ADHD stimulants"},
            {"label": "LD specialist services", "value": "Regional inpatient LD provision"},
            {"label": "ICB", "value": "Hertfordshire and West Essex ICB"}
        ],
        "notes": "HPFT's drug spend is largely antipsychotics (oral + depot), SSRIs/SNRIs, mood stabilisers, clozapine (with extensive haematology monitoring), stimulants and opioid-substitution therapy. LD services use proportionately higher volumes of melatonin and behavioural-phenotype prescribing. The 2023-24 national stimulant supply disruption required brand-switching protocols across CAMHS and adult ADHD services. Drug costs remain a small share of trust revenue (~1.5%).",
        "sources": [
            {"publisher": "Hertfordshire Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.hpft.nhs.uk/about-us/corporate-information/annual-reports-and-accounts/"},
            {"publisher": "CQC", "title": "Hertfordshire Partnership University NHS Foundation Trust — inspection reports", "year": "2024", "url": "https://www.cqc.org.uk/provider/RWR"},
            {"publisher": "DHSC", "title": "ADHD stimulant supply notifications 2023-24", "year": "2024", "url": "https://www.gov.uk/drug-safety-update"}
        ],
        "related": ["Hertfordshire Partnership University NHS Foundation Trust", "Clinical Supplies & Drugs — Hertfordshire Partnership University NHS Foundation Trust"]
    },

    "Drugs costs — Kent and Medway NHS and Social Care Partnership Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Kent and Medway NHS and Social Care Partnership Trust"}],
        "description": "Drug spend at KMPT — the MH/LD trust for Kent and Medway, a large county-footprint mental health provider. Drug mix is exclusively psychotropic plus OST and stimulants.",
        "beneficiaries": "~1.9M residents of Kent and Medway",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£3.8M"},
            {"label": "Operating revenue", "value": "~£260M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,500"},
            {"label": "Catchment", "value": "Kent and Medway (~1.9M)"},
            {"label": "Service scope", "value": "Adult, older-adult, forensic, CAMHS (co-commissioned), LD"},
            {"label": "Drug mix", "value": "Psychotropics + OST + ADHD stimulants"},
            {"label": "CQC history", "value": "Requires Improvement 2023 — improvement plan in delivery"},
            {"label": "ICB", "value": "Kent and Medway ICB"}
        ],
        "notes": "KMPT's drug bill is dominated by long-acting antipsychotic injections, clozapine, antidepressants, lithium and valproate (valproate under MHRA pregnancy-prevention programme), plus methadone and buprenorphine for addictions services. The 2023-24 stimulant and HRT supply disruption required sustained clinical pharmacy input. At ~1.5% of revenue, drug costs remain a small portion of total spend — a typical MH-trust signature.",
        "sources": [
            {"publisher": "Kent and Medway NHS and Social Care Partnership Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.kmpt.nhs.uk/about-us/our-publications/annual-report/"},
            {"publisher": "MHRA", "title": "Valproate pregnancy-prevention programme", "year": "2024", "url": "https://www.gov.uk/drug-safety-update/valproate-pregnancy-prevention-programme"},
            {"publisher": "Kent and Medway ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.kentandmedway.icb.nhs.uk/"}
        ],
        "related": ["Kent and Medway NHS and Social Care Partnership Trust", "Clinical Supplies & Drugs — Kent and Medway NHS and Social Care Partnership Trust"]
    },

    "Drugs costs — Sussex Community NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Sussex Community NHS Foundation Trust"}],
        "description": "Drug spend at Sussex Community NHSFT — a community health provider delivering district nursing, community hospitals, specialist nursing, children's community services and end-of-life care across Brighton & Hove, East Sussex and West Sussex. Drug mix is dominated by community-nurse-administered drugs (IV antibiotics, end-of-life syringe drivers, wound care).",
        "beneficiaries": "~1.6M Sussex residents receiving community, district-nursing or end-of-life care",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£3.6M"},
            {"label": "Operating revenue", "value": "~£200M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,500"},
            {"label": "Service scope", "value": "District nursing + community hospitals + end-of-life + children's community"},
            {"label": "Community hospitals", "value": "Multiple bedded units across Sussex"},
            {"label": "Drug mix", "value": "OPAT antibiotics + syringe drivers + wound/dressings + vaccinations"},
            {"label": "CQC rating", "value": "Outstanding — one of highest-performing community trusts"},
            {"label": "ICB", "value": "Sussex ICB"}
        ],
        "notes": "SCFT's drug bill is small (~1.8% of revenue) and focused on community OPAT antibiotics (ceftriaxone, teicoplanin), end-of-life syringe-driver drugs (diamorphine, midazolam, hyoscine butylbromide, levomepromazine), seasonal vaccinations and wound care. Community providers typically hold a much smaller share of dispensed drug cost than acute trusts — the majority of community prescribing flows through the ICB primary-care pharmacy budget rather than this trust line.",
        "sources": [
            {"publisher": "Sussex Community NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.sussexcommunity.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "CQC", "title": "Sussex Community NHS Foundation Trust — inspection reports", "year": "2024", "url": "https://www.cqc.org.uk/provider/RDR"},
            {"publisher": "NHS England", "title": "Community services outpatient parenteral antimicrobial therapy (OPAT) guidance", "year": "2023", "url": "https://www.england.nhs.uk/"}
        ],
        "related": ["Sussex Community NHS Foundation Trust", "Clinical Supplies & Drugs — Sussex Community NHS Foundation Trust"]
    },

    "Drugs costs — Cornwall Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Cornwall Partnership NHS Foundation Trust"}],
        "description": "Drug spend at Cornwall Partnership NHSFT — the combined mental health and community health provider for Cornwall and the Isles of Scilly. Drug mix blends psychotropics (adult MH, CAMHS, LD, older-adult memory services) with community-nurse-administered medicines (end-of-life, OPAT) given the integrated MH + community model.",
        "beneficiaries": "~570k residents of Cornwall and Isles of Scilly",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£2.5M"},
            {"label": "Operating revenue", "value": "~£250M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,500"},
            {"label": "Service scope", "value": "MH + LD + CAMHS + community health (district nursing, community hospitals)"},
            {"label": "Geography", "value": "Cornwall + Isles of Scilly — dispersed rural/coastal"},
            {"label": "Drug mix", "value": "Psychotropics + end-of-life syringe drivers + OPAT"},
            {"label": "Community hospitals", "value": "14 community hospitals across Cornwall"},
            {"label": "ICB", "value": "NHS Cornwall and Isles of Scilly ICB"}
        ],
        "notes": "The combined MH + community remit gives CPFT a different drug profile from a pure MH trust: antipsychotics, SSRIs, clozapine and OST for MH; plus end-of-life medicines, IV antibiotics, wound dressings and immunisations via community services. The Isles of Scilly supply chain adds logistical complexity (ferry/flight). The 2023-24 ADHD stimulant disruption required sustained pharmacy management across CAMHS and adult ADHD.",
        "sources": [
            {"publisher": "Cornwall Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.cornwallft.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS Cornwall and Isles of Scilly ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.cornwall.nhs.uk/"},
            {"publisher": "DHSC", "title": "ADHD stimulant supply notifications 2023-24", "year": "2024", "url": "https://www.gov.uk/drug-safety-update"}
        ],
        "related": ["Cornwall Partnership NHS Foundation Trust", "Clinical Supplies & Drugs — Cornwall Partnership NHS Foundation Trust"]
    },

    "Drugs costs — Pennine Care NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Pennine Care NHS Foundation Trust"}],
        "description": "Drug spend at Pennine Care NHSFT — the MH/LD trust for five Greater Manchester boroughs (Bury, Oldham, Rochdale, Stockport, Tameside) plus some Cheshire localities. Drug mix is entirely psychotropic + OST.",
        "beneficiaries": "~1.3M residents of five Greater Manchester boroughs plus some Cheshire localities",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£2.4M"},
            {"label": "Operating revenue", "value": "~£240M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~3,000"},
            {"label": "Catchment", "value": "Bury + Oldham + Rochdale + Stockport + Tameside"},
            {"label": "Service scope", "value": "Adult MH + older-adult + CAMHS + LD"},
            {"label": "Drug mix", "value": "Psychotropics + ADHD stimulants + OST"},
            {"label": "Inquest focus", "value": "Edenfield-era parallel inquiries raised governance focus"},
            {"label": "ICB", "value": "Greater Manchester ICB"}
        ],
        "notes": "Pennine Care's drug spend is small (~1% of revenue) — typical of a MH-only trust. Main lines are long-acting antipsychotic injections, clozapine, SSRIs/SNRIs, mood stabilisers, stimulants and OST. The Greater Manchester system-wide medicines collaborative delivers pricing advantages on shared formulary items. The 2023-24 stimulant supply disruption was an active operational focus across CAMHS and adult ADHD teams.",
        "sources": [
            {"publisher": "Pennine Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.penninecare.nhs.uk/annualreports"},
            {"publisher": "Greater Manchester ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://gmintegratedcare.org.uk/"},
            {"publisher": "DHSC", "title": "ADHD stimulant supply notifications 2023-24", "year": "2024", "url": "https://www.gov.uk/drug-safety-update"}
        ],
        "related": ["Pennine Care NHS Foundation Trust", "Clinical Supplies & Drugs — Pennine Care NHS Foundation Trust"]
    },

    "Drugs costs — Leeds and York Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Leeds and York Partnership NHS Foundation Trust"}],
        "description": "Drug spend at LYPFT — the MH/LD trust for Leeds plus specialist services in York (and some national-tier specialist services, e.g. the National Deaf CAMHS service, the Yorkshire Centre for Eating Disorders). Drug mix is psychotropic with specialist-service overlay.",
        "beneficiaries": "~800k residents of Leeds for general MH + national/regional specialist catchments (eating disorders, deaf MH)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£2.2M"},
            {"label": "Operating revenue", "value": "~£210M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~2,900"},
            {"label": "Catchment", "value": "Leeds + York specialist services"},
            {"label": "National services", "value": "National Deaf CAMHS (one of few UK providers)"},
            {"label": "Yorkshire Centre for Eating Disorders", "value": "Regional specialist inpatient + outpatient service"},
            {"label": "Drug mix", "value": "Psychotropics + eating-disorder refeeding + stimulants"},
            {"label": "ICB", "value": "West Yorkshire ICB"}
        ],
        "notes": "LYPFT's drug spend is small but shaped by its specialist-service footprint: in addition to standard antipsychotics/antidepressants/mood stabilisers, the eating-disorder service drives refeeding-related prescribing (thiamine, multivitamins, electrolyte management), and the deaf CAMHS service is included in specialist commissioning arrangements. Clozapine monitoring is material. Drug costs are ~1% of trust revenue.",
        "sources": [
            {"publisher": "Leeds and York Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.leedsandyorkpft.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Specialist eating disorder services — service specification", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/"},
            {"publisher": "West Yorkshire ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://www.wypartnership.co.uk/"}
        ],
        "related": ["Leeds and York Partnership NHS Foundation Trust", "Clinical Supplies & Drugs — Leeds and York Partnership NHS Foundation Trust"]
    },

    "Drugs costs — The Royal Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Royal Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "Drug spend at The Royal Orthopaedic Hospital (Birmingham) — a specialist orthopaedic trust covering elective and revision joint surgery, bone tumour and musculoskeletal oncology (Midlands regional sarcoma service), paediatric orthopaedics and spinal surgery. Drug mix is surgical: anaesthesia, peri-op analgesia, LMWH and sarcoma-related SACT.",
        "beneficiaries": "Midlands regional referrals for complex orthopaedic surgery and bone tumour services",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£1.9M"},
            {"label": "Operating revenue", "value": "~£130M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~1,400"},
            {"label": "Site", "value": "Northfield, Birmingham"},
            {"label": "Sarcoma service", "value": "Midlands regional bone and soft-tissue sarcoma centre"},
            {"label": "Elective focus", "value": "High-volume hip, knee, spinal and paediatric orthopaedic surgery"},
            {"label": "Drug mix", "value": "Anaesthetic agents + LMWH thromboprophylaxis + analgesia + sarcoma SACT"},
            {"label": "ICB", "value": "Birmingham and Solihull ICB (host)"}
        ],
        "notes": "ROH's drug bill is small and reflects an almost entirely surgical casemix: general and regional anaesthetic agents, peri-operative antimicrobial prophylaxis, LMWH for thromboprophylaxis (high-volume joint replacement), multimodal post-op analgesia and controlled drugs. Sarcoma SACT — where delivered on-site — is the main HCD pass-through line. Biosimilar opportunities are limited given the drug mix. The trust is a longstanding contributor to the Getting It Right First Time (GIRFT) orthopaedic best-practice programme.",
        "sources": [
            {"publisher": "The Royal Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.roh.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "NHS England", "title": "GIRFT orthopaedic programme", "year": "2024", "url": "https://gettingitrightfirsttime.co.uk/surgical_specialties/orthopaedic-surgery/"},
            {"publisher": "NHS England", "title": "Sarcoma service specification", "year": "2023", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/"}
        ],
        "related": ["The Royal Orthopaedic Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — The Royal Orthopaedic Hospital NHS Foundation Trust"]
    },

    "Drugs costs — South East Coast Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "South East Coast Ambulance Service NHS Foundation Trust"}],
        "description": "Drug spend at SECAmb — the 999 and NHS 111 ambulance provider for Kent, Surrey, Sussex, north-east Hampshire and parts of London. Drug mix is entirely pre-hospital emergency medicines carried on 700+ emergency vehicles and by HART/air-ambulance clinicians.",
        "beneficiaries": "~4.8M residents of Kent, Surrey, Sussex, NE Hampshire — ~1 million ambulance responses/yr",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · POM for paramedic-administered medicines · MHRA",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£1.5M"},
            {"label": "Operating revenue", "value": "~£330M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~4,500"},
            {"label": "Catchment", "value": "Kent + Surrey + Sussex + NE Hants — ~4.8M people"},
            {"label": "Emergency responses", "value": "~1 million/yr (999 + 111-dispatched)"},
            {"label": "Drug mix", "value": "Morphine, midazolam, adrenaline, tranexamic acid, naloxone, nitrates, salbutamol, paracetamol IV"},
            {"label": "Controlled drug governance", "value": "Extensive — CQC accountable officer oversight of opioid carriage"},
            {"label": "ICB", "value": "Cross-ICB (Kent & Medway, Surrey Heartlands, Sussex, Hampshire & IoW)"}
        ],
        "notes": "Ambulance drug spend is modest in absolute terms but carries unusual governance overhead: controlled-drug carriage across 700+ vehicles, multi-site stock reconciliation and a statutory accountable officer. Key pre-hospital medicines include IV morphine, midazolam, IV paracetamol, adrenaline (anaphylaxis + cardiac arrest), tranexamic acid (major haemorrhage), naloxone (overdose), nitrates (chest pain) and salbutamol (asthma). Drug shortages at manufacturer level flow directly into operational response planning — SECAmb has established alternative-product protocols for known shortages.",
        "sources": [
            {"publisher": "South East Coast Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.secamb.nhs.uk/about_us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Ambulance services — JRCALC clinical guidelines", "year": "2024", "url": "https://aace.org.uk/clinical-practice-supplements/"},
            {"publisher": "MHRA", "title": "Medicines carriage in ambulances — controlled drug guidance", "year": "2023", "url": "https://www.gov.uk/drug-safety-update"}
        ],
        "related": ["South East Coast Ambulance Service NHS Foundation Trust", "Clinical Supplies & Drugs — South East Coast Ambulance Service NHS Foundation Trust"]
    },

    "Drugs costs — Sheffield Health and Social Care NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Sheffield Health and Social Care NHS Foundation Trust"}],
        "description": "Drug spend at SHSC — Sheffield's mental health, learning disability and substance-misuse provider, delivering adult, older-adult, forensic, LD and addictions services. Drug mix is psychotropic + OST.",
        "beneficiaries": "~580k Sheffield residents using mental health, LD or substance-misuse services",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NICE TAs",
        "key_stats": [
            {"label": "Drugs costs 2023-24", "value": "£1.1M"},
            {"label": "Operating revenue", "value": "~£150M (2023-24)"},
            {"label": "Staff (WTE)", "value": "~2,200"},
            {"label": "Catchment", "value": "City of Sheffield (~580k)"},
            {"label": "Service scope", "value": "Adult MH + older-adult + forensic + LD + substance misuse (Sheffield Treatment and Recovery Team)"},
            {"label": "Drug mix", "value": "Psychotropics + OST + ADHD stimulants"},
            {"label": "CQC history", "value": "Requires Improvement (2023) — improvement plan under delivery"},
            {"label": "ICB", "value": "South Yorkshire ICB"}
        ],
        "notes": "SHSC's drug spend is among the smallest in the brief (~0.7% of revenue) — reflecting Sheffield's population size and the MH-only scope. Main lines are antipsychotics (oral + LAI), clozapine with haematology monitoring, SSRIs/SNRIs, mood stabilisers (lithium, valproate with pregnancy-prevention), stimulants and OST (methadone, buprenorphine). The 2023-24 ADHD stimulant disruption required sustained clinical pharmacy input. At this scale, individual high-cost drug initiations (e.g. esketamine TA854 treatment-resistant depression) can materially move the trust's in-year position.",
        "sources": [
            {"publisher": "Sheffield Health and Social Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "year": "2024", "url": "https://www.shsc.nhs.uk/about-us/trust-publications/annual-reports"},
            {"publisher": "NICE", "title": "TA854: Esketamine for treatment-resistant depression", "year": "2024", "url": "https://www.nice.org.uk/guidance/ta854"},
            {"publisher": "South Yorkshire ICB", "title": "Joint Forward Plan 2024", "year": "2024", "url": "https://syics.co.uk/"}
        ],
        "related": ["Sheffield Health and Social Care NHS Foundation Trust", "Clinical Supplies & Drugs — Sheffield Health and Social Care NHS Foundation Trust"]
    },
}
