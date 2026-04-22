# AvivaVirtual AI (GitHub Pages + FastAPI)

This repository now contains a deploy-ready split:

- `index.html` (site root for GitHub Pages)
- `frontend/index.html` (same page copy, if you prefer folder-based deployment)
- `backend/` FastAPI API for chat + voice websocket placeholder

## Frontend (GitHub Pages)

Use root `index.html` for GitHub Pages.

The page includes:

- floating AI support widget
- text chat to `POST /chat`
- browser voice capture to `wss://.../media-stream`
- local session id tracking

## Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# set OPENAI_API_KEY in .env
uvicorn main:app --reload --port 5050
```

## Production wiring

- frontend domain: `https://avivavirtual.com`
- backend domain: `https://api.avivavirtual.com`
- update DNS so `api.avivavirtual.com` points to your FastAPI host (Render/Railway/etc.)

## Endpoints

- `GET /` health
- `POST /chat` text assistant response
- `WS /media-stream` browser voice stream endpoint (placeholder logic)
