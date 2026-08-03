from pydantic import BaseModel, ConfigDict


class MessageSchema(BaseModel):

    id: int
    session_id: int
    role: str
    message: str
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
    response_time: float

    model_config = ConfigDict(
        from_attributes=True,
    )


class MessageCreateSchema(BaseModel):

    session_id: int
    role: str
    message: str


class MessageUpdateSchema(BaseModel):

    role: str
    message: str


class ResponseSchema(BaseModel):

    success: bool
    message: str