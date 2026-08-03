from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.auth.permissions import has_permission

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
    current_user=Depends(
        has_permission("AI Chat")
    ),
):

    return ChatService.chat(
        db=db,
        session_id=data.session_id,
        message=data.message,
        user_id=current_user.id,
    )
