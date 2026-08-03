from sqlalchemy.orm import Session

from app.models.role import Role


class RoleService:

    @staticmethod
    def get_roles(db: Session):

        return (
            db.query(Role)
            .all()
        )

    @staticmethod
    def get_role_by_id(
        db: Session,
        role_id: int,
    ):

        return (
            db.query(Role)
            .filter(Role.id == role_id)
            .first()
        )

    @staticmethod
    def create_role(
        db: Session,
        data,
    ):

        role = Role(
            role_name=data.role_name,
        )

        db.add(role)
        db.commit()
        db.refresh(role)

        return role

    @staticmethod
    def update_role(
        db: Session,
        role_id: int,
        data,
    ):

        role = (
            db.query(Role)
            .filter(Role.id == role_id)
            .first()
        )

        if not role:
            return {
                "success": False,
                "message": "Role Not Found"
            }

        role.role_name = data.role_name

        db.commit()
        db.refresh(role)

        return role

    @staticmethod
    def delete_role(
        db: Session,
        role_id: int,
    ):

        role = (
            db.query(Role)
            .filter(Role.id == role_id)
            .first()
        )

        if not role:
            return {
                "success": False,
                "message": "Role Not Found"
            }

        db.delete(role)
        db.commit()

        return {
            "success": True,
            "message": "Role Deleted Successfully"
        }