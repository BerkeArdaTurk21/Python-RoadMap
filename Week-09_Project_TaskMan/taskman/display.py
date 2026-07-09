"""ANSI color output and pretty tables — no external dependencies."""

import os
import sys

from taskman.models import Task

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

PRIORITY_COLOR = {"high": RED, "medium": YELLOW, "low": GREEN}

if os.name == "nt":
    os.system("")   # enables ANSI escape processing in the classic Windows console


def use_color() -> bool:
    """Respect pipes and the NO_COLOR convention (https://no-color.org)."""
    return sys.stdout.isatty() and "NO_COLOR" not in os.environ


def paint(text: str, *codes: str) -> str:
    if not codes or not use_color():
        return text
    return "".join(codes) + text + RESET


def error(message: str) -> None:
    print(paint(f"error: {message}", RED, BOLD), file=sys.stderr)


def info(message: str) -> None:
    print(paint(message, CYAN))


def _row(task: Task) -> list[str]:
    return [
        str(task.id),
        "✔" if task.done else " ",
        task.title,
        task.priority,
        task.due or "-",
        ", ".join(task.tags) or "-",
    ]


def format_table(tasks: list[Task]) -> str:
    """Aligned columns sized to the widest cell — plain string, colors applied last."""
    headers = ["ID", "✔", "Title", "Priority", "Due", "Tags"]
    rows = [_row(t) for t in tasks]
    widths = [
        max(len(headers[col]), *(len(r[col]) for r in rows)) if rows else len(headers[col])
        for col in range(len(headers))
    ]

    def pad(cells: list[str]) -> list[str]:
        return [cell.ljust(widths[i]) for i, cell in enumerate(cells)]

    lines = [
        paint("  ".join(pad(headers)), BOLD),
        paint("─" * (sum(widths) + 2 * (len(widths) - 1)), DIM),
    ]
    for task, cells in zip(tasks, rows):
        padded = pad(cells)
        if task.done:
            line = paint("  ".join(padded), DIM)
        elif task.is_overdue():
            line = paint("  ".join(padded), RED)
        else:
            padded[3] = paint(padded[3], PRIORITY_COLOR[task.priority])
            line = "  ".join(padded)
        lines.append(line)
    return "\n".join(lines)
