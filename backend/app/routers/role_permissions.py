from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db

from app.schemas.role_permission import (
    RolePermissionSchema,
    RolePermissionCreateSchema,
    RolePermissionUpdateSchema,
    MessageSchema,
)

from app.services.role_permission_service import (
    RolePermissionService,
)

router = APIRouter(
    prefix="/api/v1/role-permissions",
    tags=["Role Permissions"],
)


@router.get(
    "",
    response_model=List[RolePermissionSchema],
)
def get_role_permissions(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return RolePermissionService.get_role_permissions(db)


@router.get(
    "/{id}",
    response_model=RolePermissionSchema,
)
def get_role_permission_by_id(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return RolePermissionService.get_role_permission_by_id(
        db,
        id,
    )


@router.post(
    "",
    response_model=RolePermissionSchema,
)
def create_role_permission(
    data: RolePermissionCreateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return RolePermissionService.create_role_permission(
        db,
        data,
    )


@router.put(
    "/{id}",
    response_model=RolePermissionSchema,
)
def update_role_permission(
    id: int,
    data: RolePermissionUpdateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return RolePermissionService.update_role_permission(
        db,
        id,
        data,
    )


@router.delete(
    "/{id}",
    response_model=MessageSchema,
)
def delete_role_permission(
    id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    return RolePermissionService.delete_role_permission(
        db,
        id,
    )