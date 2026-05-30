# =============================================================================
# Week 04 - Day 02 | Tuples
# =============================================================================
# Topics: Creating tuples, immutability, indexing, packing/unpacking,
#         when to use tuples, namedtuple
# =============================================================================

# -----------------------------------------------------------------------------
# 1. CREATING TUPLES
# -----------------------------------------------------------------------------
# A tuple is an ORDERED, IMMUTABLE sequence.
# Once created, its elements cannot be changed.

empty     = ()
single    = (42,)          # ⚠️ the trailing comma makes it a tuple!
not_tuple = (42)           # this is just the integer 42 in parentheses
numbers   = (1, 2, 3, 4, 5)
mixed     = (1, "hello", 3.14, True)
nested    = ((1, 2), (3, 4), (5, 6))

print(single)       # (42,)
print(not_tuple)    # 42    ← NOT a tuple
print(type(single))     # <class 'tuple'>
print(type(not_tuple))  # <class 'int'>

# Parentheses are often optional — the COMMA makes a tuple
a = 1, 2, 3        # tuple without parentheses
print(a)           # (1, 2, 3)
print(type(a))     # <class 'tuple'>

# tuple() constructor
from_list   = tuple([1, 2, 3])    # (1, 2, 3)
from_string = tuple("hello")      # ('h', 'e', 'l', 'l', 'o')
from_range  = tuple(range(5))     # (0, 1, 2, 3, 4)
print(from_list)
print(from_string)

# -----------------------------------------------------------------------------
# 2. INDEXING & SLICING (same as lists)
# -----------------------------------------------------------------------------
coords = (10, 20, 30, 40, 50)

print(coords[0])    # 10
print(coords[-1])   # 50
print(coords[1:4])  # (20, 30, 40)
print(coords[::-1]) # (50, 40, 30, 20, 10)

# Nested tuple access
matrix = ((1, 2), (3, 4), (5, 6))
print(matrix[1][0])  # 3

# -----------------------------------------------------------------------------
# 3. IMMUTABILITY — you CANNOT change a tuple
# -----------------------------------------------------------------------------
point = (3, 7)

# point[0] = 10   # ← TypeError: 'tuple' object does not support item assignment
# point.append(5) # ← AttributeError: 'tuple' object has no attribute 'append'

# BUT — if a tuple contains a mutable object, THAT object can change:
mutable_inside = ([1, 2], [3, 4])
mutable_inside[0].append(99)   # the list inside can be modified
print(mutable_inside)           # ([1, 2, 99], [3, 4])
# The tuple itself still holds the same two list references — that hasn't changed.

# -----------------------------------------------------------------------------
# 4. TUPLE METHODS (only 2 — no modification methods)
# -----------------------------------------------------------------------------
t = (1, 2, 3, 2, 1, 4, 2)

print(t.count(2))   # 3  (how many times 2 appears)
print(t.index(3))   # 2  (index of first occurrence of 3)

# Membership test
print(3 in t)       # True
print(9 in t)       # False
print(len(t))       # 7

# -----------------------------------------------------------------------------
# 5. PACKING & UNPACKING
# -----------------------------------------------------------------------------
# Packing: assigning multiple values into one tuple
person = "Berke", 21, "Warsaw"   # packing
print(person)   # ('Berke', 21, 'Warsaw')

# Unpacking: extracting tuple values into separate variables
name, age, city = person
print(name)   # Berke
print(age)    # 21
print(city)   # Warsaw

# Number of variables MUST match tuple length (or use * to catch the rest)
# name, age = person   # ← ValueError: too many values to unpack

# Extended unpacking with * (star)
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]   ← rest is a LIST

*start, last = (1, 2, 3, 4, 5)
print(start)   # [1, 2, 3, 4]
print(last)    # 5

a, *middle, b = (1, 2, 3, 4, 5)
print(a, middle, b)   # 1 [2, 3, 4] 5

