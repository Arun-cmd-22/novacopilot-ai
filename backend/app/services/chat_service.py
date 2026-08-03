import time

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.ai_model import AIModel
from app.models.chat_session import ChatSession
from app.models.message import Message

from app.services.ollama_service import OllamaService


class ChatService:

    @staticmethod
    def chat(
        db: Session,
        session_id: int | None,
        message: str,
        user_id: int = 1,
    ):

        # Get Default AI Model
        model = (
            db.query(AIModel)
            .filter(
                AIModel.is_default == True,
                AIModel.status == True,
            )
            .first()
        )

        if not model:

            raise HTTPException(
                status_code=404,
                detail="Default AI Model Not Found",
            )

        # Create New Session Automatically
        if session_id is None:

            chat_session = ChatSession(
                user_id=user_id,
                ai_model_id=model.id,
                title=message[:50],
                status=True,
            )

            db.add(chat_session)
            db.commit()
            db.refresh(chat_session)

            session_id = chat_session.id

        else:

            chat_session = (
                db.query(ChatSession)
                .filter(
                    ChatSession.id == session_id,
                    ChatSession.status == True,
                )
                .first()
            )

            if not chat_session:

                raise HTTPException(
                    status_code=404,
                    detail="Chat Session Not Found",
                )

            model = (
                db.query(AIModel)
                .filter(
                    AIModel.id == chat_session.ai_model_id,
                    AIModel.status == True,
                )
                .first()
            )

            if not model:

                raise HTTPException(
                    status_code=404,
                    detail="AI Model Not Found",
                )

        previous_messages = (
            db.query(Message)
            .filter(
                Message.session_id == session_id
            )
            .order_by(
                Message.created_at.asc()
            )
            .all()
        )

        history = []

        for item in previous_messages:

            history.append(
                {
                    "role": item.role,
                    "content": item.message,
                }
            )

        history.append(
            {
                "role": "user",
                "content": message,
            }
        )

        start_time = time.time()

        result = OllamaService.chat(
            model.base_url,
            model.model_name,
            history,
        )

        end_time = time.time()

        response_time = round(
            end_time - start_time,
            2,
        )

        ai_response = result["message"]["content"]

        user_message = Message(
            session_id=session_id,
            role="user",
            message=message,
        )

        db.add(user_message)

        assistant_message = Message(
            session_id=session_id,
            role="assistant",
            message=ai_response,
            prompt_tokens=0,
            completion_tokens=0,
            total_tokens=0,
            response_time=response_time,
        )

        db.add(assistant_message)

        db.commit()

        return {
            "session_id": session_id,
            "response": ai_response,
            "response_time": response_time,
        }