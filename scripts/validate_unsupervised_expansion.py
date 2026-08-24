#!/usr/bin/env python3
"""Validate the selective 30-project unsupervised-learning portfolio."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.dont_write_bytecode = True

from build_unsupervised_expansion import CONNECT, KEPT_CODE, NEW_PROJECTS, REFURBISHED_CODE


ROOT = Path(__file__).resolve().parents[1]
UNSUPERVISED = ROOT / "Unsupervised Learning Projects"
EXPECTED_PROJECTS = 30
EXPECTED_NEW = 25


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")


def project_directories() -> list[Path]:
    projects = sorted(path for path in UNSUPERVISED.iterdir() if path.is_dir())
    if len(projects) != EXPECTED_PROJECTS:
        fail(f"expected {EXPECTED_PROJECTS} project directories, found {len(projects)}")
    for project in projects:
        notebooks = list(project.glob("*.ipynb"))
        if len(notebooks) != 1:
            fail(f"{project.name}: expected exactly one canonical notebook, found {len(notebooks)}")
        if not (project / "README.md").is_file():
            fail(f"{project.name}: README.md is missing")
    return projects


def validate_audit_definition(projects: list[Path]) -> None:
    new_titles = {cfg["title"] for cfg in NEW_PROJECTS}
    if len(NEW_PROJECTS) != EXPECTED_NEW or len(new_titles) != EXPECTED_NEW:
        fail(f"expected {EXPECTED_NEW} unique new project definitions")
    if len(KEPT_CODE) != 2 or len(REFURBISHED_CODE) != 3:
        fail("audit must remain 2 maintained + 3 refurbished existing projects")
    expected = new_titles | KEPT_CODE | REFURBISHED_CODE
    actual = {project.name for project in projects}
    if expected != actual:
        fail(f"project directory set differs from audit definition: missing={sorted(expected-actual)}, extra={sorted(actual-expected)}")


def validate_notebooks(projects: list[Path]) -> None:
    changed_or_new = {cfg["title"] for cfg in NEW_PROJECTS} | REFURBISHED_CODE
    for project in projects:
        notebook_path = next(project.glob("*.ipynb"))
        try:
            document = json.loads(notebook_path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"{notebook_path}: invalid notebook JSON ({exc})")
        if document.get("nbformat") != 4:
            fail(f"{notebook_path}: unsupported notebook format")
        code_cells = [cell for cell in document.get("cells", []) if cell.get("cell_type") == "code"]
        if not code_cells:
            fail(f"{notebook_path}: notebook contains no code")
        outputs = [output for cell in code_cells for output in cell.get("outputs", [])]
        if not outputs:
            fail(f"{notebook_path}: notebook contains no saved outputs")
        errors = [output for output in outputs if output.get("output_type") == "error"]
        if errors:
            fail(f"{notebook_path}: contains {len(errors)} stored execution error(s)")
        if project.name in changed_or_new:
            execution = document.get("metadata", {}).get("execution", {})
            if execution.get("status") != "completed" or not execution.get("outputs_preserved"):
                fail(f"{notebook_path}: changed/new notebook lacks completed execution metadata")
            if any(cell.get("execution_count") is None for cell in code_cells):
                fail(f"{notebook_path}: changed/new notebook contains unexecuted code cells")


def validate_branding() -> None:
    readmes = sorted(path for path in ROOT.rglob("README.md") if path.is_file())
    expected = 1 + 51 + 31  # root + supervised index/projects + unsupervised index/projects
    if len(readmes) != expected:
        fail(f"expected {expected} repository READMEs, found {len(readmes)}")
    locked = CONNECT.rstrip()
    for readme in readmes:
        text = readme.read_text(encoding="utf-8", errors="replace")
        if text.count(locked) != 1:
            fail(f"{readme}: exact locked Let's Connect block is missing or duplicated")
        if "tajamul.datascientist" in text:
            fail(f"{readme}: contains the retired Instagram handle")
    root_text = (ROOT / "README.md").read_text(encoding="utf-8")
    if "| Unsupervised Learning | 30 |" not in root_text:
        fail("root README does not report 30 unsupervised projects")


def validate_index() -> None:
    index = (UNSUPERVISED / "README.md").read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^)]+/)\)", index)
    local_links = [link for link in links if not link.startswith(("http://", "https://"))]
    if len(local_links) != EXPECTED_PROJECTS:
        fail(f"unsupervised index should contain {EXPECTED_PROJECTS} project links, found {len(local_links)}")
    for link in local_links:
        target = UNSUPERVISED / unquote(link.rstrip("/"))
        if not target.is_dir():
            fail(f"broken project index link: {link}")
    if not (UNSUPERVISED / "AUDIT.md").is_file():
        fail("AUDIT.md is missing")


def validate_hygiene() -> None:
    forbidden_names = {"add.ipynb", ".ipynb_checkpoints"}
    for path in UNSUPERVISED.rglob("*"):
        if path.name in forbidden_names:
            fail(f"stale or duplicate artifact remains: {path}")

    secret_patterns = [
        re.compile(r"ghp_[A-Za-z0-9]{30,}"),
        re.compile(r"sk-(?:proj-)?[A-Za-z0-9]{20,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    foreign_markers = ["tajamulk2", "FaeyO", "foyinbo250@gmail.com"]
    scannable = {".md", ".py", ".ipynb", ".txt", ".json", ".code-workspace"}
    for path in [item for item in UNSUPERVISED.rglob("*") if item.is_file() and item.suffix.lower() in scannable]:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(pattern.search(text) for pattern in secret_patterns):
            fail(f"potential credential found in {path}")
        if any(marker in text for marker in foreign_markers):
            fail(f"legacy or third-party creator credential found in {path}")


def main() -> None:
    projects = project_directories()
    validate_audit_definition(projects)
    validate_notebooks(projects)
    validate_branding()
    validate_index()
    validate_hygiene()
    print("Validation passed: 2 maintained + 3 refurbished + 25 new = 30 unsupervised projects.")
    print("All 30 notebooks contain saved outputs; all 28 changed/new notebooks executed successfully.")


if __name__ == "__main__":
    main()
