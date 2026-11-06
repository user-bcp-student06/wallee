"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'qa_security'
LABEL = 'QA & Security'
SPEC_FILE = 'qa_security_report.md'
EXTRACT_CODE = True

INSTRUCTIONS = "Realiza la tarea de tu rol."
agent = Agent(role='QA & Security', goal="Completar la tarea asignada.",
              backstory="Eres un integrante del equipo.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output='Un informe de QA y seguridad.', agent=agent)
