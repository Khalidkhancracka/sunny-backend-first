from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.db.models import Product
from app.schemas.product_image import (
    ProductImageCreate,
    ProductImageResponse,
    ProductImageUpdate,
)
from app.services.product_image import (
    create_product_image,
    delete_product_image,
    get_product_image,
    get_product_images,
    update_product_image,
)


router = APIRouter(
    prefix="/products/{product_id}/images",
    tags=["Product Images"],
)


@router.post(
    "",
    response_model=ProductImageResponse,
)
def create(
    product_id: int,
    data: ProductImageCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return create_product_image(
        db=db,
        product_id=product_id,
        data=data,
    )


@router.get(
    "",
    response_model=list[ProductImageResponse],
)
def list_all(
    product_id: int,
    db: Session = Depends(get_db),
):
    return get_product_images(
        db=db,
        product_id=product_id,
    )


@router.get(
    "/{image_id}",
    response_model=ProductImageResponse,
)
def get_one(
    product_id: int,
    image_id: int,
    db: Session = Depends(get_db),
):
    image = get_product_image(
        db=db,
        image_id=image_id,
    )

    if not image or image.product_id != product_id:
        raise HTTPException(
            status_code=404,
            detail="Product image not found",
        )

    return image


@router.put(
    "/{image_id}",
    response_model=ProductImageResponse,
)
def update(
    product_id: int,
    image_id: int,
    data: ProductImageUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    image = get_product_image(
        db=db,
        image_id=image_id,
    )

    if not image or image.product_id != product_id:
        raise HTTPException(
            status_code=404,
            detail="Product image not found",
        )

    return update_product_image(
        db=db,
        image=image,
        data=data,
    )


@router.delete(
    "/{image_id}",
)
def delete(
    product_id: int,
    image_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    image = get_product_image(
        db=db,
        image_id=image_id,
    )

    if not image or image.product_id != product_id:
        raise HTTPException(
            status_code=404,
            detail="Product image not found",
        )

    delete_product_image(
        db=db,
        image=image,
    )

    return {
        "message": "Product image deleted successfully",
    }