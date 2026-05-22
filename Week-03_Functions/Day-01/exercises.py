# Week 3 - Day 1: Defining Functions — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: Temperature Converter
# ─────────────────────────────────────────────
# Write THREE functions:
#   celsius_to_fahrenheit(c)  → returns c * 9/5 + 32
#   fahrenheit_to_celsius(f)  → returns (f - 32) * 5/9
#   celsius_to_kelvin(c)      → returns c + 273.15
#
# Then write a fourth function: convert_all(celsius)
# that calls all three and prints a full report.
#
# Expected output for convert_all(100):
#   100°C = 212.00°F
#   100°C = 373.15K
#   212°F = 100.00°C


# ─────────────────────────────────────────────
# Exercise 2: String Utilities
# ─────────────────────────────────────────────
# Write these four functions (no built-in shortcuts):
#   count_vowels(text)    → count a,e,i,o,u (case-insensitive)
#   is_palindrome(text)   → True if text reads same forwards/backwards
#                           (ignore spaces, case-insensitive)
#   title_case(text)      → capitalise first letter of each word
#   reverse_words(text)   → reverse the ORDER of words in the sentence
#
# Expected output:
#   count_vowels("Hello World")    → 3
#   is_palindrome("racecar")       → True
#   is_palindrome("hello")         → False
#   is_palindrome("A man a plan a canal Panama") → True
#   title_case("hello world")      → Hello World
#   reverse_words("I love Python") → Python love I


# ─────────────────────────────────────────────
# Exercise 3: Math Toolkit
# ─────────────────────────────────────────────
# Write these functions with docstrings:
#   is_prime(n)       → True if n is prime, False otherwise
#   factorial(n)      → n! using a loop (not recursion yet)
#   gcd(a, b)         → Greatest Common Divisor using subtraction loop
#   is_perfect(n)     → True if sum of proper divisors equals n
#                       (e.g. 6: 1+2+3=6 → True)
#
# Expected output:
#   is_prime(7)     → True
#   is_prime(10)    → False
#   factorial(5)    → 120
#   gcd(48, 18)     → 6
#   is_perfect(6)   → True
#   is_perfect(28)  → True
#   is_perfect(12)  → False


# ─────────────────────────────────────────────
# Exercise 4: Grade Calculator
# ─────────────────────────────────────────────
# Write these functions:
#   average(scores)         → returns the mean of a list of numbers
#   letter_grade(avg)       → returns A/B/C/D/F based on avg
#   passed(avg, minimum=50) → True if avg >= minimum
#   student_report(name, scores) → prints a formatted report
#
# Expected output for student_report("Alice", [88, 92, 75, 95]):
#   ── Student Report ──
#   Name    : Alice
#   Scores  : 88, 92, 75, 95
#   Average : 87.5
#   Grade   : B
#   Status  : PASSED


# ─────────────────────────────────────────────
# Exercise 5: Shape Calculator
# ─────────────────────────────────────────────
# Write area and perimeter functions for three shapes.
# All functions must have docstrings.
#
#   circle_area(r)          → π * r²
#   circle_perimeter(r)     → 2 * π * r
#   rectangle_area(w, h)    → w * h
#   rectangle_perimeter(w, h) → 2 * (w + h)
#   triangle_area(b, h)     → 0.5 * b * h
#   triangle_perimeter(a, b, c) → a + b + c
#
# Then write shape_report(shape, *dims) that calls the right
# functions and prints area + perimeter.
#
# Expected output:
#   shape_report("circle", 5)
#     Circle r=5: area=78.54, perimeter=31.42
#
#   shape_report("rectangle", 4, 6)
#     Rectangle 4×6: area=24, perimeter=20
#
#   shape_report("triangle", 3, 4, 5)  (base=3, height=4, sides=3,4,5)
#     Triangle: area=6.0, perimeter=12
