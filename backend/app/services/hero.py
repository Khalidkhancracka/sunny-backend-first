from sqlalchemy.orm import Session

from app.db.models import HeroSection
from app.schemas.hero import HeroUpdate


def get_hero(
    db: Session,
) -> HeroSection | None:
    return (
        db.query(HeroSection)
        .filter(HeroSection.id == 1)
        .first()
    )


def update_hero(
    db: Session,
    hero: HeroSection,
    data: HeroUpdate,
) -> HeroSection:
    update_data = data.model_dump(exclude_unset=True)

    for field, field_value in update_data.items():
        setattr(hero, field, field_value)

    db.commit()
    db.refresh(hero)

    return hero