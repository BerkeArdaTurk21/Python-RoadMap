# =============================================================================
# Week 05 - Day 01 | Classes & Objects — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — BankAccount Class
# -----------------------------------------------------------------------------
# Create a BankAccount class with:
#   - __init__(self, owner, balance=0)  ← balance defaults to 0
#   - deposit(self, amount)             ← adds amount to balance
#   - withdraw(self, amount)            ← subtracts amount IF balance is enough;
#                                          otherwise print "Insufficient funds"
#   - get_balance(self)                 ← returns current balance
#   - __str__                           ← "Account[Alice]: $250.00"
#
# Expected output:
#   Account[Alice]: $0.00
#   Account[Alice]: $500.00
#   Account[Alice]: $350.00
#   Insufficient funds
#   350.00

class BankAccount:
    pass  # TODO


acc = BankAccount("Alice")
print(acc)                  # Account[Alice]: $0.00
acc.deposit(500)
print(acc)                  # Account[Alice]: $500.00
acc.withdraw(150)
print(acc)                  # Account[Alice]: $350.00
acc.withdraw(1000)          # Insufficient funds
print(acc.get_balance())    # 350.0
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Temperature Converter
# -----------------------------------------------------------------------------
# Create a Temperature class with:
#   - __init__(self, celsius)
#   - to_fahrenheit(self)   → returns (celsius * 9/5) + 32
#   - to_kelvin(self)       → returns celsius + 273.15
#   - is_boiling(self)      → True if celsius >= 100
#   - is_freezing(self)     → True if celsius <= 0
#   - __str__               → "25°C"
#
# Expected output:
#   25°C
#   77.0
#   298.15
#   False
#   False
#   100°C
#   True

class Temperature:
    pass  # TODO


t1 = Temperature(25)
print(t1)                   # 25°C
print(t1.to_fahrenheit())   # 77.0
print(t1.to_kelvin())       # 298.15
print(t1.is_boiling())      # False
print(t1.is_freezing())     # False

t2 = Temperature(100)
print(t2)                   # 100°C
print(t2.is_boiling())      # True
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Student Class
# -----------------------------------------------------------------------------
# Create a Student class with:
#   - __init__(self, name, student_id)
#   - add_grade(self, subject, grade)   ← stores subject → grade in a dict
#   - average(self)                     ← returns average of all grades,
#                                          or 0.0 if no grades yet
#   - highest(self)                     ← returns (subject, grade) of best grade
#   - __str__                           ← "Student[S001] Alice — avg: 88.3"
#
# Expected output:
#   Student[S001] Alice — avg: 0.0
#   Student[S001] Alice — avg: 86.7
#   ('Math', 95)

class Student:
    pass  # TODO


s = Student("Alice", "S001")
print(s)                    # Student[S001] Alice — avg: 0.0
s.add_grade("Math",    95)
s.add_grade("English", 82)
s.add_grade("Science", 83)
print(s)                    # Student[S001] Alice — avg: 86.7
print(s.highest())          # ('Math', 95)
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Vector2D Class
# -----------------------------------------------------------------------------
# Create a Vector2D class representing a 2D vector (x, y) with:
#   - __init__(self, x, y)
#   - magnitude(self)          → sqrt(x² + y²), rounded to 4 decimal places
#   - add(self, other)         → returns a NEW Vector2D that is self + other
#   - scale(self, factor)      → returns a NEW Vector2D with x and y multiplied
#   - dot(self, other)         → dot product: self.x*other.x + self.y*other.y
#   - __str__                  → "Vector2D(3, 4)"
#
# Expected output:
#   Vector2D(3, 4)
#   5.0
#   Vector2D(6, 9)
#   Vector2D(6, 8)
#   25

class Vector2D:
    pass  # TODO


import math

v1 = Vector2D(3, 4)
v2 = Vector2D(3, 5)

print(v1)                    # Vector2D(3, 4)
print(v1.magnitude())        # 5.0
print(v1.add(v2))            # Vector2D(6, 9)
print(v1.scale(2))           # Vector2D(6, 8)
print(v1.dot(v2))            # 29
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Queue Class
# -----------------------------------------------------------------------------
# Implement a Queue (FIFO — First In, First Out) class using a list internally.
#   - __init__(self)
#   - enqueue(self, item)   ← adds item to the back of the queue
#   - dequeue(self)         ← removes and returns the FRONT item;
#                              if empty, print "Queue is empty" and return None
#   - peek(self)            ← returns front item WITHOUT removing it;
#                              if empty, return None
#   - is_empty(self)        ← returns True if queue has no items
#   - size(self)            ← returns number of items
#   - __str__               ← "Queue[front → back]: [1, 2, 3]"
#
# Expected output:
#   True
#   Queue[front → back]: [10, 20, 30]
#   3
#   10
#   10
#   Queue[front → back]: [20, 30]
#   Queue is empty

class Queue:
    pass  # TODO


q = Queue()
print(q.is_empty())          # True
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print(q)                     # Queue[front → back]: [10, 20, 30]
print(q.size())              # 3
print(q.peek())              # 10
print(q.dequeue())           # 10
print(q)                     # Queue[front → back]: [20, 30]
q.dequeue()
q.dequeue()
q.dequeue()                  # Queue is empty
