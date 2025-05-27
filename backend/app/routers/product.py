from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.crud.product import (
    delete_product,
    get_all_products,
    get_product,
    post_product,
    update_product,
)
from app.db.db_setup import get_session
from app.models.product import Product, ProductCreate, ProductUpdate

router = APIRouter(
    tags=["products"], 
    responses={404: {"description": "No products found, sorry!"}}
)

@router.post("/products/", response_model=Product, status_code=201)
def create(product: ProductCreate, session: Session = Depends(get_session)) -> Product:
    new_product = Product.model_validate(product)
    return post_product(session, new_product)


@router.get("/products/{product_name}", response_model=Product, status_code=200)
def get_by_name(product_name: str, session: Session = Depends(get_session)) -> Product:
    product = get_product(session, product_name)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product