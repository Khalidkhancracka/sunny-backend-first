from sqlalchemy.orm import Session

from app.db.models import Product
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(
    db: Session,
    data: ProductCreate,
) -> Product:
    product = Product(
        name=data.name,
        slug=data.slug,
        description=data.description,
        category_id=data.category_id,
        is_featured=data.is_featured,
        is_published=data.is_published,
        display_order=data.display_order,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_products(
    db: Session,
) -> list[Product]:
    return (
        db.query(Product)
        .order_by(Product.display_order.asc(), Product.id.asc())
        .all()
    )


def get_product(
    db: Session,
    product_id: int,
) -> Product | None:
    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )


def update_product(
    db: Session,
    product: Product,
    data: ProductUpdate,
) -> Product:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(
    db: Session,
    product: Product,
) -> None:
    db.delete(product)
    db.commit()