# =============================================================================
# Week 08 - Day 07 | Weekly Review Quiz
# =============================================================================
# Topics: decorators, iterators, generators, context managers,
#         type hints, testing with pytest
# =============================================================================

score = 0
print("=" * 62)
print("  Week 08 — Advanced Python | Weekly Review Quiz")
print("=" * 62)
print()

# ─── PART A: Multiple Choice (10 questions, 1 pt each) ────────────────────────

print("── PART A: Multiple Choice ──")
print()

# Q1
print("Q1. What does the @my_decorator syntax above a function do?")
print("      A) runs the function immediately")
print("      B) replaces the function with my_decorator(function)")
print("      C) copies the function into my_decorator")
print("      D) registers the function for import")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! @deco is sugar for func = deco(func)."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q2
print("Q2. Why use @functools.wraps(func) inside a decorator's wrapper?")
print("      A) it makes the wrapper run faster")
print("      B) it preserves the original function's __name__ and __doc__")
print("      C) it is required or the decorator crashes")
print("      D) it caches the function's return values")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! Without wraps, metadata shows the wrapper's name."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q3
print("Q3. Which two methods must an object implement to be an ITERATOR?")
print("      A) __iter__ and __next__     B) __next__ and __stop__")
print("      C) __iter__ and __len__      D) __getitem__ and __index__")
a = input("    Your answer: ").strip().upper()
if a == "A":
    print("    ✅ Correct! __iter__ returns self; __next__ yields values."); score += 1
else:
    print("    ❌ Correct answer: A.")
print()

# Q4
print("Q4. How does a for loop know an iterator is exhausted?")
print("      A) __next__ returns None")
print("      B) __next__ raises StopIteration")
print("      C) __iter__ returns False")
print("      D) the loop counts len() iterations")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! for catches StopIteration and ends silently."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q5
print("Q5. What does calling a generator function (one containing yield) return?")
print("      A) the first yielded value")
print("      B) a list of all yielded values")
print("      C) a generator object — no body code runs yet")
print("      D) None")
a = input("    Your answer: ").strip().upper()
if a == "C":
    print("    ✅ Correct! The body only runs when next() is called (lazy)."); score += 1
else:
    print("    ❌ Correct answer: C.")
print()

# Q6
print("Q6. Main advantage of a generator expression over a list comprehension?")
print("      A) it is always faster to fully consume")
print("      B) it produces values lazily — no full list in memory")
print("      C) it can be indexed like a list")
print("      D) it can be reused many times")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! (x*x for x in data) yields one value at a time."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q7
print("Q7. In a class-based context manager, when does __exit__ run?")
print("      A) only if the with-block succeeds")
print("      B) only if the with-block raises an exception")
print("      C) always — success or exception")
print("      D) only when the object is garbage-collected")
a = input("    Your answer: ").strip().upper()
if a == "C":
    print("    ✅ Correct! __exit__ always runs — that's the cleanup guarantee."); score += 1
else:
    print("    ❌ Correct answer: C.")
print()

# Q8
print("Q8. In a @contextlib.contextmanager generator, what does yield separate?")
print("      A) arguments from return values")
print("      B) setup code from cleanup code")
print("      C) the happy path from error handling")
print("      D) public code from private code")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! Before yield = __enter__, after yield = __exit__."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q9
print("Q9. What does the type hint Optional[int] mean?")
print("      A) the argument may be omitted")
print("      B) int or None")
print("      C) any numeric type")
print("      D) an int that may change later")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! Optional[X] = Union[X, None] = X | None (3.10+)."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q10
print("Q10. Which function names does pytest collect automatically?")
print("      A) any function with an assert inside")
print("      B) functions whose name starts with test_")
print("      C) functions decorated with @pytest.test")
print("      D) functions listed in pytest.ini only")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! test_*.py files and test_* functions are collected."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# ─── PART B: Code Challenges (5 questions, 1 pt each) ─────────────────────────

print("── PART B: Code Challenges ──")
print("(Type your answer or press Enter to see the solution)")
print()

# CB1
print("CB1. Inside a decorator, write the decorator line that preserves")
print("     func's metadata on the wrapper.")
ans = input("     Your answer: ").strip()
print("     Solution: @functools.wraps(func)   (or @wraps(func))")
correct = "wraps" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: @functools.wraps(func) goes right above def wrapper.")
print()

# CB2
print("CB2. Write a generator function countdown(n) that yields n, n-1, ... 1.")
ans = input("     Your answer: ").strip()
print("     Solution:")
print("       def countdown(n):")
print("           while n > 0:")
print("               yield n")
print("               n -= 1")
correct = "def" in ans and "yield" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: a generator is a normal def that uses yield.")
print()

# CB3
print("CB3. Write a generator EXPRESSION for the squares of 1..5.")
ans = input("     Your answer: ").strip()
print("     Solution: (x * x for x in range(1, 6))")
correct = "for" in ans and ("**" in ans or "*" in ans) and "[" not in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: parentheses (not brackets) make it a generator.")
print()

# CB4
print("CB4. Open 'data.txt' for reading so the file closes automatically,")
print("     even if an exception occurs.")
ans = input("     Your answer: ").strip()
print("     Solution: with open('data.txt') as f:")
correct = "with" in ans and "open" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: with open(...) as f: — open() returns a context manager.")
print()

# CB5
print("CB5. Write the pytest decorator line that runs one test for the")
print("     cases (2, 4) and (3, 9) with parameters 'n, expected'.")
ans = input("     Your answer: ").strip()
print("     Solution: @pytest.mark.parametrize('n, expected', [(2, 4), (3, 9)])")
correct = "parametrize" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: @pytest.mark.parametrize(params, list_of_tuples)")
print()

# ─── Final Score ───────────────────────────────────────────────────────────────
print("=" * 62)
print(f"  Final Score: {score}/15")
print("=" * 62)
if score == 15:
    print("  Perfect! You've mastered Week 8 — fundamentals are DONE.")
elif score >= 11:
    print("  Great work! Ready for Week 9 — the first project week.")
elif score >= 8:
    print("  Good effort. Review the topics where you lost points.")
else:
    print("  Re-read the lessons and retry the exercises before moving on.")
