---
id: DISC-02-03
titulo: Mapa de historias
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/user-stories/*.sp.md, base de hechos del prompt (Compromiso propuesto)]
depende_de: [DISC-04-01, DISC-04-02]
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
17 de 28 AC comprometidos en cuatro HU (W1, W2, W4, W5). W3 y W6 son stretch. Owners y AC comprometidos son PROPUESTOS.

## Matriz
| HU | Nombre | W | Persona | Valor | AC totales | AC comprometidos | Prioridad | Sprint | Hora límite | Owner | Depende de | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| user-onboarding-mvp-completion | Registro y activación | W1 | Usuario que transfiere a diario | Empezar a pagar sin abandonar | 6 | 4 (AC1–AC4) | 1 | S1 | 11:15 | AI Engineer A | Base | PARCIAL |
| payer-low-value-payment-confirmation | Confirmación de pagos de bajo monto | W2 | Pagador | Confiar en si el pago se hizo | 6 | 5 (AC1–AC4, AC6 parcial) | 2 | S1 | 11:45 | AI Engineer A | W1 | PARCIAL |
| payment-idempotency-protection | Idempotencia en pagos | W4 | Analista de operaciones | Evitar duplicidad financiera | 4 | 4 (AC4 parcial) | 3 | S1 | 12:30 | AI Engineer A | W2 | PARCIAL |
| payment-failure-reversal-handling | Fallas de pago y reversos | W5 | Especialista de soporte | Guía consistente ante fallas | 4 | 4 | 4 | S2 | 14:45 | AI Engineer B | W2, W4 | Completo |
| merchant-qr-payment-status-visibility | Visibilidad de estado QR | W3 | Pequeño comercio | Decidir cuándo entregar | 4 | 0 | 5 (stretch) | S2 | No comprometida | AI Engineer A | W2, W4 | Diferido |
| operations-transaction-reconciliation | Conciliación operativa | W6 | Analista de operaciones | Detectar descalces | 4 | 0 | 6 (stretch) | S2 | No comprometida | AI Engineer A | W4 | Diferido |

Una HU con algún AC diferido o parcial se documenta como PARCIAL (W1, W2, W4). W5 es completa; W3 y W6 están diferidas.

## Orden de construcción
Base → W1 → W2 → W4 → W5. Stretch: W3 y luego W6.

## Decisiones pendientes
- PA-10: confirmar compromiso y AC comprometidos.

## Siguiente paso para el rol consumidor
Cada owner: abrir su HU y su handoff ([06-handoff-por-rol](../06-handoff-por-rol/)).
