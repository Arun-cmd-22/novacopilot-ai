from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.auth.permissions import has_permission

from app.schemas.ai_sql import (
    AISQLRequestSchema,
    AISQLResponseSchema,
)

from app.services.ai_sql_service import AISQLService

router = APIRouter(
    prefix="/api/v1/ai/sql",
    tags=["AI SQL"],
)


@router.post(
    "",
    response_model=AISQLResponseSchema,
)
def generate_sql(
    data: AISQLRequestSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Use AI SQL")
    ),
):

    return AISQLService.generate_sql(
        db,
        data.database,
        data.prompt,
    )