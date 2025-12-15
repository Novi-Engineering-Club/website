from functools import wraps
from flask import request, session, jsonify
from config import ADMIN_PASSWORD

def check_password(password):
    """Verify the admin password."""
    return password == ADMIN_PASSWORD

def require_auth(f):
    """Decorator to require authentication for API endpoints."""

    @wraps(f)
    def decorated(*args, **kwargs):
        # Check session first
        if session.get("authenticated"):
            return f(*args, **kwargs)
        # Then check request header/body for password
        password = request.headers.get("X-Admin-Password") or (request.json or {}).get(
            "password"
        )
        if not password or not check_password(password):
            return jsonify({"error": "Unauthorized: Invalid or missing password"}), 401
        return f(*args, **kwargs)

    return decorated
