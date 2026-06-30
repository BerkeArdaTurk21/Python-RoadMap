# =============================================================================
# Week 08 - Day 05 | Type Hints — Solutions
# =============================================================================

from typing import Optional, Union, Callable, TypeVar, Generic

# -----------------------------------------------------------------------------
# Solution 1 — Basic Function Hints
# -----------------------------------------------------------------------------

def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32

print(to_fahrenheit(37.0))
print()

# -----------------------------------------------------------------------------
# Solution 2 — Collection Hints
# -----------------------------------------------------------------------------

def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(average([2.0, 3.0, 4.0]))
print(word_count("the cat sat the mat"))
print()

# -----------------------------------------------------------------------------
# Solution 3 — Optional and Union
# -----------------------------------------------------------------------------

def find_item(catalog: dict[str, int], key: str) -> Optional[int]:
    return catalog.get(key)

def to_int(value: Union[int, str, float]) -> int:
    return int(value)

catalog = {"apples": 5, "bananas": 3}
print(find_item(catalog, "apples"))
print(find_item(catalog, "cherries"))
print(to_int("42"))
print(to_int(42.9))
print()

# -----------------------------------------------------------------------------
# Solution 4 — Callable Hint
# -----------------------------------------------------------------------------

def apply_to_all(items: list[int], func: Callable[[int], int]) -> list[int]:
    return [func(item) for item in items]

def square(x: int) -> int:
    return x * x

print(apply_to_all([1, 2, 3, 4], square))
print()

# -----------------------------------------------------------------------------
# Solution 5 — Generic Class
# -----------------------------------------------------------------------------

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def is_empty(self) -> bool:
        return len(self._items) == 0

s: Stack[int] = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.is_empty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())
