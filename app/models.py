from __future__ import annotations

from datetime import datetime, timedelta

from pydantic import BaseModel
from pydantic.types import OptionalInt

from app.settings import ACCESS_TOKEN_EXPIRE_MINUTES


class User(BaseModel):
    pk: int
    username: str
    full_name: OptionalInt
    is_active: bool
    created_at: datetime


class UserIn(BaseModel):
    username: str
    password: str


class JWTMeta(BaseModel):
    iat: datetime = datetime.utcnow()
    exp: datetime = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    sub: str
    scope: str = 'access_token'


class JWTCredentials(BaseModel):
    pass


class JWTPayload(JWTMeta, JWTCredentials):
    pass
