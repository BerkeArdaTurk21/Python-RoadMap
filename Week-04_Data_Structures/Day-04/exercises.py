# =============================================================================
# Week 04 - Day 04 | Sets — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Unique Characters
# -----------------------------------------------------------------------------
# Write unique_chars(s) that returns the number of UNIQUE characters in a string.
# Spaces should be ignored (don't count them).
#
# Expected output:
#   unique_chars("hello")          → 4   (h, e, l, o — 'l' appears twice)
#   unique_chars("aabbcc")         → 3
#   unique_chars("hello world")    → 7   (h,e,l,o,w,r,d — space ignored)
#   unique_chars("")               → 0

def unique_chars(s):
    pass  # TODO


print("Exercise 1 — Unique Characters")
print(unique_chars("hello"))         # 4
print(unique_chars("aabbcc"))        # 3
print(unique_chars("hello world"))   # 7
print(unique_chars(""))              # 0
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Common Elements
# -----------------------------------------------------------------------------
# Write common_elements(lst1, lst2) that returns a SORTED LIST of elements
# that appear in both lists. No duplicates in the result.
#
# Expected output:
#   common_elements([1,2,3,4], [3,4,5,6])       → [3, 4]
#   common_elements(["a","b","c"], ["b","c","d"]) → ['b', 'c']
#   common_elements([1,2,3], [4,5,6])            → []

def common_elements(lst1, lst2):
    pass  # TODO


print("Exercise 2 — Common Elements")
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))            # [3, 4]
print(common_elements(["a", "b", "c"], ["b", "c", "d"]))      # ['b', 'c']
print(common_elements([1, 2, 3], [4, 5, 6]))                  # []
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Unique to Each
# -----------------------------------------------------------------------------
# Write unique_to_each(lst1, lst2) that returns a tuple:
#   (elements only in lst1, elements only in lst2)
# Both results should be sorted lists.
#
# Expected output:
#   unique_to_each([1,2,3,4], [3,4,5,6])  → ([1, 2], [5, 6])
#   unique_to_each(["a","b"], ["b","c"])   → (['a'], ['c'])

def unique_to_each(lst1, lst2):
    pass  # TODO


print("Exercise 3 — Unique to Each")
print(unique_to_each([1, 2, 3, 4], [3, 4, 5, 6]))     # ([1, 2], [5, 6])
print(unique_to_each(["a", "b"], ["b", "c"]))          # (['a'], ['c'])
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Remove Duplicates (keep order)
# -----------------------------------------------------------------------------
# Write deduplicate(lst) that removes duplicates while PRESERVING the original
# order of first appearances.
#
# You may use a set as a helper (to track what you've seen) but the RESULT
# must be a list in the original order.
#
# Expected output:
#   deduplicate([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])  → [3, 1, 4, 5, 9, 2, 6]
#   deduplicate(["b", "a", "b", "c", "a"])        → ['b', 'a', 'c']
#   deduplicate([1, 2, 3])                        → [1, 2, 3]

def deduplicate(lst):
    pass  # TODO


print("Exercise 4 — Remove Duplicates (keep order)")
print(deduplicate([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))   # [3, 1, 4, 5, 9, 2, 6]
print(deduplicate(["b", "a", "b", "c", "a"]))          # ['b', 'a', 'c']
print(deduplicate([1, 2, 3]))                          # [1, 2, 3]
print()

# -----------------------------------------------------------------------------
# Exercise 5 — All Unique Across Lists
# -----------------------------------------------------------------------------
# Write all_unique(*lists) that returns True if no element appears in more
# than one of the given lists. The lists themselves may have internal
# duplicates — only cross-list duplicates matter.
#
# Expected output:
#   all_unique([1,2,3], [4,5,6], [7,8,9])     → True
#   all_unique([1,2,3], [3,4,5])              → False  (3 is shared)
#   all_unique([1,1,2], [3,3,4])              → True   (no cross-list overlap)

def all_unique(*lists):
    pass  # TODO


print("Exercise 5 — All Unique Across Lists")
print(all_unique([1, 2, 3], [4, 5, 6], [7, 8, 9]))   # True
print(all_unique([1, 2, 3], [3, 4, 5]))               # False
print(all_unique([1, 1, 2], [3, 3, 4]))               # True
