# Week 2 - Day 3: while Loops — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: Sum Until Limit
# ─────────────────────────────────────────────
# Ask the user to enter positive numbers one by one.
# Keep a running total. Stop and print the total
# as soon as it reaches or exceeds 100.
# Also print how many numbers were entered.
#
# Expected output example:
#   Enter number: 30
#   Enter number: 45
#   Enter number: 35
#   Total reached: 110 after 3 numbers.


# ─────────────────────────────────────────────
# Exercise 2: Input Validator
# ─────────────────────────────────────────────
# Ask the user for a number between 1 and 10 (inclusive).
# Keep asking until they enter a valid number.
# Once valid, print "Accepted: X".
#
# Expected output example:
#   Enter a number (1-10): 0
#   Out of range. Try again.
#   Enter a number (1-10): 15
#   Out of range. Try again.
#   Enter a number (1-10): abc
#   Not a number. Try again.
#   Enter a number (1-10): 7
#   Accepted: 7


# ─────────────────────────────────────────────
# Exercise 3: Collatz Sequence
# ─────────────────────────────────────────────
# The Collatz conjecture:
#   - If n is even  → n = n // 2
#   - If n is odd   → n = n * 3 + 1
#   - Repeat until n == 1
#
# Ask the user for a positive integer.
# Print each number in the sequence and count the steps.
#
# Expected output (input = 6):
#   6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1
#   Steps: 8


# ─────────────────────────────────────────────
# Exercise 4: ATM Simulator
# ─────────────────────────────────────────────
# Simulate a simple ATM with a starting balance of 500.
# Show a menu on each loop:
#   1. Check balance
#   2. Deposit
#   3. Withdraw
#   4. Exit
#
# Rules:
#   - Deposit must be > 0
#   - Withdrawal must be > 0 and <= current balance
#   - Print an error for invalid amounts
#   - Exit when the user chooses 4
#
# Expected output example:
#   1. Check balance → Balance: $500
#   2. Deposit 200   → Deposited $200. Balance: $700
#   3. Withdraw 900  → Insufficient funds.
#   4. Exit          → Goodbye!


# ─────────────────────────────────────────────
# Exercise 5: Password Strength Checker
# ─────────────────────────────────────────────
# Keep asking the user to enter a password until it meets
# ALL of these requirements:
#   - At least 8 characters long
#   - Contains at least one digit
#   - Contains at least one uppercase letter
#
# Print which requirement(s) failed on each attempt.
# When valid, print "Strong password accepted."
#
# Expected output example:
#   Enter password: hello
#   ✗ Too short (min 8 chars)
#   ✗ No digit found
#   ✗ No uppercase letter
#   Enter password: Hello123
#   Strong password accepted.
