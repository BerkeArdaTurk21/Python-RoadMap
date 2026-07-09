# =============================================================================
# taskman test suite — run with:  pytest -v
# =============================================================================

import argparse
import json
from datetime import date, timedelta

import pytest

from taskman.cli import build_parser, main, parse_due, positive_int, sort_tasks, tag_list
from taskman.models import Task
from taskman.storage import StorageError, file_lock, load_tasks, next_id, save_tasks

# ─── Argument validators ───────────────────────────────────────────────────────

def test_parse_due_iso():
    assert parse_due("2026-07-20") == "2026-07-20"

def test_parse_due_keywords():
    assert parse_due("today") == date.today().isoformat()
    assert parse_due("tomorrow") == (date.today() + timedelta(days=1)).isoformat()
    assert parse_due("+7") == (date.today() + timedelta(days=7)).isoformat()

def test_parse_due_invalid():
    with pytest.raises(argparse.ArgumentTypeError):
        parse_due("next friday")

def test_positive_int_rejects_zero_and_text():
    with pytest.raises(argparse.ArgumentTypeError):
        positive_int("0")
    with pytest.raises(argparse.ArgumentTypeError):
        positive_int("abc")

def test_tag_list_splits_and_strips():
    assert tag_list("home, urgent ,errands,") == ["home", "urgent", "errands"]

# ─── Parser ────────────────────────────────────────────────────────────────────

def test_parser_add_full():
    args = build_parser().parse_args(
        ["add", "Buy", "milk", "-p", "high", "-d", "2026-07-20", "-t", "home,errands"]
    )
    assert args.command == "add"
    assert args.title == ["Buy", "milk"]
    assert args.priority == "high"
    assert args.due == "2026-07-20"
    assert args.tags == ["home", "errands"]

def test_parser_rejects_bad_priority():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["add", "x", "--priority", "urgent"])

def test_parser_rejects_bad_due():
    with pytest.raises(SystemExit):
        build_parser().parse_args(["add", "x", "--due", "someday"])

# ─── Task model ────────────────────────────────────────────────────────────────

def test_task_roundtrip():
    task = Task(id=1, title="Test", priority="high", due="2026-01-01", tags=["a"])
    assert Task.from_dict(task.to_dict()) == task

def test_task_overdue():
    yesterday = (date.today() - timedelta(days=1)).isoformat()
    task = Task(id=1, title="Late", due=yesterday)
    assert task.is_overdue()
    task.mark_done()
    assert not task.is_overdue()          # done tasks are never overdue
    assert task.completed is not None

def test_task_matches_title_and_tags():
    task = Task(id=1, title="Water the plants", tags=["garden"])
    assert task.matches("PLANTS")
    assert task.matches("garden")
    assert not task.matches("invoice")

def test_sort_by_priority_then_id():
    tasks = [
        Task(id=1, title="a", priority="low"),
        Task(id=2, title="b", priority="high"),
        Task(id=3, title="c", priority="medium"),
    ]
    assert [t.id for t in sort_tasks(tasks, "priority")] == [2, 3, 1]

def test_sort_by_due_puts_undated_last():
    tasks = [
        Task(id=1, title="a"),
        Task(id=2, title="b", due="2026-02-01"),
        Task(id=3, title="c", due="2026-01-01"),
    ]
    assert [t.id for t in sort_tasks(tasks, "due")] == [3, 2, 1]

# ─── Storage ───────────────────────────────────────────────────────────────────

def test_load_missing_file_is_empty(tmp_path):
    assert load_tasks(tmp_path / "nope.json") == []

def test_save_load_roundtrip(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = [Task(id=1, title="One"), Task(id=2, title="Two", done=True)]
    save_tasks(tasks, path)
    assert load_tasks(path) == tasks

def test_load_corrupt_json_raises(tmp_path):
    path = tmp_path / "tasks.json"
    path.write_text("{not json!", encoding="utf-8")
    with pytest.raises(StorageError):
        load_tasks(path)

def test_save_leaves_no_temp_files(tmp_path):
    path = tmp_path / "tasks.json"
    save_tasks([Task(id=1, title="x")], path)
    assert [p.name for p in tmp_path.iterdir()] == ["tasks.json"]

def test_next_id_never_reuses():
    tasks = [Task(id=1, title="a"), Task(id=7, title="b")]
    assert next_id(tasks) == 8
    assert next_id([]) == 1

def test_file_lock_blocks_second_holder(tmp_path):
    path = tmp_path / "tasks.json"
    with file_lock(path):
        with pytest.raises(StorageError):
            with file_lock(path, timeout=0.2):
                pass

# ─── End-to-end through main() ─────────────────────────────────────────────────

@pytest.fixture
def task_file(tmp_path):
    return str(tmp_path / "tasks.json")

def run(task_file, *argv):
    return main(["--file", task_file, *argv])

def test_e2e_add_list_done_delete(task_file, capsys):
    assert run(task_file, "add", "Buy milk", "-p", "high", "-t", "home") == 0
    assert run(task_file, "add", "Ship report", "-d", "tomorrow") == 0
    capsys.readouterr()

    assert run(task_file, "list") == 0
    out = capsys.readouterr().out
    assert "Buy milk" in out and "Ship report" in out

    assert run(task_file, "done", "1") == 0
    capsys.readouterr()
    assert run(task_file, "list") == 0
    assert "Buy milk" not in capsys.readouterr().out    # open-only by default

    assert run(task_file, "list", "--done") == 0
    assert "Buy milk" in capsys.readouterr().out

    assert run(task_file, "search", "report") == 0
    assert "Ship report" in capsys.readouterr().out

    assert run(task_file, "delete", "2") == 0
    saved = json.loads(open(task_file, encoding="utf-8").read())
    assert [t["id"] for t in saved] == [1]

def test_e2e_missing_id_fails(task_file, capsys):
    assert run(task_file, "done", "99") == 1
    assert "no task with id 99" in capsys.readouterr().err
