# =============================================================================
# Week 08 - Day 05 | Type Hints
# =============================================================================
# Type hints document what types a function expects and returns. Python does
# NOT enforce them at runtime — they're checked by external tools like mypy
# and used by IDEs for autocomplete and error detection.
#
# Topics:
#   1. Why type hints?
#   2. Basic hints — variables, parameters, return types
#   3. Built-in generic collections (list[int], dict[str, int], ...)
#   4. Optional and Union
#   5. Callable and Any
#   6. TypeVar and Generic classes
#   7. dataclasses with type hints
#   8. Running mypy

from typing import Optional, Union, Callable, Any, TypeVar, Generic

# -----------------------------------------------------------------------------
# 1. Why Type Hints?
# -----------------------------------------------------------------------------
# - Documentation: readers immediately know expected types
# - IDE support: autocomplete, inline errors before running the code
# - Static analysis: tools like mypy catch type bugs without running the program
# - Type hints are OPTIONAL and have ZERO effect at runtime by default

def add_no_hints(a, b):       # no hints — unclear what a, b should be
    return a + b

def add(a: int, b: int) -> int:    # hints — clearly expects/returns int
    return a + b

print(add(2, 3))              # 5
print(add("2", "3"))          # "23" — Python does NOT enforce hints at runtime!

# -----------------------------------------------------------------------------
# 2. Basic Hints — Variables, Parameters, Return Types
# -----------------------------------------------------------------------------

name: str = "Alice"
age: int = 30
price: float = 19.99
is_active: bool = True

def greet(name: str, excited: bool = False) -> str:
    suffix = "!" if excited else "."
    return f"Hello, {name}{suffix}"

def no_return(message: str) -> None:    # -> None means "returns nothing"
    print(message)

print(greet("Bob", excited=True))   # Hello, Bob!

# -----------------------------------------------------------------------------
# 3. Built-in Generic Collections (Python 3.9+)
# -----------------------------------------------------------------------------
# Since Python 3.9, you can use built-in types directly as generics —
# no need to import List, Dict, Tuple from typing for simple cases.

def total(numbers: list[int]) -> int:
    return sum(numbers)

def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}

def coordinates() -> tuple[float, float]:
    return (3.5, 7.2)

print(total([1, 2, 3]))                       # 6
print(word_lengths(["hi", "python"]))         # {'hi': 2, 'python': 6}
print(coordinates())                          # (3.5, 7.2)

# Nested generics:
def group_scores(data: dict[str, list[int]]) -> dict[str, float]:
    return {name: sum(scores) / len(scores) for name, scores in data.items()}

print(group_scores({"Alice": [90, 80, 100]}))  # {'Alice': 90.0}

# -----------------------------------------------------------------------------
# 4. Optional and Union
# -----------------------------------------------------------------------------
# Optional[X] means "X or None" — shorthand for Union[X, None]
# Union[X, Y] means "X or Y"
# Python 3.10+ also allows the X | None and X | Y syntax directly.

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)     # returns str or None

result = find_user(1)
print(result)         # Alice
result2 = find_user(99)
print(result2)         # None

def parse_id(value: Union[int, str]) -> int:    # accepts int OR str
    return int(value)

print(parse_id(42))      # 42
print(parse_id("42"))    # 42

# Python 3.10+ pipe syntax (equivalent, more concise):
def find_user_modern(user_id: int) -> str | None:
    users = {1: "Alice"}
    return users.get(user_id)

# -----------------------------------------------------------------------------
# 5. Callable and Any
# -----------------------------------------------------------------------------
# Callable[[ArgTypes], ReturnType] describes a function's signature.
# Any disables type checking for that value — use sparingly.

def apply_operation(x: int, y: int, op: Callable[[int, int], int]) -> int:
    return op(x, y)

def multiply(a: int, b: int) -> int:
    return a * b

print(apply_operation(3, 4, multiply))   # 12

def process(data: Any) -> Any:    # accepts/returns literally anything
    return data

print(process(42))
print(process("hello"))
print(process([1, 2, 3]))

# -----------------------------------------------------------------------------
# 6. TypeVar and Generic Classes
# -----------------------------------------------------------------------------
# TypeVar lets you write functions/classes that work with ANY type,
# while still preserving type relationships (generics).

T = TypeVar("T")

def first_item(items: list[T]) -> T:
    """Works for list[int], list[str], etc. — return type matches input type."""
    return items[0]

print(first_item([1, 2, 3]))         # 1   (int)
print(first_item(["a", "b", "c"]))   # 'a' (str)

class Box(Generic[T]):
    """A generic container that holds one item of type T."""

    def __init__(self, item: T) -> None:
        self.item = item

    def get(self) -> T:
        return self.item

int_box: Box[int] = Box(42)
str_box: Box[str] = Box("hello")
print(int_box.get())   # 42
print(str_box.get())   # hello

# -----------------------------------------------------------------------------
# 7. dataclasses with Type Hints
# -----------------------------------------------------------------------------
# Type hints are REQUIRED for dataclass fields — they define the class structure.

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    label: str = "origin"

p = Point(1.5, 2.5)
print(p)               # Point(x=1.5, y=2.5, label='origin')
print(p.x, p.y)         # 1.5 2.5

# -----------------------------------------------------------------------------
# 8. Running mypy (Static Type Checker)
# -----------------------------------------------------------------------------
# mypy reads your type hints and reports mismatches WITHOUT running the code.
#
# Install:    pip install mypy
# Run:        mypy lesson.py
#
# Example of what mypy would catch (commented out — would fail type check):
#
#   def strict_add(a: int, b: int) -> int:
#       return a + b
#
#   strict_add("2", "3")   # mypy error: Argument has incompatible type "str"
#
# mypy does NOT run at runtime — it's a separate analysis step,
# usually run in CI or before committing code.
