from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.permissions import has_permission
from app.database.database import get_db

from app.schemas.message import (
    MessageSchema,
    MessageCreateSchema,
    MessageUpdateSchema,
    ResponseSchema,
)

from app.services.message_service import MessageService

router = APIRouter(
    prefix="/api/v1/messages",
    tags=["Messages"],
)


@router.get(
    "",
    response_model=List[MessageSchema],
)
def get_messages(
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("View Message")
    ),
):

    return MessageService.get_messages(db)


@router.get(
    "/{message_id}",
    response_model=MessageSchema,
)
def get_message_by_id(
    message_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("View Message")
    ),
):

    return MessageService.get_message_by_id(
        db,
        message_id,
    )


@router.get(
    "/session/{session_id}",
    response_model=List[MessageSchema],
)
def get_messages_by_session(
    session_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("View Message")
    ),
):

    return MessageService.get_messages_by_session(
        db,
        session_id,
    )


@router.post(
    "",
    response_model=MessageSchema,
)
def create_message(
    data: MessageCreateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Create Message")
    ),
):

    return MessageService.create_message(
        db,
        data,
    )


@router.put(
    "/{message_id}",
    response_model=MessageSchema,
)
def update_message(
    message_id: int,
    data: MessageUpdateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Update Message")
    ),
):

    return MessageService.update_message(
        db,
        message_id,
        data,
    )


@router.delete(
    "/{message_id}",
    response_model=ResponseSchema,
)
def delete_message(
    message_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Delete Message")
    ),
):

    return MessageService.delete_message(
        db,
        message_id,
    )