from sqlmodel import Session, select

from app.db.db_setup import engine
from app.models.product import Product, ProductCreate, ProductUpdate


def post_product(session: Session, product: ProductCreate) -> Product:
    db_product = Product.model_validate(product) 
    session.add(db_product)
    session.commit()
    session.refresh(db_product)
    return db_product

def get_product(session: Session, product_name: str) -> Product | None:
    query = select(Product).where(Product.name == product_name)
    return session.exec(query).first()


def get_all_products(session: Session) -> list[Product]:
    query = select(Product)
    return list(session.exec(query).all())


def update_product(session: Session, product_name: str, product_update: ProductUpdate) -> Product | None:
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
    product = get_product(session, product_name)
    if product:
        session.delete(product)
        session.commit()
        return product
    return None