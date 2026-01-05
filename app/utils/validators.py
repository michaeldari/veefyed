from fastapi import UploadFile
from .config import MAX_FILE_SIZE_MB, ALLOWED_EXTENSIONS
from fastapi.responses import JSONResponse
from pathlib import Path
import logging


def validate_image(file: UploadFile):
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        logging.warning(f"Invalid file type upload attempt: {file.filename}")
        return JSONResponse(
            status_code=400,
            content={"error": f"Invalid file type: {ext}. Only JPEG or PNG allowed."},
        )

    file.file.seek(0, 2)
    size_mb = file.file.tell() / (1024 * 1024)
    file.file.seek(0)

    if size_mb > MAX_FILE_SIZE_MB:
        logging.warning(f"File too large: {file.filename} ({size_mb} bytes)")
        return JSONResponse(
            status_code=400,
            content={"error": f"File too large ({size_mb} bytes). Max 5MB allowed."},
        )
