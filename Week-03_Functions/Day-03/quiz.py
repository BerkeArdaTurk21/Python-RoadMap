# Week 3 - Day 3: *args & **kwargs — Interactive Quiz

score = 0

print("=" * 52)
print("  Week 3 - Day 3 Quiz: *args & **kwargs")
print("=" * 52)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("Inside a function, what TYPE does *args collect into?")
print()
print("A) list")
print("B) tuple")
print("C) dict")
print("D) set")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! *args collects extra positional arguments into a tuple.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. *args is a tuple, **kwargs is a dict.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("What is printed?")
print()
print("    def f(*nums):")
print("        return sum(nums)")
print()
print("    print(f(1, 2, 3, 4))")
print()
print("A) 10")
print("B) [1, 2, 3, 4]")
print("C) (1, 2, 3, 4)")
print("D) Error")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "A":
    print("✅ Correct! *nums collects (1,2,3,4) — sum is 10.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: A. sum((1,2,3,4)) = 10.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("Which is the CORRECT parameter order?")
print()
print("A) def f(**kwargs, *args, x):")
print("B) def f(*args, x, **kwargs):")
print("C) def f(x, *args, **kwargs):")
print("D) def f(x, **kwargs, *args):")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! Order: positional → *args → keyword-only → **kwargs.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: C. *args must come before **kwargs.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("What does this do?")
print()
print("    nums = [1, 2, 3]")
print("    print(*nums)")
print()
print("A) Prints [1, 2, 3]")
print("B) Prints 1 2 3")
print("C) Prints (1, 2, 3)")
print("D) Error — cannot unpack in print")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! * unpacks the list into separate positional arguments.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. print(*nums) is print(1, 2, 3).")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("What is printed?")
print()
print("    def show(**info):")
print("        for k, v in info.items():")
print("            print(f'{k}={v}')")
print()
print("    data = {'name': 'Berke', 'age': 22}")
print("    show(**data)")
print()
print("A) name=Berke / age=22")
print("B) **data")
print("C) {'name': 'Berke', 'age': 22}")
print("D) Error")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "A":
    print("✅ Correct! **data unpacks the dict into keyword args.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: A. **data → name='Berke', age=22.")
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
