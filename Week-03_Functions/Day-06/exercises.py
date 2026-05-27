# =============================================================================
# Week 03 - Day 06 | Recursion — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# No solutions here — that's the point!
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Sum of Digits
# -----------------------------------------------------------------------------
# Write a recursive function digit_sum(n) that returns the sum of all
# digits in a non-negative integer.
#
# Rules:
# - Must use recursion (not str() tricks or loops)
# - Handle n == 0 as a base case
#
# Hint: the last digit is n % 10, the rest is n // 10
#
# Expected output:
#   digit_sum(0)    → 0
#   digit_sum(5)    → 5
#   digit_sum(123)  → 6   (1 + 2 + 3)
#   digit_sum(9999) → 36  (9 + 9 + 9 + 9)

def digit_sum(n):
    pass  # TODO: implement recursively


print("Exercise 1 — Sum of Digits")
print(digit_sum(0))     # 0
print(digit_sum(5))     # 5
print(digit_sum(123))   # 6
print(digit_sum(9999))  # 36
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Count Occurrences
# -----------------------------------------------------------------------------
# Write a recursive function count_occurrences(lst, target) that returns
# how many times target appears in a (possibly nested) list.
#
# Expected output:
#   count_occurrences([1, 2, 3, 2], 2)              → 2
#   count_occurrences([1, [2, [3, 2]], 2], 2)        → 3
#   count_occurrences(["a", ["b", "a"], "c"], "a")   → 2
#   count_occurrences([], 5)                         → 0

def count_occurrences(lst, target):
    pass  # TODO: implement recursively


print("Exercise 2 — Count Occurrences")
print(count_occurrences([1, 2, 3, 2], 2))               # 2
print(count_occurrences([1, [2, [3, 2]], 2], 2))         # 3
print(count_occurrences(["a", ["b", "a"], "c"], "a"))    # 2
print(count_occurrences([], 5))                          # 0
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Reverse a String
# -----------------------------------------------------------------------------
# Write a recursive function reverse_string(s) that returns the reversed
# version of a string.
#
# Do NOT use s[::-1] or reversed() — use recursion!
#
# Hint: reverse_string("hello") = "o" + reverse_string("hell")
#
# Expected output:
#   reverse_string("")       → ""
#   reverse_string("a")      → "a"
#   reverse_string("hello")  → "olleh"
#   reverse_string("Python") → "nohtyP"

def reverse_string(s):
    pass  # TODO: implement recursively


print("Exercise 3 — Reverse a String")
print(repr(reverse_string("")))        # ''
print(repr(reverse_string("a")))       # 'a'
print(repr(reverse_string("hello")))   # 'olleh'
print(repr(reverse_string("Python")))  # 'nohtyP'
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Tower of Hanoi
# -----------------------------------------------------------------------------
# The classic recursion puzzle: move n discs from peg A to peg C using peg B.
# Rules: never place a larger disc on a smaller one; move one disc at a time.
#
# Write hanoi(n, source, target, auxiliary) that prints each move.
#
# Expected output for hanoi(3, "A", "C", "B"):
#   Move disc 1 from A to C
#   Move disc 2 from A to B
#   Move disc 1 from C to B
#   Move disc 3 from A to C
#   Move disc 1 from B to A
#   Move disc 2 from B to C
#   Move disc 1 from A to C

def hanoi(n, source, target, auxiliary):
    pass  # TODO: implement recursively


print("Exercise 4 — Tower of Hanoi (3 discs)")
hanoi(3, "A", "C", "B")
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Find Maximum in a List
# -----------------------------------------------------------------------------
# Write a recursive function find_max(lst) that returns the largest element.
# Do NOT use Python's built-in max() function.
#
# Approach: max of a list = max(first element, max of the rest)
#
# Expected output:
#   find_max([3])              → 3
#   find_max([1, 5, 2])        → 5
#   find_max([7, 3, 9, 1, 5])  → 9
#   find_max([-3, -1, -7])     → -1

def find_max(lst):
    pass  # TODO: implement recursively


print("Exercise 5 — Find Maximum")
print(find_max([3]))               # 3
print(find_max([1, 5, 2]))         # 5
print(find_max([7, 3, 9, 1, 5]))   # 9
print(find_max([-3, -1, -7]))      # -1
