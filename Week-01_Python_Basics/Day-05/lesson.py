"""
================================================
Week 1 | Day 5 — Operators & Expressions
================================================
Level       : Beginner
Topics      : comparison operators, logical operators,
              identity operators, membership operators,
              bitwise operators, augmented assignment,
              ternary expressions, operator precedence
Goal        : Master every operator Python provides,
              understand evaluation order, and write
              concise expressive conditions
================================================
"""


# ── SECTION 1: Comparison Operators ──────────────────
# Comparison operators compare two values and always return a bool (True/False).
#
#   ==   equal to
#   !=   not equal to
#   <    less than
#   >    greater than
#   <=   less than or equal to
#   >=   greater than or equal to

x = 10
y = 3

print(x == 10)          # Output: True
print(x != y)           # Output: True
print(x > y)            # Output: True
print(x < y)            # Output: False
print(x >= 10)          # Output: True
print(x <= 9)           # Output: False

# Python compares int and float by value — no type mismatch error.
print(3 == 3.0)         # Output: True   (same numeric value)
print(3 != 3.0)         # Output: False

# Strings are compared lexicographically (alphabetical order).
print("apple" < "banana")   # Output: True  ('a' comes before 'b')
print("Z" < "a")            # Output: True  (uppercase letters have smaller codes)

# CHAINED COMPARISONS — unique to Python, very readable.
# 0 < x < 100 is equivalent to (0 < x) and (x < 100).
age = 25
print(18 <= age < 65)   # Output: True   (adult working age)
print(0 < age < 18)     # Output: False  (not a minor)

score = 75
print(60 <= score <= 79)    # Output: True   (C grade range)


# ── SECTION 2: Logical Operators ─────────────────────
# Combine boolean conditions with and, or, not.
#
#   and  — True only if BOTH sides are True
#   or   — True if AT LEAST ONE side is True
#   not  — inverts a boolean

has_ticket = True
is_adult   = True
is_vip     = False

print(has_ticket and is_adult)      # Output: True   (both True)
print(has_ticket and is_vip)        # Output: False  (one False)
print(is_vip or is_adult)           # Output: True   (one True)
print(not is_vip)                   # Output: True   (inverts False)
print(not has_ticket)               # Output: False  (inverts True)

# SHORT-CIRCUIT EVALUATION:
# and stops at the FIRST falsy value and returns it.
# or  stops at the FIRST truthy value and returns it.
# Neither evaluates the right side if it's not needed.

print(0 and "hello")        # Output: 0       (0 is falsy → return it, skip "hello")
print(5 and "hello")        # Output: hello   (5 is truthy → evaluate and return "hello")
print(0 or "hello")         # Output: hello   (0 is falsy → check next → "hello" is truthy)
print("hi" or "hello")      # Output: hi      ("hi" is truthy → return it, skip "hello")
print(False or 0 or "")     # Output:         (all falsy → returns last value "")

# PRACTICAL USE of short-circuit:
# Provide a default value when a variable might be empty.
username = ""
display  = username or "Anonymous"
print(display)              # Output: Anonymous  (username is falsy, so "Anonymous" is used)

username = "Berke"
display  = username or "Anonymous"
print(display)              # Output: Berke      (username is truthy, returned immediately)

# not ALWAYS returns a bool (True or False), unlike and/or.
print(not 0)                # Output: True
print(not "hello")          # Output: False
print(type(not 0))          # Output: <class 'bool'>


# ── SECTION 3: Identity Operators ────────────────────
# is   — True if both variables point to the SAME object in memory
# is not — True if they point to DIFFERENT objects
#
# == compares VALUES.  is compares IDENTITY (memory address).

a = [1, 2, 3]
b = [1, 2, 3]
c = a               # c points to the same list object as a

print(a == b)       # Output: True   (same content)
print(a is b)       # Output: False  (different objects in memory)
print(a is c)       # Output: True   (same object — c is just another name for a)
print(a is not b)   # Output: True

# The ONLY correct use of is: checking against None, True, False.
# These are singletons — Python guarantees there is only one of each.

value = None
print(value is None)        # Output: True   ← correct idiom
print(value == None)        # Output: True   (works, but PEP 8 says use 'is')

