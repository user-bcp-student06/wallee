---
id: DISC-README
titulo: Discovery — Wallet Perú (índice)
estado: propuesto
responsable: Product Owner
actualizado: 2026-11-06 10:20
fuentes: [challenge/epic/peru-wallet-mvp.sp.md, challenge/user-stories/*.sp.md]
depende_de: []
lo_consumen: [Arquitecto/a, AI Engineer A, AI Engineer B, QA & Security, Presenter/Timekeeper]
---

## Resumen
Discovery de la wallet de pagos cotidianos de bajo monto en Perú. Compromiso propuesto: W1, W2, W4 y W5 (17 de 28 AC); stretch: W3 y W6. Todo está en estado `propuesto` hasta que un humano lo confirme.

## Cómo leer
Lee este README y tu handoff. Si necesitas más contexto, sigue los enlaces.

## Orden de lectura por rol
| Rol | Lee en este orden |
|---|---|
| Arquitecto/a | [handoff](06-handoff-por-rol/arquitecto.md) → [reglas](04-reglas-y-contratos/01-reglas-de-negocio.md) → [estados](04-reglas-y-contratos/02-estados-y-transiciones.md) → [mock](04-reglas-y-contratos/03-convenciones-mock.md) |
| AI Engineer A | [handoff](06-handoff-por-rol/ai-engineer-a-dominio.md) → [W1](02-producto/historias/W1-onboarding.md) → [W2](02-producto/historias/W2-pago-contacto.md) → [W4](02-producto/historias/W4-idempotencia.md) |
| AI Engineer B | [handoff](06-handoff-por-rol/ai-engineer-b-crew.md) → [flujo](02-producto/02-flujo-end-to-end.md) → [W5](02-producto/historias/W5-fallas-reversos.md) |
| QA & Security | [handoff](06-handoff-por-rol/qa-security.md) → [reglas](04-reglas-y-contratos/01-reglas-de-negocio.md) → [matriz](05-trazabilidad/01-matriz-trazabilidad.md) |
| Presenter/Timekeeper | [handoff](06-handoff-por-rol/presenter.md) → [reto](00-contexto/01-reto-hackathon.md) → [plan](03-alcance-hackathon/02-plan-de-sprints.md) |

## Índice y estado
| Archivo | Estado |
|---|---|
| [00-contexto/01-reto-hackathon](00-contexto/01-reto-hackathon.md) · [02-glosario](00-contexto/02-glosario.md) | propuesto |
| [01-discovery/01-problema-y-oportunidad](01-discovery/01-problema-y-oportunidad.md) | propuesto |
| [01-discovery/02-usuarios-y-necesidades](01-discovery/02-usuarios-y-necesidades.md) | propuesto |
| [01-discovery/03-objetivos-y-metricas](01-discovery/03-objetivos-y-metricas.md) | propuesto |
| [01-discovery/04-alcance-in-out](01-discovery/04-alcance-in-out.md) | propuesto |
| [01-discovery/05-supuestos-restricciones](01-discovery/05-supuestos-restricciones.md) | propuesto |
| [01-discovery/06-riesgos-y-dependencias](01-discovery/06-riesgos-y-dependencias.md) | propuesto |
| [02-producto/01-epica](02-producto/01-epica.md) · [02-flujo-end-to-end](02-producto/02-flujo-end-to-end.md) · [03-mapa-de-historias](02-producto/03-mapa-de-historias.md) | propuesto |
| [02-producto/historias](02-producto/historias/) W1 a W6 | propuesto |
| [03-alcance-hackathon](03-alcance-hackathon/) (4 archivos) | propuesto |
| [04-reglas-y-contratos](04-reglas-y-contratos/) (3 archivos) | propuesto |
| [05-trazabilidad/01-matriz-trazabilidad](05-trazabilidad/01-matriz-trazabilidad.md) | propuesto (plantilla vacía) |
| [05-trazabilidad/02-decisiones](05-trazabilidad/02-decisiones.md) | propuesto |
| [06-handoff-por-rol](06-handoff-por-rol/) (5 archivos) | propuesto |

## Cifras clave (PROPUESTAS)
S/ 500 por transacción · ventana de idempotencia 24 h · PENDING no es terminal · mock por último dígito del celular.

## Decisiones pendientes
- PA-01 a PA-10 en [02-decisiones](05-trazabilidad/02-decisiones.md).

## Siguiente paso para el rol consumidor
Humano PO: confirmar PA-02, PA-04, PA-09 y PA-10 en el G1 (10:00).
