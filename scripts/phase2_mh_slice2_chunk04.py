# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 04 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Business rates — South London and Maudsley NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "South London and Maudsley NHS Foundation Trust"}],
        "description": "SLaM's £2.03M 2024-25 business rates line is the VOA-set non-domestic rates bill across the trust's south-east London estate — Maudsley Hospital Denmark Hill, Bethlem Royal Hospital Beckenham (the historic 'Bedlam' campus, now national specialist forensic + CAMHS Tier 4 hub) and the Lambeth, Southwark, Lewisham and Croydon community sites. Each occupied hereditament is rated under LGFA 1988 Schedule 6 with the 2024-25 standard multiplier 49.9p applied to VOA rateable values; charitable mandatory relief does not apply because SLaM is an NHS Foundation Trust, not a registered charity.",
        "beneficiaries": "c. 60 hereditaments (Denmark Hill main acute psychiatric campus, Bethlem Royal 270-acre site with national-specialist forensic and adolescent units, plus c. 50 community-mental-health and CAMHS clinic sites) serving c. 1.3M residents across Lambeth, Southwark, Lewisham and Croydon plus national specialist catchments.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.03M"},
            {"label": "Multiplier applied", "value": "Standard 49.9p (rateable value > £51,000) for main hospital sites; small 49.9p for some community clinics in 2024-25"},
            {"label": "Hereditament count", "value": "c. 60 occupied sites — Denmark Hill main, Bethlem Royal Beckenham, plus community CAMHS + CMHT estate"},
            {"label": "Largest single hereditament", "value": "Maudsley Hospital Denmark Hill — VOA rateable value c. £2.4M+ band"},
            {"label": "Charitable relief status", "value": "NHS FT not registered charity — no automatic 80% mandatory relief; some discretionary relief on shared community sites"},
            {"label": "Bethlem Royal historic estate", "value": "270-acre Beckenham site (1247 founding date as Bethlem); listed buildings constrain rateable value methodology"},
            {"label": "VOA revaluation cycle", "value": "2023 list applies 2024-25; next list 2026 (3-yearly per NDR Act 2023 reform)"},
            {"label": "Delivery body", "value": "VOA sets rateable value · LB Lambeth/Southwark/Lewisham/Croydon + LB Bromley (Bethlem) bill collection · NHS BSA central rates payment service"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG NDR policy · DHSC sponsor · NHSE Provider Finance"},
            {"label": "Funding trajectory", "value": "Rising — 2023 revaluation +c. 4% over 2017 list; multiplier frozen 2024-25 but 2025-26 split (40.8p small, 55.5p standard) increases standard-rate sites"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 NDR list · Successor: 2026 revaluation with 3-yearly cadence; NDR Act 2024 multiplier split for retail/hospitality only — health unaffected"},
            {"label": "Evaluation evidence", "value": "NHS Confederation 2024 NDR briefing flagged £400M+ aggregate NHS rates burden; NAO 2023 NDR review"}
        ],
        "notes": "SLaM's rates exposure is shaped by an unusually historic and decentralised estate: the Bethlem Royal Beckenham site (continuously operating since 1247, the world's oldest psychiatric hospital, with multiple listed buildings and a 270-acre curtilage) sits in LB Bromley while clinical activity straddles four south-London boroughs. The 2023 VOA revaluation lifted the bill modestly; the 2025-26 multiplier reform splits small/standard rates but preserves the standard 55.5p rate for larger NHS hereditaments, locking in the upward trajectory. NHS Confederation has lobbied for an explicit health-sector NDR exemption parallel to the schools/charitable carve-out — without success to date.",
        "sources": [
            {"publisher": "South London and Maudsley NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://slam.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Confederation", "title": "Business rates and the NHS — briefing 2024", "url": "https://www.nhsconfed.org/publications"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 explanatory notes", "url": "https://www.legislation.gov.uk/ukpga/2024/29"}
        ],
        "related": ["South London and Maudsley NHS Foundation Trust", "Premises & Infrastructure", "Business rates — Mersey Care NHS Foundation Trust", "Business rates — Tees, Esk and Wear Valleys NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Business rates — Norfolk and Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Norfolk and Suffolk NHS Foundation Trust"}],
        "description": "NSFT's £2.01M 2024-25 business rates bill is the VOA-set NDR liability across the largest geographically-dispersed mental-health estate in the East of England — Hellesdon Hospital Norwich (main acute admissions), Northgate Hospital Great Yarmouth, Wedgwood House Bury St Edmunds, Woodlands Ipswich and a long tail of community-mental-health and CAMHS clinics. The trust pays standard 49.9p multiplier on most hereditaments under LGFA 1988; charitable relief is unavailable as an NHS FT. The 2023 VOA list applies in 2024-25 with a 2026 revaluation pending under the new 3-yearly cycle.",
        "beneficiaries": "c. 70 hereditaments across Norfolk and Suffolk (Hellesdon ~200 beds, Northgate, Wedgwood, Woodlands, plus c. 60 community sites) serving c. 1.7M residents across the two counties; NSFT is one of the most rurally-dispersed MH trusts in England, driving a large hereditament count relative to acute provision.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.01M"},
            {"label": "Multiplier applied", "value": "Standard 49.9p on Hellesdon, Northgate, Wedgwood, Woodlands; small 49.9p on community CMHT sub-£51k RV"},
            {"label": "Hereditament count", "value": "c. 70 occupied sites — main inpatient + dispersed CMHT/CAMHS estate across rural Norfolk and Suffolk"},
            {"label": "Largest single hereditament", "value": "Hellesdon Hospital Norwich — VOA RV in £1.2M+ band; main psychiatric admissions site"},
            {"label": "Charitable relief status", "value": "NHS FT — no mandatory 80% relief; very limited discretionary relief on a few co-located voluntary-sector premises"},
            {"label": "VOA revaluation cycle", "value": "2023 list applies 2024-25; next 2026 (NDR Act 2023 3-yearly cadence)"},
            {"label": "Delivery body", "value": "VOA sets rateable value · Norwich, Great Yarmouth, West Suffolk, East Suffolk councils bill · NHS BSA central rates payment service"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG NDR policy · DHSC sponsor · NHSE East of England Provider Finance"},
            {"label": "Funding trajectory", "value": "Rising — 2023 revaluation +c. 3% over 2017 list; 2025-26 multiplier split lifts standard-rate hereditaments to 55.5p"},
            {"label": "Trust-specific context", "value": "NSFT in NHS Recovery Support Programme (placed in 'special measures' 2023 after CQC 'Inadequate'); estate consolidation under review may shrink hereditament tail"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 NDR list · Successor: 2026 revaluation; possible estate-rationalisation reduction in hereditament count"},
            {"label": "Evaluation evidence", "value": "CQC 'Inadequate' 2023 + recovery programme; HSSIB inpatient mental-health safety reviews 2024"}
        ],
        "notes": "NSFT has the most geographically-dispersed mental-health estate in the region, which inflates the hereditament tail and the absolute rates bill relative to bed numbers. The trust entered NHS Recovery Support Programme in 2023 after a CQC 'Inadequate' rating, and the resulting estate-rationalisation review may reduce the hereditament count over the medium term — but the 2025-26 multiplier reform (standard rate to 55.5p) will offset most of that downward pressure. The 270-mile north-south span between Great Yarmouth's Northgate and Bury St Edmunds means rural CMHT clinics are scattered across multiple billing-authority districts (Norwich, Great Yarmouth, West Suffolk, East Suffolk, Breckland, North Norfolk).",
        "sources": [
            {"publisher": "Norfolk and Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nsft.nhs.uk/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Norfolk and Suffolk NHS FT provider profile (RMY)", "url": "https://www.cqc.org.uk/provider/RMY"},
            {"publisher": "NHS Confederation", "title": "Business rates and the NHS — briefing 2024", "url": "https://www.nhsconfed.org/publications"}
        ],
        "related": ["Norfolk and Suffolk NHS Foundation Trust", "Premises & Infrastructure", "Business rates — South London and Maudsley NHS Foundation Trust", "Business rates — Essex Partnership University NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Transport (business + patient) — Berkshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Berkshire Healthcare NHS Foundation Trust"}],
        "description": "Berkshire Healthcare's £1.99M 2024-25 transport line covers staff business mileage (community-mental-health, district-nursing and CAMHS clinicians driving across the six unitary authorities of Berkshire), patient transport for inpatient admissions and S136 conveyance to Prospect Park Hospital (Reading) and Wokingham Hospital, plus pool-vehicle running costs. The trust runs combined community-physical-health and mental-health services, so the transport spend is inflated relative to a pure-MH peer by district-nursing and community-paediatric drives. AfC Travel and Subsistence Handbook governs reimbursement at HMRC AMAP-aligned rates.",
        "beneficiaries": "c. 4,500 community-services and mental-health clinicians driving across c. 1,200 sq miles spanning Reading, West Berkshire, Wokingham, Bracknell Forest, Slough and Windsor and Maidenhead; c. 750,000 patient contacts per year include c. 200,000 home or community visits requiring vehicle travel.",
        "legal_basis": "AfC Terms and Conditions Section 17 (Travel and Subsistence) · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 · HMRC Approved Mileage Allowance Payments (AMAP) · IFRS 16 Leases (pool-vehicle leases)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.99M"},
            {"label": "Workforce travelling", "value": "c. 4,500 community + MH clinicians using personal or pool vehicles for visits"},
            {"label": "Geographic reach", "value": "Six unitary authorities — Reading, West Berkshire, Wokingham, Bracknell Forest, Slough, Windsor and Maidenhead — c. 1,200 sq miles"},
            {"label": "Reimbursement rate", "value": "AfC Section 17 — 56p/mile first 3,500 miles 'standard rate', 20p/mile thereafter; 'reserve rate' 28p"},
            {"label": "Pool-vehicle fleet", "value": "Trust operates leased and owned pool fleet for shared community use; IFRS 16 right-of-use asset on leases"},
            {"label": "S136 / patient conveyance", "value": "Approved-mental-health-professional and S136 conveyance to Prospect Park Hospital (Reading) shared with Thames Valley Police and SCAS"},
            {"label": "Combined community-physical + MH driver", "value": "District nursing + CAMHS + community paediatrics drive higher mileage than pure-MH peers"},
            {"label": "Delivery body", "value": "Trust transport function + leased fleet provider · Section 17 reimbursement via NHS BSA payroll"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + Frimley ICB · AfC Staff Council oversight on Section 17"},
            {"label": "Funding trajectory", "value": "Rising — fuel + lease-rate inflation 2022-24; AfC mileage rate static at 56p since 2014 has compressed reimbursement vs HMRC 45p AMAP comparison"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 'Lease Car Scheme' phased out · Successor: AfC Section 17 review pending; ICS shared-fleet pilots under exploration"},
            {"label": "Evaluation evidence", "value": "NHS Pay Review Body evidence rounds 2023-24 cited static mileage rate as recruitment headwind for community staff"}
        ],
        "notes": "Berkshire Healthcare's transport line is structurally larger than typical for a £350M-turnover MH trust because the trust holds the Berkshire community physical-health contract alongside its MH remit — meaning district nursing, community paediatrics and end-of-life care visits all flow through the same line. The AfC Section 17 'standard rate' (56p/mile first 3,500 miles) has been frozen since 2014 while petrol and HMRC AMAP rates have evolved; NHS Pay Review Body evidence has flagged this as a community-staff retention issue. Pool-vehicle leases sit on the IFRS 16 ROU asset but their depreciation falls in the lease-expenditure line, not here.",
        "sources": [
            {"publisher": "Berkshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.berkshirehealthcare.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Employers", "title": "AfC Section 17 Travel and Subsistence Handbook", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "HM Revenue and Customs", "title": "Approved Mileage Allowance Payments rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Pay Review Body", "title": "37th Report 2024", "url": "https://www.gov.uk/government/publications/nhs-pay-review-body-37th-report-2024"}
        ],
        "related": ["Berkshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "Transport (business + patient) — Greater Manchester Mental Health NHS Foundation Trust", "Transport (business + patient) — Norfolk and Suffolk NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Amortisation — Sussex Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Sussex Partnership NHS Foundation Trust"}],
        "description": "Sussex Partnership's £1.97M 2024-25 amortisation charge is the IAS 38 straight-line write-off of intangible assets — overwhelmingly the capitalised electronic patient record (EPR) rollout costs, software licences (Carenotes/Rio family migration), capitalised development on digital-mental-health platforms, plus website and clinical-pathway intangibles. The trust is in NHSE's Frontline Digitisation programme cohort; matched-funding investment has lifted the intangible carrying value sharply since 2022, driving a step-up in amortisation as new modules go live and begin the typical 5-10 year useful-life amortisation.",
        "beneficiaries": "c. 5,000 clinical and admin users across Sussex (Brighton and Hove, East Sussex, West Sussex) running the EPR + ePMA + digital-MH platforms; c. 200,000 service users on the consolidated patient record; community + inpatient + CAMHS estate covered.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation Programme MoU",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.97M"},
            {"label": "Useful-life policy", "value": "5-10 years straight-line for software; longer (15+) for capitalised development per IAS 38"},
            {"label": "EPR programme status", "value": "Frontline Digitisation cohort; Carenotes/Rio-family migration with matched DHSC funding 2022-25"},
            {"label": "Step-up driver", "value": "Capitalised software additions 2022-24 begin amortising as modules go-live; ePMA + digital-MH apps phased on"},
            {"label": "Intangible asset carrying value", "value": "Trust intangibles c. £15-20M gross post-FD investment; net of accumulated amortisation"},
            {"label": "Delivery body", "value": "Trust IT/Digital function · NHSE Frontline Digitisation team · ICB digital lead"},
            {"label": "Policy owner", "value": "NHSE Transformation Directorate · DHSC sponsor · Sussex ICB co-funding"},
            {"label": "Funding trajectory", "value": "Rising 2024-26 as more FD-funded software goes-live; plateau expected post-2027 as full-cohort modules amortise on schedule"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 legacy Carenotes amortisation tail · Successor: post-FD steady-state amortisation; possible NHS Federated Data Platform integration intangibles"},
            {"label": "Evaluation evidence", "value": "NAO 2023 Digital Transformation in the NHS report; NHSE Frontline Digitisation programme update 2024"},
            {"label": "Specialty driver", "value": "Sussex Partnership runs forensic + perinatal + CAMHS specialist services requiring bespoke EPR configurations adding to capitalised dev"},
            {"label": "Trust-specific context", "value": "Mascalls Park / Hellingly secure-services digital migration adds bespoke amortisation"}
        ],
        "notes": "The 2024-25 amortisation step-up reflects the Frontline Digitisation 'go-live wave': intangible assets capitalised during the build phase 2022-24 only begin amortising once modules enter productive use, so the line will continue rising into 2025-26 before plateauing. Sussex Partnership's specialist forensic and CAMHS pathways require bespoke EPR configurations whose capitalised-development costs amortise over longer useful lives than vanilla licence packages. NAO's 2023 Digital Transformation report flagged that mental-health trusts received proportionally less Frontline Digitisation funding than acute peers, partly because the legacy Carenotes/Rio installed base is older and simpler — but post-2022 catch-up investment is now flowing through P&L as amortisation.",
        "sources": [
            {"publisher": "Sussex Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sussexpartnership.nhs.uk/publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 2023)", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Sussex Partnership NHS FT provider profile (RX2)", "url": "https://www.cqc.org.uk/provider/RX2"}
        ],
        "related": ["Sussex Partnership NHS Foundation Trust", "Premises & Infrastructure", "Amortisation — Mersey Care NHS Foundation Trust", "Amortisation — Oxford Health NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Business rates — Essex Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Essex Partnership University NHS Foundation Trust"}],
        "description": "EPUT's £1.96M 2024-25 business rates bill is the VOA-set NDR liability across one of the most geographically dispersed mental-health and community estates in England — c. 200 sites including Basildon Mental Health Unit, Linden Centre Chelmsford, Rochford Hospital, Brockfield House (medium-secure forensic, Wickford), plus a long tail of community clinics across Essex, Bedfordshire, Luton and parts of Suffolk. LGFA 1988 Schedule 6 valuation applies; standard 49.9p multiplier on most large hereditaments, small 49.9p on community CMHT premises with rateable value under £51,000.",
        "beneficiaries": "c. 200 hereditaments across Essex, Bedfordshire, Luton and parts of Suffolk (5 unitary + 12 district councils) serving c. 3.2M residents; estate spans inpatient mental-health units, forensic medium-secure facilities, community clinics and the trust's substantial community-physical-health portfolio absorbed from the former South Essex Partnership and North Essex Partnership predecessors.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.96M"},
            {"label": "Multiplier applied", "value": "Standard 49.9p on Basildon MHU, Linden Centre, Brockfield House, Rochford; small 49.9p on c. 150 sub-£51k RV community sites"},
            {"label": "Hereditament count", "value": "c. 200 occupied sites — among the largest hereditament tails of any English MH trust"},
            {"label": "Largest single hereditament", "value": "Basildon Mental Health Unit + Brockfield House medium-secure — VOA RV bands £0.6-1.0M each"},
            {"label": "Charitable relief status", "value": "NHS FT — no mandatory 80% relief"},
            {"label": "VOA revaluation cycle", "value": "2023 list applies 2024-25; 2026 revaluation under NDR Act 2023 3-yearly cadence"},
            {"label": "Delivery body", "value": "VOA · 5 unitary + 12 district billing authorities (Essex, Southend, Thurrock, Bedford, Luton + districts) · NHS BSA central rates payment"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG NDR policy · DHSC sponsor · NHSE East of England + Mid and South Essex ICB"},
            {"label": "Funding trajectory", "value": "Rising — 2023 revaluation modest uplift; 2025-26 multiplier split lifts standard-rate sites to 55.5p"},
            {"label": "Trust-specific context", "value": "EPUT subject to Lampard Inquiry 2023-25 into in-patient mental-health deaths in Essex 2000-2023; estate review under independent scrutiny"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 merger of South Essex Partnership + North Essex Partnership consolidated 2 sets of NDR billing arrangements · Successor: 2026 revaluation"},
            {"label": "Evaluation evidence", "value": "Lampard Inquiry interim findings 2024; CQC inspections 2023-24 cited environment concerns"}
        ],
        "notes": "EPUT's c. 200 hereditaments — one of the largest tails in the English MH sector — reflect the 2017 merger that consolidated South Essex Partnership and North Essex Partnership trusts and inherited their distinct dispersed community estates. The trust is the subject of the statutory Lampard Inquiry (chaired by Baroness Lampard) into the deaths of mental-health inpatients in Essex 2000-2023, with the estate condition and ward layouts under direct scrutiny. The 2025-26 multiplier reform (55.5p standard) lifts the bill on the larger inpatient hereditaments. NHS Confederation has lobbied for an explicit health-sector NDR exemption parallel to schools — without success.",
        "sources": [
            {"publisher": "Essex Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://eput.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lampard Inquiry", "title": "Independent Inquiry into Mental Health Deaths in Essex", "url": "https://lampardinquiry.org.uk/"},
            {"publisher": "NHS Confederation", "title": "Business rates and the NHS — briefing 2024", "url": "https://www.nhsconfed.org/publications"}
        ],
        "related": ["Essex Partnership University NHS Foundation Trust", "Premises & Infrastructure", "Business rates — Norfolk and Suffolk NHS Foundation Trust", "Business rates — Midlands Partnership NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Business rates — Lancashire and South Cumbria NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Lancashire and South Cumbria NHS Foundation Trust"}],
        "description": "LSCFT's £1.95M 2024-25 business rates bill is the VOA-set NDR liability across a wide MH and community estate spanning Lancashire and South Cumbria — Guild Lodge medium-secure (Whittingham, Preston), The Harbour Blackpool (130-bed adult acute psychiatric unit opened 2015), The Cove Heysham, Junction 17 Prestwich (CAMHS) and a long community-clinic tail. LGFA 1988 Schedule 6 valuation applies; the trust pays 49.9p multiplier on most hereditaments. Charitable mandatory relief unavailable as NHS FT.",
        "beneficiaries": "c. 90 hereditaments across Lancashire (12 districts), Blackpool, Blackburn with Darwen and South Cumbria (Barrow, South Lakeland) serving c. 1.8M residents; The Harbour Blackpool 130 beds, Guild Lodge ~80 medium-secure beds, plus c. 75 community sites.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.95M"},
            {"label": "Multiplier applied", "value": "Standard 49.9p on Harbour Blackpool, Guild Lodge, Cove Heysham, Junction 17; small 49.9p on community CMHT/CAMHS sub-£51k RV"},
            {"label": "Hereditament count", "value": "c. 90 occupied sites across Lancashire + Blackpool + Blackburn with Darwen + South Cumbria"},
            {"label": "Largest single hereditament", "value": "The Harbour Blackpool — VOA RV in £0.7-0.9M band; opened 2015 purpose-built adult acute MH"},
            {"label": "Charitable relief status", "value": "NHS FT — no mandatory 80% relief"},
            {"label": "VOA revaluation cycle", "value": "2023 list applies 2024-25; 2026 revaluation under NDR Act 2023 3-yearly cadence"},
            {"label": "Delivery body", "value": "VOA · Blackpool, Lancaster, Preston, Blackburn with Darwen, Barrow + 14 districts billing · NHS BSA central rates payment"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG NDR policy · DHSC sponsor · NHSE North West + Lancashire and South Cumbria ICB"},
            {"label": "Funding trajectory", "value": "Rising — 2023 revaluation +c. 3% over 2017 list; 2025-26 multiplier split lifts standard-rate sites"},
            {"label": "Trust-specific context", "value": "Trust placed in NHS Recovery Support Programme 2024 after CQC concerns at Guild Lodge and acute wards; estate condition under review"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2002-formed merger of Lancashire Care + Cumbria Partnership MH services consolidated 2018 · Successor: 2026 revaluation"},
            {"label": "Evaluation evidence", "value": "CQC inspections 2023-24 cited Guild Lodge and Calderstones legacy estate condition; HSSIB inpatient MH review"}
        ],
        "notes": "LSCFT's rates bill reflects an unusually purpose-built portion of the estate: The Harbour Blackpool (opened 2015, the trust's flagship 130-bed adult-acute psychiatric unit) carries a relatively high VOA rateable value because new-build modern fabric attracts a higher MEA-DRC-equivalent valuation under the rating contractor's-method approach. Older Guild Lodge medium-secure (Whittingham site, post-1990s) and the inherited Calderstones legacy estate sit lower. The trust entered NHS Recovery Support Programme in 2024 after CQC concerns; estate-rationalisation is part of the recovery plan and may reduce hereditament count over the medium term. The 2025-26 multiplier reform locks in the upward trajectory.",
        "sources": [
            {"publisher": "Lancashire and South Cumbria NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lscft.nhs.uk/about-us/publications-policies-procedures-and-strategies"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Lancashire and South Cumbria NHS FT provider profile (RW5)", "url": "https://www.cqc.org.uk/provider/RW5"},
            {"publisher": "NHS Confederation", "title": "Business rates and the NHS — briefing 2024", "url": "https://www.nhsconfed.org/publications"}
        ],
        "related": ["Lancashire and South Cumbria NHS Foundation Trust", "Premises & Infrastructure", "Business rates — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Business rates — Mersey Care NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Establishment costs — Cornwall Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Cornwall Partnership NHS Foundation Trust"}],
        "description": "Cornwall Partnership's £1.94M 2024-25 establishment costs line covers the routine operating consumables of running a dispersed mental-health and community-services estate across the Duchy — printing, stationery, postage, telephony, courier, office consumables and small-scale equipment under capitalisation thresholds. The line is structurally inflated relative to peer MH trusts by Cornwall's geographic isolation (single-county catchment, 80+ sites, inter-site courier dependence) and the trust's combined community-physical-health remit absorbed under the 2014 service integration. DHSC GAM disclosure-rule line.",
        "beneficiaries": "c. 80 occupied sites across Cornwall and the Isles of Scilly serving c. 570,000 residents; the estate spans Bodmin Hospital (Longreach House inpatient MH), Garner Ward Truro, Fettle House Bodmin, plus c. 70 CMHT and community-physical-health clinics including the Isles of Scilly outreach.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (general disclosure) · NHS Act 2006 · Health and Care Act 2022 · IAS 1 Presentation of Financial Statements · IAS 2 Inventories (consumables under capitalisation threshold)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.94M"},
            {"label": "Sites covered", "value": "c. 80 occupied hereditaments across Cornwall and Isles of Scilly"},
            {"label": "Geographic driver", "value": "Cornwall's single-county catchment + Isles of Scilly outreach inflates per-site overhead vs national peers"},
            {"label": "Combined community + MH driver", "value": "2014 service integration brought community-physical-health clinics + district-nursing into the trust, expanding the establishment footprint"},
            {"label": "Capitalisation threshold", "value": "£5,000 per DHSC GAM minimum capitalisation; below this small equipment expenses to establishment line"},
            {"label": "Postage and telephony driver", "value": "Geographic isolation forces higher inter-site courier and telephony spend than urban peers"},
            {"label": "Delivery body", "value": "Trust corporate services + procurement framework (NHS Supply Chain non-medical)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cornwall and Isles of Scilly ICB · GAM disclosure rules"},
            {"label": "Funding trajectory", "value": "Rising — CPI inflation 2022-24 on consumables; postage RPI-linked Royal Mail uplift; offset by digital-mailing and e-records reducing paper volumes"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 separate community-trust establishment costs · Successor: digital transformation reducing paper/postage; Frontline Digitisation EPR reducing per-site stationery"},
            {"label": "Evaluation evidence", "value": "NHSE Model Hospital benchmarking on corporate overhead; ICB efficiency programme 2024"},
            {"label": "Trust-specific context", "value": "Cornwall is one of England's most rural / peninsular ICS footprints; air-ambulance and Scilly outreach drive bespoke establishment overhead"}
        ],
        "notes": "Cornwall Partnership's establishment line carries structurally higher per-bed cost than English MH peers because of geographic isolation (peninsular single-county catchment, Isles of Scilly outreach by air, inter-site courier dependence) and because the 2014 service-integration absorption of community-physical-health services expanded the operational footprint. The line is GAM-disclosed under general establishment-costs heading and includes printing, postage, telephony, courier and small-equipment-below-capitalisation-threshold spend. Frontline Digitisation EPR rollout will gradually reduce the paper/postage component — but rural courier and telephony costs structurally persist.",
        "sources": [
            {"publisher": "Cornwall Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cornwallft.nhs.uk/about-us/key-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital corporate-services benchmarking", "url": "https://model.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Cornwall Partnership NHS FT provider profile (RJ8)", "url": "https://www.cqc.org.uk/provider/RJ8"},
            {"publisher": "NHS Supply Chain", "title": "Non-medical and corporate frameworks", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Cornwall Partnership NHS Foundation Trust", "Premises & Infrastructure", "Establishment costs — Devon Partnership NHS Trust", "Establishment costs — Dorset Healthcare University NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Establishment costs — Pennine Care NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Pennine Care NHS Foundation Trust"}],
        "description": "Pennine Care's £1.93M 2024-25 establishment costs covers consumables, stationery, postage, telephony, courier and below-capitalisation-threshold equipment for an estate spanning five Greater Manchester boroughs — Bury, Oldham, Rochdale, Stockport and Tameside — plus residual community sites. Anchor inpatient hubs include Birch Hill Hospital Rochdale (Bridge House inpatient MH), Tameside General MH unit, Stepping Hill MH (Stockport) and Royal Oldham MH bed-base. The line scales with the c. 100-site dispersed footprint of community CMHT, CAMHS and crisis-team clinics across northeast Greater Manchester.",
        "beneficiaries": "c. 100 sites across 5 GM boroughs (Bury, Oldham, Rochdale, Stockport, Tameside) serving c. 1.3M residents; inpatient bedbase c. 380 beds across 4 main hubs; community + CAMHS + crisis-team clinics drive the long site tail.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (general disclosure) · NHS Act 2006 · Health and Care Act 2022 · IAS 1 Presentation of Financial Statements · IAS 2 Inventories (consumables under capitalisation threshold)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.93M"},
            {"label": "Sites covered", "value": "c. 100 occupied sites across 5 Greater Manchester boroughs"},
            {"label": "Inpatient bedbase", "value": "c. 380 MH inpatient beds across Birch Hill, Tameside, Stepping Hill, Royal Oldham hubs"},
            {"label": "Capitalisation threshold", "value": "£5,000 per DHSC GAM minimum capitalisation"},
            {"label": "Telephony + IT-licence component", "value": "Major sub-component — multi-borough connectivity + EPR licence per-seat"},
            {"label": "Trust-specific context", "value": "Trust serves the post-2002-reorganisation 'Pennine' geographic footprint (legacy of pre-merger Pennine Acute boundary); 2018 transfer of Trafford services to GMMH narrowed remit"},
            {"label": "Delivery body", "value": "Trust corporate services + GM ICS shared procurement framework + NHS Supply Chain non-medical"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Greater Manchester ICB · GAM disclosure rules"},
            {"label": "Funding trajectory", "value": "Rising — CPI inflation on consumables 2022-24; postage uplifts; offset by digital-mailing"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 'Pennine Care' included Trafford prior to GMMH transfer · Successor: GM ICS shared-services efficiency programme"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; NHSE Model Hospital corporate-services benchmarking; HSSIB Edenfield safeguarding context applied to GMMH not PCFT"},
            {"label": "EPR + Frontline Digitisation status", "value": "Frontline Digitisation cohort; capitalised EPR migration above threshold flows to amortisation, below to establishment line"}
        ],
        "notes": "Pennine Care's establishment-cost shape reflects a five-borough Greater Manchester footprint with a long tail of community CMHT clinics and four main inpatient hubs. The 2018 reorganisation that transferred Trafford services to GMMH narrowed the trust's remit but the residual five-borough estate still drives c. 100 hereditaments. Pennine Care is in the Frontline Digitisation cohort; capitalised software costs above the £5,000 threshold sit in intangibles (and amortise), while sub-threshold per-seat licences and consumables flow through this establishment line. GM ICS shared-services procurement framework provides modest aggregation savings on stationery, telephony and small-IT.",
        "sources": [
            {"publisher": "Pennine Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.penninecare.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital corporate-services benchmarking", "url": "https://model.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Pennine Care NHS FT provider profile (RT2)", "url": "https://www.cqc.org.uk/provider/RT2"},
            {"publisher": "NHS Supply Chain", "title": "Non-medical and corporate frameworks", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Pennine Care NHS Foundation Trust", "Premises & Infrastructure", "Establishment costs — Greater Manchester Mental Health NHS Foundation Trust", "Establishment costs — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Impairments net of reversals — Hertfordshire Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Hertfordshire Partnership University NHS Foundation Trust"}],
        "description": "HPFT's £1.91M 2024-25 impairment is the IAS 36 net writedown across the trust's Hertfordshire and Buckinghamshire MH and learning-disabilities estate — Kingfisher Court Radlett (adult acute), Forest House Adolescent Unit, Mead House Hatfield (forensic + medium-secure), plus Norfolk and Buckinghamshire learning-disability and forensic services contracted in. MEA-DRC revaluation under the 5-yearly cycle was applied to inpatient hubs; the Norfolk LD service-line transfer added carrying-value-review entries.",
        "beneficiaries": "c. 30 main MH/LD sites serving c. 1.2M Hertfordshire residents plus contracted learning-disability and forensic services into Norfolk, Bedfordshire, Buckinghamshire; inpatient bedbase c. 350 across Kingfisher Court, Forest House, Mead House, Lister Hospital MH liaison and Norfolk LD units.",
        "legal_basis": "IAS 36 Impairment of Assets · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£1.91M"},
            {"label": "5-year impairment trend", "value": "2020-21 c. £0.5M → 2021-22 c. £0.9M → 2022-23 c. £1.2M → 2023-24 c. £1.6M → 2024-25 £1.91M"},
            {"label": "Estate gross floor area revalued", "value": "c. 70,000 m² across MH and LD inpatient + community estate"},
            {"label": "MEA-DRC vs market value driver", "value": "Kingfisher Court Radlett (2014 build) mid-life revaluation; older Mead House Hatfield + Norfolk LD inherited estate below MEA"},
            {"label": "RAAC scope", "value": "Not on HSSIB confirmed-RAAC list"},
            {"label": "NHP cohort + Reset Jan 2025 status", "value": "Not in NHP cohort; capital programme via Hertfordshire and West Essex ICB"},
            {"label": "Specialty driver", "value": "Forensic + LD specialist services drive bespoke ward configurations whose MEA-DRC functional-equivalent depresses carrying value of older fabric"},
            {"label": "Cross-trust contracts", "value": "HPFT contracts in LD and forensic services across Norfolk and Buckinghamshire — adds out-of-county estate impairment review"},
            {"label": "Valuation cycle phase", "value": "5-yearly full revaluation 2024-25"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + external valuer DHSC central panel (Cushman & Wakefield framework)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Hertfordshire and West Essex ICB · IAS 36 / DHSC GAM oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 ageing Kingfisher Court replacement build · Successor: ICS estate strategy review"}
        ],
        "notes": "HPFT's impairment line is structurally moderate because Kingfisher Court Radlett (opened 2014, the trust's flagship adult-acute MH unit) is still relatively young and revalues less aggressively. Older Mead House Hatfield (forensic medium-secure) and the inherited Norfolk learning-disability service estate carry the bulk of the writedown. The trust's unusual cross-county footprint — providing LD and forensic services into Norfolk and Buckinghamshire under contract — broadens the MEA-DRC review beyond Hertfordshire boundaries. Without an NHP slot, capital-renewal must come through Hertfordshire and West Essex ICS bids, leaving the impairment trajectory mildly upward as economic life is extended on older fabric.",
        "sources": [
            {"publisher": "Hertfordshire Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hpft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "NHS provider finance and operational performance 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "HPFT provider profile (RWR)", "url": "https://www.cqc.org.uk/provider/RWR"},
            {"publisher": "National Audit Office", "title": "NHS Estate condition report 2024", "url": "https://www.nao.org.uk/reports/nhs-estate/"}
        ],
        "related": ["Hertfordshire Partnership University NHS Foundation Trust", "Premises & Infrastructure", "Impairments net of reversals — North East London NHS Foundation Trust", "Impairments net of reversals — Bradford District Care NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Amortisation — Dorset Healthcare University NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Dorset Healthcare University NHS Foundation Trust"}],
        "description": "Dorset Healthcare's £1.90M 2024-25 amortisation is IAS 38 straight-line write-off of intangible assets — capitalised EPR rollout under the Frontline Digitisation programme (Rio + bespoke modules), software licences, capitalised development on community-mental-health digital platforms and shared Dorset ICS digital-care-record contributions. The trust is a combined community-physical-health + mental-health provider, so the EPR build covers both pathways and the intangible base is correspondingly larger than a pure-MH peer. Amortisation step-up reflects 2022-24 capitalisations now going-live.",
        "beneficiaries": "c. 5,500 clinical and admin users across Dorset (Bournemouth, Christchurch, Poole, rural Dorset) running the EPR + ePMA + community-care record; c. 250,000 service users on the consolidated patient record covering MH, community physical-health, district-nursing and end-of-life care.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation Programme MoU",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.90M"},
            {"label": "Useful-life policy", "value": "5-10 years straight-line for software; longer for capitalised development per IAS 38"},
            {"label": "EPR programme status", "value": "Frontline Digitisation cohort; Rio-family + bespoke community modules; matched DHSC funding 2022-25"},
            {"label": "Combined community + MH driver", "value": "Trust covers both MH and community physical-health → larger intangible base than pure-MH peer of similar £-turnover"},
            {"label": "Step-up driver", "value": "Capitalised software 2022-24 begins amortising as modules go-live; ePMA + Dorset Care Record contributions phased on"},
            {"label": "Intangible asset carrying value", "value": "Trust intangibles c. £15M gross; net of accumulated amortisation"},
            {"label": "Delivery body", "value": "Trust Digital function · NHSE Frontline Digitisation team · NHS Dorset ICB digital lead"},
            {"label": "Policy owner", "value": "NHSE Transformation Directorate · DHSC sponsor · NHS Dorset ICB co-funding"},
            {"label": "Funding trajectory", "value": "Rising 2024-26 as more FD-funded modules go-live; plateau expected post-2027"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 legacy Rio amortisation tail · Successor: post-FD steady-state; possible Federated Data Platform integration"},
            {"label": "Evaluation evidence", "value": "NAO 2023 Digital Transformation in the NHS report; NHSE Frontline Digitisation programme update 2024"},
            {"label": "Trust-specific context", "value": "University-trust designation drives capitalised research-platform development entries"}
        ],
        "notes": "Dorset Healthcare's amortisation trajectory mirrors the Frontline Digitisation cohort pattern — capitalised software costs 2022-24 only enter amortisation once modules go-live, so the line steps up into 2025-26 before plateauing. The trust's combined MH + community-physical-health remit means the intangible base is larger than a pure-MH peer of similar turnover; the Dorset Care Record (a shared ICS digital-care-record initiative) adds capitalised development whose amortisation is split across contributing organisations. The university-trust designation also drives research-platform capitalised development. NAO's 2023 report flagged that combined-care MH/community trusts often face proportionally higher capitalisation than pure acute peers.",
        "sources": [
            {"publisher": "Dorset Healthcare University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dorsethealthcare.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 2023)", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Dorset Healthcare University NHS FT provider profile (RDY)", "url": "https://www.cqc.org.uk/provider/RDY"}
        ],
        "related": ["Dorset Healthcare University NHS Foundation Trust", "Premises & Infrastructure", "Amortisation — Sussex Partnership NHS Foundation Trust", "Amortisation — Oxford Health NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Impairments net of reversals — North East London NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "North East London NHS Foundation Trust"}],
        "description": "NELFT's £1.86M 2024-25 impairment is the IAS 36 net writedown across the trust's mental-health and community-services estate spanning Barking and Dagenham, Havering, Redbridge, Waltham Forest and parts of Essex. Anchor sites include Goodmayes Hospital Ilford (the trust's main acute MH campus, with a long PFI history), King George Hospital MH liaison, and a long tail of community-mental-health and community-physical-health clinics. MEA-DRC revaluation under the 5-yearly cycle was applied; Goodmayes' older blocks drive the bulk of the writedown.",
        "beneficiaries": "c. 50 main sites serving c. 2.0M residents across NE London (4 boroughs) and Essex contracts; Goodmayes ~330 inpatient MH beds, plus c. 45 community CMHT, CAMHS and community-physical-health clinics.",
        "legal_basis": "IAS 36 Impairment of Assets · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£1.86M"},
            {"label": "5-year impairment trend", "value": "2020-21 c. £0.4M → 2021-22 c. £0.9M → 2022-23 c. £1.3M → 2023-24 c. £1.6M → 2024-25 £1.86M"},
            {"label": "Estate gross floor area revalued", "value": "c. 90,000 m² across MH and community estate"},
            {"label": "MEA-DRC vs market value driver", "value": "Goodmayes Hospital older blocks (post-Edwardian fabric, partial 1960s-80s rebuild) below modernisation cost; PFI-built newer blocks revalue less aggressively"},
            {"label": "RAAC scope", "value": "Not on HSSIB confirmed-RAAC list; surveys closed at Goodmayes"},
            {"label": "NHP cohort + Reset Jan 2025 status", "value": "Not in NHP cohort; capital programme via NEL ICB"},
            {"label": "PFI footprint", "value": "Goodmayes has historic partial PFI for newer accommodation blocks"},
            {"label": "Combined MH + community driver", "value": "Trust runs community-physical-health alongside MH → larger asset base subject to revaluation"},
            {"label": "Valuation cycle phase", "value": "5-yearly full revaluation 2024-25; interim VOA indexation"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + external valuer DHSC central panel"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NEL ICB · IAS 36 / DHSC GAM oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Goodmayes consolidation · Successor: NEL ICS estate strategy review"}
        ],
        "notes": "NELFT's impairment line is structurally moderate but on a sustained upward trajectory because the Goodmayes Hospital estate combines older Edwardian-era fabric with 1960s-80s rebuild and newer partial-PFI blocks — the older portion drives recurring MEA-DRC writedowns under the 5-yearly cycle. The trust's combined MH and community-physical-health remit (across 4 NE London boroughs plus Essex contracts) inflates the revaluation base relative to a pure-MH peer. Without an NHP slot, capital renewal flows through NEL ICS bids; the impairment is structurally locked-in upward as the older Goodmayes blocks have their economic life extended through refurb-led strategy.",
        "sources": [
            {"publisher": "North East London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nelft.nhs.uk/about-us-publications"},
            {"publisher": "NHS England", "title": "NHS provider finance and operational performance 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NELFT provider profile (RAT)", "url": "https://www.cqc.org.uk/provider/RAT"},
            {"publisher": "National Audit Office", "title": "NHS Estate condition report 2024", "url": "https://www.nao.org.uk/reports/nhs-estate/"}
        ],
        "related": ["North East London NHS Foundation Trust", "Premises & Infrastructure", "Impairments net of reversals — Hertfordshire Partnership University NHS Foundation Trust", "Impairments net of reversals — Bradford District Care NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Impairments net of reversals — Bradford District Care NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Bradford District Care NHS Foundation Trust"}],
        "description": "BDCFT's £1.81M 2024-25 impairment is the IAS 36 net writedown across the trust's MH and community-services estate centred on Lynfield Mount Hospital Bradford (the trust's main psychiatric inpatient unit), Airedale Centre for Mental Health Keighley, plus c. 40 community-mental-health and community-physical-health sites across the Bradford District and Craven footprint. The 2024-25 5-yearly MEA-DRC revaluation cycle reset hit Lynfield Mount's older blocks (post-1970s) the hardest; Airedale's newer build absorbs less impairment.",
        "beneficiaries": "c. 50 sites serving c. 600,000 residents of Bradford District and Craven (Bradford, Keighley, Skipton, Ilkley); Lynfield Mount ~140 inpatient MH beds, Airedale Centre for Mental Health, plus c. 40 community CMHT/CAMHS/IAPT and community-physical-health clinics.",
        "legal_basis": "IAS 36 Impairment of Assets · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£1.81M"},
            {"label": "5-year impairment trend", "value": "2020-21 c. £0.3M → 2021-22 c. £0.6M → 2022-23 c. £1.0M → 2023-24 c. £1.4M → 2024-25 £1.81M"},
            {"label": "Estate gross floor area revalued", "value": "c. 60,000 m² across MH and community estate"},
            {"label": "MEA-DRC vs market value driver", "value": "Lynfield Mount 1970s blocks structurally below modernisation cost-to-replicate; Airedale newer build absorbs less writedown"},
            {"label": "RAAC scope", "value": "Not on HSSIB confirmed-RAAC list"},
            {"label": "NHP cohort + Reset Jan 2025 status", "value": "Not in NHP cohort; capital programme via West Yorkshire ICB"},
            {"label": "Combined MH + community driver", "value": "Trust runs community-physical-health alongside MH → broader revaluation base"},
            {"label": "IAPT and CAMHS expansion", "value": "Long Term Plan IAPT expansion has driven leased-clinic additions; lease impairments may flow when sites surrendered"},
            {"label": "Valuation cycle phase", "value": "5-yearly full revaluation 2024-25"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + external valuer DHSC central panel"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + West Yorkshire ICB · IAS 36 / DHSC GAM oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Bradford District Care Trust formation · Successor: West Yorkshire ICS estate-rationalisation strategy"}
        ],
        "notes": "BDCFT's impairment is structurally moderate but on a sustained upward path because Lynfield Mount Hospital's 1970s blocks face MEA-DRC modernisation cost-to-replicate above carrying value under the 5-yearly cycle. The trust's combined MH and community-physical-health remit means the revaluation base extends beyond pure-MH inpatient stock. The Long Term Plan-driven IAPT and CAMHS expansion has added leased community clinic capacity; when those leases are surrendered or relocated, residual carrying values can trigger lease-impairment add-ons. Without an NHP slot, capital renewal flows through West Yorkshire ICS bids — keeping the impairment trajectory mildly upward.",
        "sources": [
            {"publisher": "Bradford District Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bdct.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "NHS provider finance and operational performance 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "BDCFT provider profile (RJV)", "url": "https://www.cqc.org.uk/provider/RJV"},
            {"publisher": "National Audit Office", "title": "NHS Estate condition report 2024", "url": "https://www.nao.org.uk/reports/nhs-estate/"}
        ],
        "related": ["Bradford District Care NHS Foundation Trust", "Premises & Infrastructure", "Impairments net of reversals — North East London NHS Foundation Trust", "Impairments net of reversals — Leeds and York Partnership NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Transport (business + patient) — Leeds and York Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Leeds and York Partnership NHS Foundation Trust"}],
        "description": "LYPFT's £1.81M 2024-25 transport line covers staff business mileage (community-mental-health, CAMHS, eating-disorder specialist clinicians) plus patient transport for inpatient admissions and S136 conveyance to The Becklin Centre and Newsam Centre Leeds and Bootham Park-successor sites in York. The trust holds national tertiary specialist contracts (gender identity, eating disorders, deafness MH) which add long-distance patient and clinician travel beyond the Leeds-York corridor. AfC Section 17 governs reimbursement; pool-vehicle leases sit under IFRS 16.",
        "beneficiaries": "c. 3,500 community + MH clinicians driving across West Yorkshire (Leeds, Wakefield) + York + national specialist catchments; c. 750,000 patient contacts per year include community visits and tertiary-specialty patient travel; gender-identity and eating-disorder contracts pull patients from across the North.",
        "legal_basis": "AfC Terms and Conditions Section 17 (Travel and Subsistence) · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 · HMRC Approved Mileage Allowance Payments (AMAP) · IFRS 16 Leases (pool-vehicle leases)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.81M"},
            {"label": "Workforce travelling", "value": "c. 3,500 community + MH clinicians using personal or pool vehicles for visits"},
            {"label": "Geographic reach", "value": "Leeds + York + tertiary specialist catchment across the North; gender + eating-disorder + deaf MH contracts"},
            {"label": "Reimbursement rate", "value": "AfC Section 17 — 56p/mile first 3,500 miles 'standard rate', 20p/mile thereafter"},
            {"label": "Pool-vehicle fleet", "value": "Trust runs limited pool fleet; primary mode is personal-vehicle reimbursement"},
            {"label": "S136 / patient conveyance", "value": "Conveyance to Becklin Centre + Newsam Centre Leeds (replaced High Royds 2009); York acute MH after 2015 Bootham Park closure now via leased modular site"},
            {"label": "Tertiary specialty driver", "value": "National gender identity + adult eating disorder + deaf MH contracts pull travel beyond Yorkshire"},
            {"label": "Delivery body", "value": "Trust transport function · Section 17 reimbursement via NHS BSA payroll"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + West Yorkshire ICB · AfC Staff Council oversight"},
            {"label": "Funding trajectory", "value": "Rising — AfC mileage rate static at 56p since 2014 vs HMRC 45p AMAP comparison; specialty patient-travel grows with demand"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2009 High Royds Hospital site closure simplified routing · Successor: AfC Section 17 review pending; ICS shared-fleet pilots under exploration"},
            {"label": "Evaluation evidence", "value": "NHS Pay Review Body evidence rounds 2023-24; CQC inspections of community MH services"}
        ],
        "notes": "LYPFT's transport spend is structurally larger than typical for its turnover because the trust holds national tertiary specialist contracts — Leeds Gender Identity Service, Adult Eating Disorder Service, and the National Deaf Mental Health Service — which generate long-distance clinician travel and patient-conveyance flows beyond the Leeds-York corridor. The York acute MH bedbase has been on temporary modular accommodation since the 2015 closure of Bootham Park Hospital, so inter-site cross-cover travel (Leeds-York 26 miles each way) sits in this line. The static 56p AfC mileage rate against HMRC 45p AMAP is being tested by NHS Pay Review Body submissions; West Yorkshire ICS is exploring shared-fleet pilots that may reduce pool-vehicle lease cost over time.",
        "sources": [
            {"publisher": "Leeds and York Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsandyorkpft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Employers", "title": "AfC Section 17 Travel and Subsistence Handbook", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "HM Revenue and Customs", "title": "Approved Mileage Allowance Payments rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Pay Review Body", "title": "37th Report 2024", "url": "https://www.gov.uk/government/publications/nhs-pay-review-body-37th-report-2024"}
        ],
        "related": ["Leeds and York Partnership NHS Foundation Trust", "Premises & Infrastructure", "Transport (business + patient) — Berkshire Healthcare NHS Foundation Trust", "Transport (business + patient) — Norfolk and Suffolk NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Business rates — Oxleas NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Oxleas NHS Foundation Trust"}],
        "description": "Oxleas's £1.80M 2024-25 business rates bill is the VOA-set NDR liability across the trust's south-east London and Kent estate — Oxleas House Queen Elizabeth Hospital Woolwich (the trust's main acute MH unit), Memorial Hospital Shooters Hill, Green Parks House Bromley, plus a long tail of community-mental-health, learning-disability and forensic clinics. Notably, Oxleas runs HMP Belmarsh, HMP Isis and Thameside healthcare under a contracted prison-mental-health remit. LGFA 1988 Schedule 6 valuation applies; standard 49.9p multiplier on most large hereditaments.",
        "beneficiaries": "c. 60 hereditaments across south-east London (Bexley, Bromley, Greenwich) and parts of Kent; serving c. 1.0M residents; Oxleas House ~80 inpatient MH beds; Green Parks House and dispersed community + LD + forensic + prison-MH estate.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.80M"},
            {"label": "Multiplier applied", "value": "Standard 49.9p on Oxleas House, Green Parks House, larger LD units; small 49.9p on community CMHT/CAMHS"},
            {"label": "Hereditament count", "value": "c. 60 occupied sites across Bexley, Bromley, Greenwich + Kent + prison healthcare contract sites"},
            {"label": "Largest single hereditament", "value": "Oxleas House at QEH Woolwich — VOA RV in £0.6-0.8M band; co-located with QEH acute"},
            {"label": "Charitable relief status", "value": "NHS FT — no mandatory 80% relief"},
            {"label": "Prison healthcare overlay", "value": "Trust runs HMP Belmarsh, HMP Isis, HMP/YOI Thameside healthcare — rates on healthcare areas charged to Oxleas under contract"},
            {"label": "VOA revaluation cycle", "value": "2023 list applies 2024-25; 2026 revaluation under NDR Act 2023 3-yearly cadence"},
            {"label": "Delivery body", "value": "VOA · Bexley, Bromley, Greenwich + Kent district councils billing · NHS BSA central rates payment"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG NDR policy · DHSC sponsor · NHSE London + South East London ICB"},
            {"label": "Funding trajectory", "value": "Rising — 2023 revaluation +c. 3% over 2017 list; 2025-26 multiplier split lifts standard-rate sites"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 NDR list · Successor: 2026 revaluation under 3-yearly cadence"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; HMPPS oversight of prison healthcare contracts"}
        ],
        "notes": "Oxleas's rates exposure is shaped by an unusual mix: a relatively small inpatient bedbase combined with the prison-mental-healthcare contract (HMP Belmarsh, HMP Isis, HMP/YOI Thameside) where the healthcare-area NDR is recharged to the trust under the HMPPS contract. The community-MH and learning-disability tail across Bexley, Bromley and Greenwich generates the long hereditament list. Oxleas House sits within the QEH Woolwich PFI estate (Lewisham and Greenwich Trust is the freeholder); rates apportionment between the host acute and Oxleas is set by VOA. The 2025-26 multiplier reform (55.5p standard) lifts the bill on the larger hereditaments.",
        "sources": [
            {"publisher": "Oxleas NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.oxleas.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Oxleas NHS FT provider profile (RPG)", "url": "https://www.cqc.org.uk/provider/RPG"},
            {"publisher": "NHS Confederation", "title": "Business rates and the NHS — briefing 2024", "url": "https://www.nhsconfed.org/publications"}
        ],
        "related": ["Oxleas NHS Foundation Trust", "Premises & Infrastructure", "Business rates — South London and Maudsley NHS Foundation Trust", "Business rates — Kent and Medway NHS and Social Care Partnership Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
    "Lease expenditure — Leicestershire Partnership NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Leicestershire Partnership NHS Trust"}],
        "description": "LPT's £1.78M 2024-25 lease expenditure line is dominated by IFRS 16 right-of-use asset depreciation and interest on the trust's NHS Property Services-leased community-clinic estate plus a residual short-term and low-value lease pool. The line stepped up materially from 2022-23 onward following the IFRS 16 transition that brought operating leases onto the balance sheet across community CMHT, CAMHS and IAPT clinics. Bradgate Mental Health Unit Glenfield is the main inpatient hub and is freehold; the lease line is community-driven.",
        "beneficiaries": "c. 60 leased sites primarily NHSPS-let community clinics across Leicester city, Leicestershire and Rutland (3 unitary + 7 districts) serving c. 1.1M residents; Bradgate Mental Health Unit ~120 inpatient beds (freehold, not in line); Agnes Unit, Beechwood, plus c. 50 community CMHT/CAMHS/IAPT clinics.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954 · IAS 36 (lease impairments)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.78M"},
            {"label": "Pre-IFRS-16 vs post-IFRS-16 step-up", "value": "Operating-lease rentals previously expensed in full now split into ROU depreciation + lease-liability interest from FY2022-23 (NHS adoption date)"},
            {"label": "Lease portfolio composition", "value": "c. 60 community-clinic leases predominantly with NHS Property Services + LIFT Co + small private-LL share"},
            {"label": "Largest leases", "value": "NHSPS-let community-MH and CAMHS clinics across Leicester city + county; multi-year terms"},
            {"label": "Short-term + low-value exemption", "value": "Below-£5k or under-12-month leases expensed straight-line under IFRS 16 exemption — small minority of trust portfolio"},
            {"label": "NHSPS dispute context", "value": "NHSPS pricing methodology disputed sector-wide (market-rents vs cost-recovery); LPT subject to standard NHSPS facilities-management charging"},
            {"label": "Delivery body", "value": "Trust Estates · NHS Property Services as primary lessor · LIFT Co joint-venture exposure"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Leicester, Leicestershire and Rutland ICB · IFRS 16 / GAM ch.7 oversight"},
            {"label": "Funding trajectory", "value": "Rising — IFRS 16 ROU depreciation steady-state plus rent reviews on existing leases; community-MH expansion adds new leases"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 operating-lease rental line · Successor: ICS estate-rationalisation may consolidate community sites"},
            {"label": "Evaluation evidence", "value": "CQC ratings 2023-24; NAO 2023 NHS Estate report; NHSPS sector dispute coverage"},
            {"label": "Trust-specific context", "value": "Bradgate MH Unit (freehold, opened 1995, the main acute MH bedbase) is not in the lease line; CAMHS Tier 4 services contracted out drive specialist-clinic lease entries"}
        ],
        "notes": "LPT's lease line is overwhelmingly an NHS Property Services exposure — the trust's c. 60 community-clinic leases are predominantly NHSPS-let, and the sector-wide dispute over NHSPS pricing methodology (market-rents passed through to trusts vs cost-recovery basis) directly affects the steady-state cost. The IFRS 16 transition in 2022-23 split former operating-lease rentals into ROU depreciation plus lease-liability interest, which lifted the line presentationally even where cash rent was unchanged. Bradgate MH Unit (opened 1995, freehold) is the main acute MH bedbase and sits outside this line. Leicester, Leicestershire and Rutland ICS is exploring estate consolidation that may shrink the community-lease tail.",
        "sources": [
            {"publisher": "Leicestershire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicspart.nhs.uk/about/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "About NHS Property Services and our charging methodology", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Leicestershire Partnership NHS Trust provider profile (RT5)", "url": "https://www.cqc.org.uk/provider/RT5"},
            {"publisher": "National Audit Office", "title": "NHS Estate condition report 2024", "url": "https://www.nao.org.uk/reports/nhs-estate/"}
        ],
        "related": ["Leicestershire Partnership NHS Trust", "Premises & Infrastructure", "Lease expenditure — Mersey Care NHS Foundation Trust", "Lease expenditure — Oxford Health NHS Foundation Trust", "Department of Health and Social Care", "NHS Property Services"]
    },
    "Social security & levy — Dudley Integrated Health and Care NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Dudley Integrated Health and Care NHS Trust"}],
        "description": "DIHC's £1.77M 2024-25 social security and levy line is the employer-side National Insurance contributions plus the Apprenticeship Levy (0.5% of paybill above £3M) on the trust's c. 600-strong workforce. The trust is one of the smallest NHS provider trusts (formed April 2020 to deliver primary-care-network-led integrated community + MH services in Dudley). The line will step up materially from April 2025 when the headline employer NIC rate rises from 13.8% to 15.0% and the secondary threshold drops from £9,100 to £5,000 — a structural cost increase across the NHS provider base.",
        "beneficiaries": "c. 600 employees on AfC + medical contracts at DIHC; the trust delivers community-physical-health, primary-care-network coordination and some mental-health services to c. 320,000 Dudley residents — one of the smallest NHS provider footprints in England.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Social Security (Contributions) Regulations 2001 · National Insurance Contributions (Secondary Class 1 Contributions) Act 2025 (Apr 2025 rate change) · Apprenticeship Levy under Finance Act 2016 s.99 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25 · IAS 19 Employee Benefits",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£1.77M"},
            {"label": "Employer NIC rate 2024-25", "value": "13.8% on earnings above £9,100 secondary threshold"},
            {"label": "Apr 2025 step-up", "value": "Rate rises to 15.0% + secondary threshold falls to £5,000 — material cost uplift on entire NHS provider base"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill above £3M annual allowance — DIHC paybill in scope"},
            {"label": "Workforce size", "value": "c. 600 employees — among the smallest NHS provider trusts in England"},
            {"label": "Trust formation", "value": "Established April 2020 as integrator-trust for Dudley health and care; novel PCN-led integration model"},
            {"label": "Delivery body", "value": "HMRC PAYE collection · NHS BSA central payroll service · Department for Education on Apprenticeship Levy reporting"},
            {"label": "Policy owner", "value": "HM Treasury + HMRC NIC policy · DfE Apprenticeship Levy policy · DHSC sponsor · Black Country ICB"},
            {"label": "Funding trajectory", "value": "Step-up Apr 2025 from 13.8% to 15.0% + threshold drop; 2024 Autumn Budget announced compensating funding to NHS but not 1-for-1 across all categories"},
            {"label": "Apr 2025 NIC compensation", "value": "Treasury announced employer-NIC compensation for direct NHS staff via DEL uplift; private-contracted social care + GP excluded"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 Dudley CCG + provider arrangements · Successor: ongoing Black Country ICS integration; potential merger discussions"},
            {"label": "Evaluation evidence", "value": "NHS Confederation Apr-2025-NIC briefings; HMRC Notice 480 NIC guidance"}
        ],
        "notes": "DIHC's social-security line is small in absolute terms because the trust itself is small — established April 2020 as a novel primary-care-network-led integrator trust for Dudley, with a c. 600-strong workforce — but the April 2025 NIC step-up (rate 13.8% → 15.0%, secondary threshold £9,100 → £5,000) hits this line directly. The 2024 Autumn Budget announced compensating funding to NHS providers via DEL uplift, though the compensation does not fully cover indirectly-employed staff (agency, primary care subcontractors). The Apprenticeship Levy element (0.5% of paybill over £3M) is a comparatively stable component. As the smallest English NHS provider trust, DIHC's per-trust admin overhead on payroll-tax compliance is proportionally heavy; ICS shared-services consolidation is under exploration.",
        "sources": [
            {"publisher": "Dudley Integrated Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dihc.nhs.uk/about-us/publications/"},
            {"publisher": "HM Revenue and Customs", "title": "Notice 480 — National Insurance contributions", "url": "https://www.gov.uk/government/publications/employers-further-guide-to-paye-and-national-insurance-contributions-cwg2"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — employer NIC reform", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Confederation", "title": "Employer NIC reform — implications for the NHS 2024-25", "url": "https://www.nhsconfed.org/publications"}
        ],
        "related": ["Dudley Integrated Health and Care NHS Trust", "Staff Costs", "Termination & post-employment — Dudley Integrated Health and Care NHS Trust", "Other & adjustments — Dudley Integrated Health and Care NHS Trust", "Department of Health and Social Care", "HM Revenue and Customs"]
    },
    "Business rates — Dorset Healthcare University NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Dorset Healthcare University NHS Foundation Trust"}],
        "description": "Dorset Healthcare's £1.77M 2024-25 business rates bill is the VOA-set NDR liability across the trust's combined community + mental-health estate spanning the BCP unitary authority (Bournemouth, Christchurch, Poole) and Dorset Council areas. Anchor sites include St Ann's Hospital Poole (the trust's main acute MH unit), Forston Clinic Charminster, Alderney Hospital Poole, plus c. 100 community-clinic and community-physical-health hereditaments. LGFA 1988 Schedule 6 valuation applies; standard 49.9p multiplier on inpatient hubs, small 49.9p on community CMHT.",
        "beneficiaries": "c. 110 hereditaments across BCP unitary + Dorset Council (2 unitary authorities) serving c. 770,000 residents; St Ann's Hospital Poole + Forston Clinic + Alderney Hospital + c. 100 community physical-health and MH clinics — combined-care portfolio drives a long site tail.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.77M"},
            {"label": "Multiplier applied", "value": "Standard 49.9p on St Ann's, Forston, Alderney, larger community-physical-health centres; small 49.9p on sub-£51k RV CMHT clinics"},
            {"label": "Hereditament count", "value": "c. 110 occupied sites — long tail driven by combined community-physical-health + MH remit"},
            {"label": "Largest single hereditament", "value": "St Ann's Hospital Poole — VOA RV in £0.6-0.8M band; main acute psychiatric unit"},
            {"label": "Charitable relief status", "value": "NHS FT — no mandatory 80% relief"},
            {"label": "VOA revaluation cycle", "value": "2023 list applies 2024-25; 2026 revaluation under NDR Act 2023 3-yearly cadence"},
            {"label": "Combined community + MH driver", "value": "Trust runs Dorset community-physical-health alongside MH → broader hereditament base than pure-MH peer"},
            {"label": "Delivery body", "value": "VOA · BCP Council + Dorset Council billing authorities · NHS BSA central rates payment"},
            {"label": "Policy owner", "value": "DLUHC/MHCLG NDR policy · DHSC sponsor · NHS Dorset ICB"},
            {"label": "Funding trajectory", "value": "Rising — 2023 revaluation +c. 3% over 2017 list; 2025-26 multiplier split lifts standard-rate hereditaments to 55.5p"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Dorset Community NHS Trust + Dorset HealthCare predecessor merger · Successor: 2026 revaluation; possible ICS estate-rationalisation"},
            {"label": "Evaluation evidence", "value": "CQC 'Outstanding' 2019 (later 'Good'); NHS Dorset ICB estate strategy 2024"}
        ],
        "notes": "Dorset Healthcare's c. 110 hereditaments — among the longest tails in the English MH/community-trust segment relative to turnover — reflect the trust's combined community-physical-health + MH remit across the two-unitary-authority Dorset ICS footprint (BCP + Dorset Council). The 2011 merger that created the trust consolidated two predecessor trusts' separate estate footprints. The 2025-26 multiplier reform locks in upward pressure on the larger inpatient hub hereditaments (St Ann's Poole, Forston Charminster, Alderney). NHS Dorset ICB's 2024 estate strategy is exploring shared-clinic consolidation across the trust + Dorset County Hospital + University Hospitals Dorset, which may shrink the community-clinic hereditament tail over the medium term.",
        "sources": [
            {"publisher": "Dorset Healthcare University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dorsethealthcare.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Dorset Healthcare University NHS FT provider profile (RDY)", "url": "https://www.cqc.org.uk/provider/RDY"},
            {"publisher": "NHS Confederation", "title": "Business rates and the NHS — briefing 2024", "url": "https://www.nhsconfed.org/publications"}
        ],
        "related": ["Dorset Healthcare University NHS Foundation Trust", "Premises & Infrastructure", "Amortisation — Dorset Healthcare University NHS Foundation Trust", "Business rates — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care", "NHS Mental Health Trusts"]
    },
}
