from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Role(BaseModel):
    __tablename__ = "roles"

    role_name = Column(String(100), unique=True, nullable=False)

    description = Column(String(255))

    users = relationship(
        "User",
        back_populates="role"
    )