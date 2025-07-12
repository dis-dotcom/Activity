import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, PlainTextResponse
from DateTime import Now
from index import index as index_page

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    log_activity()

    return index_page


@app.get("/api/version")
async def version():
    return {
        'version': '0.0.0.1',
        's': os.getenv('token')
    }


@app.get("/api/logs")
async def log():
    with open('/home/.log', 'r', encoding='utf-8') as file:
        content = file.readlines()

    return {
        'lines': content
    }


def log_activity():
    now = str(Now()) + '\n'

    with open('/home/.log', 'a', encoding='utf-8') as file:
        file.write(now)
