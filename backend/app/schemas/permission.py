from pydantic import BaseModel, ConfigDict


class PermissionSchema(BaseModel):
    id: int
    permission_name: str
    module_name: str | None = None
    status: bool

    model_config = ConfigDict(
        from_attributes=True
    )


class PermissionCreateSchema(BaseModel):
    permission_name: str
    module_name: str | None = None
    status: bool = True


class PermissionUpdateSchema(BaseModel):
    permission_name: str
    module_name: str | None = None
    status: bool


class MessageSchema(BaseModel):
    success: bool
    message: str