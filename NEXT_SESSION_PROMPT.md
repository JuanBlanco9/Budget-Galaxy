# Budget Galaxy — Next Session prompt

## 🚨 READ FIRST — Latest state 2026-04-21

**Full handoff**: `SESSION_HANDOFF_2026_04_21.md` (in repo root). Read that FIRST, it has everything.

**Short version:**
- Branch `claude/mystifying-ardinghelli-f4e66f` · last commit `80f37ed`
- **2,621 Tier A entries** · **82.12% tailor-made per-entity** (not the 99.117% figure you might see in audit output — that one counts anything that "resolves", including 6,948 sub-items absorbing parent content)
- User mandate: 100% tailor-made per-entity · no cut corners · pace batches 4-5 agents max · rate limits reset 2pm + 7pm Buenos Aires
- **6,948 shared-parent orphan nodes remain** — user saw this visually (Social Fund - Cold Weather / Community Care / Net Lending all showing same COFOG parent content)
- Fact-check is PENDING — I (previous Claude) did structural verification only, not factual. User explicitly flagged this.
- Depth-4 work 60% done: ✅ Salaries & wages · Agency · Pensions · Depreciation · ❌ Drugs, Clinical supplies, Premises (other), Establishment, PFI, Transport, Business rates, Amortisation, Impairments, Lease, Termination, Inventories, Other (~2,250 entries)

**Live production is NOT up to date**: production (budgetgalaxy.com) is at commit `7126451` era. Last 3 commits (depth-4 work) are committed locally but NOT deployed.

---

## 🔖 OLDER STATE — 2026-04-20 (paused mid-Sprint-4)

**52 Tier A gold entries**. Sprint 4a complete in JSON.

**Just shipped (last session)**: Sprint 3 (DESNZ + DCMS + DSIT + DEFRA) + Academies-Pre-16/Offset + Sprint 4a (MoD 2.1 Military defence · 7.A Medical services multi-nation · Financial Assistance to Other Institutions £71B mystery bucket decoded). All verified with 3 agents catching my own brief errors (CB6 78% not 68% · gambling GGY £15.6B not £27B · academies 82% not 52% secondary).

**Next steps queued (not started)**:
- **Sprint 4b**: B-compact → gold upgrades (8 items): NHS Commissioning Board £63B · MHCLG Local Gov £34B · Dept of Health (NHS) £14B · Nuclear Decommissioning Authority £13.5B · MHCLG Communities £8B · BBC £7.7B · National Highways £7B · Office for Students £3.2B
- **Sprint 4c**: DWP benefit lines falling to Tier D: Housing Benefit £8.5B · DLA £7.7B · ESA combined £12B · New State Pension (Excluding Protected Payments) £46B
- **Sprint 4d**: COFOG-code alias overrides (10.1 Sickness → PIP/DLA/ESA · 9.4 Tertiary → HE Funding · 9.5 Education → Schools Block · 3.3 Courts · 3.4 Prisons)
- **Post-launch**: FCDO + DBT + Cabinet Office (3 remaining top-level depts)

**Live**: dev server FastAPI en `localhost:8765` (process may still be running — `py -m uvicorn api.main:app --host 127.0.0.1 --port 8765`)

**Verifier**: `py scripts/verify_enrichment.py` · **Subdivision audit**: `py scripts/audit_subdivisions.py`

---



Paste this as your first message to Claude:

---

Continuamos Budget Galaxy. **Semana de lanzamiento.** Frontend prácticamente listo; quedan acabados finales y QA en producción.

Working directory: `D:\germany-ngo-map`
Repo: https://github.com/JuanBlanco9/Budget-Galaxy → `main`
Producción: Vultr Atlanta `96.30.199.112` → `https://budgetgalaxy.com`
Handoff completo: `PROJECT_HANDOFF.md` (leer primero)

## Estado al 2026-04-18 (fin de sesión)

### Frontend — ya shippeado
- **Nav actual**: `💡 Insights · 💰 Your Taxes · 🌌 Budget Galaxy · 📊 Explore & Compare · 🏢 Budget Recipients · About`
  - Budget Galaxy sigue siendo landing por defecto.
  - Explore & Compare movido **antes** de Budget Recipients (pedido del usuario).
