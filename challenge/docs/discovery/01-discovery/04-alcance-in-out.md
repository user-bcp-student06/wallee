---
id: DISC-01-04
titulo: Alcance — dentro y fuera
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/epic/peru-wallet-mvp.sp.md (Alcance), base de hechos del prompt]
depende_de: [DISC-01-03]
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
El MVP cubre onboarding, pago de bajo monto, estado y excepciones. El hackathon compromete W1, W2, W4 y W5; W3 y W6 son stretch.

## Dentro (épica)
- Onboarding de wallet para el segmento MVP en Perú.
- Flujos de pago de bajo monto y cobro a comercios con QR.
- Visibilidad de confirmación y estado de pago.
- Instrumentación base de funnel, onboarding y activación.

## Fuera (épica)
- Despliegue multipaís amplio.
- Programas de lealtad o mecánicas de crecimiento no esenciales.
- Paridad funcional con todos los proveedores/bancos desde el día uno.
- APIs de pago abiertas para terceros.

## Alcance del hackathon
| Elemento | Dentro | Fuera |
|---|---|---|
| HU comprometidas | W1, W2, W4, W5 | |
| HU stretch | W3, luego W6 | |
| AC de KPI | Solo el evento | Medición de KPI |
| Integraciones | Mocks controlables | Proveedores reales, core, CCE |
| Datos | Sintéticos | Datos reales, secretos |

Detalle: [01-compromiso-y-prioridad](../03-alcance-hackathon/01-compromiso-y-prioridad.md) y [04-real-vs-mock](../03-alcance-hackathon/04-real-vs-mock.md).

## Decisiones pendientes
- PA-10: confirmar el compromiso de HUs en el G1.

## Siguiente paso para el rol consumidor
Todos: ante un pedido fuera de este alcance, consultar al PO (HITL).
