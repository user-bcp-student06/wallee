---
id: DISC-01-02
titulo: Usuarios y necesidades
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/epic/peru-wallet-mvp.sp.md (Usuarios objetivo), challenge/user-stories/*.sp.md]
depende_de: []
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security]
---

## Resumen
Dos usuarios objetivo en la épica y dos roles internos en las historias. El flujo comprometido atiende al usuario que paga y a soporte.

## Personas
| Persona | Necesidad | HU | Compromiso |
|---|---|---|---|
| Usuario de smartphone con transferencias diarias de bajo monto | Recorrido rápido y de baja fricción, de la intención a la confirmación | W1, W2 | Comprometido |
| Pequeño comercio que cobra con QR | Aceptación predecible y confirmación confiable | W3 | Stretch |
| Analista de operaciones y confiabilidad | Que los reintentos no dupliquen dinero ni desvíen la conciliación | W4, W6 | W4 comprometido; W6 stretch |
| Especialista de soporte al cliente | Rutas de atención explícitas para pagos fallidos, expirados y disputados | W5 | Comprometido |

## Qué necesita saber el usuario que paga
1. Si su operación se realizó, falló o expiró.
2. Cuál es el siguiente paso cuando algo sale mal.
3. Que un reintento no le cobrará dos veces.

## Decisiones pendientes
- PA-03: canal de consulta del comercio (afecta solo W3, stretch).

## Siguiente paso para el rol consumidor
AI Engineer A: construir primero el recorrido del pagador ([W1](../02-producto/historias/W1-onboarding.md) y [W2](../02-producto/historias/W2-pago-contacto.md)).
