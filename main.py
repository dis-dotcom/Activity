from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from DateTime import Now
from index import index as indexPage

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def index():
    log_activity()

    return indexPage


@app.get("/api/version")
async def version():
    return {
        'version': '0.0.0.1'
    }

'''
@app.get("/api/logs")
async def log():
    #with open('/home/.log', 'r', encoding='utf-8') as file:
    #    lines = file.readlines()

    return {
        lines: 1
    }
'''

def log_activity():
    now = Now()

    with open('/home/.log', 'a', encoding='utf-8') as file:
        file.writelines([str(now)])
