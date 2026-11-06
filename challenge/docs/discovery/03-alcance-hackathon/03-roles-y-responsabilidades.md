---
id: DISC-03-03
titulo: Roles y responsabilidades
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [base de hechos del prompt (Equipo)]
depende_de: [DISC-03-02]
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
Seis personas, solo estos roles; AI Engineer va dos veces (A dominio/backend, B Crew/agentes). La asignación de HUs es PROPUESTA.

## Roles
| Rol | Responsabilidad | HU / AC | Handoff |
|---|---|---|---|
| Product Owner | Prioriza, fija alcance, mantiene criterios, decide en HITL | Todas (decisiones) | — |
| Arquitecto/a | Define módulos, mocks, permisos y decisiones técnicas | Base, contrato `channel` | [arquitecto](../06-handoff-por-rol/arquitecto.md) |
| AI Engineer A (dominio/backend) | Implementa dominio, wallet, pagos, idempotencia | W1, W2, W4 (y stretch W3, W6) | [ai-engineer-a](../06-handoff-por-rol/ai-engineer-a-dominio.md) |
| AI Engineer B (Crew/agentes) | Implementa el Crew y la guía de excepciones | W5 | [ai-engineer-b](../06-handoff-por-rol/ai-engineer-b-crew.md) |
| QA & Security | Prueba flujos, bordes, fallos y guardrails desde el inicio | Casos T2/T3 de todas las HU | [qa-security](../06-handoff-por-rol/qa-security.md) |
| Presenter/Timekeeper | Controla tiempos, evidencia y pitch | Docs y demo | [presenter](../06-handoff-por-rol/presenter.md) |

## Reglas de colaboración
- Cada cambio referencia el ID de la HU, el AC y la task en commit y PR.
- Las decisiones que cambian alcance, cifras o AC se consultan al PO (HITL).
- Todos pueden ser preguntados en el pitch: cada persona debe conocer las HU comprometidas.

## Decisiones pendientes
- PA-10: confirmar la asignación de owners.

## Siguiente paso para el rol consumidor
Cada persona: leer su handoff y el [mapa de historias](../02-producto/03-mapa-de-historias.md).
