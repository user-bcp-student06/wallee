---
id: DISC-06-ARQ
titulo: Handoff — Arquitecto/a
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [DISC-03-02, DISC-04-01, DISC-04-02, DISC-04-03]
depende_de: [DISC-03-02]
lo_consumen: [Arquitecto/a]
---

## Resumen
Defines la arquitectura, los mocks y los permisos. El PO solo entrega el qué; tú decides el cómo.

## Objetivo
Dejar una Base ejecutable a las 10:45 y un contrato claro (incluido `channel`: CONTACT | QR) para que AI Engineers y QA trabajen sin esperar.

## HU y AC que te tocan
Base y contrato de todas las HU comprometidas (W1, W2, W4, W5). No eres owner de AC; apruebas decisiones técnicas.

## Entradas que necesitas
| Entrada | De quién |
|---|---|
| [Reglas](../04-reglas-y-contratos/01-reglas-de-negocio.md), [estados](../04-reglas-y-contratos/02-estados-y-transiciones.md), [mock](../04-reglas-y-contratos/03-convenciones-mock.md) | PO |
| Confirmación del stack propuesto (SUP-08) | PO en el G1 |

## Entregables y hora límite
| Entregable | Hora |
|---|---|
| Confirmar o ajustar el stack | 10:15 |
| BASE-T1: repo ejecutable, mock, directorio sintético | 10:45 |
| Decisión de cómo persistir estados y registrar auditoría | 11:15 |
| Arquitectura en README | 15:15 |

## Decisiones que consultas al PO (HITL)
Cambio de S/ 500, 24 h o del mapeo de estados · cambio del orden o del número de HU · cualquier cosa que agregue alcance.

## Definición de listo
Base corre en local; mocks se disparan por último dígito; los demás roles no tienen bloqueos.

## No te corresponde
Priorizar HU, cambiar AC o cifras de negocio, implementar W1–W5 completos.

## Decisiones pendientes
- PA-09.

## Siguiente paso para el rol consumidor
Responder en el G1 si el stack propuesto se mantiene.
