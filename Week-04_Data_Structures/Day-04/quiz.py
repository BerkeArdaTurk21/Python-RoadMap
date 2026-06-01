# =============================================================================
# Week 04 - Day 04 | Sets — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 04 - Day 04 Quiz: Sets")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the type of x = {} ?")
print()
print("  A) set")
print("  B) dict")
print("  C) frozenset")
print("  D) tuple")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "B":
    print("✅ Correct! {} creates an empty DICT, not a set.")
    print("   To create an empty set: set()  ← you must use the constructor.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: B.")
    print("   {} → dict.  set() → empty set.  {1,2,3} → set with elements.")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What is the output?")
print()
print("  a = {1, 2, 3, 4, 5}")
print("  b = {4, 5, 6, 7, 8}")
print("  print(a & b)")
print()
print("  A) {1, 2, 3, 4, 5, 6, 7, 8}")
print("  B) {1, 2, 3}")
print("  C) {4, 5}")
print("  D) {1, 2, 3, 6, 7, 8}")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "C":
    print("✅ Correct! & is intersection — elements present in BOTH sets.")
    print("   4 and 5 are the only elements in both a and b.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: C.")
    print("   & = intersection (both).  | = union (either).  - = difference.  ^ = symmetric diff.")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("What is the output?")
print()
print("  s = {3, 1, 4, 1, 5, 9, 2, 6, 5}")
print("  print(len(s))")
print()
print("  A) 9")
print("  B) 8")
print("  C) 7")
print("  D) 6")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "C":
    print("✅ Correct! The set has 9 elements but 1 and 5 are duplicates.")
    print("   Unique values: {1, 2, 3, 4, 5, 6, 9} → length 7.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: C.")
    print("   Sets remove duplicates. 1 appears twice, 5 appears twice → 9 - 2 = 7 unique.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("What is the difference between remove() and discard()?")
print()
print("  A) remove() returns the value; discard() does not")
print("  B) remove() raises KeyError if element missing; discard() does not")
print("  C) discard() raises KeyError if element missing; remove() does not")
print("  D) They are identical")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "B":
    print("✅ Correct! remove() raises KeyError if the element isn't found.")
    print("   discard() silently does nothing — safer when you're not sure if it exists.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: B.")
    print("   remove() → KeyError if missing.  discard() → no error if missing.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("What does a ^ b return for these sets?")
print()
print("  a = {1, 2, 3}")
print("  b = {2, 3, 4}")
print("  print(a ^ b)")
print()
print("  A) {2, 3}")
print("  B) {1, 4}")
print("  C) {1, 2, 3, 4}")
print("  D) {1}")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "B":
    print("✅ Correct! ^ is symmetric difference — elements in ONE set but NOT BOTH.")
    print("   2 and 3 are in both → excluded. 1 is only in a, 4 only in b → {1, 4}.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: B.")
    print("   Symmetric difference = union minus intersection = {1,2,3,4} - {2,3} = {1,4}.")
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
