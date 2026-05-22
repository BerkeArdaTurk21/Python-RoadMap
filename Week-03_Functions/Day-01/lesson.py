# Week 3 - Day 1: Defining Functions
# Topic: def, parameters, return, docstrings

# ─────────────────────────────────────────────
# 1. WHY FUNCTIONS?
# ─────────────────────────────────────────────
# Functions let you:
#   - Reuse code without repeating it (DRY principle)
#   - Break a large problem into small named pieces
#   - Test and fix logic in one place
#   - Make code readable with descriptive names

# Without functions — repeated logic:
print(2 ** 2)
print(3 ** 2)
print(5 ** 2)

# With a function — defined once, called many times:
def square(n):
    return n ** 2

print(square(2))    # 4
print(square(3))    # 9
print(square(5))    # 25


# ─────────────────────────────────────────────
# 2. DEFINING A FUNCTION — def
# ─────────────────────────────────────────────
# Syntax:
#   def function_name(parameters):
#       <body>
#       return value        ← optional

def greet():                # no parameters
    print("Hello, World!")

greet()                     # Hello, World!
greet()                     # call it again — code runs twice


# ─────────────────────────────────────────────
# 3. PARAMETERS AND ARGUMENTS
# ─────────────────────────────────────────────
# Parameter = the variable name in the function definition
# Argument  = the actual value passed when calling the function

def greet_person(name):     # 'name' is a parameter
    print(f"Hello, {name}!")

greet_person("Berke")       # "Berke" is the argument
greet_person("Alice")

# Multiple parameters
def add(a, b):
    print(f"{a} + {b} = {a + b}")

add(3, 5)                   # 3 + 5 = 8
add(10, 20)                 # 10 + 20 = 30


# ─────────────────────────────────────────────
# 4. return STATEMENT
# ─────────────────────────────────────────────
# return sends a value BACK to the caller.
# Without return, a function implicitly returns None.

def multiply(a, b):
    return a * b

result = multiply(4, 7)     # capture the returned value
print(result)               # 28
print(multiply(3, 3))       # 9 — use directly in print

# return exits the function immediately
def first_positive(numbers):
    for n in numbers:
        if n > 0:
            return n        # exits as soon as one is found
    return None             # only reached if none found

print(first_positive([-3, -1, 4, 7]))   # 4
print(first_positive([-3, -1, -5]))     # None

# Returning multiple values (as a tuple)
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 2, 9, 1, 7])
print(f"Min: {low}, Max: {high}")       # Min: 1, Max: 9


# ─────────────────────────────────────────────
# 5. FUNCTIONS WITHOUT return
# ─────────────────────────────────────────────
# A function that only performs an action (no return value).
# These are called for their SIDE EFFECT (e.g. printing).

def print_separator(char="-", length=30):
    print(char * length)

print_separator()           # ------------------------------
print_separator("=", 20)    # ====================

# Implicit None return
def do_nothing():
    pass

result = do_nothing()
print(result)               # None


# ─────────────────────────────────────────────
# 6. DOCSTRINGS — DOCUMENTING YOUR FUNCTION
# ─────────────────────────────────────────────
# A docstring is a string literal on the first line of a function body.
# It describes what the function does, its parameters, and return value.
# Access it with: function.__doc__ or help(function)

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Parameters:
        celsius (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return celsius * 9 / 5 + 32

print(celsius_to_fahrenheit(0))     # 32.0
print(celsius_to_fahrenheit(100))   # 212.0
print(celsius_to_fahrenheit.__doc__)


# ─────────────────────────────────────────────
# 7. FUNCTIONS CALLING OTHER FUNCTIONS
# ─────────────────────────────────────────────

def square(n):
    """Return n squared."""
    return n ** 2

def sum_of_squares(a, b):
    """Return the sum of squares of a and b."""
    return square(a) + square(b)

print(sum_of_squares(3, 4))     # 9 + 16 = 25
print(sum_of_squares(5, 12))    # 25 + 144 = 169


# ─────────────────────────────────────────────
# 8. FUNCTIONS AS VALUES
# ─────────────────────────────────────────────
# In Python, functions are first-class objects.
# You can assign them to variables, pass them as arguments,
# store them in lists, etc.

def double(x):
    return x * 2

def triple(x):
    return x * 3

operation = double          # assign function to a variable
print(operation(5))         # 10

operation = triple
print(operation(5))         # 15

# Pass a function as an argument
def apply(func, value):
    return func(value)

print(apply(double, 7))     # 14
print(apply(triple, 7))     # 21


# ─────────────────────────────────────────────
# 9. TYPE HINTS (ANNOTATIONS)
# ─────────────────────────────────────────────
# Python 3 supports optional type hints.
# They don't enforce types at runtime but improve readability
# and help IDEs and tools like mypy catch errors.

def add_ints(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b

def full_name(first: str, last: str) -> str:
    """Return the full name."""
    return f"{first} {last}"

print(add_ints(3, 7))               # 10
print(full_name("Berke", "Türk"))   # Berke Türk


# ─────────────────────────────────────────────
# 10. PRACTICAL EXAMPLE — Unit Converter
# ─────────────────────────────────────────────

def km_to_miles(km: float) -> float:
    """Convert kilometres to miles."""
    return km * 0.621371

def kg_to_pounds(kg: float) -> float:
    """Convert kilograms to pounds."""
    return kg * 2.20462

def liters_to_gallons(liters: float) -> float:
    """Convert litres to US gallons."""
    return liters * 0.264172

def convert_and_report(km: float, kg: float, liters: float) -> None:
    """Print a full conversion report."""
    print("── Unit Conversion Report ──")
    print(f"  {km} km       = {km_to_miles(km):.2f} miles")
    print(f"  {kg} kg       = {kg_to_pounds(kg):.2f} pounds")
    print(f"  {liters} L    = {liters_to_gallons(liters):.2f} gallons")

convert_and_report(100, 70, 50)
# ── Unit Conversion Report ──
#   100 km    = 62.14 miles
#   70 kg     = 154.32 pounds
#   50 L      = 13.21 gallons
