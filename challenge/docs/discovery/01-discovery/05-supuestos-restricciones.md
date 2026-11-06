---
id: DISC-01-05
titulo: Supuestos y restricciones
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/epic/peru-wallet-mvp.sp.md (Supuestos y restricciones), challenge/user-stories/*.sp.md (Supuestos), base de hechos del prompt]
depende_de: []
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security]
---

## Resumen
Restricciones de la épica y supuestos PROPUESTOS que cierran las preguntas abiertas. Ningún supuesto está confirmado por un humano.

## Restricciones (fuente: épica)
| ID | Restricción |
|---|---|
| RES-01 | El ecosistema es multirriel; no asumir un único riel de procesamiento |
| RES-02 | Las integraciones reales son contractuales; el alta de proveedores no es inmediata |
| RES-03 | Los límites por proveedor pueden estar bajo el máximo regulatorio; la UX debe contemplarlo |
| RES-04 | Se espera pagos inmediatos con alias 24x7x365 |

## Supuestos PROPUESTOS — por confirmar
| ID | Supuesto | Cierra |
|---|---|---|
| SUP-01 | Monto máximo de bajo monto: S/ 500 por transacción | PA-02 |
| SUP-02 | Ventana de idempotencia: 24 h | PA-04 |
| SUP-03 | Mapeo mock → terminal: APPROVED→exitoso, DECLINED→fallido, TIMEOUT→expirado; PENDING no es terminal | W2-AC2 |
| SUP-04 | Los AC de KPI de negocio no se miden hoy; solo se instrumenta el evento | W1-AC5/AC6, W2-AC5 |
| SUP-05 | Destino: celular (9 dígitos, empieza con 9) o alias, contra un directorio sintético | W2-AC1 |
| SUP-06 | Mock por último dígito del celular: 0→DECLINED, 1→TIMEOUT, 2→PENDING, resto→APPROVED | convención mock |
| SUP-07 | `channel` (CONTACT \| QR) es un campo del contrato; un solo motor de pago | W3 |
| SUP-08 | Stack: Node.js, React, CrewAI (Python), SQLite, datos sintéticos (por confirmar en G1) | PA-09 |
| SUP-09 | Onboarding: inicio = `onboarding_started`; fin = `onboarding_completed` con wallet ACTIVA | PA-01 |
| SUP-10 | Conjunto mínimo de estados del comercio = estados del proveedor mock (APPROVED, DECLINED, PENDING, TIMEOUT); consulta vía la misma app web | PA-03 |
| SUP-11 | Disputas en MVP: solo se clasifica la ruta (reintento, investigación, disputa) y se registra; la resolución de disputas se difiere | PA-05 |
| SUP-12 | Sin SLA ni niveles de escalamiento formales hoy; el escalamiento es HITL hacia un humano | PA-06 |
| SUP-13 | Conciliación sobre fixtures; todo descalce se marca y ninguno queda sin tipo; no se fija una tasa objetivo | PA-07 |
| SUP-14 | KYC, OTP y biometría simulados | W1 |
| SUP-15 | Saldo inicial sintético; un pago no se ejecuta si el saldo es menor al monto | PA-08 |

## Decisiones pendientes
- PA-08, PA-09, PA-10 (ver [02-decisiones](../05-trazabilidad/02-decisiones.md)).

## Siguiente paso para el rol consumidor
Arquitecto/a: confirmar o ajustar SUP-08 en el G1 (10:00).
