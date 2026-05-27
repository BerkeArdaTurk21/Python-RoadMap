# =============================================================================
# Week 03 - Day 06 | Recursion — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 03 - Day 06 Quiz: Recursion")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("Which component is REQUIRED to prevent infinite recursion?")
print("  A) A loop inside the function")
print("  B) A base case that stops the recursion")
print("  C) A return type annotation")
print("  D) A global variable")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "B":
    print("✅ Correct! The base case is what stops recursion — without it you get RecursionError.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: B.")
    print("   The base case is the stopping condition — it is mandatory in every recursive function.")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What is the output of the following code?")
print()
print("  def factorial(n):")
print("      if n == 0:")
print("          return 1")
print("      return n * factorial(n - 1)")
print()
print("  print(factorial(4))")
print()
print("  A) 10")
print("  B) 16")
print("  C) 24")
print("  D) 0")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "C":
    print("✅ Correct! 4 * 3 * 2 * 1 * 1 = 24.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: C.")
    print("   factorial(4) = 4 * factorial(3) = 4 * 3 * 2 * 1 * 1 = 24.")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("What error does Python raise when recursion depth exceeds the limit?")
print("  A) OverflowError")
print("  B) MemoryError")
print("  C) RecursionError")
print("  D) RuntimeError")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "C":
    print("✅ Correct! Python raises RecursionError when the call stack exceeds ~1000 frames.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: C.")
    print("   RecursionError: maximum recursion depth exceeded.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("For the Fibonacci function defined as:")
print("  F(0) = 0,  F(1) = 1,  F(n) = F(n-1) + F(n-2)")
print()
print("What is fibonacci(5)?")
print("  A) 3")
print("  B) 5")
print("  C) 8")
print("  D) 13")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "B":
    print("✅ Correct! F(5) = F(4)+F(3) = 3+2 = 5. Sequence: 0,1,1,2,3,5...")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: B.")
    print("   Sequence: F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("Which situation is BEST suited for recursion?")
print("  A) Printing numbers from 1 to 100")
print("  B) Flattening a list with unknown nesting depth")
print("  C) Summing two integers")
print("  D) Checking if a number is even")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "B":
    print("✅ Correct! Nested structures of unknown depth are a classic recursion use case.")
    print("   A simple loop can't handle arbitrary nesting; recursion handles it naturally.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: B.")
    print("   Recursion shines when the problem structure is recursive itself (trees, nested data).")
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
