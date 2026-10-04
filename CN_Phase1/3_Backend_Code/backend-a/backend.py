#!/usr/bin/env python3
"""
CN Project - Backend A (plain Python), Laptop 1, port 3001
Usage: python3 backend.py A 3001

GET /            -> JSON page, cacheable (Cache-Control + ETag "home-v1", supports 304)
GET /api/status  -> JSON with backend id and status, never cached (no-store)
Every response carries  X-Backend: A
"""
import sys
import json
from datetime import datetime
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

BACKEND = sys.argv[1] if len(sys.argv) > 1 else "A"
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 3001

# Same content and same ETag as Backend B, so 304 works whichever backend answers
HOME_BODY = json.dumps({
    "service": "Private Network Service Platform",
    "team": "teamX",
    "message": "Service is running"
}).encode()
HOME_ETAG = '"home-v1"'


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def send(self, code, body, extra_headers=None):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("X-Backend", BACKEND)
        for key, value in (extra_headers or {}).items():
            self.send_header(key, value)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def handle_request(self):
        if self.path == "/":
            headers = {"Cache-Control": "max-age=60", "ETag": HOME_ETAG}
            if self.headers.get("If-None-Match") == HOME_ETAG:
                return self.send(304, b"", headers)
            return self.send(200, HOME_BODY, headers)

        if self.path == "/api/status":
            body = json.dumps({
                "backend": BACKEND,
                "status": "ok",
                "port": PORT,
                "time": datetime.now().isoformat(timespec="seconds")
            }).encode()
            return self.send(200, body, {"Cache-Control": "no-store"})

        self.send(404, json.dumps({"error": "not found", "backend": BACKEND}).encode())

    do_GET = handle_request
    do_HEAD = handle_request


if __name__ == "__main__":
    # 0.0.0.0 = listen on all interfaces (Wi-Fi too), not just 127.0.0.1
    print(f"Backend {BACKEND} listening on 0.0.0.0:{PORT}")
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
