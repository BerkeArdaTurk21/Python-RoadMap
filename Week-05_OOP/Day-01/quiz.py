# =============================================================================
# Week 05 - Day 01 | Classes & Objects — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 05 - Day 01 Quiz: Classes & Objects")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the purpose of __init__ in a Python class?")
print()
print("  A) It is called when an object is deleted")
print("  B) It is the constructor — runs when a new instance is created")
print("  C) It defines a class-level variable")
print("  D) It converts the object to a string")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "B":
    print("✅ Correct! __init__ is called automatically when you write MyClass().")
    print("   It sets up the initial state of the new instance.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: B.")
    print("   __init__ is the constructor. Python calls it automatically")
    print("   as soon as you create a new instance with MyClass(...).")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What does 'self' refer to inside an instance method?")
print()
print("  A) The class itself")
print("  B) The parent class")
print("  C) The specific instance the method was called on")
print("  D) A global variable named 'self'")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "C":
    print("✅ Correct! self is a reference to the particular instance.")
    print("   When you call rex.bark(), Python passes rex as self.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: C.")
    print("   self refers to the specific object the method was called on.")
    print("   rex.bark() → Python translates this to Dog.bark(rex).")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("What is the output of the following code?")
print()
print("  class Counter:")
print("      def __init__(self):")
print("          self.count = 0")
print("      def increment(self):")
print("          self.count += 1")
print()
print("  a = Counter()")
print("  b = Counter()")
print("  a.increment()")
print("  a.increment()")
print("  b.increment()")
print("  print(a.count, b.count)")
print()
print("  A) 2 2")
print("  B) 3 0")
print("  C) 2 1")
print("  D) 1 1")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "C":
    print("✅ Correct! a and b are INDEPENDENT instances with their own count.")
    print("   a.increment() was called twice → a.count = 2.")
    print("   b.increment() was called once  → b.count = 1.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: C.")
    print("   Each instance has its own copy of count.")
    print("   a.count = 2 (incremented twice), b.count = 1 (incremented once).")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("Given the class below, which line creates a valid instance?")
print()
print("  class Rectangle:")
print("      def __init__(self, width, height):")
print("          self.width  = width")
print("          self.height = height")
print()
print("  A) r = Rectangle()")
print("  B) r = Rectangle(10)")
print("  C) r = Rectangle(10, 5)")
print("  D) r = Rectangle.new(10, 5)")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "C":
    print("✅ Correct! __init__ expects width and height, so you must pass both.")
    print("   Rectangle(10, 5) → self.width=10, self.height=5.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: C.")
    print("   __init__(self, width, height) requires two arguments.")
    print("   A and B raise TypeError (missing arguments).")
    print("   D is not valid Python syntax.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("What does __dict__ return on an instance?")
print()
print("  A) A list of all method names")
print("  B) A dictionary of all instance attributes and their values")
print("  C) The class definition as a string")
print("  D) The memory address of the object")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "B":
    print("✅ Correct! obj.__dict__ gives you a plain dict of all instance attributes.")
    print("   e.g. {'name': 'Rex', 'breed': 'Labrador', 'age': 3}")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: B.")
    print("   obj.__dict__ returns a dictionary mapping attribute names to values.")
    print("   It's useful for debugging to see what data an object holds.")
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
