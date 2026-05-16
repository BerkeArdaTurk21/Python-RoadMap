# Week 2 - Day 2: for Loops — Solutions

# ─────────────────────────────────────────────
# Solution 1: Multiplication Table
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")
n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n}  x  {i:2}  =  {n * i}")


# ─────────────────────────────────────────────
# Solution 2: Word Frequency Counter
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")
sentence = "the cat sat on the mat and the cat sat"
frequency = {}

for word in sentence.split():
    word = word.lower()
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

for word, count in frequency.items():
    print(f"{word}: {count}")


# ─────────────────────────────────────────────
# Solution 3: Student Grade Summary
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")
students = [
    ("Alice",   [88, 92, 95]),
    ("Bob",     [60, 55, 70]),
    ("Charlie", [78, 82, 80]),
]

for name, scores in students:
    avg = sum(scores) / len(scores)
    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"{name:<8} | Avg: {avg:.1f} | Grade: {grade}")


# ─────────────────────────────────────────────
# Solution 4: Number Pattern Printer
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")
n = int(input("Enter a number: "))

for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(col, end=" ")
    print()


# ─────────────────────────────────────────────
# Solution 5: Inventory Checker
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")
products = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
stock    = [50, 0, 23, 0, 8]

out_of_stock = 0
for product, qty in zip(products, stock):
    if qty == 0:
        print(f"{product:<12}: {qty:2} units  ← OUT OF STOCK")
        out_of_stock += 1
    else:
        print(f"{product:<12}: {qty:2} units")

print(f"\nOut of stock: {out_of_stock} products")
