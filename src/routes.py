from flask import Blueprint, render_template, request, session, jsonify
from auth import check_password, require_auth
import content

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template(
        "base.html", content=content.get_page_or_404("/"), nav_links=content.get_nav_links()
    )

@bp.route("/admin")
def admin():
    if not session.get("authenticated"):
        return render_template(
            "admin.html", authenticated=False, slugs={}, file_tree={}
        )
    return render_template(
        "admin.html", authenticated=True, slugs=content.slug_cache, file_tree=content.build_file_tree()
    )

@bp.route("/api/login", methods=["POST"])
def login():
    """Authenticate user and create session."""
    data = request.json or {}
    password = data.get("password", "")

    if check_password(password):
        session["authenticated"] = True
        return jsonify({"success": True, "message": "Login successful"})
    return jsonify({"error": "Invalid password"}), 401

@bp.route("/api/logout", methods=["POST"])
def logout():
    """Clear user session."""
    session.pop("authenticated", None)
    return jsonify({"success": True, "message": "Logged out successfully"})

@bp.route("/api/page/root")
def get_root_page_content():
    """Get raw markdown content for root page."""
    return content.get_page_content_by_slug("/")

@bp.route("/api/page/<path:slug>")
def get_page_content(slug):
    """Get raw markdown content for editing."""
    return content.get_page_content_by_slug(slug)

@bp.route("/api/page", methods=["POST"])
@require_auth
def save_page():
    """Save markdown content by converting to HTML and storing."""
    data = request.json
    path = data.get("path", "").strip()
    markdown_content = data.get("content", "")
    priority = data.get("priority", -1)

    success, message, action = content.save_page_content(path, markdown_content, priority)
    
    if not success:
        return jsonify({"error": message}), 400
        
    return jsonify(
        {
            "success": True,
            "path": path,
            "message": message,
            "action": action,
        }
    )

@bp.route("/api/page", methods=["DELETE"])
@require_auth
def delete_page():
    """Delete a markdown file."""
    slug = request.json.get("slug", "")
    success, message, path = content.delete_page_content(slug)
    
    if not success:
        return jsonify({"error": message}), 404
        
    return jsonify(
        {
            "success": True,
            "message": message,
            "path": path,
        }
    )

@bp.route("/<path:slug>")
def serve_page(slug):
    return render_template(
        "base.html", content=content.get_page_or_404(slug), nav_links=content.get_nav_links()
    )
