from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.ai_model import AIModel
from app.schemas.ai_model import (
    AIModelCreateSchema,
    AIModelUpdateSchema,
)
from app.services.ollama_service import OllamaService


class AIModelService:

    @staticmethod
    def get_ai_models(db: Session):

        return (
            db.query(AIModel)
            .all()
        )

    @staticmethod
    def get_installed_models(db: Session):

        ai_model = (
            db.query(AIModel)
            .filter(
                AIModel.is_default == True,
                AIModel.status == True,
            )
            .first()
        )

        if not ai_model:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Default AI Model Not Found",
            )

        return OllamaService.get_installed_models(
            ai_model.base_url
        )

    @staticmethod
    def get_ai_model_by_id(
        db: Session,
        model_id: int,
    ):

        ai_model = (
            db.query(AIModel)
            .filter(AIModel.id == model_id)
            .first()
        )

        if not ai_model:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="AI Model Not Found",
            )

        return ai_model

    @staticmethod
    def create_ai_model(
        db: Session,
        data: AIModelCreateSchema,
    ):

        exists = (
            db.query(AIModel)
            .filter(
                AIModel.model_name == data.model_name
            )
            .first()
        )

        if exists:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="AI Model Already Exists",
            )

        if data.is_default:
            (
                db.query(AIModel)
                .update(
                    {
                        AIModel.is_default: False
                    }
                )
            )

        ai_model = AIModel(
            model_name=data.model_name,
            display_name=data.display_name,
            provider=data.provider,
            model_version=data.model_version,
            base_url=data.base_url,
            api_key=data.api_key,
            is_local=data.is_local,
            is_default=data.is_default,
            status=data.status,
        )

        db.add(ai_model)
        db.commit()
        db.refresh(ai_model)

        return ai_model

    @staticmethod
    def update_ai_model(
        db: Session,
        model_id: int,
        data: AIModelUpdateSchema,
    ):

        ai_model = (
            db.query(AIModel)
            .filter(AIModel.id == model_id)
            .first()
        )

        if not ai_model:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="AI Model Not Found",
            )

        if data.is_default:
            (
                db.query(AIModel)
                .update(
                    {
                        AIModel.is_default: False
                    }
                )
            )

        ai_model.model_name = data.model_name
        ai_model.display_name = data.display_name
        ai_model.provider = data.provider
        ai_model.model_version = data.model_version
        ai_model.base_url = data.base_url
        ai_model.api_key = data.api_key
        ai_model.is_local = data.is_local
        ai_model.is_default = data.is_default
        ai_model.status = data.status

        db.commit()
        db.refresh(ai_model)

        return ai_model

    @staticmethod
    def delete_ai_model(
        db: Session,
        model_id: int,
    ):

        ai_model = (
            db.query(AIModel)
            .filter(AIModel.id == model_id)
            .first()
        )

        if not ai_model:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="AI Model Not Found",
            )

        db.delete(ai_model)
        db.commit()

        return {
            "success": True,
            "message": "AI Model Deleted Successfully",
        }