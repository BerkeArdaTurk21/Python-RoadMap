# =============================================================================
# Week 04 - Day 01 | Lists — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — Reverse Without reverse()
# -----------------------------------------------------------------------------
# KEY INSIGHT: Build a new list by iterating the original from the last index
# down to 0. range(len-1, -1, -1) generates indices in reverse order.

def reverse_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

print("Solution 1 — Reverse Without reverse()")
print(reverse_list([1, 2, 3, 4, 5]))   # [5, 4, 3, 2, 1]
print(reverse_list([10, 20]))           # [20, 10]
print(reverse_list([]))                 # []
print()

# BONUS: the Pythonic way once you learn slicing is lst[::-1]
# But building it manually reinforces indexing understanding.

# -----------------------------------------------------------------------------
# Solution 2 — Remove Duplicates (preserve order)
# -----------------------------------------------------------------------------
# KEY INSIGHT: Keep a "seen" set for O(1) lookup, but build the result as a
# list to preserve insertion order. If item not in seen → add to both.

def remove_duplicates(lst):
    seen   = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print("Solution 2 — Remove Duplicates")
print(remove_duplicates([1, 2, 3, 2, 1, 4]))     # [1, 2, 3, 4]
print(remove_duplicates(["a", "b", "a", "c"]))   # ['a', 'b', 'c']
print(remove_duplicates([1, 1, 1]))               # [1]
print()

# WHY not just set()? set({1,2,3,2,1,4}) → {1,2,3,4} but ORDER is not guaranteed.

# -----------------------------------------------------------------------------
# Solution 3 — Rotate Left
# -----------------------------------------------------------------------------
# KEY INSIGHT: Rotating n positions left = lst[n:] + lst[:n]
# Use n % len(lst) to handle n >= length gracefully.

def rotate_left(lst, n):
    if not lst:
        return lst
    n = n % len(lst)          # handle n >= len(lst)
    return lst[n:] + lst[:n]

print("Solution 3 — Rotate Left")
print(rotate_left([1, 2, 3, 4, 5], 2))   # [3, 4, 5, 1, 2]
print(rotate_left([1, 2, 3, 4, 5], 0))   # [1, 2, 3, 4, 5]
print(rotate_left([10, 20, 30], 1))       # [20, 30, 10]
print()

# Trace: [1,2,3,4,5], n=2 → lst[2:] = [3,4,5], lst[:2] = [1,2] → [3,4,5,1,2]

# -----------------------------------------------------------------------------
# Solution 4 — Chunk a List
# -----------------------------------------------------------------------------
# KEY INSIGHT: Step through the list with a stride of `size`.
# range(0, len(lst), size) generates the start index of each chunk.
# Each chunk is lst[i : i+size].

def chunk(lst, size):
    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i : i + size])
    return result

print("Solution 4 — Chunk a List")
print(chunk([1, 2, 3, 4, 5, 6], 2))   # [[1,2],[3,4],[5,6]]
print(chunk([1, 2, 3, 4, 5], 2))       # [[1,2],[3,4],[5]]
print(chunk([1, 2, 3, 4, 5, 6], 3))   # [[1,2,3],[4,5,6]]
print(chunk([], 3))                    # []
print()

# Slicing past the end is safe — lst[4:999] just returns what exists.

# -----------------------------------------------------------------------------
# Solution 5 — Flatten One Level
# -----------------------------------------------------------------------------
# KEY INSIGHT: Loop through items. If an item IS a list → extend result with it
# (adds its elements individually). If NOT a list → append it as-is.
# This flattens exactly one level regardless of deeper nesting.

def flatten_one(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(item)   # spread the sublist items in
        else:
            result.append(item)   # plain value → add directly
    return result

print("Solution 5 — Flatten One Level")
print(flatten_one([[1, 2], [3, 4], [5]]))       # [1,2,3,4,5]
print(flatten_one([[1, [2, 3]], [4]]))           # [1,[2,3],4]
print(flatten_one([[], [1], [2, 3]]))            # [1,2,3]
print(flatten_one([1, 2, 3]))                   # [1,2,3]
print()

# WHY extend not append?
# append([3,4]) → adds the list AS ONE ITEM: [..., [3,4]]
# extend([3,4]) → spreads the items in:     [..., 3, 4]
