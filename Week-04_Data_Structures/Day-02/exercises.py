# =============================================================================
# Week 04 - Day 02 | Tuples — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Unpack a Record
# -----------------------------------------------------------------------------
# You are given a tuple representing a student record:
#   (name, age, grade, city)
#
# Unpack it into individual variables and print each on its own line
# using the format shown below.
#
# Expected output:
#   Name : Alice
#   Age  : 20
#   Grade: A
#   City : London

student = ("Alice", 20, "A", "London")

# TODO: unpack student and print each field
print("Exercise 1 — Unpack a Record")
# your code here
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Swap Without a Temp Variable
# -----------------------------------------------------------------------------
# Use tuple unpacking to swap x and y WITHOUT using a third variable.
#
# Expected output:
#   Before: x=10, y=25
#   After:  x=25, y=10

x = 10
y = 25

print("Exercise 2 — Swap Variables")
print(f"Before: x={x}, y={y}")
# TODO: swap x and y using tuple unpacking
print(f"After:  x={x}, y={y}")
print()

# -----------------------------------------------------------------------------
# Exercise 3 — First, Middle, Last
# -----------------------------------------------------------------------------
# Write split_tuple(t) that uses extended unpacking (*) to return a tuple of
# three items: (first_element, middle_elements_as_list, last_element).
#
# Expected output:
#   split_tuple((1, 2, 3, 4, 5))   → (1, [2, 3, 4], 5)
#   split_tuple((10, 20, 30))       → (10, [20], 30)
#   split_tuple(('a', 'b', 'c', 'd')) → ('a', ['b', 'c'], 'd')

def split_tuple(t):
    pass  # TODO: use extended unpacking


print("Exercise 3 — First, Middle, Last")
print(split_tuple((1, 2, 3, 4, 5)))          # (1, [2, 3, 4], 5)
print(split_tuple((10, 20, 30)))              # (10, [20], 30)
print(split_tuple(("a", "b", "c", "d")))     # ('a', ['b', 'c'], 'd')
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Named Tuple: Playing Card
# -----------------------------------------------------------------------------
# Define a namedtuple called Card with fields: rank, suit
#
# Then:
# 1. Create these cards: Ace of Spades, King of Hearts, 7 of Diamonds
# 2. Print each card in the format: "rank of suit"
# 3. Print the rank of the second card using the named field
#
# Expected output:
#   Ace of Spades
#   King of Hearts
#   7 of Diamonds
#   Rank of second card: King

from collections import namedtuple

# TODO: define Card namedtuple and create the three cards

print("Exercise 4 — Named Tuple: Playing Card")
# your code here
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Zip & Unzip
# -----------------------------------------------------------------------------
# Part A: Given two lists, combine them into a list of tuples using zip().
# Part B: Given a list of tuples, split it back into two separate tuples.
#
# Expected output:
#   Zipped:   [(1, 'a'), (2, 'b'), (3, 'c')]
#   Numbers:  (1, 2, 3)
#   Letters:  ('a', 'b', 'c')

numbers = [1, 2, 3]
letters = ["a", "b", "c"]

print("Exercise 5 — Zip & Unzip")
# TODO Part A: zip numbers and letters into a list of tuples called 'paired'

# TODO Part B: unzip 'paired' back into two tuples called 'nums_back' and 'lets_back'
#   Hint: zip(*paired) transposes; wrap in tuple()

# print(f"Zipped:   {paired}")
# print(f"Numbers:  {nums_back}")
# print(f"Letters:  {lets_back}")
