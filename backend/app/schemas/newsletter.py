from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class NewsletterSubscribe(BaseModel):
    email: EmailStr


class NewsletterSubscriberResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr
    is_active: bool
    subscribed_at: datetime