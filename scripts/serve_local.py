#!/usr/bin/env python3
"""
serve_local.py — Dev server replicating nginx routing.

The frontend expects these absolute paths from origin root:
  /                  -> frontend/index.html
  /frontend/...      -> frontend/...
  /tax/...           -> frontend/tax/...
  /data/...          -> data/...

Usage:  py scripts/serve_local.py [PORT]
Default port: 8765
"""
import http.server
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class BGDevHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Strip query string
        path = path.split('?', 1)[0].split('#', 1)[0]

        # Root -> frontend/index.html
        if path in ('/', '/index.html'):
            return str(ROOT / 'frontend' / 'index.html')

        # /tax/... -> frontend/tax/...
        if path.startswith('/tax/'):
            return str(ROOT / 'frontend' / path.lstrip('/'))

        # /data/... -> data/...
        if path.startswith('/data/'):
            return str(ROOT / path.lstrip('/'))

        # /frontend/... -> frontend/...
        if path.startswith('/frontend/'):
            return str(ROOT / path.lstrip('/'))

        # Default: serve from repo root
        return str(ROOT / path.lstrip('/'))

    def log_message(self, fmt, *args):
        # Quiet the per-file access log; only show non-200s
        code = args[1] if len(args) >= 2 else ''
        if not code.startswith('2'):
            super().log_message(fmt, *args)

    def end_headers(self):
        # Disable caching during dev so refresh always wins
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        super().end_headers()


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    os.chdir(ROOT)
    with http.server.ThreadingHTTPServer(('127.0.0.1', port), BGDevHandler) as s:
        print(f'Budget Galaxy dev server')
        print(f'  http://localhost:{port}/')
        print(f'  Ctrl+C to stop')
        try:
            s.serve_forever()
        except KeyboardInterrupt:
            print('\nShutting down.')


if __name__ == '__main__':
    main()
