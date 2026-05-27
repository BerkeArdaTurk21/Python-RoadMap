# =============================================================================
# Week 03 - Day 06 | Recursion
# =============================================================================
# Topics: Base case, recursive case, call stack, practical recursion
# =============================================================================

# -----------------------------------------------------------------------------
# 1. WHAT IS RECURSION?
# -----------------------------------------------------------------------------
# A function that calls ITSELF is called recursive.
# Every recursive function needs TWO things:
#   1. BASE CASE   → the condition that STOPS the recursion
#   2. RECURSIVE CASE → the part that calls itself (with a simpler input)

# Without a base case → infinite loop → RecursionError (stack overflow)

# Simple example: countdown
def countdown(n):
    if n <= 0:           # BASE CASE: stop here
        print("Go!")
    else:                # RECURSIVE CASE: call itself with n-1
        print(n)
        countdown(n - 1)

countdown(5)
# Output: 5, 4, 3, 2, 1, Go!

# -----------------------------------------------------------------------------
# 2. THE CALL STACK
# -----------------------------------------------------------------------------
# Each function call adds a "frame" to the call stack.
# When the base case is hit, frames "unwind" back up.

# Let's trace factorial(3):
#   factorial(3)
#     └─ 3 * factorial(2)
#            └─ 2 * factorial(1)
#                   └─ 1 * factorial(0)
#                          └─ returns 1  ← base case
#                   └─ returns 1 * 1 = 1
#            └─ returns 2 * 1 = 2
#     └─ returns 3 * 2 = 6

def factorial(n):
    if n == 0:           # BASE CASE: 0! = 1 (by definition)
        return 1
    return n * factorial(n - 1)   # RECURSIVE CASE

print(factorial(0))   # 1
print(factorial(1))   # 1
print(factorial(5))   # 120
print(factorial(10))  # 3628800

# -----------------------------------------------------------------------------
# 3. FIBONACCI SEQUENCE
# -----------------------------------------------------------------------------
# F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

def fibonacci(n):
    if n == 0:           # BASE CASE 1
        return 0
    if n == 1:           # BASE CASE 2
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)   # RECURSIVE CASE

print(fibonacci(0))   # 0
print(fibonacci(6))   # 8
print(fibonacci(10))  # 55

# Print first 10 fibonacci numbers
fib_sequence = [fibonacci(i) for i in range(10)]
print(fib_sequence)   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ⚠️ NOTE: This naive fibonacci is slow for large n (exponential time).
# fibonacci(40) recalculates the same values millions of times.
# Solved with memoization (functools.lru_cache) — covered in Week 08.

# -----------------------------------------------------------------------------
# 4. SUM OF A LIST (RECURSIVE THINKING)
# -----------------------------------------------------------------------------
# Problem: sum [1, 2, 3, 4, 5]
# Think: sum([1,2,3,4,5]) = 1 + sum([2,3,4,5])
#                              = 1 + 2 + sum([3,4,5])
#                                       ... until sum([]) = 0

def recursive_sum(lst):
    if len(lst) == 0:    # BASE CASE: empty list
        return 0
    return lst[0] + recursive_sum(lst[1:])   # RECURSIVE CASE

print(recursive_sum([]))           # 0
print(recursive_sum([5]))          # 5
print(recursive_sum([1, 2, 3]))    # 6
print(recursive_sum([1, 2, 3, 4, 5]))  # 15

# -----------------------------------------------------------------------------
# 5. POWER FUNCTION
# -----------------------------------------------------------------------------
# x^n = x * x^(n-1)   (recursive case)
# x^0 = 1             (base case)

def power(base, exp):
    if exp == 0:         # BASE CASE
        return 1
    return base * power(base, exp - 1)   # RECURSIVE CASE

print(power(2, 0))   # 1
print(power(2, 3))   # 8
print(power(3, 4))   # 81
print(power(5, 2))   # 25

