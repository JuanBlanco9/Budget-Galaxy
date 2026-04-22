# -*- coding: utf-8 -*-
"""Tier A depth-4 enrichment for NHS trust 'Drugs costs' sub-lines (batch D).

47 trust-specific entries. No generic template content — each entry reflects
the trust's specialty mix, formulary posture, and procurement context in
2024-25 (VPAG year 1, industrial-action carryover, GLP-1 rollout,
biosimilar bevacizumab/aflibercept introductions).
"""

NEW = {
    "Drugs costs — Manchester University NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Manchester University NHS Foundation Trust"}],
        "description": "MFT's £297.9M drugs bill — the largest in this batch — is driven by Manchester Royal Infirmary, Wythenshawe (heart & lung transplantation, cystic fibrosis), Saint Mary's (obstetric anti-D and HIV in pregnancy) and Royal Manchester Children's (paediatric oncology, metabolic disorders). The trust runs one of England's biggest homecare medicines programmes via its Homecare Pharmacy team, and is a lead centre for CAR-T delivery commissioned by NHS England Specialised Commissioning.",
        "beneficiaries": "Greater Manchester residents (~750k registered across MFT sites) plus tertiary referrals for transplant, CF, paediatric oncology and haemophilia",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning (CAR-T, transplant immunosuppression)",
        "key_stats": [
            "Drugs costs 2023-24: £297.9M (largest trust drug bill in this batch)",
            "Adult CF service at Wythenshawe: >450 patients on Kaftrio/Symkevi (Vertex)",
            "Heart & lung transplant programme drives high-cost immunosuppressant spend (tacrolimus, basiliximab)",
            "Royal Manchester Children's — lead centre for paediatric CAR-T (tisagenlecleucel)",
            "Saint Mary's — one of England's largest HIV-in-pregnancy cohorts",
            "Part of NOE CPC (NHS North of England Commercial Procurement Collaborative)",
            "VPAG payback receipts (2024) offset branded spend growth",
            "Homecare Pharmacy team manages direct-to-patient HAE and IBD biologics"
        ],
        "notes": "The Wythenshawe CF cohort alone accounts for tens of millions in Vertex CFTR-modulator spend, reimbursed centrally under the NICE TA717 managed access agreement. Biosimilar switches on adalimumab (2018) and infliximab are fully embedded; rituximab and trastuzumab are exclusively biosimilar. CAR-T activity is pass-through funded by NHSE specialised commissioning but drug acquisition still flows through trust accounts.",
        "sources": [
            {"title": "MFT Annual Report & Accounts 2023-24", "url": "https://mft.nhs.uk/the-trust/corporate-reports-and-strategies/"},
            {"title": "NHSE Specialised Commissioning — CAR-T provider sites", "url": "https://www.england.nhs.uk/cancer/cdf/car-t-therapy/"},
            {"title": "NICE TA717 — Ivacaftor–tezacaftor–elexacaftor for cystic fibrosis", "url": "https://www.nice.org.uk/guidance/ta717"}
        ],
        "related": ["Manchester University NHS Foundation Trust", "Clinical Supplies & Drugs — Manchester University NHS Foundation Trust"]
    },
    "Drugs costs — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "STH's £240.9M drugs spend reflects its role as South Yorkshire's tertiary hub at the Royal Hallamshire and Northern General sites, with specialist centres for neurosciences, cardiothoracics, renal transplantation and haematology-oncology. Weston Park Cancer Centre — one of only three dedicated cancer hospitals in England — drives a disproportionate share of high-cost SACT (systemic anti-cancer therapy) spend.",
        "beneficiaries": "South Yorkshire (~640k Sheffield residents) and tertiary referrals from Chesterfield, Rotherham, Doncaster and Bassetlaw",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · Weston Park Cancer Charity research protocols",
        "key_stats": [
            "Drugs costs 2023-24: £240.9M",
            "Weston Park — one of four UK cancer centres with on-site radiopharmacy (lutetium-177 PSMA)",
            "Sheffield Kidney Institute — >900 transplant recipients on immunosuppression",
            "Northern General — major trauma centre driving anti-infective and blood product spend",
            "Lead provider for South Yorkshire Regional Genetics Service (ASOs, gene therapies)",
            "Part of NOE CPC procurement collaborative",
            "Homecare IVIG programme for neurology/haematology indications"
        ],
        "notes": "Weston Park's early-phase trials unit means off-label and Cancer Drugs Fund (CDF) agents appear alongside standard SACT. Lutetium-177 and radium-223 radiopharmaceuticals are procured on short shelf-life contracts. The Royal Hallamshire haemophilia centre is one of England's comprehensive care centres, driving clotting-factor and emicizumab (Hemlibra) spend.",
        "sources": [
            {"title": "Sheffield Teaching Hospitals Annual Report 2023-24", "url": "https://www.sth.nhs.uk/about-us/how-we-are-run/annual-reports"},
            {"title": "NHSE Specialised Commissioning — Haemophilia comprehensive care centres", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/blood-and-infection-group-f/"},
            {"title": "NICE TA880 — Lutetium (177Lu) vipivotide tetraxetan for PSMA-positive hormone-relapsed metastatic prostate cancer", "url": "https://www.nice.org.uk/guidance/ta880"}
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Sheffield Teaching Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "CUH (Addenbrooke's and Rosie) spends £206.3M on drugs, reflecting its role as the East of England's tertiary centre for transplantation, neurosciences, genomics and early-phase oncology trials. The Cambridge Cancer Research UK Centre and the NIHR Cambridge BRC drive substantial investigational medicinal product (IMP) activity alongside NICE-approved high-cost drugs.",
        "beneficiaries": "Cambridgeshire and Peterborough residents plus pan-regional tertiary referrals for liver transplant, bone marrow transplant, complex neurosurgery",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · MHRA CTA framework (for IMPs) · NHSE Specialised Commissioning",
        "key_stats": [
            "Drugs costs 2023-24: £206.3M",
            "Addenbrooke's Liver Unit — one of six UK adult liver transplant centres",
            "Cambridge BMT service — >200 allogeneic transplants/year driving conditioning regimen spend",
            "Rosie Hospital — regional NICU tertiary neonatal service",
            "Host of NIHR Cambridge Clinical Research Facility (early-phase trials)",
            "Part of NHS East of England Commercial Procurement Collaborative",
            "100,000 Genomes Project legacy — rare disease gene therapy referrals"
        ],
        "notes": "Liver transplant immunosuppression (tacrolimus, mycophenolate, basiliximab induction) is a sustained high-cost line. CUH is a designated AAV gene therapy delivery centre (onasemnogene for SMA in infants) via NHSE-commissioned specialised pathway. The trust was a lead site for tocilizumab and dexamethasone usage in RECOVERY trial-derived protocols.",
        "sources": [
            {"title": "CUH Annual Report 2023-24", "url": "https://www.cuh.nhs.uk/about-us/our-performance/annual-report-and-accounts/"},
            {"title": "NHS Blood and Transplant — Adult liver transplant centres", "url": "https://www.odt.nhs.uk/transplantation/liver/"},
            {"title": "NICE TA755 — Onasemnogene abeparvovec for treating pre-symptomatic spinal muscular atrophy", "url": "https://www.nice.org.uk/guidance/ta755"}
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Cambridge University Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — University Hospitals Bristol and Weston NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "University Hospitals Bristol and Weston NHS Foundation Trust"}],
        "description": "UHBW's £183.2M drugs bill spans the Bristol Royal Infirmary, Bristol Haematology and Oncology Centre, Bristol Royal Hospital for Children, St Michael's maternity, and Weston General. The BHOC operates one of South West England's largest SACT services, and Bristol is a lead paediatric congenital cardiac centre commissioned by NHSE.",
        "beneficiaries": "Bristol, North Somerset and South Gloucestershire populations plus South West tertiary paediatric cardiac and haematology-oncology referrals",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHSE Specialised Commissioning (paediatric cardiac, BMT)",
        "key_stats": [
            "Drugs costs 2023-24: £183.2M",
            "BHOC delivers >25,000 SACT episodes annually",
            "Bristol Royal Hospital for Children — one of two SW paediatric BMT centres",
            "Congenital cardiac services — NHSE-designated level 1 centre",
            "Weston merger (2020) broadened acute drug demand across Somerset coast",
            "Member of NHS SW Regional Pharmacy Procurement Specialists",
            "Part of BNSSG ICB joint formulary with secondary care"
        ],
        "notes": "Paediatric congenital cardiac surgery drives milrinone, sildenafil and specialist anticoagulant spend. BHOC's position as the South West SACT lead means novel immune-oncology agents (pembrolizumab, atezolizumab, nivolumab) and ADCs (trastuzumab deruxtecan) are core cost drivers. The Weston site integration adds community-facing generic and antimicrobial demand.",
        "sources": [
            {"title": "UHBW Annual Report 2023-24", "url": "https://www.uhbw.nhs.uk/p/about-us/annual-reports-and-accounts"},
            {"title": "NHSE — Paediatric congenital heart disease specialised service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-e/e05/"},
            {"title": "NICE TA866 — Trastuzumab deruxtecan for HER2-low advanced breast cancer", "url": "https://www.nice.org.uk/guidance/ta866"}
        ],
        "related": ["University Hospitals Bristol and Weston NHS Foundation Trust", "Clinical Supplies & Drugs — University Hospitals Bristol and Weston NHS Foundation Trust"]
    },
    "Drugs costs — Royal Devon University Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Royal Devon University Healthcare NHS Foundation Trust"}],
        "description": "Royal Devon (RD&E Exeter and Northern Devon Healthcare, merged 2022) spends £126.5M on drugs across a geographically dispersed footprint stretching from Exeter to Barnstaple. The trust hosts the South West Genomic Medicine Service Alliance hub at Exeter and runs one of the region's largest outpatient biologics clinics for gastroenterology and rheumatology.",
        "beneficiaries": "Exeter, East Devon, Mid Devon and Northern Devon residents (~620k) plus regional genomics referrals",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · NHS GMS Alliance service specification",
        "key_stats": [
            "Drugs costs 2023-24: £126.5M",
            "Post-merger footprint: >8,000 km² (Exeter to Lynton)",
            "IBD biologics cohort — >1,200 patients on infliximab/adalimumab/vedolizumab biosimilars",
            "Exeter hosts SW Genomic Medicine Service Alliance",
            "Homecare dispensing via trust pharmacy for >2,500 patients",
            "Part of NHS SW Regional Procurement Specialists",
            "Northern Devon site drives rural community hospital drug logistics"
        ],
        "notes": "The 2022 merger introduced operational complexity in formulary harmonisation between the former RD&E and Northern Devon. Biosimilar penetration for adalimumab is >95% (Amgevita/Imraldi/Hyrimoz), consistent with NHSE best-value biologics programme. Rural dispensing to community hospitals (Tiverton, Okehampton, Honiton, Bideford, Ilfracombe) creates inventory carrying costs not seen at single-site trusts.",
        "sources": [
            {"title": "Royal Devon Annual Report 2023-24", "url": "https://www.royaldevon.nhs.uk/about-us/publications/annual-reports/"},
            {"title": "NHSE — Best value biological medicines: adalimumab", "url": "https://www.england.nhs.uk/commissioning/biosimilars/"},
            {"title": "NHS Genomic Medicine Service — South West GMS Alliance", "url": "https://www.england.nhs.uk/genomics/nhs-genomic-med-service/"}
        ],
        "related": ["Royal Devon University Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs — Royal Devon University Healthcare NHS Foundation Trust"]
    },
    "Drugs costs — The Christie NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Christie NHS Foundation Trust"}],
        "description": "The Christie is a pure-play cancer specialist trust — virtually all of its £122.0M drugs spend is SACT, supportive care and clinical trial IMPs. It is one of Europe's largest single-site cancer centres, delivers proton beam therapy (one of two NHSE-commissioned English centres), and runs the largest early-phase trials portfolio in the UK.",
        "beneficiaries": "2.7M population of Greater Manchester, Cheshire and parts of the North West served by The Christie's catchment",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · NHSE Specialised Commissioning (systemic anti-cancer therapy, CAR-T, proton beam therapy)",
        "key_stats": [
            "Drugs costs 2023-24: £122.0M (NHS Specialist — cancer)",
            ">60,000 chemotherapy episodes per year",
            "One of two NHSE proton beam therapy centres (2018-)",
            "Largest UK early-phase trials unit (>300 trials open)",
            "Designated CAR-T delivery centre (tisagenlecleucel, axicabtagene ciloleucel, brexucabtagene)",
            "Lead centre for MHRA Innovative Licensing and Access Pathway oncology pilots",
            "VPAG 2024 oncology carve-out: relevant for high-cost branded agents",
            "Homecare oral oncology service (abiraterone, enzalutamide, olaparib) via Christie Pharmacy Ltd"
        ],
        "notes": "The Christie's wholly-owned subsidiary Christie Pharmacy Ltd supplies homecare oral oncology direct to patients, booking the margin back to the trust. Cancer Drugs Fund managed-access drugs (tagged as pass-through) sit alongside NICE-approved tariff-excluded SACT. As a single-specialty trust, there is no dilution from general-acute drug demand — every line is oncology, supportive care (antiemetics, G-CSF filgrastim/pegfilgrastim biosimilars), or palliative.",
        "sources": [
            {"title": "The Christie Annual Report 2023-24", "url": "https://www.christie.nhs.uk/about-us/corporate-information/publications/annual-reports-and-summaries"},
            {"title": "NHSE — Proton beam therapy service", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-b/b01/"},
            {"title": "NHSE Cancer Drugs Fund managed access list", "url": "https://www.england.nhs.uk/cancer/cdf/"}
        ],
        "related": ["The Christie NHS Foundation Trust", "Clinical Supplies & Drugs — The Christie NHS Foundation Trust"]
    },
    "Drugs costs — Great Ormond Street Hospital for Children NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Great Ormond Street Hospital for Children NHS Foundation Trust"}],
        "description": "GOSH's £111.5M drugs bill is the largest of any English paediatric specialist trust. As the national tertiary and quaternary referral centre for rare paediatric disease, GOSH delivers gene therapies (Zolgensma for SMA, Libmeldy for MLD, Strimvelis legacy patients), BMT conditioning, and metabolic specialty drugs that have no equivalent at general hospitals.",
        "beneficiaries": "Children from across England (and UK/overseas) with rare and complex conditions; national referral centre status",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · NHSE Specialised Commissioning (>80% of GOSH activity) · Orbis/SMA pathways",
        "key_stats": [
            "Drugs costs 2023-24: £111.5M (NHS Specialist — children's)",
            "AAV gene therapy delivery centre: Zolgensma (SMA), Libmeldy (MLD), Upstaza (AADC deficiency)",
            "Lysosomal storage disorders — one of two paediatric ERT centres with Manchester",
            "Paediatric BMT activity — largest UK volume",
            "Host of NIHR GOSH BRC (rare disease trials)",
            "Zayed Centre for Research into Rare Disease in Children",
            "Part of Medicines for Children Research Network legacy",
            "Homecare ERT infusions (alglucosidase, laronidase, agalsidase) for regional patients"
        ],
        "notes": "Single-dose gene therapies carry list prices of £1.79M (Zolgensma) to £2.8M (Libmeldy) — one patient materially moves the annual drug line. Enzyme replacement therapy for MPS, Gaucher and Pompe disease is chronic lifetime-cost. GOSH operates under a specific NHSE highly specialised technologies (HST) funding envelope for ultra-rare indications that sits outside routine tariff.",
        "sources": [
            {"title": "GOSH Annual Report 2023-24", "url": "https://www.gosh.nhs.uk/about-us/corporate-information/annual-report-and-accounts/"},
            {"title": "NICE TA588 — Onasemnogene abeparvovec (Zolgensma) for SMA", "url": "https://www.nice.org.uk/guidance/ta588"},
            {"title": "NHSE Highly Specialised Services", "url": "https://www.england.nhs.uk/commissioning/spec-services/highly-spec-services/"}
        ],
        "related": ["Great Ormond Street Hospital for Children NHS Foundation Trust", "Clinical Supplies & Drugs — Great Ormond Street Hospital for Children NHS Foundation Trust"]
    },
    "Drugs costs — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "St George's (Tooting, south-west London) spends £100.8M on drugs as a major acute teaching trust and the South West London & Surrey trauma network hub. Specialist services include cardiothoracic surgery, neurosurgery (one of London's four neurosciences centres) and the South West Thames Regional Genetics Service.",
        "beneficiaries": "3.5M people in SW London and Surrey for trauma and specialist services; ~500k local catchment",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · NHSE Specialised Commissioning (neuro, cardiothoracic) · London Procurement Partnership",
        "key_stats": [
            "Drugs costs 2023-24: £100.8M",
            "Major Trauma Centre for SW London / Surrey",
            "One of four London adult neurosurgery centres",
            "Cardiothoracic service — >1,200 cardiac surgical procedures/year",
            "Atkinson Morley neurosciences wing — neuro-oncology biologics user",
            "Part of London Procurement Partnership (LPP) consortium",
            "Homecare IBD/rheumatology biologics for ~1,500 patients",
            "Sub-specialist infectious diseases (HIV, TB) clinics"
        ],
        "notes": "The trauma role drives fibrinogen concentrate, prothrombin complex concentrate (Octaplex/Beriplex) and tranexamic acid spend. The HIV service at the Courtyard Clinic uses first-line InSTI-based ART (bictegravir/tenofovir alafenamide/emtricitabine) under NHSE HIV commissioning. Cardiothoracic post-op anticoagulation and pulmonary hypertension agents (bosentan, sildenafil, macitentan) represent stable high-cost lines.",
        "sources": [
            {"title": "St George's Annual Report 2023-24", "url": "https://www.stgeorges.nhs.uk/about/publications/annual-report-and-accounts/"},
            {"title": "London Procurement Partnership", "url": "https://www.lpp.nhs.uk/"},
            {"title": "NHSE HIV clinical reference group", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/blood-and-infection-group-f/f03/"}
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — St George's University Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — East Kent Hospitals University NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "East Kent Hospitals University NHS Foundation Trust"}],
        "description": "EKHUFT's £95.4M drugs spend covers three acute sites (William Harvey Ashford, Queen Elizabeth The Queen Mother Margate, Kent & Canterbury) and a dispersed East Kent catchment. The trust provides the county's tertiary vascular, renal and cancer services, and serves a coastal population with above-average cardiovascular and COPD prevalence.",
        "beneficiaries": "East Kent residents (~760k) across Ashford, Canterbury, Dover, Folkestone, Thanet",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Kent & Medway ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £95.4M",
            "Three acute sites + satellite dialysis units (Canterbury, Dover, Folkestone)",
            "Kent Cancer Centre at Maidstone is not EKHUFT — EKHUFT runs day-case SACT locally",
            "Renal replacement — >600 patients on haemodialysis/peritoneal",
            "Coastal demographic drives COPD inhaler and cardiovascular spend",
            "Part of NHS South East Regional Pharmacy Procurement",
            "Homecare biologics service for rheumatology/IBD cohorts"
        ],
        "notes": "Multi-site logistics inflate pharmacy distribution costs. Renal services drive darbepoetin, iron sucrose (Venofer) and phosphate binder (sevelamer, lanthanum) spend. EKHUFT was under regulatory scrutiny post-Kirkup review (2022) on maternity safety — anti-D, magnesium sulphate and oxytocin prescribing sit within obstetric governance. The trust is part of the Kent & Medway ICB joint formulary aligned with MTW and Medway.",
        "sources": [
            {"title": "EKHUFT Annual Report 2023-24", "url": "https://www.ekhuft.nhs.uk/patients-and-visitors/about-us/publications/annual-reports/"},
            {"title": "Kent & Medway Joint Formulary", "url": "https://www.kmformulary.nhs.uk/"},
            {"title": "Kirkup Review — Independent Investigation into East Kent Maternity Services (2022)", "url": "https://www.gov.uk/government/publications/maternity-and-neonatal-services-in-east-kent-reading-the-signals-report"}
        ],
        "related": ["East Kent Hospitals University NHS Foundation Trust", "Clinical Supplies & Drugs — East Kent Hospitals University NHS Foundation Trust"]
    },
    "Drugs costs — Chelsea and Westminster Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
        "description": "Chelsea and Westminster (two sites: Chelsea and West Middlesex) has an £84.9M drugs bill disproportionately shaped by its nationally-recognised HIV service (one of Europe's largest) and its sexual & reproductive health 56 Dean Street outreach clinic. The trust also runs one of London's busiest maternity units and a major burns service.",
        "beneficiaries": "Chelsea, Fulham, Hammersmith, Ealing, Hounslow populations plus pan-London HIV/SRH cohort",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · NHSE HIV clinical commissioning policy · PrEP service specification",
        "key_stats": [
            "Drugs costs 2023-24: £84.9M",
            "~9,000 HIV outpatients — one of Europe's largest cohorts",
            "56 Dean Street — UK's busiest SRH / PrEP clinic",
            "London-wide HIV pre-exposure prophylaxis (PrEP) delivery via NHSE pathway",
            "West Middlesex — >6,000 deliveries/year drives obstetric drug spend",
            "Burns unit — anti-infective and analgesic demand",
            "Part of London Procurement Partnership",
            "Neonatal ICU — surfactant, caffeine citrate, paediatric antimicrobial use"
        ],
        "notes": "HIV antiretrovirals (predominantly generic tenofovir disoproxil/emtricitabine and branded bictegravir-based Biktarvy) are centrally commissioned by NHSE and represent the single largest high-cost line. PrEP (tenofovir/emtricitabine generic) has been a routine NHS offering since 2020. Cabotegravir-LA long-acting injectable (NICE TA807) is being introduced for selected patients. Biosimilar adoption (adalimumab, trastuzumab) is fully embedded.",
        "sources": [
            {"title": "Chelsea and Westminster Annual Report 2023-24", "url": "https://www.chelwest.nhs.uk/about-us/corporate-information/annual-reports"},
            {"title": "NHSE — HIV pre-exposure prophylaxis (PrEP) routine commissioning", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/blood-and-infection-group-f/f03/"},
            {"title": "NICE TA807 — Cabotegravir with rilpivirine for HIV", "url": "https://www.nice.org.uk/guidance/ta807"}
        ],
        "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Chelsea and Westminster Hospital NHS Foundation Trust"]
    },
    "Drugs costs — The Royal Wolverhampton NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Royal Wolverhampton NHS Trust"}],
        "description": "RWT's £77.9M drugs spend spans New Cross Hospital (acute tertiary services including neonatal ICU and heart & lung centre), Cannock Chase Hospital and a growing primary-care integration portfolio. The trust is one of England's few acute trusts also operating GP practices (Vertical Integration model), which creates an unusually broad primary-secondary formulary interface.",
        "beneficiaries": "Wolverhampton, South Staffordshire and Cannock Chase residents (~400k) plus vertical-integration GP list (~70k)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NICE TAs · Black Country ICB joint formulary · GMS contract (for integrated practices)",
        "key_stats": [
            "Drugs costs 2023-24: £77.9M",
            "Vertical Integration: operates multiple Wolverhampton GP practices",
            "Heart & Lung Centre at New Cross — PCI, cardiothoracic surgery",
            "Neonatal ICU — regional level 3 unit",
            "Diabetes hub — high GLP-1 RA (semaglutide, tirzepatide) interface with primary care",
            "Renal replacement service with satellite unit",
            "Part of NHS Midlands Regional Pharmacy Procurement",
            "Homecare biologics for rheumatology/IBD"
        ],
        "notes": "The vertical integration with GP practices means RWT directly experiences the GLP-1 RA supply constraints that dominated 2023-24 (semaglutide Ozempic/Wegovy rationing under DHSC National Patient Safety Alert). Heart-failure drugs (sacubitril/valsartan, dapagliflozin, empagliflozin) and PCI antithrombotics (ticagrelor, prasugrel) are high-volume lines. The trust is integrated into the Black Country ICB joint formulary with Dudley, Sandwell and Walsall.",
        "sources": [
            {"title": "RWT Annual Report 2023-24", "url": "https://www.royalwolverhampton.nhs.uk/about-us/corporate-information/"},
            {"title": "Black Country ICB Joint Area Prescribing Committee", "url": "https://blackcountry.icb.nhs.uk/"},
            {"title": "DHSC National Patient Safety Alert — GLP-1 RA shortage (2023)", "url": "https://www.cas.mhra.gov.uk/"}
        ],
        "related": ["The Royal Wolverhampton NHS Trust", "Clinical Supplies & Drugs — The Royal Wolverhampton NHS Trust"]
    },
    "Drugs costs — East And North Hertfordshire NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "East And North Hertfordshire NHS Trust"}],
        "description": "ENHT's £73.6M drugs bill is shaped decisively by its hosting of Mount Vernon Cancer Centre at Northwood — a regional tertiary oncology and radiotherapy centre serving ~2M people across NW London, Herts, Beds and Bucks. Acute services at Lister (Stevenage) and the New QEII (Welwyn Garden City) add the general-acute baseline.",
        "beneficiaries": "East & North Hertfordshire residents (~600k) plus Mount Vernon's ~2M pan-regional cancer catchment",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · NHSE Specialised Commissioning (Mount Vernon SACT/radiotherapy)",
        "key_stats": [
            "Drugs costs 2023-24: £73.6M",
            "Mount Vernon Cancer Centre — ~2M catchment",
            "Lister Hospital — main acute site (Stevenage)",
            "SACT activity pushes drug share well above typical district-general ratio",
            "Mount Vernon future — reconfiguration proposals under NHSE review since 2021",
            "Part of NHS East of England Regional Procurement",
            "Homecare oral anticancer drugs dispensed via MVCC Pharmacy",
            "Radiopharmacy on-site for lutetium/radium therapies"
        ],
        "notes": "Mount Vernon's catchment includes parts of NW London, Buckinghamshire and Bedfordshire, so ENHT's drug bill is disproportionate to its local population. Immuno-oncology agents (pembrolizumab, nivolumab, atezolizumab) and HER2-targeted therapies (trastuzumab biosimilar, T-DXd, tucatinib) are primary cost drivers. The long-running reconfiguration debate about moving Mount Vernon services to a new site creates capital/operational uncertainty but has not changed drug demand.",
        "sources": [
            {"title": "ENHT Annual Report 2023-24", "url": "https://www.enherts-tr.nhs.uk/about-us/how-we-are-run/annual-reports/"},
            {"title": "Mount Vernon Cancer Centre review (NHSE)", "url": "https://www.england.nhs.uk/east-of-england/mount-vernon-cancer-centre/"},
            {"title": "NICE TA1015 — Tucatinib with trastuzumab and capecitabine for HER2-positive breast cancer", "url": "https://www.nice.org.uk/guidance/ta1015"}
        ],
        "related": ["East And North Hertfordshire NHS Trust", "Clinical Supplies & Drugs — East And North Hertfordshire NHS Trust"]
    },
    "Drugs costs — Bedfordshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Bedfordshire Hospitals NHS Foundation Trust"}],
        "description": "Bedfordshire Hospitals (Bedford Hospital and Luton & Dunstable, merged 2020) runs a £70.6M drugs budget across two acute sites serving contrasting populations — Bedford's older rural catchment and Luton's younger, highly-diverse urban community. The trust is the tertiary provider for much of the BLMK ICB system.",
        "beneficiaries": "Bedford, Central Bedfordshire and Luton residents (~720k)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · BLMK ICB joint formulary",
        "key_stats": [
            "Drugs costs 2023-24: £70.6M",
            "Two-site trust (Bedford + Luton & Dunstable, merged 2020)",
            "Luton — >6,000 deliveries/year (one of busiest non-London units)",
            "Ethnic diversity (Luton) drives haemoglobinopathy service demand",
            "Oncology day unit on each site",
            "Part of NHS East of England Regional Procurement",
            "Diabetes cohort drives GLP-1 RA and SGLT2 inhibitor interface",
            "Post-merger formulary harmonisation completed 2023"
        ],
        "notes": "Luton's obstetric volume drives high consumption of oxytocin, misoprostol, magnesium sulphate and anti-D. The haemoglobinopathy service (sickle-cell, thalassaemia) uses hydroxycarbamide, deferasirox (Exjade) chelation and transfusion support. Post-merger formulary integration completed in 2023, with Luton's historic biosimilar lead pace adopted trust-wide.",
        "sources": [
            {"title": "Bedfordshire Hospitals Annual Report 2023-24", "url": "https://www.bedfordshirehospitals.nhs.uk/about-us/publications/annual-reports/"},
            {"title": "BLMK ICB — Joint Formulary", "url": "https://www.blmkformulary.nhs.uk/"},
            {"title": "NHSE — Sickle cell disease service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/blood-and-infection-group-f/f05/"}
        ],
        "related": ["Bedfordshire Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Bedfordshire Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — South Tyneside and Sunderland NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "South Tyneside and Sunderland NHS Foundation Trust"}],
        "description": "STSFT's £63.1M drugs spend serves Sunderland Royal Hospital (tertiary neurosciences, stroke, major trauma) and South Tyneside District Hospital. Sunderland is a regional stroke thrombectomy centre within the North East Integrated Stroke Delivery Network, and the trust hosts specialist ophthalmology including the North East's main sub-tenon anti-VEGF service.",
        "beneficiaries": "Sunderland and South Tyneside populations (~440k) plus regional stroke and ophthalmology referrals",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · North East & North Cumbria ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £63.1M",
            "Sunderland Royal — regional hyperacute stroke unit with thrombectomy",
            "South Tyneside — integrated acute/community site",
            "Ophthalmology — large anti-VEGF (ranibizumab/aflibercept) cohort",
            "Stroke alteplase/tenecteplase and edoxaban/apixaban spend",
            "Member of NOE CPC procurement collaborative",
            "Homecare biologics service",
            "Biosimilar aflibercept launch Q3 2024 — switch programme active"
        ],
        "notes": "The Q3 2024 launch of biosimilar aflibercept (Yesafili/Opuviz) is particularly significant for STSFT given its large AMD/DMO ophthalmology cohort — the trust is one of the early adopters under NHSE best-value biologics guidance. Stroke thrombectomy volume drives tenecteplase/alteplase and antiplatelet switching (ticagrelor, clopidogrel). The North East ICB operates a strongly biosimilar-first formulary.",
        "sources": [
            {"title": "STSFT Annual Report 2023-24", "url": "https://www.stsft.nhs.uk/about-us/publications/annual-reports-accounts"},
            {"title": "NHSE — Best value biological medicines: aflibercept (2024)", "url": "https://www.england.nhs.uk/commissioning/biosimilars/"},
            {"title": "North East & North Cumbria ICB", "url": "https://northeastnorthcumbria.nhs.uk/"}
        ],
        "related": ["South Tyneside and Sunderland NHS Foundation Trust", "Clinical Supplies & Drugs — South Tyneside and Sunderland NHS Foundation Trust"]
    },
    "Drugs costs — Blackpool Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Blackpool Teaching Hospitals NHS Foundation Trust"}],
        "description": "Blackpool Teaching Hospitals' £56.8M drugs spend supports Blackpool Victoria Hospital and integrated community services on the Fylde Coast. The trust hosts the Lancashire Cardiac Centre — the county's tertiary cardiothoracic hub performing PCI, cardiac surgery and electrophysiology — which drives a disproportionate share of cardiovascular drug spend.",
        "beneficiaries": "Blackpool, Fylde and Wyre populations (~330k) plus pan-Lancashire cardiac referrals",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Lancashire and South Cumbria ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £56.8M",
            "Lancashire Cardiac Centre — tertiary PCI and cardiac surgery hub",
            "~2,000 PCI procedures per year drives antithrombotic spend",
            "Blackpool — England's highest male CVD mortality (ONS)",
            "Integrated community services include care home prescribing liaison",
            "Member of NOE CPC procurement collaborative",
            "Coastal demographic — high COPD inhaler and opioid prevalence",
            "Homecare IBD/rheumatology biologics"
        ],
        "notes": "Blackpool's population has one of England's highest CVD mortality rates (ONS), so statin, antihypertensive and SGLT2 inhibitor (dapagliflozin, empagliflozin) spend — while mostly primary-care — spills into secondary-care post-PCI and heart-failure clinics. The Cardiac Centre's electrophysiology service uses amiodarone, flecainide and DOACs at volume. Community-integrated services mean the trust dispenses end-of-life drugs (morphine, midazolam, glycopyrronium) in the community under care-home support models.",
        "sources": [
            {"title": "Blackpool Teaching Hospitals Annual Report 2023-24", "url": "https://www.bfwh.nhs.uk/about-the-trust/publications/annual-report-and-accounts/"},
            {"title": "ONS — Avoidable mortality in the UK", "url": "https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/causesofdeath/bulletins/avoidablemortalityinenglandandwales/latest"},
            {"title": "Lancashire Cardiac Centre service summary", "url": "https://www.bfwh.nhs.uk/departments/cardiology/"}
        ],
        "related": ["Blackpool Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Blackpool Teaching Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "ELHT's £55.3M drugs bill supports Royal Blackburn Teaching Hospital, Burnley General Teaching Hospital and community sites serving a Pennine Lancashire population with above-average deprivation and high TB/diabetes prevalence. The trust runs a notable respiratory service reflecting legacy textile-industry occupational disease.",
        "beneficiaries": "East Lancashire residents of Blackburn, Burnley, Hyndburn, Pendle, Ribble Valley, Rossendale (~530k)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Lancashire and South Cumbria ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £55.3M",
            "Royal Blackburn + Burnley General two-site acute model",
            "Notably high TB notification rate (Blackburn with Darwen)",
            "Diabetes specialist service — high South Asian cohort",
            "Respiratory service — occupational and inner-city COPD mix",
            "Member of NOE CPC procurement collaborative",
            "Homecare biologics dispensed in partnership with ICB",
            "BDC (Burnley Day Case) oncology unit"
        ],
        "notes": "Elevated TB notifications (>15/100k in Blackburn with Darwen, among England's highest) drive isoniazid, rifampicin, ethambutol, pyrazinamide and bedaquiline usage under NHSE-commissioned TB service specification. The South Asian heritage of much of the population (particularly Pakistani-heritage in Blackburn/Burnley) correlates with higher diabetes prevalence and thus GLP-1 RA/SGLT2i demand at the specialist interface.",
        "sources": [
            {"title": "ELHT Annual Report 2023-24", "url": "https://www.elht.nhs.uk/about-us/corporate-publications"},
            {"title": "UKHSA — Tuberculosis in England annual report", "url": "https://www.gov.uk/government/publications/tuberculosis-in-england-annual-report"},
            {"title": "NICE NG33 — Tuberculosis", "url": "https://www.nice.org.uk/guidance/ng33"}
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Clinical Supplies & Drugs — East Lancashire Hospitals NHS Trust"]
    },
    "Drugs costs — The Mid Yorkshire Hospitals NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Mid Yorkshire Hospitals NHS Trust"}],
        "description": "Mid Yorks' £52.6M drugs spend serves Pinderfields (Wakefield — major trauma-feeder site with regional spinal injuries centre), Dewsbury & District, and Pontefract hospitals. The trust's regional spinal injuries service and burns care at Pinderfields drive a specialist drug profile alongside general acute demand. Note: Mid Yorks was renamed 'Mid Yorkshire Teaching NHS Trust' in 2023.",
        "beneficiaries": "Wakefield, Kirklees (Dewsbury) and Five Towns (Pontefract) populations (~540k) plus regional spinal/burns referrals",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · West Yorkshire ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £52.6M",
            "Pinderfields — Yorkshire Regional Spinal Injuries Centre",
            "Pinderfields Burns Unit — regional adult & paediatric",
            "Three acute sites (Pinderfields, Dewsbury, Pontefract)",
            "Renamed Mid Yorkshire Teaching NHS Trust (2023)",
            "Member of NOE CPC procurement collaborative",
            "West Yorkshire Association of Acute Trusts (WYAAT) partner",
            "Homecare dispensing for chronic conditions"
        ],
        "notes": "Spinal injuries service drives baclofen (including intrathecal), botulinum toxin for spasticity, and antibiotic prophylaxis for neurogenic bladder. The burns unit uses specialist anti-infectives (silver-impregnated dressings, systemic antifungals) and high-volume analgesics. Part of the WYAAT collaborative alongside Leeds, Bradford, Calderdale & Huddersfield and Airedale — gives procurement leverage comparable to larger single trusts.",
        "sources": [
            {"title": "Mid Yorkshire Teaching Annual Report 2023-24", "url": "https://www.midyorks.nhs.uk/annual-reports"},
            {"title": "NHSE — Spinal cord injury services specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d13/"},
            {"title": "West Yorkshire Association of Acute Trusts", "url": "https://www.wyhpartnership.co.uk/our-priorities/west-yorkshire-association-acute-trusts"}
        ],
        "related": ["The Mid Yorkshire Hospitals NHS Trust", "Clinical Supplies & Drugs — The Mid Yorkshire Hospitals NHS Trust"]
    },
    "Drugs costs — Lewisham and Greenwich NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Lewisham and Greenwich NHS Trust"}],
        "description": "LGT's £49.5M drugs budget covers University Hospital Lewisham and Queen Elizabeth Hospital Woolwich, serving a diverse and relatively young South East London population. The trust has one of SE London's busiest maternity services (>8,000 combined deliveries) and a sickle cell cohort shaped by its Black African and Caribbean heritage patient base.",
        "beneficiaries": "Lewisham, Greenwich and Bexley residents (~830k combined)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · SE London ICB joint formulary · London Procurement Partnership",
        "key_stats": [
            "Drugs costs 2023-24: £49.5M",
            "Two sites: University Hospital Lewisham + Queen Elizabeth Woolwich",
            "Combined maternity — >8,000 deliveries/year",
            "Active sickle cell/thalassaemia service (SE London cohort)",
            "Part of London Procurement Partnership (LPP)",
            "SE London ICB — joint formulary with GSTT, KCH, SLaM",
            "Paediatric A&E — both sites — drives paediatric antimicrobial spend",
            "Homecare rheumatology/IBD biologics"
        ],
        "notes": "Sickle cell disease service uses hydroxycarbamide at volume and has increasing exposure to crizanlizumab (NICE TA743, though withdrawn 2023) and voxelotor (TA878) under NHSE haemoglobinopathy commissioning. The trust's paediatric population drives seasonal RSV nirsevimab roll-out (from autumn 2024). Maternity volume drives oxytocin, magnesium sulphate, misoprostol and anti-D immunoglobulin demand.",
        "sources": [
            {"title": "Lewisham and Greenwich Annual Report 2023-24", "url": "https://www.lewishamandgreenwich.nhs.uk/about-us/our-publications"},
            {"title": "NHSE — Haemoglobinopathies service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/blood-and-infection-group-f/f05/"},
            {"title": "NICE TA878 — Voxelotor for sickle cell disease", "url": "https://www.nice.org.uk/guidance/ta878"}
        ],
        "related": ["Lewisham and Greenwich NHS Trust", "Clinical Supplies & Drugs — Lewisham and Greenwich NHS Trust"]
    },
    "Drugs costs — Torbay and South Devon NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Torbay and South Devon NHS Foundation Trust"}],
        "description": "Torbay and South Devon is one of England's few fully integrated care trusts — acute, community and adult social care under one roof since 2015. Its £45.0M drugs spend reflects Torbay Hospital's acute drug demand plus an unusual volume of community-dispensed end-of-life and chronic-disease medicines delivered directly to patients' homes or care homes.",
        "beneficiaries": "Torbay (Torquay, Paignton, Brixham) and South Devon residents (~286k), with older-than-average demographic",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Care Act 2014 (social care integration) · NICE TAs · Devon ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £45.0M",
            "Fully integrated acute/community/social care trust (since 2015)",
            "Over-65 population share — ~27% (one of England's oldest)",
            "Torbay Hospital — major coastal district general",
            "Integrated community pharmacy service serving care homes",
            "Member of NHS SW Regional Pharmacy Procurement",
            "End-of-life drug volume disproportionate to acute peers",
            "Dementia services — anticholinesterase (donepezil, rivastigmine, memantine) caseload"
        ],
        "notes": "The integration model means Torbay's drug spend includes items that at other trusts sit in community provider or social-care budgets — palliative-care syringe drivers (morphine, midazolam, glycopyrronium, levomepromazine), care-home antibiotic prescribing, and anticipatory prescribing packs. The age profile drives osteoporosis agents (denosumab, zoledronic acid, teriparatide — NICE TAs 464/204) and Parkinson's disease drug demand.",
        "sources": [
            {"title": "Torbay and South Devon Annual Report 2023-24", "url": "https://www.torbayandsouthdevon.nhs.uk/about-us/our-publications/"},
            {"title": "Care Act 2014", "url": "https://www.legislation.gov.uk/ukpga/2014/23/contents"},
            {"title": "ONS — Population estimates for Torbay", "url": "https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates"}
        ],
        "related": ["Torbay and South Devon NHS Foundation Trust", "Clinical Supplies & Drugs — Torbay and South Devon NHS Foundation Trust"]
    },
    "Drugs costs — Moorfields Eye Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Moorfields Eye Hospital NHS Foundation Trust"}],
        "description": "Moorfields is the UK's only specialist eye hospital trust — its £42.6M drugs spend is almost entirely ophthalmic. Intravitreal anti-VEGF injections (aflibercept, ranibizumab, faricimab) for wet AMD, diabetic macular oedema and retinal vein occlusion dominate, delivered through >30 satellite clinics across London and South East England.",
        "beneficiaries": "London-wide ophthalmology population plus national tertiary referrals (uveitis, paediatric ophthalmology, inherited retinal disease)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · NHSE Specialised Commissioning (inherited retinal disease, ocular oncology, complex uveitis)",
        "key_stats": [
            "Drugs costs 2023-24: £42.6M (NHS Specialist — ophthalmology)",
            ">180,000 intravitreal injections per year (largest UK service)",
            "30+ satellite sites across London and SE England",
            "Inherited retinal disease — UK delivery centre for voretigene neparvovec (Luxturna) for RPE65 dystrophy",
            "Ocular oncology — melphalan intra-arterial chemo for retinoblastoma",
            "Uveitis — adalimumab biosimilar, mycophenolate, infliximab use",
            "Member of London Procurement Partnership",
            "Biosimilar aflibercept launch Q3 2024 — Moorfields lead implementer"
        ],
        "notes": "Biosimilar aflibercept (Yesafili/Opuviz) arrival in Q3 2024 is transformational — Moorfields consumes a higher volume of aflibercept than any other UK trust, and switch savings are pivotal to the NHSE 2024-25 best-value biologics programme. Faricimab (Vabysmo, TA800) is an increasingly preferred alternative for its extended dosing interval. Voretigene neparvovec (£613k per eye) is delivered under NICE TA635 with managed access.",
        "sources": [
            {"title": "Moorfields Annual Report 2023-24", "url": "https://www.moorfields.nhs.uk/content/annual-reports"},
            {"title": "NICE TA635 — Voretigene neparvovec for treating inherited retinal dystrophies", "url": "https://www.nice.org.uk/guidance/ta635"},
            {"title": "NHSE — Best value biological medicines: aflibercept (2024)", "url": "https://www.england.nhs.uk/commissioning/biosimilars/"}
        ],
        "related": ["Moorfields Eye Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Moorfields Eye Hospital NHS Foundation Trust"]
    },
    "Drugs costs — Medway NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Medway NHS Foundation Trust"}],
        "description": "Medway Maritime Hospital (Gillingham) has a £39.8M drugs bill serving a coastal Kent population with significant deprivation and health inequalities. The trust is a single-site district general providing A&E, maternity, and acute medical/surgical services for the Medway Towns.",
        "beneficiaries": "Medway towns (Chatham, Gillingham, Rochester, Strood) and Swale residents (~380k)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Kent & Medway ICB joint formulary",
        "key_stats": [
            "Drugs costs 2023-24: £39.8M",
            "Single-site acute DGH (Medway Maritime, Gillingham)",
            "Kent & Medway ICB joint formulary with EKHUFT, MTW, DVH",
            "Maternity service supporting Medway Towns",
            "Oncology day unit (SACT delivered locally)",
            "Part of NHS South East Regional Pharmacy Procurement",
            "Coastal deprivation drives COPD/cardiovascular chronic-disease spend",
            "Homecare biologics for rheumatology/IBD"
        ],
        "notes": "Medway had CQC 'Requires Improvement' ratings through much of 2019-23 including pharmacy governance scrutiny — the trust invested in pharmacy workforce expansion in 2023-24. The Kent & Medway ICB joint formulary harmonises decisions across EKHUFT, Maidstone & Tunbridge Wells, Dartford & Gravesham and Medway. Biosimilar penetration for adalimumab and infliximab is fully embedded.",
        "sources": [
            {"title": "Medway NHS Foundation Trust Annual Report 2023-24", "url": "https://www.medway.nhs.uk/about-us/publications/annual-reports"},
            {"title": "Kent & Medway Joint Formulary", "url": "https://www.kmformulary.nhs.uk/"},
            {"title": "CQC — Medway NHS Foundation Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RPA"}
        ],
        "related": ["Medway NHS Foundation Trust", "Clinical Supplies & Drugs — Medway NHS Foundation Trust"]
    },
    "Drugs costs — Surrey And Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Surrey And Sussex Healthcare NHS Trust"}],
        "description": "SASH runs East Surrey Hospital (Redhill) and spends £34.9M on drugs. It is a single-site DGH serving the border between Surrey and Sussex with a catchment including Gatwick Airport — the airport's presence and the trust's proximity to M23/M25 traffic drives a distinctive trauma/major incident preparedness profile.",
        "beneficiaries": "East Surrey, North Sussex and South Croydon residents (~535k) plus Gatwick Airport catchment",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Surrey Heartlands ICB formulary · Sussex ICB interface",
        "key_stats": [
            "Drugs costs 2023-24: £34.9M",
            "East Surrey Hospital — single acute site (Redhill)",
            "Gatwick Airport catchment — international traveller-associated ID caseload",
            "Maternity — ~4,000 deliveries/year",
            "Oncology day-unit SACT service",
            "Part of NHS South East Regional Pharmacy Procurement",
            "CQC 'Outstanding' rated 2018, sustained through 2023",
            "Homecare rheumatology/IBD biologics"
        ],
        "notes": "Gatwick catchment results in occasional imported tropical infections (malaria, typhoid, dengue) and international traveller blood-borne virus screening — drives specialist anti-infective stockholding (artemether-lumefantrine, atovaquone-proguanil). SASH is on the Surrey/Sussex ICB border so operates two-ICB formulary interfaces. The trust has had consistent CQC 'Outstanding' ratings since 2018.",
        "sources": [
            {"title": "SASH Annual Report 2023-24", "url": "https://www.surreyandsussex.nhs.uk/about-us/publications/"},
            {"title": "Surrey Heartlands ICB Formulary", "url": "https://surreyheartlands.nhs.uk/"},
            {"title": "CQC — Surrey and Sussex Healthcare NHS Trust", "url": "https://www.cqc.org.uk/provider/RTP"}
        ],
        "related": ["Surrey And Sussex Healthcare NHS Trust", "Clinical Supplies & Drugs — Surrey And Sussex Healthcare NHS Trust"]
    },
    "Drugs costs — Milton Keynes University Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Milton Keynes University Hospital NHS Foundation Trust"}],
        "description": "MKUH's £32.7M drugs spend supports a single-site DGH in one of England's fastest-growing cities. The trust has invested heavily in digital pharmacy systems (it was an HSCN early-adopter for electronic prescribing) and is part of the BLMK ICB joint formulary alongside Bedfordshire Hospitals.",
        "beneficiaries": "Milton Keynes, Buckingham and surrounding North Bucks / South Northants residents (~320k and growing rapidly)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · BLMK ICB joint formulary",
        "key_stats": [
            "Drugs costs 2023-24: £32.7M",
            "Single-site DGH in fastest-growing English city (ONS)",
            "Digital pharmacy leader — early EPMA adopter",
            "Maternity — expanding unit reflecting city growth",
            "Medical school partnership with University of Buckingham",
            "BLMK ICB joint formulary (with Bedfordshire Hospitals)",
            "Part of NHS East of England Regional Procurement",
            "Oncology day-unit SACT service"
        ],
        "notes": "MKUH's rapid local population growth (Milton Keynes is the UK's fastest-growing city per ONS) means maternity, paediatric and acute-admission drug volumes outpace historical baseline. The trust's medical school partnership with University of Buckingham supports clinical research including biosimilar switch studies. Fully digital EPMA reduces prescribing error and has improved VPAG data submission accuracy.",
        "sources": [
            {"title": "MKUH Annual Report 2023-24", "url": "https://www.mkuh.nhs.uk/about-us/corporate-information/annual-reports"},
            {"title": "BLMK ICB Joint Formulary", "url": "https://www.blmkformulary.nhs.uk/"},
            {"title": "ONS — Milton Keynes population projections", "url": "https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationprojections"}
        ],
        "related": ["Milton Keynes University Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Milton Keynes University Hospital NHS Foundation Trust"]
    },
    "Drugs costs — Sherwood Forest Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Sherwood Forest Hospitals NHS Foundation Trust"}],
        "description": "SFH-FT's £30.4M drugs spend supports King's Mill Hospital (Sutton-in-Ashfield), Newark Hospital and Mansfield Community Hospital, serving north Nottinghamshire — a semi-rural former coalfield catchment with significant deprivation and high chronic-disease prevalence. The trust was one of the earliest to be rated CQC 'Outstanding' among small/medium DGHs.",
        "beneficiaries": "North Nottinghamshire (Mansfield, Ashfield, Newark & Sherwood) residents (~420k)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Nottingham & Nottinghamshire ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £30.4M",
            "King's Mill (Sutton-in-Ashfield) + Newark + Mansfield Community",
            "Former coalfield demographic — elevated COPD prevalence",
            "CQC 'Outstanding' rated",
            "Member of NHS Midlands Regional Procurement",
            "Joint formulary aligned with Nottingham University Hospitals",
            "Diabetes service — high insulin and GLP-1 RA caseload",
            "Homecare biologics for rheumatology/IBD"
        ],
        "notes": "North Nottinghamshire's ex-coalfield legacy produces one of England's highest pneumoconiosis and COPD inhaled therapy caseloads (triple therapy ICS/LABA/LAMA combinations — Trelegy, Trimbow, Trixeo). Diabetes service delivery intersects with the 2023-24 GLP-1 RA (semaglutide) shortage managed via DHSC National Patient Safety Alert rationing. Small trust size means single high-cost patient (e.g. CAR-T onward-care) can move quarterly drug spend visibly.",
        "sources": [
            {"title": "SFH-FT Annual Report 2023-24", "url": "https://www.sfh-tr.nhs.uk/about-us/publications/"},
            {"title": "Nottingham & Nottinghamshire ICB Joint Formulary", "url": "https://www.nottsapc.nhs.uk/"},
            {"title": "CQC — Sherwood Forest Hospitals NHS Foundation Trust", "url": "https://www.cqc.org.uk/provider/RK5"}
        ],
        "related": ["Sherwood Forest Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — Sherwood Forest Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — Chesterfield Royal Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Chesterfield Royal Hospital NHS Foundation Trust"}],
        "description": "Chesterfield Royal's £29.4M drugs spend serves north Derbyshire from a single acute site. The trust's wholly-owned subsidiary DRI Ltd provides estates, facilities and pharmacy-linked services. Its catchment overlaps with Sheffield Teaching Hospitals for tertiary referrals, creating a mature formulary interface for high-cost SACT and biologics pass-through.",
        "beneficiaries": "Chesterfield, Bolsover, North East Derbyshire, High Peak, Derbyshire Dales residents (~405k)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Joined-up Care Derbyshire ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £29.4M",
            "Single-site DGH (Chesterfield)",
            "Derbyshire Support and Facilities Services Ltd (DRI) — wholly-owned sub",
            "Tertiary referral interface with Sheffield Teaching Hospitals",
            "Part of NHS Midlands Regional Procurement",
            "Oncology SACT day-unit (pass-through from STH)",
            "Joined-up Care Derbyshire ICB joint formulary",
            "Homecare biologics for rheumatology/IBD"
        ],
        "notes": "Patients needing CAR-T, proton beam, complex neuro-oncology or tertiary haematology are referred to Sheffield Teaching Hospitals, so the trust's Drugs costs line reflects a district-general profile without the highest-cost specialist outliers — except for tariff-excluded SACT delivered locally as continuation of STH-initiated regimens. The DRI subsidiary handles pharmacy stores and distribution under a service-level agreement.",
        "sources": [
            {"title": "Chesterfield Royal Annual Report 2023-24", "url": "https://www.chesterfieldroyal.nhs.uk/our-trust/corporate-publications/annual-reports-and-accounts"},
            {"title": "Joined-up Care Derbyshire ICB", "url": "https://joinedupcarederbyshire.co.uk/"},
            {"title": "DRI — Derbyshire Support and Facilities Services", "url": "https://www.dsfsltd.co.uk/"}
        ],
        "related": ["Chesterfield Royal Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Chesterfield Royal Hospital NHS Foundation Trust"]
    },
    "Drugs costs — North Middlesex University Hospital NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "North Middlesex University Hospital NHS Trust"}],
        "description": "North Mid's £28.3M drugs bill serves Edmonton, Haringey and Enfield — one of London's most ethnically diverse and economically deprived catchments. The trust has a notable HIV cohort and one of inner-London's most active sickle cell services, in addition to maternity and acute medicine for a younger-than-average population. North Mid merged with Royal Free London Group in autumn 2024.",
        "beneficiaries": "Enfield, Haringey and upper Edmonton residents (~450k) — highly diverse, significant deprivation",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · North Central London ICB formulary · NHSE HIV / haemoglobinopathy specs",
        "key_stats": [
            "Drugs costs 2023-24: £28.3M",
            "Edmonton — one of London's most diverse postcodes",
            "HIV outpatient cohort — high proportion of African heritage patients",
            "Sickle cell service — significant volume for catchment size",
            "Maternity — >5,500 deliveries/year",
            "Part of London Procurement Partnership",
            "Joined Royal Free London Group (2024) — procurement harmonisation underway",
            "Enfield/Haringey ICB interface"
        ],
        "notes": "The 2024 integration with Royal Free London Group creates procurement scale benefits and formulary harmonisation opportunities, particularly for high-cost HIV antiretrovirals and haemoglobinopathy drugs. The trust's demographic profile means DOT (directly-observed therapy) for TB, HIV ART, and sickle cell transfusion support form a large share of specialist spend. Maternity drug demand (oxytocin, misoprostol, magnesium sulphate, anti-D) is high for trust size.",
        "sources": [
            {"title": "North Middlesex Annual Report 2023-24", "url": "https://www.northmid.nhs.uk/about-us/publications/annual-reports"},
            {"title": "Royal Free London Group — North Middlesex merger (2024)", "url": "https://www.royalfree.nhs.uk/"},
            {"title": "NHSE — HIV routine commissioning (ART + PrEP)", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/blood-and-infection-group-f/f03/"}
        ],
        "related": ["North Middlesex University Hospital NHS Trust", "Clinical Supplies & Drugs — North Middlesex University Hospital NHS Trust"]
    },
    "Drugs costs — Bolton NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Bolton NHS Foundation Trust"}],
        "description": "Bolton FT's £27.3M drugs spend supports Royal Bolton Hospital and community services across the Metropolitan Borough of Bolton. A notable feature is the trust's high-volume maternity unit (one of England's busiest single-site services, >6,000 deliveries) and its neonatal ICU.",
        "beneficiaries": "Bolton Metropolitan Borough residents (~297k)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Greater Manchester ICB joint formulary",
        "key_stats": [
            "Drugs costs 2023-24: £27.3M",
            "Royal Bolton — >6,000 births/year (among highest English single-site volumes)",
            "Neonatal ICU — level 3 regional unit",
            "Integrated acute + community trust",
            "Greater Manchester ICB joint formulary with MFT and peers",
            "Member of NOE CPC procurement collaborative",
            "Paediatric service volume proportionate to obstetric activity",
            "Homecare biologics for rheumatology/IBD"
        ],
        "notes": "The maternity volume drives demand for oxytocin, ergometrine, misoprostol, magnesium sulphate, carbetocin and anti-D immunoglobulin at a scale rivalling trusts twice its size. Neonatal spend includes surfactant (poractant alfa), caffeine citrate and vancomycin/gentamicin paediatric dosing. The community-integrated model adds district-nursing-dispensed wound-care, insulin and anticoagulant lines.",
        "sources": [
            {"title": "Bolton FT Annual Report 2023-24", "url": "https://www.boltonft.nhs.uk/about-us/publications/"},
            {"title": "Greater Manchester Medicines Management Group", "url": "https://gmmmg.nhs.uk/"},
            {"title": "NHS Maternity Statistics (England)", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/nhs-maternity-statistics"}
        ],
        "related": ["Bolton NHS Foundation Trust", "Clinical Supplies & Drugs — Bolton NHS Foundation Trust"]
    },
    "Drugs costs — Walsall Healthcare NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Walsall Healthcare NHS Trust"}],
        "description": "Walsall Healthcare's £25.8M drugs spend covers Manor Hospital (Walsall) plus integrated community services in a West Midlands borough with above-average deprivation and a significant South Asian heritage population. The trust is part of Black Country ICB's joint formulary alongside Royal Wolverhampton, Dudley and Sandwell.",
        "beneficiaries": "Walsall Metropolitan Borough residents (~285k)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Black Country ICB joint formulary",
        "key_stats": [
            "Drugs costs 2023-24: £25.8M",
            "Manor Hospital + integrated community services",
            "South Asian heritage population share — elevated T2DM prevalence",
            "Black Country ICB joint formulary (with RWT, Dudley, Sandwell)",
            "Member of NHS Midlands Regional Procurement",
            "Part of RWT Group arrangement — shared back-office efficiencies",
            "Maternity service — Manor Hospital",
            "Community dispensing supporting care homes"
        ],
        "notes": "Walsall entered a group arrangement with Royal Wolverhampton from 2022, with joint executive leadership and shared corporate services driving procurement alignment. The diabetes population drives insulin and GLP-1 RA demand shaped by the 2023-24 semaglutide shortage (DHSC NatPSA). Community integration means district-nursing dispensing of insulin, anticoagulants and end-of-life drugs sit within trust budget.",
        "sources": [
            {"title": "Walsall Healthcare Annual Report 2023-24", "url": "https://www.walsallhealthcare.nhs.uk/about-us/publications/"},
            {"title": "Black Country ICB", "url": "https://blackcountry.icb.nhs.uk/"},
            {"title": "Royal Wolverhampton / Walsall group arrangement", "url": "https://www.royalwolverhampton.nhs.uk/about-us/rwt-walsall-group/"}
        ],
        "related": ["Walsall Healthcare NHS Trust", "Clinical Supplies & Drugs — Walsall Healthcare NHS Trust"]
    },
    "Drugs costs — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Stepping Hill Hospital (Stockport) is the single acute site behind Stockport FT's £23.0M drugs bill. The trust serves a Greater Manchester borough with mixed suburban and urban catchment, and is part of the Greater Manchester ICB joint formulary framework alongside MFT, Bolton, Wrightington-Wigan-Leigh and others.",
        "beneficiaries": "Stockport Metropolitan Borough residents (~295k) and parts of High Peak",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Greater Manchester ICB joint formulary",
        "key_stats": [
            "Drugs costs 2023-24: £23.0M",
            "Stepping Hill — single acute site",
            "Greater Manchester ICB joint formulary",
            "Member of NOE CPC procurement collaborative",
            "Tertiary oncology referrals to The Christie",
            "Rheumatology biologics homecare service",
            "Maternity — Starlight Unit Stepping Hill",
            "High-street pharmacy interface via community provision"
        ],
        "notes": "Stockport's drug profile is a balanced DGH mix — no single specialty dominates, but homecare biologics for IBD/rheumatology and pass-through tertiary oncology continuation (from The Christie) represent the largest high-cost lines. Part of the Greater Manchester Medicines Management Group which runs a coordinated biosimilar switch programme. The Starlight Maternity Unit drives standard obstetric drug demand.",
        "sources": [
            {"title": "Stockport FT Annual Report 2023-24", "url": "https://www.stockport.nhs.uk/corporate-information/publications/annual-report-and-accounts/"},
            {"title": "Greater Manchester Medicines Management Group", "url": "https://gmmmg.nhs.uk/"},
            {"title": "The Christie — tertiary oncology referrals", "url": "https://www.christie.nhs.uk/"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Clinical Supplies & Drugs — Stockport NHS Foundation Trust"]
    },
    "Drugs costs — The Hillingdon Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "The Hillingdon Hospitals NHS Foundation Trust"}],
        "description": "Hillingdon Hospitals FT (Hillingdon Hospital + Mount Vernon acute services) has a £21.3M drugs bill. Its catchment includes Heathrow Airport, creating a unique traveller-infectious-diseases profile (it is England's de facto Heathrow ED). The trust is in a long-standing estate redevelopment programme with a new Hillingdon Hospital under construction.",
        "beneficiaries": "London Borough of Hillingdon residents (~310k) plus Heathrow Airport workers/travellers",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · North West London ICB formulary · London Procurement Partnership",
        "key_stats": [
            "Drugs costs 2023-24: £21.3M",
            "Heathrow Airport catchment — traveller-associated ID",
            "Hillingdon Hospital + acute services at Mount Vernon (distinct from MVCC)",
            "New Hospital Programme — Hillingdon redevelopment",
            "Part of London Procurement Partnership",
            "NW London ICB formulary (with Imperial, CLCH, LNWH, CWFT)",
            "Maternity — Hillingdon Birth Centre",
            "Homecare biologics for rheumatology/IBD"
        ],
        "notes": "Heathrow catchment means occasional imported tropical disease caseload (malaria, enteric fever, dengue) and HIV/TB cosmopolitan presentations — drives specialist anti-infective stockholding. The forthcoming New Hospital Programme redevelopment at Hillingdon is a capital project not affecting the drugs line directly, though pharmacy department workflow will redesign. Part of NW London ICB formulary shared with Imperial.",
        "sources": [
            {"title": "The Hillingdon Hospitals FT Annual Report 2023-24", "url": "https://www.thh.nhs.uk/about-us/publications/annual-reports-accounts/"},
            {"title": "NW London ICB Formulary", "url": "https://www.nwlondonformulary.nhs.uk/"},
            {"title": "New Hospital Programme — Hillingdon", "url": "https://www.england.nhs.uk/new-hospital-programme/"}
        ],
        "related": ["The Hillingdon Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs — The Hillingdon Hospitals NHS Foundation Trust"]
    },
    "Drugs costs — Barnsley Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Barnsley Hospital NHS Foundation Trust"}],
        "description": "Barnsley Hospital's £19.9M drugs spend supports a single acute site serving the former coalfield and former industrial population of Barnsley. The catchment has some of Yorkshire's highest rates of COPD, ischaemic heart disease and type 2 diabetes, driving a chronic-disease-heavy drug profile. The trust operates in a group arrangement with The Rotherham NHS FT.",
        "beneficiaries": "Metropolitan Borough of Barnsley residents (~245k)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · South Yorkshire ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £19.9M",
            "Single-site DGH (Gawber Road, Barnsley)",
            "Former coalfield catchment — elevated COPD/IHD prevalence",
            "Group arrangement with The Rotherham NHS FT",
            "Tertiary referrals to Sheffield Teaching Hospitals",
            "Member of NOE CPC procurement collaborative",
            "Oncology SACT delivery on-site (continuation from STH)",
            "Cardiac rehabilitation drives secondary-prevention Rx"
        ],
        "notes": "Post-coalfield pulmonary disease burden drives ICS/LABA/LAMA triple-therapy inhaler spend (Trelegy Ellipta, Trimbow, Trixeo Aerosphere) — Barnsley has some of England's highest inhaler prescribing rates. The Barnsley/Rotherham group arrangement gives procurement scale. Tertiary oncology is referred to Sheffield Teaching Hospitals; Barnsley delivers continuation SACT cycles locally with pass-through reimbursement.",
        "sources": [
            {"title": "Barnsley Hospital FT Annual Report 2023-24", "url": "https://www.barnsleyhospital.nhs.uk/annual-reports/"},
            {"title": "South Yorkshire ICB Area Prescribing Committee", "url": "https://www.syapc.co.uk/"},
            {"title": "OHID — Fingertips: COPD prevalence", "url": "https://fingertips.phe.org.uk/"}
        ],
        "related": ["Barnsley Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Barnsley Hospital NHS Foundation Trust"]
    },
    "Drugs costs — Whittington Health NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Whittington Health NHS Trust"}],
        "description": "Whittington Health — an integrated acute and community provider in Islington/Haringey — has a £16.5M drugs bill. Its relatively low drug spend (for an acute trust) reflects its lack of tertiary services: no cardiothoracic surgery, no major trauma, limited specialist oncology. It is one of London's few integrated acute-community trusts, with a broad district-nursing footprint.",
        "beneficiaries": "Islington and Haringey residents (~490k) — young, ethnically diverse, urban",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · North Central London ICB formulary · London Procurement Partnership",
        "key_stats": [
            "Drugs costs 2023-24: £16.5M (relatively low — no tertiary specialties)",
            "Integrated acute + community provider",
            "Whittington Hospital single acute site (Archway)",
            "Community district-nursing footprint across Islington/Haringey",
            "Part of North Central London ICB (with UCLH, Royal Free, North Mid, Moorfields)",
            "Tertiary referrals to UCLH/Royal Free",
            "Maternity — Whittington Birthing Centre",
            "Member of London Procurement Partnership"
        ],
        "notes": "The trust's integrated model means community-dispensed medicines (district-nursing wound care, insulin, anticoagulants, end-of-life drug packs) sit within its budget. Tertiary oncology and cardiology are referred to UCLH/Royal Free, keeping Whittington's high-cost drug line modest. Homecare biologics volumes are proportionate for trust size. The North Central London ICB shared formulary aligns with the largest providers in the patch.",
        "sources": [
            {"title": "Whittington Health Annual Report 2023-24", "url": "https://www.whittington.nhs.uk/default.asp?c=26355"},
            {"title": "North Central London ICB", "url": "https://northcentrallondon.icb.nhs.uk/"},
            {"title": "London Procurement Partnership", "url": "https://www.lpp.nhs.uk/"}
        ],
        "related": ["Whittington Health NHS Trust", "Clinical Supplies & Drugs — Whittington Health NHS Trust"]
    },
    "Drugs costs — Solent NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Solent NHS Trust"}],
        "description": "Solent NHS Trust is a community and mental-health provider for Portsmouth and Southampton, so its £10.1M drugs spend is modest and profile-distinctive. Dispensing is dominated by community-based prescribing — sexual health (including PrEP), HIV community care, learning-disability services and district-nursing-dispensed insulin, anticoagulants and end-of-life drugs.",
        "beneficiaries": "Portsmouth and Southampton urban communities (~520k combined) — community-based services only",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Hampshire & Isle of Wight ICB formulary · NHSE PrEP / sexual health commissioning",
        "key_stats": [
            "Drugs costs 2023-24: £10.1M (NHS Community Trust)",
            "Community + sexual-health + some mental-health services",
            "Portsmouth & Southampton sexual health hub (PrEP provision)",
            "Learning disability health-check and annual medication review programmes",
            "District-nursing dispensing volume (insulin, anticoagulants, EOL drugs)",
            "Part of NHS South Central Regional Procurement",
            "Tertiary medicines referred to University Hospital Southampton",
            "Integrated approach with ICB pharmacy teams"
        ],
        "notes": "Community trust drug profile is fundamentally different from acute — no tariff-excluded oncology, no transplant immunosuppression, no tertiary biologics. PrEP (tenofovir/emtricitabine generic) and ART for HIV community follow-up form the largest high-cost lines. Learning-disability service provision drives antipsychotic de-prescribing (STOMP/STAMP programme) monitoring. End-of-life anticipatory prescribing packs are a core community pharmacy workstream.",
        "sources": [
            {"title": "Solent NHS Trust Annual Report 2023-24", "url": "https://www.solent.nhs.uk/about-us/publications/annual-reports/"},
            {"title": "NHSE — STOMP (stopping over-medication of people with a learning disability)", "url": "https://www.england.nhs.uk/learning-disabilities/improving-health/stomp/"},
            {"title": "Hampshire & IoW ICB", "url": "https://www.hantsiowhealthandcare.org.uk/"}
        ],
        "related": ["Solent NHS Trust", "Clinical Supplies & Drugs — Solent NHS Trust"]
    },
    "Drugs costs — Cambridgeshire Community Services NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Cambridgeshire Community Services NHS Trust"}],
        "description": "CCS is a community-services-only trust serving Cambridgeshire, Luton, Peterborough, Bedfordshire and Norfolk — its £8.0M drugs spend reflects community nursing, children's services, specialist community paediatrics, sexual health clinics and 0-19 health visiting. There is no acute or mental-health dispensing.",
        "beneficiaries": "Cambridgeshire, Bedfordshire, Luton, Peterborough and Norfolk community-service users (multi-million population, but community-only contact)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE TAs · Healthy Child Programme · NHSE sexual health commissioning",
        "key_stats": [
            "Drugs costs 2023-24: £8.0M (NHS Community Trust)",
            "Multi-county community provider (Cambs, Beds, Luton, Peterboro, Norfolk)",
            "0-19 Healthy Child Programme delivery",
            "Community paediatrics and children's therapy services",
            "Sexual health service commissioning includes PrEP",
            "Vaccination programme delivery (seasonal flu, childhood imm)",
            "District-nursing dispensing support",
            "Part of NHS East of England Regional Procurement"
        ],
        "notes": "Community-only drug profile: childhood immunisation programme (MenB Bexsero, MenACWY, MMR, HPV Gardasil 9), seasonal flu vaccine (Fluenz Tetra for children, Flucelvax Tetra for adults), routine antibiotics for community-acquired infection, and school-age vaccination logistics. Sexual health PrEP and EHC (emergency hormonal contraception) dispensing runs through commissioned clinics. 0-19 Healthy Child Programme is a significant activity volume.",
        "sources": [
            {"title": "CCS Annual Report 2023-24", "url": "https://www.cambscommunityservices.nhs.uk/about-us/how-we-operate/annual-reports"},
            {"title": "NHSE — Healthy Child Programme", "url": "https://www.gov.uk/government/publications/healthy-child-programme-0-to-19-health-visitor-and-school-nurse-commissioning"},
            {"title": "UKHSA — Immunisation against infectious disease (Green Book)", "url": "https://www.gov.uk/government/collections/immunisation-against-infectious-disease-the-green-book"}
        ],
        "related": ["Cambridgeshire Community Services NHS Trust", "Clinical Supplies & Drugs — Cambridgeshire Community Services NHS Trust"]
    },
    "Drugs costs — Northamptonshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Northamptonshire Healthcare NHS Foundation Trust"}],
        "description": "NHFT is a combined community and mental-health provider for Northamptonshire (and some Leicestershire services). Its £6.8M drugs spend — here classified as NHS Community Trust — covers community nursing dispensing, CAMHS psychotropic prescribing, community learning-disability services and adult community mental-health teams. There is no acute inpatient activity.",
        "beneficiaries": "Northamptonshire residents (~750k) using community and mental-health services",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE CGs for MH prescribing · Mental Health Act 1983 · NHSE MH policy",
        "key_stats": [
            "Drugs costs 2023-24: £6.8M (Community Trust classification)",
            "Combined community + mental health provider",
            "CAMHS prescribing for Northamptonshire children",
            "Community learning disability service (STOMP programme)",
            "Adult community mental health teams",
            "District nursing medication support across Northants",
            "Part of NHS Midlands Regional Procurement",
            "Acute inpatient drug demand referred to Northampton General / Kettering"
        ],
        "notes": "Mental-health-dominant prescribing profile: clozapine (requires Clozaril/ZTAS blood monitoring), long-acting antipsychotic injectables (aripiprazole, paliperidone, risperidone depots), lithium level monitoring and STOMP-driven de-prescribing for learning disability patients. CAMHS prescribing is conservative — methylphenidate/lisdexamfetamine for ADHD under NICE NG87, and low-dose fluoxetine for adolescent depression. No tariff-excluded high-cost lines except a handful of homecare SC methotrexate/adalimumab pass-through.",
        "sources": [
            {"title": "NHFT Annual Report 2023-24", "url": "https://www.nhft.nhs.uk/about-us/corporate-publications/"},
            {"title": "NICE NG87 — Attention deficit hyperactivity disorder: diagnosis and management", "url": "https://www.nice.org.uk/guidance/ng87"},
            {"title": "NHSE — STOMP/STAMP", "url": "https://www.england.nhs.uk/learning-disabilities/improving-health/stomp/"}
        ],
        "related": ["Northamptonshire Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs — Northamptonshire Healthcare NHS Foundation Trust"]
    },
    "Drugs costs — Dorset Healthcare University NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Dorset Healthcare University NHS Foundation Trust"}],
        "description": "Dorset Healthcare is a combined mental-health and community provider for Dorset. Its £6.5M drugs spend is shaped by adult mental-health inpatient units, CAMHS, older-person mental-health (significant given Dorset's older demographic), community nursing and specialist learning-disability services.",
        "beneficiaries": "Dorset residents (~780k including Bournemouth/Christchurch/Poole) using MH and community services",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE CGs MH · Mental Health Act 1983 · NHSE Dementia policy",
        "key_stats": [
            "Drugs costs 2023-24: £6.5M (Mental Health Trust classification)",
            "Combined mental health + community provider",
            "Older-person MH — dementia-focused prescribing (donepezil, rivastigmine, memantine)",
            "Adult MH inpatient units — clozapine, LAI antipsychotics",
            "CAMHS service — ADHD Rx",
            "Learning disability — STOMP de-prescribing",
            "Community nursing dispensing support",
            "Part of NHS South West Regional Procurement"
        ],
        "notes": "Dorset's older demographic (one of England's oldest median ages) drives a significant dementia-drug caseload — anticholinesterase inhibitors (donepezil, rivastigmine, galantamine) and memantine under NICE TA217. Older-person MH prescribing is conservative around QT-prolonging antipsychotics. Clozapine is used under ZTAS monitoring. Lecanemab/donanemab are not in routine use (not NHSE-commissioned as of 2024-25 pending appraisal).",
        "sources": [
            {"title": "Dorset Healthcare Annual Report 2023-24", "url": "https://www.dorsethealthcare.nhs.uk/about-us/publications"},
            {"title": "NICE TA217 — Donepezil, galantamine, rivastigmine and memantine for the treatment of Alzheimer's disease", "url": "https://www.nice.org.uk/guidance/ta217"},
            {"title": "NHS Digital — Dementia prescribing", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/recorded-dementia-diagnoses"}
        ],
        "related": ["Dorset Healthcare University NHS Foundation Trust", "Clinical Supplies & Drugs — Dorset Healthcare University NHS Foundation Trust"]
    },
    "Drugs costs — Essex Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Essex Partnership University NHS Foundation Trust"}],
        "description": "EPUT is the largest mental-health and community provider in the East of England, serving the Essex, Suffolk and Bedfordshire footprint. Its £5.4M drugs spend — modest relative to trust scale — is dominated by psychotropic medicines across adult, older-adult and forensic mental-health inpatient and community services.",
        "beneficiaries": "Essex, Suffolk, Bedfordshire residents receiving MH/community care (multi-million footprint but per-capita dispensing is low)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE CGs MH · Mental Health Act 1983 · NHSE forensic services commissioning",
        "key_stats": [
            "Drugs costs 2023-24: £5.4M (Mental Health Trust classification)",
            "Largest MH/community provider in East of England",
            "Medium-secure and low-secure forensic units — specialist prescribing",
            "Adult + older-adult + CAMHS (Hertfordshire/Essex)",
            "Clozapine cohort under ZTAS monitoring",
            "Long-acting injectable antipsychotic programme",
            "Part of NHS East of England Regional Procurement",
            "Under Thirlwall-related oversight post-inquiry scrutiny"
        ],
        "notes": "Forensic services drive higher-dose antipsychotic and mood-stabiliser prescribing under NHSE specialised commissioning. Clozapine monitoring (ZTAS — Zaponex Treatment Access System — or Clozaril Patient Monitoring Service) adds registry and blood-test costs. Long-acting injectables (paliperidone palmitate Xeplion/Trevicta, aripiprazole Abilify Maintena) are used to support community discharge and relapse prevention.",
        "sources": [
            {"title": "EPUT Annual Report 2023-24", "url": "https://eput.nhs.uk/about-us/publications/annual-reports/"},
            {"title": "NICE CG178 — Psychosis and schizophrenia in adults", "url": "https://www.nice.org.uk/guidance/cg178"},
            {"title": "NHSE — Adult medium secure service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/mental-health-group-c/c02/"}
        ],
        "related": ["Essex Partnership University NHS Foundation Trust", "Clinical Supplies & Drugs — Essex Partnership University NHS Foundation Trust"]
    },
    "Drugs costs — West London NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "West London NHS Trust"}],
        "description": "West London NHS Trust is a mental-health specialist trust hosting Broadmoor Hospital (the UK's most famous high-secure forensic hospital). Its £4.5M drugs bill reflects Broadmoor's high-secure prescribing, medium-secure Three Bridges unit, local adult/older MH services for Hammersmith & Fulham, Hounslow and Ealing, and community services.",
        "beneficiaries": "NHSE national high-secure forensic patients (Broadmoor) plus NW London local MH catchment",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · NHSE High Secure Services specification · NICE CGs MH",
        "key_stats": [
            "Drugs costs 2023-24: £4.5M (Mental Health Trust classification)",
            "Hosts Broadmoor Hospital — UK high-secure forensic (national service)",
            "Three Bridges — medium-secure forensic unit",
            "Local adult + older MH for Hammersmith & Fulham, Hounslow, Ealing",
            "Clozapine cohort under ZTAS monitoring",
            "Complex forensic prescribing — high-dose antipsychotics, mood stabilisers",
            "Part of London Procurement Partnership",
            "NHSE high-secure forensic commissioning (national pathway)"
        ],
        "notes": "Broadmoor as a high-secure hospital has some of England's most complex and high-dose forensic psychiatry prescribing — clozapine-resistant schizophrenia, treatment-resistant depression with ECT augmentation, mood stabiliser polypharmacy. Long-acting injectables are widely used to support adherence. The new Broadmoor hospital building (opened 2019) did not change prescribing patterns materially. Commissioning is national (NHSE high-secure pathway), not local ICB.",
        "sources": [
            {"title": "West London NHS Trust Annual Report 2023-24", "url": "https://www.westlondon.nhs.uk/about-us/our-publications/annual-reports"},
            {"title": "NHSE — High Secure Hospital service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/mental-health-group-c/c02/"},
            {"title": "Broadmoor Hospital", "url": "https://www.westlondon.nhs.uk/our-services/adult/forensic-services/broadmoor-hospital"}
        ],
        "related": ["West London NHS Trust", "Clinical Supplies & Drugs — West London NHS Trust"]
    },
    "Drugs costs — Derbyshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Derbyshire Healthcare NHS Foundation Trust"}],
        "description": "Derbyshire Healthcare is a combined mental-health and substance-misuse provider for Derby and Derbyshire. Its £4.4M drugs spend covers adult and older-adult MH, CAMHS, eating-disorder services and — distinctively — the county's NHSE-commissioned substance-misuse specialist service (methadone, buprenorphine, naltrexone prescribing).",
        "beneficiaries": "Derby City and Derbyshire residents (~1.05M) accessing MH and substance-misuse services",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE CGs MH + substance misuse · Misuse of Drugs Act 1971 · NHSE/DHSC substance misuse commissioning",
        "key_stats": [
            "Drugs costs 2023-24: £4.4M (Mental Health Trust classification)",
            "Adult + older adult + CAMHS mental health",
            "Specialist substance-misuse service — methadone, buprenorphine",
            "Eating disorder service — Derby",
            "Clozapine cohort under ZTAS",
            "LAI antipsychotic programme",
            "Joined-up Care Derbyshire ICB formulary",
            "Part of NHS Midlands Regional Procurement"
        ],
        "notes": "Substance-misuse prescribing (methadone 1mg/ml oral solution, buprenorphine/naloxone Suboxone sublingual, depot buprenorphine Buvidal LA) makes Derbyshire's drug line profile unusual for a MH trust. Controlled drug accountability and safe-storage costs are disproportionate. Naltrexone oral/depot for alcohol dependence use has grown under NICE NG115. Acamprosate remains standard for relapse prevention.",
        "sources": [
            {"title": "Derbyshire Healthcare Annual Report 2023-24", "url": "https://www.derbyshirehealthcareft.nhs.uk/about-us/publications"},
            {"title": "NICE CG115 — Alcohol-use disorders: diagnosis and management", "url": "https://www.nice.org.uk/guidance/cg115"},
            {"title": "Joined-up Care Derbyshire ICB", "url": "https://joinedupcarederbyshire.co.uk/"}
        ],
        "related": ["Derbyshire Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs — Derbyshire Healthcare NHS Foundation Trust"]
    },
    "Drugs costs — South West Yorkshire Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "South West Yorkshire Partnership NHS Foundation Trust"}],
        "description": "SWYPFT is a mental-health, learning-disability and community provider serving Barnsley, Calderdale, Kirklees and Wakefield. Its £4.0M drugs spend is dominated by adult and older-adult mental-health inpatient psychotropic prescribing, a substantial learning-disability specialist service, and perinatal mental-health care.",
        "beneficiaries": "South West Yorkshire residents (~1.1M) across four boroughs",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE CGs MH · Mental Health Act 1983 · NHSE perinatal MH commissioning",
        "key_stats": [
            "Drugs costs 2023-24: £4.0M (Mental Health Trust classification)",
            "Four-borough MH footprint — Barnsley, Calderdale, Kirklees, Wakefield",
            "Perinatal MH service — specialist mother & baby unit referrals",
            "Learning disability specialist provision — STOMP programme",
            "Clozapine cohort under ZTAS",
            "LAI antipsychotic programme",
            "West Yorkshire ICB formulary alignment",
            "Member of NOE CPC procurement collaborative"
        ],
        "notes": "Perinatal mental-health prescribing requires careful agent selection (SSRIs preferred, sertraline for breastfeeding per UKTIS guidance). Learning-disability prescribing has been the focus of national STOMP/STAMP de-prescribing drives since 2016, reducing antipsychotic burden in this cohort. Clozapine and LAIs drive the controlled-drug/monitored-drug budget lines.",
        "sources": [
            {"title": "SWYPFT Annual Report 2023-24", "url": "https://www.southwestyorkshire.nhs.uk/about-us/our-publications/annual-report/"},
            {"title": "UK Teratology Information Service (UKTIS)", "url": "https://uktis.org/"},
            {"title": "NHSE — Perinatal mental health services", "url": "https://www.england.nhs.uk/mental-health/perinatal/"}
        ],
        "related": ["South West Yorkshire Partnership NHS Foundation Trust", "Clinical Supplies & Drugs — South West Yorkshire Partnership NHS Foundation Trust"]
    },
    "Drugs costs — Avon and Wiltshire Mental Health Partnership NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Avon and Wiltshire Mental Health Partnership NHS Trust"}],
        "description": "AWP is the mental-health provider for Bristol, North Somerset, South Gloucestershire, Bath & North East Somerset, Swindon and Wiltshire — a large, geographically dispersed footprint. Its £3.8M drugs spend covers adult and older-adult MH, CAMHS, eating-disorder services (incl. the specialist STEPS unit for young people) and forensic services.",
        "beneficiaries": "Avon + Wiltshire residents (~1.8M across six council areas)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE CGs MH · Mental Health Act 1983",
        "key_stats": [
            "Drugs costs 2023-24: £3.8M (Mental Health Trust classification)",
            "Six-council footprint (Bristol, N Som, S Glos, BANES, Swindon, Wilts)",
            "STEPS — specialist eating disorder unit (young people)",
            "Adult + older-adult inpatient + community",
            "Forensic low/medium-secure service",
            "Clozapine cohort under ZTAS",
            "LAI antipsychotic depot programme",
            "Part of NHS South West Regional Procurement"
        ],
        "notes": "Eating-disorder prescribing includes olanzapine (for weight gain) and careful SSRI use in adolescent anorexia (per NICE NG69). Forensic service drives higher-dose antipsychotic and mood-stabiliser prescribing. The geographic dispersion across six council areas creates community pharmacy logistics complexity compared with single-city MH trusts.",
        "sources": [
            {"title": "AWP Annual Report 2023-24", "url": "https://www.awp.nhs.uk/about-us/publications/"},
            {"title": "NICE NG69 — Eating disorders: recognition and treatment", "url": "https://www.nice.org.uk/guidance/ng69"},
            {"title": "BNSSG / BSW ICB joint working", "url": "https://bnssg.icb.nhs.uk/"}
        ],
        "related": ["Avon and Wiltshire Mental Health Partnership NHS Trust", "Clinical Supplies & Drugs — Avon and Wiltshire Mental Health Partnership NHS Trust"]
    },
    "Drugs costs — Norfolk and Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Norfolk and Suffolk NHS Foundation Trust"}],
        "description": "NSFT is the MH provider for Norfolk and Suffolk — a rural, dispersed footprint that has been the subject of sustained regulatory scrutiny (repeated CQC 'Inadequate' ratings and independent inquiry on patient deaths, 2023). Its £3.2M drugs spend is notably low per population served, a feature under clinical review as part of the trust's improvement programme.",
        "beneficiaries": "Norfolk and Suffolk residents (~1.6M)",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE CGs MH · Mental Health Act 1983 · independent inquiry improvement requirements",
        "key_stats": [
            "Drugs costs 2023-24: £3.2M (Mental Health Trust classification)",
            "Two-county footprint — Norfolk + Suffolk (rural + coastal)",
            "Under CQC scrutiny (repeat 'Inadequate' ratings 2014-24)",
            "NHSE independent inquiry into patient deaths (reporting 2023-24)",
            "Adult + older adult + CAMHS (shared with Suffolk Community)",
            "Clozapine cohort under ZTAS",
            "Part of NHS East of England Regional Procurement",
            "Improvement programme includes pharmacy workforce expansion"
        ],
        "notes": "NSFT has been under sustained improvement programmes since first CQC 'Inadequate' in 2014. The 2023 independent inquiry into unexpected patient deaths led to wider scrutiny of medicines management, including controlled-drug handling and clozapine monitoring. Rural geography means community dispensing logistics (repeat Rx for lithium, clozapine, LAI depots) involves significant courier/pharmacy transport.",
        "sources": [
            {"title": "NSFT Annual Report 2023-24", "url": "https://www.nsft.nhs.uk/corporate-reports-and-policies/"},
            {"title": "CQC — Norfolk and Suffolk NHS Foundation Trust", "url": "https://www.cqc.org.uk/provider/RMY"},
            {"title": "NHSE Norfolk and Suffolk independent review", "url": "https://www.england.nhs.uk/east-of-england/norfolk-suffolk-independent-review/"}
        ],
        "related": ["Norfolk and Suffolk NHS Foundation Trust", "Clinical Supplies & Drugs — Norfolk and Suffolk NHS Foundation Trust"]
    },
    "Drugs costs — Southport And Ormskirk Hospital NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Southport And Ormskirk Hospital NHS Trust"}],
        "description": "Southport & Ormskirk's £2.5M drugs spend figure is anomalously low for an acute trust and reflects the trust's transition: in July 2024 its acute services merged into Mersey and West Lancashire Teaching Hospitals NHS Trust, with community services transferring to Lancashire & South Cumbria NHS FT. The 2023-24 figure captures only a partial or residual dispensing pattern during the pre-dissolution wind-down.",
        "beneficiaries": "Historic: Sefton and West Lancashire (Southport, Ormskirk) residents — services now delivered by MWL and L&SC",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NHSE reconfiguration legal framework · dissolution order 2024",
        "key_stats": [
            "Drugs costs 2023-24: £2.5M (residual — pre-dissolution)",
            "Trust dissolved July 2024 — acute services → MWL, community → L&SC",
            "Southport District General Hospital + Ormskirk Hospital",
            "Historic Cheshire & Merseyside ICB member",
            "Pharmacy services migrated to MWL formulary",
            "Final audited accounts for period to dissolution date",
            "Member of NOE CPC procurement collaborative (pre-2024)",
            "Catchment now served by two successor trusts"
        ],
        "notes": "This Drugs costs line reflects the wind-down period. Most acute prescribing activity was being migrated to the successor trusts' systems during 2023-24, so reported spend under 'Southport and Ormskirk' does not reflect a normalised year. Readers should interpret this alongside the corresponding increase in Mersey and West Lancashire Teaching Hospitals' drug line. Historical comparability is broken at the dissolution date.",
        "sources": [
            {"title": "Southport and Ormskirk Annual Report 2023-24 (final)", "url": "https://www.southportandormskirk.nhs.uk/"},
            {"title": "Mersey and West Lancashire Teaching Hospitals — merger", "url": "https://www.merseywestlancs.nhs.uk/"},
            {"title": "NHSE reconfiguration — Southport & Ormskirk dissolution", "url": "https://www.england.nhs.uk/north-west/"}
        ],
        "related": ["Southport And Ormskirk Hospital NHS Trust", "Clinical Supplies & Drugs — Southport And Ormskirk Hospital NHS Trust"]
    },
    "Drugs costs — Herefordshire and Worcestershire Health and Care NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Herefordshire and Worcestershire Health and Care NHS Trust"}],
        "description": "H&W Health and Care NHS Trust is a combined community and mental-health provider for Herefordshire and Worcestershire. Its £2.4M drugs spend — classified as Community Trust — covers community nursing, district-nursing-dispensed medicines, CAMHS, adult mental health, and a geographically-dispersed rural service delivery model.",
        "beneficiaries": "Herefordshire + Worcestershire residents (~790k combined) using community and MH services",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE CGs MH + community care · Herefordshire & Worcestershire ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £2.4M (Community Trust classification)",
            "Combined community + MH provider (formed 2020)",
            "Rural two-county footprint",
            "CAMHS + adult MH prescribing",
            "District-nursing medicines support",
            "Part of NHS Midlands Regional Procurement",
            "Herefordshire & Worcestershire ICB formulary alignment",
            "Acute care referred to WVT Hereford and WAHT Worcester"
        ],
        "notes": "Rural geography creates community pharmacy transport cost disproportionate to the modest drug budget — particularly for repeat Rx and medication disposal. Adult MH prescribing profile is standard (SSRIs, LAI depots for severe mental illness, clozapine cohort under ZTAS). The trust was formed by a 2020 merger of the former 2gether NHS FT with Worcestershire Health and Care.",
        "sources": [
            {"title": "H&W Health and Care Annual Report 2023-24", "url": "https://www.hacw.nhs.uk/about-us/publications/"},
            {"title": "Herefordshire and Worcestershire ICB", "url": "https://herefordshireandworcestershireicb.nhs.uk/"},
            {"title": "NHSE — Mental health community-services commissioning", "url": "https://www.england.nhs.uk/mental-health/adults/cmhs/"}
        ],
        "related": ["Herefordshire and Worcestershire Health and Care NHS Trust", "Clinical Supplies & Drugs — Herefordshire and Worcestershire Health and Care NHS Trust"]
    },
    "Drugs costs — Devon Partnership NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Devon Partnership NHS Trust"}],
        "description": "DPT is Devon's county-wide mental-health provider, with services ranging from adult inpatient units in Exeter to rural community MH teams in North Devon and specialist eating-disorder and perinatal services. Its £2.2M drugs spend is modest — standard psychotropic prescribing plus a designated medium-secure forensic unit.",
        "beneficiaries": "Devon residents (~820k) accessing MH services — large rural footprint",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NICE CGs MH · Mental Health Act 1983 · NHSE forensic commissioning",
        "key_stats": [
            "Drugs costs 2023-24: £2.2M (Mental Health Trust classification)",
            "County-wide Devon MH provider",
            "Medium-secure forensic unit (Langdon, Exeter)",
            "Perinatal MH — mother & baby unit (regional)",
            "CAMHS + adult + older-adult + LD services",
            "Clozapine cohort under ZTAS",
            "Part of NHS South West Regional Procurement",
            "Devon ICB formulary alignment with Royal Devon, University Hospitals Plymouth, Torbay"
        ],
        "notes": "Rural Devon geography creates community pharmacy/courier cost disproportionate to the £2.2M drug bill — particularly for controlled-drug repeat Rx and LAI depot logistics. Perinatal MH inpatient care requires specific maternal/infant safety prescribing (sertraline preferred for breastfeeding per UKTIS). Forensic services drive specialist mood-stabiliser and high-dose antipsychotic prescribing.",
        "sources": [
            {"title": "DPT Annual Report 2023-24", "url": "https://www.dpt.nhs.uk/about-us/our-performance/our-annual-reports"},
            {"title": "One Devon ICB", "url": "https://onedevon.org.uk/"},
            {"title": "NHSE Perinatal Mental Health", "url": "https://www.england.nhs.uk/mental-health/perinatal/"}
        ],
        "related": ["Devon Partnership NHS Trust", "Clinical Supplies & Drugs — Devon Partnership NHS Trust"]
    },
    "Drugs costs — Central London Community Healthcare NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Central London Community Healthcare NHS Trust"}],
        "description": "CLCH is one of London's largest community providers, serving multiple boroughs (Barnet, Brent, Hammersmith & Fulham, Hertfordshire, K&C, Merton, Wandsworth, Westminster). Its £1.8M drugs spend is modest and community-service-focused: district nursing, community paediatrics, sexual health clinics, 0-19 health visiting, and specialist community teams.",
        "beneficiaries": "Multi-borough London and parts of Hertfordshire community-service users — ~2M touched by CLCH services",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Healthy Child Programme · NHSE sexual health commissioning · NW London & NC London ICB formulary",
        "key_stats": [
            "Drugs costs 2023-24: £1.8M (Community Trust classification)",
            "Multi-borough footprint — 8+ London boroughs + Herts",
            "0-19 Healthy Child Programme (multiple boroughs)",
            "Community paediatric and therapy services",
            "Sexual health clinic contracts include PrEP",
            "District-nursing medication support",
            "Part of London Procurement Partnership",
            "Vaccinations programme delivery (seasonal + childhood imm)"
        ],
        "notes": "Community provider drug profile — no acute or tertiary exposure. Childhood immunisation programme (routine schedule: 6-in-1 Infanrix Hexa, MenB Bexsero, MenACWY, HPV Gardasil 9, MMR VaxPro) and seasonal flu (Fluenz Tetra children, Flucelvax Tetra adults) are volume-critical. Sexual health services include emergency hormonal contraception (levonorgestrel, ulipristal), STI testing/treatment, and PrEP.",
        "sources": [
            {"title": "CLCH Annual Report 2023-24", "url": "https://clch.nhs.uk/corporate-information/our-publications"},
            {"title": "UKHSA Green Book — Immunisation against infectious disease", "url": "https://www.gov.uk/government/collections/immunisation-against-infectious-disease-the-green-book"},
            {"title": "London Procurement Partnership", "url": "https://www.lpp.nhs.uk/"}
        ],
        "related": ["Central London Community Healthcare NHS Trust", "Clinical Supplies & Drugs — Central London Community Healthcare NHS Trust"]
    },
    "Drugs costs — Queen Victoria Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Queen Victoria Hospital NHS Foundation Trust"}],
        "description": "Queen Victoria Hospital (East Grinstead) is a small specialist trust focused on plastic, reconstructive and burns surgery — a legacy of Sir Archibald McIndoe's Guinea Pig Club from WW2. Its £1.5M drugs bill is the smallest in this batch, reflecting its narrow specialist scope: no A&E, no maternity, no chronic-disease outpatients.",
        "beneficiaries": "South East England and beyond — tertiary reconstructive/plastic surgery referrals; national burns aftercare",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · NHSE Specialised Commissioning (major burns, reconstructive, corneoplastic, sleep)",
        "key_stats": [
            "Drugs costs 2023-24: £1.5M (smallest in batch — NHS Specialist)",
            "Corneoplastic, reconstructive, burns and sleep medicine specialist",
            "One of four UK major burns centres (SE England)",
            "Legacy of McIndoe Burns Unit (WW2 Guinea Pig Club)",
            "Sleep disorders centre",
            "Hand surgery and maxillofacial reconstructive",
            "Part of NHS South East Regional Procurement",
            "No A&E, no maternity, no chronic-disease outpatients"
        ],
        "notes": "Specialist scope explains small drug bill — core agents are perioperative anti-infectives (teicoplanin, piperacillin-tazobactam, cefuroxime), analgesia (oxycodone, morphine, ketamine), topical burns antimicrobials (silver sulfadiazine, mupirocin) and anaesthetic drugs. No oncology, no transplant, no tertiary biologics. Sleep service uses modafinil and hypnotics under specialist initiation per NICE NG202.",
        "sources": [
            {"title": "QVH FT Annual Report 2023-24", "url": "https://www.qvh.nhs.uk/about-us/publications/annual-reports/"},
            {"title": "NHSE — Specialised burn care service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d06/"},
            {"title": "NICE NG202 — Obstructive sleep apnoea/hypopnoea syndrome", "url": "https://www.nice.org.uk/guidance/ng202"}
        ],
        "related": ["Queen Victoria Hospital NHS Foundation Trust", "Clinical Supplies & Drugs — Queen Victoria Hospital NHS Foundation Trust"]
    },
}
