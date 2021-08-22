from __future__ import annotations

import databases
from sqlalchemy.ext.declarative import declarative_base

from app.settings import DATABASE_URL

database = databases.Database(DATABASE_URL)
Base = declarative_base()
