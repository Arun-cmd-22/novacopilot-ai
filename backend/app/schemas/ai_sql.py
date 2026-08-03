from pydantic import BaseModel


class AISQLRequestSchema(BaseModel):

    database: str
    prompt: str


class AISQLResponseSchema(BaseModel):

    response: str