# =============================================================================
# Week 05 - Day 06 | Magic Methods — Solutions
# =============================================================================

from math import gcd

# -----------------------------------------------------------------------------
# Solution 1 — Fraction Class
# -----------------------------------------------------------------------------
# KEY INSIGHT: Reduce fractions in __init__ using GCD. All arithmetic methods
# return NEW Fraction instances (immutable style). __eq__ compares the already-
# reduced numerators and denominators.

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        common = gcd(abs(numerator), abs(denominator))
        sign   = -1 if denominator < 0 else 1
        self.n = sign * numerator   // common
        self.d = sign * denominator // common

    def __str__(self):
        if self.d == 1:
            return str(self.n)
        return f"{self.n}/{self.d}"

    def __repr__(self):
        return f"Fraction({self.n}, {self.d})"

    def __add__(self, other):
        return Fraction(self.n * other.d + other.n * self.d, self.d * other.d)

    def __sub__(self, other):
        return Fraction(self.n * other.d - other.n * self.d, self.d * other.d)

    def __mul__(self, other):
        return Fraction(self.n * other.n, self.d * other.d)

    def __eq__(self, other):
        return self.n == other.n and self.d == other.d

    def __lt__(self, other):
        return self.n * other.d < other.n * self.d


f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print(f1)
print(repr(f1))
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(Fraction(2, 4) == f1)
print(f2 < f1)
print()

# WHY reduce in __init__? So Fraction(2,4) and Fraction(1,2) are equal.
# Reducing once at creation is cleaner than reducing in every comparison.

# -----------------------------------------------------------------------------
# Solution 2 — Stack Class
# -----------------------------------------------------------------------------
# KEY INSIGHT: The internal list stores items with the TOP at index -1
# (last element). __str__ reverses for display. __contains__ delegates to
# the internal list's 'in' operator which calls list.__contains__.

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("peek at empty stack")
        return self._data[-1]

    def __len__(self):
        return len(self._data)

    def __bool__(self):
        return len(self._data) > 0

    def __contains__(self, item):
        return item in self._data

    def __str__(self):
        return f"Stack(top→bottom): {list(reversed(self._data))}"

    def __repr__(self):
        return f"Stack({self._data!r})"


s = Stack()
s.push(1); s.push(2); s.push(3)
print(s)
print(len(s))
print(s.peek())
print(bool(s))
s.pop()
print(s)
print(5 in s)
print()

# -----------------------------------------------------------------------------
# Solution 3 — Money Class
# -----------------------------------------------------------------------------

SYMBOLS = {"USD": "$", "EUR": "€", "GBP": "£"}

class Money:
    def __init__(self, amount, currency="USD"):
        self.amount   = float(amount)
        self.currency = currency

    def _check_currency(self, other):
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")

    def __str__(self):
        sym = SYMBOLS.get(self.currency, self.currency)
        return f"{sym}{self.amount:.2f}"

    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"

    def __add__(self, other):
        self._check_currency(other)
        return Money(self.amount + other.amount, self.currency)

    def __sub__(self, other):
        self._check_currency(other)
        return Money(self.amount - other.amount, self.currency)

    def __mul__(self, scalar):
        return Money(self.amount * scalar, self.currency)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other):
        self._check_currency(other)
        return self.amount < other.amount


m1 = Money(10, "USD")
m2 = Money(5,  "USD")
print(m1 + m2)
print(m1 - m2)
print(m1 * 2)
print(2 * m1 == Money(20, "USD"))
print(m2 < m1)
try:
    m1 + Money(5, "EUR")
except ValueError as e:
    print(f"ValueError raised: {e}")
print()

# -----------------------------------------------------------------------------
# Solution 4 — Matrix (2x2) Class
# -----------------------------------------------------------------------------

class Matrix:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def __str__(self):
        return f"[[{self.a}, {self.b}]\n [{self.c}, {self.d}]]"

    def __repr__(self):
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"

    def __add__(self, other):
        return Matrix(self.a+other.a, self.b+other.b,
                      self.c+other.c, self.d+other.d)

    def __mul__(self, other):
        return Matrix(
            self.a*other.a + self.b*other.c,
            self.a*other.b + self.b*other.d,
            self.c*other.a + self.d*other.c,
            self.c*other.b + self.d*other.d,
        )

    def __eq__(self, other):
        return (self.a == other.a and self.b == other.b and
                self.c == other.c and self.d == other.d)

    def __getitem__(self, index):
        if index == 0:
            return (self.a, self.b)
        if index == 1:
            return (self.c, self.d)
        raise IndexError("Matrix index must be 0 or 1")


m1 = Matrix(1, 2, 3, 4)
m2 = Matrix(5, 6, 7, 8)
print(m1)
print(m1 + m2)
print(m1 * m2)
print(m1[0])
print()

# -----------------------------------------------------------------------------
# Solution 5 — SortedList Class
# -----------------------------------------------------------------------------
# KEY INSIGHT: bisect.insort keeps the list sorted on every insertion in O(log n)
# without re-sorting the whole list each time. __iter__ just returns
# iter(self._data), delegating to list's built-in iterator.

import bisect

class SortedList:
    def __init__(self):
        self._data = []

    def add(self, item):
        bisect.insort(self._data, item)

    def remove(self, item):
        if item not in self._data:
            raise ValueError(f"{item} not in SortedList")
        self._data.remove(item)

    def __len__(self):
        return len(self._data)

    def __contains__(self, item):
        return item in self._data

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __str__(self):
        return f"SortedList({self._data})"

    def __repr__(self):
        return self.__str__()


sl = SortedList()
for x in [5, 3, 9, 1, 7]:
    sl.add(x)
print(sl)
print(len(sl))
print(5 in sl)
print(4 in sl)
print(sl[1])
print(' '.join(str(x) for x in sl))
sl.remove(3)
print(sl)

# WHY bisect.insort? It uses binary search to find the insertion point,
# then inserts in one step — O(n) total but much cleaner than sorting each time.
