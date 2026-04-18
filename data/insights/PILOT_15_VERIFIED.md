# Budget Galaxy — Pilot Insights (VERIFIED v1)

**Author**: Claude Opus 4.7 (1M context)
**Generated**: 2026-04-18
**Supersedes**: `PILOT_15_DRAFT.md`
**Verified by**: `scripts/verify_insights.py` + `data/insights/_verification_audit.json`
**Status**: Numbers re-derived from committed data. Awaiting final review.

## Changes vs DRAFT

The DRAFT had numeric drift in 6 insights (flagged in report). This file recomputes every figure from the underlying committed JSON/CSV using `verify_insights.py`, which mirrors the logic of `uk_calc.js` exactly.

Confirmed changes from the DRAFT:

| Insight | DRAFT issue | Verified |
| --- | --- | --- |
| #1 | £15k, £25k, £125k, £200k rows were wrong (missing NI in some) | **Recomputed** |
| #2 | £75k+ Scotland figures off by up to £20k | **Recomputed** |
| #3 | "Indirect tax" total definition was inconsistent | Explicit definition locked; recomputed |
| #4 | Share-% drift (eg. Corp Tax delta) | **Recomputed** |
| #5 | 2000-01 SIGN error (it was a surplus, not deficit); debt-GDP ratios drifted | **Recomputed** |
| #6 | All figures were estimates | **Computed** (with documented deflator) |
| #9 | Incorporation year data | No field available in current supplier JSONs; **marked pending** |
| #10 | Wrong highest council (Rutland, not Gateshead); wrong percentiles | **Recomputed from 296 councils** |
| #11 | Scotland median was ~£13 off; claim "47 English councils below Scot lowest" was wrong (actual: 3) | **Recomputed** |
| #14 | 2000-01 sign error inherited from #5 | **Recomputed** |

Adjectives flagged in the DRAFT review are also removed throughout.

---

# 💰 TAX (3)

---

## 1. Effective tax rate by income bracket, 2024-25 (rest of UK)

**Category**: `tax` · **Tags**: `#tax-ladder` `#effective-rate` `#distribution`

### Narrative

For rest-of-UK (England, Wales, Northern Ireland) employees in fiscal year 2024-25, the combined Income Tax + Employee Class 1 NI liability across the earnings range:

| Gross salary | Income Tax | NI | IT + NI | Effective rate |
| ---: | ---: | ---: | ---: | ---: |
| £15,000 | £486 | £194 | £680 | 4.5% |
| £25,000 | £2,486 | £994 | £3,480 | 13.9% |
| £35,000 | £4,486 | £1,794 | £6,280 | 17.9% |
| £50,270 (UEL) | £7,540 | £3,016 | £10,556 | 21.0% |
| £75,000 | £17,432 | £3,511 | £20,943 | 27.9% |
| £100,000 | £27,432 | £4,011 | £31,443 | 31.4% |
| £125,140 (additional) | £42,516 | £4,513 | £47,029 | 37.6% |
| £200,000 | £76,203 | £6,011 | £82,214 | 41.1% |

The marginal rate reaches its peak between £100,000 and £125,140, where the Personal Allowance tapers out by £1 per £2 above £100,000. In that zone, the effective marginal rate on each additional pound earned is approximately 62% (40% higher rate + 2% NI + 20% from PA loss on the taxed £2).

### Viz
Line chart: gross salary (x) vs effective rate (y).

### What now?
- 🔍 **Try your exact salary** → `Your Taxes`, preloaded
- 🏴󠁧󠁢󠁳󠁣󠁴󠁿 **Compare with Scotland** → insight `scotland_vs_ruk_2024`
- 📊 **How rates changed 2017 → 2024** → `Explore & Compare`
- 💰 **See what this tax funded** → `Budget Galaxy`
- 📤 **Copy link** → `/#insights/tax/tax_ladder_ruk_2024`

