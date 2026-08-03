from pydantic import BaseModel, ConfigDict


class ChatSessionSchema(BaseModel):

    id: int
    user_id: int
    ai_model_id: int
    title: str | None = None
    status: bool

    model_config = ConfigDict(
        from_attributes=True,
    )


class ChatSessionCreateSchema(BaseModel):

    ai_model_id: int
    title: str


class ChatSessionUpdateSchema(BaseModel):

    ai_model_id: int
    title: str
    status: bool


class MessageSchema(BaseModel):

    success: bool
    message: str