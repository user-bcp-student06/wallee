---
id: DISC-02-W3
titulo: W3 — Visibilidad del estado de pagos QR para comercios (stretch)
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/user-stories/merchant-qr-payment-status-visibility.sp.md]
depende_de: [DISC-02-W2, DISC-02-W4]
lo_consumen: [AI Engineer A, QA & Security, Arquitecto/a]
---

## Resumen
El comercio ve el estado confiable de cada pago QR. Es stretch: 0 de 4 AC comprometidos. Se activa solo si W1, W2 y W4 están en verde a las 12:30. Estado: DIFERIDO.

## 1. Historia
Como pequeño comercio que cobra con QR, quiero ver el estado confiable de cada transacción de cliente, para decidir correctamente cuándo entregar el producto o servicio.

## 2. Real y mock
| Real | Mock |
|---|---|
| Vista de estados, filtros, uso del mismo motor con `channel = QR` | Lectura de QR, gateway y callbacks |

## 3. AC (texto original)
| ID | Criterio |
|---|---|
| W3-AC1 | El comercio ve cada intento de pago QR con una referencia única de transacción |
| W3-AC2 | Cada intento muestra un estado actual del conjunto habilitado para el MVP |
| W3-AC3 | La vista se actualiza cuando callbacks/eventos del proveedor cambian el estado |
| W3-AC4 | El comercio filtra el historial por fecha y referencia de transacción |

## 4. Comprometidos vs diferidos
| AC | Hoy | Motivo |
|---|---|---|
| AC1–AC4 | Diferidos (stretch) | Prioridad 5; solo si el corte de 12:30 está en verde |

## 5. Reglas aplicables
RN-05, RN-06, RN-07, RN-08, RN-13. Un solo motor de pago (SUP-07).

## 6. Estados
APPROVED, DECLINED, PENDING, TIMEOUT (SUP-10).

## 7. Dependencias
W2 (motor de pago) y W4 (idempotencia). El QR es un adaptador de entrada.

## 8. Bordes y errores
- Callback que cambia el estado de PENDING a terminal (AC3).
- Callback duplicado: no cambia el estado.
- Filtro sin resultados.

## 9. QA debe probar (si se activa)
| Caso | Qué prueba |
|---|---|
| W3-AC1-T2 | Referencia única por intento |
| W3-AC2-T2 | Estado dentro del conjunto habilitado |
| W3-AC3-T2 | Actualización tras callback |
| W3-AC4-T2 | Filtro por fecha y referencia |

## 10. Evidencia esperada
Tests y captura de la vista, solo si se activa.

## 11. Definición de listo
AC1–AC4 con T1 y T2 en verde. Si solo parte queda listo, se documenta como PARCIAL.

## 12. Plan por sprint
| Sprint | Horario | Trabajo |
|---|---|---|
| 1 | — | Ninguno |
| 2 | 13:45–14:45 (si se activa) | AI Engineer A en paralelo a W5 |

## 13. Preguntas abiertas
| ID | Pregunta | Supuesto PROPUESTO |
|---|---|---|
| PA-03 | ¿Cuál es el conjunto mínimo de estados del comercio y el canal de consulta (app, web o ambos)? | Los cuatro estados del mock; consulta en la misma app web (SUP-10) |

## Decisiones pendientes
- PA-03.

## Siguiente paso para el rol consumidor
AI Engineer A: no empezar hasta el corte de 12:30 y la confirmación del PO.
