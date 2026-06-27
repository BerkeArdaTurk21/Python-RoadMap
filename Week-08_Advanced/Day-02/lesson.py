# =============================================================================
# Week 08 - Day 02 | Iterators
# =============================================================================
# An iterator is an object that produces values one at a time on demand.
# Understanding iterators explains how for loops, list comprehensions,
# zip(), map(), and many built-ins actually work under the hood.
#
# Topics:
#   1. Iterables vs Iterators — the key distinction
#   2. The iterator protocol: __iter__ and __next__
#   3. iter() and next() built-ins
#   4. How for loops work internally
#   5. StopIteration
#   6. Custom iterator class — Countdown
#   7. Custom iterator class — Fibonacci
#   8. Infinite iterators

# -----------------------------------------------------------------------------
# 1. Iterables vs Iterators
# -----------------------------------------------------------------------------
# ITERABLE:  An object you can loop over. Has __iter__() method.
#            Examples: list, tuple, str, dict, set, range
#
# ITERATOR:  An object that tracks position and yields one value at a time.
#            Has both __iter__() and __next__() methods.
#            Once exhausted, it cannot be reset.
#
# Key rule:  Every iterator is an iterable, but not every iterable is an iterator.

numbers = [1, 2, 3]          # list is an ITERABLE (not an iterator)
it = iter(numbers)            # iter() creates an ITERATOR from it

print(type(numbers))          # <class 'list'>
print(type(it))               # <class 'list_iterator'>

print(next(it))               # 1
print(next(it))               # 2
print(next(it))               # 3
# next(it)                    # StopIteration — iterator exhausted

# A list can produce many independent iterators:
it1 = iter(numbers)
it2 = iter(numbers)
print(next(it1))              # 1
print(next(it2))              # 1  (independent from it1)

# -----------------------------------------------------------------------------
# 2. The Iterator Protocol
# -----------------------------------------------------------------------------
# To make a class an iterator, implement two methods:
#
#   __iter__(self)    → returns self  (so the iterator is also an iterable)
#   __next__(self)    → returns the next value, raises StopIteration when done

class Countdown:
    """Counts down from n to 1."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self          # iterator returns itself

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

cd = Countdown(5)
print(next(cd))   # 5
print(next(cd))   # 4
print(next(cd))   # 3

# Because __iter__ returns self, you can use it in a for loop directly:
for n in Countdown(3):
    print(n, end=" ")    # 3 2 1
print()

# -----------------------------------------------------------------------------
# 3. iter() and next() Built-ins
# -----------------------------------------------------------------------------
# iter(obj)          → calls obj.__iter__()
# next(obj)          → calls obj.__next__()
# next(obj, default) → returns default instead of raising StopIteration

it = iter([10, 20, 30])
print(next(it))           # 10
print(next(it, "done"))   # 20
print(next(it, "done"))   # 30
print(next(it, "done"))   # done  (no StopIteration)

# iter() with a sentinel — two-argument form:
# iter(callable, sentinel) calls callable() repeatedly until it returns sentinel.
import io
data = io.StringIO("line1\nline2\nline3\n")
for line in iter(data.readline, ""):  # stop when readline returns ""
    print(line, end="")

# -----------------------------------------------------------------------------
# 4. How for Loops Work Internally
# -----------------------------------------------------------------------------
# This for loop:
#   for x in iterable:
#       do_something(x)
#
# Is equivalent to:
#   _it = iter(iterable)
#   while True:
#       try:
#           x = next(_it)
#       except StopIteration:
#           break
#       do_something(x)

fruits = ["apple", "banana", "cherry"]

# Manual version of for loop:
_it = iter(fruits)
while True:
    try:
        fruit = next(_it)
        print(fruit)
    except StopIteration:
        break

# -----------------------------------------------------------------------------
# 5. Checking the Protocol
# -----------------------------------------------------------------------------
# Use hasattr() to check if an object supports the iterator protocol.

def is_iterator(obj):
    return hasattr(obj, "__iter__") and hasattr(obj, "__next__")

def is_iterable(obj):
    return hasattr(obj, "__iter__")

print(is_iterable([1, 2, 3]))        # True  (list is iterable)
print(is_iterator([1, 2, 3]))        # False (list is NOT an iterator)
print(is_iterator(iter([1, 2, 3])))  # True  (list_iterator IS an iterator)
print(is_iterator(Countdown(5)))     # True  (our custom iterator)

# -----------------------------------------------------------------------------
# 6. Custom Iterator — Fibonacci Sequence
# -----------------------------------------------------------------------------

class Fibonacci:
    """Yields the Fibonacci sequence up to n terms."""

    def __init__(self, max_terms):
        self.max_terms = max_terms
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_terms:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

fib = Fibonacci(8)
print(list(fib))    # [0, 1, 1, 2, 3, 5, 8, 13]

# After exhaustion, the iterator is done — cannot be reused:
print(list(fib))    # []  (already exhausted)

# To iterate again, create a new instance:
print(list(Fibonacci(5)))   # [0, 1, 1, 2, 3]

# -----------------------------------------------------------------------------
# 7. Infinite Iterator
# -----------------------------------------------------------------------------
# Iterators don't have to end — just never raise StopIteration.
# Use itertools.islice or a manual break to stop.

class Counter:
    """Counts up from start indefinitely."""

    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += self.step
        return value

counter = Counter(start=1, step=2)   # odd numbers: 1, 3, 5, 7, ...

# Manually take 5 values from an infinite iterator:
first_five_odds = [next(counter) for _ in range(5)]
print(first_five_odds)   # [1, 3, 5, 7, 9]

# Or use itertools.islice:
import itertools
evens = Counter(start=0, step=2)
print(list(itertools.islice(evens, 6)))  # [0, 2, 4, 6, 8, 10]

# -----------------------------------------------------------------------------
# 8. Iterators from the Standard Library
# -----------------------------------------------------------------------------
import itertools

# zip() returns an iterator:
pairs = zip([1, 2, 3], ["a", "b", "c"])
print(type(pairs))          # <class 'zip'>
print(next(pairs))          # (1, 'a')
print(list(pairs))          # [(2, 'b'), (3, 'c')]

# enumerate() returns an iterator:
en = enumerate(["x", "y", "z"])
print(next(en))             # (0, 'x')

# map() returns an iterator:
squares = map(lambda x: x ** 2, range(5))
print(list(squares))        # [0, 1, 4, 9, 16]

# filter() returns an iterator:
evens_filter = filter(lambda x: x % 2 == 0, range(10))
print(list(evens_filter))   # [0, 2, 4, 6, 8]
