from sqlalchemy.orm import Session

from app.db.models import TeamMember
from app.schemas.team_member import TeamMemberCreate, TeamMemberUpdate


def create_team_member(
    db: Session,
    data: TeamMemberCreate,
) -> TeamMember:
    member = TeamMember(
        name=data.name,
        position=data.position,
        tagline=data.tagline,
        display_order=data.display_order,
        is_published=data.is_published,
    )

    db.add(member)
    db.commit()
    db.refresh(member)

    return member


def get_team_members(
    db: Session,
) -> list[TeamMember]:
    return (
        db.query(TeamMember)
        .order_by(
            TeamMember.display_order.asc(),
            TeamMember.id.asc(),
        )
        .all()
    )


def get_team_member(
    db: Session,
    member_id: int,
) -> TeamMember | None:
    return (
        db.query(TeamMember)
        .filter(TeamMember.id == member_id)
        .first()
    )


def update_team_member(
    db: Session,
    member: TeamMember,
    data: TeamMemberUpdate,
) -> TeamMember:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(member, field, value)

    db.commit()
    db.refresh(member)

    return member


def delete_team_member(
    db: Session,
    member: TeamMember,
) -> None:
    db.delete(member)
    db.commit()