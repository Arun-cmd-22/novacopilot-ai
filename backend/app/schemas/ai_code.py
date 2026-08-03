from pydantic import BaseModel


class AICodeRequestSchema(BaseModel):

    language: str
    prompt: str


class AICodeResponseSchema(BaseModel):

    response: str