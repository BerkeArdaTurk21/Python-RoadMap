# =============================================================================
# Week 04 - Day 02 | Tuples — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 04 - Day 02 Quiz: Tuples")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the type of the following variable?")
print()
print("  x = (42)")
print()
print("  A) tuple")
print("  B) int")
print("  C) list")
print("  D) set")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "B":
    print("✅ Correct! (42) is just parentheses around an integer — it is an int, not a tuple.")
    print("   To make a single-element tuple: (42,)  ← the comma is mandatory.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: B.")
    print("   (42) = int. (42,) = tuple. The comma makes the difference.")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What is printed?")
print()
print("  a, *b, c = (1, 2, 3, 4, 5)")
print("  print(a, b, c)")
print()
print("  A) 1 [2, 3, 4] 5")
print("  B) 1 (2, 3, 4) 5")
print("  C) 1 2 5")
print("  D) ValueError")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "A":
    print("✅ Correct! *b captures the 'middle' items as a LIST: [2, 3, 4].")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: A.")
    print("   Extended unpacking: a=1, c=5, *b catches everything in between as a list.")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("Which of the following will raise a TypeError?")
print()
print("  t = (1, 2, 3)")
print()
print("  A) print(t[0])")
print("  B) print(t[-1])")
print("  C) t[0] = 99")
print("  D) print(len(t))")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "C":
    print("✅ Correct! Tuples are immutable — t[0] = 99 raises TypeError.")
    print("   You cannot change, add, or remove elements after creation.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: C.")
    print("   Indexing (A, B) and len() (D) are all valid on tuples.")
    print("   Only assignment raises TypeError: 'tuple' object does not support item assignment.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("What does this function actually return?")
print()
print("  def stats(numbers):")
print("      return min(numbers), max(numbers), sum(numbers)")
print()
print("  result = stats([3, 1, 4, 1, 5])")
print("  print(type(result))")
print()
print("  A) list")
print("  B) dict")
print("  C) tuple")
print("  D) int")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "C":
    print("✅ Correct! When a function returns multiple comma-separated values,")
    print("   Python automatically packs them into a TUPLE.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: C.")
    print("   return a, b, c  is shorthand for  return (a, b, c).")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("Which of these can be used as a dictionary KEY?")
print()
print("  A) [1, 2, 3]")
print("  B) {1, 2, 3}")
print("  C) (1, 2, 3)")
print("  D) {'a': 1}")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "C":
    print("✅ Correct! Tuples are HASHABLE (immutable), so they can be dict keys.")
    print("   Lists and sets are mutable/unhashable — TypeError if used as dict keys.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: C.")
    print("   Dict keys must be hashable. Tuples are hashable; lists and sets are not.")
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
