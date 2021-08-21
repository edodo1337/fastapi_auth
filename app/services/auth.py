from __future__ import annotations

import jwt
from fastapi import HTTPException
from passlib.context import CryptContext

from app import settings
from app.models import JWTPayload


class AuthFacade:
    hasher = CryptContext(schemes=['bcrypt'])
    secret = settings.SECRET

    def encode_password(self, password: str) -> str:
        return self.hasher.hash(password)

    def verify_password(self, password: str, encoded_password: str) -> bool:
        return self.hasher.verify(password, encoded_password)

    def encode_token(self, username: str) -> str:
        payload = JWTPayload(scope='access_token', sub=username)
        return jwt.encode(payload=payload.dict(), key=self.secret, algorithm='HS256')

    def decode_token(self, token: str) -> JWTPayload:
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return JWTPayload(**payload)

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')
