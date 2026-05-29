# =============================================================================
# Week 04 - Day 01 | Lists — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Reverse Without reverse()
# -----------------------------------------------------------------------------
# Given a list of numbers, return a new reversed list WITHOUT using
# .reverse() or [::-1].
#
# Hint: use a loop and build a new list from the end.
#
# Expected output:
#   reverse_list([1, 2, 3, 4, 5])  → [5, 4, 3, 2, 1]
#   reverse_list([10, 20])         → [20, 10]
#   reverse_list([42])             → [42]
#   reverse_list([])               → []

def reverse_list(lst):
    pass  # TODO


print("Exercise 1 — Reverse Without reverse()")
print(reverse_list([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]
print(reverse_list([10, 20]))           # [20, 10]
print(reverse_list([]))                 # []
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Remove Duplicates (preserve order)
# -----------------------------------------------------------------------------
# Given a list, return a new list with duplicates removed.
# The ORDER of first appearances must be preserved.
#
# Do NOT use set() directly (it doesn't preserve order).
#
# Expected output:
#   remove_duplicates([1, 2, 3, 2, 1, 4])    → [1, 2, 3, 4]
#   remove_duplicates(["a", "b", "a", "c"])  → ['a', 'b', 'c']
#   remove_duplicates([1, 1, 1])             → [1]
#   remove_duplicates([])                    → []

def remove_duplicates(lst):
    pass  # TODO


print("Exercise 2 — Remove Duplicates")
print(remove_duplicates([1, 2, 3, 2, 1, 4]))     # [1, 2, 3, 4]
print(remove_duplicates(["a", "b", "a", "c"]))   # ['a', 'b', 'c']
print(remove_duplicates([1, 1, 1]))               # [1]
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Rotate Left
# -----------------------------------------------------------------------------
# Write rotate_left(lst, n) that rotates the list n positions to the left.
# Rotating [1,2,3,4,5] by 2 gives [3,4,5,1,2].
#
# Hint: slicing is your friend.
#
# Expected output:
#   rotate_left([1, 2, 3, 4, 5], 2)  → [3, 4, 5, 1, 2]
#   rotate_left([1, 2, 3, 4, 5], 0)  → [1, 2, 3, 4, 5]
#   rotate_left([1, 2, 3, 4, 5], 5)  → [1, 2, 3, 4, 5]
#   rotate_left([10, 20, 30], 1)     → [20, 30, 10]

def rotate_left(lst, n):
    pass  # TODO


print("Exercise 3 — Rotate Left")
print(rotate_left([1, 2, 3, 4, 5], 2))   # [3, 4, 5, 1, 2]
print(rotate_left([1, 2, 3, 4, 5], 0))   # [1, 2, 3, 4, 5]
print(rotate_left([10, 20, 30], 1))       # [20, 30, 10]
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Chunk a List
# -----------------------------------------------------------------------------
# Write chunk(lst, size) that splits a list into sublists of length `size`.
# The last chunk may be smaller if the list doesn't divide evenly.
#
# Expected output:
#   chunk([1,2,3,4,5,6], 2)    → [[1,2],[3,4],[5,6]]
#   chunk([1,2,3,4,5], 2)      → [[1,2],[3,4],[5]]
#   chunk([1,2,3,4,5,6], 3)    → [[1,2,3],[4,5,6]]
#   chunk([], 3)               → []

def chunk(lst, size):
    pass  # TODO


print("Exercise 4 — Chunk a List")
print(chunk([1, 2, 3, 4, 5, 6], 2))   # [[1,2],[3,4],[5,6]]
print(chunk([1, 2, 3, 4, 5], 2))       # [[1,2],[3,4],[5]]
print(chunk([1, 2, 3, 4, 5, 6], 3))   # [[1,2,3],[4,5,6]]
print(chunk([], 3))                    # []
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Flatten One Level
# -----------------------------------------------------------------------------
# Write flatten_one(lst) that flattens exactly ONE level of nesting.
# Deeply nested lists are left as-is at the inner level.
#
# Expected output:
#   flatten_one([[1,2],[3,4],[5]])         → [1,2,3,4,5]
#   flatten_one([[1,[2,3]],[4]])           → [1,[2,3],4]
#   flatten_one([[], [1], [2, 3]])         → [1,2,3]
#   flatten_one([1, 2, 3])                → [1,2,3]

def flatten_one(lst):
    pass  # TODO


print("Exercise 5 — Flatten One Level")
print(flatten_one([[1, 2], [3, 4], [5]]))       # [1,2,3,4,5]
print(flatten_one([[1, [2, 3]], [4]]))           # [1,[2,3],4]
print(flatten_one([[], [1], [2, 3]]))            # [1,2,3]
print(flatten_one([1, 2, 3]))                   # [1,2,3]
