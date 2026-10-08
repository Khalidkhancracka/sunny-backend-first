from sqlalchemy.orm import Session

from app.db.models import Category
from app.schemas.category import CategoryCreate, CategoryUpdate


def create_category(
    db: Session,
    data: CategoryCreate,
) -> Category:
    category = Category(
        name=data.name,
        slug=data.slug,
        banner_file_id=data.banner_file_id,
        display_order=data.display_order,
        is_published=data.is_published,
    )

    db.add(category)
    db.commit()
    db.refresh(category)

    return category


def get_categories(
    db: Session,
) -> list[Category]:
    return (
        db.query(Category)
        .order_by(Category.display_order.asc(), Category.id.asc())
        .all()
    )


def get_category(
    db: Session,
    category_id: int,
) -> Category | None:
    return (
        db.query(Category)
        .filter(Category.id == category_id)
        .first()
    )


def update_category(
    db: Session,
    category: Category,
    data: CategoryUpdate,
) -> Category:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(category, field, value)

    db.commit()
    db.refresh(category)

    return category


def delete_category(
    db: Session,
    category: Category,
) -> None:
    db.delete(category)
    db.commit()