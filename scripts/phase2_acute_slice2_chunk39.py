# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 39 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — East Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "East Sussex Healthcare NHS Trust"}],
        "description": "East Sussex Healthcare NHS Trust's £0.711M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly EPR/PAS software (Sunrise Allscripts/Oracle Health), PACS imaging archives, capitalised digital-pathology assets and back-office software deployed across Conquest Hospital (Hastings), Eastbourne District General Hospital and the Bexhill Hospital community footprint. The trust's coastal-elderly catchment and stroke/cardiac specialist services drive bespoke clinical-software intangibles. Sussex Health and Care ICS context.",
        "beneficiaries": "c. 7,000 WTE staff serving a c. 525,000 East Sussex catchment (Hastings, Rother, Eastbourne, Wealden, Lewes); c. 165,000 ED attendances/yr; c. 95,000 admissions/yr; c. 580,000 outpatient attendances/yr; trust serves disproportionately elderly coastal population with high frailty, stroke and cardiac demand.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 3 (acquired-software treatment) — IAS 36 (impairment interaction)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.711M"},
            {"label": "Trust scale", "value": "Conquest Hospital + Eastbourne DGH + Bexhill Hospital + community sites; c. 7,000 WTE"},
            {"label": "Principal intangibles", "value": "EPR/PAS software + PACS/RIS imaging + e-prescribing modules + pathology LIMS + back-office software"},
            {"label": "EPR platform", "value": "Sunrise (Allscripts/Oracle Health) heritage with Frontline Digitisation alignment"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; major EPR modules amortised over 7-10 yrs; PACS image storage ~10 years"},
            {"label": "Frontline Digitisation pipeline", "value": "Trust within NHSE Frontline Digitisation cohort — capitalisation/amortisation profile shifting as new EPR tranches go live"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.55M → 2023-24 c. £0.66M → 2024-25 £0.711M — module additions + new-EPR amortisation kicking in"},
            {"label": "Sussex Health and Care ICS", "value": "Member of Sussex ICB; shared digital and pathology arrangements with UHSussex and Maidstone & Tunbridge Wells"},
            {"label": "Coastal-elderly demand", "value": "Stroke/frailty/cardiac specialism shapes clinical-software intangibles (e.g. stroke-pathway, cardiac-imaging modules)"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Allscripts/Oracle Health + Frontline Digitisation programme team + ICS digital lead"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + Sussex ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangibles note; NAO digital-transformation reports; CQC RXC inspections; DHSC GAM compliance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Sunrise paper-PAS baseline · Successor: Frontline Digitisation EPR refresh + AI-imaging modules + community-EPR convergence"}
        ],
        "notes": "ESHT's amortisation line is shaped by the Sunrise EPR/PAS heritage and the Frontline Digitisation refresh path — the trust came out of CQC special measures in 2018 and has rebuilt digital infrastructure since, driving steady intangibles growth. CQC most recently rated the trust 'Good' overall (2023). The Conquest-Eastbourne two-site model means duplicated PACS/RIS storage and dual EPR modules historically — convergence under the Frontline Digitisation programme should rationalise this from 2025-27. Coastal-elderly demand and stroke specialism drive bespoke clinical-pathway software capitalisation. Future intangibles balance step-up expected as Frontline Digitisation EPR tranches go live.",
        "sources": [
            {"publisher": "East Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esht.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "East Sussex Healthcare NHS Trust provider profile (RXC)", "url": "https://www.cqc.org.uk/provider/RXC"},
            {"publisher": "Sussex Integrated Care Board", "title": "Sussex ICS digital strategy", "url": "https://www.sussex.ics.nhs.uk/"}
        ],
        "related": ["East Sussex Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "NHS England Frontline Digitisation", "Department of Health and Social Care", "Sussex Integrated Care Board"]
    },
    "Business rates — James Paget University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "James Paget University Hospitals NHS Foundation Trust"}],
        "description": "James Paget University Hospitals NHS FT's £0.711M business-rates line covers non-domestic rates payable to Great Yarmouth Borough Council on the trust's hospital estate centred on the James Paget University Hospital (Gorleston-on-Sea) plus satellite sites. Rates are levied on Valuation Office Agency (VOA) rateable values under the Local Government Finance Act 1988, with NHS bodies receiving no charitable relief. The 2023 revaluation reset rateable values; the trust's 1980s-build PFI estate has specific RAAC remediation context. Norfolk & Waveney ICS context.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 230,000 catchment across Great Yarmouth, Waveney (Lowestoft) and east Norfolk; c. 75,000 ED attendances/yr; c. 50,000 admissions/yr; c. 270,000 outpatient attendances/yr; trust serves coastal-elderly population with high deprivation in Great Yarmouth and Lowestoft.",
        "legal_basis": "Local Government Finance Act 1988 — Non-Domestic Rating Act 2023 — VOA 2023 revaluation list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.711M"},
            {"label": "Trust scale", "value": "James Paget University Hospital (Gorleston-on-Sea) + satellite sites; c. 3,500 WTE"},
            {"label": "Billing authority", "value": "Great Yarmouth Borough Council (collecting authority)"},
            {"label": "Rateable value basis", "value": "VOA 2023 revaluation list — antecedent valuation date 1 April 2021"},
            {"label": "Charitable relief", "value": "Not applicable — NHS trusts/FTs are public-sector bodies, no mandatory 80% charitable relief (unlike charities)"},
            {"label": "RAAC context", "value": "James Paget hospital is a designated 'New Hospital Programme' RAAC-rebuild site — full reconstruction under NHP cohort"},
            {"label": "Multiplier 2024-25", "value": "Standard multiplier 54.6p; small-business multiplier 49.9p (NHS estate uses standard)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.61M → 2023-24 c. £0.69M → 2024-25 £0.711M — 2023 revaluation step-up + multiplier inflation"},
            {"label": "Norfolk & Waveney ICS", "value": "Member of Norfolk & Waveney ICB; estate strategy aligned with NNUH and Queen Elizabeth King's Lynn"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + VOA (valuation) + Great Yarmouth BC (billing) + DLUHC/MHCLG (policy)"},
            {"label": "Policy owner", "value": "MHCLG (business-rates policy) + HM Treasury + DHSC + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "VOA rating list public record; NAO Business Rates report 2014; HMT Business Rates Review 2021; New Hospital Programme NAO reports on RAAC"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list · Successor: 2026 revaluation; New Hospital Programme rebuild will reset rateable values on completion"}
        ],
        "notes": "JPUH's business-rates line is materially shaped by the New Hospital Programme RAAC rebuild — JPUH is one of seven RAAC-construction hospitals confirmed for full reconstruction (October 2023 NHP announcement), with completion targeted for 2030. RAAC remediation is concentrated in the planks/roof of the existing 1982-build hospital. Recent context: NAO July 2023 report on NHP delivery flagged RAAC trusts as priority cohort; January 2025 government reset of NHP timelines pushed JPUH delivery later. The trust's coastal/deprivation catchment and 1980s estate drive ongoing maintenance overhead until rebuild completes. CQC rated the trust 'Good' overall (2022 inspection).",
        "sources": [
            {"publisher": "James Paget University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.jpaget.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List — find a business rates valuation", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care / NHS England", "title": "New Hospital Programme — RAAC cohort", "url": "https://www.gov.uk/government/publications/new-hospital-programme"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, 17 July 2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "HM Treasury", "title": "Business Rates Review final report (October 2021)", "url": "https://www.gov.uk/government/publications/business-rates-review-final-report"}
        ],
        "related": ["James Paget University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Norfolk and Waveney Integrated Care Board", "Valuation Office Agency"]
    },
    "Lease expenditure — East Kent Hospitals University NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "East Kent Hospitals University NHS Foundation Trust"}],
        "description": "East Kent Hospitals University NHS FT's £0.708M lease-expenditure line covers IFRS 16 short-term/low-value lease costs and pre-IFRS-16 operating-lease residuals across the trust's three-acute-site footprint — William Harvey Hospital (Ashford), Queen Elizabeth The Queen Mother Hospital (Margate) and Kent and Canterbury Hospital — plus community/clinic lease commitments across east Kent. Drivers include modular-ward leases, equipment leases (imaging, pathology), vehicle/fleet leases and satellite-clinic premises. Kent and Medway ICS context.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 760,000 east Kent catchment (Ashford, Canterbury, Dover, Folkestone & Hythe, Thanet); c. 200,000 ED attendances/yr; c. 130,000 admissions/yr; c. 740,000 outpatient attendances/yr; trust delivers tertiary services for cardiology, vascular and renal across east Kent.",
        "legal_basis": "IFRS 16 Leases (HMT FReM-adapted) — DHSC Group Accounting Manual 2024-25 chapter 7 — NHS Act 2006 — Health and Care Act 2022 — IAS 17 (legacy operating-lease treatment for transition)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.708M (P&L charge for short-term/low-value leases + variable lease payments)"},
            {"label": "Trust scale", "value": "William Harvey (Ashford) + QEQM (Margate) + Kent & Canterbury + community sites; c. 8,500 WTE"},
            {"label": "IFRS 16 adoption", "value": "Adopted by NHS bodies from 1 April 2022 per HMT FReM (deferred from 2019)"},
            {"label": "Composition", "value": "Modular-ward leases + imaging-equipment leases (MRI/CT) + pathology analyser leases + vehicle/fleet leases + satellite-clinic premises"},
            {"label": "Right-of-use asset interaction", "value": "Major leases capitalised as ROU assets — depreciation runs through depreciation line; lease line captures only short-term/low-value/variable"},
            {"label": "Modular wards", "value": "East Kent has been a national hotspot for modular-ward deployment (winter capacity, RAAC mitigation) — Vanguard / ModuleCo lease arrangements"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.55M → 2023-24 c. £0.65M → 2024-25 £0.708M — modular-ward rentals + winter-capacity surge leases"},
            {"label": "Kent and Medway ICS", "value": "Member of Kent and Medway ICB; estate-strategy alignment with Medway NHS FT and Maidstone & Tunbridge Wells"},
            {"label": "Maternity context", "value": "Reading 2022 maternity report (Bill Kirkup) shaped governance overhead but not directly lease-line driver"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + Procurement + ModuleCo/Vanguard (modular wards) + NHS Shared Business Services (lease admin)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (FReM/IFRS 16) + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HMT FReM IFRS 16 adaptation; NAO winter-capacity reports; CQC RVV inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: IAS 17 operating-lease treatment pre-2022 · Successor: IFRS 16 ROU-asset capitalisation; modular-ward pipeline tied to RAAC mitigation"}
        ],
        "notes": "East Kent's lease line is shaped by modular-ward leases for winter-capacity surge — the trust has historically operated some of the largest temporary-ward footprints in NHS England, deployed via Vanguard Healthcare Solutions and ModuleCo. The 2022 Kirkup independent investigation into east Kent maternity services ('Reading the Signals') found 45 baby deaths and 23 brain-damaged babies could potentially have had different outcomes, driving substantial governance and capital overhead — though not directly material to the lease line. CQC most recent inspection rated the trust 'requires improvement' (2023). Future lease trajectory tied to RAAC mitigation pipeline and capacity strategy ahead of any New Hospital Programme bids.",
        "sources": [
            {"publisher": "East Kent Hospitals University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ekhuft.nhs.uk/about-us/publications/"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 — IFRS 16 Leases adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Bill Kirkup CBE", "title": "Reading the Signals — Maternity and neonatal services in East Kent (October 2022)", "url": "https://www.gov.uk/government/publications/maternity-and-neonatal-services-in-east-kent-reading-the-signals"},
            {"publisher": "Care Quality Commission", "title": "East Kent Hospitals University NHS FT provider profile (RVV)", "url": "https://www.cqc.org.uk/provider/RVV"}
        ],
        "related": ["East Kent Hospitals University NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Kent and Medway Integrated Care Board", "Department of Health and Social Care", "HM Treasury"]
    },
    "Inventories written down — Imperial College Healthcare NHS Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Imperial College Healthcare NHS Trust"}],
        "description": "Imperial College Healthcare NHS Trust's £0.707M inventories-written-down line covers IAS 2 net-realisable-value impairments and obsolescence write-offs against clinical-supplies, drugs and consumables stockholdings across its five-hospital footprint — St Mary's (Paddington), Charing Cross (Hammersmith), Hammersmith Hospital, Queen Charlotte's & Chelsea, and Western Eye. Drivers include short-dated drug expiries (notably high-cost specialist drugs given tertiary case-mix), single-use device standards changes and pathology-reagent product churn. North West London ICS context.",
        "beneficiaries": "c. 14,500 WTE staff serving a c. 2.0M North West London catchment plus tertiary referral population for cardiac surgery, neurosciences, transplant, oncology and major trauma (St Mary's MTC); c. 350,000 ED attendances/yr; c. 240,000 admissions/yr; c. 1.4M outpatient attendances/yr; trust hosts Imperial College London academic partnership.",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Human Medicines Regulations 2012 (drug expiry/destruction) — IAS 36 (impairment interaction)",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.707M"},
            {"label": "Trust scale", "value": "5 hospitals (St Mary's MTC + Charing Cross + Hammersmith + QCCH + Western Eye); c. 14,500 WTE; AHSC partnership with Imperial College London"},
            {"label": "Composition", "value": "Short-dated specialist-drug expiries (oncology, transplant, biologics) + single-use device obsolescence + COVID-PPE legacy + pathology-reagent churn + theatre consumable spec changes"},
            {"label": "Tertiary case-mix driver", "value": "High-cost specialist drugs (oncology, transplant, haematology) drive higher write-down exposure than DGH peers"},
            {"label": "Drug-expiry destruction", "value": "Per Human Medicines Regs 2012 + MHRA controlled-drug destruction protocols + DHSC GAM"},
            {"label": "COVID-PPE legacy", "value": "DHSC central stockpile transferred 2022-23; trust-held residuals continue to flow through write-down line"},
            {"label": "Stock policy", "value": "IAS 2 lower-of-cost-and-NRV; Cerner Millennium EPR + integrated stock-control + NHS Supply Chain Logistics Online Marketplace"},
            {"label": "Industrial action 2023-24 effect", "value": "Cancelled elective lists drove theatre-pack write-off and drug-prep-set wastage at St Mary's, Charing Cross, Hammersmith"},
            {"label": "Funding trajectory", "value": "2022-23 c. £0.55M → 2023-24 c. £0.65M → 2024-25 £0.707M — COVID-PPE tail + specialist-drug expiry exposure"},
            {"label": "North West London ICS", "value": "Member of NWL ICB; collaborative procurement with Chelsea & Westminster, LNWH and CNWL"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Theatres + Pathology + NHS Supply Chain + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Supply Chain + MHRA (controlled drug destruction) + NWL ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 inventory note; NAO NHS Supply Chain reports; Carter Lord review legacy on stockholding ratios; Model Hospital inventory benchmark"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2007-merger separate stockholdings (Hammersmith Hospitals + St Mary's NHS Trust merger 2007) · Successor: integrated trust-wide inventory + Frontline Digitisation EPR-linked stock-control + ICS pooling"}
        ],
        "notes": "Imperial's inventories-written-down line is shaped by tertiary specialist-drug expiry exposure — the trust is one of NHS England's largest oncology, transplant and haematology centres, and high-value biologics, CAR-T precursors, advanced therapeutics and cardiac-surgery consumables drive higher-than-baseline write-off risk. The 2023-24 industrial-action cycle drove cancelled-list theatre-pack wastage. CQC inspection rated the trust 'Good' overall (2023). Imperial is a designated New Hospital Programme cohort trust — full St Mary's/Charing Cross/Hammersmith redevelopment now scheduled later in the NHP under the January 2025 reset. AHSC partnership with Imperial College London drives clinical-trial reagent and bespoke-product stockholding.",
        "sources": [
            {"publisher": "Imperial College Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.imperial.nhs.uk/about-us/who-we-are/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Imperial College Healthcare NHS Trust provider profile (RYJ)", "url": "https://www.cqc.org.uk/provider/RYJ"},
            {"publisher": "Medicines and Healthcare products Regulatory Agency", "title": "Disposal of unwanted medicines guidance", "url": "https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency"}
        ],
        "related": ["Imperial College Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "Department of Health and Social Care", "North West London Integrated Care Board"]
    },
    "Business rates — Warrington and Halton Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Warrington and Halton Teaching Hospitals NHS Foundation Trust"}],
        "description": "Warrington and Halton Teaching Hospitals NHS FT's £0.704M business-rates line covers non-domestic rates payable to Warrington Borough Council and Halton Borough Council on the trust's two-acute-site footprint — Warrington Hospital and Halton General Hospital (Runcorn) — plus satellite community sites. Rates are levied on Valuation Office Agency (VOA) rateable values under the Local Government Finance Act 1988, with NHS bodies receiving no charitable relief. The 2023 revaluation reset rateable values; the trust has a recently-built CDC. Cheshire and Merseyside ICS context.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 330,000 catchment across Warrington, Halton and parts of Cheshire West; c. 110,000 ED attendances/yr; c. 65,000 admissions/yr; c. 380,000 outpatient attendances/yr; trust gained 'Teaching' status 2018 in partnership with University of Chester.",
        "legal_basis": "Local Government Finance Act 1988 — Non-Domestic Rating Act 2023 — VOA 2023 revaluation list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.704M"},
            {"label": "Trust scale", "value": "Warrington Hospital + Halton General Hospital (Runcorn) + Captain Sir Tom Moore Building CDC (Halton); c. 4,500 WTE"},
            {"label": "Billing authorities", "value": "Warrington Borough Council + Halton Borough Council (collecting authorities)"},
            {"label": "Rateable value basis", "value": "VOA 2023 revaluation list — antecedent valuation date 1 April 2021"},
            {"label": "Charitable relief", "value": "Not applicable — NHS trusts/FTs are public-sector bodies, no mandatory 80% charitable relief (unlike charities)"},
            {"label": "Halton CDC", "value": "Captain Sir Tom Moore Building Community Diagnostic Centre opened 2022 — added rateable value to Halton site"},
            {"label": "Multiplier 2024-25", "value": "Standard multiplier 54.6p; small-business multiplier 49.9p (NHS estate uses standard)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.6M → 2023-24 c. £0.68M → 2024-25 £0.704M — 2023 revaluation step-up + CDC additions + multiplier inflation"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB; estate strategy aligned with Mid Cheshire Hospitals and St Helens & Knowsley"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + VOA (valuation) + Warrington/Halton councils (billing) + DLUHC/MHCLG (policy)"},
            {"label": "Policy owner", "value": "MHCLG (business-rates policy) + HM Treasury + DHSC + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "VOA rating list public record; NAO Business Rates report 2014; HMT Business Rates Review 2021"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list · Successor: 2026 revaluation; Hospital 2.0 scheme aspirations would reset rateable values"}
        ],
        "notes": "WHH's business-rates line is shaped by the addition of the Captain Sir Tom Moore Building Community Diagnostic Centre (opened 2022) at the Halton site, which added significant rateable footprint. The trust has actively pursued a 'Hospital 2.0' redevelopment vision but is not in the current New Hospital Programme cohort. CQC most recent inspection rated the trust 'Good' overall (2022). 2023 revaluation drove the step-up in rates from 2023-24 onwards. 'Teaching' status awarded 2018 reflects University of Chester medical-school partnership but does not directly affect business rates. Future trajectory tied to multiplier inflation and any New Hospital Programme bid success.",
        "sources": [
            {"publisher": "Warrington and Halton Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whh.nhs.uk/about-us/publications-and-policies"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List — find a business rates valuation", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "NHS England", "title": "Community Diagnostic Centres programme", "url": "https://www.england.nhs.uk/diagnostics-and-screening/community-diagnostic-centres/"},
            {"publisher": "Care Quality Commission", "title": "Warrington and Halton Teaching Hospitals NHS FT provider profile (RWW)", "url": "https://www.cqc.org.uk/provider/RWW"},
            {"publisher": "HM Treasury", "title": "Business Rates Review final report (October 2021)", "url": "https://www.gov.uk/government/publications/business-rates-review-final-report"}
        ],
        "related": ["Warrington and Halton Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Cheshire and Merseyside Integrated Care Board", "Valuation Office Agency", "Community Diagnostic Centres"]
    },
    "Lease expenditure — Wrightington, Wigan and Leigh NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Wrightington, Wigan and Leigh NHS Foundation Trust"}],
        "description": "Wrightington, Wigan and Leigh NHS FT's £0.687M lease-expenditure line covers IFRS 16 short-term/low-value lease costs and pre-IFRS-16 operating-lease residuals across the trust's three-site footprint — Royal Albert Edward Infirmary (Wigan), Wrightington Hospital (specialist orthopaedic centre, Appley Bridge) and Leigh Infirmary. Drivers include modular-ward leases, equipment leases (orthopaedic imaging, theatre kit), pathology analyser leases and satellite-clinic premises. Greater Manchester ICS context.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 320,000 catchment across Wigan and Leigh; Wrightington serves a national/international referral base for orthopaedic surgery (Charnley legacy hip-replacement centre); c. 110,000 ED attendances/yr; c. 75,000 admissions/yr; c. 380,000 outpatient attendances/yr.",
        "legal_basis": "IFRS 16 Leases (HMT FReM-adapted) — DHSC Group Accounting Manual 2024-25 chapter 7 — NHS Act 2006 — Health and Care Act 2022 — IAS 17 (legacy operating-lease treatment for transition)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.687M (P&L charge for short-term/low-value leases + variable lease payments)"},
            {"label": "Trust scale", "value": "Royal Albert Edward Infirmary (Wigan) + Wrightington Hospital + Leigh Infirmary; c. 5,500 WTE"},
            {"label": "IFRS 16 adoption", "value": "Adopted by NHS bodies from 1 April 2022 per HMT FReM (deferred from 2019)"},
            {"label": "Composition", "value": "Modular-ward leases + orthopaedic imaging/theatre equipment leases (Wrightington) + pathology analyser leases + vehicle/fleet leases + satellite-clinic premises"},
            {"label": "Right-of-use asset interaction", "value": "Major leases capitalised as ROU assets — depreciation runs through depreciation line; lease line captures only short-term/low-value/variable"},
            {"label": "Wrightington specialism", "value": "John Charnley legacy national orthopaedic centre — bespoke implant/equipment leases for hip/knee/upper-limb tertiary surgery"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.55M → 2023-24 c. £0.64M → 2024-25 £0.687M — modular-ward rentals + orthopaedic equipment refresh"},
            {"label": "Greater Manchester ICS", "value": "Member of Greater Manchester ICB; estate-strategy alignment with Manchester FT and Bolton FT"},
            {"label": "Industrial action effect", "value": "2023-24 strikes drove cancelled-list elective recovery via insourcing — some short-term modular-theatre leases"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + Procurement + ModuleCo/Vanguard (modular wards) + NHS Shared Business Services (lease admin)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (FReM/IFRS 16) + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HMT FReM IFRS 16 adaptation; CQC RRF inspections; Getting It Right First Time (GIRFT) orthopaedic benchmarking"},
            {"label": "Predecessor / successor", "value": "Predecessor: IAS 17 operating-lease treatment pre-2022 · Successor: IFRS 16 ROU-asset capitalisation; orthopaedic equipment refresh cycle drives lease pipeline"}
        ],
        "notes": "WWL's lease line is shaped by the Wrightington orthopaedic specialism — Wrightington Hospital is a globally renowned hip/knee surgery centre (John Charnley legacy) with bespoke implant and equipment lease arrangements that exceed typical DGH proportions. Modular-ward leases and elective-recovery insourcing capacity contribute to the line. CQC most recent inspection rated the trust 'Good' overall (2022). The trust has been a high performer on elective waiting times (top-quartile RTT) and is part of the Greater Manchester ICS provider collaborative. Future lease trajectory tied to Wrightington tertiary-orthopaedic equipment refresh cycles and any modular-capacity redeployment.",
        "sources": [
            {"publisher": "Wrightington, Wigan and Leigh NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wwl.nhs.uk/about-us/publications"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 — IFRS 16 Leases adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Wrightington, Wigan and Leigh NHS FT provider profile (RRF)", "url": "https://www.cqc.org.uk/provider/RRF"},
            {"publisher": "Getting It Right First Time", "title": "GIRFT Orthopaedic National Specialty Report", "url": "https://gettingitrightfirsttime.co.uk/surgical_specialties/orthopaedic-surgery/"}
        ],
        "related": ["Wrightington, Wigan and Leigh NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Greater Manchester Integrated Care Board", "Department of Health and Social Care", "HM Treasury"]
    },
    "PFI / LIFT charges — The Rotherham NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "The Rotherham NHS Foundation Trust"}],
        "description": "The Rotherham NHS Foundation Trust's £0.687M PFI/LIFT charges line covers payments under NHS Local Improvement Finance Trust (LIFT) arrangements for community-health buildings serving the Rotherham catchment, plus residual PFI service charges. LIFT is a public-private partnership model used to fund GP, primary-care and community-health premises. Rotherham PFI/LIFT spend is small relative to large-acute PFI peers, reflecting limited use of full PFI for the Rotherham Hospital site; charges concentrate on community-LIFT estate. South Yorkshire ICS context.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 265,000 Rotherham catchment; LIFT-funded buildings host community-health services, GP practices and integrated-care hubs; c. 100,000 ED attendances/yr; c. 60,000 admissions/yr; c. 320,000 outpatient attendances/yr; trust holds an integrated community-services contract.",
        "legal_basis": "NHS LIFT Programme — National Health Service Act 1977 / 2006 — Local Government (Contracts) Act 1997 — Health and Social Care Act 2012 — IFRIC 12 Service Concession Arrangements — DHSC Group Accounting Manual 2024-25 chapter 6",
        "key_stats": [
            {"label": "PFI/LIFT charges 2024-25", "value": "£0.687M"},
            {"label": "Trust scale", "value": "Rotherham Hospital + community sites; c. 4,500 WTE; integrated acute + community provider"},
            {"label": "LIFT vehicle", "value": "Rotherham was served via Rotherham Doncaster and South Humber LIFT (or comparable LIFT Co); LIFT Cos are 60/40 private/public JVs"},
            {"label": "Composition", "value": "LIFT unitary charge for community-health buildings (rent + service + lifecycle) + residual PFI service charges (where applicable)"},
            {"label": "PFI exposure", "value": "Low — Rotherham Hospital itself was not built under PFI; LIFT exposure is concentrated in community estate"},
            {"label": "IFRIC 12 treatment", "value": "On-balance-sheet asset + finance-lease-style liability for IFRS-aligned schemes; service element flows through P&L"},
            {"label": "Community-services contract", "value": "Trust holds Rotherham community-services contract (won 2011) — LIFT estate critical to delivery"},
            {"label": "Funding trajectory", "value": "LIFT unitary charges typically index-linked (RPI/CPI); 2024-25 £0.687M reflects steady inflation uplift"},
            {"label": "South Yorkshire ICS", "value": "Member of South Yorkshire ICB; estate strategy aligned with Sheffield Teaching, Doncaster & Bassetlaw and Barnsley"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + LIFT Co (private-sector partner) + Community Health Partnerships (CHP — government LIFT shareholder)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (PFI/LIFT policy legacy) + Community Health Partnerships + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI and PF2 report (HC 718, 2018); HMT PFI exit guidance; CHP LIFT performance reports; Trust ARA 2023-24 PFI/LIFT note"},
            {"label": "Predecessor / successor", "value": "Predecessor: Conventional capital pre-LIFT (early 2000s) · Successor: LIFT contracts running to expiry (typically 25-30 yrs); some early hand-back / refinancing under HMT PFI Centre of Expertise"}
        ],
        "notes": "Rotherham FT's PFI/LIFT line is materially smaller than acute peers because Rotherham Hospital itself was not built under PFI — exposure concentrates in community-LIFT estate (GP hubs, community-health centres). The LIFT programme was launched 2001 by HMT/DH and largely closed to new schemes by 2010; existing contracts run typically to 25-30 year terms. CHP (Community Health Partnerships) holds the public-sector 40% stake in LIFT Cos. CQC most recent inspection rated the trust 'Good' overall (2023). NAO 2018 PFI and PF2 report flagged value-for-money concerns across PFI/LIFT estate. Future trajectory tied to LIFT contract expiries and any HMT PFI Centre of Expertise interventions.",
        "sources": [
            {"publisher": "The Rotherham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.therotherhamft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "About CHP and LIFT", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 18 January 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "HM Treasury", "title": "PFI Centre of Expertise (Infrastructure and Projects Authority)", "url": "https://www.gov.uk/government/organisations/infrastructure-and-projects-authority"},
            {"publisher": "Care Quality Commission", "title": "The Rotherham NHS Foundation Trust provider profile (RFR)", "url": "https://www.cqc.org.uk/provider/RFR"}
        ],
        "related": ["The Rotherham NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Community Health Partnerships", "South Yorkshire Integrated Care Board", "HM Treasury"]
    },
    "Lease expenditure — The Leeds Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "The Leeds Teaching Hospitals NHS Trust"}],
        "description": "The Leeds Teaching Hospitals NHS Trust's £0.677M lease-expenditure line covers IFRS 16 short-term/low-value lease costs and pre-IFRS-16 operating-lease residuals across the trust's six-site footprint — Leeds General Infirmary (LGI), St James's University Hospital ('Jimmy's'), Chapel Allerton Hospital, Seacroft Hospital, Wharfedale Hospital and Leeds Dental Institute. Drivers include modular-ward leases, equipment leases (imaging, pathology, theatre kit), specialist tertiary equipment (cardiac, transplant) and satellite-clinic premises. West Yorkshire ICS context.",
        "beneficiaries": "c. 20,000 WTE staff serving a c. 800,000 Leeds catchment plus tertiary referral population for cardiac, transplant (renal, liver, cardiothoracic), oncology, neurosciences and major trauma (LGI MTC); c. 290,000 ED attendances/yr; c. 250,000 admissions/yr; c. 1.6M outpatient attendances/yr; one of the largest teaching trusts in NHS England.",
        "legal_basis": "IFRS 16 Leases (HMT FReM-adapted) — DHSC Group Accounting Manual 2024-25 chapter 7 — NHS Act 2006 — Health and Care Act 2022 — IAS 17 (legacy operating-lease treatment for transition)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.677M (P&L charge for short-term/low-value leases + variable lease payments)"},
            {"label": "Trust scale", "value": "6 hospitals (LGI MTC + St James's + Chapel Allerton + Seacroft + Wharfedale + Leeds Dental Institute); c. 20,000 WTE; tertiary referral centre"},
            {"label": "IFRS 16 adoption", "value": "Adopted by NHS bodies from 1 April 2022 per HMT FReM (deferred from 2019)"},
            {"label": "Composition", "value": "Modular-ward leases + tertiary imaging-equipment leases (cardiac MRI, PET-CT) + transplant-suite kit + pathology analyser leases + vehicle/fleet leases + Leeds Children's Hospital fit-out"},
            {"label": "Right-of-use asset interaction", "value": "Major leases capitalised as ROU assets — depreciation runs through depreciation line; lease line captures only short-term/low-value/variable"},
            {"label": "Tertiary specialism driver", "value": "Cardiac, transplant, oncology and major trauma drive bespoke equipment-lease arrangements (e.g. specialist robotics, imaging, ECMO)"},
            {"label": "Hospitals of the Future", "value": "Leeds is in NHP cohort for new Adults Hospital + Children's Hospital on LGI site (announced 2019, reset Jan 2025)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.55M → 2023-24 c. £0.62M → 2024-25 £0.677M — modular-ward rentals + tertiary equipment refresh + winter-capacity surge"},
            {"label": "West Yorkshire ICS", "value": "Member of West Yorkshire ICB; tertiary lead for region; collaborative arrangements with Mid Yorkshire, Bradford and Calderdale & Huddersfield"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + Procurement + ModuleCo/Vanguard (modular wards) + NHS Shared Business Services (lease admin)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (FReM/IFRS 16) + West Yorkshire ICB + New Hospital Programme"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HMT FReM IFRS 16 adaptation; CQC RR8 inspections; NAO New Hospital Programme reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: IAS 17 operating-lease treatment pre-2022 · Successor: IFRS 16 ROU-asset capitalisation; New Hospital Programme rebuild will reshape lease/equipment profile from late 2020s"}
        ],
        "notes": "Leeds Teaching Hospitals' lease line is shaped by tertiary specialism and the 'Hospitals of the Future' New Hospital Programme rebuild — Leeds is one of the original NHP cohort with new Adults Hospital and Leeds Children's Hospital planned for the LGI site. The January 2025 NHP reset placed Leeds in 'Wave 2' delivery (later this decade). Modular-ward and specialist-equipment leases sustain capacity ahead of rebuild. CQC most recent inspection rated the trust 'Good' overall (2023). Industrial action 2023-24 drove additional short-term theatre and recovery leases. Future lease trajectory tied closely to Hospitals of the Future delivery profile and tertiary equipment refresh.",
        "sources": [
            {"publisher": "The Leeds Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsth.nhs.uk/about-us/publications/"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 — IFRS 16 Leases adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England / DHSC", "title": "New Hospital Programme — Hospitals of the Future (Leeds)", "url": "https://www.gov.uk/government/publications/new-hospital-programme"},
            {"publisher": "Care Quality Commission", "title": "The Leeds Teaching Hospitals NHS Trust provider profile (RR8)", "url": "https://www.cqc.org.uk/provider/RR8"}
        ],
        "related": ["The Leeds Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "West Yorkshire Integrated Care Board", "Department of Health and Social Care"]
    },
    "Lease expenditure — Isle of Wight NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Isle of Wight NHS Trust"}],
        "description": "Isle of Wight NHS Trust's £0.672M lease-expenditure line covers IFRS 16 short-term/low-value lease costs and pre-IFRS-16 operating-lease residuals across the trust's unique integrated footprint — St Mary's Hospital (Newport, IoW) plus community, mental-health and ambulance-service estate. Drivers include modular-ward leases, equipment leases, ambulance-fleet vehicle leases, mental-health community-clinic premises and IT-asset leases. The trust is the only fully integrated acute/community/mental-health/ambulance trust in England. Hampshire and Isle of Wight ICS context.",
        "beneficiaries": "c. 3,200 WTE staff serving the c. 140,000 Isle of Wight resident population plus c. 2.5M annual visitors (peak summer); c. 50,000 ED attendances/yr at St Mary's; c. 35,000 admissions/yr; c. 200,000 outpatient attendances/yr; trust runs the only acute hospital, ambulance service and community/mental-health services on the island.",
        "legal_basis": "IFRS 16 Leases (HMT FReM-adapted) — DHSC Group Accounting Manual 2024-25 chapter 7 — NHS Act 2006 — Health and Care Act 2022 — IAS 17 (legacy operating-lease treatment for transition)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.672M (P&L charge for short-term/low-value leases + variable lease payments)"},
            {"label": "Trust scale", "value": "St Mary's Hospital (Newport) + ambulance service + community + mental-health estate; c. 3,200 WTE; only fully integrated acute/MH/community/ambulance trust in England"},
            {"label": "IFRS 16 adoption", "value": "Adopted by NHS bodies from 1 April 2022 per HMT FReM (deferred from 2019)"},
            {"label": "Composition", "value": "Modular-ward leases + ambulance-fleet vehicle leases + imaging-equipment leases + mental-health clinic premises + IT-asset leases"},
            {"label": "Right-of-use asset interaction", "value": "Major leases capitalised as ROU assets — depreciation runs through depreciation line; lease line captures only short-term/low-value/variable"},
            {"label": "Island-isolation premium", "value": "Geographic isolation drives higher per-capita lease costs (vehicle fleet, equipment redundancy) — no off-island fallback"},
            {"label": "Mainland partnership", "value": "Acute clinical-service partnership with Portsmouth Hospitals University NHS Trust (PHU) — some shared/lease arrangements"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.5M → 2023-24 c. £0.62M → 2024-25 £0.672M — modular-capacity rentals + ambulance fleet refresh"},
            {"label": "Hampshire and Isle of Wight ICS", "value": "Member of HIOW ICB; mainland partner trusts: PHU, UHS, HHFT"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + Procurement + ModuleCo/Vanguard + NHS Shared Business Services + Portsmouth FT (clinical partnership)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (FReM/IFRS 16) + Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HMT FReM IFRS 16 adaptation; CQC R1F inspections; NHSE 'Maintaining a sustainable Isle of Wight model' review"},
            {"label": "Predecessor / successor", "value": "Predecessor: IAS 17 operating-lease treatment pre-2022 · Successor: IFRS 16 ROU-asset capitalisation; potential PHU group-merger model could reshape lease portfolio"}
        ],
        "notes": "Isle of Wight's lease line is shaped by its unique island integrated-trust model — geographic isolation drives higher equipment redundancy and ambulance-fleet leasing per capita than mainland peers. The trust has been in CQC special measures historically (2017) and was rated 'Requires Improvement' overall in the 2023 inspection, with an active improvement programme led in partnership with Portsmouth Hospitals University Trust. The clinical partnership with PHU was formalised 2019 and reshapes some equipment/lease arrangements. NHSE-commissioned reviews (Lord Carter 2018, NHSE 2020) have considered sustainability of the island model. Future lease trajectory tied to ambulance fleet refresh and any PHU group-merger development.",
        "sources": [
            {"publisher": "Isle of Wight NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.iow.nhs.uk/About-Us/our-publications.htm"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 — IFRS 16 Leases adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Isle of Wight NHS Trust provider profile (R1F)", "url": "https://www.cqc.org.uk/provider/R1F"},
            {"publisher": "NHS England", "title": "Maintaining a sustainable Isle of Wight model — review", "url": "https://www.england.nhs.uk/publication/"}
        ],
        "related": ["Isle of Wight NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Portsmouth Hospitals University NHS Trust", "Hampshire and Isle of Wight Integrated Care Board", "HM Treasury"]
    },
    "Business rates — Countess of Chester Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
        "description": "Countess of Chester Hospital NHS FT's £0.666M business-rates line covers non-domestic rates payable to Cheshire West and Chester Council on the trust's estate centred on the Countess of Chester Hospital site (Chester) plus the Ellesmere Port Hospital satellite. Rates are levied on Valuation Office Agency (VOA) rateable values under the Local Government Finance Act 1988, with NHS bodies receiving no charitable relief. The 2023 revaluation reset rateable values. Cheshire and Merseyside ICS context; trust subject to the Lucy Letby criminal proceedings and ongoing Thirlwall Inquiry.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 450,000 catchment across Cheshire West, Wirral peninsula and parts of north Wales; c. 110,000 ED attendances/yr; c. 65,000 admissions/yr; c. 360,000 outpatient attendances/yr; trust hosts a regional neonatal-care service.",
        "legal_basis": "Local Government Finance Act 1988 — Non-Domestic Rating Act 2023 — VOA 2023 revaluation list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.666M"},
            {"label": "Trust scale", "value": "Countess of Chester Hospital + Ellesmere Port Hospital; c. 4,500 WTE"},
            {"label": "Billing authority", "value": "Cheshire West and Chester Council (collecting authority)"},
            {"label": "Rateable value basis", "value": "VOA 2023 revaluation list — antecedent valuation date 1 April 2021"},
            {"label": "Charitable relief", "value": "Not applicable — NHS trusts/FTs are public-sector bodies, no mandatory 80% charitable relief (unlike charities)"},
            {"label": "Multiplier 2024-25", "value": "Standard multiplier 54.6p; small-business multiplier 49.9p (NHS estate uses standard)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.58M → 2023-24 c. £0.64M → 2024-25 £0.666M — 2023 revaluation step-up + multiplier inflation"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB; estate alignment with Mid Cheshire and Wirral University Teaching Hospital"},
            {"label": "Neonatal context", "value": "Trust runs Level 2 Local Neonatal Unit — subject of Lucy Letby criminal proceedings 2018-23 + ongoing Thirlwall Inquiry"},
            {"label": "Thirlwall Inquiry", "value": "Statutory inquiry chaired by Lady Justice Thirlwall (2023-) examining events at the trust — substantial governance/legal cost overhead, not directly material to rates"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + VOA (valuation) + Cheshire West & Chester Council (billing) + DLUHC/MHCLG (policy)"},
            {"label": "Policy owner", "value": "MHCLG (business-rates policy) + HM Treasury + DHSC + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "VOA rating list public record; NAO Business Rates report 2014; HMT Business Rates Review 2021"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list · Successor: 2026 revaluation"}
        ],
        "notes": "Countess of Chester's business-rates line is conventional in scale, but the trust operates under exceptional governance scrutiny following the conviction of nurse Lucy Letby (August 2023, retrial conviction July 2024) for the murder of seven babies and attempted murder of others on the neonatal unit (2015-16). The Thirlwall Inquiry, chaired by Lady Justice Thirlwall, opened in 2024 to examine the events. While not directly material to the business-rates line, the trust faces substantial governance, legal and reputational overhead. CQC most recent inspection rated the trust 'Good' overall (2022) but neonatal services have been under particular focus. 2023 revaluation drove the step-up in rates from 2023-24 onwards.",
        "sources": [
            {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.coch.nhs.uk/about-us/publications-policies-and-statements/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List — find a business rates valuation", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "The Thirlwall Inquiry", "title": "Statutory inquiry into events at the Countess of Chester Hospital", "url": "https://thirlwall.public-inquiry.uk/"},
            {"publisher": "Care Quality Commission", "title": "Countess of Chester Hospital NHS FT provider profile (RJR)", "url": "https://www.cqc.org.uk/provider/RJR"},
            {"publisher": "HM Treasury", "title": "Business Rates Review final report (October 2021)", "url": "https://www.gov.uk/government/publications/business-rates-review-final-report"}
        ],
        "related": ["Countess of Chester Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Cheshire and Merseyside Integrated Care Board", "Valuation Office Agency", "The Thirlwall Inquiry"]
    },
    "Amortisation — Epsom and St Helier University Hospitals NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Epsom and St Helier University Hospitals NHS Trust"}],
        "description": "Epsom and St Helier University Hospitals NHS Trust's £0.665M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly EPR/PAS software, PACS imaging archives, capitalised digital-pathology assets and back-office software deployed across Epsom Hospital, St Helier Hospital (Sutton/Carshalton) and Sutton Hospital community sites. The trust's intangibles balance is shaped by digital-transformation investment ahead of the New Hospital Programme Sutton specialist-emergency-care hospital build. South West London ICS context.",
        "beneficiaries": "c. 5,800 WTE staff serving a c. 490,000 catchment across Sutton, Merton and Surrey; c. 165,000 ED attendances/yr split across Epsom and St Helier; c. 90,000 admissions/yr; c. 540,000 outpatient attendances/yr; trust runs South West London Elective Orthopaedic Centre (SWLEOC) joint venture.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 3 (acquired-software treatment) — IAS 36 (impairment interaction)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.665M"},
            {"label": "Trust scale", "value": "Epsom Hospital + St Helier Hospital + Sutton Hospital + community sites + SWLEOC; c. 5,800 WTE"},
            {"label": "Principal intangibles", "value": "Cerner Millennium EPR + PACS/RIS imaging + e-prescribing modules + pathology LIMS + back-office software + SWLEOC orthopaedic-systems"},
            {"label": "EPR platform", "value": "Cerner Millennium (Oracle Health) — shared regional instance with St George's, Croydon and Kingston via Cerner Joint Venture"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; major EPR modules amortised over 7-10 yrs; PACS image storage ~10 years"},
            {"label": "New Hospital Programme — Sutton", "value": "Building the New Sutton specialist emergency-care hospital — pre-construction digital systems being capitalised; major step-up expected on opening"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.5M → 2023-24 c. £0.6M → 2024-25 £0.665M — Frontline Digitisation module additions + Sutton pre-build digital investment"},
            {"label": "South West London ICS", "value": "Member of SWL ICB; partnership with St George's University Hospitals NHS FT (Group operating model in development)"},
            {"label": "St George's group model", "value": "ESH and SGUH formed group operating model 2024 (combined leadership) — shapes shared digital-platform strategy"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Cerner/Oracle Health + Frontline Digitisation programme team + SWL ICB digital lead"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + SWL ICB + New Hospital Programme"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangibles note; NAO digital-transformation reports; CQC RVR inspections; NHP NAO scrutiny"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cerner legacy PAS · Successor: New Sutton specialist hospital opening will drive substantial capitalisation tranche; group-model harmonisation with SGUH"}
        ],
        "notes": "Epsom and St Helier's amortisation line is shaped by the Cerner Millennium EPR and the pre-build digital investment for the New Sutton specialist-emergency-care hospital — the trust's NHP scheme to consolidate emergency, acute and tertiary services on a new Sutton Hospital site (announced 2020, business case approved 2024 but reset under January 2025 NHP delivery reset). The 2024 group operating model with St George's University Hospitals (combined chair/CEO leadership) shapes future shared digital-platform strategy. CQC most recent inspection rated the trust 'Requires Improvement' overall (2023). Future intangibles step-up tied to Sutton hospital opening.",
        "sources": [
            {"publisher": "Epsom and St Helier University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.epsom-sthelier.nhs.uk/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England / DHSC", "title": "New Hospital Programme — Building the New Sutton hospital", "url": "https://www.gov.uk/government/publications/new-hospital-programme"},
            {"publisher": "Care Quality Commission", "title": "Epsom and St Helier University Hospitals NHS Trust provider profile (RVR)", "url": "https://www.cqc.org.uk/provider/RVR"},
            {"publisher": "South West London ICB", "title": "SWL ICS digital strategy and group operating model", "url": "https://www.southwestlondon.icb.nhs.uk/"}
        ],
        "related": ["Epsom and St Helier University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "St George's University Hospitals NHS Foundation Trust", "New Hospital Programme", "South West London Integrated Care Board"]
    },
    "Inventories written down — Northern Care Alliance NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Northern Care Alliance NHS Foundation Trust"}],
        "description": "Northern Care Alliance NHS FT's £0.663M inventories-written-down line covers IAS 2 net-realisable-value impairments and obsolescence write-offs against clinical-supplies, drugs and consumables stockholdings across the trust's four-hospital footprint — Salford Royal, Royal Oldham Hospital, Fairfield General Hospital (Bury) and Rochdale Infirmary. Drivers include short-dated drug expiries, post-merger catalogue rationalisation (NCA formed 2021), single-use device standards changes and pathology-reagent product churn. Greater Manchester ICS context.",
        "beneficiaries": "c. 20,000 WTE staff serving a c. 1.0M catchment across Salford, Oldham, Bury, Rochdale and parts of Manchester; c. 350,000 ED attendances/yr; c. 200,000 admissions/yr; c. 1.3M outpatient attendances/yr; trust hosts the regional Major Trauma Centre at Salford Royal and tertiary neurosciences/neurosurgery services.",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Human Medicines Regulations 2012 (drug expiry/destruction) — IAS 36 (impairment interaction)",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.663M"},
            {"label": "Trust scale", "value": "4 hospitals (Salford Royal MTC + Royal Oldham + Fairfield Bury + Rochdale Infirmary); c. 20,000 WTE; formed October 2021 from Salford Royal + Pennine Acute Hospitals merger"},
            {"label": "Composition", "value": "Short-dated drug expiries + single-use device obsolescence + post-merger catalogue duplication + COVID-PPE legacy + pathology-reagent churn + theatre consumable spec changes"},
            {"label": "Post-merger driver", "value": "NCA formed 2021 from Salford Royal + Pennine Acute (Bury, Oldham, Rochdale) — catalogue rationalisation in progress drives elevated write-off"},
            {"label": "Drug-expiry destruction", "value": "Per Human Medicines Regs 2012 + MHRA controlled-drug destruction protocols + DHSC GAM"},
            {"label": "COVID-PPE legacy", "value": "DHSC central stockpile transferred 2022-23; trust-held residuals continue to flow through write-down line"},
            {"label": "Stock policy", "value": "IAS 2 lower-of-cost-and-NRV; post-merger inventory-management harmonisation in progress + NHS Supply Chain Logistics Online Marketplace"},
            {"label": "Industrial action 2023-24 effect", "value": "Cancelled elective lists drove theatre-pack write-off and drug-prep-set wastage across all four sites"},
            {"label": "Funding trajectory", "value": "2022-23 c. £0.45M (first full post-merger year) → 2023-24 c. £0.6M → 2024-25 £0.663M — catalogue rationalisation tail + COVID-PPE residuals"},
            {"label": "Greater Manchester ICS", "value": "Member of GM ICB; collaborative procurement with MFT and Bolton FT"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Theatres + Pathology + NHS Supply Chain + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Supply Chain + MHRA (controlled drug destruction) + GM ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 inventory note; NAO NHS Supply Chain reports; Carter Lord review legacy on stockholding ratios; Model Hospital inventory benchmark"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger Salford Royal + Pennine Acute separate stockholdings · Successor: integrated trust-wide inventory + Frontline Digitisation EPR-linked stock-control + ICS pooling"}
        ],
        "notes": "NCA's inventories-written-down line is shaped principally by post-merger catalogue rationalisation — NCA was formed October 2021 from the merger of Salford Royal NHS FT (former Shelford Group, high-performing) and Pennine Acute Hospitals NHS Trust (Bury, Oldham, Rochdale). Pre-merger, the two heritage organisations had divergent stock catalogues, theatre packs and pharmacy stock conventions; rationalisation continues to drive elevated write-offs. The 2023-24 industrial-action cycle drove cancelled-list theatre-pack and drug-prep-set wastage. CQC most recent inspection rated NCA 'Good' overall (2023). Tertiary neurosciences and Salford Royal's MTC role drive specialist-reagent expiry exposure. Future trajectory tied to EPR convergence (different EPRs across sites historically) and Frontline Digitisation roll-out.",
        "sources": [
            {"publisher": "Northern Care Alliance NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northerncarealliance.nhs.uk/about-us/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Northern Care Alliance NHS Foundation Trust provider profile (R0A)", "url": "https://www.cqc.org.uk/provider/R0A"},
            {"publisher": "Medicines and Healthcare products Regulatory Agency", "title": "Disposal of unwanted medicines guidance", "url": "https://www.gov.uk/government/organisations/medicines-and-healthcare-products-regulatory-agency"}
        ],
        "related": ["Northern Care Alliance NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "Greater Manchester Integrated Care Board", "Department of Health and Social Care"]
    },
    "Lease expenditure — Frimley Health NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Frimley Health NHS Foundation Trust"}],
        "description": "Frimley Health NHS FT's £0.657M lease-expenditure line covers IFRS 16 short-term/low-value lease costs and pre-IFRS-16 operating-lease residuals across the trust's three-acute-site footprint — Frimley Park Hospital (Camberley, Surrey), Wexham Park Hospital (Slough) and Heatherwood Hospital (Ascot, opened 2022). Drivers include modular-ward leases, equipment leases (imaging, pathology, theatre kit) and satellite-clinic premises. The trust is in the New Hospital Programme cohort for full Frimley Park rebuild (RAAC). Frimley ICS context.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 900,000 catchment across north-east Hampshire, west Surrey, east Berkshire and south Buckinghamshire; c. 220,000 ED attendances/yr; c. 130,000 admissions/yr; c. 800,000 outpatient attendances/yr; trust serves significant Ministry of Defence (Aldershot Garrison, Sandhurst) population.",
        "legal_basis": "IFRS 16 Leases (HMT FReM-adapted) — DHSC Group Accounting Manual 2024-25 chapter 7 — NHS Act 2006 — Health and Care Act 2022 — IAS 17 (legacy operating-lease treatment for transition)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.657M (P&L charge for short-term/low-value leases + variable lease payments)"},
            {"label": "Trust scale", "value": "Frimley Park (RAAC) + Wexham Park + new Heatherwood (opened 2022); c. 9,000 WTE"},
            {"label": "IFRS 16 adoption", "value": "Adopted by NHS bodies from 1 April 2022 per HMT FReM (deferred from 2019)"},
            {"label": "Composition", "value": "Modular-ward leases (RAAC mitigation at Frimley Park) + imaging-equipment leases + pathology analyser leases + Heatherwood elective-hub equipment + satellite-clinic premises"},
            {"label": "Right-of-use asset interaction", "value": "Major leases capitalised as ROU assets — depreciation runs through depreciation line; lease line captures only short-term/low-value/variable"},
            {"label": "RAAC context", "value": "Frimley Park is one of seven RAAC-construction hospitals confirmed for full New Hospital Programme reconstruction — modular-ward leases sustain capacity ahead of rebuild"},
            {"label": "Heatherwood elective hub", "value": "New Heatherwood Hospital (opened March 2022) — equipment-fit-out leases included in pre-2022 base"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.6M → 2024-25 £0.657M — RAAC modular capacity surge + Heatherwood operational equipment refresh"},
            {"label": "Frimley ICS", "value": "Member of Frimley Health and Care ICB; geographic footprint spans 4 county boundaries"},
            {"label": "MoD population", "value": "Significant defence-population catchment (Aldershot Garrison, Sandhurst Royal Military Academy) — bespoke-service arrangements"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + Procurement + ModuleCo/Vanguard (modular wards) + NHS Shared Business Services (lease admin)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (FReM/IFRS 16) + Frimley Health and Care ICB + New Hospital Programme"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HMT FReM IFRS 16 adaptation; CQC RDU inspections; NAO New Hospital Programme reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: IAS 17 operating-lease treatment pre-2022 · Successor: IFRS 16 ROU-asset capitalisation; Frimley Park RAAC rebuild will reset lease/equipment profile late 2020s"}
        ],
        "notes": "Frimley Health's lease line is shaped by RAAC modular-capacity sustaining at Frimley Park ahead of full New Hospital Programme reconstruction (Frimley Park is one of seven RAAC-priority NHP rebuilds). The new Heatherwood Hospital opened March 2022 — purpose-built elective hub focusing on planned orthopaedic and short-stay surgery. CQC most recent inspection rated the trust 'Good' overall (2023). The Frimley ICS spans an unusual four-county geography. January 2025 NHP reset placed Frimley Park in the priority RAAC cohort for delivery this decade. Future lease trajectory tied to RAAC mitigation modular footprint and Frimley Park rebuild progression.",
        "sources": [
            {"publisher": "Frimley Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.fhft.nhs.uk/about-us/publications/"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 — IFRS 16 Leases adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England / DHSC", "title": "New Hospital Programme — RAAC cohort", "url": "https://www.gov.uk/government/publications/new-hospital-programme"},
            {"publisher": "Care Quality Commission", "title": "Frimley Health NHS Foundation Trust provider profile (RDU)", "url": "https://www.cqc.org.uk/provider/RDU"}
        ],
        "related": ["Frimley Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Frimley Health and Care Integrated Care Board", "HM Treasury"]
    },
    "Lease expenditure — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "Worcestershire Acute Hospitals NHS Trust's £0.654M lease-expenditure line covers IFRS 16 short-term/low-value lease costs and pre-IFRS-16 operating-lease residuals across the trust's three-acute-site footprint — Worcestershire Royal Hospital (Worcester, PFI), Alexandra Hospital (Redditch) and Kidderminster Hospital. Drivers include modular-ward leases, equipment leases (imaging, pathology, theatre kit), satellite-clinic premises and PFI-related variable charges. Worcestershire Royal is a major PFI scheme. Herefordshire and Worcestershire ICS context.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 580,000 Worcestershire catchment; c. 195,000 ED attendances/yr; c. 100,000 admissions/yr; c. 540,000 outpatient attendances/yr; trust historically subject to capacity and emergency-care performance scrutiny, currently in NHSE Recovery Support Programme.",
        "legal_basis": "IFRS 16 Leases (HMT FReM-adapted) — DHSC Group Accounting Manual 2024-25 chapter 7 — NHS Act 2006 — Health and Care Act 2022 — IAS 17 (legacy operating-lease treatment for transition) — IFRIC 12 (PFI service concession)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.654M (P&L charge for short-term/low-value leases + variable lease payments)"},
            {"label": "Trust scale", "value": "Worcestershire Royal Hospital (Worcester, PFI) + Alexandra Hospital (Redditch) + Kidderminster Hospital; c. 6,000 WTE"},
            {"label": "IFRS 16 adoption", "value": "Adopted by NHS bodies from 1 April 2022 per HMT FReM (deferred from 2019)"},
            {"label": "Composition", "value": "Modular-ward leases (winter capacity) + imaging-equipment leases + pathology analyser leases + vehicle/fleet leases + satellite-clinic premises"},
            {"label": "Right-of-use asset interaction", "value": "Major leases capitalised as ROU assets; lease line captures only short-term/low-value/variable; PFI assets/liabilities sit separately under IFRIC 12"},
            {"label": "PFI context", "value": "Worcestershire Royal Hospital opened 2002 under a major PFI scheme — separate PFI charges captured under PFI/LIFT line, not this lease line"},
            {"label": "Recovery Support Programme", "value": "Trust placed in NHSE RSP segment 4 in past — significant performance/governance overhead; modular-ward leases sustain ED/admission capacity"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.55M → 2023-24 c. £0.61M → 2024-25 £0.654M — winter modular capacity + equipment refresh"},
            {"label": "Herefordshire and Worcestershire ICS", "value": "Member of Herefordshire and Worcestershire ICB; estate alignment with Wye Valley NHS Trust and primary-care network"},
            {"label": "ED capacity context", "value": "Worcestershire Royal ED has been one of the most-pressured EDs in NHS England — modular-ward leases critical to flow"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + Procurement + ModuleCo/Vanguard (modular wards) + NHS Shared Business Services (lease admin)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (FReM/IFRS 16) + Herefordshire and Worcestershire ICB + NHSE Recovery Support"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HMT FReM IFRS 16 adaptation; CQC RWP inspections; NAO winter-capacity reports; NHSE RSP reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: IAS 17 operating-lease treatment pre-2022 · Successor: IFRS 16 ROU-asset capitalisation; potential capital scheme to refresh Alexandra Hospital footprint"}
        ],
        "notes": "Worcestershire Acute's lease line is shaped by sustained winter modular-capacity surge — the trust's three-site model and intense ED pressure (Worcestershire Royal historically among NHS England's most-challenged EDs) drive ongoing modular-ward and capacity-hub leasing. The trust has been in NHSE Recovery Support Programme historically and faced sustained performance scrutiny including 2016 CQC special-measures designation. CQC most recent inspection (2023) rated the trust 'Requires Improvement' overall. The Worcestershire Royal PFI (opened 2002) is a major fixed cost separate from this lease line. Future trajectory tied to RSP exit, capital strategy and any ICS-level reconfiguration affecting the Alexandra/Kidderminster footprint.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.worcsacute.nhs.uk/about-us/publications"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 — IFRS 16 Leases adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Worcestershire Acute Hospitals NHS Trust provider profile (RWP)", "url": "https://www.cqc.org.uk/provider/RWP"},
            {"publisher": "NHS England", "title": "Recovery Support Programme — segmentation framework", "url": "https://www.england.nhs.uk/system-support/"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Herefordshire and Worcestershire Integrated Care Board", "Department of Health and Social Care", "HM Treasury"]
    },
    "Lease expenditure — Norfolk and Norwich University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Norfolk and Norwich University Hospitals NHS Foundation Trust"}],
        "description": "Norfolk and Norwich University Hospitals NHS FT's £0.650M lease-expenditure line covers IFRS 16 short-term/low-value lease costs and pre-IFRS-16 operating-lease residuals across the trust's footprint centred on the Norfolk and Norwich University Hospital (NNUH, Colney) plus Cromer and District Hospital and outreach sites. Drivers include modular-ward leases, equipment leases (imaging, pathology, theatre kit), specialist tertiary equipment and satellite-clinic premises. NNUH is a major PFI hospital (opened 2001). Norfolk and Waveney ICS context.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 1.0M Norfolk catchment plus tertiary referral population for cancer, cardiology, neurology and renal services; c. 200,000 ED attendances/yr; c. 130,000 admissions/yr; c. 850,000 outpatient attendances/yr; trust hosts the UEA Norwich Medical School academic partnership.",
        "legal_basis": "IFRS 16 Leases (HMT FReM-adapted) — DHSC Group Accounting Manual 2024-25 chapter 7 — NHS Act 2006 — Health and Care Act 2022 — IAS 17 (legacy operating-lease treatment for transition) — IFRIC 12 (PFI service concession)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.650M (P&L charge for short-term/low-value leases + variable lease payments)"},
            {"label": "Trust scale", "value": "NNUH (Colney, PFI) + Cromer Hospital + outreach sites; c. 9,500 WTE; tertiary referral centre"},
            {"label": "IFRS 16 adoption", "value": "Adopted by NHS bodies from 1 April 2022 per HMT FReM (deferred from 2019)"},
            {"label": "Composition", "value": "Modular-ward leases (capacity surge) + tertiary imaging-equipment leases (cancer, cardiac) + pathology analyser leases + vehicle/fleet leases + satellite-clinic premises"},
            {"label": "Right-of-use asset interaction", "value": "Major leases capitalised as ROU assets; lease line captures only short-term/low-value/variable; PFI assets/liabilities sit separately under IFRIC 12"},
            {"label": "PFI context", "value": "NNUH opened 2001 under one of NHS England's largest PFI schemes (Octagon Healthcare Ltd) — separate charges captured under PFI/LIFT line, not this lease line"},
            {"label": "Tertiary specialism driver", "value": "Cancer, cardiology, neurology and renal drive bespoke equipment-lease arrangements"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.5M → 2023-24 c. £0.6M → 2024-25 £0.650M — winter modular capacity + tertiary equipment refresh"},
            {"label": "Norfolk and Waveney ICS", "value": "Member of Norfolk and Waveney ICB; tertiary lead for region; partnership with QEH King's Lynn and James Paget"},
            {"label": "UEA partnership", "value": "Academic partnership with University of East Anglia Norwich Medical School + Norwich Research Park"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + Procurement + ModuleCo/Vanguard (modular wards) + NHS Shared Business Services (lease admin)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (FReM/IFRS 16) + Norfolk and Waveney ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HMT FReM IFRS 16 adaptation; CQC RM1 inspections; NAO PFI/PF2 reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: IAS 17 operating-lease treatment pre-2022 · Successor: IFRS 16 ROU-asset capitalisation; PFI contract approaches mid-life refresh, will reshape capital/lease portfolio"}
        ],
        "notes": "NNUH's lease line is small relative to the dominant PFI fixed cost — NNUH opened 2001 as one of the largest PFI hospitals in NHS England (Octagon Healthcare Ltd), and PFI charges absorb the majority of premises spend (separate line). The lease line captures incremental modular-ward and equipment leasing for capacity surge and tertiary-specialism kit. CQC most recent inspection rated the trust 'Good' overall (2023). The trust has a strong academic partnership with UEA Norwich Medical School and Norwich Research Park. PFI mid-life refresh and contract-management interventions (HMT PFI Centre of Expertise) shape the medium-term cost trajectory. Future lease trajectory tied to PFI evolution and tertiary-equipment refresh.",
        "sources": [
            {"publisher": "Norfolk and Norwich University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nnuh.nhs.uk/about-us/our-publications/"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 — IFRS 16 Leases adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 18 January 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Care Quality Commission", "title": "Norfolk and Norwich University Hospitals NHS FT provider profile (RM1)", "url": "https://www.cqc.org.uk/provider/RM1"}
        ],
        "related": ["Norfolk and Norwich University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Norfolk and Waveney Integrated Care Board", "Department of Health and Social Care", "HM Treasury"]
    },
    "Transport (business + patient) — Northampton General Hospital NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Northampton General Hospital NHS Trust"}],
        "description": "Northampton General Hospital NHS Trust's £0.640M transport (business + patient) line covers business-mileage reimbursements (staff travel between sites/community visits/training), patient-transport contract spend (non-emergency patient transport with EMED Group / regional NEPTS provider), inter-hospital pathology/sample-courier services, mortuary transport and clinical-fleet running costs across the trust's NGH (Cliftonville, Northampton) acute footprint plus outreach. Northamptonshire ICS context.",
        "beneficiaries": "c. 4,800 WTE staff serving a c. 380,000 catchment across Northampton, Daventry, South Northants and parts of Wellingborough; c. 130,000 ED attendances/yr; c. 75,000 admissions/yr; c. 380,000 outpatient attendances/yr; trust hosts the regional Heart Centre and oncology services serving wider Midlands.",
        "legal_basis": "AfC NHS Mileage Allowances (Agenda for Change Section 17 / NHS Terms & Conditions Handbook) — HMRC Approved Mileage Allowance Payments (AMAP) — Healthcare Travel Costs Scheme (HC11/HC12) — NHS Act 2006 — Health and Care Act 2022 — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport spend 2024-25", "value": "£0.640M"},
            {"label": "Trust scale", "value": "Northampton General Hospital + outreach; c. 4,800 WTE; regional Heart Centre and oncology"},
            {"label": "Composition", "value": "Business mileage (AfC reimbursement) + NEPTS patient-transport contract + pathology/sample courier + mortuary transport + clinical fleet running"},
            {"label": "AfC mileage rates", "value": "Standard rate 59p/mile (first 3,500 miles), reserve rate 30p/mile thereafter (rates uplifted June 2023 in NHS Staff Council pay deal)"},
            {"label": "NEPTS provider", "value": "Non-emergency patient transport contracted (East Midlands regional procurement — EMED Group / G4S / E-zec depending on lot/year)"},
            {"label": "Group operating model", "value": "NGH operates in group with Kettering General Hospital (University Hospitals of Northamptonshire group) — shared transport overhead/courier"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.50M → 2023-24 c. £0.60M → 2024-25 £0.640M — June 2023 mileage-rate uplift + fuel-cost pass-through + courier inflation"},
            {"label": "Northamptonshire ICS", "value": "Member of Northamptonshire ICB; transport strategy aligned with KGH and Northamptonshire Healthcare NHS FT (community)"},
            {"label": "Pathology network", "value": "East Midlands Pathology Hub (NUH-led) drives sample-courier overhead — shared transport contracts"},
            {"label": "Healthcare Travel Costs Scheme", "value": "Patient reimbursement under HC11/HC12 means-tested scheme — handled separately"},
            {"label": "Delivery body", "value": "Trust Travel & Transport + Finance + NEPTS contractor + courier providers + Pathology Network"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHS Staff Council (AfC mileage) + DHSC + HMRC (AMAP) + NHSE NEPTS Strategic Framework"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 transport note; NHSE NEPTS strategic framework 2021; NAO patient-transport report 2018; AfC pay-deal documentation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 NEPTS contract era · Successor: 2024-25 NEPTS regional re-procurement; group-model fleet rationalisation with KGH"}
        ],
        "notes": "NGH's transport line is shaped by the June 2023 NHS Staff Council pay deal which uplifted AfC mileage rates (the standard rate moved from 56p/mile to 59p/mile in line with HMRC AMAP) — the cumulative effect is substantial in 2024-25. The University Hospitals of Northamptonshire group operating model (NGH + Kettering General Hospital, formed 2021 with shared chair/CEO) drives fleet/courier rationalisation, though formal merger is not yet under way. CQC most recent inspection rated NGH 'Good' overall (2022). The 2024-25 East Midlands NEPTS re-procurement reset the patient-transport contract baseline. Future trajectory tied to fuel-cost evolution, AfC pay rounds and group-model rationalisation savings.",
        "sources": [
            {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northamptongeneral.nhs.uk/About/PublicationScheme/Reports-and-publications.aspx"},
            {"publisher": "NHS Employers / NHS Staff Council", "title": "Agenda for Change Section 17 — Mileage Allowances", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Strategic Framework (2021)", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-strategic-framework/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Northampton General Hospital NHS Trust provider profile (RNS)", "url": "https://www.cqc.org.uk/provider/RNS"}
        ],
        "related": ["Northampton General Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Kettering General Hospital NHS Foundation Trust", "Northamptonshire Integrated Care Board", "NHS England"]
    },
    "Lease expenditure — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "Sheffield Teaching Hospitals NHS FT's £0.637M lease-expenditure line covers IFRS 16 short-term/low-value lease costs and pre-IFRS-16 operating-lease residuals across the trust's footprint — Royal Hallamshire Hospital, Northern General Hospital (housing the regional Major Trauma Centre and South Yorkshire Cardiothoracic Centre), Weston Park Hospital (cancer centre), Jessop Wing (maternity), Charles Clifford Dental Hospital and outreach community sites. Drivers include modular-ward leases, tertiary-equipment leases (cardiac, oncology, neuro), pathology analyser leases and satellite-clinic premises. South Yorkshire ICS context.",
        "beneficiaries": "c. 18,500 WTE staff serving a c. 600,000 Sheffield catchment plus tertiary referral population for cancer (Weston Park), cardiac (NGH), neurosciences, transplant (renal), spinal-injuries and major trauma (NGH MTC); c. 280,000 ED attendances/yr; c. 220,000 admissions/yr; c. 1.4M outpatient attendances/yr; trust hosts University of Sheffield academic partnership.",
        "legal_basis": "IFRS 16 Leases (HMT FReM-adapted) — DHSC Group Accounting Manual 2024-25 chapter 7 — NHS Act 2006 — Health and Care Act 2022 — IAS 17 (legacy operating-lease treatment for transition)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.637M (P&L charge for short-term/low-value leases + variable lease payments)"},
            {"label": "Trust scale", "value": "Royal Hallamshire + Northern General (MTC, cardiothoracic) + Weston Park (cancer) + Jessop Wing (maternity) + Charles Clifford Dental + outreach; c. 18,500 WTE; tertiary referral centre"},
            {"label": "IFRS 16 adoption", "value": "Adopted by NHS bodies from 1 April 2022 per HMT FReM (deferred from 2019)"},
            {"label": "Composition", "value": "Modular-ward leases + tertiary imaging-equipment leases (cancer, cardiac, neuro) + pathology analyser leases + dental-school equipment + vehicle/fleet leases + satellite-clinic premises"},
            {"label": "Right-of-use asset interaction", "value": "Major leases capitalised as ROU assets — depreciation runs through depreciation line; lease line captures only short-term/low-value/variable"},
            {"label": "Tertiary specialism driver", "value": "Cancer (Weston Park), cardiac (NGH), neurosciences, transplant, spinal-injuries and MTC drive bespoke equipment-lease arrangements"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.5M → 2023-24 c. £0.59M → 2024-25 £0.637M — winter modular capacity + tertiary equipment refresh"},
            {"label": "South Yorkshire ICS", "value": "Member of South Yorkshire ICB; tertiary lead for region; partnership with Doncaster & Bassetlaw, Barnsley and Rotherham"},
            {"label": "University of Sheffield partnership", "value": "Academic partnership; shared research and clinical-trial infrastructure"},
            {"label": "Maternity context", "value": "Jessop Wing maternity unit subject of CQC concerns and HSIB / MNSI investigations — equipment refresh drove some short-term leasing"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + Procurement + ModuleCo/Vanguard (modular wards) + NHS Shared Business Services (lease admin)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (FReM/IFRS 16) + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; HMT FReM IFRS 16 adaptation; CQC RHQ inspections; HSIB / MNSI maternity investigations"},
            {"label": "Predecessor / successor", "value": "Predecessor: IAS 17 operating-lease treatment pre-2022 · Successor: IFRS 16 ROU-asset capitalisation; potential capital schemes for Hallamshire/NGH refresh"}
        ],
        "notes": "Sheffield Teaching Hospitals' lease line is shaped by tertiary specialism — cancer (Weston Park), cardiac (Northern General), spinal-injuries, neurosciences and MTC drive bespoke equipment-lease arrangements that exceed typical DGH proportions. Jessop Wing maternity unit has been subject to ongoing CQC and HSIB/MNSI scrutiny in recent years (rated 'Requires Improvement' in maternity at last CQC inspection 2022, with broader trust 'Good'). Industrial action 2023-24 drove additional short-term theatre and recovery leases. The trust is one of the UK's largest teaching hospitals with strong University of Sheffield academic partnership. Future lease trajectory tied to maternity-equipment investment, tertiary refresh and any capital programme for the Hallamshire/NGH estate.",
        "sources": [
            {"publisher": "Sheffield Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sth.nhs.uk/about-us/publications"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 — IFRS 16 Leases adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Teaching Hospitals NHS Foundation Trust provider profile (RHQ)", "url": "https://www.cqc.org.uk/provider/RHQ"},
            {"publisher": "Maternity and Newborn Safety Investigations (MNSI)", "title": "MNSI investigations programme", "url": "https://www.mnsi.org.uk/"}
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "South Yorkshire Integrated Care Board", "Department of Health and Social Care", "HM Treasury"]
    },
}
