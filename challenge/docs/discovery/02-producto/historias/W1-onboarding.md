---
id: DISC-02-W1
titulo: W1 — Registro y activación del MVP de wallet
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/user-stories/user-onboarding-mvp-completion.sp.md]
depende_de: [DISC-04-01, DISC-04-02]
lo_consumen: [AI Engineer A, QA & Security, Arquitecto/a]
---

## Resumen
El usuario completa el onboarding con pasos guiados y la wallet pasa a ACTIVA. Se comprometen AC1–AC4; AC5 y AC6 (KPI) se difieren. Estado: PARCIAL.

## 1. Historia
Como usuario de smartphone que realiza transferencias diarias de bajo monto, quiero completar el onboarding de la wallet con un flujo guiado y señales claras de siguiente paso, para poder empezar a pagar sin abandonar el proceso.

## 2. Real y mock
| Real | Mock |
|---|---|
| Flujo de pasos, validaciones, estado de la wallet, eventos | KYC, OTP, biometría (SUP-14) |

## 3. AC (texto original)
| ID | Criterio |
|---|---|
| W1-AC1 | El flujo muestra la secuencia de pasos requeridos y el paso actual en todo momento |
| W1-AC2 | Si falta información obligatoria o hay datos inválidos, bloquea el avance y muestra un mensaje accionable |
| W1-AC3 | Al finalizar, la wallet pasa a activa y el usuario accede al punto de entrada de pagos de bajo monto |
| W1-AC4 | Se registran eventos de inicio, finalización de cada paso y cierre del flujo |
| W1-AC5 | El tiempo mediano de onboarding baja de 8 a 3 minutos dentro del trimestre posterior al lanzamiento |
| W1-AC6 | La salida analítica incluye conteos mensuales de nuevos usuarios activos y atribución de gasto para verificar MAU 1,000–2,000 y CAC PEN 10 |

## 4. Comprometidos vs diferidos
| AC | Hoy | Motivo |
|---|---|---|
| AC1–AC4 | Comprometidos | Forman el flujo e2e |
| AC5 | Diferido | KPI no medido hoy (RN-17); el evento de AC4 lo habilita |
| AC6 | Diferido | KPI no medido hoy (RN-17); sin datos de gasto de adquisición |

## 5. Reglas aplicables
RN-09, RN-10, RN-17. Ver [reglas](../../04-reglas-y-contratos/01-reglas-de-negocio.md).

## 6. Estados
Wallet: PENDIENTE_ONBOARDING → ACTIVA ([estados](../../04-reglas-y-contratos/02-estados-y-transiciones.md)).

## 7. Dependencias
Base (repo, mock, datos sintéticos). Ninguna HU previa.

## 8. Bordes y errores
- Campo obligatorio vacío o inválido (AC2).
- Abandono a mitad del flujo: se conserva el último paso completado (PROPUESTO).
- Intento de pagar con wallet no activa (RN-10).

## 9. QA debe probar
| Caso | Qué prueba |
|---|---|
| W1-AC1-T2 | Se muestran los pasos y el paso actual |
| W1-AC2-T2 | Datos inválidos bloquean con mensaje accionable |
| W1-AC3-T2 | Wallet ACTIVA y acceso a pagos al finalizar |
| W1-AC3-T3 | Wallet no activa no accede al pago |
| W1-AC4-T2 | Se emiten `onboarding_started`, `onboarding_step_completed`, `onboarding_completed` |

## 10. Evidencia esperada
Salida de tests, captura del flujo y registro de eventos, referenciados en `evidence.md`.

## 11. Definición de listo
AC1–AC4 con T1 y T2 en verde; eventos visibles; PR enlazado en la [matriz](../../05-trazabilidad/01-matriz-trazabilidad.md).

## 12. Plan por sprint
| Sprint | Horario | Trabajo |
|---|---|---|
| 1 | 10:45–11:15 | W1-AC1-T1, W1-AC2-T1, W1-AC3-T1, W1-AC4-T1 y sus T2 |
| 2 | — | Ninguno; corte de 12:30 verifica W1 en verde |

## 13. Preguntas abiertas
| ID | Pregunta | Supuesto PROPUESTO |
|---|---|---|
| PA-01 | ¿Qué frontera de eventos define la duración del onboarding? | Inicio = `onboarding_started`; fin = `onboarding_completed` con wallet ACTIVA (SUP-09) |

## Decisiones pendientes
- PA-01.

## Siguiente paso para el rol consumidor
AI Engineer A: construir W1-AC1-T1 a W1-AC4-T1 entre 10:45 y 11:15.
