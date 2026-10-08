from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.category import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
)
from app.services.category import (
    create_category,
    delete_category,
    get_categories,
    get_category,
    update_category,
)


router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


@router.post(
    "",
    response_model=CategoryResponse,
)
def create(
    data: CategoryCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    return create_category(
        db=db,
        data=data,
    )


@router.get(
    "",
    response_model=list[CategoryResponse],
)
def list_all(
    db: Session = Depends(get_db),
):
    return get_categories(db=db)


@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
)
def get_one(
    category_id: int,
    db: Session = Depends(get_db),
):
    category = get_category(
        db=db,
        category_id=category_id,
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    return category


@router.put(
    "/{category_id}",
    response_model=CategoryResponse,
)
def update(
    category_id: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    category = get_category(
        db=db,
        category_id=category_id,
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    return update_category(
        db=db,
        category=category,
        data=data,
    )


@router.delete(
    "/{category_id}",
)
def delete(
    category_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    category = get_category(
        db=db,
        category_id=category_id,
    )

    if not category:
        raise HTTPException(
            status_code=404,
            detail="Category not found",
        )

    delete_category(
        db=db,
        category=category,
    )

    return {
        "message": "Category deleted successfully",
    }