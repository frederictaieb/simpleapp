from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from src.db.crud import (
    delete_product,
    get_all_products,
    get_product,
    post_product,
    update_product,
)
from src.db.db_setup import get_session
from src.db.product import Product, ProductCreate, ProductUpdate

router = APIRouter(
    tags=["products"], 
    responses={404: {"description": "No products found, sorry!"}}
)

@router.post("/products/", response_model=Product, status_code=201)
def create(product: ProductCreate, session: Session = Depends(get_session)) -> Product:
    """
    Create a new product.

    Args:
        product (ProductCreate): The product data to create.
        session (Session, optional): The database session. Defaults to Depends(get_session).

    Returns:
        Product: The created product.
    """
    new_product = Product.model_validate(product)
    return post_product(session, new_product)


@router.get("/products/{product_name}", response_model=Product, status_code=200)
def get_by_name(product_name: str, session: Session = Depends(get_session)) -> Product:
    """
    Retrieve a product by its name.

    Args:
        product_name (str): The name of the product to retrieve.
        session (Session, optional): The database session. Defaults to Depends(get_session).

    Returns:
        Product: The retrieved product.

    Raises:
        HTTPException: If the product is not found.
    """
    product = get_product(session, product_name)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product