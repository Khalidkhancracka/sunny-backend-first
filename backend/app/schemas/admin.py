from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


AdminRole = Literal["super_admin", "admin"]


class AdminCreate(BaseModel):
    username: str = Field(
        ...,
        min_length=3,
        max_length=100,
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )

    role: AdminRole = "admin"

    @field_validator("username", mode="before")
    @classmethod
    def strip_username(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class AdminUpdate(BaseModel):
    username: str | None = Field(
        default=None,
        min_length=3,
        max_length=100,
    )

    email: EmailStr | None = None

    role: AdminRole | None = None

    @field_validator("username", mode="before")
    @classmethod
    def strip_username(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class AdminStatusUpdate(BaseModel):
    is_active: bool


class AdminPasswordReset(BaseModel):
    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
    )


class AdminResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    role: AdminRole
    is_active: bool
    last_login_at: datetime | None
    created_at: datetime
    updated_at: datetime