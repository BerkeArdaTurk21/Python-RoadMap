"""
================================================
Week 1 | Day 2 — Exercises & Mini Quiz
================================================
Instructions: Try to solve each exercise before looking at the solution.
              Cover the Solution block, write your own code, then compare.
================================================
"""

# ══ MINI QUIZ (Multiple Choice) ══════════════════════════════════════════════

# Q1: What is the output of: "Python"[1:4]
# A) "Pyt"
# B) "yth"
# C) "ytho"
# D) "ython"
# Answer: B — slicing is start-inclusive, stop-exclusive.
#             Indices 1, 2, 3 → characters 'y', 't', 'h' → "yth".

# Q2: What does "  hello  ".strip() return?
# A) "hello  "
# B) "  hello"
# C) "hello"
# D) "  hello  "
# Answer: C — strip() removes all leading and trailing whitespace.
#             lstrip() removes only the left; rstrip() removes only the right.

# Q3: What does "banana".find("x") return?
# A) 0
# B) False
# C) ValueError
# D) -1
# Answer: D — find() returns -1 when the substring is not found.
#             index() would raise ValueError; find() is the safe alternative.

# Q4: What is the output of: "abc"[::-1]
# A) "abc"
# B) "acb"
# C) "cba"
# D) "bca"
# Answer: C — a step of -1 reverses the sequence. Start defaults to the last
#             character, stop defaults to before the first, stepping backwards.

# Q5: What is the output of: f"{'hi':*^6}"
# A) "hi****"
# B) "****hi"
# C) "**hi**"
# D) "hi    "
# Answer: C — *^6 means: center in a field of width 6, fill empty space with *.
#             "hi" is 2 chars; 4 padding chars split evenly → ** on each side.


# ══ CODING EXERCISES ═════════════════════════════════════════════════════════

# ─────────────────────────────────────────────────────────────────────────────
# Exercise 1 — String Slicer  (Difficulty: Easy)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   Given the string below, use slicing (no methods) to extract and print:
#     1. The first 5 characters
#     2. The last 6 characters
#     3. Every 2nd character from the full string
#     4. The entire string reversed
#
#   message = "Hello, World!"
#
#   Expected output:
#     First 5  : Hello
#     Last 6   : World!
#     Every 2nd: Hlo ol!
#     Reversed : !dlroW ,olleH

# Solution:
message = "Hello, World!"

print(f"First 5  : {message[:5]}")
print(f"Last 6   : {message[-6:]}")
print(f"Every 2nd: {message[::2]}")
print(f"Reversed : {message[::-1]}")
# Output:
# First 5  : Hello
# Last 6   : orld!
# Every 2nd: Hlo ol!
# Reversed : !dlroW ,olleH


# ─────────────────────────────────────────────────────────────────────────────
# Exercise 2 — Text Normalizer  (Difficulty: Easy)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   User input is messy — mixed case and extra whitespace.
#   Clean it up using string methods and print the result.
#
#   raw = "  pYtHoN pRoGrAmMiNg  "
#
#   Steps:
#     1. Strip leading/trailing whitespace
#     2. Convert to title case
#     3. Count how many words are in the cleaned string
#     4. Print formatted output:
#
#   Expected output:
#     Cleaned  : Python Programming
#     Words    : 2
#     Length   : 18

# Solution:
raw = "  pYtHoN pRoGrAmMiNg  "

cleaned = raw.strip().title()
word_count = len(cleaned.split())

print(f"Cleaned  : {cleaned}")
print(f"Words    : {word_count}")
print(f"Length   : {len(cleaned)}")
# Output:
# Cleaned  : Python Programming
# Words    : 2
# Length   : 18


# ─────────────────────────────────────────────────────────────────────────────
# Exercise 3 — Initials Generator  (Difficulty: Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   Given a full name (possibly in any case), generate the initials.
#
#   full_name = "berke can turk"
#
#   Rules:
#     - Split the name into words
#     - Take the first character of each word
#     - Uppercase each initial
#     - Join them with dots and add a trailing dot
#
#   Expected output:
#     Full name : Berke Can Turk
#     Initials  : B.C.T.

# Solution:
full_name = "berke can turk"

parts = full_name.split()
initials = ".".join(word[0].upper() for word in parts) + "."
formatted_name = full_name.title()

print(f"Full name : {formatted_name}")
print(f"Initials  : {initials}")
# Output:
# Full name : Berke Can Turk
# Initials  : B.C.T.


# ─────────────────────────────────────────────────────────────────────────────
# Exercise 4 — String Statistics  (Difficulty: Medium)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   Analyze a sentence and print a report.
#
#   text = "Python is Amazing"
#
#   Print:
#     - Total characters (including spaces)
#     - Total letters only (no spaces)
#     - Number of vowels (a, e, i, o, u — case-insensitive)
#     - Number of words
#     - Uppercase version
#
#   Expected output:
#     Characters : 17
#     Letters    : 15
#     Vowels     : 5
#     Words      : 3
#     Upper      : PYTHON IS AMAZING

# Solution:
text = "Python is Amazing"

vowels = "aeiouAEIOU"
vowel_count = sum(1 for ch in text if ch in vowels)
letter_count = sum(1 for ch in text if ch.isalpha())

print(f"Characters : {len(text)}")
print(f"Letters    : {letter_count}")
print(f"Vowels     : {vowel_count}")
print(f"Words      : {len(text.split())}")
print(f"Upper      : {text.upper()}")
# Output:
# Characters : 17
# Letters    : 15
# Vowels     : 5  (o, i, A, a, i)
# Words      : 3
# Upper      : PYTHON IS AMAZING


# ─────────────────────────────────────────────────────────────────────────────
# Exercise 5 — Password Strength Checker  (Difficulty: Hard)
# ─────────────────────────────────────────────────────────────────────────────
# Description:
#   Write a password strength checker using only string methods and len().
#   No conditionals needed beyond simple boolean checks.
#
#   password = "Python3!"
#
#   Check all four rules and print a formatted report:
#     [OK] / [X]  At least 8 characters
#     [OK] / [X]  Contains an uppercase letter
#     [OK] / [X]  Contains a lowercase letter
#     [OK] / [X]  Contains a digit
#
#   Then print overall result: STRONG or WEAK
#
#   Expected output:
#     Password  : Python3!
#     [OK] At least 8 characters
#     [OK] Contains an uppercase letter
#     [OK] Contains a lowercase letter
#     [OK] Contains a digit
#     Strength  : STRONG

# Solution:
password = "Python3!"

has_length   = len(password) >= 8
has_upper    = any(ch.isupper() for ch in password)
has_lower    = any(ch.islower() for ch in password)
has_digit    = any(ch.isdigit() for ch in password)

def mark(condition):
    return "[OK]" if condition else "[X] "

print(f"Password  : {password}")
print(f"{mark(has_length)} At least 8 characters")
print(f"{mark(has_upper)} Contains an uppercase letter")
print(f"{mark(has_lower)} Contains a lowercase letter")
print(f"{mark(has_digit)} Contains a digit")

is_strong = has_length and has_upper and has_lower and has_digit
print(f"Strength  : {'STRONG' if is_strong else 'WEAK'}")
# Output:
# Password  : Python3!
# [OK] At least 8 characters
# [OK] Contains an uppercase letter
# [OK] Contains a lowercase letter
# [OK] Contains a digit
# Strength  : STRONG
