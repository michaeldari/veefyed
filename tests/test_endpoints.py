import os
import io
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
API_KEY = os.getenv("API_KEY")


def test_upload_png():
    png_file = io.BytesIO(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR")
    response = client.post(
        "/upload",
        files={"file": ("test.png", png_file, "image/png")},
        headers={"X-API-KEY": API_KEY},
    )
    assert response.status_code == 201
    data = response.json()
    assert "image_id" in data
    assert len(data["image_id"]) == 32


def test_upload_invalid_file():
    mp3_file = io.BytesIO(b"ID3")
    response = client.post(
        "/upload",
        files={"file": ("test.mp3", mp3_file, "audio/mpeg")},
        headers={"X-API-KEY": API_KEY},
    )
    assert response.status_code == 400
    data = response.json()
    assert "error" in data


def test_analyze_image():
    png_file = io.BytesIO(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR")
    upload_resp = client.post(
        "/upload",
        files={"file": ("test.png", png_file, "image/png")},
        headers={"X-API-KEY": API_KEY},
    )
    image_id = upload_resp.json()["image_id"]

    analyze_resp = client.post(
        "/analyze", json={"image_id": image_id}, headers={"X-API-KEY": API_KEY}
    )
    assert analyze_resp.status_code == 200
    data = analyze_resp.json()
    assert data["image_id"] == image_id
    assert "skin_type" in data
    assert "issues" in data
    assert "confidence" in data


def test_upload_with_invalid_api_key():
    png_file = io.BytesIO(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR")

    response = client.post(
        "/upload",
        files={"file": ("test.png", png_file, "image/png")},
        headers={"X-API-KEY": "wkey"},
    )

    assert response.status_code == 401

    data = response.json()
    assert "detail" in data
    assert data["detail"] == "Invalid API key"
