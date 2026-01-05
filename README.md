# Veefyed API

A small backend service that allows a mobile app to upload images and receive mock analysis results (skin type, issues, confidence).

This project demonstrates a backend-driven workflow using **FastAPI**, with image upload, validation, API key authentication, and basic logging.

---

## 🏃 How to Run the Service

### 1. Clone the repository

```bash
git clone https://github.com/michaeldari/veefyed.git
cd veefyed
```

### 2.1 Run with Docker

```bash
docker build -t veefyed-api .
docker run -p 8000:8000 -v $(pwd)/uploads:/app/uploads -e API_KEY=xyo3ZJe5WUrh veefyed-api
```

### 2.2 Run with Docker for unit test
```bash
docker run --rm -e PYTHONPATH=/app -e API_KEY=xyo3ZJe5WUrh veefyed-api pytest tests -v
```

### 3. Run the service locally
```
Server will run on http://127.0.0.1:8000

Swagger docs: http://127.0.0.1:8000/docs
```

## 🔑 Authentication

* API requests require an **API key**
* Example key used in this project:

```
veefyed-secret-key
```

* Include it as a **header**:

```
X-API-KEY: veefyed-secret-key
```


## 🛠 Available Endpoints

### 1. Upload Image

```
POST /upload
```

* **Headers:** `X-API-KEY` required
* **Body:** Form-data with key `file` (JPEG or PNG, max 5MB)
* **Success Response (201):**

```json
{
  "image_id": "ae58e891fbaf48fab803858d1ebaa0c5"
}
```

* **Error Responses:**

```json
{
  "error": "Invalid file type"
}
```

```json
{
  "error": "File too large (max 5MB)"
}
```

---

### 2. Analyze Image

```
POST /analyze
```

* **Headers:** `X-API-KEY` required
* **Body:** JSON

```json
{
  "image_id": "ae58e891fbaf48fab803858d1ebaa0c5"
}
```

* **Success Response (200):**

```json
{
  "image_id": "ae58e891fbaf48fab803858d1ebaa0c5",
  "skin_type": "Oily",
  "issues": ["Acne"],
  "confidence": 0.87
}
```

* **Error Responses:**

```json
{
  "error": "Image not found"
}
```

```json
{
  "error": "Invalid API key"
}
```

---

## 💡 Assumptions Made

* Images are stored **locally** in `/app/uploads/`. No cloud storage is used.
* “Analysis” is **mocked/randomized**; no real AI model is implemented.
* API key is **hardcoded** for simplicity.
* Only **JPEG and PNG files** are allowed.
* Maximum upload size is **5MB**.

---

## 🚀 Improvements for Production

* Use **cloud storage** (e.g., S3, GCP Storage) instead of local filesystem.
* Implement **real AI/ML model** for analysis.
* Secure API key in **environment variables**, not hardcoded.
* Add **rate limiting** to prevent abuse.
* Add **structured logging** to a file or centralized service (ELK, Datadog).
* Add **user authentication** if multiple clients/users exist.
* Add **unit tests and integration tests**.
* Support **image deletion and cleanup**.
* Validate uploaded files using **magic numbers**, not just extension, to prevent fake files.

---

## ⚡ Notes

* All responses (success or error) are JSON.
* HTTP status codes are used appropriately (`201`, `200`, `400`, `404`, `401`, `422`, `500`).
* Swagger/OpenAPI docs are available at `/docs` for testing endpoints interactively.

