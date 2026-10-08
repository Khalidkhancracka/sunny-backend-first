from pydantic import BaseModel, ConfigDict, Field


class ProductImageCreate(BaseModel):
    file_id: int = Field(
        ...,
        gt=0,
    )

    is_primary: bool = False

    display_order: int = Field(
        default=0,
        ge=0,
    )


class ProductImageUpdate(BaseModel):
    is_primary: bool | None = None

    display_order: int | None = Field(
        default=None,
        ge=0,
    )


class ProductImageResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    file_id: int
    is_primary: bool
    display_order: int