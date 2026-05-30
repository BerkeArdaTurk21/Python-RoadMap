# =============================================================================
# Week 04 - Day 02 | Tuples — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================

from collections import namedtuple

# -----------------------------------------------------------------------------
# Solution 1 — Unpack a Record
# -----------------------------------------------------------------------------
# KEY INSIGHT: Assign each position to a named variable in one line.
# The number of variables must match the tuple length.

student = ("Alice", 20, "A", "London")

name, age, grade, city = student

print("Solution 1 — Unpack a Record")
print(f"Name : {name}")
print(f"Age  : {age}")
print(f"Grade: {grade}")
print(f"City : {city}")
print()

# -----------------------------------------------------------------------------
# Solution 2 — Swap Without a Temp Variable
# -----------------------------------------------------------------------------
# KEY INSIGHT: Python evaluates the RIGHT side fully before assigning.
# x, y = y, x  packs (y, x) into a tuple then unpacks into x, y.
# No temporary variable needed.

x = 10
y = 25

print("Solution 2 — Swap Variables")
print(f"Before: x={x}, y={y}")
x, y = y, x            # tuple packing + unpacking in one step
print(f"After:  x={x}, y={y}")
print()

# -----------------------------------------------------------------------------
# Solution 3 — First, Middle, Last
# -----------------------------------------------------------------------------
# KEY INSIGHT: a, *b, c = t
#   a → first element
#   *b → everything in between (as a list)
#   c → last element
# Return them packed as a tuple using (a, b, c).

def split_tuple(t):
    first, *middle, last = t
    return (first, middle, last)

print("Solution 3 — First, Middle, Last")
print(split_tuple((1, 2, 3, 4, 5)))          # (1, [2, 3, 4], 5)
print(split_tuple((10, 20, 30)))              # (10, [20], 30)
print(split_tuple(("a", "b", "c", "d")))     # ('a', ['b', 'c'], 'd')
print()

# -----------------------------------------------------------------------------
# Solution 4 — Named Tuple: Playing Card
# -----------------------------------------------------------------------------
# KEY INSIGHT: namedtuple("Card", ["rank", "suit"]) creates a class where
# each element has a name. Access by attribute (card.rank) OR index (card[0]).
# Still immutable — just more readable than plain tuples.

Card = namedtuple("Card", ["rank", "suit"])

ace_of_spades  = Card("Ace", "Spades")
king_of_hearts = Card("King", "Hearts")
seven_of_diamonds = Card("7", "Diamonds")

cards = [ace_of_spades, king_of_hearts, seven_of_diamonds]

print("Solution 4 — Named Tuple: Playing Card")
for card in cards:
    print(f"{card.rank} of {card.suit}")

print(f"Rank of second card: {king_of_hearts.rank}")
print()

# -----------------------------------------------------------------------------
# Solution 5 — Zip & Unzip
# -----------------------------------------------------------------------------
# KEY INSIGHT (Part A):
#   zip(a, b) produces pairs lazily — wrap with list() to materialise.
#   Result: [(1,'a'), (2,'b'), (3,'c')]
#
# KEY INSIGHT (Part B):
#   zip(*paired) "transposes" — unpacks each tuple as an argument to zip.
#   zip(*[(1,'a'),(2,'b'),(3,'c')]) → zip((1,2,3), ('a','b','c'))
#   Each result of zip is a tuple of corresponding elements.

numbers = [1, 2, 3]
letters = ["a", "b", "c"]

# Part A — zip
paired = list(zip(numbers, letters))

# Part B — unzip
nums_back, lets_back = zip(*paired)

print("Solution 5 — Zip & Unzip")
print(f"Zipped:   {paired}")
print(f"Numbers:  {nums_back}")
print(f"Letters:  {lets_back}")
print()

# WHY zip(*paired) works:
# *paired unpacks the list: zip(*[(1,'a'),(2,'b'),(3,'c')])
#                        = zip((1,'a'), (2,'b'), (3,'c'))
# zip groups by position → (1,2,3) and ('a','b','c')
