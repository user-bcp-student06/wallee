---
id: DISC-02-W2
titulo: W2 — Confirmación de pagos de bajo monto (pago a contacto)
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/user-stories/payer-low-value-payment-confirmation.sp.md]
depende_de: [DISC-02-W1, DISC-04-01, DISC-04-02, DISC-04-03]
lo_consumen: [AI Engineer A, QA & Security, Arquitecto/a]
---

## Resumen
El pagador paga a un celular o alias y recibe un único resultado terminal. Se comprometen AC1–AC4 y AC6 parcial; AC5 (KPI) se difiere. Estado: PARCIAL.

## 1. Historia
Como pagador, quiero completar una transferencia de bajo monto y recibir una confirmación definitiva del resultado, para confiar en si el pago se realizó o no.

## 2. Real y mock
| Real | Mock |
|---|---|
| Validaciones, motor de pago, estados, historial, ledger local, evento de activación | Proveedor de pagos y callbacks (RN-08) |

## 3. AC (texto original)
| ID | Criterio |
|---|---|
| W2-AC1 | Antes de la confirmación final, la pantalla muestra la identidad del destino y el monto |
| W2-AC2 | El pagador recibe un único resultado terminal por intento: exitoso, fallido o expirado |
| W2-AC3 | Si es exitoso, se muestra una referencia de transacción y queda persistida en el historial |
| W2-AC4 | Si falla o expira, hay una siguiente acción clara (reintentar o volver) sin cobros duplicados |
| W2-AC5 | La caída en checkout baja de 30% a 8% dentro del trimestre posterior al lanzamiento |
| W2-AC6 | Las transacciones exitosas emiten el evento de activación usado en el cálculo de MAU 1,000–2,000 |

## 4. Comprometidos vs diferidos
| AC | Hoy | Motivo |
|---|---|---|
| AC1–AC4 | Comprometidos | Forman el flujo e2e |
| AC6 | PARCIAL | Se emite `payment_succeeded`; el cálculo de MAU no se mide (RN-17) |
| AC5 | Diferido | KPI no medido hoy (RN-17) |

## 5. Reglas aplicables
RN-01, RN-04, RN-05, RN-06, RN-07, RN-08, RN-10, RN-11, RN-12, RN-17, RN-18.

## 6. Estados
Transacción: CREADA → PENDING → APPROVED/DECLINED/TIMEOUT; terminal: exitoso, fallido, expirado.

## 7. Dependencias
W1 (wallet ACTIVA, RN-10). Componentes: mock de proveedor, directorio sintético, saldo.

## 8. Bordes y errores
| Caso | Esperado |
|---|---|
| Monto = S/ 500 | Permitido |
| Monto > S/ 500 | Bloqueado antes de enviar (RN-01) |
| Celular que no empieza con 9 o sin 9 dígitos | Rechazado (RN-04) |
| Saldo menor al monto | No se ejecuta (RN-18) |
| Último dígito 2 (PENDING) | No muestra terminal hasta el callback (RN-07) |

## 9. QA debe probar
| Caso | Qué prueba |
|---|---|
| W2-AC1-T2 | Se muestran destino y monto antes de confirmar |
| W2-AC2-T2 | Un único terminal por intento en los escenarios 0, 1 y resto |
| W2-AC3-T2 | Referencia mostrada y persistida en historial |
| W2-AC4-T2 | Fallido y expirado ofrecen reintentar o volver sin cobro duplicado |
| W2-AC4-T3 | Monto sobre S/ 500, saldo insuficiente y celular inválido |
| W2-AC6-T2 | Pago exitoso emite `payment_succeeded` |

## 10. Evidencia esperada
Tests de comportamiento, historial con referencia y eventos, referenciados en `evidence.md`.

## 11. Definición de listo
AC1–AC4 y AC6 parcial con T1 y T2 en verde; los tres escenarios mock demostrables sin intervención manual.

## 12. Plan por sprint
| Sprint | Horario | Trabajo |
|---|---|---|
| 1 | 11:15–11:45 | W2-AC1-T1 a W2-AC4-T1, W2-AC6-T1 y sus T2/T3 |
| 2 | 14:45–15:05 | Integración con W4 y W5 |

## 13. Preguntas abiertas
| ID | Pregunta | Supuesto PROPUESTO |
|---|---|---|
| PA-02 | ¿Qué regla de monto bajo se configura por proveedor/canal? | S/ 500 por transacción (SUP-01) |
| PA-08 | (nueva) ¿Hay validación de saldo? | No se ejecuta si saldo < monto (SUP-15) |

Pendiente adicional de la fuente: las etiquetas finales de estados terminales están por definir con producto (supuesto: exitoso, fallido, expirado).

## Decisiones pendientes
- PA-02, PA-08.

## Siguiente paso para el rol consumidor
AI Engineer A: construir W2 entre 11:15 y 11:45, solo con wallet ACTIVA.
