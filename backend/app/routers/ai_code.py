from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.database.database import get_db

from app.auth.permissions import has_permission

from app.schemas.ai_code import (

    AICodeRequestSchema,

    AICodeResponseSchema,

)

from app.services.ai_code_service import (

    AICodeService,

)

router = APIRouter(

    prefix="/api/v1/ai/code",

    tags=["AI Code"],

)


@router.post(

    "",

    response_model=AICodeResponseSchema,

)
def generate_code(

    data: AICodeRequestSchema,

    db: Session = Depends(get_db),

    current_user=Depends(

        has_permission("Use AI Code")

    ),

):

    return AICodeService.generate_code(

        db,

        data.language,

        data.prompt,

    )