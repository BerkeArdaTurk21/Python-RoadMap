# Week 3 - Day 2: Default & Keyword Arguments — Interactive Quiz

score = 0

print("=" * 52)
print("  Week 3 - Day 2 Quiz: Default & Keyword Args")
print("=" * 52)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("What is printed?")
print()
print("    def greet(name, msg='Hello'):")
print("        print(f'{msg}, {name}!')")
print()
print("    greet('Berke')")
print()
print("A) Hello, Berke!")
print("B) Berke, Hello!")
print("C) msg, name!")
print("D) Error — msg is required")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "A":
    print("✅ Correct! msg defaults to 'Hello', so 'Hello, Berke!' is printed.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: A. Default values are used when the argument is omitted.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("Which function signature causes a SyntaxError?")
print()
print("A) def f(a, b=10):")
print("B) def f(a=10, b=20):")
print("C) def f(a=10, b):")
print("D) def f(a, b, c=30):")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! A parameter with a default cannot come before one without a default.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: C. Required params must come before optional ones.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("What is printed?")
print()
print("    def power(base, exp):")
print("        return base ** exp")
print()
print("    print(power(exp=3, base=2))")
print()
print("A) 9")
print("B) 6")
print("C) 8")
print("D) Error")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! Keyword args can be in any order: base=2, exp=3 → 2³ = 8.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: C. 2**3 = 8. Keyword args ignore position.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("What is wrong with this function?")
print()
print("    def add_item(item, items=[]):")
print("        items.append(item)")
print("        return items")
print()
print("A) Nothing — it works correctly")
print("B) Lists cannot be used as default values")
print("C) The mutable default list is shared across all calls")
print("D) append() does not work inside functions")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! The list is created once and reused — use None as default instead.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: C. Mutable defaults persist between calls.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("What does a bare * in a parameter list mean?")
print()
print("    def send(to, subject, *, cc='', priority='normal'):")
print()
print("A) Accept unlimited positional arguments")
print("B) Parameters after * must be passed as keyword arguments")
print("C) Parameters after * are ignored")
print("D) The function returns multiple values")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! A bare * forces all following parameters to be keyword-only.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. Parameters after * cannot be positional.")
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
