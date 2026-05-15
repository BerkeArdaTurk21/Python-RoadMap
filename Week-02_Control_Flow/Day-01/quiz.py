# Week 2 - Day 1: if / elif / else — Interactive Quiz

score = 0

print("=" * 50)
print("  Week 2 - Day 1 Quiz: if / elif / else")
print("=" * 50)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("What will this code print?")
print()
print("    x = 10")
print("    if x > 5:")
print('        print("big")')
print("    else:")
print('        print("small")')
print()
print("A) small")
print("B) big")
print("C) Nothing")
print("D) Error")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! 10 > 5 is True, so 'big' is printed.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. 10 > 5 is True, so the if block runs.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("Which of the following is a FALSY value in Python?")
print()
print("A) 1")
print('B) "hello"')
print("C) []")
print("D) True")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! An empty list [] is falsy. Non-empty collections are truthy.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. [] (empty list) is falsy.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("How many elif branches can an if/elif/else chain have?")
print()
print("A) Only 1")
print("B) Maximum 3")
print("C) Maximum 10")
print("D) As many as needed")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "D":
    print("✅ Correct! You can chain as many elif blocks as your logic requires.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: D. Python has no limit on elif branches.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("What does this expression evaluate to?")
print()
print('    status = "adult" if 20 >= 18 else "minor"')
print()
print('A) "minor"')
print('B) "adult"')
print("C) True")
print("D) 20")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! 20 >= 18 is True, so the ternary returns 'adult'.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. The condition is True so 'adult' is assigned.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("What will this code print?")
print()
print("    a = 5")
print("    b = 10")
print("    if a > 3 and b < 5:")
print('        print("yes")')
print("    else:")
print('        print("no")')
print()
print('A) "yes"')
print('B) "no"')
print("C) Nothing")
print("D) Error")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! a > 3 is True but b < 5 is False. True AND False = False, so else runs.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. Both conditions must be True for 'and'.")
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
