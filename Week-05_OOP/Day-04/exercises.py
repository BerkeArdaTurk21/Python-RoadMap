# =============================================================================
# Week 05 - Day 04 | Encapsulation — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Validated Age
# -----------------------------------------------------------------------------
# Create a Person class with a validated age property:
#   - __init__(self, name, age)      ← age goes through the setter
#   - @property age                  ← returns _age
#   - @age.setter                    ← age must be 0–150; raise ValueError otherwise
#   - @property is_adult             ← read-only; True if age >= 18
#   - __str__                        ← "Alice (age 25)"
#
# Expected output:
#   Alice (age 25)
#   True
#   Alice (age 15)
#   False
#   ValueError raised: Age must be between 0 and 150

class Person:
    pass  # TODO


p1 = Person("Alice", 25)
print(p1)               # Alice (age 25)
print(p1.is_adult)      # True

p2 = Person("Alice", 15)
print(p2)               # Alice (age 15)
print(p2.is_adult)      # False

try:
    p3 = Person("Alice", 200)
except ValueError as e:
    print(f"ValueError raised: {e}")   # Age must be between 0 and 150
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Circle with Validated Radius
# -----------------------------------------------------------------------------
# Create a Circle class:
#   - __init__(self, radius)
#   - @property radius               ← getter
#   - @radius.setter                 ← must be > 0; raise ValueError otherwise
#   - @property diameter             ← read-only: 2 * radius
#   - @property area                 ← read-only: π * r²  (use 3.14159)
#   - @property circumference        ← read-only: 2 * π * r
#   - __str__                        ← "Circle(r=5, area=78.54)"
#
# Expected output:
#   Circle(r=5, area=78.54)
#   10
#   78.54
#   31.42
#   Circle(r=3, area=28.27)
#   ValueError raised: Radius must be positive

class Circle:
    PI = 3.14159
    pass  # TODO


c = Circle(5)
print(c)                  # Circle(r=5, area=78.54)
print(c.diameter)         # 10
print(c.area)             # 78.54
print(c.circumference)    # 31.42

c.radius = 3
print(c)                  # Circle(r=3, area=28.27)

try:
    c.radius = -1
except ValueError as e:
    print(f"ValueError raised: {e}")
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Password Manager Entry
# -----------------------------------------------------------------------------
# Create a Credential class that stores a username and password securely:
#   - __init__(self, username, password)
#   - @property username             ← getter
#   - @property password             ← returns "****" (never exposes real password)
#   - @password.setter               ← must be at least 8 chars; raise ValueError
#   - check_password(self, attempt)  ← returns True if attempt == real password
#   - __str__                        ← "Credential[alice] password=****"
#
# Expected output:
#   Credential[alice] password=****
#   ****
#   True
#   False
#   ValueError raised: Password must be at least 8 characters

class Credential:
    pass  # TODO


cred = Credential("alice", "securepass")
print(cred)                            # Credential[alice] password=****
print(cred.password)                   # ****
print(cred.check_password("securepass"))  # True
print(cred.check_password("wrong"))    # False

try:
    cred.password = "short"
except ValueError as e:
    print(f"ValueError raised: {e}")
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Temperature with Multiple Scales
# -----------------------------------------------------------------------------
# Create a Temperature class using @property for unit conversions:
#   - __init__(self, celsius)
#   - @property celsius              ← getter/setter (>= -273.15 or ValueError)
#   - @property fahrenheit           ← read-only: (c * 9/5) + 32
#   - @property kelvin               ← read-only: c + 273.15
#   - @classmethod from_fahrenheit(cls, f)  ← factory
#   - @classmethod from_kelvin(cls, k)      ← factory
#   - __str__                        ← "100.0°C / 212.0°F / 373.15K"
#
# Expected output:
#   100.0°C / 212.0°F / 373.15K
#   0.0°C / 32.0°F / 273.15K
#   -40.0°C / -40.0°F / 233.15K
#   ValueError raised: Temperature below absolute zero

class Temperature:
    pass  # TODO


t1 = Temperature(100)
print(t1)                              # 100.0°C / 212.0°F / 373.15K

t2 = Temperature.from_fahrenheit(32)
print(t2)                              # 0.0°C / 32.0°F / 273.15K

t3 = Temperature.from_kelvin(233.15)
print(t3)                              # -40.0°C / -40.0°F / 233.15K

try:
    t4 = Temperature(-300)
except ValueError as e:
    print(f"ValueError raised: {e}")
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Bank Account with Full Encapsulation
# -----------------------------------------------------------------------------
# Create a BankAccount class:
#   - __init__(self, owner, balance=0)
#   - __owner stored as __owner (private name mangling)
#   - @property owner                ← read-only getter (no setter)
#   - @property balance              ← getter
#   - @balance.setter                ← balance >= 0; raise ValueError
#   - deposit(self, amount)          ← amount > 0; raise ValueError
#   - withdraw(self, amount)         ← amount > 0 and <= balance; else raise ValueError
#   - __str__                        ← "Account[Alice]: $500.00"
#
# Expected output:
#   Account[Alice]: $0.00
#   Account[Alice]: $500.00
#   Account[Alice]: $350.00
#   ValueError raised: Withdrawal amount exceeds balance
#   ValueError raised: Deposit amount must be positive

class BankAccount:
    pass  # TODO


acc = BankAccount("Alice")
print(acc)                            # Account[Alice]: $0.00
acc.deposit(500)
print(acc)                            # Account[Alice]: $500.00
acc.withdraw(150)
print(acc)                            # Account[Alice]: $350.00

try:
    acc.withdraw(1000)
except ValueError as e:
    print(f"ValueError raised: {e}")   # Withdrawal amount exceeds balance

try:
    acc.deposit(-50)
except ValueError as e:
    print(f"ValueError raised: {e}")   # Deposit amount must be positive
