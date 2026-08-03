from sqlalchemy import Column, String

from app.models.base import BaseModel


class Permission(BaseModel):
    __tablename__ = "permissions"

    permission_name = Column(
        String(150),
        unique=True,
        nullable=False
    )

    module_name = Column(String(100))