# =============================================================================
# Week 06 - Day 03 | Working with Paths — Quiz
# =============================================================================
score = 0
print("=" * 60)
print("  Week 06 - Day 03 Quiz: Working with Paths")
print("=" * 60)
print()

print("Question 1:")
print("Which pathlib expression correctly joins 'data', '2024', 'report.csv'?")
print()
print("  A) Path('data') + '2024' + 'report.csv'")
print("  B) Path('data') / '2024' / 'report.csv'")
print("  C) Path.join('data', '2024', 'report.csv')")
print("  D) Path('data', '2024', 'report.csv')")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "B":
    print("✅ Correct! pathlib overloads / as the path join operator."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   Path objects use / — cleaner than os.path.join().")
print()

print("Question 2:")
print("Given p = Path('/home/user/data/report.csv'), what is p.stem?")
print()
print("  A) '.csv'    B) 'report.csv'    C) 'report'    D) '/home/user/data'")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "C":
    print("✅ Correct! .stem is the filename WITHOUT the extension."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   .name = 'report.csv', .stem = 'report', .suffix = '.csv'")
print()

print("Question 3:")
print("Which method lists all files matching '*.py' in a directory")
print("AND all its subdirectories recursively?")
print()
print("  A) path.glob('*.py')    B) path.iterdir('*.py')")
print("  C) path.rglob('*.py')   D) path.find('*.py')")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "C":
    print("✅ Correct! rglob() is recursive glob — it walks all subdirs."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   glob() is single-dir; rglob() searches recursively.")
print()

print("Question 4:")
print("What does Path.mkdir(exist_ok=True) do that")
print("Path.mkdir() (without exist_ok) does NOT?")
print()
print("  A) Creates parent directories automatically")
print("  B) Skips the error if the directory already exists")
print("  C) Creates the directory with specific permissions")
print("  D) Returns True if the directory existed already")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()
if ans4 == "B":
    print("✅ Correct! Without exist_ok=True, mkdir() raises FileExistsError"); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   exist_ok=True makes it idempotent (safe to call multiple times).")
print()

print("Question 5:")
print("What is the difference between os.path and pathlib.Path?")
print()
print("  A) os.path is newer and more cross-platform")
print("  B) pathlib is only available on Linux/macOS")
print("  C) os.path uses string functions; pathlib uses objects with")
print("     methods and the / operator for joining")
print("  D) They are completely identical in all ways")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()
if ans5 == "C":
    print("✅ Correct! pathlib is the modern OOP approach (Python 3.4+)."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   pathlib is OOP; os.path is function-based. Both are cross-platform.")
print()

print("=" * 60)
print(f"  Final Score: {score}/5")
print("=" * 60)
if score == 5:
    print("Perfect score! You master the path.")
elif score >= 3:
    print("Good job! Review your mistakes then try the exercises.")
else:
    print("Review lesson.py again before attempting exercises.")
