from fastapi import FastAPI
from app.routes import upload, analyze
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

app = FastAPI(
    title="Veefyed Image Analysis API",
    description="Backend service for uploading and analyzing skin images using mocked AI logic.",
    version="1.0.0",
)

app.include_router(upload.router, tags=["Image Upload"])
app.include_router(analyze.router, tags=["Image Analysis"])


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok"}
