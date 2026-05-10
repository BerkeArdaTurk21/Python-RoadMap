"""
================================================
Week 1 | Day 1 — Exercises
================================================
Instructions: Solve each exercise yourself.
              Do NOT open solutions.py until you have tried your best.
              Each exercise is a small runnable program — write real code.
================================================
"""

# ─────────────────────────────────────────
# Exercise 1 — Your Profile Card (Difficulty: Easy)
# ─────────────────────────────────────────
# Description: Build a small program that creates 5 variables describing
#   yourself and prints a formatted profile card using f-strings.
#
#   Variables to create:
#     full_name (str), age (int), height_m (float), is_student (bool), hobby (str)
#
#   Expected output:
#     ╔══════════════════════════╗
#     ║  Name    : Berke Turk   ║
#     ║  Age     : 25           ║
#     ║  Height  : 1.82 m       ║
#     ║  Student : False        ║
#     ║  Hobby   : Coding       ║
#     ╚══════════════════════════╝
#
# Write your solution below:


# ─────────────────────────────────────────
# Exercise 2 — Type Inspector (Difficulty: Easy)
# ─────────────────────────────────────────
# Description: Build a program that prints each value from the list below
#   alongside its type, using a single f-string per line.
#
#   values = [42, 3.14, "hello", True, None, "123", 0]
#
#   Expected output:
#     Value: 42         | Type: <class 'int'>
#     Value: 3.14       | Type: <class 'float'>
#     Value: hello      | Type: <class 'str'>
#     Value: True       | Type: <class 'bool'>
#     Value: None       | Type: <class 'NoneType'>
#     Value: 123        | Type: <class 'str'>
#     Value: 0          | Type: <class 'int'>
#
# Write your solution below:


# ─────────────────────────────────────────
# Exercise 3 — Swap Without a Temp Variable (Difficulty: Medium)
# ─────────────────────────────────────────
# Description: Start with a = "morning" and b = "evening". Swap their values
#   in ONE line of Python (no temp variable). Print before and after.
#
#   Expected output:
#     Before: a=morning, b=evening
#     After : a=evening, b=morning
#
# Write your solution below:


# ─────────────────────────────────────────
# Exercise 4 — Memory Address Detective (Difficulty: Medium)
# ─────────────────────────────────────────
# Description: Check which pairs of variables share the same memory address
#   using id(). Print "SAME" or "DIFFERENT" for each pair.
#
#   Pairs to check:
#     p = 100  q = 100
#     m = 257  n = 257
#     s = "hi" t = "hi"
#
#   Expected output (typical CPython):
#     p=100, q=100 : SAME
#     m=257, n=257 : DIFFERENT
#     s="hi",t="hi": SAME
#
# Write your solution below:


# ─────────────────────────────────────────
# Exercise 5 — Constants & PEP 8 Refactor (Difficulty: Hard)
# ─────────────────────────────────────────
# Description: The code below works but violates PEP 8 naming conventions.
#   Rewrite it with proper names and print a formatted summary.
#
#   Original (bad style):
#     MaxSpeed = 300
#     minspeed = 0
#     CurrentSpeed = 150
#     SpeedUnit = "km/h"
#     IS_moving = True
#
#   Rules:
#     MaxSpeed, minspeed → constants → UPPER_SNAKE_CASE
#     CurrentSpeed, SpeedUnit, IS_moving → variables → snake_case
#
#   Expected output:
#     Speed: 150 km/h | Moving: True | Range: 0–300 km/h
#
# Write your solution below:
