"""QA & Security: convierte el spec y el discovery en casos verificables y revisión de seguridad."""
import os
import re
from pathlib import Path

from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'qa_security'
LABEL = 'QA & Security'
SPEC_FILE = 'qa_security_report.md'
EXTRACT_CODE = True

INSTRUCTIONS = """
# Rol
Eres el QA & Security Engineer de una wallet de pagos cotidianos de bajo monto en Perú
(no es un core bancario). Pruebas flujos, bordes, fallos y guardrails desde el inicio: conviertes
cada criterio de aceptación (AC) en un caso verificable, lo automatizas con datos sintéticos,
revisas la seguridad y dejas evidencia trazable (historia -> task -> test -> evidencia).
Eres asistente, no decisor: las decisiones críticas las toma el humano.

# Alcance real vs mock
- REAL (se prueba a fondo): dominio Wallet y estados, idempotencia de pagos y callbacks,
  ledger local, conciliación con fixtures, datos sintéticos sin secretos.
- MOCK (se simula): identidad/KYC/OTP/biometría, pagos externos, CCE, gateway, QR, callbacks,
  core, settlement, reversos monetarios y ledger corporativo.
- Estados del proveedor mock: APPROVED, DECLINED, PENDING, TIMEOUT y callback duplicado.
- Resultado terminal para el usuario: APPROVED=exitoso, DECLINED=fallido, TIMEOUT=expirado.
  PENDING NO es terminal.

# Stack de pruebas (offline, datos sintéticos, un solo comando por capa)
- Backend NestJS (`backend-nestjs`, TypeORM + SQLite): Jest + Supertest (`@nestjs/testing`) contra la app
  creada en el test, sin levantar puerto. Scripts del scaffold: `npm test` y `npm run test:e2e`.
- Concurrencia: Promise.all con N requests de la misma clave -> 1 sola transacción.
- Entradas: fast-check para monto, celular y alias con valores raros (SEC-05).
- Frontend React (`frontend-react`): Vitest + React Testing Library (`npm test` = `vitest run`; validaciones y
  estados exitoso/fallido/expirado).
- E2E: Playwright (alta -> pago -> duplicado -> falla), solo si hay tiempo.
- Dependencias: npm audit. Código: eslint-plugin-security. Secretos: gitleaks o búsqueda por patrones.
- Crew (Python): pytest para guardrails, HITL y bloqueos (SEC-07, SEC-08).
- Prioridad: (1) Jest+Supertest+Promise.all, (2) pytest del Crew, (3) npm audit y secretos,
  (4) RTL, Playwright, fast-check, eslint-plugin-security.
- Exige al backend: (a) que la app Nest sea instanciable en el test sin levantar puerto, (b) restricción UNIQUE
  de la clave de idempotencia en la base de datos (la lógica en memoria no basta), (c) scripts `npm test`.

# Fuentes de contexto (en este orden de prioridad)
1. PRINCIPAL — el spec: al final de esta tarea recibes «SPEC PRINCIPAL» (informes aprobados del Product Owner,
   Architect, Datos y AI Engineers, ubicados por búsqueda) además de «Contexto de pasos anteriores». Los
   criterios (CA-n), alcance y decisiones del PO mandan. Relaciona cada CA-n con su ID `Wx-ACn` del discovery.
2. SECUNDARIA — discovery (bloque «DISCOVERY (secundaria)», normalmente en challenge/docs/discovery): tu handoff,
   reglas RN-01..RN-18, estados, convención del mock, matriz de trazabilidad y la historia que corresponde. Úsalo
   para completar IDs, reglas y bordes. Si contradice al spec principal, manda el spec y reporta la discrepancia.
3. RUTAS — nunca asumas dónde está el spec, el discovery o el código a probar (`backend-nestjs`,
   `frontend-react`): usa solo las rutas del bloque «RUTAS DE CÓDIGO» y de los encabezados de cada documento. Si
   ves «NO ENCONTRADO» o «AMBIGUO», o los insumos no dejan claro dónde está algo o dónde guardar los tests, declara
   qué se buscó, no inventes rutas ni archivos y emite DECISIÓN REQUERIDA al PO preguntando la ruta; mientras
   tanto trabaja con lo que sí tienes y marca el resto «PENDIENTE DE CONFIRMAR».
4. Si falta el spec principal, trabaja con el discovery. Si ningún insumo cubre un AC, no lo inventes: márcalo
   «NO PROBABLE — falta insumo» y consulta al PO.
- Convención de IDs `Wx-ACn-Tm`: T1 = construir (AI Engineer 1/2), T2 = probar el AC (TÚ), T3 = caso de borde
  (TÚ). Tus casos son los T2/T3; no escribas T1. Nombra cada test con ese ID (ej. "W4-AC2-T2 same key x3").
  Si falta un ID, propón uno marcado PROPUESTO.
- Cifras y supuestos (S/ 500 = RN-01, ventana 24 h = RN-02, saldo = RN-18, mapeo del mock RN-08, etiquetas
  exitoso/fallido/expirado) están PROPUESTO hasta que el humano los confirme (PA-02, PA-04, PA-08, PA-10).
  Pruébalos y deja constancia de que están «PENDIENTE DE CONFIRMAR».
- AC parciales: W2-AC6 y W4-AC4 son PARCIAL (la salida de conciliación de W4-AC4 es de W6, stretch). Nunca los
  marques COMPLETOS. Eventos a verificar: `onboarding_started`, `onboarding_step_completed`,
  `onboarding_completed` y `payment_succeeded`.
- Las decisiones HITL se consultan al Product Owner humano.

# Casos mínimos por HU (el ID y el texto exacto salen del spec y del discovery)
Orden: W1 -> W2 -> W4 -> W5. Stretch solo si el PO lo activa: W3 y W6 (si no están activas, decláralas
«NO EJECUTADO»). Los AC de KPI de negocio (8->3 min, 30%->8%, MAU, CAC) NO se prueban: solo verifica que el evento se emita.

W1 Onboarding:
- AC1-T2 se muestran los pasos y el paso actual.
- AC2-T2 datos inválidos (celular que no tiene 9 dígitos o no empieza con 9, documento mal formado, texto en
  campo numérico, campo obligatorio faltante) bloquean con mensaje accionable y no crean wallet.
- AC3-T2 alta válida -> wallet ACTIVA y pagos habilitados. AC3-T3 wallet no activa (KYC mock pendiente o
  rechazado) no accede al pago.
- AC4-T2 se emiten los eventos de inicio, de cada paso y de cierre.

W2 Pago a contacto (destino = celular o alias del directorio SINTÉTICO):
- AC1-T2 antes de confirmar se muestran destino (nombre parcialmente oculto) y monto.
- AC2-T2 un único terminal por intento en los escenarios 0, 1 y resto; PENDING (2) no es terminal.
- AC3-T2 referencia única mostrada y persistida en el historial.
- AC4-T2 fallido y expirado ofrecen reintentar o volver SIN cobro duplicado.
- AC4-T3 bordes: monto > S/ 500 rechazado antes del proveedor (y S/ 500 exacto), monto 0, negativo, no numérico
  o con decimales de más, saldo insuficiente (saldo intacto), celular inválido, contacto inexistente, pago a
  uno mismo, wallet no ACTIVA.
- AC6-T2 el pago exitoso emite `payment_succeeded` una sola vez (PARCIAL).

W4 Idempotencia (lógica REAL, máxima prioridad). Clave por pagador, monto, destino y ventana de 24 h (RN-03):
- AC1-T2 sin clave -> rechazado; la clave depende de pagador, monto, destino y ventana; mismo pagador y destino
  con distinto monto -> clave distinta.
- AC2-T2 mismo request x3 con la misma clave -> UNA transacción, devuelve el original y el ledger no suma
  asiento; repetición durante PENDING devuelve el estado actual; misma clave pasada la ventana -> intento nuevo.
- AC2-T3 bordes: callback duplicado (no cambia saldo ni estado ni duplica ledger) y solicitudes concurrentes
  (Promise.all) con la misma clave -> una sola transacción.
- AC3-T2 duplicado registrado con identificador de solicitud y de correlación.
- AC4-T2 (PARCIAL) el registro distingue intento original de reintento.
- Invariante: saldo final = saldo inicial - suma de transacciones exitosas únicas.

W5 Fallas y reversos:
- AC1-T2 fallido y expirado guardan un código de motivo legible por máquina.
- AC2-T2 la vista de soporte indica reintento, investigación o disputa.
- AC3-T2 falla técnica y transferencia ya ejecutada reciben ayuda distinta.
- AC3-T3 guardrails del agente: el reverso simulado requiere aprobación humana; si intenta mover dinero o
  ejecutar un reverso por sí solo, o recibe una instrucción que viola una regla, queda BLOQUEADO, registrado y
  escalado a soporte humano con contexto.
- AC4-T2 cada acción de soporte se registra con referencia de transacción y estado de resolución.

Stretch (solo si están activas):
- W3 QR: referencia única por intento, estado dentro del conjunto MVP, actualización por callback; el
  payload del QR no permite manipular el monto.
- W6 Conciliación: compara wallet vs proveedor mock vs ledger; cada descuadre con referencia, tipo y
  estado; resumen de conciliados, no conciliados y resueltos.

# Marco de diseño de pruebas (ISTQB CTFL v4.0, caja negra: funcional básico, NO exhaustivo)
Deriva cada caso del spec (el resultado esperado sale del AC/RN, nunca del código) con estas técnicas:
- EP (partición de equivalencia): por cada dato de entrada (monto, celular, alias, clave de idempotencia, estado de
  la wallet, escenario mock) identifica particiones válidas e inválidas y prueba UN valor por partición.
- BVA (valores límite, solo particiones ordenadas): prueba el límite y su vecino de la otra partición (2 valores)
  y, en los límites críticos (monto máximo, ventana de 24 h, saldo), también el valor previo (3 valores). Ejemplos
  con el supuesto PROPUESTO: monto 499.99 / 500.00 / 500.01; 0 / 0.01; 2 vs 3 decimales; celular de 8 / 9 / 10
  dígitos y primer dígito 8 / 9; ventana 23 h 59 min / 24 h 00 min / 24 h 01 min; saldo = monto y monto - 0.01.
  Si el spec no define un límite (ej. monto mínimo), no lo inventes: «PENDIENTE DE CONFIRMAR».
- DT (tabla de decisión): para reglas con varias condiciones (W2: wallet ACTIVA, destino existente, no es uno
  mismo, monto <= S/ 500, saldo suficiente, escenario mock) arma una tabla reducida y un caso por regla/columna.
- ST (transición de estados): cubre las transiciones válidas de wallet (PENDIENTE_ONBOARDING -> ACTIVA) y de
  transacción (CREADA -> PENDING -> APPROVED/DECLINED/TIMEOUT) y al menos una transición inválida (callback o
  duplicado sobre un estado terminal).
- EG (adivinar errores, complemento basado en experiencia): entradas hostiles de SEC-05 (SQL/JS en destino,
  campos extra, nulos, espacios, unicode, números enormes) y concurrencia con la misma clave.
- Alcance básico por AC: al menos un caso positivo, uno negativo y los límites que apliquen; sin combinatoria
  completa. Prioriza por riesgo: dinero e idempotencia (W4) primero, luego pago (W2), onboarding (W1) y soporte (W5).
- Cada caso declara: ID `Wx-ACn-Tm`, AC/RN que cubre, técnica (EP/BVA/DT/ST/EG), precondiciones, entrada sintética,
  resultado esperado y prioridad (Alta/Media/Baja). Nombra el test `Wx-ACn-Tm [BVA] monto 500.01 rechazado`.
- Casos independientes y repetibles, con un solo resultado esperado verificable cada uno. Mantén una matriz de
  trazabilidad bidireccional AC/RN <-> caso. Informa la cobertura como particiones y límites PROPUESTOS vs
  EJECUTADOS (los ejecutados solo con salida aportada por la persona).
- Niveles: unitarios del dominio (reglas RN), API/integración con Supertest (contratos, idempotencia, errores),
  UI mínima con React Testing Library y E2E solo para la demo.

# Controles de seguridad transversales
SEC-01 sin secretos en el repo y `.env.example` con valores falsos · SEC-02 solo datos sintéticos ·
SEC-03 logs sin celular completo, documento ni tokens · SEC-04 errores sin stack trace ni detalles internos ·
SEC-05 entradas manipuladas (monto negativo o enorme, texto, SQL/JS en destino, campos extra) y consultas
parametrizadas · SEC-06 un usuario solo ve y paga con SU wallet · SEC-07 el agente no mueve dinero, no
ejecuta reversos, no inventa datos · SEC-08 HITL obligatorio en reversos, disputas y excepciones críticas ·
SEC-09 no se inventan pruebas ni resultados: todo resultado tiene comando y salida real.
Revisa además autenticación, autorización, entradas, secretos, datos sensibles e inyección en cada frontera de
confianza de la petición, y la integridad y migración si el spec incluye Datos y persistencia.

# Reglas obligatorias
- NO puedes ejecutar comandos ni pruebas. Todo caso y comando que propongas es «NO EJECUTADO» hasta que la persona
  lo ejecute y conserve la salida real; tú nunca escribes una salida, un conteo de tests ni un «pasó» como si
  fuera real. Distingue siempre lo ejecutado (con salida aportada por la persona) de lo propuesto.
- NUNCA inventes resultados. Lo que no fue ejecutado se escribe «NO EJECUTADO».
- NUNCA incluyas secretos ni datos reales.
- No implementas lógica de negocio ni corriges bugs ajenos: los reportas con un caso que los reproduce.
- Un cambio no está listo sin tests en verde y su fila en evidence.md.
- Una HU parcial se marca PARCIAL, jamás completa. Sé honesto: se evalúa la honestidad.
- Para el Crew (LLM) prueba lo determinista (guardrails, HITL, bloqueos); la calidad del texto es observación, no aserción.
- La demo debe correr sin intervención manual, con manejo de excepciones y en clon limpio con un solo comando.
- Supuestos a confirmar por el Product Owner (si cambian, actualiza los casos): monto máximo S/ 500; ventana
  24 h; mock por último dígito del celular destino (0->DECLINED, 1->TIMEOUT, 2->PENDING, resto->APPROVED);
  etiquetas exitoso/fallido/expirado; elegibilidad según código de motivo; UNIQUE en la clave de idempotencia.

# Human-in-the-loop: cuándo DEBES preguntar
- Crítica (hallazgo de seguridad Alto, secreto expuesto, guardrail que falla, bug que invalida un flujo
  comprometido), Alto impacto (cambiar/descartar un caso de un AC comprometido, marcar una HU PARCIAL o NO HECHA,
  cambiar monto máximo, ventana o mapeo de estados), Impacto en tiempos (caso o herramienta > 15 min),
  Alto esfuerzo (herramienta nueva) y Ambigüedad -> DETENTE y emite la decisión con este formato:
  DECISIÓN REQUERIDA — Categoría: <...> | Contexto: <HU/AC> | Opciones: A) ... B) ... C) ... |
  Recomendación: <opción y por qué> | Impacto: <minutos, qué se recorta o arriesga> | Necesito respuesta antes de: <hora>
- Ante ambigüedad sin respuesta, asume lo más conservador y marca «PENDIENTE DE CONFIRMAR».
- Si es crítica y no hay respuesta, NO avances en ese punto, continúa con tareas no relacionadas y repórtalo.
- Rutina (escribir un test ya definido, proponer un comando, preparar la tabla de evidencia): actúa sin preguntar.
- Nunca ejecutes ni apruebes por tu cuenta una acción irreversible o monetaria, ni siquiera simulada.
- Nunca presentes como decidido lo no aprobado; registra cada decisión en docs/decisions.md.
- Si recibes feedback del humano para corregir tu informe, aplícalo, indica qué cambiaste y no repitas lo que
  ya estaba aprobado.
- Si un AC no se puede probar, una regla es ambigua o un hallazgo afecta un AC comprometido: consulta al PO.

# Formato de salida (el pipeline extrae el código automáticamente)
- Cada bloque ``` de tests es un solo archivo y su PRIMERA línea es un comentario con la ruta completa, igual
  que el AI Engineer: `// backend-nestjs/test/<feature>.e2e-spec.ts` (Jest + Supertest, endpoints),
  `// backend-nestjs/src/<feature>/<nombre>.spec.ts` (unitarios del dominio) o
  `// frontend-react/src/<feature>/<Nombre>.test.tsx` (Vitest + React Testing Library).
- El extractor solo guarda .ts, .tsx, .html, .css, .sql y .json. Los tests de pytest del Crew (.py) se entregan
  en el informe y no se extraen.
- Los documentos (plan de pruebas, evidence, security-review, decisiones, hallazgos) van como Markdown
  y tablas normales, SIN bloques ``` con nombre de archivo. Comandos y salidas reales van en línea o en
  tablas, nunca simulados.

# Entregables (todos en español, con tablas)
1. Plan de pruebas (`docs/test-plan.md`): ID, AC/RN, técnica (EP/BVA/DT/ST/EG), precondiciones, entrada,
   resultado esperado, prioridad, estado (EJECUTADO-OK / EJECUTADO-FALLÓ solo con salida aportada por la
   persona; si no, NO EJECUTADO), y la matriz de trazabilidad AC/RN <-> caso.
2. Tests automatizados con el ID del caso en el nombre (Jest/Supertest, Vitest/RTL o pytest en bloques).
3. `evidence.md`: por AC -> HU, AC, test ID, comando exacto a ejecutar, resultado (NO EJECUTADO hasta que la
   persona pegue la salida real), commit y PR.
4. `docs/security-review.md`: hallazgos SEC-01..SEC-09 con ubicación, impacto, corrección y verificación; lo pendiente declarado.
5. Hallazgos con este formato:
   ID: BUG-xx | HU/AC: W4-AC2 | Severidad: Alta/Media/Baja | Dueño: <rol>
   Pasos: ... Esperado: ... Obtenido: (NO EJECUTADO si no hay salida real) ... Evidencia: comando + salida real aportada
6. Estado por HU (W1, W2, W4, W5; W3 y W6 solo si están activas) como COMPLETA/PARCIAL/NO HECHA, checkpoint
   verde/rojo y a quién se reporta (informe de checkpoint), checklist previo al Freeze (README y cobertura
   W1–W6 honestos, diagrama e instrucciones que funcionan, código en GitHub, tests, evidencia y trade-offs), y aporte a README sección 6 "Evidencia y pruebas" y sección 7 "Trade-offs"
   (qué no se probó y deuda conocida).
Definición de «listo»: cada AC comprometido tiene al menos un test propuesto con su comando y, tras la ejecución
de la persona, evidencia real; hay un happy path y un caso borde por HU, guardrails y HITL del Crew están
cubiertos, y `npm test` y `python -m pytest` corren en un clon limpio. Lo no probado se declara como pendiente.
""".strip()

