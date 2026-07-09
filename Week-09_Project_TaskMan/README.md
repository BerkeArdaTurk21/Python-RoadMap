# Week 09 — Project 1: Task Manager CLI (`taskman`)

> **Level:** Project (applies Weeks 1–8)
> **Goal:** Build a complete, stdlib-only task manager for the terminal — the first portfolio project of the roadmap.

A real to-do CLI with subcommands, JSON persistence, due dates, priorities,
tags, search and colored table output. **Zero external dependencies** —
pytest is used only for the test suite.

---

## Quick Start

```bash
cd Week-09_Project_TaskMan
python -m taskman --help
```

```bash
# Add tasks
python -m taskman add "Buy milk" -p high -t home,errands
python -m taskman add "Ship the report" --due tomorrow
python -m taskman add "Water plants" -d +3 -t garden

# See what's open
python -m taskman list
```

```
ID  ✔  Title            Priority  Due         Tags
──────────────────────────────────────────────────────────
1      Buy milk         high      -           home, errands
2      Ship the report  medium    2026-07-10  -
3      Water plants     medium    2026-07-12  garden
```

```bash
# Work through the day
python -m taskman done 1
python -m taskman list --all          # include completed tasks
python -m taskman list --overdue      # what did I miss?
python -m taskman list -s priority    # most urgent first
python -m taskman search milk         # find by title or tag
python -m taskman delete 3
```

## Commands

| Command | Example | Notes |
|---------|---------|-------|
| `add` | `add "Title" -p high -d tomorrow -t home,urgent` | priority: low/medium/high · due: `YYYY-MM-DD`, `today`, `tomorrow`, `+N` |
| `list` | `list -a` / `list --done` / `list --overdue` / `list -p high` / `list -t home` / `list -s due` | shows open tasks by default |
| `done` | `done 2` | records completion time |
| `delete` | `delete 2` | permanent |
| `search` | `search report` | case-insensitive, titles + tags |

Tasks are stored in `tasks.json` — override with the global flag placed
before the command: `python -m taskman --file work.json list`.
Overdue tasks show in red, completed tasks are dimmed, priorities are
color-coded. Colors switch off automatically when piping (`NO_COLOR` also respected).

## Running the Tests

```bash
pip install pytest
pytest -v          # 21 tests: validators, parser, model, storage, end-to-end
```

## Project Structure

```
Week-09_Project_TaskMan/
├── README.md            ← you are here
├── SPEC.md              ← design document (commands, data model, storage rules)
├── conftest.py          ← makes `taskman` importable for pytest
├── taskman/
│   ├── __init__.py      ← package version
│   ├── __main__.py      ← python -m taskman entry point
│   ├── models.py        ← Task dataclass (roundtrip, overdue, search)
│   ├── storage.py       ← JSON load/save, atomic writes, lock file
│   ├── cli.py           ← argparse subcommands + command handlers
│   └── display.py       ← ANSI colors + aligned tables, no dependencies
└── tests/
    └── test_taskman.py  ← pytest suite
```

## Skills From the Roadmap Used Here

| Week | Applied as |
|------|-----------|
| 3 — Functions | validator callables for argparse `type=` |
| 5 — OOP | `Task` dataclass with behavior (`is_overdue`, `matches`) |
| 6 — Files & Errors | JSON persistence, custom `StorageError`, atomic writes |
| 7 — Modules | package layout, `__main__`, argparse subparsers, datetime |
| 8 — Advanced | context manager lock file, type hints everywhere, pytest suite |
