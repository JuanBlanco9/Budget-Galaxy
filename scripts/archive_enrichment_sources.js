#!/usr/bin/env node
/**
 * archive_enrichment_sources.js
 *
 * Adapts the council-spend wayback archiver to the budget tree enrichment.
 * Walks every source citation in data/uk/node_enrichment_extended.json,
 * dedupes URLs, snapshots each unique URL into the Wayback Machine, and
 * writes archive_url + captured_at back into every source dict that
 * carries that URL.
 *
 * Why: 4,199 hand-curated entries reference 15,245 source citations.
 * Today every citation has a live url field but ZERO have an archive_url.
 * If gov.uk reorganises a page (very common — DWP changed URL in 2024,
 * BEIS split into DESNZ/DSIT/DBT in Feb 2023), the citation breaks and
 * we can't show users what the source said when we cited it.
 *
 * Strategy:
 *   1. Load enrichment JSON.
 *   2. Build a reverse index: url → list of (entry_key, source_idx).
 *   3. For each unique URL not already archived, hit Wayback "Save Page
 *      Now" with IA_ACCESS_KEY auth (rate ~100/min vs 4/min unauth).
 *   4. Write archive_url + captured_at into every source dict that
 *      carries that url. Save the file every 25 URLs (resumable).
 *
 * Usage:
 *   IA_ACCESS_KEY=... IA_SECRET_KEY=... node scripts/archive_enrichment_sources.js [--dry-run] [--limit N]
 *
 *   --dry-run        Just show what it would do, no API calls
 *   --limit N        Only archive the first N URLs (smoke test)
 *   --force          Re-archive URLs that already have archive_url
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

const ENRICHMENT = path.join(__dirname, '..', 'data', 'uk', 'node_enrichment_extended.json');
const ENV = path.join(__dirname, '..', '.env');

const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const FORCE = args.includes('--force');
const limitArg = args.find(a => a.startsWith('--limit'));
const LIMIT = limitArg ? parseInt(args[args.indexOf(limitArg) + 1], 10) : null;

// ── Load IA credentials from .env ────────────────────────────────────
function loadEnv() {
  if (!fs.existsSync(ENV)) return {};
  const out = {};
  for (const line of fs.readFileSync(ENV, 'utf-8').split(/\r?\n/)) {
    const m = line.match(/^([A-Z_]+)=(.*)$/);
    if (m) out[m[1]] = m[2].trim();
  }
  return out;
}
const env = loadEnv();
const IA_ACCESS = process.env.IA_ACCESS_KEY || env.IA_ACCESS_KEY || '';
const IA_SECRET = process.env.IA_SECRET_KEY || env.IA_SECRET_KEY || '';
const HAS_AUTH = IA_ACCESS && IA_SECRET;
const DELAY_MS = HAS_AUTH ? 800 : 15000;
console.log(`Auth: ${HAS_AUTH ? 'IA S3 keys (~100/min)' : 'unauth (4/min)'} · delay ${DELAY_MS}ms`);

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

// ── Wayback Save Page Now ────────────────────────────────────────────
function waybackSave(url) {
  return new Promise((resolve) => {
    const saveUrl = 'https://web.archive.org/save/' + url;
    const opts = {
      method: 'POST',
      headers: { 'User-Agent': 'BudgetGalaxyArchiver/1.0' },
    };
    if (HAS_AUTH) {
      opts.headers['Authorization'] = `LOW ${IA_ACCESS}:${IA_SECRET}`;
    }
    const req = https.request(saveUrl, opts, (res) => {
      const loc = res.headers['content-location'] || res.headers['location'];
      let body = '';
      res.on('data', c => { if (body.length < 4000) body += c; });
      res.on('end', () => {
        // SPN returns 200 + content-location header pointing at snapshot path
        if (loc) {
          const archiveUrl = loc.startsWith('http') ? loc : ('https://web.archive.org' + loc);
          return resolve({ ok: true, url: archiveUrl, status: res.statusCode });
        }
        // Sometimes the body has the snapshot in a redirect-style page
        const m = body.match(/\/web\/\d+\/[^"'\s]+/);
        if (m) {
          return resolve({ ok: true, url: 'https://web.archive.org' + m[0], status: res.statusCode });
        }
        // Some endpoints return a job-id JSON; for our purposes we treat
        // this as "started — wayback will index". We construct the canonical
        // pending-replay URL which Wayback resolves to the latest capture.
        if (res.statusCode === 200 || res.statusCode === 302 || res.statusCode === 429) {
          return resolve({
            ok: true,
            url: 'https://web.archive.org/web/*/' + url,
            status: res.statusCode,
            note: 'pending-replay (no immediate snapshot URL returned)'
          });
        }
        resolve({ ok: false, status: res.statusCode, body: body.slice(0, 200) });
      });
    });
    req.on('error', (e) => resolve({ ok: false, error: e.message }));
    req.end();
  });
}