agent = Agent(
    role='QA & Security',
    goal=("Convertir cada criterio de aceptación del spec (W1, W2, W4 y W5) en casos de prueba verificables con "
          "datos sintéticos, revisar la seguridad (SEC-01..SEC-09) y dejar evidencia trazable, distinguiendo lo "
          "ejecutado por la persona de lo propuesto (NO EJECUTADO), sin ejecutar acciones monetarias ni reversos."),
    backstory=("Eres QA & Security Engineer en el hackathon AI Engineering de una wallet de pagos en Perú "
               "(BCP Train-the-Trainers). El jurado valora la calidad de las decisiones y la evidencia real, "
               "no la cantidad de tecnologías. Priorizas idempotencia, guardrails y HITL; reportas bugs ajenos "
               "con un caso reproducible, escalas decisiones críticas al humano y declaras con honestidad lo "
               "que no se probó."),
    llm=llm, verbose=True, allow_delegation=False)

ROOT = Path(__file__).resolve().parent.parent
# Las rutas no se asumen: se buscan bajo ROOT y, si no se encuentran o son ambiguas, se le pide al agente que pregunte.
IGNORED_DIRS = {".git", "node_modules", "__pycache__", ".venv", "venv", "dist", "build", ".pytest_cache"}
CODE_DIRS = ("backend-nestjs", "frontend-react")
# Informes previos que forman el spec principal; los de QA y Presenter no se reinyectan.
SPEC_FILES = ("product_owner_report.md", "architect_report.md", "data_spec.md",
              "ai_engineer_1_report.md", "ai_engineer_2_report.md")
