#!/usr/bin/env python3
"""Static quality checks for the machine-learning portfolio."""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


REPO = Path(__file__).resolve().parents[1]
SUPERVISED = REPO / "Supervised Learning Projects"
EXPECTED_PROJECTS = 29

HANDSHAKE_IMAGE_URL = "https://github.com/JayantGoel001/JayantGoel001/blob/master/GIF/Handshake.gif"
LOCKED_CONNECT_BLOCK = f'''## Let's Connect <img src="{HANDSHAKE_IMAGE_URL}" height="30px" style="max-width:100%;">

<div align="center">

<a href="https://www.linkedin.com/in/tajamulkhann/">
<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white">
</a>
<a href="https://www.instagram.com/tajamul.codes/" target="_blank">
<img src="https://img.shields.io/badge/Instagram-%23E4405F.svg?style=for-the-badge&logo=instagram&logoColor=white">
</a>
<a href="https://topmate.io/tajamulkhan" target="_blank">
<img src="https://img.shields.io/badge/Topmate-FF0000?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIj48Y2lyY2xlIGN4PSI1MCIgY3k9IjUwIiByPSI0MCIgZmlsbD0id2hpdGUiLz48L3N2Zz4=&logoColor=white">
</a>
<a href="https://www.whatsapp.com/channel/0029VaYs05jJkK7JKCesw42f">
<img src="https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white">
</a>
<a href="https://t.me/tajamul_khan">
<img src="https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white">
</a>
<a href="https://substack.com/@tajamulkhan">
<img src="https://img.shields.io/badge/Substack-%23006f5c.svg?style=for-the-badge&logo=substack&logoColor=FF6719">
</a>
<a href="https://www.kaggle.com/tajamulkhan">
<img src="https://img.shields.io/badge/Kaggle-035a7d?style=for-the-badge&logo=kaggle&logoColor=white">
</a>
<a href="https://github.com/tajamulkhann">
<img src="https://img.shields.io/badge/Github-12100E?style=for-the-badge&logo=github&logoColor=white">
</a>
<a href="https://medium.com/@tajamulkhan">
<img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white">
</a>
<a href="https://www.youtube.com">
<img src="https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white">
</a>
</div>'''

