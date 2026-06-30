# =============================================================================
# Week 08 - Day 05 | Type Hints — Exercises
# =============================================================================

from typing import Optional, Union, Callable, TypeVar, Generic

# -----------------------------------------------------------------------------
# Exercise 1 — Basic Function Hints
# -----------------------------------------------------------------------------
# Add type hints to the function below:
#   - celsius is a float
#   - it returns a float
#
# Expected output:
#   98.6

def to_fahrenheit(celsius):   # TODO: add type hints
    return celsius * 9 / 5 + 32

print(to_fahrenheit(37.0))
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Collection Hints
# -----------------------------------------------------------------------------
# Write a function `average(numbers: list[float]) -> float` that returns
# the average of a list of numbers.
#
# Write a function `word_count(text: str) -> dict[str, int]` that counts
# how many times each word appears in the text (split on spaces).
#
# Expected output:
#   3.0
#   {'the': 2, 'cat': 1, 'sat': 1}

# TODO: define average() here

# TODO: define word_count() here

# (uncomment to test)
# print(average([2.0, 3.0, 4.0]))
# print(word_count("the cat sat the mat"))
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Optional and Union
# -----------------------------------------------------------------------------
# Write a function `find_item(catalog: dict[str, int], key: str) -> Optional[int]`
# that returns the value for key, or None if not found.
#
# Write a function `to_int(value: Union[int, str, float]) -> int`
# that converts any of those types to an int.
#
# Expected output:
#   5
#   None
#   42
#   42

# TODO: define find_item() here

# TODO: define to_int() here

# (uncomment to test)
# catalog = {"apples": 5, "bananas": 3}
# print(find_item(catalog, "apples"))
# print(find_item(catalog, "cherries"))
# print(to_int("42"))
# print(to_int(42.9))
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Callable Hint
# -----------------------------------------------------------------------------
# Write a function `apply_to_all(items: list[int], func: Callable[[int], int]) -> list[int]`
# that applies func to every item and returns the new list.
#
# Expected output:
#   [1, 4, 9, 16]

# TODO: define apply_to_all() here

# (uncomment to test)
# def square(x: int) -> int:
#     return x * x
#
# print(apply_to_all([1, 2, 3, 4], square))
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Generic Class
# -----------------------------------------------------------------------------
# Write a generic class `Stack(Generic[T])` with:
#   - push(item: T) -> None
#   - pop() -> T
#   - is_empty() -> bool
#
# Expected output:
#   False
#   3
#   2
#   1
#   True

T = TypeVar("T")

# TODO: define Stack(Generic[T]) class here

# (uncomment to test)
# s: Stack[int] = Stack()
# s.push(1)
# s.push(2)
# s.push(3)
# print(s.is_empty())
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.is_empty())
print()
