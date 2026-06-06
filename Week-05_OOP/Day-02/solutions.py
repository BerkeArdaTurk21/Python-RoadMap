# =============================================================================
# Week 05 - Day 02 | Instance & Class Variables — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — Library Book Tracker
# -----------------------------------------------------------------------------
# KEY INSIGHT: The mutable default bug — never use a list as a class variable
# for per-instance data. Here books is intentionally per-instance, so it goes
# in __init__. total_books is intentionally shared, so it stays as class var.

class Library:
    total_books = 0

    def __init__(self, name):
        self.name  = name
        self.books = []   # per-instance list — NOT a class variable

    def add_book(self, title):
        self.books.append(title)
        Library.total_books += 1   # update the class variable, not self

    @classmethod
    def get_total(cls):
        return cls.total_books

    def __str__(self):
        return f"Library[{self.name}] — {len(self.books)} books"


lib1 = Library("City Library")
lib2 = Library("School Library")

lib1.add_book("1984")
lib1.add_book("Dune")
lib2.add_book("The Hobbit")

print(lib1)
print(lib2)
print(f"Total books across all libraries: {Library.get_total()}")
print()

# WHY Library.total_books += 1 instead of self.total_books += 1?
# self.total_books += 1 would SHADOW the class variable with an instance
# variable on that specific library — the shared counter would stay at 0.
# Always increment via the class name when updating shared state.

# -----------------------------------------------------------------------------
# Solution 2 — Circle with Class Constant
# -----------------------------------------------------------------------------
# KEY INSIGHT: PI is stored once as a class variable so it can be changed in
# one place if precision needs updating. unit_circle() uses cls() so that
# subclasses of Circle would also work correctly.

class Circle:
    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(Circle.PI * self.radius ** 2, 2)

    def circumference(self):
        return round(2 * Circle.PI * self.radius, 2)

    @classmethod
    def unit_circle(cls):
        return cls(1)

    @staticmethod
    def is_valid_radius(r):
        return r > 0

    def __str__(self):
        return f"Circle(r={self.radius})"


c = Circle(5)
print(c)
print(c.area())
print(c.circumference())
unit = Circle.unit_circle()
print(unit)
print(Circle.is_valid_radius(3))
print(Circle.is_valid_radius(-1))
print()

# WHY use cls(1) not Circle(1) in unit_circle?
# If someone subclasses Circle (e.g. class ColoredCircle(Circle):),
# ColoredCircle.unit_circle() would correctly return a ColoredCircle,
# not a plain Circle. This is good factory-method practice.

# -----------------------------------------------------------------------------
# Solution 3 — Fleet Manager
# -----------------------------------------------------------------------------
# KEY INSIGHT: fleet is intentionally a class-level list here — it IS shared
# state. Every Car appends itself to the same list. oldest() uses min() with
# a key to find the lowest year without sorting the whole list.

class Car:
    fleet      = []
    total_cars = 0

    def __init__(self, year, make, model):
        self.year  = year
        self.make  = make
        self.model = model
        Car.fleet.append(self)
        Car.total_cars += 1

    @classmethod
    def fleet_summary(cls):
        print("Fleet:")
        for car in cls.fleet:
            print(f"  {car}")

    @classmethod
    def oldest(cls):
        return min(cls.fleet, key=lambda car: car.year)

    @staticmethod
    def is_vintage(year):
        return year <= 1980

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


c1 = Car(2020, "Toyota",     "Corolla")
c2 = Car(2018, "Ford",       "Mustang")
c3 = Car(1975, "Volkswagen", "Beetle")

Car.fleet_summary()
print(f"Oldest: {Car.oldest()}")
print(f"Is 1975 vintage? {Car.is_vintage(1975)}")
print(f"Is 2020 vintage? {Car.is_vintage(2020)}")
print()

# WHY min(..., key=lambda car: car.year)?
# fleet is a list of Car objects, not ints. We tell min() to compare
# by the .year attribute using a lambda key function.

# -----------------------------------------------------------------------------
# Solution 4 — User Registration
# -----------------------------------------------------------------------------
# KEY INSIGHT: _next_id uses a single underscore to signal it's internal.
# from_string() is a classic @classmethod factory that parses a string and
# delegates to __init__. is_valid_email() is @staticmethod — pure logic,
# no instance or class state needed.

class User:
    user_count = 0
    _next_id   = 1

    def __init__(self, username, email):
        self.username = username
        self.email    = email
        self.user_id  = User._next_id
        User._next_id   += 1
        User.user_count += 1

    @classmethod
    def from_string(cls, s):
        username, email = s.split(":")
        return cls(username, email)

    @staticmethod
    def is_valid_email(email):
        return "@" in email and "." in email

    def __str__(self):
        return f"User#{self.user_id} {self.username} ({self.email})"


u1 = User("alice", "alice@example.com")
u2 = User.from_string("bob:bob@example.com")
u3 = User("carol", "carol@example.com")

print(u1)
print(u2)
print(u3)
print(f"Total users: {User.user_count}")
print(User.is_valid_email("test@mail.com"))
print(User.is_valid_email("notanemail"))
print()

# WHY split(":") with exactly one colon?
# The spec says the format is "username:email". In a real project you'd
# validate the format first, but for this exercise one split is enough.

# -----------------------------------------------------------------------------
# Solution 5 — Geometry Toolkit
# -----------------------------------------------------------------------------
# KEY INSIGHT: larger() is @staticmethod because it compares two Rectangle
# objects using only their public area() method — it needs no class or
# instance state of its own. square() uses cls(side, side) so subclasses
# inherit the factory correctly.

class Rectangle:
    shapes_created = 0

    def __init__(self, width, height):
        self.width  = width
        self.height = height
        Rectangle.shapes_created += 1

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    @classmethod
    def square(cls, side):
        return cls(side, side)

    @staticmethod
    def larger(r1, r2):
        return r1 if r1.area() >= r2.area() else r2

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"


r1 = Rectangle(4, 6)
r2 = Rectangle.square(5)

print(r1)
print(r1.area())
print(r1.perimeter())
print(r1.is_square())
print(r2)
print(r2.is_square())
print(Rectangle.larger(r1, r2))
print(f"Shapes created: {Rectangle.shapes_created}")

# WHY r1.area() >= r2.area() (not just >)?
# Using >= means if two rectangles have equal area, r1 is returned.
# This makes the tie-breaking rule explicit and deterministic.
