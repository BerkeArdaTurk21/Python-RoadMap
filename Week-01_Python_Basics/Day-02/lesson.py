"""
================================================
Week 1 | Day 2 — String Operations
================================================
Level       : Beginner
Topics      : string indexing, slicing, escape characters, string methods,
              f-string formatting, string immutability, len()
Goal        : Manipulate text data confidently — extract characters,
              build substrings, and transform strings with built-in methods
================================================
"""

# ── SECTION 1: String Creation ───────────────────
# A string is an ordered sequence of characters enclosed in quotes.
# Single and double quotes are interchangeable; choose one and stay consistent.

single = 'Python'
double = "Python"
print(single == double)         # Output: True  — content is identical

# Use the opposite quote style when the string itself contains quotes.
sentence = "It's a beautiful day."
dialogue = 'She said, "Hello!"'

# Triple quotes span multiple lines and preserve every newline literally.
haiku = """Old pond,
a frog jumps in —
sound of water."""

print(sentence)                 # Output: It's a beautiful day.
print(dialogue)                 # Output: She said, "Hello!"
print(haiku)
# Output:
# Old pond,
# a frog jumps in —
# sound of water.


# ── SECTION 2: String Indexing ───────────────────
# Every character has a position number called an index.
# Positive indices count from the left, starting at 0.
# Negative indices count from the right, starting at -1.
#
#   String:    P  y  t  h  o  n
#   Positive:  0  1  2  3  4  5
#   Negative: -6 -5 -4 -3 -2 -1

word = "Python"

print(word[0])                  # Output: P  (first character)
print(word[5])                  # Output: n  (last character)
print(word[-1])                 # Output: n  (last, negative index)
print(word[-6])                 # Output: P  (first, negative index)

# Accessing an index that doesn't exist raises IndexError.
# print(word[10])               # IndexError: string index out of range


# ── SECTION 3: String Slicing ────────────────────
# Slice syntax: string[start:stop:step]
#   start — index to begin at (inclusive), default 0
#   stop  — index to stop before (exclusive), default len(string)
#   step  — how many positions to jump each time, default 1

text = "Hello, World!"
#       0123456789...

print(text[0:5])                # Output: Hello   (indices 0,1,2,3,4)
print(text[7:12])               # Output: World
print(text[:5])                 # Output: Hello   (start defaults to 0)
print(text[7:])                 # Output: World!  (stop defaults to end)
print(text[:])                  # Output: Hello, World!  (full copy)
print(text[::2])                # Output: Hlo ol! (every 2nd character)
print(text[::-1])               # Output: !dlroW ,olleH  (reversed)

# Negative indices work in slices too.
print(text[-6:-1])              # Output: World


# ── SECTION 4: Escape Characters ─────────────────
# Some characters can't be typed literally inside a string.
# Prefix them with a backslash (\) to create an escape sequence.
#
#   \n   — newline        (moves cursor to next line)
#   \t   — tab            (adds horizontal whitespace)
#   \\   — literal backslash
#   \'   — literal single quote inside a single-quoted string
#   \"   — literal double quote inside a double-quoted string

path = "C:\\Users\\Berke\\Documents"
print(path)                     # Output: C:\Users\Berke\Documents

tabbed = "Name:\tBerke"
print(tabbed)                   # Output: Name:	Berke

multiline = "Line 1\nLine 2\nLine 3"
print(multiline)
# Output:
# Line 1
# Line 2
# Line 3

# Raw strings (r"...") treat every backslash as a literal character.
# Very useful for Windows file paths and regular expressions.
raw_path = r"C:\Users\Berke\new_folder"
print(raw_path)                 # Output: C:\Users\Berke\new_folder


# ── SECTION 5: String Methods — Transforming Text ─
# Strings are immutable: methods always return a NEW string,
# they never modify the original.

original = "  hello, world!  "

print(original.strip())         # Output: hello, world!   (both ends)
print(original.lstrip())        # Output: hello, world!   (left only)
print(original.rstrip())        # Output:   hello, world! (right only)

phrase = "hello, world!"
print(phrase.upper())           # Output: HELLO, WORLD!
print(phrase.lower())           # Output: hello, world!
print(phrase.title())           # Output: Hello, World!
print(phrase.capitalize())      # Output: Hello, world!