- **Insights tab** (`tab-insights`): 15 findings editoriales, 5 categorías (tax · evolution · recipients · councils · structure). Todos verificados por 2 pasadas de auditoría + script Python (`scripts/verify_insights.py`). Data en `data/insights/` (un JSON por insight + `_index.json`). Generador: `scripts/md_to_insight_json.py` desde `PILOT_15_VERIFIED.md`.
- **Your Taxes tab**: Honest Taxpayer Slider con cálculo IT + NI + IVA + council tax, Sankey flow, per-council trace, URL hash deep-linking (`#taxpayer/s/.../j/r/...`).
- **Budget Galaxy**: colores ampliados (70 hues, 17 categorías), borrowing-node legible, breadcrumb fix.
- **Budget Recipients**: 402 perfiles de supplier enriquecidos con UBO resolution.
- **Explore & Compare (rebuilt hoy)**: master-detail layout (tree sidebar 340px + detail panel). Ya NO es columnas compare — es navegación persistente tipo Recipients.
  - **Enriquecimiento any-depth (hoy)**: cada nodo a cualquier profundidad muestra sparkline 10-year (si hay match), Δ y/y, Δ 5y, % of UK, % of parent, per-capita chip, "Where this line sits" con porcentajes de cada ancestor, composition bar, sub-items con sparklines inline.
  - **Source attribution (hoy)**: cada nodo tiene footer de fuente con chain de resolución:
    1. `_source` propio del nodo
    2. `_source` del ancestor más cercano
    3. Fallback por branch: Local Gov → MHCLG RO5 · NHS Provider Sector → NHS TAC · Scottish Gov → gov.scot · Welsh → gov.wales · NI → finance-ni.gov.uk · resto → **HMT OSCAR II**
    4. URL link al publisher + exp_codes/sta_codes como chips · aviso amarillo si `_estimated_source_year`
  - Funciones clave (todas nuevas hoy): `_cmplistResolveSource`, `_cmplistBranchDefault`, `_cmplistSourceFooter`, `_cmplistAncestorNames`, `_UK_SOURCE_URLS`.

### UK data
- **86.54% MHCLG coverage** (167/411 councils, £122.61B / £141.68B) — sin cambios desde 2026-04-17.
- Tree en vivo: `data/uk/uk_budget_tree_2024.json` (16.09 MB).
- 1488 service nodes con `_top_suppliers`, 96.7% con `top_purposes`.

## TODO para la semana de lanzamiento (ordenado por prioridad)

### P0 — Smoke test pre-launch (1-2h)
1. **Deploy + hard-refresh + full smoke test** de las 6 tabs en producción.
2. **Verificar todos los deep-links**: `#insights/{cat}/{id}`, `#suppliers/{CH}`, `#taxpayer/s/.../j/r/...`, `#galaxy`.
3. **Source resolver sanity**: clickear 8-10 nodos random en Explore & Compare + Galaxy (mezcla de depths 1-5, mezcla de branches: DWP, Local Gov, NHS, Scottish). Confirmar que el footer de fuente sale correcto para cada uno.
4. **Chart hover test**: abrir un nodo con history (ej. "DEPARTMENT FOR WORK AND PENSIONS"). Pasar el mouse por el chart. Verificar que el tooltip aparece con `año · valor · %y/y`.
5. **Mobile**: revisar 3 breakpoints (900/768/480) en tabs nuevos (Insights, Your Taxes, Explore master-detail).
6. **Activar monitoring**:
   - Sign-up en plausible.io · setear `BG_MONITOR.plausibleDomain = 'budgetgalaxy.com'` en el `<head>`
   - Sign-up en sentry.io · crear proyecto "browser-js" · copiar DSN · setear `BG_MONITOR.sentryDsn = 'https://...@....ingest.sentry.io/...'`
   - Redeploy
   - Abrir la app en incógnito → verificar en Plausible "1 visitor" y en Sentry "session healthy"

### P1 — Acabados frontend
1. **Per-capita tooltip**: el chip nuevo dice "£X / person" — verificar que el title attribute con la pop muestra bien.
2. **Insights cross-refs**: los `related: [...]` IDs apuntan correctamente, pero no hay UI todavía para saltar entre insights relacionados. Agregar chips clickeables al final de cada insight.
3. **SEO final pass**: meta tags por tab, structured data para insights.
4. **Real-terms lens**: activar la opción "Real £" en Explore — necesita GDP deflator series (HMT deflators table). Backend simple: dividir nominal por deflator(year).
5. **% GDP lens**: activar — necesita OBR 2024-25 GDP (~£2.7T nominal).

