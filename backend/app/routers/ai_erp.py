from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.auth.permissions import has_permission

from app.schemas.ai_erp import (
    AIERPRequestSchema,
    AIERPResponseSchema,
)

from app.services.ai_erp_service import (
    AIERPService,
)

router = APIRouter(
    prefix="/api/v1/ai/erp",
    tags=["ERP Assistant"],
)


@router.post(
    "",
    response_model=AIERPResponseSchema,
)
def ask(
    data: AIERPRequestSchema,
    db: Session = Depends(get_db),
    current_user=Depends(
        has_permission("Use ERP Assistant")
    ),
):

    return AIERPService.ask(
        db,
        data.module,
        data.question,
    )