from fastapi import APIRouter, HTTPException, Depends
from app.services.image_storage import get_image_path
from app.services.analysis_service import analyze_image
from app.utils.security import verify_api_key
from app.models.schemas import AnalyzeRequest
from fastapi.responses import JSONResponse
import logging

router = APIRouter()


@router.post("/analyze")
async def analyze(payload: AnalyzeRequest, _: str = Depends(verify_api_key)):
    image_id = payload.image_id
    logging.info(f"Analyze request received for image_id: {image_id}")

    image_path = get_image_path(image_id)

    if not image_path:
        logging.error(f"Analyze failed: Image not found {image_id}")
        return JSONResponse(status_code=404, content={"error": "Image not found"})

    result = analyze_image(image_id)
    logging.info(f"Analysis complete for image_id: {image_id} -> {result}")
    return JSONResponse(status_code=200, content=result)
