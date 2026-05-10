"""
================================================
Week 1 | Day 1 — Solutions
================================================
Only open this after you've genuinely tried exercises.py!
================================================
"""

# ═══════════════════════════════════════════════════
# Exercise 1 — Your Profile Card Solution
# ═══════════════════════════════════════════════════
# Explanation: Store each value in a descriptively named variable, then use
# f-strings with the < alignment specifier to pad every field to a fixed width
# so the right-side border lines up perfectly.
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


# ═══════════════════════════════════════════════════
# Exercise 2 — Type Inspector Solution
# ═══════════════════════════════════════════════════
# Explanation: Iterate the list and call type() on each element inside the
# f-string. Using str(v) as the display value ensures None prints as "None"
# rather than being silently skipped. :<10 left-aligns the value in a 10-char
# field so all Type columns align vertically.
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


# ═══════════════════════════════════════════════════
# Exercise 3 — Swap Without a Temp Variable Solution
# ═══════════════════════════════════════════════════
# Explanation: Python evaluates the entire right-hand side of an assignment
# before doing any binding. So a, b = b, a packs the current values of b and a
# into a tuple first, then unpacks them in order — a clean one-line swap.
a = "morning"
b = "evening"
print(f"Before: a={a}, b={b}")

a, b = b, a

print(f"After : a={a}, b={b}")
# Output:
# Before: a=morning, b=evening
# After : a=evening, b=morning


# ═══════════════════════════════════════════════════
# Exercise 4 — Memory Address Detective Solution
# ═══════════════════════════════════════════════════
# Explanation: CPython caches small integers (-5 to 256) and interned short
# strings, so identical small ints and simple string literals share addresses.
# Integers outside that range (like 257) are not cached — each assignment
# creates a fresh object, so id() values differ.
p = 100;  q = 100
m = 257;  n = 257
s = "hi"; t = "hi"

print("p=100, q=100 :", "SAME" if id(p) == id(q) else "DIFFERENT")
print("m=257, n=257 :", "SAME" if id(m) == id(n) else "DIFFERENT")
print('s="hi",t="hi":', "SAME" if id(s) == id(t) else "DIFFERENT")
# Output (typical CPython):
# p=100, q=100 : SAME
# m=257, n=257 : DIFFERENT
# s="hi",t="hi": SAME


# ═══════════════════════════════════════════════════
# Exercise 5 — Constants & PEP 8 Refactor Solution
# ═══════════════════════════════════════════════════
# Explanation: PEP 8 reserves UPPER_SNAKE_CASE for module-level constants
# (values that never change at runtime) and snake_case for regular variables.
# Renaming makes the intent immediately clear to any reader of the code.
MAX_SPEED = 300         # constant — UPPER_SNAKE_CASE
MIN_SPEED = 0           # constant — UPPER_SNAKE_CASE
current_speed = 150
speed_unit = "km/h"
is_moving = True

print(
    f"Speed: {current_speed} {speed_unit} | "
    f"Moving: {is_moving} | "
    f"Range: {MIN_SPEED}–{MAX_SPEED} {speed_unit}"
)
# Output:
# Speed: 150 km/h | Moving: True | Range: 0–300 km/h
