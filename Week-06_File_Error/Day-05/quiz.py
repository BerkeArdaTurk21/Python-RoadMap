# =============================================================================
# Week 06 - Day 05 | Raising Exceptions — Quiz
# =============================================================================
score = 0
print("=" * 60)
print("  Week 06 - Day 05 Quiz: Raising Exceptions")
print("=" * 60)
print()

print("Question 1:")
print("What does a bare 'raise' statement (with no argument) do")
print("inside an except block?")
print()
print("  A) Raises a new RuntimeError")
print("  B) Silences the exception")
print("  C) Re-raises the currently active exception, preserving")
print("     the original traceback")
print("  D) This is a syntax error")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "C":
    print("✅ Correct! Bare raise re-raises without modifying the traceback."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   Use bare raise to log and then let the exception propagate.")
print()

print("Question 2:")
print("When should you use 'raise ValueError' vs 'raise TypeError'?")
print()
print("  A) They are interchangeable — pick either")
print("  B) ValueError: wrong value for the right type.")
print("     TypeError: wrong type entirely")
print("  C) TypeError: wrong value. ValueError: wrong type")
print("  D) Always use RuntimeError — it covers both cases")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "B":
    print("✅ Correct! ValueError = bad value; TypeError = bad type."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   int('abc') → ValueError. 1 + 'a' → TypeError.")
print()

print("Question 3:")
print("What does 'raise RuntimeError(\"msg\") from original_exc' accomplish?")
print()
print("  A) Raises RuntimeError and discards the original exception")
print("  B) Chains RuntimeError to original_exc, preserving both")
print("     in the traceback and setting __cause__")
print("  C) Raises both exceptions simultaneously")
print("  D) This syntax is invalid in Python")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "B":
    print("✅ Correct! 'raise B from A' sets B.__cause__ = A."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   Exception chaining helps callers see both the what and the why.")
print()

print("Question 4:")
print("Why should you NOT use 'assert' to validate user input?")
print()
print("  A) assert is too slow for user input")
print("  B) assert only works with boolean values")
print("  C) Assertions are disabled when Python runs with the -O flag,")
print("     so the check would be silently skipped")
print("  D) assert raises ValueError, not AssertionError")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()
if ans4 == "C":
    print("✅ Correct! -O (optimize) strips all assert statements at runtime."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   Use raise ValueError for user data. Reserve assert for internal checks.")
print()

print("Question 5:")
print("Which exception type is most appropriate when a method MUST")
print("be overridden in a subclass but has NOT been?")
print()
print("  A) ValueError    B) RuntimeError")
print("  C) NotImplementedError    D) AbstractMethodError")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()
if ans5 == "C":
    print("✅ Correct! NotImplementedError signals 'subclass must implement this'."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   It's the conventional signal for abstract-like methods in Python.")
print()

print("=" * 60)
print(f"  Final Score: {score}/5")
print("=" * 60)
if score == 5:
    print("Perfect score! You raise exceptions like a pro.")
elif score >= 3:
    print("Good job! Review your mistakes then try the exercises.")
else:
    print("Review lesson.py again before attempting exercises.")
