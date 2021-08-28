from __future__ import annotations

from typing import Optional
from asyncpg.exceptions import UniqueViolationError

from app.repositories.base import BaseRepository
from app.schemes import User, UserCreate


class UserUniqueException(BaseException):
    pass


class UsersRepository(BaseRepository):
    def delete(self, pk: int) -> None:
        pass

    def get_by_id(self, pk: int) -> Optional[User]:
        pass

    async def get_by_username(self, username: str) -> Optional[User]:
        query = 'SELECT * FROM users WHERE username = :username LIMIT 1'
        values = {'username': username}
        data = await self.db.fetch_one(query=query, values=values)
        if data is None:
            return None
        return User(**data)

    async def create(self, data: UserCreate) -> User:
        query = (
            'INSERT INTO users(username, is_active, salt, hashed_password) '
            'VALUES (:username, :is_active, :salt, :hashed_password)'
        )
        try:
            data = await self.db.execute(query=query, values=data.dict())
        except UniqueViolationError:
            raise UserUniqueException
        return data

    def update(self, pk: int, data: User) -> None:
        return None
