---
id: DISC-06-QA
titulo: Handoff — QA & Security
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [DISC-02-W1, DISC-02-W2, DISC-02-W4, DISC-02-W5, DISC-04-01]
depende_de: [DISC-03-02]
lo_consumen: [QA & Security]
---

## Resumen
Pruebas flujos, bordes, fallos y guardrails desde el inicio, no al final. Cubres todos los AC comprometidos.

## Objetivo
Cada AC comprometido tiene un caso T2 (y T3 si hay borde) y evidencia real en `evidence.md`.

## HU y AC que te tocan
| HU | Casos |
|---|---|
| W1 | W1-AC1-T2, W1-AC2-T2, W1-AC3-T2, W1-AC3-T3, W1-AC4-T2 |
| W2 | W2-AC1-T2, W2-AC2-T2, W2-AC3-T2, W2-AC4-T2, W2-AC4-T3, W2-AC6-T2 |
| W4 | W4-AC1-T2, W4-AC2-T2, W4-AC2-T3, W4-AC3-T2, W4-AC4-T2 |
| W5 | W5-AC1-T2, W5-AC2-T2, W5-AC3-T2, W5-AC3-T3, W5-AC4-T2 |

Los casos de W3 y W6 están en sus HU y solo aplican si se activan.

## Entradas que necesitas
| Entrada | De quién |
|---|---|
| Reglas, estados y convención mock | PO |
| Código a probar | AI Engineer A y B |

## Entregables y hora límite
| Entregable | Hora |
|---|---|
| Casos y datos sintéticos de W1 | 11:15 |
| Casos de W2 | 11:45 |
| Casos de W4 (incluye callback duplicado y simultáneas) | 12:30 |
| Casos de W5 y guardrails del agente | 14:45 |
| Evidencia en `evidence.md` | 15:15 |

## Seguridad
- Sin datos reales, secretos ni credenciales en el repositorio.
- Validar entradas (celular, alias, monto) y que el agente no exceda sus guardrails.
- No afirmar que algo pasó sin salida real de la prueba.

## Decisiones que consultas al PO (HITL)
Un AC que no se puede probar · una regla ambigua · un hallazgo que afecte un AC comprometido.

## Definición de listo
Todos los casos T2 ejecutados con salida real adjunta; los fallos reportados con su AC.

## No te corresponde
Corregir el código de otros ni cambiar reglas de negocio.

## Decisiones pendientes
- PA-02, PA-04, PA-08.

## Siguiente paso para el rol consumidor
Empezar los casos de W1 en la Base (10:15), antes de que exista el código.
