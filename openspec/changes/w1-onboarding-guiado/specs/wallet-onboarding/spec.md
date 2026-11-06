# Spec Delta

## Purpose

Define el comportamiento observable del alta de usuario en la wallet: pasos guiados, validación, activación de la wallet y eventos de analítica, para que el usuario pueda empezar a pagar sin abandonar el proceso.

## ADDED Requirements

### Requirement: Secuencia de pasos visible
El sistema SHALL mostrar al usuario la secuencia completa de pasos requeridos y el paso actual en todo momento durante el onboarding.

#### Scenario: Inicio del onboarding
- **WHEN** el usuario inicia el onboarding
- **THEN** el sistema muestra todos los pasos requeridos y marca el primero como paso actual

#### Scenario: Avance al siguiente paso
- **WHEN** el usuario completa un paso correctamente
- **THEN** el sistema marca ese paso como completado y muestra el siguiente como paso actual

### Requirement: Bloqueo del avance con datos faltantes o inválidos
El sistema SHALL impedir avanzar al siguiente paso cuando falte información obligatoria o haya datos inválidos, e SHALL indicar qué corregir mediante un mensaje accionable.

#### Scenario: Campo obligatorio vacío
- **WHEN** el usuario intenta avanzar con un campo obligatorio vacío
- **THEN** el sistema bloquea el avance, conserva el paso actual y muestra un mensaje que indica qué campo completar

#### Scenario: Número de celular inválido
- **WHEN** el usuario ingresa un celular que no tiene 9 dígitos o no empieza con 9
- **THEN** el sistema bloquea el avance y muestra un mensaje con el formato esperado

#### Scenario: Código de verificación incorrecto
- **WHEN** el usuario ingresa un código de verificación incorrecto
- **THEN** el sistema bloquea el avance y muestra un mensaje que permite reintentar

### Requirement: Activación de la wallet al finalizar
El sistema SHALL cambiar el estado de la wallet de `PENDIENTE_ONBOARDING` a `ACTIVA` únicamente cuando todos los pasos requeridos se completen correctamente.

#### Scenario: Onboarding completado
- **WHEN** el usuario completa todos los pasos requeridos
- **THEN** la wallet queda en estado `ACTIVA` y el usuario accede al punto de entrada de pagos de bajo monto

#### Scenario: Onboarding incompleto
- **WHEN** el usuario no ha completado todos los pasos requeridos
- **THEN** la wallet permanece en `PENDIENTE_ONBOARDING` y el sistema no permite acceder al punto de entrada de pagos

### Requirement: Registro de eventos del onboarding
El sistema SHALL registrar un evento al iniciar el onboarding, un evento por cada paso completado y un evento al cerrar el flujo, para la analítica del MVP.

#### Scenario: Inicio registrado
- **WHEN** el usuario inicia el onboarding
- **THEN** el sistema registra el evento `onboarding_started` con su marca de tiempo

#### Scenario: Paso completado registrado
- **WHEN** el usuario completa un paso
- **THEN** el sistema registra el evento `onboarding_step_completed` identificando el paso y su marca de tiempo

#### Scenario: Cierre registrado
- **WHEN** el onboarding finaliza con la wallet activa
- **THEN** el sistema registra el evento `onboarding_completed` con su marca de tiempo

### Requirement: Verificación de identidad simulada
El sistema SHALL resolver la verificación de identidad (KYC, OTP y biometría) mediante un mecanismo simulado y reproducible, y SHALL NOT presentarlo como una integración real.

#### Scenario: Verificación con datos de prueba
- **WHEN** el usuario envía un código de verificación de prueba válido
- **THEN** el sistema considera completado el paso de verificación sin invocar ningún proveedor externo
