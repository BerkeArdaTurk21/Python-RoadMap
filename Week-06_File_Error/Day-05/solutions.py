# =============================================================================
# Week 06 - Day 05 | Raising Exceptions — Solutions
# =============================================================================
import json

# Solution 1
class Rectangle:
    def __init__(self, width, height):
        if width <= 0:
            raise ValueError(f"Width must be > 0, got {width}")
        if height <= 0:
            raise ValueError(f"Height must be > 0, got {height}")
        self.width  = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"Rectangle({self.width}x{self.height})"

try:
    r = Rectangle(4, 6)
    print(f"{r} — area {r.area()}")
    Rectangle(-1, 5)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    Rectangle(3, 0)
except ValueError as e:
    print(f"ValueError: {e}")
print()

# Solution 2
# KEY INSIGHT: raise NotImplementedError in the base; override in subclass.
class AbstractContainer:
    def push(self, item):
        raise NotImplementedError("subclass must implement push")
    def pop(self):
        raise NotImplementedError("subclass must implement pop")
    def peek(self):
        raise NotImplementedError("subclass must implement peek")

class ListStack(AbstractContainer):
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

s = ListStack()
s.push(10)
print(s.peek())
print(s.pop())

try:
    AbstractContainer().push(1)
except NotImplementedError as e:
    print(f"NotImplementedError: {e}")
print()

# Solution 3
def load_data(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError as e:
        raise RuntimeError(f"Failed to load data from {path}") from e

def load_data_silent(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        raise RuntimeError("Failed to load data (silent)") from None

try:
    load_data("missing.csv")
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    print(f"Has cause: {e.__cause__ is not None}")
print("---")
try:
    load_data_silent("missing.csv")
except RuntimeError as e:
    print(f"RuntimeError: {e}")
    print(f"Has cause: {e.__cause__ is not None}")
print()

# Solution 4
# KEY INSIGHT: assert for internal invariants — checks that caller passes
# sensible data types and sorted lists.
def merge_sorted(a, b):
    assert isinstance(a, list) and isinstance(b, list), "both inputs must be lists"
    assert a == sorted(a), "list a must be sorted"
    assert b == sorted(b), "list b must be sorted"
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    return result + a[i:] + b[j:]

print(merge_sorted([1, 3, 5], [2, 4, 6]))

try:
    merge_sorted("not a list", [1, 2])
except AssertionError as e:
    print(f"AssertionError: {e}")

try:
    merge_sorted([3, 1, 2], [4, 5])
except AssertionError as e:
    print(f"AssertionError: {e}")
print()

# Solution 5
def safe_parse_json(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        print("[ERROR] Invalid JSON")
        raise   # bare raise — re-raises JSONDecodeError

print(safe_parse_json('{"key": "value"}'))

try:
    safe_parse_json("not json {{{{")
except json.JSONDecodeError:
    print("JSONDecodeError raised")
