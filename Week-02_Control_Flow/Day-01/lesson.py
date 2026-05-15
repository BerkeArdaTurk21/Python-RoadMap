# Week 2 - Day 1: if / elif / else
# Topic: Conditions, Nested if, Truthiness

# ─────────────────────────────────────────────
# 1. BASIC if STATEMENT
# ─────────────────────────────────────────────
# Syntax:
#   if condition:
#       <block runs when condition is True>

age = 20

if age >= 18:
    print("You are an adult.")          # Runs because 20 >= 18 is True

temperature = 5

if temperature < 0:
    print("It is freezing!")            # Does NOT run — condition is False


# ─────────────────────────────────────────────
# 2. if / else
# ─────────────────────────────────────────────
# else runs when the if condition is False.

score = 45

if score >= 50:
    print("Pass")
else:
    print("Fail")                       # Runs — 45 < 50


# ─────────────────────────────────────────────
# 3. if / elif / else
# ─────────────────────────────────────────────
# elif lets you check multiple conditions in order.
# Python stops at the FIRST True branch.

grade = 78

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")                          # Runs — 78 is >= 70
elif grade >= 60:
    print("D")
else:
    print("F")


# ─────────────────────────────────────────────
# 4. COMPARISON OPERATORS (used in conditions)
# ─────────────────────────────────────────────
# ==   equal to
# !=   not equal to
# >    greater than
# <    less than
# >=   greater than or equal to
# <=   less than or equal to

x = 10
print(x == 10)   # True
print(x != 5)    # True
print(x > 15)    # False
print(x <= 10)   # True


# ─────────────────────────────────────────────
# 5. LOGICAL OPERATORS IN CONDITIONS
# ─────────────────────────────────────────────
# and  → both must be True
# or   → at least one must be True
# not  → reverses the boolean value

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed.")             # Runs

is_raining = False
has_umbrella = True

if is_raining or has_umbrella:
    print("You are prepared.")          # Runs — has_umbrella is True

is_logged_in = False
if not is_logged_in:
    print("Please log in.")             # Runs — not False == True


# ─────────────────────────────────────────────
# 6. TRUTHINESS (Truthy vs Falsy values)
# ─────────────────────────────────────────────
# Python treats certain values as False even without == False.
# FALSY values:
#   False, None, 0, 0.0, "", [], {}, set(), ()
# Everything else is TRUTHY.

name = ""
if name:
    print("Name is set.")
else:
    print("Name is empty.")             # Runs — empty string is falsy

items = [1, 2, 3]
if items:
    print("List has items.")            # Runs — non-empty list is truthy

count = 0
if count:
    print("Count is non-zero.")
else:
    print("Count is zero.")             # Runs — 0 is falsy

value = None
if value is None:
    print("No value provided.")         # Runs


# ─────────────────────────────────────────────
# 7. NESTED if STATEMENTS
# ─────────────────────────────────────────────
# You can place if blocks inside other if blocks.
# Use indentation carefully.

is_member = True
balance = 150

if is_member:
    if balance >= 100:
        print("Purchase approved.")     # Runs — both conditions met
    else:
        print("Insufficient balance.")
else:
    print("Members only.")


# ─────────────────────────────────────────────
# 8. ONE-LINE if (Ternary / Inline)
# ─────────────────────────────────────────────
# value_if_true  if  condition  else  value_if_false

age = 17
status = "adult" if age >= 18 else "minor"
print(status)                           # minor

# Equivalent to:
# if age >= 18:
#     status = "adult"
# else:
#     status = "minor"


# ─────────────────────────────────────────────
# 9. in OPERATOR IN CONDITIONS
# ─────────────────────────────────────────────
# Check membership in a string, list, tuple, or dict.

fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is available.")       # Runs

letter = "e"
if letter in "hello":
    print("Letter found.")              # Runs

role = "admin"
allowed_roles = ["admin", "moderator"]
if role in allowed_roles:
    print("Access granted.")            # Runs


# ─────────────────────────────────────────────
# 10. COMBINING EVERYTHING — PRACTICAL EXAMPLE
# ─────────────────────────────────────────────

def classify_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    print(f"BMI: {bmi:.1f}")

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25.0:
        category = "Normal weight"
    elif bmi < 30.0:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Category: {category}")

classify_bmi(70, 1.75)    # BMI: 22.9  →  Normal weight
classify_bmi(50, 1.75)    # BMI: 16.3  →  Underweight
classify_bmi(100, 1.75)   # BMI: 32.7  →  Obese
