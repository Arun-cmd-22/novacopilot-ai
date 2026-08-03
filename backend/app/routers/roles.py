from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.permissions import has_permission
from app.database.database import get_db

from app.schemas.role import (
    RoleSchema,
    RoleCreateSchema,
    RoleUpdateSchema,
    MessageSchema,
)

from app.services.role_service import RoleService

router = APIRouter(
    prefix="/api/v1/roles",
    tags=["Roles"],
)


@router.get(
    "",
    response_model=List[RoleSchema],
)
def get_roles(
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("View Role")),
):

    return RoleService.get_roles(db)


@router.get(
    "/{role_id}",
    response_model=RoleSchema,
)
def get_role_by_id(
    role_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("View Role")),
):

    return RoleService.get_role_by_id(
        db,
        role_id,
    )


@router.post(
    "",
    response_model=RoleSchema,
)
def create_role(
    data: RoleCreateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Create Role")),
):

    return RoleService.create_role(
        db,
        data,
    )


@router.put(
    "/{role_id}",
    response_model=RoleSchema,
)
def update_role(
    role_id: int,
    data: RoleUpdateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Update Role")),
):

    return RoleService.update_role(
        db,
        role_id,
        data,
    )


@router.delete(
    "/{role_id}",
    response_model=MessageSchema,
)
def delete_role(
    role_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Delete Role")),
):

    return RoleService.delete_role(
        db,
        role_id,
    )