# Week 2 - Day 1: if / elif / else — Solutions

# ─────────────────────────────────────────────
# Solution 1: Age Category Classifier
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age.")
elif age <= 12:
    print("Child")
elif age <= 17:
    print("Teenager")
elif age <= 64:
    print("Adult")
else:
    print("Senior")


# ─────────────────────────────────────────────
# Solution 2: Simple Login System
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")
correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username != correct_username:
    print("Unknown user.")
elif password != correct_password:
    print("Wrong password.")
else:
    print("Login successful!")


# ─────────────────────────────────────────────
# Solution 3: Season Finder
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")
month = int(input("Enter month (1-12): "))

if month < 1 or month > 12:
    print("Invalid month.")
elif month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
else:
    print("Autumn")


# ─────────────────────────────────────────────
# Solution 4: Discount Calculator
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")
amount = float(input("Enter purchase amount: "))

if amount >= 500:
    discount = 20
elif amount >= 200:
    discount = 10
elif amount >= 100:
    discount = 5
else:
    discount = 0

final_price = amount * (1 - discount / 100)
print(f"Discount: {discount}% | Final price: {final_price:.2f}")


# ─────────────────────────────────────────────
# Solution 5: Fizz Buzz (single number)
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")
number = int(input("Enter number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
