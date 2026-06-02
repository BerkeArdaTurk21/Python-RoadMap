# =============================================================================
# Week 04 - Day 05 | Comprehensions
# =============================================================================
# Topics: List comprehensions, dict comprehensions, set comprehensions,
#         generator expressions, conditions, nesting
# =============================================================================

# -----------------------------------------------------------------------------
# 1. LIST COMPREHENSIONS
# -----------------------------------------------------------------------------
# Syntax: [expression for item in iterable]
# Produces a new LIST in one readable line.

# Without comprehension (verbose)
squares_loop = []
for x in range(6):
    squares_loop.append(x ** 2)

# With comprehension (Pythonic)
squares = [x ** 2 for x in range(6)]
print(squares)       # [0, 1, 4, 9, 16, 25]

# Works on any iterable
chars     = [c.upper() for c in "hello"]
print(chars)         # ['H', 'E', 'L', 'L', 'O']

lengths   = [len(w) for w in ["apple", "banana", "cherry"]]
print(lengths)       # [5, 6, 6]

doubled   = [x * 2 for x in [1, 2, 3, 4, 5]]
print(doubled)       # [2, 4, 6, 8, 10]

# -----------------------------------------------------------------------------
# 2. COMPREHENSIONS WITH CONDITIONS (filtering)
# -----------------------------------------------------------------------------
# Syntax: [expression for item in iterable IF condition]

evens  = [x for x in range(20) if x % 2 == 0]
print(evens)         # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

long_words = [w for w in ["hi", "hello", "hey", "world"] if len(w) > 3]
print(long_words)    # ['hello', 'world']

# Filter and transform together
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Multiple conditions
fizz = [x for x in range(1, 31) if x % 3 == 0 if x % 5 == 0]
print(fizz)          # [15, 30]  (divisible by both 3 AND 5)

# -----------------------------------------------------------------------------
# 3. COMPREHENSIONS WITH if/else (value transformation, not filtering)
# -----------------------------------------------------------------------------
# Syntax: [A if condition else B for item in iterable]
# NOTE: the if/else goes BEFORE the for when it's a value choice (not a filter)

labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print(labels)        # ['even', 'odd', 'even', 'odd', 'even', 'odd']

# Replace negative numbers with 0 (clamp)
data  = [3, -1, 4, -1, 5, -9, 2, 6]
clamped = [x if x >= 0 else 0 for x in data]
print(clamped)       # [3, 0, 4, 0, 5, 0, 2, 6]

# Filter (if at end) vs transform (if/else before for) — different!
# Filter:    [x for x in lst if condition]         → shorter list
# Transform: [A if condition else B for x in lst]  → same length

# -----------------------------------------------------------------------------
# 4. NESTED LIST COMPREHENSIONS
# -----------------------------------------------------------------------------
# Syntax: [expr for outer in iterable for inner in iterable]
# The order mirrors nested for loops — outer loop first.

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat   = [cell for row in matrix for cell in row]
print(flat)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Equivalent loop:
# for row in matrix:
#     for cell in row:
#         flat.append(cell)

# Cartesian product — all (x, y) pairs
coords = [(x, y) for x in range(3) for y in range(3)]
print(coords)
# [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]

# Build a multiplication table as a 2D list
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
for row in table:
    print(row)

# ⚠️ READABILITY: if your comprehension needs more than 2 levels deep or
# complex logic — use a regular loop. Readability > brevity.

# -----------------------------------------------------------------------------
# 5. DICT COMPREHENSIONS
# -----------------------------------------------------------------------------
# Syntax: {key_expr: value_expr for item in iterable}

squares_dict = {x: x ** 2 for x in range(6)}
print(squares_dict)   # {0:0, 1:1, 2:4, 3:9, 4:16, 5:25}

# From two lists with zip
keys   = ["name", "age", "city"]
values = ["Berke", 21, "Warsaw"]
person = {k: v for k, v in zip(keys, values)}
print(person)   # {'name': 'Berke', 'age': 21, 'city': 'Warsaw'}

