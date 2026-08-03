from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.permissions import has_permission

from app.schemas.ai_debug import (
    AIDebugRequestSchema,
    AIDebugResponseSchema,
)

from app.services.ai_debug_service import (
    AIDebugService,
)

router = APIRouter(
    prefix="/api/v1/ai/debug",
    tags=["AI Debug"],
)


@router.post(
    "",
    response_model=AIDebugResponseSchema,
)
def debug(
    data: AIDebugRequestSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Use AI Debug")
    ),
):

    return AIDebugService.debug(
        db,
        data.language,
        data.code,
        data.error,
    )