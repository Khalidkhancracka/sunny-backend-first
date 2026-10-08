from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.media import MediaCreate, MediaResponse
from app.services.media import (
    create_media,
    delete_media,
    get_media,
    get_media_files,
)


router = APIRouter(
    prefix="/media",
    tags=["Media"],
)


@router.post(
    "",
    response_model=MediaResponse,
)
def create(
    data: MediaCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    return create_media(
        db=db,
        data=data,
    )


@router.get(
    "",
    response_model=list[MediaResponse],
)
def list_all(
    db: Session = Depends(get_db),
):
    return get_media_files(
        db=db,
    )


@router.get(
    "/{media_id}",
    response_model=MediaResponse,
)
def get_one(
    media_id: int,
    db: Session = Depends(get_db),
):
    media = get_media(
        db=db,
        media_id=media_id,
    )

    if not media:
        raise HTTPException(
            status_code=404,
            detail="Media not found",
        )

    return media


@router.delete(
    "/{media_id}",
)
def delete(
    media_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    media = get_media(
        db=db,
        media_id=media_id,
    )

    if not media:
        raise HTTPException(
            status_code=404,
            detail="Media not found",
        )

    delete_media(
        db=db,
        media=media,
    )

    return {
        "message": "Media deleted successfully",
    }