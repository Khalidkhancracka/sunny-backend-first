
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth import authenticate_admin


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post("/login", response_model=TokenResponse)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db),
):
    result = authenticate_admin(
        db=db,
        username=login_data.username,
        password=login_data.password,
    )

    if not result:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password",
        )

    admin, access_token = result

    return TokenResponse(
        access_token=access_token,
    )

