from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    role_id = Column(
        ForeignKey("roles.id"),
        nullable=False
    )

    full_name = Column(
        String(150),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )

    mobile = Column(String(20))

    profile_image = Column(String(255))

    last_login = Column(DateTime)

    role = relationship(
        "Role",
        back_populates="users"
    )

    chat_sessions = relationship(
        "ChatSession",
        back_populates="user",
    )
