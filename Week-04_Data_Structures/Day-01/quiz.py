# =============================================================================
# Week 04 - Day 01 | Lists — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 04 - Day 01 Quiz: Lists")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the output of the following code?")
print()
print("  fruits = ['apple', 'banana', 'cherry']")
print("  print(fruits[-1])")
print()
print("  A) apple")
print("  B) banana")
print("  C) cherry")
print("  D) IndexError")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "C":
    print("✅ Correct! Negative index -1 always refers to the last element.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: C.")
    print("   fruits[-1] = 'cherry'. Negative indexing counts from the end.")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What does this slice return?")
print()
print("  nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
print("  print(nums[2:7:2])")
print()
print("  A) [2, 3, 4, 5, 6]")
print("  B) [2, 4, 6]")
print("  C) [1, 3, 5]")
print("  D) [2, 5]")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "B":
    print("✅ Correct! Start=2, stop=7 (excluded), step=2 → indices 2, 4, 6 → values 2, 4, 6.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: B.")
    print("   nums[2:7:2] picks every 2nd element from index 2 up to (not including) 7.")
    print("   Indices: 2→2, 4→4, 6→6. Result: [2, 4, 6].")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("What is the difference between list.sort() and sorted(list)?")
print()
print("  A) sort() returns a new sorted list; sorted() modifies the original")
print("  B) sort() modifies the original in place; sorted() returns a new list")
print("  C) They are identical — both modify in place")
print("  D) sorted() only works with numbers")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "B":
    print("✅ Correct! sort() is in-place (returns None). sorted() leaves the original unchanged.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: B.")
    print("   list.sort() → modifies in place, returns None.")
    print("   sorted(list) → returns a new sorted list, original unchanged.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("What is the output?")
print()
print("  a = [1, 2, 3]")
print("  b = a")
print("  b.append(4)")
print("  print(a)")
print()
print("  A) [1, 2, 3]")
print("  B) [1, 2, 3, 4]")
print("  C) [4]")
print("  D) TypeError")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "B":
    print("✅ Correct! b = a does NOT copy — both variables point to the SAME list object.")
    print("   Appending to b also changes a.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: B.")
    print("   Assignment creates a reference, not a copy. a and b point to the same list.")
    print("   Use a.copy() or a[:] to get an independent copy.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("Which method removes AND RETURNS the last element of a list?")
print()
print("  A) remove()")
print("  B) delete()")
print("  C) pop()")
print("  D) discard()")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "C":
    print("✅ Correct! pop() removes and returns the last element (or the element at a given index).")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: C.")
    print("   pop() → removes and returns the last element.")
    print("   remove(value) → removes first occurrence but returns None.")
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
