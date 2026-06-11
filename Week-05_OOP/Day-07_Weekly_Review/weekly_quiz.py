# =============================================================================
# Week 05 — Weekly Review Quiz
# =============================================================================
# 10 MCQ + 5 Code Challenges covering Days 1-6
# Run: python weekly_quiz.py
# =============================================================================

score = 0

print("=" * 60)
print("  Week 05 — OOP Weekly Quiz")
print("=" * 60)
print()

# ══════════════════════════════════════════════════════════════
# PART A — 10 Multiple Choice Questions
# ══════════════════════════════════════════════════════════════

print("── PART A: Multiple Choice (10 questions) ──")
print()

# Q1
print("Q1. What keyword is used to call the parent class's __init__?")
print("  A) parent()  B) base()  C) super()  D) inherit()")
a = input("Answer: ").strip().upper()
if a == "C":
    print("✅ super() calls the parent's __init__ and other methods."); score += 1
else:
    print("❌ C) super() — it's the standard way to call parent methods.")
print()

# Q2
print("Q2. What does @property allow you to do?")
print("  A) Make a method private")
print("  B) Access a method like an attribute (getter)")
print("  C) Prevent subclasses from overriding a method")
print("  D) Share a method across all instances")
a = input("Answer: ").strip().upper()
if a == "B":
    print("✅ @property turns a getter into attribute-like access."); score += 1
else:
    print("❌ B) @property — obj.name instead of obj.get_name().")
print()

# Q3
print("Q3. What is the MRO (Method Resolution Order)?")
print("  A) The order in which Python imports modules")
print("  B) The order Python searches classes for a method")
print("  C) The order attributes are initialised in __init__")
print("  D) A list of all methods in a class")
a = input("Answer: ").strip().upper()
if a == "B":
    print("✅ MRO defines where Python looks for a method: Child → Parent → ..."); score += 1
else:
    print("❌ B) MRO determines search order across the inheritance chain.")
print()

# Q4
print("Q4. Which is TRUE about 'duck typing' in Python?")
print("  A) Objects must inherit from a common base class")
print("  B) Type checking is done at compile time")
print("  C) An object's fitness is determined by its methods, not its type")
print("  D) Python automatically converts object types")
a = input("Answer: ").strip().upper()
if a == "C":
    print("✅ If it has the needed methods, it works — regardless of class."); score += 1
else:
    print("❌ C) Duck typing: method presence matters, not class hierarchy.")
print()

# Q5
print("Q5. What is name mangling?")
print("  A) Renaming a class when it is imported")
print("  B) Python renames __attr to _ClassName__attr to avoid")
print("     accidental overriding in subclasses")
print("  C) Adding underscores to all public attributes")
print("  D) Deleting private attributes after __init__")
a = input("Answer: ").strip().upper()
if a == "B":
    print("✅ __attr → _ClassName__attr. Used to prevent subclass clashes."); score += 1
else:
    print("❌ B) __name becomes _ClassName__name through name mangling.")
print()

# Q6
print("Q6. What does isinstance(x, Animal) return if x is a Dog")
print("    and Dog inherits from Animal?")
print("  A) False  B) True  C) None  D) AttributeError")
a = input("Answer: ").strip().upper()
if a == "B":
    print("✅ isinstance() returns True for the class AND all parent classes."); score += 1
else:
    print("❌ B) isinstance checks the full inheritance chain — Dog IS-A Animal.")
print()

# Q7
print("Q7. Which magic method makes obj[i] work?")
print("  A) __access__  B) __index__  C) __getitem__  D) __get__")
a = input("Answer: ").strip().upper()
if a == "C":
    print("✅ __getitem__(self, index) is called when you write obj[i]."); score += 1
else:
    print("❌ C) __getitem__ handles subscript access obj[i].")
print()

# Q8
print("Q8. What does __repr__ ideally return?")
print("  A) A short summary for logs")
print("  B) A string that would recreate the object in Python")
print("  C) The memory address of the object")
print("  D) A JSON representation")
a = input("Answer: ").strip().upper()
if a == "B":
    print("✅ repr() should return eval()-able code: Point(3, 4) not '(3,4)'."); score += 1
else:
    print("❌ B) __repr__ should produce valid Python that recreates the object.")
print()

# Q9
print("Q9. A @property with NO @x.setter is...")
print("  A) A write-only property")
print("  B) A read-only property — assignment raises AttributeError")
print("  C) A cached property that only computes once")
print("  D) An abstract property")
a = input("Answer: ").strip().upper()
if a == "B":
    print("✅ No setter = read-only. Writing to it raises AttributeError."); score += 1
else:
    print("❌ B) Without @x.setter, the property is read-only.")
print()

