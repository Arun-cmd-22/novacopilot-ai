from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.message import Message
from app.schemas.message import (
    MessageCreateSchema,
    MessageUpdateSchema,
)


class MessageService:

    @staticmethod
    def get_messages(
        db: Session,
    ):

        return (
            db.query(Message)
            .order_by(Message.created_at.asc())
            .all()
        )

    @staticmethod
    def get_message_by_id(
        db: Session,
        message_id: int,
    ):

        message = (
            db.query(Message)
            .filter(
                Message.id == message_id
            )
            .first()
        )

        if not message:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Message Not Found",
            )

        return message

    @staticmethod
    def get_messages_by_session(
        db: Session,
        session_id: int,
    ):

        return (
            db.query(Message)
            .filter(
                Message.session_id == session_id
            )
            .order_by(Message.created_at.asc())
            .all()
        )

    @staticmethod
    def create_message(
        db: Session,
        data: MessageCreateSchema,
    ):

        message = Message(
            session_id=data.session_id,
            role=data.role,
            message=data.message,
        )

        db.add(message)
        db.commit()
        db.refresh(message)

        return message

    @staticmethod
    def update_message(
        db: Session,
        message_id: int,
        data: MessageUpdateSchema,
    ):

        message = (
            db.query(Message)
            .filter(
                Message.id == message_id
            )
            .first()
        )

        if not message:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Message Not Found",
            )

        message.role = data.role
        message.message = data.message

        db.commit()
        db.refresh(message)

        return message

    @staticmethod
    def delete_message(
        db: Session,
        message_id: int,
    ):

        message = (
            db.query(Message)
            .filter(
                Message.id == message_id
            )
            .first()
        )

        if not message:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Message Not Found",
            )

        db.delete(message)
        db.commit()

        return {
            "success": True,
            "message": "Message Deleted Successfully",
        }