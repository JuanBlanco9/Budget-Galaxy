# -*- coding: utf-8 -*-
# D4_07 Premises (other) — chunk 06 (20 NHS trusts)
# Hand-curated trust-specific enrichment entries.

NEW = {
    "Premises (other) — Surrey And Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Surrey And Sussex Healthcare NHS Trust"}],
        "description": "Premises running costs at SASH — East Surrey Hospital (Redhill, the trust's principal acute site, ~700 beds) plus Crawley Hospital, Caterham Dene Hospital and Earlswood community estate. East Surrey is a 1980s-vintage build with significant subsequent additions (cancer unit, ED expansion); the Crawley urgent treatment centre operates within an older shared estate.",
        "beneficiaries": "535,000+ patients across east Surrey, north-west Sussex and south Croydon — major emergency and maternity at East Surrey, urgent treatment + planned care at Crawley, rehabilitation at Caterham Dene.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.89M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute (East Surrey ~700 beds) + Crawley + Caterham Dene + Earlswood"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "East Surrey age", "value": "1980s build with phased additions · ED expanded 2017 · cancer unit 2014"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + heat-pump feasibility at East Surrey"},
            {"label": "YoY change", "value": "c. +5-7% (RM6011 energy reset + hard-FM inflation)"},
            {"label": "Peer benchmark", "value": "Mid-range vs south-east acute peers per m²"}
        ],
        "notes": "SASH's premises spend reflects a single-acute-led estate with no PFI burden, meaning utilities, hard FM and soft FM all flow through this line rather than being absorbed into a unitary charge. East Surrey's 1980s fabric carries a steady backlog-maintenance overhead, with periodic capital injections for ED and cancer additions. The 2024-25 uplift is dominated by RM6011 energy reset pricing and 5-7% construction inflation feeding into hard-FM contracts.",
        "sources": [
            {"publisher": "Surrey and Sussex Healthcare NHS Trust", "title": "Annual report and accounts publications", "url": "https://www.surreyandsussex.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Surrey And Sussex Healthcare NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Portsmouth Hospitals University NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Portsmouth Hospitals University NHS Trust"}],
        "description": "Premises running costs at PHU — Queen Alexandra Hospital (Cosham, the trust's single principal acute site, opened 2009 under one of the largest NHS PFI deals) plus St Mary's Community Health Campus and Gosport War Memorial Hospital. The QA PFI envelope absorbs a substantial share of hard FM, soft FM and lifecycle into the D4_11 unitary charge, with Premises (other) covering non-PFI sites and PFI variations.",
        "beneficiaries": "675,000+ patients across south-east Hampshire — major emergency, regional cancer, vascular and cardiology services at Queen Alexandra; community and rehabilitation at St Mary's and Gosport.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.64M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "1 acute (Queen Alexandra ~1,200 beds) + St Mary's + Gosport"},
            {"label": "Hard FM model", "value": "QA under PFI envelope · St Mary's + Gosport in-house Estates"},
            {"label": "PFI footprint", "value": "Queen Alexandra PFI (Project Co — The Hospital Company) — unitary charge in D4_11"},
            {"label": "PFI expiry", "value": "2040 — handback distant"},
            {"label": "Coastal exposure", "value": "Cosham + Gosport coastal · saline-air premium on hard FM"},
            {"label": "Net Zero milestone", "value": "PFI-led BMS upgrades at QA · PSDS feasibility at St Mary's"},
            {"label": "YoY change", "value": "c. +5% (energy + PFI variations)"},
            {"label": "Peer benchmark", "value": "Below acute median per m² (PFI absorbs hard FM)"}
        ],
        "notes": "PHU's relatively contained Premises (other) line reflects how much of its operating estate cost is captured inside the Queen Alexandra PFI unitary charge (one of England's largest acute PFI envelopes). Real estate-management focus has been on St Mary's community campus and PFI variations as service patterns evolve. Gosport's coastal exposure and St Mary's older fabric drive the per-m² premium on the non-PFI portion.",
        "sources": [
            {"publisher": "Portsmouth Hospitals University NHS Trust", "title": "Annual reports and accounts", "url": "https://www.porthosp.nhs.uk/about-us/publications.htm"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"}
        ],
        "related": ["Portsmouth Hospitals University NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Greater Manchester Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Greater Manchester Mental Health NHS Foundation Trust"}],
        "description": "Mental-health and substance-misuse premises operating costs across GMMH's Greater Manchester estate — Edenfield Centre (Prestwich, medium-secure forensic), Wells Inpatient Centre, Park House (North Manchester General co-located), Laureate House (Wythenshawe), Meadowbrook (Salford Royal co-located), plus extensive community-clinic estate. Spend is shaped by the Edenfield aftermath, the closure plan for Park House, and major-site redevelopment.",
        "beneficiaries": "1.3M residents of Manchester, Salford, Trafford, Bolton and Wigan — adult acute MH, secure/forensic, CAMHS, substance misuse, plus national high-secure referrals.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.31M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "Edenfield + Park House + Laureate House + Meadowbrook + Wells + 60+ community sites"},
            {"label": "Hard FM model", "value": "Mixed in-house + shared-services on co-located acute sites"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · medium-secure forensic at Edenfield · CAMHS"},
            {"label": "Edenfield context", "value": "BBC Panorama Sep 2022 abuse exposé · ongoing investment in environment, ligature reduction, CCTV"},
            {"label": "Park House", "value": "North Manchester General co-located block · planned closure, replacement at NMGH redevelopment"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Edenfield · LED community rollout"},
            {"label": "YoY change", "value": "c. +6-8% (Edenfield environmental works + energy)"},
            {"label": "Peer benchmark", "value": "Above MH median per inpatient bed (forensic mix + Edenfield works)"}
        ],
        "notes": "GMMH's premises spend is structurally elevated by the post-Edenfield environmental and ligature-reduction programme following the September 2022 Panorama exposé, by the medium-secure forensic estate's resilience requirements, and by the long-running plan to replace Park House as part of the North Manchester redevelopment. Several CQC reports since 2022 have driven additional capital and operating spend on inpatient environments.",
        "sources": [
            {"publisher": "Greater Manchester Mental Health NHS FT", "title": "Annual reports and accounts", "url": "https://www.gmmh.nhs.uk/publications/"},
            {"publisher": "Care Quality Commission", "title": "Provider report — GMMH (RXV)", "url": "https://www.cqc.org.uk/provider/RXV"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Greater Manchester Mental Health NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Birmingham and Solihull Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Birmingham and Solihull Mental Health NHS Foundation Trust"}],
        "description": "Mental-health premises operating costs across BSMHFT's Birmingham + Solihull estate — Reaside Clinic (medium-secure forensic, Rubery), Ardenleigh (medium-secure women's + adolescent forensic, Erdington), Tamarind Centre (PICU/acute, Birmingham), Oleaster (acute, Edgbaston co-located with QEHB), Zinnia Centre + The Barberry (specialist), plus 100+ community sites.",
        "beneficiaries": "1.3M residents of Birmingham + Solihull — adult acute MH, medium-secure forensic, women's secure, CAMHS forensic, plus regional/national specialist referrals.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.28M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "Reaside + Ardenleigh + Tamarind + Oleaster + Barberry + Zinnia + 100+ community sites"},
            {"label": "Hard FM model", "value": "Mixed in-house + shared services on co-located UHB sites"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · medium-secure forensic · women's secure · ECT facilities"},
            {"label": "Forensic estate", "value": "Reaside + Ardenleigh secure perimeter, CCTV, gatehouse — premium hard-FM cost"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Reaside · LED community rollout"},
            {"label": "YoY change", "value": "c. +5-6% (energy + ligature reduction works)"},
            {"label": "Peer benchmark", "value": "Above MH median per inpatient bed (heavy secure mix)"}
        ],
        "notes": "BSMHFT's premises spend reflects an unusually high share of secure/forensic estate (Reaside + Ardenleigh) where perimeter security, CCTV and gatehouse running costs add a structural premium versus general MH peers. Co-location with UHB at Oleaster brings shared estate-services pricing. Ligature-reduction programmes following national CQC scrutiny continue to drive operating spend on inpatient environments.",
        "sources": [
            {"publisher": "Birmingham and Solihull Mental Health NHS FT", "title": "Annual reports and publications", "url": "https://www.bsmhft.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "Provider report — BSMHFT (RXT)", "url": "https://www.cqc.org.uk/provider/RXT"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Birmingham and Solihull Mental Health NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Warrington and Halton Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Warrington and Halton Teaching Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across WHH's two-site estate — Warrington Hospital (the principal acute, mix of Victorian-era + late-20th-century build) and Halton General Hospital (Runcorn, planned-care focus). Warrington Hospital is on the HSSIB RAAC list with confirmed mitigation works ongoing, and the trust is in the NHP cohort for a new acute build whose timing was deferred at the January 2025 Reset.",
        "beneficiaries": "330,000+ patients across Warrington and Halton — major emergency at Warrington, planned and elective surgery at Halton, plus community estate.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.26M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "2 acute hospitals (Warrington + Halton) + community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "RAAC status", "value": "Warrington Hospital on HSSIB Sep 2023 RAAC list · ongoing mitigation"},
            {"label": "NHP scheme status", "value": "New Warrington Hospital in NHP cohort · Reset Jan 2025 deferred timeline"},
            {"label": "Estate vintage", "value": "Warrington mixes Victorian + 1970s-90s blocks · Halton 1990s build"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + BMS works at Warrington"},
            {"label": "YoY change", "value": "c. +6-8% (RAAC mitigation + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (Warrington age + RAAC)"}
        ],
        "notes": "WHH is one of the trusts most-exposed to the NHP Reset because its principal acute is both RAAC-affected and was scheduled for full replacement. Reset deferral means continued RAAC props, monitoring and decant within Premises (other), plus extended life of estate scheduled for demolition. Halton's elective focus drives some specialist FM (clean-utility ventilation) cost.",
        "sources": [
            {"publisher": "Warrington and Halton Teaching Hospitals NHS FT", "title": "Annual reports and publications", "url": "https://www.whh.nhs.uk/about-us/publications"},
            {"publisher": "HSSIB", "title": "RAAC in the NHS — patient safety investigations", "url": "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/"},
            {"publisher": "GOV.UK / DHSC", "title": "New Hospital Programme update", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"}
        ],
        "related": ["Warrington and Halton Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Royal Cornwall Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal Cornwall Hospitals NHS Trust"}],
        "description": "Premises running costs across RCHT's geographically dispersed estate — Royal Cornwall Hospital (Treliske, Truro, the only major acute in the county), West Cornwall Hospital (Penzance) and St Michael's Hospital (Hayle). Cornwall's peninsula geography means RCHT is the sole acute provider for the county, with elevated rural and coastal-resilience costs.",
        "beneficiaries": "570,000+ residents of Cornwall and Isles of Scilly — major emergency, maternity, regional cancer and stroke services concentrated at Treliske; smaller acute and rehabilitation at Penzance and Hayle.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.17M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "1 main acute (Treliske) + 2 secondary acute hospitals · peninsula geography"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "RAAC status", "value": "RCHT on HSSIB list with confirmed RAAC mitigation works"},
            {"label": "Coastal premium", "value": "Penzance + Hayle coastal · saline-air corrosion drives MEP premium"},
            {"label": "NHP scheme status", "value": "Treliske women & children's redevelopment in capital pipeline"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump and solar feasibility at Treliske · LED rollout"},
            {"label": "YoY change", "value": "c. +6-7% (RAAC + coastal + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (RAAC + coastal + isolation)"}
        ],
        "notes": "RCHT's premises spend is structurally elevated by its monopoly acute role for a peninsula population — supply-chain isolation drives standby spares and resilience costs, coastal exposure at Penzance and Hayle adds 5-10% MEP premium, and confirmed RAAC at Treliske means continuous mitigation works. The trust has been a regular Salix / PSDS recipient for heat decarbonisation feasibility at Treliske.",
        "sources": [
            {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Publications and annual reports", "url": "https://www.royalcornwall.nhs.uk/about-us/publications/"},
            {"publisher": "HSSIB", "title": "RAAC in the NHS — patient safety investigations", "url": "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Royal Cornwall Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Gateshead Health NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Gateshead Health NHS Foundation Trust"}],
        "description": "Premises running costs across GHFT's compact estate — the Queen Elizabeth Hospital (Gateshead, the principal acute, opened 2005 under a major PFI redevelopment) plus Bensham Hospital (community + older-people's services), Blaydon Primary Care Centre and Dunston Hill Day Hospital. The QE PFI envelope absorbs much of the hard FM into the D4_11 unitary charge, with Premises (other) covering Bensham, satellite estate and PFI variations.",
        "beneficiaries": "200,000+ residents of Gateshead — major emergency, maternity and cancer services at QE Gateshead; community and rehabilitation at Bensham and satellite sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.16M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "1 acute (QE Gateshead ~600 beds) + Bensham + 2 community sites"},
            {"label": "Hard FM model", "value": "QE under PFI envelope · Bensham + satellites in-house Estates"},
            {"label": "PFI footprint", "value": "Queen Elizabeth Gateshead PFI — unitary charge in D4_11"},
            {"label": "Bensham Hospital", "value": "Older-people's services site · Edwardian + later additions · backlog pressure"},
            {"label": "Net Zero milestone", "value": "PFI-led BMS upgrades at QE · PSDS feasibility at Bensham"},
            {"label": "YoY change", "value": "c. +5-7% (energy + Bensham backlog)"},
            {"label": "Peer benchmark", "value": "High % of opex due to small trust scale (PFI absorbs large share but trust is small)"}
        ],
        "notes": "GHFT's Premises (other) line is shaped by the dual structure — the QE Gateshead PFI absorbing core hard FM into D4_11, while Bensham's older fabric drives a disproportionate operating overhead at non-PFI sites. The trust is one of the smaller acute FTs in England, so this line represents a higher % of opex than at larger PFI-anchored trusts. CQC inspections have raised premises-environment concerns at Bensham historically.",
        "sources": [
            {"publisher": "Gateshead Health NHS Foundation Trust", "title": "Annual reports and publications", "url": "https://www.gatesheadhealth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Gateshead Health NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "London Ambulance Service NHS Trust"}],
        "description": "Estate operating costs for England's busiest ambulance service — 70+ ambulance stations across Greater London, two emergency operations centres (Waterloo + Bow), Make-Ready depots, fleet workshops, the HART (Hazardous Area Response Team) base, training facilities and Pocklington Place HQ. Premises (other) covers utilities, hard FM, soft FM, security, fuel-island maintenance and grounds across this dispersed estate.",
        "beneficiaries": "9.6M Londoners — 999 emergency response, 111 integrated urgent care, plus pan-London HART CBRN response, supporting NHS hospitals across the capital.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£17.16M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "70+ ambulance stations + 2 EOCs + HART base + workshops + HQ"},
            {"label": "Hard FM model", "value": "Mixed in-house Estates + station-level contracts · workshops in-house"},
            {"label": "Make-Ready model", "value": "Centralised vehicle prep depots driving estate consolidation"},
            {"label": "Fleet ops", "value": "Fuel islands, AdBlue, EV charging rollout · workshop COSHH controls"},
            {"label": "Net Zero milestone", "value": "EV ambulance pilot · charging infrastructure rollout · PSDS station retrofit"},
            {"label": "London premium", "value": "London property pricing + congestion-area logistics inflate site costs"},
            {"label": "YoY change", "value": "c. +6-8% (energy + EV-charging capex flow + London cost base)"},
            {"label": "Peer benchmark", "value": "Highest absolute among English ambulance trusts (London scale + density)"}
        ],
        "notes": "LAS's premises spend is structurally elevated by London property and logistics costs, by the dispersed station estate (70+ across 32 boroughs) and by the parallel running of an ageing station network alongside Make-Ready depot consolidation. EV-fleet rollout adds charging-infrastructure operating costs (grid upgrades, station works). The two EOCs (Waterloo + Bow) carry resilience-grade utilities and tier-3 IT premises requirements.",
        "sources": [
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual reports and accounts", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["London Ambulance Service NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Surrey and Borders Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Surrey and Borders Partnership NHS Foundation Trust"}],
        "description": "Mental-health, learning-disability and substance-misuse premises operating costs across SABP's Surrey + NE Hants estate — Farnham Road Hospital (Guildford), Abraham Cowley Unit (Chertsey, on St Peter's Hospital site), Ridgewood Centre (Frimley), Hellingly Centre satellite arrangements and 70+ community sites. Spend is shaped by the 2024-25 opening of the new Farnham Road inpatient block and continued investment in s.136 places of safety.",
        "beneficiaries": "1.3M residents of Surrey and NE Hampshire — adult acute MH, CAMHS, learning disability, perinatal and substance-misuse services across one of England's most-affluent ICS footprints.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£16.92M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "Farnham Road + Abraham Cowley + Ridgewood + 70+ community sites"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · LD inpatient · perinatal MBU pathway"},
            {"label": "Farnham Road", "value": "New inpatient block opened 2024 — improved environment, lower ligature risk"},
            {"label": "Abraham Cowley Unit", "value": "Co-located on Ashford & St Peter's site · shared estate-services"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility · LED community rollout"},
            {"label": "YoY change", "value": "c. +5-7% (new Farnham Road run-rate + energy)"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH-trust median per inpatient bed"}
        ],
        "notes": "SABP's premises spend in 2024-25 reflects the step-change from completion of the new Farnham Road inpatient block — higher operating run-rate on a modern facility, partially offset by phased decommissioning of older estate. Co-location with Ashford & St Peter's at the Abraham Cowley Unit brings shared estate-services pricing. The community-clinic estate (70+ sites across affluent commuter Surrey) drives a long tail of small-site overhead.",
        "sources": [
            {"publisher": "Surrey and Borders Partnership NHS FT", "title": "Annual reports and publications", "url": "https://www.sabp.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Care Quality Commission", "title": "Provider report — SABP (RXX)", "url": "https://www.cqc.org.uk/provider/RXX"}
        ],
        "related": ["Surrey and Borders Partnership NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Berkshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Berkshire Healthcare NHS Foundation Trust"}],
        "description": "Combined mental-health and community premises operating costs across BHFT's Berkshire-wide estate — Prospect Park Hospital (Reading, the principal MH inpatient site), Wokingham Hospital, West Berkshire Community Hospital (Thatcham), King Edward VII Hospital (Windsor), St Mark's Hospital (Maidenhead) plus 100+ community-clinic sites. BHFT is one of England's larger combined MH + community trusts.",
        "beneficiaries": "900,000+ residents across Berkshire — adult acute MH at Prospect Park, CAMHS, community physical health, district nursing, end-of-life care across the county.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£16.81M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "Prospect Park + 4 community hospitals + 100+ community sites"},
            {"label": "Hard FM model", "value": "Mixed in-house Estates + NHS Property Services occupancy at many community sites"},
            {"label": "MH-specific", "value": "s.136 suite + PICU at Prospect Park · CAMHS Willow House"},
            {"label": "NHS Property Services", "value": "Significant rental/service-charge exposure on PCT-era community sites"},
            {"label": "Combined model", "value": "Acute MH inpatients + community physical health share corporate estate"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump works at Prospect Park · LED community rollout"},
            {"label": "YoY change", "value": "c. +5-6% (NHSPS service-charge uplift + energy)"},
            {"label": "Peer benchmark", "value": "Above MH median per opex (community-hospital footprint adds estate)"}
        ],
        "notes": "BHFT's premises spend reflects the combined-trust model — MH inpatient operating costs at Prospect Park + community hospital running + a long tail of clinic-site occupancy where NHS Property Services service charges form a structural element. Service-charge inflation from NHSPS and 5-7% hard-FM construction inflation drive the 2024-25 uplift. Prospect Park has been the focus of repeated CQC environmental scrutiny.",
        "sources": [
            {"publisher": "Berkshire Healthcare NHS Foundation Trust", "title": "Annual reports and publications", "url": "https://www.berkshirehealthcare.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Property Services", "title": "Service charges and customer information", "url": "https://www.property.nhs.uk/customers/"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Berkshire Healthcare NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — George Eliot Hospital NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "George Eliot Hospital NHS Trust"}],
        "description": "Premises running costs at George Eliot Hospital (Nuneaton, north Warwickshire) — a small district general acute on a single site, including the Eliot Hospital Outpatient Centre, plus a small community footprint. GEH is one of the smaller acute trusts in England and is in the NHP cohort for a significant new-build / redevelopment whose timing was deferred at the January 2025 NHP Reset.",
        "beneficiaries": "300,000+ patients across north Warwickshire, south Leicestershire and east Birmingham — emergency, maternity, planned and elective care concentrated on one site.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£16.79M"},
            {"label": "Share of trust total opex", "value": "c. 8%"},
            {"label": "Estate scale", "value": "1 acute site (Nuneaton ~360 beds) + outpatient centre"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Estate vintage", "value": "1990s + 2000s phased build with older legacy blocks · backlog pressure"},
            {"label": "NHP scheme status", "value": "GEH redevelopment in NHP cohort · Reset Jan 2025 deferred timeline"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + BMS works"},
            {"label": "YoY change", "value": "c. +6-7% (energy + extended-life maintenance)"},
            {"label": "Peer benchmark", "value": "Among highest % of opex for small acute (no PFI absorption)"}
        ],
        "notes": "GEH's Premises (other) line is a relatively high share of total opex by acute-trust standards — the trust is small, has no PFI envelope to absorb hard FM, and runs an ageing single-site estate. NHP Reset deferral means continued operating spend on fabric scheduled for replacement, with capital-recovery pressure flowing into hard FM and backlog-maintenance items. Construction inflation 5-7% feeds directly into FM contract pricing.",
        "sources": [
            {"publisher": "George Eliot Hospital NHS Trust", "title": "Annual reports and publications", "url": "https://www.geh.nhs.uk/about-us/publications/"},
            {"publisher": "GOV.UK / DHSC", "title": "New Hospital Programme update", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["George Eliot Hospital NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Homerton Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Homerton Healthcare NHS Foundation Trust"}],
        "description": "Premises running costs at Homerton — Homerton University Hospital (Hackney, the principal acute on a 1980s-90s build) plus an extensive community-services footprint serving City & Hackney (since the 2014 community-services merger). Homerton is unusual as an acute trust running a substantial community estate, including Mary Seacole Nursing Home, John Howard Centre (forensic MH on shared site) and over 60 community sites.",
        "beneficiaries": "300,000+ patients across Hackney, the City of London and surrounding areas — major emergency, neonatal intensive care, maternity, plus an integrated community-services portfolio for City & Hackney.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£16.30M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute (Homerton) + 60+ community sites + Mary Seacole Nursing Home"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Acute estate", "value": "1986 main build + Maternity wing + Birth Centre additions"},
            {"label": "Community integration", "value": "City & Hackney community services since 2014 — large clinic estate"},
            {"label": "London premium", "value": "Inner-London property + service-charge pricing inflate site costs"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + heat-pump feasibility at Homerton"},
            {"label": "YoY change", "value": "c. +5-7% (London cost base + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (London + community-estate footprint)"}
        ],
        "notes": "Homerton's premises spend reflects the combined acute + community model uncommon among English FTs, with a long tail of City & Hackney community-clinic sites adding small-site overhead alongside the main hospital. Inner-London property pricing inflates the cost base. NHS Property Services service charges form a meaningful share of the community-site running cost.",
        "sources": [
            {"publisher": "Homerton Healthcare NHS Foundation Trust", "title": "Annual reports and publications", "url": "https://www.homerton.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Property Services", "title": "Service charges and customer information", "url": "https://www.property.nhs.uk/customers/"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Homerton Healthcare NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Northampton General Hospital NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Northampton General Hospital NHS Trust"}],
        "description": "Premises running costs at Northampton General — a single-site district general acute (Cliftonville, Northampton) with a Victorian-Edwardian core and substantial 20th-21st century additions (Heart Centre, Maternity, ED). NGH operates as a group with Kettering General under the 'University Hospitals of Northamptonshire' arrangement, with shared corporate functions emerging in estates.",
        "beneficiaries": "380,000+ residents of Northampton and south Northamptonshire — major emergency, regional cancer (Northamptonshire Centre for Oncology), heart centre, and maternity services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£16.23M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute site (Cliftonville ~750 beds) + outreach clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Estate vintage", "value": "Victorian core + 1960s, 1990s and 2010s additions · backlog pressure on legacy fabric"},
            {"label": "UHN group", "value": "Group working with Kettering General — shared estate strategy emerging"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat decarbonisation + LED rollout"},
            {"label": "YoY change", "value": "c. +5-6% (energy reset + Victorian-fabric backlog)"},
            {"label": "Peer benchmark", "value": "Mid-range vs east-midlands acute peers per m²"}
        ],
        "notes": "NGH's premises spend reflects an estate of multiple vintages, with Victorian-Edwardian listed-status fabric driving disproportionate maintenance overhead alongside more efficient 21st-century blocks. The University Hospitals of Northamptonshire group with Kettering has begun yielding shared estate-services thinking, though cost effects materialise slowly. Without an NHP slot, capital recovery rests on operating-line spend.",
        "sources": [
            {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual reports and publications", "url": "https://www.northamptongeneral.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Northampton General Hospital NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — South West London and St George's Mental Health NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "South West London and St George's Mental Health NHS Trust"}],
        "description": "Mental-health premises operating costs at SWLSTG — Springfield University Hospital (Tooting, the principal site, undergoing one of England's largest MH estate redevelopments with new acute and forensic blocks) plus Tolworth Hospital, Queen Mary's Hospital Roehampton MH unit and 50+ community sites. The Springfield redevelopment (Trinity Hospital + Shaftesbury Hospital) has materially reshaped operating run-rate.",
        "beneficiaries": "1.1M residents of Wandsworth, Merton, Sutton, Kingston, Richmond — adult acute MH, forensic, eating disorders, perinatal MBU and CAMHS.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.93M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "Springfield + Tolworth + Queen Mary's MH + 50+ community sites"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · medium-secure forensic · MBU · eating-disorder unit"},
            {"label": "Springfield redevelopment", "value": "Trinity (acute) + Shaftesbury (forensic) blocks delivered · land-sale part-funded"},
            {"label": "Old estate decant", "value": "Phased demolition of legacy Victorian Springfield blocks ongoing"},
            {"label": "Net Zero milestone", "value": "New blocks BREEAM-rated · PSDS feasibility for residual estate"},
            {"label": "YoY change", "value": "c. +6-8% (run-rate of new blocks + decant + energy)"},
            {"label": "Peer benchmark", "value": "Above MH median per inpatient bed (London + Springfield mid-transition)"}
        ],
        "notes": "SWLSTG's Premises (other) line is materially shaped by the Springfield redevelopment — England's largest MH estate transformation, part-funded by enabling-development land sales. The trust is mid-transition: paying to run new high-spec blocks (higher utilities and BMS) while continuing to mothball/decant Victorian legacy fabric. London property pricing inflates the cost base across the community estate.",
        "sources": [
            {"publisher": "South West London and St George's Mental Health NHS Trust", "title": "Annual reports and publications", "url": "https://www.swlstg.nhs.uk/publications"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Care Quality Commission", "title": "Provider report — SWLSTG (RQY)", "url": "https://www.cqc.org.uk/provider/RQY"}
        ],
        "related": ["South West London and St George's Mental Health NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Oxford Health NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Oxford Health NHS Foundation Trust"}],
        "description": "Combined mental-health and community premises operating costs across OHFT's Oxon, Bucks, Wilts and BSW estate — Warneford Hospital (Oxford, the principal MH inpatient site, listed-status Victorian build), Littlemore Mental Health Centre, Whiteleaf Centre (Aylesbury), Highfield Adolescent Unit, plus community hospitals (Witney, Wallingford, Bicester) and 100+ clinic sites. Highly unusual estate spread for a combined MH/community trust.",
        "beneficiaries": "2.5M residents across Oxfordshire, Buckinghamshire and parts of Wiltshire/BSW — adult acute MH, forensic, CAMHS at Highfield, plus community physical health and a national specialist forensic CAMHS service.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.76M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "Warneford + Littlemore + Whiteleaf + 6+ community hospitals + 100+ sites"},
            {"label": "Hard FM model", "value": "Mixed in-house Estates + NHSPS service charges on PCT-era community sites"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · CAMHS Highfield · adult eating disorders · forensic"},
            {"label": "Warneford listed status", "value": "Grade II listed Victorian buildings — premium maintenance overhead"},
            {"label": "Oxford academic partnership", "value": "Co-located University of Oxford psychiatry research (Department of Psychiatry)"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + heat-pump feasibility · Warneford listed-fabric constraints"},
            {"label": "YoY change", "value": "c. +5-6% (NHSPS service charges + energy + listed-fabric maintenance)"},
            {"label": "Peer benchmark", "value": "Above MH median per inpatient bed (listed-fabric + community footprint)"}
        ],
        "notes": "OHFT's premises spend reflects an exceptionally diverse estate — listed-status Victorian fabric at Warneford (where decarbonisation options are constrained by heritage), a substantial community-hospital network across three counties, and one of the highest community-clinic site counts in NHS England. NHSPS service charges form a structural element of the cost base on legacy PCT properties.",
        "sources": [
            {"publisher": "Oxford Health NHS Foundation Trust", "title": "Annual reports and publications", "url": "https://www.oxfordhealth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Property Services", "title": "Service charges and customer information", "url": "https://www.property.nhs.uk/customers/"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Oxford Health NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — The Mid Yorkshire Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "The Mid Yorkshire Hospitals NHS Trust"}],
        "description": "Premises running costs across Mid Yorks — Pinderfields Hospital (Wakefield, the principal acute, opened 2011 under a major PFI redevelopment), Dewsbury and District Hospital (post-2017 service reconfiguration to planned care + maternity-light) and Pontefract Hospital. The Pinderfields/Pontefract PFI envelope absorbs a large share of hard FM into D4_11; Dewsbury is in-house.",
        "beneficiaries": "550,000+ residents across Wakefield, Kirklees and parts of north Yorkshire — major emergency at Pinderfields, planned and step-down care at Dewsbury and Pontefract.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.76M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "1 acute (Pinderfields ~700 beds) + Dewsbury + Pontefract"},
            {"label": "Hard FM model", "value": "Pinderfields + Pontefract under PFI envelope · Dewsbury in-house Estates"},
            {"label": "PFI footprint", "value": "Mid Yorkshire PFI (Project Co — Consort Healthcare) — unitary charge in D4_11"},
            {"label": "Reconfiguration", "value": "Dewsbury A&E to urgent treatment 2017 · maternity reorganisation"},
            {"label": "Net Zero milestone", "value": "PFI-led BMS at Pinderfields · PSDS feasibility at Dewsbury"},
            {"label": "YoY change", "value": "c. +5% (energy + PFI variations)"},
            {"label": "Peer benchmark", "value": "Below acute median per m² (PFI absorbs hard FM)"}
        ],
        "notes": "Mid Yorks' relatively contained Premises (other) line reflects how much of its operating estate cost is captured inside the Pinderfields/Pontefract PFI unitary charge. Dewsbury's older fabric carries the bulk of the in-house operating spend, plus the lingering reconfiguration costs (decant, signage, IT cabling) from the 2017 service moves. PFI variations remain a routine cost driver as service patterns shift.",
        "sources": [
            {"publisher": "The Mid Yorkshire Hospitals NHS Trust", "title": "Publications and annual reports", "url": "https://www.midyorks.nhs.uk/publication-scheme"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"}
        ],
        "related": ["The Mid Yorkshire Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Avon and Wiltshire Mental Health Partnership NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Avon and Wiltshire Mental Health Partnership NHS Trust"}],
        "description": "Mental-health and learning-disability premises operating costs across AWP's Avon + Wiltshire estate — Callington Road Hospital (Bristol), Southmead Hospital MH unit, Fountain Way (Salisbury), Sandalwood Court (Swindon), Hillview Lodge (Bath, Royal United Hospital site) plus 80+ community sites. AWP covers one of the largest geographic MH footprints in England, spanning two ICS areas (BNSSG + BSW).",
        "beneficiaries": "1.8M residents of Bristol, Bath & North East Somerset, North Somerset, South Gloucestershire, Wiltshire and Swindon — adult acute MH, forensic, CAMHS, learning disability, perinatal services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.35M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "5 main MH inpatient sites + 80+ community sites · two ICS footprint"},
            {"label": "Hard FM model", "value": "Mixed in-house + shared services on co-located acute sites"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · medium-secure forensic · LD inpatient"},
            {"label": "Co-location", "value": "Hillview Lodge on RUH Bath · Southmead MH on NBT · shared estate-services"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Callington Road · LED community rollout"},
            {"label": "YoY change", "value": "c. +5-6% (energy + ligature reduction works)"},
            {"label": "Peer benchmark", "value": "Mid-range vs MH-trust median per inpatient bed"}
        ],
        "notes": "AWP's premises spend reflects one of the most-stretched MH-trust geographies in England, spanning two ICS areas and requiring inpatient sites in both Bristol and Wiltshire to limit travel for service users. Co-location with North Bristol Trust (Southmead) and Royal United Hospitals Bath (Hillview Lodge) brings shared estate-services pricing on those sites. CQC environmental scrutiny of Callington Road has driven recent capital and operating spend.",
        "sources": [
            {"publisher": "Avon and Wiltshire Mental Health Partnership NHS Trust", "title": "Annual reports and publications", "url": "https://www.awp.nhs.uk/about-us/publications"},
            {"publisher": "Care Quality Commission", "title": "Provider report — AWP (RVN)", "url": "https://www.cqc.org.uk/provider/RVN"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Avon and Wiltshire Mental Health Partnership NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Tameside and Glossop Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Tameside and Glossop Integrated Care NHS Foundation Trust"}],
        "description": "Premises running costs at Tameside and Glossop — Tameside General Hospital (Ashton-under-Lyne, the principal acute on a 1960s tower-block estate with later additions) plus integrated community-services estate (the trust merged community services in 2017). T&G is a small acute trust with one of the highest opex-shares for premises among English peers and a recognised backlog-maintenance challenge.",
        "beneficiaries": "260,000+ residents of Tameside and Glossop — emergency, maternity and integrated acute + community care concentrated on the Ashton site, plus a community footprint.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.29M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "1 acute (Tameside General) + integrated community-services estate"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Estate vintage", "value": "1960s tower + 2012 New Hartshead block · ageing legacy alongside modern wing"},
            {"label": "Backlog maintenance", "value": "Reported high-significance backlog in NHS ERIC returns"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump + LED works"},
            {"label": "YoY change", "value": "c. +6-7% (legacy-tower MEP + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median % of opex (small trust + ageing tower + no PFI)"}
        ],
        "notes": "T&G's Premises (other) line is a relatively high share of total opex for an acute trust — driven by the 1960s tower-block at the core of the Ashton site, persistent high-significance backlog reported in NHS ERIC, and the absence of any PFI envelope to absorb hard FM. The 2012 New Hartshead block coexists with much older fabric, requiring continuous backlog intervention. Integrated community services add a long tail of small-site overhead.",
        "sources": [
            {"publisher": "Tameside and Glossop Integrated Care NHS FT", "title": "Annual reports and publications", "url": "https://www.tamesidehospital.nhs.uk/about-us/publications.htm"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC)", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Tameside and Glossop Integrated Care NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Gloucestershire Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Gloucestershire Health and Care NHS Foundation Trust"}],
        "description": "Combined mental-health and community-services premises operating costs across GHC's Gloucestershire-wide estate — Wotton Lawn Hospital (Gloucester, the principal MH inpatient site), Charlton Lane Centre (Cheltenham), Laurel House (Stroud) plus seven community hospitals (Cirencester, Stroud, North Cotswolds, Tewkesbury, Vale of Berkeley, Dilke Memorial, Lydney) and 80+ clinic sites. GHC was formed in 2019 by merging Glos MH with community services.",
        "beneficiaries": "650,000+ residents of Gloucestershire — adult acute MH at Wotton Lawn, older-people's MH at Charlton Lane, plus community-hospital inpatient beds, district nursing, end-of-life and integrated community physical health.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.25M"},
            {"label": "Share of trust total opex", "value": "c. 7%"},
            {"label": "Estate scale", "value": "Wotton Lawn + Charlton Lane + 7 community hospitals + 80+ sites"},
            {"label": "Hard FM model", "value": "Mixed in-house Estates + NHSPS service charges on PCT-era sites"},
            {"label": "MH-specific", "value": "s.136 suite + PICU at Wotton Lawn · older-people's MH at Charlton Lane"},
            {"label": "Community hospitals", "value": "7 inpatient community hospitals — substantial estate burden for a Combined trust"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility · LED community rollout"},
            {"label": "YoY change", "value": "c. +5-6% (NHSPS service-charge uplift + energy)"},
            {"label": "Peer benchmark", "value": "Above MH median per opex (extensive community-hospital estate)"}
        ],
        "notes": "GHC's premises spend is structurally elevated by an unusually large community-hospital footprint for a combined MH/community trust — seven inpatient sites carrying full hard-FM, soft-FM and resilience overhead. The 2019 merger continues to drive estate-rationalisation and shared-services work captured in operating spend. NHSPS service-charge inflation is a meaningful component on legacy PCT properties.",
        "sources": [
            {"publisher": "Gloucestershire Health and Care NHS FT", "title": "Annual reports and publications", "url": "https://www.ghc.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Property Services", "title": "Service charges and customer information", "url": "https://www.property.nhs.uk/customers/"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Gloucestershire Health and Care NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Premises running costs at Stockport — Stepping Hill Hospital (the principal acute on a multi-decade Stockport site, with 1970s tower and subsequent additions including 2014 Acute Block) plus integrated community services (community hospitals + clinics) since the 2011 community-services transfer. Stepping Hill is on the HSSIB RAAC list with confirmed mitigation works.",
        "beneficiaries": "350,000+ residents of Stockport, High Peak and parts of east Cheshire — major emergency, maternity, planned care at Stepping Hill plus integrated community services across Stockport.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£15.15M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "1 acute (Stepping Hill ~750 beds) + integrated community estate"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "RAAC status", "value": "Stepping Hill on HSSIB Sep 2023 RAAC list · ongoing mitigation"},
            {"label": "Estate vintage", "value": "1970s tower + 2014 Acute Block + Edwardian heritage outbuildings"},
            {"label": "NHP scheme status", "value": "Stepping Hill not in original NHP cohort; recent post-Reset bidding for capital"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump + LED works"},
            {"label": "YoY change", "value": "c. +6-8% (RAAC mitigation + energy + ageing-tower MEP)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (RAAC + ageing tower)"}
        ],
        "notes": "Stockport's premises cost is shaped by confirmed RAAC at Stepping Hill (continuous structural monitoring, props and decant), the 1970s tower-block fabric requiring ongoing MEP refresh, and integrated community services adding a long tail of small-site overhead. Without an NHP slot in the original 40-hospital cohort, capital recovery falls disproportionately on the operating line, with construction inflation 5-7% and energy reset compounding the YoY pressure.",
        "sources": [
            {"publisher": "Stockport NHS Foundation Trust", "title": "Annual reports and publications", "url": "https://www.stockport.nhs.uk/about-us/publications/"},
            {"publisher": "HSSIB", "title": "RAAC in the NHS — patient safety investigations", "url": "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/"},
            {"publisher": "NHS England", "title": "NHS provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Premises & Infrastructure"]
    },
}
