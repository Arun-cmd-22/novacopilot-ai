from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.auth import LoginSchema, RegisterSchema, RefreshTokenSchema, LogoutSchema
from app.services.auth_service import AuthService

router = APIRouter(prefix="/api/v1", tags=["Authentication"])


@router.post("/register")
def register(data: RegisterSchema, db: Session = Depends(get_db)):
    return AuthService.register(db, data)


@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    return AuthService.login(db, data)


@router.post("/refresh-token")
def refresh_token(data: RefreshTokenSchema, db: Session = Depends(get_db)):
    return AuthService.refresh(db, data.refresh_token)


@router.post("/logout")
def logout(data: LogoutSchema, db: Session = Depends(get_db)):
    return AuthService.logout(db, data.refresh_token)