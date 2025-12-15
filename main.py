import json
import os
import re
from functools import wraps
from pathlib import Path

import dotenv
import markdown
from flask import Flask, abort, jsonify, render_template, request, session
from html_to_markdown import convert as html_to_markdown
from werkzeug.security import safe_join

dotenv.load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

# Set admin password via environment variable, or use default for development
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin")

CONTENT_DIR = Path(__file__).parent / "pages"
CACHE_FILE = Path(__file__).parent / "slugs.json"

extensions = [
    "extra",
    "codehilite",
]


def extract_metadata_from_html(html_content):
    """Extract metadata from HTML comment block."""
    metadata = {"priority": -1}
    match = re.search(r"<!--\s*METADATA\s*\n(.*?)\n-->", html_content, re.DOTALL)
    if match:
        meta_lines = match.group(1).strip().split("\n")
        for line in meta_lines:
            if ":" in line:
                key, value = line.split(":", 1)
                key = key.strip().lower()
                value = value.strip()
                if key == "priority":
                    try:
                        metadata["priority"] = int(value)
                    except ValueError:
                        pass
    return metadata


def embed_metadata_in_html(html_content, priority=-1):
    """Embed metadata in HTML as a comment block."""
    if priority >= 0:
        metadata_comment = f"<!-- METADATA\npriority: {priority}\n-->\n"
        return metadata_comment + html_content
    return html_content


def build_slug_cache():
    """Build cache of page slugs by scanning CONTENT_DIR for HTML files."""
    slugs = {}
    CONTENT_DIR.mkdir(exist_ok=True)

    for html_file in CONTENT_DIR.rglob("*.html"):
        relative_path = html_file.relative_to(CONTENT_DIR)
        path_str = relative_path.as_posix()

        if html_file.name == "index.html":
            parent = relative_path.parent.as_posix()
            slug = "/" if parent == "." else parent
        else:
            slug = path_str[:-5]  # Remove .html extension

        priority = -1
        try:
            html_content = html_file.read_text(encoding="utf-8")
            metadata = extract_metadata_from_html(html_content)
            priority = metadata["priority"]
        except Exception:
            pass

        slugs[slug] = {"path": path_str, "priority": priority}

    CACHE_FILE.write_text(json.dumps(slugs), encoding="utf-8")
    return slugs


def load_slug_cache():
    """Load slug cache from file, rebuilding if missing or corrupted."""
    if not CACHE_FILE.exists():
        return build_slug_cache()
    try:
        return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return build_slug_cache()


def strip_metadata_from_html(html_content):
    """Remove metadata comment block from HTML content."""
    return re.sub(
        r"<!--\s*METADATA\s*\n.*?\n-->\s*\n?", "", html_content, flags=re.DOTALL
    )


def get_page_or_404(slug):
    """Retrieve and serve an HTML page, or abort with 404."""
    if slug not in slug_cache:
        abort(404, description="Page not found")

    full_path = safe_join(str(CONTENT_DIR), slug_cache[slug]["path"])
    try:
        html_content = Path(full_path).read_text(encoding="utf-8")
        content = strip_metadata_from_html(html_content)
        return content
    except FileNotFoundError:
        abort(404, description="Page not found")


slug_cache = load_slug_cache()


def get_priority(slug):
    """Get priority for a slug (-1 means unordered/last)."""
    return slug_cache.get(slug, {}).get("priority", -1)


def is_folder(slug):
    """Check if slug represents a folder (has children or is from index.html)."""
    if slug == "/":
        return False
    path = slug_cache.get(slug, {}).get("path", "")
    if path.endswith("index.html"):
        return True
    return any(s.startswith(f"{slug}/") for s in slug_cache)


def sort_key(slug):
    """Sort key: root first, then by priority, then files before folders."""
    priority = get_priority(slug)
    if slug == "/":
        return (0, 0, "")
    if priority >= 0:
        return (1, priority, slug)
    return (2, 0, slug) if not is_folder(slug) else (3, 0, slug)


def get_nav_links():
    """Generate navigation structure with top-level items and children."""
    top_level = [s for s in slug_cache if s == "/" or "/" not in s]
    children = [s for s in slug_cache if s != "/" and "/" in s]

    top_level.sort(key=sort_key)
    children.sort(key=sort_key)

    nav_links = []
    for parent_slug in top_level:
        item = {
            "url": "/" if parent_slug == "/" else f"/{parent_slug}",
            "title": "Home"
            if parent_slug == "/"
            else parent_slug.replace("-", " ").title(),
            "children": [],
        }

        if parent_slug != "/":
            prefix = f"{parent_slug}/"
            item["children"] = [
                {"url": f"/{s}", "title": s.split("/")[-1].replace("-", " ").title()}
                for s in children
                if s.startswith(prefix)
            ]

        nav_links.append(item)

    return nav_links


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


@app.route("/")
def index():
    return render_template(
        "base.html", content=get_page_or_404("/"), nav_links=get_nav_links()
    )


def sort_tree_key(item):
    """Sort key for tree items: root first, then by priority, then files before folders."""
    name, data = item
    if name == "/":
        return (0, 0, "")
    has_children = "_children" in data and data["_children"]
    priority = get_priority(data.get("slug", ""))
    if priority >= 0:
        return (1, priority, name)
    return (2, 0, name) if not has_children else (3, 0, name)


