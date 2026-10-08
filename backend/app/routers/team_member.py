from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.team_member import (
    TeamMemberCreate,
    TeamMemberResponse,
    TeamMemberUpdate,
)
from app.services.team_member import (
    create_team_member,
    delete_team_member,
    get_team_member,
    get_team_members,
    update_team_member,
)


router = APIRouter(
    prefix="/team-members",
    tags=["Team Members"],
)


@router.post(
    "",
    response_model=TeamMemberResponse,
)
def create(
    data: TeamMemberCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    return create_team_member(
        db=db,
        data=data,
    )


@router.get(
    "",
    response_model=list[TeamMemberResponse],
)
def list_all(
    db: Session = Depends(get_db),
):
    return get_team_members(
        db=db,
    )


@router.get(
    "/{member_id}",
    response_model=TeamMemberResponse,
)
def get_one(
    member_id: int,
    db: Session = Depends(get_db),
):
    member = get_team_member(
        db=db,
        member_id=member_id,
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Team member not found",
        )

    return member


@router.put(
    "/{member_id}",
    response_model=TeamMemberResponse,
)
def update(
    member_id: int,
    data: TeamMemberUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    member = get_team_member(
        db=db,
        member_id=member_id,
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Team member not found",
        )

    return update_team_member(
        db=db,
        member=member,
        data=data,
    )


@router.delete(
    "/{member_id}",
)
def delete(
    member_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    member = get_team_member(
        db=db,
        member_id=member_id,
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Team member not found",
        )

    delete_team_member(
        db=db,
        member=member,
    )

    return {
        "message": "Team member deleted successfully",
    }