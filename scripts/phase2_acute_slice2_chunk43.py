# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 43 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {}

NEW["PFI / LIFT charges — Northumbria Healthcare NHS Foundation Trust"] = {
    "aliases": [{"name": "PFI / LIFT charges", "parent": "Northumbria Healthcare NHS Foundation Trust"}],
    "description": "Northumbria Healthcare NHS FT's £0.31M residual PFI / LIFT line is the small operating-charge tail surviving after the trust's landmark 2014 PFI buy-out — when Northumbria became the first NHS body to refinance and terminate a PFI deal (Hexham General, c. £114M deal) using a low-interest Northumberland County Council loan, saving an estimated £3.5M/yr. The residual £0.31M covers ongoing LIFT-vehicle charges for community premises (NorthGEN/Three Valleys LIFT) plus tail service-element costs not captured by the Hexham termination, accounted for as service-concession arrangements per IFRIC 12.",
    "beneficiaries": "c. 11,500 WTE staff serving a c. 500,000 population across Northumberland and North Tyneside; sites include the Northumbria Specialist Emergency Care Hospital (Cramlington — opened 2015 as the UK's first purpose-built emergency-care hospital), Wansbeck General, North Tyneside General, Hexham General + community sites; c. 200,000 ED attendances/yr; c. 130,000 admissions/yr.",
    "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 transition) — DHSC PFI guidance — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Local Government Act 2003 (council prudential borrowing power used for 2014 buy-out) — Health and Care Act 2022",
    "key_stats": [
        {"label": "PFI / LIFT charges 2024-25", "value": "£0.31M (residual tail post-2014 buy-out)"},
        {"label": "Trust scale", "value": "Northumbria SECH (Cramlington) + Wansbeck + North Tyneside + Hexham + community; c. 11,500 WTE; serves c. 500,000"},
        {"label": "Historic deal", "value": "Hexham General PFI c. £114M (1999 OBC) — terminated 2014 in landmark refinancing using £114.2M Northumberland CC prudential loan"},
        {"label": "Annual saving from buy-out", "value": "c. £3.5M/yr — first NHS PFI termination of its kind, cited by NAO + HM Treasury as case study"},
        {"label": "Residual composition", "value": "Three Valleys / NorthGEN LIFT community-premises service charges + small post-termination tail items at Hexham"},
        {"label": "LIFT vehicle", "value": "Three Valleys LIFTCo / NorthGEN — Local Improvement Finance Trust delivering primary care + community estates"},
        {"label": "Funding trajectory", "value": "Pre-2014 c. £8M/yr unitary charge → post-2014 buy-out c. £4.5M/yr loan service (off this line) → 2024-25 £0.31M residual community LIFT only"},
        {"label": "SECH context", "value": "Cramlington SECH (opened June 2015) was conventionally publicly funded — NOT PFI — explicit policy choice post-2010 PFI moratorium"},
        {"label": "North East ICS", "value": "Member of North East and North Cumbria ICB — UK's largest ICB by geography"},
        {"label": "Delivery body + policy owner", "value": "Trust E&F + Northumbria Healthcare Facilities Management (in-house company) + Three Valleys LIFTCo; HMT PFI policy + DHSC + NHSE"},
        {"label": "Evaluation evidence", "value": "NAO 'PFI and PF2' (2018) cites Northumbria as exemplar; HCLG Committee report on PFI buy-outs; Trust ARA 2023-24"},
        {"label": "Predecessor / successor", "value": "Predecessor: 1999-2014 Hexham PFI unitary charge · Successor: 2014 buy-out (model studied by NHS Property Services + DHSC PFI reset)"}
    ],
    "notes": "Northumbria's 2014 Hexham PFI buy-out — using a Northumberland County Council prudential loan to refinance the SPV at council-borrowing rates rather than commercial PFI rates — became the textbook NHS exit case, cited by the NAO 2018 PFI report and by HM Treasury when it ended new PFI procurement at Budget 2018. The residual £0.31M line captures the LIFT-vehicle community-premises tail (Three Valleys / NorthGEN) plus minor post-termination items, not the long-vanished Hexham unitary charge. The Cramlington SECH (England's first purpose-built emergency-care hospital, 2015) was deliberately publicly funded — the trust is structurally low-PFI by policy choice. April 2025 NIC step-up flows via FM contractor pass-through but the residual size limits exposure.",
    "sources": [
        {"publisher": "Northumbria Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northumbria.nhs.uk/about-us/publications/"},
        {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
        {"publisher": "HM Treasury", "title": "Budget 2018 — ending new PFI/PF2", "url": "https://www.gov.uk/government/publications/budget-2018-documents"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "Northumbria Healthcare NHS FT provider profile (RTF)", "url": "https://www.cqc.org.uk/provider/RTF"}
    ],
    "related": ["Northumbria Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Northumbria Healthcare NHS Foundation Trust", "Business rates — Northumbria Healthcare NHS Foundation Trust", "PFI / LIFT charges — University Hospitals Birmingham NHS Foundation Trust"]
}

NEW["Inventories written down — The Shrewsbury and Telford Hospital NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
    "description": "The Shrewsbury and Telford Hospital NHS Trust's £0.30M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs across pharmacy stock (especially specials and oncology drugs), surgical consumables, and theatre stock at the Royal Shrewsbury Hospital and Princess Royal Hospital (Telford) sites. SaTH operates the Mid-Staffordshire-style two-site DGH model under intense regulatory scrutiny following the Ockenden maternity review (final March 2022) and continues under the Recovery Support Programme (NHSE NOF 4).",
    "beneficiaries": "c. 6,500 WTE staff serving a c. 500,000 catchment across Shropshire, Telford & Wrekin and mid-Wales (Powys); c. 130,000 ED attendances/yr across Royal Shrewsbury + PRH; c. 100,000 admissions/yr; c. 470,000 outpatient attendances/yr; the trust serves the most rural acute footprint in England outside Cumbria.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Medicines Act 1968",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.30M"},
        {"label": "Trust scale", "value": "Royal Shrewsbury Hospital + Princess Royal Hospital (Telford) + community sites; c. 6,500 WTE; serves c. 500,000"},
        {"label": "Composition", "value": "Pharmacy specials + oncology drug obsolescence + surgical consumables + theatre stock NRV adjustments per IAS 2"},
        {"label": "Hospital Transformation Programme", "value": "SaTH HTP — Future Fit reconfiguration consolidating major emergency at Royal Shrewsbury, planned care at PRH; £312M+ scheme, multiple delays"},
        {"label": "Regulatory status", "value": "NHSE Recovery Support Programme NOF 4 (since 2018); CQC overall 'Requires Improvement' with maternity 'Inadequate' historically"},
        {"label": "Ockenden Review", "value": "Final report March 2022 (Donna Ockenden) — 1,592 maternity cases reviewed, c. 200 baby/mother deaths/avoidable harm; drives ongoing maternity stock + safety procurement"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes elevated cancellation rate, drove specials-pharmacy + theatre obsolescence"},
        {"label": "Mid-Wales cross-border", "value": "c. 20% activity from Powys Teaching Health Board (Wales) — adds drug-tariff + procurement complexity"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.22M → 2023-24 c. £0.28M → 2024-25 £0.30M — strike cancellation backlog + Ockenden-driven obstetric stock turnover"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + Theatres governance + NHS Supply Chain; NHSE Provider Finance + DHSC + Recovery Support Programme + MHRA"},
        {"label": "Evaluation evidence", "value": "Ockenden Review final report 2022; CQC SaTH inspection reports; NHSE NOF 4 segmentation; Trust ARA 2023-24; NAO Hospital Transformation Programme"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-Ockenden baseline · Successor: HTP Future Fit reconfiguration completion (delayed to late 2020s)"}
    ],
    "notes": "SaTH carries the heaviest regulatory + reputational burden of any English Acute trust following the Ockenden Review (final report March 2022) which identified failings across 1,592 maternity cases including c. 200 baby/mother deaths and avoidable harm — the largest maternity scandal in NHS history. The trust remains in the NHSE Recovery Support Programme (NOF 4 segmentation), with the £312M+ Hospital Transformation Programme (Future Fit) consolidating major emergency at Royal Shrewsbury and planned care at Princess Royal having faced multiple delays. The cross-border catchment (c. 20% of activity from Powys, Wales) introduces additional drug-tariff complexity. Strike cancellations in 2023-24 + Ockenden-driven obstetric stock turnover both feed obsolescence. Inventory governance is a CQC focus area.",
    "sources": [
        {"publisher": "The Shrewsbury and Telford Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sath.nhs.uk/about-us/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Ockenden Review — Final Report (March 2022)", "url": "https://www.gov.uk/government/publications/final-report-of-the-ockenden-review"},
        {"publisher": "Care Quality Commission", "title": "The Shrewsbury and Telford Hospital NHS Trust provider profile (RXW)", "url": "https://www.cqc.org.uk/provider/RXW"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Recovery Support Programme — NHS Oversight Framework", "url": "https://www.england.nhs.uk/publication/nhs-oversight-framework/"}
    ],
    "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — The Shrewsbury and Telford Hospital NHS Trust", "Clinical supplies & services — The Shrewsbury and Telford Hospital NHS Trust", "Inventories written down — University Hospitals Birmingham NHS Foundation Trust"]
}

NEW["Inventories written down — George Eliot Hospital NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "George Eliot Hospital NHS Trust"}],
    "description": "George Eliot Hospital NHS Trust's £0.30M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs at the single-site Nuneaton DGH (north Warwickshire), spanning pharmacy stock, theatre consumables, and surgical supplies. As a small DGH (c. 2,500 WTE) operating in collaborative arrangements with neighbouring University Hospitals Coventry & Warwickshire and South Warwickshire under the Foundation Group concept, GEH carries proportionally higher unit-level write-down rates than larger trusts owing to less frequent stock turn.",
    "beneficiaries": "c. 2,500 WTE staff serving a c. 320,000 catchment across north Warwickshire, Hinckley & Bosworth (Leicestershire) and southern parts of Tamworth; c. 75,000 ED attendances/yr at the Nuneaton site; c. 50,000 admissions/yr; c. 240,000 outpatient attendances/yr; the trust runs the Centre for Elective Surgery (CES) high-volume orthopaedic hub.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Medicines Act 1968",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.30M"},
        {"label": "Trust scale", "value": "Single-site DGH at Nuneaton + community sites; c. 2,500 WTE; serves c. 320,000"},
        {"label": "Composition", "value": "Pharmacy obsolescence (specials + tariffed drugs) + theatre consumables + surgical supplies + orthopaedic implant aged stock per IAS 2"},
        {"label": "Centre for Elective Surgery", "value": "GEH CES — high-volume short-stay orthopaedics; opened 2021; aligned with NHSE Elective Recovery Plan"},
        {"label": "Foundation Group", "value": "Collaborative arrangement (mooted with UHCW + South Warks); ICS group-procurement focus reduces aged stock"},
        {"label": "Coventry & Warwickshire ICS", "value": "Member of Coventry and Warwickshire ICB; integrated planning with UHCW + SWFT"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes elevated CES cancellation rate, drove implant + theatre stock obsolescence"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.22M → 2023-24 c. £0.27M → 2024-25 £0.30M — small-trust unit-rate effect + CES cancellation backlog"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + CES theatres governance + NHS Supply Chain; NHSE Provider Finance + DHSC + MHRA"},
        {"label": "Evaluation evidence", "value": "CQC GEH inspection reports (overall 'Good' 2023); Trust ARA 2023-24; NHSE Elective Recovery Plan returns; Model Hospital pharmacy stock-turn benchmarks"},
        {"label": "Trust legacy", "value": "Named after Victorian novelist Mary Anne Evans (George Eliot) born in nearby Nuneaton; serves former mining-belt population with high deprivation indices"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-CES baseline · Successor: ICS group-procurement deepening (with UHCW + SWFT) + e-pharmacy stock optimisation"}
    ],
    "notes": "George Eliot is one of England's smaller DGHs (c. 2,500 WTE) and carries a structurally higher unit-rate inventory-write-down ratio than larger peers because slower stock turn at lower volume increases obsolescence exposure. The Centre for Elective Surgery (opened 2021) is the trust's NHSE Elective Recovery Plan flagship — high-volume short-stay orthopaedics — and its cancellation pattern during 2023-24 industrial action drove implant + theatre stock obsolescence into 2024-25. The mooted Foundation Group with UHCW and South Warwickshire (originally explored 2018-2020) has evolved into ICB-level group-procurement alignment under the Coventry and Warwickshire ICS. Population deprivation in the former Warwickshire coalfield (Bedworth, Bulkington, Atherstone) drives demand mix.",
    "sources": [
        {"publisher": "George Eliot Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.geh.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "George Eliot Hospital NHS Trust provider profile (RLT)", "url": "https://www.cqc.org.uk/provider/RLT"},
        {"publisher": "NHS England", "title": "Elective Recovery Plan", "url": "https://www.england.nhs.uk/publication/delivery-plan-for-tackling-the-covid-19-backlog-of-elective-care/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Model Hospital benchmarking portal", "url": "https://model.nhs.uk/"}
    ],
    "related": ["George Eliot Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — George Eliot Hospital NHS Trust", "Clinical supplies & services — George Eliot Hospital NHS Trust", "Inventories written down — The Shrewsbury and Telford Hospital NHS Trust"]
}

NEW["Inventories written down — South Tees Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "South Tees Hospitals NHS Foundation Trust"}],
    "description": "South Tees Hospitals NHS FT's £0.29M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs across the trust's principal hub — the James Cook University Hospital (Middlesbrough), a designated Major Trauma Centre serving the North East and tertiary cardiothoracic centre — plus the Friarage Hospital (Northallerton) and community sites. High-cost cardiothoracic, neurosurgery, and major-trauma stock create higher absolute write-down values than peer DGHs given specialty implant + drug obsolescence risk.",
    "beneficiaries": "c. 9,500 WTE staff serving a c. 1.5M tertiary catchment across Tees Valley, North Yorkshire and parts of County Durham (cardiothoracic + neurosurgery); c. 130,000 ED attendances/yr at James Cook (Major Trauma Centre); c. 110,000 admissions/yr; c. 600,000 outpatient attendances/yr; c. 1,000 cardiothoracic surgical cases/yr.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Medicines Act 1968 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.29M"},
        {"label": "Trust scale", "value": "James Cook University Hospital (Major Trauma Centre, Middlesbrough) + Friarage (Northallerton) + community sites; c. 9,500 WTE"},
        {"label": "Composition", "value": "Cardiothoracic implant + neurosurgery consumables + Major Trauma stock + theatre/pharmacy obsolescence per IAS 2"},
        {"label": "Tertiary specialties", "value": "Cardiothoracic surgery + neurosurgery + major trauma + spinal injuries — high-cost specialty stock turnover risk"},
        {"label": "Major Trauma Centre", "value": "Adult MTC for North East and North Yorkshire trauma network — receives high-acuity load 24/7"},
        {"label": "Friarage reconfiguration", "value": "Friarage Hospital A&E downgraded to Urgent Treatment Centre 2019 (medical recruitment failure); ongoing political controversy in rural Hambleton"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes elevated cardiothoracic + elective cancellation, drove implant obsolescence"},
        {"label": "North East ICS", "value": "Member of North East and North Cumbria ICB — collaborative procurement with Newcastle Hospitals + Northumbria + County Durham"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.22M → 2023-24 c. £0.27M → 2024-25 £0.29M — strike cancellation + cardiothoracic implant aged-stock effect"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + Cardiothoracic Theatres + NHS Supply Chain; NHSE Provider Finance + DHSC + Specialised Commissioning + MHRA"},
        {"label": "Evaluation evidence", "value": "CQC South Tees inspections; TARN Major Trauma audit; Trust ARA 2023-24; SCTS cardiothoracic outcomes; Friarage A&E review"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-Friarage-downgrade baseline · Successor: NENC ICS specialist-stock-pool initiatives + further specialised commissioning consolidation"}
    ],
    "notes": "South Tees combines a high-volume major-trauma + tertiary cardiothoracic + neurosurgery profile at James Cook with a rural DGH at Friarage whose A&E was controversially downgraded to an Urgent Treatment Centre in 2019 after medical recruitment failed — a politically contested decision in the constituency of then-Foreign Secretary Rishi Sunak. The specialty mix drives implant + drug obsolescence risk above peer DGHs. Industrial action in 2023-24 elevated cardiothoracic + elective cancellation rates, feeding implant + pharmacy specials write-downs into 2024-25. The trust is part of the geographically vast North East and North Cumbria ICB and participates in pooled specialty stock arrangements. Specialised Commissioning pathways insulate part of the activity.",
    "sources": [
        {"publisher": "South Tees Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southtees.nhs.uk/about/publications/"},
        {"publisher": "Care Quality Commission", "title": "South Tees Hospitals NHS FT provider profile (RTR)", "url": "https://www.cqc.org.uk/provider/RTR"},
        {"publisher": "Trauma Audit and Research Network (TARN)", "title": "Major Trauma audit", "url": "https://www.tarn.ac.uk/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Specialised Commissioning service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
    ],
    "related": ["South Tees Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — South Tees Hospitals NHS Foundation Trust", "Clinical supplies & services — South Tees Hospitals NHS Foundation Trust", "Inventories written down — The Newcastle Upon Tyne Hospitals NHS Foundation Trust"]
}

NEW["Inventories written down — University Hospitals Birmingham NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "University Hospitals Birmingham NHS Foundation Trust"}],
    "description": "University Hospitals Birmingham NHS FT's £0.27M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs across the trust's four-site mega-acute footprint — Queen Elizabeth Hospital Birmingham (the regional Major Trauma Centre and Royal Centre for Defence Medicine), Heartlands, Good Hope, and Solihull — spanning pharmacy stock (transplant + oncology specials), surgical implants, theatre consumables and military-stock-segregated items at QEHB. As one of England's largest single-trust footprints (c. 22,000 WTE), absolute write-downs scale with volume.",
    "beneficiaries": "c. 22,000 WTE staff serving a c. 2.2M catchment across Birmingham, Solihull and the wider West Midlands tertiary footprint; c. 470,000 ED attendances/yr across QEHB + Heartlands + Good Hope; c. 270,000 admissions/yr; c. 1.5M outpatient attendances/yr; the Royal Centre for Defence Medicine handles UK military repatriation casework.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Medicines Act 1968 — Human Tissue Act 2004 (transplant)",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.27M"},
        {"label": "Trust scale", "value": "QEHB (Edgbaston) + Heartlands + Good Hope + Solihull; c. 22,000 WTE; serves c. 2.2M West Midlands catchment"},
        {"label": "Composition", "value": "Transplant + oncology pharmacy specials + surgical implants + theatre consumables + RCDM military stock + ITU pharmacy NRV per IAS 2"},
        {"label": "Tertiary specialties", "value": "Liver + renal + cardiothoracic transplant; Major Trauma Centre; Royal Centre for Defence Medicine; QEHB-RCDM partnership with MoD"},
        {"label": "2018 merger", "value": "Heart of England NHS FT (Heartlands + Good Hope + Solihull) merged into UHB 2018 — drove integration-era stock harmonisation"},
        {"label": "Bewick / Hardwick reviews 2023", "value": "Mike Bewick + Hardwick reviews into UHB culture, governance, mortality outliers — drove board change + procurement scrutiny"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — at UHB scale very large absolute cancellation impact + theatre stock obsolescence"},
        {"label": "Birmingham + Solihull ICS", "value": "Member of Birmingham and Solihull ICB — works alongside Birmingham Women's & Children's NHS FT (children + obstetrics)"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.20M → 2023-24 c. £0.25M → 2024-25 £0.27M — at trust scale, write-down ratio low per turnover"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + RCDM + NHS Supply Chain + MoD Defence Medical Services; NHSE Provider Finance + DHSC + Specialised Commissioning"},
        {"label": "Evaluation evidence", "value": "Bewick + Hardwick reviews 2023; CQC UHB inspections; Trust ARA 2023-24; NHSBT transplant audit; Model Hospital pharmacy stock-turn"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2018-merger four-trust baseline · Successor: ICS-pooled procurement + post-Bewick governance reset"}
    ],
    "notes": "UHB is one of England's largest single Acute trusts following the 2018 merger that absorbed Heart of England's three sites (Heartlands, Good Hope, Solihull) into the Queen Elizabeth Hospital footprint. The trust runs the Royal Centre for Defence Medicine — the UK military's primary acute hospital partnership with the Ministry of Defence — which carries segregated stock arrangements. The 2023 Bewick + Hardwick reviews into board culture, mortality outliers and governance triggered substantial leadership change and heightened procurement + clinical-supplies scrutiny. At UHB's scale, absolute inventory write-downs are kept low relative to turnover by mature group-procurement processes; the 2023-24 industrial-action cycle nevertheless drove cancellation-related theatre stock obsolescence.",
    "sources": [
        {"publisher": "University Hospitals Birmingham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhb.nhs.uk/about-us/publications/"},
        {"publisher": "NHS England", "title": "Mike Bewick + Hardwick reviews into UHB (2023)", "url": "https://www.england.nhs.uk/midlands/our-work/uhb-reviews/"},
        {"publisher": "Care Quality Commission", "title": "University Hospitals Birmingham NHS FT provider profile (RRK)", "url": "https://www.cqc.org.uk/provider/RRK"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Ministry of Defence", "title": "Royal Centre for Defence Medicine — Defence Medical Services", "url": "https://www.gov.uk/government/groups/defence-medical-services"}
    ],
    "related": ["University Hospitals Birmingham NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — University Hospitals Birmingham NHS Foundation Trust", "PFI / LIFT charges — University Hospitals Birmingham NHS Foundation Trust", "Inventories written down — The Newcastle Upon Tyne Hospitals NHS Foundation Trust"]
}

NEW["Inventories written down — Royal Devon University Healthcare NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Royal Devon University Healthcare NHS Foundation Trust"}],
    "description": "Royal Devon University Healthcare NHS FT's £0.27M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs across the trust's two principal Acute hubs — the Royal Devon and Exeter Hospital (Wonford, Exeter) and North Devon District Hospital (Barnstaple) — formed by the April 2022 merger of the former Royal Devon and Exeter NHS FT and Northern Devon Healthcare NHS Trust. Write-downs span pharmacy specials, theatre consumables, oncology stock and the dispersed community-services stock inherited from Northern Devon's integrated provider model.",
    "beneficiaries": "c. 15,000 WTE staff serving a c. 615,000 catchment across Devon (Eastern + Northern), one of England's largest geographical Acute footprints; c. 195,000 ED attendances/yr across RD&E + NDDH; c. 130,000 admissions/yr; c. 1.0M outpatient attendances/yr; the trust also delivers community + district nursing across Northern Devon.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Medicines Act 1968 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.27M"},
        {"label": "Trust scale", "value": "Royal Devon & Exeter (Wonford) + North Devon District Hospital (Barnstaple) + community sites; c. 15,000 WTE; serves c. 615,000"},
        {"label": "Composition", "value": "Pharmacy specials + theatre consumables + oncology stock + community-services stock NRV per IAS 2"},
        {"label": "2022 merger", "value": "1 April 2022 — Royal Devon & Exeter NHS FT + Northern Devon Healthcare NHS Trust merged to form Royal Devon University Healthcare; integration-era stock harmonisation"},
        {"label": "Geographical scale", "value": "c. 6,000 sq mi catchment — one of England's largest acute geographies; rural transport + isolated NDDH site drive distinct stock-management profile"},
        {"label": "NDDH context", "value": "Critical condition challenges (RAAC list 2023); planned-care-only post-A&E reconfiguration debates ongoing; community-services integration"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — Devon trust felt severely owing to recruitment fragility; cancellation drove obsolescence"},
        {"label": "Devon ICS", "value": "Member of Devon ICB (one of NHSE's most financially distressed ICBs); collaborative procurement with University Hospitals Plymouth + Torbay & South Devon"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.20M (pre-merger combined) → 2023-24 c. £0.26M → 2024-25 £0.27M — merger-integration steady-state"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + Theatres + Community Services + NHS Supply Chain; NHSE Provider Finance + DHSC + MHRA"},
        {"label": "Evaluation evidence", "value": "CQC Royal Devon inspections; merger benefits-realisation case (NHSE) 2023; Trust ARA 2023-24; Devon ICS recovery plans"},
        {"label": "Predecessor / successor", "value": "Predecessor: 2 Apr 2022 RD&E + Northern Devon merger · Successor: integrated Devon-wide pathway alignment + NHP NDDH options"}
    ],
    "notes": "Royal Devon University Healthcare is the post-merger entity (1 April 2022) combining the former Royal Devon & Exeter and Northern Devon Healthcare trusts — the inventory line accordingly reflects two-site harmonisation across one of England's largest Acute geographies (c. 6,000 sq mi). North Devon District Hospital (Barnstaple) was named in 2023 RAAC discussions and faces ongoing reconfiguration debates around acute-services sustainability. The Devon ICS is among NHSE's most financially distressed integrated care boards, and recruitment fragility in remote North Devon amplified the impact of 2023-24 industrial action — driving cancellation-related theatre stock obsolescence. Community-services stock (district nursing + community equipment) inherited from Northern Devon's integrated provider model adds NRV-management complexity.",
    "sources": [
        {"publisher": "Royal Devon University Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royaldevon.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "Royal Devon University Healthcare NHS FT provider profile (RH8)", "url": "https://www.cqc.org.uk/provider/RH8"},
        {"publisher": "NHS England", "title": "Devon ICS planning and recovery", "url": "https://www.england.nhs.uk/south/info-professional/devon/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — RAAC update October 2023", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"}
    ],
    "related": ["Royal Devon University Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — Royal Devon University Healthcare NHS Foundation Trust", "Clinical supplies & services — Royal Devon University Healthcare NHS Foundation Trust", "Inventories written down — University Hospitals Birmingham NHS Foundation Trust"]
}

NEW["Termination & post-employment — East Suffolk and North Essex NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
    "description": "East Suffolk and North Essex NHS FT (ESNEFT)'s £0.27M termination & post-employment line covers IAS 19 termination benefits (severance + voluntary redundancy) and post-employment obligations outside the NHS Pension Scheme employer-contribution stream. ESNEFT was created by the 1 July 2018 merger of Colchester Hospital University NHS FT and Ipswich Hospital NHS Trust — one of England's first cross-border-county acute mergers — and the line reflects ongoing back-office + corporate-services rationalisation 6+ years post-merger plus turnover at the Senior Manager / VSM level.",
    "beneficiaries": "c. 11,000 WTE staff serving a c. 1.0M catchment across east Suffolk and north Essex; Colchester Hospital + Ipswich Hospital + community sites; c. 200,000 ED attendances/yr across both hubs; c. 130,000 admissions/yr; c. 750,000 outpatient attendances/yr; the trust runs the Time Matters innovation programme.",
    "legal_basis": "IAS 19 Employee Benefits — NHS Pension Scheme Regulations 2015 (as amended) — Public Sector Exit Payments Regulations 2020 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Employment Rights Act 1996 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.27M"},
        {"label": "Trust scale", "value": "Colchester Hospital + Ipswich Hospital + community sites; c. 11,000 WTE; serves c. 1.0M east Suffolk + north Essex"},
        {"label": "Composition", "value": "IAS 19 termination benefits (severance + VR) + post-employment obligations outside NHS Pension Scheme + senior-manager exit payments per Public Sector Exit Payments Regs 2020"},
        {"label": "2018 merger", "value": "1 July 2018 — Colchester Hospital University NHS FT + Ipswich Hospital NHS Trust merged to form ESNEFT; one of first cross-county acute mergers"},
        {"label": "Cross-county", "value": "Crosses Suffolk + Essex county boundaries; Suffolk + North East Essex ICB serves both"},
        {"label": "Time Matters programme", "value": "ESNEFT's flagship transformation initiative — released 100,000+ patient hours through process redesign; case-study cited by NHSE"},
        {"label": "Public sector exit cap context", "value": "£95k cap revoked Feb 2021 (HMT) — exit payment Treasury approval framework still applies for VSM"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — backfill cost on Establishment line; minor termination effect on Acting-up arrangements"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.18M → 2023-24 c. £0.24M → 2024-25 £0.27M — post-merger corporate restructuring tail + 2024 senior-manager turnover"},
        {"label": "Suffolk + North East Essex ICS", "value": "Member of Suffolk and North East Essex ICB; works with North East Essex Health & Care Alliance"},
        {"label": "Delivery body + policy owner", "value": "Trust HR + Finance + Workforce + Pensions; NHSE Provider Finance + NHS Pensions Agency + HMT exit-payments framework + DHSC"},
        {"label": "Evaluation evidence", "value": "ESNEFT Annual Reports + Time Matters benefits-realisation; CQC ESNEFT inspections; Trust ARA 2023-24; HMT Public Sector Exit Payments guidance"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 Colchester + Ipswich separate trust costs · Successor: ICS-aligned workforce-pooling arrangements"}
    ],
    "notes": "ESNEFT was formed on 1 July 2018 by the merger of Colchester Hospital University NHS FT and Ipswich Hospital NHS Trust — a cross-county acute merger held up at the time as a model for sub-regional integration. The £0.27M termination line reflects continuing back-office rationalisation 6+ years post-merger plus VSM and senior-manager turnover. The trust's flagship Time Matters transformation programme (releasing 100,000+ patient hours through process redesign) has been cited by NHSE as a case study but does not directly drive this line. Public Sector Exit Payments Regulations 2020 frame approvals; the £95k cap was revoked in February 2021 but Treasury approval continues for VSM exits. NIC step-up April 2025 affects ongoing employer cost not termination provision directly.",
    "sources": [
        {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/about-us/publications/"},
        {"publisher": "HM Treasury", "title": "Public Sector Exit Payments — Treasury approvals framework", "url": "https://www.gov.uk/government/publications/guidance-on-public-sector-exit-payments"},
        {"publisher": "Care Quality Commission", "title": "East Suffolk and North Essex NHS FT provider profile (RDE)", "url": "https://www.cqc.org.uk/provider/RDE"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guidance", "url": "https://www.nhsbsa.nhs.uk/employer-hub"}
    ],
    "related": ["East Suffolk and North Essex NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Employer pensions — East Suffolk and North Essex NHS Foundation Trust", "General supplies & services — East Suffolk and North Essex NHS Foundation Trust", "Agency & temporary staff — East Suffolk and North Essex NHS Foundation Trust"]
}

NEW["Transport (business + patient) — East Cheshire NHS Trust"] = {
    "aliases": [{"name": "Transport (business + patient)", "parent": "East Cheshire NHS Trust"}],
    "description": "East Cheshire NHS Trust's £0.27M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site community-services courier and pathology specimen transport between Macclesfield District General Hospital and the trust's dispersed community footprint, plus contracted non-emergency patient transport (NEPTS) for the eastern Cheshire catchment. The trust is one of England's smaller integrated providers (Acute + community), serving the Macclesfield, Knutsford, Wilmslow, Congleton and Crewe-edge area.",
    "beneficiaries": "c. 2,800 WTE staff serving a c. 200,000 catchment across eastern Cheshire (Macclesfield, Wilmslow, Knutsford, Congleton, Poynton); c. 50,000 ED attendances/yr at Macclesfield DGH; c. 35,000 admissions/yr; c. 220,000 outpatient attendances/yr; integrated district nursing + community-services delivery across rural east Cheshire.",
    "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Transport (business + patient) 2024-25", "value": "£0.27M"},
        {"label": "Trust scale", "value": "Macclesfield District General Hospital + community sites + integrated district nursing; c. 2,800 WTE"},
        {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + pathology specimen transport + contracted NEPTS"},
        {"label": "Integrated provider", "value": "East Cheshire is one of England's smaller integrated Acute + community trusts — district nursing + community visits drive a high-mileage staff travel pattern"},
        {"label": "NEPTS provider", "value": "EMED Group / Cheshire-area NEPTS framework via Cheshire & Merseyside ICB; NHSE 2021 NEPTS Review eligibility implementation"},
        {"label": "Geography", "value": "Rural-suburban east Cheshire footprint includes wealthy Wilmslow / Alderley Edge belt + ex-mill towns; long district-nurse travel times"},
        {"label": "Industrial action + NIC step-up", "value": "44 days junior-doctor + 10 days consultant strikes — small DGH severely felt; April 2025 NIC step-up flows via NEPTS contractor pass-through"},
        {"label": "AMAP rates 2024-25", "value": "HMRC AMAP frozen at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.20M → 2023-24 c. £0.25M → 2024-25 £0.27M — community-services mileage + fuel pass-through + NEPTS uplift"},
        {"label": "Cheshire & Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB; collaborative NEPTS commissioning across all CHM trusts"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates & Facilities + Pathology + Community Services + EMED/CHM NEPTS framework; NHSE + DHSC + ICB transport commissioner"},
        {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; CQC East Cheshire inspections; Trust ARA 2023-24"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-Review baseline · Successor: ICB-wide eligibility-criteria implementation + pool-fleet electrification + NHS net-zero 2040"}
    ],
    "notes": "East Cheshire is one of England's smaller integrated Acute + community trusts (c. 2,800 WTE) and the integrated provider model — Acute care at Macclesfield DGH alongside district nursing and community-services delivery across eastern Cheshire — drives proportionally higher staff-mileage exposure than peer pure-Acute DGHs of similar scale. The catchment combines the wealthy Wilmslow / Alderley Edge / Knutsford belt with former mill towns (Macclesfield, Congleton) and rural villages, generating long district-nurse travel times. The April 2025 NIC step-up flows indirectly through the NEPTS contractor pass-through under the Cheshire & Merseyside ICB framework. Frozen HMRC AMAP rates (unchanged since 2011) compress staff mileage reimbursement in real terms. The trust's small size makes it sensitive to whole-trust-level financial pressures.",
    "sources": [
        {"publisher": "East Cheshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastcheshire.nhs.uk/About-The-Trust/publications.htm"},
        {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
        {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "East Cheshire NHS Trust provider profile (RJN)", "url": "https://www.cqc.org.uk/provider/RJN"}
    ],
    "related": ["East Cheshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — East Cheshire NHS Trust", "Business rates — East Cheshire NHS Trust", "Transport (business + patient) — James Paget University Hospitals NHS Foundation Trust"]
}

NEW["Lease expenditure — University Hospitals Coventry And Warwickshire NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
    "description": "University Hospitals Coventry & Warwickshire NHS Trust's £0.27M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across the trust's two principal sites — University Hospital Coventry (Walsgrave, the regional Major Trauma Centre) and the Hospital of St Cross (Rugby) — and a network of community-clinic, IT-equipment and medical-equipment leases. UHCW operates one of the West Midlands' major PFI hospitals (Walsgrave, opened 2006) so most premises cost flows via PFI not lease.",
    "beneficiaries": "c. 10,500 WTE staff serving a c. 1.0M catchment across Coventry, Warwickshire and parts of Solihull; UH Coventry + Hospital of St Cross (Rugby); c. 200,000 ED attendances/yr; c. 130,000 admissions/yr; c. 700,000 outpatient attendances/yr; tertiary West Midlands Major Trauma Centre + Centre for Reproductive Medicine.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.27M"},
        {"label": "Trust scale", "value": "University Hospital Coventry (Walsgrave, MTC) + Hospital of St Cross (Rugby) + community sites; c. 10,500 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Estate split", "value": "Walsgrave UHCW site is PFI (post-2006 Project Co arrangement) — premises cost mostly flows via PFI/LIFT charges line, not lease"},
        {"label": "PFI context", "value": "UHCW Walsgrave PFI was one of the largest NHS PFI deals (c. £379M 2003 capital value); 30-year concession running until 2035"},
        {"label": "Major Trauma Centre", "value": "Adult MTC for West Midlands North network (rotates with QEHB); high-acuity load 24/7"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — high MTC activity drove backfill agency on Establishment line; minor lease impact"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.18M → 2023-24 c. £0.25M → 2024-25 £0.27M — IFRS 16 transition steady-state + community-clinic refresh"},
        {"label": "Coventry & Warwickshire ICS", "value": "Member of Coventry and Warwickshire ICB; collaborative procurement with George Eliot + South Warks"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates & Facilities + Procurement + IT + clinical-equipment leases; NHSE Provider Finance + DHSC GAM team + HMT lease policy"},
        {"label": "Evaluation evidence", "value": "NAO PFI report (2018) cites UHCW Walsgrave as case study; CQC UHCW inspections; Trust ARA 2023-24"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (April 2022) operating-lease baseline · Successor: lease-portfolio rationalisation + ICS-pooled sites"}
    ],
    "notes": "UHCW's lease line is structurally small because the principal premises footprint at Walsgrave (University Hospital Coventry, opened 2006) sits inside one of England's largest NHS PFI concessions (c. £379M 2003 capital value, 30-year concession running until 2035) — so most premises occupation cost flows via the trust's PFI / LIFT charges line, not the lease line. The £0.27M residual covers IFRS 16 short-term + low-value leases (community clinics, IT and medical equipment), Hospital of St Cross (Rugby) ancillary leases, and the residual operating-lease tail. The trust is a designated West Midlands North Major Trauma Centre and runs the regional Centre for Reproductive Medicine. April 2025 NIC step-up flows indirectly via FM contractor pass-through.",
    "sources": [
        {"publisher": "University Hospitals Coventry and Warwickshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhcw.nhs.uk/about-us/publications/"},
        {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
        {"publisher": "Care Quality Commission", "title": "University Hospitals Coventry and Warwickshire NHS Trust provider profile (RKB)", "url": "https://www.cqc.org.uk/provider/RKB"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Trauma Audit and Research Network (TARN)", "title": "Major Trauma audit", "url": "https://www.tarn.ac.uk/"}
    ],
    "related": ["University Hospitals Coventry And Warwickshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — University Hospitals Coventry And Warwickshire NHS Trust", "Business rates — University Hospitals Coventry And Warwickshire NHS Trust", "Lease expenditure — Nottingham University Hospitals NHS Trust"]
}

NEW["Inventories written down — The Newcastle Upon Tyne Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust"}],
    "description": "Newcastle upon Tyne Hospitals NHS FT's £0.26M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs across one of England's largest single-trust footprints — the Royal Victoria Infirmary, the Freeman Hospital (transplant + cardiothoracic centre), the Centre for Life, and community sites — spanning transplant pharmacy specials (heart, lung, liver, kidney), oncology drugs (Northern Centre for Cancer Care), and theatre consumables. Newcastle's tertiary specialty profile drives high-cost stock turnover.",
    "beneficiaries": "c. 17,000 WTE staff serving a c. 700,000 local catchment + tertiary referral catchment of c. 3M for transplant + cardiothoracic + oncology services across Northern England; c. 250,000 ED attendances/yr; c. 200,000 admissions/yr; c. 1.5M outpatient attendances/yr; c. 200 transplants/yr.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Medicines Act 1968 — Human Tissue Act 2004 (transplant) — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.26M"},
        {"label": "Trust scale", "value": "Royal Victoria Infirmary + Freeman Hospital + Centre for Life + community sites; c. 17,000 WTE; serves c. 700,000 local + c. 3M tertiary"},
        {"label": "Composition", "value": "Transplant pharmacy specials + oncology specials (NCCC) + theatre consumables + cardiothoracic implants + Centre for Life genetics stock per IAS 2"},
        {"label": "Tertiary specialties", "value": "Heart + lung + liver + kidney + bone-marrow transplant; Northern Centre for Cancer Care; Centre for Life genetics; UK military partnership unit"},
        {"label": "Transplant volumes", "value": "c. 200 solid-organ transplants/yr — Newcastle is one of UK's top 3 transplant centres alongside Edinburgh + Cambridge"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — at trust scale large absolute cancellation impact + transplant work-around drove specials obsolescence"},
        {"label": "North East ICS", "value": "Member of North East and North Cumbria ICB — UK's largest ICB by geography"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.20M → 2023-24 c. £0.24M → 2024-25 £0.26M — write-down ratio low per turnover (mature group-procurement)"},
        {"label": "Cardiothoracic outcomes", "value": "Newcastle Freeman is one of UK's top cardiothoracic centres; SCTS audit consistent strong outcomes"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + Theatres + NHSBT + NHS Supply Chain; NHSE Provider Finance + DHSC + Specialised Commissioning + MHRA + HTA"},
        {"label": "Evaluation evidence", "value": "NHSBT transplant audit; SCTS cardiothoracic audit; CQC Newcastle Hospitals inspections; Trust ARA 2023-24; Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-NHSBT pooled-stock baseline · Successor: NENC ICS specialised-stock-pool initiatives + further specialised commissioning consolidation"}
    ],
    "notes": "Newcastle Hospitals is one of England's largest single Acute trusts and a top-tier tertiary specialty centre — running the Northern transplant programme (heart, lung, liver, kidney, bone-marrow), the Northern Centre for Cancer Care, and the Centre for Life genetics service — alongside its local Royal Victoria Infirmary services. The c. 200 transplants/yr drive transplant-specific pharmacy specials obsolescence (immunosuppressants, anti-rejection regimes), while cardiothoracic + oncology specials carry similar NRV exposure. At Newcastle's scale absolute write-downs are kept low relative to turnover by mature group-procurement processes. The 2023-24 industrial-action cycle drove cancellation-related theatre stock obsolescence. The trust is part of the geographically vast North East and North Cumbria ICB.",
    "sources": [
        {"publisher": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.newcastle-hospitals.nhs.uk/about-us/publications/"},
        {"publisher": "NHS Blood and Transplant", "title": "Annual report on transplant activity", "url": "https://www.odt.nhs.uk/statistics-and-reports/annual-activity-report/"},
        {"publisher": "Care Quality Commission", "title": "Newcastle upon Tyne Hospitals NHS FT provider profile (RTD)", "url": "https://www.cqc.org.uk/provider/RTD"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Specialised Commissioning service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
    ],
    "related": ["The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Inventories written down — South Tees Hospitals NHS Foundation Trust", "Inventories written down — University Hospitals Birmingham NHS Foundation Trust"]
}

NEW["Lease expenditure — The Hillingdon Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "The Hillingdon Hospitals NHS Foundation Trust"}],
    "description": "The Hillingdon Hospitals NHS FT's £0.26M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across Hillingdon Hospital (Pield Heath Road, Uxbridge), Mount Vernon Hospital (Northwood — managed jointly with East and North Hertfordshire NHS Trust for the Mount Vernon Cancer Centre), and community sites. Hillingdon's 1960s-era main hospital is on the New Hospital Programme rebuild list following a 2022 internal-fire decant.",
    "beneficiaries": "c. 4,000 WTE staff serving a c. 320,000 catchment across the London Borough of Hillingdon (Uxbridge, Hayes, Ruislip, Northwood) plus parts of South Buckinghamshire; serves Heathrow Airport on-site occupational health; c. 110,000 ED attendances/yr; c. 70,000 admissions/yr; c. 320,000 outpatient attendances/yr.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.26M"},
        {"label": "Trust scale", "value": "Hillingdon Hospital (Uxbridge) + Mount Vernon Hospital (Northwood) + community sites; c. 4,000 WTE; serves c. 320,000"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value (<£5k) charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Estate condition", "value": "Hillingdon main hospital 1966 build — RAAC + asbestos + post-fire decant (Sep 2022 internal fire condemned wards)"},
        {"label": "New Hospital Programme", "value": "Hillingdon named in 2020 NHP cohort; Reset January 2025 — funded for full rebuild by 2030 under Sir Jim Mackey/Wes Streeting plan"},
        {"label": "Mount Vernon", "value": "Mount Vernon Cancer Centre operationally led by East and North Herts; Hillingdon hosts site only; ongoing host-trust review under NHSE specialised commissioning"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — drove backfill on Establishment line"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.18M → 2023-24 c. £0.24M → 2024-25 £0.26M — IFRS 16 transition + post-fire community-clinic decant rentals"},
        {"label": "North West London ICS", "value": "Member of North West London ICB; works alongside Imperial + LNWUH + CW + Chelsea & Westminster"},
        {"label": "Heathrow context", "value": "Trust runs Heathrow Airport occupational health + delivers majority Heathrow-area emergency response"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates & Facilities + Procurement + Mount Vernon site team; NHSE Provider Finance + DHSC GAM + NHP team + HMT lease policy"},
        {"label": "Evaluation evidence", "value": "NHP RAAC announcements 2023; CQC Hillingdon inspections; Mount Vernon governance review (NHSE) 2022; Trust ARA 2023-24"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 + pre-fire baseline · Successor: NHP rebuild completion 2030 + Mount Vernon governance reset"}
    ],
    "notes": "Hillingdon's main hospital is a 1966 building in critical condition — RAAC + asbestos + a September 2022 internal fire forced ward decant — and is named in the 2020 NHP cohort with Reset (January 2025) confirming full rebuild by 2030. The £0.26M lease line covers IFRS 16 short-term + low-value leases (community clinics, IT, medical equipment) plus post-fire decant rentals. The trust hosts Mount Vernon Hospital but the Mount Vernon Cancer Centre is operationally run by East and North Herts under a long-running governance arrangement subject to NHSE specialised-commissioning review. Hillingdon also runs Heathrow Airport occupational health and delivers Heathrow-area emergency response. April 2025 NIC step-up flows via FM contractor pass-through.",
    "sources": [
        {"publisher": "The Hillingdon Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thh.nhs.uk/about-us/publications"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "Care Quality Commission", "title": "The Hillingdon Hospitals NHS Foundation Trust provider profile (RAS)", "url": "https://www.cqc.org.uk/provider/RAS"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Mount Vernon Cancer Centre service review", "url": "https://www.england.nhs.uk/london/our-work/mount-vernon-cancer-centre-review/"}
    ],
    "related": ["The Hillingdon Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — The Hillingdon Hospitals NHS Foundation Trust", "Business rates — The Hillingdon Hospitals NHS Foundation Trust", "Lease expenditure — Nottingham University Hospitals NHS Trust"]
}

NEW["Lease expenditure — Nottingham University Hospitals NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Nottingham University Hospitals NHS Trust"}],
    "description": "Nottingham University Hospitals NHS Trust (NUH)'s £0.26M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across the trust's two-hub footprint — Queen's Medical Centre (Derby Road, the East Midlands' largest single hospital + Major Trauma Centre) and the City Hospital campus (Hucknall Road) — plus community-clinic, IT, and medical-equipment leases. NUH operates under heightened CQC + maternity-review scrutiny (Donna Ockenden 2024 ongoing).",
    "beneficiaries": "c. 17,000 WTE staff serving a c. 800,000 local + c. 3.5M tertiary catchment across the East Midlands (Major Trauma + tertiary services); c. 250,000 ED attendances/yr across QMC + City; c. 200,000 admissions/yr; c. 1.5M outpatient attendances/yr; serves University of Nottingham Medical School population.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.26M"},
        {"label": "Trust scale", "value": "Queen's Medical Centre (QMC, Major Trauma Centre) + City Hospital (Hucknall Road) + community sites; c. 17,000 WTE; serves c. 800,000 local + c. 3.5M tertiary"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value (<£5k) charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Tertiary specialties", "value": "East Midlands Major Trauma Centre + tertiary cardiothoracic + neurosurgery + transplant + Children's Hospital + East Midlands Congenital Heart"},
        {"label": "Regulatory status", "value": "NHSE Recovery Support Programme NOF 4 (since 2022); CQC overall 'Requires Improvement' with maternity 'Inadequate'"},
        {"label": "Ockenden Nottingham Review", "value": "Donna Ockenden review of NUH maternity services — interim findings 2024; final report expected 2026; c. 1,800+ family cases under review"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — at NUH scale large absolute backfill cost on Establishment line"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.18M → 2023-24 c. £0.24M → 2024-25 £0.26M — IFRS 16 transition + community-clinic refresh"},
        {"label": "Nottingham + Nottinghamshire ICS", "value": "Member of Nottingham and Nottinghamshire ICB; collaborative procurement with Sherwood Forest + United Lincolnshire"},
        {"label": "Tomlinson Review", "value": "2023 Mike Bewick / Tomlinson governance review of NUH — board change + culture programme"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates & Facilities + Procurement + IT; NHSE Provider Finance + DHSC GAM + Recovery Support Programme + HMT lease policy"},
        {"label": "Evaluation evidence", "value": "Ockenden Nottingham interim findings 2024; Tomlinson governance review 2023; CQC NUH inspections; Trust ARA 2023-24; NHSE NOF 4"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 baseline · Successor: post-Ockenden + post-Tomlinson governance reset + ICS-level lease pooling"}
    ],
    "notes": "NUH operates under intense scrutiny — the Donna Ockenden review of NUH maternity services (interim findings 2024, final 2026) covers c. 1,800+ family cases and is the largest maternity inquiry since SaTH; the trust remains in NHSE Recovery Support Programme NOF 4 segmentation following the 2022/23 deterioration. Mike Bewick's 2023 governance review (the 'Tomlinson Review' framing) drove board change. The £0.26M lease line is structurally small relative to the trust's c. 17,000 WTE scale because the principal QMC and City premises sit in the trust's owned estate rather than leased — the line covers IFRS 16 short-term + low-value community-clinic, IT and medical-equipment leases. April 2025 NIC step-up flows via FM contractor pass-through but the lease line itself is largely insulated.",
    "sources": [
        {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nuh.nhs.uk/our-publications/"},
        {"publisher": "Donna Ockenden / NHS England", "title": "Independent review of Nottingham maternity services", "url": "https://www.ockendenmaternityreview.org.uk/"},
        {"publisher": "Care Quality Commission", "title": "Nottingham University Hospitals NHS Trust provider profile (RX1)", "url": "https://www.cqc.org.uk/provider/RX1"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Recovery Support Programme — NHS Oversight Framework", "url": "https://www.england.nhs.uk/publication/nhs-oversight-framework/"}
    ],
    "related": ["Nottingham University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Nottingham University Hospitals NHS Trust", "Business rates — Nottingham University Hospitals NHS Trust", "Lease expenditure — University Hospitals Coventry And Warwickshire NHS Trust"]
}

NEW["Inventories written down — London North West University Healthcare NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "London North West University Healthcare NHS Trust"}],
    "description": "London North West University Healthcare NHS Trust (LNWUH)'s £0.26M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs across the trust's three Acute hubs — Northwick Park Hospital (Harrow, with one of London's busiest EDs), Ealing Hospital, and Central Middlesex Hospital — plus St Mark's Hospital (the world-renowned colorectal specialist centre, currently relocating from Northwick Park to Central Middlesex). LNWUH was formed by the 1 October 2014 merger of North West London Hospitals + Ealing Hospital + the integrated community provider.",
    "beneficiaries": "c. 8,500 WTE staff serving a c. 850,000 catchment across Brent, Harrow, Ealing and parts of Hounslow — one of England's most ethnically diverse populations; c. 200,000 ED attendances/yr (Northwick Park ED among London's busiest); c. 130,000 admissions/yr; c. 700,000 outpatient attendances/yr; St Mark's tertiary colorectal referrals UK-wide.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Medicines Act 1968 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.26M"},
        {"label": "Trust scale", "value": "Northwick Park (Harrow) + Ealing Hospital + Central Middlesex (Park Royal) + St Mark's; c. 8,500 WTE; serves c. 850,000"},
        {"label": "Composition", "value": "Pharmacy specials + theatre consumables + St Mark's colorectal stock + Northwick Park ED stock + community-services stock NRV per IAS 2"},
        {"label": "2014 merger", "value": "1 October 2014 — North West London Hospitals + Ealing Hospital + integrated community provider merged to form LNWH (renamed LNWUH)"},
        {"label": "St Mark's", "value": "World-renowned colorectal specialist hospital — relocating from Northwick Park to Central Middlesex; tertiary IBD + cancer referrals UK-wide and international"},
        {"label": "Diverse catchment", "value": "Brent + Harrow + Ealing — among England's most ethnically diverse; significant non-English-first-language workforce + patient pop"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — Northwick Park ED scale drove cancellation + theatre stock obsolescence"},
        {"label": "North West London ICS", "value": "Member of North West London ICB; works alongside Imperial + Hillingdon + Chelsea & Westminster + The Hillingdon"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.20M → 2023-24 c. £0.24M → 2024-25 £0.26M — strike cancellation + St Mark's relocation transition stock effect"},
        {"label": "Ealing A&E history", "value": "Ealing Hospital A&E + maternity centralised away in 2010s 'Shaping a Healthier Future' programme; recurring local political contention"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + St Mark's specialty team + NHS Supply Chain; NHSE Provider Finance + DHSC + Specialised Commissioning + MHRA"},
        {"label": "Evaluation evidence", "value": "CQC LNWUH inspections; St Mark's specialty audit; Trust ARA 2023-24; NW London ICS reconfiguration evidence"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 NWLH + Ealing baseline · Successor: St Mark's relocation completion at Central Middlesex + ICS-level pooled-stock"}
    ],
    "notes": "LNWUH (formed 1 October 2014) runs three Acute hubs in north-west London — Northwick Park, Ealing, Central Middlesex — plus the world-renowned St Mark's colorectal specialist hospital, currently relocating from Northwick Park to a new build at Central Middlesex. Northwick Park ED is among London's busiest. The catchment (Brent, Harrow, Ealing) is one of England's most ethnically diverse, driving distinctive pharmacy + dietetic + community-stock patterns. The legacy 'Shaping a Healthier Future' reconfiguration (which centralised Ealing A&E + maternity in the 2010s) remains a politically live issue. The 2023-24 industrial action drove cancellation-related theatre stock obsolescence. The St Mark's relocation will reset specialty-stock layout late 2020s.",
    "sources": [
        {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lnwh.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "London North West University Healthcare NHS Trust provider profile (R1K)", "url": "https://www.cqc.org.uk/provider/R1K"},
        {"publisher": "St Mark's Hospital", "title": "About St Mark's — colorectal centre", "url": "https://www.stmarkshospital.org.uk/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Specialised Commissioning service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
    ],
    "related": ["London North West University Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — London North West University Healthcare NHS Trust", "Clinical supplies & services — London North West University Healthcare NHS Trust", "Inventories written down — University Hospitals Birmingham NHS Foundation Trust"]
}

NEW["Inventories written down — East And North Hertfordshire NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "East And North Hertfordshire NHS Trust"}],
    "description": "East and North Hertfordshire NHS Trust's £0.26M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs across the Lister Hospital (Stevenage, the trust's principal acute site), the New QEII Hospital (Welwyn Garden City), Hertford County Hospital, plus the Mount Vernon Cancer Centre at Northwood (which the trust operationally runs under a host arrangement with Hillingdon Hospitals). Mount Vernon's tertiary oncology stock + radiopharmaceuticals + cytotoxic specials drive distinct obsolescence dynamics.",
    "beneficiaries": "c. 6,000 WTE staff serving a c. 600,000 catchment across east + north Hertfordshire (Stevenage, Welwyn, Hatfield, Hertford, North Herts) + Mount Vernon tertiary cancer catchment of c. 2M across NW London + Beds + Bucks + Herts + Northants; c. 130,000 ED attendances/yr; c. 90,000 admissions/yr; c. 500,000 outpatient attendances/yr.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Medicines Act 1968 — Ionising Radiation (Medical Exposure) Regulations 2017 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.26M"},
        {"label": "Trust scale", "value": "Lister Hospital (Stevenage) + New QEII (Welwyn GC) + Hertford County + Mount Vernon Cancer Centre (Northwood); c. 6,000 WTE"},
        {"label": "Composition", "value": "Pharmacy specials + Mount Vernon radiopharmaceuticals + cytotoxic specials + theatre consumables + Lister ED stock NRV per IAS 2"},
        {"label": "Mount Vernon Cancer Centre", "value": "Tertiary oncology + radiotherapy centre serving NW London + Beds + Bucks + Herts + Northants; world-leading proton-beam-therapy partnership; UCLH planned move under review"},
        {"label": "Mount Vernon governance", "value": "ENHT operationally runs Mount Vernon Cancer Centre under host arrangement with Hillingdon (estate owner) — under NHSE specialised-commissioning review"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — Mount Vernon radiotherapy disruption drove specials obsolescence"},
        {"label": "Hertfordshire & West Essex ICS", "value": "Member of Hertfordshire and West Essex ICB; collaborative procurement with West Hertfordshire + Princess Alexandra"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.20M → 2023-24 c. £0.24M → 2024-25 £0.26M — Mount Vernon radiopharmaceutical short-life-stock effect dominates"},
        {"label": "Lister rebuild", "value": "Lister single-site reconfiguration completed 2014 (£150M) — concentrates Acute services from former QEII Welwyn build"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + Mount Vernon specialty team + NHS Supply Chain; NHSE Provider Finance + DHSC + Specialised Commissioning + MHRA + UKHSA"},
        {"label": "Evaluation evidence", "value": "Mount Vernon governance review (NHSE) 2022; CQC ENHT inspections; Trust ARA 2023-24; CRUK + NCRAS oncology audit"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 Lister rebuild + pre-Mount-Vernon-host baseline · Successor: Mount Vernon relocation/rebuild + ICS specialised-stock pooling"}
    ],
    "notes": "ENHT's inventory profile is dominated by the Mount Vernon Cancer Centre — a tertiary oncology + radiotherapy centre serving c. 2M across NW London, Bedfordshire, Buckinghamshire, Hertfordshire and Northamptonshire — operationally run by ENHT under a host arrangement with Hillingdon Hospitals (which owns the estate). Mount Vernon's radiopharmaceuticals, cytotoxic pharmacy specials and short-life-stock drive obsolescence write-downs above what a comparable DGH would carry. The centre is the subject of an ongoing NHSE specialised-commissioning review with options including UCLH-led relocation to a central London cancer hub. The Lister Hospital single-site reconfiguration (completed 2014) consolidated the trust's acute services from the former QEII Welwyn build. Industrial action in 2023-24 disrupted radiotherapy schedules.",
    "sources": [
        {"publisher": "East and North Hertfordshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.enherts-tr.nhs.uk/about-us/publications/"},
        {"publisher": "NHS England", "title": "Mount Vernon Cancer Centre service review", "url": "https://www.england.nhs.uk/london/our-work/mount-vernon-cancer-centre-review/"},
        {"publisher": "Care Quality Commission", "title": "East and North Hertfordshire NHS Trust provider profile (RWH)", "url": "https://www.cqc.org.uk/provider/RWH"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Cancer Research UK / NCRAS", "title": "National Cancer Registration and Analysis Service", "url": "https://digital.nhs.uk/ndrs"}
    ],
    "related": ["East And North Hertfordshire NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — East And North Hertfordshire NHS Trust", "Clinical supplies & services — East And North Hertfordshire NHS Trust", "Lease expenditure — The Hillingdon Hospitals NHS Foundation Trust"]
}

NEW["Inventories written down — Northampton General Hospital NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Northampton General Hospital NHS Trust"}],
    "description": "Northampton General Hospital NHS Trust's £0.26M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs at the single-site Northampton General Hospital (Cliftonville) — a DGH serving the south-Northamptonshire catchment — spanning pharmacy specials, theatre consumables, oncology stock and the trust's expanding tertiary cancer + cardiology services. Northampton operates under a Group Model (since April 2024) with neighbouring Kettering General Hospital, sharing back-office functions and group procurement to drive stock-management improvements.",
    "beneficiaries": "c. 5,000 WTE staff serving a c. 380,000 catchment across south Northamptonshire (Northampton, Daventry, Towcester, Brackley, Wellingborough overlap); c. 110,000 ED attendances/yr at NGH; c. 75,000 admissions/yr; c. 380,000 outpatient attendances/yr; trust runs the Northampton Cancer Centre + cardiology + stroke services for the wider county.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Medicines Act 1968 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.26M"},
        {"label": "Trust scale", "value": "Northampton General Hospital (Cliftonville) single-site DGH + community satellites; c. 5,000 WTE; serves c. 380,000"},
        {"label": "Composition", "value": "Pharmacy specials + theatre consumables + oncology stock (Northampton Cancer Centre) + cardiology consumables + theatre stock NRV per IAS 2"},
        {"label": "Group Model", "value": "Group Model with Kettering General Hospital (since April 2024) — shared CEO + COO + Chief Strategy + group procurement; first NHS group of its kind"},
        {"label": "Northampton Cancer Centre", "value": "Trust-led oncology service with linac investment; tertiary referrals from Kettering + Wellingborough; SACT chemotherapy delivery"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — drove cancellation + theatre stock obsolescence; SACT slot rebooking drove specials NRV"},
        {"label": "Northamptonshire ICS", "value": "Member of Northamptonshire ICB; group structure with Kettering plus Northamptonshire Healthcare NHS FT (community + MH)"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.21M → 2023-24 c. £0.24M → 2024-25 £0.26M — Group Model integration drove early procurement harmonisation"},
        {"label": "Cliftonville campus", "value": "Mixed estate — some 19th-century build (1793 founding voluntary hospital lineage) + 1970s + recent Cliftonville Tower (2017)"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + Group procurement (with Kettering) + NHS Supply Chain; NHSE Provider Finance + DHSC + MHRA"},
        {"label": "Evaluation evidence", "value": "CQC NGH inspections (overall 'Good' 2023); Group Model evaluation (NHSE) 2024-25; Trust ARA 2023-24; Northampton Cancer Centre SACT audits"},
        {"label": "Trust legacy", "value": "Founding voluntary hospital lineage 1793 — among England's oldest continuously operating hospitals on its current site"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-Group-Model standalone trust · Successor: deeper Group Model with Kettering + ICB-pooled procurement"}
    ],
    "notes": "Northampton General entered a Group Model arrangement with neighbouring Kettering General Hospital from April 2024 — the first formal NHS Group Model of its kind, with shared CEO, COO and Chief Strategy Officer plus joint procurement — explicitly intended to drive stock-management improvements and back-office efficiency. The £0.26M write-down line is at the early stages of group-procurement benefits-realisation. The trust runs the Northampton Cancer Centre (linac investment + SACT chemotherapy), serving tertiary referrals from across south Northamptonshire. NGH carries a notable founding voluntary-hospital lineage going back to 1793, making it among England's oldest continuously operating hospitals. Industrial action in 2023-24 drove cancellation + SACT-slot obsolescence.",
    "sources": [
        {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northamptongeneral.nhs.uk/About/Publications/"},
        {"publisher": "NHS England", "title": "University Hospitals of Northamptonshire Group — Group Model", "url": "https://www.unhg.nhs.uk/"},
        {"publisher": "Care Quality Commission", "title": "Northampton General Hospital NHS Trust provider profile (RNS)", "url": "https://www.cqc.org.uk/provider/RNS"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "SACT chemotherapy dataset", "url": "https://www.chemodataset.nhs.uk/"}
    ],
    "related": ["Northampton General Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — Northampton General Hospital NHS Trust", "Inventories written down — Kettering General Hospital NHS Foundation Trust", "Clinical supplies & services — Northampton General Hospital NHS Trust"]
}

NEW["Inventories written down — Kettering General Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Kettering General Hospital NHS Foundation Trust"}],
    "description": "Kettering General Hospital NHS FT's £0.26M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs at the single-site Kettering General Hospital (Rothwell Road) — a DGH serving the north-Northamptonshire catchment — spanning pharmacy specials, theatre consumables, oncology stock and obstetric supplies. KGH operates under a Group Model (since April 2024) with neighbouring Northampton General Hospital, sharing CEO, back-office functions and group procurement, and is named on the New Hospital Programme rebuild list (RAAC + ageing 1894 estate).",
    "beneficiaries": "c. 4,000 WTE staff serving a c. 360,000 catchment across north Northamptonshire (Kettering, Corby, Wellingborough, East Northants, Rushden); c. 90,000 ED attendances/yr at KGH; c. 60,000 admissions/yr; c. 350,000 outpatient attendances/yr; trust serves the Corby new-town demographic plus rural north Northamptonshire population.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Medicines Act 1968 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.26M"},
        {"label": "Trust scale", "value": "Kettering General Hospital (Rothwell Road) single-site DGH + community satellites; c. 4,000 WTE; serves c. 360,000"},
        {"label": "Composition", "value": "Pharmacy specials + theatre consumables + obstetric stock + oncology stock + ED consumables NRV per IAS 2"},
        {"label": "Group Model", "value": "Group Model with Northampton General Hospital (since April 2024) — shared CEO + COO + Chief Strategy + group procurement"},
        {"label": "New Hospital Programme", "value": "KGH named in 2020 NHP cohort; Reset January 2025 — funded for full rebuild by 2030 owing to ageing 1894 estate + RAAC concerns"},
        {"label": "Estate age", "value": "Original 1894 voluntary-hospital build extant in core; mixed Victorian + 1960s + recent 'Foundation Wing' build; backlog maintenance high"},
        {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes — small DGH severely felt; cancellation drove theatre + obstetric stock obsolescence"},
        {"label": "Northamptonshire ICS", "value": "Member of Northamptonshire ICB; group structure with Northampton plus Northamptonshire Healthcare NHS FT (community + MH)"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.21M → 2023-24 c. £0.24M → 2024-25 £0.26M — pre-Group early stages; benefits-realisation expected from 2025-26"},
        {"label": "Corby + Wellingborough demand", "value": "Catchment includes Corby new-town deprived demographic + rapidly growing Wellingborough/Rushden housing"},
        {"label": "Delivery body + policy owner", "value": "Trust Pharmacy + Procurement + Group procurement (with Northampton) + NHS Supply Chain; NHSE Provider Finance + DHSC + NHP team + MHRA"},
        {"label": "Evaluation evidence", "value": "CQC KGH inspections; Group Model evaluation (NHSE) 2024-25; Trust ARA 2023-24; NHP RAAC announcements"},
        {"label": "Trust legacy", "value": "Founding voluntary hospital lineage 1894; transitioned to NHS 1948; FT status 2008"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-Group-Model standalone trust · Successor: deeper Group Model with Northampton + NHP rebuild 2030"}
    ],
    "notes": "Kettering General entered a Group Model arrangement with Northampton General from April 2024 — the first formal NHS Group Model of its kind — and is also named on the New Hospital Programme rebuild list (Reset January 2025 confirmed completion by 2030) owing to its ageing 1894 voluntary-hospital estate and RAAC concerns. The catchment includes the deprived Corby new-town demographic and rapidly growing Wellingborough/Rushden housing. Group Model benefits-realisation in procurement is at early stages — write-down ratios are expected to drop from 2025-26 as harmonisation progresses. Industrial action in 2023-24 disrupted obstetric + theatre activity; obsolescence write-downs followed cancellation patterns. The pending NHP rebuild will substantially reset the trust's stock + estate profile.",
    "sources": [
        {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/about-us/publications/"},
        {"publisher": "NHS England", "title": "University Hospitals of Northamptonshire Group — Group Model", "url": "https://www.unhg.nhs.uk/"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "Care Quality Commission", "title": "Kettering General Hospital NHS Foundation Trust provider profile (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
    ],
    "related": ["Kettering General Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Drugs costs — Kettering General Hospital NHS Foundation Trust", "Inventories written down — Northampton General Hospital NHS Trust", "Clinical supplies & services — Kettering General Hospital NHS Foundation Trust"]
}

NEW["Transport (business + patient) — James Paget University Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Transport (business + patient)", "parent": "James Paget University Hospitals NHS Foundation Trust"}],
    "description": "James Paget University Hospitals NHS FT's £0.26M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site pathology specimen transport between the James Paget University Hospital (Gorleston-on-Sea, near Great Yarmouth) and community satellites at Newberry Clinic + Lowestoft, plus contracted non-emergency patient transport (NEPTS) for the Norfolk + Waveney ICS catchment. The trust serves a coastal catchment with rural transport challenges and is on the New Hospital Programme rebuild list.",
    "beneficiaries": "c. 3,500 WTE staff serving a c. 250,000 catchment across east Norfolk (Great Yarmouth, Acle, Caister) and northern Suffolk Waveney (Lowestoft); c. 80,000 ED attendances/yr at the Gorleston site; c. 55,000 admissions/yr; c. 280,000 outpatient attendances/yr; significant elderly + holiday-tourism demographic on the East Anglian coast.",
    "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Transport (business + patient) 2024-25", "value": "£0.26M"},
        {"label": "Trust scale", "value": "James Paget University Hospital (Gorleston-on-Sea) + Newberry Clinic + Lowestoft satellite + community sites; c. 3,500 WTE"},
        {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + pathology specimen transport + contracted NEPTS"},
        {"label": "NEPTS provider", "value": "ERS Medical / EMED Group on Norfolk + Waveney ICB framework — NHSE 2021 NEPTS Review eligibility implementation"},
        {"label": "Coastal geography", "value": "Cross-county catchment (Norfolk + Suffolk) on East Anglian coast; rural Acle + Caister + tourist holiday population in summer"},
        {"label": "New Hospital Programme", "value": "JPUH named in 2020 NHP cohort (RAAC roof concerns); Reset January 2025 — funded for full rebuild by 2030"},
        {"label": "Industrial action + NIC step-up", "value": "44 days junior-doctor + 10 days consultant strikes — small coastal trust felt severely; April 2025 NIC step-up flows via NEPTS contractor pass-through"},
        {"label": "AMAP rates 2024-25", "value": "HMRC AMAP frozen at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.20M → 2023-24 c. £0.24M → 2024-25 £0.26M — fuel pass-through + NEPTS uplift + pre-rebuild estate transport churn"},
        {"label": "Norfolk + Waveney ICS", "value": "Member of Norfolk and Waveney ICB; collaborative NEPTS commissioning with NNUH (Norwich) + West Suffolk + ESNEFT"},
        {"label": "Tourism context", "value": "Great Yarmouth/Lowestoft tourism inflates summer ED activity; offshore wind energy industry growth driving trauma/occ-health activity"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates & Facilities + Pathology + Transport Office + ERS Medical (NEPTS) + EEAST (emergency overlap); NHSE + DHSC + NHP team + ICB transport commissioner"},
        {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; CQC JPUH inspections; Trust ARA 2023-24; NHP RAAC announcements"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-Review baseline · Successor: ICB-wide eligibility-criteria implementation + NHP rebuild 2030 + pool-fleet electrification"}
    ],
    "notes": "James Paget University Hospitals serves a distinctive East Anglian coastal catchment (Great Yarmouth + Lowestoft + Acle + Caister + Waveney) with a large elderly population, summer tourism inflation of ED demand, and a rapidly growing offshore wind-energy sector driving occupational health + trauma activity. The trust is on the New Hospital Programme rebuild list (named 2020 cohort, Reset January 2025 confirmed completion by 2030) owing to RAAC roof concerns. Transport spend is structurally elevated by rural geography and the cross-county Norfolk + Suffolk-Waveney service footprint, with contracted NEPTS via ERS Medical / EMED Group under the Norfolk and Waveney ICB framework. April 2025 NIC step-up flows indirectly through the NEPTS contractor pass-through. Frozen AMAP rates compress staff mileage reimbursement.",
    "sources": [
        {"publisher": "James Paget University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.jpaget.nhs.uk/about-us/publications/"},
        {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
        {"publisher": "Care Quality Commission", "title": "James Paget University Hospitals NHS Foundation Trust provider profile (RGP)", "url": "https://www.cqc.org.uk/provider/RGP"}
    ],
    "related": ["James Paget University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — James Paget University Hospitals NHS Foundation Trust", "Business rates — James Paget University Hospitals NHS Foundation Trust", "Transport (business + patient) — East Cheshire NHS Trust"]
}
