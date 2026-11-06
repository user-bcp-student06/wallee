---
id: DISC-01-03
titulo: Objetivos y métricas
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/epic/peru-wallet-mvp.sp.md (Objetivos, Métricas de éxito), challenge/user-stories/*.sp.md]
depende_de: []
lo_consumen: [Arquitecto/a, AI Engineer A, QA & Security, Presenter/Timekeeper]
---

## Resumen
La épica define cuatro KPI de negocio a un trimestre. En el hackathon NO se miden: solo se instrumenta el evento (RN-17).

## KPI de negocio (fuente: épica)
| ID | KPI | Línea base | Meta | Medido hoy | HU / AC |
|---|---|---|---|---|---|
| KPI-01 | Caída en checkout | 30% | 8% | No | W2-AC5 |
| KPI-02 | Tiempo de onboarding | 8 min | 3 min | No | W1-AC5 |
| KPI-03 | MAU meses 1–3 | — | 1,000–2,000 | No | W1-AC6, W2-AC6 |
| KPI-04 | CAC meses 1–3 | — | PEN 10 por usuario nuevo | No | W1-AC6 |

MAU y CAC son umbrales definidos por el Product Owner.

## Qué sí se instrumenta hoy
| Evento (PROPUESTO) | Origen |
|---|---|
| `onboarding_started`, `onboarding_step_completed`, `onboarding_completed` | W1-AC4 |
| `payment_succeeded` (evento de activación) | W2-AC6 (PARCIAL) |

## Objetivos del hackathon
Ver criterios de éxito en [01-reto-hackathon](../00-contexto/01-reto-hackathon.md): e2e local, tests de comportamiento e idempotencia, trazabilidad, defensa.

## Decisiones pendientes
- PA-01: definición oficial de inicio y fin del onboarding (supuesto en [02-decisiones](../05-trazabilidad/02-decisiones.md)).

## Siguiente paso para el rol consumidor
Presenter: presentar los KPI como metas de negocio, no como resultados medidos.
