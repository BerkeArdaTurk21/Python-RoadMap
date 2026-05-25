# Week 3 - Day 4: Lambda Functions — Solutions

# ─────────────────────────────────────────────
# Solution 1: Square the Evens
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")

nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = list(map(lambda x: x ** 2,
                  filter(lambda x: x % 2 == 0, nums)))
print(result)


# ─────────────────────────────────────────────
# Solution 2: Sort Names by Last Character
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")

names = ["Berke", "Alice", "Bob", "Eve", "Charlie"]
by_last = sorted(names, key=lambda n: n[-1].lower())
print(by_last)


# ─────────────────────────────────────────────
# Solution 3: Filter & Format Products
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")

products = [
    {"name": "Laptop", "price": 1500},
    {"name": "Phone",  "price":  800},
    {"name": "Tablet", "price":  450},
    {"name": "Camera", "price":  990},
    {"name": "TV",     "price": 1200},
]

affordable = filter(lambda p: p["price"] <= 1000, products)
ordered    = sorted(affordable, key=lambda p: p["price"])
formatted  = list(map(lambda p: f"{p['name']}: ${p['price']}", ordered))
print(formatted)


# ─────────────────────────────────────────────
# Solution 4: Best Student per Subject
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")

students = [
    {"name": "Berke", "math": 88, "science": 75},
    {"name": "Alice", "math": 92, "science": 81},
    {"name": "Bob",   "math": 78, "science": 95},
    {"name": "Eve",   "math": 85, "science": 90},
]

top_math    = max(students, key=lambda s: s["math"])
top_science = max(students, key=lambda s: s["science"])

print(f"Top in math    : {top_math['name']} ({top_math['math']})")
print(f"Top in science : {top_science['name']} ({top_science['science']})")


# ─────────────────────────────────────────────
# Solution 5: Sort by Multiple Keys
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")

employees = [
    {"name": "Berke", "dept": "Eng",   "salary": 5500},
    {"name": "Alice", "dept": "Eng",   "salary": 6000},
    {"name": "Bob",   "dept": "Sales", "salary": 4500},
    {"name": "Eve",   "dept": "Sales", "salary": 6000},
    {"name": "Mark",  "dept": "Eng",   "salary": 6000},
]

ordered = sorted(
    employees,
    key=lambda e: (e["dept"], -e["salary"], e["name"]),
)

for e in ordered:
    print(f"  {e['name']:<6} {e['dept']:<6} {e['salary']}")
