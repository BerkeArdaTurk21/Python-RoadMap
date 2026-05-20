# Week 2 - Day 6: match / case — Interactive Quiz

score = 0

print("=" * 50)
print("  Week 2 - Day 6 Quiz: match / case")
print("=" * 50)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("What Python version introduced match / case?")
print()
print("A) Python 3.7")
print("B) Python 3.8")
print("C) Python 3.9")
print("D) Python 3.10")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "D":
    print("✅ Correct! Structural pattern matching was introduced in Python 3.10 (PEP 634).")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: D. match/case requires Python 3.10+.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("What does 'case _:' mean in a match statement?")
print()
print("A) Match only None values")
print("B) Match only empty strings")
print("C) Match anything — the default/wildcard case")
print("D) Skip this branch always")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! case _ is the wildcard — it matches any value not caught above, like 'else'.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. _ is the catch-all wildcard pattern.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("How do you match multiple values in one case branch?")
print()
print("A) case 1, 2, 3:")
print("B) case [1, 2, 3]:")
print("C) case 1 | 2 | 3:")
print("D) case (1 or 2 or 3):")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! The | operator lets you match multiple values in one case branch.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. Use | to combine patterns.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("What is a guard clause in match / case?")
print()
print("A) A case that always runs last")
print("B) An 'if' condition added after a pattern for extra filtering")
print("C) A special keyword to protect sensitive data")
print("D) A way to skip the match statement entirely")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! A guard is 'case pattern if condition:' — both must be True to match.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. Guards add extra conditions to a pattern.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("What does this code print?")
print()
print("    point = (0, 5)")
print("    match point:")
print("        case (0, 0):")
print('            print("Origin")')
print("        case (0, y):")
print('            print(f"y-axis at {y}")')
print("        case (x, 0):")
print('            print(f"x-axis at {x}")')
print("        case (x, y):")
print('            print(f"Point {x},{y}")')
print()
print('A) "Origin"')
print('B) "y-axis at 5"')
print('C) "x-axis at 0"')
print('D) "Point 0,5"')
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! (0, 5) matches case (0, y) with y=5, printing 'y-axis at 5'.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. x=0 matches the second pattern.")
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
