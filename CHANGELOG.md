# Changelog

Todos los cambios relevantes de este proyecto se documentarán en este archivo.

## [Unreleased]

- Pendiente.

## [v1.2.0] - 2026-08-24

### Auditoría de configuración

- Se agregó `LICENSE` (MIT), corrigiendo un hallazgo de la auditoría física de
  elementos de configuración (`ISSUE-22`).
- Se documentó la validación funcional de `REQ-001` y `REQ-002` con 3 criterios
  de aceptación por endpoint y evidencia de pruebas en
  `docs/CM/VALIDACION_FUNCIONAL.md` (`ISSUE-23`).
- Se actualizó `CM_STATUS_REGISTER.md` con la trazabilidad issue → PR → elemento
  de configuración del ciclo (`ISSUE-24`).
- Se preparó y documentó la emisión del release `v1.2.0` (`ISSUE-25`).

## [v1.1.0] - 2026-08-21

### Seguridad

- Se retiró `config/.env` del control de versiones.
- Se agregaron `.gitignore` y `config/.env.example` para evitar exposición de configuración local.

### Gestión de configuración

- Se normalizó el versionado mediante tags SemVer.
- Se documentó la baseline `v1.0.0` y el alcance de `v1.1.0`.
- Se completó el registro de estados de los elementos de configuración.
- Se agregó una plantilla de Pull Request con controles de trazabilidad.
- Se corrigieron requisitos y notas sin relación con el alcance del producto.

## [v1.0.0] - 2026-08-21

- Baseline inicial con la estructura auditable del repositorio.
- API mínima con operaciones para listar y agregar productos.
- SRS v1 y pruebas automatizadas iniciales.
