from sqlalchemy.orm import Session

from app.auth.password import hash_password
from app.models.role import Role
from app.models.user import User


class UserService:

    @staticmethod
    def profile(user):
        return user

    @staticmethod
    def get_users(db: Session):

        users = (
            db.query(User)
            .all()
        )

        return users

    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id: int,
    ):

        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        return user

    @staticmethod
    def create_user(
        db: Session,
        data,
    ):

        role = (
            db.query(Role)
            .filter(Role.role_name == data.role_name)
            .first()
        )

        if not role:
            return {
                "success": False,
                "message": "Invalid Role"
            }

        existing_user = (
            db.query(User)
            .filter(User.email == data.email)
            .first()
        )

        if existing_user:
            return {
                "success": False,
                "message": "Email already exists"
            }

        user = User(
            role_id=role.id,
            full_name=data.full_name,
            email=data.email,
            password=hash_password(data.password),
            mobile=data.mobile,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def update_user(
        db: Session,
        user_id: int,
        data,
    ):

        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return {
                "success": False,
                "message": "User Not Found"
            }

        role = (
            db.query(Role)
            .filter(Role.role_name == data.role_name)
            .first()
        )

        if not role:
            return {
                "success": False,
                "message": "Invalid Role"
            }

        user.role_id = role.id
        user.full_name = data.full_name
        user.email = data.email
        user.mobile = data.mobile

        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def delete_user(
        db: Session,
        user_id: int,
    ):

        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if not user:
            return {
                "success": False,
                "message": "User Not Found"
            }

        db.delete(user)
        db.commit()

        return {
            "success": True,
            "message": "User Deleted Successfully"
        }