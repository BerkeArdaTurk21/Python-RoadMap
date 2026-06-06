# =============================================================================
# Week 05 - Day 02 | Instance & Class Variables
# =============================================================================
# Topics: instance variables, class variables, @classmethod, @staticmethod,
#         when to use each, class variable pitfalls
# =============================================================================

# -----------------------------------------------------------------------------
# 1. INSTANCE VARIABLES vs CLASS VARIABLES
# -----------------------------------------------------------------------------
# Instance variable: belongs to ONE specific object — each instance has its own
# Class variable:    belongs to the CLASS itself — shared by ALL instances
#
# Use instance variables for data that differs per object (name, age, balance).
# Use class variables for data that is the same for every object of that type.

class Dog:
    # CLASS variable — shared across ALL Dog instances
    species = "Canis lupus familiaris"

    def __init__(self, name, age):
        # INSTANCE variables — each dog has its own name and age
        self.name = name
        self.age  = age

rex  = Dog("Rex",  3)
luna = Dog("Luna", 5)

print(rex.name)       # Rex    ← instance variable
print(luna.name)      # Luna   ← different instance, different value

print(rex.species)    # Canis lupus familiaris  ← class variable
print(luna.species)   # Canis lupus familiaris  ← same value for all dogs
print(Dog.species)    # Canis lupus familiaris  ← access directly on the class

# -----------------------------------------------------------------------------
# 2. CLASS VARIABLES — SHARED STATE
# -----------------------------------------------------------------------------
# A common use-case: counting how many instances have been created.

class Employee:
    employee_count = 0   # class variable — starts at 0

    def __init__(self, name, department):
        self.name       = name
        self.department = department
        Employee.employee_count += 1   # update the CLASS variable, not self

    def __str__(self):
        return f"{self.name} ({self.department})"

e1 = Employee("Alice", "Engineering")
e2 = Employee("Bob",   "Marketing")
e3 = Employee("Carol", "Engineering")

print(Employee.employee_count)   # 3 — shared counter
print(e1.employee_count)         # 3 — visible via instance too
print(e2.employee_count)         # 3 — same value

# -----------------------------------------------------------------------------
# 3. THE SHADOWING PITFALL
# -----------------------------------------------------------------------------
# If you assign to an instance attribute with the SAME name as a class variable,
# Python creates a NEW instance attribute — it does NOT change the class variable.

class Config:
    debug = False   # class variable

c1 = Config()
c2 = Config()

c1.debug = True     # creates an INSTANCE variable on c1 — shadows class var

print(c1.debug)     # True   ← c1's own instance variable
print(c2.debug)     # False  ← still reads the class variable
print(Config.debug) # False  ← class variable is unchanged

# To change the class variable for ALL instances, assign on the CLASS:
Config.debug = True
print(c2.debug)     # True   ← now all instances see the change

# Reset for clarity
Config.debug = False

# -----------------------------------------------------------------------------
# 4. CLASS METHODS — @classmethod
# -----------------------------------------------------------------------------
# A class method receives the CLASS (not an instance) as its first argument.
# Convention: name the first parameter 'cls' (short for class).
#
# Most common uses:
#   • Alternative constructors (factory methods)
#   • Operating on class variables

class Temperature:
    unit = "Celsius"   # class variable

    def __init__(self, celsius):
        self.celsius = celsius

    def __str__(self):
        return f"{self.celsius}°C"

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        """Alternative constructor — create Temperature from Fahrenheit."""
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)   # cls(...) calls __init__ just like Temperature(...)

    @classmethod
    def from_kelvin(cls, kelvin):
        """Alternative constructor — create Temperature from Kelvin."""
        celsius = kelvin - 273.15
        return cls(celsius)

    @classmethod
    def change_unit(cls, new_unit):
        cls.unit = new_unit   # modifies the class variable for all instances

t1 = Temperature(100)
t2 = Temperature.from_fahrenheit(212)   # 100°C
t3 = Temperature.from_kelvin(373.15)    # 100°C

print(t1)   # 100°C
print(t2)   # 100.0°C
print(t3)   # 100.0°C

print(Temperature.unit)   # Celsius
Temperature.change_unit("Kelvin")
print(Temperature.unit)   # Kelvin

# -----------------------------------------------------------------------------
# 5. STATIC METHODS — @staticmethod
# -----------------------------------------------------------------------------
# A static method receives NEITHER self NOR cls.
# It's a plain function that lives inside a class for organisational reasons.
#
# Use it when:
#   • The logic belongs conceptually to the class
#   • It doesn't need to read or write any instance or class data

