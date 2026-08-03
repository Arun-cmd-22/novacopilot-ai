from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    TIMESTAMP,
    text,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class ChatSession(Base):
    __tablename__ = "chat_sessions"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    ai_model_id = Column(
        Integer,
        ForeignKey("ai_models.id"),
        nullable=False,
    )

    title = Column(
        String(255),
        nullable=True,
    )

    status = Column(
        Boolean,
        default=True,
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    updated_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"),
    )

    user = relationship(
        "User",
        back_populates="chat_sessions",
    )

    ai_model = relationship(
        "AIModel",
        back_populates="chat_sessions",
    )

    messages = relationship(
        "Message",
        back_populates="chat_session",
        cascade="all, delete-orphan",
    )