# =============================================================================
# Week 08 - Day 01 | Decorators — Solutions
# =============================================================================

import functools
import time

# -----------------------------------------------------------------------------
# Solution 1 — Basic Decorator
# -----------------------------------------------------------------------------

def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"hello, {name}!"

@uppercase
def status():
    return "all systems running"

print(greet("Alice"))   # HELLO, ALICE!
print(status())         # ALL SYSTEMS RUNNING
print()

# -----------------------------------------------------------------------------
# Solution 2 — Call Logger
# -----------------------------------------------------------------------------

def log_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        arg_parts = [repr(a) for a in args]
        kwarg_parts = [f"{k}={v!r}" for k, v in kwargs.items()]
        sig = ", ".join(arg_parts + kwarg_parts)
        print(f"Calling {func.__name__}({sig})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def repeat_str(s, n=2):
    return s * n

add(10, 5)
repeat_str("hi", n=3)
print()

# -----------------------------------------------------------------------------
# Solution 3 — Timer
# -----------------------------------------------------------------------------

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed * 1000:.3f}ms")
        return result
    return wrapper

@timer
def slow_add(n):
    return sum(range(n))

result = slow_add(1_000_000)
print(f"Result: {result}")
print()

# -----------------------------------------------------------------------------
# Solution 4 — Stacked Decorators
# -----------------------------------------------------------------------------

def wrap_brackets(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"[{func(*args, **kwargs)}]"
    return wrapper

def wrap_arrows(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f">> {func(*args, **kwargs)} <<"
    return wrapper

@wrap_arrows    # applied second — outermost
@wrap_brackets  # applied first  — innermost
def format_name(first, last):
    return f"{first} {last}"

print(format_name("Alice", "Smith"))   # >> [Alice Smith] <<
print()

# -----------------------------------------------------------------------------
# Solution 5 — Decorator Factory
# -----------------------------------------------------------------------------

def repeat(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

@repeat(5)
def cheer(word):
    return f"{word}! "

say_hello()
print(cheer("Go").strip())
