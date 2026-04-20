# Changelog

All notable changes to Budget Galaxy are documented here.

## [Unreleased] - 2026-04-18 — Launch-week frontend polish (session 2)

### Added
- **Axis-labeled time chart** replaces the decorative sparkline in Explore's detail hero. Function `_cmplistTimeChart()` renders £-axis (min/max), year-axis (first/middle/last), gridlines, and a hover tooltip showing `year · value · Δ y/y`. Title is explicit: *"Nominal spend · {firstYear} → {lastYear}"*. Subtitle warns "Not inflation-adjusted. Hover a year for the exact figure and year-on-year change." The thin 90×18 sparkline remains for sub-item inline decoration. When no history is available at a given depth, a plain explainer card replaces it instead of silent-blank.
- **Source footer on every Galaxy node**. New `_galaxyResolveSource()` walks the d3.hierarchy `.parent` chain (vs. the pathArr walker used in Explore), then shares `_cmplistBranchDefault()` + `_UK_SOURCE_URLS` + `_cmplistSourceFooter()` with Explore. Parity of attribution across the two tabs.
- **"Sources · every number above is traceable" panel** at the bottom of Your Taxes. Six-row grid listing each data layer with publisher name + URL + committed file path. Layers: HMRC 2024-25 bands · ONS ETB 2022 · MHCLG 2024-25 CT · HMT OSCAR II · MHCLG RO5 per-council · OBR March 2024 EFO. Footer links to GitHub repo + issue tracker.
- **Monitoring infrastructure** (launch-ready, disabled by default). `window.BG_MONITOR` config object in `<head>` gates:
  - Plausible Analytics — cookie-less, DNT-respecting pageviews. Script only loads on `budgetgalaxy.com` hostname.
  - Sentry browser SDK — JS errors + unhandled promise rejections. 10% trace sample, session replay off (privacy).
  - Fallback `window.onerror` + `unhandledrejection` loggers (always on) write structured context to console.
  Activated by filling `plausibleDomain` + `sentryDsn` post-launch. No DSN = no network calls.
- `showTab()` now calls `window.bgTrackTab(name)` for per-tab usage analytics via Plausible custom events (no-op if Plausible not loaded).

### Changed
- Explore detail panel: sparkline box replaced by full `.tchart-wrap` with axis labels and hover tooltip. CSS: `.tchart-wrap`, `.tchart-title`, `.tchart-surface`, `.tchart-tooltip`, `.tchart-dot`.

### Deferred to v1.1 (post-launch)
- **Split 15k-line `frontend/index.html`** into `app.js` + `styles.css` + templates. Decision: too risky the week of launch; single-file works; refactor after first 500 users. Tracked in `NEXT_SESSION_PROMPT.md`.
- **UK councils at 13.5% missing** (Dorset £721M, Northumberland £604M, big PCCs). Requires Hetzner London VPS (~€4/mo) for geo-gated downloads. Tracked in existing `NEXT_SESSION_PROMPT.md` archive section.

## [Unreleased] - 2026-04-18 — Launch-week frontend polish

### Added
- **Insights tab** (`💡 Insights`) — 15 pilot editorial findings across 5 categories (tax, evolution, recipients, councils, structure). Every insight: narrative · viz spec · "what now?" actions · sources (publisher URL + our file SHA256) · related-insight IDs.
  - Generator: `scripts/md_to_insight_json.py` (markdown → per-category JSON + `_index.json`)
  - Verifier: `scripts/verify_insights.py` (Python mirror of `uk_calc.js`; recomputes every number in every insight from the underlying data files)
  - Editorial rules enforced programmatically: no adjectives, no proper names in body, descriptive not negative, sourced + drillable
- **Your Taxes tab** (`💰 Your Taxes`) — Honest Taxpayer Slider. Full IT + NI + VAT + council-tax calc, Sankey flow visualisation, per-council trace of where the user's CT share lands, URL hash deep-links (`#taxpayer/s/{salary}/j/r/{jurisdiction}/r/{region}/c/{council}`).
- **Explore & Compare — master-detail rebuild**. Replaced dry "click drills to next layer" with persistent tree sidebar (340px) + rich detail panel on every selection. Expansion state in a Set of path keys; localStorage persistence.
- **Any-depth enrichment** in Explore & Compare — every node at every depth now renders: 10-year sparkline, Δ y/y, Δ 5y, % of UK total, % of parent, per-capita chip, "Where this line sits" ancestor-percentage card, composition bar, and sub-items with inline sparklines.
- **Source attribution on every node** in Explore & Compare. New `_cmplistResolveSource()` walks ancestors, then falls back to branch-specific defaults: Local Gov → MHCLG RO5; NHS Provider Sector → NHS TAC 2023/24; Scottish Gov → gov.scot Budget; Welsh → gov.wales; NI → finance-ni.gov.uk; everything else → HMT OSCAR II. Footer shows publisher + link + `_exp_codes` / `_sta_codes` as chips + yellow warning for estimated years.
- 402-supplier Budget Recipients tab with UBO resolution badges (government / individual / listed / foreign / data-gap).
- Budget Galaxy: 70-colour palette across 17 department categories (was grey-heavy with 2 colours).

