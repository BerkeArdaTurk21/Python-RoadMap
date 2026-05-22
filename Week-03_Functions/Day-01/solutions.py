# Week 3 - Day 1: Defining Functions — Solutions

import math

# ─────────────────────────────────────────────
# Solution 1: Temperature Converter
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15

def convert_all(celsius):
    """Print a full temperature conversion report."""
    f = celsius_to_fahrenheit(celsius)
    k = celsius_to_kelvin(celsius)
    print(f"{celsius}°C = {f:.2f}°F")
    print(f"{celsius}°C = {k:.2f}K")
    print(f"{f:.0f}°F = {fahrenheit_to_celsius(f):.2f}°C")

convert_all(100)


# ─────────────────────────────────────────────
# Solution 2: String Utilities
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")

def count_vowels(text):
    """Count vowels in text (case-insensitive)."""
    return sum(1 for ch in text.lower() if ch in "aeiou")

def is_palindrome(text):
    """Return True if text is a palindrome (ignores spaces and case)."""
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

def title_case(text):
    """Capitalise the first letter of each word."""
    return " ".join(word.capitalize() for word in text.split())

def reverse_words(text):
    """Reverse the order of words in a sentence."""
    return " ".join(text.split()[::-1])

print(count_vowels("Hello World"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("A man a plan a canal Panama"))
print(title_case("hello world"))
print(reverse_words("I love Python"))


# ─────────────────────────────────────────────
# Solution 3: Math Toolkit
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Return n! using a loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def gcd(a, b):
    """Return the Greatest Common Divisor of a and b."""
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def is_perfect(n):
    """Return True if n equals the sum of its proper divisors."""
    if n < 2:
        return False
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

print(is_prime(7))
print(is_prime(10))
print(factorial(5))
print(gcd(48, 18))
print(is_perfect(6))
print(is_perfect(28))
print(is_perfect(12))


# ─────────────────────────────────────────────
# Solution 4: Grade Calculator
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")

def average(scores):
    """Return the mean of a list of numbers."""
    return sum(scores) / len(scores)

def letter_grade(avg):
    """Return letter grade for a numeric average."""
    if avg >= 90:   return "A"
    elif avg >= 80: return "B"
    elif avg >= 70: return "C"
    elif avg >= 60: return "D"
    else:           return "F"

def passed(avg, minimum=50):
    """Return True if avg meets the minimum passing score."""
    return avg >= minimum

def student_report(name, scores):
    """Print a formatted student grade report."""
    avg    = average(scores)
    grade  = letter_grade(avg)
    status = "PASSED" if passed(avg) else "FAILED"
    scores_str = ", ".join(str(s) for s in scores)
    print("── Student Report ──")
    print(f"Name    : {name}")
    print(f"Scores  : {scores_str}")
    print(f"Average : {avg:.1f}")
    print(f"Grade   : {grade}")
    print(f"Status  : {status}")

student_report("Alice", [88, 92, 75, 95])


# ─────────────────────────────────────────────
# Solution 5: Shape Calculator
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")

def circle_area(r):
    """Return the area of a circle with radius r."""
    return math.pi * r ** 2

def circle_perimeter(r):
    """Return the circumference of a circle with radius r."""
    return 2 * math.pi * r

def rectangle_area(w, h):
    """Return the area of a rectangle."""
    return w * h

def rectangle_perimeter(w, h):
    """Return the perimeter of a rectangle."""
    return 2 * (w + h)

def triangle_area(b, h):
    """Return the area of a triangle with base b and height h."""
    return 0.5 * b * h

def triangle_perimeter(a, b, c):
    """Return the perimeter of a triangle with sides a, b, c."""
    return a + b + c

def shape_report(shape, *dims):
    """Print area and perimeter for the given shape and dimensions."""
    match shape:
        case "circle":
            r = dims[0]
            print(f"Circle r={r}: area={circle_area(r):.2f}, perimeter={circle_perimeter(r):.2f}")
        case "rectangle":
            w, h = dims[0], dims[1]
            print(f"Rectangle {w}×{h}: area={rectangle_area(w,h)}, perimeter={rectangle_perimeter(w,h)}")
        case "triangle":
            b, h, a, c = dims[0], dims[1], dims[0], dims[2]
            print(f"Triangle: area={triangle_area(b,h)}, perimeter={triangle_perimeter(a,dims[1],c)}")
        case _:
            print(f"Unknown shape: {shape}")

shape_report("circle", 5)
shape_report("rectangle", 4, 6)
shape_report("triangle", 3, 4, 5)
