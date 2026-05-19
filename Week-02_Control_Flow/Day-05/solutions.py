# Week 2 - Day 5: Nested Loops — Solutions

# ─────────────────────────────────────────────
# Solution 1: Star Patterns
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")
n = int(input("Enter size n: "))

print("\nPattern A — Right Triangle:")
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

print("\nPattern B — Left Triangle:")
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars  = "*" * i
    print(spaces + stars)

print("\nPattern C — Pyramid:")
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars  = "*" * (2 * i - 1)
    print(spaces + stars)


# ─────────────────────────────────────────────
# Solution 2: Matrix Operations
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")
matrix = [
    [3,  8,  2],
    [7,  1, 15],
    [4,  9,  6],
]

# a) Print formatted
for row in matrix:
    for val in row:
        print(f"{val:4}", end="")
    print()

# b) Find maximum and its position
max_val = matrix[0][0]
max_row, max_col = 0, 0
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        if val > max_val:
            max_val = val
            max_row, max_col = i, j
print(f"\nMax value: {max_val} at [{max_row}][{max_col}]")

# c) Sum of each row
print()
for i, row in enumerate(matrix):
    row_sum = 0
    for val in row:
        row_sum += val
    print(f"Row {i} sum: {row_sum}")


# ─────────────────────────────────────────────
# Solution 3: Multiplication Table
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")
n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i * j:5}", end="")
    print()


# ─────────────────────────────────────────────
# Solution 4: 2D Search
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")
grid = [
    ["Alice",  "Bob",   "Charlie"],
    ["Diana",  "Eve",   "Frank"],
    ["Grace",  "Heidi", "Ivan"],
]

target = input("Search: ").strip()
found = False

for i, row in enumerate(grid):
    for j, name in enumerate(row):
        if name.lower() == target.lower():
            print(f"Found at Row {i + 1}, Col {j + 1}")
            found = True
            break
    if found:
        break

if not found:
    print("Not found.")


# ─────────────────────────────────────────────
# Solution 5: Classroom Grade Summary
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")
students = [
    ("Alice",   [85, 92, 78, 90]),
    ("Bob",     [70, 65, 80, 75]),
    ("Charlie", [95, 98, 92, 100]),
    ("Diana",   [60, 72, 68, 55]),
]

best_score  = 0
best_student = ""

for name, scores in students:
    avg = sum(scores) / len(scores)
    score_str = "".join(f"{s:4}" for s in scores)
    print(f"{name:<8} | Scores:{score_str} | Avg: {avg:.1f}")

    for s in scores:
        if s > best_score:
            best_score   = s
            best_student = name

print(f"\nHighest score overall: {best_score} ({best_student})")
