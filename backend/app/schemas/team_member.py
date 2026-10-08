from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class TeamMemberCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=150,
    )

    position: str = Field(
        ...,
        min_length=2,
        max_length=150,
    )

    tagline: str | None = Field(
        default=None,
        max_length=500,
    )

    display_order: int = Field(
        default=0,
        ge=0,
    )

    is_published: bool = False

    @field_validator(
        "name",
        "position",
        "tagline",
        mode="before",
    )
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class TeamMemberUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=150,
    )

    position: str | None = Field(
        default=None,
        min_length=2,
        max_length=150,
    )

    tagline: str | None = Field(
        default=None,
        max_length=500,
    )

    display_order: int | None = Field(
        default=None,
        ge=0,
    )

    is_published: bool | None = None

    @field_validator(
        "name",
        "position",
        "tagline",
        mode="before",
    )
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class TeamMemberResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    position: str
    tagline: str | None
    display_order: int
    is_published: bool
    created_at: datetime
    updated_at: datetime