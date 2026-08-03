from sqlalchemy.orm import Session

from app.services.ai_service import AIService


class AIDebugService:

    @staticmethod
    def debug(
        db: Session,
        language: str,
        code: str,
        error: str,
    ):

        prompt = f"""
Language:
{language}

Error:
{error}

Code:

{code}
"""

        response = AIService.generate(
            db,
            "Debug Code",
            prompt,
        )

        return {
            "response": response,
        }