# -----------------------------------------------------------------------------
# 6. FLATTEN A NESTED LIST
# -----------------------------------------------------------------------------
# This is where recursion shines — loops struggle with unknown nesting depth!

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):        # it's a sublist → recurse
            result.extend(flatten(item))
        else:                             # it's a plain value → add it
            result.append(item)
    return result

nested = [1, [2, 3], [4, [5, 6]], [[7, [8, 9]]]]
print(flatten(nested))    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# A loop with fixed depth could not handle this generically.

# -----------------------------------------------------------------------------
# 7. BINARY SEARCH (RECURSIVE)
# -----------------------------------------------------------------------------
# Search a SORTED list by repeatedly halving the search space.
# Base cases: found it | list exhausted

def binary_search(lst, target, low=0, high=None):
    if high is None:
        high = len(lst) - 1

    if low > high:           # BASE CASE: not found
        return -1

    mid = (low + high) // 2

    if lst[mid] == target:   # BASE CASE: found
        return mid
    elif lst[mid] < target:  # search right half
        return binary_search(lst, target, mid + 1, high)
    else:                    # search left half
        return binary_search(lst, target, low, mid - 1)

sorted_list = [2, 5, 8, 12, 16, 23, 38, 42, 56, 72, 91]
print(binary_search(sorted_list, 23))   # 5  (index)
print(binary_search(sorted_list, 99))   # -1 (not found)
print(binary_search(sorted_list, 2))    # 0

# -----------------------------------------------------------------------------
# 8. RECURSION DEPTH LIMIT
# -----------------------------------------------------------------------------
# Python limits recursion depth to prevent stack overflow.
import sys
print(sys.getrecursionlimit())   # 1000 (default)

# You CAN increase it, but usually deep recursion signals a design problem:
# sys.setrecursionlimit(5000)

# If recursion is too deep → RecursionError
def infinite(n):
    return infinite(n + 1)   # NO base case!

# infinite(0)   # ← RecursionError: maximum recursion depth exceeded

# -----------------------------------------------------------------------------
# 9. RECURSION vs ITERATION — WHEN TO USE WHICH
# -----------------------------------------------------------------------------
# USE RECURSION when:
#   ✅ The problem is naturally recursive (trees, nested structures, divide & conquer)
#   ✅ Code clarity matters more than raw speed
#   ✅ Depth is bounded and predictable

# USE ITERATION when:
#   ✅ Simple counting / looping tasks
#   ✅ Performance is critical (no function call overhead)
#   ✅ Very deep recursion could hit Python's limit

# Iterative factorial (for comparison):
def factorial_iter(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(factorial_iter(5))   # 120  (same result, no call stack overhead)

# -----------------------------------------------------------------------------
# 10. PALINDROME CHECK (RECURSIVE)
# -----------------------------------------------------------------------------
# "racecar" → is first == last? recurse on the middle.

def is_palindrome(s):
    s = s.lower().replace(" ", "")   # normalize
    if len(s) <= 1:                  # BASE CASE: 0 or 1 char → palindrome
        return True
    if s[0] != s[-1]:                # BASE CASE: first ≠ last → not palindrome
        return False
    return is_palindrome(s[1:-1])    # RECURSIVE CASE: check the middle

print(is_palindrome("racecar"))      # True
print(is_palindrome("hello"))        # False
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("level"))        # True

# =============================================================================
# SUMMARY
# =============================================================================
# ┌─────────────────────────────────────────────────────────┐
# │  Concept          │  Key Point                          │
# ├─────────────────────────────────────────────────────────┤
# │  Base case        │  Stops recursion — ALWAYS required  │
# │  Recursive case   │  Calls itself with simpler input    │
# │  Call stack       │  Each call adds a frame; unwinds    │
# │  RecursionError   │  No base case OR too deep (>1000)   │
# │  Best use cases   │  Trees, nested data, divide/conquer │
# └─────────────────────────────────────────────────────────┘
print("\nDay 06 — Recursion complete!")
