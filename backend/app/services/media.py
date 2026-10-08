from sqlalchemy.orm import Session

from app.db.models import MediaFile
from app.schemas.media import MediaCreate


def create_media(
    db: Session,
    data: MediaCreate,
) -> MediaFile:
    media = MediaFile(
        storage_path=data.storage_path,
        mime_type=data.mime_type,
        size_bytes=data.size_bytes,
        original_name=data.original_name,
    )

    db.add(media)
    db.commit()
    db.refresh(media)

    return media


def get_media_files(
    db: Session,
) -> list[MediaFile]:
    return (
        db.query(MediaFile)
        .order_by(MediaFile.id.desc())
        .all()
    )


def get_media(
    db: Session,
    media_id: int,
) -> MediaFile | None:
    return (
        db.query(MediaFile)
        .filter(MediaFile.id == media_id)
        .first()
    )


def delete_media(
    db: Session,
    media: MediaFile,
) -> None:
    db.delete(media)
    db.commit()