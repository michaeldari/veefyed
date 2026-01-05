import uuid
from pathlib import Path
from fastapi import UploadFile
from app.utils.config import UPLOAD_DIR
from typing import Optional


def save_image(file: UploadFile) -> str:
    image_id = uuid.uuid4().hex
    extension = ".jpg" if file.content_type == "image/jpeg" else ".png"

    file_path = UPLOAD_DIR / f"{image_id}{extension}"

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    return image_id


def get_image_path(image_id: str) -> Optional[Path]:
    for ext in [".jpg", ".png"]:
        path = UPLOAD_DIR / f"{image_id}{ext}"
        if path.exists():
            return path
    return None
