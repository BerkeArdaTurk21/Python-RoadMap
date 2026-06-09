# =============================================================================
# Week 05 - Day 05 | Polymorphism
# =============================================================================
# Topics: polymorphism definition, method overriding, duck typing,
#         polymorphic functions, operator overloading preview
# =============================================================================

# -----------------------------------------------------------------------------
# 1. WHAT IS POLYMORPHISM?
# -----------------------------------------------------------------------------
# Polymorphism = "many forms". In OOP, the same method name behaves
# DIFFERENTLY depending on the object it is called on.
#
# Two main mechanisms in Python:
#   1. Method overriding — subclass redefines a parent method
#   2. Duck typing      — any object with the right methods "fits"

# -----------------------------------------------------------------------------
# 2. METHOD OVERRIDING — RUNTIME POLYMORPHISM
# -----------------------------------------------------------------------------
# The same call (animal.speak()) produces different output for each type.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name}: ..."

class Dog(Animal):
    def speak(self):
        return f"{self.name}: Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name}: Meow!"

class Duck(Animal):
    def speak(self):
        return f"{self.name}: Quack!"

animals = [Dog("Rex"), Cat("Whiskers"), Duck("Donald"), Animal("?")]

for a in animals:
    print(a.speak())   # same call — different result

# Python decides WHICH speak() to call at runtime based on the object's type.

# -----------------------------------------------------------------------------
# 3. POLYMORPHIC FUNCTIONS
# -----------------------------------------------------------------------------
# A function can work with any object that has the required interface.

def make_sound(animal):
    """Works with ANY object that has a speak() method."""
    print(animal.speak())

make_sound(Dog("Buddy"))      # Buddy: Woof!
make_sound(Cat("Mittens"))    # Mittens: Meow!

# The function doesn't know or care what TYPE animal is — only that it
# has a speak() method. This is the open/closed principle in action.

# -----------------------------------------------------------------------------
# 4. DUCK TYPING
# -----------------------------------------------------------------------------
# "If it walks like a duck and quacks like a duck, it IS a duck."
# Python checks for METHOD EXISTENCE at runtime, not inheritance.
# An object doesn't need to inherit from Animal to work with make_sound().

class Robot:
    """Not an Animal, but has speak() — so it works!"""
    def __init__(self, model):
        self.name = model

    def speak(self):
        return f"{self.name}: BEEP BOOP"

make_sound(Robot("R2D2"))   # R2D2: BEEP BOOP  ← works! No inheritance needed.

# Contrast: Java / C++ would require Robot to implement an Animal interface.
# Python simply tries to call .speak() and raises AttributeError if missing.

# -----------------------------------------------------------------------------
# 5. POLYMORPHISM WITH BUILT-IN FUNCTIONS
# -----------------------------------------------------------------------------
# Python's built-in functions already use polymorphism via magic methods.

print(len("hello"))     # 5 — str.__len__
print(len([1, 2, 3]))   # 3 — list.__len__
print(len({1, 2}))      # 2 — set.__len__

# len() works on ANY object that defines __len__.
# abs(), str(), repr(), bool(), iter() — all polymorphic via magic methods.

# -----------------------------------------------------------------------------
# 6. PRACTICAL SHAPE EXAMPLE
# -----------------------------------------------------------------------------

import math

class Shape:
    def area(self):
        return 0.0

    def describe(self):
        return f"{type(self).__name__} with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


class Triangle(Shape):
    def __init__(self, base, height):
        self.base, self.height = base, height

    def area(self):
        return 0.5 * self.base * self.height


def total_area(shapes):
    """Polymorphic — works with ANY Shape subclass."""
    return sum(s.area() for s in shapes)


shapes = [Rectangle(4, 6), Circle(3), Triangle(5, 8)]

for s in shapes:
    print(s.describe())

print(f"Total area: {total_area(shapes):.2f}")   # any mix of shapes works

# -----------------------------------------------------------------------------
# 7. OPERATOR OVERLOADING (PREVIEW)
# -----------------------------------------------------------------------------
# Operators like +, ==, < are polymorphic too. Python calls magic methods.
# Full coverage in Day 06 — Magic Methods.

class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):       # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):        # v1 == v2
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)       # Vector(4, 6)
print(v1 == v2)      # False
print(v1 == Vector(1, 2))  # True

# Same '+' operator behaves differently for int, str, list, and now Vector.

# -----------------------------------------------------------------------------
# 8. isinstance() IN POLYMORPHIC CODE
# -----------------------------------------------------------------------------
# Sometimes you need type-specific behaviour inside a polymorphic function.
# Prefer method overriding when possible; use isinstance() only when needed.

def process(shape):
    if isinstance(shape, Circle):
        print(f"Circle: diameter = {shape.r * 2:.2f}")
    elif isinstance(shape, Rectangle):
        print(f"Rectangle: perimeter = {2*(shape.w+shape.h):.2f}")
    else:
        print(f"Shape: area = {shape.area():.2f}")


for s in shapes:
    process(s)

# =============================================================================
# SUMMARY
# =============================================================================
# ┌─────────────────────┬────────────────────────────────────────────────────┐
# │  Concept            │  Key Point                                         │
# ├─────────────────────┼────────────────────────────────────────────────────┤
# │  Polymorphism       │  Same interface → different behaviour per type     │
# │  Method overriding  │  Subclass redefines a parent method                │
# │  Duck typing        │  Works if the object has the needed methods        │
# │  Polymorphic fn     │  Functions that work on many types via an interface│
# │  Operator overload  │  +, ==, < etc. call magic methods (__add__, ...)   │
# └─────────────────────┴────────────────────────────────────────────────────┘
print("\nDay 05 — Polymorphism complete!")