### Changed
- **Nav order**: `Insights · Your Taxes · Budget Galaxy · Explore & Compare · Budget Recipients · About`. Budget Galaxy remains default landing. Explore & Compare moved *before* Budget Recipients per user.
- Explore tab switched from 2-column compare to master-detail. `_cmplistRender_legacy` preserved for deep-link backwards-compat.
- Budget Galaxy borrowing node made always-legible (fixed min height, red tint, always-shown label, explicit tooltip) after it visually "shrank" at high salaries under proportional Sankey scaling.
- Fixed 2017 vs 2024 Health department name drift (DoH single bucket vs NHS Provider Sector split-out) in Insight #6 calculation.

### Fixed
- Tax ladder bracket numbers recomputed from verifier (multiple NI gaps in earlier draft).
- PSNB 2000-01 sign flip (was +£15.6B deficit; actual −£15.2B surplus).
- Insight #11: "Kensington & Chelsea 3rd-lowest English Band D" was wrong — K&C is £1,529, City of London is the lowest. Caught only via programmatic audit. Count of English councils above Scotland's highest corrected from 293 to 291.
- Insight #15 council count: 401 → 423 (353 principal + 40 police + 30 fire). Year label: "2024" → "fiscal 2023-24".
- SHA256 of `uk_tax_bands.json` refreshed (stale hash in earlier draft).
- Unified duplicate "Hillingdon" nodes in Sankey into single `council_user` with two inputs (CT + grant-share).
- Galaxy breadcrumb overlap with UK header at root depth.

## [Unreleased] - 2026-04-16 — UK supplier metadata to 65.2% MHCLG

### Added
- 23 new councils with supplier-level `_top_suppliers` metadata
  - Wave 1 (Met Districts): Kirklees, Knowsley, Oldham, St Helens, Wigan, Sefton, Rotherham, Bolton, Stockport, Wolverhampton, Wirral, Sandwell, Walsall, Sunderland, S Tyneside, Salford (16 councils, commits 986383f → 81cc14f)
  - Wave 2 (ad-hoc): North Tyneside via legacy subdomain (9/12 months, commit 1e9c7eb)
  - Wave 3: Wakefield, Bury (Wayback), North Somerset (commit bef4bf9)
  - Wave 4 (Unitaries): N Northants, Worcestershire, Cheshire West, W Berkshire, Bracknell Forest, Isles of Scilly (commit 06a7036)
- `£100M sanity cap` in build_council_spend_lookup.js — rejects pair-reversal entries that otherwise inflate totals (negative-drop + positive-keep asymmetry)
- `MBC` and `METROPOLITAN DISTRICT COUNCIL` strip rules in inject_council_spend_metadata.js normalizer
- Wakefield alias in NAME_ALIASES

### Changed
- Coverage: 19.7% → 46.7% → 56.5% → **65.2% MHCLG** (£85.8B / £131.6B)
- Lookup entries: 28 → 87 → **110**
- Service nodes with metadata: 920 → **986**
- Bury MBC CSVs hand-normalized via sed (10 months had 5 variants of Dept column name)

### Known issues (next session)
- Worcestershire CC £873M in only 2 services (under-classified — 46 patterns insufficient)
- Cheshire West £430M in only 6 services (same issue — 6 patterns)
- Bolton MBC £16M vs £613M MHCLG node (wrong source file or missing data)
- Westmorland & Furness dropped `blocker=red` — needs 4-stream preprocessor for legacy councils

## [2.1.0] - 2026-04-06

### Added
- Mobile responsive layout (3 breakpoints: 900px, 768px, 480px)
- Touch support: pinch-to-zoom and drag pan for Galaxy and Multiverse
- Touch-friendly tap targets for all interactive elements
- SEO: meta tags, Open Graph, Twitter cards, JSON-LD structured data
- SEO: `/sitemap.xml` and `/robots.txt` endpoints
- Dynamic page title updates on country switch
- GitHub Sponsors integration (FUNDING.yml)

### Changed
- Externalized programme enrichments to per-country JSON files (HTML: 1.85MB -> 0.45MB)
- Enrichments now load on-demand via fetch() when switching countries
- API serves `/data/` directory as static files for enrichment JSONs

## [2.0.0] - 2026-04-05

### Added
- Multiverse: all 4 countries in one zoomable SVG, normalized to USD
- United States budget data (2017-2025, ~5,500 accounts/year)
- France budget data (2020-2025, ~1,200 programmes/year)
- United Kingdom budget data (2020-2024, ~800 items/year)
- 4,035 programme-level enrichments (US: 2,410, FR: 974, UK: 651)
- 33 ministry-level enrichments with key figures and notable facts
- Country switcher in header (Globe ALL, DE, US, FR, UK)
- Spending type breakdown for 14 US agencies
- Multi-country Budget Evolution with country-specific event annotations
- Year picker for Budget Explorer across all countries

### Changed
- Renamed project from "German Budget Galaxy" to "Budget Galaxy"
- Architecture: removed PostgreSQL, now uses static JSON tree files
- API: added `/budget/country/{id}` endpoints for multi-country support

## [1.0.0] - 2026-03-15

### Added
- Budget Galaxy: D3.js circle packing with semantic zoom
- Budget Explorer: hierarchical navigation with breadcrumbs
- Budget Evolution: Chart.js multi-year line charts (2015-2025)
- 75 enriched German budget nodes with beneficiary data, OECD/NATO comparisons
- Bilingual DE/EN support with 300+ translations
- Landing page with galaxy background
- Share button with URL state encoding
- Galaxy sidebar with tree navigation
- Search functionality within Galaxy view
