# =============================================================================
# Week 03 - Day 07 | Weekly Review Quiz — Functions
# =============================================================================
# Run: python weekly_quiz.py
# 10 MCQ + 5 Code Challenges — covers all 6 days of Week 3
# =============================================================================

score = 0
total = 15

print("=" * 60)
print("  Week 03 Weekly Review Quiz — Functions")
print("  10 Multiple Choice + 5 Code Challenges")
print("=" * 60)
print()

# ===========================================================================
# PART 1 — MULTIPLE CHOICE (10 questions)
# ===========================================================================
print("── PART 1: Multiple Choice ─────────────────────────────────")
print()

# ── Q1 ──────────────────────────────────────────────────────────────────────
print("Q1. What is the output of the following code?")
print()
print("  def greet(name='World'):")
print("      return f'Hello, {name}!'")
print()
print("  print(greet())")
print()
print("  A) Hello, !")
print("  B) Hello, World!")
print("  C) TypeError: missing argument")
print("  D) None")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! 'World' is the default value used when no argument is passed.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   Default parameters are used when the caller doesn't provide a value.")
print()

# ── Q2 ──────────────────────────────────────────────────────────────────────
print("Q2. Which call is INVALID for this function?")
print()
print("  def func(a, b=2, c=3):")
print("      pass")
print()
print("  A) func(1)")
print("  B) func(1, c=5)")
print("  C) func(b=2, 1)")
print("  D) func(1, 2, 3)")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "C":
    print("✅ Correct! Positional arguments cannot follow keyword arguments — SyntaxError.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: C.")
    print("   'func(b=2, 1)' is a SyntaxError — positional args must come before keyword args.")
print()

# ── Q3 ──────────────────────────────────────────────────────────────────────
print("Q3. What does *args collect inside a function?")
print()
print("  A) A dictionary of keyword arguments")
print("  B) A tuple of extra positional arguments")
print("  C) A list of all arguments")
print("  D) The first positional argument only")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! *args collects extra positional arguments into a TUPLE.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   *args → tuple. **kwargs → dictionary.")
print()

# ── Q4 ──────────────────────────────────────────────────────────────────────
print("Q4. What is the output?")
print()
print("  def total(**kwargs):")
print("      return sum(kwargs.values())")
print()
print("  print(total(a=1, b=2, c=3))")
print()
print("  A) {'a':1, 'b':2, 'c':3}")
print("  B) 6")
print("  C) (1, 2, 3)")
print("  D) TypeError")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! kwargs.values() gives (1, 2, 3), sum gives 6.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   **kwargs is a dict; .values() returns the values; sum adds them up.")
print()

# ── Q5 ──────────────────────────────────────────────────────────────────────
print("Q5. What does this lambda return for x=4?")
print()
print("  f = lambda x: x ** 2 if x % 2 == 0 else x")
print("  print(f(4))")
print()
print("  A) 4")
print("  B) 16")
print("  C) 2")
print("  D) True")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! 4 is even → 4**2 = 16.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   4 % 2 == 0 is True → x**2 branch → 4**2 = 16.")
print()

# ── Q6 ──────────────────────────────────────────────────────────────────────
print("Q6. What does filter() return?")
print()
print("  nums = [1, 2, 3, 4, 5]")
print("  result = filter(lambda x: x > 3, nums)")
print("  print(list(result))")
print()
print("  A) [1, 2, 3]")
print("  B) [4, 5]")
print("  C) [True, True]")
print("  D) filter object (not iterable)")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! filter() keeps elements where the function returns True. 4 > 3 and 5 > 3.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   filter() keeps items where lambda returns True → only 4 and 5.")
print()

# ── Q7 ──────────────────────────────────────────────────────────────────────
print("Q7. What is the LEGB rule?")
print()
print("  A) A Python sorting algorithm")
print("  B) The order Python searches for variable names: Local → Enclosing → Global → Built-in")
print("  C) The order of function arguments: Lambda → Expression → Global → Builtin")
print("  D) A memory management technique")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! LEGB = Local → Enclosing → Global → Built-in scope lookup order.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   When Python sees a name, it searches: Local first, then Enclosing, Global, Built-in.")
print()

# ── Q8 ──────────────────────────────────────────────────────────────────────
print("Q8. What is a closure?")
print()
print("  A) A function that takes no arguments")
print("  B) An inner function that remembers variables from its enclosing scope")
print("  C) A function that returns None")
print("  D) A decorator that closes over a module")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! A closure is an inner function that 'closes over' (remembers) variables")
    print("   from its enclosing function, even after the enclosing function has returned.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   Closures let inner functions remember the enclosing scope's state.")
print()

# ── Q9 ──────────────────────────────────────────────────────────────────────
print("Q9. What is REQUIRED in every recursive function to prevent infinite recursion?")
print()
print("  A) A return type annotation")
print("  B) A global variable counter")
print("  C) A base case")
print("  D) A loop")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "C":
    print("✅ Correct! The base case stops the recursion. Without it → RecursionError.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: C.")
    print("   The base case is the stopping condition — mandatory in every recursive function.")
