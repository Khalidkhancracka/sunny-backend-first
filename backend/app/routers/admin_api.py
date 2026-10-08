from fastapi import APIRouter, Depends

from app.dependencies.auth import get_current_admin

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


router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"],
    dependencies=[Depends(get_current_admin)],
)


# Products
router.include_router(product_router)

# Product images
router.include_router(product_image_router)

# Categories
router.include_router(category_router)

# Gallery
router.include_router(gallery_router)

# Team members
router.include_router(team_member_router)

# Core values
router.include_router(core_value_router)

# Social links
router.include_router(social_link_router)

# Site settings
router.include_router(site_settings_router)

# Hero section
router.include_router(hero_router)

# About section
router.include_router(about_router)

# Media
router.include_router(media_router)