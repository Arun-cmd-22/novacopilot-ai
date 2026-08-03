from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Text,
    TIMESTAMP,
    text,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class AIModel(Base):
    __tablename__ = "ai_models"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    model_name = Column(
        String(100),
        nullable=False,
        unique=True,
    )

    display_name = Column(
        String(150),
        nullable=False,
    )

    provider = Column(
        String(100),
        nullable=False,
    )

    model_version = Column(
        String(100),
    )

    base_url = Column(
        String(255),
    )

    api_key = Column(
        Text,
    )

    is_local = Column(
        Boolean,
        default=True,
    )

    is_default = Column(
        Boolean,
        default=False,
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

    chat_sessions = relationship(
        "ChatSession",
        back_populates="ai_model",
    )