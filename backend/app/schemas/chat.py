from typing import Optional

from pydantic import BaseModel


class ChatRequestSchema(BaseModel):

    session_id: Optional[int] = None
    message: str


class ChatResponseSchema(BaseModel):

    session_id: int
    response: str
    response_time: float