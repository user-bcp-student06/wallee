---
id: DISC-05-02
titulo: Decisiones y preguntas abiertas
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/user-stories/*.sp.md (Preguntas abiertas y Supuestos), base de hechos del prompt]
depende_de: [DISC-01-05]
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
Todas las preguntas abiertas de las historias tienen un supuesto PROPUESTO. Ningún humano confirmó aún ninguna decisión; esto se hace en el G1 (10:00).

## Preguntas abiertas
| ID | Pregunta | HU | Supuesto PROPUESTO — por confirmar | Impacto si cambia | Estado |
|---|---|---|---|---|---|
| PA-01 | ¿Qué frontera de eventos define la duración del onboarding? | W1 | Inicio `onboarding_started`; fin `onboarding_completed` con wallet ACTIVA (SUP-09) | Evento W1-AC4 | Abierta |
| PA-02 | ¿Qué regla de monto bajo se configura por proveedor/canal? | W2 | S/ 500 por transacción (SUP-01) | RN-01, tests de borde | Abierta |
| PA-03 | ¿Conjunto mínimo de estados del comercio y canal de consulta? | W3 | Cuatro estados del mock; misma app web (SUP-10) | Solo stretch | Abierta |
| PA-04 | ¿Ventana de retención de claves de idempotencia por canal? | W4 | 24 h para ambos canales (SUP-02) | RN-02, W4-AC2 | Abierta |
| PA-05 | ¿Categorías de disputa en MVP y cuáles se difieren? | W5 | Se clasifica y registra la ruta; resolución diferida (SUP-11) | W5-AC2, W5-AC3 | Abierta |
| PA-06 | Niveles de escalamiento y SLA de soporte | W5 | Sin SLA formal; escalamiento HITL (SUP-12) | W5-AC4 | Abierta |
| PA-07 | ¿Tasa máxima diaria de descalce aceptable? | W6 | Sin tasa; todo descalce se marca (SUP-13) | Solo stretch | Abierta |
| PA-08 | (nueva) ¿Hay validación de saldo antes de pagar? | W2 | No se ejecuta si saldo < monto (SUP-15) | RN-18 | Abierta |
| PA-09 | Confirmar el stack propuesto | Base | Node.js, React, CrewAI, SQLite (SUP-08) | Base | Abierta — G1 |
| PA-10 | Confirmar compromiso de HU, AC comprometidos y owners | Todas | W1, W2, W4, W5; 17 de 28 AC (ver mapa) | Alcance y plan | Abierta — G1 |

Las fuentes también dejan por definir las etiquetas finales de estados terminales (supuesto: exitoso, fallido, expirado) y las herramientas de conciliación (supuesto: fixtures y script local).

## Log de decisiones
| ID | Fecha y hora | Decisión | Quién | Alternativas | Impacto |
|---|---|---|---|---|---|
| DEC-01 | 2026-11-06 10:20 | Generar el discovery con todos los supuestos como PROPUESTO | Product Owner (agente) | Esperar confirmación humana de cada supuesto | Evita frenar la construcción; el humano confirma en el G1 |
| DEC-02 | 2026-11-06 10:20 | Comprometer AC1–AC4 de W1, AC1–AC4 y AC6 parcial de W2, W4 completo (AC4 parcial) y W5 completo; diferir AC de KPI | Product Owner (agente) | Comprometer también los AC de KPI | Los KPI no se miden hoy (RN-17); requiere confirmación (PA-10) |
| DEC-03 | 2026-11-06 10:20 | Asignar owners: AI Engineer A para W1, W2, W4; AI Engineer B para W5 | Product Owner (agente) | Otra asignación | Plan de sprints; requiere confirmación (PA-10) |

## Decisiones pendientes
- PA-01 a PA-10. Las de categoría Crítica o Alto impacto (PA-02, PA-04, PA-10) requieren respuesta humana antes de las 10:45.

## Siguiente paso para el rol consumidor
PO humano: confirmar o corregir PA-02, PA-04, PA-09 y PA-10 en el G1 y actualizar este archivo.
