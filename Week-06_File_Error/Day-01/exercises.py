# =============================================================================
# Week 06 - Day 01 | Reading Files — Exercises
# =============================================================================
import os

# Helper: create files needed for exercises
def _setup():
    with open("names.txt", "w", encoding="utf-8") as f:
        f.write("Alice\nBob\nCarol\nDave\nEve\n")
    with open("scores.csv", "w", encoding="utf-8") as f:
        f.write("name,score\nAlice,88\nBob,72\nCarol,95\nDave,60\nEve,83\n")
    with open("poem.txt", "w", encoding="utf-8") as f:
        f.write("Roses are red\nViolets are blue\nPython is great\nAnd so are you\n")

_setup()

# -----------------------------------------------------------------------------
# Exercise 1 — Count Lines
# -----------------------------------------------------------------------------
# Read "names.txt" and print:
#   - Total number of lines
#   - The first name (stripped of whitespace)
#   - The last name (stripped of whitespace)
#
# Expected output:
#   Lines: 5
#   First: Alice
#   Last: Eve

# TODO: solve here


print()

# -----------------------------------------------------------------------------
# Exercise 2 — Word Count
# -----------------------------------------------------------------------------
# Read "poem.txt" and print:
#   - Total lines
#   - Total words
#   - Total characters (excluding newlines)
#
# Expected output:
#   Lines: 4
#   Words: 16
#   Characters: 60

# TODO: solve here


print()

# -----------------------------------------------------------------------------
# Exercise 3 — CSV Reader
# -----------------------------------------------------------------------------
# Read "scores.csv" (skip the header line) and:
#   - Print each student and their score: "Alice: 88"
#   - Print the average score rounded to 1 decimal
#
# Expected output:
#   Alice: 88
#   Bob: 72
#   Carol: 95
#   Dave: 60
#   Eve: 83
#   Average: 79.6

# TODO: solve here


print()

# -----------------------------------------------------------------------------
# Exercise 4 — Find High Scorers
# -----------------------------------------------------------------------------
# Read "scores.csv", find all students with score >= 80, and print them.
# Also print how many students passed (score >= 60).
#
# Expected output:
#   High scorers (>=80):
#     Alice: 88
#     Carol: 95
#     Eve: 83
#   Passed (>=60): 5/5

# TODO: solve here


print()

# -----------------------------------------------------------------------------
# Exercise 5 — File Statistics
# -----------------------------------------------------------------------------
# Read "poem.txt" using seek/tell to:
#   - Print the size of the file in bytes (seek to end, tell position)
#   - Print the first 5 characters
#   - Seek back to start and print the last line using readlines()[-1]
#
# Expected output (approximate, may vary by OS newline):
#   File size: 63 bytes
#   First 5 chars: Roses
#   Last line: And so are you

# TODO: solve here


# Cleanup
for f in ["names.txt", "scores.csv", "poem.txt"]:
    if os.path.exists(f):
        os.remove(f)
