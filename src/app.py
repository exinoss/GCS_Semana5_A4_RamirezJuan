"""Aplicación FastAPI para administrar un inventario en memoria."""

from fastapi import FastAPI, status
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    """Datos necesarios para registrar un producto."""

    name: str = Field(min_length=1)
    qty: int = Field(ge=0)


class Product(ProductCreate):
    """Producto almacenado en el inventario."""


app = FastAPI(title="API Inventario", version="1.1.0")
products: list[Product] = []


@app.get("/products", response_model=list[Product])
async def list_products() -> list[Product]:
    """Devuelve todos los productos registrados."""

    return products


@app.post(
    "/products",
    response_model=Product,
    status_code=status.HTTP_201_CREATED,
)
async def add_product(product: ProductCreate) -> Product:
    """Registra un producto válido en el inventario."""

    stored_product = Product(name=product.name, qty=product.qty)
    products.append(stored_product)
    return stored_product
