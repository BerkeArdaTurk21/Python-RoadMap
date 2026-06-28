# =============================================================================
# Week 08 - Day 03 | Generators — Exercises
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Countdown Generator
# -----------------------------------------------------------------------------
# Write a generator function countdown(n) that yields n, n-1, ..., 1.
#
# Expected output:
#   5 4 3 2 1
#   [3, 2, 1]

# TODO: define countdown(n) here

# (uncomment to test)
# for x in countdown(5):
#     print(x, end=" ")
# print()
# print(list(countdown(3)))
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Even Numbers Generator Expression
# -----------------------------------------------------------------------------
# Using a single GENERATOR EXPRESSION (not a function), build `evens` that
# produces the even numbers from 0 to 20 inclusive. Then print the list and
# the sum WITHOUT building an intermediate list for the sum.
#
# Expected output:
#   [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
#   sum: 110

# TODO: evens = ...

# (uncomment to test)
# print(list(evens))
# print("sum:", sum(n for n in range(21) if n % 2 == 0))
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Infinite Fibonacci Generator
# -----------------------------------------------------------------------------
# Write an INFINITE generator fibonacci() that yields 0, 1, 1, 2, 3, 5, 8, ...
# forever. Use itertools.islice to take the first 10 values.
#
# Expected output:
#   [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

import itertools

# TODO: define fibonacci() here

# (uncomment to test)
# print(list(itertools.islice(fibonacci(), 10)))
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Running Maximum
# -----------------------------------------------------------------------------
# Write a generator running_max(numbers) that yields the largest value seen
# so far at each step.
#
# Expected output:
#   [3, 3, 7, 7, 7, 9]   ← from [3, 1, 7, 2, 5, 9]

# TODO: define running_max(numbers) here

# (uncomment to test)
# print(list(running_max([3, 1, 7, 2, 5, 9])))
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Pipeline with yield from
# -----------------------------------------------------------------------------
# Build a small text-processing pipeline of generators:
#   a) split_words(text)  -> yields each word (text.split())
#   b) clean(words)       -> yields each word lowercased, stripped of '.,!?'
#   c) long_words(words)  -> yields only words with length >= 4
# Then chain them: long_words(clean(split_words(text))).
#
# Also write merge(*iterables) that uses `yield from` to yield every item
# from each iterable in order.
#
# Expected output:
#   ['generators', 'lazy', 'memory', 'friendly']
#   [1, 2, 3, 10, 20]

text = "Generators are Lazy and memory friendly."

# TODO: define split_words, clean, long_words, and merge here

# (uncomment to test)
# print(list(long_words(clean(split_words(text)))))
# print(list(merge([1, 2, 3], (10, 20))))
print()
