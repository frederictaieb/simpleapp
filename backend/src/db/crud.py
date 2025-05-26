from sqlmodel import Session, select

from src.db.db_setup import engine
from src.db.product import Product, ProductCreate, ProductUpdate


def post_product(session: Session, product: ProductCreate) -> Product:
    """
    Adds a new product to the database.

    Args:
        product (ProductCreate): The product object to be added.

    Returns:
        Product: The added product object.

    """
    db_product = Product.model_validate(product) 
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


def get_product(session: Session, product_name: str) -> Product | None:
    """
    Retrieve a product from the database by its name.

    Args:
        product_name (str): The name of the product to retrieve.

    Returns:
        Product: The retrieved product.

    """
    query = select(Product).where(Product.name == product_name)
    return session.exec(query).first()


def get_all_products(session: Session) -> list[Product]:
    """
    Retrieve all products from the database.

    Returns:
        list[Product]: A list of all products.
    """
    query = select(Product)
    return list(session.exec(query).all())


def update_product(session: Session, product_name: str, product_update: ProductUpdate) -> Product | None:
    """
    Update an existing product.

    Args:
        product_name (str): The name of the product to update.
        product_update (ProductUpdate): The data to update the product with.

    Returns:
        Product: The updated product, or None if not found.
    """
    db_product = get_product(session, product_name)
    if not db_product:
        return None
    
    product_data = product_update.model_dump(exclude_unset=True)
    for key, value in product_data.items():
        setattr(db_product, key, value)
    
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product


def delete_product(session: Session, product_name: str) -> Product | None:
    """
    Delete a product from the database.

    Args:
        product_name (str): The name of the product to delete.

    Returns:
        Product: The deleted product, or None if not found.
    """
    product = get_product(session, product_name)
    if product:
        session.delete(product)
        session.commit()
        return product
    return None