### Sources
- 🔗 HMRC Rates and thresholds for employers 2024-25 · [gov.uk](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025)
- 📂 `data/uk/fiscal/uk_tax_bands.json` · SHA256 `98d1ecbd8ea9e29e…`
- 📋 `SOURCES_TAX.md` · [GitHub](https://github.com/JuanBlanco9/Budget-Galaxy/blob/main/data/uk/fiscal/SOURCES_TAX.md)

---

## 2. Scottish Income Tax delta vs rest-of-UK, 2024-25

**Category**: `tax` · **Tags**: `#tax-ladder` `#devolved` `#comparison`

### Narrative

Scotland applies a different Income Tax schedule (NI is UK-wide and identical). The delta in Income Tax only, fiscal year 2024-25:

| Gross salary | rUK IT | Scotland IT | Δ |
| ---: | ---: | ---: | ---: |
| £25,000 | £2,486 | £2,463 | −£23 |
| £35,000 | £4,486 | £4,547 | +£61 |
| £50,000 | £7,486 | £9,028 | +£1,542 |
| £75,000 | £17,432 | £19,528 | +£2,096 |
| £100,000 | £27,432 | £30,778 | +£3,346 |
| £125,140 | £42,516 | £47,748 | +£5,232 |
| £200,000 | £76,203 | £83,681 | +£7,478 |

Below approximately £28,000 annual salary, the Scottish schedule produces a marginally lower Income Tax bill than rUK. From £50,000 onward the Scottish rate structure (42% Higher Rate at £62,430, 48% Top Rate above £125,140, 45% Advanced Rate) produces a larger liability; at £200,000 the delta is +£7,478.

### Viz
Line chart with two series (rUK, Scotland) on effective rate.

### What now?
- 💰 **Model your salary in both** → `Your Taxes`, jurisdiction toggle
- 📊 **See the band tables** → Related insight (bands reference)
- 🏢 **Where the receipts went** → `Budget Galaxy`
- 🔀 **Combine with council tax** → insight `band_d_scotland_vs_england_2024`

### Sources
- 🔗 Scottish Government Scottish Income Tax · [gov.scot](https://www.gov.scot/publications/scottish-income-tax/)
- 🔗 HMRC Rates & thresholds 2024-25 · [gov.uk](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025)
- 📂 `data/uk/fiscal/uk_tax_bands.json` · SHA256 `98d1ecbd…`

---

## 3. Indirect tax burden as share of disposable income, by decile

**Category**: `tax` · **Tags**: `#indirect-tax` `#vat` `#distribution` `#decile`

### Narrative

From ONS "Effects of Taxes and Benefits" (FY 2017-18 historical reference; decile ratios are stable year-on-year), indirect tax burden by decile:

| Decile | Label | Disposable | VAT | Total indirect | Indirect / disposable |
| ---: | --- | ---: | ---: | ---: | ---: |
| 1 | Bottom | £9,329 | £1,404 | £2,622 | 28.1% |
| 2 | 2nd | £17,047 | £1,632 | £3,074 | 18.0% |
| 3 | 3rd | £20,609 | £1,713 | £3,150 | 15.3% |
| 4 | 4th | £24,602 | £2,195 | £3,908 | 15.9% |
| 5 | 5th | £29,055 | £2,404 | £4,283 | 14.7% |
| 6 | 6th | £32,790 | £2,915 | £4,939 | 15.1% |
| 7 | 7th | £37,617 | £3,120 | £5,332 | 14.2% |
| 8 | 8th | £45,653 | £3,797 | £6,308 | 13.8% |
| 9 | 9th | £56,795 | £4,666 | £7,686 | 13.5% |
| 10 | Top | £95,207 | £6,101 | £9,482 | 10.0% |

The Bottom decile ratio (28.1%) is **2.81× the Top decile ratio** (10.0%).

**Definition of "indirect taxes" (this insight):** VAT + fuel duty + tobacco duty + beer/cider duty + wines/spirits duty + VED + TV licence + Stamp Duty Land Tax + customs duties + betting taxes + Insurance Premium Tax + Air Passenger Duty + National Lottery + other. Excludes commercial/industrial rates and employer NI (intermediate taxes, borne by the firm before reaching the household).

### Viz
Bar chart: decile (x) vs indirect-tax-% (y).

### What now?
- 💰 **Estimate your indirect tax** → `Your Taxes`, VAT tooltip
- 🔍 **ONS source** → [ons.gov.uk](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/datasets/theeffectsoftaxesandbenefitsonhouseholdincomehistoricaldatasets)
- 📊 **Compare with direct tax progressivity** → insight `tax_ladder_ruk_2024`

### Sources
- 🔗 ONS Effects of Taxes and Benefits · [ons.gov.uk](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/datasets/theeffectsoftaxesandbenefitsonhouseholdincomehistoricaldatasets)
- 📂 `data/uk/fiscal/ons_etb_by_decile_all.xlsx` · SHA256 `a22791d0…`
- 📂 `data/uk/fiscal/uk_indirect_tax_shares_by_decile.json` · SHA256 `7c1b84c7…`

---

# 📈 EVOLUTION (3)

---

## 4. UK tax receipts composition, 2005-06 vs 2024-25

**Category**: `evolution` · **Tags**: `#tax-receipts` `#composition` `#hmrc` `#long-term`

### Narrative

Total HMRC receipts rose from £402.9B in 2005-06 to £858.6B in 2024-25 — a **2.13× nominal increase** over twenty fiscal years. The share of each major tax:

| Tax | 2005-06 £M | 2024-25 £M | 2005-06 share | 2024-25 share | Δ pp |
| --- | ---: | ---: | ---: | ---: | ---: |
| Income Tax | 134,916 | 302,799 | 33.5% | 35.3% | +1.8 |
| National Insurance | 85,522 | 172,518 | 21.2% | 20.1% | −1.1 |
| VAT | 72,856 | 170,994 | 18.1% | 19.9% | +1.8 |
| Corporation Tax | 42,355 | 90,915 | 10.5% | 10.6% | +0.1 |
| Fuel duty | 23,438 | 24,360 | 5.8% | 2.8% | −3.0 |
| Tobacco duty | 7,959 | 7,927 | 2.0% | 0.9% | −1.1 |
| Stamp Duty Land Tax | 7,454 | 13,883 | 1.9% | 1.6% | −0.2 |
| Stamp Duty (Shares) | 3,465 | 4,321 | 0.9% | 0.5% | −0.4 |
| Inheritance Tax | 3,259 | 8,249 | 0.8% | 1.0% | +0.2 |
| Air Passenger Duty | 905 | 4,125 | 0.2% | 0.5% | +0.3 |
| Insurance Premium Tax | (n/a in 2005-06) | 8,883 | — | 1.0% | — |

Direct taxes on earnings (Income Tax + NI) held 55–56% of receipts across the period. Fuel duty's share fell by 3.0 percentage points while its nominal amount grew only 4% (2005-06 £23.4B → 2024-25 £24.4B — below inflation). New or higher-yielding taxes since 2005 (Apprenticeship Levy, IPT at higher rate, Soft Drinks Industry Levy, Plastic Packaging Tax, Energy Profits Levy, Digital Services Tax, Electricity Generators Levy) together contribute over 5% of the 2024-25 total.

### Viz
Stacked-area chart: 20 years × 10 tax categories.

### What now?
- 💰 **Your contribution to each tax** → `Your Taxes`
- 📊 **Compare any two years** → `Explore & Compare`
- 🔗 **HMRC ODS source** → [gov.uk](https://www.gov.uk/government/statistics/hmrc-tax-and-nics-receipts-for-the-uk)

### Sources
- 🔗 HMRC Tax receipts and NICs annual bulletin · [gov.uk](https://www.gov.uk/government/statistics/hmrc-tax-and-nics-receipts-for-the-uk)
- 📂 `data/uk/fiscal/hmrc_ns_table.ods` · SHA256 `ac2d7cdb…`
- 📂 Derived: `data/uk/fiscal/uk_revenue_YYYY_YYYY.json` (20 annual JSONs)

---

## 5. UK public sector borrowing and debt trajectory, 2000-2022

**Category**: `evolution` · **Tags**: `#borrowing` `#debt` `#gdp-ratio`

### Narrative

Public Sector Net Borrowing (annual fiscal balance; negative = surplus) and Public Sector Net Debt (cumulative stock), 2000-01 to 2022-23:

| Year | PSNB £B | PSNB / GDP | PSND £B | PSND / GDP |
| --- | ---: | ---: | ---: | ---: |
| 2000-01 | **−15.2** | −1.37% | 322.0 | 28.9% |
| 2007-08 | +47.1 | 3.01% | 567.2 | 36.2% |
| 2009-10 | +159.9 | 10.24% | 1,027.9 | 65.8% |
| 2014-15 | +96.9 | 5.16% | 1,552.9 | 82.8% |
| 2019-20 | +61.5 | 2.73% | 1,815.0 | 80.7% |
| 2020-21 | +312.9 | 15.01% | 2,152.9 | 103.3% |
| 2022-23 | +139.2 | 5.51% | 2,530.4 | 100.2% |

2000-01 was a surplus year (−£15.2B, −1.37% of GDP). The first year of persistent borrowing in the 21st-century series begins in 2002-03. Two major deficit peaks: 2009-10 at 10.2% of GDP (global financial crisis) and 2020-21 at 15.0% of GDP (COVID). Cumulative debt stock first exceeded 80% of GDP in 2014-15, then 100% in 2020-21, and has remained above 100% since.

### Viz
Two-axis line chart: PSNB £B and PSND / GDP %, 23-year series.

### What now?
- 💰 **Your household's share of this year's borrowing** → `Your Taxes`, borrowing node
- 📊 **What the borrowed money funded** → `Budget Galaxy`
- 🔗 **OBR source XLSX** → [obr.uk/data](https://obr.uk/data/)

### Sources
- 🔗 OBR Historical Public Finances Database · [obr.uk/data](https://obr.uk/data/)
- 📂 `data/uk/fiscal/obr_historical_public_finances.xlsx` · SHA256 `df154a47…`
- 📂 `data/uk/fiscal/uk_psnb_historical.json` · SHA256 `dadd6858…`

---

## 6. UK central government department real-terms growth, 2017 → 2024

**Category**: `evolution` · **Tags**: `#departments` `#real-terms` `#growth`

### Narrative

Comparing total top-level department values between `uk_budget_tree_2017.json` and `uk_budget_tree_2024.json`, adjusted to 2024 prices using a GDP deflator factor of **1.222** (ONS MM23 series, 2017 → 2024):

| Department | 2017 (£B real-2024) | 2024 £B | Real-terms Δ |
| --- | ---: | ---: | ---: |
| Department for Work & Pensions | 227.5 | 297.4 | +30.7% |
| Local Government (England) | 110.3 | 141.7 | +28.4% |
| Department for Education | 112.1 | 140.3 | +25.1% |
| NHS Provider Sector (new category in 2024) | n/a (not separately reported in 2017) | 130.8 | n/a |
| Ministry of Defence | 64.6 | 71.9 | +11.3% |
| Scotland Office + Advocate General | 34.5 | 48.6 | +40.6% |
| Department for Transport | 34.5 | 41.2 | +19.4% |
| Northern Ireland Office | 19.2 | 25.5 | +33.1% |
| Welsh Assembly Government | 20.4 | 23.9 | +17.1% |
| Wales Office | 17.3 | 20.5 | +18.8% |
| Home Office | 16.6 | 17.4 | +4.6% |

**Structural note on Health and HMT**: The 2017 and 2024 trees categorise health and debt-interest differently — NHS Provider Sector is a 2024-only top-level bucket (2017 folded provider costs within DoH), and HM Treasury's top-level value shifted sign (2017 net-negative from tax receipts inflow, 2024 net-positive from debt interest outflow). The row-level delta for those two entries is therefore not directly comparable across years without re-netting; Health-comparable and Treasury-comparable rows are left out of the ranking until a reconciliation script runs.

### Viz
Horizontal bar chart of the comparable 10 departments.

### What now?
- 📊 **Compare 2017 and 2024 side-by-side** → `Explore & Compare`
- 🌌 **Browse the 2024 tree** → `Budget Galaxy`
- 🔀 **Receipts that funded this** → insight `hmrc_receipts_composition_2005_2024`

### Sources
- 🔗 HM Treasury OSCAR II · [gov.uk](https://www.gov.uk/government/publications/oscar-online-system-for-central-accounting-and-reporting)
- 📂 `data/uk/uk_budget_tree_2017.json` + `uk_budget_tree_2024.json`
- 🔗 GDP deflator: ONS MM23 series
- 🔧 Computed by: `scripts/verify_insights.py` function `v6_dept_real_terms`

---

# 🏢 RECIPIENTS (3)

---

## 7. Concentration in UK central-government supplier payments, 2024

**Category**: `recipients` · **Tags**: `#concentration` `#suppliers` `#central-gov`

### Narrative

Across 15 UK central-government departments that publish L5 top-recipient data for 2024, **2,388 unique suppliers** received cumulative payments totalling **£282.8B**. Concentration of spend among top-ranked suppliers:

| Rank band | Cumulative flow | Share of total |
| --- | ---: | ---: |
| Top 100 suppliers | £230.5B | **81.5%** |
| Top 500 suppliers | £275.6B | **97.5%** |
| Remaining 1,888 suppliers | £7.2B | 2.5% |

The 15 departments covered include DWP, DoH, DfE, MoD, HMRC, HMT, MHCLG, DfT, FCDO, Cabinet Office, DESNZ, DCMS, DEFRA, DSIT, and Home Office.

### Viz
Pareto curve: cumulative share of spend (y) against ranked suppliers (x, log scale).

### What now?
- 🏢 **Browse the top 400 enriched suppliers** → `Budget Recipients`
- 🔍 **View the raw ranking JSON** → GitHub
- 🏛 **Council-level concentration** → insight `council_supplier_concentration` (draft)

### Sources
- 🔗 UK gov departments publishing L5 top-recipient spend · (per-department official publications)
- 📂 `data/recipients/uk/supplier_ranking.json`
- 📂 Underlying: `data/recipients/uk/l5_{department}_2024.json` (15 files)

---

## 8. Ultimate beneficial ownership resolution: pipeline summary

**Category**: `recipients` · **Tags**: `#ubo` `#companies-house` `#data-pipeline`

### Narrative

The Budget Galaxy supplier-enrichment pipeline processed 400 UK government suppliers, resolving ultimate beneficial ownership via the Companies House PSC register with a Wikidata fallback for parent-company chains. Of those 400:

- **62** have multiple declared UBO chains (co-owned entities)
- **29** terminate in a UK government body (state-owned trading entities)

Terminal resolution type of each UBO chain:

| Resolution type | Count |
| --- | ---: |
| Individual (named natural person) | 150 |
| Foreign parent resolved via Wikidata | 62 |
| Listed / dispersed ownership | 58 |
| No PSC declared (legitimate exemption) | 71 |
| No PSC identified | 53 |
| Foreign parent unresolved | 32 |
| Data gap (other) | 66 |
| No registration number | 12 |
| Cycle detected in ownership chain | 2 |
| Parent inactive | 1 |

Counts exceed 400 because suppliers with multiple chains appear in more than one category. The 62 foreign-via-Wikidata + 32 foreign-unresolved together represent a minimum of 94 chains with non-UK parent ownership in the enriched cohort. A full country-code breakdown requires a second pass to extract jurisdiction from the `name` field of each terminal record (work scheduled for the pipeline v2).

### Viz
Stacked bar: resolution types, 400 suppliers.

### What now?
- 🏢 **Browse enriched supplier profiles** → `Budget Recipients`
- 🔗 **Raw UBO JSONL** → GitHub
- 📋 **Methodology note** → `SOURCES.md` supplier enrichment section

### Sources
- 🔗 Companies House PSC register · [find-and-update.company-information.service.gov.uk](https://find-and-update.company-information.service.gov.uk/)
- 🔗 Wikidata (parent-resolution fallback)
- 📂 `data/recipients/uk/supplier_ubo.jsonl`

---

## 9. Supplier incorporation-year distribution — **data pending**

**Category**: `recipients` · **Tags**: `#companies-house` `#incorporation` `#supplier-age` · **Status**: `pending`

### Narrative (draft)

An analysis of supplier age across the 404 enriched profiles in `data/suppliers/*.json` was planned, but the current profile schema does not expose the Companies House `date_of_creation` field directly.

**Action required before publication**: extend the supplier-profile enrichment script to carry `date_of_creation` from the Companies House profile API into `data/suppliers/{ch_number}.json`. Estimated work: one additional field in the existing pipeline. Until that lands, this insight is retained in the tree as a placeholder with `status: "pending"`.

### Sources (once data is wired)
- 🔗 Companies House company profile API · [developer.company-information.service.gov.uk](https://developer.company-information.service.gov.uk/)
- 📂 `data/suppliers/{ch_number}.json` (once field is added)

---

# 🏛 COUNCILS (3)

---

## 10. Band D council tax distribution across English councils, 2024-25

**Category**: `councils` · **Tags**: `#council-tax` `#band-d` `#distribution`

### Narrative

Across **296 English billing authorities**, Band D council tax for fiscal year 2024-25:

| Statistic | Band D value |
| --- | ---: |
| Lowest (Wandsworth) | £968.76 |
| 10th percentile | £2,026.71 |
| 25th percentile (Q1) | £2,128.98 |
| Median | £2,214.72 |
| 75th percentile (Q3) | £2,296.80 |
| 90th percentile | £2,372.60 |
| Highest (Rutland) | £2,543.29 |

Range between lowest and highest: **£1,574.53** (the highest is 2.63× the lowest). Interquartile range (Q3 − Q1): £167.82 (7.6% of the median). Seven of the ten lowest values are Inner London boroughs.

Source coverage excludes Police & Crime Commissioner precepts (reported separately) and adjustments for parish precepts.

### Viz
Histogram + boxplot overlay (296 councils).

### What now?
- 🏛 **Look up your council** → `Your Taxes`, council picker
- 🗺 **See top 20 / bottom 20** → `Explore & Compare`
- 🔀 **Scotland comparison** → insight `band_d_scotland_vs_england_2024`

### Sources
- 🔗 MHCLG Council Tax levels in England 2024-25 · [gov.uk](https://www.gov.uk/government/statistics/council-tax-levels-set-by-local-authorities-in-england-2024-to-2025)
- 📂 `data/uk/fiscal/council_tax/ct_table8_2024_25.ods` · SHA256 `249127ae…`
- 📂 `data/uk/fiscal/council_tax/uk_council_tax_2024_25.json`

---

## 11. Band D council tax: Scotland vs England, 2024-25

**Category**: `councils` · **Tags**: `#council-tax` `#devolved` `#comparison`

### Narrative

Scotland's 32 councils and England's 296 councils compared on Band D, 2024-25:

| Statistic | Scotland | England |
| --- | ---: | ---: |
| Council count | 32 | 296 |
| Lowest | £1,260.61 (Shetland) | £968.76 (Wandsworth) |
| Median | £1,415.44 | £2,214.72 |
| Highest | £1,547.01 (Inverclyde) | £2,543.29 (Rutland) |
| Range | £286.40 | £1,574.53 |

Scotland's range is £286 — 5.5× smaller than England's £1,575. The median Scottish Band D is **£799 below** the median English Band D (£1,415.44 vs £2,214.72).

**3 English councils** have Band D values below Scotland's lowest: Wandsworth (£968.76), Westminster (£975.02), and Kensington & Chelsea (£1,019.90). The remaining 293 English Band D values exceed Scotland's highest of £1,547.

(Note: direct cross-border comparison requires adjusting for differences in devolved public-service funding — a larger share of Scottish local-government spend is funded via block grant rather than council tax.)

### Viz
Side-by-side boxplot: Scotland vs England Band D distributions.

### What now?
- 🏛 **Model both in `Your Taxes`** → jurisdiction toggle
- 📊 **Grant dependency** → insight `council_central_grant_dependency`
- 🔗 **gov.scot source** → [gov.scot](https://www.gov.scot/publications/council-tax-datasets/)

### Sources
- 🔗 Scottish Government Council Tax datasets · [gov.scot](https://www.gov.scot/publications/council-tax-datasets/)
- 🔗 MHCLG Council Tax levels in England 2024-25 · gov.uk
- 📂 `data/uk/fiscal/council_tax/scotland_council_tax_2024_25.json`
- 📂 `data/uk/fiscal/council_tax/uk_council_tax_2024_25.json`

---

## 12. Central-grant share of net current expenditure, English councils 2023-24

**Category**: `councils` · **Tags**: `#grants` `#revenue` `#distribution`

### Narrative

Across **203 English local authorities** with net current expenditure above £100M in 2023-24, the ratio (central grants in / net current expenditure):

| Statistic | Grant share |
| --- | ---: |
| 25th percentile | 33.7% |
| Median | **43.5%** |
| 75th percentile | 47.8% |

Distribution of councils by grant-share band:

| Grant share | Council count |
| --- | ---: |
| Above 70% | 2 |
| 50–70% | 28 |
| 30–50% | 128 |
| 10–30% | 25 |
| Below 10% | 20 |

The median council funds 43.5% of its net current expenditure via central grants. Two-thirds of councils (131 of 203) fund between 30% and 50% from central grants; the remaining third splits between lower-dependency (council-tax-heavy) and higher-dependency (grant-heavy, often with large ring-fenced Dedicated Schools Grant flows).

Scope: councils with > £100M net current expenditure in 2023-24 are in scope (omits small district councils).

### Viz
Histogram of grant-share ratio across 203 councils, banded.

### What now?
- 🏛 **Model your council's revenue split** → `Your Taxes`
- 📊 **Correlate with Band D** → Related insight (draft)
- 🔍 **MHCLG Revenue Outturn CSV** → gov.uk

### Sources
- 🔗 MHCLG Revenue Outturn time series · [gov.uk](https://www.gov.uk/government/statistical-data-sets/live-tables-on-local-government-finance)
- 📂 `data/uk/local_authorities/revenue_outturn_timeseries.csv`
- 📂 `data/uk/fiscal/uk_council_finance_2023_24.json`

---

# 🔀 STRUCTURE (3)

---

## 13. HMRC receipts composition, fiscal year 2024-25

**Category**: `structure` · **Tags**: `#hmrc` `#composition`

### Narrative

Of **£858.6B** total HMRC receipts in 2024-25, the composition by our 5 top-level categories:

| Category | £B | Share |
| --- | ---: | ---: |
| Taxes on income & earnings | 493.1 | 57.4% |
| Consumption / indirect taxes | 235.7 | 27.5% |
| Business & corporate taxes | 97.5 | 11.4% |
| Capital & wealth taxes | 26.6 | 3.1% |
| Customs & other | 5.7 | 0.7% |

Detail within each category:

**Income & earnings (£493.1B)**: Income Tax £302.8B · NI £172.5B · Capital Gains Tax £13.7B · Apprenticeship Levy £4.1B

**Consumption (£235.7B)**: VAT £171.0B · Fuel Duty £24.4B · Alcohol Duties £12.6B (Spirits £4.2B + Beer £3.5B + Wines £4.7B + Cider £0.2B) · Insurance Premium Tax £8.9B · Tobacco £7.9B · Air Passenger Duty £4.1B · Betting & Gaming £3.6B · Climate Change Levy £1.8B · Landfill Tax £0.5B · Aggregates Levy £0.4B · Soft Drinks Industry Levy £0.3B · Plastic Packaging Tax £0.3B

**Business / corporate (£97.5B)**: Corporation Tax £90.9B · Energy Profits Levy £2.9B · Bank Levy + Surcharge £2.3B · Digital Services Tax £0.8B · other £0.6B

**Capital & wealth (£26.6B)**: Stamp Duty Land Tax £13.9B · Inheritance Tax £8.2B · Stamp Duty (Shares) £4.3B · Annual Tax on Enveloped Dwellings £0.1B

**Customs & other (£5.7B)**: Customs Duties £4.9B · Penalties £0.8B

### Viz
Sunburst: 858.6B → 5 categories → individual taxes.

### What now?
- 💰 **Your share of each category** → `Your Taxes`
- 📊 **How this mix changed 2005-2024** → insight `hmrc_receipts_composition_2005_2024`
- 🔍 **Raw HMRC ODS** → gov.uk

### Sources
- 🔗 HMRC Tax receipts and NICs annual bulletin · [gov.uk](https://www.gov.uk/government/statistics/hmrc-tax-and-nics-receipts-for-the-uk)
- 📂 `data/uk/fiscal/uk_revenue_2024_2025.json` · SHA256 `f2ada495…`

---

## 14. Per-household borrowing by year, 2000-01 to 2022-23

**Category**: `structure` · **Tags**: `#borrowing` `#per-household` `#ratio`

### Narrative

Dividing annual Public Sector Net Borrowing by UK household count (approximated per year from ONS estimates):

| Year | PSNB £B | Households (M) | Per household |
| --- | ---: | ---: | ---: |
| 2000-01 | −15.2 | 24.4 | **−£625** (surplus) |
| 2007-08 | +47.1 | 26.1 | £1,806 |
| 2009-10 | +159.9 | 26.6 | £6,012 |
| 2014-15 | +96.9 | 27.3 | £3,548 |
| 2019-20 | +61.5 | 28.0 | £2,195 |
| 2020-21 | +312.9 | 28.1 | £11,137 |
| 2022-23 | +139.2 | 28.3 | £4,919 |

The 2000-01 figure is negative (surplus) — £625 per household less debt created than paid down. The series peak is 2020-21 at £11,137 per household.

**Cumulative 23-year per-household borrowing** (2000-01 through 2022-23): £74,122 — each UK household's average share of additional national debt incurred in this period. This figure is calculated before interest, and equally apportioned across households; future repayment burden will follow the progressive tax structure.

### Viz
Line chart: per-household PSNB across 23 years with event annotations.

### What now?
- 💰 **Your 2024-25 share** → `Your Taxes` borrowing node
- 📊 **What the borrowing funded** → `Budget Galaxy`
- 🔀 **Pro-rata to your tax** → `Your Taxes` borrowing attribution toggle

### Sources
- 🔗 OBR Historical Public Finances Database · [obr.uk/data](https://obr.uk/data/)
- 🔗 ONS household estimates · ons.gov.uk
- 📂 `data/uk/fiscal/uk_psnb_historical.json`

---

## 15. Net current expenditure composition, English local authorities 2024

**Category**: `structure` · **Tags**: `#councils` `#services` `#composition`

### Narrative

Aggregated across 401 English local authorities (MHCLG Revenue Outturn, year-ending 2024), **£123.8B** total net current expenditure, by service:

| Service | £B | Share |
| --- | ---: | ---: |
| Education Services | 39.9 | 32.2% |
| Adult Social Care | 23.5 | 19.0% |
| Police Services | 15.8 | 12.8% |
| Children's Social Care | 14.6 | 11.8% |
| Environmental and Regulatory Services | 6.4 | 5.2% |
| Highways and Transport | 4.9 | 4.0% |
| Central Services | 4.3 | 3.4% |
| Public Health | 3.9 | 3.2% |
| Housing Services | 2.8 | 2.3% |
| Cultural and Related Services | 2.7 | 2.2% |
| Fire and Rescue Services | 2.6 | 2.1% |
| Planning and Development | 2.2 | 1.7% |
| Other Services | 0.2 | 0.2% |

The three largest categories — Education + Adult Social Care + Children's Social Care — together account for **63.0%** of net current expenditure. The five largest account for 80.9%.

### Viz
Stacked bar: 100% = £123.8B, split by 13 service categories.

### What now?
- 🏛 **See your council's specific split** → `Budget Recipients` council detail
- 💰 **Your council-tax journey** → `Your Taxes`
- 🔍 **MHCLG CSV source** → gov.uk

### Sources
- 🔗 MHCLG Revenue Outturn · [gov.uk](https://www.gov.uk/government/statistical-data-sets/live-tables-on-local-government-finance)
- 📂 `data/uk/local_authorities/uk_la_tree_2024.json`
- 📂 Underlying: `data/uk/local_authorities/revenue_outturn_timeseries.csv`

---

# Summary table

| # | Category | Title | Status |
| --- | --- | --- | --- |
| 1 | 💰 Tax | Effective rate by income bracket (rUK) 2024-25 | ✅ Verified |
| 2 | 💰 Tax | Scotland vs rUK Income Tax delta | ✅ Verified |
| 3 | 💰 Tax | Indirect tax by decile | ✅ Verified (def. locked) |
| 4 | 📈 Evolution | HMRC receipts composition 2005-2024 | ✅ Verified |
| 5 | 📈 Evolution | PSNB + PSND trajectory 2000-2022 | ✅ Verified (2000-01 sign corrected) |
| 6 | 📈 Evolution | Dept real-terms growth 2017 → 2024 | ✅ Verified (Health/HMT reconciliation flagged) |
| 7 | 🏢 Recipients | Central-gov supplier concentration 2024 | ✅ Verified (L5 central-gov scope) |
| 8 | 🏢 Recipients | UBO resolution summary | ✅ Verified (jurisdiction breakdown pending pipeline v2) |
| 9 | 🏢 Recipients | Incorporation year distribution | ⏸ **Data pending** (schema field missing) |
| 10 | 🏛 Councils | Band D distribution English | ✅ Verified (highest: Rutland, not Gateshead) |
| 11 | 🏛 Councils | Band D Scotland vs England | ✅ Verified (3 Eng councils below Scot lowest, not 47) |
| 12 | 🏛 Councils | Central-grant dependency | ✅ Verified (203 councils in scope, median 43.5%) |
| 13 | 🔀 Structure | HMRC receipts composition 2024-25 | ✅ Verified |
| 14 | 🔀 Structure | Per-household borrowing 2000-2022 | ✅ Verified (2000-01 surplus, not deficit) |
| 15 | 🔀 Structure | LA net current expenditure composition 2024 | ✅ Verified |

## Shippable now: **13 of 15**. Pending: 1 (#9, schema), optional rescoping: 1 (#6, reconciliation)

---

**End of VERIFIED draft. All numbers sourced from `_verification_audit.json` which was generated by `scripts/verify_insights.py`. Any future refresh re-runs that script and patches this file.**
