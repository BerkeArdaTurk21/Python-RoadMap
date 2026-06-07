# =============================================================================
# Week 05 - Day 03 | Inheritance — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Animal Hierarchy
# -----------------------------------------------------------------------------
# Build this hierarchy:
#
#   Animal
#     ├── Dog
#     └── Cat
#
# Animal:
#   - __init__(self, name, age)
#   - eat(self)    → "{name} is eating."
#   - __str__      → "{name} (age {age})"
#
# Dog(Animal):
#   - __init__(self, name, age, breed)   ← use super().__init__
#   - speak(self)  → "{name} says: Woof!"
#   - fetch(self, item) → "{name} fetches the {item}!"
#   - __str__      → "{name} the {breed} (age {age})"
#
# Cat(Animal):
#   - __init__(self, name, age, indoor)  ← use super().__init__
#   - speak(self)  → "{name} says: Meow!"
#   - __str__      → "{name} (indoor cat, age {age})" if indoor
#                    "{name} (outdoor cat, age {age})" otherwise
#
# Expected output:
#   Rex the Labrador (age 3)
#   Rex is eating.
#   Rex says: Woof!
#   Rex fetches the ball!
#   Whiskers (indoor cat, age 4)
#   Whiskers says: Meow!
#   True
#   True

class Animal:
    pass  # TODO

class Dog(Animal):
    pass  # TODO

class Cat(Animal):
    pass  # TODO


rex      = Dog("Rex", 3, "Labrador")
whiskers = Cat("Whiskers", 4, indoor=True)

print(rex)
print(rex.eat())
print(rex.speak())
print(rex.fetch("ball"))
print(whiskers)
print(whiskers.speak())
print(isinstance(rex, Animal))       # True
print(isinstance(whiskers, Animal))  # True
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Shape Area Calculator
# -----------------------------------------------------------------------------
# Build this hierarchy:
#
#   Shape
#     ├── Rectangle
#     └── Triangle
#
# Shape:
#   - __init__(self, color="red")
#   - area(self) → returns 0   (to be overridden)
#   - describe(self) → "A {color} shape with area {area:.2f}"
#                       ← calls self.area() so subclasses get correct value
#
# Rectangle(Shape):
#   - __init__(self, width, height, color="red")  ← use super().__init__
#   - area(self) → width * height
#   - __str__    → "Rectangle({width}x{height})"
#
# Triangle(Shape):
#   - __init__(self, base, height, color="blue")  ← use super().__init__
#   - area(self) → 0.5 * base * height
#   - __str__    → "Triangle(base={base}, height={height})"
#
# Expected output:
#   Rectangle(4x6)
#   24
#   A red shape with area 24.00
#   Triangle(base=3, height=8)
#   12.0
#   A blue shape with area 12.00

class Shape:
    pass  # TODO

class Rectangle(Shape):
    pass  # TODO

class Triangle(Shape):
    pass  # TODO


r = Rectangle(4, 6)
t = Triangle(3, 8)

print(r)
print(r.area())
print(r.describe())
print(t)
print(t.area())
print(t.describe())
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Employee Hierarchy
# -----------------------------------------------------------------------------
# Build this hierarchy:
#
#   Employee
#     ├── Manager
#     └── Developer
#
# Employee:
#   - __init__(self, name, salary)
#   - work(self) → "{name} is working."
#   - get_info(self) → "Employee: {name}, Salary: ${salary:,.2f}"
#
# Manager(Employee):
#   - __init__(self, name, salary, team_size)  ← super().__init__
#   - work(self) → "{name} is managing a team of {team_size}."
#                  (override — use a different message, NOT super())
#   - give_raise(self, employee, amount)
#     → increases employee.salary by amount, returns "{emp.name} got a raise!"
#   - get_info(self) → extend parent: add "| Team size: {team_size}"
#                      (use super().get_info() + the extra part)
#
# Developer(Employee):
#   - __init__(self, name, salary, language)  ← super().__init__
#   - work(self) → "{name} is coding in {language}."  (override)
#   - get_info(self) → extend parent: add "| Language: {language}"
#
# Expected output:
#   Employee: Alice, Salary: $90,000.00 | Team size: 5
#   Alice is managing a team of 5.
#   Employee: Bob, Salary: $80,000.00 | Language: Python
#   Bob is coding in Python.
#   Bob got a raise!
#   Employee: Bob, Salary: $85,000.00 | Language: Python