# Q10
print("Q10. What is the output?")
print("  class A:")
print("      def greet(self): return 'Hello from A'")
print("  class B(A):")
print("      def greet(self): return super().greet() + ' and B'")
print("  print(B().greet())")
print("  A) Hello from A")
print("  B) Hello from B")
print("  C) Hello from A and B")
print("  D) AttributeError")
a = input("Answer: ").strip().upper()
if a == "C":
    print("✅ super().greet() calls A.greet() → 'Hello from A'.")
    print("   B appends ' and B' → 'Hello from A and B'."); score += 1
else:
    print("❌ C) super().greet() gets parent result, B extends it.")
print()

# ══════════════════════════════════════════════════════════════
# PART B — 5 Code Challenges
# ══════════════════════════════════════════════════════════════

print("─" * 60)
print("── PART B: Code Challenges ──")
print("Each challenge is worth 1 point. Type your answer or")
print("describe the output. Type SKIP to skip.")
print("─" * 60)
print()

# C1
print("Challenge 1:")
print("  class Dog:")
print("      species = 'Canis'")
print("      def __init__(self, name):")
print("          self.name = name")
print("  d = Dog('Rex')")
print("  d.species = 'Unknown'")
print("  print(Dog.species, d.species)")
print()
print("What is the output? (format: 'X Y')")
a = input("Answer: ").strip()
if a in ("Canis Unknown", "Canis, Unknown"):
    print("✅ Correct! d.species = 'Unknown' creates an INSTANCE variable")
    print("   that shadows the class variable. Dog.species remains 'Canis'."); score += 1
else:
    print("❌ Answer: 'Canis Unknown'")
    print("   Assigning to d.species creates an instance var — class var unchanged.")
print()

# C2
print("Challenge 2:")
print("  class Rectangle:")
print("      def __init__(self, w, h):")
print("          self.w, self.h = w, h")
print("      def area(self): return self.w * self.h")
print("      def __gt__(self, other):")
print("          return self.area() > other.area()")
print()
print("  r1 = Rectangle(4, 6)   # area 24")
print("  r2 = Rectangle(5, 5)   # area 25")
print("  print(r1 > r2)")
print()
print("What is the output? (True/False)")
a = input("Answer: ").strip()
if a.lower() == "false":
    print("✅ Correct! r1.area()=24 < r2.area()=25 → False."); score += 1
else:
    print("❌ Answer: False. __gt__ compares areas: 24 > 25 is False.")
print()

# C3
print("Challenge 3:")
print("  class Animal:")
print("      def sound(self): return '...'")
print("  class Dog(Animal):")
print("      def sound(self): return 'Woof'")
print("  class Puppy(Dog): pass")
print()
print("  print(Puppy().sound())")
print("  print(isinstance(Puppy(), Animal))")
print()
print("What are the two outputs? (format: 'X, Y')")
a = input("Answer: ").strip()
if a.lower() in ("woof, true", "woof,true"):
    print("✅ Puppy inherits Dog.sound() → 'Woof'. Puppy IS-A Animal → True."); score += 1
else:
    print("❌ Answer: 'Woof, True'. MRO: Puppy→Dog (has sound)→Animal.")
print()

# C4
print("Challenge 4:")
print("  class Counter:")
print("      def __init__(self): self._n = 0")
print("      @property")
print("      def value(self): return self._n")
print("      @value.setter")
print("      def value(self, v):")
print("          if v >= 0: self._n = v")
print()
print("  c = Counter()")
print("  c.value = 5")
print("  c.value = -1")
print("  print(c.value)")
print()
print("What is the output?")
a = input("Answer: ").strip()
if a == "5":
    print("✅ Correct! c.value=-1 fails the guard (not >= 0), so _n stays 5."); score += 1
else:
    print("❌ Answer: 5. The setter ignores values < 0.")
print()

# C5
print("Challenge 5:")
print("  class Num:")
print("      def __init__(self, n): self.n = n")
print("      def __add__(self, other): return Num(self.n + other.n)")
print("      def __mul__(self, s): return Num(self.n * s)")
print("      def __str__(self): return str(self.n)")
print()
print("  a = Num(3)")
print("  b = Num(4)")
print("  print(a + b)")
print("  print(a * 10)")
print()
print("What are the two outputs? (format: 'X, Y')")
a = input("Answer: ").strip()
if a.lower() in ("7, 30", "7,30"):
    print("✅ a + b → Num(7) → prints 7. a * 10 → Num(30) → prints 30."); score += 1
else:
    print("❌ Answer: '7, 30'. __add__ and __mul__ return new Num instances.")
print()

# ══════════════════════════════════════════════════════════════
print("=" * 60)
print(f"  TOTAL SCORE: {score}/15")
print("=" * 60)
if score == 15:
    print("🏆 Perfect! You mastered Week 5 — OOP.")
elif score >= 10:
    print("👍 Great job! Review any missed topics.")
elif score >= 6:
    print("📖 Good effort. Revisit the days you found tricky.")
else:
    print("🔁 Review the week's lessons before moving on.")
