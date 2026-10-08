from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db.models import (
    Category,
    Product,
    ProductImage,
    GalleryImage,
    TeamMember,
    CoreValue,
    SocialLink,
)

from app.schemas.category import CategoryResponse
from app.schemas.product import ProductResponse
from app.schemas.product_image import ProductImageResponse
from app.schemas.gallery import GalleryImageResponse
from app.schemas.team_member import TeamMemberResponse
from app.schemas.core_value import CoreValueResponse
from app.schemas.social_link import SocialLinkResponse
from app.schemas.site_settings import SiteSettingsResponse
from app.schemas.hero import HeroResponse
from app.schemas.about import AboutResponse

from app.services.category import get_category
from app.services.product import get_product
from app.services.product_image import get_product_image
from app.services.gallery import get_gallery_image
from app.services.team_member import get_team_member
from app.services.core_value import get_core_value
from app.services.social_link import get_social_links
from app.services.site_settings import get_site_settings
from app.services.hero import get_hero
from app.services.about import get_about


router = APIRouter(
    prefix="/api/public",
    tags=["Public API"],
)


# ============================================================
# HERO
# ============================================================

@router.get(
    "/hero",
    response_model=HeroResponse,
)
def public_hero(
    db: Session = Depends(get_db),
):
    hero = get_hero(db=db)

    if not hero:
        raise HTTPException(
            status_code=404,
            detail="Hero section not found",
        )

    return hero


# ============================================================
# ABOUT
# ============================================================

@router.get(
    "/about",
    response_model=AboutResponse,
)
def public_about(
    db: Session = Depends(get_db),
):
    about = get_about(db=db)

    if not about:
        raise HTTPException(
            status_code=404,
            detail="About section not found",
        )

    return about


# ============================================================
# SITE SETTINGS
# ============================================================

@router.get(
    "/site-settings",
    response_model=SiteSettingsResponse,
)
def public_site_settings(
    db: Session = Depends(get_db),
):
    settings = get_site_settings(db=db)

    if not settings:
        raise HTTPException(
            status_code=404,
            detail="Site settings not found",
        )

    return settings


# ============================================================
# CATEGORIES
# ============================================================

@router.get(
    "/categories",
    response_model=list[CategoryResponse],
)
def public_categories(
    db: Session = Depends(get_db),
):
    return (
        db.query(Category)
        .filter(Category.is_published == True)
        .order_by(
            Category.display_order.asc(),
            Category.id.asc(),
        )
        .all()
    )


@router.get(
    "/categories/{category_id}",
    response_model=CategoryResponse,
)
def public_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    category = (
        db.query(Category)
        .filter(
            Category.id == category_id,
            Category.is_published == True,
        )
        .first()
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    return category


# ============================================================
# PRODUCTS
# ============================================================

@router.get(
    "/products",
    response_model=list[ProductResponse],
)
def public_products(
    db: Session = Depends(get_db),
):
    return (
        db.query(Product)
        .filter(Product.is_published == True)
        .order_by(
            Product.display_order.asc(),
            Product.id.asc(),
        )
        .all()
    )


@router.get(
    "/products/{product_id}",
    response_model=ProductResponse,
)
def public_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = (
        db.query(Product)
        .filter(
            Product.id == product_id,
            Product.is_published == True,
        )
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product


# ============================================================
# PRODUCT IMAGES
# ============================================================

@router.get(
    "/products/{product_id}/images",
    response_model=list[ProductImageResponse],
)
def public_product_images(
    product_id: int,
    db: Session = Depends(get_db),
):
    # Customer can only access images belonging to a
    # published product.
    product = (
        db.query(Product)
        .filter(
            Product.id == product_id,
            Product.is_published == True,
        )
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return (
        db.query(ProductImage)
        .filter(ProductImage.product_id == product_id)
        .order_by(
            ProductImage.display_order.asc(),
            ProductImage.id.asc(),
        )
        .all()
    )


@router.get(
    "/products/{product_id}/images/{image_id}",
    response_model=ProductImageResponse,
)
def public_product_image(
    product_id: int,
    image_id: int,
    db: Session = Depends(get_db),
):
    # Product must be published.
    product = (
        db.query(Product)
        .filter(
            Product.id == product_id,
            Product.is_published == True,
        )
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    image = (
        db.query(ProductImage)
        .filter(
            ProductImage.id == image_id,
            ProductImage.product_id == product_id,
        )
        .first()
    )

    if not image:
        raise HTTPException(
            status_code=404,
            detail="Product image not found",
        )

    return image


# ============================================================
# GALLERY
# ============================================================

@router.get(
    "/gallery",
    response_model=list[GalleryImageResponse],
)
def public_gallery(
    db: Session = Depends(get_db),
):
    return (
        db.query(GalleryImage)
        .filter(GalleryImage.is_published == True)
        .order_by(
            GalleryImage.display_order.asc(),
            GalleryImage.id.asc(),
        )
        .all()
    )


@router.get(
    "/gallery/{image_id}",
    response_model=GalleryImageResponse,
)
def public_gallery_image(
    image_id: int,
    db: Session = Depends(get_db),
):
    image = (
        db.query(GalleryImage)
        .filter(
            GalleryImage.id == image_id,
            GalleryImage.is_published == True,
        )
        .first()
    )

    if not image:
        raise HTTPException(
            status_code=404,
            detail="Gallery image not found",
        )

    return image


# ============================================================
# TEAM MEMBERS
# ============================================================

@router.get(
    "/team-members",
    response_model=list[TeamMemberResponse],
)
def public_team_members(
    db: Session = Depends(get_db),
):
    return (
        db.query(TeamMember)
        .filter(TeamMember.is_published == True)
        .order_by(
            TeamMember.display_order.asc(),
            TeamMember.id.asc(),
        )
        .all()
    )


@router.get(
    "/team-members/{member_id}",
    response_model=TeamMemberResponse,
)
def public_team_member(
    member_id: int,
    db: Session = Depends(get_db),
):
    member = (
        db.query(TeamMember)
        .filter(
            TeamMember.id == member_id,
            TeamMember.is_published == True,
        )
        .first()
    )

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Team member not found",
        )

    return member


# ============================================================
# CORE VALUES
# ============================================================

@router.get(
    "/core-values",
    response_model=list[CoreValueResponse],
)
def public_core_values(
    db: Session = Depends(get_db),
):
    return (
        db.query(CoreValue)
        .filter(CoreValue.is_published == True)
        .order_by(
            CoreValue.display_order.asc(),
            CoreValue.id.asc(),
        )
        .all()
    )


@router.get(
    "/core-values/{value_id}",
    response_model=CoreValueResponse,
)
def public_core_value(
    value_id: int,
    db: Session = Depends(get_db),
):
    value = (
        db.query(CoreValue)
        .filter(
            CoreValue.id == value_id,
            CoreValue.is_published == True,
        )
        .first()
    )

    if not value:
        raise HTTPException(
            status_code=404,
            detail="Core value not found",
        )

    return value


# ============================================================
# SOCIAL LINKS
# ============================================================

@router.get(
    "/social-links",
    response_model=list[SocialLinkResponse],
)
def public_social_links(
    db: Session = Depends(get_db),
):
    return (
        db.query(SocialLink)
        .filter(SocialLink.is_active == True)
        .order_by(
            SocialLink.display_order.asc(),
            SocialLink.id.asc(),
        )
        .all()
    )