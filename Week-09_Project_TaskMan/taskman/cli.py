"""argparse CLI for taskman — subcommands, validation, command handlers."""

import argparse
from datetime import date, timedelta
from pathlib import Path

from taskman import __version__
from taskman.models import PRIORITIES, PRIORITY_RANK, Task
from taskman.storage import (
    DEFAULT_FILE,
    StorageError,
    file_lock,
    load_tasks,
    next_id,
    save_tasks,
)
from taskman import display

# ─── Argument validators (argparse `type=` callables) ─────────────────────────

def parse_due(value: str) -> str:
    """Accept YYYY-MM-DD, 'today', 'tomorrow' or '+N' (N days from today)."""
    value = value.strip().lower()
    if value == "today":
        return date.today().isoformat()
    if value == "tomorrow":
        return (date.today() + timedelta(days=1)).isoformat()
    if value.startswith("+") and value[1:].isdigit():
        return (date.today() + timedelta(days=int(value[1:]))).isoformat()
    try:
        return date.fromisoformat(value).isoformat()
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"invalid due date {value!r} — use YYYY-MM-DD, 'today', 'tomorrow' or '+N'"
        )


def positive_int(value: str) -> int:
    try:
        n = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value!r} is not a number")
    if n <= 0:
        raise argparse.ArgumentTypeError("task id must be a positive integer")
    return n


def tag_list(value: str) -> list[str]:
    """'home,urgent, errands' → ['home', 'urgent', 'errands']"""
    return [t.strip() for t in value.split(",") if t.strip()]


# ─── Parser ────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="taskman",
        description="A simple task manager for your terminal.",
        epilog="Run 'taskman <command> -h' for help on a specific command.",
    )
    parser.add_argument("--version", action="version", version=f"taskman {__version__}")
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_FILE,
        help=f"task file to use (default: {DEFAULT_FILE})",
    )
    sub = parser.add_subparsers(dest="command", metavar="command")

    p_add = sub.add_parser("add", help="add a new task")
    p_add.add_argument("title", nargs="+", help="task title")
    p_add.add_argument("-p", "--priority", choices=PRIORITIES, default="medium")
    p_add.add_argument("-d", "--due", type=parse_due, default=None,
                       help="YYYY-MM-DD, 'today', 'tomorrow' or '+N' days")
    p_add.add_argument("-t", "--tags", type=tag_list, default=[],
                       help="comma-separated tags, e.g. home,urgent")

    p_list = sub.add_parser("list", help="list tasks (open tasks by default)")
    p_list.add_argument("-a", "--all", action="store_true", help="include done tasks")
    p_list.add_argument("--done", action="store_true", help="only done tasks")
    p_list.add_argument("-p", "--priority", choices=PRIORITIES, help="filter by priority")
    p_list.add_argument("-t", "--tag", help="filter by tag")
    p_list.add_argument("--overdue", action="store_true", help="only overdue tasks")
    p_list.add_argument("-s", "--sort", choices=("id", "due", "priority"), default="id")

    p_done = sub.add_parser("done", help="mark a task as done")
    p_done.add_argument("id", type=positive_int)

    p_del = sub.add_parser("delete", help="delete a task")
    p_del.add_argument("id", type=positive_int)

    p_search = sub.add_parser("search", help="search titles and tags")
    p_search.add_argument("query", nargs="+", help="text to search for")

    return parser


# ─── Filtering / sorting helpers ───────────────────────────────────────────────

def apply_filters(tasks: list[Task], args: argparse.Namespace) -> list[Task]:
    if args.done:
        tasks = [t for t in tasks if t.done]
    elif not args.all:
        tasks = [t for t in tasks if not t.done]
    if args.priority:
        tasks = [t for t in tasks if t.priority == args.priority]
    if args.tag:
        tasks = [t for t in tasks if args.tag.lower() in (tag.lower() for tag in t.tags)]
    if args.overdue:
        tasks = [t for t in tasks if t.is_overdue()]
    return tasks


def sort_tasks(tasks: list[Task], key: str) -> list[Task]:
    if key == "due":
        return sorted(tasks, key=lambda t: (t.due is None, t.due or "", t.id))
    if key == "priority":
        return sorted(tasks, key=lambda t: (PRIORITY_RANK[t.priority], t.id))
    return sorted(tasks, key=lambda t: t.id)


def find_task(tasks: list[Task], task_id: int) -> Task:
    for task in tasks:
        if task.id == task_id:
            return task
    raise StorageError(f"no task with id {task_id}")


# ─── Command handlers ──────────────────────────────────────────────────────────

def cmd_add(args: argparse.Namespace) -> None:
    with file_lock(args.file):
        tasks = load_tasks(args.file)
        task = Task(
            id=next_id(tasks),
            title=" ".join(args.title),
            priority=args.priority,
            due=args.due,
            tags=args.tags,
        )
        tasks.append(task)
        save_tasks(tasks, args.file)
    display.info(f"Added task #{task.id}: {task.title}")


def cmd_list(args: argparse.Namespace) -> None:
    tasks = sort_tasks(apply_filters(load_tasks(args.file), args), args.sort)
    if not tasks:
        display.info("No tasks found. Add one with: taskman add \"My first task\"")
        return
    print(display.format_table(tasks))


def cmd_done(args: argparse.Namespace) -> None:
    with file_lock(args.file):
        tasks = load_tasks(args.file)
        task = find_task(tasks, args.id)
        if task.done:
            display.info(f"Task #{task.id} is already done.")
            return
        task.mark_done()
        save_tasks(tasks, args.file)
    display.info(f"Done ✔ #{task.id}: {task.title}")


def cmd_delete(args: argparse.Namespace) -> None:
    with file_lock(args.file):
        tasks = load_tasks(args.file)
        task = find_task(tasks, args.id)
        tasks.remove(task)
        save_tasks(tasks, args.file)
    display.info(f"Deleted #{task.id}: {task.title}")


def cmd_search(args: argparse.Namespace) -> None:
    query = " ".join(args.query)
    hits = [t for t in load_tasks(args.file) if t.matches(query)]
    if not hits:
        display.info(f"No tasks matching {query!r}.")
        return
    print(display.format_table(hits))


HANDLERS = {
    "add": cmd_add,
    "list": cmd_list,
    "done": cmd_done,
    "delete": cmd_delete,
    "search": cmd_search,
}


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        HANDLERS[args.command](args)
    except StorageError as exc:
        display.error(str(exc))
        return 1
    return 0
