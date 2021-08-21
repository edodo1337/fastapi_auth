from __future__ import annotations

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import TIMESTAMP, VARCHAR, Boolean, SmallInteger

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(SmallInteger)
    full_name = Column(String)
    created_at = Column(TIMESTAMP(timezone=True))
    is_active = Column(Boolean)
    salt = Column(VARCHAR(length=255))
    hashed_password = Column(VARCHAR(length=255))