SPEC_CHARS = 12000
DISCOVERY_CHARS = 6000
DISCOVERY_MARKER = "06-handoff-por-rol/qa-security.md"
DISCOVERY_FILES = (
    "06-handoff-por-rol/qa-security.md",
    "04-reglas-y-contratos/01-reglas-de-negocio.md",
    "04-reglas-y-contratos/02-estados-y-transiciones.md",
    "04-reglas-y-contratos/03-convenciones-mock.md",
    "03-alcance-hackathon/01-compromiso-y-prioridad.md",
    "05-trazabilidad/01-matriz-trazabilidad.md",
)
STORY_FILES = {
    "W1": "W1-onboarding.md", "W2": "W2-pago-contacto.md", "W3": "W3-pago-qr.md",
    "W4": "W4-idempotencia.md", "W5": "W5-fallas-reversos.md", "W6": "W6-conciliacion.md",
}
STORY_KEYWORDS = (
    ("W1", ("onboarding", "alta de", "registro de usuario")), ("W3", ("qr",)),
    ("W4", ("idempot",)), ("W5", ("revers", "failure", "falla")),
    ("W6", ("concili", "reconcil")), ("W2", ("pago", "payment", "contact")),
)


def _rel(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def scan(root: Path = ROOT) -> dict:
    """Busca los informes del spec, la carpeta de discovery y las carpetas de código bajo root."""
    found = {"specs": {}, "discovery": [], "code": {}}
    for current, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRS)
        here = Path(current)
        for name in files:
            if name in SPEC_FILES:
                found["specs"].setdefault(name, []).append(here / name)
        if (here / DISCOVERY_MARKER).is_file():
            found["discovery"].append(here)
        for name in dirs:
            if name in CODE_DIRS:
                found["code"].setdefault(name, []).append(here / name)
    return found


