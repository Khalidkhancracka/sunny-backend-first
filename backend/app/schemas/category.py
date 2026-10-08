from pydantic import BaseModel, ConfigDict, Field, field_validator


class CategoryBase(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    slug: str = Field(
        ...,
        min_length=2,
        max_length=100,
    )

    banner_file_id: int | None = Field(
        default=None,
        gt=0,
    )

    display_order: int = Field(
        default=0,
        ge=0,
    )

    is_published: bool = False

    @field_validator("name", "slug", mode="before")
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    slug: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    banner_file_id: int | None = Field(
        default=None,
        gt=0,
    )

    display_order: int | None = Field(
        default=None,
        ge=0,
    )

    is_published: bool | None = None

    @field_validator("name", "slug", mode="before")
    @classmethod
    def strip_whitespace(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value


class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str
    banner_file_id: int | None
    display_order: int
    is_published: bool
class CategorySummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    slug: str