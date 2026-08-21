# SRS v1

## Requisitos funcionales

- **REQ-001:** El sistema permitirá listar los productos registrados mediante `GET /products`.
- **REQ-002:** El sistema permitirá agregar productos mediante `POST /products`, siempre que el nombre no esté vacío y la cantidad sea mayor o igual a cero.

## Requisitos no funcionales

- **RNF-001:** Los cambios deben ser trazables a un Issue y contar con evidencias.
- **RNF-002:** El versionado seguirá SemVer mediante tags y un changelog.
- **RNF-003:** Las dependencias y el entorno de Python serán administrados con `uv`.

