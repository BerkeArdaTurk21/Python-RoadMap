# =============================================================================
# Week 08 - Day 04 | Context Managers — Solutions
# =============================================================================

import contextlib
import time

# -----------------------------------------------------------------------------
# Solution 1 — Basic Class-Based Context Manager
# -----------------------------------------------------------------------------

class Announcer:
    def __enter__(self):
        print("Starting...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Finished.")
        return False

with Announcer():
    print("doing work")
print()

# -----------------------------------------------------------------------------
# Solution 2 — Suppressing a Specific Exception
# -----------------------------------------------------------------------------

class IgnoreErrors:
    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exc_type):
            return True     # suppress only this exception type
        return False        # let everything else propagate

with IgnoreErrors(ValueError):
    raise ValueError("bad value")
print("caught ValueError, continuing")
print()

# -----------------------------------------------------------------------------
# Solution 3 — Generator-Based Timer
# -----------------------------------------------------------------------------

@contextlib.contextmanager
def timed(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"{label} took {elapsed * 1000:.2f}ms")

with timed("sum-loop"):
    total = sum(range(1_000_000))
print()

# -----------------------------------------------------------------------------
# Solution 4 — Resource Manager
# -----------------------------------------------------------------------------

@contextlib.contextmanager
def open_connection(name):
    print(f"Connecting to {name}")
    conn = {"name": name, "connected": True}
    try:
        yield conn
    finally:
        print(f"Closing {name}")

with open_connection("db1") as conn:
    print(f"Connected: {conn['connected']}")
print()

# -----------------------------------------------------------------------------
# Solution 5 — Multiple Context Managers
# -----------------------------------------------------------------------------

@contextlib.contextmanager
def section(name):
    print(f"enter {name}")
    yield
    print(f"exit {name}")

with section("Outer"), section("Inner"):
    print("working")
