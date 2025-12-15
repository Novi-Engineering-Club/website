import os
from pathlib import Path
import dotenv

dotenv.load_dotenv()

SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin")

# Use absolute paths relative to the project root (assuming config.py is in root)
BASE_DIR = Path(__file__).parent
CONTENT_DIR = BASE_DIR / "pages"
CACHE_FILE = BASE_DIR / "slugs.json"

STORAGE_BACKEND = "filesystem"

MARKDOWN_EXTENSIONS = [
    "extra",
    "codehilite",
]
