# =============================================================================
# Week 04 - Day 03 | Dictionaries — Exercises
# =============================================================================
# Solve each challenge yourself BEFORE looking at solutions.py
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Word Frequency Counter
# -----------------------------------------------------------------------------
# Write word_count(text) that returns a dict mapping each word to how many
# times it appears in the text (case-insensitive).
#
# Hint: split on spaces, lower() the text first.
#
# Expected output:
#   word_count("the cat sat on the mat")
#   → {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
#
#   word_count("Hello hello HELLO")
#   → {'hello': 3}

def word_count(text):
    pass  # TODO


print("Exercise 1 — Word Frequency Counter")
print(word_count("the cat sat on the mat"))
print(word_count("Hello hello HELLO"))
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Invert a Dictionary
# -----------------------------------------------------------------------------
# Write invert_dict(d) that swaps keys and values.
# Assume all values are unique (no duplicates).
#
# Expected output:
#   invert_dict({'a': 1, 'b': 2, 'c': 3})  → {1: 'a', 2: 'b', 3: 'c'}
#   invert_dict({1: 'one', 2: 'two'})       → {'one': 1, 'two': 2}

def invert_dict(d):
    pass  # TODO


print("Exercise 2 — Invert a Dictionary")
print(invert_dict({"a": 1, "b": 2, "c": 3}))   # {1: 'a', 2: 'b', 3: 'c'}
print(invert_dict({1: "one", 2: "two"}))         # {'one': 1, 'two': 2}
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Group by First Letter
# -----------------------------------------------------------------------------
# Write group_by_letter(words) that takes a list of words and returns a dict
# where each key is a letter and the value is a list of words starting with it.
#
# Expected output:
#   group_by_letter(["apple", "avocado", "banana", "blueberry", "cherry"])
#   → {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

def group_by_letter(words):
    pass  # TODO


print("Exercise 3 — Group by First Letter")
result = group_by_letter(["apple", "avocado", "banana", "blueberry", "cherry"])
print(result)
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Nested Dict: Student Report
# -----------------------------------------------------------------------------
# Given the students dict below, write get_top_student(students) that
# returns the name of the student with the highest AVERAGE score.
#
# Expected output:
#   get_top_student(students) → 'carol'

students = {
    "alice": {"scores": [85, 90, 78]},
    "bob":   {"scores": [70, 65, 80]},
    "carol": {"scores": [95, 92, 98]},
    "dave":  {"scores": [88, 76, 84]},
}

def get_top_student(students):
    pass  # TODO


print("Exercise 4 — Nested Dict: Top Student")
print(get_top_student(students))   # carol
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Merge and Override
# -----------------------------------------------------------------------------
# Write merge_configs(default, override) that merges two config dicts.
# Keys in override take precedence over default.
# Return a NEW dict — do not modify either input.
#
# Expected output:
#   default  = {'color': 'blue', 'size': 'M', 'debug': False}
#   override = {'color': 'red', 'debug': True, 'verbose': True}
#   result   = {'color': 'red', 'size': 'M', 'debug': True, 'verbose': True}

def merge_configs(default, override):
    pass  # TODO


print("Exercise 5 — Merge and Override")
default  = {"color": "blue", "size": "M", "debug": False}
override = {"color": "red", "debug": True, "verbose": True}
result   = merge_configs(default, override)
print(result)
# Verify originals are not modified
print("default unchanged:", default)
print("override unchanged:", override)
