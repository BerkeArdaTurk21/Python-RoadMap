# Week 03 — Functions

> **Level:** Beginner  
> **Goal:** Write reusable, clean, and well-documented functions — the foundation of every Python program.

---

## What You Will Learn

By the end of this week you will be able to:

- Define and call functions with `def`
- Use positional, default, and keyword arguments
- Accept any number of arguments with `*args` and `**kwargs`
- Write concise one-liner functions with `lambda`
- Use `map()`, `filter()`, and `sorted()` with a key function
- Understand variable scope: local, global, nonlocal, LEGB rule
- Write closures that remember enclosing state
- Solve problems recursively with a base case and recursive case

---

## Daily Breakdown

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| 01 | Defining Functions | def, parameters, return, docstrings |
| 02 | Default & Keyword Args | default values, keyword arguments, argument order |
| 03 | *args & **kwargs | variable length arguments, unpacking |
| 04 | Lambda Functions | lambda, map(), filter(), sorted() with key |
| 05 | Scope & Closures | local, global, nonlocal, LEGB rule, closures |
| 06 | Recursion | base case, recursive case, call stack |
| 07 | Weekly Review | weekly_quiz.py (10 MCQ + 5 code challenges) + weekly project |

---

## Progress

| Day | Topic | Status |
|-----|-------|--------|
| 01 | Defining Functions | ✅ Done |
| 02 | Default & Keyword Args | ✅ Done |
| 03 | *args & **kwargs | ⏳ Upcoming |
| 04 | Lambda Functions | ⏳ Upcoming |
| 05 | Scope & Closures | ⏳ Upcoming |
| 06 | Recursion | ⏳ Upcoming |
| 07 | Weekly Review | ⏳ Upcoming |

---

## Folder Structure

```
Week-03_Functions/
├── README.md                    ← You are here
├── Day-01/
│   ├── lesson.py                ← Defining Functions
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-02/
│   ├── lesson.py                ← Default & Keyword Args
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-03/
│   ├── lesson.py                ← *args & **kwargs
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-04/
│   ├── lesson.py                ← Lambda Functions
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-05/
│   ├── lesson.py                ← Scope & Closures
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-06/
│   ├── lesson.py                ← Recursion
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
cd Week-03_Functions/Day-01
python quiz.py
```

---

## Key Takeaways

```python
# Defining a function
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Berke"))       # Hello, Berke!

# Default arguments
def power(base, exp=2):
    return base ** exp

print(power(3))             # 9   (exp defaults to 2)
print(power(2, 10))         # 1024

# *args and **kwargs
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))    # 10

# Lambda
square = lambda x: x ** 2
print(square(5))            # 25

# map / filter
nums = [1, 2, 3, 4, 5]
doubled  = list(map(lambda x: x * 2, nums))   # [2,4,6,8,10]
evens    = list(filter(lambda x: x % 2 == 0, nums))  # [2,4]

# Scope
x = 10                      # global
def foo():
    x = 20                  # local — does NOT affect global x
    print(x)                # 20
foo()
print(x)                    # 10

# Recursion
def factorial(n):
    if n == 0: return 1     # base case
    return n * factorial(n - 1)

print(factorial(5))         # 120
```

---

## Prerequisites

Completed Week 02 — Control Flow. You should be comfortable with:
- if/elif/else conditions and truthiness
- for and while loops
- break, continue, pass
- Nested loops and 2D data
