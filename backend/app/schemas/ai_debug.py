from pydantic import BaseModel


class AIDebugRequestSchema(BaseModel):

    language: str
    code: str
    error: str


class AIDebugResponseSchema(BaseModel):

    response: str