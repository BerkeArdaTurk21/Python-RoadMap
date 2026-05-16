# Week 2 - Day 2: for Loops
# Topic: range(), iterate lists/strings/dicts, enumerate(), zip()

# ─────────────────────────────────────────────
# 1. BASIC for LOOP
# ─────────────────────────────────────────────
# Syntax:
#   for variable in iterable:
#       <block runs once per item>

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry

# The loop variable can be named anything
for number in [10, 20, 30]:
    print(number * 2)
# 20  40  60


# ─────────────────────────────────────────────
# 2. range() FUNCTION
# ─────────────────────────────────────────────
# range(stop)          → 0, 1, 2, ..., stop-1
# range(start, stop)   → start, start+1, ..., stop-1
# range(start, stop, step) → every step-th value

for i in range(5):
    print(i, end=" ")       # 0 1 2 3 4
print()

for i in range(1, 6):
    print(i, end=" ")       # 1 2 3 4 5
print()

for i in range(0, 11, 2):
    print(i, end=" ")       # 0 2 4 6 8 10
print()

# Counting backwards
for i in range(5, 0, -1):
    print(i, end=" ")       # 5 4 3 2 1
print()


# ─────────────────────────────────────────────
# 3. ITERATING OVER A STRING
# ─────────────────────────────────────────────
# Strings are sequences — each character is one iteration.

word = "Python"
for char in word:
    print(char, end="-")    # P-y-t-h-o-n-
print()

# Count vowels
vowels = 0
for char in "Hello World":
    if char.lower() in "aeiou":
        vowels += 1
print(f"Vowels: {vowels}")  # 3


# ─────────────────────────────────────────────
# 4. ITERATING OVER A DICTIONARY
# ─────────────────────────────────────────────
# By default, iterating a dict gives its keys.

student = {"name": "Berke", "age": 22, "grade": "A"}

for key in student:
    print(key)              # name  age  grade

# .values() — iterate values only
for value in student.values():
    print(value)            # Berke  22  A

# .items() — iterate key-value pairs as tuples
for key, value in student.items():
    print(f"{key}: {value}")
# name: Berke
# age: 22
# grade: A


# ─────────────────────────────────────────────
# 5. enumerate() — INDEX + VALUE TOGETHER
# ─────────────────────────────────────────────
# enumerate(iterable, start=0) → (index, value) pairs
# Avoids manual counter variables.

colors = ["red", "green", "blue"]

for index, color in enumerate(colors):
    print(f"{index}: {color}")
# 0: red
# 1: green
# 2: blue

# Start index from 1
for i, color in enumerate(colors, start=1):
    print(f"{i}. {color}")
# 1. red
# 2. green
# 3. blue


# ─────────────────────────────────────────────
# 6. zip() — ITERATE TWO SEQUENCES IN PARALLEL
# ─────────────────────────────────────────────
# zip(a, b) pairs items at the same position.
# Stops at the shortest sequence.

names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 85
# Bob: 92
# Charlie: 78

# zip with three sequences
x_coords = [1, 2, 3]
y_coords = [4, 5, 6]
labels   = ["A", "B", "C"]

for x, y, label in zip(x_coords, y_coords, labels):
    print(f"{label}({x}, {y})")
# A(1, 4)  B(2, 5)  C(3, 6)


# ─────────────────────────────────────────────
# 7. LIST BUILT WITH A for LOOP (accumulator pattern)
# ─────────────────────────────────────────────
# Common pattern: start with an empty list, append inside the loop.

squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)              # [1, 4, 9, 16, 25]

# Running total
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print(f"Total: {total}")    # 100


# ─────────────────────────────────────────────
# 8. LOOP WITH else CLAUSE
# ─────────────────────────────────────────────
# The else block runs after the loop finishes normally
# (i.e., NOT interrupted by break).

for i in range(3):
    print(i)
else:
    print("Loop finished.")         # Always runs here

# Useful for search patterns:
target = 7
for n in [1, 3, 5, 9]:
    if n == target:
        print("Found!")
        break
else:
    print("Not found.")             # Runs — 7 is not in the list


# ─────────────────────────────────────────────
# 9. NESTED for LOOPS
# ─────────────────────────────────────────────
# Inner loop completes fully for each outer iteration.

for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)

# Multiplication table (partial)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:3}", end="")
    print()
#  1  2  3
#  2  4  6
#  3  6  9


# ─────────────────────────────────────────────
# 10. PRACTICAL EXAMPLE — Grade Report
# ─────────────────────────────────────────────

students = [
    {"name": "Alice",   "scores": [85, 90, 92]},
    {"name": "Bob",     "scores": [70, 65, 80]},
    {"name": "Charlie", "scores": [95, 98, 100]},
]

print("\n── Grade Report ──")
for i, student in enumerate(students, start=1):
    avg = sum(student["scores"]) / len(student["scores"])
    grade = "A" if avg >= 90 else "B" if avg >= 80 else "C"
    print(f"{i}. {student['name']:<10} Avg: {avg:.1f}  Grade: {grade}")
# 1. Alice      Avg: 89.0  Grade: B
# 2. Bob        Avg: 71.7  Grade: C
# 3. Charlie    Avg: 97.7  Grade: A
