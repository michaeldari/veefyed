from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"

MAX_FILE_SIZE_MB = 5
ALLOWED_EXTENSIONS = {".jpg", ".jpeg", ".png"}

# Simple API Key (for demo purposes)
API_KEY = os.getenv("API_KEY", "veefyed-secret-key")

UPLOAD_DIR.mkdir(exist_ok=True)
