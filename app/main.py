from __future__ import annotations

from fastapi import FastAPI

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
    return application


APP = get_application()
