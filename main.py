import Logger
import LogActivityJob

from Secret import get
from S3 import S3
from VK import VK
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from apscheduler.schedulers.background import BackgroundScheduler

settings = {
    'vk': {
        'token': get('token')
    },
    's3': {
        'bucket': get('s3_bucket_name'),
        'access_key': get('s3_access_key'),
        'secret_access_key': get('s3_secret_access_key'),
        'region_name': 'ru-1'
    }
}

vk, s3 = VK(settings), S3(settings)

scheduler = BackgroundScheduler()
scheduler.add_job(lambda: LogActivityJob.run(vk, s3), 'interval', minutes=1)
scheduler.start()

app = FastAPI()


@app.get("/logs")
async def logs():
    async def content():
        yield """
            <!DOCTYPE html>
            <html>
            <head>
                <title>Постепенная загрузка</title>
            </head>
            <body>
                <ul style="font-family: monospace">
        """

        for message in Logger.Logger.logs:
            yield "<li>"
            yield message
            yield "</li>"

        yield """
                </ul>
            </body>
            </html>
        """

    return StreamingResponse(
        content(),
        media_type="text/html"
    )

