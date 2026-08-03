from sqlalchemy.orm import Session

from app.auth.jwt_handler import create_access_token
from app.auth.password import hash_password, verify_password
from app.models.role import Role
from app.models.user import User


class AuthService:

    @staticmethod
    def register(
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
                "message": "Email already registered"
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

        return {
            "success": True,
            "message": "Registration Successful"
        }

    @staticmethod
    def login(
        db: Session,
        data,
    ):

        user = (
            db.query(User)
            .filter(User.email == data.email)
            .first()
        )

        if not user:
            return {
                "success": False,
                "message": "Invalid Email"
            }

        if not verify_password(
            data.password,
            user.password,
        ):
            return {
                "success": False,
                "message": "Invalid Password"
            }

        token = create_access_token(
            {
                "user_id": user.id,
                "email": user.email,
                "role_id": user.role_id,
            }
        )

        role = (
            db.query(Role)
            .filter(Role.id == user.role_id)
            .first()
        )

        return {
            "success": True,
            "message": "Login Successful",
            "access_token": token,
            "token_type": "Bearer",
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "mobile": user.mobile,
                "role": role.role_name if role else None,
            }
        }