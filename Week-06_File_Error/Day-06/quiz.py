# =============================================================================
# Week 06 - Day 06 | Custom Exceptions — Quiz
# =============================================================================
score = 0
print("=" * 60)
print("  Week 06 - Day 06 Quiz: Custom Exceptions")
print("=" * 60)
print()

print("Question 1:")
print("What is the minimum requirement to create a valid custom exception?")
print()
print("  A) Must implement __init__ and __str__")
print("  B) Must inherit from BaseException")
print("  C) Inheriting from Exception (with a docstring or pass body)")
print("  D) Must define a custom message attribute")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "C":
    print("✅ Correct! class MyError(Exception): pass is a complete custom exception."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   You never need to inherit from BaseException — use Exception.")
print()

print("Question 2:")
print("Why is it recommended to inherit from Exception rather than")
print("BaseException for custom exceptions?")
print()
print("  A) BaseException is deprecated in Python 3")
print("  B) BaseException also covers KeyboardInterrupt and SystemExit;")
print("     catching your custom error would silently swallow Ctrl+C")
print("  C) Exception has better __str__ formatting")
print("  D) There is no difference")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "B":
    print("✅ Correct! You almost never want to catch Ctrl+C accidentally."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   except AppError would catch KeyboardInterrupt if AppError extends BaseException.")
print()

print("Question 3:")
print("You define: class ValidationError(AppError).")
print("If someone writes 'except AppError as e:', will ValidationError be caught?")
print()
print("  A) No — you must name the exact class")
print("  B) Yes — ValidationError IS-A AppError (subclass)")
print("  C) Only if ValidationError.__init__ calls super().__init__()")
print("  D) Only on Python 3.11+")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "B":
    print("✅ Correct! Catching a parent type catches all subclasses."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   This is why hierarchies are useful — broad vs. specific catching.")
print()

print("Question 4:")
print("What is the purpose of calling super().__init__(message)")
print("inside a custom exception's __init__?")
print()
print("  A) Required for Python to recognise it as an exception")
print("  B) Passes the message to the base Exception so it appears")
print("     in str(e), repr(e), and tracebacks")
print("  C) Sets the __class__ attribute correctly")
print("  D) It is not needed — you can skip it")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()
if ans4 == "B":
    print("✅ Correct! Without super().__init__, str(e) will be empty."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   Always call super().__init__(message) so the message shows up.")
print()

print("Question 5:")
print("When should you create a CUSTOM exception instead of using")
print("a built-in one like ValueError?")
print()
print("  A) Always — custom exceptions are always better")
print("  B) Never — always reuse built-in exceptions")
print("  C) When you need to attach extra structured data, build a")
print("     catchable hierarchy, or signal domain-specific errors")
print("     that callers must handle differently")
print("  D) Only when building web frameworks")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()
if ans5 == "C":
    print("✅ Correct! Built-ins are fine when they fit. Custom adds value"); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   Don't create CardDeclinedError when ValueError would do fine.")
print()

print("=" * 60)
print(f"  Final Score: {score}/5")
print("=" * 60)
if score == 5:
    print("Perfect score! You can architect exception hierarchies.")
elif score >= 3:
    print("Good job! Review your mistakes then try the exercises.")
else:
    print("Review lesson.py again before attempting exercises.")
