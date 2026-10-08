from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, HttpUrl, field_validator


class SocialLinkCreate(BaseModel):
    platform: str = Field(
        ...,
        min_length=2,
        max_length=50,
    )

    url: HttpUrl

    display_order: int = Field(
        default=0,
        ge=0,
    )

    is_active: bool = True

    @field_validator("platform", mode="before")
    @classmethod
    def strip_platform(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class SocialLinkUpdate(BaseModel):
    platform: str | None = Field(
        default=None,
        min_length=2,
        max_length=50,
    )

    url: HttpUrl | None = None

    display_order: int | None = Field(
        default=None,
        ge=0,
    )

    is_active: bool | None = None

    @field_validator("platform", mode="before")
    @classmethod
    def strip_platform(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class SocialLinkResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    platform: str
    url: HttpUrl
    display_order: int
    is_active: bool
    created_at: datetime
    updated_at: datetime