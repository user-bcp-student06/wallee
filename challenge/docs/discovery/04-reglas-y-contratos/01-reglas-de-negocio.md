---
id: DISC-04-01
titulo: Reglas de negocio
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/user-stories/*.sp.md (AC y Contexto), base de hechos del prompt]
depende_de: [DISC-01-05]
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security]
---

## Resumen
Reglas RN-01 a RN-18 que gobiernan el MVP. Las cifras (S/ 500, 24 h) son PROPUESTAS hasta que un humano las confirme.

## Reglas
| ID | Regla | Origen | HU | Estado |
|---|---|---|---|---|
| RN-01 | El monto de una transacción no debe superar S/ 500 | SUP-01 | W2 | PROPUESTO |
| RN-02 | La ventana de idempotencia es de 24 h | SUP-02 | W4 | PROPUESTO |
| RN-03 | La clave de idempotencia es única por pagador, monto, destino y ventana de intento | W4-AC1 | W4 | Fuente |
| RN-04 | El destino debe ser un celular (9 dígitos, empieza con 9) o un alias del directorio sintético | SUP-05 | W2 | PROPUESTO |
| RN-05 | Mapeo del proveedor mock al estado terminal: APPROVED→exitoso, DECLINED→fallido, TIMEOUT→expirado | SUP-03 | W2 | PROPUESTO |
| RN-06 | Cada intento debe tener un único resultado terminal | W2-AC2 | W2 | Fuente |
| RN-07 | PENDING no es terminal y no debe mostrarse como resultado final | SUP-03 | W2 | PROPUESTO |
| RN-08 | El último dígito del celular dispara el escenario mock: 0→DECLINED, 1→TIMEOUT, 2→PENDING, resto→APPROVED | SUP-06 | W2, W4, W5 | PROPUESTO |
| RN-09 | El onboarding no debe avanzar con datos obligatorios faltantes o inválidos; debe mostrar un mensaje accionable | W1-AC2 | W1 | Fuente |
| RN-10 | Solo una wallet ACTIVA puede acceder al pago de bajo monto | W1-AC3 | W1, W2 | Fuente |
| RN-11 | Un pago exitoso debe mostrar una referencia de transacción y persistirla en el historial | W2-AC3 | W2 | Fuente |
| RN-12 | Un pago fallido o expirado debe ofrecer una siguiente acción (reintentar o volver) sin crear cobros duplicados | W2-AC4 | W2 | Fuente |
| RN-13 | Una solicitud repetida con la misma clave debe devolver el resultado original y no crear transacción ni asiento nuevos | W4-AC2 | W4 | Fuente |
| RN-14 | Un pago fallido o expirado debe guardar un código de motivo legible por máquina | W5-AC1 | W5 | Fuente |
| RN-15 | La ayuda debe diferenciar una falla técnica de una transferencia ya ejecutada | W5-AC3 | W5 | Fuente |
| RN-16 | Cada acción de soporte debe registrarse con referencia de transacción y estado de resolución | W5-AC4 | W5 | Fuente |
| RN-17 | Los KPI de negocio no se miden hoy; solo se emite el evento | SUP-04 | W1, W2 | PROPUESTO |
| RN-18 | Un pago no debe ejecutarse si el saldo es menor al monto | SUP-15 | W2 | PROPUESTO |

## Validaciones visibles antes del envío
- Se muestra la identidad del destino y el monto (W2-AC1).
- Se valida el monto máximo antes de enviar (RN-01), porque el límite por proveedor puede ser menor al regulatorio.

## Decisiones pendientes
- PA-02, PA-04, PA-08 (ver [02-decisiones](../05-trazabilidad/02-decisiones.md)).

## Siguiente paso para el rol consumidor
AI Engineer A: implementar RN-01, RN-03, RN-13 y RN-18 como validaciones del dominio, con un test por regla.
