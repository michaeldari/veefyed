from fastapi import APIRouter, UploadFile, File, Depends
from app.utils.validators import validate_image
from app.services.image_storage import save_image
from app.utils.security import verify_api_key
from fastapi.responses import JSONResponse
import logging

router = APIRouter()


@router.post("/upload")
async def upload_image(file: UploadFile = File(...), _: str = Depends(verify_api_key)):
    error_response = validate_image(file)
    if error_response:
        return error_response
    image_id = save_image(file)
    logging.info(f"Image uploaded: {image_id} ({file.filename})")
    return JSONResponse(status_code=201, content={"image_id": image_id})
