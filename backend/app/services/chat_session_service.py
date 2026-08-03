from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.chat_session import ChatSession
from app.schemas.chat_session import (
    ChatSessionCreateSchema,
    ChatSessionUpdateSchema,
)


class ChatSessionService:

    @staticmethod
    def get_chat_sessions(
        db: Session,
    ):

        return (
            db.query(ChatSession)
            .all()
        )

    @staticmethod
    def get_chat_session_by_id(
        db: Session,
        session_id: int,
    ):

        chat_session = (
            db.query(ChatSession)
            .filter(
                ChatSession.id == session_id
            )
            .first()
        )

        if not chat_session:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Chat Session Not Found",
            )

        return chat_session

    @staticmethod
    def create_chat_session(
        db: Session,
        user_id: int,
        data: ChatSessionCreateSchema,
    ):

        chat_session = ChatSession(
            user_id=user_id,
            ai_model_id=data.ai_model_id,
            title=data.title,
            status=True,
        )

        db.add(chat_session)
        db.commit()
        db.refresh(chat_session)

        return chat_session

    @staticmethod
    def update_chat_session(
        db: Session,
        session_id: int,
        data: ChatSessionUpdateSchema,
    ):

        chat_session = (
            db.query(ChatSession)
            .filter(
                ChatSession.id == session_id
            )
            .first()
        )

        if not chat_session:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Chat Session Not Found",
            )

        chat_session.ai_model_id = data.ai_model_id
        chat_session.title = data.title
        chat_session.status = data.status

        db.commit()
        db.refresh(chat_session)

        return chat_session

    @staticmethod
    def delete_chat_session(
        db: Session,
        session_id: int,
    ):

        chat_session = (
            db.query(ChatSession)
            .filter(
                ChatSession.id == session_id
            )
            .first()
        )

        if not chat_session:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Chat Session Not Found",
            )

        db.delete(chat_session)
        db.commit()

        return {
            "success": True,
            "message": "Chat Session Deleted Successfully",
        }