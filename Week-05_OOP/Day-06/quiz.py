# =============================================================================
# Week 05 - Day 06 | Magic Methods — Quiz
# =============================================================================
score = 0
print("=" * 60)
print("  Week 05 - Day 06 Quiz: Magic Methods")
print("=" * 60)
print()

print("Question 1:")
print("What is the difference between __str__ and __repr__?")
print()
print("  A) __str__ is for numbers; __repr__ is for strings")
print("  B) __str__ gives a human-readable string (used by print);")
print("     __repr__ gives a developer-readable string (used by repr)")
print("  C) __repr__ is called by print(); __str__ is called by repr()")
print("  D) They are identical — just different names for the same thing")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "B":
    print("✅ Correct! __str__ is for end-users (print, str()).")
    print("   __repr__ is for developers (repr(), shell). It should")
    print("   ideally produce code that recreates the object.")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: B.")
    print("   __str__ → human readable. __repr__ → developer readable.")
print()

print("Question 2:")
print("Which method is called by len(obj)?")
print()
print("  A) __size__")
print("  B) __count__")
print("  C) __len__")
print("  D) __length__")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "C":
    print("✅ Correct! len(obj) internally calls obj.__len__().")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: C.")
    print("   len() calls __len__(). Must return a non-negative integer.")
print()

print("Question 3:")
print("What is the output?")
print()
print("  class Wallet:")
print("      def __init__(self, coins):")
print("          self.coins = coins")
print("      def __add__(self, other):")
print("          return Wallet(self.coins + other.coins)")
print("      def __str__(self):")
print("          return f'Wallet({self.coins})'")
print()
print("  w1 = Wallet(5)")
print("  w2 = Wallet(3)")
print("  print(w1 + w2)")
print()
print("  A) Wallet(5)")
print("  B) Wallet(8)")
print("  C) TypeError")
print("  D) 8")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "B":
    print("✅ Correct! w1 + w2 calls w1.__add__(w2), which returns")
    print("   Wallet(5+3) = Wallet(8). Then print() calls __str__.")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: B.")
    print("   __add__ is called for +, returns Wallet(8). __str__ prints it.")
print()

print("Question 4:")
print("To make 'x in obj' work, which method must be defined?")
print()
print("  A) __has__")
print("  B) __contains__")
print("  C) __includes__")
print("  D) __member__")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()
if ans4 == "B":
    print("✅ Correct! 'x in obj' calls obj.__contains__(x).")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: B.")
    print("   'x in obj' triggers obj.__contains__(x).")
print()

print("Question 5:")
print("What does __rmul__ handle that __mul__ does not?")
print()
print("  A) Multiplication with negative numbers")
print("  B) When the object is on the RIGHT side: scalar * obj")
print("  C) In-place multiplication: obj *= scalar")
print("  D) Floating-point multiplication")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()
if ans5 == "B":
    print("✅ Correct! v * 3 calls v.__mul__(3).")
    print("   3 * v calls int.__mul__(v) first; if that returns NotImplemented,")
    print("   Python then calls v.__rmul__(3). This makes 3*v work.")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: B.")
    print("   __rmul__ handles the case where your object is on the right.")
print()

print("=" * 60)
print(f"  Final Score: {score}/5")
print("=" * 60)
if score == 5:
    print("🏆 Perfect score! You're ready for the exercises.")
elif score >= 3:
    print("👍 Good job! Review your mistakes then try the exercises.")
else:
    print("📖 Review lesson.py again before attempting exercises.")
