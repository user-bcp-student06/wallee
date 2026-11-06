"""QA & Security agent: contract, searched (never assumed) context and ISTQB test-design rules."""

from pathlib import Path
import tempfile
import unittest

from agents import qa_security
from crew.workflow import workflow_steps

FEATURE = {
    "title": "Payment idempotency protection",
    "description": "Repeated requests with the same key return the original result",
    "acceptance_criteria": ["W4-AC2 same key returns the original result"],
}


def write(root: Path, rel: str, text: str) -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


class QaSecurityContractTests(unittest.TestCase):
    def test_workflow_contract_is_unchanged(self):
        step = next(s for s in workflow_steps() if s[0] == "qa_security")
        self.assertEqual(step[1:], ("QA & Security", qa_security.agent, "qa_security_report.md", True))

    def test_instructions_keep_honesty_hitl_and_path_rules(self):
        text = qa_security.INSTRUCTIONS
        for expected in ("NO EJECUTADO", "SPEC PRINCIPAL", "DISCOVERY", "DECISIÓN REQUERIDA", "PROPUESTO",
                         "Wx-ACn-Tm", "nunca asumas dónde está", "AMBIGUO"):
            self.assertIn(expected, text)

    def test_instructions_apply_istqb_black_box_techniques(self):
        text = qa_security.INSTRUCTIONS
        for expected in ("ISTQB", "EP (partición de equivalencia)", "BVA (valores límite", "DT (tabla de decisión)",
                         "ST (transición de estados)", "EG (adivinar errores", "NO exhaustivo",
                         "499.99 / 500.00 / 500.01", "trazabilidad bidireccional",
                         "Alcance del sprint: descúbrelo", "FUERA DEL ALCANCE DEL SPRINT"):
            self.assertIn(expected, text)

    def test_instructions_are_autonomous_and_say_whom_to_ask(self):
        text = qa_security.INSTRUCTIONS
        for expected in ("Autonomía primero", "Pregunta SOLO ante una duda real", "NO te detengas",
                         "DECISIONES REQUERIDAS", "A quién preguntar", "Product Owner humano", "Architect"):
            self.assertIn(expected, text)

    def test_instructions_read_openspec_as_the_primary_spec(self):
        text = qa_security.INSTRUCTIONS
        for expected in ("openspec/changes/<cambio>/", "Scenario", "tasks.md", "Fuera de alcance", "archive"):
            self.assertIn(expected, text)

    def test_task_embeds_spec_discovery_and_paths(self):
        task = qa_security.build_task(FEATURE)
        self.assertIs(task.agent, qa_security.agent)
        for section in ("## SPEC PRINCIPAL", "## DISCOVERY (secundaria", "## RUTAS DE CÓDIGO"):
            self.assertIn(section, task.description)
        self.assertIn("challenge/docs/discovery/06-handoff-por-rol/qa-security.md", task.description)
        self.assertIn("NO EJECUTADO", task.expected_output)
        self.assertIn("BVA", task.expected_output)