# WARNING: never use is to compare integers or strings in general.
# Python caches small ints (-5 to 256) and some strings, but this is
# an implementation detail you should never rely on.
x = 1000
y = 1000
print(x == y)       # Output: True   (always correct — use this)
print(x is y)       # Output: False  (may vary — don't use is for numbers)


# ── SECTION 4: Membership Operators ──────────────────
# in     — True if the left value is found in the right collection
# not in — True if the left value is NOT found

# Works on strings (substring check):
text = "Hello, Python!"
print("Python" in text)     # Output: True
print("Java" in text)       # Output: False
print("java" not in text)   # Output: True   (case-sensitive)

# Works on lists:
primes = [2, 3, 5, 7, 11]
print(5 in primes)          # Output: True
print(4 in primes)          # Output: False
print(4 not in primes)      # Output: True

# Works on tuples and sets:
vowels = ("a", "e", "i", "o", "u")
print("e" in vowels)        # Output: True

# Works on dict KEYS (not values):
scores = {"Alice": 95, "Bob": 80}
print("Alice" in scores)    # Output: True   (checks keys)
print(95 in scores)         # Output: False  (95 is a value, not a key)
print(95 in scores.values())# Output: True   (check values explicitly)


# ── SECTION 5: Bitwise Operators ─────────────────────
# Bitwise operators work on the binary (bit-level) representation of integers.
#
#   &   AND  — 1 only where BOTH bits are 1
#   |   OR   — 1 where AT LEAST ONE bit is 1
#   ^   XOR  — 1 only where bits DIFFER
#   ~   NOT  — flips every bit (result = -(n + 1))
#   <<  left shift  — shift bits left (multiply by 2 per shift)
#   >>  right shift — shift bits right (floor-divide by 2 per shift)

a = 0b1010      # decimal 10  (binary: 1010)
b = 0b1100      # decimal 12  (binary: 1100)

print(bin(a & b))   # Output: 0b1000  (8)  — only bit 3 is 1 in both
print(bin(a | b))   # Output: 0b1110  (14) — bits set in either
print(bin(a ^ b))   # Output: 0b0110  (6)  — bits that differ
print(~a)           # Output: -11     — flips all bits: -(10 + 1)

print(a << 1)       # Output: 20  — shift left 1 = multiply by 2
print(a << 2)       # Output: 40  — shift left 2 = multiply by 4
print(a >> 1)       # Output: 5   — shift right 1 = floor-divide by 2

# PRACTICAL: permission flags (used in file systems, APIs, game logic)
READ    = 0b001     # 1
WRITE   = 0b010     # 2
EXECUTE = 0b100     # 4

user_perms = READ | WRITE       # 0b011 = 3  (has read + write)

print(bool(user_perms & READ))      # Output: True   (can read)
print(bool(user_perms & WRITE))     # Output: True   (can write)
print(bool(user_perms & EXECUTE))   # Output: False  (cannot execute)

# Grant execute permission:
user_perms |= EXECUTE
print(bool(user_perms & EXECUTE))   # Output: True   (now can execute)

# Revoke write permission:
user_perms &= ~WRITE
print(bool(user_perms & WRITE))     # Output: False  (write revoked)


# ── SECTION 6: Augmented Assignment Operators ─────────
# All augmented operators update a variable using itself.
# Arithmetic: +=  -=  *=  /=  //=  %=  **=  (covered in Day 3)
# Bitwise:    &=  |=  ^=  <<=  >>=

flags = 0b0000
flags |= 0b0001     # set bit 0  →  0b0001
flags |= 0b0100     # set bit 2  →  0b0101
print(bin(flags))   # Output: 0b101

flags &= ~0b0001    # clear bit 0 →  0b0100
print(bin(flags))   # Output: 0b100

flags ^= 0b1111     # toggle all 4 bits  →  0b1011
print(bin(flags))   # Output: 0b1011

flags <<= 2         # shift left 2  →  0b101100
print(bin(flags))   # Output: 0b101100

flags >>= 3         # shift right 3 →  0b101
print(bin(flags))   # Output: 0b101

