# =============================================================================
# Week 08 - Day 03 | Generators — Solutions
# =============================================================================

import itertools

# -----------------------------------------------------------------------------
# Solution 1 — Countdown Generator
# -----------------------------------------------------------------------------

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(5):
    print(x, end=" ")
print()
print(list(countdown(3)))
print()

# -----------------------------------------------------------------------------
# Solution 2 — Even Numbers Generator Expression
# -----------------------------------------------------------------------------

evens = (n for n in range(21) if n % 2 == 0)

print(list(evens))
print("sum:", sum(n for n in range(21) if n % 2 == 0))
print()

# -----------------------------------------------------------------------------
# Solution 3 — Infinite Fibonacci Generator
# -----------------------------------------------------------------------------

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(list(itertools.islice(fibonacci(), 10)))
print()

# -----------------------------------------------------------------------------
# Solution 4 — Running Maximum
# -----------------------------------------------------------------------------

def running_max(numbers):
    current = None
    for n in numbers:
        current = n if current is None else max(current, n)
        yield current

print(list(running_max([3, 1, 7, 2, 5, 9])))
print()

# -----------------------------------------------------------------------------
# Solution 5 — Pipeline with yield from
# -----------------------------------------------------------------------------

def split_words(text):
    for word in text.split():
        yield word

def clean(words):
    for word in words:
        yield word.lower().strip(".,!?")

def long_words(words):
    for word in words:
        if len(word) >= 4:
            yield word

def merge(*iterables):
    for it in iterables:
        yield from it

text = "Generators are Lazy and memory friendly."

print(list(long_words(clean(split_words(text)))))
print(list(merge([1, 2, 3], (10, 20))))
