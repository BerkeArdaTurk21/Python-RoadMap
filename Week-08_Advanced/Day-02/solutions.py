# =============================================================================
# Week 08 - Day 02 | Iterators — Solutions
# =============================================================================

import itertools

# -----------------------------------------------------------------------------
# Solution 1 — Manual Iteration
# -----------------------------------------------------------------------------

colors = ["red", "green", "blue"]

it = iter(colors)
print(next(it))             # red
print(next(it))             # green
print(next(it))             # blue
print(next(it, "done"))     # done
print()

# -----------------------------------------------------------------------------
# Solution 2 — Custom Range Iterator
# -----------------------------------------------------------------------------

class MyRange:
    def __init__(self, start, stop, step=1):
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        if self.step < 0 and self.current <= self.stop:
            raise StopIteration
        value = self.current
        self.current += self.step
        return value

for n in MyRange(2, 12, 3):
    print(n, end=" ")
print()
print(list(MyRange(0, 5, 1)))
print(list(MyRange(10, 0, -2)))
print()

# -----------------------------------------------------------------------------
# Solution 3 — Fibonacci Iterator
# -----------------------------------------------------------------------------

class FibIter:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        value = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return value

print(list(FibIter(8)))
print("First 5:", *FibIter(5))
print()

# -----------------------------------------------------------------------------
# Solution 4 — Filtering Iterator
# -----------------------------------------------------------------------------

class EvenFilter:
    def __init__(self, iterable):
        self._it = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            value = next(self._it)    # raises StopIteration when source is exhausted
            if value % 2 == 0:
                return value

print(list(EvenFilter(range(11))))
print(list(EvenFilter([1, 2, 3, 4, 5, 6, 7])))
print()

# -----------------------------------------------------------------------------
# Solution 5 — Infinite Counter with islice
# -----------------------------------------------------------------------------

class InfiniteCounter:
    def __init__(self, start=0, step=1):
        self.current = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        value = self.current
        self.current += self.step
        return value

print(list(itertools.islice(InfiniteCounter(), 5)))
print(list(itertools.islice(InfiniteCounter(10, 5), 5)))
