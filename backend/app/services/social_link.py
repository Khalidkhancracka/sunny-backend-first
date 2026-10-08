from sqlalchemy.orm import Session

from app.db.models import SocialLink
from app.schemas.social_link import SocialLinkCreate, SocialLinkUpdate


def create_social_link(
    db: Session,
    data: SocialLinkCreate,
) -> SocialLink:
    link = SocialLink(
        platform=data.platform,
        url=data.url,
        display_order=data.display_order,
        is_active=data.is_active,
    )

    db.add(link)
    db.commit()
    db.refresh(link)

    return link


def get_social_links(
    db: Session,
) -> list[SocialLink]:
    return (
        db.query(SocialLink)
        .order_by(
            SocialLink.display_order.asc(),
            SocialLink.id.asc(),
        )
        .all()
    )


def get_social_link(
    db: Session,
    link_id: int,
) -> SocialLink | None:
    return (
        db.query(SocialLink)
        .filter(SocialLink.id == link_id)
        .first()
    )


def update_social_link(
    db: Session,
    link: SocialLink,
    data: SocialLinkUpdate,
) -> SocialLink:
    update_data = data.model_dump(exclude_unset=True)

    for field, field_value in update_data.items():
        setattr(link, field, field_value)

    db.commit()
    db.refresh(link)

    return link


def delete_social_link(
    db: Session,
    link: SocialLink,
) -> None:
    db.delete(link)
    db.commit()