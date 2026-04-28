# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 38 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Inventories written down — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "University Hospitals Sussex NHS FT's £0.847M inventories-written-down line covers IAS 2 net-realisable-value impairments and obsolescence write-offs against clinical-supplies, drugs and consumables stockholdings across the trust's seven-hospital footprint (Royal Sussex County, Princess Royal Haywards Heath, Worthing, St Richard's Chichester, Southlands, Brighton General, Royal Alexandra Children's). Drivers include short-dated drug expiries, single-use device standards changes, COVID-PPE legacy stock obsolescence and pathology-reagent product churn. Sussex Health and Care ICS context.",
        "beneficiaries": "c. 13,500 WTE staff serving a c. 1.8M Sussex catchment plus tertiary referral population for cardiac, neurosciences, paediatrics and HIV; c. 320,000 ED attendances/yr; c. 220,000 admissions/yr; c. 1.4M outpatient attendances/yr; trust formed by 2021 merger of Brighton & Sussex University Hospitals + Western Sussex Hospitals.",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Human Medicines Regulations 2012 (drug expiry/destruction) — IAS 36 (impairment interaction)",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.847M"},
            {"label": "Trust scale", "value": "7 hospitals across Brighton, Worthing, Chichester, Haywards Heath; c. 13,500 WTE; 2021 merger entity"},
            {"label": "Composition", "value": "Short-dated drug expiries + single-use device obsolescence + COVID-PPE legacy stock + pathology-reagent churn + theatre consumable spec changes"},
            {"label": "Drug-expiry destruction", "value": "Per Human Medicines Regs 2012 + MHRA controlled-drug destruction protocols + DHSC GAM"},
            {"label": "COVID-PPE legacy", "value": "DHSC central stockpile transferred 2022-23; trust-held residuals continue to flow through write-down line"},
            {"label": "Stock policy", "value": "IAS 2 lower-of-cost-and-NRV; trust-level inventory-management system + NHS Supply Chain Logistics Online Marketplace"},
            {"label": "Industrial action 2023-24 effect", "value": "Cancelled elective lists drove theatre-pack write-off (single-use sterile expiry) and drug-prep-set wastage"},
            {"label": "Funding trajectory", "value": "2022-23 c. £0.6M (post-merger) → 2023-24 c. £0.78M → 2024-25 £0.847M — COVID-PPE tail + EPR-driven catalogue rationalisation"},
            {"label": "Sussex Health and Care ICS", "value": "Member of Sussex ICB; collaborative procurement and stock-pooling across acute trusts"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Theatres + Pathology + NHS Supply Chain + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Supply Chain + MHRA (controlled drug destruction) + Sussex ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 inventory note; NAO NHS Supply Chain reports; Carter Lord review legacy on stockholding ratios; Model Hospital inventory benchmark"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021-merger separate stockholdings · Successor: integrated trust-wide inventory + Frontline Digitisation EPR-linked stock-control + ICS pooling"}
        ],
        "notes": "University Hospitals Sussex NHS FT's inventories-written-down line is shaped by post-merger (April 2021) catalogue-rationalisation legacy across seven hospitals — duplicated SKUs, divergent theatre packs and pharmacy stock conventions drive higher-than-baseline write-offs. COVID-PPE legacy stock continues to tail through the write-down line as 2020-21 procurement reaches expiry. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) drove cancelled-list theatre-pack and drug-prep-set wastage. CQC inspection March 2024 raised maternity-services concerns at Royal Sussex County (rated 'requires improvement') but did not directly drive inventory write-offs. The trust's tertiary cardiac, neurosciences and HIV roles drive specialist-reagent and high-cost-drug expiry exposure.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhsussex.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Sussex NHS Foundation Trust provider profile (RYR)", "url": "https://www.cqc.org.uk/provider/RYR"},
            {"publisher": "Medicines and Healthcare products Regulatory Agency", "title": "Disposal of unwanted medicines guidance", "url": "https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — University Hospitals Sussex NHS Foundation Trust", "NHS Supply Chain", "Department of Health and Social Care"]
    },
    "Amortisation — University Hospitals of Morecambe Bay NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospitals of Morecambe Bay NHS Foundation Trust"}],
        "description": "University Hospitals of Morecambe Bay NHS FT's £0.847M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the Lorenzo (DXC/CSC) EPR legacy plus successor Frontline Digitisation modules deployed across the Royal Lancaster Infirmary, Furness General Hospital (Barrow-in-Furness) and Westmorland General (Kendal), plus capitalised software for pathology, radiology and back-office systems. The trust's geographic footprint across Cumbria-Lancashire borders drives separate site-licence intangibles. Lancashire and South Cumbria ICS context.",
        "beneficiaries": "c. 7,000 WTE staff serving a c. 365,000 catchment across Lancaster, South Cumbria, Furness and the Lake District; c. 105,000 ED attendances/yr at RLI + Furness EDs; c. 70,000 admissions/yr; c. 530,000 outpatient attendances/yr; trust serves geographically isolated Furness peninsula population dependent on FGH for acute care.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 3 (acquired-software treatment)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.847M"},
            {"label": "Trust scale", "value": "Royal Lancaster Infirmary + Furness General + Westmorland General; c. 7,000 WTE"},
            {"label": "Principal intangibles", "value": "Lorenzo EPR legacy + PACS/RIS imaging + e-prescribing modules + pathology LIMS + back-office software"},
            {"label": "EPR platform", "value": "Lorenzo (DXC/CSC) — successor Frontline Digitisation deployment in scope under NHSE Wave 3-4"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; major EPR modules amortised over 7-10 yrs; PACS image storage ~10 years"},
            {"label": "Frontline Digitisation pipeline", "value": "Trust in NHSE convergence cohort moving off Lorenzo to new EPR — capitalisation tranche pending"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.79M → 2024-25 £0.847M — module additions + Lorenzo run-out amortisation"},
            {"label": "Lancashire and South Cumbria ICS", "value": "Member of Lancashire and South Cumbria ICB; shared digital roadmap with neighbouring trusts"},
            {"label": "Morecambe Bay legacy", "value": "Kirkup 2015 maternity inquiry shaped governance overhead — not directly material to amortisation"},
            {"label": "Delivery body", "value": "Trust IT + Finance + DXC (Lorenzo) + Frontline Digitisation programme team + ICS digital lead"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NAO Lorenzo / NPfIT legacy reports; Trust ARA 2023-24 intangibles note; CQC RTX inspections; DHSC GAM compliance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Lorenzo paper-record baseline · Successor: Frontline Digitisation new-EPR (Cerner / Epic / Oracle Health TBD) capitalisation tranche from 2025-27"}
        ],
        "notes": "UHMB's amortisation line is shaped by the Lorenzo (DXC/CSC) EPR legacy — UHMB is one of the trusts being moved off Lorenzo in NHSE's convergence programme, with a successor EPR (likely procured via Frontline Digitisation Wave 3-4) bringing a substantial capitalisation tranche from 2025-27. The trust's three-site geography (Royal Lancaster Infirmary, Furness General Hospital, Westmorland General) drives duplicated digital-infrastructure intangibles. The Kirkup 2015 maternity inquiry into Morecambe Bay shaped governance and culture overhead but is not directly material to amortisation. Future EPR refresh is the medium-term cliff for the intangibles balance — likely to step up materially from 2027 onwards.",
        "sources": [
            {"publisher": "University Hospitals of Morecambe Bay NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhmb.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals of Morecambe Bay NHS Foundation Trust provider profile (RTX)", "url": "https://www.cqc.org.uk/provider/RTX"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 317, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"}
        ],
        "related": ["University Hospitals of Morecambe Bay NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Royal Free London NHS Foundation Trust", "NHS England", "Department of Health and Social Care"]
    },
    "Business rates — Barnsley Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Barnsley Hospital NHS Foundation Trust"}],
        "description": "Barnsley Hospital NHS FT's £0.841M business-rates line covers non-domestic rate liability across the trust's principal Barnsley Hospital site (Gawber Road) plus satellite community-clinic estate. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. South Yorkshire ICS context. Smaller single-site DGH so business-rates liability is dominated by the Gawber Road hereditament.",
        "beneficiaries": "c. 3,300 WTE staff serving a c. 245,000 Barnsley borough catchment; c. 90,000 ED attendances/yr; c. 60,000 admissions/yr; c. 360,000 outpatient attendances/yr; trust runs the South Yorkshire Eye Service (regional ophthalmology) and a co-located NHS Children's Service.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.841M"},
            {"label": "Trust scale", "value": "Barnsley Hospital (Gawber Road) + satellite community clinics; c. 3,300 WTE; single-site DGH"},
            {"label": "Principal hereditament", "value": "Barnsley Hospital Gawber Road — likely standard-multiplier tier (under £500k RV high-tier threshold)"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.74M → 2023-24 c. £0.81M → 2024-25 £0.841M — 2023 list revaluation + multiplier uplift"},
            {"label": "Billing authority", "value": "Barnsley Metropolitan Borough Council"},
            {"label": "South Yorkshire ICS", "value": "Member of South Yorkshire ICB; collaborative E&F services across DGHs"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + Barnsley MBC (billing)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; Trust ARA 2023-24 disclosure; CQC RFF inspections; NAO local government finance reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation; trust appeal route via Check Challenge Appeal"}
        ],
        "notes": "Barnsley Hospital NHS FT's business-rates line is dominated by the single Gawber Road acute hereditament — as a smaller-footprint DGH the trust escapes the £500k+ RV higher-tier multiplier introduced by the NDR (Multipliers and Private Finance) Act 2024 from April 2025, applying instead the standard non-domestic multiplier. NHS trusts are not eligible for the mandatory 80% charitable rate relief. The 1 April 2026 next revaluation is the medium-term lever — expected to reflect post-COVID rental and capital-value adjustments. The trust runs a working partnership with Sheffield Children's NHS FT for paediatrics and with Sheffield Teaching for cardiology and stroke care, but rates are paid on the Barnsley estate as occupier.",
        "sources": [
            {"publisher": "Barnsley Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.barnsleyhospital.nhs.uk/about-us/board-of-directors/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Barnsley Hospital NHS Foundation Trust provider profile (RFF)", "url": "https://www.cqc.org.uk/provider/RFF"}
        ],
        "related": ["Barnsley Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Oxford University Hospitals NHS Foundation Trust", "Valuation Office Agency", "Department of Health and Social Care"]
    },
    "Amortisation — Countess of Chester Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
        "description": "Countess of Chester Hospital NHS FT's £0.837M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the Cerner Millennium EPR plus successor Frontline Digitisation modules deployed at the principal Liverpool Road site (Chester) plus the Ellesmere Port Hospital community footprint. The trust's small-footprint DGH scale relative to teaching peers gives a lower intangibles base. Cheshire and Merseyside ICS context. Note: the Letby criminal-trial governance overhead shaped HR/legal/inquiry costs but is not directly material to amortisation.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 250,000 west Cheshire catchment plus cross-border Welsh-flow patients; c. 80,000 ED attendances/yr at Liverpool Road; c. 55,000 admissions/yr; c. 320,000 outpatient attendances/yr; trust runs maternity, paediatrics, ED, cancer and elective services with regional plastics partnership.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 3 (acquired-software treatment)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.837M"},
            {"label": "Trust scale", "value": "Countess of Chester Hospital (Liverpool Road) + Ellesmere Port Hospital; c. 4,500 WTE"},
            {"label": "Principal intangibles", "value": "Cerner Millennium EPR + PACS/RIS imaging + e-prescribing + pathology LIMS + back-office software"},
            {"label": "EPR platform", "value": "Cerner Millennium (deployed 2014) — Frontline Digitisation upgrade pathway in scope"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; EPR major modules 7-10 yrs; PACS image storage ~10 years"},
            {"label": "Frontline Digitisation pipeline", "value": "Ongoing capitalised module additions (clinical noting, decision-support, mobile apps)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.78M → 2024-25 £0.837M — Cerner mid-life amortisation + module additions"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of Cheshire & Merseyside ICB; collaborative digital roadmap (LCR) and pathology partnership"},
            {"label": "Letby inquiry context", "value": "Thirlwall Inquiry running 2024-25 — drives HR/legal/governance overhead, not directly amortisation"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Cerner (Oracle Health) + Frontline Digitisation programme team + ICS digital lead"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation reports; Trust ARA 2023-24 intangibles note; CQC RJR inspections; Thirlwall Inquiry evidence"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner-2014 paper-record baseline · Successor: Frontline Digitisation Wave 4-5 module deployment + future EPR refresh-cycle (2030+)"}
        ],
        "notes": "Countess of Chester Hospital NHS FT's amortisation line is shaped by the 2014 Cerner Millennium EPR deployment now in mid-late life amortisation under IAS 38 useful-economic-life conventions, plus continued Frontline Digitisation module additions. The trust's small-footprint DGH scale gives a lower intangibles base than tertiary peers. The Lucy Letby criminal trial (2022-23) and ongoing Thirlwall Inquiry (2024-25) drive substantial HR/legal/inquiry-response governance overhead but are not directly material to amortisation. Future EPR refresh-cycle (likely 2030+) is the medium-term cliff for the intangibles balance. The trust's regional partnerships with Liverpool plastics, neurosurgery and oncology services do not generate intangibles at COCH level (cross-trust SLAs).",
        "sources": [
            {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.coch.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Countess of Chester Hospital NHS Foundation Trust provider profile (RJR)", "url": "https://www.cqc.org.uk/provider/RJR"},
            {"publisher": "Thirlwall Inquiry", "title": "Thirlwall Inquiry into events at the Countess of Chester Hospital", "url": "https://thirlwall.public-inquiry.uk/"}
        ],
        "related": ["Countess of Chester Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — University Hospitals of Morecambe Bay NHS Foundation Trust", "NHS England", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Kettering General Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Kettering General Hospital NHS Foundation Trust"}],
        "description": "Kettering General Hospital NHS FT's £0.823M transport line covers staff business mileage (AfC Section 17 + AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between the Rothwell Road site and outreach community clinics, plus contracted non-emergency patient transport (NEPTS) for the Northamptonshire ICS catchment. The trust runs the Group with Northampton General (since 2021) so cross-trust pathology and specimen courier flows have grown materially.",
        "beneficiaries": "c. 3,800 WTE staff serving a c. 380,000 north Northamptonshire catchment (Kettering, Corby, Wellingborough, East Northants, Rushden); c. 100,000 ED attendances/yr; c. 70,000 admissions/yr; c. 320,000 outpatient attendances/yr; KGH operates jointly with Northampton General Hospital under University Hospitals of Northamptonshire Group governance.",
        "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.823M"},
            {"label": "Trust scale", "value": "Kettering General Hospital (Rothwell Rd) + community-clinic outreach; c. 3,800 WTE; UHN Group with NGH"},
            {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site KGH-NGH pathology/courier + contracted NEPTS"},
            {"label": "NEPTS provider", "value": "EMED Group (East Midlands Ambulance NEPTS framework, retendered 2022-23)"},
            {"label": "UHN Group context", "value": "Group operating model with Northampton General since 2021 — drives KGH-NGH pathology/specimen/blood-product courier flow"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement + NEPTS rebooking spike"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via NEPTS contractor + agency-driver pass-through (15% over £5k)"},
            {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.65M → 2023-24 c. £0.78M → 2024-25 £0.823M — strike backfill + NHS Group cross-site flows + fuel-cost pass-through"},
            {"label": "Northamptonshire ICS", "value": "Member of Northamptonshire ICB; collaborative NEPTS commissioning with NGH"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + EMED Group (NEPTS) + EMAS (when emergency overlap)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Patient Transport Services policy + DHSC + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; Trust ARA 2023-24; CQC RNQ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-retender + pre-UHN-Group baseline · Successor: NEPTS-Review-aligned eligibility implementation + further UHN Group consolidation of cross-site logistics"}
        ],
        "notes": "Kettering General Hospital NHS FT's transport line is shaped by the University Hospitals of Northamptonshire (UHN) Group operating model with Northampton General Hospital (since 2021) — cross-trust pathology, specimen and blood-product courier flow between Kettering and Northampton sites drives a structural premium. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) drove locum travel reimbursement and NEPTS rebooking. The NEPTS contract (EMED Group) is procured via the East Midlands NEPTS framework. The trust's New Hospital Programme bid (Kettering wave) was deferred in the January 2025 NHP Reset to a 2030s delivery window — does not affect transport directly but may shape future site-consolidation logistics. April 2025 employer NIC step-up flows indirectly via NEPTS and agency-driver contracts.",
        "sources": [
            {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Kettering General Hospital NHS Foundation Trust provider profile (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"}
        ],
        "related": ["Kettering General Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Cambridge University Hospitals NHS Foundation Trust", "Northampton General Hospital NHS Trust", "NHS England"]
    },
    "Amortisation — Tameside and Glossop Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Tameside and Glossop Integrated Care NHS Foundation Trust"}],
        "description": "Tameside and Glossop Integrated Care NHS FT's £0.823M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the trust's electronic-patient-record stack plus successor Frontline Digitisation modules deployed at Tameside General Hospital (Ashton-under-Lyne) plus integrated community services across Tameside borough and Glossopdale. The trust is one of the few England integrated-care provider trusts (acute + community combined). Greater Manchester ICS context.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 250,000 catchment across Tameside (Ashton, Stalybridge, Hyde, Denton, Audenshaw, Mossley, Droylsden) plus Glossopdale Derbyshire borough; c. 95,000 ED attendances/yr; c. 60,000 admissions/yr; c. 295,000 outpatient attendances/yr; trust delivers integrated acute + community + intermediate-care services.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 3 (acquired-software treatment)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.823M"},
            {"label": "Trust scale", "value": "Tameside General Hospital + integrated community services across Tameside + Glossopdale; c. 4,000 WTE"},
            {"label": "Principal intangibles", "value": "EPR stack (Lorenzo legacy + successor) + PACS/RIS imaging + e-prescribing + community-services systems + back-office software"},
            {"label": "EPR platform", "value": "Lorenzo legacy + Frontline Digitisation upgrade pathway via GM Care Record + ICS digital programme"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; major EPR modules amortised over 7-10 yrs; PACS image storage ~10 years"},
            {"label": "Frontline Digitisation pipeline", "value": "Tameside in NHSE convergence cohort moving off Lorenzo — successor EPR procurement under Wave 4-5"},
            {"label": "Integrated trust model", "value": "One of few England integrated-care FTs (acute + community + intermediate) — drives wider community-systems intangibles"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.78M → 2024-25 £0.823M — Lorenzo run-out + module additions"},
            {"label": "Greater Manchester ICS", "value": "Member of GM ICB; integrated with GM Care Record shared-care-record platform"},
            {"label": "Delivery body", "value": "Trust IT + Finance + DXC (Lorenzo legacy) + Frontline Digitisation programme team + GM Care Record"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NAO Lorenzo / NPfIT legacy reports; Trust ARA 2023-24 intangibles note; CQC RMP inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Lorenzo paper-record baseline · Successor: Frontline Digitisation new-EPR capitalisation tranche from 2025-27 + ongoing GM Care Record integration"}
        ],
        "notes": "Tameside and Glossop's amortisation line is shaped by the Lorenzo (DXC/CSC) EPR legacy — Tameside is in NHSE's convergence cohort moving off Lorenzo, with a successor EPR (likely procured via Frontline Digitisation Wave 4-5) bringing a substantial capitalisation tranche from 2025-27. The trust's integrated acute + community + intermediate-care operating model drives broader community-systems intangibles than peer DGHs. The Greater Manchester Care Record shared-care-record platform contributes to capitalised software amortised across the trust. Future EPR refresh is the medium-term cliff — likely to step up materially from 2027 onwards. The trust's previous CQC special-measures history (lifted 2017) is not directly material to amortisation.",
        "sources": [
            {"publisher": "Tameside and Glossop Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.tamesidehospital.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Tameside and Glossop Integrated Care NHS Foundation Trust provider profile (RMP)", "url": "https://www.cqc.org.uk/provider/RMP"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 317, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"}
        ],
        "related": ["Tameside and Glossop Integrated Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — University Hospitals of Morecambe Bay NHS Foundation Trust", "Business rates — Tameside and Glossop Integrated Care NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Tameside and Glossop Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Tameside and Glossop Integrated Care NHS Foundation Trust"}],
        "description": "Tameside and Glossop Integrated Care NHS FT's £0.820M business-rates line covers non-domestic rate liability across the principal Tameside General Hospital site (Fountain Street, Ashton-under-Lyne) plus integrated community-clinic estate across Tameside borough and Glossopdale. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Greater Manchester ICS context.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 250,000 catchment across Tameside (Ashton, Stalybridge, Hyde, Denton, Audenshaw, Mossley, Droylsden) plus Glossopdale Derbyshire borough; c. 95,000 ED attendances/yr; c. 60,000 admissions/yr; c. 295,000 outpatient attendances/yr; trust delivers integrated acute + community + intermediate-care services.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.820M"},
            {"label": "Trust scale", "value": "Tameside General + integrated community-clinic estate across Tameside + Glossopdale; c. 4,000 WTE"},
            {"label": "Principal hereditament", "value": "Tameside General Hospital (Fountain St, Ashton) + multiple smaller community-clinic hereditaments"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 — main hospital potentially in higher-tier band"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.72M → 2023-24 c. £0.79M → 2024-25 £0.820M — 2023 list revaluation + multiplier uplift"},
            {"label": "Billing authorities", "value": "Tameside Metropolitan Borough Council + High Peak Borough Council (Glossopdale)"},
            {"label": "Greater Manchester ICS", "value": "Member of GM ICB; collaborative E&F services across GM acute + community trusts"},
            {"label": "Integrated trust footprint", "value": "Acute hospital + multiple community-clinic hereditaments — broader rates exposure than acute-only DGHs"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + Tameside MBC + High Peak BC (billing)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + GM ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; Trust ARA 2023-24 disclosure; CQC RMP inspections; NAO local government finance reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation; trust appeal route via Check Challenge Appeal"}
        ],
        "notes": "Tameside and Glossop's business-rates line is shaped by the trust's integrated-care operating model — alongside the principal Tameside General Hospital hereditament, the trust holds multiple community-clinic and intermediate-care hereditaments scattered across Tameside borough plus Glossopdale (the cross-Pennine Derbyshire footprint). NHS trusts are not eligible for the mandatory 80% charitable rate relief. The 1 April 2026 next revaluation is the medium-term lever. The principal Tameside General hereditament potentially crosses the £500k+ RV threshold introduced by the NDR (Multipliers and Private Finance) Act 2024 from April 2025, attracting the higher-tier multiplier. The Glossopdale community estate is billed through High Peak Borough Council (a separate billing authority from Tameside MBC).",
        "sources": [
            {"publisher": "Tameside and Glossop Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.tamesidehospital.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Tameside and Glossop Integrated Care NHS Foundation Trust provider profile (RMP)", "url": "https://www.cqc.org.uk/provider/RMP"}
        ],
        "related": ["Tameside and Glossop Integrated Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Barnsley Hospital NHS Foundation Trust", "Amortisation — Tameside and Glossop Integrated Care NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — The Shrewsbury and Telford Hospital NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
        "description": "The Shrewsbury and Telford Hospital NHS Trust's £0.814M transport line covers staff business mileage (AfC Section 17 + AMAP), pool-fleet leases (IFRS 16 right-of-use), high-volume inter-site courier and pathology specimen transport between the Royal Shrewsbury Hospital (RSH) and the Princess Royal Hospital Telford (PRH) — c. 17 miles apart, with the trust's two-site clinical-services-reconfiguration unresolved — plus contracted non-emergency patient transport (NEPTS) for the Shropshire, Telford & Wrekin ICS catchment.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 500,000 catchment across Shropshire, Telford & Wrekin and mid-Wales border populations; c. 165,000 ED attendances/yr (RSH + PRH); c. 90,000 admissions/yr; c. 600,000 outpatient attendances/yr; trust runs the only acute services for a large rural footprint with significant cross-border Welsh patient flow.",
        "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.814M"},
            {"label": "Trust scale", "value": "Royal Shrewsbury Hospital + Princess Royal Hospital Telford (17mi apart) + community outreach; c. 5,500 WTE"},
            {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + structural inter-site RSH-PRH pathology/courier + contracted NEPTS"},
            {"label": "NEPTS provider", "value": "DHU Healthcare / Falck commissioned via Shropshire NEPTS framework"},
            {"label": "Two-site reconfiguration", "value": "Hospitals Transformation Programme — proposed split with emergency at RSH + planned care at PRH (delayed, decision pending)"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement + NEPTS rebooking spike"},
            {"label": "Ockenden context", "value": "Maternity-services scrutiny (Ockenden 2022 final report) drives HR/legal overhead, not directly transport"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via NEPTS contractor + agency-driver pass-through (15% over £5k)"},
            {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.65M → 2023-24 c. £0.78M → 2024-25 £0.814M — strike backfill + structural inter-site flow + fuel pass-through"},
            {"label": "Shropshire ICS", "value": "Member of Shropshire, Telford & Wrekin ICB; cross-border relationship with Powys Teaching HB (Wales)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + DHU Healthcare/Falck (NEPTS) + WMAS (when emergency overlap)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Patient Transport Services policy + DHSC + Shropshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Review 2021; Ockenden Report 2022; Trust ARA 2023-24; CQC RXW inspections (special measures history)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Hospitals-Transformation-Programme baseline · Successor: HTP-implementation-aligned site-specialisation (would dramatically reshape inter-site flow)"}
        ],
        "notes": "Shrewsbury and Telford Hospital NHS Trust's transport line is structurally elevated by the two-site geography (Royal Shrewsbury and Princess Royal Telford c. 17 miles apart) — every patient transfer, specimen courier and on-call rotation drives mileage. The Hospitals Transformation Programme (HTP) proposes a split of emergency care to RSH and planned care to PRH but has been delayed multiple times — implementation would materially change the inter-site flow. The Ockenden Inquiry into maternity services (final report 2022) drives HR/legal/inquiry-response overhead. The trust's cross-border patient flow with mid-Wales (Powys Teaching Health Board catchment) drives additional inter-trust patient-transport billing. April 2025 employer NIC step-up flows indirectly via NEPTS contracts.",
        "sources": [
            {"publisher": "The Shrewsbury and Telford Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sath.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Shrewsbury and Telford Hospital NHS Trust provider profile (RXW)", "url": "https://www.cqc.org.uk/provider/RXW"}
        ],
        "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Kettering General Hospital NHS Foundation Trust", "Ockenden Review", "NHS England"]
    },
    "Amortisation — Northern Lincolnshire and Goole NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Northern Lincolnshire and Goole NHS Foundation Trust"}],
        "description": "Northern Lincolnshire and Goole NHS FT's £0.802M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the trust's electronic-patient-record stack plus successor Frontline Digitisation modules deployed across the Diana Princess of Wales Hospital (Grimsby), Scunthorpe General Hospital and Goole and District Hospital, plus capitalised software for pathology, radiology and back-office systems. Humber and North Yorkshire ICS context. Group operating model with Hull University Teaching Hospitals.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 360,000 catchment across North East Lincolnshire, North Lincolnshire and East Riding (Goole); c. 130,000 ED attendances/yr (DPoW + Scunthorpe + Goole MIU); c. 80,000 admissions/yr; c. 470,000 outpatient attendances/yr; trust delivers acute services to a geographically spread rural and coastal catchment.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 3 (acquired-software treatment)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.802M"},
            {"label": "Trust scale", "value": "Diana Princess of Wales (Grimsby) + Scunthorpe General + Goole & District; c. 4,500 WTE"},
            {"label": "Principal intangibles", "value": "EPR stack + PACS/RIS imaging + e-prescribing + pathology LIMS + back-office software"},
            {"label": "EPR platform", "value": "Lorenzo legacy + Frontline Digitisation upgrade pathway via group with Hull University Teaching Hospitals"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; major EPR modules amortised over 7-10 yrs"},
            {"label": "Group with HUTH", "value": "Humber Health Partnership group operating model with Hull University Teaching Hospitals — drives shared digital roadmap"},
            {"label": "Frontline Digitisation pipeline", "value": "Ongoing capitalised module additions; Lorenzo convergence migration in scope"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.68M → 2023-24 c. £0.76M → 2024-25 £0.802M — Lorenzo run-out + module additions"},
            {"label": "Humber and North Yorkshire ICS", "value": "Member of Humber & North Yorkshire ICB; collaborative digital roadmap"},
            {"label": "Delivery body", "value": "Trust IT + Finance + DXC (Lorenzo legacy) + Frontline Digitisation programme team + HUTH (group partner)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + Humber & North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Lorenzo / NPfIT legacy reports; Trust ARA 2023-24 intangibles note; CQC RJL inspections (CQC special-measures history)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Lorenzo paper-record baseline · Successor: Frontline Digitisation new-EPR capitalisation tranche from 2025-27 in partnership with HUTH"}
        ],
        "notes": "NLAG's amortisation line is shaped by the Lorenzo (DXC/CSC) EPR legacy, with the trust now in NHSE's convergence cohort moving off Lorenzo. The Humber Health Partnership group operating model with Hull University Teaching Hospitals (HUTH) drives a shared digital roadmap — the successor EPR is likely to be procured jointly under Frontline Digitisation Wave 4-5, bringing a substantial capitalisation tranche from 2025-27. The trust's three-site geography across coastal, Humber-bank and East Riding catchments drives duplicated digital-infrastructure intangibles. CQC special-measures history (lifted/relifted multiple times since 2013) drives governance overhead but is not directly material to amortisation. Future EPR refresh is the medium-term cliff for the intangibles balance.",
        "sources": [
            {"publisher": "Northern Lincolnshire and Goole NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nlg.nhs.uk/about/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Northern Lincolnshire and Goole NHS Foundation Trust provider profile (RJL)", "url": "https://www.cqc.org.uk/provider/RJL"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 317, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"}
        ],
        "related": ["Northern Lincolnshire and Goole NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Hull University Teaching Hospitals NHS Trust", "Amortisation — Tameside and Glossop Integrated Care NHS Foundation Trust", "NHS England"]
    },
    "Lease expenditure — Portsmouth Hospitals University NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Portsmouth Hospitals University NHS Trust"}],
        "description": "Portsmouth Hospitals University NHS Trust's £0.787M lease-expenditure line covers IFRS 16 lease-payment costs for short-life and low-value leases (depreciation + interest captured separately on right-of-use assets) plus residual operating-lease tail under the post-2022 transition. Coverage includes pool-vehicle fleet, modular-clinical-building leases, satellite outpatient and community-clinic premises, plus office and IT-equipment leases supporting the Queen Alexandra Hospital (Cosham) footprint. Hampshire and Isle of Wight ICS context.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 675,000 south-east Hampshire catchment plus tertiary referral population for renal, oncology and major trauma; c. 175,000 ED attendances/yr at QA Hospital (designated trauma unit); c. 130,000 admissions/yr; c. 870,000 outpatient attendances/yr; trust holds a major trauma unit role within the Wessex trauma network.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (commercial leases) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.787M"},
            {"label": "Trust scale", "value": "Queen Alexandra Hospital (Cosham) + community + satellite estate; c. 8,500 WTE; major trauma unit"},
            {"label": "Composition", "value": "Short-life + low-value leases (P&L) + pool-vehicle fleet + modular-clinical-building leases + satellite community-clinic premises + IT/equipment leases"},
            {"label": "PFI context", "value": "QA Hospital is a major PFI scheme (£256M, opened 2009) — unitary charge captured separately under IFRIC 12 / IFRS 16 from PFI line"},
            {"label": "IFRS 16 transition", "value": "DHSC adopted IFRS 16 from 1 April 2022 — most leases now ROU asset on balance sheet; this line is residual operating-lease tail + low-value/short-life exemptions"},
            {"label": "Modular-building leases", "value": "Temporary modular-clinical-space leases for elective recovery + winter pressures + decant during refurbishment"},
            {"label": "Industrial action 2023-24 effect", "value": "Drove modular-clinical-space and pool-vehicle short-term lease extensions"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £2.4M → 2022-23 (IFRS 16) c. £0.7M residual → 2023-24 c. £0.76M → 2024-25 £0.787M — modular extensions + low-value tail"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via lessor pass-through (15% over £5k threshold)"},
            {"label": "Hampshire and Isle of Wight ICS", "value": "Member of HIOW ICB; collaborative procurement and shared-services frameworks"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + lessors (NHSPS, modular-build providers, vehicle-lease companies)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (IFRS 16 adoption) + HIOW ICB"},
            {"label": "Evaluation evidence", "value": "DHSC GAM ch.7 IFRS 16 implementation; Trust ARA 2023-24 lease note; CQC RHU inspections; NAO PFI report (re QA scheme)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease GAAP · Successor: ongoing modular + low-value-lease activity + future post-PFI estate refresh post-2032"}
        ],
        "notes": "Portsmouth Hospitals University NHS Trust's lease-expenditure line is the residual P&L charge after IFRS 16 adoption (1 April 2022) — the bulk of the trust's lease commitments now sit as right-of-use assets on the balance sheet with depreciation and interest separately captured. This residual line covers short-life leases (under 12 months), low-value-asset leases (under c. £5,000) and any operating-lease tail. The major QA Hospital PFI (£256M, opened 2009) unitary charge runs on a separate PFI/LIFT line. Modular clinical-building leases for elective recovery and winter pressures are the key flex driver. The 2023-24 industrial-action cycle drove modular-extension and pool-vehicle short-term-lease activity. April 2025 employer NIC step-up flows indirectly via lessor pass-through.",
        "sources": [
            {"publisher": "Portsmouth Hospitals University NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.porthosp.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "IFRS 16 Leases adoption in central government", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2023-24"},
            {"publisher": "Care Quality Commission", "title": "Portsmouth Hospitals University NHS Trust provider profile (RHU)", "url": "https://www.cqc.org.uk/provider/RHU"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"}
        ],
        "related": ["Portsmouth Hospitals University NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Portsmouth Hospitals University NHS Trust", "Lease expenditure — South Tyneside and Sunderland NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — County Durham and Darlington NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "County Durham and Darlington NHS Foundation Trust"}],
        "description": "County Durham and Darlington NHS FT's £0.786M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the trust's electronic-patient-record stack plus successor Frontline Digitisation modules deployed across the University Hospital of North Durham, Darlington Memorial Hospital, Bishop Auckland Hospital and community-clinic estate, plus capitalised software for pathology, radiology and back-office systems. The trust's geographically dispersed estate drives multi-site digital-infrastructure intangibles. North East and North Cumbria ICS context.",
        "beneficiaries": "c. 7,800 WTE staff serving a c. 650,000 catchment across County Durham, Darlington and Tees Valley borders; c. 200,000 ED attendances/yr (UHND + Darlington + Bishop Auckland UCC); c. 130,000 admissions/yr; c. 850,000 outpatient attendances/yr; trust runs PFI-financed estate alongside the Bishop Auckland reconfigured site.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 3 (acquired-software treatment)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.786M"},
            {"label": "Trust scale", "value": "UH North Durham + Darlington Memorial + Bishop Auckland + community estate; c. 7,800 WTE"},
            {"label": "Principal intangibles", "value": "EPR stack + PACS/RIS imaging + e-prescribing + pathology LIMS + back-office software"},
            {"label": "EPR platform", "value": "Cerner Millennium + Frontline Digitisation upgrade pathway under NHSE Wave 3-4"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; major EPR modules amortised over 7-10 yrs; PACS image storage ~10 years"},
            {"label": "Frontline Digitisation pipeline", "value": "Ongoing capitalised module additions (clinical noting, decision-support, mobile apps)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.66M → 2023-24 c. £0.74M → 2024-25 £0.786M — Cerner mid-life amortisation + module additions"},
            {"label": "PFI context", "value": "UH North Durham PFI scheme (1990s vintage) and Bishop Auckland reconfiguration shape estate but separately captured under PFI/LIFT charges"},
            {"label": "North East and North Cumbria ICS", "value": "Member of NENC ICB; collaborative digital roadmap with Northumbria, North Tees, Newcastle"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Cerner (Oracle Health) + Frontline Digitisation programme team + ICS digital lead"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + NENC ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation reports; Trust ARA 2023-24 intangibles note; CQC RXP inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner paper-record baseline · Successor: Frontline Digitisation Wave 4-5 module deployment + future EPR refresh-cycle (2030+)"}
        ],
        "notes": "County Durham and Darlington NHS FT's amortisation line is shaped by Cerner Millennium EPR mid-life amortisation under IAS 38 useful-economic-life conventions, plus continued Frontline Digitisation module additions. The trust's geographically dispersed multi-site estate (UHND, Darlington Memorial, Bishop Auckland, plus community clinics) drives broader digital-infrastructure intangibles than single-site DGHs. The Bishop Auckland Hospital reconfiguration (urgent-care centre, planned care, community focus) reshaped the trust's estate footprint but does not directly drive amortisation. The PFI-financed estate at UHND is captured under a separate PFI/LIFT line. Future EPR refresh-cycle (likely 2030+) is the medium-term cliff for the intangibles balance.",
        "sources": [
            {"publisher": "County Durham and Darlington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cddft.nhs.uk/about-us/publications-and-reports.aspx"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "County Durham and Darlington NHS Foundation Trust provider profile (RXP)", "url": "https://www.cqc.org.uk/provider/RXP"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 317, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"}
        ],
        "related": ["County Durham and Darlington NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — County Durham and Darlington NHS Foundation Trust", "Amortisation — Northern Lincolnshire and Goole NHS Foundation Trust", "NHS England"]
    },
    "Lease expenditure — South Tyneside and Sunderland NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "South Tyneside and Sunderland NHS Foundation Trust"}],
        "description": "South Tyneside and Sunderland NHS FT's £0.780M lease-expenditure line covers IFRS 16 lease-payment costs for short-life and low-value leases (depreciation + interest captured separately on right-of-use assets) plus residual operating-lease tail under the post-2022 transition. Coverage includes pool-vehicle fleet, modular-clinical-building leases, satellite outpatient and community-clinic premises, plus office and IT-equipment leases supporting Sunderland Royal Hospital, South Tyneside District Hospital and integrated community estate. North East and North Cumbria ICS context.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 430,000 catchment across Sunderland and South Tyneside (South Shields, Jarrow, Hebburn, Boldon); c. 200,000 ED attendances/yr (Sunderland Royal + South Tyneside ED); c. 130,000 admissions/yr; c. 850,000 outpatient attendances/yr; trust formed by 2019 merger of South Tyneside FT + City Hospitals Sunderland.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (commercial leases) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.780M"},
            {"label": "Trust scale", "value": "Sunderland Royal + South Tyneside District + integrated community estate; c. 8,500 WTE; 2019 merger entity"},
            {"label": "Composition", "value": "Short-life + low-value leases (P&L) + pool-vehicle fleet + modular-clinical-building leases + satellite community-clinic premises + IT/equipment leases"},
            {"label": "IFRS 16 transition", "value": "DHSC adopted IFRS 16 from 1 April 2022 — most leases now ROU asset on balance sheet; this line is residual operating-lease tail + low-value/short-life exemptions"},
            {"label": "Modular-building leases", "value": "Temporary modular-clinical-space leases for elective recovery + winter pressures + decant during refurbishment"},
            {"label": "Industrial action 2023-24 effect", "value": "Drove modular-clinical-space and pool-vehicle short-term lease extensions"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £2.3M → 2022-23 (IFRS 16) c. £0.7M residual → 2023-24 c. £0.75M → 2024-25 £0.780M — modular extensions + post-merger estate consolidation tail"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via lessor pass-through (15% over £5k threshold)"},
            {"label": "Post-merger estate", "value": "2019 merger drove duplicated lease commitments + ongoing rationalisation of community-clinic footprint"},
            {"label": "North East and North Cumbria ICS", "value": "Member of NENC ICB; collaborative procurement and shared-services frameworks"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + lessors (NHSPS, modular-build providers, vehicle-lease companies)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (IFRS 16 adoption) + NENC ICB"},
            {"label": "Evaluation evidence", "value": "DHSC GAM ch.7 IFRS 16 implementation; Trust ARA 2023-24 lease note; CQC R0B inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease GAAP + pre-2019-merger separate trust leases · Successor: ongoing modular + low-value-lease activity + post-merger estate rationalisation"}
        ],
        "notes": "South Tyneside and Sunderland NHS FT's lease-expenditure line is the residual P&L charge after IFRS 16 adoption (1 April 2022) — the bulk of the trust's lease commitments now sit as right-of-use assets on the balance sheet. The 2019 merger of South Tyneside FT and City Hospitals Sunderland generated duplicated community-clinic and back-office lease commitments that the merged trust has been rationalising. Modular clinical-building leases for elective recovery, winter pressures and decant are the key flex driver. The 2023-24 industrial-action cycle drove modular-extension and pool-vehicle short-term-lease activity. April 2025 employer NIC step-up flows indirectly via lessor pass-through.",
        "sources": [
            {"publisher": "South Tyneside and Sunderland NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stsft.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "IFRS 16 Leases adoption in central government", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2023-24"},
            {"publisher": "Care Quality Commission", "title": "South Tyneside and Sunderland NHS Foundation Trust provider profile (R0B)", "url": "https://www.cqc.org.uk/provider/R0B"},
            {"publisher": "NHS Property Services", "title": "About NHS Property Services", "url": "https://www.property.nhs.uk/about-us/"}
        ],
        "related": ["South Tyneside and Sunderland NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Portsmouth Hospitals University NHS Trust", "Amortisation — County Durham and Darlington NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — East Cheshire NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "East Cheshire NHS Trust"}],
        "description": "East Cheshire NHS Trust's £0.773M business-rates line covers non-domestic rate liability across the Macclesfield District General Hospital site (Victoria Road, Macclesfield) plus community-clinic and intermediate-care estate at Congleton War Memorial Hospital, Knutsford and District Community Hospital and outreach sites. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Cheshire and Merseyside ICS context.",
        "beneficiaries": "c. 2,800 WTE staff serving a c. 200,000 east Cheshire catchment (Macclesfield, Congleton, Knutsford, Wilmslow, Poynton); c. 60,000 ED attendances/yr at Macclesfield DGH; c. 40,000 admissions/yr; c. 220,000 outpatient attendances/yr; trust delivers integrated acute + community + intermediate-care services to a rural and semi-rural population.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.773M"},
            {"label": "Trust scale", "value": "Macclesfield DGH + Congleton War Memorial + Knutsford & District Community Hospital + outreach; c. 2,800 WTE"},
            {"label": "Principal hereditaments", "value": "Macclesfield DGH (main) + multiple community-hospital and clinic hereditaments"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 — main hospital potentially in higher-tier band"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.68M → 2023-24 c. £0.74M → 2024-25 £0.773M — 2023 list revaluation + multiplier uplift"},
            {"label": "Billing authorities", "value": "Cheshire East Council (unitary) — covers Macclesfield, Congleton, Knutsford"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of Cheshire & Merseyside ICB; small-trust collaborative-procurement participant"},
            {"label": "Integrated trust footprint", "value": "Acute hospital + community hospitals + intermediate-care estate — broader rates exposure than acute-only DGHs"},
            {"label": "Trust strategic context", "value": "Long-running speculation re possible merger with Mid Cheshire / Stockport — would consolidate rates billing"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + Cheshire East Council (billing)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; Trust ARA 2023-24 disclosure; CQC RJN inspections; NAO local government finance reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation; possible trust-merger consolidation"}
        ],
        "notes": "East Cheshire NHS Trust's business-rates line is shaped by a small-trust footprint with one main acute site (Macclesfield DGH) plus multiple smaller community-hospital and clinic hereditaments across affluent east-Cheshire towns (Congleton, Knutsford, Wilmslow, Poynton). NHS trusts are not eligible for the mandatory 80% charitable rate relief. The 1 April 2026 next revaluation is the medium-term lever — affluent east-Cheshire commercial-property values may drive material upward revaluation. Long-running speculation about a possible trust merger with Mid Cheshire or Stockport could consolidate future rates billing. The Macclesfield DGH hereditament potentially crosses the £500k+ RV threshold introduced by the NDR (Multipliers and Private Finance) Act 2024 from April 2025.",
        "sources": [
            {"publisher": "East Cheshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastcheshire.nhs.uk/About-The-Trust/publications.htm"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "East Cheshire NHS Trust provider profile (RJN)", "url": "https://www.cqc.org.uk/provider/RJN"}
        ],
        "related": ["East Cheshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Barnsley Hospital NHS Foundation Trust", "Business rates — Tameside and Glossop Integrated Care NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Dorset County Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Dorset County Hospital NHS Foundation Trust"}],
        "description": "Dorset County Hospital NHS FT's £0.764M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the trust's electronic-patient-record stack plus successor Frontline Digitisation modules deployed at the Dorset County Hospital (Williams Avenue, Dorchester) plus satellite outpatient and community-clinic estate. The trust serves a largely rural Dorset catchment from a single main acute hereditament. Dorset ICS context. New Hospital Programme cohort member with a full-rebuild scheme.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 215,000 west and north Dorset catchment (Dorchester, Weymouth, Bridport, Sherborne, Blandford); c. 60,000 ED attendances/yr; c. 50,000 admissions/yr; c. 230,000 outpatient attendances/yr; trust covers a rural catchment with significant tourist-season seasonal-population uplift.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 3 (acquired-software treatment)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.764M"},
            {"label": "Trust scale", "value": "Dorset County Hospital (Dorchester) + satellite clinics; c. 3,500 WTE; single-site DGH"},
            {"label": "Principal intangibles", "value": "EPR stack + PACS/RIS imaging + e-prescribing + pathology LIMS + back-office software"},
            {"label": "EPR platform", "value": "System C Careflow + Frontline Digitisation upgrade pathway"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; major EPR modules amortised over 7-10 yrs; PACS image storage ~10 years"},
            {"label": "New Hospital Programme cohort", "value": "DCH was in original NHP-40 cohort with full-rebuild scheme — Reset Jan 2025 deferred delivery to 2030s"},
            {"label": "Frontline Digitisation pipeline", "value": "Ongoing capitalised module additions; pre-NHP-rebuild digital-readiness investment"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.65M → 2023-24 c. £0.72M → 2024-25 £0.764M — System C mid-life amortisation + module additions"},
            {"label": "Dorset ICS", "value": "Member of NHS Dorset ICB; collaborative digital roadmap with University Hospitals Dorset"},
            {"label": "Delivery body", "value": "Trust IT + Finance + System C + Frontline Digitisation programme team + ICS digital lead"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + NHS Dorset ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation reports; NAO New Hospital Programme reports; Trust ARA 2023-24 intangibles note; CQC RBD inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-System C paper-record baseline · Successor: Frontline Digitisation Wave 4-5 module deployment + NHP-rebuild digital-greenfield capitalisation tranche from 2030s"}
        ],
        "notes": "Dorset County Hospital NHS FT's amortisation line is shaped by System C Careflow EPR mid-life amortisation under IAS 38 useful-economic-life conventions, plus continued Frontline Digitisation module additions. The trust was in the original New Hospital Programme 40-hospitals cohort with a full-rebuild scheme — the January 2025 NHP Reset deferred its delivery to the 2030s, pushing the digital-greenfield capitalisation tranche far into the future. The trust's small single-site DGH scale gives a lower intangibles base than tertiary peers, but the rural west-Dorset geography drives outreach-clinic system additions. The trust collaborates closely with University Hospitals Dorset (Bournemouth/Poole) on the Dorset Digital Care Record. Future EPR refresh plus eventual NHP rebuild are the medium-term cliffs.",
        "sources": [
            {"publisher": "Dorset County Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Dorset County Hospital NHS Foundation Trust provider profile (RBD)", "url": "https://www.cqc.org.uk/provider/RBD"},
            {"publisher": "National Audit Office", "title": "The New Hospital Programme (HC 1662, 2023-24)", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"}
        ],
        "related": ["Dorset County Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Amortisation — County Durham and Darlington NHS Foundation Trust", "NHS England"]
    },
    "Lease expenditure — East And North Hertfordshire NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "East And North Hertfordshire NHS Trust"}],
        "description": "East and North Hertfordshire NHS Trust's £0.759M lease-expenditure line covers IFRS 16 lease-payment costs for short-life and low-value leases (depreciation + interest captured separately on right-of-use assets) plus residual operating-lease tail under the post-2022 transition. Coverage includes pool-vehicle fleet, modular-clinical-building leases, satellite outpatient and community-clinic premises, plus office and IT-equipment leases supporting the Lister Hospital (Stevenage), Mount Vernon Cancer Centre (Northwood) and New QEII Hospital (Welwyn Garden City). Hertfordshire and West Essex ICS context.",
        "beneficiaries": "c. 5,800 WTE staff serving a c. 600,000 east and north Hertfordshire catchment plus a north-west London tertiary cancer-centre population for Mount Vernon; c. 130,000 ED attendances/yr at Lister; c. 90,000 admissions/yr; c. 700,000 outpatient attendances/yr; trust hosts Mount Vernon Cancer Centre (regional tertiary cancer centre in Hillingdon serving north-west London + Herts).",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (commercial leases) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.759M"},
            {"label": "Trust scale", "value": "Lister Hospital (Stevenage) + Mount Vernon Cancer Centre + New QEII (Welwyn) + community estate; c. 5,800 WTE"},
            {"label": "Composition", "value": "Short-life + low-value leases (P&L) + pool-vehicle fleet + modular-clinical-building leases + satellite community-clinic premises + IT/equipment leases"},
            {"label": "Mount Vernon context", "value": "Regional tertiary cancer centre on Hillingdon site — drives sub-leases from London Northwest landlord arrangement; Mount Vernon Future Plan reconfiguration in scope"},
            {"label": "IFRS 16 transition", "value": "DHSC adopted IFRS 16 from 1 April 2022 — most leases now ROU asset on balance sheet; this line is residual operating-lease tail + low-value/short-life exemptions"},
            {"label": "Modular-building leases", "value": "Temporary modular-clinical-space leases for elective recovery + winter pressures + decant during refurbishment"},
            {"label": "Industrial action 2023-24 effect", "value": "Drove modular-clinical-space and pool-vehicle short-term lease extensions"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £2.2M → 2022-23 (IFRS 16) c. £0.7M residual → 2023-24 c. £0.73M → 2024-25 £0.759M — modular extensions + Mount Vernon ongoing flex"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via lessor pass-through (15% over £5k threshold)"},
            {"label": "Hertfordshire and West Essex ICS", "value": "Member of HWE ICB; collaborative procurement and shared-services frameworks"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + lessors (NHSPS, modular-build providers, vehicle-lease companies)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (IFRS 16 adoption) + HWE ICB"},
            {"label": "Evaluation evidence", "value": "DHSC GAM ch.7 IFRS 16 implementation; Trust ARA 2023-24 lease note; CQC RWH inspections; NHSE Mount Vernon Future Plan reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease GAAP · Successor: ongoing modular + low-value-lease activity + Mount Vernon Future Plan reconfiguration"}
        ],
        "notes": "East and North Hertfordshire NHS Trust's lease-expenditure line is the residual P&L charge after IFRS 16 adoption (1 April 2022). The trust is unusual among acute trusts in operating Mount Vernon Cancer Centre on a Hillingdon site (London Northwest University Hospitals landlord) — generating sub-lease and licence-fee arrangements on a non-trust-owned estate. The Mount Vernon Future Plan (NHSE-led reconfiguration to relocate cancer services) is in long-running scoping, with capital-investment decisions pending. Modular clinical-building leases for elective recovery and winter pressures are the key flex driver. The 2023-24 industrial-action cycle drove modular-extension and pool-vehicle short-term-lease activity. April 2025 employer NIC step-up flows indirectly via lessor pass-through.",
        "sources": [
            {"publisher": "East and North Hertfordshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.enherts-tr.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Mount Vernon Cancer Centre Strategic Review", "url": "https://www.england.nhs.uk/london/our-work/specialised-commissioning/mvcc/"},
            {"publisher": "Care Quality Commission", "title": "East and North Hertfordshire NHS Trust provider profile (RWH)", "url": "https://www.cqc.org.uk/provider/RWH"},
            {"publisher": "HM Treasury", "title": "IFRS 16 Leases adoption in central government", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2023-24"}
        ],
        "related": ["East And North Hertfordshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — South Tyneside and Sunderland NHS Foundation Trust", "Lease expenditure — Portsmouth Hospitals University NHS Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "East Lancashire Hospitals NHS Trust's £0.744M lease-expenditure line covers IFRS 16 lease-payment costs for short-life and low-value leases (depreciation + interest captured separately on right-of-use assets) plus residual operating-lease tail under the post-2022 transition. Coverage includes pool-vehicle fleet, modular-clinical-building leases, satellite outpatient and community-clinic premises across Royal Blackburn Teaching Hospital, Burnley General Teaching Hospital, Pendle Community Hospital, Clitheroe Community Hospital and Accrington Victoria Hospital. Lancashire and South Cumbria ICS context.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 530,000 east Lancashire catchment (Blackburn with Darwen, Burnley, Hyndburn, Pendle, Ribble Valley, Rossendale); c. 200,000 ED attendances/yr at Royal Blackburn + Burnley UCC; c. 130,000 admissions/yr; c. 850,000 outpatient attendances/yr; trust delivers acute services to a deprived east-Lancashire population.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (commercial leases) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.744M"},
            {"label": "Trust scale", "value": "Royal Blackburn + Burnley General + Pendle + Clitheroe + Accrington Victoria; c. 8,500 WTE"},
            {"label": "Composition", "value": "Short-life + low-value leases (P&L) + pool-vehicle fleet + modular-clinical-building leases + community-clinic premises + IT/equipment leases"},
            {"label": "PFI context", "value": "Royal Blackburn (Phase 5) and Burnley General (Phase 6) PFI schemes — unitary charges captured separately under PFI/LIFT line"},
            {"label": "IFRS 16 transition", "value": "DHSC adopted IFRS 16 from 1 April 2022 — most leases now ROU asset on balance sheet; this line is residual operating-lease tail + low-value/short-life exemptions"},
            {"label": "Modular-building leases", "value": "Temporary modular-clinical-space leases for elective recovery + winter pressures + decant during refurbishment"},
            {"label": "Industrial action 2023-24 effect", "value": "Drove modular-clinical-space and pool-vehicle short-term lease extensions"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £2.0M → 2022-23 (IFRS 16) c. £0.65M residual → 2023-24 c. £0.71M → 2024-25 £0.744M — modular extensions + community-clinic estate flex"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via lessor pass-through (15% over £5k threshold)"},
            {"label": "Lancashire and South Cumbria ICS", "value": "Member of LSC ICB; collaborative procurement and shared-services frameworks"},
            {"label": "Multi-site community estate", "value": "Five-site footprint drives broader satellite-clinic lease commitments than single-site DGHs"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + lessors (NHSPS, modular-build providers, vehicle-lease companies)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (IFRS 16 adoption) + LSC ICB"},
            {"label": "Evaluation evidence", "value": "DHSC GAM ch.7 IFRS 16 implementation; Trust ARA 2023-24 lease note; CQC RXR inspections; NAO PFI report (re Phase 5/6 schemes)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease GAAP · Successor: ongoing modular + low-value-lease activity + community-estate consolidation"}
        ],
        "notes": "East Lancashire Hospitals NHS Trust's lease-expenditure line is the residual P&L charge after IFRS 16 adoption (1 April 2022). The trust's two PFI schemes (Royal Blackburn Phase 5 and Burnley General Phase 6) generate separate unitary charges captured under the PFI/LIFT line — this lease line covers short-life, low-value and modular-clinical-space activity outside those PFI envelopes. The five-site community-and-acute footprint drives broader satellite-clinic lease commitments than single-site peers. The 2023-24 industrial-action cycle drove modular-extension and pool-vehicle short-term-lease activity. April 2025 employer NIC step-up flows indirectly via lessor pass-through. The trust serves a notably deprived east-Lancashire population (Blackburn with Darwen and Burnley among lower decile IMD).",
        "sources": [
            {"publisher": "East Lancashire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.elht.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "IFRS 16 Leases adoption in central government", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2023-24"},
            {"publisher": "Care Quality Commission", "title": "East Lancashire Hospitals NHS Trust provider profile (RXR)", "url": "https://www.cqc.org.uk/provider/RXR"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"}
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — East And North Hertfordshire NHS Trust", "Lease expenditure — South Tyneside and Sunderland NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Dartford and Gravesham NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Dartford and Gravesham NHS Trust"}],
        "description": "Dartford and Gravesham NHS Trust's £0.717M transport line covers staff business mileage (AfC Section 17 + AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between Darent Valley Hospital (Dartford) and the Gravesham Community Hospital footprint, plus contracted non-emergency patient transport (NEPTS) for the Kent and Medway ICS catchment serving north-west Kent. The trust's Darent Valley site is one of the early PFI schemes (1999) which shapes facilities-management context but is captured under PFI/LIFT line.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 500,000 north-west Kent catchment (Dartford, Gravesend, Swanley, parts of Bexley borough); c. 130,000 ED attendances/yr at Darent Valley; c. 80,000 admissions/yr; c. 480,000 outpatient attendances/yr; trust serves a heavily commuter-population catchment with cross-river M25/Dartford-Crossing access dynamics.",
        "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.717M"},
            {"label": "Trust scale", "value": "Darent Valley Hospital (Dartford) + Gravesham Community Hospital + outreach; c. 4,000 WTE; PFI estate"},
            {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site Dartford-Gravesham courier + contracted NEPTS"},
            {"label": "NEPTS provider", "value": "G4S NEPTS / South Central Ambulance NEPTS framework — Kent & Medway commissioning"},
            {"label": "PFI context", "value": "Darent Valley Hospital was one of the first major NHS PFI schemes (opened 2000) — FM contract via The Hospital Company; transport ringfenced separately"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement + NEPTS rebooking spike"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via NEPTS contractor + agency-driver pass-through (15% over £5k threshold)"},
            {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.55M → 2023-24 c. £0.68M → 2024-25 £0.717M — strike backfill + Dartford Crossing fuel/access cost + NEPTS uplift"},
            {"label": "Kent and Medway ICS", "value": "Member of Kent & Medway ICB; collaborative NEPTS commissioning with neighbouring Kent acute trusts"},
            {"label": "Cross-river dynamics", "value": "Dartford Crossing toll + M25 congestion drives staff travel time + agency mileage premium"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + G4S/SCAS (NEPTS) + SECAmb (when emergency overlap)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Patient Transport Services policy + DHSC + Kent & Medway ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Review 2021; Trust ARA 2023-24; CQC RN7 inspections; NAO PFI report (re Darent Valley early-vintage scheme)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-retender baseline · Successor: NEPTS-Review-aligned eligibility implementation + ongoing PFI-end-of-contract (2032) transport implications"}
        ],
        "notes": "Dartford and Gravesham NHS Trust's transport line is shaped by the Darent Valley Hospital PFI estate (one of the first major NHS PFI schemes, opened 2000, contract running to 2032) — facilities management is delivered via The Hospital Company (consortium SPV) but transport sits outside the PFI envelope on the trust P&L. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) drove locum travel reimbursement and NEPTS rebooking. The trust's north-west Kent catchment has notable Dartford Crossing toll and M25 congestion dynamics that elevate staff travel-time costs and agency-mileage premiums. The PFI 2032 end-of-contract is a major medium-term planning event (estate handback) that may reshape transport logistics. April 2025 employer NIC step-up flows indirectly via NEPTS contracts.",
        "sources": [
            {"publisher": "Dartford and Gravesham NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dgt.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Dartford and Gravesham NHS Trust provider profile (RN7)", "url": "https://www.cqc.org.uk/provider/RN7"}
        ],
        "related": ["Dartford and Gravesham NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — The Shrewsbury and Telford Hospital NHS Trust", "Transport (business + patient) — Kettering General Hospital NHS Foundation Trust", "NHS England"]
    },
}
