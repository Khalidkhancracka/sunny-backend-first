from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class MediaCreate(BaseModel):
    storage_path: str = Field(
        ...,
        min_length=1,
        max_length=500,
    )

    mime_type: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )

    size_bytes: int = Field(
        ...,
        ge=0,
    )

    original_name: str = Field(
        ...,
        min_length=1,
        max_length=255,
    )


class MediaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    storage_path: str
    mime_type: str
    size_bytes: int
    original_name: str
    created_at: datetime