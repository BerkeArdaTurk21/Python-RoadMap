"""
================================================
Week 1 | Day 4 — Exercises
================================================
Instructions: Solve each exercise yourself.
              Do NOT open solutions.py until you have tried your best.
              Each exercise is a small runnable program — write real code.
================================================
"""

# ─────────────────────────────────────────────────
# Exercise 1 — Age & Retirement Calculator (Difficulty: Easy)
# ─────────────────────────────────────────────────
# Description: Build a program that asks for the user's name and birth year,
#   then calculates their current age and how many years until retirement (age 65).
#   Use 2025 as the current year.
#
#   Expected output (example input: name=Berke, birth_year=2000):
#     Enter your name      : Berke
#     Enter your birth year: 2000
#
#     Hello, Berke!
#     Current age       : 25
#     Retirement age    : 65
#     Years to retire   : 40
#     Year of retirement: 2065
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 2 — Rectangle Calculator (Difficulty: Easy)
# ─────────────────────────────────────────────────
# Description: Build a program that asks for the width and height of a rectangle
#   as decimal numbers, then prints the area and perimeter.
#
#   Formulas:
#     area      = width * height
#     perimeter = 2 * (width + height)
#
#   Expected output (example: width=5.5, height=3.2):
#     Enter width (m) : 5.5
#     Enter height (m): 3.2
#
#     Rectangle Results
#     Width    : 5.50 m
#     Height   : 3.20 m
#     Area     : 17.60 m²
#     Perimeter: 17.40 m
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 3 — Simple Calculator (Difficulty: Medium)
# ─────────────────────────────────────────────────
# Description: Build a calculator that asks for two numbers and an operator,
#   then computes and displays the result. Handle division by zero gracefully.
#
#   Supported operators: +  -  *  /
#
#   Expected output (example: 10, 3, *):
#     Enter first number : 10
#     Enter operator (+,-,*,/): *
#     Enter second number: 3
#
#     10.0 * 3.0 = 30.0
#
#   Expected output for division by zero (example: 5, /, 0):
#     5.0 / 0.0 = Error: Cannot divide by zero!
#
#   Expected output for unknown operator (example: 5, ^, 2):
#     Unknown operator: ^
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 4 — Input Validator (Difficulty: Medium)
# ─────────────────────────────────────────────────
# Description: Build a program that keeps asking the user to enter a positive
#   integer until they give a valid one. Count the number of attempts.
#   A valid answer is a whole number greater than zero.
#
#   Expected output (example: user types "hello", "-3", "0", then "7"):
#     Enter a positive integer: hello
#     ❌ Invalid! "hello" is not a whole number. Try again.
#
#     Enter a positive integer: -3
#     ❌ Invalid! "-3" is not positive. Try again.
#
#     Enter a positive integer: 0
#     ❌ Invalid! "0" is not positive. Try again.
#
#     Enter a positive integer: 7
#     ✅ Great! You entered 7 after 4 attempt(s).
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 5 — Registration Form (Difficulty: Hard)
# ─────────────────────────────────────────────────
# Description: Build a registration form that collects user data, validates the
#   age field, and prints a formatted membership card.
#
#   Fields to collect:
#     - Full name  (any non-empty string)
#     - Age        (must be a valid integer between 1 and 120)
#     - Email      (any non-empty string — no format validation needed)
#     - City       (any non-empty string)
#
#   Age validation: if the user enters an invalid age, print an error and ask again.
#
#   Expected output (example: Berke Turk, 25, berke@mail.com, Istanbul):
#
#     === MEMBERSHIP REGISTRATION ===
#     Full name : Berke Turk
#     Age       : 25
#     Email     : berke@mail.com
#     City      : Istanbul
#
#     ╔══════════════════════════════════╗
#     ║        MEMBERSHIP CARD           ║
#     ║  Name  : Berke Turk              ║
#     ║  Age   : 25                      ║
#     ║  City  : Istanbul                ║
#     ║  Email : berke@mail.com          ║
#     ║  Status: Active Member           ║
#     ╚══════════════════════════════════╝
#
# Write your solution below:
