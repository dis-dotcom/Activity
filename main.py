from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from datetime import datetime

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def root():
    return "❤"


@app.get("/log")
async def log():
    now = datetime.now()
    with open('.log', 'a', encoding='utf-8') as file:
        file.writelines([str(now)])

    return now
