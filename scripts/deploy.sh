#!/usr/bin/env bash
# Deploy Budget Galaxy to prod (Vultr 96.30.199.112).
#
# Pushing to GitHub != deploying. The server doesn't pull anything.
# This script is the deploy. Run it after every commit that touches
# frontend/, data/uk/, or data/suppliers*.
#
# Usage:
#   bash scripts/deploy.sh                  # interactive: prompts before each step
#   bash scripts/deploy.sh frontend         # only frontend/index.html
#   bash scripts/deploy.sh enrichment       # only data/uk/node_enrichment_extended.json
#   bash scripts/deploy.sh suppliers-index  # only data/suppliers_v2/_index.json (fast)
#   bash scripts/deploy.sh suppliers-full   # full data/suppliers_v2/ (slow, ~150MB)
#   bash scripts/deploy.sh all              # everything in safe order
#   bash scripts/deploy.sh smoke            # smoke test only

set -euo pipefail

SSH_KEY="${SSH_KEY:-$HOME/.ssh/id_agro_intel}"
REMOTE="${REMOTE:-root@96.30.199.112}"
PROD_ROOT="${PROD_ROOT:-/opt/germany-ngo-map}"
LOCAL_ROOT="${LOCAL_ROOT:-$(git rev-parse --show-toplevel)}"

# Colors
G='\033[1;32m'; Y='\033[1;33m'; R='\033[1;31m'; N='\033[0m'
ok()   { echo -e "${G}✓${N} $*"; }
warn() { echo -e "${Y}⚠${N} $*"; }
err()  { echo -e "${R}✗${N} $*" >&2; }

deploy_frontend() {
  echo "→ Deploying frontend/index.html"
  scp -i "$SSH_KEY" "$LOCAL_ROOT/frontend/index.html" "$REMOTE:$PROD_ROOT/frontend/index.html"
  ok "frontend deployed"
}

deploy_enrichment() {
  echo "→ Deploying data/uk/node_enrichment_extended.json"
  scp -i "$SSH_KEY" "$LOCAL_ROOT/data/uk/node_enrichment_extended.json" "$REMOTE:$PROD_ROOT/data/uk/"
  ok "node_enrichment_extended.json deployed"
}

deploy_suppliers_index() {
  echo "→ Deploying data/suppliers_v2/_index.json"
  scp -i "$SSH_KEY" "$LOCAL_ROOT/data/suppliers_v2/_index.json" "$REMOTE:$PROD_ROOT/data/suppliers_v2/"
  ok "suppliers_v2/_index.json deployed"
}

deploy_suppliers_curated_index() {
  echo "→ Deploying data/suppliers/_index.json (400 curated)"
  scp -i "$SSH_KEY" "$LOCAL_ROOT/data/suppliers/_index.json" "$REMOTE:$PROD_ROOT/data/suppliers/"
  ok "suppliers/_index.json deployed"
}

deploy_suppliers_full() {
  echo "→ Deploying full data/suppliers_v2/ (this can take several minutes)"
  warn "If the bulk-enrich pipeline is running, files may be in flux. Stop it first."
  cd "$LOCAL_ROOT/data"
  tar --exclude=_ch_api_progress.json --exclude=_ch_api_state.json -czf /tmp/v2.tgz suppliers_v2
  scp -i "$SSH_KEY" /tmp/v2.tgz "$REMOTE:/tmp/"
  ssh -i "$SSH_KEY" "$REMOTE" "cd $PROD_ROOT/data && tar xzf /tmp/v2.tgz && rm /tmp/v2.tgz && ls suppliers_v2 | wc -l"
  rm /tmp/v2.tgz
  ok "suppliers_v2/ full deployed"
}

deploy_pdfs() {
  echo "→ Deploying cached supplier accounts PDFs (~1.6GB, ~3-5 min)"
  echo "  These are the FY-snapshot frozen PDFs for the curated 400. They are"
  echo "  point-in-time copies — not maintained as suppliers refile. Each"
  echo "  fiscal-year snapshot will have its own set."
  cd "$LOCAL_ROOT/data"
  tar -czf /tmp/sup_pdfs.tgz recipients/uk/supplier_financials
  scp -i "$SSH_KEY" /tmp/sup_pdfs.tgz "$REMOTE:/tmp/"
  ssh -i "$SSH_KEY" "$REMOTE" "mkdir -p $PROD_ROOT/data/recipients/uk && cd $PROD_ROOT/data && tar xzf /tmp/sup_pdfs.tgz && rm /tmp/sup_pdfs.tgz && ls recipients/uk/supplier_financials | wc -l && du -sh recipients/uk/supplier_financials"
  rm /tmp/sup_pdfs.tgz
  ok "supplier PDFs deployed"
}

smoke_test() {
  echo "→ Smoke test"
  local ts=$(date +%s)
  echo
  echo "Frontend:"
  curl -sI "https://budgetgalaxy.com/?nocache=$ts" | grep -iE "HTTP|last-modified|content-length"
  echo
  echo "v2 index:"
  curl -sI "https://budgetgalaxy.com/data/suppliers_v2/_index.json?nocache=$ts" | grep -iE "HTTP|last-modified|content-length"
  echo
  echo "Enrichment:"
  curl -sI "https://budgetgalaxy.com/data/uk/node_enrichment_extended.json?nocache=$ts" | grep -iE "HTTP|last-modified|content-length"
  echo
  echo "v2 index sample (top_buyer_type distribution):"
  curl -s "https://budgetgalaxy.com/data/suppliers_v2/_index.json?nocache=$ts" \
    | python -c "import sys,json; from collections import Counter; d=json.load(sys.stdin); bt=Counter(e.get('top_buyer_type') or '(none)' for e in d.values()); n=sum(1 for e in d.values() if (e.get('enrichment_stages') or {}).get('ch_api_profile')); print(f'{len(d):,} entries · {n:,} enriched'); [print(f'  {t:15s} {c:>6,}') for t,c in sorted(bt.items(),key=lambda kv:-kv[1])]"
}

case "${1:-help}" in
  frontend)         deploy_frontend ;;
  enrichment)       deploy_enrichment ;;
  suppliers-index)  deploy_suppliers_index; deploy_suppliers_curated_index ;;
  suppliers-full)   deploy_suppliers_full ;;
  pdfs)             deploy_pdfs ;;
  all)
    deploy_frontend
    deploy_enrichment
    deploy_suppliers_curated_index
    deploy_suppliers_index
    deploy_suppliers_full
    smoke_test
    ;;
  smoke)            smoke_test ;;
  help|*)
    cat <<EOF
Usage: bash scripts/deploy.sh <target>

Targets:
  frontend          frontend/index.html only
  enrichment        data/uk/node_enrichment_extended.json only
  suppliers-index   data/suppliers/_index.json + suppliers_v2/_index.json (fast)
  suppliers-full    everything under data/suppliers_v2/ (slow, ~150MB)
  pdfs              cached supplier accounts PDFs (~1.6GB, one-time per FY)
  all               full deploy in safe order + smoke test
  smoke             smoke test only (curl + verify)

Environment overrides:
  SSH_KEY     (default: ~/.ssh/id_agro_intel)
  REMOTE      (default: root@96.30.199.112)
  PROD_ROOT   (default: /opt/germany-ngo-map)
EOF
    ;;
esac
