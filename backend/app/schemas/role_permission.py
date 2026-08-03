from pydantic import BaseModel, ConfigDict


class RolePermissionSchema(BaseModel):
    id: int
    role_id: int
    permission_id: int

    model_config = ConfigDict(
        from_attributes=True
    )


class RolePermissionCreateSchema(BaseModel):
    role_id: int
    permission_id: int


class RolePermissionUpdateSchema(BaseModel):
    role_id: int
    permission_id: int


class MessageSchema(BaseModel):
    success: bool
    message: str