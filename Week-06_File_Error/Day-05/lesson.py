# =============================================================================
# Week 06 - Day 05 | Raising Exceptions
# =============================================================================
# Topics: raise, raise from, assert, re-raising, built-in exception types
# =============================================================================

# -----------------------------------------------------------------------------
# 1. raise — SIGNALLING AN ERROR FROM YOUR CODE
# -----------------------------------------------------------------------------
# raise ExceptionType("message")  — creates and raises immediately
# raise ExceptionInstance         — raises an already-created exception

print("── raise basics ──")

def set_age(age):
    if age < 0 or age > 150:
        raise ValueError(f"Age must be 0-150, got {age}")
    return age

try:
    set_age(200)
except ValueError as e:
    print(f"Caught: {e}")

# Raising different types for different conditions
def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Divisor cannot be zero")
    return a / b

for args in [(10, 2), (10, 0), ("x", 2)]:
    try:
        print(divide(*args))
    except (ZeroDivisionError, TypeError) as e:
        print(f"{type(e).__name__}: {e}")

# -----------------------------------------------------------------------------
# 2. BARE raise — RE-RAISING THE CURRENT EXCEPTION
# -----------------------------------------------------------------------------
# Inside an except block, plain `raise` re-raises the active exception
# without losing the original traceback.

print("\n── re-raise ──")

def load_config(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print("  [load_config] logging: config not found")
        raise    # re-raises FileNotFoundError with original traceback

try:
    load_config("missing.json")
except FileNotFoundError as e:
    print(f"  Caller caught: {e}")

# -----------------------------------------------------------------------------
# 3. raise ... from ... — EXCEPTION CHAINING
# -----------------------------------------------------------------------------
# Wraps a low-level exception in a higher-level one.
# "raise B from A" sets B.__cause__ = A.
# The original exception is still visible in the traceback.

print("\n── raise from ──")

def parse_config(path):
    try:
        with open(path) as f:
            import json
            return json.load(f)
    except FileNotFoundError as e:
        raise RuntimeError(f"Config file not found: {path}") from e

try:
    parse_config("settings.json")
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    print(f"Caused by:    {e.__cause__}")

# Use `raise B from None` to suppress the original exception in tracebacks.

# -----------------------------------------------------------------------------
# 4. assert — DEFENSIVE PROGRAMMING
# -----------------------------------------------------------------------------
# assert condition, "message"
# Raises AssertionError if condition is False.
# Used for invariants and sanity checks, NOT for user-input validation.
# NOTE: assertions are disabled when Python runs with -O (optimize flag).

print("\n── assert ──")

def compute_average(numbers):
    assert isinstance(numbers, list), "numbers must be a list"
    assert len(numbers) > 0, "cannot average an empty list"
    return sum(numbers) / len(numbers)

try:
    print(compute_average([10, 20, 30]))   # 20.0
    print(compute_average([]))             # AssertionError
except AssertionError as e:
    print(f"AssertionError: {e}")

# ❌ Don't use assert for input validation — it can be disabled:
#    assert user_age >= 0     # WRONG for user data
# ✅ Use assert for internal invariants / developer mistakes:
#    assert isinstance(result, list)   # sanity check after our own code

# -----------------------------------------------------------------------------
# 5. CHOOSING THE RIGHT EXCEPTION TYPE
# -----------------------------------------------------------------------------
# Python's built-in exceptions carry semantic meaning. Use them correctly:
#
# ValueError   — right type, wrong value:    int("abc"), age = -1
# TypeError    — wrong type entirely:         1 + "a"
# KeyError     — missing dict key
# IndexError   — list index out of range
# AttributeError — object has no such attribute
# RuntimeError — generic runtime error (when no built-in fits)
# NotImplementedError — method must be overridden in subclass
# FileNotFoundError / PermissionError — file system issues

print("\n── choosing exceptions ──")

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError("peek at empty stack")
        return self._data[-1]

s = Stack()
s.push(1)
s.push(2)
print(s.pop())   # 2
try:
    s.pop()
    s.pop()      # empty — raises IndexError
except IndexError as e:
    print(f"IndexError: {e}")

# =============================================================================
# SUMMARY
# =============================================================================
# ┌──────────────────────────┬─────────────────────────────────────────────┐
# │  Syntax                  │  Use case                                   │
# ├──────────────────────────┼─────────────────────────────────────────────┤
# │  raise ValueError("msg") │  Signal bad input/state with message        │
# │  raise                   │  Re-raise the current exception (in except) │
# │  raise B from A          │  Wrap A in B; chain cause                   │
# │  raise B from None       │  Suppress cause in traceback                │
# │  assert cond, "msg"      │  Internal invariant (disabled with -O)      │
# └──────────────────────────┴─────────────────────────────────────────────┘
print("\nDay 05 — Raising Exceptions complete!")
