from __future__ import annotations

from fastapi import APIRouter
from starlette.responses import JSONResponse

from app.services.auth import AuthFacade

auth_router = APIRouter()


@auth_router.post('/signup')
def signup() -> JSONResponse:
    return 'Sign up endpoint'


@auth_router.post('/login')
def login(username: str) -> JSONResponse:
    return AuthFacade().encode_token(username=username)


@auth_router.get('/refresh_token')
def refresh_token(token: str) -> JSONResponse:
    return 'Refresh token'


@auth_router.post('/secret')
def secret_data() -> JSONResponse:
    return 'Secret data'


@auth_router.get('/notsecret')
def not_secret_data() -> JSONResponse:
    return 'Not secret data'
