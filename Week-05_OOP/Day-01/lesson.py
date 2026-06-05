# =============================================================================
# Week 05 - Day 01 | Classes & Objects
# =============================================================================
# Topics: class keyword, __init__, self, instance creation, instance methods,
#         attributes, object identity, __str__ preview
# =============================================================================

# -----------------------------------------------------------------------------
# 1. WHAT IS A CLASS?
# -----------------------------------------------------------------------------
# A class is a BLUEPRINT for creating objects.
# An object (instance) is one specific thing built from that blueprint.
#
# Real-world analogy:
#   Class  = the blueprint for a house
#   Object = an actual house built from that blueprint
#
# Before OOP, you'd store related data in separate variables:
name  = "Rex"
breed = "Labrador"
age   = 3
# This gets messy fast. OOP bundles data AND behaviour together.

# -----------------------------------------------------------------------------
# 2. DEFINING A CLASS
# -----------------------------------------------------------------------------
# Syntax:
#   class ClassName:
#       def __init__(self, ...):
#           ...
#
# Convention: class names use PascalCase (each word capitalised).

class Dog:
    """A simple class representing a dog."""

    def __init__(self, name, breed, age):
        # __init__ is the CONSTRUCTOR — called automatically when you create
        # a new instance. It sets up the object's initial state.
        #
        # 'self' refers to the specific instance being created.
        # Every method's first parameter must be 'self'.
        self.name  = name    # instance attribute
        self.breed = breed   # instance attribute
        self.age   = age     # instance attribute

# -----------------------------------------------------------------------------
# 3. CREATING INSTANCES (OBJECTS)
# -----------------------------------------------------------------------------
# Call the class like a function — Python calls __init__ for you.

rex  = Dog("Rex",  "Labrador", 3)
luna = Dog("Luna", "Husky",    5)
max_ = Dog("Max",  "Poodle",   1)

print(rex)           # <__main__.Dog object at 0x...>  ← raw memory address
print(type(rex))     # <class '__main__.Dog'>
print(type(rex) == Dog)   # True

# Each instance is a SEPARATE object with its OWN copy of attributes
print(rex.name)    # Rex
print(luna.name)   # Luna
print(max_.age)    # 1

# -----------------------------------------------------------------------------
# 4. SELF — THE INSTANCE REFERENCE
# -----------------------------------------------------------------------------
# 'self' is NOT a keyword — it is just a convention.
# Python passes the instance automatically as the first argument.
#
# When you write:
#   rex.bark()
# Python translates it to:
#   Dog.bark(rex)
#
# So 'self' inside the method IS 'rex'.

class Cat:
    def __init__(self, name):
        self.name = name   # self = the specific cat being created

    def speak(self):
        # self.name uses THIS instance's name
        return f"{self.name} says: Meow!"

whiskers = Cat("Whiskers")
shadow   = Cat("Shadow")

print(whiskers.speak())   # Whiskers says: Meow!
print(shadow.speak())     # Shadow says: Meow!

# -----------------------------------------------------------------------------
# 5. INSTANCE METHODS
# -----------------------------------------------------------------------------
# A method is a function defined INSIDE a class.
# It always takes 'self' as the first parameter.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def circumference(self):
        import math
        return 2 * math.pi * self.radius

    def is_bigger_than(self, other):
        # 'other' is another Circle instance
        return self.radius > other.radius

c1 = Circle(5)
c2 = Circle(3)

print(f"Area of c1:          {c1.area():.2f}")           # 78.54
print(f"Circumference of c1: {c1.circumference():.2f}")  # 31.42
print(f"c1 bigger than c2?   {c1.is_bigger_than(c2)}")   # True

# -----------------------------------------------------------------------------
# 6. ADDING / MODIFYING ATTRIBUTES
# -----------------------------------------------------------------------------
# You can add or change attributes on an instance at any time.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def greet(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

    def have_birthday(self):
        self.age += 1   # modify an attribute inside a method

alice = Person("Alice", 30)
print(alice.greet())         # Hi, I'm Alice and I'm 30 years old.

alice.have_birthday()
print(alice.age)             # 31  ← changed via method

# Add a brand-new attribute after creation (possible but not ideal — use __init__)
alice.email = "alice@example.com"
print(alice.email)           # alice@example.com

# Change an attribute directly
alice.name = "Alice Smith"
print(alice.name)            # Alice Smith

# -----------------------------------------------------------------------------
# 7. MULTIPLE INSTANCES ARE INDEPENDENT
# -----------------------------------------------------------------------------
# Changing one instance NEVER affects another.

p1 = Person("Bob",   25)
p2 = Person("Carol", 28)

p1.have_birthday()

print(p1.age)   # 26  ← only p1 changed
print(p2.age)   # 28  ← p2 is unaffected

# Each instance has its own namespace
print(p1.__dict__)   # {'name': 'Bob', 'age': 26}
print(p2.__dict__)   # {'name': 'Carol', 'age': 28}

# -----------------------------------------------------------------------------
# 8. THE __str__ METHOD (PREVIEW)
# -----------------------------------------------------------------------------
# By default, print(obj) shows <ClassName object at 0x...>.
# Define __str__ to control what print() shows.
# (Covered fully in Week 05 - Day 06 — Magic Methods.)

class Book:
    def __init__(self, title, author, pages):
        self.title  = title
        self.author = author
        self.pages  = pages

    def __str__(self):
        return f'"{self.title}" by {self.author} ({self.pages} pages)'

    def is_long(self):
        return self.pages > 300

b1 = Book("1984",              "George Orwell",  328)
b2 = Book("The Great Gatsby",  "F. Scott Fitzgerald", 180)

print(b1)               # "1984" by George Orwell (328 pages)
print(b2)               # "The Great Gatsby" by F. Scott Fitzgerald (180 pages)
print(b1.is_long())     # True
print(b2.is_long())     # False

# -----------------------------------------------------------------------------
# 9. OBJECT IDENTITY & EQUALITY
# -----------------------------------------------------------------------------
# Two variables can point to the SAME object (identity) or equal objects.

a = Dog("Rex", "Labrador", 3)
b = a            # b is the SAME object as a (reference)
c = Dog("Rex", "Labrador", 3)   # c is a DIFFERENT object with same data

print(a is b)    # True  — same object in memory
print(a is c)    # False — different objects
print(id(a))     # memory address of a
print(id(c))     # different address

# Without __eq__ defined, == also checks identity (same as 'is')
print(a == b)    # True  (same object)
print(a == c)    # False (different objects, __eq__ not customised yet)

# (We'll customise == with __eq__ in Day 06.)

# =============================================================================
# SUMMARY
# =============================================================================
# ┌─────────────────────────────────────────────────────────────────────┐
# │  Concept          │  What it means                                  │
# ├─────────────────────────────────────────────────────────────────────┤
# │  class            │  Blueprint / template for objects               │
# │  __init__         │  Constructor — sets up initial state            │
# │  self             │  Reference to the specific instance             │
# │  instance         │  One object created from the class              │
# │  attribute        │  Data stored on an instance (self.x = ...)      │
# │  method           │  Function defined inside a class                │
# │  __str__          │  Controls what print(obj) shows                 │
# │  __dict__         │  Dict of all instance attributes                │
# └─────────────────────────────────────────────────────────────────────┘
print("\nDay 01 — Classes & Objects complete!")
