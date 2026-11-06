---
id: DISC-06-AIB
titulo: Handoff — AI Engineer B (Crew/agentes)
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [DISC-02-W5, DISC-02-02, DISC-03-02]
depende_de: [DISC-03-02]
lo_consumen: [AI Engineer B]
---

## Resumen
Construyes el Crew que interpreta, recomienda, explica y escala excepciones de pago (W5) en el Sprint 2.

## Objetivo
W5 integrado a las 14:45, con un agente que no ejecuta acciones críticas sin un humano.

## HU y AC que te tocan
| HU | AC | Hora |
|---|---|---|
| [W5](../02-producto/historias/W5-fallas-reversos.md) | AC1–AC4 | 14:45 |

## Entradas que necesitas
| Entrada | De quién |
|---|---|
| Estados terminales y códigos de motivo | AI Engineer A (W2) |
| Idempotencia al reintentar | AI Engineer A (W4) |
| Guardrails y casos de prueba | QA & Security |
| Rutas de atención (reintento, investigación, disputa) | [estados](../04-reglas-y-contratos/02-estados-y-transiciones.md) |

## Entregables y hora límite
| Entregable | Hora |
|---|---|
| Definir con AI Engineer A los códigos de motivo | 12:30 |
| W5-AC1-T1 a W5-AC4-T1 con el Crew | 14:45 |
| Integración del Crew al flujo | 15:05 |

## Decisiones que consultas al PO (HITL)
Qué acciones puede ejecutar el agente sin humano · qué se escala · cambio de categorías de disputa (PA-05).

## Definición de listo
Los cuatro AC en verde; el agente escala con HITL y respeta sus guardrails; la demo muestra una excepción.

## No te corresponde
Cambiar las reglas de idempotencia, ejecutar reversos monetarios reales, resolver disputas (solo clasificar y registrar, SUP-11).

## Decisiones pendientes
- PA-05, PA-06.

## Siguiente paso para el rol consumidor
Antes de 13:45, acordar con QA & Security los guardrails del agente.
