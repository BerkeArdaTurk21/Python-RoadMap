# Week 2 - Day 4: break / continue / pass — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: First Negative Finder
# ─────────────────────────────────────────────
# Given the list below, loop through it and stop
# (using break) as soon as you find the first negative number.
# Print its value and index. If none found, print "No negatives."
#
# numbers = [4, 7, 2, 9, -3, 5, -1, 8]
#
# Expected output:
#   First negative: -3 at index 4


# ─────────────────────────────────────────────
# Exercise 2: Skip Banned Words
# ─────────────────────────────────────────────
# Given the sentence and banned words list below,
# print the sentence word by word — but skip any
# banned word using continue.
# At the end, print the cleaned sentence as one string.
#
# sentence = "the quick brown fox jumps over the lazy dog"
# banned = ["the", "over", "lazy"]
#
# Expected output (words printed one per line, then joined):
#   quick
#   brown
#   fox
#   jumps
#   dog
#   Cleaned: quick brown fox jumps dog


# ─────────────────────────────────────────────
# Exercise 3: Prime Number Finder
# ─────────────────────────────────────────────
# Print all prime numbers between 2 and 50.
# Use break in the inner loop + for/else to detect primes.
#
# Expected output:
#   2 3 5 7 11 13 17 19 23 29 31 37 41 43 47


# ─────────────────────────────────────────────
# Exercise 4: Loop with pass Skeleton
# ─────────────────────────────────────────────
# Given the list of transactions below, categorise each:
#   amount > 0   → "Credit"
#   amount < 0   → "Debit"
#   amount == 0  → leave as pass (do nothing, skip it)
#
# Print only Credit and Debit transactions in this format:
#   +200  → Credit
#   -50   → Debit
#
# transactions = [200, -50, 0, 150, -30, 0, -10, 75]


# ─────────────────────────────────────────────
# Exercise 5: Smart Shopping Cart
# ─────────────────────────────────────────────
# Given a list of (item, price) tuples and a budget,
# add items to the cart in order until the budget runs out.
# Use break when the next item would exceed the remaining budget.
# Use continue to skip items that cost 0 or less (invalid).
# Print each item added, then the final total and remaining budget.
#
# budget = 100
# items = [
#     ("Apple",  1.5),
#     ("Laptop", 999),
#     ("Book",   12),
#     ("Free",   0),
#     ("Pen",    2),
#     ("Notebook", 5),
# ]
#
# Expected output:
#   Added: Apple     $1.50   | Remaining: $98.50
#   Skipped (over budget): Laptop $999.00
#   Added: Book      $12.00  | Remaining: $86.50
#   Skipped (invalid price): Free $0.00
#   Added: Pen       $2.00   | Remaining: $84.50
#   Added: Notebook  $5.00   | Remaining: $79.50
#   ──────────────────────────
#   Total spent: $20.50  |  Budget left: $79.50
