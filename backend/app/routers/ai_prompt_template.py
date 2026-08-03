from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.permissions import has_permission
from app.database.database import get_db

from app.schemas.ai_prompt_template import (
    AIPromptTemplateSchema,
    AIPromptTemplateCreateSchema,
    AIPromptTemplateUpdateSchema,
    MessageSchema,
)

from app.services.ai_prompt_template_service import (
    AIPromptTemplateService,
)

router = APIRouter(
    prefix="/api/v1/ai-prompt-templates",
    tags=["AI Prompt Templates"],
)


@router.get(
    "",
    response_model=List[AIPromptTemplateSchema],
)
def get_prompt_templates(
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("View AI Prompt Template")
    ),
):

    return AIPromptTemplateService.get_prompt_templates(db)


@router.get(
    "/{template_id}",
    response_model=AIPromptTemplateSchema,
)
def get_prompt_template_by_id(
    template_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("View AI Prompt Template")
    ),
):

    return AIPromptTemplateService.get_prompt_template_by_id(
        db,
        template_id,
    )


@router.post(
    "",
    response_model=AIPromptTemplateSchema,
)
def create_prompt_template(
    data: AIPromptTemplateCreateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Create AI Prompt Template")
    ),
):

    return AIPromptTemplateService.create_prompt_template(
        db,
        data,
    )


@router.put(
    "/{template_id}",
    response_model=AIPromptTemplateSchema,
)
def update_prompt_template(
    template_id: int,
    data: AIPromptTemplateUpdateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Update AI Prompt Template")
    ),
):

    return AIPromptTemplateService.update_prompt_template(
        db,
        template_id,
        data,
    )


@router.delete(
    "/{template_id}",
    response_model=MessageSchema,
)
def delete_prompt_template(
    template_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Delete AI Prompt Template")
    ),
):

    return AIPromptTemplateService.delete_prompt_template(
        db,
        template_id,
    )