# =============================================================================
# Week 04 - Day 04 | Sets
# =============================================================================
# Topics: Creating sets, uniqueness, set operations, methods,
#         when to use sets, frozenset
# =============================================================================

# -----------------------------------------------------------------------------
# 1. CREATING SETS
# -----------------------------------------------------------------------------
# A set is an UNORDERED collection of UNIQUE, HASHABLE elements.
# No duplicates, no guaranteed order, no indexing.

empty_set = set()          # ⚠️ {} creates a dict, NOT a set — use set()
numbers   = {1, 2, 3, 4, 5}
mixed     = {1, "hello", 3.14, True}

print(numbers)          # {1, 2, 3, 4, 5}
print(type(numbers))    # <class 'set'>
print(type(set()))      # <class 'set'>
print(type({}))         # <class 'dict'>  ← common trap!

# Duplicates are AUTOMATICALLY removed
dupes = {1, 2, 2, 3, 3, 3, 4}
print(dupes)            # {1, 2, 3, 4}

# set() constructor — great for deduplicating a list
names = ["alice", "bob", "alice", "carol", "bob"]
unique_names = set(names)
print(unique_names)     # {'alice', 'bob', 'carol'}  (order may vary)

# Convert back to list if needed
unique_list = list(set(names))
print(unique_list)

# -----------------------------------------------------------------------------
# 2. BASIC PROPERTIES
# -----------------------------------------------------------------------------
s = {3, 1, 4, 1, 5, 9, 2, 6}

# Length
print(len(s))       # 7  (one duplicate removed)

# Membership test — O(1), much faster than list for large collections
print(3 in s)       # True
print(7 in s)       # False

# Sets are UNORDERED — no indexing, no slicing
# print(s[0])   # ← TypeError: 'set' object is not subscriptable

# Iteration (order is not guaranteed)
for item in s:
    print(item, end=" ")
print()

# -----------------------------------------------------------------------------
# 3. SET METHODS — ADDING & REMOVING
# -----------------------------------------------------------------------------
fruits = {"apple", "banana", "cherry"}

# Add one element
fruits.add("date")
print(fruits)

# add() is safe — adding an existing element does nothing
fruits.add("apple")
print(fruits)   # still same

# Remove — raises KeyError if not found
fruits.remove("banana")
print(fruits)
# fruits.remove("mango")  # ← KeyError!

# discard — removes if present, NO error if missing
fruits.discard("cherry")
fruits.discard("mango")   # no error
print(fruits)

# pop — removes and returns an ARBITRARY element (not predictable!)
popped = fruits.pop()
print(f"Popped: {popped}")

# clear — remove all elements
s_copy = {1, 2, 3}
s_copy.clear()
print(s_copy)   # set()

# update — add multiple elements from any iterable
s2 = {1, 2, 3}
s2.update([4, 5, 6])
s2.update("abc")   # adds 'a', 'b', 'c' as individual chars
print(s2)

# -----------------------------------------------------------------------------
# 4. SET OPERATIONS — THE REAL POWER
# -----------------------------------------------------------------------------
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

# UNION — elements in A OR B (or both)
print(a | b)              # {1, 2, 3, 4, 5, 6, 7, 8}
print(a.union(b))         # same

# INTERSECTION — elements in BOTH A AND B
print(a & b)              # {4, 5}
print(a.intersection(b))  # same

# DIFFERENCE — elements in A but NOT in B
print(a - b)              # {1, 2, 3}
print(a.difference(b))    # same
print(b - a)              # {6, 7, 8}  (order matters!)

# SYMMETRIC DIFFERENCE — elements in A OR B but NOT BOTH
print(a ^ b)                          # {1, 2, 3, 6, 7, 8}
print(a.symmetric_difference(b))      # same

# Visual summary:
# a = {1,2,3,4,5}   b = {4,5,6,7,8}
#         ┌─────────────────────────┐
#   a only│  1 2 3  │ both │  6 7 8 │ b only
#         │         │ 4 5  │        │
#         └─────────────────────────┘
# union   = all 8 elements
# intersect = 4, 5
# a-b     = 1, 2, 3
# b-a     = 6, 7, 8
# sym diff = 1, 2, 3, 6, 7, 8

# -----------------------------------------------------------------------------
# 5. SET COMPARISON OPERATIONS
# -----------------------------------------------------------------------------
x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
z = {10, 20}

