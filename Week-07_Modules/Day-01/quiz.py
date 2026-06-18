# =============================================================================
# Week 07 - Day 01 | Import System & venv — Quiz
# =============================================================================
score = 0
print("=" * 60)
print("  Week 07 - Day 01 Quiz: Import System & venv")
print("=" * 60)
print()

print("Question 1:")
print("What is the value of __name__ when a Python file is run")
print("DIRECTLY (e.g. 'python lesson.py')?")
print()
print("  A) None")
print("  B) '__main__'")
print("  C) The filename without .py extension")
print("  D) 'main'")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "B":
    print("✅ Correct! '__main__' is the sentinel for the entry-point script."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   When imported, __name__ is the module filename. When run, it's '__main__'.")
print()

print("Question 2:")
print("What does 'from math import sqrt as s' allow you to do?")
print()
print("  A) Import all of math and rename the module to 's'")
print("  B) Import sqrt from math and use it as s() in this file")
print("  C) Create a copy of the sqrt function named s in math")
print("  D) This syntax is invalid")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "B":
    print("✅ Correct! 'as' creates a local alias for the imported name."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   Aliasing is common to shorten long names or avoid clashes.")
print()

print("Question 3:")
print("What is the purpose of 'if __name__ == \"__main__\":'?")
print()
print("  A) Checks if the module name is spelled correctly")
print("  B) Prevents the file from being imported")
print("  C) Lets code run when the file is executed directly,")
print("     but NOT when it is imported by another module")
print("  D) Defines the main() function automatically")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "C":
    print("✅ Correct! This guard makes files useful both as scripts and modules."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   Without it, imports would trigger unwanted side effects.")
print()

print("Question 4:")
print("Which command creates a new virtual environment in a folder called .venv?")
print()
print("  A) pip create .venv   B) python -m venv .venv")
print("  C) venv install .venv D) python --venv .venv")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()
if ans4 == "B":
    print("✅ Correct! 'python -m venv .venv' is the standard way."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   -m runs a module as a script; 'venv' is the module name.")
print()

print("Question 5:")
print("What does 'pip freeze > requirements.txt' do?")
print()
print("  A) Installs all packages listed in requirements.txt")
print("  B) Deletes all installed packages")
print("  C) Saves the current list of installed packages with their")
print("     exact versions to requirements.txt")
print("  D) Updates all packages to their latest versions")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()
if ans5 == "C":
    print("✅ Correct! freeze snapshots your environment so others can recreate it."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   To recreate: pip install -r requirements.txt")
print()

print("=" * 60)
print(f"  Final Score: {score}/5")
print("=" * 60)
if score == 5:
    print("🏆 Perfect score! You're ready for the exercises.")
elif score >= 3:
    print("👍 Good job! Review mistakes then try the exercises.")
else:
    print("📖 Review lesson.py again before attempting exercises.")
