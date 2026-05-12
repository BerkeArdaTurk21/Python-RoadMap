"""
================================================
Week 1 | Day 5 — Solutions
================================================
Only open this after you've genuinely tried exercises.py!
================================================
"""

# ═══════════════════════════════════════════════════
# Exercise 1 — Grade Classifier Solution
# ═══════════════════════════════════════════════════
# Explanation: Chained comparisons (80 <= score < 90) are used in each branch
# for clarity. The pass/fail status is a natural fit for a ternary — it is a
# binary outcome that maps directly to score >= 60. Printing an empty line
# before the results keeps the output clean when running interactively.
score = int(input("Enter score (0-100): "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score < 90:
    grade = "B"
elif 70 <= score < 80:
    grade = "C"
elif 60 <= score < 70:
    grade = "D"
else:
    grade = "F"

status = "Pass" if score >= 60 else "Fail"

print()
print(f"Score  : {score}")
print(f"Grade  : {grade}")
print(f"Status : {status}")
# Output (score=85): Score: 85 | Grade: B | Status: Pass
# Output (score=45): Score: 45 | Grade: F | Status: Fail


# ═══════════════════════════════════════════════════
# Exercise 2 — Leap Year Checker Solution
# ═══════════════════════════════════════════════════
# Explanation: The leap year rule has three parts combined with logical operators.
# The outer or handles the two valid cases: (divisible by 4 but not 100) OR
# (divisible by 400). Grouping with parentheses makes the logic explicit and
# avoids relying on operator precedence (and binds tighter than or).
year = int(input("Enter a year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print(f"{year} is a leap year. ✅")
else:
    print(f"{year} is NOT a leap year. ❌")
# Output (2000): 2000 is a leap year. ✅
# Output (1900): 1900 is NOT a leap year. ❌
# Output (2024): 2024 is a leap year. ✅


# ═══════════════════════════════════════════════════
# Exercise 3 — Number Analyzer Solution
# ═══════════════════════════════════════════════════
# Explanation: Each property uses the most direct operator for the job.
# Parity uses bitwise & 1 (the least-significant bit is 1 for odd numbers).
# Abs value uses a ternary to avoid the abs() builtin as required.
# Divisibility by both is checked first so it takes priority over the
# individual checks. bit_length() is a built-in int method.
number = int(input("Enter an integer: "))

sign      = "Positive" if number > 0 else ("Negative" if number < 0 else "Zero")
parity    = "Odd" if number & 1 else "Even"
in_range  = "Yes" if -100 <= number <= 100 else "No"
abs_val   = number if number >= 0 else -number

by3  = number % 3 == 0
by5  = number % 5 == 0
if by3 and by5:
    divisible = "by both (3 and 5)"
elif by3:
    divisible = "by 3"
elif by5:
    divisible = "by 5"
else:
    divisible = "by neither (3 nor 5)"

bit_len = abs_val.bit_length() if abs_val > 0 else 1

print()
print(f"─── Number Analysis: {number} ───")
print(f"Sign      : {sign}")
print(f"Parity    : {parity}")
print(f"In range  : {in_range}  (-100 to 100)")
print(f"Abs value : {abs_val}")
print(f"Divisible : {divisible}")
print(f"Bit length: {bit_len} bits")
# Output (number=-42):
# ─── Number Analysis: -42 ───
# Sign      : Negative
# Parity    : Even
# In range  : Yes  (-100 to 100)
# Abs value : 42
# Divisible : by neither (3 nor 5)
# Bit length: 6 bits


# ═══════════════════════════════════════════════════
# Exercise 4 — Membership & Identity Checker Solution
# ═══════════════════════════════════════════════════
# Explanation: raw stores the original input before stripping so we can
# compare it against the stripped version to detect whitespace. The word
# for the approved-list check is lowercased so "Python" matches "python".
# Identity (is None) is demonstrated even though input() never returns None —
# it shows the correct idiom. All bool results are formatted as Yes/No strings.
raw  = input("Enter a word: ")
word = raw.strip().lower()

approved = ["python", "data", "science", "code", "learn"]
vowels   = "aeiou"

in_approved   = word in approved
starts_vowel  = len(word) > 0 and word[0] in vowels
longer_than_4 = len(word) > 4
had_whitespace = raw != raw.strip()
is_none       = word is None

def yes_no(b):
    return "Yes" if b else "No"

print()
print(f'─── Word Analysis: "{word}" ───')
print(f"In approved list : {yes_no(in_approved)}")
print(f"Starts with vowel: {yes_no(starts_vowel)}")
print(f"Longer than 4    : {yes_no(longer_than_4)}")
print(f"Had whitespace   : {yes_no(had_whitespace)}")
print(f"Is None          : {yes_no(is_none)}")
# Output ("python"):
# ─── Word Analysis: "python" ───
# In approved list : Yes
# Starts with vowel: No
# Longer than 4    : Yes
# Had whitespace   : No
# Is None          : No


# ═══════════════════════════════════════════════════
# Exercise 5 — Bitwise Permission Manager Solution
# ═══════════════════════════════════════════════════
# Explanation: Each permission is a distinct power of 2 so exactly one bit
# is set per flag. Testing a permission uses bitwise AND: (perms & FLAG) is
# non-zero only when that bit is set, and bool() converts it to True/False.
# ADMIN is granted with |= only when all three basic flags are present.
# The final loop re-reads the updated permissions for a clean summary.
READ    = 1     # 0b0001
WRITE   = 2     # 0b0010
EXECUTE = 4     # 0b0100
ADMIN   = 8     # 0b1000

perms = int(input("Enter permission value (1-15): "))

has_read    = bool(perms & READ)
has_write   = bool(perms & WRITE)
has_execute = bool(perms & EXECUTE)
has_admin   = bool(perms & ADMIN)

def tick(b):
    return "✅" if b else "❌"

print()
print("─── Permission Report ───")
print(f"Input value : {perms}  (binary: {bin(perms)})")
print(f"READ        : {tick(has_read)}")
print(f"WRITE       : {tick(has_write)}")
print(f"EXECUTE     : {tick(has_execute)}")
print(f"ADMIN       : {tick(has_admin)}")

if has_read and has_write and has_execute:
    perms |= ADMIN
    print()
    print("All basic permissions found — ADMIN granted!")
    print(f"Final value : {perms}  (binary: {bin(perms)})")
    print(
        f"Final perms : "
        f"READ {tick(bool(perms & READ))}  "
        f"WRITE {tick(bool(perms & WRITE))}  "
        f"EXECUTE {tick(bool(perms & EXECUTE))}  "
        f"ADMIN {tick(bool(perms & ADMIN))}"
    )
else:
    print()
    print("Missing basic permissions — ADMIN not granted.")
# Output (perm=7):
# ─── Permission Report ───
# Input value : 7  (binary: 0b111)
# READ        : ✅
# WRITE       : ✅
# EXECUTE     : ✅
# ADMIN       : ❌
#
# All basic permissions found — ADMIN granted!
# Final value : 15  (binary: 0b1111)
# Final perms : READ ✅  WRITE ✅  EXECUTE ✅  ADMIN ✅
