# Week 2 - Day 5: Nested Loops — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: Star Patterns
# ─────────────────────────────────────────────
# Print the following three patterns using nested loops.
# Ask the user for n (the size).
#
# Pattern A — Right triangle (n=4):
#   *
#   **
#   ***
#   ****
#
# Pattern B — Left triangle (n=4):
#      *
#     **
#    ***
#   ****
#
# Pattern C — Pyramid (n=4):
#    *
#   ***
#  *****
# *******


# ─────────────────────────────────────────────
# Exercise 2: Matrix Operations
# ─────────────────────────────────────────────
# Given the 3x3 matrix below, use nested loops to:
#   a) Print it formatted (each number right-aligned in 4 chars)
#   b) Find and print the maximum value and its position [row][col]
#   c) Print the sum of each row
#
# matrix = [
#     [3,  8,  2],
#     [7,  1, 15],
#     [4,  9,  6],
# ]
#
# Expected output:
#    3   8   2
#    7   1  15
#    4   9   6
#
#   Max value: 15 at [1][2]
#
#   Row 0 sum: 13
#   Row 1 sum: 23
#   Row 2 sum: 19


# ─────────────────────────────────────────────
# Exercise 3: Multiplication Table
# ─────────────────────────────────────────────
# Ask the user for n.
# Print a full n×n multiplication table with aligned columns.
#
# Expected output (n=4):
#      1    2    3    4
#      2    4    6    8
#      3    6    9   12
#      4    8   12   16


# ─────────────────────────────────────────────
# Exercise 4: 2D Search
# ─────────────────────────────────────────────
# Given the grid of names below, ask the user to enter
# a name to search for. Use nested loops to find it.
# Print its position as "Row X, Col Y" (1-based).
# If not found, print "Not found."
#
# grid = [
#     ["Alice",  "Bob",    "Charlie"],
#     ["Diana",  "Eve",    "Frank"],
#     ["Grace",  "Heidi",  "Ivan"],
# ]
#
# Expected output:
#   Search: Eve   → Found at Row 2, Col 2
#   Search: Zara  → Not found.


# ─────────────────────────────────────────────
# Exercise 5: Classroom Grade Summary
# ─────────────────────────────────────────────
# Given the student data below, use nested loops to:
#   a) Calculate each student's average
#   b) Find the highest individual score across all students
#   c) Print a formatted report
#
# students = [
#     ("Alice",   [85, 92, 78, 90]),
#     ("Bob",     [70, 65, 80, 75]),
#     ("Charlie", [95, 98, 92, 100]),
#     ("Diana",   [60, 72, 68, 55]),
# ]
#
# Expected output:
#   Alice   | Scores: 85  92  78  90 | Avg: 86.3
#   Bob     | Scores: 70  65  80  75 | Avg: 72.5
#   Charlie | Scores: 95  98  92 100 | Avg: 96.3
#   Diana   | Scores: 60  72  68  55 | Avg: 63.8
#
#   Highest score overall: 100 (Charlie)
