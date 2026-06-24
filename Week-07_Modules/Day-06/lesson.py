# =============================================================================
# Week 07 - Day 06 | Regular Expressions (re module)
# =============================================================================
# Regular expressions ("regex") are a mini-language for describing text
# patterns: validation, search, extraction, and replacement.
# Python's `re` module is the standard tool.
#
# TIP: always write patterns as raw strings (r"...") so backslashes are not
# interpreted by Python before regex sees them.

import re

# -----------------------------------------------------------------------------
# 1. The Core Functions
# -----------------------------------------------------------------------------
text = "The year 2026 starts now, 100 days to go."

# re.search  — first match anywhere (returns a Match object or None)
m = re.search(r"\d+", text)
print(f"search:   {m.group()} at index {m.start()}")   # '2026'

# re.match   — match only at the START of the string
print(f"match:    {re.match(r'The', text) is not None}")   # True
print(f"match2:   {re.match(r'year', text) is not None}")  # False (not at start)

# re.findall — every non-overlapping match, as a list
print(f"findall:  {re.findall(r'\d+', text)}")          # ['2026', '100']

# re.finditer — like findall but yields Match objects (with positions)
positions = [(mm.group(), mm.start()) for mm in re.finditer(r"\d+", text)]
print(f"finditer: {positions}")

# re.sub     — replace matches
print(f"sub:      {re.sub(r'\d+', '#', text)}")

# re.split   — split on a pattern
print(f"split:    {re.split(r'\W+', 'a-b_c d')}")       # non-word chars

# -----------------------------------------------------------------------------
# 2. Metacharacters & Character Classes
# -----------------------------------------------------------------------------
# .   any char (except newline)      \d  digit        \D  non-digit
# \w  word char [a-zA-Z0-9_]         \W  non-word     \s  whitespace
# \b  word boundary                  ^   start        $   end
# [abc] one of a/b/c   [^abc] none of   [a-z] range
print("\nCharacter classes:")
print(f"  vowels in 'education': {re.findall(r'[aeiou]', 'education')}")
print(f"  words:                 {re.findall(r'\b\w+\b', 'hi, world!')}")
print(f"  not digits:            {re.findall(r'\D+', 'a1b22c')}")

# -----------------------------------------------------------------------------
# 3. Quantifiers
# -----------------------------------------------------------------------------
# *   0 or more     +   1 or more     ?   0 or 1
# {n} exactly n     {n,} n or more    {n,m} between n and m
# Add ? after a quantifier for NON-greedy (smallest) matching.
print("\nQuantifiers:")
print(f"  greedy <.+>:     {re.findall(r'<.+>', '<a><b>')}")     # ['<a><b>']
print(f"  lazy   <.+?>:    {re.findall(r'<.+?>', '<a><b>')}")    # ['<a>', '<b>']
print(f"  3-digit groups:  {re.findall(r'\d{3}', '12 345 6789')}")  # ['345','678']

# -----------------------------------------------------------------------------
# 4. Groups & Capturing
# -----------------------------------------------------------------------------
# Parentheses (...) capture sub-parts. Access with .group(n) or .groups().
date_str = "2026-06-24"
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", date_str)
print(f"\nGroups: whole={m.group(0)}, year={m.group(1)}, "
      f"month={m.group(2)}, day={m.group(3)}")
print(f"  .groups() -> {m.groups()}")

# Named groups: (?P<name>...) — more readable
m = re.search(r"(?P<user>\w+)@(?P<domain>[\w.]+)", "berke@example.com")
print(f"  named: user={m.group('user')}, domain={m.group('domain')}")

# Backreferences in sub: \1, \2 refer to captured groups
swapped = re.sub(r"(\w+)-(\w+)", r"\2-\1", "first-second")
print(f"  sub with backref: {swapped}")    # 'second-first'

# -----------------------------------------------------------------------------
# 5. Compiling Patterns (re.compile)
# -----------------------------------------------------------------------------
# Compile once, reuse many times — clearer and slightly faster in loops.
email_re = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
blob = "Mail a@x.com or b@y.org please"
print(f"\nCompiled findall: {email_re.findall(blob)}")

# -----------------------------------------------------------------------------
# 6. Flags
# -----------------------------------------------------------------------------
# re.IGNORECASE (re.I) — case-insensitive
# re.MULTILINE (re.M)  — ^ and $ match at each line
# re.DOTALL (re.S)     — . also matches newline
print("\nFlags:")
print(f"  IGNORECASE: {re.findall(r'python', 'Python PYTHON pyThon', re.I)}")

# -----------------------------------------------------------------------------
# 7. A Practical Validator
# -----------------------------------------------------------------------------
def is_valid_email(addr):
    pattern = r"^[\w.+-]+@[\w-]+\.[\w.-]+$"
    return re.match(pattern, addr) is not None

for addr in ["berke@example.com", "bad@", "no-at-sign.com", "a.b@c.co.uk"]:
    print(f"  {addr:<20} -> {is_valid_email(addr)}")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
# re.search / re.match — first match (anywhere / at start)
# re.findall / finditer — all matches (list / iterator of Match)
# re.sub / re.split    — replace / split on a pattern
# \d \w \s . [] ^ $    — metacharacters & classes
# * + ? {n,m}          — quantifiers (add ? for non-greedy)
# (...) (?P<name>...)  — capturing & named groups; \1 backrefs in sub
# re.compile           — reuse a pattern efficiently
# flags: re.I / re.M / re.S
# Always use raw strings: r"\d+"
