from __future__ import annotations

from fastapi import FastAPI

from app.core.database import database
from app.settings import get_settings
from app.v1.api import api_router


def get_application() -> FastAPI:
    """Base app configuration."""
    settings = get_settings()
    application = FastAPI(
        title=settings.project_name,
        debug=settings.debug,
        version=settings.app_version,
        docs_url=settings.docs_url,
    )
    application.include_router(api_router, prefix='/v1')

    @application.on_event('startup')
    async def startup() -> None:
        await database.connect()

    @application.on_event('shutdown')
    async def shutdown() -> None:
        await database.disconnect()

    return application


APP = get_application()