# Subset — is every element of x also in y?
print(x.issubset(y))       # True    ({1,2,3} ⊆ {1,2,3,4,5})
print(x <= y)              # True    (same with operator)
print(x < y)               # True    (STRICT subset — x is not equal to y)
print(x < x)               # False   (x is not a strict subset of itself)
print(x <= x)              # True    (a set is a subset of itself)

# Superset — is every element of y also in x?
print(y.issuperset(x))     # True
print(y >= x)              # True
print(y > x)               # True    (strict superset)

# Disjoint — do they share NO elements?
print(x.isdisjoint(z))     # True    (no common elements)
print(x.isdisjoint(y))     # False   (they share 1, 2, 3)

# Equality
print({1, 2, 3} == {3, 1, 2})   # True  (order doesn't matter in sets)

# -----------------------------------------------------------------------------
# 6. IN-PLACE SET OPERATIONS (modify the set itself)
# -----------------------------------------------------------------------------
s = {1, 2, 3}

s |= {4, 5}         # union in place         → {1,2,3,4,5}
print(s)
s &= {2, 3, 4}      # intersection in place  → {2,3,4}
print(s)
s -= {4}            # difference in place    → {2,3}
print(s)
s ^= {1, 2}         # sym diff in place      → {1,3}
print(s)

# Method equivalents:
# s.update(other)                 → s |= other
# s.intersection_update(other)    → s &= other
# s.difference_update(other)      → s -= other
# s.symmetric_difference_update() → s ^= other

# -----------------------------------------------------------------------------
# 7. FROZENSET — IMMUTABLE SET
# -----------------------------------------------------------------------------
# frozenset is like a set but CANNOT be changed after creation.
# Use case: when you need a set as a dict key or inside another set.

fs = frozenset([1, 2, 3, 4])
print(fs)                  # frozenset({1, 2, 3, 4})
print(type(fs))            # <class 'frozenset'>

# Supports all read operations
print(1 in fs)             # True
print(fs | {5, 6})         # frozenset({1,2,3,4,5,6})

# Cannot be modified
# fs.add(5)    # ← AttributeError: 'frozenset' object has no attribute 'add'

# frozenset as a dict key (regular set cannot be a key — it's unhashable)
graph = {
    frozenset({1, 2}): "edge A",
    frozenset({2, 3}): "edge B",
}
print(graph[frozenset({1, 2})])   # edge A

# -----------------------------------------------------------------------------
# 8. PRACTICAL USE CASES
# -----------------------------------------------------------------------------

# USE CASE 1: Remove duplicates from a list (fastest way)
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = list(set(data))
print(unique)

# USE CASE 2: Fast membership test (much faster than list for large data)
valid_users = {"alice", "bob", "carol", "dave"}
user = "alice"
if user in valid_users:    # O(1) lookup
    print(f"{user} is valid")

# USE CASE 3: Find common elements between two lists
list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
common = set(list_a) & set(list_b)
print(common)   # {3, 4, 5}

# USE CASE 4: Find items in one list but not the other
only_in_a = set(list_a) - set(list_b)
print(only_in_a)   # {1, 2}

# USE CASE 5: Check for duplicates
def has_duplicates(lst):
    return len(lst) != len(set(lst))

print(has_duplicates([1, 2, 3, 2]))   # True
print(has_duplicates([1, 2, 3, 4]))   # False

# =============================================================================
# SUMMARY
# =============================================================================
# ┌────────────────────────────────────────────────────────────────────┐
# │  Concept           │  Key Point                                    │
# ├────────────────────────────────────────────────────────────────────┤
# │  Unique            │  Duplicates are silently ignored              │
# │  Unordered         │  No indexing, no slicing                      │
# │  Empty set         │  set() — NOT {} (that's a dict)               │
# │  add / discard     │  discard is safe (no error if missing)        │
# │  Union             │  a | b  — in either                           │
# │  Intersection      │  a & b  — in both                             │
# │  Difference        │  a - b  — in a but not b                      │
# │  Sym. difference   │  a ^ b  — in one but not both                 │
# │  frozenset         │  immutable set, can be a dict key             │
# └────────────────────────────────────────────────────────────────────┘
print("\nDay 04 — Sets complete!")
