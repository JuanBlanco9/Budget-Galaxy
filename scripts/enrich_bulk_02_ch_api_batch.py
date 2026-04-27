#!/usr/bin/env python3
"""Bulk enrichment phase 2: CH API lookup for officers + PSCs + accounts PDF.

Run with daily batches:
  py scripts/enrich_bulk_02_ch_api_batch.py --top 500
  py scripts/enrich_bulk_02_ch_api_batch.py --rank-from 500 --rank-to 1500
  py scripts/enrich_bulk_02_ch_api_batch.py --all --resume

Rate-limit aware: sleeps when hitting 429; resumes from where it left off.
"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

# Force UTF-8 stdout: supplier names contain en-dashes, em-dashes, accented
# chars, etc. Default Windows cp1252 crashes on those mid-pipeline.
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

ROOT = Path(__file__).resolve().parent.parent
SUPPLIERS_V2 = ROOT / "data/suppliers_v2"
INDEX_FILE = SUPPLIERS_V2 / "_index.json"
PROGRESS_FILE = SUPPLIERS_V2 / "_ch_api_progress.json"
STATE_FILE = SUPPLIERS_V2 / "_ch_api_state.json"
ENV_FILE = ROOT / ".env"

# Rate-limit: CH caps at 600 per 5min per key.
# We self-throttle well under: ~5 calls/sec → 300/min = 1500/5min but the server-side hard cap is 600.
# Be safer: 1.5 calls/sec → ~450/5min · leaves headroom.
CALL_INTERVAL = 0.7  # seconds between requests
BACKOFF_ON_429 = 15  # seconds


def load_key():
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
            if line.startswith("CH_API_KEY="):
                return line.split("=", 1)[1].strip()
    return os.environ.get("CH_API_KEY")


def ch_request(path, key):
    """GET https://api.company-information.service.gov.uk/{path} with basic auth."""
    url = "https://api.company-information.service.gov.uk" + path
    auth = base64.b64encode(f"{key}:".encode()).decode()
    req = urllib.request.Request(url, headers={"Authorization": f"Basic {auth}"})
    while True:
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.getcode(), json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 429:
                print(f"    429 rate-limited · sleeping {BACKOFF_ON_429}s…", flush=True)
                time.sleep(BACKOFF_ON_429)
                continue
            elif e.code == 404:
                return 404, None
            else:
                # 400, 500, etc — return whatever for the caller
                try:
                    body = json.loads(e.read().decode("utf-8"))
                except Exception:
                    body = None
                return e.code, body
        except Exception as e:
            print(f"    request error: {e} · retry in 5s")
            time.sleep(5)


