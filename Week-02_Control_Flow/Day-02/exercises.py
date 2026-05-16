# Week 2 - Day 2: for Loops — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: Multiplication Table
# ─────────────────────────────────────────────
# Ask the user for a number (integer).
# Print its multiplication table from 1 to 10.
#
# Expected output (input = 7):
#   7  x  1  =  7
#   7  x  2  =  14
#   7  x  3  =  21
#   ...
#   7  x  10 =  70


# ─────────────────────────────────────────────
# Exercise 2: Word Frequency Counter
# ─────────────────────────────────────────────
# Given the sentence below, count how many times
# each word appears and print each word with its count.
# Ignore case (treat "The" and "the" as the same word).
#
# sentence = "the cat sat on the mat and the cat sat"
#
# Expected output (any order):
#   the: 3
#   cat: 2
#   sat: 2
#   on: 1
#   mat: 1
#   and: 1


# ─────────────────────────────────────────────
# Exercise 3: Student Grade Summary
# ─────────────────────────────────────────────
# Given the list of students below, print a formatted
# summary showing name, average score, and letter grade.
#
# students = [
#     ("Alice",   [88, 92, 95]),
#     ("Bob",     [60, 55, 70]),
#     ("Charlie", [78, 82, 80]),
# ]
#
# Grading scale:
#   90+ → A,  80+ → B,  70+ → C,  60+ → D,  below 60 → F
#
# Expected output:
#   Alice   | Avg: 91.7 | Grade: A
#   Bob     | Avg: 61.7 | Grade: D
#   Charlie | Avg: 80.0 | Grade: B


# ─────────────────────────────────────────────
# Exercise 4: Number Pattern Printer
# ─────────────────────────────────────────────
# Ask the user for a number n.
# Print a right-aligned triangle of numbers.
#
# Expected output (n = 4):
#   1
#   1 2
#   1 2 3
#   1 2 3 4


# ─────────────────────────────────────────────
# Exercise 5: Inventory Checker
# ─────────────────────────────────────────────
# Given the two lists below, use zip() to pair each
# product with its stock. Print a formatted inventory
# report and at the end print how many products are
# out of stock (stock == 0).
#
# products = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
# stock    = [50, 0, 23, 0, 8]
#
# Expected output:
#   Apple       : 50 units
#   Banana      :  0 units  ← OUT OF STOCK
#   Cherry      : 23 units
#   Date        :  0 units  ← OUT OF STOCK
#   Elderberry  :  8 units
#
#   Out of stock: 2 products
