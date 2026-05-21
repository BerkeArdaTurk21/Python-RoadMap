# Week 2 - Day 7: Weekly Review Quiz
# Covers: if/elif/else, for loops, while loops,
#         break/continue/pass, nested loops, match/case

score = 0
total_questions = 15

print("=" * 55)
print("  Week 2 Weekly Review Quiz — Control Flow")
print("=" * 55)
print("  10 Multiple Choice + 5 Code Challenges")
print("=" * 55)
print()

# ════════════════════════════════════════════
# PART 1 — MULTIPLE CHOICE (10 questions)
# ════════════════════════════════════════════
print("── PART 1: Multiple Choice ──\n")

# ── MCQ 1 ───────────────────────────────────
print("Q1. What is printed?")
print()
print("    score = 75")
print("    if score >= 90:   print('A')")
print("    elif score >= 80: print('B')")
print("    elif score >= 70: print('C')")
print("    else:             print('F')")
print()
print("A) A   B) B   C) C   D) F")
answer = input("Your answer: ").strip().upper()
if answer == "C":
    print("✅ Correct! 75 >= 70 is the first True branch → C.")
    score += 1
else:
    print(f"❌ Wrong! Correct: C. 75 >= 70 is True, so C is printed.")
print()

# ── MCQ 2 ───────────────────────────────────
print("Q2. Which value is FALSY in Python?")
print()
print("A) [0]   B) 'False'   C) 0.0   D) -1")
answer = input("Your answer: ").strip().upper()
if answer == "C":
    print("✅ Correct! 0.0 is falsy. [0] is a non-empty list (truthy), 'False' is a non-empty string (truthy), -1 is truthy.")
    score += 1
else:
    print(f"❌ Wrong! Correct: C. Only 0, 0.0, '', [], {{}}, None, False are falsy.")
print()

# ── MCQ 3 ───────────────────────────────────
print("Q3. What does range(2, 10, 3) produce?")
print()
print("A) [2, 5, 8, 11]   B) [2, 5, 8]   C) [2, 4, 6, 8]   D) [3, 6, 9]")
answer = input("Your answer: ").strip().upper()
if answer == "B":
    print("✅ Correct! Starts at 2, steps by 3, stops before 10: 2, 5, 8.")
    score += 1
else:
    print(f"❌ Wrong! Correct: B. range(2, 10, 3) → 2, 5, 8.")
print()

# ── MCQ 4 ───────────────────────────────────
print("Q4. What is printed?")
print()
print("    for i, v in enumerate(['a','b','c'], start=1):")
print("        print(i, v)")
print()
print("A) 0 a / 1 b / 2 c")
print("B) 1 a / 2 b / 3 c")
print("C) a 1 / b 2 / c 3")
print("D) Error")
answer = input("Your answer: ").strip().upper()
if answer == "B":
    print("✅ Correct! start=1 shifts the index, so pairs are (1,'a'), (2,'b'), (3,'c').")
    score += 1
else:
    print(f"❌ Wrong! Correct: B. enumerate with start=1 begins counting at 1.")
print()

# ── MCQ 5 ───────────────────────────────────
print("Q5. What is the output?")
print()
print("    x = 10")
print("    while x > 0:")
print("        x -= 4")
print("    print(x)")
print()
print("A) 0   B) 2   C) -2   D) 4")
answer = input("Your answer: ").strip().upper()
if answer == "C":
    print("✅ Correct! 10→6→2→-2. When x=-2 the condition x>0 is False, loop exits.")
    score += 1
else:
    print(f"❌ Wrong! Correct: C. 10-4=6, 6-4=2, 2-4=-2 → loop exits, prints -2.")
print()

# ── MCQ 6 ───────────────────────────────────
print("Q6. What does 'continue' do inside a loop?")
print()
print("A) Exits the loop immediately")
print("B) Skips to the next iteration")
print("C) Does nothing — placeholder only")
print("D) Restarts the loop from the beginning")
answer = input("Your answer: ").strip().upper()
if answer == "B":
    print("✅ Correct! continue skips the rest of the current iteration and rechecks the condition.")
    score += 1
else:
    print(f"❌ Wrong! Correct: B. break exits, pass does nothing, continue skips one iteration.")
print()

# ── MCQ 7 ───────────────────────────────────
print("Q7. How many times does 'hello' print?")
print()
print("    for i in range(3):")
print("        for j in range(2):")
print("            print('hello')")
print()
print("A) 2   B) 3   C) 5   D) 6")
answer = input("Your answer: ").strip().upper()
if answer == "D":
    print("✅ Correct! 3 outer × 2 inner = 6 total iterations.")
    score += 1
else:
    print(f"❌ Wrong! Correct: D. Total = outer_count × inner_count = 3 × 2 = 6.")
print()

# ── MCQ 8 ───────────────────────────────────
print("Q8. When does the else block of a for loop run?")
print()
print("A) When the loop body raises an error")
print("B) Every time the loop body executes")
print("C) When the loop exits via break")
print("D) When the loop completes without hitting break")
answer = input("Your answer: ").strip().upper()
if answer == "D":
    print("✅ Correct! The else runs after normal loop completion — break bypasses it.")
    score += 1
