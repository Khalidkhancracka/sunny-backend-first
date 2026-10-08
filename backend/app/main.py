from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.routers.admin_api import router as admin_api_router
from app.routers.public_api import router as public_api_router
from app.routers.auth import router as auth_router
from app.routers.category import router as category_router
from app.routers.product import router as product_router
from app.routers.product_image import router as product_image_router
from app.routers.gallery import router as gallery_router
from app.routers.team_member import router as team_member_router
from app.routers.core_value import router as core_value_router
from app.routers.social_link import router as social_link_router
from app.routers.site_settings import router as site_settings_router
from app.routers.hero import router as hero_router
from app.routers.about import router as about_router
from app.routers.media import router as media_router


app = FastAPI()
app.include_router(admin_api_router)
app.include_router(public_api_router)
app.include_router(auth_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(product_image_router)
app.include_router(gallery_router)
app.include_router(team_member_router)
app.include_router(core_value_router)
app.include_router(social_link_router)
app.include_router(site_settings_router)
app.include_router(hero_router)
app.include_router(about_router)
app.include_router(media_router)



@app.get("/")
def root():
    return {"message": "Backend is working!"}


@app.get("/db-test")
def db_test(db: Session = Depends(get_db)):
    return {"message": "Database session created successfully"}


@app.get("/admin-test")
def admin_test(current_admin=Depends(get_current_admin)):
    return {
        "message": "Authentication successful",
        "admin_id": current_admin.id,
        "role": current_admin.role,
    }