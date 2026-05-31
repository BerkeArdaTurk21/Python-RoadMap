# =============================================================================
# Week 04 - Day 03 | Dictionaries
# =============================================================================
# Topics: Creating dicts, accessing, modifying, methods, iteration,
#         nested dicts, dict comprehensions (preview), merging
# =============================================================================

# -----------------------------------------------------------------------------
# 1. CREATING DICTIONARIES
# -----------------------------------------------------------------------------
# A dictionary is an ORDERED (Python 3.7+), MUTABLE collection of KEY→VALUE pairs.
# Keys must be UNIQUE and HASHABLE (strings, ints, tuples — not lists).

empty = {}
person = {"name": "Berke", "age": 21, "city": "Warsaw"}
scores = {1: "one", 2: "two", 3: "three"}
mixed_keys = {"name": "Alice", 42: True, (1, 2): "point"}

print(person)
print(type(person))   # <class 'dict'>

# dict() constructor
from_kwargs = dict(name="Bob", age=30)       # {"name": "Bob", "age": 30}
from_pairs  = dict([("a", 1), ("b", 2)])     # {"a": 1, "b": 2}
print(from_kwargs)
print(from_pairs)

# -----------------------------------------------------------------------------
# 2. ACCESSING VALUES
# -----------------------------------------------------------------------------
person = {"name": "Berke", "age": 21, "city": "Warsaw"}

# Square bracket — raises KeyError if key missing
print(person["name"])    # Berke
print(person["age"])     # 21

# .get() — returns None (or default) if key missing — SAFER
print(person.get("city"))          # Warsaw
print(person.get("email"))         # None  (no error)
print(person.get("email", "N/A"))  # N/A   (custom default)

# KeyError example
# print(person["email"])   # ← KeyError: 'email'

# Membership test
print("name" in person)    # True
print("email" in person)   # False

# -----------------------------------------------------------------------------
# 3. MODIFYING DICTIONARIES
# -----------------------------------------------------------------------------
person = {"name": "Berke", "age": 21}

# Add or update
person["city"] = "Warsaw"       # add new key
person["age"]  = 22             # update existing key
print(person)

# Update multiple keys at once
person.update({"email": "b@example.com", "age": 23})
print(person)

# Delete
del person["email"]             # delete key (KeyError if missing)
age = person.pop("age")         # remove and return value
print(f"Removed age: {age}")
print(person)

# pop with default (no error if key missing)
val = person.pop("missing_key", "default")
print(val)   # default

# Remove last inserted item (Python 3.7+)
person["temp"] = "remove me"
removed = person.popitem()      # returns (key, value) tuple
print(f"Popped: {removed}")

# Clear all
copy = dict(person)
copy.clear()
print(copy)   # {}

# -----------------------------------------------------------------------------
# 4. DICTIONARY METHODS
# -----------------------------------------------------------------------------
inventory = {"apple": 5, "banana": 3, "cherry": 8, "date": 2}

# Keys, values, items — all return VIEW objects (dynamic, not copies)
print(inventory.keys())    # dict_keys(['apple', 'banana', 'cherry', 'date'])
print(inventory.values())  # dict_values([5, 3, 8, 2])
print(inventory.items())   # dict_items([('apple', 5), ('banana', 3), ...])

# Convert to list if you need a static snapshot
keys_list = list(inventory.keys())
print(keys_list)

# setdefault — get value if key exists, else set AND return default
inventory.setdefault("elderberry", 0)  # adds key with value 0
print(inventory["elderberry"])         # 0
inventory.setdefault("apple", 999)     # apple already exists — no change
print(inventory["apple"])              # 5  (unchanged)

# copy
original  = {"a": 1, "b": 2}
copy      = original.copy()
copy["c"] = 3
print(original)   # {"a": 1, "b": 2}  ← unchanged
print(copy)       # {"a": 1, "b": 2, "c": 3}

# fromkeys — create dict with same value for multiple keys
defaults = dict.fromkeys(["width", "height", "depth"], 0)
print(defaults)   # {'width': 0, 'height': 0, 'depth': 0}

