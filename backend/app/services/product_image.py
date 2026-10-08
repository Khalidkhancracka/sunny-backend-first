from sqlalchemy.orm import Session

from app.db.models import ProductImage
from app.schemas.product_image import (
    ProductImageCreate,
    ProductImageUpdate,
)


def create_product_image(
    db: Session,
    product_id: int,
    data: ProductImageCreate,
) -> ProductImage:
    image = ProductImage(
        product_id=product_id,
        file_id=data.file_id,
        is_primary=data.is_primary,
        display_order=data.display_order,
    )

    db.add(image)
    db.commit()
    db.refresh(image)

    return image


def get_product_images(
    db: Session,
    product_id: int,
) -> list[ProductImage]:
    return (
        db.query(ProductImage)
        .filter(ProductImage.product_id == product_id)
        .order_by(
            ProductImage.display_order.asc(),
            ProductImage.id.asc(),
        )
        .all()
    )


def get_product_image(
    db: Session,
    image_id: int,
) -> ProductImage | None:
    return (
        db.query(ProductImage)
        .filter(ProductImage.id == image_id)
        .first()
    )


def update_product_image(
    db: Session,
    image: ProductImage,
    data: ProductImageUpdate,
) -> ProductImage:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(image, field, value)

    db.commit()
    db.refresh(image)

    return image


def delete_product_image(
    db: Session,
    image: ProductImage,
) -> None:
    db.delete(image)
    db.commit()