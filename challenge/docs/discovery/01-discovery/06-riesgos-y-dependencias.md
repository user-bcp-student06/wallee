---
id: DISC-01-06
titulo: Riesgos y dependencias
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/epic/peru-wallet-mvp.sp.md (Dependencias y riesgos), challenge/user-stories/*.sp.md (Contexto)]
depende_de: []
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
Cuatro riesgos de la épica más riesgos de ejecución del hackathon. La mitigación principal es idempotencia, estados claros y mocks reproducibles.

## Riesgos de producto (fuente: épica)
| ID | Riesgo | Mitigación | HU |
|---|---|---|---|
| RSK-01 | Reintentos sin idempotencia generan duplicidad financiera y desvíos de conciliación | Clave de idempotencia y resultado original (RN-03, RN-13) | W4 |
| RSK-02 | Transiciones asíncronas deterioran la confianza si la confirmación no es clara | Un único estado terminal por intento (RN-06); PENDING no es terminal (RN-07) | W2 |
| RSK-03 | Reversos y disputas no están garantizados de forma uniforme (no hay cancelación unilateral de P2P) | Ruta de atención explícita y distinción entre falla técnica y transferencia ejecutada (RN-15) | W5 |
| RSK-04 | Dependencia de partners de adquirencia/gateway para QR | Mock de proveedor; QR como adaptador de entrada | W3 |

## Riesgos de ejecución (PROPUESTOS)
| ID | Riesgo | Mitigación |
|---|---|---|
| RSK-05 | W4 no queda en verde a las 12:30 | Cancelar el stretch (regla de corte) |
| RSK-06 | W5 no integra con el Crew a las 14:45 | Escalar al PO; reducir a AC1–AC3 con HITL manual |
| RSK-07 | Demo con intervención manual | Mocks por último dígito y fixtures reproducibles |

## Dependencias
| Dependencia | De | Para |
|---|---|---|
| Base (repo, mock, directorio sintético) | Arquitecto/a + AI Engineer A | W1, W2, W4, W5 |
| W2 | W1 (wallet ACTIVA) | W4 |
| W4 | W2 (motor de pago) | W5 |
| W3 | W2 y W4 (motor y idempotencia) | — |
| W6 | W4 (marca de reintento) | — |

## Decisiones pendientes
- Ninguna.

## Siguiente paso para el rol consumidor
QA & Security: convertir RSK-01 a RSK-03 en casos de prueba prioritarios.
