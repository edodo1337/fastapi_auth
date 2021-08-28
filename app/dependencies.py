from __future__ import annotations

from typing import Callable, Type
from databases import Database

from fastapi import Depends
from starlette.requests import Request

from app.repositories.base import BaseRepository
from app.services.auth import AuthService


def get_database(request: Request) -> Database:
    return request.app.state._db


def get_repository(repo_cls: Type[BaseRepository]) -> Callable:
    def get_repo(db: Database = Depends(get_database)) -> Type[BaseRepository]:
        return repo_cls(db)

    return get_repo


def get_auth_service() -> Callable:
    def get_service() -> Type[AuthService]:
        return AuthService()

    return get_service
