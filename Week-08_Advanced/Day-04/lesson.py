# =============================================================================
# Week 08 - Day 04 | Context Managers
# =============================================================================
# Context managers guarantee that setup/cleanup code always runs — even if
# an exception happens in between. The `with` statement is the syntax for using them.
#
# Topics:
#   1. The problem context managers solve
#   2. The with statement
#   3. The protocol: __enter__ and __exit__
#   4. Handling exceptions inside __exit__
#   5. contextlib.contextmanager — generator-based context managers
#   6. contextlib.suppress
#   7. Multiple context managers in one with statement
#   8. Practical examples: timer, redirecting output

import contextlib
import time

# -----------------------------------------------------------------------------
# 1. The Problem Context Managers Solve
# -----------------------------------------------------------------------------
# Without a context manager, cleanup code can be skipped if an exception occurs:

def risky_without_with():
    f = open("temp_demo.txt", "w")
    f.write("hello")
    # if an exception happened here, f.close() below would NEVER run
    f.close()

# The `with` statement guarantees cleanup runs, no matter what:

def safe_with_with():
    with open("temp_demo.txt", "w") as f:
        f.write("hello")
    # f.close() is called automatically here — even if an exception happened

safe_with_with()
import os
os.remove("temp_demo.txt")   # cleanup demo file

# -----------------------------------------------------------------------------
# 2. The with Statement
# -----------------------------------------------------------------------------
# with EXPRESSION as VARIABLE:
#     # body
#
# Under the hood:
#   1. mgr = EXPRESSION
#   2. VARIABLE = mgr.__enter__()
#   3. run the body
#   4. mgr.__exit__(exc_type, exc_val, exc_tb)  <- always runs, even on exception

# -----------------------------------------------------------------------------
# 3. The Protocol: __enter__ and __exit__
# -----------------------------------------------------------------------------

class Timer:
    """Context manager that times a block of code."""

    def __enter__(self):
        self.start = time.perf_counter()
        return self                      # becomes the "as" variable

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed * 1000:.2f}ms")
        return False                     # False/None = don't suppress exceptions

with Timer() as t:
    total = sum(range(1_000_000))

print(f"Sum was: {total}")

# -----------------------------------------------------------------------------
# 4. Handling Exceptions Inside __exit__
# -----------------------------------------------------------------------------
# __exit__ receives exception info if one occurred inside the with block:
#   exc_type — the exception class (or None)
#   exc_val  — the exception instance (or None)
#   exc_tb   — the traceback (or None)
#
# Return True from __exit__  -> exception is SUPPRESSED (swallowed)
# Return False/None          -> exception PROPAGATES normally

class SuppressErrors:
    """Context manager that suppresses a given exception type and logs it."""

    def __init__(self, exc_type):
        self.exc_type = exc_type

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None and issubclass(exc_type, self.exc_type):
            print(f"Suppressed: {exc_type.__name__}: {exc_val}")
            return True    # suppress the exception
        return False       # let other exceptions propagate

with SuppressErrors(ZeroDivisionError):
    print(1 / 0)           # exception happens here
print("Program continues normally")

# -----------------------------------------------------------------------------
# 5. contextlib.contextmanager — Generator-Based Context Managers
# -----------------------------------------------------------------------------
# Writing a class with __enter__/__exit__ is verbose for simple cases.
# @contextmanager turns a generator function into a context manager:
#   - Code BEFORE yield  = __enter__ logic
#   - The yielded value  = the "as" variable
#   - Code AFTER yield    = __exit__ logic (runs even if an exception occurs)

@contextlib.contextmanager
def timer_cm():
    start = time.perf_counter()
    try:
        yield start                      # this becomes "as start_time"
    finally:
        elapsed = time.perf_counter() - start
        print(f"timer_cm elapsed: {elapsed * 1000:.2f}ms")

with timer_cm():
    total = sum(range(500_000))
print(f"Sum: {total}")

# A resource-management example:

@contextlib.contextmanager
def managed_resource(name):
    print(f"Acquiring {name}")
    resource = {"name": name, "open": True}
    try:
        yield resource
    finally:
        resource["open"] = False
        print(f"Releasing {name}")

with managed_resource("database") as db:
    print(f"Using {db['name']}, open={db['open']}")
# Acquiring database
# Using database, open=True
# Releasing database

# -----------------------------------------------------------------------------
# 6. contextlib.suppress
# -----------------------------------------------------------------------------
# A built-in shortcut for ignoring specific exceptions cleanly.

with contextlib.suppress(FileNotFoundError):
    os.remove("does_not_exist.txt")    # no error raised, silently ignored

print("Still running after suppress")

# -----------------------------------------------------------------------------
# 7. Multiple Context Managers in One with Statement
# -----------------------------------------------------------------------------

@contextlib.contextmanager
def section(name):
    print(f"--- enter {name} ---")
    yield
    print(f"--- exit {name} ---")

with section("A"), section("B"):
    print("inside both sections")
# --- enter A ---
# --- enter B ---
# inside both sections
# --- exit B ---
# --- exit A ---

# -----------------------------------------------------------------------------
# 8. Practical: Redirecting stdout
# -----------------------------------------------------------------------------
import io

buffer = io.StringIO()
with contextlib.redirect_stdout(buffer):
    print("this goes into the buffer, not the terminal")

captured = buffer.getvalue()
print(f"Captured: {captured!r}")
