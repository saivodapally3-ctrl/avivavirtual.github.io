import os
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

try:
    from openai import OpenAI
except ImportError:  # handled by requirements during deploy
    OpenAI = None


load_dotenv()

app = FastAPI(title="AvivaVirtual AI Backend", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    text: str
    session_id: str | None = None
    source: str | None = None


def build_openai_client() -> Any:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key or OpenAI is None:
        return None
    return OpenAI(api_key=api_key)


@app.get("/")
async def health() -> dict[str, str]:
    return {"status": "running"}


@app.post("/chat")
async def chat(req: ChatRequest) -> dict[str, str]:
    client = build_openai_client()

    if client is None:
        return {
            "reply": "Backend is online, but OPENAI_API_KEY is not configured yet."
        }

    completion = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
        temperature=0.4,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are AvivaVirtual customer support AI. "
                    "Be concise, practical, and empathetic."
                ),
            },
            {"role": "user", "content": req.text},
        ],
    )

    reply = completion.choices[0].message.content or "Sorry, I could not respond."
    return {"reply": reply}


@app.websocket("/media-stream")
async def media_stream(websocket: WebSocket) -> None:
    """Placeholder WebSocket endpoint for browser voice streaming."""
    await websocket.accept()
    await websocket.send_json(
        {
            "text": (
                "Voice socket connected. Deploy realtime audio pipeline next "
                "(Twilio or OpenAI Realtime relay)."
            )
        }
    )

    try:
        while True:
            await websocket.receive_bytes()
    except WebSocketDisconnect:
        return