FORBIDDEN_TEXT = {
    "unrelated branding": re.compile(r"JayantGoel|tajamul\.datascientist", re.I),
    "machine-specific path": re.compile(r"/content/|/kaggle/input/|/Users/|[A-Za-z]:\\\\"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
}

REQUIRED_README_HEADINGS = {
    "## Overview",
    "## Problem statement",
    "## Dataset",
    "## Project workflow",
    "## Evaluation",
    "## Verified results",
    "## How to run",
    "## Author",
}


def fail(issues: list[str], message: str) -> None:
    issues.append(message)


def scan_text(path: Path, text: str, issues: list[str]) -> None:
    # The locked connect block intentionally sources its handshake GIF from this URL.
    text = text.replace(HANDSHAKE_IMAGE_URL, "")
    for label, pattern in FORBIDDEN_TEXT.items():
        if pattern.search(text):
            fail(issues, f"{path.relative_to(REPO)}: contains {label}")


def validate_locked_connect_blocks(issues: list[str]) -> None:
    readmes = sorted(REPO.rglob("README.md"))
    for readme in readmes:
        text = readme.read_text(encoding="utf-8")
        occurrences = text.count(LOCKED_CONNECT_BLOCK)
        if occurrences != 1:
            fail(
                issues,
                f"{readme.relative_to(REPO)}: expected one exact locked Let's Connect block; found {occurrences}",
            )


def validate_notebook(path: Path, issues: list[str]) -> None:
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(issues, f"{path.relative_to(REPO)}: invalid notebook JSON ({error})")
        return

    if notebook.get("nbformat") != 4:
        fail(issues, f"{path.relative_to(REPO)}: expected nbformat 4")

    cells = notebook.get("cells", [])
    if not cells or cells[0].get("cell_type") != "markdown":
        fail(issues, f"{path.relative_to(REPO)}: missing opening project markdown")

    code_count = markdown_count = 0
    for index, cell in enumerate(cells):
        source = "".join(cell.get("source", []))
        scan_text(path, source, issues)
        if cell.get("cell_type") == "code":
            code_count += 1
            if cell.get("outputs"):
                fail(issues, f"{path.relative_to(REPO)}: cell {index} contains stored output")
            try:
                ast.parse(source, filename=f"{path}:cell-{index}")
            except SyntaxError as error:
                fail(issues, f"{path.relative_to(REPO)}: cell {index} does not compile ({error})")
        elif cell.get("cell_type") == "markdown":
            markdown_count += 1

    if code_count < 5 or markdown_count < 5:
        fail(issues, f"{path.relative_to(REPO)}: notebook is too sparse ({code_count} code, {markdown_count} markdown)")


def validate_readme(path: Path, issues: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    scan_text(path, text, issues)
    headings = set(re.findall(r"(?m)^## .+$", text))
    missing = sorted(REQUIRED_README_HEADINGS - headings)
    if missing:
        fail(issues, f"{path.relative_to(REPO)}: missing headings {missing}")
    for credential in ["Tajamul Khan", "github.com/tajamulkhann", "linkedin.com/in/tajamulkhann/", "@tajamul.codes"]:
        if credential not in text:
            fail(issues, f"{path.relative_to(REPO)}: missing author credential {credential!r}")


def validate_markdown_links(path: Path, issues: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for raw_target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        target = raw_target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        local = (path.parent / unquote(target)).resolve()
        try:
            local.relative_to(REPO)
        except ValueError:
            fail(issues, f"{path.relative_to(REPO)}: link escapes the repository ({raw_target})")
            continue
        if not local.exists():
            fail(issues, f"{path.relative_to(REPO)}: broken local link {raw_target}")


def validate_index_links(issues: list[str]) -> None:
    index = (SUPERVISED / "README.md").read_text(encoding="utf-8")
    links = re.findall(r"\[[^]]+\]\(([^)]+/)\)", index)
    for link in links:
        if link.startswith(("http://", "https://")):
            continue
        target = SUPERVISED / unquote(link.rstrip("/"))
        if not target.is_dir():
            fail(issues, f"Supervised Learning Projects/README.md: broken directory link {link}")


def main() -> int:
    issues: list[str] = []
    if not SUPERVISED.is_dir():
        print("Supervised Learning Projects directory is missing", file=sys.stderr)
        return 1

    projects = sorted(path for path in SUPERVISED.iterdir() if path.is_dir())
    if len(projects) != EXPECTED_PROJECTS:
        fail(issues, f"Expected {EXPECTED_PROJECTS} project directories; found {len(projects)}")

    for project in projects:
        notebooks = list(project.glob("*.ipynb"))
        if len(notebooks) != 1:
            fail(issues, f"{project.relative_to(REPO)}: expected one canonical notebook; found {len(notebooks)}")
        else:
            validate_notebook(notebooks[0], issues)
        readme = project / "README.md"
        if not readme.exists():
            fail(issues, f"{project.relative_to(REPO)}: README.md is missing")
        else:
            validate_readme(readme, issues)
            validate_markdown_links(readme, issues)

    obsolete = []
    for path in SUPERVISED.rglob("*"):
        if path.is_file() and (
            path.name in {".DS_Store", ".gitignore"}
            or path.suffix.lower() in {".pdf"}
            or "rough" in path.name.lower()
        ):
            obsolete.append(str(path.relative_to(REPO)))
    if obsolete:
        fail(issues, f"Obsolete generated or temporary files remain: {obsolete}")

    validate_index_links(issues)
    validate_locked_connect_blocks(issues)
    validate_markdown_links(SUPERVISED / "README.md", issues)
    validate_markdown_links(REPO / "README.md", issues)
    scan_text(REPO / "README.md", (REPO / "README.md").read_text(encoding="utf-8"), issues)

    if issues:
        print("Portfolio validation failed:", file=sys.stderr)
        for issue in issues:
            print(f"- {issue}", file=sys.stderr)
        return 1

    print(f"Portfolio validation passed: {len(projects)} projects, {len(projects)} notebooks, {len(projects)} project READMEs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
