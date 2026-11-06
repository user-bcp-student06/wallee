---
id: DISC-06-AIA
titulo: Handoff — AI Engineer A (dominio/backend)
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [DISC-02-W1, DISC-02-W2, DISC-02-W4, DISC-03-02]
depende_de: [DISC-03-02]
lo_consumen: [AI Engineer A]
---

## Resumen
Construyes el dominio: onboarding, pago a contacto e idempotencia, en ese orden.

## Objetivo
W1, W2 y W4 en verde a las 12:30, con tests de comportamiento e idempotencia.

## HU y AC que te tocan
| HU | AC | Hora |
|---|---|---|
| [W1](../02-producto/historias/W1-onboarding.md) | AC1–AC4 | 11:15 |
| [W2](../02-producto/historias/W2-pago-contacto.md) | AC1–AC4, AC6 parcial | 11:45 |
| [W4](../02-producto/historias/W4-idempotencia.md) | AC1–AC4 (AC4 parcial) | 12:30 |
| W3, luego W6 (stretch) | Ninguno comprometido | Solo si el PO confirma |

## Entradas que necesitas
| Entrada | De quién |
|---|---|
| Base (repo, mock, directorio sintético) | Arquitecto/a, 10:45 |
| Reglas RN-01 a RN-18 | PO |
| Casos de prueba T2/T3 | QA & Security |

## Entregables y hora límite
Ver [plan de sprints](../03-alcance-hackathon/02-plan-de-sprints.md). Cada task T1 se referencia en commit y PR con su ID.

## Decisiones que consultas al PO (HITL)
Cambiar S/ 500, 24 h o el mapeo de estados · omitir un AC comprometido · empezar el stretch.

## Definición de listo
T1 y T2 en verde por AC; escenarios mock demostrables sin intervención manual.

## No te corresponde
Elegir arquitectura sin el Arquitecto/a, construir el Crew (AI Engineer B), usar datos reales o secretos.

## Decisiones pendientes
- PA-02, PA-04, PA-08.

## Siguiente paso para el rol consumidor
Empezar W1 a las 10:45, al cerrar la Base.
