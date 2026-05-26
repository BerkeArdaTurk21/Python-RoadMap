# Week 3 - Day 5: Scope & Closures — Interactive Quiz

score = 0

print("=" * 52)
print("  Week 3 - Day 5 Quiz: Scope & Closures")
print("=" * 52)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("What is the LEGB rule's lookup order?")
print()
print("A) Built-in → Global → Enclosing → Local")
print("B) Local → Enclosing → Global → Built-in")
print("C) Global → Local → Built-in → Enclosing")
print("D) Enclosing → Local → Built-in → Global")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! Python searches Local first, then outward to Built-in.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. L → E → G → B.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("What is printed?")
print()
print("    x = 10")
print("    def f():")
print("        x = 99")
print("    f()")
print("    print(x)")
print()
print("A) 10")
print("B) 99")
print("C) None")
print("D) Error")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "A":
    print("✅ Correct! Inside f(), x = 99 creates a LOCAL — global x is untouched.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: A. Without 'global', the assignment is local.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("Which keyword lets you REBIND a variable from the ENCLOSING")
print("(not global) function scope?")
print()
print("A) global")
print("B) nonlocal")
print("C) outer")
print("D) enclosing")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! 'nonlocal' targets the nearest enclosing function scope.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. 'global' is for module level only.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("What does this print?")
print()
print("    def make_mul(n):")
print("        def mul(x):")
print("            return x * n")
print("        return mul")
print()
print("    triple = make_mul(3)")
print("    print(triple(4))")
print()
print("A) 7")
print("B) 12")
print("C) Error — n is out of scope")
print("D) <function mul>")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! The closure remembers n=3, so triple(4) = 4 * 3 = 12.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. mul keeps n=3 captured.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("What is a CLOSURE?")
print()
print("A) A function that has been decorated")
print("B) A function that remembers variables from its enclosing scope")
print("C) A function with no parameters")
print("D) A function written with the lambda keyword")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! A closure binds names from the surrounding scope when defined.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. Closures capture enclosing variables.")
print()

# ── Final Score ─────────────────────────────
print("=" * 52)
print(f"  Final Score: {score}/5")
if score == 5:
    print("  🏆 Perfect score! You're ready for the exercises.")
elif score >= 3:
    print("  👍 Good job! Review mistakes then try the exercises.")
else:
    print("  📖 Review lesson.py again before attempting exercises.")
print("=" * 52)
