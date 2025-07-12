from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from DateTime import Now
from index import index
app = FastAPI()


@app.get("/")
async def log():
    now = Now()
    lines = [str(now)]

    with open('/home/.log', 'a', encoding='utf-8') as file:
        file.writelines(lines)

    return index


@app.get("/api/logs")
async def log():
    with open('/home/.log', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return {
        items: lines
    }
