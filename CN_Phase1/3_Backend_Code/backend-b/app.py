"""
CN Project - Backend B (Flask), Laptop 2, port 3002

GET /            -> JSON page, cacheable (Cache-Control + ETag "home-v1", supports 304)
GET /api/status  -> JSON with backend id and status, never cached (no-store)
Every response carries  X-Backend: B
"""
from datetime import datetime
from flask import Flask, jsonify, make_response, request

app = Flask(__name__)
BACKEND = "B"
PORT = 3002
HOME_ETAG = '"home-v1"'   # must be the SAME as Backend A's ETag for "/"


@app.after_request
def add_backend_header(response):
    # Added to every response (including errors) so we always know who answered
    response.headers["X-Backend"] = BACKEND
    return response


@app.route("/")
def home():
    # Conditional request: client already has version "home-v1" -> 304, no body
    if request.headers.get("If-None-Match") == HOME_ETAG:
        response = make_response("", 304)
    else:
        response = make_response(jsonify({
            "service": "Private Network Service Platform",
            "team": "teamX",
            "message": "Service is running"
        }))
    response.headers["Cache-Control"] = "max-age=60"
    response.headers["ETag"] = HOME_ETAG
    return response


@app.route("/api/status")
def status():
    response = make_response(jsonify({
        "backend": BACKEND,
        "status": "ok",
        "port": PORT,
        "time": datetime.now().isoformat(timespec="seconds")
    }))
    response.headers["Cache-Control"] = "no-store"   # live status: never cache
    return response


if __name__ == "__main__":
    # 0.0.0.0 = reachable from other machines on the LAN, not just localhost
    app.run(host="0.0.0.0", port=PORT)