def sort_tree(tree):
    """Recursively sort tree items."""
    sorted_tree = dict(sorted(tree.items(), key=sort_tree_key))
    for name, data in sorted_tree.items():
        if "_children" in data and data["_children"]:
            sorted_tree[name]["_children"] = sort_tree(data["_children"])
    return sorted_tree


def build_file_tree():
    """Build a nested tree structure from slugs for sidebar display."""
    tree = {}

    for slug in slug_cache:
        if "/" in slug and slug != "/":
            parts = slug.split("/")
            current = tree
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {"_children": {}}
                elif "_children" not in current[part]:
                    current[part]["_children"] = {}
                current = current[part]["_children"]

    for slug, data in slug_cache.items():
        path = data["path"]
        node = {
            "slug": slug,
            "path": path,
            "is_index": path.endswith("index.html"),
            "priority": get_priority(slug),
        }

        if slug == "/":
            tree["/"] = node
        elif "/" not in slug:
            if slug in tree:
                tree[slug].update(node)
            else:
                tree[slug] = node
        else:
            parts = slug.split("/")
            current = tree
            for part in parts[:-1]:
                current = current[part]["_children"]
            current[parts[-1]] = node

    return sort_tree(tree)


@app.route("/admin")
def admin():
    if not session.get("authenticated"):
        return render_template(
            "admin.html", authenticated=False, slugs={}, file_tree={}
        )
    return render_template(
        "admin.html", authenticated=True, slugs=slug_cache, file_tree=build_file_tree()
    )


@app.route("/api/login", methods=["POST"])
def login():
    """Authenticate user and create session."""
    data = request.json or {}
    password = data.get("password", "")

    if check_password(password):
        session["authenticated"] = True
        return jsonify({"success": True, "message": "Login successful"})
    return jsonify({"error": "Invalid password"}), 401


@app.route("/api/logout", methods=["POST"])
def logout():
    """Clear user session."""
    session.pop("authenticated", None)
    return jsonify({"success": True, "message": "Logged out successfully"})


@app.route("/api/page/root")
def get_root_page_content():
    """Get raw markdown content for root page."""
    return get_page_content_by_slug("/")


@app.route("/api/page/<path:slug>")
def get_page_content(slug):
    """Get raw markdown content for editing."""
    return get_page_content_by_slug(slug)


def strip_priority_metadata(content):
    """Extract priority from HTML content and return clean markdown."""
    # This function is called when getting page content for editing
    # It receives HTML, extracts metadata, converts to markdown
    metadata = extract_metadata_from_html(content)
    priority = metadata["priority"]
    clean_html = strip_metadata_from_html(content)
    # Convert HTML to markdown for editing
    markdown_content = html_to_markdown(clean_html)
    return markdown_content, priority


def get_page_content_by_slug(slug):
    """Get markdown content (converted from HTML) by slug for editing."""
    if slug not in slug_cache:
        return jsonify({"error": "Page not found"}), 404
    relative_path = slug_cache[slug]["path"]
    full_path = safe_join(str(CONTENT_DIR), relative_path)
    try:
        html_content = Path(full_path).read_text(encoding="utf-8")
        markdown_content, priority = strip_priority_metadata(html_content)
        return jsonify(
            {"content": markdown_content, "path": relative_path, "priority": priority}
        )
    except FileNotFoundError:
        return jsonify({"error": "Page not found"}), 404


@app.route("/api/page", methods=["POST"])
@require_auth
def save_page():
    """Save markdown content by converting to HTML and storing."""
    global slug_cache
    data = request.json
    path = data.get("path", "").strip()
    markdown_content = data.get("content", "")
    priority = data.get("priority", -1)

    if not path:
        return jsonify({"error": "Path is required"}), 400

    # Convert .md extension to .html, or add .html if no extension
    if path.endswith(".md"):
        path = path[:-3] + ".html"
    elif not path.endswith(".html"):
        path += ".html"

    full_path = safe_join(str(CONTENT_DIR), path)
    if not full_path:
        return jsonify({"error": "Invalid path"}), 400

    # Check if this is a new page or update
    is_new = not Path(full_path).exists()

    try:
        priority = int(priority)
    except (ValueError, TypeError):
        priority = -1

    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=extensions)

    # Embed metadata in HTML
    html_with_metadata = embed_metadata_in_html(html_content, priority)

    Path(full_path).parent.mkdir(parents=True, exist_ok=True)
    Path(full_path).write_text(html_with_metadata, encoding="utf-8")
    slug_cache = build_slug_cache()

    action = "created" if is_new else "updated"
    return jsonify(
        {
            "success": True,
            "path": path,
            "message": f"Page '{path}' {action} successfully",
            "action": action,
        }
    )


@app.route("/api/page", methods=["DELETE"])
@require_auth
def delete_page():
    """Delete a markdown file."""
    global slug_cache
    slug = request.json.get("slug", "")
    if slug not in slug_cache:
        return jsonify({"error": "Page not found"}), 404

    page_path = slug_cache[slug]["path"]
    full_path = safe_join(str(CONTENT_DIR), page_path)
    try:
        Path(full_path).unlink()
        slug_cache = build_slug_cache()
        return jsonify(
            {
                "success": True,
                "message": f"Page '{page_path}' deleted successfully",
                "path": page_path,
            }
        )
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404


@app.route("/<path:slug>")
def serve_page(slug):
    return render_template(
        "base.html", content=get_page_or_404(slug), nav_links=get_nav_links()
    )


if __name__ == "__main__":
    app.run(debug=True)
