from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.auth.permissions import has_permission
from app.database.database import get_db

from app.schemas.user import (
    UserProfileSchema,
    UserListSchema,
    UserCreateSchema,
    UserUpdateSchema,
    UserDeleteSchema,
)

from app.services.user_service import UserService

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
)


@router.get(
    "/profile",
    response_model=UserProfileSchema,
)
def profile(
    current_user=Depends(get_current_user),
):
    return UserService.profile(current_user)


@router.get(
    "",
    response_model=List[UserListSchema],
)
def get_users(
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("View User")),
):
    return UserService.get_users(db)


@router.get(
    "/{user_id}",
    response_model=UserProfileSchema,
)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("View User")),
):
    return UserService.get_user_by_id(
        db,
        user_id,
    )


@router.post(
    "",
    response_model=UserProfileSchema,
)
def create_user(
    data: UserCreateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Create User")),
):
    return UserService.create_user(
        db,
        data,
    )


@router.put(
    "/{user_id}",
    response_model=UserProfileSchema,
)
def update_user(
    user_id: int,
    data: UserUpdateSchema,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Update User")),
):
    return UserService.update_user(
        db,
        user_id,
        data,
    )


@router.delete(
    "/{user_id}",
    response_model=UserDeleteSchema,
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(has_permission("Delete User")),
):
    return UserService.delete_user(
        db,
        user_id,
    )