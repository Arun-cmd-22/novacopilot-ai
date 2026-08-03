from pydantic import BaseModel


class AIExplainRequestSchema(BaseModel):

    language: str
    code: str


class AIExplainResponseSchema(BaseModel):

    response: str