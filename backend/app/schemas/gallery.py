from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class GalleryImageCreate(BaseModel):
    file_id: int = Field(
        ...,
        gt=0,
    )

    caption: str | None = Field(
        default=None,
        max_length=500,
    )

    display_order: int = Field(
        default=0,
        ge=0,
    )

    is_published: bool = False


class GalleryImageUpdate(BaseModel):
    file_id: int | None = Field(
        default=None,
        gt=0,
    )

    caption: str | None = Field(
        default=None,
        max_length=500,
    )

    display_order: int | None = Field(
        default=None,
        ge=0,
    )

    is_published: bool | None = None


class GalleryImageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    file_id: int
    caption: str | None
    display_order: int
    is_published: bool
    created_at: datetime
    updated_at: datetime