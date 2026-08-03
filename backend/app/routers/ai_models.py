from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.permissions import has_permission
from app.database.database import get_db

from app.schemas.ai_model import (
    AIModelSchema,
    AIModelCreateSchema,
    AIModelUpdateSchema,
    MessageSchema,
)

from app.services.ai_model_service import AIModelService

router = APIRouter(
    prefix="/api/v1/ai-models",
    tags=["AI Models"],
)


@router.get(
    "",
    response_model=List[AIModelSchema],
)
def get_ai_models(
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("View AI Model")),
):

    return AIModelService.get_ai_models(db)


# -----------------------------
# Installed Models (Ollama)
# -----------------------------
@router.get(
    "/installed",
)
def get_installed_models(
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("View AI Model")),
):

    return AIModelService.get_installed_models(db)


@router.get(
    "/{model_id}",
    response_model=AIModelSchema,
)
def get_ai_model_by_id(
    model_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("View AI Model")),
):

    return AIModelService.get_ai_model_by_id(
        db,
        model_id,
    )


@router.post(
    "",
    response_model=AIModelSchema,
)
def create_ai_model(
    data: AIModelCreateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Create AI Model")),
):

    return AIModelService.create_ai_model(
        db,
        data,
    )


@router.put(
    "/{model_id}",
    response_model=AIModelSchema,
)
def update_ai_model(
    model_id: int,
    data: AIModelUpdateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Update AI Model")),
):

    return AIModelService.update_ai_model(
        db,
        model_id,
        data,
    )


@router.delete(
    "/{model_id}",
    response_model=MessageSchema,
)
def delete_ai_model(
    model_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Delete AI Model")),
):

    return AIModelService.delete_ai_model(
        db,
        model_id,
    )