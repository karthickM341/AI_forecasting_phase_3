from pydantic import (
    BaseModel,
    EmailStr,
    Field
)
from typing import Optional
from datetime import datetime


class UserCreateSchema(BaseModel):

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


class UserUpdateSchema(BaseModel):

    username: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None


class UserResponseSchema(BaseModel):

    id: int
    username: str
    email: EmailStr
    role: str
    is_active: bool
    created_at: datetime
    updated_at: datetime


class UserProfileSchema(BaseModel):

    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    department: Optional[str] = None
    designation: Optional[str] = None
    profile_image: Optional[str] = None


class UserActivitySchema(BaseModel):

    username: str
    activity: str
    module: str
    login_time: datetime


class UserDashboardSchema(BaseModel):

    total_users: int
    active_users: int
    analysts: int
    viewers: int
    super_admins: int