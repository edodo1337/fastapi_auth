from __future__ import annotations

from fastapi import APIRouter

from app.v1.endpoints.auth import auth_router
from app.v1.endpoints.root import root_router

api_router = APIRouter()

api_router.include_router(root_router, prefix='', tags=['root'])
api_router.include_router(auth_router, prefix='', tags=['root'])
