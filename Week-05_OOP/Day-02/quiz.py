# =============================================================================
# Week 05 - Day 02 | Instance & Class Variables — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 05 - Day 02 Quiz: Instance & Class Variables")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the key difference between an instance variable")
print("and a class variable?")
print()
print("  A) Instance variables are faster to access than class variables")
print("  B) Class variables are shared by all instances; instance")
print("     variables belong to one specific object")
print("  C) Instance variables must be integers; class variables can be any type")
print("  D) Class variables are deleted when the program ends")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "B":
    print("✅ Correct! A class variable lives on the class itself and is")
    print("   shared by every instance. An instance variable is stored on")
    print("   each individual object and can differ from object to object.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: B.")
    print("   Class variables are shared across all instances.")
    print("   Instance variables belong to one specific object.")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What does the first parameter of a @classmethod receive?")
print()
print("  A) The current instance (like self)")
print("  B) A copy of the class dictionary")
print("  C) The class itself (conventionally named cls)")
print("  D) Nothing — @classmethod takes no extra parameters")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "C":
    print("✅ Correct! A class method receives the class as its first")
    print("   argument (conventionally named cls), NOT the instance.")
    print("   This lets it call cls(...) to create new instances.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: C.")
    print("   @classmethod passes the class (cls) as the first argument.")
    print("   This is different from instance methods which pass self.")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("What is the output of the following code?")
print()
print("  class Counter:")
print("      total = 0")
print("      def __init__(self):")
print("          Counter.total += 1")
print()
print("  a = Counter()")
print("  b = Counter()")
print("  c = Counter()")
print("  print(a.total, Counter.total)")
print()
print("  A) 1 3")
print("  B) 3 3")
print("  C) 0 3")
print("  D) 3 0")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "B":
    print("✅ Correct! Counter.total is a class variable shared by all.")
    print("   After 3 instances are created, total == 3.")
    print("   a.total reads the same class variable, so it also shows 3.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: B.")
    print("   Counter.total is incremented 3 times (once per instance).")
    print("   a.total reads the class variable too — both show 3.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("A developer writes a helper function inside a class that")
print("does NOT need access to any instance data (self) or class")
print("data (cls). Which decorator should they use?")
print()
print("  A) @classmethod")
print("  B) @instancemethod")
print("  C) @staticmethod")
print("  D) @property")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "C":
    print("✅ Correct! @staticmethod is for utility functions that belong")
    print("   to the class conceptually but don't need self or cls.")
    print("   They receive no automatic first argument.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: C.")
    print("   @staticmethod creates a plain function inside the class.")
    print("   It's called on the class or instance but gets no self/cls.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("What happens when you run the following code?")
print()
print("  class Team:")
print("      members = []")
print()
print("  t1 = Team()")
print("  t2 = Team()")
print("  t1.members.append('Alice')")
print("  print(t2.members)")
print()
print("  A) []")
print("  B) ['Alice']")
print("  C) AttributeError")
print("  D) None")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "B":
    print("✅ Correct! members is a class variable — a SINGLE list shared")
    print("   by all instances. Appending via t1.members modifies the")
    print("   shared list, so t2.members also shows ['Alice'].")
    print("   Fix: move self.members = [] into __init__.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: B.")
    print("   members is a class variable — one list shared by ALL.")
    print("   t1.members.append('Alice') modifies that shared list.")
    print("   t2.members reads the same list → ['Alice'].")
print()

# ── Final Score ──────────────────────────────────────────────
print("=" * 60)
print(f"  Final Score: {score}/5")
print("=" * 60)

if score == 5:
    print("🏆 Perfect score! You're ready for the exercises.")
elif score >= 3:
    print("👍 Good job! Review your mistakes then try the exercises.")
else:
    print("📖 Review lesson.py again before attempting exercises.")
