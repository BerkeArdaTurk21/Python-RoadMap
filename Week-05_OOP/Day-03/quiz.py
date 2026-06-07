# =============================================================================
# Week 05 - Day 03 | Inheritance — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 05 - Day 03 Quiz: Inheritance")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the primary purpose of super().__init__() inside")
print("a child class constructor?")
print()
print("  A) To create a second object of the parent class")
print("  B) To call the parent's __init__ so inherited attributes")
print("     are set up without re-writing them")
print("  C) To prevent the child class from adding new attributes")
print("  D) To delete the parent class after the child is created")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "B":
    print("✅ Correct! super().__init__() delegates to the parent")
    print("   constructor so shared attributes (like name, age) are")
    print("   initialised once in the parent and reused in the child.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: B.")
    print("   super().__init__() calls the parent's constructor.")
    print("   Without it, the child would not inherit the parent's attributes.")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What is the output of the following code?")
print()
print("  class Animal:")
print("      def speak(self):")
print("          return 'Some sound'")
print()
print("  class Dog(Animal):")
print("      def speak(self):")
print("          return 'Woof!'")
print()
print("  class Puppy(Dog):")
print("      pass")
print()
print("  p = Puppy()")
print("  print(p.speak())")
print()
print("  A) Some sound")
print("  B) Woof!")
print("  C) AttributeError")
print("  D) None")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "B":
    print("✅ Correct! Python searches the MRO: Puppy → Dog → Animal.")
    print("   Puppy has no speak(), so Python checks Dog next.")
    print("   Dog.speak() exists and returns 'Woof!' — search stops there.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: B.")
    print("   MRO: Puppy → Dog → Animal. Puppy has no speak().")
    print("   Dog.speak() is found first → returns 'Woof!'.")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("Given these classes:")
print()
print("  class Vehicle: pass")
print("  class Car(Vehicle): pass")
print("  class ElectricCar(Car): pass")
print()
print("  ec = ElectricCar()")
print()
print("Which of the following evaluates to True?")
print()
print("  A) isinstance(ec, Car) and isinstance(ec, Vehicle)")
print("  B) isinstance(ec, Car) and not isinstance(ec, Vehicle)")
print("  C) issubclass(Vehicle, ElectricCar)")
print("  D) issubclass(Car, ElectricCar)")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "A":
    print("✅ Correct! isinstance() checks the entire inheritance chain.")
    print("   ElectricCar IS-A Car IS-A Vehicle, so both return True.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: A.")
    print("   isinstance(ec, Car) → True  (ElectricCar IS-A Car)")
    print("   isinstance(ec, Vehicle) → True  (ElectricCar IS-A Vehicle)")
    print("   issubclass goes parent → child, not the other way.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("What does the following code print?")
print()
print("  class Shape:")
print("      def describe(self):")
print("          return 'I am a shape'")
print()
print("  class Circle(Shape):")
print("      def describe(self):")
print("          return super().describe() + ' — specifically a circle'")
print()
print("  c = Circle()")
print("  print(c.describe())")
print()
print("  A) I am a shape")
print("  B) I am a shape — specifically a circle")
print("  C) specifically a circle")
print("  D) AttributeError: super() not allowed here")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "B":
    print("✅ Correct! super().describe() calls Shape.describe() which")
    print("   returns 'I am a shape'. Circle then concatenates")
    print("   ' — specifically a circle' and returns the full string.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: B.")
    print("   super().describe() returns the parent's result.")
    print("   Circle appends to it → 'I am a shape — specifically a circle'.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("A developer has this code and notices a bug:")
print()
print("  class Person:")
print("      def __init__(self, name):")
print("          self.name = name")
print()
print("  class Student(Person):")
print("      def __init__(self, name, gpa):")
print("          self.gpa = gpa")
print()
print("  s = Student('Alice', 3.9)")
print("  print(s.name)  # AttributeError!")
print()
print("What is the correct fix for Student.__init__?")
print()
print("  A) Add: self.name = name")
print("  B) Add: super().__init__(name)")
print("  C) Change class Student to class Student(object)")
print("  D) Remove the Student __init__ entirely")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "B":
    print("✅ Correct! The fix is super().__init__(name), which calls")
    print("   Person.__init__ and sets self.name properly.")
    print("   This reuses the parent's logic instead of duplicating it.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: B.")
    print("   Without super().__init__(name), Person.__init__ never runs,")
    print("   so self.name is never set → AttributeError on s.name.")
    print("   A would also work but duplicates code — B is the OOP way.")
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
