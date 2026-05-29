# =============================================================================
# Week 04 - Day 01 | Lists
# =============================================================================
# Topics: Creating lists, indexing, slicing, methods, mutability, nested lists
# =============================================================================

# -----------------------------------------------------------------------------
# 1. CREATING LISTS
# -----------------------------------------------------------------------------
# A list is an ORDERED, MUTABLE collection of items.
# Items can be of any type — even mixed.

empty      = []
numbers    = [1, 2, 3, 4, 5]
strings    = ["apple", "banana", "cherry"]
mixed      = [1, "hello", 3.14, True, None]
nested     = [[1, 2], [3, 4], [5, 6]]

print(numbers)   # [1, 2, 3, 4, 5]
print(mixed)     # [1, 'hello', 3.14, True, None]
print(type(numbers))  # <class 'list'>

# list() constructor
from_string = list("hello")   # ['h', 'e', 'l', 'l', 'o']
from_range  = list(range(5))  # [0, 1, 2, 3, 4]
print(from_string)
print(from_range)

# -----------------------------------------------------------------------------
# 2. INDEXING
# -----------------------------------------------------------------------------
# Lists are zero-indexed.
# Negative indexes count from the end.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#           0         1          2        3          4
#          -5        -4         -3       -2         -1

print(fruits[0])    # apple      (first)
print(fruits[2])    # cherry     (third)
print(fruits[-1])   # elderberry (last)
print(fruits[-2])   # date       (second from end)

# Accessing nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])   # 6  (row 1, col 2)
print(matrix[0][0])   # 1  (top-left)

# IndexError if out of range
# print(fruits[10])   # IndexError: list index out of range

# -----------------------------------------------------------------------------
# 3. SLICING
# -----------------------------------------------------------------------------
# list[start:stop:step]
# start → included, stop → excluded

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:5])     # [2, 3, 4]       start=2, stop=5
print(nums[:4])      # [0, 1, 2, 3]    from beginning to 4
print(nums[6:])      # [6, 7, 8, 9]    from 6 to end
print(nums[:])       # [0,1,...,9]      full copy
print(nums[::2])     # [0, 2, 4, 6, 8] every 2nd element
print(nums[1::2])    # [1, 3, 5, 7, 9] every 2nd, starting at 1
print(nums[::-1])    # [9,8,...,0]      reversed!
print(nums[7:2:-1])  # [7, 6, 5, 4, 3] backwards from 7 to 3

# Slicing never raises IndexError — it just returns what exists
print(nums[5:100])   # [5, 6, 7, 8, 9]

# -----------------------------------------------------------------------------
# 4. MUTABILITY — lists can be changed in place
# -----------------------------------------------------------------------------
colors = ["red", "green", "blue"]

# Change a single element
colors[1] = "yellow"
print(colors)   # ['red', 'yellow', 'blue']

# Change a slice
colors[1:3] = ["purple", "orange"]
print(colors)   # ['red', 'purple', 'orange']

# Delete an element
del colors[0]
print(colors)   # ['purple', 'orange']

# -----------------------------------------------------------------------------
# 5. COMMON LIST METHODS
# -----------------------------------------------------------------------------
nums = [3, 1, 4, 1, 5, 9, 2, 6]

# Adding elements
nums.append(7)          # adds to END          → [..., 7]
nums.insert(0, 99)      # insert at index 0    → [99, 3, 1, ...]
nums.extend([10, 11])   # extend with iterable → [..., 10, 11]
print(nums)

# Removing elements
nums.remove(99)         # removes FIRST occurrence of value
popped = nums.pop()     # removes & returns LAST element
popped2 = nums.pop(0)   # removes & returns element at index 0
print(f"Popped: {popped}, {popped2}")
print(nums)

# Searching
lst = [10, 20, 30, 20, 40]
print(lst.index(20))    # 1  (index of FIRST occurrence)
print(lst.count(20))    # 2  (how many times 20 appears)
print(20 in lst)        # True
print(99 in lst)        # False

# Sorting
letters = ["banana", "apple", "cherry", "date"]
letters.sort()                  # sorts IN PLACE (modifies original)
print(letters)                  # ['apple', 'banana', 'cherry', 'date']

letters.sort(reverse=True)      # reverse sort
print(letters)

nums2 = [3, 1, 4, 1, 5, 9]
sorted_copy = sorted(nums2)     # returns NEW sorted list, original unchanged
print(sorted_copy)
print(nums2)                    # still [3, 1, 4, 1, 5, 9]

# Reversing
nums2.reverse()                 # reverses IN PLACE
print(nums2)                    # [9, 5, 1, 4, 1, 3]

# Other useful methods
lst2 = [1, 2, 3]
lst2.clear()        # removes all items → []
print(lst2)

original = [1, 2, 3]
copy     = original.copy()   # shallow copy
print(copy)

# -----------------------------------------------------------------------------
# 6. LIST OPERATIONS
# -----------------------------------------------------------------------------
a = [1, 2, 3]
b = [4, 5, 6]

# Concatenation
print(a + b)         # [1, 2, 3, 4, 5, 6]

# Repetition
print(a * 3)         # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Length
print(len(a))        # 3

# Min / max / sum
nums3 = [4, 1, 7, 2, 9]
print(min(nums3))    # 1
print(max(nums3))    # 9
print(sum(nums3))    # 23

# -----------------------------------------------------------------------------
# 7. COPYING — SHALLOW vs REFERENCE
# -----------------------------------------------------------------------------
# ⚠️ IMPORTANT: assignment creates a REFERENCE, not a copy!

original = [1, 2, 3]
reference = original      # same object!
reference.append(4)
print(original)           # [1, 2, 3, 4]  ← original was changed too!

# To get an independent copy:
original2 = [1, 2, 3]
copy1 = original2.copy()   # method 1
copy2 = original2[:]       # method 2 (slicing)
copy3 = list(original2)    # method 3

copy1.append(99)
print(original2)           # [1, 2, 3]  ← unchanged

# -----------------------------------------------------------------------------
# 8. ITERATING OVER LISTS
# -----------------------------------------------------------------------------
fruits2 = ["apple", "banana", "cherry"]

# Basic loop
for fruit in fruits2:
    print(fruit)

# With index — enumerate()
for i, fruit in enumerate(fruits2):
    print(f"{i}: {fruit}")

# zip() — iterate two lists together
prices = [1.5, 0.75, 2.0]
for fruit, price in zip(fruits2, prices):
    print(f"{fruit}: ${price}")

# -----------------------------------------------------------------------------
# 9. NESTED LISTS (2D)
# -----------------------------------------------------------------------------
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Access element
print(grid[1][1])   # 5 (center)

# Iterate over 2D grid
for row in grid:
    for cell in row:
        print(cell, end=" ")
    print()

# Flatten with list comprehension (preview — covered fully in Day 05)
flat = [cell for row in grid for cell in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# =============================================================================
# SUMMARY
# =============================================================================
# ┌──────────────────────────────────────────────────────────────┐
# │  Operation       │  Example                                  │
# ├──────────────────────────────────────────────────────────────┤
# │  Index           │  lst[0], lst[-1]                          │
# │  Slice           │  lst[1:4], lst[::-1]                      │
# │  Add             │  append(), insert(), extend()             │
# │  Remove          │  remove(), pop(), del lst[i]              │
# │  Search          │  index(), count(), in                     │
# │  Sort            │  sort() in-place, sorted() new copy       │
# │  Copy            │  .copy(), [:], list()                     │
# │  Mutable         │  lst[i] = x  (strings can't do this!)     │
# └──────────────────────────────────────────────────────────────┘
print("\nDay 01 — Lists complete!")
