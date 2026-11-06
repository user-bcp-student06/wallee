---
id: DISC-02-W5
titulo: W5 — Manejo de fallas de pago y reversos
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/user-stories/payment-failure-reversal-handling.sp.md]
depende_de: [DISC-02-W2, DISC-02-W4, DISC-04-02]
lo_consumen: [AI Engineer B, AI Engineer A, QA & Security, Arquitecto/a]
---

## Resumen
Los pagos fallidos, expirados y disputados siguen rutas de atención explícitas, con guía del agente y HITL. Se comprometen los 4 AC. Se construye con el Crew en el Sprint 2.

## 1. Historia
Como especialista de soporte al cliente, quiero que los pagos fallidos, expirados y disputados sigan rutas de atención explícitas, para que los usuarios reciban guía consistente y soporte pueda resolver incidentes de forma predecible.

## 2. Real y mock
| Real | Mock |
|---|---|
| Clasificación, códigos de motivo, vista de soporte, registro de acciones, agente (interpreta, recomienda, explica, escala) | Reversos monetarios y core/settlement |

## 3. AC (texto original)
| ID | Criterio |
|---|---|
| W5-AC1 | Los resultados fallido y expirado se clasifican y almacenan con un código de motivo legible por máquina |
| W5-AC2 | La vista de soporte muestra si un pago es elegible para reintento, investigación o flujo de disputa |
| W5-AC3 | La ayuda diferencia una falla técnica de un escenario de transferencia ya ejecutada |
| W5-AC4 | Las acciones de soporte se registran con referencia de transacción y estado de resolución |

## 4. Comprometidos vs diferidos
| AC | Hoy | Motivo |
|---|---|---|
| AC1–AC4 | Comprometidos | Cierran el flujo de excepciones de la demo |

## 5. Reglas aplicables
RN-12, RN-14, RN-15, RN-16, RN-08.

## 6. Estados
DECLINED→fallido y TIMEOUT→expirado, con ruta: reintento, investigación o disputa ([estados](../../04-reglas-y-contratos/02-estados-y-transiciones.md)).

## 7. Dependencias
W2 (estados terminales) y W4 (sin cobros duplicados al reintentar). Componente: Crew de agentes.

## 8. Bordes y errores
- Reintento tras expirado con la misma clave (W4): devuelve el original.
- Estado incierto tras TIMEOUT: ruta de investigación.
- Transferencia ya ejecutada: no se ofrece reintento; ruta de disputa (RN-15).
- Decisión crítica del agente: escala a un humano (HITL).

## 9. QA debe probar
| Caso | Qué prueba |
|---|---|
| W5-AC1-T2 | Fallido y expirado guardan un código de motivo |
| W5-AC2-T2 | La vista indica reintento, investigación o disputa |
| W5-AC3-T2 | Falla técnica vs transferencia ejecutada reciben ayuda distinta |
| W5-AC3-T3 | El agente escala con HITL y no ejecuta acciones fuera de su guardrail |
| W5-AC4-T2 | Acción de soporte registrada con referencia y estado |

## 10. Evidencia esperada
Tests, salida del Crew con la recomendación y registro de la acción de soporte, en `evidence.md`.

## 11. Definición de listo
AC1–AC4 con T1 y T2 en verde y W5 integrado a las 14:45.

## 12. Plan por sprint
| Sprint | Horario | Trabajo |
|---|---|---|
| 1 | — | Preparar casos de QA y definir los códigos de motivo con AI Engineer A |
| 2 | 13:45–14:45 | W5-AC1-T1 a W5-AC4-T1 con el Crew |
| 2 | 14:45–15:05 | Integración |

## 13. Preguntas abiertas
| ID | Pregunta | Supuesto PROPUESTO |
|---|---|---|
| PA-05 | ¿Qué categorías de disputa se habilitan en MVP? | Solo se clasifica y registra la ruta; la resolución se difiere (SUP-11) |
| PA-06 | Niveles de escalamiento y SLA | Sin SLA formal; el escalamiento es HITL a un humano (SUP-12) |

## Decisiones pendientes
- PA-05, PA-06.

## Siguiente paso para el rol consumidor
AI Engineer B: construir W5 con el Crew entre 13:45 y 14:45. QA & Security: definir los guardrails del agente.
