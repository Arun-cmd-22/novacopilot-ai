from pydantic import BaseModel, ConfigDict


class AIModelSchema(BaseModel):
    id: int
    model_name: str
    display_name: str
    provider: str
    model_version: str | None = None
    base_url: str | None = None
    api_key: str | None = None
    is_local: bool
    is_default: bool
    status: bool

    model_config = ConfigDict(
        from_attributes=True
    )


class AIModelCreateSchema(BaseModel):
    model_name: str
    display_name: str
    provider: str
    model_version: str | None = None
    base_url: str | None = None
    api_key: str | None = None
    is_local: bool = True
    is_default: bool = False
    status: bool = True


class AIModelUpdateSchema(BaseModel):
    model_name: str
    display_name: str
    provider: str
    model_version: str | None = None
    base_url: str | None = None
    api_key: str | None = None
    is_local: bool
    is_default: bool
    status: bool


class MessageSchema(BaseModel):
    success: bool
    message: str