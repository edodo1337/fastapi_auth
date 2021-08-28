from __future__ import annotations

from sqlalchemy import Column, Integer
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.sqltypes import TIMESTAMP, VARCHAR, Boolean

from app.core.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True, nullable=False, unique=True)
    username = Column(VARCHAR(length=255), unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.NOW(), nullable=False)
    is_active = Column(Boolean, default=True)
    salt = Column(VARCHAR(length=255), nullable=False)
    hashed_password = Column(VARCHAR(length=255), nullable=False)
