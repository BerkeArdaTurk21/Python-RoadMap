# Week 01 — Python Basics

> **Level:** Beginner
> **Goal:** Master the absolute fundamentals — variables, data types, user input, and type conversion.

---

## What You Will Learn

By the end of this week you will be able to:

- Store and manipulate data using Python variables
- Understand and use all core data types (int, float, str, bool, NoneType)
- Accept input from the user and process it
- Convert between data types safely
- Write clean, readable Python code following PEP 8 conventions
- Use f-strings for professional string formatting
- Understand how Python manages memory with id() and type()

---

## Daily Breakdown

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| 01 | Variables & Data Types | assignment, naming rules, int, float, str, bool, None |
| 02 | String Operations | indexing, slicing, methods, f-strings, escape characters |
| 03 | Numbers & Math | arithmetic, integer division, modulo, math module, round() |
| 04 | User Input & Type Conversion | input(), int(), float(), str(), bool(), ValueError |
| 05 | Boolean Logic & None | True/False, comparison operators, logical operators, None |
| 06 | PEP 8 & Best Practices | naming conventions, comments, code style, readability |
| 07 | Weekly Review | quiz (10 MCQ + 5 challenges) + homework project |

---

## Folder Structure

```
Week-01_Python_Basics/
├── README.md                    ← You are here
├── Day-01/
│   ├── lesson.py                ← Variables & Data Types
│   ├── lesson.ipynb
│   └── exercises.py
├── Day-02/
│   ├── lesson.py                ← String Operations
│   ├── lesson.ipynb
│   └── exercises.py
├── Day-03/
│   ├── lesson.py                ← Numbers & Math
│   ├── lesson.ipynb
│   └── exercises.py
├── Day-04/
│   ├── lesson.py                ← User Input & Type Conversion
│   ├── lesson.ipynb
│   └── exercises.py
├── Day-05/
│   ├── lesson.py                ← Boolean Logic & None
│   ├── lesson.ipynb
│   └── exercises.py
├── Day-06/
│   ├── lesson.py                ← PEP 8 & Best Practices
│   ├── lesson.ipynb
│   └── exercises.py
└── Day-07_Weekly_Review/
    ├── weekly_quiz.py           ← 10 MCQ + 5 code challenges
    ├── weekly_quiz.ipynb
    └── weekly_homework.py       ← Project: Personal Info Card Generator
```

---

## How to Run

```bash
cd Week-01_Python_Basics/Day-01
python lesson.py
```

---

## Key Takeaways

```python
# Variables — containers that store data
name = "Berke"          # str
age = 25                # int
height = 1.82           # float
is_developer = True     # bool
middle_name = None      # NoneType

# Check type at runtime
print(type(name))       # <class 'str'>

# Type conversion
age_str = str(age)      # "25"
num = int("42")         # 42

# f-strings — the modern way to format strings
print(f"Hello, {name}! You are {age} years old.")
```

---

## Prerequisites

No prior programming knowledge required. Just Python 3.11+ installed.

```bash
python --version   # should print Python 3.11.x or higher
```
