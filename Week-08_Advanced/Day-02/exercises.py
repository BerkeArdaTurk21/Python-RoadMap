# =============================================================================
# Week 08 - Day 02 | Iterators — Exercises
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Manual Iteration
# -----------------------------------------------------------------------------
# Given the list below, use iter() and next() MANUALLY (no for loop) to:
#   a) Create an iterator from the list
#   b) Print each element one by one using next()
#   c) Print "done" using the default parameter of next() when exhausted
#
# Expected output:
#   red
#   green
#   blue
#   done

colors = ["red", "green", "blue"]

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Custom Range Iterator
# -----------------------------------------------------------------------------
# Build a class called MyRange that works like range(start, stop, step).
# It must implement __iter__ and __next__.
#
# Expected output:
#   2 5 8 11
#   (loop over MyRange(2, 12, 3) and print each value space-separated)
#
# Also verify:
#   list(MyRange(0, 5, 1))  →  [0, 1, 2, 3, 4]
#   list(MyRange(10, 0, -2)) →  [10, 8, 6, 4, 2]

# TODO: define MyRange class here

# (uncomment to test)
# for n in MyRange(2, 12, 3):
#     print(n, end=" ")
# print()
# print(list(MyRange(0, 5, 1)))
# print(list(MyRange(10, 0, -2)))
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Fibonacci Iterator
# -----------------------------------------------------------------------------
# Build a class called FibIter(n) that yields the first n Fibonacci numbers.
#
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
#
# Expected output:
#   [0, 1, 1, 2, 3, 5, 8, 13]   ← list(FibIter(8))
#   First 5: 0 1 1 2 3           ← loop over FibIter(5)

# TODO: define FibIter class here

# (uncomment to test)
# print(list(FibIter(8)))
# print("First 5:", *FibIter(5))
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Filtering Iterator
# -----------------------------------------------------------------------------
# Build a class called EvenFilter(iterable) that wraps any iterable and
# yields only the even numbers from it.
#
# Expected output:
#   [0, 2, 4, 6, 8, 10]
#   [2, 4, 6]
#
# Hint: use iter() on the wrapped iterable in __init__,
#       then call next() on it in __next__.

# TODO: define EvenFilter class here

# (uncomment to test)
# print(list(EvenFilter(range(11))))
# print(list(EvenFilter([1, 2, 3, 4, 5, 6, 7])))
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Infinite Counter with islice
# -----------------------------------------------------------------------------
# Build an infinite iterator called InfiniteCounter(start=0, step=1) that
# counts forever. Then use itertools.islice to safely take the first 5 values.
#
# Expected output:
#   [0, 1, 2, 3, 4]
#   [10, 15, 20, 25, 30]   ← InfiniteCounter(10, 5), first 5
#
# Verify: calling next() many times never raises StopIteration.

import itertools

# TODO: define InfiniteCounter class here

# (uncomment to test)
# print(list(itertools.islice(InfiniteCounter(), 5)))
# print(list(itertools.islice(InfiniteCounter(10, 5), 5)))
print()
