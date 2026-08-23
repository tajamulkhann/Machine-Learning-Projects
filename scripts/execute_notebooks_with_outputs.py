#!/usr/bin/env python3
"""Execute notebook code cells and persist readable outputs without Jupyter.

The workspace intentionally has no nbformat/nbclient installation. This runner
supports the portfolio's pure-Python cells, captures stdout, rich HTML/text
representations, and Matplotlib figures, and fails on the first cell error.
"""

from __future__ import annotations

import argparse
import ast
import base64
import contextlib
import io
import json
import os
import sys
import time
import traceback
from pathlib import Path

os.environ.setdefault("MPLBACKEND", "Agg")
os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib-supervised-portfolio")

import matplotlib.pyplot as plt


def output_for_object(value: object) -> dict:
    data = {"text/plain": repr(value)}
    html = getattr(value, "_repr_html_", None)
    if callable(html):
        rendered = html()
        if rendered:
            data["text/html"] = rendered
    return {"output_type": "display_data", "metadata": {}, "data": data}


def figure_output(number: int) -> dict:
    buffer = io.BytesIO()
    plt.figure(number).savefig(buffer, format="png", dpi=110, bbox_inches="tight")
    encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
    return {
        "output_type": "display_data",
        "metadata": {},
        "data": {"image/png": encoded, "text/plain": "<Figure>"},
    }


def execute_notebook(path: Path) -> tuple[int, float]:
    started = time.perf_counter()
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace: dict[str, object] = {"__name__": "__main__", "__file__": str(path)}
    execution_count = 0
    total_outputs = 0

    for cell_index, cell in enumerate(notebook.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        source = cell.get("source", "")
        if isinstance(source, list):
            source = "".join(source)
        execution_count += 1
        cell["execution_count"] = execution_count
        cell["outputs"] = []
        displays: list[dict] = []

        def display(*values: object) -> None:
            displays.extend(output_for_object(value) for value in values)

        namespace["display"] = display
        stdout = io.StringIO()
        try:
            tree = ast.parse(source, filename=f"{path}:cell-{cell_index}", mode="exec")
            final_expression = None
            if tree.body and isinstance(tree.body[-1], ast.Expr):
                final_expression = ast.Expression(tree.body.pop().value)
                ast.fix_missing_locations(final_expression)
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stdout):
                if tree.body:
                    compiled = compile(tree, f"{path}:cell-{cell_index}", "exec")
                    exec(compiled, namespace)
                if final_expression is not None:
                    value = eval(compile(final_expression, f"{path}:cell-{cell_index}", "eval"), namespace)
                    if value is not None:
                        display(value)
        except Exception as exc:
            text = stdout.getvalue()
            if text:
                cell["outputs"].append({"output_type": "stream", "name": "stdout", "text": text})
            cell["outputs"].extend(displays)
            cell["outputs"].append(
                {
                    "output_type": "error",
                    "ename": type(exc).__name__,
                    "evalue": str(exc),
                    "traceback": traceback.format_exc().splitlines(),
                }
            )
            path.write_text(json.dumps(notebook, indent=1) + "\n", encoding="utf-8")
            raise RuntimeError(f"{path}: cell {cell_index} failed: {type(exc).__name__}: {exc}") from exc

        text = stdout.getvalue()
        if text:
            cell["outputs"].append({"output_type": "stream", "name": "stdout", "text": text})
        cell["outputs"].extend(displays)
        for figure_number in list(plt.get_fignums()):
            cell["outputs"].append(figure_output(figure_number))
            plt.close(figure_number)
        total_outputs += len(cell["outputs"])

    notebook.setdefault("metadata", {})["execution"] = {
        "runner": "scripts/execute_notebooks_with_outputs.py",
        "status": "completed",
        "outputs_preserved": True,
    }
    path.write_text(json.dumps(notebook, indent=1) + "\n", encoding="utf-8")
    return total_outputs, time.perf_counter() - started


def collect_notebooks(inputs: list[str]) -> list[Path]:
    notebooks: set[Path] = set()
    for raw in inputs:
        path = Path(raw)
        if path.is_dir():
            notebooks.update(path.rglob("*.ipynb"))
        elif path.suffix == ".ipynb" and path.exists():
            notebooks.add(path)
        else:
            notebooks.update(Path().glob(raw))
    return sorted(notebooks)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Notebook files, directories, or glob patterns")
    args = parser.parse_args()
    notebooks = collect_notebooks(args.paths)
    if not notebooks:
        raise SystemExit("No notebooks matched")
    for index, path in enumerate(notebooks, start=1):
        outputs, elapsed = execute_notebook(path)
        print(f"[{index:02d}/{len(notebooks):02d}] PASS {path} | outputs={outputs} | {elapsed:.2f}s", flush=True)


if __name__ == "__main__":
    main()
