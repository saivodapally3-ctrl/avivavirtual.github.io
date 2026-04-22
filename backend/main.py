import os
from typing import Any

from dotenv import load_dotenv
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

load_dotenv()

app = FastAPI(title="AvivaVirtual AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@app.get("/")
async def root() -> dict[str, str]:
    return {"status": "running"}


@app.post("/chat")
async def chat(payload: dict[str, Any]) -> dict[str, str]:
    user_text = str(payload.get("text", "")).strip()
    if not user_text:
        return {"reply": "Please send a message."}

    completion = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": "You are a concise, friendly AI support assistant for AvivaVirtual.",
            },
            {"role": "user", "content": user_text},
        ],
    )

    return {"reply": completion.output_text or "I could not generate a response."}


@app.websocket("/media-stream")
async def media_stream(websocket: WebSocket) -> None:
    await websocket.accept()
    await websocket.send_json({"status": "connected"})

    try:
        async for message in websocket.iter_json():
            event = message.get("event")
            if event == "browser_audio":
                # Placeholder for browser audio -> model streaming pipeline.
                # Keeps protocol stable for GitHub Pages widget.
                await websocket.send_json(
                    {
                        "status": "audio_received",
                        "text_delta": "(Voice pipeline placeholder) Audio chunk received.",
                    }
                )
            else:
                await websocket.send_json({"status": "unknown_event"})
    except WebSocketDisconnect:
        return
