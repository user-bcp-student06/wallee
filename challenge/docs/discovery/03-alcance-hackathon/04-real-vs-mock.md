---
id: DISC-03-04
titulo: Real vs mock
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [base de hechos del prompt (Frontera real/mock)]
depende_de: [DISC-04-03]
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
Se construye el dominio y se simula todo lo externo, de forma controlable y reproducible. En el pitch hay que defender esta frontera.

## Frontera
| Componente | REAL (se construye) | MOCK (se simula) | HU |
|---|---|---|---|
| Dominio Wallet y estados | Sí | | W1, W2 |
| Idempotencia de pagos y callbacks | Sí | | W4 |
| Ledger local | Sí | | W2, W4 |
| Conciliación con fixtures | Sí (stretch) | | W6 |
| Datos sintéticos | Sí | | Todas |
| Identidad / KYC / OTP / biometría | | Sí | W1 |
| Pagos externos / CCE / gateway / QR / callbacks | | Sí | W2, W3 |
| Core / settlement / reversos monetarios / ledger corporativo | | Sí | W5, W6 |
| Estados APPROVED, DECLINED, PENDING, TIMEOUT y callback duplicado | | Sí | W2, W4 |

## Reglas
- Un mock no debe presentarse como integración real en la demo.
- Cada mock tiene una convención de disparo documentada ([convenciones](../04-reglas-y-contratos/03-convenciones-mock.md)).
- La defensa incluye qué se simuló, por qué y qué queda pendiente.

## Decisiones pendientes
- Ninguna.

## Siguiente paso para el rol consumidor
Presenter: incluir esta tabla en la defensa de la arquitectura.
