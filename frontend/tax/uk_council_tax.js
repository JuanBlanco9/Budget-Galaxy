/* Budget Galaxy — UK Council Tax lookup.
 *
 * Given a council name (or ONS code or E code) and a band (A-H), return the
 * annual Council Tax bill for that dwelling. Uses MHCLG's published
 * "area council tax by band" — the all-in value that residents actually pay
 * (billing authority + county + GLA + police + fire + parish).
 *
 * Usage:
 *   await UKCouncilTax.load();
 *   const bill = UKCouncilTax.lookup({ council: 'Hillingdon', band: 'D' });
 *   // → { council, band: 'D', amount_gbp: 1850.66, year: '2024-25' }
 */
(function (global) {
  'use strict';

  let _data = null;

  async function load(opts) {
    if (_data) return _data;
    const o = (typeof opts === 'string') ? { englandUrl: opts } : (opts || {});
    const englandUrl = o.englandUrl || '/data/uk/fiscal/council_tax/uk_council_tax_2024_25.json';
    const scotlandUrl = o.scotlandUrl || '/data/uk/fiscal/council_tax/scotland_council_tax_2024_25.json';
    const [eng, sco] = await Promise.all([
      fetch(englandUrl).then(r => r.ok ? r.json() : null).catch(() => null),
      fetch(scotlandUrl).then(r => r.ok ? r.json() : null).catch(() => null),
    ]);
    const merged = { ...(eng || {}), councils: [] };
    if (eng && eng.councils) merged.councils = merged.councils.concat(eng.councils);
    if (sco && sco.councils) {
      // Tag jurisdiction on each Scottish council so UI can display flag/hint
      const scoTagged = sco.councils.map(c => ({ ...c, jurisdiction: 'scotland' }));
      merged.councils = merged.councils.concat(scoTagged);
    }
    merged.england = eng;
    merged.scotland = sco;
    _data = merged;
    return _data;
  }

  function setData(d) { _data = d; }
  function setDataMerged(england, scotland) {
    const merged = { ...(england || {}), councils: [] };
    if (england && england.councils) merged.councils = merged.councils.concat(england.councils);
    if (scotland && scotland.councils) {
      merged.councils = merged.councils.concat(
        scotland.councils.map(c => ({ ...c, jurisdiction: 'scotland' }))
      );
    }
    merged.england = england;
    merged.scotland = scotland;
    _data = merged;
  }

  function _normalise(s) {
    return String(s || '')
      .toLowerCase()
      .replace(/\bcouncil\b/g, '')
      .replace(/\bborough\b/g, '')
      .replace(/\bcity of\b/g, '')
      .replace(/\bcity\b/g, '')
      .replace(/\bmetropolitan\b/g, '')
      .replace(/\bdistrict\b/g, '')
      .replace(/\bcounty\b/g, '')
      .replace(/&/g, 'and')
      .replace(/\s+/g, ' ')
      .trim();
  }

  /** Find a council record by: ONS code ('E09000017'), E-code ('E5020'), or name. */
  function findCouncil(identifier) {
    if (!_data) throw new Error('UKCouncilTax: call load() first');
    const id = String(identifier || '').trim();
    if (!id) return null;
    const councils = _data.councils;

    // Exact ONS / E code match
    for (const c of councils) {
      if (c.ons_code === id || c.e_code === id) return c;
    }
    // Exact name match
    for (const c of councils) {
      if (c.name === id) return c;
    }
    // Normalised name match
    const nid = _normalise(id);
    for (const c of councils) {
      if (_normalise(c.name) === nid) return c;
    }
    // Substring (fuzzy)
    for (const c of councils) {
      const cn = _normalise(c.name);
      if (cn.includes(nid) || nid.includes(cn)) return c;
    }
    return null;
  }

  function listCouncils() {
    if (!_data) throw new Error('UKCouncilTax: call load() first');
    return _data.councils.map(c => ({
      name: c.name,
      ons_code: c.ons_code,
      region_code: c.region_code,
      band_D: c.band_D,
    }));
  }

  /** opts: { council, band }  band defaults to 'D'. */
  function lookup(opts) {
    const c = findCouncil(opts.council);
    if (!c) return null;
    const band = String(opts.band || 'D').toUpperCase();
    if (!/^[A-H]$/.test(band)) throw new Error(`Invalid band: ${band}`);
    const amount = c[`band_${band}`];
    if (amount == null) return null;
    return {
      council_name: c.name,
      ons_code: c.ons_code,
      region_code: c.region_code,
      jurisdiction: c.jurisdiction || 'england',
      band,
      amount_gbp: amount,
      fiscal_year_label: _data.fiscal_year_label,
      all_bands: 'ABCDEFGH'.split('').reduce((acc, b) => {
        acc[b] = c[`band_${b}`] ?? null;
        return acc;
      }, {}),
    };
  }

  function listCouncilsFor(jurisdiction) {
    if (!_data) throw new Error('UKCouncilTax: call load() first');
    const j = (jurisdiction || 'rUK').toLowerCase();
    return _data.councils
      .filter(c => j === 'scotland'
        ? c.jurisdiction === 'scotland'
        : c.jurisdiction !== 'scotland')
      .map(c => ({
        name: c.name,
        ons_code: c.ons_code,
        region_code: c.region_code,
        jurisdiction: c.jurisdiction || 'england',
        band_D: c.band_D,
      }));
  }

  const api = { load, setData, setDataMerged, lookup, findCouncil, listCouncils, listCouncilsFor };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = api;
  } else {
    global.UKCouncilTax = api;
  }
})(typeof globalThis !== 'undefined' ? globalThis : this);
