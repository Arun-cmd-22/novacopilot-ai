from sqlalchemy.orm import Session

from app.services.ai_service import AIService


class AISQLService:

    @staticmethod
    def generate_sql(
        db: Session,
        database: str,
        prompt: str,
    ):

        template_map = {

            "MySQL": "SQL Generator",

            "PostgreSQL": "SQL Generator",

            "SQL Server": "SQL Generator",

        }

        template = template_map.get(
            database,
            "SQL Generator",
        )

        response = AIService.generate(

            db,

            template,

            prompt,

        )

        return {

            "response": response,

        }