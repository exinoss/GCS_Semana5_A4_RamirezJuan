"""Pruebas de integración de los endpoints de inventario."""

import asyncio
from typing import Any

import httpx
import pytest

from src.app import app, products


@pytest.fixture(autouse=True)
def clear_inventory() -> None:
    """Aísla cada prueba limpiando el inventario en memoria."""

    products.clear()


def request(method: str, path: str, **kwargs: Any) -> httpx.Response:
    """Realiza una petición ASGI sin iniciar un servidor externo."""

    async def send() -> httpx.Response:
        transport = httpx.ASGITransport(app=app)
        async with httpx.AsyncClient(
            transport=transport,
            base_url="http://testserver",
        ) as client:
            return await client.request(method, path, **kwargs)

    return asyncio.run(send())


def test_list_products_starts_empty() -> None:
    response = request("GET", "/products")

    assert response.status_code == 200
    assert response.json() == []


def test_add_and_list_product() -> None:
    create_response = request(
        "POST",
        "/products",
        json={"name": "Teclado", "qty": 5},
    )

    assert create_response.status_code == 201
    assert create_response.json() == {"name": "Teclado", "qty": 5}

    list_response = request("GET", "/products")
    assert list_response.status_code == 200
    assert list_response.json() == [{"name": "Teclado", "qty": 5}]


@pytest.mark.parametrize(
    "payload",
    [
        {"name": "", "qty": 1},
        {"name": "Monitor", "qty": -1},
    ],
)
def test_rejects_invalid_product(payload: dict[str, object]) -> None:
    response = request("POST", "/products", json=payload)

    assert response.status_code == 422
