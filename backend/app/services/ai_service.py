from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.models.ai_model import AIModel
from app.models.ai_prompt_template import AIPromptTemplate

from app.services.ollama_service import OllamaService


class AIService:

    @staticmethod
    def generate(
        db: Session,
        template_name: str,
        prompt: str,
    ):

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

        template = (
            db.query(AIPromptTemplate)
            .filter(
                AIPromptTemplate.name == template_name,
                AIPromptTemplate.status == True,
            )
            .first()
        )

        if not template:

            raise HTTPException(
                status_code=404,
                detail="Prompt Template Not Found",
            )

        messages = [

            {
                "role": "system",
                "content": template.system_prompt,
            },

            {
                "role": "user",
                "content": prompt,
            },

        ]

        result = OllamaService.chat(
            model.base_url,
            model.model_name,
            messages,
        )

        return result["message"]["content"]