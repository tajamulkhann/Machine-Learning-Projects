#!/usr/bin/env python3
"""Validate the selective 50-project supervised-learning portfolio."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

sys.dont_write_bytecode = True

from build_supervised_expansion import (
    CLASSIFICATION_PROJECTS,
    CONNECT,
    FORECAST_PROJECTS,
    KEPT,
    REFURBISHED,
    REGRESSION_PROJECTS,
    TEXT_PROJECTS,
)


ROOT = Path(__file__).resolve().parents[1]
SUPERVISED = ROOT / "Supervised Learning Projects"
EXPECTED_PROJECTS = 50


def fail(message: str) -> None:
    raise SystemExit(f"VALIDATION FAILED: {message}")


def validate_structure() -> list[Path]:
    projects = sorted(path for path in SUPERVISED.iterdir() if path.is_dir())
    if len(projects) != EXPECTED_PROJECTS:
        fail(f"expected {EXPECTED_PROJECTS} project directories, found {len(projects)}")
    for project in projects:
        notebooks = list(project.glob("*.ipynb"))
        if len(notebooks) != 1:
            fail(f"{project.name}: expected exactly one notebook, found {len(notebooks)}")
        if not (project / "README.md").exists():
            fail(f"{project.name}: README.md is missing")
    return projects


def validate_notebooks(projects: list[Path]) -> None:
    changed = set(REFURBISHED)
    new = {
        cfg["title"]
        for cfg in TEXT_PROJECTS + CLASSIFICATION_PROJECTS + REGRESSION_PROJECTS + FORECAST_PROJECTS
    }
    if len(new) != 21:
        fail(f"expected 21 new project definitions, found {len(new)}")
    if len(KEPT) != 18 or len(changed) != 11:
        fail("audit classification must remain 18 maintained + 11 refurbished")

    for project in projects:
        notebook_path = next(project.glob("*.ipynb"))
        try:
            notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
        except Exception as exc:
            fail(f"{notebook_path}: invalid notebook JSON ({exc})")
        if notebook.get("nbformat") != 4:
            fail(f"{notebook_path}: unsupported notebook format")
        outputs = [
            output
            for cell in notebook.get("cells", [])
            if cell.get("cell_type") == "code"
            for output in cell.get("outputs", [])
        ]
        if not outputs:
            fail(f"{notebook_path}: notebook has no saved outputs")
        errors = [output for output in outputs if output.get("output_type") == "error"]
        if errors:
            fail(f"{notebook_path}: contains {len(errors)} stored execution error(s)")
        if project.name in changed | new:
            execution = notebook.get("metadata", {}).get("execution", {})
            if execution.get("status") != "completed" or not execution.get("outputs_preserved"):
                fail(f"{notebook_path}: changed/new notebook lacks completed execution metadata")


def validate_branding() -> None:
    readmes = sorted(path for path in ROOT.rglob("*") if path.is_file() and path.name.lower() == "readme.md")
    expected = EXPECTED_PROJECTS + 1 + 5 + 1 + 1  # supervised projects/index + unsupervised projects/index + root
    if len(readmes) != expected:
        fail(f"expected {expected} repository READMEs, found {len(readmes)}")
    locked = CONNECT.rstrip()
    for readme in readmes:
        text = readme.read_text(encoding="utf-8", errors="replace")
        if text.count(locked) != 1:
            fail(f"{readme}: exact locked Let's Connect block is missing or duplicated")
        if "tajamul.datascientist" in text:
            fail(f"{readme}: contains the retired Instagram handle")
    if "| Supervised Learning | 50 |" not in (ROOT / "README.md").read_text(encoding="utf-8"):
        fail("root README does not report 50 supervised projects")


def validate_index_links() -> None:
    index = (SUPERVISED / "README.md").read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^)]+/)\)", index)
    project_links = [link for link in links if not link.startswith(("http://", "https://"))]
    if len(project_links) != EXPECTED_PROJECTS:
        fail(f"supervised index should contain {EXPECTED_PROJECTS} project links, found {len(project_links)}")
    for link in project_links:
        target = SUPERVISED / unquote(link.rstrip("/"))
        if not target.is_dir():
            fail(f"broken project index link: {link}")


def validate_repository_hygiene() -> None:
    forbidden_names = {"add.ipynb", ".ipynb_checkpoints", "Bank_Telemarketing_Rough_Code.ipynb"}
    for path in SUPERVISED.rglob("*"):
        if path.name in forbidden_names:
            fail(f"stale or duplicate artifact remains: {path}")
    secret_patterns = [
        re.compile(r"ghp_[A-Za-z0-9]{30,}"),
        re.compile(r"sk-(?:proj-)?[A-Za-z0-9]{20,}"),
        re.compile(r"AKIA[0-9A-Z]{16}"),
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    ]
    for path in [ROOT / "README.md", SUPERVISED / "README.md", *SUPERVISED.rglob("*.py"), *SUPERVISED.rglob("*.ipynb")]:
        text = path.read_text(encoding="utf-8", errors="ignore")
        if any(pattern.search(text) for pattern in secret_patterns):
            fail(f"potential credential found in {path}")


def main() -> None:
    projects = validate_structure()
    validate_notebooks(projects)
    validate_branding()
    validate_index_links()
    validate_repository_hygiene()
    print("Validation passed: 18 maintained + 11 refurbished + 21 new = 50 supervised projects.")
    print("All 50 notebooks contain saved outputs; all 32 changed/new notebooks executed successfully.")


if __name__ == "__main__":
    main()
