import time

from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.models.ai_model import AIModel
from app.models.chat_session import ChatSession
from app.models.message import Message

from app.services.ollama_service import OllamaService


class ChatService:

    # ==========================================================
    # NORMAL CHAT
    # ==========================================================

    @staticmethod
    def chat(
        db: Session,
        session_id: int | None,
        message: str,
        user_id: int,
    ):
        # ------------------------------------------------------
        # Get default AI model
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # Create new session
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # Existing session
        # ------------------------------------------------------

        else:

            chat_session = (
                db.query(ChatSession)
                .filter(
                    ChatSession.id == session_id,
                    ChatSession.status == True,
                    ChatSession.user_id == user_id,
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

        # ------------------------------------------------------
        # Get previous messages
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # Add current user message to history
        # ------------------------------------------------------

        history.append(
            {
                "role": "user",
                "content": message,
            }
        )

        # ------------------------------------------------------
        # Call Ollama
        # ------------------------------------------------------

        start_time = time.time()

        result = OllamaService.chat(
            model.base_url,
            model.model_name,
            history,
        )

        response_time = round(
            time.time() - start_time,
            2,
        )

        ai_response = result["message"]["content"]

        # ------------------------------------------------------
        # Save user message
        # ------------------------------------------------------

        user_message = Message(
            session_id=session_id,
            role="user",
            message=message,
        )

        db.add(user_message)

        # ------------------------------------------------------
        # Save assistant message
        # ------------------------------------------------------

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

    # ==========================================================
    # STREAMING CHAT
    # ==========================================================

    @staticmethod
    def chat_stream(
        db: Session,
        session_id: int | None,
        message: str,
        user_id: int,
    ):

        # ------------------------------------------------------
        # Get default model
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # Create new session
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # Existing session
        # ------------------------------------------------------

        else:

            chat_session = (
                db.query(ChatSession)
                .filter(
                    ChatSession.id == session_id,
                    ChatSession.status == True,
                    ChatSession.user_id == user_id,
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

        # ------------------------------------------------------
        # Get previous conversation
        # ------------------------------------------------------

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

        # ------------------------------------------------------
        # Add current message
        # ------------------------------------------------------

        history.append(
            {
                "role": "user",
                "content": message,
            }
        )

        # ------------------------------------------------------
        # Save user message
        # ------------------------------------------------------

        user_message = Message(
            session_id=session_id,
            role="user",
            message=message,
        )

        db.add(user_message)
        db.commit()

        # ------------------------------------------------------
        # Start Ollama streaming
        # ------------------------------------------------------

        stream = OllamaService.chat_stream(
            model.base_url,
            model.model_name,
            history,
        )

        def generate():

            start_time = time.time()

            full_response = ""

            try:

                for token in stream:

                    if not token:
                        continue

                    full_response += token

                    # Send token immediately
                    yield token

                # --------------------------------------------------
                # Save complete response
                # --------------------------------------------------

                response_time = round(
                    time.time() - start_time,
                    2,
                )

                assistant_message = Message(
                    session_id=session_id,
                    role="assistant",
                    message=full_response,
                    prompt_tokens=0,
                    completion_tokens=0,
                    total_tokens=0,
                    response_time=response_time,
                )

                db.add(assistant_message)
                db.commit()

            except Exception:

                db.rollback()

                raise

        return StreamingResponse(
            generate(),
            media_type="text/plain; charset=utf-8",
            headers={
                "Cache-Control": "no-cache",
                "X-Accel-Buffering": "no",
                "X-Session-Id": str(session_id),
            },
        )