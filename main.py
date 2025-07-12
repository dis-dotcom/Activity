from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from DateTime import Now
from index import index
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    log_activity()

    return index


@app.get("/api/logs")
async def log():
    with open('/home/.log', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return {
        items: lines
    }


def log_activity():
    now = Now()
    lines = [str(now)]

    with open('/home/.log', 'a', encoding='utf-8') as file:
        file.writelines(lines)
