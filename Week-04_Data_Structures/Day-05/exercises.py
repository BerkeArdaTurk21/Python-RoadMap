# =============================================================================
# Week 04 - Day 05 | Comprehensions — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# Every solution must use a comprehension (list / dict / set / generator).
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — FizzBuzz with a List Comprehension
# -----------------------------------------------------------------------------
# Build the FizzBuzz list for numbers 1–30 using a list comprehension.
# Rules:
#   - Divisible by both 3 and 5 → "FizzBuzz"
#   - Divisible by 3 only       → "Fizz"
#   - Divisible by 5 only       → "Buzz"
#   - Otherwise                 → the number itself (as an int)
#
# Expected (first 15):
#   [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz',
#    11, 'Fizz', 13, 14, 'FizzBuzz', ...]

def fizzbuzz(n):
    pass  # TODO: return list comprehension


print("Exercise 1 — FizzBuzz Comprehension")
print(fizzbuzz(15))
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Word Lengths Dict
# -----------------------------------------------------------------------------
# Given a list of words, build a dict {word: len(word)} using a dict comprehension.
# Exclude words shorter than 4 characters.
#
# Expected output:
#   word_lengths(["hi", "hello", "hey", "world", "sun", "python"])
#   → {'hello': 5, 'world': 5, 'python': 6}

def word_lengths(words):
    pass  # TODO: dict comprehension


print("Exercise 2 — Word Lengths Dict")
print(word_lengths(["hi", "hello", "hey", "world", "sun", "python"]))
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Transpose a Matrix
# -----------------------------------------------------------------------------
# Given an N×M matrix (list of lists), return its transpose using a nested
# list comprehension. In a transpose, rows become columns and vice versa.
#
# Hint: transpose[i][j] = matrix[j][i]
# Use range(len(matrix[0])) for the outer loop (number of columns).
#
# Expected output:
#   transpose([[1,2,3],[4,5,6]])
#   → [[1, 4], [2, 5], [3, 6]]
#
#   transpose([[1,2],[3,4],[5,6]])
#   → [[1,3,5],[2,4,6]]

def transpose(matrix):
    pass  # TODO: nested list comprehension


print("Exercise 3 — Transpose a Matrix")
print(transpose([[1, 2, 3], [4, 5, 6]]))         # [[1,4],[2,5],[3,6]]
print(transpose([[1, 2], [3, 4], [5, 6]]))        # [[1,3,5],[2,4,6]]
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Unique Vowels per Word
# -----------------------------------------------------------------------------
# Given a list of words, build a dict {word: set_of_unique_vowels}
# using a dict comprehension with a nested set comprehension for the values.
#
# Vowels: a, e, i, o, u  (lowercase)
#
# Expected output:
#   vowel_map(["hello", "python", "beautiful"])
#   → {'hello': {'e', 'o'}, 'python': {'o'}, 'beautiful': {'a', 'e', 'i', 'u'}}

VOWELS = set("aeiou")

def vowel_map(words):
    pass  # TODO: dict comprehension + set comprehension


print("Exercise 4 — Unique Vowels per Word")
result = vowel_map(["hello", "python", "beautiful"])
for word, vowels in result.items():
    print(f"  {word}: {sorted(vowels)}")
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Lazy Sum of Squares
# -----------------------------------------------------------------------------
# Write sum_of_squares(n) using a GENERATOR EXPRESSION (not a list
# comprehension) passed directly to sum().
# Return the sum of squares of all odd numbers from 1 to n (inclusive).
#
# Expected output:
#   sum_of_squares(10)  → 165   (1² + 3² + 5² + 7² + 9²)
#   sum_of_squares(5)   → 35    (1² + 3² + 5²)
#   sum_of_squares(1)   → 1

def sum_of_squares(n):
    pass  # TODO: use sum(generator expression)


print("Exercise 5 — Lazy Sum of Squares (generator)")
print(sum_of_squares(10))   # 165
print(sum_of_squares(5))    # 35
print(sum_of_squares(1))    # 1
