from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class AboutUpdate(BaseModel):
    title: str | None = Field(
        default=None,
        min_length=2,
        max_length=200,
    )

    description: str | None = Field(
        default=None,
        max_length=5000,
    )

    button_text: str | None = Field(
        default=None,
        max_length=100,
    )

    button_link: str | None = Field(
        default=None,
        max_length=500,
    )

    image_file_id: int | None = Field(
        default=None,
        gt=0,
    )

    @field_validator(
        "title",
        "description",
        "button_text",
        "button_link",
        mode="before",
    )
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class AboutResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str | None
    description: str | None
    button_text: str | None
    button_link: str | None
    image_file_id: int | None
    updated_at: datetime