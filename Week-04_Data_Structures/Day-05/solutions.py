# =============================================================================
# Week 04 - Day 05 | Comprehensions — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — FizzBuzz with a List Comprehension
# -----------------------------------------------------------------------------
# KEY INSIGHT: Use a ternary chain inside the comprehension.
# The condition order matters: check divisible-by-15 FIRST.
# If you check 3 first, "FizzBuzz" would never be reached.
#
# Pattern: (A if cond1 else (B if cond2 else (C if cond3 else D)))

def fizzbuzz(n):
    return [
        "FizzBuzz" if x % 15 == 0 else
        "Fizz"     if x %  3 == 0 else
        "Buzz"     if x %  5 == 0 else
        x
        for x in range(1, n + 1)
    ]

print("Solution 1 — FizzBuzz Comprehension")
print(fizzbuzz(15))
# [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
print()

# WHY check % 15 first?
# 15 is divisible by both 3 and 5. If we checked % 3 first, 15 → "Fizz" (wrong).

# -----------------------------------------------------------------------------
# Solution 2 — Word Lengths Dict
# -----------------------------------------------------------------------------
# KEY INSIGHT: Dict comprehension with a filter condition.
# {word: len(word) for word in words if len(word) >= 4}
# The 'if' comes at the END of the comprehension — it filters which words enter.

def word_lengths(words):
    return {word: len(word) for word in words if len(word) >= 4}

print("Solution 2 — Word Lengths Dict")
print(word_lengths(["hi", "hello", "hey", "world", "sun", "python"]))
# {'hello': 5, 'world': 5, 'python': 6}
print()

# -----------------------------------------------------------------------------
# Solution 3 — Transpose a Matrix
# -----------------------------------------------------------------------------
# KEY INSIGHT: For each column index j, collect matrix[row][j] for all rows.
# Outer loop: j over columns (range of row width)
# Inner loop: row over each row in the matrix
#
# transpose[j] = [matrix[row][j] for each row]

def transpose(matrix):
    return [[row[j] for row in matrix] for j in range(len(matrix[0]))]

print("Solution 3 — Transpose a Matrix")
print(transpose([[1, 2, 3], [4, 5, 6]]))         # [[1,4],[2,5],[3,6]]
print(transpose([[1, 2], [3, 4], [5, 6]]))        # [[1,3,5],[2,4,6]]
print()

# Reading it aloud: "For each column j, build a list of matrix[row][j] for all rows."
# zip(*matrix) achieves the same thing — but knowing the manual way builds intuition.

# BONUS — idiomatic Python transpose:
print([list(row) for row in zip(*[[1,2,3],[4,5,6]])])   # [[1,4],[2,5],[3,6]]

# -----------------------------------------------------------------------------
# Solution 4 — Unique Vowels per Word
# -----------------------------------------------------------------------------
# KEY INSIGHT: Dict comprehension where the VALUE is itself a set comprehension.
# {word: {c for c in word if c in VOWELS} for word in words}
#
# Inner set comp: {c for c in word if c in VOWELS}
#   → collects only vowel characters, deduplicated by the set.

VOWELS = set("aeiou")

def vowel_map(words):
    return {word: {c for c in word if c in VOWELS} for word in words}

print("Solution 4 — Unique Vowels per Word")
result = vowel_map(["hello", "python", "beautiful"])
for word, vowels in result.items():
    print(f"  {word}: {sorted(vowels)}")
# hello:     ['e', 'o']
# python:    ['o']
# beautiful: ['a', 'e', 'i', 'u']
print()

# -----------------------------------------------------------------------------
# Solution 5 — Lazy Sum of Squares (generator expression)
# -----------------------------------------------------------------------------
# KEY INSIGHT: sum() accepts any iterable — pass a generator directly.
# No list is created in memory; values are produced and consumed one at a time.
#
# sum(x**2 for x in range(1, n+1) if x % 2 != 0)
# The generator filters odd numbers, squares them, sum() adds them up.

def sum_of_squares(n):
    return sum(x ** 2 for x in range(1, n + 1) if x % 2 != 0)

print("Solution 5 — Lazy Sum of Squares (generator)")
print(sum_of_squares(10))   # 165  (1+9+25+49+81)
print(sum_of_squares(5))    # 35   (1+9+25)
print(sum_of_squares(1))    # 1
print()

# WHY generator instead of list?
# sum([x**2 for x in ...]) — builds entire list THEN sums it: two passes, more memory.
# sum(x**2 for x in ...)   — generates and sums in ONE pass: O(1) memory.
# For large n, the difference is significant.
