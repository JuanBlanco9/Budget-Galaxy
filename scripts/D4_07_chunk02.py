# -*- coding: utf-8 -*-
# D4_07 Premises (other) — chunk 02 (20 NHS trusts)
# Hand-curated trust-specific enrichment entries. Tailor-made — no boilerplate.

NEW = {
    "Premises (other) — Oxford University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
        "description": "Non-depreciation estate running costs across OUH's four hospital sites — John Radcliffe (Headington campus, including West Wing, Children's, Women's Centre, West Wing PFI block), Churchill (oncology + transplant + renal), Nuffield Orthopaedic Centre (Headington), and the Horton General (Banbury). Headington campus density and the academic co-location with Oxford University Medical Sciences Division drive higher-grade laboratory and imaging utilities.",
        "beneficiaries": "Thames Valley + national tertiary catchment — major trauma + neurosciences + transplant at JR, oncology + renal at Churchill, planned orthopaedics at NOC, district acute at Horton General (Banbury, ~700,000 catchment).",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£46.88M"},
            {"label": "Share of trust total opex", "value": "c. 3.5%"},
            {"label": "Estate scale", "value": "4 hospital sites · ~340,000 m² clinical floorspace · Headington campus dominant"},
            {"label": "Hard FM model", "value": "Mixed in-house Estates + JR West Wing PFI carve-out (PFI charges in D4_11, NOT here)"},
            {"label": "Horton General", "value": "Banbury district hospital — separate rural premises load (35-mile transfer to JR)"},
            {"label": "Academic co-location", "value": "Oxford BRC labs + Big Data Institute neighbours drive lab-grade HVAC"},
            {"label": "NHP scheme status", "value": "No core NHP scheme; Oxford Cancer + Oxford Children's hospital ambitions outside NHP cohort"},
            {"label": "Net Zero milestone", "value": "Churchill heat decarbonisation + Headington district heat network feasibility"},
            {"label": "YoY change", "value": "c. +6% (energy reset + research-grade utilities + Horton resilience works)"},
            {"label": "Peer benchmark", "value": "Top-quartile teaching-trust premises spend (multi-campus + academic-grade utilities)"}
        ],
        "notes": "OUH's premises cost reflects four campuses each with distinct estate dynamics — JR's PFI'd West Wing is fenced off this line, but the rest of the Headington estate (1970s towers + research wings) carries heavy hard-FM load. The Horton General in Banbury adds rural-acute premises cost (own A&E, maternity, theatres) disproportionate to its size. Energy contract under NHS RM6011 saw partial 2022-23 spike pass-through. No core NHP scheme means continued operating spend on legacy estate rather than new-build transition.",
        "sources": [
            "https://www.ouh.nhs.uk/about/publications/annual-report-and-accounts.aspx",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["Oxford University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "Estate running costs across ESNEFT's two main acute sites — Ipswich Hospital and Colchester General Hospital — plus an extensive community estate (Aldeburgh, Felixstowe, Halstead, Bluebird Lodge, Walton-on-the-Naze) inherited from the 2018 merger of the two former trusts. Colchester General is a 1980s-vintage build with significant backlog; Ipswich's tower block dates from the same era.",
        "beneficiaries": "c. 800,000 patients across north-east Essex + east Suffolk — A&E + maternity at both Ipswich and Colchester, with cancer services centralised at Colchester (Helen Rollason Cancer Centre) and orthopaedics at Ipswich.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£46.28M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "2 acute hospitals + 20+ community sites across c. 60-mile Essex/Suffolk corridor"},
            {"label": "Hard FM model", "value": "In-house Estates + outsourced soft-FM (Serco at Colchester historically)"},
            {"label": "RAAC status", "value": "RAAC identified at Ipswich Hospital — mitigation works/props in place across affected areas"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort; backlog maintenance pressure persistent post-merger"},
            {"label": "Merger legacy", "value": "2018 ESNEFT merger left two estates with different FM contracts and standards to harmonise"},
            {"label": "Net Zero milestone", "value": "Colchester solar PV + LED rolling programme; Ipswich BMS upgrade phase 2"},
            {"label": "YoY change", "value": "c. +6% (RAAC mitigation + energy + soft-FM uplift)"},
            {"label": "Peer benchmark", "value": "Above-median acute-trust premises spend (2-site dispersion + RAAC)"}
        ],
        "notes": "ESNEFT's premises spend is materially inflated by RAAC mitigation works at Ipswich Hospital — props, ceiling monitoring and partial decants sit in this line. The geographic spread (Ipswich to Clacton-on-Sea is ~50 miles) plus the merger-legacy of two separate FM contracts means the trust carries duplicate management overhead it has been progressively rationalising. No NHP funding means RAAC remediation is being financed through capital rather than rebuild.",
        "sources": [
            "https://www.esneft.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.hssib.org.uk/patient-safety-investigations/raac/"
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "Estate running costs across STH's five-hospital footprint — Royal Hallamshire (Glossop Road), Northern General (Herries Road, including the Major Trauma Centre and Cardiothoracic Centre), Weston Park (specialist cancer), Charles Clifford Dental, and Jessop Wing (maternity). Hallamshire's 18-storey tower (opened 1978) and the dispersed Northern General campus are the principal cost drivers.",
        "beneficiaries": "c. 640,000 Sheffield residents plus South Yorkshire + Bassetlaw tertiary referrals — major trauma + cardiothoracic at Northern General, neurosciences + tertiary medicine at Hallamshire, regional cancer at Weston Park.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£45.95M"},
            {"label": "Share of trust total opex", "value": "c. 3.5%"},
            {"label": "Estate scale", "value": "5 hospitals across Sheffield · Hallamshire 18-storey tower + sprawling Northern General campus"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (lift OEMs, BMS)"},
            {"label": "Hallamshire tower", "value": "1978-vintage tower block — high-rise FM premium (lift maintenance, façade, fire compartmentation)"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort; longstanding case for Hallamshire replacement unfunded"},
            {"label": "Cancer estate", "value": "Weston Park is one of three dedicated cancer hospitals in England — specialist radiotherapy bunker utilities"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat decarbonisation at Northern General; LED rolling"},
            {"label": "YoY change", "value": "c. +5-7% (energy reset + Hallamshire fire-safety remediation)"},
            {"label": "Peer benchmark", "value": "Mid-range vs large teaching peers per m² but absolute cost elevated by tower-block FM"}
        ],
        "notes": "STH's premises cost is shaped by the Hallamshire tower — high-rise FM (cladding, fire compartmentation post-Grenfell, lift modernisation) commands a structural premium absent from low-rise estates. Northern General's mile-long campus carries grounds, security and inter-block transport overhead. Weston Park's radiotherapy bunkers require specialist utility resilience. No NHP scheme means continued operating spend on a tower whose long-term replacement remains unfunded.",
        "sources": [
            "https://www.sth.nhs.uk/about-us/corporate-information/annual-report",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Estate running costs across RFL's three-hospital group — Royal Free Hampstead (the 1970s Hampstead tower, North London tertiary), Barnet General, and Chase Farm Hospital (Enfield, rebuilt 2018 — the modern building's PFI/charges sit in D4_11, not here). Premises (other) is dominated by the Hampstead tower's FM load and Barnet's 1990s-vintage estate.",
        "beneficiaries": "c. 1.6M patients across north-central London — liver transplant + HIV + amyloidosis + haematology tertiary services at Hampstead; general acute at Barnet and Chase Farm.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£44.11M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "3 acute hospitals across NCL · Hampstead 1970s tower dominates"},
            {"label": "Hard FM model", "value": "In-house Estates + Chase Farm new-build FM contractor (PFI charges in D4_11)"},
            {"label": "Hampstead tower", "value": "Hampstead 13-storey block (1974 opened) — high-rise FM + fire-safety remediation overhead"},
            {"label": "Group model", "value": "RFL Group hosts North Mid acute services partnership — premises remain trust-specific"},
            {"label": "NHP scheme status", "value": "Not in current NHP cohort; long-term Hampstead redevelopment unfunded"},
            {"label": "Net Zero milestone", "value": "Hampstead heat decarbonisation feasibility + LED rolling"},
            {"label": "YoY change", "value": "c. +5-7% (energy + Hampstead fire-safety + soft-FM uplift)"},
            {"label": "Peer benchmark", "value": "Below absolute London-teaching peers but high per-m² at Hampstead due to tower"}
        ],
        "notes": "Royal Free's premises cost is structurally weighted to the Hampstead tower, which carries high-rise FM premium (cladding remediation, lift modernisation, fire compartmentation) inherited from a 1970s typology. Chase Farm's modern PFI building carves out a chunk of estate cost into D4_11 — what remains in Premises (other) is the older estate and shared services. No NHP scheme means the long-debated Hampstead replacement remains operating-cost dependent.",
        "sources": [
            "https://www.royalfree.nhs.uk/about-us/corporate-information/annual-reports/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — North Bristol NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "North Bristol NHS Trust"}],
        "description": "Estate running costs centred on the Brunel building at Southmead Hospital — opened May 2014 as a £430M PFI scheme delivered by Carillion (Hospital Company (Southmead) Ltd) — plus the older Cotswold and Beaufort wings, and the Cossham Hospital satellite. The Brunel PFI unitary charge sits in D4_11, but soft-FM extensions, retrofit and non-PFI estate run through Premises (other).",
        "beneficiaries": "c. 900,000 patients across Bristol, South Gloucestershire and North Somerset — major trauma + neurosurgery + plastic surgery + renal transplant tertiary services at Southmead.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£40.73M"},
            {"label": "Share of trust total opex", "value": "c. 4.5%"},
            {"label": "Estate scale", "value": "Southmead campus (Brunel + legacy wings) + Cossham + community sites"},
            {"label": "Hard FM model", "value": "PFI consortium (HCSL, originally Carillion → now Vinci/EQUANS) for Brunel; in-house elsewhere"},
            {"label": "PFI carve-out", "value": "Brunel building unitary charge in D4_11 — NOT here; Premises (other) covers the residual estate"},
            {"label": "Carillion legacy", "value": "Carillion's 2018 collapse triggered FM provider novation — operational continuity preserved"},
            {"label": "Net Zero milestone", "value": "Brunel building energy-performance review under PFI variation; legacy estate LED conversion"},
            {"label": "Cossham Hospital", "value": "Modernised 2012 satellite for outpatients/diagnostics — separate FM"},
            {"label": "YoY change", "value": "c. +5-6% (energy + PFI variation cost + legacy estate maintenance)"},
            {"label": "Peer benchmark", "value": "Mid-range acute-trust premises spend; PFI carve-out reduces visible cost vs non-PFI peers"}
        ],
        "notes": "The Brunel PFI scheme, signed 2010 with Carillion as lead, dominates Southmead's estate but its unitary charge is reported separately in D4_11. Premises (other) reflects the older Cotswold/Beaufort wings, Cossham, and the soft-FM variations the trust has negotiated within and around the PFI envelope (e.g. catering insourcing tested 2017-18). Carillion's 2018 collapse novated FM to Vinci/EQUANS, which preserved continuity but compressed the trust's negotiating room on contract variations.",
        "sources": [
            "https://www.nbt.nhs.uk/about-us/our-publications/annual-report",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.nao.org.uk/reports/the-collapse-of-carillion/"
        ],
        "related": ["North Bristol NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Lancashire Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Lancashire Teaching Hospitals NHS Foundation Trust"}],
        "description": "Estate running costs across LTH's two-hospital footprint — the Royal Preston Hospital (Fulwood, including the major-trauma centre and regional neurosciences) and Chorley & South Ribble Hospital. Royal Preston's 1980s-vintage main block plus specialist tertiary services (cardiology, neurosciences, renal) drive specialist-utility load.",
        "beneficiaries": "c. 1.5M Lancashire and South Cumbria population for tertiary services, plus c. 370,000 local catchment for general acute — major trauma, neurosciences, renal, vascular, cardiology centralised at Royal Preston.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£40.42M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "2 acute hospitals (Royal Preston + Chorley) · ~140,000 m² clinical floorspace"},
            {"label": "Hard FM model", "value": "In-house Estates + outsourced soft-FM"},
            {"label": "NHP scheme status", "value": "New Hospitals for Lancashire and South Cumbria programme proposed Royal Preston replacement — pre-NHP business case stage; NHP Reset Jan 2025 deferred timeline"},
            {"label": "Chorley A&E", "value": "Chorley A&E reopened part-time 2017 after 2016 closure; estate carries modular extensions"},
            {"label": "Tertiary load", "value": "Major trauma + neurosciences + renal + vascular = high-resilience utility demand"},
            {"label": "Net Zero milestone", "value": "PSDS phase 3 funding for Royal Preston heat decarbonisation"},
            {"label": "YoY change", "value": "c. +6% (energy + Royal Preston backlog maintenance + Chorley modular)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median per m² (tertiary load + ageing main block)"}
        ],
        "notes": "Royal Preston's ageing main block is among the longest-debated NHS replacement candidates, with the 'New Hospitals for Lancashire and South Cumbria' programme moved to pre-NHP business case stage. The Reset (Jan 2025) further extends operating reliance on the existing estate, inflating Premises (other) for backlog maintenance and resilience works. Chorley's modular A&E extensions add non-permanent FM burden. PSDS-funded heat works underway at Royal Preston.",
        "sources": [
            "https://www.lancsteachinghospitals.nhs.uk/annual-reports",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["Lancashire Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Mersey Care NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Mersey Care NHS Foundation Trust"}],
        "description": "Mental-health, learning-disability, addictions and community-services premises running costs across Mersey Care's 100+ site Merseyside footprint — including the high-secure Ashworth Hospital (Maghull, one of three high-secure psychiatric hospitals in England), Clock View (Walton), Hesketh Centre (Southport), Rowan View (medium-secure), Whalley addiction services, plus the community estate inherited from the former Liverpool Community Health acquisition.",
        "beneficiaries": "1.5M+ Merseyside population for community + adult MH services; national catchment for high-secure forensic psychiatry at Ashworth; specialist personality-disorder + addictions cohorts.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety; high-secure under s.4 NHS Act) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£39.75M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "100+ MH/community sites across Merseyside + Ashworth high-secure (national)"},
            {"label": "Hard FM model", "value": "In-house Estates + specialist forensic-grade FM at Ashworth"},
            {"label": "Ashworth Hospital", "value": "1 of 3 English high-secure hospitals — perimeter, anti-ligature, custodial-grade utilities"},
            {"label": "MH-specific", "value": "s.136 suites + PICU + ECT room + medium-secure (Rowan View) + low-secure"},
            {"label": "Community legacy", "value": "Liverpool Community Health (acquired 2017) added c. 30 community premises"},
            {"label": "Net Zero milestone", "value": "Clock View + Rowan View energy-efficiency works; Ashworth heat scheme under feasibility"},
            {"label": "YoY change", "value": "c. +5-7% (energy + anti-ligature retrofit + forensic-FM uplift)"},
            {"label": "Peer benchmark", "value": "Above MH-trust median (high-secure + multi-site dispersion + community add-on)"}
        ],
        "notes": "Mersey Care's premises cost is uniquely shaped by Ashworth — high-secure psychiatric estate carries custodial-grade perimeter security, anti-ligature compliance and forensic-FM workforce premium not seen in standard MH trusts. The 2017 Liverpool Community Health acquisition added a long tail of small community sites (clinics, district-nurse bases) requiring active rationalisation. Anti-ligature retrofit programmes run continually post the 2018 NHSE MH safety guidance. RAAC clearance largely confirmed at the major secure sites.",
        "sources": [
            "https://www.merseycare.nhs.uk/about-us/our-publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.cqc.org.uk/provider/RW4"
        ],
        "related": ["Mersey Care NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Lewisham and Greenwich NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Lewisham and Greenwich NHS Trust"}],
        "description": "Estate running costs across LGT's two-hospital footprint — University Hospital Lewisham (Catford/Lewisham High Street) and Queen Elizabeth Hospital Woolwich (a 2001-vintage PFI build, with PFI charges reported separately in D4_11). Premises (other) covers the legacy Lewisham estate, the residual non-PFI elements at QEH Woolwich, and a constellation of community/outpatient sites.",
        "beneficiaries": "c. 526,000 patients across Lewisham and Greenwich boroughs — A&E, maternity, paediatrics at both sites; deprivation-weighted SE London catchment.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£38.22M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "2 acute hospitals + ~12 community sites · UHL legacy estate + QEH Woolwich PFI"},
            {"label": "Hard FM model", "value": "In-house at UHL; PFI consortium at QEH Woolwich (PFI charges in D4_11)"},
            {"label": "PFI carve-out", "value": "QEH Woolwich PFI unitary charge in D4_11; this line is residual estate + UHL"},
            {"label": "UHL Riverside Wing", "value": "Lewisham's modern Riverside Building (2008) co-exists with older blocks — mixed maintenance regime"},
            {"label": "Demand pressure", "value": "Highest-deprivation London acute trust by IMD weighting — high A&E + maternity throughput"},
            {"label": "Net Zero milestone", "value": "Lewisham LED conversion + QEH heat scheme under PFI variation"},
            {"label": "YoY change", "value": "c. +5-7% (energy + soft-FM uplift)"},
            {"label": "Peer benchmark", "value": "Above-median per m² for SE London peers (older Lewisham estate)"}
        ],
        "notes": "LGT's premises cost is split between two estate models — a self-managed Lewisham campus carrying historical maintenance debt, and the PFI'd QEH Woolwich whose unitary charge is reported in D4_11 (excluded here). The trust's 2013 South London Healthcare dissolution legacy left ongoing financial pressure on the QEH PFI envelope. Lewisham's mixed-vintage estate (Owen building, Riverside Wing) means uneven hard-FM costs per m².",
        "sources": [
            "https://www.lewishamandgreenwich.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.nao.org.uk/reports/the-performance-of-the-department-of-health-2012-13/"
        ],
        "related": ["Lewisham and Greenwich NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Royal Berkshire NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal Berkshire NHS Foundation Trust"}],
        "description": "Estate running costs centred on the Royal Berkshire Hospital site (London Road, Reading) — a constrained urban campus whose oldest blocks date from the 1830s (the Grade II listed Victorian original) alongside 1980s-vintage and modular extensions. The trust also runs satellite outpatient sites across West Berkshire (West Berkshire Community Hospital, Henley, Bracknell).",
        "beneficiaries": "c. 600,000 patients across Berkshire West (Reading, Wokingham, West Berkshire) — A&E, maternity, oncology, stroke services centralised in Reading.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£38.15M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "1 main hospital (constrained Reading central site) + 4 satellite community sites"},
            {"label": "Hard FM model", "value": "In-house Estates + outsourced soft-FM"},
            {"label": "Listed building", "value": "Victorian Grade II listed original block — restoration constraints raise unit cost"},
            {"label": "NHP scheme status", "value": "Royal Berkshire Hospital in NHP cohort 8 — Reset Jan 2025 deferred construction; site search still active (Reading-area)"},
            {"label": "Site constraint", "value": "London Road site is land-locked; mixed-vintage estate (1830s, 1980s, modular)"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat scheme; rooftop PV at modular blocks"},
            {"label": "YoY change", "value": "c. +6-8% (energy + NHP-deferred backlog + temporary works)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median per m² (listed-building + constrained site)"}
        ],
        "notes": "Royal Berkshire is one of the NHP cohort whose Reset (Jan 2025) most directly inflates Premises (other) — having planned to vacate London Road for a new-build, the trust now carries continued maintenance and temporary-works cost on a Victorian + 1980s mixed estate that is not fit-for-purpose long-term. Listed-building constraints on the original block raise unit hard-FM cost. Site-search uncertainty for the eventual replacement adds planning overhead.",
        "sources": [
            "https://www.royalberkshire.nhs.uk/about-us/publications/annual-reports/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["Royal Berkshire NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Great Ormond Street Hospital for Children NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Great Ormond Street Hospital for Children NHS Foundation Trust"}],
        "description": "Estate running costs at GOSH's central London (Bloomsbury) paediatric specialist campus — a dense, multi-block site combining the historic Cromwell Building (Grade II listed), the Octav Botnar Wing, the Morgan Stanley Clinical Building (2012), the Premier Inn Clinical Building (2018), and the Sight & Sound Centre (2020). Specialist paediatric tertiary services drive equipment-grade utility demand.",
        "beneficiaries": "Children with the rarest and most complex conditions — national + international referrals for paediatric cardiothoracic, neurosurgery, transplant, immunology, cancer, rare-disease genomics. Approximately 60,000 inpatient episodes annually.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£34.39M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "Single Bloomsbury campus · multi-block historic + modern · ~80,000 m² clinical"},
            {"label": "Hard FM model", "value": "In-house Estates + specialist sub-contractors (medical-gases, BMS, lift OEMs)"},
            {"label": "Listed buildings", "value": "Cromwell Building Grade II listed — constrained refurbishment options"},
            {"label": "Specialist load", "value": "Paediatric cardiothoracic, NICU, transplant + GMP-grade ATMP labs (Zayed Centre across road) drive resilient utilities"},
            {"label": "Charity-funded estate", "value": "GOSH Charity historically funds capital extensions (Botnar, Morgan Stanley, Premier Inn Wing) — operating cost still falls to Trust"},
            {"label": "Net Zero milestone", "value": "BMS upgrade in train; central London district-heat link feasibility"},
            {"label": "YoY change", "value": "c. +6% (energy + specialist-utility resilience + listed-building works)"},
            {"label": "Peer benchmark", "value": "High share of opex vs general specialist peers (single-site dense + paediatric tertiary load)"}
        ],
        "notes": "GOSH's premises cost is unusually high as a share of opex for a single-site specialist trust — driven by paediatric tertiary equipment power demand (NICU, ECMO, transplant theatres, ATMP manufacturing at the adjacent Zayed Centre), listed-building constraints on the Cromwell Building, and the dense Bloomsbury campus making logistics expensive. Operating cost on charity-funded extensions (e.g. Premier Inn Clinical Building 2018, Sight & Sound Centre 2020) falls to the Trust even where capital was donated.",
        "sources": [
            "https://www.gosh.nhs.uk/about-us/publications/annual-reports/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gosh.org/about-us/"
        ],
        "related": ["Great Ormond Street Hospital for Children NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Mersey and West Lancashire Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Mersey and West Lancashire Teaching Hospitals NHS Trust"}],
        "description": "Estate running costs across the post-July 2023 merged trust footprint — combining the former St Helens and Knowsley (Whiston Hospital, St Helens Hospital) and the former Southport and Ormskirk (Southport District General, Ormskirk Hospital). Whiston Hospital is a 2010 PFI build (Renova consortium) with PFI charges in D4_11; the rest of the estate is older mixed-vintage NHS.",
        "beneficiaries": "c. 600,000 patients across St Helens, Knowsley, Sefton, West Lancashire — A&E + acute services at Whiston (regional burns + plastics) and Southport, planned care at St Helens and Ormskirk.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£34.15M"},
            {"label": "Share of trust total opex", "value": "c. 4.5%"},
            {"label": "Estate scale", "value": "4 hospital sites post-merger · Whiston (PFI) + St Helens + Southport DGH + Ormskirk"},
            {"label": "Hard FM model", "value": "PFI consortium (Renova → operator) at Whiston/St Helens; in-house at Southport/Ormskirk"},
            {"label": "PFI carve-out", "value": "Whiston/St Helens PFI unitary charge in D4_11 — not in this line"},
            {"label": "Merger date", "value": "St Helens & Knowsley + Southport & Ormskirk merged 1 July 2023 — first full FY 2024-25"},
            {"label": "Southport DGH", "value": "Older 1980s estate — long-debated rebuild (NHP cohort exclusion); RAAC survey ongoing"},
            {"label": "Net Zero milestone", "value": "Southport solar PV + LED rolling; Whiston PFI variation for energy"},
            {"label": "YoY change", "value": "c. +6% (merger harmonisation + energy + Southport backlog)"},
            {"label": "Peer benchmark", "value": "Mid-range vs large acute peers; PFI carve-out reduces visible cost"}
        ],
        "notes": "MWL is a brand-new merged entity (1 July 2023) — 2024-25 is the first full reporting year and Premises (other) carries one-off harmonisation cost as the legacy FM contracts and Estates teams converge. The Whiston PFI fences off a chunk of estate cost into D4_11; what shows in this line is dominated by the older Southport and Ormskirk estate, which has long-debated rebuild needs that fell outside the NHP cohort. RAAC surveys continue at Southport.",
        "sources": [
            "https://www.merseywestlancs.nhs.uk/our-trust/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["Mersey and West Lancashire Teaching Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Lancashire and South Cumbria NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Lancashire and South Cumbria NHS Foundation Trust"}],
        "description": "Mental-health and learning-disability premises running costs across LSCft's c. 400-mile footprint from Carlisle/Kendal (south Cumbria) to Burnley/Blackburn (East Lancashire) and the Fylde Coast — including The Harbour (Blackpool, opened 2015 as a flagship MH inpatient hub), Avondale Unit (Preston), Guild Lodge (medium-secure forensic, Whittingham), Scarisbrick Centre, and a long tail of community MH bases.",
        "beneficiaries": "c. 1.8M Lancashire and South Cumbria population for adult MH, CAMHS, older-adult and learning-disability services; Guild Lodge medium-secure forensic catchment broader.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 + s.37/41 forensic) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£33.43M"},
            {"label": "Share of trust total opex", "value": "c. 9%"},
            {"label": "Estate scale", "value": "60+ MH/LD sites across Lancashire + South Cumbria · The Harbour flagship + Guild Lodge medium-secure"},
            {"label": "Hard FM model", "value": "In-house Estates + specialist forensic-FM at Guild Lodge"},
            {"label": "MH-specific", "value": "s.136 suites + PICU + ECT room + medium-secure (Guild Lodge) anti-ligature compliance"},
            {"label": "The Harbour", "value": "Flagship Blackpool inpatient unit (2015) — 154 beds, modern build, lower hard-FM cost per m²"},
            {"label": "Geographic dispersion", "value": "Carlisle to Blackburn ~120 miles — community estate carries travel/grounds cost"},
            {"label": "Net Zero milestone", "value": "Avondale + Guild Lodge BMS upgrades; The Harbour solar PV"},
            {"label": "YoY change", "value": "c. +5-7% (energy + anti-ligature retrofit at older inpatient units)"},
            {"label": "Peer benchmark", "value": "High share of opex vs MH-trust median (rural dispersion + forensic estate)"}
        ],
        "notes": "LSCft's premises cost is structurally elevated by the very wide rural footprint (Carlisle to Burnley) and the forensic estate at Guild Lodge (medium-secure). The Harbour flagship dilutes per-m² cost, but older inpatient units (Scarisbrick, Avondale) require ongoing anti-ligature retrofit under NHSE MH safety guidance. CQC enforcement at older sites in 2022-23 added compliance-driven works. Geographic dispersion means community-base rationalisation is a perennial board theme.",
        "sources": [
            "https://www.lscft.nhs.uk/about-us/publications-and-reports",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.cqc.org.uk/provider/RW5"
        ],
        "related": ["Lancashire and South Cumbria NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Buckinghamshire Healthcare NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Buckinghamshire Healthcare NHS Trust"}],
        "description": "Estate running costs across BHT's three-hospital footprint — Stoke Mandeville Hospital (Aylesbury, including the National Spinal Injuries Centre), Wycombe Hospital (High Wycombe), and Amersham Hospital — plus an integrated community estate inherited from BHT's 2011 acute+community integration. Stoke Mandeville's NSIC drives specialist long-stay rehabilitation utility demand.",
        "beneficiaries": "c. 580,000 Buckinghamshire residents — A&E + maternity at Stoke Mandeville, planned care + cardiac at Wycombe, rehab + community at Amersham; national catchment for the National Spinal Injuries Centre.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£33.13M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "3 hospitals + 25+ community sites · Stoke Mandeville campus dominant"},
            {"label": "Hard FM model", "value": "In-house Estates + outsourced soft-FM (catering insourced 2019)"},
            {"label": "National Spinal Injuries Centre", "value": "Specialist long-stay rehabilitation — 24/7 high-resilience utilities, hoists, pressure-care equipment"},
            {"label": "RAAC status", "value": "RAAC identified at Stoke Mandeville in 2023 — mitigation works ongoing across affected blocks"},
            {"label": "Wycombe minor injuries", "value": "Wycombe A&E downgraded to MIU 2014 — estate transitioned to planned care + cardiac"},
            {"label": "Net Zero milestone", "value": "Solar PV + LED rolling; Stoke Mandeville heat scheme under feasibility"},
            {"label": "YoY change", "value": "c. +7-9% (RAAC mitigation + energy + soft-FM uplift)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median (RAAC + tertiary spinal load + 3-site dispersion)"}
        ],
        "notes": "Buckinghamshire's premises spend is materially inflated by RAAC mitigation at Stoke Mandeville — confirmed affected in the 2023 HSSIB cohort, with props, monitoring and partial decants running through Premises (other). The National Spinal Injuries Centre adds specialist long-stay utility load (high humidity control, hoists, 24/7 backup) absent from typical district acutes. The 2011 acute+community integration left a long tail of small community premises requiring active rationalisation.",
        "sources": [
            "https://www.buckshealthcare.nhs.uk/our-trust/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.hssib.org.uk/patient-safety-investigations/raac/"
        ],
        "related": ["Buckinghamshire Healthcare NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Estate running costs centred on a single Kingston-upon-Thames hospital site — a constrained suburban campus with mixed-vintage blocks (Sir William Rous Wing, Esher Wing, Hambleden Wing) plus modular extensions. The trust also took on Kingston's adult community services in October 2023, materially expanding its estate footprint.",
        "beneficiaries": "c. 320,000 patients across Kingston + Richmond + parts of Surrey — A&E, maternity (one of largest in SW London), elective orthopaedic surgery, plus newly-acquired adult community services from Hounslow & Richmond CHCT.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£32.75M"},
            {"label": "Share of trust total opex", "value": "c. 7%"},
            {"label": "Estate scale", "value": "1 acute hospital + community estate (acquired Oct 2023) · ~70,000 m² acute footprint"},
            {"label": "Hard FM model", "value": "In-house Estates + outsourced soft-FM"},
            {"label": "Community services acquisition", "value": "Kingston adult community services transferred from HRCH October 2023 — c. 15 added sites"},
            {"label": "Site constraint", "value": "Galsworthy Road campus is land-locked; expansion via decant + modular only"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort; longstanding case for Kingston rebuild unfunded"},
            {"label": "Net Zero milestone", "value": "Solar PV at Esher Wing + LED rolling programme"},
            {"label": "YoY change", "value": "c. +8-10% (community services acquisition + energy + modular maintenance)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median per m² (constrained site + community add-on)"}
        ],
        "notes": "Kingston's 2024-25 Premises (other) is unusually inflated by the October 2023 transfer-in of Kingston adult community services from Hounslow & Richmond CHCT — the first full FY of carrying that estate footprint. The Galsworthy Road site is land-locked, meaning capacity expansion happens via decant + modular extensions which carry higher unit FM cost than permanent build. No NHP scheme means continued operating reliance on a 1970s-vintage core.",
        "sources": [
            "https://www.kingstonhospital.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.hrch.nhs.uk/about-us/news-and-publications"
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Hull University Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Hull University Teaching Hospitals NHS Trust"}],
        "description": "Estate running costs across HUTH's two-hospital footprint — Hull Royal Infirmary (Anlaby Road, including the regional major-trauma, neurosciences and the high-rise tower block opened 1967) and Castle Hill Hospital (Cottingham, including the Queen's Centre for Oncology and Haematology and the Daisy Centre). The HRI tower is among the oldest high-rise NHS hospital blocks still operational.",
        "beneficiaries": "c. 1.25M Hull, East Yorkshire + Northern Lincolnshire population for tertiary services — major trauma + neurosurgery + cardiology + specialist cancer + bone marrow transplant.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£32.29M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 hospitals (HRI + Castle Hill) · ~150,000 m² clinical · HRI tower 14 storeys"},
            {"label": "Hard FM model", "value": "In-house Estates + outsourced soft-FM"},
            {"label": "HRI tower block", "value": "1967-vintage 14-storey tower — among oldest operational NHS high-rise; fire-safety, cladding, lifts ongoing"},
            {"label": "NHP scheme status", "value": "HRI replacement in NHP cohort (Hull Royal Infirmary new-build) — Reset Jan 2025 deferred"},
            {"label": "Castle Hill", "value": "Modern oncology campus (Queen's Centre 2008, Daisy Centre 2013) — lower per-m² cost"},
            {"label": "Net Zero milestone", "value": "Castle Hill solar PV + heat-pump pilot; HRI tower-block fire-safety remediation"},
            {"label": "YoY change", "value": "c. +6-8% (energy + HRI fire-safety remediation + NHP-deferred backlog)"},
            {"label": "Peer benchmark", "value": "Mid-range per m² overall but high HRI-tower per-m² cost"}
        ],
        "notes": "HUTH's premises cost is split between an ageing high-rise core at Hull Royal Infirmary and a modern Castle Hill cancer campus. The HRI tower carries fire-safety remediation cost (cladding, compartmentation), structural surveys and lift modernisation — all running through Premises (other). HRI is in the NHP cohort, but the Reset (Jan 2025) extends operating reliance on the existing tower. Castle Hill's newer build dilutes the trust's per-m² average.",
        "sources": [
            "https://www.hey.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["Hull University Teaching Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Shrewsbury and Telford Hospital NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
        "description": "Estate running costs across SaTH's two-hospital footprint — Royal Shrewsbury Hospital (Mytton Oak Road) and Princess Royal Hospital (Telford). The trust has been mid-reconfiguration ('Hospitals Transformation Programme') since 2018 to specialise the two sites — emergency at Shrewsbury, planned care at Telford — with capital scheme caught up in NHP cohort 8 and the Reset delay.",
        "beneficiaries": "c. 500,000 patients across Shropshire, Telford & Wrekin and mid-Wales border — A&E split between both sites pending HTP, maternity, paediatrics, specialty acute services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£31.89M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "2 hospitals (RSH + PRH) · ~120,000 m² clinical floorspace"},
            {"label": "Hard FM model", "value": "In-house Estates + outsourced soft-FM"},
            {"label": "NHP scheme status", "value": "Hospitals Transformation Programme in NHP cohort 8 — Reset Jan 2025 deferred construction; both sites continue operating dual A&Es"},
            {"label": "Maternity context", "value": "Ockenden Review (2022) compliance work added estate spend on maternity environment improvements"},
            {"label": "CQC special measures", "value": "In CQC special measures since 2018 — premises-related Reg 15 actions live"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at Telford; LED rolling at both sites"},
            {"label": "YoY change", "value": "c. +6-8% (HTP-deferred backlog + Ockenden compliance + energy)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median (CQC-driven works + 2-site dispersion + transformation delay)"}
        ],
        "notes": "SaTH's premises spend is shaped by the prolonged Hospitals Transformation Programme — having planned to specialise sites and reduce duplication, the NHP Reset (Jan 2025) extends the operating cost of running two full A&E + acute estates rather than the planned single-emergency model. The Ockenden Review (2022) drove compliance investment on maternity environments, including dedicated bereavement suites and improved ward configurations. CQC special measures (since 2018) keep Reg 15 actions on the live agenda.",
        "sources": [
            "https://www.sath.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/publications/final-report-of-the-ockenden-review"
        ],
        "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — North East London NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "North East London NHS Foundation Trust"}],
        "description": "Mental-health and community premises running costs across NELFT's footprint covering Barking & Dagenham, Havering, Redbridge, Waltham Forest plus Essex community services (south-west and west Essex) and Kent & Medway children's services — including Goodmayes Hospital (Ilford, the historic asylum site, with the modern Sunflowers Court inpatient unit), Mascalls Park (medium-secure forensic, Brentwood), and a long tail of community premises.",
        "beneficiaries": "c. 4.7M total population served across NE London + parts of Essex + Kent — adult acute MH, CAMHS (largest CAMHS provider in England by some measures), forensic, community physical health.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 + forensic) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£31.00M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "Goodmayes campus + Mascalls Park forensic + ~80 community sites across NEL/Essex/Kent"},
            {"label": "Hard FM model", "value": "In-house Estates + specialist forensic-FM at Mascalls Park"},
            {"label": "Goodmayes site", "value": "Historic asylum site (1901); modern Sunflowers Court (2014) inpatient unit; legacy Victorian buildings being rationalised"},
            {"label": "Mascalls Park", "value": "Medium-secure forensic — anti-ligature + perimeter compliance regime"},
            {"label": "Geographic dispersion", "value": "NE London + parts of Essex + Kent CAMHS — c. 80-mile spread"},
            {"label": "Net Zero milestone", "value": "Goodmayes site rationalisation reducing footprint; Sunflowers Court solar PV"},
            {"label": "YoY change", "value": "c. +5-7% (energy + anti-ligature retrofit + community estate uplift)"},
            {"label": "Peer benchmark", "value": "Above MH-trust median (very dispersed footprint + forensic estate + CAMHS volume)"}
        ],
        "notes": "NELFT's premises cost is shaped by an unusually dispersed footprint (north-east London plus parts of Essex and Kent for children's services) and an active site-rationalisation programme at Goodmayes — disposing legacy Victorian asylum buildings while consolidating modern provision around Sunflowers Court. Mascalls Park brings forensic-grade FM premium. The trust's CAMHS scale (one of the largest in England) means its community-clinic footprint is materially larger per head than peer MH trusts.",
        "sources": [
            "https://www.nelft.nhs.uk/about-us-publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.cqc.org.uk/provider/RAT"
        ],
        "related": ["North East London NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Sandwell And West Birmingham Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Sandwell And West Birmingham Hospitals NHS Trust"}],
        "description": "Estate running costs across SWBH's transitional footprint — City Hospital (Dudley Road, Birmingham), Sandwell General (West Bromwich), Rowley Regis Hospital, plus the new Midland Metropolitan University Hospital (Smethwick) which opened October 2024 and absorbs City + Sandwell acute services. The MMUH PFI/charges sit in D4_11; Premises (other) carries the legacy estates plus transitional running cost.",
        "beneficiaries": "c. 530,000 patients across Sandwell + West Birmingham + parts of Dudley — A&E, maternity, planned acute services migrating to MMUH from October 2024.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£30.86M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "City + Sandwell + Rowley Regis + MMUH (opened Oct 2024) · transitional dual-running"},
            {"label": "Hard FM model", "value": "In-house Estates at legacy sites; PFI consortium (Hospital Company Sandwell) at MMUH"},
            {"label": "MMUH opening", "value": "Midland Metropolitan University Hospital opened Oct 2024 after Carillion-collapse delay (originally due 2018)"},
            {"label": "Carillion legacy", "value": "Original PFI builder Carillion collapsed 2018 — Balfour Beatty took over construction; novation shaped final delivery cost"},
            {"label": "Site disposal", "value": "City Hospital + parts of Sandwell General planned for disposal post-MMUH transfer (PFI charge for MMUH in D4_11)"},
            {"label": "Net Zero milestone", "value": "MMUH built to BREEAM Excellent; legacy estate decarbonisation deferred to disposal"},
            {"label": "YoY change", "value": "c. +8-10% (dual-running pre/post MMUH opening + transitional cost)"},
            {"label": "Peer benchmark", "value": "Elevated mid-acute peer (transition cost + dual-running)"}
        ],
        "notes": "SWBH's 2024-25 Premises (other) is uniquely shaped by the MMUH opening (October 2024) — for most of FY24-25 the trust was running both legacy City + Sandwell acute estates AND the new MMUH simultaneously, generating dual-running cost in this line. The MMUH PFI unitary charge belongs in D4_11. Carillion's 2018 collapse delayed MMUH delivery by 6+ years; Balfour Beatty completed the build under novation. Site disposal of City Hospital + parts of Sandwell will reduce future-year operating cost.",
        "sources": [
            "https://www.swbh.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.nao.org.uk/reports/the-collapse-of-carillion/"
        ],
        "related": ["Sandwell And West Birmingham Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Royal Wolverhampton NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Royal Wolverhampton NHS Trust"}],
        "description": "Estate running costs across RWT's three-site acute + community footprint — New Cross Hospital (Wolverhampton, the main acute campus including the Heart and Lung Centre and the Eye Infirmary Centre on-site), West Park Hospital (rehabilitation), Cannock Chase Hospital (run jointly with Mid Cheshire post-2014), plus a network of community premises. RWT is also one of the larger NHS-run primary-care providers (vertical integration).",
        "beneficiaries": "c. 470,000 Wolverhampton + south Staffordshire population — A&E + maternity + tertiary cardiology at New Cross, planned care at Cannock, rehab at West Park, plus c. 30 GP-surgery vertically-integrated sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£30.28M"},
            {"label": "Share of trust total opex", "value": "c. 4.5%"},
            {"label": "Estate scale", "value": "3 hospital sites + ~30 GP sites + community estate · vertically integrated primary care"},
            {"label": "Hard FM model", "value": "In-house Estates + outsourced soft-FM"},
            {"label": "Vertical integration", "value": "RWT operates ~30 GP surgeries — primary-care premises run through this trust line, atypical for acute trusts"},
            {"label": "Cannock Chase", "value": "Operated jointly with Mid Cheshire from 2014 — planned-care DGH, cost-share arrangement"},
            {"label": "Heart and Lung Centre", "value": "Tertiary cardiology on-site at New Cross — high-resilience utility demand"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat decarbonisation at New Cross; LED rolling"},
            {"label": "YoY change", "value": "c. +5-6% (energy + GP-network premises uplift)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median because of GP-network footprint included"}
        ],
        "notes": "RWT is unusual among acute trusts in directly operating c. 30 vertically-integrated GP surgeries — those primary-care premises run through Premises (other), which inflates the line vs comparator acute trusts that don't host primary care. The Cannock Chase shared-operation arrangement with Mid Cheshire (since 2014) means cost-share complications. The Heart and Lung Centre adds tertiary-grade utility resilience demand at New Cross. PSDS-funded heat works in train.",
        "sources": [
            "https://www.royalwolverhampton.nhs.uk/about-us/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["The Royal Wolverhampton NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "Estate running costs across UHD's two-hospital footprint — The Royal Bournemouth Hospital and Poole Hospital — plus Christchurch Hospital (rehab + outpatients). UHD was formed October 2020 by the merger of Royal Bournemouth & Christchurch Hospitals FT with Poole Hospital FT, and is mid-reconfiguration ('UHD Reconfiguration Programme') with major capital schemes deferred under NHP Reset.",
        "beneficiaries": "c. 750,000 Dorset population — A&E split between Bournemouth and Poole pending reconfiguration, maternity, paediatrics, planned care.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£29.94M"},
            {"label": "Share of trust total opex", "value": "c. 4.5%"},
            {"label": "Estate scale", "value": "3 hospital sites (Bournemouth + Poole + Christchurch) · ~150,000 m² clinical"},
            {"label": "Hard FM model", "value": "In-house Estates + outsourced soft-FM"},
            {"label": "Merger date", "value": "RBCH + Poole Hospital merged 1 October 2020 — ongoing FM contract harmonisation"},
            {"label": "NHP scheme status", "value": "UHD reconfiguration (Bournemouth emergency centre + BEACH building) was in NHP — Reset Jan 2025 deferred construction milestones"},
            {"label": "Reconfiguration model", "value": "Bournemouth = emergency hub; Poole = planned care + maternity; Christchurch satellite = rehab/outpatient/day-surgery"},
            {"label": "Net Zero milestone", "value": "Solar PV at Bournemouth + Poole; LED rolling"},
            {"label": "YoY change", "value": "c. +6-8% (NHP-deferred backlog + dual-running pre-reconfiguration + energy)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median (3-site dispersion + reconfiguration limbo)"}
        ],
        "notes": "UHD's premises spend is driven by the post-merger reconfiguration limbo — having planned to specialise sites (Bournemouth emergency, Poole planned), the NHP Reset (Jan 2025) deferred the BEACH building and Bournemouth emergency-centre construction, extending dual-running cost across both A&Es. The 2020 merger left two sets of FM contracts which are still being progressively harmonised. Christchurch Hospital adds a satellite estate originally configured for community + day surgery.",
        "sources": [
            "https://www.uhd.nhs.uk/about-us/publications-and-reports",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Premises & Infrastructure"]
    },
}
