# Week 2 - Day 5: Nested Loops — Interactive Quiz

score = 0

print("=" * 50)
print("  Week 2 - Day 5 Quiz: Nested Loops")
print("=" * 50)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("How many total iterations do the nested loops produce?")
print()
print("    for i in range(3):")
print("        for j in range(4):")
print("            print('x')")
print()
print("A) 3")
print("B) 4")
print("C) 7")
print("D) 12")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "D":
    print("✅ Correct! The inner loop runs 4 times for each of the 3 outer iterations: 3 × 4 = 12.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: D. Total = outer × inner = 3 × 4 = 12.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("What is printed last by this code?")
print()
print("    for i in range(1, 4):")
print("        for j in range(1, 4):")
print("            print(i * j, end=' ')")
print("        print()")
print()
print("A) 3 6 9")
print("B) 9")
print("C) 1 2 3")
print("D) 7 8 9")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "A":
    print("✅ Correct! The last outer iteration (i=3) prints 3×1 3×2 3×3 → 3 6 9.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: A. Last row is i=3: 3 6 9.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("How do you access the element at row 1, column 2")
print("in this 2D list?")
print()
print("    matrix = [[1,2,3],[4,5,6],[7,8,9]]")
print()
print("A) matrix[2][1]")
print("B) matrix[1][2]")
print("C) matrix[1,2]")
print("D) matrix(1)(2)")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! matrix[1][2] = row index 1, column index 2 = 6.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. Python uses [row][col] notation.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("In a nested loop, which loop variable changes faster?")
print()
print("    for i in range(3):")
print("        for j in range(3):")
print("            print(i, j)")
print()
print("A) i (outer)")
print("B) j (inner)")
print("C) Both change at the same speed")
print("D) Neither changes")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! j cycles through all its values before i advances by 1.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. The inner loop variable changes on every step.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("What does this code print?")
print()
print("    for i in range(1, 4):")
print("        print('*' * i)")
print()
print("A) ***")
print("   ***")
print("   ***")
print()
print("B) *")
print("   **")
print("   ***")
print()
print("C) * ** ***")
print()
print("D) Nothing")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! Each iteration prints i stars on its own line: *, **, ***.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. i grows from 1 to 3, so 1/2/3 stars.")
print()

# ── Final Score ─────────────────────────────
print("=" * 50)
print(f"  Final Score: {score}/5")
if score == 5:
    print("  🏆 Perfect score! You're ready for the exercises.")
elif score >= 3:
    print("  👍 Good job! Review mistakes then try the exercises.")
else:
    print("  📖 Review lesson.py again before attempting exercises.")
print("=" * 50)
