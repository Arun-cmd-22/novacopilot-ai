from pydantic import BaseModel, EmailStr
from enum import Enum


class UserProfileSchema(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    mobile: str | None
    role_id: int

    class Config:
        from_attributes = True


class UserListSchema(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    mobile: str | None
    role_id: int

    class Config:
        from_attributes = True
        
class RoleEnum(str, Enum):
    SUPER_ADMIN = "Super Admin"
    ADMIN = "Admin"
    DEVELOPER = "Developer"
    USER = "User"
        
class UserCreateSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    mobile: str | None = None
    role_name: RoleEnum
    
class UserUpdateSchema(BaseModel):
    full_name: str
    email: EmailStr
    mobile: str | None = None

class UserDeleteSchema(BaseModel):
    success: bool
    message: str