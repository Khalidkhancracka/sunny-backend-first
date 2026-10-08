from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.social_link import (
    SocialLinkCreate,
    SocialLinkResponse,
    SocialLinkUpdate,
)
from app.services.social_link import (
    create_social_link,
    delete_social_link,
    get_social_link,
    get_social_links,
    update_social_link,
)


router = APIRouter(
    prefix="/social-links",
    tags=["Social Links"],
)


@router.post(
    "",
    response_model=SocialLinkResponse,
)
def create(
    data: SocialLinkCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    return create_social_link(
        db=db,
        data=data,
    )


@router.get(
    "",
    response_model=list[SocialLinkResponse],
)
def list_all(
    db: Session = Depends(get_db),
):
    return get_social_links(
        db=db,
    )


@router.get(
    "/{link_id}",
    response_model=SocialLinkResponse,
)
def get_one(
    link_id: int,
    db: Session = Depends(get_db),
):
    link = get_social_link(
        db=db,
        link_id=link_id,
    )

    if not link:
        raise HTTPException(
            status_code=404,
            detail="Social link not found",
        )

    return link


@router.put(
    "/{link_id}",
    response_model=SocialLinkResponse,
)
def update(
    link_id: int,
    data: SocialLinkUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    link = get_social_link(
        db=db,
        link_id=link_id,
    )

    if not link:
        raise HTTPException(
            status_code=404,
            detail="Social link not found",
        )

    return update_social_link(
        db=db,
        link=link,
        data=data,
    )


@router.delete(
    "/{link_id}",
)
def delete(
    link_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    link = get_social_link(
        db=db,
        link_id=link_id,
    )

    if not link:
        raise HTTPException(
            status_code=404,
            detail="Social link not found",
        )

    delete_social_link(
        db=db,
        link=link,
    )

    return {
        "message": "Social link deleted successfully",
    }