# Budget Galaxy — Claude Session Context

> Last session: 2026-04-22 · Branch: `claude/mystifying-ardinghelli-f4e66f`

## What is Budget Galaxy

Civic tool at **budgetgalaxy.com** that traces every £ of UK public money from your salary
(Income Tax + NI + VAT + Council Tax) down to the exact supplier that received the contract,
with source-cited data and the company's beneficial owner. No competitor does all 5 layers
(personal tax → budget tree → buyer → supplier → UBO) end-to-end.

## Stack (deliberate choices)

- **Frontend**: vanilla HTML/JS + D3 v7 + Leaflet 1.9.4 + Chart.js 4. One file: `frontend/index.html` (~25k lines).
- **Backend**: FastAPI + uvicorn on Vultr · `96.30.199.112:8088` behind nginx · SSL via Let's Encrypt
- **Data**: static JSON files served by StaticFiles. 788MB+ of precomputed public data.
- **Deploy**: `scp` (no rsync on Windows). Use `tar czf ... && scp && ssh "tar xzf"` for bulk.
- **Prod path**: `/opt/germany-ngo-map/` · start: `venv/bin/uvicorn api.main:app --host 0.0.0.0 --port 8088 --workers 2`
- **SSH key**: `~/.ssh/id_agro_intel` · user `root@96.30.199.112`

**Do NOT propose switching to React / Postgres / GraphQL.** JSON static + vanilla was
deliberate for: CDN cacheability, zero server cost, forkability (SHA256-verifiable), and
audit-friendliness. The only legitimate backend addition is a `/api/search` endpoint with
SQLite FTS for scaling supplier search past 20k entries.

## What exists today (2026-04-22)

### 5 tabs in the app
1. **Insights** — curated stories with cross-links
2. **Your Taxes** — personalized tax breakdown (slider + council + nation + year) with Sankey flow
3. **Budget Galaxy** — D3 treemap of UK budget 2015-2024
4. **Explore & Compare** — master-detail with lens selector
5. **Budget Recipients** — list + map of buyers/suppliers

### Data stack in production
| Dataset | Records | File(s) |
|---|---|---|
| UK budget trees | 2015-2024 | `data/uk/uk_budget_tree_*.json` |
| HMRC revenue trees | 2005-2025 | `data/uk/fiscal/uk_revenue_*.json` |
| Tax bands | 8 years × 2 nations | `data/uk/fiscal/uk_tax_bands.json` |
| VAT deciles | 10 × categories | `data/uk/fiscal/uk_indirect_tax_shares_by_decile.json` |
| Council Tax | 328 councils × 8 bands | `data/uk/fiscal/council_tax/` |
| Council finance | 3 years | `data/uk/fiscal/uk_council_finance_*.json` |
| PSNB historical | 20 years | `data/uk/fiscal/uk_psnb_historical.json` |
| Geocoded postcodes | 16,012 | `data/map/postcodes_cache.json` |
| OCDS contracts 2024 | 85,202 | `data/procurement/contracts_flat_2024.jsonl` |
| Aggregated buyers | 4,130 | `data/map/buyers.json` |
| Aggregated suppliers | 40,521 | `data/map/suppliers.json` |
| **Curated suppliers** (rich) | **400** | `data/suppliers/` |
| **V2 suppliers** (BCD+CH API) | **19,238** | `data/suppliers_v2/` |
| — of which CH-API enriched | ~1,500 (growing) | same dir with `ch_profile`, `governance`, `pscs`, `accounts_pdf` |

### Companies House enrichment pipeline
Three-phase pipeline in `scripts/`:
1. `enrich_bulk_01_bcd_skeletons.py` — streams BCD zip once, writes 19,068 skeleton profiles
2. `enrich_bulk_02_ch_api_batch.py` — CH API loop (profile + officers + PSCs + filing-history)
   - Rate-limited: 0.7s between calls, 15s backoff on 429
   - CLI: `--top N`, `--rank-from X --rank-to Y`, `--resume`
   - Key in `.env` as `CH_API_KEY=...`
3. `enrich_bulk_03_refresh_index.py` — rebuilds `_index.json` after batch runs so UI badges are accurate

**After any batch run, ALWAYS run script 03 before deploy** or the ENRICHED/BASIC badges will be wrong.

## Session 2026-04-22 — what we completed

