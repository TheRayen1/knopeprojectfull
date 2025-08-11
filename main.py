from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

genai.configure(api_key="AIzaSyC_9Zw3h776MRV-wz23s2DRbfaytBLLInk")  # Replace with your real key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="."), name="static")

class Message(BaseModel):
    message: str

class ChatLog(BaseModel):
    user: str

@app.get("/", response_class=HTMLResponse)
async def get_home():
    with open("chatbot.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/chat")
async def chat(msg: Message):
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(msg.message)
        return {"response": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/log")
async def log_chat(log: ChatLog):
    with open("chat_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"User: {log.user}\n")
    return {"status": "logged"}
