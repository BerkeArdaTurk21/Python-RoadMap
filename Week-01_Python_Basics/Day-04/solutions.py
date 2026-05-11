"""
================================================
Week 1 | Day 4 — Solutions
================================================
Only open this after you've genuinely tried exercises.py!
================================================
"""

# ═══════════════════════════════════════════════════
# Exercise 1 — Age & Retirement Calculator Solution
# ═══════════════════════════════════════════════════
# Explanation: input() returns str, so birth_year must be wrapped with int()
# before doing arithmetic. All derived values follow from one conversion.
# f-strings with no format spec are sufficient because all outputs are integers.
name       = input("Enter your name      : ").strip()
birth_year = int(input("Enter your birth year: "))

current_year    = 2025
age             = current_year - birth_year
retirement_age  = 65
years_to_retire = retirement_age - age
retire_year     = current_year + years_to_retire

print()
print(f"Hello, {name}!")
print(f"Current age       : {age}")
print(f"Retirement age    : {retirement_age}")
print(f"Years to retire   : {years_to_retire}")
print(f"Year of retirement: {retire_year}")
# Output (birth_year=2000):
# Hello, Berke!
# Current age       : 25
# Retirement age    : 65
# Years to retire   : 40
# Year of retirement: 2065


# ═══════════════════════════════════════════════════
# Exercise 2 — Rectangle Calculator Solution
# ═══════════════════════════════════════════════════
# Explanation: float() is used instead of int() because the user may enter
# decimal dimensions. The :.2f format spec ensures exactly two decimal places
# in all output lines, giving a clean aligned look.
width  = float(input("Enter width (m) : "))
height = float(input("Enter height (m): "))

area      = width * height
perimeter = 2 * (width + height)

print()
print("Rectangle Results")
print(f"Width    : {width:.2f} m")
print(f"Height   : {height:.2f} m")
print(f"Area     : {area:.2f} m²")
print(f"Perimeter: {perimeter:.2f} m")
# Output (width=5.5, height=3.2):
# Rectangle Results
# Width    : 5.50 m
# Height   : 3.20 m
# Area     : 17.60 m²
# Perimeter: 17.40 m


# ═══════════════════════════════════════════════════
# Exercise 3 — Simple Calculator Solution
# ═══════════════════════════════════════════════════
# Explanation: Both numbers are converted to float so the calculator works for
# decimals as well as integers. The operator is read as a plain string and
# matched with if/elif. Division by zero is caught explicitly before dividing
# rather than relying on an exception, making the intent clear.
num1 = float(input("Enter first number : "))
op   = input("Enter operator (+,-,*,/): ").strip()
num2 = float(input("Enter second number: "))

print()
if op == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif op == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif op == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif op == "/":
    if num2 == 0:
        print(f"{num1} / {num2} = Error: Cannot divide by zero!")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print(f"Unknown operator: {op}")
# Output (10, *, 3):    10.0 * 3.0 = 30.0
# Output (5, /, 0):     5.0 / 0.0 = Error: Cannot divide by zero!
# Output (5, ^, 2):     Unknown operator: ^


# ═══════════════════════════════════════════════════
# Exercise 4 — Input Validator Solution
# ═══════════════════════════════════════════════════
# Explanation: A while True loop runs indefinitely until a valid value triggers
# break. The try/except ValueError catches non-numeric strings cleanly. The
# second check (number > 0) catches valid integers that are zero or negative.
# attempt_count tracks total tries including the final valid one.
attempt_count = 0

while True:
    raw = input("Enter a positive integer: ").strip()
    attempt_count += 1

    try:
        number = int(raw)
    except ValueError:
        print(f'❌ Invalid! "{raw}" is not a whole number. Try again.\n')
        continue

    if number <= 0:
        print(f'❌ Invalid! "{raw}" is not positive. Try again.\n')
        continue

    print(f"✅ Great! You entered {number} after {attempt_count} attempt(s).")
    break
# Output (hello → -3 → 0 → 7):
# ❌ Invalid! "hello" is not a whole number. Try again.
# ❌ Invalid! "-3" is not positive. Try again.
# ❌ Invalid! "0" is not positive. Try again.
# ✅ Great! You entered 7 after 4 attempt(s).


# ═══════════════════════════════════════════════════
# Exercise 5 — Registration Form Solution
# ═══════════════════════════════════════════════════
# Explanation: Name, email, and city are accepted as-is (any non-empty string).
# Age requires a dedicated validation loop: try/except handles non-numeric input,
# and the range check handles out-of-bounds integers. The membership card uses
# f-string left-alignment (:<N) so every value fills a fixed-width column,
# keeping the right border of the box perfectly aligned.
print("=== MEMBERSHIP REGISTRATION ===")
full_name = input("Full name : ").strip()

while True:
    age_raw = input("Age       : ").strip()
    try:
        age = int(age_raw)
        if 1 <= age <= 120:
            break
        print("❌ Age must be between 1 and 120. Try again.")
    except ValueError:
        print(f'❌ "{age_raw}" is not a valid age. Enter a whole number.')

email = input("Email     : ").strip()
city  = input("City      : ").strip()

print()
print("╔══════════════════════════════════╗")
print(f"║        MEMBERSHIP CARD           ║")
print(f"║  Name  : {full_name:<24}║")
print(f"║  Age   : {age:<24}║")
print(f"║  City  : {city:<24}║")
print(f"║  Email : {email:<24}║")
print(f"║  Status: {'Active Member':<24}║")
print("╚══════════════════════════════════╝")
# Output (Berke Turk, 25, berke@mail.com, Istanbul):
# ╔══════════════════════════════════╗
# ║        MEMBERSHIP CARD           ║
# ║  Name  : Berke Turk              ║
# ║  Age   : 25                      ║
# ║  City  : Istanbul                ║
# ║  Email : berke@mail.com          ║
# ║  Status: Active Member           ║
# ╚══════════════════════════════════╝
