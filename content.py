import json
from pathlib import Path
from flask import abort, jsonify
import markdown
from html_to_markdown import convert as html_to_markdown

from config import CONTENT_DIR, CACHE_FILE, MARKDOWN_EXTENSIONS, STORAGE_BACKEND
from utils import extract_metadata_from_html, embed_metadata_in_html, strip_metadata_from_html
from storage import get_storage

# Initialize storage
storage = get_storage(STORAGE_BACKEND, root_dir=CONTENT_DIR)

# Global cache
slug_cache = {}

def build_slug_cache():
    """Build cache of page slugs by scanning storage for HTML files."""
    global slug_cache
    slugs = {}
    
    # Storage handles listing files
    files = storage.list_files()

    for path_str in files:
        if path_str.endswith("index.html"):
            # Handle index.html mapping to parent folder
            path_obj = Path(path_str)
            parent = path_obj.parent.as_posix()
            slug = "/" if parent == "." else parent
        else:
            slug = path_str[:-5]  # Remove .html extension

        priority = -1
        try:
            html_content = storage.get_content(path_str)
            metadata = extract_metadata_from_html(html_content)
            priority = metadata["priority"]
        except Exception:
            pass

        slugs[slug] = {"path": path_str, "priority": priority}

    CACHE_FILE.write_text(json.dumps(slugs), encoding="utf-8")
    slug_cache = slugs
    return slugs


def load_slug_cache():
    """Load slug cache from file, rebuilding if missing or corrupted."""
    global slug_cache
    if not CACHE_FILE.exists():
        return build_slug_cache()
    try:
        slug_cache = json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        return slug_cache
    except json.JSONDecodeError:
        return build_slug_cache()


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


def get_page_or_404(slug):
    """Retrieve and serve an HTML page, or abort with 404."""
    if slug not in slug_cache:
        abort(404, description="Page not found")

    path = slug_cache[slug]["path"]
    try:
        html_content = storage.get_content(path)
        content = strip_metadata_from_html(html_content)
        return content
    except (FileNotFoundError, ValueError):
        abort(404, description="Page not found")


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


def strip_priority_metadata(content):
    """Extract priority from HTML content and return clean markdown."""
    metadata = extract_metadata_from_html(content)
    priority = metadata["priority"]
    clean_html = strip_metadata_from_html(content)
    markdown_content = html_to_markdown(clean_html)
    return markdown_content, priority


def get_page_content_by_slug(slug):
    """Get markdown content (converted from HTML) by slug for editing."""
    if slug not in slug_cache:
        return jsonify({"error": "Page not found"}), 404
    path = slug_cache[slug]["path"]
    try:
        html_content = storage.get_content(path)
        markdown_content, priority = strip_priority_metadata(html_content)
        return jsonify(
            {"content": markdown_content, "path": path, "priority": priority}
        )
    except (FileNotFoundError, ValueError):
        return jsonify({"error": "Page not found"}), 404

def save_page_content(path, markdown_content, priority):
    """Save markdown content by converting to HTML and storing."""
    if not path:
        return False, "Path is required", None

    # Convert .md extension to .html, or add .html if no extension
    if path.endswith(".md"):
        path = path[:-3] + ".html"
    elif not path.endswith(".html"):
        path += ".html"

    # Check if this is a new page or update
    is_new = not storage.exists(path)

    try:
        priority = int(priority)
    except (ValueError, TypeError):
        priority = -1

    # Convert markdown to HTML
    html_content = markdown.markdown(markdown_content, extensions=MARKDOWN_EXTENSIONS)

    # Embed metadata in HTML
    html_with_metadata = embed_metadata_in_html(html_content, priority)

    try:
        storage.save_content(path, html_with_metadata)
    except ValueError as e:
        return False, str(e), None
    
    build_slug_cache() # Refresh cache

    action = "created" if is_new else "updated"
    return True, f"Page '{path}' {action} successfully", action

def delete_page_content(slug):
    """Delete a markdown file."""
    if slug not in slug_cache:
        return False, "Page not found", None

    page_path = slug_cache[slug]["path"]
    try:
        storage.delete_content(page_path)
        build_slug_cache() # Refresh cache
        return True, f"Page '{page_path}' deleted successfully", page_path
    except (FileNotFoundError, ValueError):
        return False, "File not found", None

# Initialize cache
load_slug_cache()
