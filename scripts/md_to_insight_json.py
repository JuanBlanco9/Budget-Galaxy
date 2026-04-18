#!/usr/bin/env python3
"""
md_to_insight_json.py — Parse data/insights/PILOT_15_VERIFIED.md into
per-insight JSON files + an index.

The markdown follows a consistent structure (one section per insight):

    ## N. Title
    **Category**: `cat` · **Tags**: `#a` `#b`
    ### Narrative
    <markdown body>
    ### Viz
    <viz spec>
    ### What now?
    - 🔍 **Label** → description
    ### Sources
    - 🔗 Publisher name · [text](url)
    - 📂 `path/to/file` · SHA256 `hash…`
    ### Related
    `id1`, `id2`, `id3`

Output:
    data/insights/{category}/{id}.json  (one per insight)
    data/insights/_index.json            (list: id, title, category, tags, order)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'data' / 'insights' / 'PILOT_15_VERIFIED.md'
OUT_DIR = ROOT / 'data' / 'insights'


# ---- Category → emoji mapping ----
CATEGORY_META = {
    'tax':        {'label': 'Tax', 'emoji': '💰'},
    'evolution':  {'label': 'Evolution', 'emoji': '📈'},
    'recipients': {'label': 'Recipients', 'emoji': '🏢'},
    'councils':   {'label': 'Councils', 'emoji': '🏛'},
    'structure':  {'label': 'Structure', 'emoji': '🔀'},
}


# ---- ID derivation: stable slug from title ----
def slugify(title):
    s = title.lower()
    s = re.sub(r'[^a-z0-9]+', '_', s)
    s = re.sub(r'_+', '_', s).strip('_')
    # Cap at 50 chars
    return s[:50]


# ---- Hand-authored IDs to match the related-links already in the markdown ----
# The markdown uses symbolic IDs like `scotland_vs_ruk_2024`; we mint consistent
# ones per insight based on content, locking them here for referential integrity.
EXPLICIT_IDS = {
    1:  'tax_ladder_ruk_2024',
    2:  'scotland_vs_ruk_2024',
    3:  'indirect_tax_by_decile',
    4:  'hmrc_receipts_composition_2005_2024',
    5:  'psnb_trajectory_2000_2022',
    6:  'dept_real_terms_2017_2024',
    7:  'central_gov_supplier_concentration_2024',
    8:  'ubo_resolution_summary',
    9:  'supplier_incorporation_years',
    10: 'band_d_distribution_english_2024',
    11: 'band_d_scotland_vs_england_2024',
    12: 'council_central_grant_dependency',
    13: 'hmrc_composition_2024_25',
    14: 'per_household_borrowing',
    15: 'la_net_current_expenditure_composition',
}


def parse_markdown(md):
    """Parse the markdown into a list of insight records."""
    # Insight sections begin at '## N. ' where N is 1–15.
    # Split by lines of the form '## <num>. <title>'.
    parts = re.split(r'\n## (\d+)\. ', md)
    # parts[0] is preamble; thereafter alternating number + body pairs.
    insights = []
    for i in range(1, len(parts) - 1, 2):
        number = int(parts[i])
        body = parts[i + 1]
        # Title is the first line
        lines = body.split('\n', 1)
        title = lines[0].strip()
        rest = lines[1] if len(lines) > 1 else ''
        insights.append(parse_insight_body(number, title, rest))
    return insights


def _extract_section(body, header_re):
    """Extract text of one ### section until the next ### or ##."""
    m = re.search(header_re, body)
    if not m:
        return ''
    start = m.end()
    # Find the next heading (### or ##) — or end of body
    stop_m = re.search(r'\n###? ', body[start:])
    end = start + stop_m.start() if stop_m else len(body)
    return body[start:end].strip()


def _parse_actions(text):
    """Parse the What now? bullet list into structured actions."""
    out = []
    for raw in re.findall(r'-\s+(.+?)(?:\n|$)', text):
        # Form: "🔍 **Label** → description" or "🔍 **Label** → `/#path`"
        em_m = re.match(r'([^\s*]+)\s+\*\*([^*]+)\*\*\s*(?:→|->)?\s*(.*)', raw)
        if em_m:
            icon, label, target = em_m.groups()
            out.append({
                'icon': icon.strip(),
                'label': label.strip(),
                'target': target.strip().strip('`'),
            })
    return out


