# =============================================================================
# Week 07 - Day 07 | Weekly Review Quiz
# =============================================================================
# Topics: Import system & venv, os module, sys & argparse,
#         datetime, random, regular expressions (re)
# =============================================================================

score = 0
print("=" * 62)
print("  Week 07 — Modules & Packages | Weekly Review Quiz")
print("=" * 62)
print()

# ─── PART A: Multiple Choice (10 questions, 1 pt each) ────────────────────────

print("── PART A: Multiple Choice ──")
print()

# Q1
print("Q1. What is the value of __name__ when a script is run directly")
print("    (not imported)?")
print("      A) the file name   B) '__main__'   C) '__init__'   D) None")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! Direct execution sets __name__ to '__main__'."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q2
print("Q2. Which import style lets you control what 'from module import *'")
print("    exposes?")
print("      A) __all__   B) __exports__   C) __public__   D) __dir__")
a = input("    Your answer: ").strip().upper()
if a == "A":
    print("    ✅ Correct! __all__ is a list of names exported by '*'."); score += 1
else:
    print("    ❌ Correct answer: A.")
print()

# Q3
print("Q3. Which os function returns the current working directory?")
print("      A) os.path.cwd()   B) os.getcwd()   C) os.pwd()   D) os.curdir()")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! os.getcwd() returns the current working dir."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q4
print("Q4. In a script, what does sys.argv[0] contain?")
print("      A) the first command-line argument")
print("      B) the script name / path")
print("      C) the number of arguments")
print("      D) always an empty string")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! argv[0] is the script name; real args start at [1]."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q5
print("Q5. With argparse, how do you make an argument optional with a flag?")
print("      A) parser.add_argument('name')")
print("      B) parser.add_argument('--name')")
print("      C) parser.add_optional('name')")
print("      D) parser.flag('name')")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! A leading '--' makes it an optional flag."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q6
print("Q6. What does (datetime(2026, 6, 24) - datetime(2026, 6, 20)) return?")
print("      A) 4              B) a timedelta of 4 days")
print("      C) '4 days'       D) TypeError")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! Subtracting datetimes yields a timedelta."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q7
print("Q7. Which strftime code formats a 4-digit year?")
print("      A) %y   B) %Y   C) %yyyy   D) %year")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! %Y = 4-digit year, %y = 2-digit year."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q8
print("Q8. Which random function picks a single element from a sequence?")
print("      A) random.sample()   B) random.shuffle()")
print("      C) random.choice()   D) random.randint()")
a = input("    Your answer: ").strip().upper()
if a == "C":
    print("    ✅ Correct! random.choice(seq) returns one element."); score += 1
else:
    print("    ❌ Correct answer: C.")
print()

# Q9
print("Q9. Why call random.seed(42) before generating random numbers?")
print("      A) To make results faster")
print("      B) To make the sequence reproducible / deterministic")
print("      C) To pick truly random numbers")
print("      D) To reset the random module to defaults")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! Same seed → same sequence, great for tests."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q10
print("Q10. In regex, what does the metacharacter \\d match?")
print("      A) any word character   B) a single digit (0-9)")
print("      C) any whitespace       D) the literal letter 'd'")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! \\d matches one digit; \\D is the opposite."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# ─── PART B: Code Challenges (5 questions, 1 pt each) ─────────────────────────

print("── PART B: Code Challenges ──")
print("(Type your answer or press Enter to see the solution)")
print()

# CB1
print("CB1. Write the standard guard so code runs only when executed directly.")
ans = input("     Your answer: ").strip()
print("     Solution: if __name__ == '__main__':")
correct = "__name__" in ans and "__main__" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: if __name__ == '__main__':")
print()

# CB2
print("CB2. Use os to build a path 'logs/app.txt' that works on any OS.")
ans = input("     Your answer: ").strip()
print("     Solution: os.path.join('logs', 'app.txt')")
print("     (or pathlib: Path('logs') / 'app.txt')")
correct = ("os.path.join" in ans) or ("Path(" in ans and "/" in ans)
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: os.path.join() builds platform-correct paths.")
print()

# CB3
print("CB3. Build an argparse parser with a required positional 'file'")
print("     and an optional '--verbose' flag (store_true).")
ans = input("     Your answer: ").strip()
print("     Solution:")
print("       p = argparse.ArgumentParser()")
print("       p.add_argument('file')")
print("       p.add_argument('--verbose', action='store_true')")
correct = "add_argument" in ans and "store_true" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: positional 'file' + --verbose with action='store_true'.")
print()

# CB4
print("CB4. Format the current date as 'YYYY-MM-DD' using datetime.")
ans = input("     Your answer: ").strip()
print("     Solution: datetime.now().strftime('%Y-%m-%d')")
correct = "strftime" in ans and "%Y" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: datetime.now().strftime('%Y-%m-%d')")
print()

# CB5
print("CB5. Write a regex with re.findall that extracts every integer")
print("     from the string '3 cats, 12 dogs, 7 birds'.")
ans = input("     Your answer: ").strip()
print("     Solution: re.findall(r'\\d+', '3 cats, 12 dogs, 7 birds')")
print("     -> ['3', '12', '7']")
correct = "findall" in ans and "\\d" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: re.findall(r'\\d+', text)")
print()

# ─── Final Score ───────────────────────────────────────────────────────────────
print("=" * 62)
print(f"  Final Score: {score}/15")
print("=" * 62)
if score == 15:
    print("  Perfect! You've mastered Week 7.")
elif score >= 11:
    print("  Great work! Ready for Week 8.")
elif score >= 8:
    print("  Good effort. Review the topics where you lost points.")
else:
    print("  Re-read the lessons and retry the exercises before moving on.")
