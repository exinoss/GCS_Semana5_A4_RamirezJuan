# Registro de Estados de Configuración

Fecha de corte: 2026-08-21  
Responsable: Juan Ramírez  
Solicitud de cambio: [ISSUE-21 / Issue #1](https://github.com/exinoss/GCS_Semana5_A4_RamirezJuan/issues/1)
Pull Request aprobado: [PR #2](https://github.com/exinoss/GCS_Semana5_A4_RamirezJuan/pull/2)

| EC-ID | Elemento de configuración | Tipo | Versión/Ref | Estado | Responsable | Evidencia |
|:------|:--------------------------|:-----|:------------|:-------|:------------|:----------|
| EC-01 | `docs/SRS/SRS_v1.md` | Documento | `v1.0.0` → `v1.1.0` | Aprobado | Analista | Issue #1 + PR #2 |
| EC-02 | `src/app.py` | Código | `v1.1.0` | Integrado | Desarrollo | Pruebas + PR #2 |
| EC-03 | `tests/test_app.py` | Prueba | `v1.1.0` | Verificado | QA | `uv run pytest` |
| EC-04 | `CHANGELOG.md` | Documento | `v1.1.0` | Aprobado | Gestión | Issue #1 + release notes |
| EC-05 | `.gitignore` | Configuración | `v1.1.0` | Aprobado | DevOps | Commit de `ISSUE-21` |
| EC-06 | `config/.env.example` | Configuración | `v1.1.0` | Integrado | DevOps | Commit de `ISSUE-21` |
| EC-07 | `.github/pull_request_template.md` | Proceso | `v1.1.0` | Aprobado | Líder | PR #2 |
| EC-08 | `README.md` | Documento | `v1.0.0` → `v1.1.0` | Aprobado | Equipo | Tags + PR #2 |
| EC-09 | `pyproject.toml` y `uv.lock` | Configuración | `v1.1.0` | Verificado | Desarrollo | `uv sync` + pruebas |
| EC-10 | `docs/CM/BASELINE.md` | Documento | `v1.1.0` | Baselined | Gestión | Tags + release `v1.1.0` |

## Resumen de estados

- **Baseline `v1.0.0`:** commit `0e5b9a8`; incluye API, pruebas, SRS v1 y documentación inicial.
- **Release `v1.1.0`:** aprobada mediante PR #2; incluye saneamiento de seguridad, SemVer y trazabilidad de `ISSUE-21`.
- **Elementos retirados:** `config/.env`, por contener configuración local no versionable.

## Ciclo v1.2.0

Fecha de corte: 2026-08-24  
Responsable: Juan Ramírez  
Solicitudes de cambio: `ISSUE-22` (Issue #3), `ISSUE-23` (Issue #5), `ISSUE-24` (Issue #7)

| EC-ID | Elemento de configuración | Tipo | Versión/Ref | Estado | Responsable | Evidencia |
|:------|:--------------------------|:-----|:------------|:-------|:------------|:----------|
| EC-11 | `LICENSE` | Documento/Legal | `v1.2.0` | Aprobado | Auditor Físico | Issue #3 + PR #4 |
| EC-12 | `docs/CM/VALIDACION_FUNCIONAL.md` | Documento | `v1.2.0` | Aprobado | Auditor Funcional | Issue #5 + PR #6 |

### Resumen de estados — v1.2.0

- **Auditoría física (`ISSUE-22`):** se detectó y corrigió la ausencia de `LICENSE`; evidencia en Issue #3 + PR #4.
- **Auditoría funcional (`ISSUE-23`):** se verificaron los 6 criterios de aceptación (REQ-001/REQ-002) con la suite `uv run pytest`; evidencia en Issue #5 + PR #6.
- **Trazabilidad (`ISSUE-24`):** este registro conecta issue → PR → elemento de configuración para los dos hallazgos anteriores; evidencia en Issue #7.
