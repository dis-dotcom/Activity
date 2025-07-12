from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from DateTime import Now

app = FastAPI()


@app.get("/", response_class=PlainTextResponse)
async def root():
    return "❤"


@app.get("/")
async def log():
    now = Now()
    lines = [str(now)]

    with open('/home/.log', 'a', encoding='utf-8') as file:
        file.writelines(lines)

    with open('/opt/build/index.html', 'a', encoding='utf-8') as file:
        content = file.read()

    return content


@app.get("/api/logs")
async def log():
    with open('/home/.log', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    return {
        items: lines
    }
