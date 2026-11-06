# Proposal

## Why

Los usuarios que pagan montos pequeños con frecuencia abandonan el alta cuando no saben cuánto falta ni qué corregir. W1 es el primer eslabón del flujo end-to-end: sin una wallet activa no existe pago posible (W2, W4, W5 dependen de ella). Debe quedar en verde a las 11:15 del Sprint 1.

## What Changes

- Flujo de onboarding guiado que muestra la secuencia de pasos y el paso actual en todo momento (W1-AC1).
- Validación por paso que bloquea el avance con datos faltantes o inválidos y devuelve un mensaje accionable (W1-AC2).
- Activación de la wallet al finalizar el onboarding: el estado pasa de `PENDIENTE_ONBOARDING` a `ACTIVA` y se habilita el punto de entrada de pagos de bajo monto (W1-AC3).
- Registro de eventos de inicio, paso completado y cierre del onboarding, para la analítica del MVP (W1-AC4).
- KYC, OTP y biometría se simulan con un mock controlable; no se presentan como integración real.

Fuera de alcance de este cambio:
- W1-AC5 y W1-AC6 (tiempo mediano de 8 a 3 min, MAU 1,000–2,000 y CAC PEN 10): son KPI de negocio que no se miden hoy. Solo se emiten los eventos de AC4 que luego los habilitan.
- El pago en sí (W2) y cualquier uso real de proveedores de identidad.

## Capabilities

### New Capabilities
- `wallet-onboarding`: flujo guiado de alta, validación por paso, activación de la wallet y eventos del onboarding.

### Modified Capabilities
<!-- No hay specs previas en el proyecto. -->

## Impact

- **Backend (NestJS, `backend-nestjs/`)**: módulo de onboarding y de wallet, DTOs con `class-validator`, mock de identidad, registro de eventos. Persistencia en SQLite (PROPUESTO, por confirmar en el G1).
- **Frontend (React, `frontend-react/`)**: pantallas del flujo con indicador de pasos y mensajes de error.
- **Dependencias del resto del plan**: W2 exige wallet `ACTIVA` (RN-10).
- **Referencias**: [W1 en el discovery](../../../challenge/docs/discovery/02-producto/historias/W1-onboarding.md), [reglas](../../../challenge/docs/discovery/04-reglas-y-contratos/01-reglas-de-negocio.md) (RN-04, RN-09, RN-10, RN-17), [estados](../../../challenge/docs/discovery/04-reglas-y-contratos/02-estados-y-transiciones.md).
- **Preguntas abiertas**: PA-01 (frontera de eventos del onboarding), con supuesto propuesto; y el público objetivo (transporte público frente a comercios y smartphone), que no cambia el comportamiento de W1 pero sí los textos y ejemplos.
