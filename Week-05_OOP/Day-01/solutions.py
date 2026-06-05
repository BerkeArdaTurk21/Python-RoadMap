# =============================================================================
# Week 05 - Day 01 | Classes & Objects — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — BankAccount Class
# -----------------------------------------------------------------------------
# KEY INSIGHT: Use a float for balance and format it with :.2f in __str__.
# withdraw() must check the balance BEFORE subtracting to avoid going negative.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner   = owner
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account[{self.owner}]: ${self.balance:.2f}"

acc = BankAccount("Alice")
print(acc)                  # Account[Alice]: $0.00
acc.deposit(500)
print(acc)                  # Account[Alice]: $500.00
acc.withdraw(150)
print(acc)                  # Account[Alice]: $350.00
acc.withdraw(1000)          # Insufficient funds
print(acc.get_balance())    # 350.0
print()

# WHY default balance=0? It lets you create BankAccount("Alice") without
# specifying a starting balance — common and convenient.

# -----------------------------------------------------------------------------
# Solution 2 — Temperature Converter
# -----------------------------------------------------------------------------
# KEY INSIGHT: The celsius value is stored once in __init__; the conversion
# methods COMPUTE and RETURN — they don't store extra attributes.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def is_boiling(self):
        return self.celsius >= 100

    def is_freezing(self):
        return self.celsius <= 0

    def __str__(self):
        return f"{self.celsius}°C"

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
# Solution 3 — Student Class
# -----------------------------------------------------------------------------
# KEY INSIGHT: Store grades in a dict {subject: grade} for O(1) lookup.
# average() guards against division-by-zero with an empty check.
# highest() uses max() with key=lambda so it works on the dict values.

class Student:
    def __init__(self, name, student_id):
        self.name       = name
        self.student_id = student_id
        self.grades     = {}   # {subject: grade}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

    def highest(self):
        return max(self.grades.items(), key=lambda item: item[1])

    def __str__(self):
        return (f"Student[{self.student_id}] {self.name} "
                f"— avg: {self.average():.1f}")

s = Student("Alice", "S001")
print(s)                    # Student[S001] Alice — avg: 0.0
s.add_grade("Math",    95)
s.add_grade("English", 82)
s.add_grade("Science", 83)
print(s)                    # Student[S001] Alice — avg: 86.7
print(s.highest())          # ('Math', 95)
print()

# WHY max(..., key=lambda item: item[1])?
# grades.items() gives [('Math', 95), ('English', 82), ...]
# We want the item with the HIGHEST grade (index 1), not alphabetical order.

# -----------------------------------------------------------------------------
# Solution 4 — Vector2D Class
# -----------------------------------------------------------------------------
# KEY INSIGHT: add() and scale() return NEW Vector2D objects — they do NOT
# modify self. This is the "immutable" style and avoids side-effect bugs.

import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitude(self):
        return round(math.sqrt(self.x ** 2 + self.y ** 2), 4)

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def scale(self, factor):
        return Vector2D(self.x * factor, self.y * factor)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

v1 = Vector2D(3, 4)
v2 = Vector2D(3, 5)

print(v1)                    # Vector2D(3, 4)
print(v1.magnitude())        # 5.0
print(v1.add(v2))            # Vector2D(6, 9)
print(v1.scale(2))           # Vector2D(6, 8)
print(v1.dot(v2))            # 29
print()

# WHY return new objects instead of modifying self?
# It lets you chain or compare without accidentally changing the original:
#   v3 = v1.add(v2)   ← v1 is still Vector2D(3, 4)

# -----------------------------------------------------------------------------
# Solution 5 — Queue Class
# -----------------------------------------------------------------------------
# KEY INSIGHT: A Python list naturally supports append() (back) and pop(0)
# (front), so it's a convenient backing store for a FIFO queue.
# peek() reads index 0 without removing — just guard against empty first.

class Queue:
    def __init__(self):
        self._items = []   # internal list; _ signals "don't touch from outside"

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __str__(self):
        return f"Queue[front → back]: {self._items}"

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

# WHY prefix _items with underscore?
# The single underscore is a Python convention for "internal / private".
# It tells other developers not to access _items directly — use the methods.
# (True private attributes with name-mangling use __ — covered in Day 04.)
