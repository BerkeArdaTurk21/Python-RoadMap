"""
================================================
Week 1 | Day 4 — User Input & Type Conversion
================================================
Level       : Beginner
Topics      : input(), int(), float(), str(), bool(),
              type conversion, truthiness, validation
              patterns, multiple inputs
Goal        : Read data from the user, convert it to the
              right type, and validate it before use
================================================
"""

# NOTE: This file demonstrates input() using hardcoded strings so it runs
# without pausing. Each section shows the real input() pattern in a comment,
# then simulates what the user would have typed. Real interactive programs
# are in exercises.py and solutions.py.


# ── SECTION 1: The input() Function ──────────────────
# input("prompt") displays a prompt, waits for the user to press Enter,
# and returns everything they typed as a STRING — always str, no exceptions.
#
# Real usage:
#   name = input("Enter your name: ")
#   # User types: Berke
#   print(f"Hello, {name}!")   →   Hello, Berke!

name = "Berke"                  # simulates: input("Enter your name: ")
print(f"Hello, {name}!")        # Output: Hello, Berke!
print(type(name))               # Output: <class 'str'>

raw_number = "25"               # simulates: input("Type any number: ")
print(type(raw_number))         # Output: <class 'str'>  — still a string!

# The key insight: even when the user types digits, input() returns a str.
# You must convert it yourself before doing arithmetic.


# ── SECTION 2: Converting Input to int ───────────────
# Wrap input() with int() to get an integer ready for math.
# Pattern: variable = int(input("prompt"))

age_str = "25"                  # simulates: input("Enter your age: ")
age = int(age_str)
print(f"You are {age} years old.")
print(f"In 10 years: {age + 10}")       # Output: In 10 years: 35
print(f"Type: {type(age)}")             # Output: Type: <class 'int'>

# Without conversion, + would concatenate strings instead of adding:
print("25" + "10")              # Output: 2510  (string concat — wrong!)
print(int("25") + 10)          # Output: 35    (integer math — correct)

# int() only works on strings that look like whole numbers.
# int("3.14")   →  ValueError: invalid literal
# int("hello")  →  ValueError: invalid literal
# int("  42  ") →  42  (int() strips whitespace automatically)
print(int("  42  "))            # Output: 42


# ── SECTION 3: Converting Input to float ─────────────
# Use float() when the user might enter a decimal number.
# Pattern: variable = float(input("prompt"))

price_str = "19.99"             # simulates: input("Enter price: ")
qty_str   = "3"                 # simulates: input("Enter quantity: ")

price    = float(price_str)
quantity = int(qty_str)
total    = price * quantity

print(f"Price   : {price}")     # Output: Price   : 19.99
print(f"Qty     : {quantity}")  # Output: Qty     : 3
print(f"Total   : {total:.2f}") # Output: Total   : 59.97

# float() is more forgiving than int():
print(float("3"))               # Output: 3.0   — accepts integer strings
print(float("3.14"))            # Output: 3.14  — accepts decimal strings
# int("3.14")  →  ValueError   — int() does NOT accept decimal strings


# ── SECTION 4: str() — Explicit String Conversion ────
# str() converts any Python value to its string representation.
# Useful when building messages by concatenating non-string values with +.

score  = 95
grade  = "A"
active = True

# This raises TypeError — cannot use + between str and int:
# message = "Score: " + score   ✗

# str() fixes it:
message = "Score: " + str(score) + " | Grade: " + grade
print(message)                  # Output: Score: 95 | Grade: A

# str() works on any type:
print(str(3.14))                # Output: 3.14
print(str(True))                # Output: True
print(str(None))                # Output: None
print(str([1, 2, 3]))           # Output: [1, 2, 3]

# f-strings call str() automatically — they are usually cleaner:
print(f"Score: {score} | Grade: {grade}")


# ── SECTION 5: bool() and Truthiness ─────────────────
# bool() converts a value to True or False.
# Python defines certain values as "falsy" — they behave like False in
# conditions. Everything else is "truthy".
#
# FALSY values:
#   0, 0.0, 0j          (zero of any numeric type)
#   ""                  (empty string)
#   [], {}, set(), ()   (empty collections)
#   None
#   False
#
# TRUTHY: every other value.

print(bool(0))                  # Output: False
print(bool(0.0))                # Output: False
print(bool(""))                 # Output: False
print(bool(None))               # Output: False
print(bool([]))                 # Output: False

print(bool(1))                  # Output: True
print(bool(-99))                # Output: True   (non-zero is truthy)
print(bool("hello"))            # Output: True
print(bool("False"))            # Output: True   (non-empty string!)
print(bool("0"))                # Output: True   (non-empty string!)
print(bool([1, 2]))             # Output: True

