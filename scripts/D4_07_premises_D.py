# -*- coding: utf-8 -*-
# D4_07 Premises (other) — slice D (51 NHS trusts)
# Hand-curated trust-specific enrichment entries.

NEW = {
    "Premises (other) — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "Non-depreciation estate operating costs at CUH covering the Addenbrooke's + Rosie hospital campus on the Cambridge Biomedical Campus — c. 200,000 m² of clinical floorspace alongside research-park co-tenancy (LMB, AstraZeneca neighbours). Dominated by hard FM at Addenbrooke's tower, life-sciences-grade utilities for genomics/MRC, and CBC-wide road/grounds shared service.",
        "beneficiaries": "1.7M+ catchment patients across East of England — Addenbrooke's (1,100 beds, major trauma + transplant), Rosie maternity, plus shared CBC research/teaching estate users (University of Cambridge Clinical School).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£88.51M"},
            {"label": "Share of trust total opex", "value": "c. 7%"},
            {"label": "Estate scale", "value": "Addenbrooke's + Rosie on CBC · ~200,000 m² clinical floorspace"},
            {"label": "Hard FM model", "value": "Mixed in-house Estates + specialist contractors; no acute-PFI"},
            {"label": "RAAC status", "value": "Limited RAAC; concrete frame Addenbrooke's tower under structural review"},
            {"label": "NHP scheme status", "value": "Cambridge Children's Hospital + Cambridge Cancer Research Hospital in NHP pipeline (Reset Jan 2025 deferred)"},
            {"label": "Net Zero milestone", "value": "Energy Centre CHP scheme; LED conversion programme rolling"},
            {"label": "YoY change", "value": "c. +7% (energy reset + research-grade utilities)"},
            {"label": "Peer benchmark", "value": "Top-quartile teaching-trust premises spend (CBC complexity)"}
        ],
        "notes": "CUH's estate cost is inflated by its co-location on the Cambridge Biomedical Campus — shared roads, security and grounds with research neighbours, plus higher-grade HVAC for genomics labs. The deferral of the Cambridge Children's Hospital and Cambridge Cancer Research Hospital under the NHP Reset (Jan 2025) means continued operating costs in legacy buildings rather than transition to new-build. Energy contract under NHS RM6011 saw partial pass-through of 2022-23 spike.",
        "sources": [
            "https://www.cuh.nhs.uk/about-us/who-we-are/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Imperial College Healthcare NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Imperial College Healthcare NHS Trust"}],
        "description": "Non-PFI premises operating costs across Imperial's five-hospital North-West London estate — St Mary's Paddington, Charing Cross, Hammersmith, Queen Charlotte's & Chelsea, and Western Eye. Heavily weighted toward backlog maintenance at St Mary's and Charing Cross, both NHP cohort schemes with listed-building constraints in central London.",
        "beneficiaries": "1.5M+ NW London catchment plus tertiary referrals — major trauma at St Mary's, cardiology at Hammersmith, maternity at Queen Charlotte's, ophthalmology at Western Eye.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£61.59M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "5 hospital sites across NW London + community clinics"},
            {"label": "Hard FM model", "value": "Mixed in-house + Mitie/equivalent for soft-FM at St Mary's"},
            {"label": "Backlog maintenance", "value": "Among NHS England's largest absolute backlog (£1bn+ historic estimate)"},
            {"label": "NHP scheme status", "value": "St Mary's + Charing Cross + Hammersmith all in NHP — Reset Jan 2025 pushed completion to 2030s"},
            {"label": "Listed building", "value": "St Mary's Clarence Wing (Queen Mary block) listed — restoration constraints"},
            {"label": "YoY change", "value": "c. +6% (energy + temporary works during NHP delay)"},
            {"label": "Peer benchmark", "value": "Below shadow-London-teaching median per m² but high absolute (estate age + 5-site dispersion)"}
        ],
        "notes": "Imperial's premises cost is shaped by an aged Victorian estate (St Mary's, where Alexander Fleming discovered penicillin) and the Reset deferral of NHP rebuild — meaning Imperial continues to pay rising operating costs on buildings it had planned to vacate. Energy spike pass-through and rising hard-FM contractor rates compound this. Backlog maintenance pressure is a perennial board risk.",
        "sources": [
            "https://www.imperial.nhs.uk/about-us/our-publications/annual-reports",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["Imperial College Healthcare NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — King’s College Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "King’s College Hospital NHS Foundation Trust"}],
        "description": "Non-PFI premises running costs across the Denmark Hill (Camberwell) and Princess Royal University Hospital (Orpington) estates plus satellite community sites. Denmark Hill is dense, multi-decade build (Ruskin, Golden Jubilee, Cicely Saunders, Hambleden Wing) with constrained footprint; PRUH is a 2003-vintage acute campus.",
        "beneficiaries": "South-East London + tertiary catchment — major trauma, hyperacute stroke, liver transplant, foetal medicine, neurosciences at Denmark Hill; general acute at PRUH (Bromley).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£57.07M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 main hospitals (Denmark Hill + PRUH) + 5 satellite sites"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "PFI footprint", "value": "Golden Jubilee Wing PFI charges sit in D4_11 — NOT here"},
            {"label": "Site complexity", "value": "Denmark Hill 17+ ward-blocks of varying age; tight central footprint"},
            {"label": "Net Zero milestone", "value": "Heat decarbonisation feasibility under Salix PSDS funding"},
            {"label": "YoY change", "value": "c. +5-7% (utilities + soft-FM contract uplift)"},
            {"label": "Peer benchmark", "value": "Mid-range vs London teaching peers"}
        ],
        "notes": "King's premises cost reflects a complex tertiary estate where high-acuity services (transplant, neurosciences) require resilient utilities and 24/7 hard-FM cover. The trust's 2018-19 financial special-measures legacy left maintenance backlog elevated; recovery has been slow. PRUH brings outer-London estate dynamics quite different from Denmark Hill — including parking, grounds and ambulance access load.",
        "sources": [
            "https://www.kch.nhs.uk/about/corporate/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["King’s College Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Northumbria Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Northumbria Healthcare NHS Foundation Trust"}],
        "description": "Premises running costs across Northumbria's distinctive multi-site rural estate — the flagship Northumbria Specialist Emergency Care Hospital (Cramlington, opened 2015) plus three general hospitals (Wansbeck, North Tyneside, Hexham) and extensive community estate. The trust uniquely owns a wholly-owned subsidiary (Northumbria Healthcare Facilities Management) handling FM in-house.",
        "beneficiaries": "500,000+ patients across Northumberland and North Tyneside — trauma + emergency at Cramlington, planned care at Wansbeck/NTGH, rural acute at Hexham, plus 30+ community sites.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£50.33M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "1 specialist emergency + 3 general + 30+ community sites · large rural footprint"},
            {"label": "Hard FM model", "value": "Northumbria Healthcare FM Ltd (wholly-owned subsidiary, insourced)"},
            {"label": "Cramlington site", "value": "England's first purpose-built specialist A&E hospital (opened June 2015)"},
            {"label": "Rural premium", "value": "Hexham + community estate carry travel/grounds/winter-resilience cost"},
            {"label": "Net Zero milestone", "value": "Solar PV + EV charging at Cramlington and NTGH; PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5% (energy + rural fuel)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median per site (rural dispersion)"}
        ],
        "notes": "Northumbria's wholly-owned FM subsidiary lets it retain margin and tactical control of soft FM — an unusual NHS model that survived the 2017 IR35/SDC tax-treatment pressure. The Cramlington specialist site requires high-availability utilities and trauma-grade resilience. Rural dispersion (Hexham, Berwick-area community sites) means winter readiness, gritting, generator cover all sit in this line.",
        "sources": [
            "https://www.northumbria.nhs.uk/about-us/publications-and-reports/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Northumbria Healthcare NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Central and North West London NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Central and North West London NHS Foundation Trust"}],
        "description": "Mental-health and community premises running costs across CNWL's sprawling NW London + Milton Keynes + offender-health estate — including Park Royal Centre for Mental Health, St Charles Hospital (Kensington), Vincent Square eating disorders, Gordon Hospital (Westminster, exit underway), plus HMP/IRC contracts (Heathrow IRC, HMP Wormwood Scrubs).",
        "beneficiaries": "Adult acute MH inpatients, CAMHS, addictions services, eating-disorder specialist patients, offender-health service users, Milton Keynes community physical-health patients.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£47.20M"},
            {"label": "Share of trust total opex", "value": "c. 7%"},
            {"label": "Estate scale", "value": "100+ sites across NW London + Milton Keynes + offender health"},
            {"label": "Specific driver", "value": "Gordon Hospital exit (Westminster) + St Charles refurbishment"},
            {"label": "MH-specific", "value": "s.136 suites + PICU + eating-disorder unit utilities"},
            {"label": "Offender health", "value": "Heathrow IRC + HMP Wormwood Scrubs healthcare premises"},
            {"label": "Net Zero milestone", "value": "Park Royal BMS upgrade in train"},
            {"label": "YoY change", "value": "c. +6-8% (energy + soft-FM uplift + Gordon decant cost)"},
            {"label": "Peer benchmark", "value": "Above large-London-MH median (estate footprint dispersed)"}
        ],
        "notes": "CNWL's premises spend is unusually high among MH trusts because of its dispersed multi-borough footprint (Westminster to Milton Keynes), plus offender-health responsibilities at IRCs and HMPs which add custodial-grade FM constraints. The Gordon Hospital closure (Westminster, services relocated to St Charles) generates transition cost. RAAC clearance survey 2024 cleared most CNWL inpatient blocks.",
        "sources": [
            "https://www.cnwl.nhs.uk/about-us/publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/publications/raac-management-guidance"
        ],
        "related": ["Central and North West London NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Non-PFI premises operating costs across the Royal Free's three-hospital group — Royal Free Hampstead, Barnet Hospital, Chase Farm (Enfield, rebuilt 2018). Heavy contrast between aged Hampstead tower (1974, Bauhaus-influenced concrete) and modern digital-hospital Chase Farm.",
        "beneficiaries": "1.6M+ NW London catchment + tertiary referrals — liver transplant, HIV, infectious diseases at Hampstead; general acute at Barnet; planned/elective at Chase Farm.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£44.11M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "3 acute sites (Hampstead, Barnet, Chase Farm) + community"},
            {"label": "Hampstead tower", "value": "1974-vintage concrete tower — high backlog, lift/façade pressures"},
            {"label": "Chase Farm rebuild", "value": "2018 digital hospital — lower backlog, higher tech-utility load"},
            {"label": "Barnet PFI", "value": "PFI unitary charge sits in D4_11 NOT here"},
            {"label": "Net Zero milestone", "value": "Hampstead heat-network feasibility ongoing"},
            {"label": "YoY change", "value": "c. +5% (utilities + Hampstead façade works)"},
            {"label": "Peer benchmark", "value": "Mid-range vs London teaching peers"}
        ],
        "notes": "Royal Free's premises line balances the high-cost Hampstead tower (clinical access constraints, lift modernisation in train) with the new-build Chase Farm — two very different cost drivers in the same opex line. The trust's group model with North Mid (folding-in delayed) and the absorption of the Royal Free Group Pathology Partnership (HSL) add some shared-estate complexity.",
        "sources": [
            "https://www.royalfree.nhs.uk/about-us/publications/annual-reports-and-summary-financial-statements/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Lewisham and Greenwich NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Lewisham and Greenwich NHS Trust"}],
        "description": "Premises running costs across LGT's two-hospital footprint — University Hospital Lewisham (Lewisham High Street, mixed-age estate) and Queen Elizabeth Hospital Woolwich (PFI 2001-vintage, unitary charge in D4_11). 'Premises (other)' captures the non-PFI portion: Lewisham hard/soft FM, both-site grounds and small community-site footprint.",
        "beneficiaries": "750,000+ SE London catchment — full general acute including maternity, paediatrics, A&E at both Lewisham and QEH Woolwich.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£38.22M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "2 acute hospitals (Lewisham + Woolwich) + community estate"},
            {"label": "PFI footprint", "value": "QEH Woolwich PFI in D4_11 — Lewisham predominantly non-PFI here"},
            {"label": "Hard FM model", "value": "In-house Estates at Lewisham; PFI co-located at QEH"},
            {"label": "Lewisham A&E history", "value": "Site of 'Save Lewisham A&E' campaign (2013) — high public-asset salience"},
            {"label": "Net Zero milestone", "value": "Lewisham PSDS-funded heat upgrades scoped"},
            {"label": "YoY change", "value": "c. +6% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Mid-range vs London acute peers"}
        ],
        "notes": "LGT's premises cost reflects the bifurcation between the older Lewisham estate (with backlog and historic save-A&E community attachment) and the PFI-managed QEH Woolwich, where the unitary charge captured elsewhere does the heavy lifting on hard FM. The trust has been in financial recovery since merger and capital investment has been constrained, raising operational maintenance pressure.",
        "sources": [
            "https://www.lewishamandgreenwich.nhs.uk/our-publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Lewisham and Greenwich NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Lancashire and South Cumbria NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Lancashire and South Cumbria NHS Foundation Trust"}],
        "description": "MH and learning-disability premises running costs across LSCFT's distinctive geographic span — the Guild Park Lodge / Guild Lodge secure unit (Preston), Scarisbrick / Avondale MH inpatient wards, plus extensive community estate from Lancaster down to Chorley and across into South Cumbria. Several units in the trust were affected by RAAC concrete surveys.",
        "beneficiaries": "1.8M MH/LD/community service-users across Lancashire + South Cumbria — including secure forensic patients at Guild Lodge, adult acute MH, CAMHS and community physical-health teams.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£33.43M"},
            {"label": "Share of trust total opex", "value": "c. 8%"},
            {"label": "Estate scale", "value": "60+ sites — secure forensic + adult MH + community physical health"},
            {"label": "Guild Lodge", "value": "Medium-secure forensic — security-grade FM cost premium"},
            {"label": "RAAC status", "value": "Some buildings flagged in 2023-24 NHS RAAC survey; mitigation works ongoing"},
            {"label": "Geographic dispersion", "value": "Lancaster to Burnley to Barrow — rural-fuel + travel cost"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump pilots at Guild Lodge"},
            {"label": "YoY change", "value": "c. +7% (energy + RAAC-mitigation works)"},
            {"label": "Peer benchmark", "value": "Above MH-trust median (forensic + dispersed estate)"}
        ],
        "notes": "LSCFT's premises spend is shaped by its forensic security obligations (Guild Lodge requires Department of Health Secure Settings standards), wide rural dispersion across two county systems, and RAAC mitigation that emerged in the 2023-24 NHS-wide survey. Mental Health Act detention-grade premises require ligature-anchor, observation-line and secure-perimeter capex that flows into operating cost.",
        "sources": [
            "https://www.lscft.nhs.uk/about-us/publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/publications/raac-management-guidance"
        ],
        "related": ["Lancashire and South Cumbria NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Shrewsbury and Telford Hospital NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
        "description": "Premises running costs across SaTH's two acute hospitals — Royal Shrewsbury Hospital and Princess Royal (Telford). The trust is mid-flight in the Hospitals Transformation Programme (formerly Future Fit) — splitting emergency vs planned care between sites — with NHP Reset (Jan 2025) implications.",
        "beneficiaries": "Approx 500,000 catchment across Shropshire, Telford & Wrekin and mid-Wales — maternity (Ockenden Review legacy investments), A&E, planned care.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£31.89M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "2 acute hospitals (RSH Shrewsbury + PRH Telford) + maternity sites"},
            {"label": "Hospitals Transformation Programme", "value": "Capital scheme to specialise sites — Reset Jan 2025 reshaped timeline"},
            {"label": "Ockenden Review legacy", "value": "Maternity-estate upgrades baked into running cost since 2022"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Net Zero milestone", "value": "RSH solar PV scoped; PSDS bids submitted"},
            {"label": "YoY change", "value": "c. +6% (energy + transition / decant)"},
            {"label": "Peer benchmark", "value": "Above small-acute median per bed (transition cost)"}
        ],
        "notes": "SaTH's premises spend is shaped by the dual-site Hospitals Transformation Programme, where extending the operating life of buildings designed to be reconfigured raises maintenance cost. The post-Ockenden Review (2022) maternity safety investments — additional bereavement suites, refurbished delivery rooms — also feed running costs. NHP Reset deferral pushes this transition cost further into the operating line.",
        "sources": [
            "https://www.sath.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "Premises running costs across UHD's three-hospital group formed Oct 2020 — Royal Bournemouth, Poole, Christchurch — undergoing a major reconfiguration with Bournemouth as planned-care hub and Poole as emergency hub (BEACH project). NHP Reset Jan 2025 affected scheme cadence.",
        "beneficiaries": "850,000+ catchment across Dorset + parts of Hampshire — emergency/maternity at Poole, planned + elective at Bournemouth, rehab at Christchurch.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£29.94M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "3 hospitals (Bournemouth, Poole, Christchurch) + community"},
            {"label": "BEACH building", "value": "Bournemouth Emergency, A&E, Critical Care, Hub — phased under NHP"},
            {"label": "NHP scheme status", "value": "BEACH partially in NHP cohort; Reset Jan 2025 reshuffle"},
            {"label": "Hard FM model", "value": "In-house Estates with specialty contractors"},
            {"label": "Net Zero milestone", "value": "Bournemouth heat-pump scheme advanced; PSDS funding awarded"},
            {"label": "YoY change", "value": "c. +7% (transition + energy)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers (transition phase)"}
        ],
        "notes": "UHD's premises cost is shaped by the merger reconfiguration — running three sites while the BEACH building enables the Bournemouth/Poole specialisation split is operationally expensive. Christchurch's rehab/community role keeps a third active site in the cost base. Coastal estate adds salt-corrosion maintenance premium on external fabric.",
        "sources": [
            "https://www.uhd.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — East Kent Hospitals University NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "East Kent Hospitals University NHS Foundation Trust"}],
        "description": "Premises running costs across EKHUFT's three-acute-hospital footprint — William Harvey (Ashford), Queen Elizabeth The Queen Mother (Margate), Kent and Canterbury — all of varied vintage and configuration, with the trust's NHP-aspiration single-site solution deferred under Reset Jan 2025.",
        "beneficiaries": "750,000+ East Kent + Medway catchment — maternity (post-Kirkup Review investments), A&E, paediatrics, elective.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£28.74M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "3 acute hospitals (Ashford, Margate, Canterbury) + satellite"},
            {"label": "Kirkup Review legacy", "value": "Maternity-estate safety investments since Oct 2022 report"},
            {"label": "NHP scheme status", "value": "East Kent reconfiguration deferred under Reset Jan 2025"},
            {"label": "Coastal estate", "value": "Margate (QEQM) — salt-corrosion + winter-resilience cost"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Net Zero milestone", "value": "PSDS heat works scoped at WHH Ashford"},
            {"label": "YoY change", "value": "c. +6% (energy + extended-life maintenance)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers (multi-site dispersion)"}
        ],
        "notes": "EKHUFT operates three acute hospitals across a coastal/rural patch where deferral of the NHP reconfiguration means continued running cost on buildings the trust had hoped to vacate. Maternity safety investments post-Kirkup Review (Oct 2022) — refurbished delivery suites, bereavement room upgrades — feed running cost. Coastal positioning at Margate adds an external-fabric maintenance premium.",
        "sources": [
            "https://www.ekhuft.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["East Kent Hospitals University NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "Premises running costs across UHNM's two-hospital footprint — Royal Stoke University Hospital (Stoke-on-Trent, major trauma centre) and County Hospital Stafford. Royal Stoke includes a substantial PFI element (sits in D4_11 not here); 'Premises (other)' captures non-PFI Stafford and shared services.",
        "beneficiaries": "3M+ regional catchment — major trauma, neurosurgery, cardiothoracic at Stoke; planned + community at Stafford.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£27.74M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "Royal Stoke (PFI + new-build elements) + County Stafford"},
            {"label": "PFI footprint", "value": "Royal Stoke PFI unitary charge in D4_11 NOT here"},
            {"label": "Trauma centre", "value": "Major Trauma Centre status — resilience-grade utilities + helipad"},
            {"label": "Hard FM model", "value": "PFI co-located at Stoke; in-house at Stafford"},
            {"label": "Net Zero milestone", "value": "Stoke + Stafford solar PV; PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Below tertiary peer median (PFI absorbs much of FM)"}
        ],
        "notes": "Premises (other) at UHNM looks artificially low among major-trauma trusts because the Royal Stoke PFI unitary charge lives in a separate accounting line. The trust's operating line here mostly captures County Hospital Stafford running costs plus shared estate-services overhead. Net Zero progression on heat pumps and solar at both sites is in early operational delivery.",
        "sources": [
            "https://www.uhnm.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across the St George's Tooting tertiary campus and Queen Mary's Roehampton site. Tooting is a 1976-vintage tower/podium with significant backlog; the trust merged into the GESH (St George's, Epsom and St Helier) hospital group in Mar 2024 — adding cross-group estate coordination.",
        "beneficiaries": "3.5M+ SW London/Surrey tertiary catchment — major trauma, neurosurgery, cardiology, hyperacute stroke, transplant surgery at Tooting; rehab/older-people at Queen Mary's.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£27.21M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "St George's Tooting tower/podium + Queen Mary's Roehampton + research/teaching shared with SGUL"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "Group structure", "value": "GESH group with Epsom & St Helier formed Mar 2024"},
            {"label": "Major trauma", "value": "MTC for SW London — resilience-grade utilities + helipad"},
            {"label": "Net Zero milestone", "value": "Tooting heat-network feasibility under PSDS"},
            {"label": "YoY change", "value": "c. +6% (energy + group-formation transition cost)"},
            {"label": "Peer benchmark", "value": "Below median for London tertiary (Tooting low rateable density)"}
        ],
        "notes": "St George's premises spend reflects an aged Tooting tower with persistent maintenance backlog and lift-modernisation pressure, plus the shared-estate complexity of co-location with St George's University of London. The GESH group formation in Mar 2024 introduces cross-group estate strategy that may reshape this line over the medium term. Major trauma centre status drives utility resilience cost.",
        "sources": [
            "https://www.stgeorges.nhs.uk/about/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — County Durham and Darlington NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "County Durham and Darlington NHS Foundation Trust"}],
        "description": "Premises running costs across CDDFT's seven-site footprint — University Hospital of North Durham, Darlington Memorial Hospital, Bishop Auckland Hospital plus four community hospitals (Chester-le-Street, Sedgefield, Shotley Bridge, Weardale). Bishop Auckland transitioned to a planned-care hub model.",
        "beneficiaries": "650,000+ County Durham and Darlington catchment — A&E + maternity at Durham + Darlington; planned/elective at Bishop Auckland; intermediate care at four community hospitals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£26.21M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "3 acute + 4 community hospitals across County Durham"},
            {"label": "Bishop Auckland", "value": "Reconfigured planned-care hub — different FM profile from full A&E"},
            {"label": "Rural dispersion", "value": "Weardale, Sedgefield, Shotley Bridge — winter-resilience premium"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at multiple sites"},
            {"label": "YoY change", "value": "c. +5-7% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Above acute median per bed (rural dispersion)"}
        ],
        "notes": "CDDFT's premises cost is shaped by a multi-site rural-dispersed model where four community hospitals plus three acute sites generate a higher-than-average estate footprint per bed. Winter-resilience cost (gritting, fuel for community-hospital generators in Weardale) is a recurring driver. Bishop Auckland's reconfiguration as a planned-care hub keeps the site active but lower-acuity.",
        "sources": [
            "https://www.cddft.nhs.uk/about-us/publications.aspx",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["County Durham and Darlington NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across DBTH's three-site footprint — Doncaster Royal Infirmary, Bassetlaw Hospital (Worksop), and Montagu Hospital (Mexborough). Operates within the South Yorkshire ICB and is a partner in the South Yorkshire Hospital Services collaborative.",
        "beneficiaries": "420,000+ catchment across Doncaster, Bassetlaw and parts of North Lincolnshire — full general acute including maternity, A&E, planned care.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£24.43M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "3 hospitals (Doncaster, Bassetlaw, Montagu) + community"},
            {"label": "Cross-border", "value": "Bassetlaw in Notts ICB — cross-ICB estate coordination"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Backlog", "value": "Doncaster + Bassetlaw both pre-2000 estate — significant backlog"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works underway"},
            {"label": "YoY change", "value": "c. +5% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers"}
        ],
        "notes": "DBTH's premises spend reflects three ageing acute sites — none recent new-build — generating sustained backlog-maintenance pressure. Bassetlaw sits in Nottinghamshire's geographical/ICB footprint, creating cross-ICB coordination overhead. Montagu's role as elective/diagnostic hub keeps it active but with lighter utility load than full-acute peers.",
        "sources": [
            "https://www.dbth.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Nottinghamshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Nottinghamshire Healthcare NHS Foundation Trust"}],
        "description": "MH, learning-disability and forensic premises running costs across NHFT's distinctive estate — including Rampton Hospital (high-secure, one of three in England), Wathwood Hospital (medium-secure), Highbury Hospital MH inpatient, plus extensive community estate across Nottinghamshire.",
        "beneficiaries": "MH/LD service-users across Nottinghamshire + nationally-commissioned high-secure forensic patients at Rampton (alongside Broadmoor, Ashworth).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£23.38M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Rampton + Wathwood + Highbury + 100+ community sites"},
            {"label": "Rampton Hospital", "value": "1 of 3 English high-secure hospitals — security-grade FM premium"},
            {"label": "Wathwood Hospital", "value": "Medium-secure forensic — security-grade utilities"},
            {"label": "Hard FM model", "value": "In-house Estates with security-cleared contractors"},
            {"label": "Net Zero milestone", "value": "Rampton/Highbury heat decarbonisation in PSDS pipeline"},
            {"label": "YoY change", "value": "c. +6% (energy + secure-estate FM)"},
            {"label": "Peer benchmark", "value": "Above MH-trust median (high-secure premium)"}
        ],
        "notes": "Nottinghamshire Healthcare's premises spend is unusually weighted by Rampton high-secure hospital — one of only three in England — where physical-security perimeters, secure-grade glazing, anti-ligature and observation infrastructure generate a substantial FM premium over standard MH estate. Forensic-estate FM contractors require security clearance, raising labour rates. Wathwood adds further medium-secure load.",
        "sources": [
            "https://www.nottinghamshirehealthcare.nhs.uk/publications-and-policies",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/publications/high-secure-services-for-patients-with-a-mental-disorder"
        ],
        "related": ["Nottinghamshire Healthcare NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Somerset NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Somerset NHS Foundation Trust"}],
        "description": "Premises running costs across Somerset FT's integrated acute + community + MH estate — Musgrove Park (Taunton), Yeovil District (added via 2023 merger), 13 community hospitals (Wellington, Burnham-on-Sea, Williton, etc.) and MH inpatient sites. One of England's most integrated trust models.",
        "beneficiaries": "560,000+ catchment across Somerset — A&E + maternity at Taunton + Yeovil; intermediate care at 13 community hospitals; MH inpatients across the county.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£22.59M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "2 acute + 13 community hospitals + MH inpatient + community clinics"},
            {"label": "Yeovil merger", "value": "Yeovil District added via Apr 2023 transaction — estate consolidation cost"},
            {"label": "Integrated model", "value": "Single trust holds acute + community + MH — unusual scope"},
            {"label": "Rural dispersion", "value": "Exmoor + Somerset Levels community sites — winter resilience"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Net Zero milestone", "value": "Musgrove Park heat-pump scheme advanced"},
            {"label": "YoY change", "value": "c. +6% (energy + post-merger harmonisation)"},
            {"label": "Peer benchmark", "value": "Mid-range despite scale (integrated economies)"}
        ],
        "notes": "Somerset FT's premises cost is shaped by its unusual integrated scope — covering acute + community + MH in one organisation — and the Apr 2023 merger with Yeovil District which brought a second acute site and harmonisation costs. The community-hospital network (13 sites) generates dispersed FM load typical of rural integrated trusts. Net Zero progression on heat pumps at Musgrove is among the more advanced.",
        "sources": [
            "https://www.somersetft.nhs.uk/about-us/publications-and-policies/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Somerset NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Birmingham Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Birmingham Community Healthcare NHS Foundation Trust"}],
        "description": "Premises running costs across BCHC's wholly-community estate — Moseley Hall Hospital (rehab), West Heath Hospital (rehab), specialist dental + LD inpatient services, plus 70+ community clinic sites. Heavily weighted toward leasehold and shared-estate (NHS Property Services / CHP) holdings.",
        "beneficiaries": "Birmingham community-services users — rehab inpatients, learning-disability inpatients, specialist dental, c.100+ community-team estate users (district nursing, therapies, child health).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£22.16M"},
            {"label": "Share of trust total opex", "value": "c. 8%"},
            {"label": "Estate scale", "value": "2 community hospitals (Moseley Hall + West Heath) + 70+ clinic sites"},
            {"label": "Estate ownership", "value": "Heavy NHSPS / CHP leasehold + shared occupancy"},
            {"label": "LD inpatient", "value": "Specialist LD beds — anti-ligature + observation premium"},
            {"label": "Hard FM model", "value": "Mixed in-house + landlord-FM at NHSPS sites"},
            {"label": "Specialist dental", "value": "Birmingham Dental Hospital co-occupancy with Birmingham Dental"},
            {"label": "Net Zero milestone", "value": "Moseley Hall PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5% (energy + lease uplifts)"},
            {"label": "Peer benchmark", "value": "Above community-trust median (urban density + LD inpatient)"}
        ],
        "notes": "BCHC's premises spend is shaped by its community-trust model where most estate is leasehold (from NHS Property Services or Community Health Partnerships LIFTCos) — exposing the trust to landlord rent reviews and NHSPS service-charge volatility rather than direct ownership backlog. Specialist LD inpatient and rehab beds at Moseley Hall and West Heath drive ligature/observation-grade FM cost.",
        "sources": [
            "https://www.bhamcommunity.nhs.uk/about/news-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.property.nhs.uk/"
        ],
        "related": ["Birmingham Community Healthcare NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Blackpool Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Blackpool Teaching Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across Blackpool Victoria Hospital (acute, including Lancashire Cardiac Centre) plus Clifton Hospital (rehab), Fleetwood Hospital and extensive community estate across the Fylde coast. Coastal positioning generates external-fabric salt-corrosion premium.",
        "beneficiaries": "Blackpool, Fylde and Wyre 330,000+ catchment — A&E + cardiac at the Vic; rehab at Clifton; community across Fylde coast plus tertiary cardiac referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£21.45M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Blackpool Victoria + Clifton + Fleetwood + community sites"},
            {"label": "Lancashire Cardiac Centre", "value": "Tertiary cardiac — resilience-grade utilities + cath labs"},
            {"label": "Coastal estate", "value": "Salt-corrosion + winter-storm fabric-maintenance premium"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Tower block", "value": "Blackpool Victoria 1970s tower — significant lift/façade backlog"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at Blackpool Victoria"},
            {"label": "YoY change", "value": "c. +6% (energy + storm-resilience repairs)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (coastal premium)"}
        ],
        "notes": "Blackpool Teaching's premises cost reflects coastal positioning (storm-damage exposure on the Promenade-facing estate, salt corrosion of external fabric) and the resilience demands of the Lancashire Cardiac Centre tertiary service. The 1970s tower at Blackpool Victoria carries lift-modernisation and façade-renewal pressure typical of estate of that vintage.",
        "sources": [
            "https://www.bfwh.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Blackpool Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — North West Ambulance Service NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "North West Ambulance Service NHS Trust"}],
        "description": "Premises running costs across NWAS's distinctive ambulance estate — c.110 ambulance stations across Cheshire, Cumbria, Greater Manchester, Lancashire and Merseyside, plus regional EOCs (Emergency Operations Centres in Manchester + Bolton + Liverpool), HART base, Make Ready depots and training centres. Vehicle-fuel volume and station-utility cost dominate.",
        "beneficiaries": "7M+ NW England population — 999 + 111 service users, plus PTS (patient transport) clients across five-county footprint.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Civil Contingencies Act 2004 · Health and Care Act 2022 · NHS Estates Code",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£20.27M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "c. 110 ambulance stations + 3 EOCs + HART + Make Ready depots + training"},
            {"label": "EOCs", "value": "Manchester (Belle Vue), Bolton, Liverpool — resilience-grade utilities"},
            {"label": "Make Ready model", "value": "Centralised vehicle prep depots — different FM profile from station-based"},
            {"label": "HART base", "value": "Hazardous Area Response Team — specialist decon/equipment storage"},
            {"label": "Hard FM model", "value": "In-house Estates with vehicle-workshop sub-contracts"},
            {"label": "Net Zero milestone", "value": "EV-charging rollout at stations; ambulance-depot solar PV"},
            {"label": "YoY change", "value": "c. +6% (fuel + station refurb cycle)"},
            {"label": "Peer benchmark", "value": "Above ambulance-trust median (largest station network)"}
        ],
        "notes": "NWAS's premises spend reflects the largest English ambulance-station network outside London — c.110 stations across five counties — plus the operational resilience demands of three regional EOCs (post-Manchester Arena attack lessons embedded). Make Ready depot model concentrates vehicle prep at hubs but doesn't reduce station footprint. Cumbria rural fuel/winter-resilience adds premium.",
        "sources": [
            "https://www.nwas.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["North West Ambulance Service NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Salisbury NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Salisbury NHS Foundation Trust"}],
        "description": "Premises running costs at Salisbury District Hospital — single-acute-site trust on Odstock site (south of Salisbury) hosting nationally-commissioned spinal injuries (Duke of Cornwall Spinal Treatment Centre), burns and plastics, and major trauma reception services for Wessex.",
        "beneficiaries": "270,000+ Salisbury, S Wiltshire and W Hampshire catchment — plus national referrals to Spinal Injuries unit + regional burns/plastics + cleft lip/palate.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£19.62M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "Single-site Odstock acute campus + small community footprint"},
            {"label": "Spinal Injuries unit", "value": "Duke of Cornwall STC — long-stay specialist beds, accessibility-grade fit-out"},
            {"label": "Burns and plastics", "value": "Regional burns service — specialist HVAC + isolation-room load"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Site age", "value": "Mixed 1990s/2000s with older nucleus — moderate backlog"},
            {"label": "Net Zero milestone", "value": "Heat-decarbonisation feasibility under PSDS"},
            {"label": "YoY change", "value": "c. +5% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Above small-acute median per bed (specialist services premium)"}
        ],
        "notes": "Salisbury's premises spend is inflated above small-DGH-peer median by the specialist services it hosts on a single site — the Spinal Injuries Centre needs accessibility-grade fit-out and long-stay-bed support, the burns unit requires specialist HVAC and isolation, and the regional plastics + cleft service requires theatres of regional standard. The single-site model gives some FM economies but specialist services dominate cost.",
        "sources": [
            "https://www.salisbury.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Salisbury NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Royal United Hospitals Bath NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal United Hospitals Bath NHS Foundation Trust"}],
        "description": "Premises running costs at the RUH Combe Park (Bath) site, with the new Dyson Cancer Centre opened Apr 2024 (charity-co-funded by Sir James Dyson) and the RNHRD (Royal National Hospital for Rheumatic Diseases) services co-located after 2015 transfer. World-Heritage-City planning constraints shape backlog.",
        "beneficiaries": "500,000+ B&NES, W Wiltshire and Mendip catchment — A&E, planned care, rheumatic specialist (RNHRD legacy), cancer (Dyson Centre).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment) · Bath WHS planning",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£19.18M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "RUH Combe Park single-site + Dyson Cancer Centre opened Apr 2024"},
            {"label": "Dyson Cancer Centre", "value": "£40M new-build (charity-co-funded) — first full year of operating cost in 2024-25"},
            {"label": "RNHRD legacy", "value": "Rheumatic services on RUH site post-2015 transfer"},
            {"label": "Bath WHS", "value": "World Heritage Site planning constrains external works"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Net Zero milestone", "value": "Dyson Centre BREEAM Excellent target; PSDS-funded works"},
            {"label": "YoY change", "value": "c. +8% (Dyson Centre full-year opening + energy)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers"}
        ],
        "notes": "RUH Bath's premises line stepped up in 2024-25 with the first full year of Dyson Cancer Centre operating cost — a £40M charity-co-funded build that opened Apr 2024. The single-site model offers FM economies but Bath's World Heritage Site status constrains external works (façade, signage). Heat-pump and PV options need conservation-officer sign-off.",
        "sources": [
            "https://www.ruh.nhs.uk/about/news_and_publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://dysoncancercentre.org/"
        ],
        "related": ["Royal United Hospitals Bath NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Bedfordshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Bedfordshire Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across Bedfordshire's two-hospital footprint formed Apr 2020 — Bedford Hospital and Luton & Dunstable University Hospital. L&D had been a longstanding standalone FT; the merger created a cross-county estate with reconfiguration tensions.",
        "beneficiaries": "700,000+ Bedfordshire catchment — A&E + maternity at both Bedford and L&D; planned care across both sites; specialist services concentrated at L&D.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.87M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "Bedford Hospital + Luton & Dunstable + community"},
            {"label": "Merger", "value": "Apr 2020 Bedford + L&D merger — harmonisation costs continuing"},
            {"label": "L&D site", "value": "Mixed 1930s nucleus with later additions — backlog intensive"},
            {"label": "Bedford site", "value": "Smaller, more compact estate"},
            {"label": "Hard FM model", "value": "In-house Estates with sub-contracts"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works scoped at L&D"},
            {"label": "YoY change", "value": "c. +6% (energy + post-merger harmonisation)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers"}
        ],
        "notes": "Bedfordshire Hospitals' premises spend reflects the post-merger (Apr 2020) coordination of two distinct estates — Bedford with a tighter single-site footprint and L&D with a sprawling Dunstable Road campus carrying significant 1930s-nucleus backlog. Harmonisation of FM contracts and Estates teams continues to feed transition cost. NHP scheme aspirations were limited; both sites operate on extended-life model.",
        "sources": [
            "https://www.bedfordshirehospitals.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Bedfordshire Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across ASPH's two-site footprint — St Peter's Hospital (Chertsey, main acute) and Ashford Hospital (planned/elective hub). St Peter's has multiple buildings of varying age including Abbey Wing and Holly Wing; Ashford is smaller and more focused.",
        "beneficiaries": "410,000+ NW Surrey, Spelthorne and Runnymede catchment — A&E + maternity at St Peter's; elective + diagnostic at Ashford.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.55M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "St Peter's Chertsey + Ashford + community sites"},
            {"label": "Ashford planned-care", "value": "Smaller site reconfigured toward elective + diagnostic"},
            {"label": "Heathrow proximity", "value": "Ashford adjacent to Heathrow — access/aviation-noise considerations"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Backlog", "value": "St Peter's mixed-age estate carries moderate backlog"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works in pipeline"},
            {"label": "YoY change", "value": "c. +5% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers"}
        ],
        "notes": "ASPH's premises cost reflects a two-site model where St Peter's Chertsey carries the bulk of acute load and a mixed-age building stock, while Ashford operates as a more focused elective + diagnostic hub. Heathrow proximity at Ashford brings aviation-noise and ground-access considerations into estate planning. The trust has been part of the Surrey-wide Surrey Heartlands ICS estate strategy.",
        "sources": [
            "https://www.ashfordstpeters.nhs.uk/about-us/publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — South East Coast Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "South East Coast Ambulance Service NHS Foundation Trust"}],
        "description": "Premises running costs across SECAmb's ambulance estate — c.70 stations across Kent, Surrey, Sussex and parts of Hampshire/NE Hampshire, plus EOCs at Coxheath (Kent) and Crawley, training centre at Banstead, HART base, and 111 service infrastructure.",
        "beneficiaries": "5M+ South-East England population — 999 + 111 service users, plus PTS clients across Kent, Surrey, Sussex.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Civil Contingencies Act 2004 · Health and Care Act 2022 · NHS Estates Code",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£18.02M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "c. 70 ambulance stations + EOCs + HART + training"},
            {"label": "EOCs", "value": "Coxheath (Kent) + Crawley — resilience-grade utilities"},
            {"label": "Coastal estate", "value": "Kent + Sussex coastline — salt-corrosion premium on station fabric"},
            {"label": "Hard FM model", "value": "In-house Estates with vehicle-workshop sub-contracts"},
            {"label": "Make Ready", "value": "Hub-and-spoke vehicle prep model in train"},
            {"label": "Net Zero milestone", "value": "EV-charging rollout at stations"},
            {"label": "YoY change", "value": "c. +6% (fuel + station refurb)"},
            {"label": "Peer benchmark", "value": "Mid-range vs ambulance peers"}
        ],
        "notes": "SECAmb's premises spend reflects a dispersed station network across SE England where coastal exposure (Kent + Sussex) drives external-fabric maintenance, plus the resilience demands of two EOCs. The trust's operational performance issues (CQC ratings volatility) have not directly inflated this line but ongoing recovery investments touch on station refurb and Make Ready depot rollout. Banstead training centre adds non-station footprint.",
        "sources": [
            "https://www.secamb.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["South East Coast Ambulance Service NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Birmingham and Solihull Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Birmingham and Solihull Mental Health NHS Foundation Trust"}],
        "description": "MH premises running costs across BSMHFT's estate — Reaside Clinic (medium-secure forensic), Ardenleigh (women's secure + CAMHS secure), Tamarind Centre, plus Oleaster Centre and 60+ community MH sites across Birmingham and Solihull.",
        "beneficiaries": "MH/forensic service-users across Birmingham + Solihull (1.4M+ catchment) plus regionally-commissioned medium-secure forensic patients at Reaside.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.28M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "Reaside + Ardenleigh + Tamarind + Oleaster + 60+ community sites"},
            {"label": "Reaside medium-secure", "value": "Forensic medium-secure — security-grade FM premium"},
            {"label": "Ardenleigh", "value": "Women's secure + CAMHS secure — specialist anti-ligature load"},
            {"label": "Hard FM model", "value": "In-house Estates with security-cleared contractors"},
            {"label": "RAAC status", "value": "Some pre-1995 blocks under monitoring"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +6% (energy + secure-estate FM)"},
            {"label": "Peer benchmark", "value": "Above MH-trust median (forensic concentration)"}
        ],
        "notes": "BSMHFT's premises spend is shaped by a concentration of secure forensic estate (Reaside medium-secure, Ardenleigh women's-secure + CAMHS-secure) where physical-security perimeters, anti-ligature fit-out and observation infrastructure command a substantial premium over standard MH estate. Tamarind and Oleaster add adult-acute MH inpatient load. Birmingham urban-density sites carry parking + access pressure.",
        "sources": [
            "https://www.bsmhft.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/publications/raac-management-guidance"
        ],
        "related": ["Birmingham and Solihull Mental Health NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "London Ambulance Service NHS Trust"}],
        "description": "Premises running costs across LAS's distinctive central-urban ambulance estate — c.70 ambulance stations across Greater London, EOCs at Waterloo HQ + Bow, training centre, HART base in Wennington, plus 111 service estate. London-density real-estate inflates per-m² cost.",
        "beneficiaries": "9.5M Greater London population — 999 + 111 service users plus events cover (LAS provides Notting Hill, marathon, state-occasion cover).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Civil Contingencies Act 2004 · Health and Care Act 2022 · NHS Estates Code",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.16M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "c. 70 ambulance stations + EOCs + HART + training across London"},
            {"label": "EOCs", "value": "Waterloo HQ + Bow — resilience-grade utilities; redundancy critical"},
            {"label": "London density", "value": "High per-m² rent + congestion-charge ops impact + ULEZ"},
            {"label": "HART Wennington", "value": "Hazardous Area Response Team base — specialist decon facility"},
            {"label": "Hard FM model", "value": "In-house Estates with workshop sub-contracts"},
            {"label": "Net Zero milestone", "value": "EV-charging rollout; ULEZ-compliant fleet support"},
            {"label": "YoY change", "value": "c. +5% (London-property uplift + energy)"},
            {"label": "Peer benchmark", "value": "Above ambulance-trust median per station (London-density premium)"}
        ],
        "notes": "LAS's premises spend reflects London-property economics — higher per-station leasehold and freehold cost than other ambulance trusts, plus the operational complexity of state-occasion and large-event cover that requires the network to be evenly distributed across the 32 boroughs. Waterloo HQ EOC carries Tier 1 resilience-grade utility load. ULEZ-compliant fleet support and EV-charging build-out are recurring themes.",
        "sources": [
            "https://www.londonambulance.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["London Ambulance Service NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Homerton Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Homerton Healthcare NHS Foundation Trust"}],
        "description": "Premises running costs at Homerton Hospital (Hackney) and across the trust's integrated community estate (acquired City & Hackney community services, plus sexual-health Lambeth/Newham via CNWL/Barts service-line transfers). Hackney urban-density and East London growth shape demand.",
        "beneficiaries": "300,000+ City & Hackney catchment — A&E, maternity (regional perinatal service), neonatal, plus community + sexual-health patients across multiple boroughs.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£16.30M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Homerton Hospital + integrated community estate (Hackney) + sexual-health sites"},
            {"label": "Site age", "value": "Homerton 1986-vintage with later phased additions — moderate backlog"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Sexual-health", "value": "Cross-borough sexual-health service-line load"},
            {"label": "Maternity", "value": "Regional perinatal expansion in train"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +6% (energy + community-estate inflation)"},
            {"label": "Peer benchmark", "value": "Mid-range vs London acute peers"}
        ],
        "notes": "Homerton's premises spend reflects a single-site acute trust with an unusually large community-services footprint (City & Hackney integration) plus cross-borough sexual-health service contracts. Hackney population growth and demand pressure on A&E/maternity feed estate intensification. Homerton Hospital's 1986 build is mid-life with backlog manageable but rising.",
        "sources": [
            "https://www.homerton.nhs.uk/our-publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Homerton Healthcare NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Mid Yorkshire Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Mid Yorkshire Hospitals NHS Trust"}],
        "description": "Premises running costs across Mid Yorks's three-site footprint — Pinderfields (Wakefield, main acute, PFI 2011-vintage), Dewsbury & District (planned/elective hub), and Pontefract Hospital (urgent care + planned). PFI unitary charge for Pinderfields/Pontefract sits in D4_11 not here.",
        "beneficiaries": "550,000+ Wakefield, Dewsbury, Pontefract catchment — A&E + maternity at Pinderfields; elective at Dewsbury; urgent care at Pontefract.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.76M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "Pinderfields + Dewsbury + Pontefract"},
            {"label": "PFI footprint", "value": "Pinderfields/Pontefract PFI unitary charge in D4_11 NOT here"},
            {"label": "Hard FM model", "value": "PFI-co-located at Pinderfields/Pontefract; in-house at Dewsbury"},
            {"label": "Dewsbury planned-care", "value": "Reconfigured planned/elective hub"},
            {"label": "Site complexity", "value": "PFI-non-PFI hybrid generates dual cost-tracking"},
            {"label": "Net Zero milestone", "value": "Dewsbury PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5% (Dewsbury energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Below acute median (PFI absorbs much of FM cost elsewhere)"}
        ],
        "notes": "Mid Yorks's Premises (other) line looks low among medium-acute peers because the major PFI hospital (Pinderfields, opened 2011 to replace Clayton Hospital) has its hard-FM unitary charge captured in a separate accounting line. The Dewsbury & District site (non-PFI) plus Pontefract (PFI) and shared services make up the bulk of this line, with Net Zero progression concentrated at Dewsbury.",
        "sources": [
            "https://www.midyorks.nhs.uk/our-publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["The Mid Yorkshire Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Premises running costs at Stepping Hill Hospital (single-site acute in Stockport) plus integrated community estate across Stockport borough. Stepping Hill is a mixed-age site with an older nucleus + later developments; community estate is mostly NHSPS / CHP leasehold.",
        "beneficiaries": "300,000+ Stockport catchment + parts of High Peak — A&E, maternity, planned care at Stepping Hill; community services across Stockport.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.15M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Stepping Hill acute + integrated community estate across Stockport"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Site age", "value": "Stepping Hill mixed-age — older Victorian nucleus + later phases"},
            {"label": "Community estate", "value": "Mostly NHSPS / CHP leasehold"},
            {"label": "GMICS context", "value": "Greater Manchester ICB shared estate strategy"},
            {"label": "Net Zero milestone", "value": "Stepping Hill heat-pump scheme advancing"},
            {"label": "YoY change", "value": "c. +5% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers"}
        ],
        "notes": "Stockport's premises cost reflects a mid-size single-acute-site DGH model where Stepping Hill's mixed-age building stock (with backlog) plus an integrated community-services portfolio (mostly leasehold) shape the line. Greater Manchester ICB-wide estate strategy provides some shared-services overhead. Stepping Hill's role as the only acute provider in Stockport gives high public-asset visibility.",
        "sources": [
            "https://www.stockport.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.property.nhs.uk/"
        ],
        "related": ["Stockport NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Medway NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Medway NHS Foundation Trust"}],
        "description": "Premises running costs at Medway Maritime Hospital (Gillingham, single-site acute on a former Royal Naval Hospital footprint). Mixed-age estate from 1905-listed buildings to 1990s additions; long-running financial-recovery context constrains capital-driven backlog reduction.",
        "beneficiaries": "424,000+ Medway towns + Swale catchment — A&E, maternity, paediatrics, planned care at Maritime.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.81M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "Medway Maritime single-site acute + small community footprint"},
            {"label": "Listed buildings", "value": "Some Naval-era listed structures — conservation constraints"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Recovery context", "value": "Multi-year financial-special-measures legacy — constrained capex"},
            {"label": "Backlog", "value": "Significant relative to peer (constrained capex history)"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works in pipeline"},
            {"label": "YoY change", "value": "c. +6% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Below acute median per bed (capex constraint suppresses opex)"}
        ],
        "notes": "Medway's premises cost is shaped by a single-site model on the historic Royal Naval Hospital footprint (1905) with mixed conservation and modern fabric, and by a long financial-recovery history that constrained capital investment — which paradoxically suppresses some operational maintenance spend while building up backlog. Listed-building constraints limit retrofit options for Net Zero.",
        "sources": [
            "https://www.medway.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Medway NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Southern Health NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Southern Health NHS Foundation Trust"}],
        "description": "MH and community premises running costs across Southern Health's Hampshire footprint — Antelope House (Southampton, MH inpatient), Melbury Lodge (Winchester), Parklands (Basingstoke), plus extensive community estate across Hampshire including LD inpatient services.",
        "beneficiaries": "1.4M MH/LD/community service-users across Hampshire — adult acute MH, CAMHS, LD inpatient, and community physical-health services.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.32M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Antelope House + Melbury Lodge + Parklands + 80+ community sites"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "MH-specific", "value": "Anti-ligature + observation-line + s.136 suite premium"},
            {"label": "LD inpatient", "value": "LD assessment & treatment beds — specialist fit-out"},
            {"label": "Mazars Review legacy", "value": "Ongoing safety-culture investments since 2015 review"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH-trust peers"}
        ],
        "notes": "Southern Health's premises spend reflects a typical MH/community model with adult acute MH at three Hampshire hubs plus dispersed community estate. The trust's history (Mazars Review 2015 on patient deaths) drove sustained investment in observation-grade premises, anti-ligature retrofit and s.136 suite improvements which feed running cost. Hampshire-wide ICS estate coordination shapes shared-services overhead.",
        "sources": [
            "https://www.southernhealth.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Southern Health NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — North West Anglia NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "North West Anglia NHS Foundation Trust"}],
        "description": "Premises running costs across NWAFT's three-site footprint — Peterborough City Hospital (PFI 2010-vintage, unitary charge in D4_11), Hinchingbrooke Hospital (Huntingdon, RAAC-affected), and Stamford and Rutland Hospital. RAAC remediation at Hinchingbrooke a major recent driver.",
        "beneficiaries": "800,000+ Peterborough, Cambridgeshire, Rutland and parts of Lincolnshire catchment — A&E + maternity at Peterborough + Hinchingbrooke; community at Stamford.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£14.03M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "Peterborough City + Hinchingbrooke + Stamford & Rutland"},
            {"label": "PFI footprint", "value": "Peterborough City PFI unitary charge in D4_11 NOT here"},
            {"label": "RAAC status", "value": "Hinchingbrooke is among 7 'national priority' RAAC trusts — full rebuild required"},
            {"label": "NHP scheme status", "value": "Hinchingbrooke RAAC rebuild in NHP — confirmed despite Reset Jan 2025"},
            {"label": "Hard FM model", "value": "PFI co-located at Peterborough; in-house at Hinchingbrooke + Stamford"},
            {"label": "Net Zero milestone", "value": "Constrained at Hinchingbrooke pending rebuild"},
            {"label": "YoY change", "value": "c. +10% (RAAC mitigation + Hinchingbrooke decant cost)"},
            {"label": "Peer benchmark", "value": "Above acute median (RAAC mitigation premium)"}
        ],
        "notes": "NWAFT's Premises (other) line is dominated by RAAC mitigation at Hinchingbrooke — one of seven national-priority RAAC hospitals where mitigation works (props, monitoring, partial decant) generate substantial operating cost premium until the NHP rebuild is delivered. The Hinchingbrooke rebuild was reaffirmed in the NHP Reset (Jan 2025). Peterborough City PFI charges sit in a separate accounting line.",
        "sources": [
            "https://www.nwangliaft.nhs.uk/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["North West Anglia NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Northamptonshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Northamptonshire Healthcare NHS Foundation Trust"}],
        "description": "MH and community premises running costs across NHFT's Northamptonshire estate — Berrywood Hospital (Northampton, MH inpatient), St Mary's Hospital (Kettering, MH inpatient), plus extensive community + paediatric estate across the county. Operates as joint provider in the integrated Northamptonshire model.",
        "beneficiaries": "750,000+ Northamptonshire MH, LD, community and children's-services users — adult acute MH at Berrywood + St Mary's; community + paediatric services countywide.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£13.28M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Berrywood + St Mary's + 70+ community sites"},
            {"label": "MH-specific", "value": "Anti-ligature + observation + s.136 premium"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Community estate", "value": "Mostly NHSPS / CHP leasehold across county"},
            {"label": "Children's services", "value": "Paediatric community services drive specialist fit-out"},
            {"label": "Net Zero milestone", "value": "Berrywood PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5% (energy + lease uplifts)"},
            {"label": "Peer benchmark", "value": "Mid-range vs community/MH peers"}
        ],
        "notes": "NHFT's premises cost reflects an integrated MH + community + children's model with two MH inpatient hubs (Berrywood, St Mary's) and extensive leasehold community estate. The trust operates within the Northamptonshire-wide integrated provider model alongside the acute trust group. Children's-services contracts drive specialist fit-out for paediatric outpatient and therapy spaces.",
        "sources": [
            "https://www.nhft.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.property.nhs.uk/"
        ],
        "related": ["Northamptonshire Healthcare NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Cambridgeshire Community Services NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Cambridgeshire Community Services NHS Trust"}],
        "description": "Premises running costs across CCS's distinctive multi-region community estate — Cambridgeshire + Peterborough + Bedfordshire + Luton + parts of Norfolk, plus children's-services contracts across multiple ICBs. Most estate is NHSPS / CHP leasehold; trust holds some community-hospital footprint.",
        "beneficiaries": "Community service-users across Cambridgeshire, Peterborough, Bedfordshire, Luton + cross-region children's services — district nursing, therapies, school nursing, 0-19 children's services.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£13.06M"},
            {"label": "Share of trust total opex", "value": "c. 7%"},
            {"label": "Estate scale", "value": "Multi-region — 80+ clinic sites + community-hospital footprint"},
            {"label": "Estate ownership", "value": "Predominantly NHSPS / CHP leasehold + some directly held"},
            {"label": "Cross-ICB span", "value": "Cambs, Beds + Luton + parts of Norfolk — multi-commissioner"},
            {"label": "Children's services", "value": "0-19 children's services drives clinic-fit-out spec"},
            {"label": "Hard FM model", "value": "Mixed in-house + landlord-FM at NHSPS sites"},
            {"label": "Net Zero milestone", "value": "Constrained by leasehold structure"},
            {"label": "YoY change", "value": "c. +5% (lease uplifts + energy)"},
            {"label": "Peer benchmark", "value": "Above community-trust median (multi-region dispersion)"}
        ],
        "notes": "CCS's premises cost is unusually high relative to revenue (c. 7% of opex) because community trusts have a dispersed estate footprint without the economies of single-site acute peers. The trust's cross-region operating model (operating contracts across multiple ICBs) drives geographically dispersed clinic estate, mostly leased from NHSPS or CHP LIFTCos which exposes it to landlord rent reviews and service-charge volatility.",
        "sources": [
            "https://www.cambscommunityservices.nhs.uk/about-us/publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.property.nhs.uk/"
        ],
        "related": ["Cambridgeshire Community Services NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Norfolk and Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Norfolk and Suffolk NHS Foundation Trust"}],
        "description": "MH premises running costs across NSFT's two-county estate — Hellesdon Hospital (Norwich, MH inpatient), Northgate (Great Yarmouth), Wedgwood House (Bury St Edmunds), Woodlands (Ipswich) — plus extensive community MH estate. The trust has been in special-measures cycle multiple times.",
        "beneficiaries": "1.6M MH/LD service-users across Norfolk + Suffolk — adult acute MH, CAMHS, LD, eating-disorder and older-people's MH services.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.47M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Hellesdon + Northgate + Wedgwood + Woodlands + 60+ community sites"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Special-measures legacy", "value": "Repeated CQC enforcement — sustained safety-investment cost"},
            {"label": "Anti-ligature", "value": "Significant ligature-mitigation programme post 2015 cluster"},
            {"label": "RAAC status", "value": "Some pre-1995 community blocks under monitoring"},
            {"label": "Net Zero milestone", "value": "Hellesdon PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5-7% (energy + safety remediation)"},
            {"label": "Peer benchmark", "value": "Mid-range despite scale (rural dispersion partly offset)"}
        ],
        "notes": "NSFT's premises cost reflects a two-county MH estate with a sustained safety-investment programme driven by repeated CQC special-measures interventions — anti-ligature retrofit, observation upgrades, s.136 suite improvements all feed running cost. The geographic span across Norfolk + Suffolk drives dispersed FM load. Hellesdon (Norwich) is the largest single inpatient site.",
        "sources": [
            "https://www.nsft.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.cqc.org.uk/provider/RMY"
        ],
        "related": ["Norfolk and Suffolk NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Walsall Healthcare NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Walsall Healthcare NHS Trust"}],
        "description": "Premises running costs at Walsall Manor Hospital (single-site acute in Walsall) plus integrated community estate across Walsall borough. The Manor underwent the £170M new-build PFI in 2010 (PFI charge in D4_11) — 'Premises (other)' captures non-PFI elements + community.",
        "beneficiaries": "270,000+ Walsall catchment — A&E, maternity, paediatrics at Manor; community services across Walsall.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£12.16M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "Walsall Manor single-site acute + integrated community estate"},
            {"label": "PFI footprint", "value": "Walsall Manor 2010 PFI unitary charge in D4_11 NOT here"},
            {"label": "Hard FM model", "value": "PFI-co-located at Manor; in-house at community"},
            {"label": "Black Country ICS", "value": "Cross-trust shared-services with Royal Wolverhampton + Dudley"},
            {"label": "Site age", "value": "Manor 2010 build — relatively low backlog"},
            {"label": "Net Zero milestone", "value": "PSDS-funded community-estate heat works"},
            {"label": "YoY change", "value": "c. +4% (community-estate energy + lease uplifts)"},
            {"label": "Peer benchmark", "value": "Below acute median (PFI absorbs much of FM)"}
        ],
        "notes": "Walsall's Premises (other) line is suppressed below peer median because the relatively new (2010) Manor PFI captures most hard-FM cost in a separate accounting line. The non-PFI line largely reflects community estate (NHSPS / CHP leasehold) plus shared-services overhead through the Black Country ICS estate strategy. Black Country Pathology + cross-trust sharing reduces some duplicated cost.",
        "sources": [
            "https://www.walsallhealthcare.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.property.nhs.uk/"
        ],
        "related": ["Walsall Healthcare NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Coventry and Warwickshire Partnership NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Coventry and Warwickshire Partnership NHS Trust"}],
        "description": "MH and community premises running costs across CWPT's two-area estate — Caludon Centre (Coventry, MH inpatient) and St Michael's (Warwick), plus extensive community + LD estate across Coventry and Warwickshire. Operates within the Coventry & Warwickshire ICS provider collaborative.",
        "beneficiaries": "1M+ Coventry + Warwickshire MH/LD/community service-users — adult acute MH at Caludon + St Michael's; CAMHS; LD inpatient + community services.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£11.24M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "Caludon + St Michael's + 60+ community sites"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "MH-specific", "value": "Anti-ligature + observation + s.136 suite premium"},
            {"label": "LD inpatient", "value": "LD assessment & treatment beds drive specialist fit-out"},
            {"label": "Community estate", "value": "Mostly NHSPS / CHP leasehold"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at Caludon"},
            {"label": "YoY change", "value": "c. +5% (energy + lease uplifts)"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH/community peers"}
        ],
        "notes": "CWPT's premises cost reflects a typical MH + community + LD model spanning two distinct urban (Coventry) and county (Warwickshire) footprints. Caludon Centre is the larger MH inpatient hub; St Michael's serves Warwickshire. Community estate is dispersed across the C&W ICS footprint, mostly leased from NHSPS or CHP LIFTCos. Anti-ligature programme remains a recurring driver.",
        "sources": [
            "https://www.covwarkpt.nhs.uk/publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.property.nhs.uk/"
        ],
        "related": ["Coventry and Warwickshire Partnership NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Gloucestershire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Gloucestershire Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across GHFT's two-site footprint — Gloucestershire Royal Hospital (Gloucester) and Cheltenham General Hospital. The trust operates the Hospitals One Gloucestershire reconfiguration with services specialising between the two sites; conservation constraints in central Cheltenham apply.",
        "beneficiaries": "650,000+ Gloucestershire catchment — A&E + maternity at Gloucester; planned care + cancer at Cheltenham.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£10.68M"},
            {"label": "Share of trust total opex", "value": "c. 1.5%"},
            {"label": "Estate scale", "value": "Gloucestershire Royal + Cheltenham General + community"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Reconfiguration", "value": "Fit for the Future programme — site specialisation in train"},
            {"label": "Cheltenham conservation", "value": "Town-centre conservation-area constraints on retrofit"},
            {"label": "Backlog", "value": "Mid-range backlog vs acute peers"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5% (energy + transition)"},
            {"label": "Peer benchmark", "value": "Below acute median per bed (relatively efficient FM)"}
        ],
        "notes": "GHFT's Premises (other) line looks low among medium-acute trusts (c. 1.5% of opex) reflecting relatively efficient in-house FM operations and the transition phase of the Fit for the Future reconfiguration where site specialisation is reducing some duplication. Cheltenham General's town-centre conservation-area location constrains external retrofit (façade, plant) options. Gloucestershire Royal carries more of the modern-build load.",
        "sources": [
            "https://www.gloshospitals.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Gloucestershire Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — James Paget University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "James Paget University Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs at James Paget Hospital (Gorleston, near Great Yarmouth) — a single-site acute trust. JPUH is one of the seven 'national priority' RAAC hospitals requiring full rebuild; mitigation works dominate current operational cost.",
        "beneficiaries": "230,000+ Great Yarmouth, Lowestoft and Waveney catchment — A&E, maternity, paediatrics, planned care.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£9.61M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Single-site acute + small community footprint"},
            {"label": "RAAC status", "value": "1 of 7 national-priority RAAC trusts — full rebuild required"},
            {"label": "NHP scheme status", "value": "JPUH rebuild reaffirmed in NHP Reset Jan 2025"},
            {"label": "Mitigation works", "value": "Roof props + monitoring + partial decant; in-house Estates manage day-to-day FM"},
            {"label": "Coastal estate", "value": "Salt-corrosion premium on external fabric"},
            {"label": "Net Zero milestone", "value": "Constrained pending rebuild"},
            {"label": "YoY change", "value": "c. +12% (RAAC mitigation + decant cost)"},
            {"label": "Peer benchmark", "value": "Above small-acute median (RAAC mitigation premium)"}
        ],
        "notes": "James Paget's premises cost is dominated by RAAC mitigation — as one of seven national-priority RAAC hospitals, the trust runs costly props, monitoring and partial-decant arrangements until the NHP-funded rebuild delivers (reaffirmed in the Jan 2025 Reset). Coastal exposure adds external-fabric premium. The single-site model concentrates risk: any RAAC failure would have full-trust operational impact.",
        "sources": [
            "https://www.jpaget.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["James Paget University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Dudley Group NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Dudley Group NHS Foundation Trust"}],
        "description": "Premises running costs across Dudley Group's three-site footprint — Russells Hall Hospital (Dudley, PFI 2005 — unitary charge in D4_11), Corbett Hospital (Stourbridge, day-case + outpatient), and Guest Hospital (Dudley, planned care). Russells Hall PFI dominates hard-FM economics.",
        "beneficiaries": "450,000+ Dudley borough catchment — A&E + maternity at Russells Hall; day-case at Corbett; planned + outpatient at Guest.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£9.34M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "Russells Hall + Corbett + Guest"},
            {"label": "PFI footprint", "value": "Russells Hall 2005 PFI unitary charge in D4_11 NOT here"},
            {"label": "Hard FM model", "value": "PFI-co-located at Russells Hall; in-house at Corbett + Guest"},
            {"label": "Black Country ICS", "value": "Shared-services with Walsall + Wolverhampton + Sandwell"},
            {"label": "Net Zero milestone", "value": "Constrained at Russells Hall by PFI VFM cycle"},
            {"label": "YoY change", "value": "c. +5% (Corbett/Guest energy + soft-FM)"},
            {"label": "Site age", "value": "Russells Hall 2005 PFI; Corbett older Victorian-Edwardian nucleus"},
            {"label": "Peer benchmark", "value": "Below acute median (PFI absorbs much of FM)"}
        ],
        "notes": "Dudley Group's Premises (other) line is suppressed below peer median because the Russells Hall PFI (opened 2005) captures the bulk of hard-FM cost in a separate PFI-charge accounting line. Net Zero progression at Russells Hall is constrained by the PFI value-for-money mechanism — any retrofit needs to be negotiated through the SPV. Corbett and Guest carry the in-house FM line.",
        "sources": [
            "https://www.dgft.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["The Dudley Group NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Cheshire and Wirral Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Cheshire and Wirral Partnership NHS Foundation Trust"}],
        "description": "MH, LD and community premises running costs across CWP's distinctive footprint — Bowmere Hospital (Chester, MH inpatient), Springview (Wirral), Soss Moss (LD), plus extensive community estate across Cheshire West, Cheshire East and the Wirral peninsula.",
        "beneficiaries": "1M+ MH/LD service-users across Cheshire + Wirral — adult acute MH at Bowmere + Springview, LD specialist services, community + offender-health.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£8.94M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Bowmere + Springview + Soss Moss + 70+ community sites"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "MH-specific", "value": "Anti-ligature + observation + s.136 premium"},
            {"label": "LD inpatient", "value": "Soss Moss specialist LD service"},
            {"label": "Cross-county", "value": "Cheshire West + East + Wirral — multi-place coordination"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at Bowmere"},
            {"label": "YoY change", "value": "c. +5% (energy + community-estate inflation)"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH peers"}
        ],
        "notes": "CWP's premises spend reflects a three-place MH + LD + community model spanning Cheshire West, Cheshire East and the Wirral. Specialist LD services at Soss Moss carry the highest fit-out premium. The trust's involvement in offender-health contracts adds custodial-grade FM constraint at certain HMP/IRC sites. Community estate is mostly NHSPS / CHP leasehold.",
        "sources": [
            "https://www.cwp.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.property.nhs.uk/"
        ],
        "related": ["Cheshire and Wirral Partnership NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Walton Centre NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Walton Centre NHS Foundation Trust"}],
        "description": "Premises running costs at the Walton Centre (Aintree, Liverpool) — England's only standalone specialist neurosciences NHS trust. Single-site model on the Aintree University Hospital campus; high resilience-grade utilities for neurosurgery, neuro-ICU, neuroradiology + Cheshire-Merseyside Rehabilitation Centre.",
        "beneficiaries": "Tertiary neurosciences referrals from Cheshire, Merseyside, Lancashire, North Wales, Isle of Man — neurosurgery, neuro-ICU, complex epilepsy, MS, neuroradiology, neurorehab.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£8.62M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "Single-site specialist + Sid Watkins Building (research/rehab)"},
            {"label": "Specialist service", "value": "Only standalone NHS neurosciences trust in England"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Resilience grade", "value": "Neuro-ICU + neurosurgery — Tier 1 utility resilience"},
            {"label": "Co-location", "value": "Aintree campus shared with Liverpool University Hospitals"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump scoping"},
            {"label": "YoY change", "value": "c. +5% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Above specialist median per m² (neuro resilience premium)"}
        ],
        "notes": "The Walton Centre's premises cost reflects its unique status as the only standalone specialist neurosciences NHS trust in England, with Tier 1 resilience-grade utilities supporting 24/7 neurosurgery, neuro-ICU and neuroradiology. The Sid Watkins Building (opened 2015) houses research and the rehab centre, adding a recent-build element to the cost base. Co-location with Liverpool University Hospitals on the Aintree campus enables some shared FM economies.",
        "sources": [
            "https://www.thewaltoncentre.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["The Walton Centre NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Wye Valley NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Wye Valley NHS Trust"}],
        "description": "Premises running costs across Wye Valley's Herefordshire estate — Hereford County Hospital (single acute), plus Bromyard, Leominster, Ross-on-Wye and Hereford community hospitals. Rural sparsely-populated catchment makes the trust one of the most geographically dispersed in England relative to revenue.",
        "beneficiaries": "190,000+ Herefordshire catchment + parts of mid-Wales — A&E + maternity at Hereford; intermediate care at four community hospitals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£8.10M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "Hereford County + 4 community hospitals across rural Herefordshire"},
            {"label": "PFI footprint", "value": "Hereford County PFI unitary charge in D4_11 NOT here"},
            {"label": "Rural dispersion", "value": "Sparse rural catchment — fuel + winter-resilience premium"},
            {"label": "Hard FM model", "value": "PFI co-located at Hereford; in-house at community"},
            {"label": "Site age", "value": "Hereford County 2002 PFI; community hospitals mixed-age"},
            {"label": "Net Zero milestone", "value": "Community-hospital heat works under PSDS"},
            {"label": "YoY change", "value": "c. +6% (rural fuel + lease uplifts)"},
            {"label": "Peer benchmark", "value": "Mid-range despite rural dispersion (PFI absorbs Hereford FM)"}
        ],
        "notes": "Wye Valley's Premises (other) line is partially suppressed by the Hereford County 2002 PFI which captures the main hospital's hard-FM cost separately. The four community hospitals (Bromyard, Leominster, Ross-on-Wye, plus a Hereford community unit) drive most of the in-house line — winter-resilience, generator cover and rural fuel are recurring drivers. Cross-border patient flow with Wales adds some commissioner complexity.",
        "sources": [
            "https://www.wyevalley.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Wye Valley NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — North Middlesex University Hospital NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "North Middlesex University Hospital NHS Trust"}],
        "description": "Premises running costs at North Middlesex Hospital (Edmonton, Enfield) — single-site acute trust with PFI-funded redevelopment opened 2010 (PFI charge in D4_11). The trust is in the process of being absorbed into the Royal Free London group (target completion through 2024-25).",
        "beneficiaries": "350,000+ Enfield, Haringey + Waltham Forest catchment — A&E (one of London's busiest), maternity, paediatrics.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£7.67M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "Single-site North Middlesex (PFI new-build 2010)"},
            {"label": "PFI footprint", "value": "2010 PFI unitary charge in D4_11 NOT here"},
            {"label": "Hard FM model", "value": "PFI-co-located"},
            {"label": "RFL group absorption", "value": "Merger with Royal Free London Group in train through 2024-25"},
            {"label": "A&E volume", "value": "Among London's busiest A&Es per capita"},
            {"label": "Net Zero milestone", "value": "Constrained by PFI VFM cycle"},
            {"label": "YoY change", "value": "c. +4% (energy + transition cost)"},
            {"label": "Peer benchmark", "value": "Below acute median (PFI absorbs much of FM)"}
        ],
        "notes": "North Middlesex's Premises (other) line sits below acute peer median because the 2010 PFI captures the bulk of hard-FM cost in a separate accounting line — leaving this line for non-PFI elements + small community footprint + transition cost. The trust's group-absorption into Royal Free London is feeding harmonisation cost into 2024-25. A&E pressure remains among London's most acute on a per-capita basis.",
        "sources": [
            "https://www.northmid.nhs.uk/our-publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["North Middlesex University Hospital NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — North Staffordshire Combined Healthcare NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "North Staffordshire Combined Healthcare NHS Trust"}],
        "description": "MH and LD premises running costs across NSCHT's Stoke-on-Trent + N Staffs estate — Harplands Hospital (Stoke, MH inpatient hub), plus community MH estate across Stoke and northern Staffordshire including LD specialist services.",
        "beneficiaries": "450,000+ MH/LD service-users in Stoke-on-Trent + North Staffordshire — adult acute MH at Harplands, CAMHS, LD inpatient + community MH services.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£6.73M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "Harplands MH inpatient hub + 30+ community sites"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "MH-specific", "value": "Anti-ligature + observation + s.136 premium"},
            {"label": "LD inpatient", "value": "LD assessment & treatment beds — specialist fit-out"},
            {"label": "Stoke ICS", "value": "Staffordshire & Stoke-on-Trent ICS shared estate strategy"},
            {"label": "Net Zero milestone", "value": "Harplands PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Mid-range vs small-MH peers"}
        ],
        "notes": "NSCHT's premises cost reflects a focused single-area MH + LD trust serving Stoke-on-Trent and northern Staffordshire — Harplands Hospital is the central adult-MH hub, with community MH estate dispersed across the Potteries and rural N Staffs. The relatively contained geography (vs cross-county MH peers) keeps FM dispersion manageable, but specialist LD beds carry a fit-out premium.",
        "sources": [
            "https://www.combined.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["North Staffordshire Combined Healthcare NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Queen Victoria Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Queen Victoria Hospital NHS Foundation Trust"}],
        "description": "Premises running costs at Queen Victoria Hospital (East Grinstead) — England's specialist reconstructive surgery centre, founded as the wartime burns/plastics unit (Sir Archibald McIndoe's 'Guinea Pig Club'). Heritage estate plus modern theatre block; specialist fit-out for plastics, burns, corneoplastic and complex hand surgery.",
        "beneficiaries": "National + regional referrals for reconstructive surgery, burns, corneoplastic, head & neck oncology — long-stay specialist patients with complex rehab.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£6.47M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "Single-site specialist East Grinstead + small satellite footprint"},
            {"label": "Specialist services", "value": "Plastics, burns, corneoplastic, complex hand, head & neck oncology"},
            {"label": "Heritage estate", "value": "WWII McIndoe-era buildings of historic significance"},
            {"label": "Hard FM model", "value": "In-house Estates"},
            {"label": "Specialist HVAC", "value": "Burns unit + theatres carry specialist HVAC + isolation premium"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works (heritage-constrained)"},
            {"label": "YoY change", "value": "c. +5% (energy + specialist FM)"},
            {"label": "Peer benchmark", "value": "Above specialist median per m² (heritage + burns specialist)"}
        ],
        "notes": "QVH's premises cost is shaped by its specialist reconstructive role — burns and plastics theatres require specialist HVAC, isolation and laminar-flow capability beyond standard surgical fit-out. The heritage Guinea Pig Club-era buildings (McIndoe's 1940s pioneering reconstructive ward) carry conservation constraints on retrofit. Long-stay patients with complex rehab needs require accessibility-grade fit-out. Highest premises share of opex among small-specialist peers.",
        "sources": [
            "https://www.qvh.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Queen Victoria Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "Premises running costs at RJAH (Gobowen, Oswestry, Shropshire) — England's only specialist orthopaedic NHS FT founded 1900 by Dame Agnes Hunt and Sir Robert Jones. Rural single-site model; wartime-vintage buildings alongside modern Headley Court Veterans rehab partnership.",
        "beneficiaries": "Tertiary orthopaedic referrals from across England + N Wales — complex spinal, paediatric ortho, sports medicine, bone tumour, oncology, plus veterans rehab.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£6.12M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "Single-site rural specialist + veterans rehab partnership"},
            {"label": "Specialist service", "value": "Tertiary orthopaedic — only specialist ortho FT in England"},
            {"label": "Heritage estate", "value": "1900-vintage buildings — Edwardian convalescent design"},
            {"label": "Rural premium", "value": "Gobowen-Oswestry rural setting — fuel + winter-resilience; in-house Estates"},
            {"label": "Theatre fit-out", "value": "Ultra-clean orthopaedic theatres — laminar flow premium"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump scoping"},
            {"label": "YoY change", "value": "c. +5% (energy + rural fuel)"},
            {"label": "Peer benchmark", "value": "Above orthopaedic-comparator median per m² (rural + heritage)"}
        ],
        "notes": "RJAH's premises spend reflects its unique status as the only specialist orthopaedic NHS FT in England, with ultra-clean laminar-flow theatres for joint replacement and complex spinal surgery, plus heritage Edwardian convalescent buildings (1900) carrying conservation constraints. The rural Gobowen setting drives winter resilience and fuel costs typical of remote sites. The veterans rehab partnership adds a specialist service line.",
        "sources": [
            "https://www.rjah.nhs.uk/About-Us/Publications.aspx",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Liverpool Heart and Chest Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Liverpool Heart and Chest Hospital NHS Foundation Trust"}],
        "description": "Premises running costs at Liverpool Heart and Chest Hospital (Broadgreen, Liverpool) — specialist cardiothoracic NHS FT serving Cheshire and Merseyside. Single-site model with cath labs, hybrid theatres, cardiothoracic ICU and respiratory beds; high resilience-grade utility load.",
        "beneficiaries": "Tertiary cardiothoracic + respiratory referrals from Cheshire, Merseyside, Lancashire, Isle of Man — cardiac surgery, complex valve, transplant, lung surgery, cardiothoracic anaesthesia.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£4.14M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "Single-site Broadgreen specialist cardiothoracic"},
            {"label": "Specialist service", "value": "Cardiothoracic surgery, valve surgery, transplant assessment"},
            {"label": "Resilience grade", "value": "Cardiac theatres + ICU — Tier 1 utility resilience; in-house Estates"},
            {"label": "Cath labs", "value": "High-spec power + radiation-shielding fit-out"},
            {"label": "Co-location", "value": "Broadgreen campus shared with Liverpool University Hospitals"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works"},
            {"label": "YoY change", "value": "c. +5% (energy + soft-FM)"},
            {"label": "Peer benchmark", "value": "Below specialist median (small efficient site)"}
        ],
        "notes": "LHCH's premises cost is unusually low per-bed for a specialist cardiothoracic centre, reflecting an efficient single-site model and shared-services arrangements with Liverpool University Hospitals on the Broadgreen campus. Cath labs and hybrid theatres carry specialist power and radiation-shielding fit-out, but the focused service mix avoids the full multi-specialty estate load of acute peers. Tier 1 resilience for cardiac surgery is mandatory.",
        "sources": [
            "https://www.lhch.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Liverpool Heart and Chest Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Norfolk Community Health and Care NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Norfolk Community Health and Care NHS Trust"}],
        "description": "Premises running costs across NCH&C's Norfolk-wide community estate — Benjamin Court (Cromer), Kelling Hospital (Holt), Cromer Hospital, Swaffham Community, plus c.50 community clinic sites. Mostly NHSPS / CHP leasehold; some directly held community-hospital sites.",
        "beneficiaries": "Norfolk community service-users — district nursing, community hospital intermediate care, end-of-life, paediatric community, learning-disability, school nursing.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£3.53M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "4 community hospitals + c. 50 clinic sites across Norfolk"},
            {"label": "Estate ownership", "value": "Mixed directly-held community hospitals + NHSPS / CHP leasehold clinics"},
            {"label": "Rural dispersion", "value": "Norfolk coast + Broads + rural west — wide footprint"},
            {"label": "Hard FM model", "value": "Mixed in-house + landlord-FM at NHSPS sites"},
            {"label": "Net Zero milestone", "value": "Community-hospital heat works under PSDS"},
            {"label": "YoY change", "value": "c. +4% (lease uplifts + energy)"},
            {"label": "Peer benchmark", "value": "Mid-range vs small-community peers"}
        ],
        "notes": "NCH&C's premises cost reflects a small Norfolk-wide community trust with four directly-held community hospitals (Cromer, Kelling, Benjamin Court, Swaffham) and dispersed leasehold clinic estate. Norfolk's rural geography (Broads, north Norfolk coast, rural west) drives travel/winter-resilience cost. Coastal community hospitals (Cromer) carry external-fabric salt-corrosion premium.",
        "sources": [
            "https://www.norfolkcommunityhealthandcare.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.property.nhs.uk/"
        ],
        "related": ["Norfolk Community Health and Care NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Tavistock and Portman NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Tavistock and Portman NHS Foundation Trust"}],
        "description": "Premises running costs at the Tavistock Centre (Belsize Lane, Hampstead) and Gloucester House (Hampstead) — England's specialist MH outpatient + training trust historically running the Gender Identity Development Service (GIDS, closed Mar 2024). Outpatient + research + training estate, no inpatient beds.",
        "beneficiaries": "Specialist MH outpatient services (psychotherapy, family + couples, complex needs adults), training (DClinPsy, MA family therapy) — c.25,000 patient contacts/year + c.1,000 trainees.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£2.65M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "Tavistock Centre + Gloucester House — Hampstead (small-site trust)"},
            {"label": "Service profile", "value": "Outpatient + training only — no inpatient beds; in-house Estates"},
            {"label": "GIDS closure", "value": "Service closed Mar 2024 — estate footprint absorbed"},
            {"label": "Hampstead location", "value": "Conservation-area constraints + London-property cost"},
            {"label": "Training role", "value": "Doctorate + masters training — teaching/seminar fit-out"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works scoped"},
            {"label": "YoY change", "value": "c. +4% (energy + post-GIDS-closure restructure)"},
            {"label": "Peer benchmark", "value": "Smallest premises spend in MH-trust set (no inpatient)"}
        ],
        "notes": "Tavistock and Portman's premises spend is the smallest among MH FTs because the trust runs no inpatient beds — its estate is outpatient consulting rooms, group-therapy spaces and training/seminar rooms. The GIDS closure (Mar 2024 — services transferred to two new regional providers) freed some specialist clinic capacity but the core estate at Belsize Lane and Gloucester House remains. Hampstead conservation constraints limit retrofit.",
        "sources": [
            "https://tavistockandportman.nhs.uk/about-us/governance/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Tavistock and Portman NHS Foundation Trust", "Premises & Infrastructure"]
    },
}