sentence = "Python is great. Python is fun."
print(sentence.replace("Python", "Coding"))
# Output: Coding is great. Coding is fun.

# split() breaks a string into a list at a delimiter.
csv_line = "Berke,25,developer"
parts = csv_line.split(",")
print(parts)                    # Output: ['Berke', '25', 'developer']

# join() is the reverse — assembles a list of strings into one string.
words = ["Python", "is", "powerful"]
print(" ".join(words))          # Output: Python is powerful
print("-".join(words))          # Output: Python-is-powerful


# ── SECTION 6: String Methods — Searching Text ────
# These methods let you locate and inspect content inside a string.

bio = "I love Python and Python loves me."

print(bio.count("Python"))      # Output: 2  (occurrences)
print(bio.find("Python"))       # Output: 7  (index of first match)
print(bio.find("Java"))         # Output: -1 (not found — no error, returns -1)

print(bio.startswith("I love")) # Output: True
print(bio.endswith("me."))      # Output: True
print(bio.startswith("You"))    # Output: False

# The in operator checks if a substring exists anywhere in the string.
print("Python" in bio)          # Output: True
print("Java" in bio)            # Output: False

# index() works like find() but raises ValueError if not found.
# Use find() when you're not sure the substring exists.
print(bio.index("Python"))      # Output: 7


# ── SECTION 7: f-String Format Specifications ────
# f-strings accept a format spec after a colon: {value:spec}
# Format spec mini-language: {value:{fill}{align}{width}.{precision}{type}}
#   Align:  <  left   >  right   ^  center
#   Fill:   any single character (default is space)
#   Width:  minimum total field width
#   .N:     decimal precision for floats
#   ,  :    thousands separator

name = "Berke"
score = 95.678
pi = 3.14159265

# Alignment and width
print(f"|{name:<10}|")          # Output: |Berke     |  (left, width 10)
print(f"|{name:>10}|")          # Output: |     Berke|  (right, width 10)
print(f"|{name:^10}|")          # Output: |  Berke   |  (centered)
print(f"|{name:*^10}|")         # Output: |**Berke***|  (centered, fill *)

# Float precision
print(f"{score:.2f}")           # Output: 95.68
print(f"{pi:.4f}")              # Output: 3.1416

# Number separators
big_number = 1_000_000
print(f"{big_number:,}")        # Output: 1,000,000
print(f"{big_number:_}")        # Output: 1_000_000


# ── SECTION 8: len() and String Immutability ─────
# len() returns the total number of characters (spaces included).
# Strings are immutable — you cannot change a character in place.

greeting = "Hello"
print(len(greeting))            # Output: 5

long_str = "Hello, World!"
print(len(long_str))            # Output: 13

# This raises TypeError — strings do not support item assignment.
# greeting[0] = "J"             # TypeError: 'str' object does not support item assignment

# To "change" part of a string, slice and concatenate to build a new one.
new_greeting = "J" + greeting[1:]
print(new_greeting)             # Output: Jello
print(greeting)                 # Output: Hello  — original is unchanged


# ── QUICK REFERENCE ──────────────────────────────
# Indexing:  s[0]  s[-1]  (first / last character)
# Slicing:   s[start:stop:step]    s[::-1] reverses
#
# Escape sequences:
#   \n newline   \t tab   \\ backslash   r"..." raw string
#
# Transform methods (all return a new string):
#   .upper()  .lower()  .title()  .capitalize()
#   .strip()  .lstrip()  .rstrip()
#   .replace(old, new)
#   .split(sep)   →  list      sep.join(list)  →  str
#
# Search methods:
#   .find(sub)      → index or -1
#   .count(sub)     → int
#   .startswith(s)  → bool
#   .endswith(s)    → bool
#   sub in s        → bool
#
# f-string format spec:
#   {val:<10}   left-aligned, width 10
#   {val:>10}   right-aligned
#   {val:^10}   centered
#   {val:*^10}  centered, fill with *
#   {val:.2f}   2 decimal places
#   {val:,}     thousands separator
#
# Length:   len(s)
# Immutable: methods never change the original — they return a new string