def enrich_supplier(ch_number, key, do_officers=True, do_pscs=True, do_filing=True):
    """Fetch profile + officers + PSCs + filing history (for accounts PDF).
    Returns a dict with the new fields, plus a list of API calls made."""
    update = {}
    calls = 0

    # 1. Profile
    code, prof = ch_request(f"/company/{ch_number}", key)
    calls += 1
    if code == 200 and prof:
        update["ch_profile"] = {
            "api_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "company_name": prof.get("company_name"),
            "company_status": prof.get("company_status"),
            "date_of_creation": prof.get("date_of_creation"),
            "date_of_cessation": prof.get("date_of_cessation"),
            "jurisdiction": prof.get("jurisdiction"),
            "has_charges": prof.get("has_charges"),
            "has_insolvency_history": prof.get("has_insolvency_history"),
            "has_super_secure_pscs": prof.get("has_super_secure_pscs"),
            "accounts_overdue": (prof.get("accounts") or {}).get("overdue"),
            "accounts_next_due": (prof.get("accounts") or {}).get("next_due"),
            "accounts_last_made_up": (prof.get("accounts") or {}).get("last_accounts", {}).get("made_up_to"),
            "confirmation_statement_overdue": (prof.get("confirmation_statement") or {}).get("overdue"),
            "confirmation_statement_next_due": (prof.get("confirmation_statement") or {}).get("next_due"),
        }
        time.sleep(CALL_INTERVAL)

    # 2. Officers
    if do_officers:
        code, off = ch_request(f"/company/{ch_number}/officers?items_per_page=50", key)
        calls += 1
        if code == 200 and off:
            items = off.get("items", []) or []
            active = [i for i in items if not i.get("resigned_on")]
            update["governance"] = {
                "api_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "total_officers": off.get("total_results"),
                "active_count": off.get("active_count"),
                "resigned_count": off.get("resigned_count"),
                "active_officers": [
                    {
                        "name": i.get("name"),
                        "role": i.get("officer_role"),
                        "appointed_on": i.get("appointed_on"),
                        "country_of_residence": i.get("country_of_residence"),
                        "nationality": i.get("nationality"),
                    }
                    for i in active[:20]
                ],
            }
            time.sleep(CALL_INTERVAL)

    # 3. PSCs
    if do_pscs:
        code, p = ch_request(f"/company/{ch_number}/persons-with-significant-control?items_per_page=25", key)
        calls += 1
        if code == 200 and p:
            items = p.get("items", []) or []
            update["pscs"] = {
                "api_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "total_results": p.get("total_results"),
                "active_count": p.get("active_count"),
                "items": [
                    {
                        "name": i.get("name"),
                        "kind": i.get("kind"),
                        "nationality": i.get("nationality"),
                        "country_of_residence": i.get("country_of_residence"),
                        "ceased": bool(i.get("ceased_on")),
                        "natures_of_control": i.get("natures_of_control", [])[:3],
                        "notified_on": i.get("notified_on"),
                        "identification": i.get("identification"),
                    }
                    for i in items[:15]
                ],
            }
            time.sleep(CALL_INTERVAL)
        elif code == 404:
            update["pscs"] = {"api_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "total_results": 0, "items": []}

    # 4. Filing history (limit=5) → look for latest accounts PDF link
    if do_filing:
        code, fil = ch_request(f"/company/{ch_number}/filing-history?category=accounts&items_per_page=5", key)
        calls += 1
        if code == 200 and fil:
            items = fil.get("items", []) or []
            latest = items[0] if items else None
            if latest:
                # Extract document URL from links.document_metadata (full URL or path)
                doc_meta = (latest.get("links") or {}).get("document_metadata", "")
                # doc_meta may be e.g. "https://document-api.company-information.service.gov.uk/document/XXX"
                # Download PDF format: append /content?format=application/pdf
                pdf_url = None
                if doc_meta:
                    if doc_meta.startswith("http"):
                        pdf_url = doc_meta + "/content?format=application/pdf"
                    else:
                        pdf_url = f"https://document-api.company-information.service.gov.uk{doc_meta}/content?format=application/pdf"
                update["accounts_pdf"] = {
                    "transaction_id": latest.get("transaction_id"),
                    "date": latest.get("date"),
                    "type": latest.get("type"),
                    "description": latest.get("description"),
                    "pdf_url": pdf_url,
                    "view_url": f"https://find-and-update.company-information.service.gov.uk/company/{ch_number}/filing-history/{latest.get('transaction_id')}",
                }
            time.sleep(CALL_INTERVAL)

    return update, calls


def load_progress():
    if PROGRESS_FILE.exists():
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    return {"completed": [], "failed": []}


def save_progress(prog):
    PROGRESS_FILE.write_text(json.dumps(prog, indent=2), encoding="utf-8")


def update_supplier_file(ch, update):
    path = SUPPLIERS_V2 / f"{ch}.json"
    if not path.exists():
        return False
    d = json.loads(path.read_text(encoding="utf-8"))
    d.update(update)
    if "ch_profile" in update:
        d.setdefault("enrichment_stages", {})["ch_api_profile"] = True
    if "governance" in update:
        d.setdefault("enrichment_stages", {})["ch_api_officers"] = True
    if "pscs" in update:
        d.setdefault("enrichment_stages", {})["ch_api_pscs"] = True
    if "accounts_pdf" in update:
        d.setdefault("enrichment_stages", {})["ch_api_accounts_pdf"] = True
    path.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, help="Enrich top N suppliers by £ spend")
    ap.add_argument("--rank-from", type=int, default=0)
    ap.add_argument("--rank-to", type=int, default=None)
    ap.add_argument("--resume", action="store_true", help="Skip already-completed")
    ap.add_argument("--all", action="store_true", help="Enrich every non-completed supplier")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    key = load_key()
    if not key:
        print("Error: no CH_API_KEY found in .env or env var", file=sys.stderr)
        sys.exit(1)

    index = json.loads(INDEX_FILE.read_text(encoding="utf-8"))
    # Order by £ descending
    ordered = sorted(index.items(), key=lambda kv: -(kv[1].get("total_gbp_2024") or 0))

    # Select batch
    if args.top:
        batch = ordered[:args.top]
    elif args.all:
        batch = ordered[args.rank_from:args.rank_to] if args.rank_to else ordered[args.rank_from:]
    else:
        batch = ordered[args.rank_from:args.rank_to or args.rank_from + 500]

    progress = load_progress()
    already = set(progress["completed"])

    todo = [(ch, info) for ch, info in batch if ch not in already]
    print(f"Batch size: {len(batch):,} · already done: {len(already):,} · todo: {len(todo):,}")
    if not todo:
        print("Nothing to do.")
        return

    if args.dry_run:
        print("\nFirst 10 to enrich:")
        for ch, info in todo[:10]:
            print(f"  {ch}  £{(info.get('total_gbp_2024') or 0)/1e6:.1f}M  {info.get('display_name')}")
        return

    total_calls = 0
    start = time.time()
    for i, (ch, info) in enumerate(todo):
        elapsed = time.time() - start
        rate = (i + 1) / max(elapsed, 1) * 60
        print(f"[{i+1}/{len(todo)}] {ch} · {(info.get('display_name') or '')[:45]:45s}  £{(info.get('total_gbp_2024') or 0)/1e6:.1f}M · {rate:.0f}/min", flush=True)
        try:
            update, calls = enrich_supplier(ch, key)
            total_calls += calls
            ok = update_supplier_file(ch, update)
            if ok:
                progress["completed"].append(ch)
            else:
                progress["failed"].append({"ch": ch, "reason": "file missing"})
        except Exception as e:
            print(f"  ERROR: {e}")
            progress["failed"].append({"ch": ch, "reason": str(e)})

        if (i + 1) % 20 == 0:
            save_progress(progress)

    save_progress(progress)
    print(f"\nBatch complete · {len(progress['completed']):,} total enriched · {total_calls:,} API calls made")


if __name__ == "__main__":
    main()
