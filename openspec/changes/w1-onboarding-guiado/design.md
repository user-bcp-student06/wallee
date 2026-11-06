# Design

## Context

Ver [proposal.md](proposal.md) para el motivo y el alcance. Restricciones que dan forma al enfoque:

- Stack acordado en el equipo: backend NestJS (TypeScript) y frontend React con Vite. El andamiaje de dependencias ya existe en `crew/scaffold.py`.
- Persistencia: SQLite con TypeORM (PROPUESTO, por confirmar en el G1). Datos solo sintéticos.
- Identidad (KYC, OTP, biometría) es MOCK; nada se conecta a proveedores reales.
- Tiempo disponible: W1 debe quedar en verde a las 11:15 (Sprint 1, 10:45–11:15), así que el diseño se mantiene mínimo.
- `output/` está en `.gitignore`: el código que viva ahí no se versiona.

## Goals / Non-Goals

**Goals:**
- Un onboarding de pasos secuenciales con estado persistido por intento, validación en el servidor y eventos registrados.
- Un contrato de API estable que W2 pueda reutilizar para comprobar que la wallet está `ACTIVA` (RN-10).
- Un mock de verificación reproducible, sin intervención manual en la demo.

**Non-Goals:**
- Autenticación, sesiones o inicio de sesión posterior al onboarding.
- Pagos, saldo y reglas de monto (W2, SUP-15).
- Cálculo o reporte de KPI (W1-AC5, W1-AC6); solo se guardan los eventos.
- Reanudar un onboarding abandonado desde otro dispositivo.

## Decisions

### D1. Ubicación del código
El código vive en `backend-nestjs/` y `frontend-react/` en la raíz del repositorio, con los mismos nombres de carpeta que usa `crew/scaffold.py`.
- Alternativa: `output/backend-nestjs` y `output/frontend-react`. Descartada porque `output/` no se versiona y el cambio quedaría fuera del PR.

### D2. Pasos del onboarding (PROPUESTO)
Tres pasos secuenciales: `datos` (nombre y celular), `identidad` (documento, KYC simulado) y `verificacion` (código OTP simulado). Al completar el tercero, la wallet pasa a `ACTIVA`.
- Las fuentes no definen los pasos ni los campos; esta es una propuesta mínima para cubrir W1-AC1 a W1-AC4.
- Alternativa: dos pasos (sin `identidad`). Más rápido, pero deja el KYC simulado fuera del recorrido.

### D3. Orden estricto
Un paso solo puede enviarse si los anteriores están completados. Si no, el servidor responde `409` con código `STEP_OUT_OF_ORDER`. Así el indicador de paso actual siempre es coherente (W1-AC1).

### D4. Modelo de datos
| Entidad | Campos clave |
|---|---|
| `Onboarding` | `id`, `status` (`EN_CURSO` \| `COMPLETADO`), `currentStep`, datos de cada paso |
| `Wallet` | `id`, `onboardingId`, `phone`, `status` (`PENDIENTE_ONBOARDING` \| `ACTIVA`) |
| `OnboardingEvent` | `id`, `onboardingId`, `type`, `step` (opcional), `occurredAt` |

La wallet se crea en `PENDIENTE_ONBOARDING` al iniciar el onboarding y cambia a `ACTIVA` en la misma transacción que marca el onboarding `COMPLETADO`. El saldo inicial lo define W2.

### D5. Contrato de API (REST, JSON)
| Método y ruta | Resultado |
|---|---|
| `POST /onboarding` | `201` con `onboardingId`, `walletId`, lista de pasos con su estado y `currentStep` |
| `GET /onboarding/:id` | `200` con el progreso actual |
| `PUT /onboarding/:id/steps/:stepKey` | `200` con el progreso actualizado; `400` `VALIDATION_ERROR` con el detalle por campo; `409` `STEP_OUT_OF_ORDER`; `404` `ONBOARDING_NOT_FOUND` |
| `GET /wallets/:id` | `200` con `status`; W2 lo usa para RN-10 |

Los errores devuelven un código de motivo estable y un mensaje que indica qué corregir (W1-AC2).

### D6. Validaciones
Con DTOs y `class-validator` en el servidor; el cliente solo ayuda. Reglas: nombre obligatorio; celular de 9 dígitos que empieza con 9 (RN-04); documento de 8 dígitos (PROPUESTO); código de verificación obligatorio.

### D7. Mock de identidad
- KYC: acepta cualquier documento con formato válido.
- OTP: el código `123456` es válido; cualquier otro devuelve `VALIDATION_ERROR`.
- El valor fijo vive en configuración y solo se acepta fuera de producción.
- Nada llama a servicios externos. Se declara como MOCK en el README y en la demo.

### D8. Eventos
Se registran `onboarding_started`, `onboarding_step_completed` (con el paso) y `onboarding_completed`, con marca de tiempo del servidor. Esto adopta el supuesto SUP-09 para PA-01: inicio = `onboarding_started`, fin = `onboarding_completed` con wallet `ACTIVA`.

### D9. Frontend
Un asistente de pasos en React con un indicador que muestra todos los pasos y el actual. Los mensajes de error se toman de la respuesta de la API. Al completar, se muestra el punto de entrada de pagos.
- El `onboardingId` se conserva en el estado del cliente; no hay reanudación entre sesiones (ver Non-Goals).

## Risks / Trade-offs

- [Pasos y campos inventados] → Se marcan PROPUESTO y se confirman en el G1; cambiarlos solo toca D2, D6 y las tareas de UI.
- [Público objetivo sin resolver: transporte público frente a comercios/smartphone] → W1 no depende del público; solo cambian textos y ejemplos de la UI.
- [30 minutos para construir y probar] → Alcance mínimo de tres pasos y un solo mock; el stretch se cancela si W1 no está en verde.
- [Sin autenticación] → Cualquiera con el `onboardingId` podría continuar el alta. Aceptable en un MVP con datos sintéticos; se anota como pendiente para después del hackathon.
- [Código OTP fijo] → Solo activo fuera de producción y sin datos reales.

## Open Questions

- ¿Los campos exactos del paso `identidad` (por ejemplo, tipo de documento)? No cambia las specs ni las tareas.
