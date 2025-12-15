import re

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


def strip_metadata_from_html(html_content):
    """Remove metadata comment block from HTML content."""
    return re.sub(
        r"<!--\s*METADATA\s*\n.*?\n-->\s*\n?", "", html_content, flags=re.DOTALL
    )
