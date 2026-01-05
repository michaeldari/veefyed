from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):
    image_id: str = Field(..., pattern=r'^[a-f0-9]{32}$')