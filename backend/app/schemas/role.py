from pydantic import BaseModel, ConfigDict


class RoleSchema(BaseModel):
    id: int
    role_name: str

    model_config = ConfigDict(
        from_attributes=True
    )


class RoleCreateSchema(BaseModel):
    role_name: str


class RoleUpdateSchema(BaseModel):
    role_name: str
    
class MessageSchema(BaseModel):
    success: bool
    message: str