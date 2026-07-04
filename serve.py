#!/usr/bin/env python3
"""Micro-server locale per il Planner Sud Francia.
Uso:  python serve.py   (poi apri http://localhost:8000)
Ferma con Ctrl+C. Nessuna dipendenza esterna."""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *args):
        pass  # silenzioso


if __name__ == "__main__":
    url = f"http://localhost:{PORT}"
    try:
        webbrowser.open(url)
    except Exception:
        pass
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"Planner attivo su {url}")
        print("Premi Ctrl+C per fermare.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nChiuso.")
