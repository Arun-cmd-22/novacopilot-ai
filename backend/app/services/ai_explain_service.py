from sqlalchemy.orm import Session

from app.services.ai_service import AIService


class AIExplainService:

    @staticmethod
    def explain(
        db: Session,
        language: str,
        code: str,
    ):

        prompt = f"""
Language:
{language}

Code:

{code}
"""

        response = AIService.generate(
            db,
            "Explain Code",
            prompt,
        )

        return {
            "response": response,
        }