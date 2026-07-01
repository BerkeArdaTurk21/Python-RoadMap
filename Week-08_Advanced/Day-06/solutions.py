# =============================================================================
# Week 08 - Day 06 | Testing with pytest — Solutions
# =============================================================================
# Run:  pytest solutions.py -v      →  12 passed
# =============================================================================

import pytest

# -----------------------------------------------------------------------------
# Solution 1 — Basic Assertions
# -----------------------------------------------------------------------------

def is_even(n: int) -> bool:
    return n % 2 == 0

def test_is_even_true():
    assert is_even(4) is True

def test_is_even_false():
    assert is_even(7) is False

# -----------------------------------------------------------------------------
# Solution 2 — Testing Exceptions
# -----------------------------------------------------------------------------

def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b

def test_safe_divide():
    assert safe_divide(10, 4) == 2.5

def test_safe_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        safe_divide(1, 0)

# -----------------------------------------------------------------------------
# Solution 3 — Fixture
# -----------------------------------------------------------------------------

@pytest.fixture
def inventory() -> dict[str, int]:
    return {"sword": 1, "potion": 3, "gold": 250}

def test_inventory_has_potions(inventory):
    assert inventory["potion"] == 3

def test_inventory_size(inventory):
    assert len(inventory) == 3

# -----------------------------------------------------------------------------
# Solution 4 — Parametrize
# -----------------------------------------------------------------------------

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (5, 120),
    (7, 5040),
])
def test_factorial(n, expected):
    assert factorial(n) == expected

# -----------------------------------------------------------------------------
# Solution 5 — Test First, Then Fix the Bug
# -----------------------------------------------------------------------------
# The bug was `price * (percent / 100)` — that returns the DISCOUNT amount.
# Fixed version subtracts the discount from the price:

def apply_discount(price: float, percent: float) -> float:
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return price * (1 - percent / 100)

def test_apply_discount():
    assert apply_discount(100.0, 20) == 80.0

def test_apply_discount_invalid():
    with pytest.raises(ValueError):
        apply_discount(50.0, 150)

# -----------------------------------------------------------------------------
# Manual run — so `python solutions.py` also works without the pytest runner
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    test_is_even_true()
    test_is_even_false()
    test_safe_divide()
    test_safe_divide_by_zero()
    test_factorial(5, 120)
    test_apply_discount()
    test_apply_discount_invalid()
    print("All manual checks passed ✅")
    print("Full suite (with fixtures):  pytest solutions.py -v")
