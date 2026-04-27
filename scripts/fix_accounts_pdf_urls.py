"""Repair malformed accounts_pdf.pdf_url across all suppliers_v2/*.json files.

Bug: pdf_url contains a base URL prepended to an already-absolute URL, e.g.:
  "https://find-and-update.company-information.service.gov.ukhttps://document-api.company-information.service.gov.uk/filing-history/<id>/document?format=pdf"

Correct shape: use links.document_metadata + "/content?format=application/pdf"
  "https://document-api.company-information.service.gov.uk/document/<id>/content?format=application/pdf"
"""
import json
import os
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(50000)

DOC_API = 'https://document-api.company-information.service.gov.uk'
fixed = 0
inspected = 0
no_change = 0
no_meta = 0

for path in glob.glob('data/suppliers_v2/[0-9A-Z]*.json'):
    inspected += 1
    try:
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        continue
    ap = data.get('accounts_pdf') or {}
    if not isinstance(ap, dict):
        continue
    cur_url = ap.get('pdf_url') or ''
    # Detect malformed: contains "find-and-update" + "document-api" both
    if 'find-and-update' in cur_url and 'document-api' in cur_url:
        # Reconstruct from links.document_metadata
        doc_meta = ((ap.get('links') or {}).get('document_metadata') or '').strip()
        if not doc_meta:
            no_meta += 1
            continue
        # Build clean URL
        if doc_meta.startswith('http'):
            new_url = doc_meta.rstrip('/') + '/content?format=application/pdf'
        else:
            new_url = f'{DOC_API}{doc_meta}/content?format=application/pdf'
        ap['pdf_url'] = new_url
        # Also set view_url if missing
        if not ap.get('view_url'):
            tx = ap.get('transaction_id', '')
            ch = data.get('company_number') or os.path.basename(path).replace('.json','')
            ap['view_url'] = f'https://find-and-update.company-information.service.gov.uk/company/{ch}/filing-history/{tx}'
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        fixed += 1
    else:
        no_change += 1

print(f'Inspected: {inspected:,}')
print(f'Fixed: {fixed:,}')
print(f'No malformation: {no_change:,}')
print(f'Malformed but no document_metadata to rebuild from: {no_meta}')