# len
print(len(inventory))   # 5

# -----------------------------------------------------------------------------
# 5. ITERATING OVER DICTIONARIES
# -----------------------------------------------------------------------------
prices = {"apple": 1.20, "banana": 0.50, "cherry": 2.00}

# Iterate over keys (default)
for key in prices:
    print(key)

# Iterate over values
for value in prices.values():
    print(value)

# Iterate over key-value pairs (most common)
for key, value in prices.items():
    print(f"{key}: ${value:.2f}")

# Iterate with enumerate to get index
for i, (key, value) in enumerate(prices.items()):
    print(f"{i}: {key} = {value}")

# -----------------------------------------------------------------------------
# 6. NESTED DICTIONARIES
# -----------------------------------------------------------------------------
# Dicts can contain other dicts — great for structured data.

students = {
    "alice": {"age": 20, "grade": "A", "scores": [95, 88, 92]},
    "bob":   {"age": 22, "grade": "B", "scores": [78, 82, 80]},
    "carol": {"age": 21, "grade": "A", "scores": [91, 95, 98]},
}

# Access nested value
print(students["alice"]["grade"])        # A
print(students["bob"]["scores"][1])      # 82  (second score)

# Safe nested access with .get()
email = students.get("alice", {}).get("email", "no email")
print(email)   # no email

# Iterate nested dict
for name, info in students.items():
    avg = sum(info["scores"]) / len(info["scores"])
    print(f"{name.capitalize()}: grade={info['grade']}, avg={avg:.1f}")

# Modify nested value
students["alice"]["age"] = 21
students["bob"]["scores"].append(85)
print(students["bob"]["scores"])   # [78, 82, 80, 85]

# -----------------------------------------------------------------------------
# 7. MERGING DICTIONARIES
# -----------------------------------------------------------------------------
defaults = {"color": "blue", "size": "M", "quantity": 1}
overrides = {"color": "red", "quantity": 3}

# Method 1: update() — modifies in place
merged1 = defaults.copy()
merged1.update(overrides)
print(merged1)   # {'color': 'red', 'size': 'M', 'quantity': 3}

# Method 2: ** unpacking (Python 3.5+) — creates new dict
merged2 = {**defaults, **overrides}
print(merged2)   # same result, clean one-liner

# Method 3: | operator (Python 3.9+)
merged3 = defaults | overrides
print(merged3)

# Right side wins on duplicate keys in all three methods.

# -----------------------------------------------------------------------------
# 8. DICT AS A COUNTER (manual, before Counter in Day 06)
# -----------------------------------------------------------------------------
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1   # clever use of get() default

print(counts)   # {'apple': 3, 'banana': 2, 'cherry': 1}

# Sort by count descending
sorted_counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)
print(sorted_counts)   # [('apple', 3), ('banana', 2), ('cherry', 1)]

# -----------------------------------------------------------------------------
# 9. DICT COMPREHENSION (preview — full coverage in Day 05)
# -----------------------------------------------------------------------------
# {key_expr: value_expr for item in iterable}

squares = {x: x**2 for x in range(6)}
print(squares)   # {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}

# Filter — only even squares
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)

# Invert a dict (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}

# =============================================================================
# SUMMARY
# =============================================================================
# ┌────────────────────────────────────────────────────────────────┐
# │  Operation            │  Example                              │
# ├────────────────────────────────────────────────────────────────┤
# │  Access (safe)        │  d.get("key", default)                │
# │  Add / update         │  d["key"] = value                     │
# │  Update many          │  d.update({...})                      │
# │  Delete               │  del d["key"]  /  d.pop("key")        │
# │  Iterate pairs        │  for k, v in d.items()                │
# │  Check key exists     │  "key" in d                           │
# │  Merge                │  {**d1, **d2}  or  d1 | d2            │
# │  Word count pattern   │  d[w] = d.get(w, 0) + 1              │
# └────────────────────────────────────────────────────────────────┘
print("\nDay 03 — Dictionaries complete!")
