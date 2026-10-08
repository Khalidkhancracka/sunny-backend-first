from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.site_settings import (
    SiteSettingsResponse,
    SiteSettingsUpdate,
)
from app.services.site_settings import (
    get_site_settings,
    update_site_settings,
)


router = APIRouter(
    prefix="/site-settings",
    tags=["Site Settings"],
)


@router.get(
    "",
    response_model=SiteSettingsResponse,
)
def get_settings(
    db: Session = Depends(get_db),
):
    settings = get_site_settings(db=db)

    if not settings:
        raise HTTPException(
            status_code=404,
            detail="Site settings not found",
        )

    return settings


@router.put(
    "",
    response_model=SiteSettingsResponse,
)
def update_settings(
    data: SiteSettingsUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    settings = get_site_settings(db=db)

    if not settings:
        raise HTTPException(
            status_code=404,
            detail="Site settings not found",
        )

    return update_site_settings(
        db=db,
        settings=settings,
        data=data,
    )