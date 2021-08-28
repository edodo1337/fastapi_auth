from __future__ import annotations

from datetime import datetime, timedelta
from typing import Optional

from pydantic import BaseModel

from app.settings import ACCESS_TOKEN_EXPIRE_MINUTES


class User(BaseModel):
    id: int
    username: str
    is_active: bool
    created_at: datetime
    salt: str
    hashed_password: str


class UserCreate(BaseModel):
    username: str
    is_active: bool
    salt: str
    hashed_password: str


class UserCreateRequest(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    pk: int
    username: str
    full_name: Optional[str]
    is_active: bool
    created_at: datetime


class UserIn(BaseModel):
    username: str
    password: str


class UserPassword(BaseModel):
    hashed_password: str
    salt: str


class JWTMeta(BaseModel):
    iat: datetime = datetime.utcnow()
    exp: datetime = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    sub: str
    scope: str = 'access_token'


class JWTCredentials(BaseModel):
    pass


class JWTPayload(JWTMeta, JWTCredentials):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str
