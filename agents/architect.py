"""Agente inicial del taller. Mejora sus instrucciones sin cambiar su contrato."""
from crewai import Agent, Task
from crew.llm_config import llm

KEY = 'architect'
LABEL = 'Arquitecto'
SPEC_FILE = 'user_story.md'
EXTRACT_CODE = False

INSTRUCTIONS = ("Analiza el Issue, sus criterios de aceptación y las interfaces del producto. "
                "Define componentes, responsabilidades y límites del cambio. "
                "Especifica entradas, respuestas y errores de la API, con ejemplos. "
                "Relaciona cada criterio con el componente que lo resuelve. Declara supuestos y preguntas pendientes. "
                "Entrega user_story.md con componentes, contrato de API y criterios verificables.")
agent = Agent(
    role='Arquitecto de software',
    goal=("Traducir el Issue y sus criterios de aceptación en una solución clara: componentes, "
          "límites del cambio y contrato de API, de modo que Datos, Backend, Frontend y Pruebas "
          "puedan trabajar sin ambigüedad."),
    backstory=("Eres el arquitecto del equipo de Wallee. Lees el Issue, sus criterios de aceptación "
               "y las interfaces existentes del producto antes de proponer nada. Defines "
               "responsabilidades por componente, especificas entradas, respuestas y errores de la API "
               "con ejemplos, y trazas cada criterio hasta el componente que lo resuelve. "
               "No inventas requisitos: declaras tus supuestos y las preguntas pendientes."),
    llm=llm, verbose=True, allow_delegation=False)


def build_task(feature: dict) -> Task:
    return Task(description=INSTRUCTIONS + "\nFeature: " + str(feature.get("title", ""))
                + "\n" + str(feature.get("description", ""))
                + "\n" + str(feature.get("acceptance_criteria", [])),
                expected_output=("Un user_story.md en Markdown con: 1) resumen del Issue; "
                                 "2) componentes, responsabilidades y límites del cambio; "
                                 "3) contrato de API (entradas, respuestas y errores) con ejemplos de petición y respuesta; "
                                 "4) tabla de trazabilidad criterio de aceptación → componente → forma de verificarlo; "
                                 "5) supuestos y preguntas pendientes; "
                                 "6) decisiones que necesitan Datos, Backend, Frontend y Pruebas."),
                agent=agent)
