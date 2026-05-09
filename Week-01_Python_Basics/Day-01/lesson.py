"""
================================================
Week 1 | Day 1 — Variables & Data Types
================================================
Level       : Beginner
Topics      : variable assignment, naming rules, int, float, str,
              bool, NoneType, type(), id(), multiple assignment
Goal        : Understand what variables are, how Python stores data,
              and which data type to use for each kind of information
================================================
"""

# ── SECTION 1: What Is a Variable? ───────────────
# A variable is a named container that holds a value in memory.
# Think of it like a labelled box: you put something inside,
# then refer to the box by its label whenever you need the value.

name = "Berke"          # str  — text data, always in quotes
age = 25                # int  — whole numbers, no quotes
height = 1.82           # float — decimal numbers
is_developer = True     # bool — only True or False (capital first letter)
middle_name = None      # NoneType — represents "nothing" or "no value yet"

print(name)             # Output: Berke
print(age)              # Output: 25
print(height)           # Output: 1.82
print(is_developer)     # Output: True
print(middle_name)      # Output: None


# ── SECTION 2: The type() Function ───────────────
# type() tells you what kind of data a variable holds.
# Python figures out the type automatically — this is called
# "dynamic typing" (you don't need to declare types manually).

print(type(name))           # Output: <class 'str'>
print(type(age))            # Output: <class 'int'>
print(type(height))         # Output: <class 'float'>
print(type(is_developer))   # Output: <class 'bool'>
print(type(middle_name))    # Output: <class 'NoneType'>


# ── SECTION 3: Naming Rules & Conventions ────────
# RULES (enforced by Python — will raise SyntaxError if broken):
#   - Can contain letters, digits, underscores
#   - Cannot start with a digit
#   - Cannot use Python keywords (if, for, class, etc.)
#   - Case-sensitive: name ≠ Name ≠ NAME

# CONVENTIONS (PEP 8 — not enforced, but expected by all Python devs):
#   - Use snake_case for variables and functions:  first_name, total_price
#   - Use UPPER_SNAKE_CASE for constants:          MAX_SIZE, PI
#   - Use PascalCase for class names:              MyClass, BankAccount
#   - Be descriptive: user_age is better than ua or x

first_name = "Berke"        # good — descriptive, snake_case
last_name = "Turk"          # good
MAX_RETRIES = 3             # good — constant
x = 42                      # acceptable for math/throwaway, avoid elsewhere

# Bad examples (valid Python but poor style):
# FirstName = "Berke"       # PascalCase — reserved for classes
# firstname = "Berke"       # hard to read
# fn = "Berke"              # cryptic abbreviation


# ── SECTION 4: Reassignment & Dynamic Typing ─────
# Variables can be reassigned — even to a different type.
# Python changes the type on the fly (dynamic typing).

counter = 10
print(counter)              # Output: 10
print(type(counter))        # Output: <class 'int'>

counter = "ten"             # reassigned to a string
print(counter)              # Output: ten
print(type(counter))        # Output: <class 'str'>


# ── SECTION 5: Multiple Assignment ───────────────
# Assign the same value to several variables at once.
x = y = z = 0
print(x, y, z)              # Output: 0 0 0

# Unpack multiple values in a single line (tuple unpacking).
first, second, third = "Python", 3.11, True
print(first)                # Output: Python
print(second)               # Output: 3.11
print(third)                # Output: True


# ── SECTION 6: The id() Function ─────────────────
# id() returns the unique memory address of an object.
# Two variables with the same small integer value often
# share the same address (Python caches small ints for speed).

a = 5
b = 5
print(id(a) == id(b))       # Output: True  (Python caches small ints)

big_a = 1000
big_b = 1000
print(id(big_a) == id(big_b))  # Output: False (large ints not cached)


# ── SECTION 7: String Basics ─────────────────────
# Strings can use single or double quotes — both are identical.
# Use triple quotes for multi-line strings.

greeting = "Hello, World!"
language = 'Python'
bio = """I am Berke.
I am a developer.
I love Python."""

print(greeting)             # Output: Hello, World!
print(language)             # Output: Python
print(bio)
# Output:
# I am Berke.
# I am a developer.
# I love Python.


# ── SECTION 8: f-Strings (Formatted String Literals) ──
# f-strings are the modern, readable way to embed variables
# inside strings. Prefix the string with f and use {} for expressions.

name = "Berke"
age = 25
language = "Python"

intro = f"Hi, I'm {name}. I'm {age} years old and I code in {language}."
print(intro)
# Output: Hi, I'm Berke. I'm 25 years old and I code in Python.

# Expressions inside {} are evaluated:
print(f"In 10 years I will be {age + 10} years old.")
# Output: In 10 years I will be 35 years old.


# ── QUICK REFERENCE ──────────────────────────────
# Data Types Summary:
#   int       → whole numbers           → age = 25
#   float     → decimal numbers         → price = 9.99
#   str       → text (in quotes)        → name = "Alice"
#   bool      → True or False           → active = True
#   NoneType  → absence of value        → result = None
#
# Useful built-ins:
#   type(x)   → returns the type of x
#   id(x)     → returns memory address of x
#   print(x)  → displays x in the terminal
#
# Naming (PEP 8):
#   variables/functions → snake_case
#   constants           → UPPER_SNAKE_CASE
#   classes             → PascalCase
#
# f-string syntax:
#   f"text {variable} text {expression}"
