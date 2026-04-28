# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 34 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Lease expenditure — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "Cambridge UHFT's £1.521M lease expenditure line covers IFRS 16 right-of-use depreciation and interest on operating-style leases held outside the PFI/LIFT envelope — chiefly imaging modality leases (MRI, CT, PET-CT), pathology analyser leases, vehicle pool leases, and short-term clinical-space leases at the Addenbrooke's and Rosie Hospital sites plus outreach community clinics. Trust is part of the Cambridge Biomedical Campus and a designated Major Trauma Centre for the East of England.",
        "beneficiaries": "c. 12,500 WTE staff serving a c. 580,000 Cambridgeshire core catchment plus tertiary referrals across the East of England (c. 6.5M); c. 145,000 ED attendances/yr at Addenbrooke's ED; c. 130,000 elective + non-elective admissions/yr; sole MTC + specialist neurosciences, transplant and oncology centre for the East of England.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — IAS 36 (impairment of right-of-use assets)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.521M"},
            {"label": "Trust scale", "value": "Addenbrooke's Hospital + Rosie Hospital (maternity) + community outposts on Cambridge Biomedical Campus; c. 12,500 WTE"},
            {"label": "Composition", "value": "Imaging modality leases (MRI/CT/PET-CT) + pathology analysers + vehicle pool + short-term clinical-space leases — IFRS 16 ROU depreciation + interest"},
            {"label": "IFRS 16 transition", "value": "DHSC GAM applied IFRS 16 from 1 April 2022 (delayed from IASB Jan 2019) — drove material reclassification of operating leases onto BS as ROU assets"},
            {"label": "Specialty mix driver", "value": "MTC + transplant + oncology + neurosciences specialty mix drives high-value imaging and pathology equipment-lease tail"},
            {"label": "Cambridge Biomedical Campus", "value": "Co-located with Royal Papworth, MRC LMB, AstraZeneca DISC, University of Cambridge — shared-equipment leasing arrangements"},
            {"label": "Funding trajectory", "value": "Pre-IFRS 16 op-lease £nil onshore → 2022-23 c. £1.3M → 2023-24 c. £1.45M → 2024-25 £1.521M — IFRS 16 capitalisation cycle"},
            {"label": "East of England ICS", "value": "Member of Cambridgeshire and Peterborough ICB; tertiary referrals across 6 East of England ICBs"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + Pharmacy + Pathology + IT + Finance + lessors (Siemens Healthineers + GE HealthCare + Philips + Roche + Beckman + lease finance houses)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cambridgeshire and Peterborough ICB + NHSE Specialised Commissioning"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 IFRS 16 disclosure; CQC RGT inspections; NAO Specialised Commissioning reports; Carter Lord review on procurement"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 operating-lease off-balance-sheet treatment · Successor: continued IFRS 16 ROU capitalisation + Cambridge Children's Hospital build (2027 ISD planned)"}
        ],
        "notes": "Cambridge UHFT's lease expenditure reflects the trust's specialty mix as a Major Trauma Centre and tertiary referrals hub on the Cambridge Biomedical Campus — high-value imaging modality leases (MRI, CT, PET-CT), pathology analysers, and vehicle pool drive the tail. The DHSC GAM applied IFRS 16 from 1 April 2022 (a 3-year delay vs the IASB January 2019 adoption date), which materially reclassified operating leases onto the balance sheet as right-of-use assets. The 2023-24 industrial-action backfill cycle drove additional short-term clinical-space leases, while the planned Cambridge Children's Hospital (2027 ISD) build feeds forward into the medium-term lease pipeline. Co-location with Royal Papworth, MRC LMB, AstraZeneca DISC and the University of Cambridge enables some shared-equipment leasing arrangements that compress unit costs.",
        "sources": [
            {"publisher": "Cambridge University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cuh.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "Care Quality Commission", "title": "Cambridge University Hospitals NHS Foundation Trust provider profile (RGT)", "url": "https://www.cqc.org.uk/provider/RGT"},
            {"publisher": "Cambridge Biomedical Campus", "title": "About Cambridge Biomedical Campus", "url": "https://cambridge-biomedical.com/"}
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Mid Cheshire Hospitals NHS Foundation Trust", "General supplies & services — Cambridge University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Stockport NHS FT's £1.494M business-rates line covers non-domestic rate liability on Stepping Hill Hospital (Stockport) — the trust's principal acute site — plus community-clinic outposts across the Stockport metropolitan footprint. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023), with rates calculated against the standard non-domestic multiplier set under the Local Government Finance Act 1988 (Sch 6) as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Greater Manchester ICS context.",
        "beneficiaries": "c. 5,200 WTE staff serving a c. 320,000 Stockport + south-east Greater Manchester catchment; c. 95,000 ED attendances/yr at Stepping Hill ED; c. 70,000 admissions/yr; trust runs Stepping Hill Hospital plus community services across Stockport metropolitan borough within the Greater Manchester ICS.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.494M"},
            {"label": "Trust scale", "value": "Stepping Hill Hospital + Stockport community outposts; c. 5,200 WTE"},
            {"label": "Principal hereditament", "value": "Stepping Hill Hospital (Poplar Grove, Stockport) — main acute site, ED, maternity, children's services"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne (cf. independent-sector charity hospitals)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.3M → 2023-24 c. £1.43M → 2024-25 £1.494M — 2023 list revaluation + multiplier uplift"},
            {"label": "Greater Manchester ICS", "value": "Member of Greater Manchester ICB; collaborative procurement and estate frameworks across GM"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA (rateable-value setter) + Stockport Metropolitan Borough Council (unitary billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24; CQC RWJ inspections (Stepping Hill governance history)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + Greater Manchester estate-rationalisation"}
        ],
        "notes": "Stockport NHS FT's business-rates line is a function of VOA 2023 rating-list valuations on Stepping Hill Hospital (Poplar Grove) — the trust's principal hereditament — with smaller liabilities on Stockport-borough community-clinic outposts. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals, so the full liability is borne. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduced the higher multiplier on £500k+ properties from April 2025 — material for Stepping Hill main hereditament. Stepping Hill has a long governance history (Beverley Allitt-style nurse-poisoning investigation 2011-15) shaping its broader cost-base scrutiny, and the Greater Manchester ICS framework drives collaborative estate-rationalisation as the medium-term lever.",
        "sources": [
            {"publisher": "Stockport NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stockport.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "Stockport NHS Foundation Trust provider profile (RWJ)", "url": "https://www.cqc.org.uk/provider/RWJ"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Mid Cheshire Hospitals NHS Foundation Trust", "Business rates — Wye Valley NHS Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Stockport NHS FT's £1.492M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP rates), patient transport services (PTS) eligible non-emergency journeys, courier services moving pathology specimens and notes between Stepping Hill and community sites, and the trust's IFRS 16-capitalised pool fleet. PTS is commissioned by Greater Manchester ICB from a regional provider (Arriva Transport Solutions / North West Ambulance Service hybrid model historically). Greater Manchester ICS context.",
        "beneficiaries": "c. 5,200 WTE staff claiming business mileage; c. 30,000 PTS-eligible patient journeys/yr (non-emergency renal, oncology, frailty); c. 95,000 ED attendances/yr at Stepping Hill ED; c. 70,000 admissions/yr; courier flow between Stepping Hill main lab and Stockport community outposts.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria (2021) — Agenda for Change Section 17 (business travel) — HMRC AMAP rates (45p/25p) — IFRS 16 Leases (pool fleet) — DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.492M"},
            {"label": "Trust scale", "value": "Stepping Hill Hospital + Stockport community outposts; c. 5,200 WTE"},
            {"label": "Composition", "value": "Staff business mileage (AfC S17 + AMAP) + PTS eligible journeys + courier (pathology/notes) + IFRS 16 pool-fleet ROU"},
            {"label": "PTS commissioner", "value": "Greater Manchester ICB (regional non-emergency PTS contract)"},
            {"label": "AMAP rate freeze", "value": "HMRC 45p/25p frozen since 2011 — 14-year cumulative real-terms erosion of business-mileage reimbursement"},
            {"label": "PTS eligibility", "value": "NHSE 2021 eligibility framework — medical-need + financial-hardship gateways; renal/oncology/frailty"},
            {"label": "IFRS 16 pool fleet", "value": "Pool vehicles (estates, courier vans, community nursing) reclassified as ROU assets from 1 April 2022"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove additional taxi/PTS for elective rebooking"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.25M → 2023-24 c. £1.42M → 2024-25 £1.492M — IFRS 16 ROU + strike rebooking taxi/PTS spike"},
            {"label": "Delivery body", "value": "Trust E&F + Operations + Pathology + courier contractor + GM ICB-commissioned PTS provider + NWAS for emergency transfers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greater Manchester ICB + HMRC (AMAP) + NHSE PTS team"},
            {"label": "Evaluation evidence", "value": "NAO PTS reports; NHSE PTS eligibility review; Trust ARA 2023-24; CQC RWJ inspections; Healthwatch Stockport patient-experience"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 PTS eligibility framework + pre-IFRS 16 op-lease · Successor: GM ICB PTS recommissioning + AMAP rate review (long-rumoured)"}
        ],
        "notes": "Stockport NHS FT's transport line aggregates business mileage paid to c. 5,200 WTE under AfC Section 17 and HMRC AMAP rates (frozen at 45p/25p since 2011 — a 14-year real-terms erosion that has shifted the burden of operational travel onto staff), PTS eligible non-emergency journeys commissioned by Greater Manchester ICB, courier services between Stepping Hill and Stockport community outposts, and the IFRS 16 pool-fleet ROU. The 2023-24 industrial-action cycle drove additional rebooking taxi/PTS spend, and the IFRS 16 transition from 1 April 2022 reclassified previously off-balance-sheet pool-fleet leases onto the balance sheet. NHSE's 2021 PTS eligibility tightening (medical-need + financial-hardship gateways) compressed the patient-journey volume but with continued cost growth driven by fuel, AMAP-rate-freeze pressure on staff mileage, and an ageing local population.",
        "sources": [
            {"publisher": "Stockport NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stockport.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-emergency patient transport services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "HMRC", "title": "Approved mileage allowance payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Care Quality Commission", "title": "Stockport NHS Foundation Trust provider profile (RWJ)", "url": "https://www.cqc.org.uk/provider/RWJ"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Barnsley Hospital NHS Foundation Trust", "Business rates — Stockport NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — The Royal Wolverhampton NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Royal Wolverhampton NHS Trust"}],
        "description": "RWT's £1.482M amortisation line is the IAS 38-compliant systematic write-down of the trust's intangible assets — chiefly capitalised electronic patient record (EPR) software, picture-archiving and communication system (PACS) licences, internally-developed clinical software, and Frontline Digitisation programme-funded EPR rollout costs. RWT operates New Cross Hospital (Wolverhampton), Cannock Chase Hospital and West Park Hospital plus an integrated GP-practice arm (Vertical Integration model). Black Country ICS context.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 700,000 Wolverhampton + Cannock Chase + Black Country catchment; c. 145,000 ED attendances/yr at New Cross ED; c. 100,000 admissions/yr; trust additionally manages c. 16 GP practices via vertical-integration model; one of the largest acute-plus-primary integrated providers in England.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — IFRS 15 Revenue from Contracts with Customers (where capitalised) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.482M"},
            {"label": "Trust scale", "value": "New Cross Hospital + Cannock Chase Hospital + West Park Hospital + c. 16 GP practices; c. 9,000 WTE"},
            {"label": "Composition", "value": "Capitalised EPR software (Sunrise — Allscripts/Altera) + PACS licences + internally-developed clinical software + Frontline Digitisation EPR rollout costs"},
            {"label": "EPR vendor", "value": "Allscripts/Altera Sunrise — historical EPR investment (one of earliest large-scale EPR adopters in England, c. 2008-2014)"},
            {"label": "Useful life", "value": "Typically 3-7 years for software per IAS 38 — drives 2024-25 in-flight amortisation tail"},
            {"label": "Frontline Digitisation", "value": "RWT NHP-cohort + EPR-mature trust — capital programme funds rollout to Cannock Chase + community"},
            {"label": "Vertical integration", "value": "RWT runs c. 16 GP practices — primary-care clinical-system capitalisation interacts with amortisation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.2M → 2023-24 c. £1.4M → 2024-25 £1.482M — Frontline Digitisation rollout cycle + capitalised software replacement cycle"},
            {"label": "Black Country ICS", "value": "Member of Black Country ICB; collaborative digital and procurement frameworks with Walsall, Sandwell + W Birmingham, Dudley"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Allscripts/Altera + NHSE Frontline Digitisation programme + Black Country ICB"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation + DHSC + NHSE Provider Finance + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation reports; CQC RL4 inspections; Trust ARA 2023-24 IAS 38 disclosure; What Good Looks Like (NHSE digital framework) self-assessment"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy paper-based clinical records · Successor: continued Frontline Digitisation rollout to Cannock Chase + community + GP-practice arm"}
        ],
        "notes": "RWT's amortisation line is shaped by the trust's status as one of the earliest large-scale EPR adopters in England (Allscripts/Altera Sunrise from c. 2008-2014) — generating a long-tail of capitalised intangible assets now in their final 2-3 years of useful life under IAS 38. The Frontline Digitisation programme is funding rollout to Cannock Chase and community sites, feeding the medium-term amortisation pipeline. RWT's vertical-integration model running c. 16 GP practices adds primary-care clinical-system capitalisation interaction. The trust sits within the Black Country ICS with collaborative digital and procurement frameworks alongside Walsall Healthcare, Sandwell + W Birmingham, and Dudley Group. RWT's NHP-cohort status was deferred under the Reset (January 2025) — material for medium-term capital and intangible-asset planning.",
        "sources": [
            {"publisher": "The Royal Wolverhampton NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalwolverhampton.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "The Royal Wolverhampton NHS Trust provider profile (RL4)", "url": "https://www.cqc.org.uk/provider/RL4"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"}
        ],
        "related": ["The Royal Wolverhampton NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation programme", "Black Country ICB", "Department of Health and Social Care"]
    },
    "Business rates — Mid Cheshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Mid Cheshire Hospitals NHS Foundation Trust"}],
        "description": "Mid Cheshire's £1.482M business-rates line covers non-domestic rate liability on Leighton Hospital (Crewe) — the trust's principal acute site — plus Victoria Infirmary (Northwich) and Elmhurst Intermediate Care Centre (Winsford). Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024. Leighton Hospital is on the RAAC HSSIB September 2023 list (concrete-plank failure risk) — a critical capital and revenue pressure point. Cheshire and Merseyside ICS context.",
        "beneficiaries": "c. 4,800 WTE staff serving a c. 320,000 mid-Cheshire catchment (Crewe, Nantwich, Northwich, Winsford, Sandbach, Middlewich); c. 90,000 ED attendances/yr at Leighton ED; c. 65,000 admissions/yr; sole acute provider for mid-Cheshire — long ambulance times due to RAAC-driven decant arrangements.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.482M"},
            {"label": "Trust scale", "value": "Leighton Hospital (Crewe) + Victoria Infirmary (Northwich) + Elmhurst (Winsford); c. 4,800 WTE"},
            {"label": "RAAC HSSIB list", "value": "Leighton Hospital on September 2023 RAAC list — concrete-plank failure risk; NHP New Hospital Programme cohort (originally 2030) — Reset Jan 2025 confirmed Leighton commitment"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "RAAC decant interaction", "value": "Decant of RAAC-affected ward space into modular units may trigger separate rateable assessments + rates revaluation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.3M → 2023-24 c. £1.42M → 2024-25 £1.482M — 2023 list revaluation + multiplier uplift + RAAC modular decant"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of NHS Cheshire and Merseyside ICB; collaborative estate frameworks across C&M"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA (rateable-value setter) + Cheshire East Council / Cheshire West and Chester Council (unitary billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + DHSC New Hospital Programme + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO RAAC reports; HSSIB September 2023 RAAC list; Trust ARA 2023-24; CQC RBT inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + Leighton NHP new-build (post-2030) — rateable assessment will reset"}
        ],
        "notes": "Mid Cheshire's business-rates line reflects the trust's three-site footprint (Leighton Hospital Crewe + Victoria Infirmary Northwich + Elmhurst Winsford) with Leighton as the principal hereditament. The September 2023 HSSIB RAAC list confirmed Leighton has concrete-plank failure risk, and the NHP Reset (January 2025) confirmed the Leighton replacement commitment — though the build is post-2030 in the deferred cohort. Decant of RAAC-affected ward space into modular units may trigger separate rateable assessments. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ properties is material for Leighton main hereditament. The 1 April 2026 next revaluation is the medium-term lever for the trust to challenge valuations alongside the eventual NHP rebuild.",
        "sources": [
            {"publisher": "Mid Cheshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mcht.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme: Plan for Implementation (Jan 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Care Quality Commission", "title": "Mid Cheshire Hospitals NHS Foundation Trust provider profile (RBT)", "url": "https://www.cqc.org.uk/provider/RBT"}
        ],
        "related": ["Mid Cheshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Mid Cheshire Hospitals NHS Foundation Trust", "Business rates — Stockport NHS Foundation Trust", "New Hospital Programme"]
    },
    "General supplies & services — Harrogate and District NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Harrogate and District NHS Foundation Trust"}],
        "description": "HDFT's £1.476M general supplies & services line covers GAM-classified clinical and operational consumables outside the drugs/clinical-supplies envelope — chiefly stationery, office supplies, hotel-services laundry, food, cleaning materials, minor medical sundries, IT consumables and specialist hospital-services-tier supplies across Harrogate District Hospital and the trust's wide community-services footprint covering c. 250 community sites across North Yorkshire, Leeds, Bradford, Wakefield, Sunderland and Darlington. West Yorkshire ICS context.",
        "beneficiaries": "c. 4,800 WTE staff serving a c. 160,000 Harrogate + Knaresborough acute catchment plus a children's community-services contract covering c. 1.4M across 6 ICBs; c. 50,000 ED attendances/yr at Harrogate ED; c. 35,000 admissions/yr; one of the smallest standalone DGH FTs in England with a disproportionately large community-services footprint.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 (procurement)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£1.476M"},
            {"label": "Trust scale", "value": "Harrogate District Hospital + c. 250 community sites across N Yorks, Leeds, Bradford, Wakefield, Sunderland, Darlington; c. 4,800 WTE"},
            {"label": "Composition", "value": "Stationery + office supplies + hotel-services (laundry, food, cleaning) + medical sundries + IT consumables + specialist hospital supplies"},
            {"label": "Community-services scale", "value": "Children's 0-19 services + healthy-child programme — c. 1.4M children covered across 6 ICB contracts (one of the largest community-children's providers in England)"},
            {"label": "NHS Supply Chain reliance", "value": "Standard NHS Supply Chain framework usage for medical sundries and clinical consumables; off-framework for community-specific supplies"},
            {"label": "Industrial action 2023-24", "value": "Lower direct impact than larger acute trusts (smaller cancellation rebooking) but additional admin-supply and recruitment-advertising consumption"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.3M → 2023-24 c. £1.42M → 2024-25 £1.476M — CPI on consumables + community-services contract uplifts"},
            {"label": "West Yorkshire ICS", "value": "Member of West Yorkshire ICB (acute) but community-services contracts cross 6 ICBs"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier and laundry/food contractor pass-through pricing"},
            {"label": "Delivery body", "value": "Trust Procurement + Hotel Services + IT + Community Services Operations + NHS Supply Chain + private suppliers (Lyreco etc.)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Supply Chain + West Yorkshire ICB + commissioning ICBs (cross-border community contracts)"},
            {"label": "Evaluation evidence", "value": "Carter Lord review on procurement; NHS Supply Chain category reviews; Trust ARA 2023-24; CQC RCD inspections; Public Health England 0-19 evaluation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Carter procurement profile · Successor: continued Supply Chain framework consolidation + community-children's service recommissioning by ICBs"}
        ],
        "notes": "HDFT is unusual in being a small standalone DGH FT (Harrogate + Knaresborough acute catchment c. 160,000) with a disproportionately large children's community-services arm covering c. 1.4M across 6 ICBs (Leeds, Bradford, Wakefield, Sunderland, Darlington plus North Yorkshire) — its general supplies & services line therefore reflects both a hospital and a sprawling community-equipment footprint. The trust's 2023-24 industrial action impact was muted relative to larger teaching trusts, but CPI on consumables (food, laundry, stationery) and community-services contract uplifts drove the line. April 2025 employer NIC step-up (15% over £5k threshold) feeds indirectly via supplier and contractor pass-through. The trust uses NHS Supply Chain frameworks but has substantial off-framework community-specific supply spend.",
        "sources": [
            {"publisher": "Harrogate and District NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hdft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain — category towers", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Harrogate and District NHS Foundation Trust provider profile (RCD)", "url": "https://www.cqc.org.uk/provider/RCD"},
            {"publisher": "NHS England", "title": "Carter Review: Operational productivity and performance in English NHS acute hospitals", "url": "https://www.gov.uk/government/publications/productivity-in-nhs-hospitals"}
        ],
        "related": ["Harrogate and District NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Cambridge University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Barnsley Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Barnsley Hospital NHS Foundation Trust"}],
        "description": "Barnsley Hospital FT's £1.464M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP rates), patient transport services (PTS) eligible non-emergency journeys, courier services moving pathology specimens and notes, and the trust's IFRS 16-capitalised pool fleet. PTS in South Yorkshire is commissioned by South Yorkshire ICB from Yorkshire Ambulance Service / Arriva Transport Solutions. South Yorkshire ICS context — Barnsley is a single-DGH trust serving a high-deprivation former-coalfield population.",
        "beneficiaries": "c. 3,800 WTE staff claiming business mileage; c. 25,000 PTS-eligible patient journeys/yr (renal, oncology, frailty); c. 80,000 ED attendances/yr at Barnsley Hospital ED; c. 55,000 admissions/yr; c. 245,000 Barnsley borough catchment plus tertiary and tail-end Yorkshire flow; high-deprivation former-coalfield population shapes PTS demand.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria (2021) — Agenda for Change Section 17 — HMRC AMAP rates (45p/25p) — IFRS 16 Leases (pool fleet) — DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.464M"},
            {"label": "Trust scale", "value": "Single-site DGH (Barnsley Hospital) + community outreach; c. 3,800 WTE"},
            {"label": "Composition", "value": "Staff business mileage (AfC S17 + AMAP) + PTS journeys + courier (pathology/notes) + IFRS 16 pool-fleet ROU"},
            {"label": "PTS commissioner", "value": "South Yorkshire ICB (regional non-emergency PTS contract); delivered by Yorkshire Ambulance Service / Arriva Transport Solutions"},
            {"label": "AMAP rate freeze", "value": "HMRC 45p/25p frozen since 2011 — 14-year cumulative real-terms erosion of business-mileage reimbursement"},
            {"label": "Deprivation driver", "value": "Barnsley borough decile-2 IMD ranking — high PTS demand from low-car-ownership patients in oncology + renal pathways"},
            {"label": "IFRS 16 pool fleet", "value": "Pool vehicles (estates, courier vans) reclassified as ROU assets from 1 April 2022"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rebooking taxi/PTS uplift"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.25M → 2023-24 c. £1.4M → 2024-25 £1.464M — IFRS 16 ROU + strike rebooking + fuel CPI"},
            {"label": "Delivery body", "value": "Trust E&F + Operations + Pathology + courier contractor + SY ICB-commissioned PTS provider (YAS / Arriva) + YAS for emergency transfers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South Yorkshire ICB + HMRC (AMAP) + NHSE PTS team"},
            {"label": "Evaluation evidence", "value": "NAO PTS reports; NHSE PTS eligibility review; Trust ARA 2023-24; CQC RFF inspections; Healthwatch Barnsley patient-experience"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 PTS framework + pre-IFRS 16 op-lease · Successor: SY ICB PTS recommissioning + Working Together Partnership integration"}
        ],
        "notes": "Barnsley Hospital FT's transport line is shaped by high local deprivation (Barnsley borough decile-2 IMD ranking) which inflates PTS demand from low-car-ownership patients on renal, oncology and frailty pathways. The HMRC AMAP rate freeze at 45p/25p (since 2011) has eroded real-terms reimbursement for the c. 3,800 WTE claiming business mileage. The IFRS 16 transition from 1 April 2022 reclassified pool-fleet operating leases onto the balance sheet as ROU assets. The 2023-24 industrial-action cycle drove rebooking taxi/PTS uplift, and Barnsley participates in the Working Together Partnership with Sheffield Teaching, Doncaster & Bassetlaw and Rotherham — material for medium-term shared logistics. South Yorkshire ICB recommissioning of PTS is the medium-term lever.",
        "sources": [
            {"publisher": "Barnsley Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.barnsleyhospital.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-emergency patient transport services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "HMRC", "title": "Approved mileage allowance payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Care Quality Commission", "title": "Barnsley Hospital NHS Foundation Trust provider profile (RFF)", "url": "https://www.cqc.org.uk/provider/RFF"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Barnsley Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Stockport NHS Foundation Trust", "Establishment costs — Barnsley Hospital NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Sandwell And West Birmingham Hospitals NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Sandwell And West Birmingham Hospitals NHS Trust"}],
        "description": "SWBH's £1.459M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), PTS eligible non-emergency journeys, courier services moving pathology specimens between Sandwell General Hospital, City Hospital, Rowley Regis Hospital, and the new Midland Metropolitan University Hospital (MMUH, opened 6 October 2024), plus IFRS 16 pool fleet. PTS in the Black Country is commissioned by Black Country ICB. The MMUH PFI legacy and 2024 opening generate a transitional transport profile.",
        "beneficiaries": "c. 7,500 WTE staff claiming business mileage; c. 35,000 PTS-eligible patient journeys/yr (renal, oncology, frailty); c. 165,000 ED attendances/yr at MMUH-consolidated ED; c. 110,000 admissions/yr; c. 530,000 Sandwell + West Birmingham catchment; very high deprivation (decile-1/2 IMD).",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria (2021) — Agenda for Change Section 17 — HMRC AMAP rates (45p/25p) — IFRS 16 Leases (pool fleet) — DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.459M"},
            {"label": "Trust scale", "value": "Sandwell General + City Hospital (Birmingham) + Rowley Regis + MMUH (opened 6 Oct 2024) + community sites; c. 7,500 WTE"},
            {"label": "MMUH transition", "value": "Midland Metropolitan University Hospital (Smethwick) opened 6 Oct 2024 — Carillion 2018 collapse + Balfour Beatty completion — drives transitional transport flows between consolidated and legacy sites"},
            {"label": "Composition", "value": "Staff business mileage (AfC S17 + AMAP) + PTS journeys + courier (pathology/notes) + IFRS 16 pool-fleet ROU"},
            {"label": "PTS commissioner", "value": "Black Country ICB (regional NEPTS contract); West Midlands Ambulance Service for emergency transfers"},
            {"label": "Deprivation driver", "value": "Sandwell + W Birmingham decile-1/2 IMD ranking — very high PTS demand from low-car-ownership patients"},
            {"label": "AMAP rate freeze", "value": "HMRC 45p/25p frozen since 2011 — 14-year cumulative real-terms erosion"},
            {"label": "IFRS 16 pool fleet", "value": "Pool vehicles reclassified as ROU assets from 1 April 2022"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.2M → 2023-24 c. £1.38M → 2024-25 £1.459M — MMUH transition courier surge + IFRS 16 ROU + strike rebooking"},
            {"label": "Delivery body", "value": "Trust E&F + Operations + Pathology + courier contractor + Black Country ICB-commissioned NEPTS provider + WMAS"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Black Country ICB + HMRC (AMAP) + NHSE PTS team"},
            {"label": "Evaluation evidence", "value": "NAO MMUH report (2020 Carillion collapse fallout); CQC RXK inspections; Trust ARA 2023-24; NHSE PTS eligibility review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-MMUH 4-site model + pre-2021 PTS framework · Successor: post-MMUH consolidation (City and Sandwell A&E closure) + Black Country ICB PTS recommissioning"}
        ],
        "notes": "SWBH's transport line is shaped by the October 2024 opening of the Midland Metropolitan University Hospital (MMUH) — long-delayed by the 2018 Carillion collapse and completed by Balfour Beatty — which consolidates ED and acute services from Sandwell General and City Hospital onto a single Smethwick site. The transitional period drives elevated courier flows and patient-transport demand between consolidated MMUH and the legacy outpatient/community arms at Sandwell and Rowley Regis. Very high local deprivation (Sandwell + W Birmingham decile-1/2 IMD) inflates PTS demand from low-car-ownership patients. The 2023-24 industrial-action backfill plus IFRS 16 pool-fleet ROU recognition from 1 April 2022 also feed the line. Black Country ICB recommissioning of NEPTS is the medium-term lever.",
        "sources": [
            {"publisher": "Sandwell and West Birmingham Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swbh.nhs.uk/about-us/publications/"},
            {"publisher": "National Audit Office", "title": "Investigation into the Midland Metropolitan University Hospital", "url": "https://www.nao.org.uk/reports/investigation-into-the-midland-metropolitan-hospital-project/"},
            {"publisher": "NHS England", "title": "Non-emergency patient transport services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Care Quality Commission", "title": "Sandwell and West Birmingham Hospitals NHS Trust provider profile (RXK)", "url": "https://www.cqc.org.uk/provider/RXK"},
            {"publisher": "HMRC", "title": "Approved mileage allowance payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"}
        ],
        "related": ["Sandwell And West Birmingham Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Midland Metropolitan University Hospital", "Transport (business + patient) — Barnsley Hospital NHS Foundation Trust", "Black Country ICB"]
    },
    "Transport (business + patient) — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "UHD's £1.453M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), PTS eligible non-emergency journeys, courier services moving pathology specimens between Royal Bournemouth Hospital, Poole Hospital, and Christchurch Hospital, and IFRS 16-capitalised pool fleet. UHD was created on 1 October 2020 by the merger of Royal Bournemouth and Christchurch + Poole Hospital trusts. The Dorset reconfiguration programme is consolidating emergency services to RBH and planned care to Poole. Dorset ICS context.",
        "beneficiaries": "c. 9,500 WTE staff claiming business mileage; c. 35,000 PTS-eligible patient journeys/yr; c. 165,000 ED attendances/yr across RBH and Poole EDs; c. 110,000 admissions/yr; c. 800,000 Bournemouth + Christchurch + Poole + East Dorset catchment plus seasonal-visitor surge.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria (2021) — Agenda for Change Section 17 — HMRC AMAP rates (45p/25p) — IFRS 16 Leases (pool fleet) — DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.453M"},
            {"label": "Trust scale", "value": "Royal Bournemouth Hospital + Poole Hospital + Christchurch Hospital + community sites; c. 9,500 WTE"},
            {"label": "Merger", "value": "Created 1 Oct 2020 by merger of Royal Bournemouth and Christchurch FT + Poole Hospital FT"},
            {"label": "Reconfiguration", "value": "Dorset reconfiguration: emergency + maternity to RBH (BEACH building) + planned care to Poole — drives inter-site patient transport"},
            {"label": "Composition", "value": "Staff business mileage (AfC S17 + AMAP) + PTS journeys + courier (pathology/notes) + IFRS 16 pool-fleet ROU"},
            {"label": "PTS commissioner", "value": "NHS Dorset ICB (regional NEPTS contract); SWASFT for emergency transfers"},
            {"label": "AMAP rate freeze", "value": "HMRC 45p/25p frozen since 2011 — 14-year cumulative real-terms erosion"},
            {"label": "IFRS 16 pool fleet", "value": "Pool vehicles reclassified as ROU assets from 1 April 2022"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.2M → 2023-24 c. £1.4M → 2024-25 £1.453M — reconfiguration inter-site transport + IFRS 16 ROU + strike rebooking"},
            {"label": "Delivery body", "value": "Trust E&F + Operations + Pathology + courier contractor + Dorset ICB-commissioned NEPTS provider + SWASFT"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Dorset ICB + HMRC (AMAP) + NHSE PTS team"},
            {"label": "Evaluation evidence", "value": "NAO Dorset reconfiguration follow-up; CQC R0D inspections; Trust ARA 2023-24; NHSE PTS eligibility review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger separate transport budgets at RBCH + PHFT · Successor: post-BEACH-building reconfiguration completion + Dorset ICB PTS recommissioning"}
        ],
        "notes": "UHD's transport line is shaped by the trust's status as a 2020-merger entity in active reconfiguration — the BEACH building at Royal Bournemouth (opened 2024) consolidates emergency and maternity services on RBH, with planned care moving to Poole — driving substantial inter-site patient and staff transport during the transition. The seasonal-visitor surge across Bournemouth + Poole inflates summer ED demand and PTS need. The HMRC AMAP rate freeze at 45p/25p (since 2011) erodes real-terms reimbursement for c. 9,500 WTE. The IFRS 16 transition from 1 April 2022 reclassified pool-fleet leases onto the balance sheet. NHS Dorset ICB recommissioning of NEPTS is the medium-term lever, with reconfiguration completion at RBH/Poole the operational milestone.",
        "sources": [
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhd.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-emergency patient transport services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "HMRC", "title": "Approved mileage allowance payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Dorset NHS Foundation Trust provider profile (R0D)", "url": "https://www.cqc.org.uk/provider/R0D"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Sandwell And West Birmingham Hospitals NHS Trust", "Business rates — Dorset County Hospital NHS Foundation Trust", "NHS Dorset ICB"]
    },
    "Business rates — Dorset County Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Dorset County Hospital NHS Foundation Trust"}],
        "description": "DCHFT's £1.409M business-rates line covers non-domestic rate liability on Dorset County Hospital (Dorchester) — the trust's single principal acute site — plus Damers Hospital and a network of community-clinic outposts across West Dorset. Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024. DCH is a designated Trauma Unit feeding University Hospitals Plymouth MTC. NHS Dorset ICS context.",
        "beneficiaries": "c. 3,200 WTE staff serving a c. 215,000 West Dorset catchment (Dorchester, Weymouth, Bridport, Sherborne, Portland) plus seasonal-visitor surge to c. 350,000 in summer; c. 60,000 ED attendances/yr at DCH ED; c. 40,000 admissions/yr; sole acute provider for West Dorset.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.409M"},
            {"label": "Trust scale", "value": "Dorset County Hospital (Dorchester) + Damers Hospital + community outposts across West Dorset; c. 3,200 WTE"},
            {"label": "Principal hereditament", "value": "Dorset County Hospital (Williams Avenue, Dorchester) — main acute, ED, maternity, Trauma Unit"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.25M → 2023-24 c. £1.36M → 2024-25 £1.409M — 2023 list revaluation + multiplier uplift"},
            {"label": "NHS Dorset ICS", "value": "Member of NHS Dorset ICB alongside University Hospitals Dorset and Dorset HealthCare"},
            {"label": "Seasonal demand", "value": "West Dorset coastal catchment population swells from 215k to c. 350k in summer — ED demand without rates relief"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA (rateable-value setter) + Dorset Council (unitary billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + NHS Dorset ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24; CQC RBD inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + future Dorset reconfiguration estate review"}
        ],
        "notes": "DCHFT's business-rates line reflects the trust's single-DGH footprint at Dorset County Hospital (Williams Avenue, Dorchester) plus Damers and community outposts. Dorset Council is the unitary billing authority covering the whole West Dorset footprint. NHS trusts are not eligible for the mandatory 80% charitable rate relief, so the full liability is borne. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ properties is material for the DCH main hereditament. The summer-visitor surge across the West Dorset coastal catchment inflates ED demand without corresponding rates relief. The 1 April 2026 revaluation is the medium-term lever, alongside any future Dorset-wide reconfiguration estate review with University Hospitals Dorset.",
        "sources": [
            {"publisher": "Dorset County Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchft.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "Dorset County Hospital NHS Foundation Trust provider profile (RBD)", "url": "https://www.cqc.org.uk/provider/RBD"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Dorset County Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Wye Valley NHS Trust", "Business rates — Stockport NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Wye Valley NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Wye Valley NHS Trust"}],
        "description": "Wye Valley NHS Trust's £1.407M business-rates line covers non-domestic rate liability on Hereford County Hospital — the trust's principal acute site, a 2002-vintage PFI hospital — plus Bromyard Community Hospital, Leominster Community Hospital, Ross Community Hospital and a network of community-clinic outposts across Herefordshire. Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024. Herefordshire and Worcestershire ICS context.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 195,000 Herefordshire catchment plus eastern Powys cross-border flow; c. 60,000 ED attendances/yr at Hereford County ED; c. 40,000 admissions/yr; sole acute provider for Herefordshire — long ambulance times reflect rural-county geography (one of the most rural counties in England).",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.406656M"},
            {"label": "Trust scale", "value": "Hereford County Hospital + Bromyard + Leominster + Ross community hospitals + community outposts; c. 3,500 WTE"},
            {"label": "PFI status", "value": "Hereford County Hospital — 2002-vintage Mercia Healthcare PFI (concession period to c. 2032); novated FM after Carillion 2018 collapse to Sodexo"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.25M → 2023-24 c. £1.36M → 2024-25 £1.407M — 2023 list revaluation + multiplier uplift"},
            {"label": "Herefordshire and Worcestershire ICS", "value": "Member of Herefordshire and Worcestershire ICB alongside Worcestershire Acute Hospitals"},
            {"label": "Cross-border flow", "value": "Eastern Powys (Wales) cross-border patient flow to Hereford County under cross-border NHS arrangements"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + Mercia Healthcare PFI co + Sodexo (FM) + Herefordshire Council (unitary billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + NHS Herefordshire and Worcestershire ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO PFI reports; Trust ARA 2023-24; CQC RLQ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + 2032 PFI concession-end estate transfer to trust ownership"}
        ],
        "notes": "Wye Valley NHS Trust's business-rates line reflects the trust's status as the sole acute provider for Herefordshire (one of the most rural counties in England) — Hereford County Hospital is a 2002-vintage Mercia Healthcare PFI scheme with an FM novation to Sodexo following the Carillion 2018 collapse. The PFI concession runs to c. 2032 when the estate transfers to trust ownership, materially changing the rates and depreciation profile. Eastern Powys (Wales) cross-border patient flow inflates ED demand without corresponding rates relief. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for Hereford County's PFI main hereditament. The 1 April 2026 next revaluation is the medium-term lever for the trust to challenge valuations.",
        "sources": [
            {"publisher": "Wye Valley NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wyevalley.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "Wye Valley NHS Trust provider profile (RLQ)", "url": "https://www.cqc.org.uk/provider/RLQ"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"}
        ],
        "related": ["Wye Valley NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Stockport NHS Foundation Trust", "Business rates — Mid Cheshire Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Lease expenditure — Mid Cheshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Mid Cheshire Hospitals NHS Foundation Trust"}],
        "description": "Mid Cheshire's £1.406M lease expenditure line covers IFRS 16 right-of-use depreciation and interest on operating-style leases held outside the PFI/LIFT envelope — chiefly imaging modality leases (MRI, CT), pathology analyser leases, vehicle pool, and short-term modular clinical-space leases used to decant RAAC-affected ward space at Leighton Hospital following the September 2023 HSSIB list. Mid Cheshire is in the NHP cohort for Leighton replacement (deferred under the Reset January 2025 to post-2030).",
        "beneficiaries": "c. 4,800 WTE staff serving a c. 320,000 mid-Cheshire catchment (Crewe, Nantwich, Northwich, Winsford); c. 90,000 ED attendances/yr at Leighton ED; c. 65,000 admissions/yr; sole acute provider for mid-Cheshire — RAAC-driven decant of ward space into modular leased units shapes the lease profile.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — IAS 36 (impairment of right-of-use assets)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.406M"},
            {"label": "Trust scale", "value": "Leighton Hospital + Victoria Infirmary + Elmhurst Intermediate Care Centre; c. 4,800 WTE"},
            {"label": "Composition", "value": "Imaging modality leases (MRI/CT) + pathology analysers + vehicle pool + RAAC modular decant clinical-space leases — IFRS 16 ROU depreciation + interest"},
            {"label": "RAAC modular decant", "value": "September 2023 HSSIB list — Leighton on RAAC list — modular ward leases driven decant of failing ceiling-plank space"},
            {"label": "IFRS 16 transition", "value": "DHSC GAM applied IFRS 16 from 1 April 2022 — material reclassification of operating leases as ROU assets"},
            {"label": "NHP status", "value": "Leighton replacement in NHP cohort — deferred under Reset Jan 2025 to post-2030 — extends RAAC-driven modular leasing"},
            {"label": "Funding trajectory", "value": "Pre-IFRS 16 op-lease £nil onshore → 2022-23 c. £1.0M → 2023-24 c. £1.3M → 2024-25 £1.406M — IFRS 16 ROU + RAAC modular ramp-up"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of NHS Cheshire and Merseyside ICB"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + Pharmacy + Pathology + IT + Finance + lessors (Siemens Healthineers, GE HealthCare, Modulek/Portakabin etc.)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + DHSC New Hospital Programme + NHS Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 IFRS 16 disclosure; HSSIB September 2023 RAAC list; NAO RAAC report; CQC RBT inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 op-lease off-BS treatment + pre-RAAC baseline · Successor: continued IFRS 16 ROU + Leighton NHP rebuild post-2030 (Reset deferred)"}
        ],
        "notes": "Mid Cheshire's lease expenditure line is materially shaped by the trust's RAAC-driven response — Leighton Hospital was on the September 2023 HSSIB RAAC list with concrete-plank failure risk, and the trust has decanted affected ward space into modular leased units (Modulek/Portakabin-style) which sit on the IFRS 16 right-of-use balance sheet. The IFRS 16 transition from 1 April 2022 reclassified operating leases (imaging modalities, pathology analysers, vehicle pool) onto the BS. The NHP Reset (January 2025) deferred Leighton replacement to post-2030, extending the RAAC-driven modular leasing exposure. Trust E&F and Finance teams manage the modular decant in coordination with the DHSC New Hospital Programme team and NHS Cheshire and Merseyside ICB. The medium-term lease line will compress only after the eventual NHP new-build delivery.",
        "sources": [
            {"publisher": "Mid Cheshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mcht.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS estates: investigation and listings", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme: Plan for Implementation (Jan 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"}
        ],
        "related": ["Mid Cheshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Cambridge University Hospitals NHS Foundation Trust", "Business rates — Mid Cheshire Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "Inventories written down — Nottingham University Hospitals NHS Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Nottingham University Hospitals NHS Trust"}],
        "description": "NUH's £1.391M inventories written down line is the IAS 2-compliant write-down of obsolete, expired or damaged stock — chiefly out-of-shelf-life sterile consumables, expired drugs (cross-ref drugs sub-line), discontinued surgical implants, manufacturer-recalled stock, and slow-moving prosthesis lines across QMC (Queen's Medical Centre) and Nottingham City Hospital. NUH is a major teaching tertiary trust hosting East Midlands Major Trauma Centre, transplant, neurosciences and oncology. East Midlands ICS context.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 800,000 Nottingham core catchment plus tertiary referrals across the East Midlands (c. 4.5M); c. 220,000 ED attendances/yr at QMC ED; c. 200,000 admissions/yr; East Midlands Major Trauma Centre; transplant, neurosciences, oncology and CDF (Children's Disability Funded) services.",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — IAS 36 (impairment of inventory) — NHS Act 2006 — Health and Care Act 2022 — MHRA medical device recall regs",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£1.391M"},
            {"label": "Trust scale", "value": "Queen's Medical Centre (QMC) + Nottingham City Hospital + Ropewalk House; c. 17,000 WTE"},
            {"label": "Composition", "value": "Out-of-shelf-life sterile consumables + expired drugs (cross-ref) + discontinued surgical implants + MHRA-recalled stock + slow-moving prostheses"},
            {"label": "Specialty mix driver", "value": "MTC + transplant + neurosciences + oncology specialty mix drives high-value implant + biologic-prosthesis tail with elevated obsolescence risk"},
            {"label": "MHRA recall interaction", "value": "Manufacturer/MHRA-driven medical-device recalls (e.g. metal-on-metal hip implants, breast implants) generate periodic write-down spikes"},
            {"label": "IAS 2 measurement", "value": "Lower of cost and net realisable value; write-down to NRV recognised in P&L when obsolescence/expiry identified"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.1M → 2023-24 c. £1.32M → 2024-25 £1.391M — driven by post-COVID PPE stockpile run-down + tertiary specialty implant churn"},
            {"label": "East Midlands ICS", "value": "Member of Nottingham and Nottinghamshire ICB; tertiary referrals across East Midlands ICBs"},
            {"label": "Section 29A warning notice", "value": "NUH maternity services placed under enhanced regulatory oversight (Donna Ockenden review of Nottingham maternity ongoing) — drives elevated stock-management scrutiny"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Pathology + Theatres + Finance + NHS Supply Chain + MHRA"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Supply Chain + Nottingham and Nottinghamshire ICB + MHRA"},
            {"label": "Evaluation evidence", "value": "Carter Lord review on inventory; NHS Supply Chain category reviews; Trust ARA 2023-24 IAS 2 disclosure; Donna Ockenden Nottingham maternity review (in progress)"},
            {"label": "Predecessor / successor", "value": "Predecessor: post-COVID PPE stockpile build-up (2020-22) · Successor: continued post-COVID stockpile run-down + Donna Ockenden recommendations on stock management"}
        ],
        "notes": "NUH's inventories written down line reflects the trust's status as a major teaching tertiary centre (Major Trauma Centre, transplant, neurosciences, oncology) with a high-value implant and biologic-prosthesis tail subject to elevated obsolescence risk. The post-COVID PPE stockpile run-down (2020-22 build-up versus shelf-life expiry 2023-25) has driven a multi-year wave of write-downs across NHS trusts including NUH. MHRA-driven medical-device recalls generate periodic spikes (e.g. metal-on-metal hip implants, breast implants). NUH is currently subject to the ongoing Donna Ockenden review into its maternity services with enhanced regulatory oversight, driving elevated stock-management and governance scrutiny across the trust. Carter Lord review benchmarks and NHS Supply Chain category-tower data inform the trust's inventory-management framework.",
        "sources": [
            {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nuh.nhs.uk/about-our-trust/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 2 Inventories", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/"},
            {"publisher": "Donna Ockenden", "title": "Independent review of NHS maternity services at Nottingham University Hospitals NHS Trust", "url": "https://www.ockendenmaternityreview.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "Nottingham University Hospitals NHS Trust provider profile (RX1)", "url": "https://www.cqc.org.uk/provider/RX1"}
        ],
        "related": ["Nottingham University Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Donna Ockenden Nottingham maternity review", "NHS Supply Chain", "MHRA"]
    },
    "PFI / LIFT charges — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "UHSussex's £1.378M PFI/LIFT charges line is a residual tail covering on-going service-concession charges under IFRIC 12 plus IFRS 16 (post-2022 lessee-side reclassifications) — chiefly small LIFT-vehicle community-clinic concession arrangements across the trust's broad Sussex footprint (St Richard's Chichester, Worthing, Brighton & Sussex (RSCH), Princess Royal Haywards Heath, Royal Alexandra Children's). Trust formed April 2021 by merger of Brighton and Sussex University Hospitals + Western Sussex Hospitals. Sussex ICS context.",
        "beneficiaries": "c. 17,500 WTE staff serving a c. 1.8M Sussex catchment (Chichester, Worthing, Brighton, Mid Sussex, Adur, Arun); c. 360,000 ED attendances/yr across 4 EDs (RSCH, Worthing, St Richard's, Princess Royal); c. 250,000 admissions/yr; one of the largest non-London acute trust footprints by site count; designated Major Trauma Centre at RSCH.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 lessee reclassification) — DHSC Group Accounting Manual 2024-25 — DHSC PFI / LIFT guidance — NHS (Local Improvement Finance Trust) Act 2002 (LIFT)",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.378M"},
            {"label": "Trust scale", "value": "RSCH (Brighton) + Princess Royal (Haywards Heath) + St Richard's (Chichester) + Worthing + Royal Alexandra Children's; c. 17,500 WTE"},
            {"label": "Merger", "value": "Created 1 April 2021 by merger of Brighton and Sussex University Hospitals + Western Sussex Hospitals"},
            {"label": "Composition", "value": "Residual tail — small LIFT community-clinic concessions + IFRS 16 reclassified service-concession components — large PFIs (RSCH 3Ts redevelopment) sit elsewhere on the BS"},
            {"label": "RSCH 3Ts", "value": "RSCH Trauma, Teaching and Tertiary care redevelopment (2018 opening) — Laing O'Rourke build, separately accounted"},
            {"label": "LIFT scheme heritage", "value": "Sussex LIFTCo community-clinic concessions across Brighton/Worthing — 25-year deals from c. 2005-2010 — small residual unitary charges"},
            {"label": "Funding trajectory", "value": "2022-23 c. £1.6M → 2023-24 c. £1.45M → 2024-25 £1.378M — slow run-off as LIFT concessions mature toward end-of-term"},
            {"label": "Sussex ICS", "value": "Member of NHS Sussex ICB (Sussex Health and Care Partnership)"},
            {"label": "Maternity scrutiny", "value": "UHSussex maternity placed under enhanced CQC regulatory oversight 2022-2024 (separate police investigation into baby deaths) — drives wider operational and governance scrutiny"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + LIFTCo (community-clinic concessionaires) + ICS estate team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC PFI/LIFT team + NHS Sussex ICB + Treasury (PFI policy)"},
            {"label": "Evaluation evidence", "value": "NAO PFI / LIFT reports; Trust ARA 2023-24 IFRIC 12 disclosure; CQC RYR inspections; police maternity investigation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger BSUH + WSHFT separate PFI/LIFT registers · Successor: ongoing LIFT concession run-off + 2027 RSCH 3Ts Stage 2 completion"}
        ],
        "notes": "UHSussex's PFI/LIFT charges line is a residual tail covering small LIFT community-clinic concessions across the trust's broad 5-site Sussex footprint — the trust was created by April 2021 merger of Brighton and Sussex University Hospitals (RSCH) and Western Sussex Hospitals (St Richard's Chichester + Worthing + Southlands). The major RSCH 3Ts redevelopment (Laing O'Rourke, opened 2018) is separately accounted for outside this residual. The Sussex LIFTCo community-clinic concessions originate from c. 2005-2010 25-year deals and are now running off toward end-of-term. UHSussex maternity has been under CQC enhanced regulatory oversight 2022-2024 alongside a separate Sussex Police investigation into baby deaths, driving wider operational and governance scrutiny across the trust. Treasury PFI policy and DHSC PFI/LIFT guidance govern the residual run-off.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhsussex.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "IFRS Foundation", "title": "IFRIC 12 Service Concession Arrangements", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifric-12-service-concession-arrangements/"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Sussex NHS Foundation Trust provider profile (RYR)", "url": "https://www.cqc.org.uk/provider/RYR"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "Business rates — East Sussex Healthcare NHS Trust", "NHS Sussex ICB"]
    },
    "Transport (business + patient) — East Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "East Sussex Healthcare NHS Trust"}],
        "description": "ESHT's £1.370M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), PTS eligible non-emergency journeys, courier services moving pathology specimens between Conquest Hospital (Hastings), Eastbourne DGH, Bexhill, Uckfield, Crowborough community sites, and IFRS 16-capitalised pool fleet. PTS in Sussex is commissioned by NHS Sussex ICB. The trust's twin-DGH model (Conquest + Eastbourne DGH) drives high inter-site patient and pathology courier volumes.",
        "beneficiaries": "c. 7,500 WTE staff claiming business mileage; c. 35,000 PTS-eligible patient journeys/yr (renal, oncology, frailty); c. 145,000 ED attendances/yr across Conquest + Eastbourne DGH EDs; c. 90,000 admissions/yr; c. 525,000 East Sussex catchment with high deprivation in Hastings + Bexhill coastal strip.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria (2021) — Agenda for Change Section 17 — HMRC AMAP rates (45p/25p) — IFRS 16 Leases (pool fleet) — DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.370M"},
            {"label": "Trust scale", "value": "Conquest Hospital (Hastings) + Eastbourne DGH + Bexhill + Uckfield + Crowborough + community outposts; c. 7,500 WTE"},
            {"label": "Twin-DGH model", "value": "Conquest + Eastbourne DGH — drives high inter-site patient + pathology courier volumes (specialty splits between sites)"},
            {"label": "Composition", "value": "Staff business mileage (AfC S17 + AMAP) + PTS journeys + courier (pathology/notes) + IFRS 16 pool-fleet ROU"},
            {"label": "PTS commissioner", "value": "NHS Sussex ICB (regional NEPTS contract); SECAmb for emergency transfers"},
            {"label": "Deprivation driver", "value": "Hastings + Bexhill coastal-strip decile-1/2 IMD ranking — high PTS demand from low-car-ownership patients"},
            {"label": "AMAP rate freeze", "value": "HMRC 45p/25p frozen since 2011 — 14-year cumulative real-terms erosion"},
            {"label": "IFRS 16 pool fleet", "value": "Pool vehicles reclassified as ROU assets from 1 April 2022"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.15M → 2023-24 c. £1.32M → 2024-25 £1.370M — twin-DGH inter-site flows + IFRS 16 ROU + strike rebooking"},
            {"label": "Delivery body", "value": "Trust E&F + Operations + Pathology + courier contractor + Sussex ICB-commissioned NEPTS provider + SECAmb"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Sussex ICB + HMRC (AMAP) + NHSE PTS team"},
            {"label": "Evaluation evidence", "value": "CQC RXC inspections (2018 'inadequate' rating + subsequent improvement); NAO PTS reports; Trust ARA 2023-24; NHSE PTS eligibility review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 pre-reconfiguration baseline + pre-IFRS 16 op-lease · Successor: Sussex ICS twin-DGH future review + ICB PTS recommissioning"}
        ],
        "notes": "ESHT's transport line is shaped by the trust's twin-DGH model (Conquest Hastings + Eastbourne DGH) which drives high inter-site patient transport and pathology courier volumes due to specialty splits between sites — a service-reconfiguration legacy from 2014-2018 disputes over stroke, A&E and maternity services. High local deprivation (Hastings + Bexhill coastal-strip decile-1/2 IMD) inflates PTS demand from low-car-ownership patients. The HMRC AMAP rate freeze at 45p/25p (since 2011) erodes real-terms reimbursement for c. 7,500 WTE. The IFRS 16 transition from 1 April 2022 reclassified pool-fleet leases onto the balance sheet. ESHT was rated 'inadequate' by CQC in 2018 with subsequent improvement; the Sussex ICS-led twin-DGH future review remains the medium-term lever, alongside ICB PTS recommissioning.",
        "sources": [
            {"publisher": "East Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esht.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-emergency patient transport services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "HMRC", "title": "Approved mileage allowance payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Care Quality Commission", "title": "East Sussex Healthcare NHS Trust provider profile (RXC)", "url": "https://www.cqc.org.uk/provider/RXC"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["East Sussex Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospitals Dorset NHS Foundation Trust", "Business rates — East Sussex Healthcare NHS Trust", "NHS Sussex ICB"]
    },
    "Transport (business + patient) — Royal United Hospitals Bath NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Royal United Hospitals Bath NHS Foundation Trust"}],
        "description": "RUH Bath's £1.369M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), PTS eligible non-emergency journeys, courier services moving pathology specimens between the RUH Combe Park (Bath) main site and outreach community sites across BANES, Wiltshire and Somerset, and IFRS 16-capitalised pool fleet. PTS in BSW (Bath, Swindon and Wiltshire) is commissioned by NHS BSW ICB. RUH is a single-DGH FT with a sprawling rural catchment.",
        "beneficiaries": "c. 5,500 WTE staff claiming business mileage; c. 25,000 PTS-eligible patient journeys/yr; c. 90,000 ED attendances/yr at RUH ED; c. 65,000 admissions/yr; c. 500,000 BANES + west Wiltshire + Mendip catchment; rural geography drives long staff and patient travel distances.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria (2021) — Agenda for Change Section 17 — HMRC AMAP rates (45p/25p) — IFRS 16 Leases (pool fleet) — DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Transport 2024-25", "value": "£1.369M"},
            {"label": "Trust scale", "value": "Royal United Hospital (Combe Park, Bath) + Sulis Hospital (subsidiary) + community outposts across BANES/Wiltshire/Somerset; c. 5,500 WTE"},
            {"label": "Composition", "value": "Staff business mileage (AfC S17 + AMAP) + PTS journeys + courier (pathology/notes) + IFRS 16 pool-fleet ROU"},
            {"label": "Sulis Hospital", "value": "Trust-owned independent-sector subsidiary (acquired 2021 — formerly Bath BMI Clinic) — additional inter-site transport flows"},
            {"label": "PTS commissioner", "value": "NHS BSW ICB (Bath, Swindon and Wiltshire); SWASFT for emergency transfers"},
            {"label": "Rural catchment", "value": "BANES + west Wiltshire + Mendip rural geography — long staff and patient travel distances drive high mileage volume"},
            {"label": "AMAP rate freeze", "value": "HMRC 45p/25p frozen since 2011 — 14-year cumulative real-terms erosion"},
            {"label": "IFRS 16 pool fleet", "value": "Pool vehicles reclassified as ROU assets from 1 April 2022"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.15M → 2023-24 c. £1.31M → 2024-25 £1.369M — Sulis integration + IFRS 16 ROU + rural mileage CPI"},
            {"label": "Delivery body", "value": "Trust E&F + Operations + Pathology + courier contractor + BSW ICB-commissioned NEPTS provider + SWASFT"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS BSW ICB + HMRC (AMAP) + NHSE PTS team"},
            {"label": "Evaluation evidence", "value": "NAO PTS reports; CQC RD1 inspections; Trust ARA 2023-24; NHSE PTS eligibility review; BSW ICB Estates Strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Sulis acquisition baseline + pre-IFRS 16 op-lease · Successor: BSW ICB PTS recommissioning + further Sulis integration"}
        ],
        "notes": "RUH Bath's transport line is shaped by the trust's rural Bath/west Wiltshire/Mendip catchment which drives long staff and patient travel distances, and the 2021 acquisition of Sulis Hospital (the former Bath BMI clinic) as a trust-owned independent-sector subsidiary which generates additional inter-site transport flows. The HMRC AMAP rate freeze at 45p/25p (since 2011) erodes real-terms reimbursement for c. 5,500 WTE in a high-mileage trust. The IFRS 16 transition from 1 April 2022 reclassified pool-fleet leases onto the balance sheet. NHS BSW ICB (Bath, Swindon and Wiltshire) recommissioning of NEPTS is the medium-term lever, alongside continued Sulis integration as the trust expands its independent-sector and elective-recovery activity.",
        "sources": [
            {"publisher": "Royal United Hospitals Bath NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ruh.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Non-emergency patient transport services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "HMRC", "title": "Approved mileage allowance payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Care Quality Commission", "title": "Royal United Hospitals Bath NHS Foundation Trust provider profile (RD1)", "url": "https://www.cqc.org.uk/provider/RD1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Royal United Hospitals Bath NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — East Sussex Healthcare NHS Trust", "Sulis Hospital", "NHS BSW ICB"]
    },
    "Business rates — University Hospitals of Morecambe Bay NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals of Morecambe Bay NHS Foundation Trust"}],
        "description": "UHMBT's £1.362M business-rates line covers non-domestic rate liability across the trust's three-DGH footprint — Royal Lancaster Infirmary (RLI), Furness General Hospital (FGH, Barrow-in-Furness) and Westmorland General Hospital (WGH, Kendal) — plus community-clinic outposts. Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024. RLI is in the New Hospital Programme cohort (deferred under the Reset January 2025). Lancashire and South Cumbria ICS context.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 365,000 Morecambe Bay catchment (Lancaster, Barrow-in-Furness, Kendal, South Lakeland, Morecambe); c. 130,000 ED attendances/yr across RLI + FGH EDs; c. 80,000 admissions/yr; sole acute provider for the Morecambe Bay catchment with severe rural and peninsula geography.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.362M"},
            {"label": "Trust scale", "value": "Royal Lancaster Infirmary (RLI) + Furness General (FGH, Barrow) + Westmorland General (WGH, Kendal) + community outposts; c. 7,500 WTE"},
            {"label": "NHP status", "value": "RLI in NHP cohort — deferred under Reset Jan 2025 to post-2030 — sustains current rateable assessment for longer than originally planned"},
            {"label": "Morecambe Bay history", "value": "Subject of 2015 Bill Kirkup Morecambe Bay Investigation into maternity-services failures — long governance overhaul"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.2M → 2023-24 c. £1.31M → 2024-25 £1.362M — 2023 list revaluation + multiplier uplift + RLI sustained assessment under NHP deferral"},
            {"label": "Lancs and South Cumbria ICS", "value": "Member of NHS Lancashire and South Cumbria ICB; cross-county geography (Lancashire + Cumbria)"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA (rateable-value setter) + Lancaster City Council / Westmorland and Furness Council (unitary billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + DHSC New Hospital Programme + NHS Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; Bill Kirkup Morecambe Bay Investigation (2015); NAO RAAC + NHP reports; Trust ARA 2023-24; CQC RTX inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + RLI NHP rebuild post-2030 (Reset deferred)"}
        ],
        "notes": "UHMBT's business-rates line reflects the trust's three-DGH footprint covering a severe rural and peninsula geography (Morecambe Bay catchment with Barrow-in-Furness peninsula isolation). Royal Lancaster Infirmary is in the NHP cohort, and the Reset (January 2025) deferred its replacement to post-2030 — sustaining the current rateable assessment for longer than originally planned. The trust is rebuilding from the 2015 Bill Kirkup Morecambe Bay Investigation into maternity-services failures with a long governance overhaul. NHS trusts are not eligible for mandatory 80% charitable relief, so the full liability is borne. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for RLI and FGH main sites. The 1 April 2026 revaluation is the medium-term lever.",
        "sources": [
            {"publisher": "University Hospitals of Morecambe Bay NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhmb.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Morecambe Bay Investigation (Bill Kirkup, 2015)", "url": "https://www.gov.uk/government/publications/morecambe-bay-investigation-report"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals of Morecambe Bay NHS Foundation Trust provider profile (RTX)", "url": "https://www.cqc.org.uk/provider/RTX"}
        ],
        "related": ["University Hospitals of Morecambe Bay NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Mid Cheshire Hospitals NHS Foundation Trust", "Business rates — Wye Valley NHS Trust", "New Hospital Programme"]
    },
}
