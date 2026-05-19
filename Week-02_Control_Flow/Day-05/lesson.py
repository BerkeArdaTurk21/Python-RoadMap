# Week 2 - Day 5: Nested Loops
# Topic: Matrix patterns, loop inside loop, 2D iteration

# ─────────────────────────────────────────────
# 1. WHAT IS A NESTED LOOP?
# ─────────────────────────────────────────────
# A nested loop is a loop placed inside another loop.
# The INNER loop completes ALL its iterations for EACH
# single iteration of the OUTER loop.

for outer in range(3):          # runs 3 times
    for inner in range(4):      # runs 4 times per outer
        print(f"({outer},{inner})", end=" ")
    print()
# (0,0) (0,1) (0,2) (0,3)
# (1,0) (1,1) (1,2) (1,3)
# (2,0) (2,1) (2,2) (2,3)

# Total iterations = outer × inner = 3 × 4 = 12


# ─────────────────────────────────────────────
# 2. MULTIPLICATION TABLE
# ─────────────────────────────────────────────
print("── Multiplication Table (1-5) ──")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:4}", end="")
    print()
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25


# ─────────────────────────────────────────────
# 3. STAR PATTERNS
# ─────────────────────────────────────────────

# Right-aligned triangle
print("\n── Right Triangle ──")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
# *
# **
# ***
# ****
# *****

# Inverted triangle
print("\n── Inverted Triangle ──")
for i in range(5, 0, -1):
    print("* " * i)
# * * * * *
# * * * *
# * * *
# * *
# *

# Pyramid
print("\n── Pyramid ──")
n = 5
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars  = "* " * i
    print(spaces + stars)
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# Diamond
print("\n── Diamond ──")
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)


# ─────────────────────────────────────────────
# 4. NUMBER PATTERNS
# ─────────────────────────────────────────────

# Floyd's Triangle
print("\n── Floyd's Triangle ──")
num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

# Row number pattern
print("\n── Row Numbers ──")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


# ─────────────────────────────────────────────
# 5. 2D LIST (MATRIX) ITERATION
# ─────────────────────────────────────────────
# A 2D list is a list of lists — like a grid or table.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("\n── Matrix ──")
for row in matrix:
    for value in row:
        print(f"{value:3}", end="")
    print()
#   1  2  3
#   4  5  6
#   7  8  9

# Access specific element: matrix[row][col]
print(f"Center: {matrix[1][1]}")    # 5
print(f"Top-right: {matrix[0][2]}") # 3

# Sum all elements
total = 0
for row in matrix:
    for val in row:
        total += val
print(f"Matrix sum: {total}")       # 45

# Diagonal elements (where row index == col index)
print("Diagonal:", end=" ")
for i in range(len(matrix)):
    print(matrix[i][i], end=" ")    # 1 5 9
print()


# ─────────────────────────────────────────────
# 6. BUILDING A 2D LIST WITH NESTED LOOPS
# ─────────────────────────────────────────────

# Create a 4x4 grid filled with 0
rows, cols = 4, 4
grid = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(0)
    grid.append(row)

print("\n── 4x4 Zero Grid ──")
for row in grid:
    print(row)

# Create a multiplication grid
print("\n── Multiplication Grid (3x3) ──")
table = []
for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i * j)
    table.append(row)

for row in table:
    print(row)
# [1, 2, 3]
# [2, 4, 6]
# [3, 6, 9]


# ─────────────────────────────────────────────
# 7. ITERATING WITH enumerate() IN NESTED LOOPS
# ─────────────────────────────────────────────

classroom = [
    ["Alice", "Bob",   "Charlie"],
    ["Diana", "Eve",   "Frank"],
    ["Grace", "Heidi", "Ivan"],
]

print("\n── Classroom Seats ──")
for row_i, row in enumerate(classroom):
    for col_i, name in enumerate(row):
        print(f"Row {row_i+1}, Seat {col_i+1}: {name}")


# ─────────────────────────────────────────────
# 8. NESTED LOOPS WITH break AND continue
# ─────────────────────────────────────────────

# Find first cell in matrix with value > 5
matrix2 = [
    [1, 2, 3],
    [4, 6, 7],
    [8, 9, 10],
]

found = False
for i, row in enumerate(matrix2):
    for j, val in enumerate(row):
        if val > 5:
            print(f"\nFirst value > 5: {val} at [{i}][{j}]")
            found = True
            break
    if found:
        break
# First value > 5: 6 at [1][1]

# Skip zeros in a matrix
sparse = [
    [0, 2, 0],
    [4, 0, 6],
    [0, 8, 0],
]

print("\nNon-zero values:")
for row in sparse:
    for val in row:
        if val == 0:
            continue
        print(val, end=" ")     # 2 4 6 8
print()


# ─────────────────────────────────────────────
# 9. PRACTICAL EXAMPLE — Seating Chart
# ─────────────────────────────────────────────

def print_seating_chart(rows, seats_per_row):
    print(f"\n── Cinema: {rows} rows × {seats_per_row} seats ──")
    for r in range(1, rows + 1):
        row_label = chr(64 + r)     # A, B, C, ...
        for s in range(1, seats_per_row + 1):
            print(f"{row_label}{s:02}", end="  ")
        print()

print_seating_chart(4, 6)
# A01  A02  A03  A04  A05  A06
# B01  B02  B03  B04  B05  B06
# C01  C02  C03  C04  C05  C06
# D01  D02  D03  D04  D05  D06


# ─────────────────────────────────────────────
# 10. PRACTICAL EXAMPLE — Grade Matrix
# ─────────────────────────────────────────────

subjects = ["Math", "Science", "English"]
students = [
    {"name": "Alice",   "grades": [92, 88, 95]},
    {"name": "Bob",     "grades": [75, 80, 70]},
    {"name": "Charlie", "grades": [60, 55, 65]},
]

print("\n── Grade Report ──")
header = f"{'Student':<10}" + "".join(f"{s:>10}" for s in subjects) + f"{'Average':>10}"
print(header)
print("-" * len(header))

for student in students:
    name   = student["name"]
    grades = student["grades"]
    avg    = sum(grades) / len(grades)
    row    = f"{name:<10}" + "".join(f"{g:>10}" for g in grades) + f"{avg:>10.1f}"
    print(row)
