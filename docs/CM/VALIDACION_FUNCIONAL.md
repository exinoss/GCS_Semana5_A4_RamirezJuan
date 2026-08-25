# Validación Funcional

Fecha: 2026-08-24
Responsable: Auditor Funcional
Referencia académica: `ISSUE-23` / GitHub Issue `#5`

## Requisito REQ-001 — `GET /products`

| # | Criterio de aceptación | Prueba que lo verifica | Resultado |
|:--|:------------------------|:------------------------|:----------|
| 1 | El endpoint responde `200 OK`. | `test_list_products_starts_empty` | Aprobado |
| 2 | Al no existir productos, devuelve una lista vacía `[]`. | `test_list_products_starts_empty` | Aprobado |
| 3 | Refleja los productos previamente agregados vía `POST /products`. | `test_add_and_list_product` | Aprobado |

## Requisito REQ-002 — `POST /products`

| # | Criterio de aceptación | Prueba que lo verifica | Resultado |
|:--|:------------------------|:------------------------|:----------|
| 1 | Crea un producto válido y responde `201 Created` con los datos registrados. | `test_add_and_list_product` | Aprobado |
| 2 | Rechaza con `422` un producto con nombre vacío. | `test_rejects_invalid_product` | Aprobado |
| 3 | Rechaza con `422` un producto con cantidad negativa. | `test_rejects_invalid_product` | Aprobado |

## Evidencia de ejecución

Comando ejecutado: `uv run pytest -v`

```
============================= test session starts =============================
platform win32 -- Python 3.12.3, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\Alex2\Documents\Visual Code\HTML\GCS_Semana5_A4_RamirezJuan
configfile: pyproject.toml
testpaths: tests
plugins: anyio-4.14.2
collected 4 items

tests\test_app.py ....                                                   [100%]

============================== 4 passed in 1.06s ==============================
```

## Conclusión

Los 6 criterios de aceptación (3 por endpoint) definidos para REQ-001 y REQ-002 del
SRS (`docs/SRS/SRS_v1.md`) quedan verificados mediante la suite automatizada
existente (`tests/test_app.py`), sin necesidad de cambios de código.
