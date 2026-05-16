# Week 2 - Day 2: for Loops — Interactive Quiz

score = 0

print("=" * 50)
print("  Week 2 - Day 2 Quiz: for Loops")
print("=" * 50)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("What does range(2, 8, 2) produce?")
print()
print("A) [2, 4, 6, 8]")
print("B) [2, 4, 6]")
print("C) [2, 3, 4, 5, 6, 7]")
print("D) [0, 2, 4, 6]")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! range(2, 8, 2) gives 2, 4, 6 — stops before 8.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. range stops BEFORE the end value.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("What does enumerate(['a', 'b', 'c'], start=1) produce?")
print()
print("A) (0,'a'), (1,'b'), (2,'c')")
print("B) (1,'a'), (2,'b'), (3,'c')")
print("C) ('a',1), ('b',2), ('c',3)")
print("D) [1, 2, 3]")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! enumerate with start=1 gives (1,'a'), (2,'b'), (3,'c').")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. start=1 shifts the index to begin at 1.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("What happens when you iterate over a dictionary?")
print()
print("A) You get the values")
print("B) You get (key, value) tuples")
print("C) You get the keys")
print("D) You get the indices")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! Iterating a dict by default gives its keys. Use .items() for key-value pairs.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. Use .values() or .items() for more.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("What does zip() do when the two lists have different lengths?")
print()
print("A) Raises an error")
print("B) Pads the shorter list with None")
print("C) Stops at the longest list")
print("D) Stops at the shortest list")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "D":
    print("✅ Correct! zip() stops as soon as the shortest iterable is exhausted.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: D. Use itertools.zip_longest to pad instead.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("When does the else clause of a for loop run?")
print()
print("A) When the loop body raises an error")
print("B) When the loop is interrupted by break")
print("C) When the loop finishes without hitting break")
print("D) When the loop runs zero iterations")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! The else runs after normal loop completion — break skips it.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. break bypasses the else block.")
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
