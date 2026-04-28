# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 41 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {}

NEW["Inventories written down — University Hospitals Plymouth NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "University Hospitals Plymouth NHS Trust"}],
    "description": "University Hospitals Plymouth NHS Trust's £0.49M inventories-written-down line covers IAS 2 net-realisable-value adjustments and provisions for obsolete, expired and damaged stock — clinical consumables, pharmacy lines, prosthetics, theatre instruments and stores items — across Derriford Hospital (the trust's principal site, the South West peninsula's only Major Trauma Centre) plus the Royal Eye Infirmary and community satellite locations. Write-downs follow DHSC GAM ch.5 stocktaking and obsolescence guidance and feed quarterly into the operating cost statement.",
    "beneficiaries": "c. 9,500 WTE staff serving a c. 450,000 trust catchment plus c. 2 million-population South West peninsula referral footprint (Devon + Cornwall + Isles of Scilly) for Major Trauma, neurosurgery, cardiothoracic and tertiary services; c. 165,000 ED attendances/yr at Derriford; c. 110,000 admissions/yr; c. 600,000 outpatient attendances/yr.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Human Medicines Regulations 2012 (pharmacy stock destruction)",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.49M"},
        {"label": "Trust scale", "value": "Derriford + Royal Eye Infirmary + community sites; c. 9,500 WTE; South West peninsula Major Trauma Centre"},
        {"label": "Composition", "value": "Pharmacy expiry + theatre prosthetics obsolescence + clinical consumables damage + COVID PPE legacy tail + recall returns"},
        {"label": "NHS Supply Chain", "value": "c. 80% of clinical consumables routed via NHS Supply Chain Coordination Limited (SCCL); residual local procurement"},
        {"label": "Stocktake cadence", "value": "Year-end full count + quarterly cycle counts per DHSC GAM ch.5; theatre prosthetics tracked via track-and-trace"},
        {"label": "Devon ICS", "value": "Member of Devon ICB; tertiary referral hub for Royal Cornwall Hospitals + Torbay and South Devon"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.65M (COVID PPE peak) → 2023-24 c. £0.52M → 2024-25 £0.49M — PPE legacy tail diminishing"},
        {"label": "Major Trauma Centre", "value": "Sole MTC for South West peninsula; c. 1,800 major trauma activations/yr — drives high-cost prosthetic + theatre stock"},
        {"label": "Industrial action", "value": "44 days junior-doctor + 10 days consultant strikes 2023-24 disrupted theatre throughput, raising prosthesis obsolescence risk"},
        {"label": "Delivery body + policy owner", "value": "Trust Procurement + Pharmacy + Materials Management + NHS Supply Chain (SCCL); NHSE Provider Finance + DHSC GAM team"},
        {"label": "Evaluation evidence", "value": "NHSE Model Hospital benchmarking; DHSC SCCL annual report; Trust ARA 2023-24; NAO NHS supply-chain reports"},
        {"label": "Predecessor / successor", "value": "Predecessor: COVID PPE legacy stock provisions · Successor: Scan4Safety + EPIC EPR-driven inventory rationalisation"}
    ],
    "notes": "Plymouth's write-down line is shaped by its role as the South West peninsula's sole Major Trauma Centre and tertiary referral hub — high-cost orthopaedic and cardiothoracic prosthetics carry obsolescence risk as device generations turn over. Derriford's geographic isolation (closest peer MTC is Bristol, 120+ miles) requires deeper safety-stock buffers, raising provision rates vs urban peers. The trust is rolling out the Epic-based Frontline Digitisation EPR (go-live phased through 2024-26), with Scan4Safety integration expected to reduce future write-downs once inventory tracking matures. Industrial action in 2023-24 disrupted elective theatre throughput, raising prosthesis obsolescence exposure. April 2025 NIC step-up affects pharmacy and stores staffing rather than inventory directly.",
    "sources": [
        {"publisher": "University Hospitals Plymouth NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.plymouthhospitals.nhs.uk/our-publications"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain (SCCL)", "title": "Annual Report and Accounts", "url": "https://www.supplychain.nhs.uk/about-us/"},
        {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
        {"publisher": "Care Quality Commission", "title": "University Hospitals Plymouth NHS Trust provider profile (RK9)", "url": "https://www.cqc.org.uk/provider/RK9"}
    ],
    "related": ["University Hospitals Plymouth NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — Royal Cornwall Hospitals NHS Trust", "NHS Supply Chain Coordination Limited", "Department of Health and Social Care"]
}

NEW["Lease expenditure — Maidstone And Tunbridge Wells NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Maidstone And Tunbridge Wells NHS Trust"}],
    "description": "Maidstone and Tunbridge Wells NHS Trust's £0.49M lease expenditure line covers IFRS 16 short-term and low-value lease charges (those falling outside on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across the trust's two principal sites — Maidstone Hospital (Hermitage Lane) and Tunbridge Wells Hospital at Pembury (a 2011 PFI-built Acute Assessment + maternity hospital) — and community/satellite locations. Lease expenditure sits alongside the trust's substantial PFI unitary-charge stream for the Pembury build.",
    "beneficiaries": "c. 6,500 WTE staff serving a c. 580,000 catchment across west Kent and parts of east Sussex; c. 165,000 ED attendances/yr split across Maidstone + Tunbridge Wells EDs; c. 100,000 admissions/yr; c. 510,000 outpatient attendances/yr; the Kent Oncology Centre at Maidstone serves a wider regional catchment for radiotherapy and chemotherapy.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.49M"},
        {"label": "Trust scale", "value": "Maidstone Hospital + Tunbridge Wells Hospital at Pembury (PFI 2011) + community sites; c. 6,500 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical-equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5; longer-term ROU assets sit elsewhere"},
        {"label": "PFI context", "value": "Tunbridge Wells Hospital at Pembury is a 2011 PFI-built facility (Hochtief PFI Solutions / Equans); separate PFI/LIFT charges line"},
        {"label": "Kent Oncology Centre", "value": "Regional radiotherapy + chemotherapy hub at Maidstone — drives leased-equipment refresh cycles (linacs, bunkers)"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.36M → 2023-24 c. £0.46M → 2024-25 £0.49M — IFRS 16 transition steady-state + community-clinic expansion"},
        {"label": "Kent and Medway ICS", "value": "Member of Kent and Medway ICB; collaboration with Dartford and Gravesham + Medway + East Kent on cancer + maternity pathways"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + NHSPS (community sites)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + Kent and Medway ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; CQC RWF inspections; NAO Acute reports; NHSE Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: ICS-wide estate rationalisation + further community-clinic consolidation"}
    ],
    "notes": "Maidstone and Tunbridge Wells's lease line is structurally shaped by the trust's split-site model, with the modern PFI-built Pembury facility taking emergency, maternity and most acute medicine while Maidstone retains the regional cancer centre and elective work. Short-term and low-value leases capture community-clinic premises, IT and medical-equipment leases that fall below IFRS 16 ROU thresholds. The Kent Oncology Centre's linac and imaging refresh cycles drive leased-equipment turnover. The trust avoided RAAC backlog exposure given Pembury's 2011 build and Maidstone's brick construction, but inherits an ageing Maidstone block estate. April 2025 NIC step-up affects E&F staffing rather than lease charges directly.",
    "sources": [
        {"publisher": "Maidstone and Tunbridge Wells NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mtw.nhs.uk/about-us/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "Current Private Finance Initiative (PFI) projects", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
        {"publisher": "Care Quality Commission", "title": "Maidstone and Tunbridge Wells NHS Trust provider profile (RWF)", "url": "https://www.cqc.org.uk/provider/RWF"},
        {"publisher": "NHS England", "title": "NHS Operational Plan 2024-25", "url": "https://www.england.nhs.uk/publication/nhs-operational-planning-and-contracting-guidance/"}
    ],
    "related": ["Maidstone And Tunbridge Wells NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Maidstone And Tunbridge Wells NHS Trust", "Lease expenditure — Dartford and Gravesham NHS Trust", "Department of Health and Social Care"]
}

NEW["PFI / LIFT charges — The Hillingdon Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "PFI / LIFT charges", "parent": "The Hillingdon Hospitals NHS Foundation Trust"}],
    "description": "The Hillingdon Hospitals NHS FT's £0.48M PFI / LIFT charges line covers residual unitary-charge components (interest, services and lifecycle elements per IFRIC 12 / DHSC GAM disaggregation) on legacy LIFT-funded community premises in the London Borough of Hillingdon, plus any remaining off-balance-sheet PFI tail. Hillingdon's main estate at Hillingdon Hospital (Pield Heath Road) is publicly funded and not under PFI — it is one of the original RAAC-plank sites in the New Hospital Programme rebuild cohort.",
    "beneficiaries": "c. 3,800 WTE staff serving a c. 320,000 Hillingdon catchment plus c. 76 million annual passengers at neighbouring Heathrow Airport (the trust services Heathrow as the local NHS provider, including infectious-disease screening); c. 105,000 ED attendances/yr at Hillingdon Hospital; c. 65,000 admissions/yr; c. 280,000 outpatient attendances/yr; Mount Vernon site delivers cancer + dermatology.",
    "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022) — DHSC Group Accounting Manual 2024-25 — DHSC PFI guidance — NHS LIFT Co arrangements — NHS Act 2006",
    "key_stats": [
        {"label": "PFI / LIFT charges 2024-25", "value": "£0.48M"},
        {"label": "Trust scale", "value": "Hillingdon Hospital (Pield Heath Rd) + Mount Vernon + community sites; c. 3,800 WTE; serves Heathrow + west London"},
        {"label": "Composition", "value": "Residual LIFT unitary-charge service + lifecycle elements on community-health hereditaments per IFRIC 12 disaggregation"},
        {"label": "LIFT scheme", "value": "Hillingdon + Ealing LIFT Co (HEHL) — built community-clinic estate under DH LIFT programme c. 2003-2010"},
        {"label": "Main site NOT PFI", "value": "Hillingdon Hospital main estate is publicly funded — 1960s build with extensive RAAC planks; in NHP rebuild cohort"},
        {"label": "RAAC + NHP", "value": "Hillingdon named in October 2023 RAAC seven announcement — funded for full rebuild by 2030 under New Hospital Programme"},
        {"label": "Heathrow context", "value": "Trust acts as local NHS provider for Heathrow Airport; high-cost infectious-disease + travel-medicine workload"},
        {"label": "Funding trajectory", "value": "Declining tail — peak unitary-charge years pre-2020; expected to fall further as LIFT contracts approach handback"},
        {"label": "NW London ICS", "value": "Member of NW London ICB with Imperial, Chelsea & Westminster, London North West UH, CNWL"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates & Finance + HEHL LIFT Co + DHSC LIFT/PFI team; NHSE Provider Finance + DHSC NHP"},
        {"label": "Evaluation evidence", "value": "HM Treasury PFI projects database; NAO PFI reports; NAO NHP report 2023; HSSIB RAAC reports; Trust ARA 2023-24"},
        {"label": "Predecessor / successor", "value": "Predecessor: 2003-2010 LIFT rollout · Successor: LIFT contract handbacks late 2020s + NHP rebuild post-2030"}
    ],
    "notes": "Hillingdon's PFI/LIFT line is small relative to the trust's overall premises spend because the principal acute estate is publicly funded — and is one of the original RAAC-plank failures (1960s build) named in the October 2023 New Hospital Programme RAAC seven for full rebuild by 2030. The £0.48M comprises residual LIFT-Co unitary-charge components on community-clinic hereditaments built under the Hillingdon + Ealing LIFT (HEHL) joint venture. The trust serves a unique Heathrow Airport-adjacent catchment with high travel-medicine workload. April 2025 NIC step-up affects FM contractor pass-through where bundled. Carillion 2018 collapse + Equans/Engie novations have limited effect given LIFT-Co structure.",
    "sources": [
        {"publisher": "The Hillingdon Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thh.nhs.uk/about/publications.php"},
        {"publisher": "HM Treasury", "title": "Current PFI projects 2018 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — RAAC announcement October 2023", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
        {"publisher": "Care Quality Commission", "title": "The Hillingdon Hospitals NHS Foundation Trust provider profile (RAS)", "url": "https://www.cqc.org.uk/provider/RAS"}
    ],
    "related": ["The Hillingdon Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "PFI / LIFT charges — London North West University Healthcare NHS Trust", "Department of Health and Social Care"]
}

NEW["Inventories written down — University Hospitals Coventry And Warwickshire NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
    "description": "University Hospitals Coventry and Warwickshire NHS Trust's £0.48M inventories-written-down line covers IAS 2 net-realisable-value adjustments and provisions for obsolete, expired and damaged stock — clinical consumables, pharmacy lines, prosthetics, theatre instruments and stores items — across University Hospital Coventry (Walsgrave) and the Hospital of St Cross at Rugby plus community satellites. Write-downs follow DHSC GAM ch.5 stocktaking and obsolescence guidance and feed quarterly into the operating cost statement.",
    "beneficiaries": "c. 9,800 WTE staff serving a c. 1 million Coventry and Warwickshire catchment plus tertiary referrals from across the West Midlands; c. 165,000 ED attendances/yr at UHCW; c. 110,000 admissions/yr; c. 720,000 outpatient attendances/yr; trust hosts the West Midlands Major Trauma Centre and a tertiary cardiac surgery + neurosciences hub.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Human Medicines Regulations 2012 (pharmacy stock destruction)",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.48M"},
        {"label": "Trust scale", "value": "UH Coventry (Walsgrave) + Hospital of St Cross Rugby + community sites; c. 9,800 WTE"},
        {"label": "Composition", "value": "Pharmacy expiry + theatre prosthetics obsolescence + clinical consumables damage + COVID PPE legacy tail + recall returns"},
        {"label": "NHS Supply Chain", "value": "c. 80% of clinical consumables routed via NHS Supply Chain Coordination Limited (SCCL); residual local procurement"},
        {"label": "Stocktake cadence", "value": "Year-end full count + quarterly cycle counts per DHSC GAM ch.5; theatre prosthetics tracked via track-and-trace"},
        {"label": "Coventry & Warwickshire ICS", "value": "Member of Coventry and Warwickshire ICB with George Eliot, South Warwickshire, Wye Valley pathways"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.62M (COVID PPE peak) → 2023-24 c. £0.51M → 2024-25 £0.48M — PPE legacy tail diminishing"},
        {"label": "Major Trauma Centre", "value": "West Midlands MTC — high-volume major trauma drives high-cost prosthetic + theatre stock"},
        {"label": "Industrial action", "value": "44 days junior-doctor + 10 days consultant strikes 2023-24 disrupted theatre throughput, raising prosthesis obsolescence risk"},
        {"label": "Delivery body + policy owner", "value": "Trust Procurement + Pharmacy + Materials Management + NHS Supply Chain (SCCL); NHSE Provider Finance + DHSC GAM team"},
        {"label": "Evaluation evidence", "value": "NHSE Model Hospital benchmarking; DHSC SCCL annual report; Trust ARA 2023-24; NAO NHS supply-chain reports"},
        {"label": "Predecessor / successor", "value": "Predecessor: COVID PPE legacy stock provisions · Successor: Scan4Safety + EPR-driven inventory rationalisation"}
    ],
    "notes": "UHCW's write-down line reflects the trust's complexity — a 2006 PFI-built principal hospital (Walsgrave) hosting the West Midlands Major Trauma Centre, tertiary cardiac and neurosciences services. High-cost interventional cardiology and orthopaedic prosthetic ranges drive obsolescence risk as device generations turn over and recall events occur. The trust is rolling out Frontline Digitisation (Oracle Health) across 2024-26 with Scan4Safety integration expected to reduce future write-downs once mature. Industrial action 2023-24 disrupted elective throughput, raising obsolescence exposure on consigned implants. April 2025 NIC step-up affects pharmacy and stores staffing rather than inventory directly. UHCW participates in the Trustmark group alongside Worcestershire and Wye Valley.",
    "sources": [
        {"publisher": "University Hospitals Coventry and Warwickshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhcw.nhs.uk/about-us/who-we-are/our-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain (SCCL)", "title": "Annual Report and Accounts", "url": "https://www.supplychain.nhs.uk/about-us/"},
        {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
        {"publisher": "Care Quality Commission", "title": "University Hospitals Coventry and Warwickshire NHS Trust provider profile (RKB)", "url": "https://www.cqc.org.uk/provider/RKB"}
    ],
    "related": ["University Hospitals Coventry And Warwickshire NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — South Warwickshire NHS Foundation Trust", "NHS Supply Chain Coordination Limited", "Department of Health and Social Care"]
}

NEW["Establishment costs — Southport And Ormskirk Hospital NHS Trust"] = {
    "aliases": [{"name": "Establishment costs", "parent": "Southport And Ormskirk Hospital NHS Trust"}],
    "description": "Southport and Ormskirk Hospital NHS Trust's £0.48M establishment costs line covers GAM operating expenses for printing, stationery, postage, telephony, courier, conference and training-room hire, advertising and recruitment-related materials across Southport and Formby DGH plus Ormskirk District General Hospital. The line absorbs back-office overhead supporting the trust's two-site model in the Cheshire and Merseyside ICS. The trust transitioned its services into Mersey and West Lancashire Teaching Hospitals during 2024-25 — this 2024-25 line captures the run-out establishment spend prior to merger consolidation.",
    "beneficiaries": "c. 3,400 WTE staff serving a c. 280,000 catchment in Southport, Formby and West Lancashire; c. 95,000 ED attendances/yr split across Southport and Ormskirk EDs; c. 60,000 admissions/yr; c. 320,000 outpatient attendances/yr. The trust's catchment includes high deprivation wards in Southport's coastal centre alongside the rural West Lancashire fringe.",
    "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Establishment costs 2024-25", "value": "£0.48M"},
        {"label": "Trust scale", "value": "Southport & Formby DGH + Ormskirk DGH + community sites; c. 3,400 WTE"},
        {"label": "Composition", "value": "Printing + stationery + postage + telephony + courier + conference/training-room hire + advertising + recruitment materials"},
        {"label": "Merger context", "value": "Acquired by Mersey and West Lancashire Teaching Hospitals NHS Trust on 1 July 2024 — final standalone year for some categories"},
        {"label": "Prior governance", "value": "Subject to multi-year CQC scrutiny and NHSE Recovery Support Programme oversight before merger"},
        {"label": "Cheshire & Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB; merger consolidates with Mersey and West Lancs Teaching"},
        {"label": "Funding trajectory", "value": "Declining trajectory pre-merger as transitional integration costs absorbed; post-merger consolidated under MWL"},
        {"label": "Industrial action", "value": "44 days junior-doctor + 10 days consultant strikes 2023-24 generated recruitment-advertising spike on agency backfill"},
        {"label": "Delivery body", "value": "Trust Corporate Services + Communications + HR + IT + Mersey and West Lancs (post-merger integration)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + NHSE Recovery Support Programme + Cheshire and Merseyside ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24; CQC RVY inspections; NHSE Recovery Support Programme reviews; merger transaction documents 2024"},
        {"label": "Predecessor / successor", "value": "Predecessor: Southport & Ormskirk legacy organisation · Successor: Mersey and West Lancashire Teaching Hospitals NHS Trust (1 July 2024)"}
    ],
    "notes": "Southport and Ormskirk's 2024-25 establishment line captures the trust's final operating period as a standalone organisation before its 1 July 2024 acquisition by Mersey and West Lancashire Teaching Hospitals NHS Trust — completing one of the most-watched NHS acquisitions of the post-CQC-Inadequate cohort and a flagship for NHSE Recovery Support Programme exit pathways. Printing, telephony and recruitment costs ran elevated during the transition due to dual-banner communications and parallel-system maintenance. April 2025 NIC step-up flows post-merger via MWL. Post-merger, this sub-line consolidates into MWL's establishment line; future Budget Galaxy traces should bridge to MWL's enrichment entry for continuity.",
    "sources": [
        {"publisher": "Southport and Ormskirk Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southportandormskirk.nhs.uk/about-us/our-publications/"},
        {"publisher": "Mersey and West Lancashire Teaching Hospitals NHS Trust", "title": "Acquisition of Southport and Ormskirk Hospital NHS Trust", "url": "https://www.merseywestlancs.nhs.uk/about-us/news-and-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Recovery Support Programme oversight framework", "url": "https://www.england.nhs.uk/publication/nhs-oversight-framework/"},
        {"publisher": "Care Quality Commission", "title": "Southport and Ormskirk Hospital NHS Trust provider profile (RVY)", "url": "https://www.cqc.org.uk/provider/RVY"}
    ],
    "related": ["Southport And Ormskirk Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Mersey and West Lancashire Teaching Hospitals NHS Trust", "PFI / LIFT charges — Southport And Ormskirk Hospital NHS Trust", "NHS England"]
}

NEW["Lease expenditure — Mersey and West Lancashire Teaching Hospitals NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Mersey and West Lancashire Teaching Hospitals NHS Trust"}],
    "description": "Mersey and West Lancashire Teaching Hospitals NHS Trust's £0.47M lease expenditure line covers IFRS 16 short-term and low-value lease charges (excluded from on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across an enlarged multi-site footprint following the 1 July 2024 acquisition of Southport and Ormskirk: Whiston Hospital (PFI 2010, principal acute), St Helens Hospital, Newton Community Hospital, Southport and Formby DGH, and Ormskirk DGH. The line sits alongside a substantial PFI unitary-charge stream for the Whiston build.",
    "beneficiaries": "c. 11,500 WTE staff (post-merger) serving a c. 700,000 catchment across St Helens, Knowsley, Halton, West Lancashire, Southport and Formby; c. 270,000 ED attendances/yr across Whiston, Southport and Ormskirk EDs; c. 175,000 admissions/yr; c. 1.0 million outpatient attendances/yr. Whiston is a designated trauma unit feeding the Aintree Major Trauma Centre.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.47M"},
        {"label": "Trust scale (post-merger)", "value": "Whiston (PFI 2010) + St Helens + Newton + Southport & Formby + Ormskirk; c. 11,500 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical-equipment leases"},
        {"label": "PFI context", "value": "Whiston Hospital is a 2010 PFI build (Healthcare Support [Newhospitals] Ltd / Equans FM); separate PFI/LIFT charges line"},
        {"label": "Merger context", "value": "1 July 2024 acquisition of Southport and Ormskirk Hospital NHS Trust — added two principal hereditaments + community sites to the lease portfolio"},
        {"label": "Cheshire & Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB with Aintree (Liverpool UH), Liverpool Heart and Chest, Wirral, Warrington pathways"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.32M (legacy STHK alone) → 2023-24 c. £0.41M → 2024-25 £0.47M — IFRS 16 + S&O acquisition lease assumption"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + NHSPS (community sites)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + Cheshire and Merseyside ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; CQC RBN inspections; NAO Acute reports; HSSIB backlog-maintenance reports"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges + standalone STHK lease portfolio · Successor: integrated MWL estate-portfolio rationalisation post-merger"}
    ],
    "notes": "MWL's lease line in 2024-25 reflects the first full quarter post-acquisition of Southport and Ormskirk (1 July 2024), bringing two additional principal hereditaments and an expanded community-clinic footprint into the portfolio. The trust's modern PFI-built Whiston facility minimises backlog-maintenance pressure on the principal acute site, but the acquired Southport and Ormskirk estate carries elevated condition risk requiring transitional leases for decant and modular accommodation. April 2025 NIC step-up affects E&F staffing rather than lease charges directly. The merger is a flagship NHSE Recovery Support Programme exit case, with Whiston's strong financial track record stabilising the combined balance sheet.",
    "sources": [
        {"publisher": "Mersey and West Lancashire Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.merseywestlancs.nhs.uk/about-us/news-and-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "Current Private Finance Initiative (PFI) projects", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
        {"publisher": "Care Quality Commission", "title": "Mersey and West Lancashire Teaching Hospitals NHS Trust provider profile (RBN)", "url": "https://www.cqc.org.uk/provider/RBN"},
        {"publisher": "NHS England", "title": "NHS Operational Plan 2024-25", "url": "https://www.england.nhs.uk/publication/nhs-operational-planning-and-contracting-guidance/"}
    ],
    "related": ["Mersey and West Lancashire Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Southport And Ormskirk Hospital NHS Trust", "PFI / LIFT charges — Mersey and West Lancashire Teaching Hospitals NHS Trust", "Department of Health and Social Care"]
}

NEW["Inventories written down — Royal Cornwall Hospitals NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Royal Cornwall Hospitals NHS Trust"}],
    "description": "Royal Cornwall Hospitals NHS Trust's £0.45M inventories-written-down line covers IAS 2 net-realisable-value adjustments and provisions for obsolete, expired and damaged stock — clinical consumables, pharmacy lines, prosthetics, theatre instruments and stores items — across the Royal Cornwall Hospital (Treliske, Truro), West Cornwall Hospital (Penzance) and St Michael's Hospital (Hayle) plus community satellite locations. Write-downs follow DHSC GAM ch.5 stocktaking and obsolescence guidance and feed quarterly into the operating cost statement.",
    "beneficiaries": "c. 5,200 WTE staff serving a c. 570,000 Cornwall + Isles of Scilly catchment — England's most peripheral large catchment with significant in-summer tourism surge demand; c. 95,000 ED attendances/yr at Treliske + WCH minor injuries; c. 75,000 admissions/yr; c. 360,000 outpatient attendances/yr; tertiary referrals onward to Plymouth + Bristol.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Human Medicines Regulations 2012 (pharmacy stock destruction)",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.45M"},
        {"label": "Trust scale", "value": "Royal Cornwall (Treliske) + West Cornwall (Penzance) + St Michael's (Hayle) + community sites; c. 5,200 WTE"},
        {"label": "Composition", "value": "Pharmacy expiry + theatre prosthetics obsolescence + clinical consumables damage + COVID PPE legacy tail + recall returns + safety-stock buffer obsolescence"},
        {"label": "NHS Supply Chain", "value": "c. 80% of clinical consumables routed via NHS Supply Chain Coordination Limited (SCCL); residual local procurement"},
        {"label": "Stocktake cadence", "value": "Year-end full count + quarterly cycle counts per DHSC GAM ch.5; theatre prosthetics tracked via track-and-trace"},
        {"label": "Geographic context", "value": "England's most peripheral acute trust — Treliske is c. 100 miles from Plymouth (next acute) — requires deeper safety-stock buffers"},
        {"label": "Cornwall ICS", "value": "Member of Cornwall and the Isles of Scilly ICB; tertiary onward to UH Plymouth (peninsula MTC) and UH Bristol Weston"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.58M (COVID PPE peak) → 2023-24 c. £0.48M → 2024-25 £0.45M — PPE legacy tail diminishing"},
        {"label": "Industrial action", "value": "44 days junior-doctor + 10 days consultant strikes 2023-24 disrupted theatre throughput, raising prosthesis obsolescence risk"},
        {"label": "Delivery body + policy owner", "value": "Trust Procurement + Pharmacy + Materials Management + NHS Supply Chain (SCCL); NHSE Provider Finance + DHSC GAM team"},
        {"label": "Evaluation evidence", "value": "NHSE Model Hospital benchmarking; DHSC SCCL annual report; Trust ARA 2023-24; NAO NHS supply-chain reports; CQC REF inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: COVID PPE legacy stock provisions · Successor: Scan4Safety + EPR-driven inventory rationalisation; Treliske women & children's NHP scheme"}
    ],
    "notes": "Royal Cornwall's write-down line is shaped by its peripheral geography — England's most distant large acute trust from peer hospitals (c. 100 miles to Plymouth, c. 200 miles to Bristol). This requires deeper safety-stock buffers in pharmacy and theatre prosthetics, raising obsolescence exposure vs urban peers. Summer tourism surge demand also distorts annual stock cycles. The trust's Frontline Digitisation EPR rollout (Oracle Health) is phased through 2024-26 with Scan4Safety integration expected to reduce future write-downs once mature. Industrial action 2023-24 disrupted elective theatre throughput. The Treliske women and children's hospital rebuild under the New Hospital Programme is in development; April 2025 NIC step-up affects pharmacy and stores staffing.",
    "sources": [
        {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalcornwall.nhs.uk/about-us/our-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain (SCCL)", "title": "Annual Report and Accounts", "url": "https://www.supplychain.nhs.uk/about-us/"},
        {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
        {"publisher": "Care Quality Commission", "title": "Royal Cornwall Hospitals NHS Trust provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"}
    ],
    "related": ["Royal Cornwall Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — University Hospitals Plymouth NHS Trust", "NHS Supply Chain Coordination Limited", "New Hospital Programme"]
}

NEW["Transport (business + patient) — George Eliot Hospital NHS Trust"] = {
    "aliases": [{"name": "Transport (business + patient)", "parent": "George Eliot Hospital NHS Trust"}],
    "description": "George Eliot Hospital NHS Trust's £0.44M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between the College Street main site (Nuneaton) and community/satellite locations, plus contracted non-emergency patient transport (NEPTS) for the Coventry and Warwickshire ICS catchment. As a small DGH on a single principal campus, GEH carries a lower transport line than peer multi-site trusts but still bears material specimen-courier and rural-NEPTS costs.",
    "beneficiaries": "c. 2,800 WTE staff serving a c. 300,000 Nuneaton, Bedworth and north Warwickshire catchment plus parts of south Leicestershire; c. 80,000 ED attendances/yr at College Street; c. 50,000 admissions/yr; c. 250,000 outpatient attendances/yr. The trust escaped a Foundation Trust takeover process in 2014 and remains a standalone DGH within Coventry and Warwickshire ICB.",
    "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Transport (business + patient) 2024-25", "value": "£0.44M"},
        {"label": "Trust scale", "value": "George Eliot Hospital (College St, Nuneaton) + community sites; c. 2,800 WTE; small DGH"},
        {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology courier + contracted NEPTS"},
        {"label": "NEPTS provider", "value": "EMED Group / E-zec on Coventry & Warwickshire ICB framework — retendered against NHSE 2021 NEPTS Review eligibility"},
        {"label": "Inter-site flow", "value": "Lower than multi-site peers — most activity on College Street campus; tertiary referrals onward to UHCW (Walsgrave)"},
        {"label": "Industrial action + NIC step-up", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel + NEPTS rebooking; April 2025 NIC step-up flows via contractor pass-through"},
        {"label": "AMAP rates 2024-25", "value": "HMRC AMAP frozen at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.32M → 2023-24 c. £0.40M → 2024-25 £0.44M — strike backfill + fuel pass-through + NEPTS uplift"},
        {"label": "Coventry & Warwickshire ICS", "value": "Member of Coventry and Warwickshire ICB; collaborative NEPTS commissioning with UHCW + South Warwickshire"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + EMED Group (NEPTS) + WMAS (emergency overlap)"},
        {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; Trust ARA 2023-24; CQC RLT inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-Review baseline · Successor: Coventry & Warwickshire ICB pool-fleet electrification + EPR-driven outpatient virtualisation"}
    ],
    "notes": "George Eliot is one of the smallest standalone Acute trusts in England, having survived a 2014 Trust Special Administrator process to remain independent. Its single-campus model keeps inter-site transport relatively contained, but rural NEPTS demand from north Warwickshire and the Bedworth periphery is significant given limited public transport. The trust feeds tertiary referrals onward to UH Coventry & Warwickshire (Walsgrave) for major trauma, cardiac and complex surgery. April 2025 NIC step-up flows indirectly via NEPTS contractor pass-through. Frozen HMRC AMAP rates compress staff-mileage real-terms reimbursement; ICB-wide NEPTS framework retendering provides some scale economies.",
    "sources": [
        {"publisher": "George Eliot Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.geh.nhs.uk/about-us/our-publications/"},
        {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
        {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "George Eliot Hospital NHS Trust provider profile (RLT)", "url": "https://www.cqc.org.uk/provider/RLT"}
    ],
    "related": ["George Eliot Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — South Warwickshire NHS Foundation Trust", "Establishment costs — George Eliot Hospital NHS Trust", "NHS England"]
}

NEW["Termination & post-employment — Oxford University Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
    "description": "Oxford University Hospitals NHS FT's £0.43M termination and post-employment line covers IAS 19 termination benefits — voluntary redundancy, MARS scheme settlements and contractual termination payments — plus injury-allowance, ill-health early-retirement and other post-employment benefit accruals not covered by the NHS Pension Scheme employer contribution. Recognition follows the earlier of the date the trust can no longer withdraw the offer and the date the related restructuring costs are recognised, per IAS 19.",
    "beneficiaries": "c. 13,500 WTE staff serving a c. 770,000 Oxfordshire catchment plus tertiary referrals from across the Thames Valley and beyond; c. 165,000 ED attendances/yr at the John Radcliffe ED; c. 130,000 admissions/yr; c. 1.0 million outpatient attendances/yr. Trust runs four principal hospitals — JR, Churchill, NOC (Headington), Horton General (Banbury) — and academic partnerships with the University of Oxford.",
    "legal_basis": "IAS 19 Employee Benefits — NHS Pension Scheme Regulations 2015 (and 1995/2008 schemes) — Public Sector Exit Payments Regulations 2020 (subsequently revoked Feb 2021) — Equality Act 2010 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.43M"},
        {"label": "Trust scale", "value": "John Radcliffe + Churchill + Nuffield Orthopaedic Centre + Horton General; c. 13,500 WTE"},
        {"label": "Composition", "value": "Voluntary redundancy + Mutually Agreed Resignation Scheme (MARS) + ill-health early retirement + injury allowance + contractual notice settlements"},
        {"label": "Recognition", "value": "IAS 19 paragraph 165 — earlier of withdrawal-of-offer date and related restructuring-cost recognition date"},
        {"label": "NHS Pension Scheme", "value": "Most accruals covered by employer contribution (NHSPS); termination line captures non-pension supplementary benefits + redundancy"},
        {"label": "Public Sector Exit Cap", "value": "£95k cap regs (2020) revoked Feb 2021; superseded by Treasury approvals process for high-value exits"},
        {"label": "Funding trajectory", "value": "Volatile by year — driven by individual exit cohorts, restructuring decisions, ill-health retirement crystallisations"},
        {"label": "BOB ICS", "value": "Member of Buckinghamshire, Oxfordshire and Berkshire West ICB; tertiary academic partner across the system"},
        {"label": "Industrial action", "value": "Junior-doctor + consultant disputes 2023-24 created limited termination exposure (most disputes resolved in-employment)"},
        {"label": "Delivery body + policy owner", "value": "Trust HR + Finance + Corporate Affairs + NHS Pensions Agency + HM Treasury (high-value approvals); DHSC + NHSE Provider Finance"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 IAS 19 disclosures; NAO Public Sector Exits reports; HM Treasury exit-payment guidance; CQC RTH inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 £95k exit-cap regime · Successor: Treasury HMT5 / Cabinet Office approval framework + IAS 19 routine accruals"}
    ],
    "notes": "OUH's termination line reflects ongoing role-rationalisation, MARS programmes and ill-health retirement crystallisations across one of England's largest research-active acute trusts (c. £900M+ research income through Oxford academic partnerships). The trust's high concentration of senior clinical academics generates higher-value termination cases than mean DGH levels, with HM Treasury exit-payment approvals occasionally required. The 2020 £95k exit-cap regulations were revoked in Feb 2021; the current regime relies on Treasury / Cabinet Office approvals plus IAS 19 routine accruals. April 2025 NIC step-up affects termination-payment costs incrementally. Industrial action 2023-24 had limited direct termination impact since most disputes resolved in-employment via pay deals.",
    "sources": [
        {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ouh.nhs.uk/about/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "Public Sector Exit Payments — guidance and approvals", "url": "https://www.gov.uk/government/publications/guidance-on-public-sector-exit-payments"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guide", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
        {"publisher": "Care Quality Commission", "title": "Oxford University Hospitals NHS Foundation Trust provider profile (RTH)", "url": "https://www.cqc.org.uk/provider/RTH"}
    ],
    "related": ["Oxford University Hospitals NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Termination & post-employment — Barts Health NHS Trust", "NHS Pension Scheme", "NHS England"]
}

NEW["PFI / LIFT charges — Southport And Ormskirk Hospital NHS Trust"] = {
    "aliases": [{"name": "PFI / LIFT charges", "parent": "Southport And Ormskirk Hospital NHS Trust"}],
    "description": "Southport and Ormskirk Hospital NHS Trust's £0.42M PFI / LIFT charges line covers residual unitary-charge components (interest, services and lifecycle elements per IFRIC 12 / DHSC GAM disaggregation) on legacy LIFT-funded community premises across the Southport, Formby and West Lancashire footprint. Neither Southport DGH nor Ormskirk DGH was procured under PFI — the principal estates are publicly funded — so this line is dominated by community-clinic LIFT exposure. The trust transitioned into Mersey and West Lancashire Teaching Hospitals on 1 July 2024.",
    "beneficiaries": "c. 3,400 WTE staff serving a c. 280,000 catchment in Southport, Formby and West Lancashire; c. 95,000 ED attendances/yr split across Southport and Ormskirk EDs; c. 60,000 admissions/yr; c. 320,000 outpatient attendances/yr. Catchment includes the Marie Curie Hospice Liverpool overlap and the Formby coastal corridor.",
    "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022) — DHSC Group Accounting Manual 2024-25 — DHSC PFI guidance — NHS LIFT Co arrangements — NHS Act 2006",
    "key_stats": [
        {"label": "PFI / LIFT charges 2024-25", "value": "£0.42M"},
        {"label": "Trust scale", "value": "Southport & Formby DGH + Ormskirk DGH + community sites; c. 3,400 WTE"},
        {"label": "Composition", "value": "Residual LIFT unitary-charge service + lifecycle elements on community-health hereditaments per IFRIC 12 disaggregation"},
        {"label": "Principal acutes NOT PFI", "value": "Both Southport DGH and Ormskirk DGH are publicly funded estates; line dominated by LIFT community-clinic component"},
        {"label": "LIFT scheme", "value": "Sefton & Knowsley LIFT / NHS LIFT framework — built community estate c. 2003-2010"},
        {"label": "Merger context", "value": "Acquired by Mersey and West Lancashire Teaching Hospitals NHS Trust on 1 July 2024 — final standalone year"},
        {"label": "Funding trajectory", "value": "Declining tail — peak unitary-charge years pre-2020; post-merger consolidates under MWL"},
        {"label": "Cheshire & Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB"},
        {"label": "Recovery Support Programme", "value": "Subject to NHSE Recovery Support Programme oversight pre-merger"},
        {"label": "Delivery body + policy owner", "value": "Trust Estates & Finance + LIFT Co + Mersey and West Lancs (post-merger); NHSE Provider Finance + DHSC LIFT/PFI team"},
        {"label": "Evaluation evidence", "value": "HM Treasury PFI projects database; NAO PFI reports; Trust ARA 2023-24; CQC RVY inspections; merger transaction documents"},
        {"label": "Predecessor / successor", "value": "Predecessor: 2003-2010 LIFT rollout · Successor: post-1 July 2024 consolidation under MWL + LIFT contract handbacks late 2020s"}
    ],
    "notes": "Southport and Ormskirk's small PFI/LIFT line in 2024-25 reflects the trust's avoidance of PFI procurement on its principal acute hospitals — both Southport and Ormskirk DGHs are publicly funded — leaving residual LIFT-Co charges on community-clinic hereditaments. This is the trust's final operating period as a standalone organisation before its 1 July 2024 acquisition by Mersey and West Lancashire Teaching Hospitals NHS Trust, completing a flagship NHSE Recovery Support Programme exit. Carillion 2018 collapse + Equans/Engie novations had limited direct effect given the LIFT-Co structure. April 2025 NIC step-up flows post-merger via MWL.",
    "sources": [
        {"publisher": "Southport and Ormskirk Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southportandormskirk.nhs.uk/about-us/our-publications/"},
        {"publisher": "HM Treasury", "title": "Current PFI projects 2018 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
        {"publisher": "Mersey and West Lancashire Teaching Hospitals NHS Trust", "title": "Acquisition of Southport and Ormskirk Hospital NHS Trust", "url": "https://www.merseywestlancs.nhs.uk/about-us/news-and-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "Southport and Ormskirk Hospital NHS Trust provider profile (RVY)", "url": "https://www.cqc.org.uk/provider/RVY"}
    ],
    "related": ["Southport And Ormskirk Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Southport And Ormskirk Hospital NHS Trust", "Mersey and West Lancashire Teaching Hospitals NHS Trust", "Department of Health and Social Care"]
}

NEW["Inventories written down — South Warwickshire NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "South Warwickshire NHS Foundation Trust"}],
    "description": "South Warwickshire NHS FT's £0.41M inventories-written-down line covers IAS 2 net-realisable-value adjustments and provisions for obsolete, expired and damaged stock — clinical consumables, pharmacy lines, prosthetics and stores items — across Warwick Hospital (Lakin Road), Stratford-upon-Avon Hospital (Arden Street) and community satellite locations. Write-downs follow DHSC GAM ch.5 stocktaking and obsolescence guidance. South Warwickshire is an integrated acute + community trust hosting most community services for south Warwickshire, raising the share of community-pharmacy and stores items in the provision profile.",
    "beneficiaries": "c. 4,800 WTE staff serving a c. 280,000 south Warwickshire catchment (Stratford-upon-Avon, Warwick, Leamington Spa, Kenilworth, rural South Warwickshire); c. 75,000 ED attendances/yr at Warwick Hospital; c. 55,000 admissions/yr; c. 350,000 outpatient + community contacts/yr; the integrated community pathway covers school nursing, district nursing and community hospitals.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Human Medicines Regulations 2012 (pharmacy stock destruction)",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.41M"},
        {"label": "Trust scale", "value": "Warwick Hospital + Stratford Hospital + community sites; c. 4,800 WTE; integrated acute + community"},
        {"label": "Composition", "value": "Pharmacy expiry + theatre prosthetics obsolescence + clinical consumables damage + community-stores items + COVID PPE legacy tail + recall returns"},
        {"label": "NHS Supply Chain", "value": "c. 80% of clinical consumables routed via NHS Supply Chain Coordination Limited (SCCL); residual local procurement"},
        {"label": "Stocktake cadence", "value": "Year-end full count + quarterly cycle counts per DHSC GAM ch.5; theatre prosthetics tracked via track-and-trace; community stores audited"},
        {"label": "Integrated pathway", "value": "Acute + community model raises community-pharmacy and stores items share of provision pool vs pure-acute peers"},
        {"label": "Coventry & Warwickshire ICS", "value": "Member of Coventry and Warwickshire ICB with George Eliot, UHCW pathways"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.52M (COVID PPE peak) → 2023-24 c. £0.43M → 2024-25 £0.41M — PPE legacy tail diminishing"},
        {"label": "Industrial action", "value": "44 days junior-doctor + 10 days consultant strikes 2023-24 disrupted theatre throughput, raising prosthesis obsolescence risk"},
        {"label": "Delivery body + policy owner", "value": "Trust Procurement + Pharmacy + Materials Management + community-services Stores + NHS Supply Chain (SCCL); NHSE Provider Finance + DHSC GAM team"},
        {"label": "Evaluation evidence", "value": "NHSE Model Hospital benchmarking; DHSC SCCL annual report; Trust ARA 2023-24; CQC RJC inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: COVID PPE legacy stock provisions · Successor: Scan4Safety + EPR-driven inventory rationalisation"}
    ],
    "notes": "South Warwickshire is one of England's longest-standing integrated acute + community trusts, with Warwick Hospital alongside an extensive community-services footprint covering school nursing, district nursing, community hospitals (Leamington, Stratford-upon-Avon) and end-of-life-care. This community integration shifts the inventory profile vs pure-acute peers — community-stores items, district-nurse equipment and integrated-pharmacy lines all contribute to provisions. The trust is part of the Coventry and Warwickshire ICB. Industrial action 2023-24 disrupted elective throughput. April 2025 NIC step-up affects pharmacy and stores staffing rather than inventory directly. Frontline Digitisation rollout drives Scan4Safety integration over 2024-26.",
    "sources": [
        {"publisher": "South Warwickshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swft.nhs.uk/about-us/publications"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain (SCCL)", "title": "Annual Report and Accounts", "url": "https://www.supplychain.nhs.uk/about-us/"},
        {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
        {"publisher": "Care Quality Commission", "title": "South Warwickshire NHS Foundation Trust provider profile (RJC)", "url": "https://www.cqc.org.uk/provider/RJC"}
    ],
    "related": ["South Warwickshire NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — University Hospitals Coventry And Warwickshire NHS Trust", "Social security & levy — South Warwickshire NHS Foundation Trust", "NHS Supply Chain Coordination Limited"]
}

NEW["Lease expenditure — Royal Surrey NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Royal Surrey NHS Foundation Trust"}],
    "description": "Royal Surrey NHS FT's £0.40M lease expenditure line covers IFRS 16 short-term and low-value lease charges (excluded from on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across the Royal Surrey County Hospital site (Egerton Road, Guildford) and community/satellite locations. The trust is the host for the St Luke's Cancer Centre — a regional radiotherapy and oncology hub for Surrey and west Sussex — driving leased-equipment refresh cycles for linacs, bunkers and imaging.",
    "beneficiaries": "c. 4,200 WTE staff serving a c. 320,000 catchment in the Guildford and Waverley areas plus a wider regional radiotherapy footprint of c. 1.5 million across Surrey and parts of West Sussex; c. 80,000 ED attendances/yr at Royal Surrey ED; c. 55,000 admissions/yr; c. 410,000 outpatient attendances/yr; the trust merged corporate functions with Ashford and St Peter's in 2020.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.40M"},
        {"label": "Trust scale", "value": "Royal Surrey County Hospital + St Luke's Cancer Centre + Cranleigh Village + community sites; c. 4,200 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical-equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "St Luke's Cancer Centre", "value": "Regional radiotherapy + oncology hub — drives leased-equipment refresh cycles (linacs, bunkers, imaging)"},
        {"label": "Surrey Heartlands ICS", "value": "Member of Surrey Heartlands ICB with Ashford and St Peter's, Epsom and St Helier (cross-ICS), Frimley pathways"},
        {"label": "Group governance", "value": "Royal Surrey + Ashford and St Peter's share executive team and governance arrangements (group model)"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.30M → 2023-24 c. £0.38M → 2024-25 £0.40M — IFRS 16 transition steady-state + cancer-equipment leases"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + NHSPS (community sites)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + Surrey Heartlands ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; CQC RA2 inspections; NAO Acute reports; NHSE Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: group-model estate-portfolio rationalisation with Ashford and St Peter's"}
    ],
    "notes": "Royal Surrey's lease line is shaped by the regional St Luke's Cancer Centre — a high-throughput radiotherapy hub whose linac and imaging refresh cycles drive material leased-equipment turnover. The trust runs a group governance model with neighbouring Ashford and St Peter's NHS Foundation Trust under a shared executive arrangement adopted from 2020, enabling joint estate and procurement strategy. Most short-term and low-value leases capture community-clinic premises (including Cranleigh Village Hospital) and IT/medical-equipment leases below IFRS 16 ROU thresholds. April 2025 NIC step-up affects E&F staffing rather than lease charges directly. The trust avoided major RAAC backlog given its principal estate construction.",
    "sources": [
        {"publisher": "Royal Surrey NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalsurrey.nhs.uk/about-us/our-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "Royal Surrey NHS Foundation Trust provider profile (RA2)", "url": "https://www.cqc.org.uk/provider/RA2"},
        {"publisher": "NHS England", "title": "NHS Operational Plan 2024-25", "url": "https://www.england.nhs.uk/publication/nhs-operational-planning-and-contracting-guidance/"},
        {"publisher": "NHS England", "title": "Cancer Alliances and radiotherapy network", "url": "https://www.england.nhs.uk/cancer/strategy/radiotherapy/"}
    ],
    "related": ["Royal Surrey NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Ashford and St Peter's Hospitals NHS Foundation Trust", "Lease expenditure — Frimley Health NHS Foundation Trust", "Department of Health and Social Care"]
}

NEW["Lease expenditure — Northampton General Hospital NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Northampton General Hospital NHS Trust"}],
    "description": "Northampton General Hospital NHS Trust's £0.40M lease expenditure line covers IFRS 16 short-term and low-value lease charges (excluded from on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across the Cliftonville site (Northampton) plus community/satellite locations. Northampton General is a DGH plus the regional cancer centre for Northamptonshire, partnered in a group model with Kettering General Hospital under the University Hospitals of Northamptonshire NHS Group adopted in 2021.",
    "beneficiaries": "c. 5,300 WTE staff serving a c. 380,000 catchment across Northampton and south Northamptonshire plus a regional cancer-centre referral footprint of c. 700,000; c. 100,000 ED attendances/yr at Cliftonville ED; c. 75,000 admissions/yr; c. 425,000 outpatient attendances/yr; co-runs the University Hospitals of Northamptonshire group with Kettering General.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.40M"},
        {"label": "Trust scale", "value": "Northampton General (Cliftonville) + community sites; c. 5,300 WTE; regional cancer centre"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical-equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Group governance", "value": "University Hospitals of Northamptonshire NHS Group with Kettering General Hospital — shared executive team and group strategy"},
        {"label": "Cancer centre", "value": "Regional cancer centre for Northamptonshire — drives leased-equipment refresh cycles (linacs, imaging)"},
        {"label": "Northamptonshire ICS", "value": "Member of Northamptonshire ICB with Kettering General, Northants Healthcare (MH/community)"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.30M → 2023-24 c. £0.38M → 2024-25 £0.40M — IFRS 16 transition steady-state"},
        {"label": "Estate condition", "value": "Mixed-age estate — some 1960s-1970s blocks; not on RAAC critical-mitigation list"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + NHSPS (community sites)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + Northamptonshire ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; CQC RNS inspections; NAO Acute reports; NHSE Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: UHN-group estate rationalisation + cancer-pathway redesign"}
    ],
    "notes": "Northampton General's lease line is shaped by the trust's group partnership with Kettering General Hospital under the University Hospitals of Northamptonshire (UHN) NHS Group, adopted from 2021 — a flagship NHSE provider-collaboration model that pre-dated the formalisation of provider collaboratives in the Health and Care Act 2022. Joint procurement and group estate strategy enable some lease consolidation across the two hospitals. The trust's regional cancer centre drives leased-equipment refresh cycles, particularly linacs and oncology imaging. April 2025 NIC step-up affects E&F staffing rather than lease charges directly. Northampton avoided RAAC critical-mitigation listing despite mixed-age estate.",
    "sources": [
        {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northamptongeneral.nhs.uk/AboutUs/Publications/"},
        {"publisher": "University Hospitals of Northamptonshire NHS Group", "title": "Group strategy and joint working", "url": "https://www.northamptongeneral.nhs.uk/AboutUs/UHN/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "Northampton General Hospital NHS Trust provider profile (RNS)", "url": "https://www.cqc.org.uk/provider/RNS"},
        {"publisher": "NHS England", "title": "Provider Collaboratives guidance", "url": "https://www.england.nhs.uk/integratedcare/integrated-care-in-action/provider-collaboratives/"}
    ],
    "related": ["Northampton General Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Kettering General Hospital NHS Foundation Trust", "Social security & levy — Kettering General Hospital NHS Foundation Trust", "Department of Health and Social Care"]
}

NEW["Lease expenditure — Wye Valley NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Wye Valley NHS Trust"}],
    "description": "Wye Valley NHS Trust's £0.40M lease expenditure line covers IFRS 16 short-term and low-value lease charges (excluded from on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across Hereford County Hospital (Stonebow Road, a 2002 PFI build), Bromyard Community Hospital, Leominster Community Hospital and Ross-on-Wye Community Hospital. The line sits alongside the trust's substantial PFI unitary-charge stream for the Hereford build. Wye Valley is an integrated acute + community trust serving Herefordshire and parts of Powys.",
    "beneficiaries": "c. 3,200 WTE staff serving a c. 200,000 Herefordshire catchment plus cross-border flows from mid-Wales; c. 65,000 ED attendances/yr at Hereford County Hospital ED; c. 45,000 admissions/yr; c. 240,000 outpatient + community contacts/yr; the integrated model covers community hospitals at Bromyard, Leominster and Ross-on-Wye with rehab and step-down beds.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.40M"},
        {"label": "Trust scale", "value": "Hereford County Hospital (PFI 2002) + Bromyard + Leominster + Ross-on-Wye community hospitals; c. 3,200 WTE"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical-equipment leases"},
        {"label": "PFI context", "value": "Hereford County Hospital is a 2002 PFI build (Mercia Healthcare Ltd, FM novated through Carillion 2018 collapse to Engie/Equans); separate PFI/LIFT charges line"},
        {"label": "Carillion fallout", "value": "Original FM contractor Carillion collapsed Jan 2018; novated to Engie / Equans; ongoing FM contract instability"},
        {"label": "Integrated pathway", "value": "Acute + community model raises community-clinic and integrated-stores items share of lease portfolio"},
        {"label": "Herefordshire & Worcestershire ICS", "value": "Member of Herefordshire and Worcestershire ICB with Worcestershire Acute Hospitals + Powys Teaching HB cross-border collaboration"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.30M → 2023-24 c. £0.38M → 2024-25 £0.40M — IFRS 16 transition steady-state"},
        {"label": "Cross-border flows", "value": "Material flows from Powys (Wales) — historic NHS England commissioning agreement with Powys Teaching Health Board"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + NHSPS (community sites)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + Herefordshire and Worcestershire ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; CQC RLQ inspections; NAO PFI reports; NAO Acute reports"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: ICS-wide community-clinic estate rationalisation"}
    ],
    "notes": "Wye Valley's lease line is shaped by its integrated acute + community model — the trust runs Hereford County (PFI 2002, FM contracts novated through the Carillion 2018 collapse to Engie/Equans) plus three community hospitals at Bromyard, Leominster and Ross-on-Wye serving a dispersed rural Herefordshire population. Cross-border patient flows from Powys (Wales) under historic NHSE commissioning arrangements with Powys Teaching Health Board add complexity to community-clinic lease portfolios. April 2025 NIC step-up affects E&F staffing rather than lease charges directly. The Carillion novation continues to drive FM contractor churn at Hereford County's PFI estate. Wye Valley is a key integrated-care exemplar for rural England.",
    "sources": [
        {"publisher": "Wye Valley NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wyevalley.nhs.uk/about-us/our-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "Current PFI projects 2018 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
        {"publisher": "National Audit Office", "title": "Investigation: the collapse of Carillion (2018)", "url": "https://www.nao.org.uk/reports/investigation-into-the-governments-handling-of-the-collapse-of-carillion/"},
        {"publisher": "Care Quality Commission", "title": "Wye Valley NHS Trust provider profile (RLQ)", "url": "https://www.cqc.org.uk/provider/RLQ"}
    ],
    "related": ["Wye Valley NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Wye Valley NHS Trust", "Lease expenditure — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
}

NEW["Termination & post-employment — Barts Health NHS Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "Barts Health NHS Trust"}],
    "description": "Barts Health NHS Trust's £0.39M termination and post-employment line covers IAS 19 termination benefits — voluntary redundancy, MARS scheme settlements and contractual termination payments — plus injury-allowance, ill-health early-retirement and other post-employment benefit accruals not covered by the NHS Pension Scheme employer contribution across England's largest acute NHS trust by turnover and workforce. Barts Health runs five principal hospitals — The Royal London, St Bartholomew's, Whipps Cross, Newham, Mile End — across east London.",
    "beneficiaries": "c. 18,000 WTE staff serving a c. 2.5 million catchment across north-east London (Tower Hamlets, Newham, Waltham Forest, City of London plus tertiary referrals from across the M25 and beyond); c. 350,000 ED attendances/yr across The Royal London, Newham and Whipps Cross EDs; c. 250,000 admissions/yr; c. 1.6 million outpatient attendances/yr; the trust hosts the London Air Ambulance Major Trauma Centre.",
    "legal_basis": "IAS 19 Employee Benefits — NHS Pension Scheme Regulations 2015 (and 1995/2008 schemes) — Public Sector Exit Payments Regulations 2020 (subsequently revoked Feb 2021) — Equality Act 2010 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.39M"},
        {"label": "Trust scale", "value": "Royal London + St Bart's + Whipps Cross + Newham + Mile End; c. 18,000 WTE; England's largest acute trust by turnover"},
        {"label": "Composition", "value": "Voluntary redundancy + Mutually Agreed Resignation Scheme (MARS) + ill-health early retirement + injury allowance + contractual notice settlements"},
        {"label": "Recognition", "value": "IAS 19 paragraph 165 — earlier of withdrawal-of-offer date and related restructuring-cost recognition date"},
        {"label": "NHS Pension Scheme", "value": "Most accruals covered by employer contribution (NHSPS); termination line captures non-pension supplementary benefits + redundancy"},
        {"label": "Public Sector Exit Cap", "value": "£95k cap regs (2020) revoked Feb 2021; superseded by Treasury approvals process for high-value exits"},
        {"label": "MTC + tertiary specialties", "value": "London Air Ambulance MTC at Royal London; tertiary cardiac at St Bart's; specialist haematology + cancer"},
        {"label": "Funding trajectory", "value": "Volatile by year — driven by individual exit cohorts, restructuring decisions, ill-health retirement crystallisations, Whipps Cross rebuild prep"},
        {"label": "NEL ICS", "value": "Member of North East London ICB; provider-collaborative member with Homerton, Barking Havering & Redbridge"},
        {"label": "Whipps Cross NHP", "value": "Whipps Cross Hospital named in the New Hospital Programme — rebuild planned with workforce-transition implications mid-2020s"},
        {"label": "Delivery body + policy owner", "value": "Trust HR + Finance + Corporate Affairs + NHS Pensions Agency + HM Treasury (high-value approvals); DHSC + NHSE Provider Finance"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 IAS 19 disclosures; NAO Public Sector Exits reports; HM Treasury exit-payment guidance; CQC R1H inspections"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 £95k exit-cap regime · Successor: Treasury HMT5 / Cabinet Office approval framework + Whipps Cross rebuild workforce planning"}
    ],
    "notes": "Barts Health is England's largest acute NHS trust by turnover (c. £2.0bn) and one of the largest by workforce (c. 18,000 WTE). Its termination line reflects ongoing role-rationalisation, MARS programmes and ill-health retirement crystallisations across five principal hospitals. The Whipps Cross rebuild under the New Hospital Programme is in preparation phase — workforce planning for transition will increasingly feed this line as construction phases progress. The trust's high concentration of senior clinical academics (Queen Mary partnership) generates higher-value termination cases than mean DGH levels. April 2025 NIC step-up affects termination-payment costs incrementally. Industrial action 2023-24 had limited direct termination impact since most disputes resolved in-employment via pay deals.",
    "sources": [
        {"publisher": "Barts Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bartshealth.nhs.uk/our-publications"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "Public Sector Exit Payments — guidance and approvals", "url": "https://www.gov.uk/government/publications/guidance-on-public-sector-exit-payments"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guide", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
        {"publisher": "Care Quality Commission", "title": "Barts Health NHS Trust provider profile (R1H)", "url": "https://www.cqc.org.uk/provider/R1H"}
    ],
    "related": ["Barts Health NHS Trust", "Staff Costs", "NHS Acute Trusts", "Termination & post-employment — Oxford University Hospitals NHS Foundation Trust", "New Hospital Programme", "NHS Pension Scheme"]
}

NEW["Lease expenditure — Hull University Teaching Hospitals NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Hull University Teaching Hospitals NHS Trust"}],
    "description": "Hull University Teaching Hospitals NHS Trust's £0.38M lease expenditure line covers IFRS 16 short-term and low-value lease charges (excluded from on-balance-sheet right-of-use treatment per DHSC GAM ch.7) plus residual operating-lease costs across Hull Royal Infirmary (Anlaby Road), Castle Hill Hospital (Cottingham — site of the Queen's Centre cancer hub) plus community/satellite locations. The trust is a major teaching trust partnered with the Hull York Medical School and serves the Humber, Coast and Vale region.",
    "beneficiaries": "c. 9,500 WTE staff serving a c. 600,000 Hull and East Riding catchment plus a wider regional referral footprint of c. 1.2 million across Humber, Coast and Vale; c. 165,000 ED attendances/yr at Hull Royal Infirmary ED; c. 110,000 admissions/yr; c. 720,000 outpatient attendances/yr; the Queen's Centre at Castle Hill is a regional cancer centre.",
    "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.38M"},
        {"label": "Trust scale", "value": "Hull Royal Infirmary + Castle Hill (Queen's Centre cancer) + community sites; c. 9,500 WTE; major teaching trust"},
        {"label": "Composition", "value": "Short-term + low-value leases excluded from ROU per IFRS 16 + residual operating-lease tail; community premises + IT + medical-equipment leases"},
        {"label": "Treatment", "value": "Leases under 12 months or low value charged direct to operating expenses per IFRS 16 paragraph 5"},
        {"label": "Tower block estate", "value": "Hull Royal Infirmary tower block is a 1960s build with significant backlog-maintenance liability; not on RAAC critical-mitigation list"},
        {"label": "Cancer centre", "value": "Queen's Centre at Castle Hill — regional cancer hub with linac and oncology imaging refresh cycles"},
        {"label": "HCV ICS", "value": "Member of Humber and North Yorkshire ICB with NLAG, York and Scarborough, Harrogate pathways"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.27M → 2023-24 c. £0.36M → 2024-25 £0.38M — IFRS 16 transition steady-state"},
        {"label": "Industrial action backfill", "value": "44 days junior-doctor + 10 days consultant strikes 2023-24 drove temporary modular accommodation + agency-locum desk leases"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Procurement + landlord counterparties + NHSPS (community sites)"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM team + Humber and North Yorkshire ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 leases note; CQC RWA inspections; NAO Acute reports; NHSE Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 (1 April 2022) operating-lease charges · Successor: Hull Royal Infirmary tower-block redevelopment + ICS estate rationalisation"}
    ],
    "notes": "Hull UTH's lease line is shaped by the trust's two-site model — the 1960s Hull Royal Infirmary tower block (significant backlog-maintenance liability but not RAAC) plus the Queen's Centre at Castle Hill (regional cancer hub). Short-term and low-value leases capture community-clinic premises, IT and medical-equipment leases that fall below IFRS 16 ROU thresholds. The Hull York Medical School partnership and major-teaching-trust status drive equipment-lease refresh cycles, particularly in cancer and imaging. Industrial action 2023-24 created modular accommodation and agency-locum desk demands. April 2025 NIC step-up affects E&F staffing rather than lease charges directly. The trust's partnership with NLAG creates joint commissioning leverage.",
    "sources": [
        {"publisher": "Hull University Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hey.nhs.uk/about-us/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "Hull University Teaching Hospitals NHS Trust provider profile (RWA)", "url": "https://www.cqc.org.uk/provider/RWA"},
        {"publisher": "NHS England", "title": "NHS Operational Plan 2024-25", "url": "https://www.england.nhs.uk/publication/nhs-operational-planning-and-contracting-guidance/"},
        {"publisher": "Hull York Medical School", "title": "Teaching trust partnership", "url": "https://www.hyms.ac.uk/about/clinical-partnerships"}
    ],
    "related": ["Hull University Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Northern Lincolnshire and Goole NHS Foundation Trust", "Lease expenditure — York and Scarborough Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
}

NEW["Inventories written down — Mid Cheshire Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Mid Cheshire Hospitals NHS Foundation Trust"}],
    "description": "Mid Cheshire Hospitals NHS FT's £0.38M inventories-written-down line covers IAS 2 net-realisable-value adjustments and provisions for obsolete, expired and damaged stock — clinical consumables, pharmacy lines, prosthetics, theatre instruments and stores items — across Leighton Hospital (Crewe), Victoria Infirmary (Northwich), Elmhurst Intermediate Care Centre and community satellites. Write-downs follow DHSC GAM ch.5 stocktaking and obsolescence guidance. Mid Cheshire is named in the October 2023 New Hospital Programme RAAC seven for full rebuild, with implications for inventory cycling during decant.",
    "beneficiaries": "c. 4,500 WTE staff serving a c. 320,000 catchment across Crewe, Nantwich, Northwich and the wider mid-Cheshire footprint; c. 80,000 ED attendances/yr at Leighton ED; c. 60,000 admissions/yr; c. 360,000 outpatient attendances/yr; the trust serves a mix of urban (Crewe railway-town deprivation) and rural (Cheshire countryside) populations.",
    "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Human Medicines Regulations 2012 (pharmacy stock destruction)",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.38M"},
        {"label": "Trust scale", "value": "Leighton (Crewe) + Victoria Infirmary (Northwich) + Elmhurst ICC + community sites; c. 4,500 WTE"},
        {"label": "Composition", "value": "Pharmacy expiry + theatre prosthetics obsolescence + clinical consumables damage + COVID PPE legacy tail + recall returns + RAAC-decant transitional stock"},
        {"label": "NHS Supply Chain", "value": "c. 80% of clinical consumables routed via NHS Supply Chain Coordination Limited (SCCL); residual local procurement"},
        {"label": "Stocktake cadence", "value": "Year-end full count + quarterly cycle counts per DHSC GAM ch.5; theatre prosthetics tracked via track-and-trace"},
        {"label": "RAAC + NHP", "value": "Leighton Hospital named in October 2023 RAAC seven announcement — funded for full rebuild by 2030 under New Hospital Programme"},
        {"label": "Cheshire & Merseyside ICS", "value": "Member of Cheshire and Merseyside ICB"},
        {"label": "Funding trajectory", "value": "2021-22 c. £0.50M (COVID PPE peak) → 2023-24 c. £0.41M → 2024-25 £0.38M — PPE legacy tail diminishing; RAAC-decant uplift offsetting"},
        {"label": "Industrial action", "value": "44 days junior-doctor + 10 days consultant strikes 2023-24 disrupted theatre throughput, raising prosthesis obsolescence risk"},
        {"label": "Delivery body + policy owner", "value": "Trust Procurement + Pharmacy + Materials Management + NHS Supply Chain (SCCL); NHSE Provider Finance + DHSC GAM team + DHSC NHP"},
        {"label": "Evaluation evidence", "value": "NHSE Model Hospital benchmarking; DHSC SCCL annual report; HSSIB RAAC reports; Trust ARA 2023-24; CQC RBT inspections"},
        {"label": "Estate condition", "value": "Leighton Hospital is RAAC-plank constructed across most clinical blocks; one of the highest-risk RAAC trusts"},
        {"label": "Predecessor / successor", "value": "Predecessor: COVID PPE legacy stock provisions · Successor: Scan4Safety + EPR-driven inventory rationalisation; post-2030 NHP rebuild stock-system reset"}
    ],
    "notes": "Mid Cheshire's write-down line is shaped by Leighton Hospital's status as one of the most extensively RAAC-affected acute estates in England — named in the October 2023 New Hospital Programme RAAC seven for full rebuild by 2030 (HSSIB tracking confirms RAAC planks across most clinical blocks). The decant and structural-mitigation programme drives transitional stock cycling — inventory held in temporary storage during ward closures carries elevated obsolescence risk. Industrial action 2023-24 also disrupted elective throughput. April 2025 NIC step-up affects pharmacy and stores staffing. Frontline Digitisation rollout drives Scan4Safety integration over 2024-26, with future inventory-system reset at the post-2030 rebuild commissioning point.",
    "sources": [
        {"publisher": "Mid Cheshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mcht.nhs.uk/about-us/our-publications/"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — RAAC announcement October 2023", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain (SCCL)", "title": "Annual Report and Accounts", "url": "https://www.supplychain.nhs.uk/about-us/"},
        {"publisher": "Care Quality Commission", "title": "Mid Cheshire Hospitals NHS Foundation Trust provider profile (RBT)", "url": "https://www.cqc.org.uk/provider/RBT"}
    ],
    "related": ["Mid Cheshire Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "New Hospital Programme", "NHS Supply Chain Coordination Limited", "Inventories written down — University Hospitals Coventry And Warwickshire NHS Trust"]
}