print()

# ── Q10 ─────────────────────────────────────────────────────────────────────
print("Q10. What is the output?")
print()
print("  def f(n):")
print("      if n == 0:")
print("          return 0")
print("      return n + f(n - 1)")
print()
print("  print(f(4))")
print()
print("  A) 4")
print("  B) 24")
print("  C) 10")
print("  D) RecursionError")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "C":
    print("✅ Correct! f(4) = 4+f(3) = 4+3+f(2) = 4+3+2+f(1) = 4+3+2+1+f(0) = 4+3+2+1+0 = 10.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: C.")
    print("   This sums 4+3+2+1+0 = 10 via recursion.")
print()

# ===========================================================================
# PART 2 — CODE CHALLENGES (5 questions)
# ===========================================================================
print("── PART 2: Code Challenges ─────────────────────────────────")
print()

# ── C1 ──────────────────────────────────────────────────────────────────────
print("C1. What is printed?")
print()
print("  def describe(*args, sep=', '):")
print("      return sep.join(str(a) for a in args)")
print()
print("  print(describe(1, 2, 3))")
print("  print(describe('a', 'b', 'c', sep=' - '))")
print()
print("  A) 1, 2, 3  /  a - b - c")
print("  B) (1, 2, 3)  /  ('a', 'b', 'c')")
print("  C) 123  /  abc")
print("  D) TypeError")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "A":
    print("✅ Correct! *args captures positional args; sep is a keyword-only default.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: A.")
    print("   sep defaults to ', ' for first call; overridden to ' - ' for second.")
print()

# ── C2 ──────────────────────────────────────────────────────────────────────
print("C2. What is printed?")
print()
print("  x = 'global'")
print()
print("  def outer():")
print("      x = 'enclosing'")
print("      def inner():")
print("          print(x)")
print("      inner()")
print()
print("  outer()")
print("  print(x)")
print()
print("  A) global / global")
print("  B) enclosing / global")
print("  C) enclosing / enclosing")
print("  D) global / enclosing")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! inner() finds 'x' in the enclosing scope first (LEGB).")
    print("   The global x is unaffected — outer() created its own local x.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   LEGB: inner() looks Local→Enclosing and finds 'enclosing'.")
    print("   The global x='global' is never touched.")
print()

# ── C3 ──────────────────────────────────────────────────────────────────────
print("C3. What does this code produce?")
print()
print("  def multiplier(factor):")
print("      return lambda x: x * factor")
print()
print("  double = multiplier(2)")
print("  triple = multiplier(3)")
print()
print("  print(double(5))")
print("  print(triple(4))")
print()
print("  A) 10 / 12")
print("  B) 5 / 4")
print("  C) 2 / 3")
print("  D) TypeError")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "A":
    print("✅ Correct! multiplier() returns a closure — the lambda remembers 'factor'.")
    print("   double(5) = 5*2 = 10; triple(4) = 4*3 = 12.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: A.")
    print("   Each call to multiplier() creates a closure with its own 'factor' value.")
print()

# ── C4 ──────────────────────────────────────────────────────────────────────
print("C4. What is the output?")
print()
print("  words = ['banana', 'apple', 'cherry', 'date']")
print("  result = sorted(words, key=lambda w: len(w))")
print("  print(result)")
print()
print("  A) ['apple', 'banana', 'cherry', 'date']")
print("  B) ['date', 'apple', 'banana', 'cherry']")
print("  C) ['banana', 'apple', 'cherry', 'date']")
print("  D) ['apple', 'date', 'banana', 'cherry']")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! Sorted by length: date(4), apple(5), banana(6), cherry(6).")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   Lengths: date=4, apple=5, banana=6, cherry=6 → ['date','apple','banana','cherry'].")
print()

# ── C5 ──────────────────────────────────────────────────────────────────────
print("C5. Trace this recursive call. What is printed?")
print()
print("  def mystery(n):")
print("      if n <= 0:")
print("          return ''")
print("      return mystery(n - 1) + str(n)")
print()
print("  print(mystery(4))")
print()
print("  A) 4321")
print("  B) 1234")
print("  C) 4444")
print("  D) RecursionError")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! The recursive call happens BEFORE str(n) is appended.")
    print("   mystery(4) = mystery(3)+'4' = mystery(2)+'3'+'4' = ... = ''+'1'+'2'+'3'+'4' = '1234'")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   The deep call returns first, so digits build up left to right: 1234.")
print()

# ===========================================================================
# FINAL SCORE
# ===========================================================================
print("=" * 60)
print(f"  Final Score: {score}/{total}")
print("=" * 60)

if score == total:
    print("🏆 Perfect score! Week 3 — Functions fully mastered.")
elif score >= 12:
    print("👍 Great job! Review the questions you missed, then tackle the homework.")
elif score >= 8:
    print("📝 Decent start. Go back to the days where you struggled before the homework.")
else:
    print("📖 Review lesson files for the topics you missed, then retake this quiz.")
