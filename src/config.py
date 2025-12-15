import os
from pathlib import Path
import dotenv

# Use absolute paths relative to the project root (assuming config.py is in src)
BASE_DIR = Path(__file__).parent.parent
CONTENT_DIR = BASE_DIR / "pages"
CACHE_FILE = BASE_DIR / "slugs.json"

dotenv.load_dotenv(BASE_DIR / ".env")

SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin")

STORAGE_BACKEND = "filesystem"

MARKDOWN_EXTENSIONS = [
    "extra",
    "codehilite",
]
