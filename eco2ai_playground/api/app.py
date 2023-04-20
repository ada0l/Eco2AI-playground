from fastapi import FastAPI

from eco2ai_playground.api.broadcaster import broadcaster
from eco2ai_playground.api.handlers.project import project_router
from eco2ai_playground.api.handlers.webhook import webhook_router
from eco2ai_playground.api.handlers.ws import ws_starlette_routes


def get_app():
    app = FastAPI(
        on_startup=[broadcaster.connect],
        on_shutdown=[broadcaster.disconnect],
        routes=ws_starlette_routes,
    )

    app.include_router(webhook_router, prefix="/webhook")
    app.include_router(project_router, prefix="/project")

    return app


app = get_app()
