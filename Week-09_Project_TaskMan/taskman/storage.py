"""JSON persistence for taskman — atomic writes + a simple lock file.

Week 6 (file I/O, custom exceptions) and Week 8 (context managers) skills.
"""

import json
import os
import tempfile
import time
from collections.abc import Generator
from contextlib import contextmanager
from pathlib import Path

from taskman.models import Task

DEFAULT_FILE = Path("tasks.json")


class StorageError(Exception):
    """Raised when the task file cannot be read, parsed or locked."""


@contextmanager
def file_lock(path: Path, timeout: float = 3.0) -> Generator[None, None, None]:
    """Crude cross-platform lock: only one process may hold <file>.lock.

    O_CREAT | O_EXCL is atomic — creating the lock file fails if it already
    exists, so two processes can never both think they own the lock.
    """
    lock_path = path.with_suffix(path.suffix + ".lock")
    deadline = time.monotonic() + timeout
    while True:
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            break
        except FileExistsError:
            if time.monotonic() >= deadline:
                raise StorageError(
                    f"could not acquire lock {lock_path} — is another taskman running? "
                    f"(delete the file if it is stale)"
                )
            time.sleep(0.05)
    try:
        os.close(fd)
        yield
    finally:
        lock_path.unlink(missing_ok=True)


def load_tasks(path: Path = DEFAULT_FILE) -> list[Task]:
    """Read all tasks. A missing file is an empty task list, not an error."""
    if not path.exists():
        return []
    try:
        with open(path, encoding="utf-8") as f:
            raw = json.load(f)
    except json.JSONDecodeError as exc:
        raise StorageError(f"{path} is not valid JSON: {exc}") from exc
    if not isinstance(raw, list):
        raise StorageError(f"{path} has an unexpected format (expected a JSON list)")
    return [Task.from_dict(item) for item in raw]


def save_tasks(tasks: list[Task], path: Path = DEFAULT_FILE) -> None:
    """Write atomically: dump to a temp file, then os.replace over the target.

    A crash mid-write can never leave a half-written tasks.json — the old
    file stays intact until the replace, and os.replace itself is atomic.
    """
    payload = json.dumps([t.to_dict() for t in tasks], indent=2, ensure_ascii=False)
    fd, tmp_name = tempfile.mkstemp(
        dir=path.parent if str(path.parent) else ".", suffix=".tmp"
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as tmp:
            tmp.write(payload + "\n")
        os.replace(tmp_name, path)
    except BaseException:
        Path(tmp_name).unlink(missing_ok=True)
        raise


def next_id(tasks: list[Task]) -> int:
    """IDs are never reused: always one past the highest ever assigned."""
    return max((t.id for t in tasks), default=0) + 1
