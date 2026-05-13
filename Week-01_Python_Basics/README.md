# Week 01 — Python Basics

> **Level:** Beginner  
> **Goal:** Master the absolute fundamentals — variables, data types, operators, user input, and output formatting.

---

## What You Will Learn

By the end of this week you will be able to:

- Store and manipulate data using Python variables
- Understand and use all core data types (int, float, str, bool, NoneType)
- Perform arithmetic and use the math module
- Accept input from the user and convert it safely
- Use every Python operator: comparison, logical, bitwise, identity, membership, ternary
- Control exactly how output looks with f-strings, format specs, and print() parameters
- Write clean, readable Python code following PEP 8 conventions

---

## Daily Breakdown

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| 01 | Variables & Data Types | assignment, naming rules, int, float, str, bool, None, type(), id(), f-strings |
| 02 | String Operations | indexing, slicing, methods, f-strings, escape characters |
| 03 | Numbers & Math | arithmetic, integer division, modulo, math module, round() |
| 04 | User Input & Type Conversion | input(), int(), float(), str(), bool(), isdigit(), ValueError |
| 05 | Operators & Expressions | comparison, logical, bitwise, identity, membership, ternary, precedence |
| 06 | Print & Formatting | sep, end, f-string format specs, format(), number formatting, print tricks |
| 07 | Weekly Review | quiz (10 MCQ + 5 challenges) + homework project |

---

## Folder Structure

```
Week-01_Python_Basics/
├── README.md                    ← You are here
├── Day-01/
│   ├── lesson.py                ← Variables & Data Types
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-02/
│   ├── lesson.py                ← String Operations
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-03/
│   ├── lesson.py                ← Numbers & Math
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-04/
│   ├── lesson.py                ← User Input & Type Conversion
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-05/
│   ├── lesson.py                ← Operators & Expressions
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-06/
│   ├── lesson.py                ← Print & Formatting
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
└── Day-07_Weekly_Review/
    ├── weekly_quiz.py           ← 10 MCQ + 5 code challenges
    ├── weekly_quiz.ipynb
    └── weekly_homework.py       ← Mini project
```

---

## How to Study

**Step 1** → Read `lesson.py` or open `lesson.ipynb` in Jupyter  
**Step 2** → Run `python quiz.py` — score 5/5 before continuing  
**Step 3** → Solve `exercises.py` challenges yourself  
**Step 4** → Check `solutions.py` to compare  

```bash
cd Week-01_Python_Basics/Day-01
python quiz.py
```

---

## Key Takeaways

```python
# Variables — containers that store data
name  = "Berke"     # str
age   = 25          # int
gpa   = 3.87        # float
active = True       # bool
alias  = None       # NoneType

# Type checking and conversion
print(type(name))   # <class 'str'>
num = int("42")     # str → int
txt = str(age)      # int → str

# User input — always returns str
score = int(input("Enter score: "))

# Operators
print(5 & 3)        # 1   (bitwise AND)
print(0.875:.1%)    # use f-string: f"{0.875:.1%}" → 87.5%
x = 5
print(1 < x < 10)  # True  (chained comparison)
label = "Adult" if age >= 18 else "Minor"   # ternary

# Print formatting
print("a", "b", "c", sep=" | ")   # a | b | c
print(f"{name:<10} {score:>6} {gpa:.2f}")
print(f"{1_000_000:,}")            # 1,000,000
print(f"{255:#x}")                 # 0xff
```

---

## Prerequisites

No prior programming knowledge required. Just Python 3.11+ installed.

```bash
python --version   # should print Python 3.11.x or higher
```
