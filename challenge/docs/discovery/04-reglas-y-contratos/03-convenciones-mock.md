---
id: DISC-04-03
titulo: Convenciones del mock
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [base de hechos del prompt (Frontera real/mock, Supuestos)]
depende_de: [DISC-04-02]
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
El mock debe ser controlable y reproducible: el último dígito del celular decide el escenario. Todos los datos son sintéticos.

## Escenarios por último dígito del celular (RN-08)
| Último dígito | Estado del proveedor | Terminal |
|---|---|---|
| 0 | DECLINED | fallido |
| 1 | TIMEOUT | expirado |
| 2 | PENDING | (no terminal) |
| 3–9 | APPROVED | exitoso |

## Callback duplicado
- Se dispara reenviando el mismo callback con el mismo identificador de transacción.
- El mecanismo exacto lo decide el Arquitecto; el comportamiento esperado está en RN-13.

## Datos sintéticos
| Dato | Convención (PROPUESTA) |
|---|---|
| Celulares | 9 dígitos, empiezan con 9, números inventados |
| Alias | Lista fija en el directorio sintético |
| Saldo inicial | Fijo, definido en fixtures (SUP-15) |
| Montos de prueba | Incluir S/ 500 y un valor mayor (RN-01) |

## Qué se simula
Identidad/KYC/OTP/biometría · pagos externos/CCE/gateway/QR/callbacks · core/settlement/reversos monetarios/ledger corporativo · estados APPROVED, DECLINED, PENDING, TIMEOUT y callback duplicado.

## Reglas
- No debe haber datos reales, secretos ni credenciales en el repositorio.
- Una demo no debe requerir intervención manual: cada escenario se dispara con datos de entrada.

## Decisiones pendientes
- Ninguna.

## Siguiente paso para el rol consumidor
AI Engineer A: construir el mock con estas convenciones en la Base (10:15–10:45).
