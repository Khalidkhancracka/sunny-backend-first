from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.hero import HeroResponse, HeroUpdate
from app.services.hero import get_hero, update_hero


router = APIRouter(
    prefix="/hero",
    tags=["Hero"],
)


@router.get(
    "",
    response_model=HeroResponse,
)
def get_hero_section(
    db: Session = Depends(get_db),
):
    hero = get_hero(db=db)

    if not hero:
        raise HTTPException(
            status_code=404,
            detail="Hero section not found",
        )

    return hero


@router.put(
    "",
    response_model=HeroResponse,
)
def update_hero_section(
    data: HeroUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    hero = get_hero(db=db)

    if not hero:
        raise HTTPException(
            status_code=404,
            detail="Hero section not found",
        )

    return update_hero(
        db=db,
        hero=hero,
        data=data,
    )