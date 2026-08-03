from pydantic import BaseModel


class AIERPRequestSchema(BaseModel):

    module: str
    question: str


class AIERPResponseSchema(BaseModel):

    response: str