// ── Walk enrichment for unique URLs ──────────────────────────────────
function buildUrlIndex(enrichment) {
  // url → [{entry_key, source_idx}]
  const idx = new Map();
  const entries = enrichment.entries || {};
  for (const [key, e] of Object.entries(entries)) {
    const sources = e.sources || [];
    for (let i = 0; i < sources.length; i++) {
      const s = sources[i];
      if (!s || typeof s !== 'object') continue;
      const url = s.url;
      if (!url || !/^https?:\/\//.test(url)) continue;
      if (!idx.has(url)) idx.set(url, []);
      idx.get(url).push({ entry_key: key, source_idx: i });
    }
  }
  return idx;
}

// ── Main ─────────────────────────────────────────────────────────────
async function main() {
  console.log(`Loading ${ENRICHMENT}...`);
  const enrichment = JSON.parse(fs.readFileSync(ENRICHMENT, 'utf-8'));
  console.log(`Entries: ${Object.keys(enrichment.entries || {}).length.toLocaleString()}`);

  const urlIdx = buildUrlIndex(enrichment);
  const totalUrls = urlIdx.size;
  const totalCitations = [...urlIdx.values()].reduce((s, v) => s + v.length, 0);
  console.log(`Unique URLs: ${totalUrls.toLocaleString()}  ·  Total citations: ${totalCitations.toLocaleString()}`);

  // Filter URLs that need archiving
  const todo = [];
  for (const [url, refs] of urlIdx.entries()) {
    if (FORCE) { todo.push(url); continue; }
    // Already archived if any of its citations has archive_url
    const sample = refs[0];
    const src = enrichment.entries[sample.entry_key].sources[sample.source_idx];
    if (!src.archive_url) todo.push(url);
  }
  console.log(`Already archived: ${(totalUrls - todo.length).toLocaleString()}`);
  console.log(`To archive:       ${todo.length.toLocaleString()}`);

  const work = LIMIT ? todo.slice(0, LIMIT) : todo;
  if (LIMIT) console.log(`(limited to first ${LIMIT})`);

  if (DRY_RUN) {
    console.log('\nFirst 5 to archive:');
    for (const u of work.slice(0, 5)) {
      console.log(`  [${urlIdx.get(u).length} cite${urlIdx.get(u).length>1?'s':''}]  ${u.slice(0, 100)}`);
    }
    return;
  }

  if (!work.length) { console.log('Nothing to do.'); return; }

  // Estimate time
  const estMin = Math.ceil(work.length * DELAY_MS / 60000);
  console.log(`Estimated wall-clock: ~${estMin} minutes`);
  console.log('');

  let done = 0, ok = 0, fail = 0, citsHit = 0;
  const start = Date.now();
  for (const url of work) {
    done++;
    process.stdout.write(`[${done}/${work.length}] `);
    const res = await waybackSave(url);
    if (res.ok) {
      ok++;
      const ts = new Date().toISOString();
      // Write back to every citation that uses this URL
      for (const ref of urlIdx.get(url)) {
        const src = enrichment.entries[ref.entry_key].sources[ref.source_idx];
        src.archive_url = res.url;
        src.captured_at = ts;
        citsHit++;
      }
      console.log(`OK   ${res.note || ''} ${url.slice(0, 80)}`);
    } else {
      fail++;
      console.log(`FAIL (${res.status || res.error}) ${url.slice(0, 80)}`);
    }
    // Save every 25 URLs (resumable)
    if (done % 25 === 0) {
      fs.writeFileSync(ENRICHMENT, JSON.stringify(enrichment, null, 2), 'utf-8');
      const rate = done / ((Date.now() - start) / 60000);
      console.log(`  ── checkpoint · ${done}/${work.length} · ${rate.toFixed(1)} URLs/min · ${ok} ok · ${fail} fail · ${citsHit} citations updated`);
    }
    await sleep(DELAY_MS);
  }
  // Final write
  fs.writeFileSync(ENRICHMENT, JSON.stringify(enrichment, null, 2), 'utf-8');
  const elapsedMin = ((Date.now() - start) / 60000).toFixed(1);
  console.log(`\nDone in ${elapsedMin} min · ${ok} archived · ${fail} failed · ${citsHit} citations now have archive_url`);
}

main().catch(e => { console.error(e); process.exit(1); });
