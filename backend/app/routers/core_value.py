from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.dependencies.auth import get_current_admin
from app.schemas.core_value import (
    CoreValueCreate,
    CoreValueResponse,
    CoreValueUpdate,
)
from app.services.core_value import (
    create_core_value,
    delete_core_value,
    get_core_value,
    get_core_values,
    update_core_value,
)


router = APIRouter(
    prefix="/core-values",
    tags=["Core Values"],
)


@router.post(
    "",
    response_model=CoreValueResponse,
)
def create(
    data: CoreValueCreate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    return create_core_value(
        db=db,
        data=data,
    )


@router.get(
    "",
    response_model=list[CoreValueResponse],
)
def list_all(
    db: Session = Depends(get_db),
):
    return get_core_values(
        db=db,
    )


@router.get(
    "/{value_id}",
    response_model=CoreValueResponse,
)
def get_one(
    value_id: int,
    db: Session = Depends(get_db),
):
    value = get_core_value(
        db=db,
        value_id=value_id,
    )

    if not value:
        raise HTTPException(
            status_code=404,
            detail="Core value not found",
        )

    return value


@router.put(
    "/{value_id}",
    response_model=CoreValueResponse,
)
def update(
    value_id: int,
    data: CoreValueUpdate,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    value = get_core_value(
        db=db,
        value_id=value_id,
    )

    if not value:
        raise HTTPException(
            status_code=404,
            detail="Core value not found",
        )

    return update_core_value(
        db=db,
        core_value=value,
        data=data,
    )


@router.delete(
    "/{value_id}",
)
def delete(
    value_id: int,
    db: Session = Depends(get_db),
    current_admin=Depends(get_current_admin),
):
    value = get_core_value(
        db=db,
        value_id=value_id,
    )

    if not value:
        raise HTTPException(
            status_code=404,
            detail="Core value not found",
        )

    delete_core_value(
        db=db,
        value=value,
    )

    return {
        "message": "Core value deleted successfully",
    }