# =============================================================================
# Week 08 - Day 04 | Context Managers — Exercises
# =============================================================================

import contextlib
import time

# -----------------------------------------------------------------------------
# Exercise 1 — Basic Class-Based Context Manager
# -----------------------------------------------------------------------------
# Write a class `Announcer` that prints "Starting..." on enter and "Finished."
# on exit. It doesn't need to return anything special from __enter__.
#
# Expected output:
#   Starting...
#   doing work
#   Finished.

# TODO: define Announcer class here

# (uncomment to test)
# with Announcer():
#     print("doing work")
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Suppressing a Specific Exception
# -----------------------------------------------------------------------------
# Write a class `IgnoreErrors(exc_type)` that suppresses ONLY the given
# exception type. Other exceptions should still propagate normally.
#
# Expected output:
#   caught ValueError, continuing
#   (then a real KeyError should still crash if tested with a different type)

# TODO: define IgnoreErrors class here

# (uncomment to test)
# with IgnoreErrors(ValueError):
#     raise ValueError("bad value")
# print("caught ValueError, continuing")
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Generator-Based Timer
# -----------------------------------------------------------------------------
# Using @contextlib.contextmanager, write a function `timed(label)` that
# prints "<label> took X.XXms" after the with block finishes.
# Use time.perf_counter() and a try/finally inside the generator.
#
# Expected output:
#   sum-loop took ~50.00ms   (value varies)

# TODO: define timed(label) generator context manager here

# (uncomment to test)
# with timed("sum-loop"):
#     total = sum(range(1_000_000))
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Resource Manager
# -----------------------------------------------------------------------------
# Using @contextlib.contextmanager, write `open_connection(name)` that:
#   1. Prints "Connecting to <name>"
#   2. Yields a dict {"name": name, "connected": True}
#   3. Always prints "Closing <name>" afterward (even on exception)
#
# Expected output:
#   Connecting to db1
#   Connected: True
#   Closing db1

# TODO: define open_connection(name) generator context manager here

# (uncomment to test)
# with open_connection("db1") as conn:
#     print(f"Connected: {conn['connected']}")
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Multiple Context Managers
# -----------------------------------------------------------------------------
# Using the `section(name)` context manager provided below, open TWO sections
# "Outer" and "Inner" in a SINGLE with statement (comma-separated).
#
# Expected output:
#   enter Outer
#   enter Inner
#   working
#   exit Inner
#   exit Outer

@contextlib.contextmanager
def section(name):
    print(f"enter {name}")
    yield
    print(f"exit {name}")

# TODO: open both sections in one with statement
# with ___:
#     print("working")
print()
