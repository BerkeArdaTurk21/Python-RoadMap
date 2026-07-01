# =============================================================================
# Week 08 - Day 06 | Testing with pytest
# =============================================================================
# pytest is Python's most popular testing framework. You write small functions
# that check your code with plain assert statements, and pytest finds and runs
# them all automatically, reporting exactly what passed and what failed.
#
# Install:    pip install pytest        (already in requirements.txt)
# Run:        pytest lesson.py -v
#
# Topics:
#   1. Why write tests?
#   2. Test discovery — how pytest finds your tests
#   3. Assertions — plain assert is all you need
#   4. Testing exceptions — pytest.raises
#   5. Fixtures — reusable setup with @pytest.fixture
#   6. Parametrize — one test, many cases
#   7. Useful command-line flags
#   8. Coverage basics

import pytest

# -----------------------------------------------------------------------------
# 1. Why Write Tests?
# -----------------------------------------------------------------------------
# - Catch bugs BEFORE users do — a failing test points at the exact problem
# - Refactor safely: if the tests still pass, the behavior didn't change
# - Tests are executable documentation: they show how the code is meant to be used
# - Every project week in this roadmap (Weeks 9-12) ships with a pytest suite

# The code under test — a tiny shopping cart module:

def add_item(cart: dict[str, int], name: str, qty: int = 1) -> None:
    """Add qty of an item to the cart (must be positive)."""
    if qty <= 0:
        raise ValueError("qty must be positive")
    cart[name] = cart.get(name, 0) + qty

def cart_total(cart: dict[str, int], prices: dict[str, float]) -> float:
    """Total price of the cart. Unknown items raise KeyError."""
    return sum(prices[name] * qty for name, qty in cart.items())

# -----------------------------------------------------------------------------
# 2. Test Discovery — How pytest Finds Your Tests
# -----------------------------------------------------------------------------
# Running plain `pytest` (no arguments) collects tests by NAMING CONVENTION:
#   - files named      test_*.py   or   *_test.py
#   - functions named  test_*
#   - classes named    Test*       (without an __init__ method)
#
# This file is lesson.py, so bare `pytest` skips it — but `pytest lesson.py`
# runs it explicitly, and every function below starting with test_ is collected.

# -----------------------------------------------------------------------------
# 3. Assertions — Plain assert Is All You Need
# -----------------------------------------------------------------------------
# No assertEqual / assertTrue like unittest — pytest rewrites plain assert
# statements so failures show BOTH sides of the comparison automatically.

def test_add_item_new():
    cart: dict[str, int] = {}
    add_item(cart, "apple", 3)
    assert cart == {"apple": 3}

def test_add_item_accumulates():
    cart = {"apple": 1}
    add_item(cart, "apple", 2)
    assert cart["apple"] == 3          # on failure pytest prints: assert 3 == ...

def test_cart_total():
    cart = {"apple": 2, "bread": 1}
    prices = {"apple": 0.5, "bread": 2.0}
    assert cart_total(cart, prices) == 3.0

# -----------------------------------------------------------------------------
# 4. Testing Exceptions — pytest.raises
# -----------------------------------------------------------------------------
# "This input SHOULD fail" is also behavior worth testing.
# pytest.raises passes only if the expected exception is raised inside the block.

def test_add_item_rejects_zero_qty():
    with pytest.raises(ValueError):
        add_item({}, "apple", 0)

def test_add_item_error_message():
    with pytest.raises(ValueError, match="positive"):   # message must match too
        add_item({}, "apple", -5)

def test_cart_total_unknown_item():
    with pytest.raises(KeyError):
        cart_total({"mystery": 1}, {"apple": 0.5})

# -----------------------------------------------------------------------------
# 5. Fixtures — Reusable Setup with @pytest.fixture
# -----------------------------------------------------------------------------
# A fixture is a function that prepares data (or a resource) for tests.
# Any test that lists the fixture's NAME as a parameter receives its return
# value — no copy-pasted setup code in every test.

@pytest.fixture
def stocked_cart() -> dict[str, int]:
    """A cart that already contains a few items."""
    return {"apple": 2, "bread": 1, "milk": 4}

@pytest.fixture
def price_list() -> dict[str, float]:
    return {"apple": 0.5, "bread": 2.0, "milk": 1.25}

def test_stocked_total(stocked_cart, price_list):     # fixtures injected by name
    assert cart_total(stocked_cart, price_list) == 8.0

def test_add_to_stocked(stocked_cart):
    add_item(stocked_cart, "milk", 1)
    assert stocked_cart["milk"] == 5

# Each test gets a FRESH copy — the fixture function runs again per test,
# so test_add_to_stocked's changes never leak into other tests.

# -----------------------------------------------------------------------------
# 6. Parametrize — One Test, Many Cases
# -----------------------------------------------------------------------------
# @pytest.mark.parametrize runs the SAME test once per argument tuple.
# 4 tuples below = 4 separate test results in the report.

@pytest.mark.parametrize("qty, expected", [
    (1, 1),
    (3, 3),
    (10, 10),
    (99, 99),
])
def test_add_item_quantities(qty, expected):
    cart: dict[str, int] = {}
    add_item(cart, "apple", qty)
    assert cart["apple"] == expected

@pytest.mark.parametrize("bad_qty", [0, -1, -100])
def test_add_item_bad_quantities(bad_qty):
    with pytest.raises(ValueError):
        add_item({}, "apple", bad_qty)

# -----------------------------------------------------------------------------
# 7. Useful Command-Line Flags
# -----------------------------------------------------------------------------
#   pytest lesson.py -v          verbose — one line per test with PASSED/FAILED
#   pytest lesson.py -q          quiet — just the summary
#   pytest -k "total"            run only tests whose name matches "total"
#   pytest -x                    stop at the first failure
#   pytest --lf                  re-run only the tests that failed last time
#   pytest -s                    show print() output (normally captured)

# -----------------------------------------------------------------------------
# 8. Coverage Basics
# -----------------------------------------------------------------------------
# Coverage measures WHICH lines of your code the tests actually executed.
#
# Install:    pip install pytest-cov
# Run:        pytest lesson.py --cov=lesson
#
# Output shows a percentage per file. 100% coverage does NOT mean bug-free —
# it only means every line ran at least once. Aim for meaningful tests first,
# high coverage second.

# -----------------------------------------------------------------------------
# Manual run — so `python lesson.py` also works without the pytest runner
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    test_add_item_new()
    test_add_item_accumulates()
    test_cart_total()
    test_add_item_rejects_zero_qty()
    test_add_item_error_message()
    test_cart_total_unknown_item()
    test_add_item_quantities(3, 3)
    test_add_item_bad_quantities(-1)
    print("All manual checks passed ✅")
    print("Now try the real runner:  pytest lesson.py -v")
    # (fixture-based tests need the pytest runner — fixtures are injected by
    #  pytest and cannot be called like normal functions)
