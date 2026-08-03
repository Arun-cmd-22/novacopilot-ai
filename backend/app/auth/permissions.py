from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.database.database import get_db

from app.models.role_permission import RolePermission
from app.models.permission import Permission


def has_permission(permission_name: str):

    def permission_checker(
        current_user=Depends(get_current_user),
        db: Session = Depends(get_db),
    ):

        permission = (
            db.query(Permission)
            .filter(
                Permission.permission_name == permission_name
            )
            .first()
        )

        if not permission:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Permission Not Found"
            )

        role_permission = (
            db.query(RolePermission)
            .filter(
                RolePermission.role_id == current_user.role_id,
                RolePermission.permission_id == permission.id,
            )
            .first()
        )

        if not role_permission:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Permission Denied"
            )

        return current_user

    return permission_checker