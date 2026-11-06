---
id: DISC-02-W4
titulo: W4 — Idempotencia en pagos
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/user-stories/payment-idempotency-protection.sp.md]
depende_de: [DISC-02-W2, DISC-04-01, DISC-04-03]
lo_consumen: [AI Engineer A, QA & Security, Arquitecto/a]
---

## Resumen
Una solicitud repetida devuelve el resultado original y no duplica dinero. Se comprometen AC1–AC4; AC4 es PARCIAL (marca de reintento en el ledger; el reporte va en W6). Estado: PARCIAL.

## 1. Historia
Como analista de operaciones y confiabilidad, quiero que los intentos de pago duplicados se manejen con comportamiento idempotente, para evitar duplicidad financiera y desvíos en conciliación cuando hay reintentos.

## 2. Real y mock
| Real | Mock |
|---|---|
| Clave de idempotencia, ventana de 24 h, registro de duplicados, ledger local | Callback duplicado del proveedor |

## 3. AC (texto original)
| ID | Criterio |
|---|---|
| W4-AC1 | Cada intento se envía con una clave de idempotencia única por pagador, monto, destino y ventana de intento |
| W4-AC2 | Una solicitud repetida con la misma clave devuelve el resultado original y no crea una nueva transacción financiera |
| W4-AC3 | Los duplicados se registran con identificadores de solicitud y de correlación para auditoría |
| W4-AC4 | Las salidas de conciliación distinguen intentos originales de reintentos duplicados |

## 4. Comprometidos vs diferidos
| AC | Hoy | Motivo |
|---|---|---|
| AC1–AC3 | Comprometidos | Núcleo de la HU |
| AC4 | PARCIAL | Se marca original/reintento en el registro; la salida de conciliación pertenece a W6 (stretch) |

## 5. Reglas aplicables
RN-02, RN-03, RN-13.

## 6. Estados
Un duplicado no crea estado nuevo; devuelve el terminal original. Un callback duplicado no altera un estado terminal.

## 7. Dependencias
W2 (motor de pago). Componentes: ledger local, registro de auditoría.

## 8. Bordes y errores
| Caso | Esperado |
|---|---|
| Misma clave dentro de 24 h | Resultado original, sin nueva transacción |
| Misma clave pasadas 24 h | Nueva ventana de intento (PROPUESTO) |
| Mismo pagador y destino, distinto monto | Clave distinta (RN-03) |
| Callback duplicado | Sin cambio de estado; registrado |
| Dos solicitudes simultáneas con la misma clave | Una sola transacción |

## 9. QA debe probar
| Caso | Qué prueba |
|---|---|
| W4-AC1-T2 | La clave depende de pagador, monto, destino y ventana |
| W4-AC2-T2 | Repetición devuelve el original y el ledger no suma un asiento |
| W4-AC2-T3 | Callback duplicado y solicitudes simultáneas |
| W4-AC3-T2 | Duplicado registrado con identificador de solicitud y de correlación |
| W4-AC4-T2 | Registro distingue original de reintento |

## 10. Evidencia esperada
Tests de idempotencia, conteo del ledger antes y después, y registros de auditoría, en `evidence.md`.

## 11. Definición de listo
AC1–AC3 y AC4 parcial con T1 y T2 en verde a las 12:30; si no, se cancela el stretch.

## 12. Plan por sprint
| Sprint | Horario | Trabajo |
|---|---|---|
| 1 | 11:45–12:30 | W4-AC1-T1 a W4-AC4-T1 y sus T2/T3 |
| 2 | 14:45–15:05 | Integración con W5 |

## 13. Preguntas abiertas
| ID | Pregunta | Supuesto PROPUESTO |
|---|---|---|
| PA-04 | ¿Cuál es la ventana de retención de claves por canal? | 24 h para ambos canales (SUP-02) |

## Decisiones pendientes
- PA-04.

## Siguiente paso para el rol consumidor
AI Engineer A: construir W4 entre 11:45 y 12:30. QA & Security: preparar W4-AC2-T3 desde la Base.
