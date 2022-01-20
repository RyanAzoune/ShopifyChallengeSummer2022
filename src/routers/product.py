from typing import List
from fastapi import status, HTTPException, Depends, APIRouter
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from src.utils import csv_iterator
from src.database import get_session
from src import models, schemas

router = APIRouter()


@router.post("/product", response_model=schemas.Product, status_code=status.HTTP_201_CREATED)
def create_product(request: schemas.ProductCreate, session: Session = Depends(get_session)):
    """
    Add a product to inventory.
    """

    product = models.Product(
        name=request.name, price=request.price, quantity=request.quantity)

    session.add(product)
    session.commit()
    session.refresh(product)

    return product


@router.get("/product/{id}", response_model=schemas.Product)
def read_product(id: int, session: Session = Depends(get_session)):
    """
    Get a product from inventory by id.
    """
    product = session.query(models.Product).get(id)

    if not product:
        raise HTTPException(
            status_code=404, detail=f"Product with id={id} not found")

    return product


@router.put("/product/{id}", response_model=schemas.Product)
def update_product(id: int, request: schemas.ProductUpdate, session: Session = Depends(get_session)):
    """
    Update a product in inventory by the given id.
    """

    product = session.query(models.Product).get(id)

    if product:
        # Overwrite fields of the product with the values specified in
        # the request, excluding unset fields.
        update_data = request.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(product, key, value)

        session.commit()

    if not product:
        raise HTTPException(
            status_code=404, detail=f"Product with id={id} not found")

    return product


@router.delete("/product/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, session: Session = Depends(get_session)):
    """
    Delete a product in inventory by the given id.
    """

    product = session.query(models.Product).get(id)

    if product:
        session.delete(product)
        session.commit()
    else:
        raise HTTPException(
            status_code=404, detail=f"product with id {id} not found")

    return None


@router.get("/product", response_model=List[schemas.Product])
def read_product_list(session: Session = Depends(get_session)):
    """
    Get all products in inventory.
    """

    product_list = session.query(models.Product).all()

    return product_list


@router.get('/export_csv')
async def export_csv(session: Session = Depends(get_session)):
    """
    Export all products in inventory to CSV format.
    """
    # This function is async s.t. we do not block when streaming the CSV data

    columns = models.Product.__table__.columns.keys()
    rows = session.query(models.Product).all()

    response = StreamingResponse(
        csv_iterator(rows, columns),
        media_type="text/csv"
    )

    response.headers["Content-Disposition"] = "attachment; filename=products.csv"

    return response
