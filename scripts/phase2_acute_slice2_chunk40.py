# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 40 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {}

NEW["Transport (business + patient) — Milton Keynes University Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Transport (business + patient)", "parent": "Milton Keynes University Hospital NHS Foundation Trust"}],
    "description": "Milton Keynes University Hospital NHS FT's £0.62M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between the Standing Way main site and community/satellite locations, plus contracted non-emergency patient transport (NEPTS) for the Bedfordshire, Luton and Milton Keynes ICS catchment. As a single-site DGH on the new-town grid, MKUH has lower inter-site flow than peer multi-site trusts but a dispersed travel-to-work hinterland.",
    "beneficiaries": "c. 4,000 WTE staff serving a c. 350,000 catchment across Milton Keynes, north Buckinghamshire and parts of Bedfordshire; c. 110,000 ED attendances/yr at Standing Way; c. 70,000 admissions/yr; c. 350,000 outpatient attendances/yr; the Open University-aligned Faculty of Medicine partnership generates additional rotation-related travel.",
    "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Transport (business + patient) 2024-25", "value": "£0.62M"},
        {"label": "Trust scale", "value": "Single-site DGH (Standing Way, Eaglestone) plus community satellites; c. 4,000 WTE; serves Milton Keynes new town"},
        {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology courier + contracted NEPTS"},
        {"label": "NEPTS provider", "value": "EMED Group (formerly E-zec) on BLMK ICB framework — retendered against NHSE 2021 NEPTS Review eligibility"},
        {"label": "Inter-site flow", "value": "Lower than multi-site peers — most activity on the Standing Way campus; outreach to Buckingham, Bletchley and community clinics"},
        {"label": "Industrial action + NIC step-up", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel + NEPTS rebooking; April 2025 NIC step-up flows via contractor pass-through"},
        {"label": "AMAP rates 2024-25", "value": "HMRC AMAP frozen at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.58M → 2024-25 £0.62M — strike backfill + fuel pass-through + NEPTS uplift"},
        {"label": "BLMK ICS", "value": "Member of Bedfordshire, Luton and Milton Keynes ICB; collaborative NEPTS commissioning with Bedfordshire Hospitals"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + EMED Group (NEPTS) + EEAST (emergency overlap)"},
        {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; Trust ARA 2023-24; CQC RD8 inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-Review baseline · Successor: ICB-wide eligibility-criteria implementation + pool-fleet electrification"}
    ],
    "notes": "MKUH sits on the Standing Way single-site campus serving one of England's fastest-growing populations (the Milton Keynes new-town footprint is designated for further expansion under the Oxford-Cambridge Arc). Transport spend is structurally below peer DGHs because most activity is concentrated on a single campus, but staff travel-to-work distances are above average given the dispersed grid-square geography. The Open University Faculty of Medicine partnership (first cohort 2023) brings additional rotation-driven travel. April 2025 NIC step-up flows indirectly through NEPTS contractor pass-through; frozen AMAP rates compress staff mileage. BLMK ICB pool-fleet electrification aligns with the NHS net-zero 2040 commitment.",
    "sources": [
        {"publisher": "Milton Keynes University Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mkuh.nhs.uk/about-us/publications-and-policies"},
        {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
        {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "Milton Keynes University Hospital NHS Foundation Trust provider profile (RD8)", "url": "https://www.cqc.org.uk/provider/RD8"}
    ],
    "related": ["Milton Keynes University Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Milton Keynes University Hospital NHS Foundation Trust", "Transport (business + patient) — Bedfordshire Hospitals NHS Foundation Trust", "NHS England"]
}

NEW["Business rates — Airedale NHS Foundation Trust"] = {
    "aliases": [{"name": "Business rates", "parent": "Airedale NHS Foundation Trust"}],
    "description": "Airedale NHS FT's £0.62M business-rates line covers non-domestic rate liability for Airedale General Hospital (Steeton, near Keighley) plus community sites. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Airedale's rates exposure is dominated by a 1970 RAAC-plank constructed principal hereditament on the national reinforced-autoclaved-aerated-concrete critical-mitigation list.",
    "beneficiaries": "c. 3,400 WTE staff serving a c. 200,000 population across the Airedale, Wharfedale and Craven districts plus parts of east Lancashire; c. 75,000 ED attendances/yr at Airedale General; c. 50,000 admissions/yr; c. 290,000 outpatient attendances/yr; trust runs the national award-winning Digital Care Hub (telehealth/remote monitoring) serving wider population.",
    "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Business rates 2024-25", "value": "£0.62M"},
        {"label": "Trust scale", "value": "Airedale General (Steeton) + community sites; c. 3,400 WTE; serves Airedale/Wharfedale/Craven"},
        {"label": "Principal hereditament", "value": "Airedale General Hospital, Skipton Road, Steeton — 1970 RAAC-plank build (national RAAC critical-mitigation list)"},
        {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
        {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 tier rules from April 2025"},
        {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne by trust"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.55M → 2023-24 c. £0.59M → 2024-25 £0.62M — 2023 list revaluation effect"},
        {"label": "RAAC New Hospital Programme", "value": "Airedale named in 2023 RAAC seven (Oct 2023 announcement) — funded for full rebuild by 2030 under NHP"},
        {"label": "West Yorkshire ICS", "value": "Member of West Yorkshire ICB; collaborative procurement with Bradford Teaching Hospitals + Calderdale & Huddersfield"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates & Finance + VOA (valuations) + Bradford MDC (billing authority); MHCLG rates policy + DHSC + NHSE + NHP"},
        {"label": "Evaluation evidence", "value": "VOA rating-list publications; HSSIB RAAC reports; Trust ARA 2023-24; CQC RCF inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + post-2030 NHP rebuild rateable-value reset"}
    ],
    "notes": "Airedale's rates line is anchored on a single principal hereditament — Airedale General, a 1970 RAAC-plank construction identified by the 2022-23 NHSE/HSSIB survey as a critical-mitigation case and confirmed in the October 2023 RAAC announcement as one of seven trusts funded for full rebuild under the NHP by 2030. The rebuild will substantially reset rateable value at the next-but-one VOA revaluation. NHS trusts have no mandatory charitable rate relief — a structural disparity vs adjacent education-charity occupiers. April 2025 multiplier reform under the NDR (Multipliers and Private Finance) Act 2024 is unlikely to push Airedale into the £500k high-tier band given hereditament size.",
    "sources": [
        {"publisher": "Airedale NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.airedale-trust.nhs.uk/about-us/publications/"},
        {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — RAAC announcement October 2023", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "Airedale NHS Foundation Trust provider profile (RCF)", "url": "https://www.cqc.org.uk/provider/RCF"}
    ],
    "related": ["Airedale NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Bradford Teaching Hospitals NHS Foundation Trust", "Business rates — Calderdale and Huddersfield NHS Foundation Trust", "Valuation Office Agency"]
}

NEW["Lease expenditure — Epsom and St Helier University Hospitals NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Epsom and St Helier University Hospitals NHS Trust"}],
    "description": "Epsom and St Helier UH NHS Trust's £0.61M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across the trust's two principal sites — Epsom General Hospital (Surrey) and St Helier Hospital (Carshalton, south London) — and community/satellite locations including Sutton Hospital. Lease expenditure is structurally tied to the trust's split-site geography pending the long-running specialist emergency care hospital (SECH) reconfiguration.",
    "beneficiaries": "c. 5,200 WTE staff serving a c. 490,000 catchment across Surrey Downs and south-west London (Sutton, Merton, Kingston borders); c. 175,000 ED attendances/yr across Epsom + St Helier ED; c. 110,000 admissions/yr; c. 480,000 outpatient attendances/yr; the trust serves both a Surrey commuter belt and a deprived south-London urban catchment (Roehampton, Mitcham).",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.61M"},
        {"label": "Trust scale", "value": "Epsom General + St Helier + Sutton Hospital + community sites; c. 5,200 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT equipment + medical equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value (<$5k threshold) charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Estate condition", "value": "St Helier identified as critical backlog-maintenance case (1930s blocks); Epsom General in better condition"},
        {"label": "SECH programme", "value": "Specialist Emergency Care Hospital at Sutton (consolidating major emergency + maternity from St Helier + Epsom) — funded under NHP, multiple delays since 2020 OBC"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.58M → 2024-25 £0.61M — IFRS 16 transition steady-state"},
        {"label": "Surrey Heartlands + SWL ICS", "value": "Cross-ICS trust — Surrey Heartlands ICB (Epsom) + South West London ICB (St Helier/Sutton)"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + DHSC NHP + Surrey Heartlands ICB + SWL ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; NAO NHP reports; HSSIB backlog-maintenance reports; CQC RVR inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: post-SECH-build estate consolidation reduces split-site lease footprint"}
    ],
    "notes": "Epsom and St Helier's lease line is shaped by the long-running SECH (Specialist Emergency Care Hospital) reconfiguration — a £500M+ NHP scheme to consolidate major emergency care, maternity and acute medicine onto a new build at the Sutton Hospital site. The OBC was approved in 2020 but slipped under the NHP January 2023 reset; construction start has shifted into the late 2020s. Until the new estate opens, the trust carries elevated split-site running costs and short-term Sutton outreach leases. St Helier's 1930s blocks remain a critical backlog-maintenance liability per HSSIB tracking. The trust spans two ICBs (Surrey Heartlands + SWL), complicating shared-service and lease-portfolio rationalisation.",
    "sources": [
        {"publisher": "Epsom and St Helier University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.epsom-sthelier.nhs.uk/about-us/our-publications"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme update January 2023", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
        {"publisher": "Care Quality Commission", "title": "Epsom and St Helier University Hospitals NHS Trust provider profile (RVR)", "url": "https://www.cqc.org.uk/provider/RVR"}
    ],
    "related": ["Epsom and St Helier University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Epsom and St Helier University Hospitals NHS Trust", "Lease expenditure — Chelsea and Westminster Hospital NHS Foundation Trust", "Department of Health and Social Care"]
}

NEW["Transport (business + patient) — Bradford Teaching Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Transport (business + patient)", "parent": "Bradford Teaching Hospitals NHS Foundation Trust"}],
    "description": "Bradford Teaching Hospitals NHS FT's £0.61M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between Bradford Royal Infirmary, St Luke's Hospital and the Westwood Park rehabilitation site, plus contracted non-emergency patient transport (NEPTS) for the Bradford District and Craven catchment within the West Yorkshire ICS. The trust's role as a major teaching trust for the University of Bradford and Leeds drives additional rotation-related travel.",
    "beneficiaries": "c. 6,000 WTE staff serving a c. 540,000 Bradford District and Craven catchment with a high-deprivation profile (Bradford ranked among the most deprived large local authorities); c. 165,000 ED attendances/yr at Bradford Royal Infirmary; c. 95,000 admissions/yr; c. 540,000 outpatient attendances/yr; trust hosts the renowned Born in Bradford cohort study.",
    "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Transport (business + patient) 2024-25", "value": "£0.61M"},
        {"label": "Trust scale", "value": "Bradford Royal Infirmary + St Luke's + Westwood Park + community sites; c. 6,000 WTE; major teaching trust"},
        {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology courier + contracted NEPTS"},
        {"label": "NEPTS provider", "value": "Yorkshire Ambulance Service NHS Trust on West Yorkshire ICB framework (NEPTS retendered against NHSE 2021 Review)"},
        {"label": "Inter-site flow", "value": "BRI (acute) ↔ St Luke's (women's & children's, mental health, community) ↔ Westwood Park (rehab) — material specimen and staff movement"},
        {"label": "Industrial action + NIC step-up", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement; April 2025 NIC step-up flows via YAS NEPTS contractor"},
        {"label": "AMAP rates 2024-25", "value": "HMRC AMAP frozen at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.57M → 2024-25 £0.61M — strike backfill + fuel pass-through + NEPTS uplift"},
        {"label": "West Yorkshire ICS", "value": "Member of West Yorkshire ICB; collaborative NEPTS commissioning with Airedale, Calderdale & Huddersfield, Mid Yorkshire and Leeds"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + Yorkshire Ambulance Service (NEPTS)"},
        {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; Trust ARA 2023-24; CQC RAE inspections; Born in Bradford research"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-Review baseline · Successor: West Yorkshire ICB pool-fleet electrification + EPR-driven outpatient virtualisation"}
    ],
    "notes": "Bradford Teaching's transport line reflects its three-site footprint (BRI + St Luke's + Westwood Park) plus a high-volume community-services interface that drives material inter-site staff and pathology flows. The Yorkshire Ambulance Service NEPTS contract (West Yorkshire ICB framework) gives economy of scale vs single-trust contracts. Bradford serves one of the most deprived large local authorities in England, with high attendance from low-mobility patients eligible for NEPTS under the 2021 NHSE criteria. Industrial action 2023-24 added locum travel reimbursement; Born in Bradford and the major teaching role drive additional research-related and rotational travel. April 2025 NIC step-up flows indirectly via NEPTS contractor pass-through.",
    "sources": [
        {"publisher": "Bradford Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bradfordhospitals.nhs.uk/about-us/publications/"},
        {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
        {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
        {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Patient Transport Service", "url": "https://www.yas.nhs.uk/our-services/patient-transport-service/"},
        {"publisher": "Care Quality Commission", "title": "Bradford Teaching Hospitals NHS Foundation Trust provider profile (RAE)", "url": "https://www.cqc.org.uk/provider/RAE"}
    ],
    "related": ["Bradford Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "General supplies & services — Bradford Teaching Hospitals NHS Foundation Trust", "Transport (business + patient) — The Leeds Teaching Hospitals NHS Trust", "NHS England"]
}

NEW["Inventories written down — Royal Surrey NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Royal Surrey NHS Foundation Trust"}],
    "description": "Royal Surrey NHS FT's £0.60M inventories-written-down line records the IAS 2 net-realisable-value adjustment and obsolescence/expiry write-off of clinical consumables, drugs and surgical supplies across Royal Surrey County Hospital (Guildford), the St Luke's Cancer Centre and community services. The line is concentrated in expired pharmacy stock (high-cost cancer medicines including biologics and PRRT-related radiopharmaceuticals at St Luke's), short-shelf-life sterile-services consumables, and obsolete implantable-device inventory subject to MHRA field-safety notices.",
    "beneficiaries": "c. 4,400 WTE staff serving a c. 350,000 west Surrey + Hampshire-borders catchment; St Luke's Cancer Centre serves a tertiary cancer-network population across Surrey, Sussex and parts of Hampshire; c. 90,000 ED attendances/yr at Royal Surrey ED; c. 65,000 admissions/yr; c. 480,000 outpatient attendances/yr; specialist radiotherapy + theranostics network host trust.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 chapter 8 — Human Medicines Regulations 2012 — MHRA Yellow Card and Field Safety Corrective Action regime — NHS Act 2006 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.60M"},
        {"label": "Trust scale", "value": "Royal Surrey County Hospital (Guildford) + St Luke's Cancer Centre + community services; c. 4,400 WTE"},
        {"label": "Composition", "value": "Expired pharmacy stock (high-cost cancer drugs, biologics, radiopharmaceuticals) + short-shelf-life sterile consumables + MHRA-recalled implants"},
        {"label": "St Luke's specialist driver", "value": "Theranostics centre — Lutathera (lutetium-177-DOTATATE) PRRT and other radiopharmaceuticals carry short half-lives + high write-down risk"},
        {"label": "Cancer drug exposure", "value": "Tertiary cancer centre status concentrates high-cost biologic and CDF-funded medicines — small expiry events drive material write-downs"},
        {"label": "Standard", "value": "IAS 2: inventory at lower of cost and net realisable value; expired/obsolete written down to zero per GAM ch.8"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.55M → 2024-25 £0.60M — high-cost drug volume growth + MHRA recall events"},
        {"label": "Surrey Heartlands ICS", "value": "Member of Surrey Heartlands ICB; cross-trust pharmacy stock-pooling with adjacent trusts"},
        {"label": "Delivery body", "value": "Trust Pharmacy + Sterile Services + Procurement + Theatres + Stock Management + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM + MHRA + NHS Supply Chain + NHSE Specialised Commissioning"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 inventories note; NHSE Commercial team stock-management benchmarks; Carter productivity reports; CQC RA2"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IAS 2 historic-cost stock loss · Successor: Scan4Safety barcoded inventory + automated FEFO controls"}
    ],
    "notes": "Royal Surrey's inventories-written-down line is structurally elevated by tertiary cancer-centre status — St Luke's runs theranostics (Lutathera and similar lutetium-177 radiopharmaceuticals for neuroendocrine and prostate tumours) where medicines have very short half-lives and missed-appointment write-downs are non-trivial. Cancer Drugs Fund and high-cost biologic chemotherapy stock carries individual-line values of £5k-£50k per dose — a single expiry or MHRA-recall event can drive material write-downs. The 2022 Genesis Care radiotherapy partnership cancellation and retender altered the consumables mix but didn't eliminate the base rate. Scan4Safety barcoded inventory and FEFO controls are the medium-term mitigation, with Surrey Heartlands ICB drug stock-pooling.",
    "sources": [
        {"publisher": "Royal Surrey NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalsurrey.nhs.uk/about-us/board-and-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 8 (inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Medicines and Healthcare products Regulatory Agency", "title": "Field Safety Corrective Action notices", "url": "https://www.gov.uk/drug-device-alerts"},
        {"publisher": "NHS England", "title": "Cancer Drugs Fund", "url": "https://www.england.nhs.uk/cancer/cdf/"},
        {"publisher": "Care Quality Commission", "title": "Royal Surrey NHS Foundation Trust provider profile (RA2)", "url": "https://www.cqc.org.uk/provider/RA2"}
    ],
    "related": ["Royal Surrey NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Establishment costs — Royal Surrey NHS Foundation Trust", "Inventories written down — King’s College Hospital NHS Foundation Trust", "Medicines and Healthcare products Regulatory Agency"]
}

NEW["Lease expenditure — East Cheshire NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "East Cheshire NHS Trust"}],
    "description": "East Cheshire NHS Trust's £0.60M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across Macclesfield District General Hospital, Congleton War Memorial Hospital and the trust's community-services portfolio. East Cheshire is one of the smallest acute trusts in England by income and is currently in a Group Hospital Working / management arrangement with Mid Cheshire Hospitals NHS FT under the 2024 NHSE turnaround framework.",
    "beneficiaries": "c. 2,300 WTE staff serving a c. 200,000 catchment across eastern Cheshire (Macclesfield, Congleton, Knutsford, Wilmslow, Bollington, Poynton); c. 55,000 ED attendances/yr at Macclesfield DGH; c. 35,000 admissions/yr; c. 200,000 outpatient attendances/yr; trust runs community + integrated care services across the High Peak borders.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.60M"},
        {"label": "Trust scale", "value": "Macclesfield DGH + Congleton War Memorial + community sites; c. 2,300 WTE; small DGH"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Group arrangement", "value": "Group Hospital Working / management consolidation with Mid Cheshire Hospitals NHS FT (Leighton Hospital) under 2024 NHSE turnaround framework"},
        {"label": "Estate condition", "value": "Macclesfield DGH 1990s build, mid-life; Congleton 1970s blocks with backlog-maintenance pressure"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.57M → 2024-25 £0.60M — IFRS 16 transition steady-state + turnaround estate review"},
        {"label": "Cheshire & Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB; collaborative delivery with Mid Cheshire under group arrangement"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + Mid Cheshire group team"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + Cheshire and Merseyside ICB + NHSE Recovery Support Programme"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; NHSE Recovery Support Programme reports; HSSIB backlog-maintenance reports; CQC RJN inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: post-Mid-Cheshire-group lease-portfolio rationalisation + estate consolidation"}
    ],
    "notes": "East Cheshire is a small DGH in NHSE Recovery Support Programme oversight in recent years that entered a Group Hospital Working arrangement with neighbouring Mid Cheshire Hospitals NHS FT (Leighton, Crewe) in 2024 — partly a response to financial fragility and to the cross-Cheshire estate review. The lease line is dominated by community-services premises (intermediate care, physio outreach, GP-aligned clinics), IT and equipment short-term leases below the IFRS 16 ROU threshold. The 2024 NHSE turnaround framework drives a lease-portfolio review aimed at consolidating community-premises occupancy with Mid Cheshire and other Cheshire & Merseyside ICB partners. Backlog-maintenance pressures at Congleton War Memorial (1970s) make some lease-out scenarios viable for non-core functions.",
    "sources": [
        {"publisher": "East Cheshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastcheshire.nhs.uk/About-The-Trust/publications/annual-reports-and-accounts.htm"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Recovery Support Programme — segmentation framework", "url": "https://www.england.nhs.uk/publication/nhs-system-oversight-framework/"},
        {"publisher": "Care Quality Commission", "title": "East Cheshire NHS Trust provider profile (RJN)", "url": "https://www.cqc.org.uk/provider/RJN"},
        {"publisher": "NHS Confederation", "title": "Cheshire and Merseyside Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
    ],
    "related": ["East Cheshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — East Cheshire NHS Trust", "General supplies & services — East Cheshire NHS Trust", "Department of Health and Social Care"]
}

NEW["Termination & post-employment — The Leeds Teaching Hospitals NHS Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "The Leeds Teaching Hospitals NHS Trust"}],
    "description": "Leeds Teaching Hospitals NHS Trust's £0.60M termination & post-employment line covers IAS 19 short-term termination benefits — voluntary redundancy / mutually agreed resignation scheme (MARS) settlements, pay-in-lieu-of-notice, contractual termination payments and any post-employment benefit movements outside the NHS Pension Scheme accrual — across one of the largest acute trusts in England. The line is governed by the Public Sector Exit Payments Regulations 2020 (£95k cap, currently disapplied since Treasury directions 2021) and HMT Managing Public Money rules.",
    "beneficiaries": "c. 22,000 WTE staff at one of the largest NHS providers (Leeds General Infirmary + St James's University Hospital + Wharfedale + Chapel Allerton + Seacroft + LGI Children's); serves a c. 800,000 Leeds local catchment plus a tertiary referral population of c. 5.4M for specialist services (transplantation, paediatric cardiac, major trauma centre, oncology); c. 285,000 ED attendances/yr; c. 250,000 admissions/yr.",
    "legal_basis": "IAS 19 Employee Benefits — Public Sector Exit Payments Regulations 2020 (currently disapplied per HMT direction 2021) — NHS Pension Scheme Regulations 2015 — HMT Managing Public Money — DHSC Group Accounting Manual 2024-25 — NHS Act 2006",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.60M"},
        {"label": "Trust scale", "value": "LGI + St James's + Wharfedale + Chapel Allerton + Seacroft + Leeds Children's; c. 22,000 WTE; major teaching trust + major trauma centre"},
        {"label": "Composition", "value": "Voluntary redundancy + MARS settlements + pay-in-lieu-of-notice + contractual termination payments + post-employment benefit IAS 19 movements"},
        {"label": "Cap regime", "value": "Public Sector Exit Payments (Restriction) Regs 2020 (£95k cap) — Regulations remain on statute but disapplied via HMT direction Feb 2021 pending review"},
        {"label": "Pension interaction", "value": "Strain-on-fund payments to NHS Pension Scheme captured separately; only non-pension termination components feed this line"},
        {"label": "Workforce restructuring", "value": "Industrial action 2023-24 did not directly drive termination — but post-strike + corporate-services consolidation with WY ICB partners adds modest MARS/VR volume"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.4M → 2023-24 c. £0.55M → 2024-25 £0.60M — modest VR programme volume + executive turnover"},
        {"label": "West Yorkshire ICS", "value": "Member of West Yorkshire ICB; lead provider for major trauma + tertiary specialties"},
        {"label": "Delivery body + policy owner", "value": "Trust HR + Finance + NHSBSA Pensions + Treasury Solicitor (high-value); NHSE People + DHSC + HMT exit-payments policy"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 remuneration & exit-package disclosure; NAO Public Sector Exit Payments reports; PAC scrutiny of Treasury direction"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 unrestricted exit-payment regime · Successor: planned re-application of £95k cap pending HMT review"}
    ],
    "notes": "Leeds Teaching's termination & post-employment line is structurally modest relative to its £2bn+ pay bill — routine voluntary-redundancy and MARS programmes plus exit packages under the (currently disapplied) Public Sector Exit Payments Regulations 2020. The £95k cap was withdrawn via HMT February 2021 direction after legal challenges, but the regulations remain on statute pending review. The trust publishes individual exit-package disclosure in its remuneration report per GAM. As a major trauma centre with extensive tertiary specialties, Leeds carries a senior medical workforce; high-value consultant or executive exits can be material individually. Industrial action 2023-24 did not directly drive termination but post-strike restructuring may feed MARS volume.",
    "sources": [
        {"publisher": "The Leeds Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsth.nhs.uk/about-us/our-publications/"},
        {"publisher": "HM Treasury", "title": "Public Sector Exit Payments — disapplication direction February 2021", "url": "https://www.gov.uk/government/publications/public-sector-exit-payments-treasury-directions"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "National Audit Office", "title": "Investigation into government's handling of the £95,000 public sector exit payment cap", "url": "https://www.nao.org.uk/reports/exit-payment-cap/"},
        {"publisher": "Care Quality Commission", "title": "The Leeds Teaching Hospitals NHS Trust provider profile (RR8)", "url": "https://www.cqc.org.uk/provider/RR8"}
    ],
    "related": ["The Leeds Teaching Hospitals NHS Trust", "Staff Costs", "NHS Acute Trusts", "Termination & post-employment — Guy's & St Thomas' NHS Foundation Trust", "Termination & post-employment — King’s College Hospital NHS Foundation Trust", "HM Treasury"]
}

NEW["Lease expenditure — North Tees and Hartlepool NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "North Tees and Hartlepool NHS Foundation Trust"}],
    "description": "North Tees and Hartlepool NHS FT's £0.60M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across the University Hospital of North Tees (Stockton-on-Tees), the University Hospital of Hartlepool and a network of community sites. The trust is a confirmed New Hospital Programme cohort-2 scheme — a single-site replacement hospital at Wynyard intended to consolidate acute services from both Stockton and Hartlepool sites.",
    "beneficiaries": "c. 5,500 WTE staff serving a c. 400,000 catchment across Stockton-on-Tees, Hartlepool and parts of County Durham; c. 145,000 ED attendances/yr (combined North Tees A&E + Hartlepool UTC); c. 85,000 admissions/yr; c. 380,000 outpatient attendances/yr; serves a high-deprivation Tees Valley population.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.60M"},
        {"label": "Trust scale", "value": "University Hospital of North Tees (Stockton) + University Hospital of Hartlepool + community sites; c. 5,500 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value (<$5k threshold) charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "New Hospital Programme", "value": "Single-site Wynyard hospital — confirmed in NHP cohort 2 (post-2030 delivery under January 2023 reset)"},
        {"label": "Estate condition", "value": "North Tees University Hospital (1968) + Hartlepool (older, partly decommissioned for acute) — significant backlog maintenance pending NHP rebuild"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.57M → 2024-25 £0.60M — IFRS 16 transition steady-state"},
        {"label": "North East and North Cumbria ICS", "value": "Member of North East and North Cumbria ICB; collaborative pathology partnership with adjacent Tees Valley trusts"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + DHSC NHP team (planning)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + DHSC NHP + NENC ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; NAO NHP reports (2023, 2025); HSSIB backlog-maintenance reports; CQC RVW inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: post-Wynyard New Hospital lease-portfolio rationalisation in 2030s"}
    ],
    "notes": "North Tees and Hartlepool's lease line reflects a two-site acute footprint (North Tees plus a much-reduced Hartlepool after loss of acute services) plus dispersed community premises across Stockton, Hartlepool and Easington. The Wynyard New Hospital (consolidating acute services on a greenfield site near Billingham) is one of the longest-running NHP commitments — first approved circa 2009, repeatedly deferred, and now in NHP cohort 2 for post-2030 delivery after the January 2023 Treasury reset. Until Wynyard, the trust runs elevated split-site costs with material backlog-maintenance pressure at North Tees and Hartlepool. NENC ICB community-premises consolidation is the medium-term mitigation alongside the NHP build.",
    "sources": [
        {"publisher": "North Tees and Hartlepool NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nth.nhs.uk/about/publications-policies-and-strategies/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — schemes and cohorts", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
        {"publisher": "Care Quality Commission", "title": "North Tees and Hartlepool NHS Foundation Trust provider profile (RVW)", "url": "https://www.cqc.org.uk/provider/RVW"}
    ],
    "related": ["North Tees and Hartlepool NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — North Tees and Hartlepool NHS Foundation Trust", "General supplies & services — North Tees and Hartlepool NHS Foundation Trust", "Department of Health and Social Care"]
}

NEW["Transport (business + patient) — Chesterfield Royal Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Transport (business + patient)", "parent": "Chesterfield Royal Hospital NHS Foundation Trust"}],
    "description": "Chesterfield Royal Hospital NHS FT's £0.59M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between the Calow main site and community/satellite locations across north Derbyshire, plus contracted non-emergency patient transport (NEPTS) for the Joined Up Care Derbyshire ICS catchment. The trust's catchment includes a dispersed rural Peak District hinterland that drives above-peer NEPTS demand under the 2021 NHSE eligibility criteria.",
    "beneficiaries": "c. 4,000 WTE staff serving a c. 410,000 catchment across north and east Derbyshire including Chesterfield, Bolsover, North East Derbyshire, the Peak District and parts of NE Derbyshire/Sheffield borders; c. 110,000 ED attendances/yr at Chesterfield Royal; c. 65,000 admissions/yr; c. 350,000 outpatient attendances/yr.",
    "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Transport (business + patient) 2024-25", "value": "£0.59M"},
        {"label": "Trust scale", "value": "Chesterfield Royal Hospital (Calow) + community sites; c. 4,000 WTE; serves north Derbyshire + Peak District"},
        {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology courier + contracted NEPTS"},
        {"label": "NEPTS provider", "value": "Thames Ambulance Service / DHU Healthcare framework — Derbyshire NEPTS retendered 2022 against NHSE Review eligibility"},
        {"label": "Rural hinterland driver", "value": "Peak District + dispersed north-Derbyshire population drives above-peer NEPTS volume under low-mobility / no-public-transport criteria"},
        {"label": "Industrial action + NIC step-up", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement; April 2025 NIC step-up flows via NEPTS contractor"},
        {"label": "AMAP rates 2024-25", "value": "HMRC AMAP frozen at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.55M → 2024-25 £0.59M — strike backfill + fuel pass-through + NEPTS uplift"},
        {"label": "Joined Up Care Derbyshire ICS", "value": "Member of Derby and Derbyshire ICB; collaborative NEPTS commissioning with University Hospitals of Derby and Burton + DHU"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Thames Ambulance / DHU (NEPTS) + EMAS (emergency overlap)"},
        {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; Trust ARA 2023-24; CQC RFS inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-Review baseline · Successor: ICB-wide eligibility implementation + EPR-driven outpatient virtualisation"}
    ],
    "notes": "Chesterfield Royal sits on the Calow campus serving a wide rural hinterland that includes a substantial part of the Peak District National Park and the dispersed villages of north-east Derbyshire. The geography drives above-peer NEPTS demand because public transport coverage is patchy and many elderly patients qualify under the 2021 NHSE 'no realistic alternative' criterion. The 2022 Derbyshire NEPTS retender (Thames Ambulance / DHU Healthcare framework) gave some price discipline. Industrial action 2023-24 added locum travel and rebooking cost. The trust's joint venture with DHU Healthcare (a CIC providing community services and NHS 111) is a notable governance feature. Joined Up Care Derbyshire ICS pool-fleet electrification is the medium-term ambition.",
    "sources": [
        {"publisher": "Chesterfield Royal Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chesterfieldroyal.nhs.uk/about-us/publications-and-policies"},
        {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
        {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "Chesterfield Royal Hospital NHS Foundation Trust provider profile (RFS)", "url": "https://www.cqc.org.uk/provider/RFS"}
    ],
    "related": ["Chesterfield Royal Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Chesterfield Royal Hospital NHS Foundation Trust", "General supplies & services — Chesterfield Royal Hospital NHS Foundation Trust", "NHS England"]
}

NEW["Inventories written down — King’s College Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "King’s College Hospital NHS Foundation Trust"}],
    "description": "King's College Hospital NHS FT's £0.59M inventories-written-down line records the IAS 2 net-realisable-value adjustment and obsolescence/expiry write-off of clinical consumables, drugs and surgical supplies across the Denmark Hill campus, the Princess Royal University Hospital (Bromley), Orpington Hospital and Beckenham Beacon. Write-downs are concentrated in expired pharmacy stock (high-cost cancer biologics, transplant immunosuppressants, hepatology specialist drugs), short-shelf-life sterile-services consumables and obsolete implantable devices subject to MHRA field-safety notices.",
    "beneficiaries": "c. 14,000 WTE staff serving a c. 1.5M south London catchment across Lambeth, Southwark, Bromley and Bexley; c. 240,000 ED attendances/yr across Denmark Hill + PRUH ED; c. 165,000 admissions/yr; c. 1.2M outpatient attendances/yr; trust hosts the King's Liver Unit (national tertiary liver-transplant centre) and a major-trauma centre at Denmark Hill.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 chapter 8 — Human Medicines Regulations 2012 — MHRA Yellow Card and Field Safety Corrective Action regime — NHS Act 2006 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.59M"},
        {"label": "Trust scale", "value": "Denmark Hill + PRUH (Bromley) + Orpington + Beckenham Beacon; c. 14,000 WTE; major trauma centre + national liver transplant centre"},
        {"label": "Composition", "value": "Expired pharmacy stock (transplant immunosuppressants, hepatology biologics, cancer drugs) + sterile consumables + MHRA-recalled implants"},
        {"label": "Liver Unit driver", "value": "King's Liver Unit — high-cost specialist immunosuppressants + hepatology drugs (high-cost-drug pass-through; expiry events drive material write-downs)"},
        {"label": "Trauma + transplant exposure", "value": "Major-trauma centre demands held stock of low-utilisation high-cost implants/devices — non-trivial MHRA-recall write-down risk"},
        {"label": "Standard", "value": "IAS 2: inventory at lower of cost and net realisable value; expired/obsolete written down to zero per GAM ch.8"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.55M → 2024-25 £0.59M — high-cost drug volume growth + MHRA recall events"},
        {"label": "South East London ICS", "value": "Member of South East London ICB; collaborative pharmacy stock-pooling with Guy's & St Thomas' + Lewisham & Greenwich"},
        {"label": "Delivery body", "value": "Trust Pharmacy + Sterile Services + Procurement + Theatres + Stock Management + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM + MHRA + NHS Supply Chain + NHSE Specialised Commissioning (transplant + cancer)"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 inventories note; NHSE Commercial team stock-management benchmarks; Carter productivity reports; CQC RJZ"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IAS 2 historic-cost stock loss · Successor: Scan4Safety barcoded inventory + FEFO + EPR-integrated stock at PRUH"}
    ],
    "notes": "King's College Hospital's inventories-written-down line is elevated by two specialist drivers: the King's Liver Unit (UK's largest liver-transplant programme — high-cost immunosuppressants and hepatology biologics often £1k-£10k per dose) and major-trauma centre status (low-utilisation high-cost implants held for emergency need). The trust has historically been in financial deficit and entered NHSE Recovery Support Programme oversight in earlier years; tighter stock controls have driven down the write-down ratio. Scan4Safety barcoded inventory and FEFO controls are the primary mitigation. The 2013 PRUH (Bromley) acquisition initially added stock-control complexity since integrated. MHRA recall notices remain a periodic trigger.",
    "sources": [
        {"publisher": "King’s College Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kch.nhs.uk/about/corporate/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 8 (inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Medicines and Healthcare products Regulatory Agency", "title": "Field Safety Corrective Action notices", "url": "https://www.gov.uk/drug-device-alerts"},
        {"publisher": "NHS England", "title": "Specialised Commissioning — high-cost drugs", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
        {"publisher": "Care Quality Commission", "title": "King’s College Hospital NHS Foundation Trust provider profile (RJZ)", "url": "https://www.cqc.org.uk/provider/RJZ"}
    ],
    "related": ["King’s College Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — Royal Surrey NHS Foundation Trust", "Inventories written down — University Hospitals of North Midlands NHS Trust", "Medicines and Healthcare products Regulatory Agency"]
}

NEW["Lease expenditure — Calderdale and Huddersfield NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
    "description": "Calderdale and Huddersfield NHS FT's £0.58M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across Calderdale Royal Hospital (Halifax — a 2001 PFI build), Huddersfield Royal Infirmary and the trust's community-services portfolio. The trust is on a confirmed New Hospital Programme reconfiguration pathway with a planned new Huddersfield acute hospital and refreshed Calderdale Royal estate.",
    "beneficiaries": "c. 6,000 WTE staff serving a c. 470,000 catchment across Calderdale and Kirklees (Huddersfield, Halifax, Brighouse, Holmfirth); c. 165,000 ED attendances/yr across Calderdale + Huddersfield ED; c. 95,000 admissions/yr; c. 480,000 outpatient attendances/yr; member of West Yorkshire ICS.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.58M"},
        {"label": "Trust scale", "value": "Calderdale Royal Hospital (Halifax — PFI 2001) + Huddersfield Royal Infirmary + community sites; c. 6,000 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical equipment"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "PFI interaction", "value": "Calderdale Royal PFI (2001, c. 35-yr concession with Catalyst Healthcare) — separate PFI/LIFT charge line, but related ancillary leases captured here"},
        {"label": "New Hospital Programme", "value": "Hospitals reconfiguration scheme — new Huddersfield acute build + refreshed Calderdale Royal, NHP cohort (post-2030 delivery)"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.55M → 2024-25 £0.58M — IFRS 16 transition steady-state"},
        {"label": "West Yorkshire ICS", "value": "Member of West Yorkshire ICB; collaborative procurement with Bradford, Mid Yorkshire, Airedale and Leeds"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + DHSC NHP team (planning)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + DHSC NHP + West Yorkshire ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases + PFI notes; NAO PFI Investigation report; NAO NHP reports; CQC RWY inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: post-NHP-build estate consolidation in 2030s"}
    ],
    "notes": "Calderdale and Huddersfield carries a long-running PFI exposure at Calderdale Royal Hospital (Halifax — 2001 NPV-pioneer scheme with Catalyst Healthcare, c. 35-year concession) captured in a separate PFI/LIFT charge line; the lease line here covers ancillary, community and equipment leases below the IFRS 16 ROU threshold. The hospitals reconfiguration scheme (originally 'Right Care Right Time Right Place' — replacement of acute services at Huddersfield plus retention of Calderdale Royal) has been a long-running planning controversy, repeatedly judicially reviewed before NHP confirmation. Until the new Huddersfield build, the trust runs a costly two-site acute model. West Yorkshire ICB pool-fleet and community-premises consolidation is the medium-term mitigation.",
    "sources": [
        {"publisher": "Calderdale and Huddersfield NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cht.nhs.uk/about-us/board-and-governance/publications-and-reports/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — schemes and cohorts", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
        {"publisher": "Care Quality Commission", "title": "Calderdale and Huddersfield NHS Foundation Trust provider profile (RWY)", "url": "https://www.cqc.org.uk/provider/RWY"}
    ],
    "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Calderdale and Huddersfield NHS Foundation Trust", "Establishment costs — Calderdale and Huddersfield NHS Foundation Trust", "Department of Health and Social Care"]
}

NEW["Lease expenditure — Chelsea and Westminster Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
    "description": "Chelsea and Westminster Hospital NHS FT's £0.56M lease line covers IFRS 16 short-term + low-value charges (outside ROU per DHSC GAM ch.7) plus residual operating-lease costs across Chelsea and Westminster Hospital (Fulham Road), West Middlesex University Hospital (Isleworth) and the trust's substantial sexual-health and HIV-services community footprint — 56 Dean Street and the John Hunter Clinic — Europe's largest sexual-health network. The main Chelsea and Westminster building's PFI is captured separately.",
    "beneficiaries": "c. 6,000 WTE staff serving a c. 1.0M north-west and central-west London catchment (Hammersmith & Fulham, Kensington & Chelsea, Westminster, Hounslow, Richmond); c. 250,000 ED attendances/yr across Chelsea + West Mid; c. 130,000 admissions/yr; specialist HIV/sexual-health services serve a national catchment via 56 Dean Street.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.56M"},
        {"label": "Trust scale", "value": "Chelsea and Westminster Hospital (Fulham Road) + West Middlesex University Hospital (Isleworth) + 56 Dean Street + community sites; c. 6,000 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community sexual-health premises + IT + medical equipment"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "PFI interaction", "value": "Chelsea and Westminster Hospital main build is PFI (1990s) — captured in PFI/LIFT charges line, not here"},
        {"label": "Sexual-health network", "value": "56 Dean Street (Soho) + John Hunter Clinic (Chelsea) + 10 Hammersmith Broadway — multiple high-rent central-London leasehold sites"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.42M → 2023-24 c. £0.53M → 2024-25 £0.56M — IFRS 16 transition steady-state + central-London rent uplift"},
        {"label": "North West London ICS", "value": "Member of North West London ICB; cross-trust HIV/sexual-health pathway with Imperial College Healthcare + CNWL"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + commercial landlord counterparties (central London)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + North West London ICB + UKHSA (sexual-health commissioning)"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; UKHSA STI surveillance reports; CQC RQM inspections; 56 Dean Street published activity stats"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: digital-first sexual-health (Sexual Health London, online-prescribing) reduces high-rent footfall premises"}
    ],
    "notes": "Chelsea and Westminster operates the largest sexual-health and HIV outpatient network in Europe — 56 Dean Street (Soho) is one of the highest-volume sexual-health clinics in the world, and the John Hunter Clinic, 10 Hammersmith Broadway and other satellite sites carry premium central-London leasehold rents that drive an above-peer leasehold-cost ratio for community premises. The trust's Chelsea and Westminster main hospital is PFI (1993, with Compass-Bouygues legacy contract) captured in a separate PFI/LIFT charge line. The 2015 acquisition of West Middlesex University Hospital added community sites in Hounslow and Richmond. Digital-first pathways (Sexual Health London online prescribing, home self-test kits) are the medium-term lever to reduce high-rent footfall premises.",
    "sources": [
        {"publisher": "Chelsea and Westminster Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chelwest.nhs.uk/about-us/corporate-information/our-publications"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "UK Health Security Agency", "title": "Sexually transmitted infections and screening surveillance", "url": "https://www.gov.uk/government/statistics/sexually-transmitted-infections-stis-annual-data-tables"},
        {"publisher": "56 Dean Street", "title": "Service activity reports", "url": "https://dean.st/"},
        {"publisher": "Care Quality Commission", "title": "Chelsea and Westminster Hospital NHS Foundation Trust provider profile (RQM)", "url": "https://www.cqc.org.uk/provider/RQM"}
    ],
    "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Chelsea and Westminster Hospital NHS Foundation Trust", "Establishment costs — Chelsea and Westminster Hospital NHS Foundation Trust", "UK Health Security Agency"]
}

NEW["Lease expenditure — York and Scarborough Teaching Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
    "description": "York and Scarborough Teaching Hospitals NHS FT's £0.54M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across York Hospital, Scarborough General Hospital, Bridlington Hospital, Selby War Memorial, Whitby Community Hospital, Malton Hospital and a network of community sites spanning the largest geographical catchment of any acute trust in England.",
    "beneficiaries": "c. 9,000 WTE staff serving a c. 800,000 catchment across York, Scarborough, Ryedale, Whitby, Bridlington, Filey, Selby, Malton and the North Yorkshire Moors / Wolds — a geographically dispersed footprint extending from the M62 to the North Sea coast; c. 200,000 ED attendances/yr; c. 130,000 admissions/yr.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.54M"},
        {"label": "Trust scale", "value": "York Hospital + Scarborough General + Bridlington + Selby + Whitby + Malton + community sites; c. 9,000 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises (highest count of any acute trust) + IT + equipment"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Geography premium", "value": "Largest acute-trust catchment by area in England — drives c. 50+ community-premises occupancies including small market-town and coastal sites"},
        {"label": "Estate condition", "value": "Scarborough General + Bridlington carry significant backlog maintenance; York Hospital partly modernised; Whitby/Malton are old community-hospital estates"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.4M → 2023-24 c. £0.5M → 2024-25 £0.54M — IFRS 16 transition steady-state + community-premises lease uplifts"},
        {"label": "Humber and North Yorkshire ICS", "value": "Member of Humber and North Yorkshire ICB; collaborative delivery with Hull, Northern Lincolnshire, Harrogate"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + ICB community-premises team"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + Humber and North Yorkshire ICB + DHSC NHP (where Scarborough rebuild)"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HSSIB backlog-maintenance reports; CQC RCB inspections; rural-NHS access reports"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: post-Scarborough-rebuild estate consolidation (NHP cohort) + community-premises rationalisation"}
    ],
    "notes": "York and Scarborough Teaching Hospitals covers what is by area the largest catchment of any acute trust in England — from the M62 corridor (Selby) to the East Yorkshire coast (Bridlington, Filey, Scarborough, Whitby) and the North Yorkshire Moors. This drives an unusually high count of small community-hospital and outreach-clinic occupancies, many under the IFRS 16 short-term / low-value exemption and feeding this line. Scarborough General has been a long-running NHP candidate with multiple delays; the trust's deep rurality has brought specific NHSE Recovery Support Programme attention in recent years. Whitby and Malton community hospitals carry historic estate-condition issues. The 2019 merger that brought Scarborough into the trust consolidated previously separate lease portfolios.",
    "sources": [
        {"publisher": "York and Scarborough Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yorkhospitals.nhs.uk/about-our-trust/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — schemes and cohorts", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "Care Quality Commission", "title": "York and Scarborough Teaching Hospitals NHS Foundation Trust provider profile (RCB)", "url": "https://www.cqc.org.uk/provider/RCB"},
        {"publisher": "NHS Confederation", "title": "Humber and North Yorkshire Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
    ],
    "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — York and Scarborough Teaching Hospitals NHS Foundation Trust", "Business rates — York and Scarborough Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
}

NEW["Inventories written down — University Hospitals of North Midlands NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "University Hospitals of North Midlands NHS Trust"}],
    "description": "UHNM's £0.53M inventories-written-down line records the IAS 2 net-realisable-value adjustment and obsolescence/expiry write-off of clinical consumables, drugs and surgical supplies across Royal Stoke University Hospital and County Hospital (Stafford). As a major-trauma centre and tertiary cardiothoracic, neurosciences and renal centre, UHNM holds high-cost specialist inventory (cardiac devices, neurosurgical implants, transplant immunosuppressants, oncology drugs) that drives most write-downs.",
    "beneficiaries": "c. 12,000 WTE staff serving a c. 900,000 Staffordshire and Stoke-on-Trent local catchment plus a tertiary referral population of c. 3M for major trauma, neurosciences, cardiothoracic, oncology and renal services; c. 235,000 ED attendances/yr at Royal Stoke + Stafford ED; c. 145,000 admissions/yr; c. 880,000 outpatient attendances/yr.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 chapter 8 — Human Medicines Regulations 2012 — MHRA Yellow Card and Field Safety Corrective Action regime — NHS Act 2006 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.53M"},
        {"label": "Trust scale", "value": "Royal Stoke University Hospital + County Hospital (Stafford); c. 12,000 WTE; major trauma centre + tertiary cardiothoracic + neurosciences"},
        {"label": "Composition", "value": "Expired pharmacy stock + sterile consumables + MHRA-recalled implants (cardiac devices, neurosurgical implants, transplant drugs)"},
        {"label": "Tertiary specialty driver", "value": "Major trauma + cardiothoracic + neurosciences + renal — high-cost low-utilisation devices held for emergency need (write-down on expiry / obsolescence)"},
        {"label": "Cardiac device exposure", "value": "Royal Stoke is a regional cardiothoracic centre — pacemakers, ICDs, cardiac valves with manufacturer-issued shelf-life and MHRA recall exposure"},
        {"label": "Standard", "value": "IAS 2: inventory at lower of cost and net realisable value; expired/obsolete written down to zero per GAM ch.8"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.4M → 2023-24 c. £0.5M → 2024-25 £0.53M — high-cost device volume growth + MHRA recall events"},
        {"label": "Staffordshire and Stoke-on-Trent ICS", "value": "Member of Staffordshire and Stoke-on-Trent ICB; collaborative pharmacy stock-pooling with Burton (UHDB)"},
        {"label": "Delivery body", "value": "Trust Pharmacy + Sterile Services + Procurement + Theatres + Cardiothoracic + Neurosciences + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM + MHRA + NHS Supply Chain + NHSE Specialised Commissioning"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 inventories note; NHSE Commercial team stock-management benchmarks; Carter productivity reports; CQC RJE"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IAS 2 historic-cost stock loss · Successor: Scan4Safety barcoded inventory + FEFO + EPR-integrated theatre stock"}
    ],
    "notes": "UHNM's inventories-written-down line is shaped by its dual role as a regional acute trust and a tertiary specialist centre. Royal Stoke is a designated major-trauma, regional cardiothoracic and neurosciences centre — these tertiary specialties drive a structurally elevated holding of high-cost low-utilisation cardiac devices (pacemakers, ICDs, valves), neurosurgical implants and tertiary drugs. MHRA field-safety corrective action notices on cardiac devices have been a periodic trigger across the sector. The trust has been in NHSE Recovery Support Programme oversight in recent years; Scan4Safety barcoded inventory and FEFO are part of the recovery plan. UHNM's 2014 merger (UHNS + Mid Staffordshire post-Francis Report) integrated previously separate stock-control regimes.",
    "sources": [
        {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhnm.nhs.uk/about-us/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 8 (inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Medicines and Healthcare products Regulatory Agency", "title": "Field Safety Corrective Action notices", "url": "https://www.gov.uk/drug-device-alerts"},
        {"publisher": "NHS England", "title": "Specialised Commissioning — high-cost drugs and devices", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
        {"publisher": "Care Quality Commission", "title": "University Hospitals of North Midlands NHS Trust provider profile (RJE)", "url": "https://www.cqc.org.uk/provider/RJE"}
    ],
    "related": ["University Hospitals of North Midlands NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — Royal Surrey NHS Foundation Trust", "Inventories written down — King’s College Hospital NHS Foundation Trust", "Medicines and Healthcare products Regulatory Agency"]
}

NEW["Transport (business + patient) — The Princess Alexandra Hospital NHS Trust"] = {
    "aliases": [{"name": "Transport (business + patient)", "parent": "The Princess Alexandra Hospital NHS Trust"}],
    "description": "Princess Alexandra Hospital NHS Trust's £0.51M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between the Hamstel Road main site (Harlow) and community/satellite locations across west Essex and east Hertfordshire, plus contracted non-emergency patient transport (NEPTS) for the Hertfordshire and West Essex ICS catchment. The trust is a confirmed NHP scheme — a single replacement hospital at the Pinnacles for Princess Alexandra is in cohort 1.",
    "beneficiaries": "c. 3,500 WTE staff serving a c. 350,000 catchment across Harlow, Epping Forest, Uttlesford and east Hertfordshire (Bishop's Stortford, Sawbridgeworth borders); c. 100,000 ED attendances/yr at Princess Alexandra; c. 60,000 admissions/yr; c. 280,000 outpatient attendances/yr; serves a small DGH footprint with high commuter-belt cross-flow.",
    "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Transport (business + patient) 2024-25", "value": "£0.51M"},
        {"label": "Trust scale", "value": "Princess Alexandra Hospital (Hamstel Road, Harlow) + community sites; c. 3,500 WTE; small DGH"},
        {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology courier + contracted NEPTS"},
        {"label": "NEPTS provider", "value": "Herts & West Essex framework (NSL / EMED) — retendered against NHSE 2021 NEPTS Review eligibility"},
        {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement spike + indirect April 2025 NIC pass-through"},
        {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
        {"label": "New Hospital Programme", "value": "PAH replacement — single new hospital at the Pinnacles, Harlow; NHP cohort 1 confirmed scheme (target post-2030 delivery)"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.38M → 2023-24 c. £0.48M → 2024-25 £0.51M — strike backfill + fuel pass-through"},
        {"label": "Hertfordshire and West Essex ICS", "value": "Member of Hertfordshire and West Essex ICB; collaborative NEPTS commissioning with West Herts + East and North Herts"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates + NEPTS contractor + EEAST emergency overlap; NHSE Provider Finance + NHSE PTS policy + DHSC + ICB + NHP"},
        {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; Trust ARA 2023-24; CQC RQW inspections; NAO NHP reports"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-Review baseline · Successor: post-Pinnacles rebuild + ICB-wide pool-fleet electrification"}
    ],
    "notes": "Princess Alexandra Hospital is a small DGH on a 1960s estate that has been on the NHP list since 2019 (the Pinnacles new-hospital scheme) and is one of the few remaining cohort 1 commitments — but with NHP delivery slipping post-2030 under the January 2023 reset. Until the new build, the trust runs an ageing single-site estate with significant backlog maintenance. The transport line is dominated by staff mileage (commuter-belt clinical workforce across north London, Hertfordshire and Essex) plus modest community outreach. April 2025 NIC step-up flows indirectly via the Herts & West Essex NEPTS contractor; frozen AMAP rates compress staff mileage. The trust is in a longstanding clinical-services partnership with East and North Hertfordshire NHS Trust for some specialties.",
    "sources": [
        {"publisher": "The Princess Alexandra Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.pah.nhs.uk/about-us/our-publications-and-strategies"},
        {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — schemes and cohorts", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
        {"publisher": "Care Quality Commission", "title": "The Princess Alexandra Hospital NHS Trust provider profile (RQW)", "url": "https://www.cqc.org.uk/provider/RQW"}
    ],
    "related": ["The Princess Alexandra Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — The Princess Alexandra Hospital NHS Trust", "General supplies & services — The Princess Alexandra Hospital NHS Trust", "Department of Health and Social Care"]
}

NEW["Lease expenditure — Wirral University Teaching Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Wirral University Teaching Hospital NHS Foundation Trust"}],
    "description": "Wirral University Teaching Hospital NHS FT's £0.51M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across Arrowe Park Hospital (Upton) and Clatterbridge Hospital (the Wirral acute site, distinct from the Clatterbridge Cancer Centre that operates independently). Wirral's lease line covers community premises across Birkenhead, Wallasey, Bebington, Heswall and West Kirby plus equipment leases.",
    "beneficiaries": "c. 5,300 WTE staff serving a c. 320,000 Wirral peninsula catchment plus referrals from north Wales (Flintshire, Wrexham); c. 145,000 ED attendances/yr at Arrowe Park; c. 75,000 admissions/yr; c. 360,000 outpatient attendances/yr; serves a high-deprivation Birkenhead urban core alongside affluent west-Wirral commuter belt.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.51M"},
        {"label": "Trust scale", "value": "Arrowe Park Hospital (Upton) + Clatterbridge Hospital (acute) + community sites; c. 5,300 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical equipment"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Site distinction", "value": "Wirral UTH Clatterbridge ≠ Clatterbridge Cancer Centre NHS FT (separate trust, co-located on Bebington campus)"},
        {"label": "Estate condition", "value": "Arrowe Park 1980s build with significant backlog maintenance; Clatterbridge older mixed estate"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.38M → 2023-24 c. £0.48M → 2024-25 £0.51M — IFRS 16 transition steady-state"},
        {"label": "Cheshire and Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB; collaborative procurement with Liverpool UH + Mersey & West Lancs"},
        {"label": "Cross-border flow", "value": "North Wales referral inflow (Betsi Cadwaladr UHB) for some specialties — drives community-clinic outreach"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates + landlord counterparties + Wirral Place ICB team; NHSE Provider Finance + DHSC GAM + C&M ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HSSIB backlog-maintenance reports; CQC RBL inspections; NHSE Recovery Support segmentation"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: C&M ICB community-premises rationalisation + potential single-site reconfiguration"}
    ],
    "notes": "Wirral UTH operates a two-site acute model (Arrowe Park + Clatterbridge — the acute Clatterbridge, distinct from the separately-trusted Clatterbridge Cancer Centre also on the Bebington campus) with significant backlog-maintenance pressure on a 1980s Arrowe Park estate. The trust has been in NHSE Recovery Support Programme oversight in recent years. The lease line is dominated by community-premises occupancies serving the dispersed Wirral peninsula plus IT and equipment leases below the IFRS 16 ROU threshold. North Wales cross-border flow (Betsi Cadwaladr UHB referrals) drives outreach-clinic activity but not lease-line cost. Cheshire and Merseyside ICB community-premises rationalisation is the medium-term lever.",
    "sources": [
        {"publisher": "Wirral University Teaching Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wuth.nhs.uk/about-us/governance/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Recovery Support Programme — segmentation framework", "url": "https://www.england.nhs.uk/publication/nhs-system-oversight-framework/"},
        {"publisher": "Care Quality Commission", "title": "Wirral University Teaching Hospital NHS Foundation Trust provider profile (RBL)", "url": "https://www.cqc.org.uk/provider/RBL"},
        {"publisher": "NHS Confederation", "title": "Cheshire and Merseyside Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
    ],
    "related": ["Wirral University Teaching Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Wirral University Teaching Hospital NHS Foundation Trust", "General supplies & services — Wirral University Teaching Hospital NHS Foundation Trust", "Department of Health and Social Care"]
}

NEW["Lease expenditure — Gateshead Health NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Gateshead Health NHS Foundation Trust"}],
    "description": "Gateshead Health NHS FT's £0.49M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across the Queen Elizabeth Hospital (Sheriff Hill, Gateshead), Bensham Hospital and a portfolio of community-services premises across the Gateshead borough. The trust is the host of QE Facilities Ltd, a wholly owned subsidiary that owns and operates significant non-clinical estate — its formation reshaped the trust's lease-cost reporting from c. 2014.",
    "beneficiaries": "c. 4,000 WTE staff serving a c. 200,000 Gateshead borough catchment plus tertiary referrals for some specialties (gynaecological oncology); c. 95,000 ED attendances/yr at QE Hospital; c. 55,000 admissions/yr; c. 280,000 outpatient attendances/yr; serves a high-deprivation Tyneside post-industrial population.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Companies Act 2006 (re QE Facilities Ltd subsidiary)",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.49M"},
        {"label": "Trust scale", "value": "Queen Elizabeth Hospital (Sheriff Hill) + Bensham Hospital + community sites; c. 4,000 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical equipment"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Wholly-owned subsidiary", "value": "QE Facilities Ltd — wholly owned subsidiary providing non-clinical/estates services; intra-group leases captured via consolidation"},
        {"label": "Estate condition", "value": "QE Hospital partly modernised; Bensham older estate (women's & maternity services historic)"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.36M → 2023-24 c. £0.46M → 2024-25 £0.49M — IFRS 16 transition steady-state"},
        {"label": "North East and North Cumbria ICS", "value": "Member of NENC ICB; collaborative pathology + procurement with Newcastle Hospitals, South Tyneside & Sunderland"},
        {"label": "VAT recovery model", "value": "QE Facilities Ltd originally devised partly to optimise VAT recovery on non-clinical services — model replicated by other trusts (Northumbria, etc.)"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates + QE Facilities Ltd + landlord counterparties; NHSE Provider Finance + DHSC GAM + NENC ICB + HMT subsidiary VAT policy"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases + subsidiary notes; NAO Trust subsidiaries reports; CQC RR7 inspections; NHS Providers subsidiary briefings"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: NENC ICB community-premises rationalisation post HMT 2018 subsidiary regime"}
    ],
    "notes": "Gateshead Health was an early adopter of the wholly-owned subsidiary model — QE Facilities Ltd, formed in 2014, provides non-clinical estates and facilities services to the trust and other NHS bodies and was widely cited as a model (and political controversy) for the broader NHS subsidiary wave of 2017-18. The HMT direction of 2018 substantially closed off the VAT-recovery rationale for new subsidiary formations, but legacy entities like QE Facilities continue to operate and shape intra-group lease and service charges captured via consolidation. The lease line itself covers community premises, IT and equipment leases below the IFRS 16 ROU threshold. NENC ICB community-premises rationalisation is the medium-term lever alongside NHS net-zero estate decarbonisation.",
    "sources": [
        {"publisher": "Gateshead Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gateshealth.nhs.uk/about-us/our-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "Guidance on NHS wholly-owned subsidiaries (2018 direction)", "url": "https://www.gov.uk/government/publications/managing-public-money"},
        {"publisher": "Care Quality Commission", "title": "Gateshead Health NHS Foundation Trust provider profile (RR7)", "url": "https://www.cqc.org.uk/provider/RR7"},
        {"publisher": "NHS Providers", "title": "NHS subsidiaries explainer", "url": "https://nhsproviders.org/"}
    ],
    "related": ["Gateshead Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Gateshead Health NHS Foundation Trust", "General supplies & services — Gateshead Health NHS Foundation Trust", "HM Treasury"]
}