# Swapping variables without a temp (tuple unpacking under the hood)
x, y = 10, 20
x, y = y, x
print(x, y)   # 20 10  ← swapped!

# -----------------------------------------------------------------------------
# 6. UNPACKING IN LOOPS
# -----------------------------------------------------------------------------
points = [(1, 2), (3, 4), (5, 6)]

for x, y in points:
    print(f"x={x}, y={y}")

# With enumerate
colors = ("red", "green", "blue")
for i, color in enumerate(colors):
    print(f"{i}: {color}")

# -----------------------------------------------------------------------------
# 7. FUNCTIONS RETURNING MULTIPLE VALUES
# -----------------------------------------------------------------------------
# Python functions that "return multiple values" are really returning a tuple.

def min_max(numbers):
    return min(numbers), max(numbers)   # returns a tuple

result = min_max([4, 1, 7, 2, 9])
print(result)         # (1, 9)   ← tuple
low, high = result    # unpack
print(low, high)      # 1  9

# Can also unpack directly:
low2, high2 = min_max([3, 5, 1, 8])
print(low2, high2)    # 1  8

# -----------------------------------------------------------------------------
# 8. NAMED TUPLES
# -----------------------------------------------------------------------------
# namedtuple gives NAMES to each position — like a lightweight class.
# Lives in the collections module.

from collections import namedtuple

# Define the "template"
Point  = namedtuple("Point",  ["x", "y"])
Person = namedtuple("Person", ["name", "age", "city"])

# Create instances
p = Point(3, 7)
print(p)          # Point(x=3, y=7)
print(p.x)        # 3   ← access by name
print(p.y)        # 7
print(p[0])       # 3   ← still works by index too

bob = Person("Bob", 30, "London")
print(bob.name)   # Bob
print(bob.age)    # 30

# Named tuples are still immutable
# p.x = 10   # ← AttributeError: can't set attribute

# Useful methods
print(p._asdict())              # OrderedDict([('x', 3), ('y', 7)])
p2 = p._replace(x=99)          # returns a NEW named tuple with x changed
print(p2)                       # Point(x=99, y=7)
print(Point._fields)            # ('x', 'y')

# -----------------------------------------------------------------------------
# 9. TUPLE vs LIST — WHEN TO USE WHICH
# -----------------------------------------------------------------------------
# Use a TUPLE when:
#   ✅ Data should NOT change (coordinates, RGB color, DB record row)
#   ✅ You want to use it as a dictionary KEY (tuples are hashable, lists are not)
#   ✅ Returning multiple values from a function
#   ✅ Slightly faster and smaller memory footprint than a list

# Use a LIST when:
#   ✅ The collection may grow or shrink
#   ✅ You need to sort, shuffle, or modify elements

# Tuples as dict keys (lists cannot be used as keys!)
locations = {
    (40.7128, -74.0060): "New York",
    (51.5074, -0.1278):  "London",
    (52.2297, 21.0122):  "Warsaw",
}
print(locations[(40.7128, -74.0060)])   # New York

# =============================================================================
# SUMMARY
# =============================================================================
# ┌──────────────────────────────────────────────────────────────────┐
# │  Concept         │  Key Point                                    │
# ├──────────────────────────────────────────────────────────────────┤
# │  Immutable       │  Cannot change after creation                 │
# │  Single-item     │  (42,) — the comma is mandatory               │
# │  Packing         │  a, b, c = 1, 2, 3  or  t = 1, 2, 3          │
# │  Unpacking       │  name, age = person                           │
# │  * operator      │  first, *rest = (1,2,3,4,5)                   │
# │  Swap            │  x, y = y, x  (no temp variable!)             │
# │  namedtuple      │  named fields, still immutable                │
# │  As dict key     │  only tuples (not lists) can be dict keys     │
# └──────────────────────────────────────────────────────────────────┘
print("\nDay 02 — Tuples complete!")
