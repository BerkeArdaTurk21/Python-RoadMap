# taskman — Specification

## Goal

A stdlib-only command-line task manager: add tasks with priorities, due dates
and tags; list, filter, search, complete and delete them. Data lives in a
human-readable JSON file.

## Non-Goals

- No GUI / web interface, no sync, no multi-user support
- No external dependencies (pytest only for the test suite)

## Commands

| Command | Arguments | Description |
|---------|-----------|-------------|
| `add` | `TITLE... [-p PRIORITY] [-d DUE] [-t TAGS]` | Create a task |
| `list` | `[-a] [--done] [-p PRIORITY] [-t TAG] [--overdue] [-s SORT]` | Show tasks (open ones by default) |
| `done` | `ID` | Mark a task as completed |
| `delete` | `ID` | Remove a task permanently |
| `search` | `QUERY...` | Case-insensitive search in titles and tags |

Global flag: `--file PATH` — the JSON file to use (default `tasks.json`).

### Input rules

- `PRIORITY` ∈ `low` / `medium` / `high` (default `medium`)
- `DUE` accepts `YYYY-MM-DD`, `today`, `tomorrow` or `+N` (N days from now)
- `TAGS` is a comma-separated list: `home,urgent`
- `ID` must be a positive integer

## Data Model

```python
@dataclass
class Task:
    id: int                # never reused, assigned as max(existing) + 1
    title: str
    priority: str          # low | medium | high
    due: str | None        # ISO date "YYYY-MM-DD"
    tags: list[str]
    done: bool
    created: str           # "YYYY-MM-DD HH:MM"
    completed: str | None  # set by `done`
```

## Storage

- JSON list of task objects, `indent=2`, UTF-8
- **Atomic writes**: dump to a temp file in the same directory, then
  `os.replace()` — a crash can never corrupt the task file
- **Lock file**: `<file>.lock` created with `O_CREAT | O_EXCL` guards every
  mutating command; acquisition retries for 3 s, then fails cleanly

## Output & Errors

- Tables use ANSI colors when stdout is a TTY (`NO_COLOR` respected):
  priorities color-coded, overdue rows red, done rows dimmed
- Errors print to **stderr** as `error: <message>`
- Exit codes: `0` success · `1` storage/user error · `2` argparse usage error
