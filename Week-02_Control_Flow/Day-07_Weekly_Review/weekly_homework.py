# Week 2 - Day 7: Weekly Homework
# Mini Project: Student Grade Management System
#
# Build a complete grade management system that uses
# EVERY control flow concept from Week 2:
#   ✅ if / elif / else      — grade letters, validation
#   ✅ for loops             — iterating students & scores
#   ✅ while loops           — menu loop, input validation
#   ✅ break / continue      — search, skip invalid entries
#   ✅ nested loops          — subject × student iteration
#   ✅ match / case          — menu dispatcher

# ─────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────
students = {}   # { name: [score1, score2, score3] }
SUBJECTS = ["Math", "Science", "English"]


# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def letter_grade(avg):
    if avg >= 90:   return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else:           return "F"


def get_valid_score(subject):
    while True:
        raw = input(f"  {subject} score (0-100): ").strip()
        if not raw.isdigit():
            print("  ⚠ Please enter a whole number.")
            continue
        score = int(raw)
        if 0 <= score <= 100:
            return score
        print("  ⚠ Score must be between 0 and 100.")


def add_student():
    print("\n── Add Student ──")
    name = input("Student name: ").strip().title()
    if not name:
        print("⚠ Name cannot be empty.")
        return
    if name in students:
        print(f"⚠ '{name}' already exists.")
        return
    scores = []
    for subject in SUBJECTS:
        scores.append(get_valid_score(subject))
    students[name] = scores
    print(f"✅ {name} added successfully.")


def view_all():
    if not students:
        print("\n⚠ No students recorded yet.")
        return
    print(f"\n{'─'*58}")
    print(f"  {'Name':<12}" + "".join(f"{s:>10}" for s in SUBJECTS) + f"{'Avg':>8}  {'Grade':>5}")
    print(f"{'─'*58}")
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        grade = letter_grade(avg)
        row = f"  {name:<12}" + "".join(f"{s:>10}" for s in scores)
        row += f"{avg:>8.1f}  {grade:>5}"
        print(row)
    print(f"{'─'*58}")


def search_student():
    print("\n── Search Student ──")
    target = input("Enter name to search: ").strip().title()
    for name, scores in students.items():
        if name == target:
            avg   = sum(scores) / len(scores)
            grade = letter_grade(avg)
            print(f"\n  Student : {name}")
            for subject, score in zip(SUBJECTS, scores):
                print(f"  {subject:<10}: {score}")
            print(f"  {'Average':<10}: {avg:.1f}  →  Grade {grade}")
            return
    print(f"⚠ '{target}' not found.")


def class_statistics():
    if not students:
        print("\n⚠ No data available.")
        return
    print("\n── Class Statistics ──")

    # Subject averages using nested loops
    for i, subject in enumerate(SUBJECTS):
        subject_scores = []
        for scores in students.values():
            subject_scores.append(scores[i])
        subj_avg = sum(subject_scores) / len(subject_scores)
        print(f"  {subject} average : {subj_avg:.1f}")

    # Best and weakest student
    best_name, best_avg = "", 0
    weak_name, weak_avg = "", 101
    for name, scores in students.items():
        avg = sum(scores) / len(scores)
        if avg > best_avg:
            best_avg, best_name = avg, name
        if avg < weak_avg:
            weak_avg, weak_name = avg, name

    print(f"\n  Top student   : {best_name} ({best_avg:.1f})")
    print(f"  Needs support : {weak_name} ({weak_avg:.1f})")

    # Grade distribution
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for scores in students.values():
        avg = sum(scores) / len(scores)
        dist[letter_grade(avg)] += 1
    print("\n  Grade distribution:")
    for grade, count in dist.items():
        bar = "█" * count
        print(f"    {grade} : {bar} ({count})")


def remove_student():
    print("\n── Remove Student ──")
    name = input("Enter name to remove: ").strip().title()
    if name in students:
        del students[name]
        print(f"✅ '{name}' removed.")
    else:
        print(f"⚠ '{name}' not found.")


def show_menu():
    print("\n" + "═" * 40)
    print("  GRADE MANAGEMENT SYSTEM")
    print("═" * 40)
    print("  1. Add student")
    print("  2. View all students")
    print("  3. Search student")
    print("  4. Class statistics")
    print("  5. Remove student")
    print("  6. Exit")
    print("─" * 40)


# ─────────────────────────────────────────────
# MAIN LOOP — match/case dispatcher
# ─────────────────────────────────────────────
def main():
    print("\nWelcome to the Grade Management System!")
    print(f"Tracking subjects: {', '.join(SUBJECTS)}")

    while True:
        show_menu()
        choice = input("  Choose (1-6): ").strip()

        match choice:
            case "1":
                add_student()
            case "2":
                view_all()
            case "3":
                search_student()
            case "4":
                class_statistics()
            case "5":
                remove_student()
            case "6":
                print("\nGoodbye! Keep learning. 🐍")
                break
            case _:
                print("⚠ Invalid option. Please choose 1–6.")


if __name__ == "__main__":
    main()
