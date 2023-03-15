import logging

from fastapi import FastAPI, Request

app = FastAPI()


@app.post("/webhook")
async def webhook(request: Request):
    data = await request.body()
    logger = logging.getLogger("uvicorn.info")
    logger.info(data)
    return {}
