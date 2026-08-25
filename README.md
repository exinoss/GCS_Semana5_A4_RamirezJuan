# API Inventario (mini)

API mínima para registrar y consultar productos. El proyecto se utiliza para
demostrar gestión de configuración, versionado y trazabilidad en Git.

## Endpoints

- `GET /products`: lista los productos registrados.
- `POST /products`: agrega un producto con nombre y cantidad mayor o igual a cero.

## Requisitos

- Python 3.12 o superior.
- `uv` para administrar el entorno y las dependencias.

## Instalación y ejecución

```bash
uv sync
uv run uvicorn src.app:app --reload
```

La documentación interactiva estará disponible en `http://127.0.0.1:8000/docs`.

## Pruebas

```bash
uv run pytest
```

## Convenciones

- Commits: `chore`, `docs`, `feat` o `fix` más una referencia `ISSUE-xx`.
- Versiones: SemVer con el formato `vMAJOR.MINOR.PATCH`.
- Todo cambio aprobado debe vincular un Issue, un Pull Request y su evidencia en
  el registro de estados.

## Baselines

- `v1.0.0`: API, pruebas, SRS v1 y documentación inicial.
- `v1.1.0`: saneamiento de seguridad, versionado y trazabilidad de `ISSUE-21`.
- `v1.2.0`: auditoría de configuración (física, funcional y de trazabilidad) y
  release controlado, `ISSUE-22` a `ISSUE-25`.
