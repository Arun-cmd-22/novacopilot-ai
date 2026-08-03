from sqlalchemy.orm import Session

from app.services.ai_service import AIService


class AIERPService:

    @staticmethod
    def ask(
        db: Session,
        module: str,
        question: str,
    ):

        prompt = f"""
ERP Module:
{module}

Question:
{question}
"""

        response = AIService.generate(
            db,
            "ERP Assistant",
            prompt,
        )

        return {
            "response": response,
        }