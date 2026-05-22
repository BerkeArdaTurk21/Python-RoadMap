# Week 3 - Day 1: Defining Functions — Interactive Quiz

score = 0

print("=" * 50)
print("  Week 3 - Day 1 Quiz: Defining Functions")
print("=" * 50)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("What keyword is used to define a function in Python?")
print()
print("A) function")
print("B) func")
print("C) def")
print("D) define")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! 'def' is the keyword used to define a function.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: C. Python uses 'def function_name():'.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("What does a function return if it has no return statement?")
print()
print("A) 0")
print("B) False")
print("C) An empty string")
print("D) None")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "D":
    print("✅ Correct! A function with no return statement implicitly returns None.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: D. Python returns None by default.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("What is a docstring?")
print()
print("A) A comment starting with #")
print("B) A string literal on the first line of a function body")
print("C) A variable that stores the function name")
print("D) A special return type annotation")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! A docstring is a string on the first line of a function that describes it.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. Access it with func.__doc__.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("What is the output?")
print()
print("    def add(a, b):")
print("        return a + b")
print()
print("    x = add(3, 4)")
print("    print(x * 2)")
print()
print("A) 7")
print("B) 14")
print("C) 34")
print("D) Error")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! add(3,4) returns 7, then 7 * 2 = 14.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. 3+4=7, 7×2=14.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("What is printed?")
print()
print("    def swap(a, b):")
print("        return b, a")
print()
print("    x, y = swap(10, 20)")
print("    print(x, y)")
print()
print("A) 10 20")
print("B) 20 10")
print("C) (20, 10)")
print("D) Error")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! swap returns (20, 10), unpacked into x=20, y=10.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct answer: B. Tuple unpacking gives x=20, y=10.")
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
