from pydantic import BaseModel, ConfigDict


class AIPromptTemplateSchema(BaseModel):

    id: int
    name: str
    category: str
    system_prompt: str
    status: bool

    model_config = ConfigDict(
        from_attributes=True,
    )


class AIPromptTemplateCreateSchema(BaseModel):

    name: str
    category: str
    system_prompt: str
    status: bool = True


class AIPromptTemplateUpdateSchema(BaseModel):

    name: str
    category: str
    system_prompt: str
    status: bool


class MessageSchema(BaseModel):

    success: bool
    message: str