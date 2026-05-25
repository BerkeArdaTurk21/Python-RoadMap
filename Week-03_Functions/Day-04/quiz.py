# Week 3 - Day 4: Lambda Functions — Interactive Quiz

score = 0

print("=" * 52)
print("  Week 3 - Day 4 Quiz: Lambda Functions")
print("=" * 52)
print()

# ── Question 1 ──────────────────────────────
print("Question 1:")
print("What does this print?")
print()
print("    f = lambda x, y: x * y")
print("    print(f(3, 4))")
print()
print("A) 7")
print("B) 12")
print("C) (3, 4)")
print("D) Error — lambda cannot take two args")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! lambda x, y: x * y returns 3 * 4 = 12.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. Lambdas can take any number of arguments.")
print()

# ── Question 2 ──────────────────────────────
print("Question 2:")
print("What does map() return in Python 3?")
print()
print("A) A list")
print("B) A tuple")
print("C) A map iterator")
print("D) A dict")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! map() returns an iterator — wrap with list() to materialize.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: C. In Python 3, map() is lazy.")
print()

# ── Question 3 ──────────────────────────────
print("Question 3:")
print("What is printed?")
print()
print("    nums = [1, 2, 3, 4, 5]")
print("    result = list(filter(lambda x: x > 2, nums))")
print("    print(result)")
print()
print("A) [1, 2]")
print("B) [3, 4, 5]")
print("C) [True, True, True]")
print("D) [2, 3, 4, 5]")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! filter keeps items where the lambda returns truthy — only 3, 4, 5.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. filter keeps items where x > 2.")
print()

# ── Question 4 ──────────────────────────────
print("Question 4:")
print("What is printed?")
print()
print("    words = ['apple', 'kiwi', 'banana']")
print("    print(sorted(words, key=len))")
print()
print("A) ['apple', 'banana', 'kiwi']")
print("B) ['banana', 'apple', 'kiwi']")
print("C) ['kiwi', 'apple', 'banana']")
print("D) ['apple', 'kiwi', 'banana']")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "C":
    print("✅ Correct! Sorted by len: 'kiwi'(4) < 'apple'(5) < 'banana'(6).")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: C. key=len sorts by string length.")
print()

# ── Question 5 ──────────────────────────────
print("Question 5:")
print("Which is INCORRECT about lambdas?")
print()
print("A) A lambda is an expression, not a statement")
print("B) Lambdas can have multiple statements with newlines")
print("C) A lambda can take *args and **kwargs")
print("D) The result of a lambda is the value of its expression")
print()
answer = input("Your answer (A/B/C/D): ").strip().upper()
if answer == "B":
    print("✅ Correct! Lambdas are SINGLE expressions — no statements, no newlines.")
    score += 1
else:
    print(f"❌ Wrong! You chose {answer}. Correct: B. Lambdas are limited to one expression.")
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