# All augmented assignment operators — quick demo:
n = 20
n +=  5 ;  print(n)    # Output: 25   (n = n + 5)
n -=  3 ;  print(n)    # Output: 22   (n = n - 3)
n *=  2 ;  print(n)    # Output: 44   (n = n * 2)
n //= 3 ;  print(n)    # Output: 14   (n = n // 3)
n %=  4 ;  print(n)    # Output: 2    (n = n % 4)
n **= 3 ;  print(n)    # Output: 8    (n = n ** 3)


# ── SECTION 7: Ternary / Conditional Expression ───────
# A one-line if/else that evaluates to a value.
# Syntax: value_if_true if condition else value_if_false

score = 72
result = "Pass" if score >= 60 else "Fail"
print(result)           # Output: Pass

age = 17
label = "Adult" if age >= 18 else "Minor"
print(label)            # Output: Minor

# Ternary works anywhere a value is expected:
speed = 120
status_msg = f"Speed: {speed} — {'OK' if speed <= 110 else 'TOO FAST'}"
print(status_msg)       # Output: Speed: 120 — TOO FAST

# Compute absolute value without abs():
x = -42
abs_x = x if x >= 0 else -x
print(abs_x)            # Output: 42

# Nested ternary — use sparingly (can hurt readability):
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade)            # Output: B

# Providing a default when a value might be None:
value = None
safe = value if value is not None else "default"
print(safe)             # Output: default

value = 42
safe = value if value is not None else "default"
print(safe)             # Output: 42


# ── SECTION 8: Operator Precedence ───────────────────
# When multiple operators appear in one expression, Python evaluates
# them in this order (highest → lowest priority):
#
#   1. ()                  Parentheses
#   2. **                  Exponentiation (right-to-left)
#   3. +x  -x  ~x          Unary plus, minus, bitwise NOT
#   4. *  /  //  %         Multiplication, division, floor, modulo
#   5. +  -                Addition, subtraction
#   6. <<  >>              Bitwise shifts
#   7. &                   Bitwise AND
#   8. ^                   Bitwise XOR
#   9. |                   Bitwise OR
#  10. ==  !=  <  >  <=  >= is  is not  in  not in   Comparisons
#  11. not                 Logical NOT
#  12. and                 Logical AND
#  13. or                  Logical OR

# Tricky examples:
print(2 + 3 * 4)            # Output: 14   (* before +)
print(True or False and False)  # Output: True  (and before or)
print(not True or False)    # Output: False ((not True)=False, False or False)
print(not (True or False))  # Output: False (parens first: True, then not)

print(5 > 3 and 10 < 20)   # Output: True  (comparisons before and)
print(1 + 1 == 2)           # Output: True  (+ before ==)

# Comparison operators chain without and in Python:
x = 5
print(1 < x < 10)          # Output: True   (Pythonic range check)
print(1 < x and x < 10)    # Output: True   (same result, more verbose)

# Rule of thumb: when in doubt, use parentheses — they always override.
print((2 + 3) * 4)          # Output: 20    (parens change order)
print(not (5 > 3 and 10 < 5))  # Output: True


# ── QUICK REFERENCE ──────────────────────────────────
# Comparison:  ==  !=  <  >  <=  >=     → always returns bool
#   Chaining:  0 < x < 100             → Pythonic range check
#
# Logical:     and   or   not
#   Short-circuit: and returns first falsy; or returns first truthy
#   Default value: result = value or "fallback"
#
# Identity:    is   is not
#   Correct use: x is None  |  x is not None
#
# Membership:  in   not in
#   Works on: str (substring), list, tuple, set, dict keys
#
# Bitwise:     &  |  ^  ~  <<  >>
#   &   AND — both bits must be 1
#   |   OR  — at least one bit is 1
#   ^   XOR — bits must differ
#   ~   NOT — -(n+1)
#   <<  left shift  = multiply by 2^n
#   >>  right shift = floor-divide by 2^n
#   Permission pattern: perm |= FLAG   perm &= ~FLAG   bool(perm & FLAG)
#
# Augmented assignment: +=  -=  *=  /=  //=  %=  **=  &=  |=  ^=  <<=  >>=
#
# Ternary: value_if_true if condition else value_if_false
#
# Precedence (high → low):
#   ()  **  unary  * / // %  + -  << >>  &  ^  |  comparisons  not  and  or