# Filter with condition
prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.0, "date": 3.5}
cheap  = {k: v for k, v in prices.items() if v < 2.0}
print(cheap)    # {'apple': 1.2, 'banana': 0.5}

# Transform values
upper_keys = {k.upper(): v for k, v in prices.items()}
print(upper_keys)   # {'APPLE': 1.2, 'BANANA': 0.5, ...}

# Invert a dict
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}

# -----------------------------------------------------------------------------
# 6. SET COMPREHENSIONS
# -----------------------------------------------------------------------------
# Syntax: {expression for item in iterable}
# Produces a SET — duplicates removed automatically.

unique_lengths = {len(w) for w in ["hi", "hello", "hey", "world", "sun"]}
print(unique_lengths)   # {2, 3, 5}  (no duplicate 3 from "hey")

first_letters = {w[0] for w in ["apple", "avocado", "banana", "cherry"]}
print(first_letters)    # {'a', 'b', 'c'}

# With condition
long_firsts = {w[0] for w in ["apple", "hi", "banana", "ok"] if len(w) > 3}
print(long_firsts)      # {'a', 'b'}

# -----------------------------------------------------------------------------
# 7. GENERATOR EXPRESSIONS
# -----------------------------------------------------------------------------
# Syntax: (expression for item in iterable)
# Like a list comprehension but LAZY — computes values on demand, not all at once.
# Uses much less memory for large sequences.

# List comprehension — creates the entire list in memory
squares_list = [x ** 2 for x in range(1_000_000)]   # 8 MB in memory

# Generator expression — computes values one at a time
squares_gen  = (x ** 2 for x in range(1_000_000))   # ~200 bytes!

print(type(squares_list))   # <class 'list'>
print(type(squares_gen))    # <class 'generator'>

# Use next() to get values one by one
gen = (x ** 2 for x in range(5))
print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 4

# Or iterate with a loop
for val in (x ** 2 for x in range(5)):
    print(val, end=" ")
print()

# Common usage: pass a generator directly to sum/max/min/any/all
total = sum(x ** 2 for x in range(10))   # no extra [] needed!
print(total)   # 285

big = any(x > 50 for x in [10, 30, 55, 20])
print(big)     # True

all_positive = all(x > 0 for x in [1, 2, 3, 4])
print(all_positive)   # True

# -----------------------------------------------------------------------------
# 8. COMPREHENSION vs LOOP — WHEN TO USE EACH
# -----------------------------------------------------------------------------
# USE comprehension when:
#   ✅ Simple transformation or filtering of an iterable → new list/dict/set
#   ✅ Code reads like English: "squares of even numbers under 20"
#   ✅ One or two lines maximum

# USE a regular loop when:
#   ✅ Multiple statements per iteration
#   ✅ Side effects (printing, writing files, updating external state)
#   ✅ Complex nesting that hurts readability
#   ✅ Early break/continue logic

# USE generator when:
#   ✅ You only need to iterate ONCE (don't need to access by index)
#   ✅ The sequence is large (memory matters)
#   ✅ Passing to sum/max/min/any/all

# =============================================================================
# SUMMARY
# =============================================================================
# ┌──────────────────────────────────────────────────────────────────┐
# │  Type        │  Syntax                          │  Result       │
# ├──────────────────────────────────────────────────────────────────┤
# │  List        │  [expr for x in it]              │  list         │
# │  List+filter │  [expr for x in it if cond]      │  list         │
# │  List+branch │  [a if c else b for x in it]     │  list         │
# │  Dict        │  {k: v for x in it}              │  dict         │
# │  Set         │  {expr for x in it}              │  set          │
# │  Generator   │  (expr for x in it)              │  generator    │
# │  Nested      │  [e for a in it1 for b in it2]   │  flat list    │
# └──────────────────────────────────────────────────────────────────┘
print("\nDay 05 — Comprehensions complete!")
