from sqlmodel import Field, SQLModel


class ProductBase(SQLModel):
    name: str = Field(index=True)
    description: str | None = Field(default=None)
    price: float | None = Field(default=None)
    in_stock: bool = Field(default=False)


class Product(ProductBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(SQLModel):  # Tous les champs sont optionnels pour une mise à jour
    name: str | None = None
    description: str | None = None
    price: float | None = None
    in_stock: bool | None = None