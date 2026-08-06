from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.auth.dependencies import get_current_user

from app.schemas.chat import (
    ChatRequestSchema,
    ChatResponseSchema,
)

from app.services.chat_service import ChatService

router = APIRouter(
    prefix="/api/v1/chat",
    tags=["AI Chat"],
)


@router.post(
    "",
    response_model=ChatResponseSchema,
)
def chat(
    data: ChatRequestSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return ChatService.chat(
        db=db,
        session_id=data.session_id,
        message=data.message,
        user_id=current_user.id,
    )


@router.post(
    "/stream",
)
def chat_stream(
    data: ChatRequestSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> StreamingResponse:

    return ChatService.chat_stream(
        db=db,
        session_id=data.session_id,
        message=data.message,
        user_id=current_user.id,
    )