else:
    print(f"❌ Wrong! Correct: D. break skips the else block.")
print()

# ── MCQ 9 ───────────────────────────────────
print("Q9. What Python version introduced match / case?")
print()
print("A) 3.8   B) 3.9   C) 3.10   D) 3.11")
answer = input("Your answer: ").strip().upper()
if answer == "C":
    print("✅ Correct! Structural pattern matching (PEP 634) was added in Python 3.10.")
    score += 1
else:
    print(f"❌ Wrong! Correct: C. match/case requires Python 3.10+.")
print()

# ── MCQ 10 ──────────────────────────────────
print("Q10. What is printed?")
print()
print("    val = (0, 7)")
print("    match val:")
print("        case (0, 0): print('origin')")
print("        case (0, y): print(f'y={y}')")
print("        case (x, 0): print(f'x={x}')")
print("        case (x, y): print(f'{x},{y}')")
print()
print("A) origin   B) y=7   C) x=0   D) 0,7")
answer = input("Your answer: ").strip().upper()
if answer == "B":
    print("✅ Correct! (0,7) matches case (0, y) with y=7 → prints 'y=7'.")
    score += 1
else:
    print(f"❌ Wrong! Correct: B. First element is 0 so (0, y) matches with y=7.")
print()

# ════════════════════════════════════════════
# PART 2 — CODE CHALLENGES (5 questions)
# ════════════════════════════════════════════
print("─" * 55)
print("── PART 2: Code Challenges ──\n")

# ── Challenge 1 ─────────────────────────────
print("Challenge 1:")
print("What is the output of this code?")
print()
print("    result = []")
print("    for i in range(1, 6):")
print("        if i % 2 != 0:")
print("            result.append(i * i)")
print("    print(result)")
print()
answer = input("Your answer: ").strip()
if answer in ["[1, 9, 25]", "[1,9,25]"]:
    print("✅ Correct! Odd numbers 1,3,5 squared → [1, 9, 25].")
    score += 1
else:
    print(f"❌ Wrong! Correct: [1, 9, 25]. Odd numbers in range(1,6) are 1,3,5 → 1²=1, 3²=9, 5²=25.")
print()

# ── Challenge 2 ─────────────────────────────
print("Challenge 2:")
print("What is printed?")
print()
print("    n = 1")
print("    while n <= 16:")
print("        n *= 2")
print("    print(n)")
print()
answer = input("Your answer: ").strip()
if answer == "32":
    print("✅ Correct! 1→2→4→8→16→32. When n=32, 32<=16 is False, loop exits.")
    score += 1
else:
    print(f"❌ Wrong! Correct: 32. n doubles each step: 1,2,4,8,16,32 → exits when 32>16.")
print()

# ── Challenge 3 ─────────────────────────────
print("Challenge 3:")
print("What does this print?")
print()
print("    for i in range(5):")
print("        if i == 3:")
print("            break")
print("    else:")
print("        print('done')")
print("    print('end')")
print()
print("A) done / end   B) end only   C) done only   D) Nothing")
answer = input("Your answer: ").strip().upper()
if answer == "B":
    print("✅ Correct! break exits the loop → else is skipped. Only 'end' prints.")
    score += 1
else:
    print(f"❌ Wrong! Correct: B. break bypasses the else block, then 'end' prints.")
print()

# ── Challenge 4 ─────────────────────────────
print("Challenge 4:")
print("What is the final value of total?")
print()
print("    matrix = [[1,2],[3,4],[5,6]]")
print("    total = 0")
print("    for row in matrix:")
print("        for val in row:")
print("            if val % 2 == 0:")
print("                total += val")
print("    print(total)")
print()
answer = input("Your answer: ").strip()
if answer == "12":
    print("✅ Correct! Even values: 2+4+6 = 12.")
    score += 1
else:
    print(f"❌ Wrong! Correct: 12. Even values in the matrix are 2, 4, 6 → sum = 12.")
print()

# ── Challenge 5 ─────────────────────────────
print("Challenge 5:")
print("What is printed?")
print()
print("    items = ['a', 'b', 'c', 'd']")
print("    for i, item in enumerate(items):")
print("        if item == 'c':")
print("            print(f'found at {i}')")
print("            break")
print()
answer = input("Your answer: ").strip()
if answer in ["found at 2", "found at 2\n", "'found at 2'"]:
    print("✅ Correct! 'c' is at index 2 → prints 'found at 2'.")
    score += 1
else:
    print(f"❌ Wrong! Correct: found at 2. enumerate gives index 2 for 'c'.")
print()

# ════════════════════════════════════════════
# FINAL SCORE
# ════════════════════════════════════════════
print("=" * 55)
print(f"  Final Score: {score}/{total_questions}")
percentage = (score / total_questions) * 100
print(f"  Percentage:  {percentage:.0f}%")
print()
if score == total_questions:
    print("  🏆 Perfect! You've mastered Week 2 Control Flow.")
elif score >= 12:
    print("  👍 Great job! You're ready for Week 3.")
elif score >= 9:
    print("  📚 Good effort. Review the topics you missed.")
else:
    print("  🔁 Go back and re-read the lessons before Week 3.")
print("=" * 55)
