from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from DateTime import Now

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def root():
    return "❤"


@app.get("/log")
async def log():
    now = Now()
    lines = [str(now)]

    with open('/home/.log', 'a', encoding='utf-8') as file:
        file.writelines(lines)

    return now
