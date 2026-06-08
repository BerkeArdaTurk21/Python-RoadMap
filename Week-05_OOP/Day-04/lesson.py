# =============================================================================
# Week 05 - Day 04 | Encapsulation
# =============================================================================
# Topics: public/protected/private, name mangling, getters/setters,
#         @property, @x.setter, @x.deleter, read-only properties
# =============================================================================

# -----------------------------------------------------------------------------
# 1. WHAT IS ENCAPSULATION?
# -----------------------------------------------------------------------------
# Encapsulation = bundling data (attributes) with the methods that operate on
# that data, AND controlling access to that data from outside the class.
#
# Goal: hide internal implementation details and expose only what is needed.
# This prevents accidental misuse and lets you change internals safely.

# -----------------------------------------------------------------------------
# 2. PUBLIC, PROTECTED, AND PRIVATE — PYTHON CONVENTIONS
# -----------------------------------------------------------------------------
# Python does NOT enforce access restrictions like Java/C++.
# It uses NAMING CONVENTIONS to signal intent:
#
#   name       — public:    anyone can read/write
#   _name      — protected: "internal use" (convention, not enforced)
#   __name     — private:   name-mangled, hard to access from outside

class BankAccount:
    interest_rate = 0.03          # public class variable

    def __init__(self, owner, balance):
        self.owner    = owner      # public
        self._balance = balance    # protected — internal, avoid direct access
        self.__pin    = 1234       # private  — name-mangled

    def show_balance(self):
        return f"Balance: ${self._balance:.2f}"   # methods CAN access _balance

acc = BankAccount("Alice", 500)

print(acc.owner)         # Alice     ← public, fine
print(acc._balance)      # 500       ← works, but "please don't"
# print(acc.__pin)       # AttributeError! name-mangled
print(acc._BankAccount__pin)  # 1234 ← mangled name — works but bad practice

# -----------------------------------------------------------------------------
# 3. NAME MANGLING
# -----------------------------------------------------------------------------
# __name becomes _ClassName__name internally. This prevents accidental
# overriding in subclasses — it's NOT true security, just collision avoidance.

class Base:
    def __init__(self):
        self.__secret = "base secret"

    def reveal(self):
        return self.__secret   # works — accesses _Base__secret

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__secret = "child secret"   # creates _Child__secret, NOT overwriting Base

b = Child()
print(b.reveal())             # base secret  ← Base's __secret is safe
print(b._Child__secret)       # child secret ← Child's own mangled attr

# -----------------------------------------------------------------------------
# 4. GETTERS AND SETTERS — MANUAL APPROACH
# -----------------------------------------------------------------------------
# Expose controlled read/write access via explicit methods.
# Problem: verbose — obj.get_x() and obj.set_x(v) feels clunky in Python.

class Celsius:
    def __init__(self, temperature):
        self._temperature = temperature

    def get_temperature(self):             # getter
        return self._temperature

    def set_temperature(self, value):      # setter with validation
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._temperature = value

t = Celsius(25)
print(t.get_temperature())   # 25
t.set_temperature(100)
print(t.get_temperature())   # 100
# t.set_temperature(-300)    # ValueError

# -----------------------------------------------------------------------------
# 5. @property — THE PYTHONIC WAY
# -----------------------------------------------------------------------------
# @property lets you define a GETTER that is accessed like an attribute.
# No parentheses needed: obj.temperature instead of obj.get_temperature()

class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter — called when you read obj.celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter — called when you write obj.celsius = value"""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Read-only computed property — no setter defined."""
        return self._celsius * 9 / 5 + 32


t = Temperature(25)

print(t.celsius)        # 25       ← calls getter, looks like attribute access
t.celsius = 100         # calls setter
print(t.celsius)        # 100
print(t.fahrenheit)     # 212.0   ← computed on the fly

# t.fahrenheit = 32     # AttributeError: can't set attribute (no setter)
# t.celsius = -300      # ValueError

# -----------------------------------------------------------------------------
# 6. @property.deleter
# -----------------------------------------------------------------------------

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @radius.deleter
    def radius(self):
        print("Radius deleted — resetting to 1")
        self._radius = 1

c = Circle(5)
print(c.radius)    # 5
c.radius = 10
print(c.radius)    # 10
del c.radius       # calls deleter
print(c.radius)    # 1

# -----------------------------------------------------------------------------
# 7. READ-ONLY PROPERTIES
# -----------------------------------------------------------------------------
# Define @property but no @x.setter — makes the attribute read-only.

class Person:
    def __init__(self, first, last):
        self._first = first
        self._last  = last

    @property
    def full_name(self):
        return f"{self._first} {self._last}"

    @property
    def initials(self):
        return f"{self._first[0]}.{self._last[0]}."


p = Person("Alice", "Smith")
print(p.full_name)    # Alice Smith
print(p.initials)     # A.S.
# p.full_name = "Bob" # AttributeError — no setter

# -----------------------------------------------------------------------------
# 8. PRACTICAL EXAMPLE — VALIDATED MODEL
# -----------------------------------------------------------------------------

class Product:
    def __init__(self, name, price, stock):
        self.name    = name
        self.price   = price    # goes through setter
        self.stock   = stock

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = round(float(value), 2)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Stock must be a non-negative integer")
        self._stock = value

    @property
    def is_available(self):
        return self._stock > 0

    def __str__(self):
        status = "In stock" if self.is_available else "Out of stock"
        return f"{self.name} — ${self._price:.2f} ({status}, {self._stock} units)"


p = Product("Laptop", 999.99, 10)
print(p)               # Laptop — $999.99 (In stock, 10 units)
p.price = 899
p.stock = 0
print(p)               # Laptop — $899.00 (Out of stock, 0 units)
print(p.is_available)  # False
# p.price = -50        # ValueError

# =============================================================================
# SUMMARY
# =============================================================================
# ┌─────────────────────┬────────────────────────────────────────────────────┐
# │  Concept            │  Key Point                                         │
# ├─────────────────────┼────────────────────────────────────────────────────┤
# │  Public (name)      │  Accessible everywhere — no restriction            │
# │  Protected (_name)  │  Convention: "internal use please"                 │
# │  Private (__name)   │  Name-mangled: _Class__name — avoids subclass clash│
# │  @property          │  Getter accessed like attribute (no parentheses)   │
# │  @x.setter          │  Setter with validation logic                      │
# │  @x.deleter         │  Called on del obj.x                               │
# │  Read-only property │  @property with no @x.setter                       │
# └─────────────────────┴────────────────────────────────────────────────────┘
print("\nDay 04 — Encapsulation complete!")
