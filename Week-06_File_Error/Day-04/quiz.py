# =============================================================================
# Week 06 - Day 04 | try/except — Quiz
# =============================================================================
score = 0
print("=" * 60)
print("  Week 06 - Day 04 Quiz: try / except")
print("=" * 60)
print()

print("Question 1:")
print("When does the 'else' clause in a try/except block execute?")
print()
print("  A) Always, after try and except")
print("  B) Only when an exception WAS raised")
print("  C) Only when NO exception was raised in the try block")
print("  D) Only when the finally block runs without error")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "C":
    print("✅ Correct! else runs only on the happy path (no exception)."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   else separates 'success code' from 'error code' cleanly.")
print()

print("Question 2:")
print("Which clause ALWAYS executes, regardless of whether an exception")
print("occurred?")
print()
print("  A) else    B) except    C) finally    D) pass")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "C":
    print("✅ Correct! finally is the cleanup clause — it always runs."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   Use finally to close files, release locks, etc.")
print()

print("Question 3:")
print("What does 'except (ValueError, TypeError) as e:' do?")
print()
print("  A) Catches ValueError only")
print("  B) Catches either ValueError or TypeError, binding the")
print("     exception object to 'e'")
print("  C) Raises both ValueError and TypeError")
print("  D) This syntax is invalid in Python")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "B":
    print("✅ Correct! A tuple in except catches multiple exception types."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   Parentheses group multiple exception types in one clause.")
print()

print("Question 4:")
print("FileNotFoundError is a subclass of OSError.")
print("If you write 'except OSError:', which exceptions are caught?")
print()
print("  A) OSError only")
print("  B) OSError and all its subclasses (including FileNotFoundError)")
print("  C) Only FileNotFoundError, not OSError itself")
print("  D) None — you must always catch the most specific class")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()
if ans4 == "B":
    print("✅ Correct! Catching a parent class also catches all subclasses."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   This is Python's exception hierarchy in action.")
print()

print("Question 5:")
print("In a try/except/else/finally block, what is the correct order")
print("of execution when NO exception occurs?")
print()
print("  A) try → finally → else")
print("  B) try → else → finally")
print("  C) try → except → else → finally")
print("  D) else → try → finally")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()
if ans5 == "B":
    print("✅ Correct! No exception: try body → else → finally."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   When exception occurs: try (partial) → except → finally.")
print()

print("=" * 60)
print(f"  Final Score: {score}/5")
print("=" * 60)
if score == 5:
    print("Perfect score! Exceptions hold no mystery for you.")
elif score >= 3:
    print("Good job! Review your mistakes then try the exercises.")
else:
    print("Review lesson.py again before attempting exercises.")
