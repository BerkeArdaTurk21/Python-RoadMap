# =============================================================================
# Week 08 - Day 06 | Testing with pytest — Exercises
# =============================================================================
# Unlike previous days, you RUN these exercises with pytest:
#
#   pytest exercises.py -v
#
# Write the missing tests below each function. When you're done, the run
# should report:  12 passed
# =============================================================================

import pytest

# -----------------------------------------------------------------------------
# Exercise 1 — Basic Assertions
# -----------------------------------------------------------------------------
# The function under test:

def is_even(n: int) -> bool:
    return n % 2 == 0

# Write TWO tests:
#   test_is_even_true()  — asserts that is_even(4) is True
#   test_is_even_false() — asserts that is_even(7) is False

# TODO: write test_is_even_true() here

# TODO: write test_is_even_false() here

# -----------------------------------------------------------------------------
# Exercise 2 — Testing Exceptions
# -----------------------------------------------------------------------------
# The function under test:

def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b

# Write TWO tests:
#   test_safe_divide()        — asserts safe_divide(10, 4) == 2.5
#   test_safe_divide_by_zero() — uses pytest.raises to check that
#                                safe_divide(1, 0) raises ZeroDivisionError

# TODO: write test_safe_divide() here

# TODO: write test_safe_divide_by_zero() here

# -----------------------------------------------------------------------------
# Exercise 3 — Fixture
# -----------------------------------------------------------------------------
# Write a fixture `inventory()` that returns:
#   {"sword": 1, "potion": 3, "gold": 250}
#
# Then write TWO tests that receive it as a parameter:
#   test_inventory_has_potions(inventory) — asserts inventory["potion"] == 3
#   test_inventory_size(inventory)        — asserts len(inventory) == 3

# TODO: write the inventory fixture here

# TODO: write test_inventory_has_potions() here

# TODO: write test_inventory_size() here

# -----------------------------------------------------------------------------
# Exercise 4 — Parametrize
# -----------------------------------------------------------------------------
# The function under test:

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Write ONE parametrized test `test_factorial(n, expected)` covering:
#   (0, 1), (1, 1), (5, 120), (7, 5040)
# parametrize expands it to 4 separate tests in the report.

# TODO: write the parametrized test_factorial() here

# -----------------------------------------------------------------------------
# Exercise 5 — Test First, Then Fix the Bug
# -----------------------------------------------------------------------------
# The function below has a BUG: it applies the discount the wrong way.
# 1. Write test_apply_discount() asserting apply_discount(100.0, 20) == 80.0
# 2. Run pytest and watch your test FAIL
# 3. Fix the function so the test passes
#
# Also write test_apply_discount_invalid() checking that a percent
# over 100 raises ValueError (this one already passes).

def apply_discount(price: float, percent: float) -> float:
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return price * (percent / 100)          # BUG: returns the discount, not the price!

# TODO: write test_apply_discount() here, run pytest, then fix the bug above

# TODO: write test_apply_discount_invalid() here
