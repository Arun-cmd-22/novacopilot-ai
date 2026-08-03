from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.permissions import has_permission

from app.schemas.ai_explain import (
    AIExplainRequestSchema,
    AIExplainResponseSchema,
)

from app.services.ai_explain_service import (
    AIExplainService,
)

router = APIRouter(
    prefix="/api/v1/ai/explain",
    tags=["AI Explain"],
)


@router.post(
    "",
    response_model=AIExplainResponseSchema,
)
def explain(
    data: AIExplainRequestSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Use AI Explain")
    ),
):

    return AIExplainService.explain(
        db,
        data.language,
        data.code,
    )