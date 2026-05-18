# Week 2 - Day 4: break / continue / pass — Interactive Quiz

score = 0

print("=" * 50)
print("  Week 2 - Day 4 Quiz: break / continue / pass")
print("=" * 50)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("What is printed by this code?")
print()
print("    for i in range(6):")
print("        if i == 3:")
print("            break")
print("        print(i, end=' ')")
print()
print("A) 0 1 2 3 4 5")
print("B) 0 1 2 3")
print("C) 0 1 2")
print("D) 3 4 5")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! break exits the loop when i==3, so only 0 1 2 are printed.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. break stops before printing 3.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("What is printed by this code?")
print()
print("    for i in range(6):")
print("        if i == 3:")
print("            continue")
print("        print(i, end=' ')")
print()
print("A) 0 1 2 3 4 5")
print("B) 0 1 2")
print("C) 3 4 5")
print("D) 0 1 2 4 5")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "D":
    print("✅ Correct! continue skips the print for i==3 but the loop keeps running.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: D. continue skips i==3, not the whole loop.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("What is the purpose of 'pass' in Python?")
print()
print("A) Exit the current loop")
print("B) Skip to the next iteration")
print("C) Do nothing — act as a placeholder")
print("D) Pause execution for 1 second")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! pass is a no-op that satisfies Python's block requirement.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. pass does nothing — it's a placeholder.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("In nested loops, what does break affect?")
print()
print("A) All loops in the program")
print("B) Only the outermost loop")
print("C) Only the innermost loop it's inside")
print("D) The function it's in")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! break only exits the innermost loop. Use a flag to break outer loops.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. break is local to the innermost loop.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("When does the else block of a for loop run?")
print()
print("    for n in [1, 2, 3]:")
print("        if n == 5:")
print("            break")
print("    else:")
print('        print("done")')
print()
print('A) Never — the else is invalid syntax')
print('B) "done" is printed — loop finished without break')
print('C) "done" is printed only if n == 5')
print("D) Only if the list is empty")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! 5 is never in the list so break never runs — else executes normally.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. else runs when no break was hit.")
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