### P2 — Data (post-launch si hay tiempo)
- **UK VPS prioridades** (si se compra Hetzner London €4/mo) — ver sección antigua abajo.
- **Real-terms lens**: necesita deflator series (GDP deflator HMT), para activar "Show as: real £" en Explore.
- **% GDP lens**: necesita OBR 2024-25 GDP number (~£2.7T nominal).

### P2.5 — Expandir el editorial-enrichment layer

**Arquitectura ya shippeada**. Tres-archivo loader en `_cmplistLoadEnrichment()`:

1. `data/uk/program_enrichment.json` — **779 entries, compact schema** `{y, d, b}` (ya existía, ahora surfaceado)
2. `data/uk/enrichment_top50.json` — **651 entries, rich schema** (ya existía, ahora surfaceado)
3. `data/uk/node_enrichment_extended.json` — **25 entries hand-curated con `key_stats[]` + `sources[]`** (escrito 2026-04-18 desde 5 research-agent batches)

**Cómo agregar más entries**: editá `node_enrichment_extended.json`. Schema:

```json
"NODE_NAME_IN_TREE": {
  "description": "2-3 sentence plain-English lede",
  "beneficiaries": "Who + how many (shown in green banner)",
  "legal_basis": "Act / statutory framework",
  "key_stats": [
    {"label": "Staff", "value": "1.35M FTE"},
    {"label": "Beds", "value": "~163,000"}
  ],
  "notes": "Why it matters / recent change / controversy (yellow banner)",
  "sources": [
    {"publisher": "NHS England", "title": "Trust Accounts Consolidation 2023-24", "url": "https://..."}
  ]
}
```

El key debe ser el nombre RAW del tree (case-sensitive). Pretty-name + normalised-fallback matching ya funciona; si una entry no aparece, el renderer cae al compact/rich layer automáticamente.

**Cómo lanzar research batches** (para escribir las próximas 25-50 entradas):

1. Pickear 8-10 nodos temáticos (ej: Top 10 DfE programmes, Top 10 MoJ, Top 10 Transport).
2. Lanzar research agent con el prompt template de esta sesión (ver memoria del 2026-04-18):
   - "You are a researcher for Budget Galaxy. Research ONLY — return markdown sections with: What it is · Beneficiaries · Scale stats · Per-unit economics · Legal basis · Recent change · Notable controversy · Sources"
   - Listar los 8-10 items.
   - Priority sources específicos al dominio (DfE stats / MoJ tribunal stats / DfT road stats).
3. Sintetizar findings → JSON entries → append al `node_enrichment_extended.json`.