class QaSecurityContextTests(unittest.TestCase):
    def test_spec_is_found_wherever_it_is_and_cited_with_its_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "docs/otra/product_owner_report.md", "---\nid: x\n---\nCA-1 spec del PO")
            write(root, "output/specs/qa_security_report.md", "INFORME PROPIO")
            context = qa_security.build_context(FEATURE, root)
        self.assertIn("### docs/otra/product_owner_report.md", context)
        self.assertIn("CA-1 spec del PO", context)
        self.assertNotIn("id: x", context)
        self.assertNotIn("INFORME PROPIO", context)
        self.assertNotIn("SPEC PRINCIPAL NO ENCONTRADO", context)

    def test_missing_spec_is_not_assumed_and_asks(self):
        with tempfile.TemporaryDirectory() as tmp:
            context = qa_security.build_context(FEATURE, Path(tmp))
        self.assertIn("SPEC PRINCIPAL NO ENCONTRADO", context)
        self.assertIn("DISCOVERY NO ENCONTRADO", context)
        self.assertIn("DECISIÓN REQUERIDA", context)
        self.assertIn("backend-nestjs: NO ENCONTRADA", context)

    def test_duplicate_spec_locations_are_ambiguous(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "output/specs/product_owner_report.md", "version A")
            write(root, "copia/product_owner_report.md", "version B")
            context = qa_security.build_context(FEATURE, root)
        self.assertIn("product_owner_report.md AMBIGUO", context)
        self.assertNotIn("version A", context)
        self.assertNotIn("version B", context)

    def test_discovery_and_code_dirs_are_searched(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            base = "algun/lugar/discovery"
            write(root, base + "/06-handoff-por-rol/qa-security.md", "HANDOFF QA")
            write(root, base + "/02-producto/historias/W4-idempotencia.md", "HISTORIA W4 T2")
            write(root, "output/backend-nestjs/package.json", "{}")
            write(root, "node_modules/backend-nestjs/x.md", "ignorado")
            context = qa_security.build_context(FEATURE, root)
        self.assertIn("### algun/lugar/discovery/06-handoff-por-rol/qa-security.md", context)
        self.assertIn("HISTORIA W4 T2", context)
        self.assertIn("historias del alcance: W4", context)
        self.assertIn("- backend-nestjs: output/backend-nestjs", context)
        self.assertIn("frontend-react: NO ENCONTRADA", context)

    def test_two_discovery_folders_are_ambiguous(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "a/06-handoff-por-rol/qa-security.md", "A")
            write(root, "b/06-handoff-por-rol/qa-security.md", "B")
            context = qa_security.build_context(FEATURE, root)
        self.assertIn("DISCOVERY AMBIGUO", context)

    def test_real_repository_context(self):
        context = qa_security.build_context(FEATURE)
        self.assertIn("challenge/docs/discovery/06-handoff-por-rol/qa-security.md", context)
        self.assertIn("W4-AC2-T2", context)
        self.assertIn("RN-01", context)

    def test_long_documents_are_truncated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "output/specs/architect_report.md", "x" * (qa_security.SPEC_CHARS * 2))
            context = qa_security.build_context(FEATURE, root)
        self.assertIn("(truncado)", context)
        self.assertLess(len(context), qa_security.SPEC_CHARS + 2500)

    def test_story_scope_comes_from_the_spec_first(self):
        known = {"W1": Path("W1-x.md"), "W2": Path("W2-x.md"), "W4": Path("W4-x.md")}
        stories, origin = qa_security.scope(FEATURE, "Criterios W1-AC1 y W2-AC2 del sprint", known)
        self.assertEqual((stories, origin), (["W1", "W2"], "spec"))

    def test_scope_uses_any_hu_prefix_found_in_the_spec(self):
        stories, origin = qa_security.scope({"title": "x"}, "H7-AC1 y H8-AC3", {})
        self.assertEqual((stories, origin), (["H7", "H8"], "spec"))

    def test_scope_falls_back_to_feature_then_keywords_then_none(self):
        known = {"W1": Path("a"), "W4": Path("b")}
        self.assertEqual(qa_security.scope({"title": "W1 alta"}, "", known), (["W1"], "feature"))
        stories, origin = qa_security.scope({"title": "Payment idempotency protection"}, "", known)
        self.assertEqual(stories, ["W4"])
        self.assertIn("heurística", origin)
        self.assertEqual(qa_security.scope({"title": "Transfer funds"}, "", known), ([], "ninguna"))

    def test_spec_with_one_story_leaves_the_rest_out_of_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "output/specs/product_owner_report.md", "Alcance del sprint: W2-AC1, W2-AC2")
            base = "challenge/docs/discovery"
            write(root, base + "/06-handoff-por-rol/qa-security.md", "HANDOFF")
            write(root, base + "/02-producto/historias/W2-pago-contacto.md", "TEXTO HISTORIA W2")
            write(root, base + "/02-producto/historias/W4-idempotencia.md", "TEXTO HISTORIA W4")
            context = qa_security.build_context({"title": "Payment idempotency protection"}, root)
        self.assertIn("HU del sprint a probar: W2 (origen: spec)", context)
        self.assertIn("Fuera del alcance del sprint (no probar): W4", context)
        self.assertIn("TEXTO HISTORIA W2", context)
        self.assertNotIn("TEXTO HISTORIA W4", context)

    def test_undetermined_scope_asks_the_po(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "challenge/docs/discovery/06-handoff-por-rol/qa-security.md", "HANDOFF")
            write(root, "challenge/docs/discovery/02-producto/historias/W1-onboarding.md", "H1")
            context = qa_security.build_context({"title": "Transfer funds"}, root)
        self.assertIn("NO DETERMINADAS", context)
        self.assertIn("DECISIÓN REQUERIDA", context)

    def test_mention_without_ac_does_not_pull_a_story_into_the_sprint(self):
        known = {"W1": Path("a"), "W2": Path("b")}
        stories, _ = qa_security.scope({"title": "x"}, "W2 depende de W1. Cubre W1-AC1 y W1-AC2.", known)
        self.assertEqual(stories, ["W1"])


