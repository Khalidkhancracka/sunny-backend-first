from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.about import AboutResponse, AboutUpdate
from app.services.about import get_about, update_about


router = APIRouter(
    prefix="/about",
    tags=["About"],
)


@router.get(
    "",
    response_model=AboutResponse,
)
def get_about_section(
    db: Session = Depends(get_db),
):
    about = get_about(db=db)

    if not about:
        raise HTTPException(
            status_code=404,
            detail="About section not found",
        )

    return about


@router.put(
    "",
    response_model=AboutResponse,
)
def update_about_section(
    data: AboutUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    about = get_about(db=db)

    if not about:
        raise HTTPException(
            status_code=404,
            detail="About section not found",
        )

    return update_about(
        db=db,
        about=about,
        data=data,
    )