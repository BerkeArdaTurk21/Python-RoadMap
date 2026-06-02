# =============================================================================
# Week 04 - Day 05 | Comprehensions — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 04 - Day 05 Quiz: Comprehensions")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the output?")
print()
print("  result = [x * 2 for x in range(5) if x % 2 != 0]")
print("  print(result)")
print()
print("  A) [2, 4, 6, 8]")
print("  B) [2, 6]")
print("  C) [0, 2, 4, 6, 8]")
print("  D) [1, 3]")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "B":
    print("✅ Correct! range(5) = 0,1,2,3,4. Odd values: 1, 3. Doubled: 2, 6.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: B.")
    print("   Filter keeps only odd x (1, 3), then doubles them → [2, 6].")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What is the output?")
print()
print("  result = ['even' if x % 2 == 0 else 'odd' for x in range(4)]")
print("  print(result)")
print()
print("  A) ['even', 'even', 'even', 'even']")
print("  B) ['even', 'odd']")
print("  C) ['even', 'odd', 'even', 'odd']")
print("  D) SyntaxError")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "C":
    print("✅ Correct! 0→even, 1→odd, 2→even, 3→odd. if/else BEFORE for = transform, not filter.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: C.")
    print("   'A if cond else B for x in it' → same-length list with values replaced.")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("What does this produce?")
print()
print("  matrix = [[1,2],[3,4],[5,6]]")
print("  flat = [n for row in matrix for n in row]")
print("  print(flat)")
print()
print("  A) [[1,2],[3,4],[5,6]]")
print("  B) [1, 2, 3, 4, 5, 6]")
print("  C) [(1,2),(3,4),(5,6)]")
print("  D) [1, 3, 5]")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "B":
    print("✅ Correct! Nested comprehension: outer loop over rows, inner loop over items.")
    print("   Equivalent to two nested for loops → flattens the 2D list.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: B.")
    print("   'for row in matrix for n in row' = outer then inner, just like nested loops.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("What is the key difference between a list comprehension and a generator expression?")
print()
print("  A) Generator expressions use [] while list comprehensions use ()")
print("  B) List comprehensions can have conditions; generators cannot")
print("  C) List comprehensions build the full list in memory; generators compute values lazily")
print("  D) They are identical — just different syntax")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "C":
    print("✅ Correct! List comp → entire list in memory immediately.")
    print("   Generator → produces values ONE AT A TIME on demand. Much less memory.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: C.")
    print("   [x**2 for x in range(1M)] → 8 MB list.")
    print("   (x**2 for x in range(1M)) → ~200 bytes generator object.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("What is the output?")
print()
print("  prices = {'apple': 1.2, 'banana': 0.5, 'cherry': 3.0}")
print("  result = {k: v * 2 for k, v in prices.items() if v < 2}")
print("  print(result)")
print()
print("  A) {'apple': 2.4, 'banana': 1.0, 'cherry': 6.0}")
print("  B) {'apple': 2.4, 'banana': 1.0}")
print("  C) {'apple': 1.2, 'banana': 0.5}")
print("  D) {'cherry': 6.0}")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "B":
    print("✅ Correct! Filter keeps apple (1.2<2) and banana (0.5<2). Cherry (3.0) excluded.")
    print("   Values are doubled: apple→2.4, banana→1.0.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: B.")
    print("   'if v < 2' filters out cherry. The remaining values are doubled.")
print()

# ── Final Score ──────────────────────────────────────────────
print("=" * 60)
print(f"  Final Score: {score}/5")
print("=" * 60)

if score == 5:
    print("🏆 Perfect score! You're ready for the exercises.")
elif score >= 3:
    print("👍 Good job! Review your mistakes then try the exercises.")
else:
    print("📖 Review lesson.py again before attempting exercises.")
