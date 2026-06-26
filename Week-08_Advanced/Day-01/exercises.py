# =============================================================================
# Week 08 - Day 01 | Decorators — Exercises
# =============================================================================

import functools
import time

# -----------------------------------------------------------------------------
# Exercise 1 — Basic Decorator
# -----------------------------------------------------------------------------
# Write a decorator called `uppercase` that converts the return value of any
# function to uppercase.
#
# When applied to the functions below:
#
#   @uppercase
#   def greet(name):
#       return f"hello, {name}!"
#
#   @uppercase
#   def status():
#       return "all systems running"
#
# Expected output:
#   HELLO, ALICE!
#   ALL SYSTEMS RUNNING

# TODO: define uppercase decorator here

# (uncomment after writing the decorator)
# @uppercase
# def greet(name):
#     return f"hello, {name}!"
#
# @uppercase
# def status():
#     return "all systems running"
#
# print(greet("Alice"))
# print(status())
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Call Logger
# -----------------------------------------------------------------------------
# Write a decorator called `log_calls` that prints:
#   Calling <function_name>(<args>)
#   <function_name> returned <result>
#
# before and after every call. Use @functools.wraps.
#
# When applied:
#
#   @log_calls
#   def add(a, b):
#       return a + b
#
#   @log_calls
#   def repeat_str(s, n=2):
#       return s * n
#
# Expected output:
#   Calling add(10, 5)
#   add returned 15
#   Calling repeat_str('hi', n=3)
#   repeat_str returned 'hihihi'
#
# Hint: format positional args with repr(), keyword args as key=repr(val).

# TODO: define log_calls decorator here

# (uncomment after writing the decorator)
# @log_calls
# def add(a, b):
#     return a + b
#
# @log_calls
# def repeat_str(s, n=2):
#     return s * n
#
# add(10, 5)
# repeat_str("hi", n=3)
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Timer
# -----------------------------------------------------------------------------
# Write a decorator called `timer` that measures execution time and prints:
#   <function_name> took X.XXXms
#
# Use time.perf_counter() for measurement. Use @functools.wraps.
# The decorator must still return the function's original return value.
#
# Expected output (times will vary):
#   slow_add took ~200ms
#   Result: 499999500000

# TODO: define timer decorator here

# (uncomment after writing the decorator)
# @timer
# def slow_add(n):
#     return sum(range(n))
#
# result = slow_add(1_000_000)
# print(f"Result: {result}")
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Stacked Decorators
# -----------------------------------------------------------------------------
# Two decorators are provided below. Apply BOTH to `format_name` so the output
# is:  >> [Alice Smith] <<
#
# Decorators provided (do not change them):

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

# TODO: apply both decorators to format_name in the correct order
# def format_name(first, last):
#     return f"{first} {last}"
#
# print(format_name("Alice", "Smith"))   # >> [Alice Smith] <<
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Decorator Factory
# -----------------------------------------------------------------------------
# Write a decorator factory called `repeat(n)` that calls the decorated
# function n times and returns the result of the LAST call. Use @functools.wraps.
#
# Expected output:
#   Hello!
#   Hello!
#   Hello!
#   Go! Go! Go! Go! Go!  <- returned from last call (n=5)

# TODO: define repeat(n) factory here

# (uncomment after writing the factory)
# @repeat(3)
# def say_hello():
#     print("Hello!")
#
# @repeat(5)
# def cheer(word):
#     return f"{word}! "
#
# say_hello()
# print(cheer("Go").strip())
print()
