# =============================================================================
# Week 05 - Day 05 | Polymorphism — Quiz
# =============================================================================
score = 0
print("=" * 60)
print("  Week 05 - Day 05 Quiz: Polymorphism")
print("=" * 60)
print()

print("Question 1:")
print("What does 'duck typing' mean in Python?")
print()
print("  A) Python only allows Duck objects to call bird methods")
print("  B) An object's suitability is determined by the presence")
print("     of certain methods, not by inheritance from a specific class")
print("  C) All objects must inherit from a common base class")
print("  D) Python automatically converts objects between types")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "B":
    print("✅ Correct! Duck typing: if the object has the required")
    print("   method, Python will use it — regardless of its class.")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: B.")
    print("   'If it quacks like a duck, it IS a duck.'")
    print("   Python cares about capabilities, not class hierarchy.")
print()

print("Question 2:")
print("What is the output?")
print()
print("  class Shape:")
print("      def area(self): return 0")
print()
print("  class Square(Shape):")
print("      def __init__(self, s): self.s = s")
print("      def area(self): return self.s ** 2")
print()
print("  shapes = [Shape(), Square(4), Square(3)]")
print("  print(sum(s.area() for s in shapes))")
print()
print("  A) 0")
print("  B) 24")
print("  C) 25")
print("  D) TypeError")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "C":
    print("✅ Correct! Shape().area()=0, Square(4).area()=16, Square(3).area()=9.")
    print("   0 + 16 + 9 = 25.")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: C.")
    print("   0 + 16 + 9 = 25. sum() works polymorphically on any iterable.")
print()

print("Question 3:")
print("Which of these is an example of polymorphism in Python?")
print()
print("  A) Calling len('hello') and len([1,2,3]) — both work")
print("     because both define __len__")
print("  B) Defining the same variable name twice in a function")
print("  C) Using a for loop to iterate over a list")
print("  D) Importing a module with 'import math'")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "A":
    print("✅ Correct! len() is polymorphic — it calls __len__ on")
    print("   whatever object it receives. str, list, dict, set all")
    print("   define __len__ differently.")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: A.")
    print("   len() is a classic example of Python's built-in polymorphism.")
print()

print("Question 4:")
print("A class Robot has a speak() method but does NOT inherit")
print("from Animal. Can it be passed to make_sound(animal)?")
print()
print("  def make_sound(animal):")
print("      print(animal.speak())")
print()
print("  A) No — it must inherit from Animal to have speak()")
print("  B) Yes — Python uses duck typing; any object with speak() works")
print("  C) No — Python checks isinstance(animal, Animal) first")
print("  D) Only if Robot is registered as a virtual subclass")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()
if ans4 == "B":
    print("✅ Correct! Python does not check the type — it just calls")
    print("   .speak() on whatever object it receives. Robot qualifies")
    print("   as long as it has a speak() method.")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: B.")
    print("   Duck typing: Python tries to call .speak(); if it exists,")
    print("   it works — no inheritance check performed.")
print()

print("Question 5:")
print("What is the purpose of defining __add__ on a class?")
print()
print("  A) To make the class iterable with a for loop")
print("  B) To allow adding extra attributes after __init__")
print("  C) To define behaviour for the + operator on instances")
print("  D) To merge two classes into one")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()
if ans5 == "C":
    print("✅ Correct! __add__ is called when Python evaluates v1 + v2.")
    print("   This is operator overloading — polymorphism via magic methods.")
    score += 1
else:
    print(f"❌ Wrong! Correct answer: C.")
    print("   __add__(self, other) defines what + does for your objects.")
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
