# Registro de Estados de Configuración

Fecha de corte: 2026-08-21  
Responsable: Juan Ramírez  
Solicitud de cambio: [ISSUE-21 / Issue #1](https://github.com/exinoss/GCS_Semana5_A4_RamirezJuan/issues/1)

| EC-ID | Elemento de configuración | Tipo | Versión/Ref | Estado | Responsable | Evidencia |
|:------|:--------------------------|:-----|:------------|:-------|:------------|:----------|
| EC-01 | `docs/SRS/SRS_v1.md` | Documento | `v1.0.0` → `v1.1.0` | Aprobado | Analista | Issue #1 + PR de `ISSUE-21` |
| EC-02 | `src/app.py` | Código | `v1.1.0` | Integrado | Desarrollo | Pruebas + PR de `ISSUE-21` |
| EC-03 | `tests/test_app.py` | Prueba | `v1.1.0` | Verificado | QA | `uv run pytest` |
| EC-04 | `CHANGELOG.md` | Documento | `v1.1.0` | Aprobado | Gestión | Issue #1 + release notes |
| EC-05 | `.gitignore` | Configuración | `v1.1.0` | Aprobado | DevOps | Commit de `ISSUE-21` |
| EC-06 | `config/.env.example` | Configuración | `v1.1.0` | Integrado | DevOps | Commit de `ISSUE-21` |
| EC-07 | `.github/pull_request_template.md` | Proceso | `v1.1.0` | Aprobado | Líder | PR de `ISSUE-21` |
| EC-08 | `README.md` | Documento | `v1.0.0` → `v1.1.0` | Aprobado | Equipo | Tags + PR de `ISSUE-21` |
| EC-09 | `pyproject.toml` y `uv.lock` | Configuración | `v1.1.0` | Verificado | Desarrollo | `uv sync` + pruebas |
| EC-10 | `docs/CM/BASELINE.md` | Documento | `v1.1.0` | Baselined | Gestión | Tags + release `v1.1.0` |

## Resumen de estados

- **Baseline `v1.0.0`:** commit `0e5b9a8`; incluye API, pruebas, SRS v1 y documentación inicial.
- **Release `v1.1.0`:** incluye saneamiento de seguridad, SemVer y trazabilidad de `ISSUE-21`.
- **Elementos retirados:** `config/.env`, por contener configuración local no versionable.
