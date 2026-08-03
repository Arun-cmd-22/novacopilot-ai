from sqlalchemy import Column, DateTime, Integer, SmallInteger
from sqlalchemy.sql import func

from app.database.database import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    status = Column(SmallInteger, default=1)

    created_at = Column(
        DateTime,
        server_default=func.now()
    )

    updated_at = Column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )