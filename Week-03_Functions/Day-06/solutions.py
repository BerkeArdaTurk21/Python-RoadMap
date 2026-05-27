# =============================================================================
# Week 03 - Day 06 | Recursion — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# Understanding WHY each solution works matters more than the code itself.
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — Sum of Digits
# -----------------------------------------------------------------------------
# KEY INSIGHT:
#   digit_sum(123) = 3 + digit_sum(12)   ← last digit + rest
#                       = 3 + 2 + digit_sum(1)
#                                = 3 + 2 + 1 + digit_sum(0)  ← base case
#                                               = 0
# So the base case is n == 0 → return 0
# The recursive case: last digit = n % 10, rest = n // 10

def digit_sum(n):
    if n == 0:                          # BASE CASE
        return 0
    return (n % 10) + digit_sum(n // 10)   # RECURSIVE CASE

print("Solution 1 — Sum of Digits")
print(digit_sum(0))     # 0
print(digit_sum(5))     # 5
print(digit_sum(123))   # 6
print(digit_sum(9999))  # 36
print()

# -----------------------------------------------------------------------------
# Solution 2 — Count Occurrences
# -----------------------------------------------------------------------------
# KEY INSIGHT: Two types of items in the list:
#   - A sublist → recurse into it with count_occurrences(item, target)
#   - A plain value → check if it equals target (add 1 or 0)
# Base case: empty list → return 0

def count_occurrences(lst, target):
    if len(lst) == 0:               # BASE CASE: nothing left to check
        return 0

    first = lst[0]
    rest_count = count_occurrences(lst[1:], target)

    if isinstance(first, list):
        return count_occurrences(first, target) + rest_count   # recurse into sublist
    else:
        return (1 if first == target else 0) + rest_count      # plain value comparison

print("Solution 2 — Count Occurrences")
print(count_occurrences([1, 2, 3, 2], 2))               # 2
print(count_occurrences([1, [2, [3, 2]], 2], 2))         # 3
print(count_occurrences(["a", ["b", "a"], "c"], "a"))    # 2
print(count_occurrences([], 5))                          # 0
print()

# -----------------------------------------------------------------------------
# Solution 3 — Reverse a String
# -----------------------------------------------------------------------------
# KEY INSIGHT:
#   reverse("hello") = "o" + reverse("hell")
#                           = "o" + "l" + reverse("hel")
#                                        = ... until "" → ""
# Base case: empty string OR single character → return as-is

def reverse_string(s):
    if len(s) <= 1:               # BASE CASE: "" or single char
        return s
    return s[-1] + reverse_string(s[:-1])   # last char + reverse the rest

print("Solution 3 — Reverse a String")
print(repr(reverse_string("")))        # ''
print(repr(reverse_string("a")))       # 'a'
print(repr(reverse_string("hello")))   # 'olleh'
print(repr(reverse_string("Python")))  # 'nohtyP'
print()

# -----------------------------------------------------------------------------
# Solution 4 — Tower of Hanoi
# -----------------------------------------------------------------------------
# KEY INSIGHT:
#   To move n discs from source → target using auxiliary:
#   1. Move n-1 discs from source → auxiliary  (using target as helper)
#   2. Move the largest disc from source → target
#   3. Move n-1 discs from auxiliary → target  (using source as helper)
#
#   Base case: n == 0 → do nothing (nothing to move)
#
# Notice how elegantly recursion solves what looks like a complex puzzle!
# A loop would need to track state manually. Recursion describes it naturally.

def hanoi(n, source, target, auxiliary):
    if n == 0:                          # BASE CASE: nothing to move
        return
    hanoi(n - 1, source, auxiliary, target)       # Step 1: move n-1 to auxiliary
    print(f"Move disc {n} from {source} to {target}")  # Step 2: move largest
    hanoi(n - 1, auxiliary, target, source)       # Step 3: move n-1 to target

print("Solution 4 — Tower of Hanoi (3 discs)")
hanoi(3, "A", "C", "B")
# Move disc 1 from A to C
# Move disc 2 from A to B
# Move disc 1 from C to B
# Move disc 3 from A to C
# Move disc 1 from B to A
# Move disc 2 from B to C
# Move disc 1 from A to C
print()

# FUN FACT: Moving n discs requires exactly 2^n - 1 moves.
# hanoi(10) requires 1023 moves. hanoi(64) would require 18,446,744,073,709,551,615 moves!

# -----------------------------------------------------------------------------
# Solution 5 — Find Maximum in a List
# -----------------------------------------------------------------------------
# KEY INSIGHT:
#   max([7, 3, 9, 1, 5]) = max(7, max([3, 9, 1, 5]))
#                                = max(7, max(3, max([9, 1, 5])))
#                                              = ... until one element → return it
# Base case: single element → that IS the maximum.
# Recursive case: compare first element vs max of the rest.

def find_max(lst):
    if len(lst) == 1:               # BASE CASE: one element → it's the max
        return lst[0]
    rest_max = find_max(lst[1:])    # RECURSIVE CASE: max of the rest
    return lst[0] if lst[0] > rest_max else rest_max

print("Solution 5 — Find Maximum")
print(find_max([3]))               # 3
print(find_max([1, 5, 2]))         # 5
print(find_max([7, 3, 9, 1, 5]))   # 9
print(find_max([-3, -1, -7]))      # -1
print()

# =============================================================================
# BONUS — Why recursion is powerful (Tower of Hanoi insight)
# =============================================================================
# The iterative version of Tower of Hanoi is complex and hard to understand.
# The recursive version is 4 lines and reads almost like the problem description.
#
# This is the real power of recursion: it lets you EXPRESS the structure
# of the problem rather than manually managing state.
#
# "To move n discs to target, first move n-1 out of the way."
# That IS the code. That's beautiful.
