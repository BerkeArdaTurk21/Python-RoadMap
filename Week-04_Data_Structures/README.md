# Week 04 — Data Structures

> **Level:** Beginner
> **Goal:** Master Python's built-in data structures — lists, tuples, dicts, sets — and learn to pick the right one for every job.

---

## What You Will Learn

By the end of this week you will be able to:

- Create, index, slice, and mutate **lists**
- Use **tuples** for immutable sequences and unpacking
- Work with **dictionaries** — keys, values, nesting, and methods
- Apply **sets** for unique collections and mathematical operations
- Write **list, dict, and set comprehensions**
- Use the **`collections` module** (Counter, defaultdict, deque, namedtuple)

---

## Daily Breakdown

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| 01 | Lists | indexing, slicing, methods, mutability |
| 02 | Tuples | immutability, packing/unpacking, named tuples |
| 03 | Dictionaries | keys, values, methods, nested dicts |
| 04 | Sets | uniqueness, set operations, frozenset |
| 05 | Comprehensions | list / dict / set comprehensions, generator expressions, nesting, conditions |
| 06 | collections Module | Counter, defaultdict, namedtuple, deque, OrderedDict |
| 07 | Weekly Review | weekly_quiz.py (10 MCQ + 5 code challenges) + weekly project |

---

## Progress

| Day | Topic | Status |
|-----|-------|--------|
| 01 | Lists | ✅ Done |
| 02 | Tuples | ✅ Done |
| 03 | Dictionaries | ✅ Done |
| 04 | Sets | ✅ Done |
| 05 | Comprehensions | ⏳ Upcoming |
| 06 | collections Module | ⏳ Upcoming |
| 07 | Weekly Review | ⏳ Upcoming |

---

## Folder Structure

```
Week-04_Data_Structures/
├── README.md                    ← You are here
├── Day-01/
│   ├── lesson.py                ← Lists
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-02/
│   ├── lesson.py                ← Tuples
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-03/
│   ├── lesson.py                ← Dictionaries
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-04/
│   ├── lesson.py                ← Sets
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-05/
│   ├── lesson.py                ← Comprehensions
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-06/
│   ├── lesson.py                ← collections Module
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
cd Week-04_Data_Structures/Day-01
python quiz.py
```

---

## Key Takeaways

```python
# Lists — ordered, mutable
lst = [1, 2, 3, 4, 5]
print(lst[-1])          # 5    (negative index)
print(lst[1:4])         # [2, 3, 4]   (slice)
lst.append(6)           # add to end
lst.sort()              # sort in place

# Tuples — ordered, immutable
point = (10, 20)
x, y = point            # unpacking

# Dictionaries — key → value
person = {"name": "Berke", "age": 21}
print(person["name"])   # Berke
person["city"] = "Warsaw"

# Sets — unique, unordered
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)            # {2, 3}  (intersection)
print(a | b)            # {1, 2, 3, 4}  (union)

# Comprehension (Day 05 preview)
squares = [x**2 for x in range(6)]   # [0, 1, 4, 9, 16, 25]

# Counter (Day 06 preview)
from collections import Counter
words = ["apple", "banana", "apple", "cherry"]
print(Counter(words))   # Counter({'apple': 2, 'banana': 1, 'cherry': 1})
```

---

## Prerequisites

Completed Week 03 — Functions. You should be comfortable with:
- Defining and calling functions
- *args, **kwargs, lambda, map, filter
- LEGB scope rule and closures
- Recursion with a base case
