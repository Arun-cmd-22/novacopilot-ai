from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.permissions import has_permission
from app.database.database import get_db

from app.schemas.permission import (
    PermissionSchema,
    PermissionCreateSchema,
    PermissionUpdateSchema,
    MessageSchema,
)

from app.services.permission_service import PermissionService

router = APIRouter(
    prefix="/api/v1/permissions",
    tags=["Permissions"],
)


@router.get(
    "",
    response_model=List[PermissionSchema],
)
def get_permissions(
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("View Permission")),
):

    return PermissionService.get_permissions(db)


@router.get(
    "/{permission_id}",
    response_model=PermissionSchema,
)
def get_permission_by_id(
    permission_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("View Permission")),
):

    return PermissionService.get_permission_by_id(
        db,
        permission_id,
    )


@router.post(
    "",
    response_model=PermissionSchema,
)
def create_permission(
    data: PermissionCreateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Create Permission")),
):

    return PermissionService.create_permission(
        db,
        data,
    )


@router.put(
    "/{permission_id}",
    response_model=PermissionSchema,
)
def update_permission(
    permission_id: int,
    data: PermissionUpdateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Update Permission")),
):

    return PermissionService.update_permission(
        db,
        permission_id,
        data,
    )


@router.delete(
    "/{permission_id}",
    response_model=MessageSchema,
)
def delete_permission(
    permission_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Delete Permission")),
):

    return PermissionService.delete_permission(
        db,
        permission_id,
    )