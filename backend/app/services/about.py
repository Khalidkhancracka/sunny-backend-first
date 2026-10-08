from sqlalchemy.orm import Session

from app.db.models import AboutSection
from app.schemas.about import AboutUpdate


def get_about(
    db: Session,
) -> AboutSection | None:
    return (
        db.query(AboutSection)
        .filter(AboutSection.id == 1)
        .first()
    )


def update_about(
    db: Session,
    about: AboutSection,
    data: AboutUpdate,
) -> AboutSection:
    update_data = data.model_dump(exclude_unset=True)

    for field, field_value in update_data.items():
        setattr(about, field, field_value)

    db.commit()
    db.refresh(about)

    return about