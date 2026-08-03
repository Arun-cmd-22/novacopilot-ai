from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.permission import Permission


class PermissionService:

    @staticmethod
    def get_permissions(db: Session):

        permissions = (
            db.query(Permission)
            .all()
        )

        return permissions

    @staticmethod
    def get_permission_by_id(
        db: Session,
        permission_id: int,
    ):

        permission = (
            db.query(Permission)
            .filter(Permission.id == permission_id)
            .first()
        )

        if not permission:
            raise HTTPException(
                status_code=404,
                detail="Permission Not Found"
            )

        return permission

    @staticmethod
    def create_permission(
        db: Session,
        data,
    ):

        permission = Permission(
            permission_name=data.permission_name,
            module_name=data.module_name,
            status=data.status,
        )

        db.add(permission)
        db.commit()
        db.refresh(permission)

        return permission

    @staticmethod
    def update_permission(
        db: Session,
        permission_id: int,
        data,
    ):

        permission = (
            db.query(Permission)
            .filter(Permission.id == permission_id)
            .first()
        )

        if not permission:
            raise HTTPException(
                status_code=404,
                detail="Permission Not Found"
            )

        permission.permission_name = data.permission_name
        permission.module_name = data.module_name
        permission.status = data.status

        db.commit()
        db.refresh(permission)

        return permission

    @staticmethod
    def delete_permission(
        db: Session,
        permission_id: int,
    ):

        permission = (
            db.query(Permission)
            .filter(Permission.id == permission_id)
            .first()
        )

        if not permission:
            raise HTTPException(
                status_code=404,
                detail="Permission Not Found"
            )

        db.delete(permission)
        db.commit()

        return {
            "success": True,
            "message": "Permission Deleted Successfully"
        }