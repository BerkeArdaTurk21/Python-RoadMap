# Week 2 - Day 1: if / elif / else — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: Age Category Classifier
# ─────────────────────────────────────────────
# Ask the user for their age (integer).
# Print the appropriate category:
#   0–12   → "Child"
#   13–17  → "Teenager"
#   18–64  → "Adult"
#   65+    → "Senior"
# If the input is negative, print "Invalid age."
#
# Expected output examples:
#   Enter age: 10  → Child
#   Enter age: 16  → Teenager
#   Enter age: 30  → Adult
#   Enter age: 70  → Senior
#   Enter age: -5  → Invalid age.


# ─────────────────────────────────────────────
# Exercise 2: Simple Login System
# ─────────────────────────────────────────────
# Store a correct username and password in variables:
#   correct_username = "admin"
#   correct_password = "1234"
# Ask the user to enter a username and password.
# If both match → print "Login successful!"
# If username is wrong → print "Unknown user."
# If username is correct but password is wrong → print "Wrong password."
#
# Expected output examples:
#   admin / 1234  → Login successful!
#   admin / abcd  → Wrong password.
#   guest / 1234  → Unknown user.


# ─────────────────────────────────────────────
# Exercise 3: Season Finder
# ─────────────────────────────────────────────
# Ask the user for a month number (1–12).
# Print the season for that month:
#   12, 1, 2   → Winter
#   3, 4, 5    → Spring
#   6, 7, 8    → Summer
#   9, 10, 11  → Autumn
# If the number is outside 1–12 → print "Invalid month."
#
# Expected output examples:
#   Enter month: 3   → Spring
#   Enter month: 7   → Summer
#   Enter month: 11  → Autumn
#   Enter month: 13  → Invalid month.


# ─────────────────────────────────────────────
# Exercise 4: Discount Calculator
# ─────────────────────────────────────────────
# Ask the user for the total purchase amount (float).
# Apply discounts based on these rules:
#   amount >= 500  → 20% discount
#   amount >= 200  → 10% discount
#   amount >= 100  → 5% discount
#   below 100      → no discount
# Print the discount percentage and the final price.
#
# Expected output examples:
#   Amount: 600  → Discount: 20% | Final price: 480.00
#   Amount: 250  → Discount: 10% | Final price: 225.00
#   Amount: 50   → Discount: 0%  | Final price: 50.00


# ─────────────────────────────────────────────
# Exercise 5: Fizz Buzz (single number)
# ─────────────────────────────────────────────
# Ask the user for a number.
# If divisible by both 3 and 5 → print "FizzBuzz"
# If divisible by only 3       → print "Fizz"
# If divisible by only 5       → print "Buzz"
# Otherwise                    → print the number itself
#
# Expected output examples:
#   Enter number: 15  → FizzBuzz
#   Enter number: 9   → Fizz
#   Enter number: 10  → Buzz
#   Enter number: 7   → 7
