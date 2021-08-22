from __future__ import annotations

from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from app.schemes import Token, UserIn
from app.services.auth import AuthException, AuthService

auth_router = APIRouter()


@auth_router.post('/signup')
async def signup() -> JSONResponse:
    return 'Sign up endpoint'


@auth_router.post('/login')
async def login(user_in: UserIn) -> Token:
    try:
        return AuthService().authenticate(user_in=user_in)
    except AuthException:
        raise HTTPException(status_code=400, detail='Login or password is not correct')


@auth_router.get('/refresh_token')
async def refresh_token(token: str) -> JSONResponse:
    from app.core.database import database

    query = 'SELECT * FROM users;'
    rows = await database.fetch_all(query=query)
    return rows
    # return 'Refresh token'


@auth_router.post('/secret')
async def secret_data() -> JSONResponse:
    return 'Secret data'


@auth_router.get('/notsecret')
async def not_secret_data() -> JSONResponse:
    return 'Not secret data'
