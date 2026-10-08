from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class HeroUpdate(BaseModel):
    script_text: str | None = Field(
        default=None,
        max_length=300,
    )

    heading: str | None = Field(
        default=None,
        min_length=2,
        max_length=300,
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
        "script_text",
        "heading",
        "button_text",
        "button_link",
        mode="before",
    )
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class HeroResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    script_text: str | None
    heading: str | None
    button_text: str | None
    button_link: str | None
    image_file_id: int | None
    updated_at: datetime