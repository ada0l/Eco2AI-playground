from fastapi import FastAPI

from eco2ai_playground.api.handlers.project import project_router
from eco2ai_playground.api.handlers.webhook import webhook_router


def get_app():
    app = FastAPI()

    app.include_router(webhook_router, prefix="/webhook")
    app.include_router(project_router, prefix="/project")
    return app


app = get_app()
