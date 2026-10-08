from pydantic import BaseModel, ConfigDict, Field, field_validator
from app.schemas.category import CategorySummary
from app.schemas.product_image import ProductImageResponse


class ProductBase(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=200,
    )

    slug: str = Field(
        ...,
        min_length=2,
        max_length=200,
    )

    description: str | None = Field(
        default=None,
        max_length=5000,
    )

    category_id: int = Field(
        ...,
        gt=0,
    )

    is_featured: bool = False

    is_published: bool = False

    display_order: int = Field(
        default=0,
        ge=0,
    )

    @field_validator("name", "slug", "description", mode="before")
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=200,
    )

    slug: str | None = Field(
        default=None,
        min_length=2,
        max_length=200,
    )

    description: str | None = Field(
        default=None,
        max_length=5000,
    )

    category_id: int | None = Field(
        default=None,
        gt=0,
    )

    is_featured: bool | None = None

    is_published: bool | None = None

    display_order: int | None = Field(
        default=None,
        ge=0,
    )

    @field_validator("name", "slug", "description", mode="before")
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value

class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str
    description: str | None
    category_id: int
    is_featured: bool
    is_published: bool
    display_order: int
class ProductDetailResponse(ProductResponse):
    category: CategorySummary
class ProductDetailResponse(ProductResponse):
    category: CategorySummary
    images: list[ProductImageResponse] = Field(
        default_factory=list,
    )