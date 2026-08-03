from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.orm import Session

from app.auth.jwt_handler import decode_access_token
from app.database.database import get_db
from app.models.user import User

# HTTP Bearer Authentication
security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    try:
        # Get JWT token
        token = credentials.credentials

        # Decode JWT
        payload = decode_access_token(token)

        # Get user from database
        user = (
            db.query(User)
            .filter(User.id == payload["user_id"])
            .first()
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )

        return user

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )