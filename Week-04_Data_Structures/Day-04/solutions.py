# =============================================================================
# Week 04 - Day 04 | Sets — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — Unique Characters
# -----------------------------------------------------------------------------
# KEY INSIGHT: Convert the string to a set — sets automatically deduplicate.
# Filter out spaces first with replace() or a generator, then len() the set.

def unique_chars(s):
    return len(set(s.replace(" ", "")))

print("Solution 1 — Unique Characters")
print(unique_chars("hello"))         # 4
print(unique_chars("aabbcc"))        # 3
print(unique_chars("hello world"))   # 7
print(unique_chars(""))              # 0
print()

# WHY set(s)? Each character in the string becomes an element.
# set("hello") → {'h', 'e', 'l', 'o'}  (only 4 unique chars despite 'l' twice)

# -----------------------------------------------------------------------------
# Solution 2 — Common Elements
# -----------------------------------------------------------------------------
# KEY INSIGHT: Intersection (set1 & set2) gives exactly the common elements.
# sorted() converts the resulting set to a sorted list.

def common_elements(lst1, lst2):
    return sorted(set(lst1) & set(lst2))

print("Solution 2 — Common Elements")
print(common_elements([1, 2, 3, 4], [3, 4, 5, 6]))            # [3, 4]
print(common_elements(["a", "b", "c"], ["b", "c", "d"]))      # ['b', 'c']
print(common_elements([1, 2, 3], [4, 5, 6]))                  # []
print()

# -----------------------------------------------------------------------------
# Solution 3 — Unique to Each
# -----------------------------------------------------------------------------
# KEY INSIGHT: Difference in both directions.
#   set1 - set2 → elements only in lst1
#   set2 - set1 → elements only in lst2
# Return as sorted lists wrapped in a tuple.

def unique_to_each(lst1, lst2):
    s1, s2 = set(lst1), set(lst2)
    return (sorted(s1 - s2), sorted(s2 - s1))

print("Solution 3 — Unique to Each")
print(unique_to_each([1, 2, 3, 4], [3, 4, 5, 6]))     # ([1, 2], [5, 6])
print(unique_to_each(["a", "b"], ["b", "c"]))          # (['a'], ['c'])
print()

# -----------------------------------------------------------------------------
# Solution 4 — Remove Duplicates (keep order)
# -----------------------------------------------------------------------------
# KEY INSIGHT: Use a set to TRACK what we've already seen in O(1) per lookup.
# Build the result list by appending only items not yet in "seen".
# This preserves original order (unlike converting directly to a set).

def deduplicate(lst):
    seen   = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print("Solution 4 — Remove Duplicates (keep order)")
print(deduplicate([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))   # [3, 1, 4, 5, 9, 2, 6]
print(deduplicate(["b", "a", "b", "c", "a"]))          # ['b', 'a', 'c']
print(deduplicate([1, 2, 3]))                          # [1, 2, 3]
print()

# WHY not just list(set(lst))?
# set() destroys order. {3,1,4,1,5} might give {1,3,4,5} in any order.
# This solution preserves first-appearance order.

# -----------------------------------------------------------------------------
# Solution 5 — All Unique Across Lists
# -----------------------------------------------------------------------------
# KEY INSIGHT: Convert each list to a set (removes internal dupes — we only
# care about cross-list overlap). Then check that the total count of UNION
# equals the sum of individual unique counts.
#
# If any element appears in two different lists, the union will be smaller
# than the sum → return False.

def all_unique(*lists):
    sets        = [set(lst) for lst in lists]
    union_size  = len(set.union(*sets))
    total_size  = sum(len(s) for s in sets)
    return union_size == total_size

print("Solution 5 — All Unique Across Lists")
print(all_unique([1, 2, 3], [4, 5, 6], [7, 8, 9]))   # True
print(all_unique([1, 2, 3], [3, 4, 5]))               # False
print(all_unique([1, 1, 2], [3, 3, 4]))               # True
print()

# Trace for all_unique([1,2,3], [3,4,5]):
#   sets = [{1,2,3}, {3,4,5}]
#   union = {1,2,3,4,5} → size 5
#   total = 3 + 3 = 6
#   5 != 6 → False  (element 3 is shared)
#
# Trace for all_unique([1,1,2], [3,3,4]):
#   sets = [{1,2}, {3,4}]   (internal dupes removed by set())
#   union = {1,2,3,4} → size 4
#   total = 2 + 2 = 4
#   4 == 4 → True  (no cross-list overlap)
