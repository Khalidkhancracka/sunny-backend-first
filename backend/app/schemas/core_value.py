from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class CoreValueCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=2,
        max_length=150,
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
    )

    icon_file_id: int | None = Field(
        default=None,
        gt=0,
    )

    display_order: int = Field(
        default=0,
        ge=0,
    )

    is_published: bool = False

    @field_validator("title", "description", mode="before")
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class CoreValueUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=2,
        max_length=150,
    )

    description: str | None = Field(
        default=None,
        max_length=1000,
    )

    icon_file_id: int | None = Field(
        default=None,
        gt=0,
    )

    display_order: int | None = Field(
        default=None,
        ge=0,
    )

    is_published: bool | None = None

    @field_validator("title", "description", mode="before")
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class CoreValueResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None
    icon_file_id: int | None
    display_order: int
    is_published: bool
    created_at: datetime
    updated_at: datetime