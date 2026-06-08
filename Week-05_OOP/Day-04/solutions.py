# =============================================================================
# Week 05 - Day 04 | Encapsulation — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — Validated Age
# -----------------------------------------------------------------------------
# KEY INSIGHT: self.age = age in __init__ goes THROUGH the setter — the setter
# runs immediately on construction. There is no need to call the setter
# explicitly; just assign the attribute and the property machinery takes over.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age   # calls the setter

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not 0 <= value <= 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value

    @property
    def is_adult(self):
        return self._age >= 18

    def __str__(self):
        return f"{self.name} (age {self._age})"


p1 = Person("Alice", 25)
print(p1)
print(p1.is_adult)

p2 = Person("Alice", 15)
print(p2)
print(p2.is_adult)

try:
    p3 = Person("Alice", 200)
except ValueError as e:
    print(f"ValueError raised: {e}")
print()

# WHY does self.age = age in __init__ trigger the setter?
# In Python, self.age = age looks up 'age' in the class, finds the property
# descriptor, and calls the setter. The _age attribute is set by the setter.

# -----------------------------------------------------------------------------
# Solution 2 — Circle with Validated Radius
# -----------------------------------------------------------------------------
# KEY INSIGHT: All computed properties (diameter, area, circumference) are
# read-only because they only have a getter. They recalculate each time they
# are accessed, so they're always in sync with the current radius.

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius   # goes through setter

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def area(self):
        return round(Circle.PI * self._radius ** 2, 2)

    @property
    def circumference(self):
        return round(2 * Circle.PI * self._radius, 2)

    def __str__(self):
        return f"Circle(r={self._radius}, area={self.area})"


c = Circle(5)
print(c)
print(c.diameter)
print(c.area)
print(c.circumference)
c.radius = 3
print(c)

try:
    c.radius = -1
except ValueError as e:
    print(f"ValueError raised: {e}")
print()

# -----------------------------------------------------------------------------
# Solution 3 — Password Manager Entry
# -----------------------------------------------------------------------------
# KEY INSIGHT: The password getter returns "****" — it NEVER exposes the real
# password. The actual password is stored in self.__password (name-mangled).
# check_password() is the ONLY way to verify the password from outside.

class Credential:
    def __init__(self, username, password):
        self._username = username
        self.password  = password   # goes through setter

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return "****"   # never expose the real password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")
        self.__password = value   # store real password privately

    def check_password(self, attempt):
        return attempt == self.__password

    def __str__(self):
        return f"Credential[{self._username}] password=****"


cred = Credential("alice", "securepass")
print(cred)
print(cred.password)
print(cred.check_password("securepass"))
print(cred.check_password("wrong"))

try:
    cred.password = "short"
except ValueError as e:
    print(f"ValueError raised: {e}")
print()

# WHY store self.__password (double underscore)?
# Name mangling makes it _Credential__password, harder to accidentally
# access from outside. Combined with the masked getter, this is as
# secure as pure Python allows.

# -----------------------------------------------------------------------------
# Solution 4 — Temperature with Multiple Scales
# -----------------------------------------------------------------------------
# KEY INSIGHT: The class stores only Celsius internally (_celsius). All other
# scales are computed properties derived from that single source of truth.
# Factory class methods use cls() so subclasses work too.

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius   # goes through setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = float(value)

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @property
    def kelvin(self):
        return self._celsius + 273.15

    @classmethod
    def from_fahrenheit(cls, f):
        return cls((f - 32) * 5 / 9)

    @classmethod
    def from_kelvin(cls, k):
        return cls(k - 273.15)

    def __str__(self):
        return (f"{self._celsius}°C / {self.fahrenheit}°F / {self.kelvin}K")


t1 = Temperature(100)
print(t1)

t2 = Temperature.from_fahrenheit(32)
print(t2)

t3 = Temperature.from_kelvin(233.15)
print(t3)

try:
    t4 = Temperature(-300)
except ValueError as e:
    print(f"ValueError raised: {e}")
print()

# -----------------------------------------------------------------------------
# Solution 5 — Bank Account with Full Encapsulation
# -----------------------------------------------------------------------------
# KEY INSIGHT: __owner uses name mangling so the owner cannot be changed even
# by subclasses. The read-only @property owner exposes it safely.
# Both deposit() and withdraw() raise ValueError for invalid input rather
# than silently ignoring it — fail loudly, not silently.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.balance = balance   # goes through setter

    @property
    def owner(self):
        return self.__owner   # read-only — no setter

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = float(value)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self._balance:
            raise ValueError("Withdrawal amount exceeds balance")
        self._balance -= amount

    def __str__(self):
        return f"Account[{self.__owner}]: ${self._balance:.2f}"


acc = BankAccount("Alice")
print(acc)
acc.deposit(500)
print(acc)
acc.withdraw(150)
print(acc)

try:
    acc.withdraw(1000)
except ValueError as e:
    print(f"ValueError raised: {e}")

try:
    acc.deposit(-50)
except ValueError as e:
    print(f"ValueError raised: {e}")

# WHY raise ValueError instead of just printing "error"?
# Raising lets the CALLER decide how to handle the error (log it, show a
# dialog, retry, etc.). Printing from inside the class is a dead end —
# the caller gets None back with no way to detect what went wrong.
