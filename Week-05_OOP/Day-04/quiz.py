# =============================================================================
# Week 05 - Day 04 | Encapsulation — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 05 - Day 04 Quiz: Encapsulation")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the purpose of the @property decorator?")
print()
print("  A) To make a method run faster")
print("  B) To allow a method to be accessed like an attribute")
print("     (without parentheses), acting as a getter")
print("  C) To make an attribute shared across all instances")
print("  D) To prevent a method from being overridden in a subclass")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "B":
    print("✅ Correct! @property turns a method into a getter that")
    print("   looks like attribute access: obj.name instead of obj.get_name().")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: B.")
    print("   @property lets you write obj.celsius instead of")
    print("   obj.get_celsius(). It's the Pythonic way to add getters.")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What happens when you define __secret in a class?")
print()
print("  A) It becomes completely inaccessible — even to the class itself")
print("  B) It is renamed to _ClassName__secret (name mangling)")
print("  C) It is deleted automatically after __init__ runs")
print("  D) It becomes a global variable")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "B":
    print("✅ Correct! Python mangles __name to _ClassName__name.")
    print("   This prevents accidental overriding in subclasses.")
    print("   It is NOT true security — it can still be accessed as obj._ClassName__name.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: B.")
    print("   __secret becomes _ClassName__secret (name mangling).")
    print("   The class methods can still access it via self.__secret.")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("What is the output of the following code?")
print()
print("  class Box:")
print("      def __init__(self, size):")
print("          self.size = size")
print()
print("      @property")
print("      def size(self):")
print("          return self._size")
print()
print("      @size.setter")
print("      def size(self, value):")
print("          if value <= 0:")
print("              raise ValueError('Must be positive')")
print("          self._size = value")
print()
print("  b = Box(10)")
print("  b.size = 5")
print("  print(b.size)")
print()
print("  A) AttributeError")
print("  B) 10")
print("  C) 5")
print("  D) ValueError")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "C":
    print("✅ Correct! Box(10) calls the setter with value=10 → _size=10.")
    print("   b.size = 5 calls the setter again → _size=5.")
    print("   print(b.size) calls the getter → returns 5.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: C.")
    print("   self.size = size in __init__ goes through the setter.")
    print("   Then b.size = 5 updates it. The getter returns 5.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("How do you create a READ-ONLY property in Python?")
print()
print("  A) Use @property without defining a @x.setter")
print("  B) Prefix the method name with two underscores")
print("  C) Use @staticmethod instead of @property")
print("  D) Set the attribute to None in __init__")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "A":
    print("✅ Correct! A @property without a @x.setter is read-only.")
    print("   Trying to assign a value to it raises AttributeError.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: A.")
    print("   Just define @property (getter) with no @x.setter.")
    print("   Assignment attempts will raise AttributeError automatically.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("What is the difference between _name and __name in Python?")
print()
print("  A) _name is slower to access; __name is faster")
print("  B) Both are identical — just different conventions")
print("  C) _name is a convention ('internal use'); __name triggers")
print("     name mangling to _ClassName__name to avoid subclass clashes")
print("  D) __name is accessible from outside; _name is not")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "C":
    print("✅ Correct! _name is just a convention meaning 'don't touch'.")
    print("   __name gets renamed by Python to _ClassName__name.")
    print("   This prevents a subclass from accidentally overriding it.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: C.")
    print("   _name = social contract ('internal/protected').")
    print("   __name = Python actively renames it (name mangling).")
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
