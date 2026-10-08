
from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.db.models import AdminUser


def authenticate_admin(
    db: Session,
    username: str,
    password: str,
):
    admin = db.query(AdminUser).filter(
        AdminUser.username == username
    ).first()

    if not admin:
        return None

    if not verify_password(password, admin.password_hash):
        return None

    if not admin.is_active:
        return None

    access_token = create_access_token(
        subject=str(admin.id),
        role=admin.role,
    )

    return admin, access_token

