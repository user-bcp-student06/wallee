---
id: DISC-05-01
titulo: Matriz de trazabilidad
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [DISC-02-03, DISC-03-02]
depende_de: [DISC-02-03]
lo_consumen: [AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
Plantilla HU → AC → task → test → commit → PR → evidencia para los 17 AC comprometidos. Las columnas Test, Commit, PR y Evidencia están vacías a propósito; las completa cada owner.

## Convención
Task: T1 construir, T2 probar, T3 caso de borde. El commit y el PR deben citar el ID de la task (`W4-AC2-T1`).

## Matriz
| HU | AC | Task construcción | Task prueba | Test (archivo o caso) | Commit | PR | Evidencia |
|---|---|---|---|---|---|---|---|
| W1 | W1-AC1 | W1-AC1-T1 | W1-AC1-T2 | | | | |
| W1 | W1-AC2 | W1-AC2-T1 | W1-AC2-T2 | | | | |
| W1 | W1-AC3 | W1-AC3-T1 | W1-AC3-T2, W1-AC3-T3 | | | | |
| W1 | W1-AC4 | W1-AC4-T1 | W1-AC4-T2 | | | | |
| W2 | W2-AC1 | W2-AC1-T1 | W2-AC1-T2 | | | | |
| W2 | W2-AC2 | W2-AC2-T1 | W2-AC2-T2 | | | | |
| W2 | W2-AC3 | W2-AC3-T1 | W2-AC3-T2 | | | | |
| W2 | W2-AC4 | W2-AC4-T1 | W2-AC4-T2, W2-AC4-T3 | | | | |
| W2 | W2-AC6 (parcial) | W2-AC6-T1 | W2-AC6-T2 | | | | |
| W4 | W4-AC1 | W4-AC1-T1 | W4-AC1-T2 | | | | |
| W4 | W4-AC2 | W4-AC2-T1 | W4-AC2-T2, W4-AC2-T3 | | | | |
| W4 | W4-AC3 | W4-AC3-T1 | W4-AC3-T2 | | | | |
| W4 | W4-AC4 (parcial) | W4-AC4-T1 | W4-AC4-T2 | | | | |
| W5 | W5-AC1 | W5-AC1-T1 | W5-AC1-T2 | | | | |
| W5 | W5-AC2 | W5-AC2-T1 | W5-AC2-T2 | | | | |
| W5 | W5-AC3 | W5-AC3-T1 | W5-AC3-T2, W5-AC3-T3 | | | | |
| W5 | W5-AC4 | W5-AC4-T1 | W5-AC4-T2 | | | | |

## Diferidos (sin fila de ejecución)
W1-AC5, W1-AC6, W2-AC5 (KPI) · W3-AC1 a W3-AC4 (stretch) · W6-AC1 a W6-AC4 (stretch). Si se activan, se agregan filas.

## Decisiones pendientes
- Ninguna.

## Siguiente paso para el rol consumidor
Cada owner: completar Commit, PR y Evidencia al cerrar cada task; QA completa la columna Test.
