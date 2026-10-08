from sqlalchemy.orm import Session

from app.db.models import SiteSetting
from app.schemas.site_settings import SiteSettingsUpdate


def get_site_settings(
    db: Session,
) -> SiteSetting | None:
    return (
        db.query(SiteSetting)
        .filter(SiteSetting.id == 1)
        .first()
    )


def update_site_settings(
    db: Session,
    settings: SiteSetting,
    data: SiteSettingsUpdate,
) -> SiteSetting:
    update_data = data.model_dump(exclude_unset=True)

    for field, field_value in update_data.items():
        setattr(settings, field, field_value)

    db.commit()
    db.refresh(settings)

    return settings