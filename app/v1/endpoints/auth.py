from __future__ import annotations

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from app.schemes import Token, UserIn
from app.services.auth import AuthException, AuthService

auth_router = APIRouter()


@auth_router.post('/signup')
def signup() -> JSONResponse:
    return 'Sign up endpoint'


@auth_router.post('/login')
def login(user_in: UserIn) -> Token:
    try:
        return AuthService().authenticate(user_in=user_in)
    except AuthException:
        raise HTTPException(status_code=400, detail='Login or password is not correct')


@auth_router.get('/refresh_token')
def refresh_token(token: str) -> JSONResponse:
    return 'Refresh token'


@auth_router.post('/secret')
def secret_data() -> JSONResponse:
    return 'Secret data'


@auth_router.get('/notsecret')
def not_secret_data() -> JSONResponse:
    return 'Not secret data'