class MathUtils:
    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def clamp(value, minimum, maximum):
        """Clamp value to the range [minimum, maximum]."""
        return max(minimum, min(maximum, value))

    @staticmethod
    def percentage(part, total):
        if total == 0:
            return 0.0
        return round(part / total * 100, 2)

print(MathUtils.is_even(4))            # True
print(MathUtils.is_even(7))            # False
print(MathUtils.clamp(15, 0, 10))      # 10
print(MathUtils.clamp(-3, 0, 10))      # 0
print(MathUtils.percentage(3, 4))      # 75.0

# Static methods can also be called on an instance (but calling on the class
# makes it clearer that no instance data is involved)
utils = MathUtils()
print(utils.is_even(6))   # True — works, but less clear

# -----------------------------------------------------------------------------
# 6. COMPARING ALL THREE TYPES
# -----------------------------------------------------------------------------
#
#  Type            First param   Receives           Typical use
#  --------------- ------------- ------------------ --------------------------
#  Instance method  self          the instance       read/modify instance data
#  Class method     cls           the class          factory methods, class vars
#  Static method    —             nothing            utility helpers
#

class Date:
    default_separator = "-"   # class variable

    def __init__(self, year, month, day):
        self.year  = year
        self.month = month
        self.day   = day

    def format(self):
        """Instance method — uses self to format this specific date."""
        sep = Date.default_separator
        return f"{self.year}{sep}{self.month:02d}{sep}{self.day:02d}"

    @classmethod
    def from_string(cls, date_str):
        """Class method (factory) — creates a Date from a 'YYYY-MM-DD' string."""
        year, month, day = map(int, date_str.split("-"))
        return cls(year, month, day)

    @classmethod
    def set_separator(cls, sep):
        """Class method — changes the separator for ALL dates."""
        cls.default_separator = sep

    @staticmethod
    def is_leap_year(year):
        """Static method — pure logic, no instance or class data needed."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

d1 = Date(2025, 6, 15)
d2 = Date.from_string("2024-02-29")   # factory method

print(d1.format())              # 2025-06-15
print(d2.format())              # 2024-02-29

Date.set_separator("/")
print(d1.format())              # 2025/06/15

print(Date.is_leap_year(2024))  # True
print(Date.is_leap_year(2025))  # False

# Reset
Date.set_separator("-")

# -----------------------------------------------------------------------------
# 7. CLASS VARIABLES WITH MUTABLE DEFAULTS — A CLASSIC BUG
# -----------------------------------------------------------------------------
# Never use a mutable object (list, dict) as a class variable if you intend
# it to be per-instance. All instances will SHARE the same list!

class BuggyStudent:
    grades = []   # WRONG — all students share this one list!

    def __init__(self, name):
        self.name = name

    def add_grade(self, g):
        self.grades.append(g)   # appends to the SHARED class list

s1 = BuggyStudent("Alice")
s2 = BuggyStudent("Bob")
s1.add_grade(90)
print(s2.grades)   # [90] ← Bob sees Alice's grade! BUG!

# FIX: initialise the list in __init__ so each instance gets its own copy

class CorrectStudent:
    def __init__(self, name):
        self.name   = name
        self.grades = []   # CORRECT — each instance gets its own list

    def add_grade(self, g):
        self.grades.append(g)

s3 = CorrectStudent("Alice")
s4 = CorrectStudent("Bob")
s3.add_grade(90)
print(s4.grades)   # []  ← Bob's list is empty, as expected

# =============================================================================
# SUMMARY
# =============================================================================
# ┌──────────────────┬─────────────────────────────────────────────────────┐
# │  Concept         │  Key Point                                          │
# ├──────────────────┼─────────────────────────────────────────────────────┤
# │  Instance var    │  Defined in __init__ via self.x — per-object        │
# │  Class var       │  Defined in class body — shared by ALL instances    │
# │  @classmethod    │  Receives cls; used for factories & class var ops   │
# │  @staticmethod   │  No self/cls; pure utility function inside class    │
# │  Shadowing       │  self.x = ... on a class var creates instance copy  │
# │  Mutable default │  Never use lists/dicts as class vars for per-obj    │
# └──────────────────┴─────────────────────────────────────────────────────┘
print("\nDay 02 — Instance & Class Variables complete!")
