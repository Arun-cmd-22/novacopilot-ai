from sqlalchemy.orm import Session

from app.services.ai_service import AIService


class AICodeService:

    @staticmethod
    def generate_code(
        db: Session,
        language: str,
        prompt: str,
    ):

        template_map = {

            "FastAPI": "FastAPI Generator",

            "Next.js": "Next.js Generator",

            "Python": "FastAPI Generator",

        }

        template = template_map.get(
            language,
            "FastAPI Generator",
        )

        response = AIService.generate(

            db,

            template,

            prompt,

        )

        return {

            "response": response,

        }