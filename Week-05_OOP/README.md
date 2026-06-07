# Week 05 — OOP (Object-Oriented Programming)

> **Level:** Intermediate
> **Goal:** Understand and apply OOP principles in Python — classes, inheritance, encapsulation, polymorphism, and magic methods.

---

## What You Will Learn

By the end of this week you will be able to:

- Define **classes** and create **objects** (instances)
- Use **instance and class variables**, class methods, and static methods
- Apply **inheritance** with `super()` and method overriding
- Implement **encapsulation** with private attributes and `@property`
- Understand **polymorphism** and duck typing
- Use **magic methods** (`__str__`, `__repr__`, `__len__`, `__eq__`, `__add__`)

---

## Daily Breakdown

| Day | Topic | Key Concepts |
|-----|-------|-------------|
| 01 | Classes & Objects | class, `__init__`, self, instance creation |
| 02 | Instance & Class Variables | instance vs class scope, class methods, static methods |
| 03 | Inheritance | super(), method override, isinstance(), issubclass() |
| 04 | Encapsulation | private/protected attributes, getters, setters, @property |
| 05 | Polymorphism | duck typing, method overriding, operator overloading |
| 06 | Magic Methods | `__str__`, `__repr__`, `__len__`, `__eq__`, `__add__` |
| 07 | Weekly Review | weekly_quiz.py (10 MCQ + 5 code challenges) + weekly project |

---

## Progress

| Day | Topic | Status |
|-----|-------|--------|
| 01 | Classes & Objects | ✅ Done |
| 02 | Instance & Class Variables | ✅ Done |
| 03 | Inheritance | ✅ Done |
| 04 | Encapsulation | ⏳ Upcoming |
| 05 | Polymorphism | ⏳ Upcoming |
| 06 | Magic Methods | ⏳ Upcoming |
| 07 | Weekly Review | ⏳ Upcoming |

---

## Folder Structure

```
Week-05_OOP/
├── README.md                    ← You are here
├── Day-01/
│   ├── lesson.py                ← Classes & Objects
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-02/
│   ├── lesson.py                ← Instance & Class Variables
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-03/
│   ├── lesson.py                ← Inheritance
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-04/
│   ├── lesson.py                ← Encapsulation
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-05/
│   ├── lesson.py                ← Polymorphism
│   ├── lesson.ipynb
│   ├── quiz.py
│   ├── exercises.py
│   └── solutions.py
├── Day-06/
│   ├── lesson.py                ← Magic Methods
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
cd Week-05_OOP/Day-01
python quiz.py
```

---

## Key Takeaways

```python
# Define a class
class Dog:
    def __init__(self, name, breed):
        self.name  = name    # instance attribute
        self.breed = breed

    def bark(self):
        return f"{self.name} says: Woof!"

# Create instances
rex  = Dog("Rex", "Labrador")
luna = Dog("Luna", "Husky")

print(rex.bark())    # Rex says: Woof!
print(luna.name)     # Luna

# Each instance has its own data
rex.age  = 3         # add attribute after creation
print(rex.age)       # 3
# luna.age → AttributeError (luna doesn't have it)
```

---

## Prerequisites

Completed Week 04 — Data Structures. You should be comfortable with:
- Lists, tuples, dicts, sets and their methods
- List/dict/set comprehensions
- The `collections` module (Counter, defaultdict, deque)
- Functions: def, *args, **kwargs, lambda, scope, closures
