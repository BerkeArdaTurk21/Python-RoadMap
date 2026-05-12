"""
================================================
Week 1 | Day 5 — Exercises
================================================
Instructions: Solve each exercise yourself.
              Do NOT open solutions.py until you have tried your best.
              Each exercise is a small runnable program — write real code.
================================================
"""

# ─────────────────────────────────────────────────
# Exercise 1 — Grade Classifier (Difficulty: Easy)
# ─────────────────────────────────────────────────
# Description: Build a program that reads a score (0–100) and prints the
#   letter grade and pass/fail status using comparison operators and a ternary.
#
#   Grade scale:
#     90 – 100  →  A
#     80 – 89   →  B
#     70 – 79   →  C
#     60 – 69   →  D
#     0  – 59   →  F
#
#   Expected output (example: score = 85):
#     Enter score (0-100): 85
#
#     Score  : 85
#     Grade  : B
#     Status : Pass
#
#   Expected output (example: score = 45):
#     Enter score (0-100): 45
#
#     Score  : 45
#     Grade  : F
#     Status : Fail
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 2 — Leap Year Checker (Difficulty: Easy)
# ─────────────────────────────────────────────────
# Description: Build a program that reads a year and uses logical operators
#   to determine whether it is a leap year.
#
#   Leap year rules (ALL must be applied):
#     - Divisible by 4           → candidate
#     - BUT divisible by 100     → NOT a leap year (exception)
#     - BUT divisible by 400     → IS a leap year  (exception to the exception)
#
#   Hint: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
#   Expected output (example: 2000):
#     Enter a year: 2000
#     2000 is a leap year. ✅
#
#   Expected output (example: 1900):
#     Enter a year: 1900
#     1900 is NOT a leap year. ❌
#
#   Expected output (example: 2024):
#     Enter a year: 2024
#     2024 is a leap year. ✅
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 3 — Number Analyzer (Difficulty: Medium)
# ─────────────────────────────────────────────────
# Description: Build a program that reads an integer and prints a full
#   analysis report using comparison, logical, membership, and bitwise operators.
#
#   Report items:
#     - Sign       : Positive / Negative / Zero
#     - Parity     : Even / Odd   (use bitwise & 1)
#     - In range   : Yes / No     (is it between -100 and 100 inclusive?)
#     - Abs value  : (use ternary — do NOT use abs())
#     - Divisible  : by 3 / by 5 / by both / by neither
#     - Bit length : number of bits needed to represent it
#
#   Expected output (example: number = -42):
#     Enter an integer: -42
#
#     ─── Number Analysis: -42 ───
#     Sign      : Negative
#     Parity    : Even
#     In range  : Yes  (-100 to 100)
#     Abs value : 42
#     Divisible : by neither (3 nor 5)
#     Bit length: 6 bits
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 4 — Membership & Identity Checker (Difficulty: Medium)
# ─────────────────────────────────────────────────
# Description: Build a program that collects a word from the user and runs
#   a series of membership and identity checks, printing a formatted report.
#
#   Checks to perform:
#     - Is the word in the approved list?
#       approved = ["python", "data", "science", "code", "learn"]
#     - Does the word start with a vowel? (use membership: first char in vowels)
#     - Is the word longer than 4 characters?
#     - Is the stripped input identical to the original? (use is not after strip)
#       Hint: check if word != word.strip() — extra whitespace was present
#     - Is the word None? (identity check)
#
#   Expected output (example: word = "python"):
#     Enter a word: python
#
#     ─── Word Analysis: "python" ───
#     In approved list : Yes
#     Starts with vowel: No
#     Longer than 4    : Yes
#     Had whitespace   : No
#     Is None          : No
#
#   Expected output (example: word = "  algo  "):
#     Enter a word:   algo
#
#     ─── Word Analysis: "algo" ───
#     In approved list : No
#     Starts with vowel: Yes
#     Longer than 4    : No
#     Had whitespace   : Yes
#     Is None          : No
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 5 — Bitwise Permission Manager (Difficulty: Hard)
# ─────────────────────────────────────────────────
# Description: Build a permission management program using bitwise operators.
#   Permissions are stored as single bits in an integer.
#
#   Permission flags:
#     READ    = 1  (bit 0 → 0b001)
#     WRITE   = 2  (bit 1 → 0b010)
#     EXECUTE = 4  (bit 2 → 0b100)
#     ADMIN   = 8  (bit 3 → 0b1000)
#
#   The program should:
#     1. Ask the user for a permission number (1–15).
#     2. Print which permissions are active using bitwise &.
#     3. Grant ADMIN if the user already has all three basic permissions.
#     4. Print the final binary representation.
#
#   Expected output (example: perm = 7 → READ + WRITE + EXECUTE):
#     Enter permission value (1-15): 7
#
#     ─── Permission Report ───
#     Input value : 7  (binary: 0b111)
#     READ        : ✅
#     WRITE       : ✅
#     EXECUTE     : ✅
#     ADMIN       : ❌
#
#     All basic permissions found — ADMIN granted!
#     Final value : 15  (binary: 0b1111)
#     Final perms : READ ✅  WRITE ✅  EXECUTE ✅  ADMIN ✅
#
#   Expected output (example: perm = 5 → READ + EXECUTE):
#     Enter permission value (1-15): 5
#
#     ─── Permission Report ───
#     Input value : 5  (binary: 0b101)
#     READ        : ✅
#     WRITE       : ❌
#     EXECUTE     : ✅
#     ADMIN       : ❌
#
#     Missing basic permissions — ADMIN not granted.
#
# Write your solution below:
