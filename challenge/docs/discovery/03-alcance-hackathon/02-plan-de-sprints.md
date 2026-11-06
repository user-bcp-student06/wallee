---
id: DISC-03-02
titulo: Plan de sprints
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [base de hechos del prompt (Cronograma, Compromiso propuesto)]
depende_de: [DISC-03-01]
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
Sprint 1 (10:15–12:30) construye Base, W1, W2 y W4. Sprint 2 (13:45–15:15) construye W5 con el Crew, integra y documenta. Owners PROPUESTOS.

## Hitos
| Hora | Hito |
|---|---|
| 10:00 | Scope check G1 |
| 10:15–10:45 | Base |
| 11:15 | W1 listo |
| 11:45 | W2 listo |
| 12:30 | W4 listo y corte: W1, W2 y W4 en verde |
| 13:30 | Scope check G2 |
| 14:45 | W5 integrado (corte) |
| 15:05 | Integración lista |
| 15:15 | Docs listas; inicio de Freeze |
| 15:15–15:45 | Freeze (GitHub, README, URL) |
| 16:00 | Demo Arena |

## Sprint 1
| Task | Descripción | Owner | Hora límite |
|---|---|---|---|
| BASE-T1 | Repo ejecutable, mock con convención, directorio sintético y datos (ver [mock](../04-reglas-y-contratos/03-convenciones-mock.md)) | Arquitecto/a + AI Engineer A | 10:45 |
| W1-AC1-T1…W1-AC4-T1 | Onboarding guiado, validaciones, wallet ACTIVA, eventos | AI Engineer A | 11:15 |
| W1-AC1-T2…W1-AC4-T2 | Pruebas de W1 | QA & Security | 11:15 |
| W2-AC1-T1…W2-AC4-T1, W2-AC6-T1 | Pago a contacto, estados terminales, historial, evento | AI Engineer A | 11:45 |
| W2-AC1-T2…W2-AC6-T2 | Pruebas de W2, incluye bordes (T3) | QA & Security | 11:45 |
| W4-AC1-T1…W4-AC4-T1 | Idempotencia, registro de duplicados, marca de reintento | AI Engineer A | 12:30 |
| W4-AC1-T2…W4-AC4-T2 | Pruebas de W4, incluye callback duplicado (T3) | QA & Security | 12:30 |

## Sprint 2
| Task | Descripción | Owner | Hora límite |
|---|---|---|---|
| W5-AC1-T1…W5-AC4-T1 | Clasificación, vista de soporte, ayuda, registro; agente con HITL | AI Engineer B | 14:45 |
| W5-AC1-T2…W5-AC4-T2 | Pruebas de W5 y guardrails del agente | QA & Security | 14:45 |
| INT-T1 | Integración del flujo completo | Todos | 15:05 |
| DOC-T1 | README, arquitectura y `evidence.md` | Presenter + Arquitecto/a | 15:15 |
| STRETCH-T1 | W3 (y luego W6) solo si el corte de 12:30 está en verde | AI Engineer A | 14:45 |

## Decisiones pendientes
- PA-10: confirmar owners y horarios en el G1.

## Siguiente paso para el rol consumidor
Cada owner: abrir su [handoff](../06-handoff-por-rol/) y confirmar sus horas límite.
