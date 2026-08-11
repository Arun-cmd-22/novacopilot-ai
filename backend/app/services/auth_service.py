from sqlalchemy.orm import Session
from jose import JWTError

from app.auth.jwt_handler import (
    create_access_token,
    create_refresh_token,
    decode_refresh_token,
)
from app.auth.password import hash_password, verify_password
from app.models.role import Role
from app.models.user import User


class AuthService:

    @staticmethod
    def register(db: Session, data):
        existing_email = (
            db.query(User)
            .filter(User.email == data.email)
            .first()
        )

        if existing_email:
            return {
                "success": False,
                "message": "Email already exists",
            }

        existing_name = (
            db.query(User)
            .filter(User.full_name == data.full_name)
            .first()
        )

        if existing_name:
            return {
                "success": False,
                "message": "Username already exists",
            }

        role = (
            db.query(Role)
            .filter(Role.role_name == "user")
            .first()
        )

        if not role:
            return {
                "success": False,
                "message": "Default user role not found",
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
            "message": "Registration Successful",
        }

    @staticmethod
    def login(db: Session, data):
        user = (
            db.query(User)
            .filter(User.email == data.email)
            .first()
        )

        if not user:
            return {
                "success": False,
                "message": "Invalid Email",
            }

        if not verify_password(data.password, user.password):
            return {
                "success": False,
                "message": "Invalid Password",
            }

        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "role_id": user.role_id,
            }
        )

        refresh_token = create_refresh_token(
            {
                "sub": str(user.id),
            }
        )

        user.access_token = access_token
        user.refresh_token = refresh_token

        db.commit()

        role = (
            db.query(Role)
            .filter(Role.id == user.role_id)
            .first()
        )

        return {
            "success": True,
            "message": "Login Successful",
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "mobile": user.mobile,
                "role": role.role_name if role else None,
            },
        }

    @staticmethod
    def refresh(db: Session, refresh_token: str):
        try:
            payload = decode_refresh_token(refresh_token)
        except JWTError:
            return {
                "success": False,
                "message": "Invalid or expired refresh token",
            }

        if payload.get("type") != "refresh":
            return {
                "success": False,
                "message": "Invalid refresh token",
            }

        user_id = payload.get("sub")

        if not user_id:
            return {
                "success": False,
                "message": "Invalid refresh token",
            }

        user = (
            db.query(User)
            .filter(
                User.id == int(user_id),
                User.refresh_token == refresh_token,
            )
            .first()
        )

        if not user:
            return {
                "success": False,
                "message": "Invalid refresh token",
            }

        access_token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
                "role_id": user.role_id,
            }
        )

        user.access_token = access_token

        db.commit()

        return {
            "success": True,
            "message": "Token refreshed successfully",
            "access_token": access_token,
            "token_type": "Bearer",
        }

    @staticmethod
    def logout(db: Session, refresh_token: str):
        user = (
            db.query(User)
            .filter(User.refresh_token == refresh_token)
            .first()
        )

        if not user:
            return {
                "success": False,
                "message": "Invalid refresh token",
            }

        user.access_token = None
        user.refresh_token = None

        db.commit()

        return {
            "success": True,
            "message": "Logout Successful",
        }