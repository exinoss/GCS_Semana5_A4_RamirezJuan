# Definición de Baselines

## Baseline v1.0.0

- Commit aprobado: `0e5b9a8`.
- API con `GET /products` y `POST /products`.
- Pruebas automatizadas de consulta, creación y validación.
- SRS v1, README, changelog y estructura inicial.
- Estado: **Baselined**.

## Release v1.1.0

- Solicitud de cambio: `ISSUE-21` / GitHub Issue `#1`.
- Aprobación: GitHub Pull Request `#2`, fusionado en `main`.
- Retiro de configuración local del control de versiones.
- Normalización de tags según SemVer.
- Changelog, registro de estados y plantilla de PR actualizados.
- Estado: **Aprobado para liberación** mediante el Pull Request `#2`.

## Release v1.2.0

- Solicitudes de cambio: `ISSUE-22` (Issue #3), `ISSUE-23` (Issue #5),
  `ISSUE-24` (Issue #7), `ISSUE-25` (Issue #9).
- Aprobación: GitHub Pull Requests `#4`, `#6`, `#8` y el PR de este issue,
  todos fusionados en `main`.
- Se incorporó `LICENSE` (MIT) como elemento de configuración faltante.
- Se documentó la validación funcional de `REQ-001` y `REQ-002`.
- Se actualizó la trazabilidad completa en `CM_STATUS_REGISTER.md`.
- Se alineó la versión de la aplicación (`src/app.py`) a `1.2.0`.
- Estado: **Aprobado para liberación** mediante los Pull Requests del ciclo.

