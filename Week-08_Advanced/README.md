# Week 08 — Advanced Python

> **Level:** Intermediate → Advanced
> **Goal:** Master Python's power features: decorators, iterators, generators, context managers, type hints, and testing.

---

## What You Will Learn

By the end of this week you will be able to:

- Write and stack **decorators** using `functools.wraps` and decorator factories
- Build **custom iterators** with `__iter__` and `__next__`
- Use **generators** with `yield` for lazy, memory-efficient sequences
- Create **context managers** with `__enter__`/`__exit__` and `@contextmanager`
- Add **type hints** using the `typing` module and understand how mypy uses them
- Write and run **tests** with `pytest` — fixtures, parametrize, and coverage basics

---

## Daily Breakdown

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| 01 | Decorators | function decorators, `@wraps`, stacked decorators, decorator factories |
| 02 | Iterators | `__iter__`, `__next__`, custom iterators, `StopIteration` |
| 03 | Generators | `yield`, generator expressions, `next()`, `send()`, lazy evaluation |
| 04 | Context Managers | `__enter__`, `__exit__`, `contextlib`, `@contextmanager` |
| 05 | Type Hints | `typing` module, `Optional`, `Union`, generics, mypy intro |
| 06 | Testing with pytest | test discovery, assertions, fixtures, parametrize, coverage basics |
| 07 | Weekly Review | weekly_quiz.py (10 MCQ + 5 code challenges) + weekly project |

---

## Progress

| Day | Topic | Status |
|-----|-------|--------|
| 01 | Decorators | ✅ Done |
| 02 | Iterators | ✅ Done |
| 03 | Generators | ⏳ Upcoming |
| 04 | Context Managers | ⏳ Upcoming |
| 05 | Type Hints | ⏳ Upcoming |
| 06 | Testing with pytest | ⏳ Upcoming |
| 07 | Weekly Review | ⏳ Upcoming |

---

## Folder Structure

```
Week-08_Advanced/
├── README.md
├── Day-01/
│   ├── lesson.py        ← Decorators
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-02/ ... Day-06/  ← Same structure
└── Day-07_Weekly_Review/
    ├── weekly_quiz.py
    ├── weekly_quiz.ipynb
    └── weekly_homework.py
```

---

## Prerequisites

Completed Week 07 — Modules & Packages. You should be comfortable with:
- Using the standard library modules (`os`, `sys`, `datetime`, `random`, `re`)
- Building virtual environments with `venv`
- Writing multi-file Python programs