def openspec_fixture(root: Path) -> None:
    base = "openspec"
    write(root, base + "/config.yaml", "schema: spec-driven")
    write(root, base + "/changes/w2-pago/proposal.md", "Cubre W2-AC1 y W2-AC2. W4 depende de W2.\n\nFuera de alcance: KPI")
    write(root, base + "/changes/w2-pago/specs/pago/spec.md",
          "### Requirement: Monto maximo\nX\n\n#### Scenario: Monto 500\n- **WHEN** a\n- **THEN** b\n"
          "#### Scenario: Monto 501\n- **WHEN** c\n- **THEN** d\n")
    write(root, base + "/changes/w2-pago/tasks.md", "- [x] 1.1 hecha\n- [ ] 1.2 pendiente (W2-AC1-T1)\n- [ ] 1.3 otra")
    write(root, base + "/changes/w2-pago/design.md", "DISENO W2")
    write(root, base + "/changes/archive/w1-viejo/proposal.md", "CAMBIO ARCHIVADO W1-AC1")
    write(root, base + "/specs/onboarding/spec.md", "SPEC VIGENTE ONBOARDING")
    discovery = "challenge/docs/discovery"
    write(root, discovery + "/06-handoff-por-rol/qa-security.md", "HANDOFF")
    for story in ("W1-onboarding", "W2-pago", "W4-idempotencia"):
        write(root, discovery + "/02-producto/historias/" + story + ".md", "HISTORIA " + story[:2])


class QaSecurityOpenSpecTests(unittest.TestCase):
    def test_active_changes_are_the_primary_spec_and_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            openspec_fixture(root)
            context = qa_security.build_context(FEATURE, root)
        self.assertIn("### openspec/changes/w2-pago/proposal.md", context)
        self.assertIn("### openspec/changes/w2-pago/specs/pago/spec.md", context)
        self.assertIn("### openspec/changes/w2-pago/tasks.md", context)
        self.assertIn("DISENO W2", context)
        self.assertIn("HU del sprint a probar: W2 (origen: OpenSpec: cambios activos)", context)
        self.assertIn("1 requirements, 2 scenarios, tareas 1 hechas / 2 pendientes", context)
        self.assertIn("HISTORIA W2", context)
        self.assertNotIn("HISTORIA W4", context)
        self.assertIn("Fuera del alcance del sprint (no probar): W1, W4", context)

    def test_archived_changes_are_only_listed_for_minimal_regression(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            openspec_fixture(root)
            context = qa_security.build_context(FEATURE, root)
        self.assertIn("Cambios archivados (sprints cerrados, solo regresión mínima): w1-viejo", context)
        self.assertNotIn("CAMBIO ARCHIVADO", context)
        self.assertIn("SPEC VIGENTE ONBOARDING", context)
        self.assertIn("spec vigente, solo regresión mínima", context)

    def test_new_active_change_extends_the_scope_sprint_by_sprint(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            openspec_fixture(root)
            write(root, "openspec/changes/w4-idem/proposal.md", "Cubre W4-AC1 a W4-AC3")
            context = qa_security.build_context(FEATURE, root)
        self.assertIn("HU del sprint a probar: W2, W4 (origen: OpenSpec", context)
        self.assertIn("Cambio activo `w4-idem`", context)

    def test_openspec_without_active_changes_asks_the_po(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "openspec/config.yaml", "schema: spec-driven")
            write(root, "openspec/changes/archive/w1/proposal.md", "viejo")
            context = qa_security.build_context({"title": "Transfer funds"}, root)
        self.assertIn("OpenSpec no tiene cambios activos", context)
        self.assertIn("SPEC PRINCIPAL NO ENCONTRADO", context)

    def test_two_openspec_folders_are_ambiguous(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "a/openspec/config.yaml", "x")
            write(root, "b/openspec/config.yaml", "y")
            context = qa_security.build_context(FEATURE, root)
        self.assertIn("OPENSPEC AMBIGUO", context)

    def test_unrelated_openspec_named_folder_is_ignored(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write(root, "docs/openspec/notas.md", "no es un workspace de OpenSpec")
            context = qa_security.build_context(FEATURE, root)
        self.assertNotIn("OPENSPEC AMBIGUO", context)
        self.assertNotIn("notas.md", context)

    def test_real_repository_reads_the_openspec_change(self):
        context = qa_security.build_context(FEATURE)
        self.assertIn("### openspec/changes/w1-onboarding-guiado/tasks.md", context)
        self.assertIn("origen: OpenSpec: cambios activos", context)


if __name__ == "__main__":
    unittest.main()
