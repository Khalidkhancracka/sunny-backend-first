from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.services.product import (
    create_product,
    delete_product,
    get_product,
    get_products,
    update_product,
)


router = APIRouter(
    prefix="/products",
    tags=["Products"],
)


@router.post(
    "",
    response_model=ProductResponse,
)
def create(
    data: ProductCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    return create_product(
        db=db,
        data=data,
    )


@router.get(
    "",
    response_model=list[ProductResponse],
)
def list_all(
    db: Session = Depends(get_db),
):
    return get_products(db=db)


@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_one(
    product_id: int,
    db: Session = Depends(get_db),
):
    product = get_product(
        db=db,
        product_id=product_id,
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product


@router.put(
    "/{product_id}",
    response_model=ProductResponse,
)
def update(
    product_id: int,
    data: ProductUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    product = get_product(
        db=db,
        product_id=product_id,
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return update_product(
        db=db,
        product=product,
        data=data,
    )


@router.delete(
    "/{product_id}",
)
def delete(
    product_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    product = get_product(
        db=db,
        product_id=product_id,
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    delete_product(
        db=db,
        product=product,
    )

    return {
        "message": "Product deleted successfully",
    }