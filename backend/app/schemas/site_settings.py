from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class SiteSettingsUpdate(BaseModel):
    company_name: str | None = Field(
        default=None,
        min_length=2,
        max_length=200,
    )

    tagline: str | None = Field(
        default=None,
        max_length=300,
    )

    footer_description: str | None = Field(
        default=None,
        max_length=2000,
    )

    phone: str | None = Field(
        default=None,
        max_length=50,
    )

    email: str | None = Field(
        default=None,
        max_length=320,
    )

    address: str | None = Field(
        default=None,
        max_length=500,
    )

    copyright_text: str | None = Field(
        default=None,
        max_length=300,
    )

    logo_file_id: int | None = Field(
        default=None,
        gt=0,
    )

    favicon_file_id: int | None = Field(
        default=None,
        gt=0,
    )

    @field_validator(
        "company_name",
        "tagline",
        "footer_description",
        "phone",
        "email",
        "address",
        "copyright_text",
        mode="before",
    )
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class SiteSettingsResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_name: str | None
    tagline: str | None
    footer_description: str | None
    phone: str | None
    email: str | None
    address: str | None
    copyright_text: str | None
    logo_file_id: int | None
    favicon_file_id: int | None
    updated_at: datetime