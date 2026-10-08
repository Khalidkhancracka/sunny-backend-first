from sqlalchemy.orm import Session

from app.db.models import GalleryImage
from app.schemas.gallery import GalleryImageCreate, GalleryImageUpdate


def create_gallery_image(
    db: Session,
    data: GalleryImageCreate,
) -> GalleryImage:
    image = GalleryImage(
        file_id=data.file_id,
        caption=data.caption,
        display_order=data.display_order,
        is_published=data.is_published,
    )

    db.add(image)
    db.commit()
    db.refresh(image)

    return image


def get_gallery_images(
    db: Session,
) -> list[GalleryImage]:
    return (
        db.query(GalleryImage)
        .order_by(
            GalleryImage.display_order.asc(),
            GalleryImage.id.asc(),
        )
        .all()
    )


def get_gallery_image(
    db: Session,
    image_id: int,
) -> GalleryImage | None:
    return (
        db.query(GalleryImage)
        .filter(GalleryImage.id == image_id)
        .first()
    )


def update_gallery_image(
    db: Session,
    image: GalleryImage,
    data: GalleryImageUpdate,
) -> GalleryImage:
    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(image, field, value)

    db.commit()
    db.refresh(image)

    return image


def delete_gallery_image(
    db: Session,
    image: GalleryImage,
) -> None:
    db.delete(image)
    db.commit()