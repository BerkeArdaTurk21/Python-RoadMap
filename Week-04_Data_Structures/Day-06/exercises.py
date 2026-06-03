# =============================================================================
# Week 04 - Day 06 | collections Module — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# =============================================================================
from collections import Counter, defaultdict, namedtuple, deque

# -----------------------------------------------------------------------------
# Exercise 1 — Top 3 Most Common Words
# -----------------------------------------------------------------------------
# Write top_words(text, n) that returns the n most common words in the text.
# Case-insensitive. Strip punctuation by replacing .,!? with empty string.
# Return a list of (word, count) tuples.
#
# Expected output:
#   top_words("to be or not to be that is the question", 3)
#   → [('to', 2), ('be', 2), ('or', 1)]  (or any correct top-3)
#
#   top_words("the cat sat on the mat the cat", 2)
#   → [('the', 3), ('cat', 2)]

def top_words(text, n):
    pass  # TODO: use Counter


print("Exercise 1 — Top 3 Most Common Words")
print(top_words("to be or not to be that is the question", 3))
print(top_words("the cat sat on the mat the cat", 2))
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Group Anagrams
# -----------------------------------------------------------------------------
# Write group_anagrams(words) that groups words that are anagrams of each other.
# Return a list of lists. Each inner list contains anagram words.
# Order within groups and order of groups does not matter.
#
# Hint: two words are anagrams if sorted(word) is the same.
#       Use defaultdict(list) with sorted(word) as the key.
#
# Expected output:
#   group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
#   → [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]  (any order)

def group_anagrams(words):
    pass  # TODO: use defaultdict(list)


print("Exercise 2 — Group Anagrams")
groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
for g in sorted(groups, key=len, reverse=True):
    print(sorted(g))
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Named Tuple: Book Catalog
# -----------------------------------------------------------------------------
# Define a namedtuple Book with fields: title, author, year, genre
#
# 1. Create a list of 4 books (your choice of data)
# 2. Write oldest_book(books) that returns the Book with the smallest year
# 3. Write books_by_genre(books, genre) that returns a list of titles
#    in the given genre (case-insensitive)
#
# Expected:
#   oldest_book(books) → Book with smallest .year
#   books_by_genre(books, "fiction") → list of title strings

Book = namedtuple("Book", ["title", "author", "year", "genre"])

books = [
    Book("1984",                    "George Orwell",    1949, "fiction"),
    Book("Clean Code",              "Robert Martin",    2008, "technical"),
    Book("Brave New World",         "Aldous Huxley",    1932, "fiction"),
    Book("The Pragmatic Programmer","David Thomas",     1999, "technical"),
]

def oldest_book(books):
    pass  # TODO


def books_by_genre(books, genre):
    pass  # TODO


print("Exercise 3 — Book Catalog")
print("Oldest:", oldest_book(books))
print("Fiction titles:", books_by_genre(books, "fiction"))
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Sliding Window Maximum
# -----------------------------------------------------------------------------
# Write sliding_max(lst, k) that returns a list of the maximum value
# in each sliding window of size k.
#
# Use a deque to solve this efficiently.
# (Hint: you can also solve it simply with slicing — the deque approach
#  is faster for large lists, but for this exercise either is fine.)
#
# Expected output:
#   sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3)
#   → [3, 3, 5, 5, 6, 7]
#
#   sliding_max([4, 2, 5, 1, 3], 2)
#   → [4, 5, 5, 3]

def sliding_max(lst, k):
    pass  # TODO: use deque or slicing


print("Exercise 4 — Sliding Window Maximum")
print(sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
print(sliding_max([4, 2, 5, 1, 3], 2))                # [4, 5, 5, 3]
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Character Frequency Difference
# -----------------------------------------------------------------------------
# Write char_diff(s1, s2) that returns a Counter showing the difference
# in character frequencies between s1 and s2.
# Positive count → character appears more in s1.
# Negative count → character appears more in s2.
# Zero-count characters should NOT appear in the result.
#
# Hint: Counter subtraction drops zeros, but you need signed differences.
#       Build two Counters and subtract using regular dict arithmetic.
#
# Expected output:
#   char_diff("aabbcc", "abcdef")
#   → {'a': 1, 'b': 1, 'c': 1, 'd': -1, 'e': -1, 'f': -1}

def char_diff(s1, s2):
    pass  # TODO: use Counter


print("Exercise 5 — Character Frequency Difference")
print(char_diff("aabbcc", "abcdef"))
# {'a': 1, 'b': 1, 'c': 1, 'd': -1, 'e': -1, 'f': -1}
