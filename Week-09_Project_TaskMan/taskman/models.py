"""Data model for taskman — a single Task dataclass (Week 5 + Week 8 skills)."""

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any

PRIORITIES = ("low", "medium", "high")
PRIORITY_RANK = {"high": 0, "medium": 1, "low": 2}   # for sorting


def _now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


@dataclass
class Task:
    id: int
    title: str
    priority: str = "medium"
    due: str | None = None                 # ISO date "YYYY-MM-DD" or None
    tags: list[str] = field(default_factory=list)
    done: bool = False
    created: str = field(default_factory=_now)
    completed: str | None = None

    # ── Behavior ──────────────────────────────────────────────────────────

    def due_date(self) -> date | None:
        """The due date as a real date object (None if no due date)."""
        if self.due is None:
            return None
        return date.fromisoformat(self.due)

    def is_overdue(self) -> bool:
        """Open task whose due date has passed."""
        d = self.due_date()
        return d is not None and d < date.today() and not self.done

    def mark_done(self) -> None:
        self.done = True
        self.completed = _now()

    def matches(self, query: str) -> bool:
        """Case-insensitive search across title and tags."""
        q = query.lower()
        return q in self.title.lower() or any(q in tag.lower() for tag in self.tags)

    # ── JSON round-trip ───────────────────────────────────────────────────

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "due": self.due,
            "tags": self.tags,
            "done": self.done,
            "created": self.created,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Task":
        return cls(
            id=int(data["id"]),
            title=str(data["title"]),
            priority=data.get("priority", "medium"),
            due=data.get("due"),
            tags=list(data.get("tags", [])),
            done=bool(data.get("done", False)),
            created=data.get("created", _now()),
            completed=data.get("completed"),
        )
