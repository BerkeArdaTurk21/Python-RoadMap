"""
================================================
Week 1 | Day 1 — Exercises & Mini Quiz
================================================
Instructions: Try to solve each exercise before looking at the solution.
              Cover the Solution block, write your own code, then compare.
================================================
"""

# ══ MINI QUIZ (Multiple Choice) ══════════════════════════════════════════════

# Q1: What is the output of: print(type(3.14))
# A) <class 'int'>
# B) <class 'float'>
# C) <class 'str'>
# D) <class 'number'>
# Answer: B — 3.14 has a decimal point, so Python classifies it as float.

# Q2: Which variable name is valid in Python?
# A) 2fast
# B) fast-car
# C) fast_car
# D) class
# Answer: C — snake_case with only letters and underscores is valid.
#             A starts with a digit, B uses a hyphen (minus operator), D is a keyword.

# Q3: What does id(x) return?
# A) The index of x in a list
# B) The data type of x
# C) The unique memory address of the object x points to
# D) The length of x
# Answer: C — id() returns the integer memory address of the object in CPython.

# Q4: Which of the following correctly creates a multi-line string?
# A) name = "line1 \n line2"
# B) name = """line1
#    line2"""
# C) name = 'line1' + 'line2'
# D) Both A and B
# Answer: D — \n inserts a newline character; triple quotes span actual lines.

# Q5: What is the output of:
#     x = y = 5
#     y = 10
#     print(x)
# A) 10
# B) 5
# C) None
# D) Error
# Answer: B — x = y = 5 makes both point to 5. Reassigning y to 10 doesn't
#             affect x. Integers are immutable; x still points to the 5 object.


# ══ CODING EXERCISES ═════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# Exercise 1 — Your Profile Card  (Difficulty: Easy)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   Create 5 variables that describe yourself:
#     - full_name (str)
#     - age (int)
#     - height_m (float)  — in meters
#     - is_student (bool)
#     - hobby (str)
#   Then print a formatted profile card using an f-string that looks like:
#
#   ╔══════════════════════════╗
#   ║  Name    : Berke Turk   ║
#   ║  Age     : 25           ║
#   ║  Height  : 1.82 m       ║
#   ║  Student : False        ║
#   ║  Hobby   : Coding       ║
#   ╚══════════════════════════╝

# Solution:
full_name = "Berke Turk"
age = 25
height_m = 1.82
is_student = False
hobby = "Coding"

print("╔══════════════════════════╗")
print(f"║  Name    : {full_name:<15}║")
print(f"║  Age     : {age:<15}║")
print(f"║  Height  : {height_m} m{'':<11}║")
print(f"║  Student : {is_student:<15}║")
print(f"║  Hobby   : {hobby:<15}║")
print("╚══════════════════════════╝")
# Output:
# ╔══════════════════════════╗
# ║  Name    : Berke Turk   ║
# ║  Age     : 25           ║
# ║  Height  : 1.82 m       ║
# ║  Student : False        ║
# ║  Hobby   : Coding       ║
# ╚══════════════════════════╝


# ─────────────────────────────────────────────────────────────────────────────
# Exercise 2 — Type Inspector  (Difficulty: Easy)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   Given the list of values below, print each value alongside its type
#   using a single f-string per line. Expected format:
#     Value: 42        | Type: <class 'int'>
#     Value: 3.14      | Type: <class 'float'>
#     ... etc.

# Solution:
values = [42, 3.14, "hello", True, None, "123", 0]

for v in values:
    print(f"Value: {str(v):<10} | Type: {type(v)}")
# Output:
# Value: 42         | Type: <class 'int'>
# Value: 3.14       | Type: <class 'float'>
# Value: hello      | Type: <class 'str'>
# Value: True       | Type: <class 'bool'>
# Value: None       | Type: <class 'NoneType'>
# Value: 123        | Type: <class 'str'>
# Value: 0          | Type: <class 'int'>


# ─────────────────────────────────────────────────────────────────────────────
# Exercise 3 — Swap Without a Temp Variable  (Difficulty: Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   Start with:   a = "morning"   b = "evening"
#   Swap their values in ONE line of Python (no temp variable).
#   Then print:
#     Before: a=morning, b=evening
#     After : a=evening, b=morning

# Solution:
a = "morning"
b = "evening"
print(f"Before: a={a}, b={b}")

a, b = b, a     # Python evaluates the right side fully before assigning

print(f"After : a={a}, b={b}")
# Output:
# Before: a=morning, b=evening
# After : a=evening, b=morning


# ─────────────────────────────────────────────────────────────────────────────
# Exercise 4 — Memory Address Detective  (Difficulty: Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   Python caches small integers (-5 to 256) to save memory.
#   Predict and verify which pairs share the same memory address.
#   Print "SAME" or "DIFFERENT" for each pair.
#
#   Pairs to check:
#     p = 100  q = 100
#     m = 257  n = 257
#     s = "hi" t = "hi"

# Solution:
p = 100;  q = 100
m = 257;  n = 257
s = "hi"; t = "hi"

print("p=100, q=100 :", "SAME" if id(p) == id(q) else "DIFFERENT")
print("m=257, n=257 :", "SAME" if id(m) == id(n) else "DIFFERENT")
print('s="hi",t="hi":', "SAME" if id(s) == id(t) else "DIFFERENT")
# Typical CPython output:
# p=100, q=100 : SAME       (cached small int)
# m=257, n=257 : DIFFERENT  (outside cache range)
# s="hi",t="hi": SAME       (string interning for short literals)


# ─────────────────────────────────────────────────────────────────────────────
# Exercise 5 — Constants & PEP 8 Refactor  (Difficulty: Hard)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   The code below works but violates PEP 8 naming conventions.
#   Rewrite it with proper names and add a formatted summary print.
#
#   Original (bad style):
#     MaxSpeed = 300
#     minspeed = 0
#     CurrentSpeed = 150
#     SpeedUnit = "km/h"
#     IS_moving = True
#
#   Rules:
#     - MaxSpeed and minspeed are constants → UPPER_SNAKE_CASE
#     - CurrentSpeed → snake_case
#     - SpeedUnit → snake_case
#     - IS_moving → snake_case
#   Print:  "Speed: 150 km/h | Moving: True | Range: 0–300 km/h"

# Solution:
MAX_SPEED = 300         # constant
MIN_SPEED = 0           # constant
current_speed = 150
speed_unit = "km/h"
is_moving = True

print(
    f"Speed: {current_speed} {speed_unit} | "
    f"Moving: {is_moving} | "
    f"Range: {MIN_SPEED}–{MAX_SPEED} {speed_unit}"
)
# Output: Speed: 150 km/h | Moving: True | Range: 0–300 km/h