**Batches pendientes sugeridos** (prioridad post-launch):
- DfE programmes: Schools · Student Loans · Pupil Premium · Early Years · FE · Apprenticeships · SEN · Teacher Pensions
- DfT: Rail subsidies · HS2 · National Highways · Bus Services · Active Travel · Cycling
- MoJ: Prisons · Courts · Probation · Legal Aid · Youth Justice · CAFCASS
- Home Office: Police Core Grant · Border Force · Asylum · Counter-Terrorism · Drugs
- Council services × 13 MHCLG categories (Adult SC, Children's SC, Public Health, Transport, Housing, Planning, etc.)
- Top 30 NHS trusts by value (need data from our `_top_suppliers` joined with NHS TAC)

Meta objetivo: **100 entries totales post-launch** para cubrir ~80% de clicks esperables.

### P3 — Backlog ideas del usuario
- Policy editorial paragraphs on Insights (un párrafo de "so what" por insight, separado del narrative técnico).
- Cross-link Insights ↔ Explore (al clickear una cifra en un insight, abrir el nodo exacto en Explore).
- Animaciones de transición en Galaxy zoom-out.

### v1.1 — post-launch (explícitamente diferido)

**Split del `frontend/index.html` de 15k líneas** — hoy el archivo tiene ~15400 líneas: HTML + CSS + 9 bloques de JS + 1 bloque de structured-data JSON-LD. Todo funciona pero mantenerlo es doloroso.

Plan propuesto (NO antes de launch; hacerlo después de que los primeros 500 users rompan cosas):

```
frontend/
  index.html          # ~500 lines: shell, meta, link tags
  css/
    base.css          # tokens, reset, typography
    tabs.css          # .panel, .tabs, layout
    galaxy.css        # galaxy-specific
    taxpayer.css      # your taxes
    explore.css       # master-detail
    insights.css
    suppliers.css
  js/
    app.js            # entry, showTab, init
    galaxy.js         # d3 force hierarchy
    taxpayer.js       # sankey + calculator wiring
    explore.js        # tree + detail + sources
    insights.js
    suppliers.js
    monitoring.js     # BG_MONITOR bootstrap
  tax/                # (unchanged — already split)
    uk_calc.js
    uk_vat.js
    uk_council_tax.js
    uk_trace.js
```

Sin build step: solo `<script src="...">` por módulo. Orden de load importante (globals) pero manejable.

Riesgos: (a) hash-fragment deep-links dependen de timing de init — hay que preservar el orden actual de carga; (b) varias `window._*` globals se comparten entre "módulos" — una pasada de grep antes de mover.

**UK VPS (Hetzner London €4/mo)** para los 13.5% MHCLG faltantes (ver sección archivo abajo). +5-7pp coverage esperado.

## Archivos clave modificados hoy

```
frontend/index.html
  + CSS: .detail-ancestors, .detail-source, .detail-pc-chip (líneas ~1336-1395)
  + JS: _cmplistResolveSource, _cmplistBranchDefault, _cmplistSourceFooter,
        _cmplistAncestorNames, _UK_SOURCE_URLS (líneas ~13057-13180)
  + _cmplistRenderDetail reescrito para any-depth enrichment
  + _cmplistSubitem rows con sparklines any-depth
  + Tab reorder: explore antes de suppliers (línea 1075)

data/insights/_index.json + 15 subfolder JSONs
scripts/md_to_insight_json.py
scripts/verify_insights.py
data/insights/PILOT_15_VERIFIED.md
```

## Comandos rápidos

```bash
# Deploy current frontend
scp frontend/index.html root@96.30.199.112:/opt/germany-ngo-map/frontend/

# Verify tree is fresh
md5sum data/uk/uk_budget_tree_2024.json
ssh root@96.30.199.112 "md5sum /opt/germany-ngo-map/data/uk/uk_budget_tree_2024.json"

# Regenerate insights JSONs from markdown
py scripts/md_to_insight_json.py

# Re-verify insight numbers against data files
py scripts/verify_insights.py
```

---

## Archivo — techo UK VPS (sin cambios desde 2026-04-17)

Los councils restantes grandes que necesitan UK VPS:
- Dorset £721M · Northumberland £604M · Tameside £486M · Blackburn £348M
- PCCs grandes: GMP £923M, West Midlands £892M, West Yorkshire £672M, Thames Valley £650M
- Oxfordshire partial (4/12 shippeados, 8 meses faltan)

Si se compra Hetzner London €4/mo:
```bash
ssh root@{HETZNER_IP} "curl -sL -A 'Mozilla/5.0' -o /tmp/{council}.csv '{URL}'"
scp root@{HETZNER_IP}:/tmp/{council}.csv data/uk/local_authorities/spend/{council}/
```
Lanzar 6 agentes paralelos para discovery. ~+5-7pp MHCLG esperado si todos dan hit.

## Descubrimientos reusables (consolidados)

1. **SharePoint download.aspx rewrite**: `/:x:/s/{site}/{TOKEN}` → `/sites/{site}/_layouts/15/download.aspx?share={TOKEN}`
2. **Wayback if_/id_ replay**: `web.archive.org/web/2025id_/{url}` para geo-blocked
3. **Wayback Save Page Now con IA S3 auth**: para councils sin snapshots
4. **Vultr Miami proxy**: para Incapsula WAFs que bloquean AR pero permiten US
5. **Manifest re-audit green/yellow**: ROI alto sobre "never built"
6. **Parallel 6-agent batches**: 75% hit rate probado
7. **Drupal /jsonapi + /document-search?field_document_target_id={term}**
8. **WordPress customfilter AJAX**: Somerset pattern (POST admin-ajax.php)
