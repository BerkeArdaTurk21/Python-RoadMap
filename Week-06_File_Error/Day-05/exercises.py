# =============================================================================
# Week 06 - Day 05 | Raising Exceptions — Exercises
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Validated Rectangle
# -----------------------------------------------------------------------------
# Create a Rectangle class with width and height.
# In __init__, raise ValueError if either dimension is <= 0.
# Add an area() method and a __repr__.
#
# Expected output:
#   Rectangle(4x6) — area 24
#   ValueError: Width must be > 0, got -1
#   ValueError: Height must be > 0, got 0

class Rectangle:
    pass  # TODO

try:
    r = Rectangle(4, 6)
    print(f"{r} — area {r.area()}")
    Rectangle(-1, 5)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    Rectangle(3, 0)
except ValueError as e:
    print(f"ValueError: {e}")
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Stack with NotImplementedError
# -----------------------------------------------------------------------------
# Create a base class AbstractContainer with methods push, pop, peek.
# Each method should raise NotImplementedError("subclass must implement <name>").
# Create a ListStack subclass that actually implements all three.
#
# Expected output:
#   10
#   10
#   10
#   NotImplementedError: subclass must implement push

class AbstractContainer:
    pass  # TODO

class ListStack(AbstractContainer):
    pass  # TODO

s = ListStack()
s.push(10)
print(s.peek())   # 10
print(s.pop())    # 10

try:
    base = AbstractContainer()
    base.push(1)
except NotImplementedError as e:
    print(f"NotImplementedError: {e}")
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Chain Exceptions
# -----------------------------------------------------------------------------
# Write load_data(path) that:
#   - Opens the file (may raise FileNotFoundError)
#   - Wraps it in a RuntimeError using raise ... from ...
#     message: "Failed to load data from <path>"
# Also write load_data_silent(path) that suppresses the original cause
# using raise ... from None
#
# Expected output:
#   RuntimeError: Failed to load data from missing.csv
#   Has cause: True
#   ---
#   RuntimeError: Failed to load data (silent)
#   Has cause: False

def load_data(path):
    pass  # TODO

def load_data_silent(path):
    pass  # TODO

try:
    load_data("missing.csv")
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    print(f"Has cause: {e.__cause__ is not None}")
print("---")
try:
    load_data_silent("missing.csv")
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    print(f"Has cause: {e.__cause__ is not None}")
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Assert Invariants
# -----------------------------------------------------------------------------
# Write a function merge_sorted(a, b) that merges two sorted lists.
# Use assert to verify that both inputs are lists.
# Use assert to verify that each list is actually sorted (ascending).
# Then perform the merge and return the result.
#
# Expected output:
#   [1, 2, 3, 4, 5, 6]
#   AssertionError: both inputs must be lists
#   AssertionError: list a must be sorted

def merge_sorted(a, b):
    pass  # TODO

print(merge_sorted([1, 3, 5], [2, 4, 6]))   # [1, 2, 3, 4, 5, 6]

try:
    merge_sorted("not a list", [1, 2])
except AssertionError as e:
    print(f"AssertionError: {e}")

try:
    merge_sorted([3, 1, 2], [4, 5])
except AssertionError as e:
    print(f"AssertionError: {e}")
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Re-raise with Logging
# -----------------------------------------------------------------------------
# Write a function safe_parse_json(text) that:
#   - Tries to parse text as JSON (import json; json.loads(text))
#   - On JSONDecodeError: prints "[ERROR] Invalid JSON" then re-raises
#   - On success: returns the parsed object
#
# Expected output:
#   {'key': 'value'}
#   [ERROR] Invalid JSON
#   JSONDecodeError raised

import json

def safe_parse_json(text):
    pass  # TODO

print(safe_parse_json('{"key": "value"}'))   # {'key': 'value'}

try:
    safe_parse_json("not json {{{{")
except json.JSONDecodeError:
    print("JSONDecodeError raised")
