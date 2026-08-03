from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.auth.permissions import has_permission

from app.database.database import get_db

from app.schemas.chat_session import (
    ChatSessionSchema,
    ChatSessionCreateSchema,
    ChatSessionUpdateSchema,
    MessageSchema,
)

from app.services.chat_session_service import ChatSessionService

router = APIRouter(
    prefix="/api/v1/chat-sessions",
    tags=["Chat Sessions"],
)


@router.get(
    "",
    response_model=List[ChatSessionSchema],
)
def get_chat_sessions(
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("View Chat Session")
    ),
):

    return ChatSessionService.get_chat_sessions(db)


@router.get(
    "/{session_id}",
    response_model=ChatSessionSchema,
)
def get_chat_session_by_id(
    session_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("View Chat Session")
    ),
):

    return ChatSessionService.get_chat_session_by_id(
        db,
        session_id,
    )


@router.post(
    "",
    response_model=ChatSessionSchema,
)
def create_chat_session(
    data: ChatSessionCreateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Create Chat Session")
    ),
):

    return ChatSessionService.create_chat_session(
        db,
        current_user.id,
        data,
    )


@router.put(
    "/{session_id}",
    response_model=ChatSessionSchema,
)
def update_chat_session(
    session_id: int,
    data: ChatSessionUpdateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Update Chat Session")
    ),
):

    return ChatSessionService.update_chat_session(
        db,
        session_id,
        data,
    )


@router.delete(
    "/{session_id}",
    response_model=MessageSchema,
)
def delete_chat_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Delete Chat Session")
    ),
):

    return ChatSessionService.delete_chat_session(
        db,
        session_id,
    )