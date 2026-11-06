"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'product_owner'
LABEL = 'Product Owner'
SPEC_FILE = 'product_owner_report.md'
EXTRACT_CODE = False

INSTRUCTIONS = "Realiza la tarea de tu rol."
agent = Agent(role='Product Owner', goal="Completar la tarea asignada.",
              backstory="Eres un integrante del equipo.", llm=llm,
              verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output='Un informe del Product Owner.', agent=agent)
