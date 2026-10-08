from app.schemas.auth import LoginRequest, TokenResponse
from app.schemas.admin import (
    AdminCreate,
    AdminUpdate,
    AdminStatusUpdate,
    AdminPasswordReset,
    AdminResponse,
)
from app.schemas.media import MediaResponse
from app.schemas.site_settings import (
    SiteSettingsUpdate,
    SiteSettingsResponse,
)
from app.schemas.social_link import (
    SocialLinkCreate,
    SocialLinkUpdate,
    SocialLinkResponse,
)
from app.schemas.hero import HeroUpdate, HeroResponse
from app.schemas.about import AboutUpdate, AboutResponse
from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
    CategorySummary,
)
from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse,
    ProductDetailResponse,
)
from app.schemas.product_image import (
    ProductImageCreate,
    ProductImageUpdate,
    ProductImageResponse,
)
from app.schemas.gallery import (
    GalleryImageCreate,
    GalleryImageUpdate,
    GalleryImageResponse,
)
from app.schemas.core_value import (
    CoreValueCreate,
    CoreValueUpdate,
    CoreValueResponse,
)
from app.schemas.team_member import (
    TeamMemberCreate,
    TeamMemberUpdate,
    TeamMemberResponse,
)
from app.schemas.newsletter import (
    NewsletterSubscribe,
    NewsletterSubscriberResponse,
)


print("All schema modules imported successfully!")