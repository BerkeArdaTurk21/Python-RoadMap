# Week 3 - Day 4: Lambda Functions — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: Square the Evens
# ─────────────────────────────────────────────
# Given a list of integers, use filter() and map() with lambdas
# to produce a new list containing the SQUARES of only the EVEN numbers.
#
# Input : [1, 2, 3, 4, 5, 6, 7, 8]
# Output: [4, 16, 36, 64]


# ─────────────────────────────────────────────
# Exercise 2: Sort Names by Last Character
# ─────────────────────────────────────────────
# Given a list of names, use sorted() with a lambda key to sort
# them by their LAST character (alphabetically).
#
# Input : ["Berke", "Alice", "Bob", "Eve", "Charlie"]
# Output: ['Alice', 'Charlie', 'Eve', 'Berke', 'Bob']
#         (sorted by last char: 'e','e','e','e','b')
# Hint: ties keep original order (sorted is stable).


# ─────────────────────────────────────────────
# Exercise 3: Filter & Format Products
# ─────────────────────────────────────────────
# Given a list of products as dicts, do the following with
# filter / map / sorted + lambdas:
#   1. Keep only products with price <= 1000
#   2. Sort them from cheapest to most expensive
#   3. Map each one to the string "<name>: $<price>"
#
# Input:
#   products = [
#       {"name": "Laptop", "price": 1500},
#       {"name": "Phone",  "price":  800},
#       {"name": "Tablet", "price":  450},
#       {"name": "Camera", "price":  990},
#       {"name": "TV",     "price": 1200},
#   ]
#
# Expected output:
#   ['Tablet: $450', 'Phone: $800', 'Camera: $990']


# ─────────────────────────────────────────────
# Exercise 4: Best Student per Subject
# ─────────────────────────────────────────────
# Given a list of student records, use max() with a lambda key
# to find the top scorer per subject.
#
# Input:
#   students = [
#       {"name": "Berke", "math": 88, "science": 75},
#       {"name": "Alice", "math": 92, "science": 81},
#       {"name": "Bob",   "math": 78, "science": 95},
#       {"name": "Eve",   "math": 85, "science": 90},
#   ]
#
# Expected output:
#   Top in math    : Alice (92)
#   Top in science : Bob   (95)


# ─────────────────────────────────────────────
# Exercise 5: Sort by Multiple Keys
# ─────────────────────────────────────────────
# Sort a list of employees by:
#   1. Department (ascending, alphabetical)
#   2. Then by salary DESCENDING
#   3. Then by name ascending (alphabetical)
#
# Input:
#   employees = [
#       {"name": "Berke", "dept": "Eng",     "salary": 5500},
#       {"name": "Alice", "dept": "Eng",     "salary": 6000},
#       {"name": "Bob",   "dept": "Sales",   "salary": 4500},
#       {"name": "Eve",   "dept": "Sales",   "salary": 6000},
#       {"name": "Mark",  "dept": "Eng",     "salary": 6000},
#   ]
#
# Expected output:
#   Alice  Eng    6000
#   Mark   Eng    6000
#   Berke  Eng    5500
#   Eve    Sales  6000
#   Bob    Sales  4500
#
# Hint: lambda e: (e["dept"], -e["salary"], e["name"])
