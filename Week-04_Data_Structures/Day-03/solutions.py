# =============================================================================
# Week 04 - Day 03 | Dictionaries — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================

# -----------------------------------------------------------------------------
# Solution 1 — Word Frequency Counter
# -----------------------------------------------------------------------------
# KEY INSIGHT: d.get(word, 0) + 1
#   If the word exists → get its current count and add 1.
#   If the word doesn't exist → get default 0, then add 1 → first occurrence = 1.
# This avoids an if/else check entirely.

def word_count(text):
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print("Solution 1 — Word Frequency Counter")
print(word_count("the cat sat on the mat"))
# {'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
print(word_count("Hello hello HELLO"))
# {'hello': 3}
print()

# -----------------------------------------------------------------------------
# Solution 2 — Invert a Dictionary
# -----------------------------------------------------------------------------
# KEY INSIGHT: Iterate .items() and build a new dict with keys/values swapped.
# Dict comprehension: {v: k for k, v in d.items()} is the Pythonic one-liner.

def invert_dict(d):
    return {v: k for k, v in d.items()}

print("Solution 2 — Invert a Dictionary")
print(invert_dict({"a": 1, "b": 2, "c": 3}))   # {1: 'a', 2: 'b', 3: 'c'}
print(invert_dict({1: "one", 2: "two"}))         # {'one': 1, 'two': 2}
print()

# -----------------------------------------------------------------------------
# Solution 3 — Group by First Letter
# -----------------------------------------------------------------------------
# KEY INSIGHT: Use setdefault(letter, []) to initialise missing keys with an
# empty list, then append to whatever is there.
# setdefault returns the existing value if the key already exists — so a single
# line handles both first-occurrence and subsequent-occurrence cases.

def group_by_letter(words):
    groups = {}
    for word in words:
        letter = word[0]
        groups.setdefault(letter, []).append(word)
    return groups

print("Solution 3 — Group by First Letter")
print(group_by_letter(["apple", "avocado", "banana", "blueberry", "cherry"]))
# {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}
print()

# WHY setdefault is cleaner than the manual if-check:
# Without it you'd write:
#   if letter not in groups:
#       groups[letter] = []
#   groups[letter].append(word)
# setdefault collapses those two lines into one.

# -----------------------------------------------------------------------------
# Solution 4 — Nested Dict: Student Report
# -----------------------------------------------------------------------------
# KEY INSIGHT: Use max() with a key= function.
# The key function computes the average for each student name.
# max() returns the NAME that produces the highest average — no explicit loop needed.

students = {
    "alice": {"scores": [85, 90, 78]},
    "bob":   {"scores": [70, 65, 80]},
    "carol": {"scores": [95, 92, 98]},
    "dave":  {"scores": [88, 76, 84]},
}

def get_top_student(students):
    return max(students, key=lambda name: sum(students[name]["scores"]) /
                                          len(students[name]["scores"]))

print("Solution 4 — Nested Dict: Top Student")
print(get_top_student(students))   # carol
print()

# Averages: alice=84.3, bob=71.7, carol=95.0, dave=82.7

# -----------------------------------------------------------------------------
# Solution 5 — Merge and Override
# -----------------------------------------------------------------------------
# KEY INSIGHT: {**default, **override}
#   Unpacks both dicts into a NEW dict. Keys from override overwrite default.
#   Neither original is modified — a new dict is created.
#
# This is the cleanest, most Pythonic merge. Python 3.9+ also supports:
#   default | override  (same result)

def merge_configs(default, override):
    return {**default, **override}

print("Solution 5 — Merge and Override")
default  = {"color": "blue", "size": "M", "debug": False}
override = {"color": "red", "debug": True, "verbose": True}
result   = merge_configs(default, override)
print(result)
# {'color': 'red', 'size': 'M', 'debug': True, 'verbose': True}
print("default unchanged:", default)
print("override unchanged:", override)
