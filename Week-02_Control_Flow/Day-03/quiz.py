# Week 2 - Day 3: while Loops — Interactive Quiz

score = 0

print("=" * 50)
print("  Week 2 - Day 3 Quiz: while Loops")
print("=" * 50)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("What is printed by this code?")
print()
print("    x = 1")
print("    while x < 4:")
print("        print(x, end=' ')")
print("        x += 1")
print()
print("A) 1 2 3 4")
print("B) 1 2 3")
print("C) 0 1 2 3")
print("D) Nothing")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! x starts at 1 and stops before 4, so 1 2 3 is printed.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. The condition x < 4 stops the loop when x reaches 4.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("What causes an infinite loop?")
print()
print("A) Using break inside the loop")
print("B) The loop condition never becomes False")
print("C) Using while True with a break")
print("D) Forgetting the else clause")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! If the condition stays True forever, the loop never exits.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. Always ensure the loop variable changes.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("What does 'while True:' mean?")
print()
print("A) The loop runs exactly once")
print("B) The loop runs only if True is defined")
print("C) The loop runs indefinitely until a break is hit")
print("D) The loop runs until False is returned")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! 'while True' is an intentional infinite loop — always paired with break.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. It loops forever until break exits it.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("When does the else clause of a while loop run?")
print()
print("A) When the loop body raises an exception")
print("B) When break exits the loop")
print("C) Every time the loop body runs")
print("D) When the condition becomes False normally")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "D":
    print("✅ Correct! else runs after normal loop completion — break bypasses it.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: D. break skips the else block.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("What is printed?")
print()
print("    i = 0")
print("    while i < 5:")
print("        i += 1")
print("        if i == 3:")
print("            continue")
print("        print(i, end=' ')")
print()
print("A) 1 2 3 4 5")
print("B) 0 1 2 4 5")
print("C) 1 2 4 5")
print("D) 1 2 3 4")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! continue skips the print when i==3, so 3 is never printed.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. continue skips to the next iteration.")
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
