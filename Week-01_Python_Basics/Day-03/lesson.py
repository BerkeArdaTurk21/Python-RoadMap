"""
================================================
Week 1 | Day 3 — Numbers & Math
================================================
Level       : Beginner
Topics      : int, float, arithmetic operators, operator precedence,
              integer division, modulo, built-in math functions,
              math module, type conversion, numeric literals
Goal        : Perform calculations confidently — understand every
              arithmetic operator, avoid common pitfalls, and use
              Python's math tools to solve real numerical problems
================================================
"""

# ── SECTION 1: Numeric Types ──────────────────
# Python has three built-in numeric types.
# You will use int and float daily; complex is rare.
#
#   int    — whole numbers, no decimal point, unlimited size
#   float  — numbers with a decimal point (IEEE 754 double precision)
#   complex— numbers with a real and imaginary part (e.g. 3+2j)

age      = 25               # int
price    = 19.99            # float
ratio    = 1 / 3            # float — any division produces a float
big_int  = 1_000_000        # int — underscores are just visual separators

print(type(age))            # Output: <class 'int'>
print(type(price))          # Output: <class 'float'>
print(type(ratio))          # Output: <class 'float'>
print(type(1 + 2j))         # Output: <class 'complex'>

# Scientific notation is valid float syntax.
speed_of_light = 3e8        # 300000000.0
electron_mass  = 9.11e-31   # 0.000000000000000000000000000000911
print(speed_of_light)       # Output: 300000000.0
print(electron_mass)        # Output: 9.11e-31


# ── SECTION 2: Arithmetic Operators ──────────
# Python supports seven arithmetic operators.
#
#   +    addition
#   -    subtraction
#   *    multiplication
#   /    true division   → always returns float
#   //   floor division  → rounds toward negative infinity
#   %    modulo          → remainder after floor division
#   **   exponentiation

a = 17
b = 5

