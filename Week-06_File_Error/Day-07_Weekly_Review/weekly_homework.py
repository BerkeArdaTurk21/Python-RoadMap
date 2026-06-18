# =============================================================================
# Week 06 - Day 07 | Weekly Homework — Student Grade Manager
# =============================================================================
# Mini project combining all Week 6 topics:
#   - File I/O: read/write student records as JSON
#   - Paths: pathlib for file operations
#   - try/except: graceful error handling
#   - Custom exceptions: domain-specific errors
#   - raise / assert: input validation
# =============================================================================

import json
from pathlib import Path

# ─── Custom Exceptions ─────────────────────────────────────────────────────────

class GradeManagerError(Exception):
    """Base exception for GradeManager."""

class StudentNotFoundError(GradeManagerError):
    def __init__(self, student_id):
        super().__init__(f"Student '{student_id}' not found")
        self.student_id = student_id

class InvalidGradeError(GradeManagerError):
    def __init__(self, grade, subject):
        super().__init__(
            f"Grade {grade!r} for '{subject}' must be 0-100"
        )
        self.grade   = grade
        self.subject = subject

class DuplicateStudentError(GradeManagerError):
    def __init__(self, student_id):
        super().__init__(f"Student '{student_id}' already exists")
        self.student_id = student_id

# ─── GradeManager Class ────────────────────────────────────────────────────────

class GradeManager:
    """
    Manages student grades with JSON persistence.

    Storage format (grades.json):
    {
        "S001": {"name": "Alice", "grades": {"Math": 90, "Science": 85}},
        ...
    }
    """

    def __init__(self, filepath="grades.json"):
        self.filepath = Path(filepath)
        self._data = {}
        self._load()

    # ── Persistence ────────────────────────────────────────────────────────────

    def _load(self):
        """Load data from JSON file if it exists."""
        try:
            with open(self.filepath, encoding="utf-8") as f:
                self._data = json.load(f)
        except FileNotFoundError:
            self._data = {}     # start fresh

    def save(self):
        """Write current data to JSON file."""
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2)

    # ── CRUD Operations ────────────────────────────────────────────────────────

    def add_student(self, student_id: str, name: str):
        assert isinstance(student_id, str) and student_id, "student_id must be a non-empty string"
        assert isinstance(name, str) and name, "name must be a non-empty string"
        if student_id in self._data:
            raise DuplicateStudentError(student_id)
        self._data[student_id] = {"name": name, "grades": {}}

    def add_grade(self, student_id: str, subject: str, grade: float):
        if student_id not in self._data:
            raise StudentNotFoundError(student_id)
        if not (0 <= grade <= 100):
            raise InvalidGradeError(grade, subject)
        self._data[student_id]["grades"][subject] = grade

    def get_student(self, student_id: str) -> dict:
        if student_id not in self._data:
            raise StudentNotFoundError(student_id)
        return self._data[student_id]

    def average(self, student_id: str) -> float:
        student = self.get_student(student_id)
        grades = student["grades"]
        if not grades:
            raise GradeManagerError(f"No grades recorded for '{student_id}'")
        return sum(grades.values()) / len(grades)

    def letter_grade(self, avg: float) -> str:
        if avg >= 90: return "A"
        if avg >= 80: return "B"
        if avg >= 70: return "C"
        if avg >= 60: return "D"
        return "F"

    def class_report(self):
        """Print a formatted report for all students."""
        if not self._data:
            print("No students enrolled.")
            return
        print(f"{'ID':<8} {'Name':<15} {'Avg':>6} {'Grade':>6}")
        print("-" * 40)
        for sid, info in self._data.items():
            try:
                avg = self.average(sid)
                letter = self.letter_grade(avg)
                print(f"{sid:<8} {info['name']:<15} {avg:>6.1f} {letter:>6}")
            except GradeManagerError as e:
                print(f"{sid:<8} {info['name']:<15} {'N/A':>6} {'?':>6}")

    def top_student(self) -> tuple[str, float]:
        """Return (student_id, average) for the highest-scoring student."""
        best_id, best_avg = None, -1.0
        for sid in self._data:
            try:
                avg = self.average(sid)
                if avg > best_avg:
                    best_avg, best_id = avg, sid
            except GradeManagerError:
                continue
        if best_id is None:
            raise GradeManagerError("No students with grades")
        return best_id, best_avg

# ─── Demo ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    mgr = GradeManager("demo_grades.json")

    # Add students
    try:
        mgr.add_student("S001", "Alice")
        mgr.add_student("S002", "Bob")
        mgr.add_student("S003", "Carol")
        print("Students added.")
    except DuplicateStudentError as e:
        print(f"DuplicateStudentError: {e}")

    # Add grades
    grades = [
        ("S001", "Math",    92),
        ("S001", "Science", 88),
        ("S001", "English", 95),
        ("S002", "Math",    74),
        ("S002", "Science", 81),
        ("S002", "English", 69),
        ("S003", "Math",    55),
        ("S003", "Science", 62),
        ("S003", "English", 58),
    ]
    for sid, subj, grade in grades:
        try:
            mgr.add_grade(sid, subj, grade)
        except (StudentNotFoundError, InvalidGradeError) as e:
            print(f"Error: {e}")

    # Invalid grade demo
    try:
        mgr.add_grade("S001", "Art", 110)
    except InvalidGradeError as e:
        print(f"InvalidGradeError: {e}")

    # Unknown student demo
    try:
        mgr.add_grade("S999", "Math", 80)
    except StudentNotFoundError as e:
        print(f"StudentNotFoundError: {e}")

    # Save to JSON
    mgr.save()
    print(f"\nData saved to {mgr.filepath.resolve()}")

    # Report
    print("\n── Class Report ──")
    mgr.class_report()

    # Top student
    print()
    top_id, top_avg = mgr.top_student()
    top_name = mgr.get_student(top_id)["name"]
    print(f"Top student: {top_name} ({top_id}) — avg {top_avg:.1f}")

    # Load from file (new instance)
    print("\n── Reload from JSON ──")
    mgr2 = GradeManager("demo_grades.json")
    mgr2.class_report()

    # Cleanup
    Path("demo_grades.json").unlink(missing_ok=True)
    print("\ndemo_grades.json removed. Done!")
