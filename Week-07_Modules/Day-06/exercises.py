# =============================================================================
# Week 07 - Day 06 | Regular Expressions — Exercises
# =============================================================================

import re

# -----------------------------------------------------------------------------
# Exercise 1 — Extract All Numbers
# -----------------------------------------------------------------------------
# From the text below, extract:
#   a) All whole numbers as a list of strings
#   b) All whole numbers as a list of INTEGERS (converted)
#   c) Their sum
#
# Expected:
#   Strings: ['3', '14', '2026', '7']
#   Ints:    [3, 14, 2026, 7]
#   Sum:     2050
#
# Hint: re.findall(r'\d+', text), then int() each.

text = "Room 3 has 14 chairs, opened in 2026, closes in 7 days."
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Validate Phone Numbers
# -----------------------------------------------------------------------------
# A valid phone number here looks like: 0XXX XXX XX XX
#   - starts with 0
#   - then 3 digits, space, 3 digits, space, 2 digits, space, 2 digits
# Write a function is_valid_phone(s) that returns True/False using re.match
# with a ^...$ anchored pattern. Test it on the list and print each result.
#
# Expected:
#   0532 123 45 67 -> True
#   532 123 45 67  -> False
#   0532 123 4567  -> False
#
# Hint: r"^0\d{3} \d{3} \d{2} \d{2}$"

numbers = ["0532 123 45 67", "532 123 45 67", "0532 123 4567"]
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Mask Email Addresses
# -----------------------------------------------------------------------------
# In the text, replace every email address with the word "[EMAIL]".
# Then ALSO print just the list of domains (the part after '@').
#
# Expected:
#   Masked: Contact [EMAIL] or [EMAIL] for help.
#   Domains: ['company.com', 'support.org']
#
# Hint: an email pattern like r"[\w.+-]+@([\w.-]+)" — the parentheses capture
#       the domain so findall returns just the domains.

text = "Contact ceo@company.com or team@support.org for help."
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Parse a Log Line with Named Groups
# -----------------------------------------------------------------------------
# Each log line looks like:  "2026-06-24 23:00:15 ERROR Disk full"
# Use ONE regex with named groups to extract: date, time, level, message.
# Print them as a dict-like output.
#
# Expected:
#   date=2026-06-24  time=23:00:15  level=ERROR  message=Disk full
#
# Hint: r"(?P<date>\S+) (?P<time>\S+) (?P<level>\w+) (?P<message>.+)"
#       Use m.group('date'), etc. (or m.groupdict()).

line = "2026-06-24 23:00:15 ERROR Disk full"
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Find Repeated Words
# -----------------------------------------------------------------------------
# Find every place where a word is immediately repeated (e.g. "the the").
# Use a backreference to match the same word twice, case-insensitively.
# Print each repeated word you find.
#
# Expected (for the sentence below):
#   Repeated: the
#   Repeated: is
#
# Hint: pattern r"\b(\w+)\s+\1\b" with re.IGNORECASE; the captured group is the
#       repeated word. \1 is a backreference to group 1.

sentence = "This is is a test where the the words repeat."
# TODO
