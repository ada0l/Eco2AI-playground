from fastapi import FastAPI

from eco2ai_playground.api.handlers.webhook import webhook_router


def get_app():
    app = FastAPI()

    app.include_router(webhook_router, prefix="/webhook")
    return app


app = get_app()
