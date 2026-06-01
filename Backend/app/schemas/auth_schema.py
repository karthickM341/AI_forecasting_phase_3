from pydantic import (
    BaseModel,
    EmailStr,
    Field
)
from datetime import datetime
from typing import Optional


class RegisterSchema(BaseModel):

    username: str = Field(
        ...,
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=6
    )

    role: str


class LoginSchema(BaseModel):

    email: EmailStr
    password: str


class TokenSchema(BaseModel):

    access_token: str
    token_type: str = "bearer"


class AuthResponseSchema(BaseModel):

    success: bool
    message: str
    data: Optional[TokenSchema] = None

class CurrentUserSchema(BaseModel):

    id: int
    username: str
    email: EmailStr
    role: str
    created_at: datetime