---
id: DISC-02-W6
titulo: W6 — Conciliación operativa de transacciones (stretch)
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/user-stories/operations-transaction-reconciliation.sp.md]
depende_de: [DISC-02-W4]
lo_consumen: [AI Engineer A, QA & Security, Arquitecto/a]
---

## Resumen
Conciliación diaria entre intenciones de pago, resultados del proveedor y asientos del ledger, con fixtures. Es stretch: 0 de 4 AC comprometidos (prioridad 6). Estado: DIFERIDO.

## 1. Historia
Como analista de operaciones, quiero una conciliación diaria entre intenciones de pago, resultados del proveedor y asientos del ledger de wallet, para detectar descalces temprano y mantener la integridad financiera del MVP.

## 2. Real y mock
| Real | Mock |
|---|---|
| Conciliación sobre fixtures, ledger local, resumen diario | Registros de resultado del proveedor y ledger corporativo |

## 3. AC (texto original)
| ID | Criterio |
|---|---|
| W6-AC1 | La salida diaria compara registros de transacción de wallet contra resultados del proveedor en los canales MVP |
| W6-AC2 | Cada descalce se marca con referencia, tipo de descalce y estado de investigación |
| W6-AC3 | Los reportes se filtran por fecha y canal de proveedor |
| W6-AC4 | Se genera un resumen diario con totales conciliados, no conciliados y resueltos |

## 4. Comprometidos vs diferidos
| AC | Hoy | Motivo |
|---|---|---|
| AC1–AC4 | Diferidos (stretch) | Prioridad 6; después de W3 |

## 5. Reglas aplicables
RN-03, RN-13 (distinguir original de reintento), RN-05.

## 6. Estados
Usa los estados terminales de W2; un descalce tiene su propio estado de investigación (nombres por definir).

## 7. Dependencias
W4 (marca de reintento, W4-AC4). Las herramientas de conciliación se definen en la implementación.

## 8. Bordes y errores
- Transacción en wallet sin resultado del proveedor, y al revés.
- Reintento duplicado: no debe contarse como transacción adicional.
- Día sin transacciones.

## 9. QA debe probar (si se activa)
| Caso | Qué prueba |
|---|---|
| W6-AC1-T2 | Comparación contra fixtures |
| W6-AC2-T2 | Descalce con referencia, tipo y estado |
| W6-AC3-T2 | Filtro por fecha y canal |
| W6-AC4-T2 | Totales coherentes con los registros |

## 10. Evidencia esperada
Reporte de conciliación sobre fixtures, solo si se activa.

## 11. Definición de listo
AC1–AC4 con T1 y T2 en verde. Si solo parte queda lista, se documenta como PARCIAL.

## 12. Plan por sprint
| Sprint | Horario | Trabajo |
|---|---|---|
| 1 | — | Ninguno |
| 2 | Sin ventana comprometida | Solo si W3 está listo y el PO lo confirma |

## 13. Preguntas abiertas
| ID | Pregunta | Supuesto PROPUESTO |
|---|---|---|
| PA-07 | ¿Cuál es la tasa máxima diaria de descalce aceptable? | No se fija una tasa; todo descalce se marca y tiene tipo (SUP-13) |

## Decisiones pendientes
- PA-07.

## Siguiente paso para el rol consumidor
AI Engineer A: no empezar sin confirmación del PO.