class Employee:
    pass  # TODO

class Manager(Employee):
    pass  # TODO

class Developer(Employee):
    pass  # TODO


mgr = Manager("Alice", 90000, team_size=5)
dev = Developer("Bob", 80000, language="Python")

print(mgr.get_info())
print(mgr.work())
print(dev.get_info())
print(dev.work())
print(mgr.give_raise(dev, 5000))
print(dev.get_info())
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Vehicle Hierarchy
# -----------------------------------------------------------------------------
# Build this multi-level hierarchy:
#
#   Vehicle
#     └── Car
#           └── ElectricCar
#
# Vehicle:
#   - __init__(self, make, model, year)
#   - start(self) → "Starting {year} {make} {model}."
#   - __str__     → "{year} {make} {model}"
#
# Car(Vehicle):
#   - __init__(self, make, model, year, num_doors)  ← super().__init__
#   - start(self) → extend parent: add " (Car, {num_doors} doors)"
#   - __str__     → "{year} {make} {model} ({num_doors}-door)"
#
# ElectricCar(Car):
#   - __init__(self, make, model, year, num_doors, battery_kwh)  ← super()
#   - start(self) → "{year} {make} {model} silently powered on."
#                   (full override — don't use super() here)
#   - charge(self) → "Charging {battery_kwh} kWh battery..."
#   - __str__     → "{year} {make} {model} [EV, {battery_kwh} kWh]"
#
# Expected output:
#   2020 Toyota Camry (4-door)
#   Starting 2020 Toyota Camry. (Car, 4 doors)
#   2023 Tesla Model 3 [EV, 75 kWh]
#   2023 Tesla Model 3 silently powered on.
#   Charging 75 kWh battery...
#   True
#   True

class Vehicle:
    pass  # TODO

class Car(Vehicle):
    pass  # TODO

class ElectricCar(Car):
    pass  # TODO


car = Car("Toyota", "Camry", 2020, 4)
ev  = ElectricCar("Tesla", "Model 3", 2023, 4, 75)

print(car)
print(car.start())
print(ev)
print(ev.start())
print(ev.charge())
print(isinstance(ev, Car))      # True
print(isinstance(ev, Vehicle))  # True
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Account Hierarchy
# -----------------------------------------------------------------------------
# Build this hierarchy:
#
#   BankAccount
#     ├── SavingsAccount
#     └── PremiumAccount
#
# BankAccount:
#   - __init__(self, owner, balance=0)
#   - deposit(self, amount)   → adds to balance
#   - withdraw(self, amount)  → subtracts if enough; else print "Insufficient funds"
#   - __str__   → "Account[{owner}]: ${balance:.2f}"
#
# SavingsAccount(BankAccount):
#   - __init__(self, owner, balance=0, rate=0.04)  ← super().__init__
#   - apply_interest(self) → balance += balance * rate
#   - withdraw(self, amount) → override: only allow if balance - amount >= 100
#                              (must keep $100 minimum); else print "Minimum balance required"
#   - __str__ → extend parent: add " [Savings {rate*100:.1f}%]"
#
# PremiumAccount(BankAccount):
#   - __init__(self, owner, balance=0, cashback_rate=0.02)  ← super().__init__
#   - deposit(self, amount) → override: add amount + cashback (amount * cashback_rate)
#   - __str__ → extend parent: add " [Premium {cashback_rate*100:.1f}% cashback]"
#
# Expected output:
#   Account[Alice]: $1000.00 [Savings 4.0%]
#   Account[Alice]: $1040.00 [Savings 4.0%]
#   Minimum balance required
#   Account[Alice]: $940.00 [Savings 4.0%]
#   Account[Bob]: $0.00 [Premium 2.0% cashback]
#   Account[Bob]: $510.00 [Premium 2.0% cashback]

class BankAccount:
    pass  # TODO

class SavingsAccount(BankAccount):
    pass  # TODO

class PremiumAccount(BankAccount):
    pass  # TODO


sav  = SavingsAccount("Alice", 1000)
prem = PremiumAccount("Bob")

print(sav)
sav.apply_interest()
print(sav)
sav.withdraw(1000)          # Minimum balance required (1040 - 1000 = 40 < 100)
sav.withdraw(100)           # Allowed: 1040 - 100 = 940 >= 100
print(sav)

print(prem)
prem.deposit(500)           # 500 + 10 cashback = 510
print(prem)
