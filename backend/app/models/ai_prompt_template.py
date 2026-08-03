from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    Text,
    TIMESTAMP,
    text,
)

from app.database.database import Base


class AIPromptTemplate(Base):
    __tablename__ = "ai_prompt_templates"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    name = Column(
        String(100),
        nullable=False,
        unique=True,
    )

    category = Column(
        String(100),
        nullable=False,
    )

    system_prompt = Column(
        Text,
        nullable=False,
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