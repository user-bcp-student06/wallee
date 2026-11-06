---
id: DISC-00-02
titulo: Glosario
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/epic/peru-wallet-mvp.sp.md, challenge/user-stories/*.sp.md]
depende_de: []
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
Términos del dominio y del proceso usados en todo el discovery. Los IDs y convenciones se definen al final.

## Términos
| Término | Significado en este proyecto |
|---|---|
| HU | Historia de usuario. Seis: W1..W6 |
| AC | Criterio de aceptación de una HU (`W4-AC2`) |
| Idempotencia | Repetir una solicitud con la misma clave devuelve el resultado original y no crea una nueva transacción financiera |
| Clave de idempotencia | Identificador único por pagador, monto, destino y ventana de intento |
| HITL | Human-in-the-loop: un humano decide en casos críticos o excepciones |
| Guardrail | Restricción de las acciones que puede ejecutar un agente |
| KYC | Verificación de identidad del usuario. MOCK en el MVP |
| OTP / biometría | Verificación de segundo factor. MOCK en el MVP |
| CCE | Cámara de compensación electrónica: riel de pagos externos. MOCK |
| QR | Código para pagar a un comercio. Es un adaptador de entrada (`channel`: QR) |
| Alias | Identificador alterno de destino, resuelto en un directorio sintético |
| Ledger | Registro de asientos de la wallet. Local y REAL; el corporativo es MOCK |
| Conciliación | Comparación diaria de intenciones de pago, resultados del proveedor y asientos del ledger |
| Callback | Notificación asíncrona del proveedor con el estado de una transacción. Puede llegar duplicada |
| Estado terminal | Resultado final para el usuario: exitoso, fallido o expirado |
| Mock | Simulación controlable y reproducible de un sistema externo |
| Fixture | Datos de prueba sintéticos fijos |
| Evento de activación | Evento emitido por un pago exitoso; base del cálculo de MAU |

## Convenciones de IDs
| Tipo | Formato | Ejemplo |
|---|---|---|
| Historia | `W1`..`W6` | W4 |
| Criterio | `Wx-ACn` | W4-AC2 |
| Task | `Wx-ACn-Tm` (T1 construir, T2 probar, T3 caso de borde) | W4-AC2-T2 |
| Regla | `RN-nn` | RN-02 |
| Supuesto | `SUP-nn` | SUP-01 |
| Riesgo | `RSK-nn` | RSK-01 |
| Decisión | `DEC-nn` | DEC-01 |
| Pregunta abierta | `PA-nn` | PA-04 |
| KPI de negocio | `KPI-nn` | KPI-01 |

## Decisiones pendientes
- Ninguna.

## Siguiente paso para el rol consumidor
Usar estos IDs sin variaciones en código, tests, commits y PR.
