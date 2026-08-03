from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.role_permission import RolePermission


class RolePermissionService:

    @staticmethod
    def get_role_permissions(db: Session):

        return (
            db.query(RolePermission)
            .all()
        )

    @staticmethod
    def get_role_permission_by_id(
        db: Session,
        id: int,
    ):

        role_permission = (
            db.query(RolePermission)
            .filter(RolePermission.id == id)
            .first()
        )

        if not role_permission:
            raise HTTPException(
                status_code=404,
                detail="Role Permission Not Found"
            )

        return role_permission

    @staticmethod
    def create_role_permission(
        db: Session,
        data,
    ):

        role_permission = RolePermission(
            role_id=data.role_id,
            permission_id=data.permission_id,
        )

        db.add(role_permission)
        db.commit()
        db.refresh(role_permission)

        return role_permission

    @staticmethod
    def update_role_permission(
        db: Session,
        id: int,
        data,
    ):

        role_permission = (
            db.query(RolePermission)
            .filter(RolePermission.id == id)
            .first()
        )

        if not role_permission:
            raise HTTPException(
                status_code=404,
                detail="Role Permission Not Found"
            )

        role_permission.role_id = data.role_id
        role_permission.permission_id = data.permission_id

        db.commit()
        db.refresh(role_permission)

        return role_permission

    @staticmethod
    def delete_role_permission(
        db: Session,
        id: int,
    ):

        role_permission = (
            db.query(RolePermission)
            .filter(RolePermission.id == id)
            .first()
        )

        if not role_permission:
            raise HTTPException(
                status_code=404,
                detail="Role Permission Not Found"
            )

        db.delete(role_permission)
        db.commit()

        return {
            "success": True,
            "message": "Role Permission Deleted Successfully"
        }