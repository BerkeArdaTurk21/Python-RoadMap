# =============================================================================
# Week 07 - Day 01 | Import System & venv — Exercises
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Import and Use
# -----------------------------------------------------------------------------
# Using the math module, compute and print:
#   a) The hypotenuse of a right triangle with sides 3 and 4
#   b) log base 10 of 1000
#   c) ceil(4.2) and floor(4.8)
#
# Expected output:
#   Hypotenuse: 5.0
#   log10(1000): 3.0
#   ceil(4.2)=5, floor(4.8)=4

# TODO: import what you need and print the results
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Alias Imports
# -----------------------------------------------------------------------------
# Import the following with aliases and use them:
#   - datetime.date as d → print today's date
#   - collections.Counter as C → count letters in "mississippi"
#   - collections.defaultdict as dd → build a word-length dict
#     from ["hi", "hello", "hey", "world"] grouped by length
#
# Expected output:
#   Today: 2026-06-19  (date will vary)
#   Letter counts: Counter({'s': 4, 'i': 4, 'p': 2, 'm': 1})
#   By length: {2: ['hi'], 5: ['hello', 'world'], 3: ['hey']}

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 3 — __name__ Guard
# -----------------------------------------------------------------------------
# Create a module-style script in THIS file:
#   - Define a function add(a, b) that returns a + b
#   - Define a function multiply(a, b) that returns a * b
#   - Define a main() function that:
#       - Prints add(3, 4)
#       - Prints multiply(5, 6)
#   - Use if __name__ == "__main__": to call main()
#
# Expected output (when this file is run directly):
#   3 + 4 = 7
#   5 × 6 = 30

def add(a, b):
    pass  # TODO

def multiply(a, b):
    pass  # TODO

def main():
    pass  # TODO

if __name__ == "__main__":
    main()
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Explore sys.path
# -----------------------------------------------------------------------------
# Print:
#   a) The number of entries in sys.path
#   b) Whether '' (empty string, meaning current dir) is in sys.path
#   c) The Python version string (just major.minor, e.g. "3.11")
#
# Expected output (will vary by system):
#   sys.path entries: 7
#   Current dir in path: True
#   Python version: 3.11

import sys
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Module Introspection
# -----------------------------------------------------------------------------
# For the 'random' module:
#   a) Print where it is located (its __file__)
#   b) Print its __name__
#   c) List 5 names from dir(random) that do NOT start with '_'
#
# Expected output (will vary):
#   File: ...random.py
#   Name: random
#   5 public names: ['BPF', 'LOG4', 'NV_MAGICCONST', 'Random', 'SG_MAGICCONST']

import random
# TODO