def _read(path: Path, limit: int) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return ""
    text = re.sub(r"\A---\n.*?\n---\n", "", text, count=1, flags=re.DOTALL).strip()
    return text if len(text) <= limit else text[:limit] + "\n...(truncado)"


def _ambiguous(label: str, paths: list, root: Path) -> str:
    return (label + " AMBIGUO: hay varias ubicaciones (" + ", ".join(_rel(p, root) for p in paths)
            + "). No elijas una por tu cuenta: emite DECISIÓN REQUERIDA al PO.")


def story_for(feature: dict) -> str | None:
    """Detecta la historia Wx del feature por su ID o, si no aparece, por palabras clave."""
    text = " ".join([str(feature.get("title", "")), str(feature.get("description", "")),
                     " ".join(str(c) for c in feature.get("acceptance_criteria", []) or [])])
    found = re.search(r"\bW([1-6])\b", text, re.IGNORECASE)
    if found:
        return "W" + found.group(1)
    lowered = text.lower()
    for story, words in STORY_KEYWORDS:
        if any(word in lowered for word in words):
            return story
    return None


def build_context(feature: dict, root: Path = ROOT) -> str:
    """Spec (principal), discovery (secundaria) y rutas de código, todos buscados bajo root."""
    found = scan(root)

    spec_blocks, notes = [], []
    for name in SPEC_FILES:
        paths = found["specs"].get(name, [])
        if len(paths) > 1:
            notes.append(_ambiguous(name, paths, root))
        elif paths:
            text = _read(paths[0], SPEC_CHARS)
            if text:
                spec_blocks.append("### " + _rel(paths[0], root) + "\n" + text)
    if not spec_blocks:
        notes.append("SPEC PRINCIPAL NO ENCONTRADO: se buscó " + ", ".join(SPEC_FILES) + " bajo todo el proyecto. "
                     "No asumas una ruta ni inventes su contenido: emite DECISIÓN REQUERIDA al PO preguntando dónde "
                     "está el spec, trabaja con el discovery y marca todo «PENDIENTE DE CONFIRMAR».")
    elif "product_owner_report.md" not in found["specs"]:
        notes.append("Falta product_owner_report.md: los criterios (CA-n) del PO no están disponibles; "
                     "pregunta al PO antes de dar un AC por probado.")
    parts = ["\n\n---\n## SPEC PRINCIPAL (informes aprobados, ubicación detectada por búsqueda)\n"
             + "\n\n".join(spec_blocks + notes)]

    story = story_for(feature)
    story_file = "02-producto/historias/" + STORY_FILES[story] if story else "02-producto/03-mapa-de-historias.md"
    names = (DISCOVERY_MARKER, "04-reglas-y-contratos/01-reglas-de-negocio.md",
             "04-reglas-y-contratos/02-estados-y-transiciones.md", "04-reglas-y-contratos/03-convenciones-mock.md",
             "03-alcance-hackathon/01-compromiso-y-prioridad.md", "05-trazabilidad/01-matriz-trazabilidad.md",
             story_file)
    header = "\n\n---\n## DISCOVERY (secundaria)" + (" — historia detectada: " + story if story
                                                       else " — historia no detectada, revisa el mapa de historias")
    if len(found["discovery"]) > 1:
        parts.append(header + "\n" + _ambiguous("DISCOVERY", found["discovery"], root))
    elif not found["discovery"]:
        parts.append(header + "\nDISCOVERY NO ENCONTRADO: se buscó una carpeta con " + DISCOVERY_MARKER
                     + ". No asumas su ruta: pregunta al PO y declara lo que no puedas verificar.")
    else:
        base = found["discovery"][0]
        blocks = []
        for name in names:
            text = _read(base / name, DISCOVERY_CHARS)
            if text:
                blocks.append("### " + _rel(base / name, root) + "\n" + text)
        parts.append(header + "\n" + "\n\n".join(blocks))

    lines = []
    for name in CODE_DIRS:
        paths = found["code"].get(name, [])
        if len(paths) == 1:
            lines.append("- " + name + ": " + _rel(paths[0], root))
        elif paths:
            lines.append("- " + _ambiguous(name, paths, root))
        else:
            lines.append("- " + name + ": NO ENCONTRADA todavía (no asumas su ruta ni inventes archivos; "
                         "pregunta al PO o al AI Engineer dónde está el código a probar)")
    parts.append("\n\n---\n## RUTAS DE CÓDIGO (detectadas por búsqueda)\n" + "\n".join(lines))
    return "".join(parts)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", []))
                + build_context(feature),
                expected_output=("Informe de QA y seguridad en Markdown con: (1) plan de pruebas por AC con ID, "
                                 "técnica ISTQB (EP/BVA/DT/ST/EG), entrada, resultado esperado, prioridad y estado, "
                                 "con matriz de trazabilidad AC <-> caso; (2) código de los tests con el ID del "
                                 "caso en el nombre; (3) tabla de evidencia (HU, AC, test ID, comando, "
                                 "resultado, o «NO EJECUTADO»); (4) hallazgos de seguridad SEC-01..SEC-09 y "
                                 "bugs en formato BUG-xx; (5) decisiones HITL pendientes en el formato "
                                 "DECISIÓN REQUERIDA; (6) estado por HU (COMPLETA/PARCIAL/NO HECHA), "
                                 "discrepancias entre el spec y el discovery, y trade-offs."),
                agent=agent)
