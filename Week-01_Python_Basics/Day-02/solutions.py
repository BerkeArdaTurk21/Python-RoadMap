"""
================================================
Week 1 | Day 2 — Solutions
================================================
Only open this after you've genuinely tried exercises.py!
================================================
"""

# ═══════════════════════════════════════════════════
# Exercise 1 — String Slicer Solution
# ═══════════════════════════════════════════════════
# Explanation: All four results come from a single slice expression each.
# [:5] takes indices 0–4; [-6:] counts 6 back from the end; [::2] picks
# every other character; [::-1] steps backward through the whole string.
message = "Hello, World!"

print(f"First 5  : {message[:5]}")
print(f"Last 6   : {message[-6:]}")
print(f"Every 2nd: {message[::2]}")
print(f"Reversed : {message[::-1]}")
# Output:
# First 5  : Hello
# Last 6   : World!
# Every 2nd: Hlo ol!
# Reversed : !dlroW ,olleH


# ═══════════════════════════════════════════════════
# Exercise 2 — Text Normalizer Solution
# ═══════════════════════════════════════════════════
# Explanation: Method calls can be chained because each method returns a new
# string. strip() removes surrounding whitespace first, then title() converts
# to title case. split() without arguments splits on any whitespace run and
# ignores leading/trailing blanks, so len() of the result gives word count.
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


# ═══════════════════════════════════════════════════
# Exercise 3 — Initials Generator Solution
# ═══════════════════════════════════════════════════
# Explanation: split() produces a list of words; a generator expression takes
# the first character of each and uppercases it. join() with "." as separator
# assembles them, and the trailing "." is appended by string concatenation.
full_name = "berke can turk"

parts = full_name.split()
initials = ".".join(word[0].upper() for word in parts) + "."
formatted_name = full_name.title()

print(f"Full name : {formatted_name}")
print(f"Initials  : {initials}")
# Output:
# Full name : Berke Can Turk
# Initials  : B.C.T.


# ═══════════════════════════════════════════════════
# Exercise 4 — String Statistics Solution
# ═══════════════════════════════════════════════════
# Explanation: sum() with a generator expression is the idiomatic way to count
# characters matching a condition. ch.isalpha() is True for letters only (no
# spaces or punctuation). Checking ch in vowels covers both upper and lowercase
# because the vowels string includes both cases.
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
# Vowels     : 5
# Words      : 3
# Upper      : PYTHON IS AMAZING


# ═══════════════════════════════════════════════════
# Exercise 5 — Password Strength Checker Solution
# ═══════════════════════════════════════════════════
# Explanation: any() short-circuits as soon as it finds one matching character,
# making it efficient. A helper function mark() avoids repeating the ternary
# operator four times. The final strength label is only STRONG when all four
# conditions are True — a single failing check gives WEAK.
password = "Python3!"

has_length = len(password) >= 8
has_upper  = any(ch.isupper() for ch in password)
has_lower  = any(ch.islower() for ch in password)
has_digit  = any(ch.isdigit() for ch in password)

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
