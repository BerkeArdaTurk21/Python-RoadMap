# Week 02 — Control Flow

> **Level:** Beginner  
> **Goal:** Control exactly how your program runs — make decisions with conditions, repeat actions with loops, and handle every branching scenario.

---

## What You Will Learn

By the end of this week you will be able to:

- Write `if / elif / else` chains to make decisions based on conditions
- Use `for` loops to iterate over sequences (lists, strings, ranges, dicts)
- Use `while` loops to repeat code until a condition becomes false
- Control loop execution with `break`, `continue`, and `pass`
- Nest loops to work with multi-dimensional data and patterns
- Use Python 3.10+ `match / case` for structural pattern matching
- Combine conditions with `and`, `or`, `not`, and understand truthiness

---

## Daily Breakdown

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| 01 | if / elif / else | conditions, comparison operators, logical operators, truthiness, nested if, ternary |
| 02 | for Loops | range(), iterate lists/strings/dicts, enumerate(), zip() |
| 03 | while Loops | condition loops, infinite loop prevention, input validation loops |
| 04 | break / continue / pass | loop control flow, early exit, skipping iterations |
| 05 | Nested Loops | matrix patterns, loop inside loop, 2D iteration |
| 06 | match / case | Python 3.10+ structural pattern matching, guard clauses |
| 07 | Weekly Review | weekly_quiz.py (10 MCQ + 5 code challenges) + weekly project |

---

## Progress

| Day | Topic | Status |
|-----|-------|--------|
| 01 | if / elif / else | ✅ Done |
| 02 | for Loops | ⏳ Upcoming |
| 03 | while Loops | ⏳ Upcoming |
| 04 | break / continue / pass | ⏳ Upcoming |
| 05 | Nested Loops | ⏳ Upcoming |
| 06 | match / case | ⏳ Upcoming |
| 07 | Weekly Review | ⏳ Upcoming |

---

## Folder Structure

```
Week-02_Control_Flow/
├── README.md                    ← You are here
├── Day-01/
│   ├── lesson.py                ← if / elif / else
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-02/
│   ├── lesson.py                ← for Loops
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-03/
│   ├── lesson.py                ← while Loops
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-04/
│   ├── lesson.py                ← break / continue / pass
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-05/
│   ├── lesson.py                ← Nested Loops
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-06/
│   ├── lesson.py                ← match / case
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
└── Day-07_Weekly_Review/
    ├── weekly_quiz.py           ← 10 MCQ + 5 code challenges
    ├── weekly_quiz.ipynb
    └── weekly_homework.py       ← Weekly mini project
```

---

## How to Study

**Step 1** → Read `lesson.py` or open `lesson.ipynb` in Jupyter  
**Step 2** → Run `python quiz.py` — score 5/5 before continuing  
**Step 3** → Solve `exercises.py` challenges yourself  
**Step 4** → Check `solutions.py` to compare  

```bash
cd Week-02_Control_Flow/Day-01
python quiz.py
```

---

## Key Takeaways

```python
# if / elif / else — decision making
score = 78
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "C"     # runs — 78 >= 70
else:
    grade = "F"

# Truthiness — falsy: False, None, 0, "", [], {}, ()
name = ""
if name:
    print("set")
else:
    print("empty")  # runs

# Ternary expression
status = "adult" if age >= 18 else "minor"

# for loop — iterating sequences
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)

for i in range(5):       # 0 1 2 3 4
    print(i)

# while loop — condition-based repetition
count = 0
while count < 3:
    print(count)
    count += 1

# break / continue
for n in range(10):
    if n == 5:
        break           # stops loop at 5
    if n % 2 == 0:
        continue        # skips even numbers
    print(n)            # prints 1 3

# match / case (Python 3.10+)
command = "quit"
match command:
    case "start":
        print("Starting...")
    case "quit":
        print("Goodbye.")   # runs
    case _:
        print("Unknown command.")
```

---

## Prerequisites

Completed Week 01 — Python Basics. You should be comfortable with:
- Variables, data types, and type conversion
- User input with `input()`
- Comparison and logical operators
- f-strings and print formatting
