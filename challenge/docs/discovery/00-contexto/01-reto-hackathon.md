---
id: DISC-00-01
titulo: Reto del hackathon — reglas, cronograma, rúbrica y artefactos
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [base de hechos del prompt del PO (sección 2)]
depende_de: []
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
Hackathon AI Engineering Día 5: construir una wallet de pagos cotidianos de bajo monto en Perú (no es un core bancario), dirigida al público de transporte público. Se evalúa funcionalidad, calidad, trazabilidad y defensa.

## Público objetivo
Usuarios de transporte público que pagan trayectos de bajo monto con la wallet.

| Modalidad | Incluida |
|---|---|
| Trenes | Sí |
| Buses | Sí |
| Metropolitano | Sí |
| Bicicletas | Sí |
| Colectivos | Sí |

## Cronograma (hora local)
| Bloque | Horario | Notas |
|---|---|---|
| Scope check G1 | 10:00 | Confirmar stack y compromiso de HUs |
| Sprint 1 | 10:15–12:30 | 150 min |
| Almuerzo | 12:30–13:30 | |
| Scope check G2 | 13:30 | |
| Sprint 2 | 13:45–15:15 | 90 min |
| Freeze | 15:15–15:45 | GitHub, README, URL |
| Demo Arena | 16:00 | Pitch 6 min + 2 preguntas; todos pueden ser preguntados |

Hay 5 tickets de mentoría por equipo.

## Rúbrica (100 pts)
| Criterio | Peso | Detalle |
|---|---|---|
| Impacto de negocio | 10% | |
| Tecnología | 60% | D1 prompts+tests 10 · D2 skills/MCP 10 · D3 spec→tasks/pipeline/agente revisor 20 · D4 orquestación CrewAI 20 |
| Demo en vivo | 30% | Sin intervención manual, con excepciones |

## Criterios de éxito
Funcionalidad (flujo e2e en local) · Calidad (tests de comportamiento e idempotencia) · Trazabilidad · Defensa (mocks, decisiones, backlog pendiente).

## Artefactos mínimos
Wallet ejecutable (app o API local) · flujo vertical e2e · tests + mocks con datos sintéticos · README y arquitectura · PR + `evidence.md`.

## Controles transversales
Seguridad (datos sintéticos, sin secretos) · Guardrails (restricción de acciones) · HITL (humano en decisiones críticas o excepciones) · Trazabilidad (historia → task → commit → PR → evidencia).

## Decisiones pendientes
- PA-09: confirmar el stack propuesto en el G1 (ver [05-supuestos-restricciones](../01-discovery/05-supuestos-restricciones.md)).

## Siguiente paso para el rol consumidor
Leer el [plan de sprints](../03-alcance-hackathon/02-plan-de-sprints.md) y su handoff en [06-handoff-por-rol](../06-handoff-por-rol/).