def _parse_sources(text):
    """Parse the Sources bullet list."""
    out = []
    for raw in re.findall(r'-\s+(.+?)(?:\n|$)', text):
        # Publisher form: "🔗 [Publisher name] · [text](url)"
        m = re.match(r'🔗\s*(?:\*\*[^*]+\*\*\s*·\s*)?(.+?)\s*·\s*\[([^\]]+)\]\(([^)]+)\)', raw)
        if m:
            _, desc, url = m.groups()
            out.append({'type': 'publisher', 'description': desc.strip(), 'url': url})
            continue
        # File form: "📂 `path/to/file` · SHA256 `hash…`" or just file
        m = re.match(r'📂\s*(?:\*\*[^*]+\*\*\s*·\s*)?`([^`]+)`\s*(?:·\s*SHA256\s*`([^`]+)`)?', raw)
        if m:
            path, sha = m.groups()
            entry = {'type': 'our_file', 'path': path}
            if sha: entry['sha256_head'] = sha
            out.append(entry)
            continue
        # Manifest / methodology form
        m = re.match(r'(📋|🔧)\s*(.+)', raw)
        if m:
            icon, body = m.groups()
            out.append({
                'type': 'manifest' if icon == '📋' else 'methodology',
                'description': body.strip(),
            })
            continue
        # Generic fallback
        if raw.strip():
            out.append({'type': 'other', 'description': raw.strip()})
    return out


def _parse_related(text):
    """Parse the Related bullet list (backtick-wrapped IDs)."""
    return [m.strip() for m in re.findall(r'`([^`]+)`', text)]


def _parse_category_tags(body):
    m = re.search(r'\*\*Category\*\*:\s*`([^`]+)`\s*·\s*\*\*Tags\*\*:\s*((?:`#[^`]+`\s*)+)', body)
    if not m:
        return None, []
    cat = m.group(1).strip()
    tags = [t.strip('`') for t in re.findall(r'`(#[^`]+)`', m.group(2))]
    return cat, tags


def parse_insight_body(number, title, body):
    cat, tags = _parse_category_tags(body)
    narrative = _extract_section(body, r'### Narrative\n')
    viz = _extract_section(body, r'### Viz\n')
    actions_text = _extract_section(body, r'### What now\?\n')
    sources_text = _extract_section(body, r'### Sources\n')
    related_text = _extract_section(body, r'### Related\n')

    return {
        'id': EXPLICIT_IDS.get(number, f'insight_{number}'),
        'order': number,
        'title': title,
        'category': cat or 'unknown',
        'category_meta': CATEGORY_META.get(cat, {}),
        'tags': tags,
        'narrative_md': narrative,
        'viz_spec': viz,
        'actions': _parse_actions(actions_text),
        'sources': _parse_sources(sources_text),
        'related': _parse_related(related_text),
        'source_markdown_section': f'## {number}. {title}',
        'last_updated': '2026-04-18',
        'human_reviewed': True,  # user approved after 2 audit passes
    }


def main():
    with open(SRC, 'r', encoding='utf-8') as f:
        md = f.read()

    insights = parse_markdown(md)
    assert len(insights) == 15, f'Expected 15 insights, got {len(insights)}'

    # Write per-category JSON files
    for ins in insights:
        cat = ins['category']
        target_dir = OUT_DIR / cat
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / f'{ins["id"]}.json'
        with open(target, 'w', encoding='utf-8') as f:
            json.dump(ins, f, indent=2, ensure_ascii=False)
        print(f'  wrote {target.relative_to(ROOT)}')

    # Write the index
    index = {
        'generated': '2026-04-18',
        'total': len(insights),
        'categories': {},
    }
    for ins in insights:
        c = ins['category']
        if c not in index['categories']:
            index['categories'][c] = {
                'label': CATEGORY_META.get(c, {}).get('label', c.title()),
                'emoji': CATEGORY_META.get(c, {}).get('emoji', '•'),
                'items': [],
            }
        index['categories'][c]['items'].append({
            'id': ins['id'],
            'order': ins['order'],
            'title': ins['title'],
            'tags': ins['tags'],
        })
    # Sort items within each category by order
    for c in index['categories'].values():
        c['items'].sort(key=lambda x: x['order'])

    idx_path = OUT_DIR / '_index.json'
    with open(idx_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    print(f'\nIndex: {idx_path.relative_to(ROOT)}')
    for cat, data in index['categories'].items():
        print(f'  {data["emoji"]} {data["label"]:12s} — {len(data["items"])} insights')


if __name__ == '__main__':
    main()
