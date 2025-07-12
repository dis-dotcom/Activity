from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import datetime

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
async def root():
    return "❤"

@app.get("/log")
async def log():
    return datetime.now()