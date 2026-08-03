from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    Enum,
    ForeignKey,
    Text,
    DECIMAL,
    TIMESTAMP,
    text,
)

from sqlalchemy.orm import relationship

from app.database.database import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(
        BigInteger,
        primary_key=True,
        index=True,
    )

    session_id = Column(
        Integer,
        ForeignKey("chat_sessions.id"),
        nullable=False,
    )

    role = Column(
        Enum(
            "system",
            "user",
            "assistant",
            name="message_role",
        ),
        nullable=False,
    )

    message = Column(
        Text,
        nullable=False,
    )

    prompt_tokens = Column(
        Integer,
        default=0,
    )

    completion_tokens = Column(
        Integer,
        default=0,
    )

    total_tokens = Column(
        Integer,
        default=0,
    )

    response_time = Column(
        DECIMAL(10, 2),
        default=0,
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text("CURRENT_TIMESTAMP"),
    )

    chat_session = relationship(
        "ChatSession",
        back_populates="messages",
    )