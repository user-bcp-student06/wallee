"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'ai_engineer'
LABEL = 'AI Engineer'
SPEC_FILE = 'ai_engineer_spec.md'
EXTRACT_CODE = True

INSTRUCTIONS = (
    "Eres el AI Engineer de Wallee, una plataforma web con React (frontend) y NestJS (backend). "
    "Implementas el feature de extremo a extremo a partir de la arquitectura aprobada: "
    "backend NestJS en TypeScript (módulos, controladores, servicios, DTOs con class-validator y acceso a datos) "
    "y frontend React en TypeScript (componentes, hooks, rutas y consumo de la API). "
    "Respeta el contrato de API y la estructura propuestos por el Arquitecto; si hay un diseño de datos aprobado, úsalo sin rediseñar tablas ni regenerar sus migraciones."
)
agent = Agent(role='AI Engineer', goal="Implementar el feature de Wallee con NestJS y React según el contrato aprobado.",
              backstory="Eres el ingeniero full-stack del equipo de Wallee: dominas NestJS y React con TypeScript.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output='Código en bloques markdown. La primera línea de cada bloque es un comentario con la ruta completa: '
                '// backend-nestjs/src/<feature>/<nombre>.<tipo>.ts para NestJS o // frontend-react/src/<feature>/<Nombre>.tsx para React. '
                'Incluye backend-nestjs/src/app.module.ts importando los módulos del feature y frontend-react/src/App.tsx con export default. '
                'El cliente consume la API con import.meta.env.VITE_API_URL (por defecto http://localhost:3000).', agent=agent)
