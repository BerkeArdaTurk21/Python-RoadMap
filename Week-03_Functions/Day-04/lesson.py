# Week 3 - Day 4: Lambda Functions
# Topic: lambda, map(), filter(), sorted() with key

# ─────────────────────────────────────────────
# 1. WHAT IS A LAMBDA?
# ─────────────────────────────────────────────
# A lambda is a small, anonymous, single-expression function.
# Syntax:    lambda parameters: expression
# It RETURNS the value of the expression — no 'return' keyword.

# Regular function
def square_def(x):
    return x ** 2

# Equivalent lambda
square = lambda x: x ** 2

print(square_def(5))    # 25
print(square(5))        # 25

# Lambdas can take multiple parameters
add      = lambda a, b: a + b
multiply = lambda a, b: a * b

print(add(3, 4))        # 7
print(multiply(3, 4))   # 12

# Lambdas with default values and keyword args
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Berke"))               # Hello, Berke!
print(greet("Alice", "Hi"))         # Hi, Alice!


# ─────────────────────────────────────────────
# 2. WHEN TO USE A LAMBDA
# ─────────────────────────────────────────────
# ✅ When you need a one-off, throwaway function
# ✅ When passing a tiny function to map/filter/sorted/etc.
# ❌ If it has multiple statements → use def
# ❌ If it has a name and is reused → use def
# ❌ If it is more than ~40 chars wide → use def for readability


# ─────────────────────────────────────────────
# 3. map() — APPLY A FUNCTION TO EVERY ITEM
# ─────────────────────────────────────────────
# map(func, iterable) → new iterator with func applied to each item.
# Wrap with list() to materialize.

numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x ** 2, numbers))
print(squared)                       # [1, 4, 9, 16, 25]

# Convert strings to uppercase
words = ["python", "is", "fun"]
upper = list(map(str.upper, words))
print(upper)                         # ['PYTHON', 'IS', 'FUN']

# map() with multiple iterables — func gets one item from each
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)                          # [11, 22, 33]


# ─────────────────────────────────────────────
# 4. filter() — KEEP ITEMS THAT PASS A CONDITION
# ─────────────────────────────────────────────
# filter(func, iterable) → keeps items where func(item) is truthy.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)                         # [2, 4, 6, 8, 10]

positives = list(filter(lambda x: x > 0, [-3, -1, 0, 2, 5, -7]))
print(positives)                     # [2, 5]

# Filter out empty strings
names = ["Berke", "", "Alice", None, "Bob", ""]
clean = list(filter(None, names))    # passing None filters falsy values
print(clean)                         # ['Berke', 'Alice', 'Bob']


# ─────────────────────────────────────────────
# 5. sorted() WITH A KEY FUNCTION
# ─────────────────────────────────────────────
# sorted(iterable, key=func, reverse=False)
# The key function decides what value each item is sorted BY.

words = ["banana", "Apple", "cherry", "date"]

# Default sort — case-sensitive (uppercase comes first)
print(sorted(words))                 # ['Apple', 'banana', 'cherry', 'date']

# Case-insensitive sort
print(sorted(words, key=str.lower))  # ['Apple', 'banana', 'cherry', 'date']

# Sort by length
print(sorted(words, key=len))        # ['date', 'Apple', 'banana', 'cherry']

# Sort numbers descending
nums = [5, 2, 9, 1, 7, 3]
print(sorted(nums, reverse=True))    # [9, 7, 5, 3, 2, 1]


# ─────────────────────────────────────────────
# 6. SORTING LIST OF TUPLES / DICTS
# ─────────────────────────────────────────────

people = [
    ("Berke",  22),
    ("Alice",  30),
    ("Bob",    25),
    ("Eve",    19),
]

# Sort by age (second element of tuple)
by_age = sorted(people, key=lambda p: p[1])
print(by_age)
# [('Eve', 19), ('Berke', 22), ('Bob', 25), ('Alice', 30)]

# Sort by name length, then alphabetically
by_name = sorted(people, key=lambda p: (len(p[0]), p[0]))
print(by_name)

# Sort dicts by a field
products = [
    {"name": "Laptop", "price": 1200},
    {"name": "Phone",  "price":  800},
    {"name": "Tablet", "price":  450},
]
cheapest = sorted(products, key=lambda p: p["price"])
for p in cheapest:
    print(f"  {p['name']:<8} ${p['price']}")


# ─────────────────────────────────────────────
# 7. CHAINING map() / filter() / sorted()
# ─────────────────────────────────────────────

numbers = [-3, 1, -1, 4, -5, 9, 2, -8]

# Take absolute values of negatives, then sort
result = sorted(map(abs, filter(lambda x: x < 0, numbers)))
print(result)                        # [1, 3, 5, 8]

# Top 3 longest words in a sentence
sentence = "Lambda functions are useful for short transformations"
top3 = sorted(sentence.split(), key=len, reverse=True)[:3]
print(top3)                          # ['transformations', 'functions', 'useful']


# ─────────────────────────────────────────────
# 8. min() / max() WITH A KEY
# ─────────────────────────────────────────────
# min and max accept the SAME key= parameter as sorted.

people = [
    {"name": "Berke", "score": 88},
    {"name": "Alice", "score": 95},
    {"name": "Bob",   "score": 72},
]

best  = max(people, key=lambda p: p["score"])
worst = min(people, key=lambda p: p["score"])

print(f"Best : {best['name']} ({best['score']})")
print(f"Worst: {worst['name']} ({worst['score']})")


# ─────────────────────────────────────────────
# 9. PRACTICAL EXAMPLE — LEADERBOARD
# ─────────────────────────────────────────────

players = [
    {"name": "Berke", "wins": 12, "losses":  3},
    {"name": "Alice", "wins":  8, "losses":  2},
    {"name": "Bob",   "wins": 15, "losses":  9},
    {"name": "Eve",   "wins":  9, "losses":  1},
]

# Compute win rate, then rank by it
ranked = sorted(
    players,
    key=lambda p: p["wins"] / (p["wins"] + p["losses"]),
    reverse=True,
)

print("── Leaderboard ──")
for i, p in enumerate(ranked, 1):
    rate = p["wins"] / (p["wins"] + p["losses"])
    print(f"  {i}. {p['name']:<6} W={p['wins']:>2}  L={p['losses']:>2}  rate={rate:.1%}")
