from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.ai_prompt_template import AIPromptTemplate
from app.schemas.ai_prompt_template import (
    AIPromptTemplateCreateSchema,
    AIPromptTemplateUpdateSchema,
)


class AIPromptTemplateService:

    @staticmethod
    def get_prompt_templates(
        db: Session,
    ):

        return (
            db.query(AIPromptTemplate)
            .all()
        )

    @staticmethod
    def get_prompt_template_by_id(
        db: Session,
        template_id: int,
    ):

        prompt_template = (
            db.query(AIPromptTemplate)
            .filter(
                AIPromptTemplate.id == template_id
            )
            .first()
        )

        if not prompt_template:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="AI Prompt Template Not Found",
            )

        return prompt_template

    @staticmethod
    def create_prompt_template(
        db: Session,
        data: AIPromptTemplateCreateSchema,
    ):

        exists = (
            db.query(AIPromptTemplate)
            .filter(
                AIPromptTemplate.name == data.name
            )
            .first()
        )

        if exists:

            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="AI Prompt Template Already Exists",
            )

        prompt_template = AIPromptTemplate(
            name=data.name,
            category=data.category,
            system_prompt=data.system_prompt,
            status=data.status,
        )

        db.add(prompt_template)
        db.commit()
        db.refresh(prompt_template)

        return prompt_template

    @staticmethod
    def update_prompt_template(
        db: Session,
        template_id: int,
        data: AIPromptTemplateUpdateSchema,
    ):

        prompt_template = (
            db.query(AIPromptTemplate)
            .filter(
                AIPromptTemplate.id == template_id
            )
            .first()
        )

        if not prompt_template:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="AI Prompt Template Not Found",
            )

        prompt_template.name = data.name
        prompt_template.category = data.category
        prompt_template.system_prompt = data.system_prompt
        prompt_template.status = data.status

        db.commit()
        db.refresh(prompt_template)

        return prompt_template

    @staticmethod
    def delete_prompt_template(
        db: Session,
        template_id: int,
    ):

        prompt_template = (
            db.query(AIPromptTemplate)
            .filter(
                AIPromptTemplate.id == template_id
            )
            .first()
        )

        if not prompt_template:

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="AI Prompt Template Not Found",
            )

        db.delete(prompt_template)
        db.commit()

        return {
            "success": True,
            "message": "AI Prompt Template Deleted Successfully",
        }