# Critical trap: bool("False") is True because "False" is a non-empty string.
# To test yes/no from user input, compare the string directly:
response = "yes"                # simulates: input("Continue? ")
if response.lower() in ("yes", "y"):
    print("Continuing...")      # Output: Continuing...


# ── SECTION 6: Validation Patterns ───────────────────
# User input is untrusted — always validate before converting.

# Pattern 1 — .isdigit()
# Returns True only if every character is a digit (no minus, no dot).
print("42".isdigit())           # Output: True
print("3.14".isdigit())         # Output: False  (dot is not a digit)
print("-5".isdigit())           # Output: False  (minus is not a digit)
print("".isdigit())             # Output: False  (empty string)

user_str = "42"                 # simulates: input("Enter a positive integer: ")
if user_str.isdigit():
    number = int(user_str)
    print(f"Valid: {number}")   # Output: Valid: 42
else:
    print("Invalid input!")

# Pattern 2 — .strip() removes accidental whitespace before converting.
messy = "  99  "                # simulates: input() where user hit space
clean = int(messy.strip())
print(clean)                    # Output: 99

# Pattern 3 — try/except catches conversion errors gracefully.
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None             # signal that conversion failed

print(safe_int("42"))           # Output: 42
print(safe_int("hello"))        # Output: None


# ── SECTION 7: Multiple Inputs ────────────────────────
# Collect several values from the user in one line using split().

# split() without args splits on any whitespace and returns a list.
line = "10 20"                  # simulates: input("Enter two numbers: ")
parts = line.split()
x = int(parts[0])
y = int(parts[1])
print(f"{x} + {y} = {x + y}")  # Output: 10 + 20 = 30

# Pythonic one-liner — unpack directly:
raw = "15 25"                   # simulates: input("Enter two numbers: ")
a, b = raw.split()
a, b = int(a), int(b)
print(f"{a} * {b} = {a * b}")  # Output: 15 * 25 = 375

# Split on a specific delimiter (useful for CSV-style input):
raw = "Berke, 25"               # simulates: input("Name, Age: ")
name_part, age_part = raw.split(",")
name_part = name_part.strip()
age_part  = int(age_part.strip())
print(f"Name: {name_part} | Age: {age_part}")   # Output: Name: Berke | Age: 25

# map() applies a function to every element of split() — clean and compact:
raw = "3 7 11"                  # simulates: input("Enter three numbers: ")
nums = list(map(int, raw.split()))
print(nums)                     # Output: [3, 7, 11]
print(sum(nums))                # Output: 21


# ── SECTION 8: Complete Program Pattern ──────────────
# How a real input-driven program is structured:
# 1. Collect all input at the top
# 2. Convert and validate
# 3. Compute
# 4. Display results

# Simulated version (hardcoded to run without pausing):
full_name  = "Berke Arda Turk"  # input("Full name   : ")
birth_year = "2000"             # input("Birth year  : ")
height_cm  = "182"              # input("Height (cm) : ")
city       = "Istanbul"         # input("City        : ")

# Convert
birth_year_int = int(birth_year)
height_m       = int(height_cm) / 100

# Compute
current_year = 2025
age          = current_year - birth_year_int
retirement   = 65 - age

# Display
print()
print("=" * 38)
print("  PROFILE CARD")
print("=" * 38)
print(f"  Name       : {full_name}")
print(f"  Age        : {age}")
print(f"  Height     : {height_m:.2f} m")
print(f"  City       : {city}")
print(f"  Born       : {birth_year_int}")
print(f"  Retirement : in {retirement} years")
print("=" * 38)
# Output:
# ======================================
#   PROFILE CARD
# ======================================
#   Name       : Berke Arda Turk
#   Age        : 25
#   Height     : 1.82 m
#   City       : Istanbul
#   Born       : 2000
#   Retirement : in 40 years
# ======================================


# ── QUICK REFERENCE ──────────────────────────────────
# input() always returns str — convert before doing math.
#
# Conversion functions:
#   int(x)    → whole number  (truncates if float; ValueError on bad str)
#   float(x)  → decimal       (accepts int strings; ValueError on bad str)
#   str(x)    → string        (works on any type, never raises)
#   bool(x)   → True / False  (see falsy list below)
#
# Falsy values: 0  0.0  ""  []  {}  ()  set()  None  False
# Truthy: everything else (including "0" and "False" — non-empty strings)
#
# Validation patterns:
#   s.isdigit()       → True only for non-negative integer strings
#   s.strip()         → remove whitespace before converting
#   try/except        → safe conversion that handles invalid input
#
# Multiple inputs:
#   a, b = input("...").split()        → split on whitespace
#   a, b = input("...").split(",")     → split on comma
#   nums = list(map(int, s.split()))   → split + convert all at once
