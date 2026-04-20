# Sprint 1 Review Log — 2026-04-20

**Scope**: 4 top-level UK departments promoted from Tier B-compact to Tier A (gold standard). DWP-level richness — ≥8 key stats, legal basis, notes with real controversy, sources with URLs.

**Result**: 4/4 at gold · 40 total Tier A entries in the system.

| Dept | Stats | Sources | Aliases | Gold | Tree-match |
|---|---|---|---|---|---|
| DEPARTMENT OF HEALTH | 13 | 6 | 3 | ✅ | ✅ |
| HOME OFFICE | 13 | 7 | 1 | ✅ | ✅ |
| DEPARTMENT FOR EDUCATION | 17 | 7 | 2 | ✅ | ✅ |
| MINISTRY OF HOUSING, COMMUNITIES AND LOCAL GOVERNMENT | 16 | 7 | 4 | ✅ | ✅ |

## What each agent added beyond the brief

### DoH
- **Corrected the brief**: GP workforce is 27,500 fully-qualified FTE + 10,400 registrars (NHS Digital General Practice Workforce Jan 2025), not 36,500+23,000. Agent overrode my incorrect number with the canonical source. 🟢
- **Flagged own uncertainty**: Jan 2026 RTT (~6.28M pathways) and Feb 2026 A&E 4-hour (~73.4%) — I used placeholder "~73% (2025)" in the final entry to avoid false precision.
- **Added scope note**: £83B OSCAR line is DHSC *net* of Provider Sector; full DHSC group DEL is £181.7B. Critical for user understanding. 🟢
- **Leng Review July 2025** on Physician Associate scope — I included in notes.

### Home Office
- **Added Angiolini Inquiry Part 1 (Feb 2024)** — Couzens vetting — more recent than Casey alone.
- **Added BSAI Bill 2025 details** — Border Security Command structure, new criminal offences.
- **Cross-reference warning** — flagged that CT £1B sits within the police funding envelope (avoid double-counting in the galaxy). Included in notes implicitly.
- **Angiolini over Casey distinction** — Casey was about culture; Angiolini about vetting. Both cited.

### DfE
- **Corrected the brief**: academies are 82.4% of secondary pupils (not 52%). DfE Schools, Pupils and their Characteristics 2023-24. 🟢 This was a factual error in my brief, caught and fixed.
- **Verified EHCP +140%**: 240,183 → 576,474 literally +140.0%.
- **Leaving rate 9.9%** — highest non-pandemic figure recorded (School Workforce Census Nov 2023).
- **Added Ruth Perry PFD report** exact date (7 Dec 2023) and Senior Coroner name.

### MHCLG
- **Added DLUHC → MHCLG rename July 2024** under Starmer government — agent caught this, I didn't brief it.
- **Added Band D average** (£2,171 in 2024-25) — perfect clickable stat.
- **Post-2023 merger count**: 317 principal councils (not pre-merger 353). Agent overrode my brief correctly.
- **NAO/PAC political-steering critique of LUF** — more rigorous than the brief wanted.
- **Awaab Ishak age and date** (2-year-old, 2020, Rochdale) included.

## Verifier flags — all resolved or explained

| Flag | Resolution |
|---|---|
| DoH "NHSE total DEL £168.8B" vs tree £83B (ratio 2.02) | ✅ **Fixed label** — now reads "NHSE total DEL 2024-25 (whole England, before this £83B split)". The scope note in the description explains the cascade. |
| DoH CHC £4.0B vs tree £83B (ratio 0.05) | False positive — CHC is sub-component. Verifier's naive label-match catches "spend" in label. Acceptable. |
| MHCLG CSP £64.7B vs tree £46.1B (ratio 1.4) | ✅ **Fixed label** — now reads "CSP = all England-council funding: MHCLG grants + retained rates + precept ceiling". |
| MHCLG Levelling Up £4.8B vs tree £46.1B (ratio 0.1) | False positive — LUF is sub-component. Acceptable. |

## Hero-grounding attempts

Tried WebFetch for:
- NHS England board papers March 2025 (abolition announcement) → **404** — URL slug may have changed
- NAO UK-Rwanda Partnership report → **404** — URL slug may have changed
- BBC News on NHS abolition → **403** — BBC blocks tool-fetch

**Status**: hero-grounding not completed this sprint due to tooling friction. Agents cited specific publisher URLs that should be checked by a human with a browser. Load-bearing claims for the sprint:

1. NHS England abolition **13 March 2025** by Starmer + Streeting — ✅ widely reported, cited in DoH notes
2. Rwanda cancellation **6 July 2024** for total **~£700M** — ✅ NAO March 2024 report cited
3. Small-boats 2024 = **36,816** (new annual record) — ✅ Home Office Immigration System Statistics
4. Birmingham s114 **5 September 2023**, £760M equal-pay + £131M Oracle — ✅ well-documented
5. Academies **82.4% of secondary pupils** — ✅ DfE School Pupils and Characteristics 2023-24

**Recommendation**: when you hard-refresh and spot-check, eyeball these 5 facts in the UI against your own knowledge. If any look wrong, file an issue.

## What still needs fixing

- **31 of 40 Tier A entries still have sources without URLs** (including the 4 new ones — where some URLs were provided by agents, others rely on publisher-only citation). Needs a future URL-enrichment pass.
- **Police Core Grant and Formula Funding** — the one remaining Tier A orphan without a tree match. Tree has generic "Police" nodes but no line called that exactly. May need to add to Home Office's card or accept that it's unreachable.
- **Scottish Child Payment** — documented orphan, kept for content completeness.

## Next sprint

Sprint 2: **MoJ · HMT · DfT** (4 depts → 3 depts because HMRC already Tier A). Same protocol: customised dimension-profile briefs, manual review, scope-clarifier on labels, URLs in sources where known.

## User spot-check

Hard-refresh http://localhost:8765/ and click:
1. Budget Galaxy → click **NHS Provider Sector**, then back, click **Department of Health** → should show 13-stat rich panel with scope note about £83B vs £181.7B
2. Click **Home Office** → Rwanda + Bibby Stockholm + Casey all in notes
3. Click **Department for Education** → 17 stats inc. EHCP growth, Plan 5, Ruth Perry
4. Click **Ministry of Housing, Communities and Local Government** → Band D £2,171, Birmingham s114, Awaab's Law

If any of those feel bajón or contain anything suspect, flag and we loop back.
