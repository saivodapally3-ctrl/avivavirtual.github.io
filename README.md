# AvivaVirtual AI Website + Backend

This repository now includes:

- `index.html` (GitHub Pages frontend with floating AI chat/voice widget)
- `backend/` (FastAPI API for chat + placeholder voice WebSocket)

## 1) Frontend (GitHub Pages)

The site remains static and can be hosted directly from this repo root.

### Deploy
1. Push to `main`.
2. In GitHub repo settings, enable **Pages** from `main` branch root.
3. Keep `CNAME` configured for `avivavirtual.com`.

## 2) Backend (Render / Railway / VPS)

Use the `backend/` folder as a Python web service.

### Local run
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload --port 5050
```

### Required environment variables
- `OPENAI_API_KEY`
- `OPENAI_MODEL` (optional, defaults to `gpt-4.1-mini`)

### Endpoints
- `GET /` health check
- `POST /chat` text chat response
- `WS /media-stream` placeholder voice socket (for future real-time audio relay)

## 3) Connect frontend to backend

`index.html` is configured to call:

- `https://api.avivavirtual.com/chat`
- `wss://api.avivavirtual.com/media-stream`

Point your DNS for `api.avivavirtual.com` to your backend host.
