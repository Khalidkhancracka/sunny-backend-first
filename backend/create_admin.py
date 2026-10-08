
from getpass import getpass

from app.core.security import hash_password
from app.db.database import SessionLocal
from app.db.models import AdminUser


db = SessionLocal()

try:
    username = input("Admin username: ")
    password = getpass("Admin password: ")

    admin = AdminUser(
        username=username,
        password_hash=hash_password(password),
        role="super_admin",
        is_active=True,
    )

    db.add(admin)
    db.commit()
    db.refresh(admin)

    print(f"Admin created successfully with ID: {admin.id}")

except Exception:
    db.rollback()
    raise

finally:
    db.close()

