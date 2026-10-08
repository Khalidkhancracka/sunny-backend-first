from sqlalchemy.orm import Session

from app.db.models import CoreValue
from app.schemas.core_value import CoreValueCreate, CoreValueUpdate


def create_core_value(
    db: Session,
    data: CoreValueCreate,
) -> CoreValue:
    value = CoreValue(
        title=data.title,
        description=data.description,
        icon_file_id=data.icon_file_id,
        display_order=data.display_order,
        is_published=data.is_published,
    )

    db.add(value)
    db.commit()
    db.refresh(value)

    return value


def get_core_values(
    db: Session,
) -> list[CoreValue]:
    return (
        db.query(CoreValue)
        .order_by(
            CoreValue.display_order.asc(),
            CoreValue.id.asc(),
        )
        .all()
    )


def get_core_value(
    db: Session,
    value_id: int,
) -> CoreValue | None:
    return (
        db.query(CoreValue)
        .filter(CoreValue.id == value_id)
        .first()
    )


def update_core_value(
    db: Session,
    value: CoreValue,
    data: CoreValueUpdate,
) -> CoreValue:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(value, field, value)

    db.commit()
    db.refresh(value)

    return value


def delete_core_value(
    db: Session,
    value: CoreValue,
) -> None:
    db.delete(value)
    db.commit()