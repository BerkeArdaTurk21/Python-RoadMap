# =============================================================================
# Week 05 - Day 02 | Instance & Class Variables — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Library Book Tracker
# -----------------------------------------------------------------------------
# Create a Library class with:
#   - Class variable total_books = 0 that increases each time a book is added
#   - Class variable books = []  (WATCH OUT — fix the mutable default bug!)
#   - __init__(self, name)        ← library name
#   - add_book(self, title)       ← appends title to THIS library's books list
#                                    AND increments total_books on the class
#   - @classmethod get_total(cls) ← returns total_books
#   - __str__                     ← "Library[City Library] — 3 books"
#
# Expected output:
#   Library[City Library] — 2 books
#   Library[School Library] — 1 books
#   Total books across all libraries: 3

class Library:
    total_books = 0
    pass  # TODO


lib1 = Library("City Library")
lib2 = Library("School Library")

lib1.add_book("1984")
lib1.add_book("Dune")
lib2.add_book("The Hobbit")

print(lib1)                             # Library[City Library] — 2 books
print(lib2)                             # Library[School Library] — 1 books
print(f"Total books across all libraries: {Library.get_total()}")  # 3
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Circle with Class Constant
# -----------------------------------------------------------------------------
# Create a Circle class with:
#   - Class variable PI = 3.14159  (used instead of importing math)
#   - __init__(self, radius)
#   - area(self)          → PI * r²,  rounded to 2 decimal places
#   - circumference(self) → 2 * PI * r, rounded to 2 decimal places
#   - @classmethod unit_circle(cls) ← factory: returns Circle with radius=1
#   - @staticmethod is_valid_radius(r) ← True if r > 0, False otherwise
#   - __str__             → "Circle(r=5)"
#
# Expected output:
#   Circle(r=5)
#   78.54
#   31.42
#   Circle(r=1)
#   True
#   False

class Circle:
    PI = 3.14159
    pass  # TODO


c = Circle(5)
print(c)                            # Circle(r=5)
print(c.area())                     # 78.54
print(c.circumference())            # 31.42
unit = Circle.unit_circle()
print(unit)                         # Circle(r=1)
print(Circle.is_valid_radius(3))    # True
print(Circle.is_valid_radius(-1))   # False
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Fleet Manager
# -----------------------------------------------------------------------------
# Create a Car class that tracks all cars ever created:
#   - Class variable fleet = []  (one shared list for all cars)
#   - Class variable total_cars = 0
#   - __init__(self, make, model, year)
#     → appends self to fleet, increments total_cars
#   - @classmethod fleet_summary(cls) ← prints each car in the fleet
#   - @classmethod oldest(cls)        ← returns the Car with the smallest year
#   - @staticmethod is_vintage(year)  ← True if year <= 1980
#   - __str__                         → "2020 Toyota Corolla"
#
# Expected output:
#   Fleet:
#     2020 Toyota Corolla
#     2018 Ford Mustang
#     1975 Volkswagen Beetle
#   Oldest: 1975 Volkswagen Beetle
#   Is 1975 vintage? True
#   Is 2020 vintage? False

class Car:
    fleet = []
    total_cars = 0
    pass  # TODO


c1 = Car(2020, "Toyota",    "Corolla")
c2 = Car(2018, "Ford",      "Mustang")
c3 = Car(1975, "Volkswagen","Beetle")

Car.fleet_summary()
print(f"Oldest: {Car.oldest()}")
print(f"Is 1975 vintage? {Car.is_vintage(1975)}")
print(f"Is 2020 vintage? {Car.is_vintage(2020)}")
print()

# -----------------------------------------------------------------------------
# Exercise 4 — User Registration
# -----------------------------------------------------------------------------
# Create a User class with:
#   - Class variable user_count = 0
#   - Class variable _next_id = 1      (private — starts at 1, auto-increments)
#   - __init__(self, username, email)
#     → assigns self.user_id = User._next_id, then increments _next_id
#     → increments user_count
#   - @classmethod from_string(cls, s) ← s is "username:email", returns User
#   - @staticmethod is_valid_email(email) ← True if "@" and "." both in email
#   - __str__  → "User#1 alice (alice@example.com)"
#
# Expected output:
#   User#1 alice (alice@example.com)
#   User#2 bob (bob@example.com)
#   User#3 carol (carol@example.com)
#   Total users: 3
#   True
#   False

class User:
    user_count = 0
    _next_id   = 1
    pass  # TODO


u1 = User("alice", "alice@example.com")
u2 = User.from_string("bob:bob@example.com")
u3 = User("carol", "carol@example.com")

print(u1)                                   # User#1 alice (alice@example.com)
print(u2)                                   # User#2 bob (bob@example.com)
print(u3)                                   # User#3 carol (carol@example.com)
print(f"Total users: {User.user_count}")    # Total users: 3
print(User.is_valid_email("test@mail.com")) # True
print(User.is_valid_email("notanemail"))    # False
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Geometry Toolkit
# -----------------------------------------------------------------------------
# Create a Rectangle class with:
#   - Class variable shapes_created = 0   (increments on each creation)
#   - __init__(self, width, height)
#   - area(self)      → width * height
#   - perimeter(self) → 2 * (width + height)
#   - is_square(self) → True if width == height
#   - @classmethod square(cls, side) ← factory: returns Rectangle(side, side)
#   - @staticmethod larger(r1, r2)   ← returns whichever rectangle has bigger area
#   - __str__                        → "Rectangle(4x6)"
#
# Expected output:
#   Rectangle(4x6)
#   24
#   20
#   False
#   Rectangle(5x5)
#   True
#   Rectangle(5x5)
#   Shapes created: 2

class Rectangle:
    shapes_created = 0
    pass  # TODO


r1 = Rectangle(4, 6)
r2 = Rectangle.square(5)

print(r1)                              # Rectangle(4x6)
print(r1.area())                       # 24
print(r1.perimeter())                  # 20
print(r1.is_square())                  # False
print(r2)                              # Rectangle(5x5)
print(r2.is_square())                  # True
print(Rectangle.larger(r1, r2))        # Rectangle(5x5)  (area 25 > 24)
print(f"Shapes created: {Rectangle.shapes_created}")  # Shapes created: 2
