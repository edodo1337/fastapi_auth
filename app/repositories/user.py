from __future__ import annotations

from datetime import datetime
from typing import Optional

from app.repositories.base import BaseRepository
from app.schemes import User, UserOut

users_mock = {
    1: User(
        pk=0,
        username='user1',
        full_name='name',
        is_active=True,
        created_at=datetime.utcnow(),
        salt='$2b$12$rRMDI9upKByWc7sawS1HDe',
        hashed_password='$2b$12$zdqQLQDnwmZnlxFV7ceLGeWcdbeLmYRQzlrKcrChjEAT9G3B7gVB.',
    )
}


class UserRepository(BaseRepository):
    def delete(self, pk: int) -> None:
        user = users_mock.get(pk)
        if user:
            del users_mock[pk]
        return None

    def get_by_id(self, pk: int) -> Optional[User]:
        user = users_mock.get(pk)
        return UserOut(**user.dict())

    def get_by_username(self, username: str) -> Optional[User]:
        filterd_users = list(filter(lambda x: x[1].username == username, users_mock.items()))
        if not bool(filterd_users):
            return None
        return filterd_users[0][1]

    def create(self, data: User) -> User:
        return UserOut(**data.dict())

    def update(self, pk: int, data: User) -> None:
        return None


def get_user_repository() -> UserRepository:
    return UserRepository()
