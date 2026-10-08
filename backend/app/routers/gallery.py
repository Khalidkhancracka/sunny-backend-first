from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.gallery import (
    GalleryImageCreate,
    GalleryImageResponse,
    GalleryImageUpdate,
)
from app.services.gallery import (
    create_gallery_image,
    delete_gallery_image,
    get_gallery_image,
    get_gallery_images,
    update_gallery_image,
)


router = APIRouter(
    prefix="/gallery",
    tags=["Gallery"],
)


@router.post(
    "",
    response_model=GalleryImageResponse,
)
def create(
    data: GalleryImageCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    return create_gallery_image(
        db=db,
        data=data,
    )


@router.get(
    "",
    response_model=list[GalleryImageResponse],
)
def list_all(
    db: Session = Depends(get_db),
):
    return get_gallery_images(
        db=db,
    )


@router.get(
    "/{image_id}",
    response_model=GalleryImageResponse,
)
def get_one(
    image_id: int,
    db: Session = Depends(get_db),
):
    image = get_gallery_image(
        db=db,
        image_id=image_id,
    )

    if not image:
        raise HTTPException(
            status_code=404,
            detail="Gallery image not found",
        )

    return image


@router.put(
    "/{image_id}",
    response_model=GalleryImageResponse,
)
def update(
    image_id: int,
    data: GalleryImageUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    image = get_gallery_image(
        db=db,
        image_id=image_id,
    )

    if not image:
        raise HTTPException(
            status_code=404,
            detail="Gallery image not found",
        )

    return update_gallery_image(
        db=db,
        image=image,
        data=data,
    )


@router.delete(
    "/{image_id}",
)
def delete(
    image_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    image = get_gallery_image(
        db=db,
        image_id=image_id,
    )

    if not image:
        raise HTTPException(
            status_code=404,
            detail="Gallery image not found",
        )

    delete_gallery_image(
        db=db,
        image=image,
    )

    return {
        "message": "Gallery image deleted successfully",
    }