print(a + b)                # Output: 22
print(a - b)                # Output: 12
print(a * b)                # Output: 85
print(a / b)                # Output: 3.4  (always float)
print(a // b)               # Output: 3    (floor division)
print(a % b)                # Output: 2    (remainder)
print(a ** b)               # Output: 1419857  (17 to the power of 5)

# True division always yields a float, even when the result is whole.
print(10 / 2)               # Output: 5.0  (not 5)
print(10 / 3)               # Output: 3.3333333333333335


# ── SECTION 3: Operator Precedence ───────────
# When multiple operators appear in one expression, Python evaluates
# them in this order (highest to lowest):
#
#   ()       Parentheses — always evaluated first
#   **       Exponentiation (right-to-left associativity)
#   +x  -x   Unary plus / minus
#   * / // % Multiplication, division, floor div, modulo (left-to-right)
#   + -      Addition, subtraction (left-to-right)
#
# Mnemonic: PEMDAS — Parentheses, Exponents, Multiply/Divide, Add/Subtract

print(2 + 3 * 4)            # Output: 14   (* before +)
print((2 + 3) * 4)          # Output: 20   (parens override)
print(2 ** 3 ** 2)          # Output: 512  (right-to-left: 3**2=9, then 2**9=512)
print(10 - 4 + 2)           # Output: 8    (left-to-right: 10-4=6, 6+2=8)
print(10 - (4 + 2))         # Output: 4    (parens change the result)

# Readable rule: when in doubt, add parentheses. They never hurt clarity.


# ── SECTION 4: Integer Division & Modulo ─────
# // (floor division) discards the fractional part by rounding toward
# negative infinity — NOT toward zero. This matters for negative numbers.

print(7 // 2)               # Output: 3    (7 / 2 = 3.5 → floor → 3)
print(-7 // 2)              # Output: -4   (-7 / 2 = -3.5 → floor → -4)
print(7 // -2)              # Output: -4

# % (modulo) gives the remainder consistent with floor division.
# The result always has the same sign as the divisor (b in a % b).

print(17 % 5)               # Output: 2    (17 = 3*5 + 2)
print(-17 % 5)              # Output: 3    (not -2 — sign follows the divisor)
print(17 % -5)              # Output: -3

# Practical uses of modulo:
# Check even / odd
print(10 % 2 == 0)          # Output: True   (even)
print(7 % 2 == 0)           # Output: False  (odd)

# Wrap a value around a range (clock arithmetic)
hour = 14
print(hour % 12)            # Output: 2     (2 PM on a 12-hour clock)

# Extract the last digit of a number
number = 12345
print(number % 10)          # Output: 5     (last digit)
print(number // 10 % 10)    # Output: 4     (second-to-last digit)


# ── SECTION 5: Built-in Math Functions ───────
# Python's builtins include useful numeric functions that need no import.

print(abs(-42))             # Output: 42    (absolute value)
print(abs(3.7))             # Output: 3.7

print(round(3.14159, 2))    # Output: 3.14  (round to 2 decimal places)
print(round(3.14159, 4))    # Output: 3.1416
print(round(2.5))           # Output: 2     (banker's rounding — rounds to even)
print(round(3.5))           # Output: 4

print(pow(2, 10))           # Output: 1024  (same as 2**10)
print(pow(2, 10, 1000))     # Output: 24    ((2**10) % 1000 — modular form)

print(min(3, 1, 4, 1, 5))   # Output: 1
print(max(3, 1, 4, 1, 5))   # Output: 5
print(sum([1, 2, 3, 4, 5])) # Output: 15

# divmod() returns (quotient, remainder) as a tuple in one call.
q, r = divmod(17, 5)
print(q, r)                 # Output: 3 2   (17 // 5 = 3, 17 % 5 = 2)


# ── SECTION 6: The math Module ────────────────
# The standard library's math module provides constants and
# functions for more advanced calculations.

import math

# Constants
print(math.pi)              # Output: 3.141592653589793
print(math.e)               # Output: 2.718281828459045
print(math.inf)             # Output: inf   (positive infinity)
print(math.tau)             # Output: 6.283185307179586  (2 * pi)

# Rounding variants
print(math.floor(3.9))      # Output: 3    (toward -infinity)
print(math.ceil(3.1))       # Output: 4    (toward +infinity)
print(math.trunc(3.9))      # Output: 3    (toward zero)
print(math.trunc(-3.9))     # Output: -3   (toward zero, not -4)

# Power and logarithms
print(math.sqrt(144))       # Output: 12.0
print(math.log(math.e))     # Output: 1.0  (natural logarithm)
print(math.log(100, 10))    # Output: 2.0  (log base 10)
print(math.log10(1000))     # Output: 3.0
print(math.log2(256))       # Output: 8.0

# Trigonometry (angles in radians)
print(math.sin(math.pi / 2))  # Output: 1.0
print(math.cos(0))            # Output: 1.0
print(math.degrees(math.pi))  # Output: 180.0
print(math.radians(90))       # Output: 1.5707963267948966

# Combinatorics & number theory
print(math.factorial(5))    # Output: 120   (5! = 5*4*3*2*1)
print(math.gcd(48, 18))     # Output: 6     (greatest common divisor)

# Predicates
print(math.isfinite(math.inf))   # Output: False
print(math.isnan(float("nan")))  # Output: True


# ── SECTION 7: Type Conversion ────────────────
# Convert between numeric types with int() and float().

print(int(3.9))             # Output: 3    (truncates — does NOT round)
print(int(-3.9))            # Output: -3   (truncates toward zero)
print(float(7))             # Output: 7.0

# Strings that look like numbers can be converted too.
print(int("42"))            # Output: 42
print(float("3.14"))        # Output: 3.14

# int() accepts a base argument for number-system conversions.
print(int("1010", 2))       # Output: 10   (binary  → decimal)
print(int("FF", 16))        # Output: 255  (hex     → decimal)
print(int("17", 8))         # Output: 15   (octal   → decimal)

# Going the other direction:
print(bin(10))              # Output: 0b1010
print(hex(255))             # Output: 0xff
print(oct(15))              # Output: 0o17

# Float arithmetic has limited precision — this is a property of
# IEEE 754, not a Python bug.
print(0.1 + 0.2)            # Output: 0.30000000000000004
print(round(0.1 + 0.2, 2))  # Output: 0.3


# ── SECTION 8: Augmented Assignment Operators ─
# Shorthand that reads "update this variable using itself".
#   +=  -=  *=  /=  //=  %=  **=

score = 100
score += 10                 # score = score + 10
print(score)                # Output: 110

score -= 5
print(score)                # Output: 105

score *= 2
print(score)                # Output: 210

score //= 3
print(score)                # Output: 70

score **= 2
print(score)                # Output: 4900

score %= 100
print(score)                # Output: 0


# ── QUICK REFERENCE ──────────────────────────
# Numeric types:
#   int   — whole number           42, -7, 0, 1_000_000
#   float — decimal / scientific   3.14, -0.5, 2e8, 9.11e-31
#
# Arithmetic operators:
#   +   addition
#   -   subtraction
#   *   multiplication
#   /   true division     → always float
#   //  floor division    → rounds toward -infinity
#   %   modulo            → remainder (sign matches divisor)
#   **  exponentiation
#
# Precedence (high → low):
#   ()  →  **  →  unary +/-  →  * / // %  →  + -
#
# Built-in functions:
#   abs(x)            absolute value
#   round(x, n)       round to n decimal places
#   pow(x, y)         x**y  (pow(x,y,mod) for modular form)
#   divmod(a, b)      (a//b, a%b) as a tuple
#   min(...)  max(...)  sum(...)
#
# math module highlights:
#   math.pi   math.e   math.inf   math.tau
#   math.floor(x)  math.ceil(x)  math.trunc(x)
#   math.sqrt(x)   math.log(x)   math.log10(x)  math.log2(x)
#   math.factorial(n)  math.gcd(a, b)
#   math.sin/cos/tan(radians)
#   math.degrees(r)  math.radians(d)
#
# Type conversion:
#   int(x)         truncates float or parses numeric string
#   float(x)       promotes int or parses numeric string
#   int(s, base)   parse string in given base (2, 8, 16 …)
#   bin(n) hex(n) oct(n)  → string representations
#
# Augmented assignment:
#   x += n   x -= n   x *= n   x /= n
#   x //= n  x %= n   x **= n
#
# Float precision note:
#   0.1 + 0.2 != 0.3 exactly — use round() or math.isclose() to compare
