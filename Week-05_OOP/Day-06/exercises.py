# =============================================================================
# Week 05 - Day 06 | Magic Methods — Exercises
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Fraction Class
# -----------------------------------------------------------------------------
# Create a Fraction class that represents p/q:
#   - __init__(self, numerator, denominator)  ← raise ValueError if denom=0
#     Automatically reduce to lowest terms using GCD
#   - __str__   → "3/4"   (or just "2" if denominator is 1)
#   - __repr__  → "Fraction(3, 4)"
#   - __add__   → returns new Fraction  (a/b + c/d = (ad+bc)/bd)
#   - __sub__   → returns new Fraction
#   - __mul__   → returns new Fraction  (a/b * c/d = ac/bd)
#   - __eq__    → True if same value after reduction
#   - __lt__    → compares cross-multiplied numerators
#
# Expected output:
#   1/2
#   Fraction(1, 2)
#   3/4
#   1/4
#   1/8
#   True
#   True

from math import gcd

class Fraction:
    pass  # TODO


f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print(f1)                    # 1/2
print(repr(f1))              # Fraction(1, 2)
print(f1 + f2)               # 3/4
print(f1 - f2)               # 1/4
print(f1 * f2)               # 1/8
print(Fraction(2, 4) == f1)  # True  (2/4 == 1/2)
print(f2 < f1)               # True  (1/4 < 1/2)
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Stack Class
# -----------------------------------------------------------------------------
# Implement a Stack with magic methods:
#   - __init__(self)
#   - push(self, item)     ← adds to top
#   - pop(self)            ← removes and returns top; raise IndexError if empty
#   - peek(self)           ← returns top without removing; raise IndexError if empty
#   - __len__              ← number of items
#   - __bool__             ← True if not empty
#   - __contains__(item)   ← True if item in stack
#   - __str__              ← "Stack(top→bottom): [3, 2, 1]"
#   - __repr__             ← "Stack([1, 2, 3])"
#
# Expected output:
#   Stack(top→bottom): [3, 2, 1]
#   3
#   3
#   True
#   Stack(top→bottom): [2, 1]
#   False

class Stack:
    pass  # TODO


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s)             # Stack(top→bottom): [3, 2, 1]
print(len(s))        # 3
print(s.peek())      # 3
print(bool(s))       # True
s.pop()
print(s)             # Stack(top→bottom): [2, 1]
print(5 in s)        # False
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Money Class
# -----------------------------------------------------------------------------
# Create a Money class with currency support:
#   - __init__(self, amount, currency="USD")
#   - __str__   → "$10.00" for USD, "€10.00" for EUR, "£10.00" for GBP
#   - __repr__  → "Money(10.0, 'USD')"
#   - __add__   → only same currency; raise ValueError otherwise
#   - __sub__   → only same currency; raise ValueError otherwise
#   - __mul__   → Money * float or int (scaling)
#   - __rmul__  → float * Money
#   - __eq__    → same amount and same currency
#   - __lt__    → same currency only; raise ValueError otherwise
#
# Expected output:
#   $15.00
#   $5.00
#   $20.00
#   True
#   True
#   ValueError raised: Cannot add USD and EUR

SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£"}

class Money:
    pass  # TODO


m1 = Money(10, "USD")
m2 = Money(5,  "USD")
print(m1 + m2)               # $15.00
print(m1 - m2)               # $5.00
print(m1 * 2)                # $20.00
print(2 * m1 == Money(20, "USD"))  # True
print(m2 < m1)               # True

try:
    m1 + Money(5, "EUR")
except ValueError as e:
    print(f"ValueError raised: {e}")
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Matrix (2x2) Class
# -----------------------------------------------------------------------------
# Create a Matrix class for 2x2 matrices:
#   - __init__(self, a, b, c, d)  ← [[a, b], [c, d]]
#   - __str__   → "[[1, 2]\n [3, 4]]"
#   - __repr__  → "Matrix(1, 2, 3, 4)"
#   - __add__   → element-wise addition
#   - __mul__   → matrix multiplication  (standard 2x2 × 2x2)
#   - __eq__    → all elements equal
#   - __getitem__(self, index) → row as tuple: m[0] = (a,b), m[1] = (c,d)
#
# Matrix multiplication formula for [[a,b],[c,d]] * [[e,f],[g,h]]:
#   result[0][0] = a*e + b*g,  result[0][1] = a*f + b*h
#   result[1][0] = c*e + d*g,  result[1][1] = c*f + d*h
#
# Expected output:
#   [[1, 2]
#    [3, 4]]
#   [[6, 8]
#    [10, 12]]
#   [[19, 22]
#    [43, 50]]
#   (1, 2)

class Matrix:
    pass  # TODO


m1 = Matrix(1, 2, 3, 4)
m2 = Matrix(5, 6, 7, 8)
print(m1)
print(m1 + m2)
print(m1 * m2)
print(m1[0])
print()

# -----------------------------------------------------------------------------
# Exercise 5 — SortedList Class
# -----------------------------------------------------------------------------
# Create a SortedList that keeps items sorted at all times:
#   - __init__(self)
#   - add(self, item)       ← inserts in sorted position
#   - remove(self, item)    ← removes item; raise ValueError if not found
#   - __len__
#   - __contains__
#   - __getitem__           ← index access
#   - __iter__              ← makes it iterable
#   - __str__               ← "SortedList([1, 3, 5, 7])"
#   - __repr__              ← same as __str__
#
# Expected output:
#   SortedList([1, 3, 5, 7, 9])
#   5
#   True
#   False
#   3
#   1 3 5 7 9
#   SortedList([1, 5, 7, 9])

class SortedList:
    pass  # TODO


sl = SortedList()
for x in [5, 3, 9, 1, 7]:
    sl.add(x)

print(sl)              # SortedList([1, 3, 5, 7, 9])
print(len(sl))         # 5
print(5 in sl)         # True
print(4 in sl)         # False
print(sl[1])           # 3
print(' '.join(str(x) for x in sl))  # 1 3 5 7 9
sl.remove(3)
print(sl)              # SortedList([1, 5, 7, 9])