1. ✅ Phase 1: 19,068 BCD skeletons written (99.1% coverage)
2. ✅ Fixed prod deploy gap: copied `frontend/tax/*.js` and `data/uk/fiscal/*` to Vultr (taxes tab was broken)
3. ✅ Wrote `_supRenderDetailV2()` in frontend — renders v2 schema with Identity, Accounts, Governance, PSCs, Spend, Sources sections
4. ✅ Day 1 CH API batch: **500/500 enriched** · 0 failures · 1,920 API calls · 45 min
5. ✅ Merged curated + v2 indexes in `loadSuppliersTab()`. Badge system: CURATED (celeste) / ENRICHED (verde) / BASIC (gris)
6. ✅ Fixed "19,123 CURATED OTHER SUPPLIERS · RICH PROFILES" label bug — now filters strictly by `_source === 'curated'`
7. ✅ Deployed: frontend/index.html + suppliers_v2/_index.json + suppliers_v2/*.json tarball (19,242 files)
8. 🔄 Day 2 running in background: `py scripts/enrich_bulk_02_ch_api_batch.py --rank-from 500 --rank-to 1500 --resume` (started ~02:00 local, ETA ~04:00)

## Open items (next session — 2026-04-23)

### Immediate
- [ ] **Check if Day 2 finished cleanly** — `python -c "import json; p=json.load(open('data/suppliers_v2/_ch_api_progress.json')); print(len(p['completed']), 'done,', len(p['failed']), 'failed')"` — expected 1,500/1,500
- [ ] **Run refresh script**: `py scripts/enrich_bulk_03_refresh_index.py` — updates `_index.json` so 1,500 suppliers get ENRICHED badge
- [ ] **Deploy updated data** to prod:
  ```bash
  cd data && tar --exclude=_ch_api_progress.json --exclude=_ch_api_state.json -czf /tmp/v2.tgz suppliers_v2
  scp -i ~/.ssh/id_agro_intel /tmp/v2.tgz root@96.30.199.112:/tmp/
  ssh -i ~/.ssh/id_agro_intel root@96.30.199.112 "cd /opt/germany-ngo-map/data && tar xzf /tmp/v2.tgz && rm /tmp/v2.tgz"
  ```

### Pending from last session
- [ ] **Day 3 batch**: `py scripts/enrich_bulk_02_ch_api_batch.py --rank-from 1500 --rank-to 3000 --resume` (~3 hours)
- [ ] **Depth-4 NHS hand-curation** (D4_04 remaining 154 + D4_05-15 ≈ 2,250 entries). See `data/uk/node_enrichment_extended.json` and existing batches for template.

### Strategic (from critique thread 2026-04-22)
User received product critique (ChatGPT-generated). Agreed with 3 of 5 points. Key directive:

> **Simplify the onboarding, not the product. The 5 layers ARE the moat; the problem is no single-flow journey.**

Next design push (when user says go):
1. **Home redesign** as single flow: salary input → tax breakdown → top recipients → supplier dossier (with Palantir example as canonical walkthrough)
2. **Ranking page** (`/rankings`): "Top 100 UK companies living off the state" · auto-generated · SEO target
3. **Nav collapse**: 5 tabs → 2 modes (Citizen / Research) with toggle

NOT a rewrite. Keep vanilla stack. Keep 5 pestañas as power-user views. Just build a different front door.

### Strategic (my own additions, not yet discussed with user)
- **Defensibility is temporal** — 6-12 months of lead before a funded competitor can replicate. Need to capture audience + SEO before then.
- **Libel risk** — if surfacing incómoda data about contractors, need clear disclaimer ("data from Companies House, we aggregate, we don't verify"), takedown process, probably liability insurance if it grows.
- **Realistic monetization**: NOT VC path. Companies House + OpenCorporates + Tussell model = freemium with paid newsroom tier (£500-2000/yr for alerts + bulk CSV + API key).
- **Operational reality**: BCD monthly; can't sustain 40k CH API refresh solo. Either snapshot-based positioning ("quarterly refresh") or a collaborator.

## Commit discipline

- Branch `claude/mystifying-ardinghelli-f4e66f` is 67+ commits ahead of `origin/main`. We've been pushing to it freely; main is the public mirror.
- `.env` (with CH_API_KEY) is gitignored and chmod 600.
- `_ch_api_progress.json` and `_ch_api_state.json` are now gitignored (added this session) — they're rewritten during batch runs.
- Co-author tag: `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`

## Git state at session handoff (2026-04-22 end-of-day)

**Commit 1 made successfully** (`fb89a3d`):
- `.gitignore` (added progress-file excludes)
- `CLAUDE.md` (this file)
- `scripts/enrich_bulk_01_bcd_skeletons.py`, `enrich_bulk_02_ch_api_batch.py`, `enrich_bulk_03_refresh_index.py`
- `frontend/index.html` (renderer v2 + index merge)

**Commit 2 NOT made — ~19,000 data files still uncommitted in working tree**:
- All `data/suppliers_v2/*.json` files (the 19,068 BCD skeletons + 500+ CH-API-enriched files from Day 1, plus growing additions from Day 2)
- `data/map/_aggregate_stats.json`
- These files **exist on disk** — they are not lost. Only the git commit of them is incomplete.

**What happened**: `git add data/suppliers_v2/` on Windows with 19k files is very slow and the shell wrapper timed out, leaving a stale `index.lock`. The lock has since been removed. A fresh `git add` can proceed in a new session.

**NOT pushed to remote**: The branch has `fb89a3d` locally but `origin/claude/mystifying-ardinghelli-f4e66f` is still at `b08a628`. No `git push` ran this session.

### To finish the handoff cleanly (first thing in next session):

```bash
cd D:/germany-ngo-map/.claude/worktrees/mystifying-ardinghelli-f4e66f

# 1. Verify no stale lock (if present, remove):
ls D:/germany-ngo-map/.git/worktrees/mystifying-ardinghelli-f4e66f/index.lock 2>/dev/null \
  && rm -f D:/germany-ngo-map/.git/worktrees/mystifying-ardinghelli-f4e66f/index.lock

# 2. If Day 2 batch still running, pause git until it finishes to avoid racing:
python -c "import json; p=json.load(open(r'data/suppliers_v2/_ch_api_progress.json')); print(f'{len(p[\"completed\"])}/1500')"

# 3. Stage data in one go (slow on Windows — can take 5-10 min with 19k files):
git add data/suppliers_v2/ data/map/_aggregate_stats.json

# 4. Commit
git commit -m "data(suppliers_v2): 19,068 BCD skeletons + 500+ CH-API-enriched profiles"

# 5. Push both commits (code + data)
git push origin claude/mystifying-ardinghelli-f4e66f
```

**Why this is NOT blocking for next session work**: The CLAUDE.md context doc loads automatically, and the data files exist on disk — the next session can read any supplier JSON, run Day 3 batch, deploy to prod, etc. without the commit being complete. Only concern is if someone else needs to clone fresh — they won't get the 19k files until commit+push happens.

**Day 2 batch status at handoff**: Running in background (last seen 840/1500 at session end, ~2h remaining). PID was owned by the session shell, so **it may have been killed when session ended** — next session MUST verify and potentially re-run with `--resume`:

```bash
# Check if still running
tasklist //FI "IMAGENAME eq py.exe" 2>/dev/null | head
# Check progress
python -c "import json; p=json.load(open(r'data/suppliers_v2/_ch_api_progress.json')); print(f'{len(p[\"completed\"])} done, {len(p[\"failed\"])} failed')"
# Resume if needed
py scripts/enrich_bulk_02_ch_api_batch.py --rank-from 500 --rank-to 1500 --resume
```

## Production endpoints that must stay healthy

| URL | Purpose | Notes |
|---|---|---|
| `/` | App root → index.html | — |
| `/data/uk/fiscal/*.json` | Tax calculator data | **Easy to forget in deploy** — always scp whole dir |
| `/tax/*.js` | Tax calculator modules | **Easy to forget in deploy** — always scp whole dir |
| `/data/map/*.json` | Buyers/suppliers aggregates | 13.3MB `suppliers.json` — keep cached |
| `/data/suppliers/{ch}.json` | Curated profiles (400) | — |
| `/data/suppliers_v2/{ch}.json` | V2 profiles (19k) | — |
| `/data/suppliers_v2/_index.json` | V2 list for UI | 8MB — regenerate after every batch |

## Command reference

```bash
# Check Day N batch progress
python -c "import json; p=json.load(open(r'data/suppliers_v2/_ch_api_progress.json')); print(f'{len(p[\"completed\"]):,} done, {len(p[\"failed\"])} failed')"

# Run next batch
py scripts/enrich_bulk_02_ch_api_batch.py --rank-from X --rank-to Y --resume

# Refresh index after batch
py scripts/enrich_bulk_03_refresh_index.py

# Deploy frontend only
scp -i ~/.ssh/id_agro_intel frontend/index.html root@96.30.199.112:/opt/germany-ngo-map/frontend/

# Deploy v2 bulk data
cd data && tar --exclude=_ch_api_progress.json --exclude=_ch_api_state.json -czf /tmp/v2.tgz suppliers_v2 \
  && scp -i ~/.ssh/id_agro_intel /tmp/v2.tgz root@96.30.199.112:/tmp/ \
  && ssh -i ~/.ssh/id_agro_intel root@96.30.199.112 "cd /opt/germany-ngo-map/data && tar xzf /tmp/v2.tgz && rm /tmp/v2.tgz"

# Restart prod server (after api/* changes)
ssh -i ~/.ssh/id_agro_intel root@96.30.199.112 "pkill -f 'uvicorn api.main:app' || true"
ssh -i ~/.ssh/id_agro_intel root@96.30.199.112 "cd /opt/germany-ngo-map && ADMIN_STATS_TOKEN=... nohup venv/bin/uvicorn api.main:app --host 0.0.0.0 --port 8088 --workers 2 > /var/log/budgetgalaxy.log 2>&1 & disown; exit 0"
```

## User preferences (important)

- **Spanish** in responses · Argentine register · direct, no-buzzword
- Values direct pushback over agreement — "te los digo sin suavizar porque acá está la diferencia entre hobby y empresa real" is the tone they want reflected
- Does not want documentation files created proactively (this CLAUDE.md was explicitly requested)
- Does not want emojis added without explicit ask
- Prefers background tasks for long operations (CH API batches, rsync-equivalents)
- Keeps commits organized but not obsessive
- Session typically ends with commit + push on their request
