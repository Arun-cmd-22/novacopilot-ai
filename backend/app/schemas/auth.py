from pydantic import BaseModel, EmailStr, Field


class RegisterSchema(BaseModel):
    full_name: str = Field(
        min_length=2,
        max_length=150,
        pattern=r"^[A-Za-z]+(?: [A-Za-z]+)*$",
    )

    email: EmailStr

    mobile: str = Field(
        min_length=8,
        max_length=15,
        pattern=r"^\+?[1-9]\d{7,14}$",
    )

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class RefreshTokenSchema(BaseModel):
    refresh_token: str


class LogoutSchema(BaseModel):
    refresh_token: str