# =============================================================================
# Week 06 - Day 07 | Weekly Review Quiz
# =============================================================================
# Topics: File I/O (read/write), Paths (os.path / pathlib),
#         try/except, raising exceptions, custom exceptions
# =============================================================================

score = 0
print("=" * 62)
print("  Week 06 — File & Error Handling | Weekly Review Quiz")
print("=" * 62)
print()

# ─── PART A: Multiple Choice (10 questions, 1 pt each) ────────────────────────

print("── PART A: Multiple Choice ──")
print()

# Q1
print("Q1. Which file mode opens a file for writing and raises")
print("    FileExistsError if the file already exists?")
print("      A) 'w'   B) 'a'   C) 'x'   D) 'r+'")
a = input("    Your answer: ").strip().upper()
if a == "C":
    print("    ✅ Correct! 'x' (exclusive create) protects existing files."); score += 1
else:
    print("    ❌ Correct answer: C. 'x' is exclusive create mode.")
print()

# Q2
print("Q2. What does readline() return when it reaches the END of a file?")
print("      A) None   B) ''   C) '\\n'   D) raises StopIteration")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! readline() returns an empty string at EOF."); score += 1
else:
    print("    ❌ Correct answer: B. Empty string signals end-of-file.")
print()

# Q3
print("Q3. Which pathlib method searches for files RECURSIVELY")
print("    matching a pattern like '*.txt'?")
print("      A) glob()   B) iterdir()   C) rglob()   D) find()")
a = input("    Your answer: ").strip().upper()
if a == "C":
    print("    ✅ Correct! rglob('*.txt') walks all subdirectories."); score += 1
else:
    print("    ❌ Correct answer: C. 'r' in rglob stands for recursive.")
print()

# Q4
print("Q4. When does the 'else' clause of a try/except block run?")
print("      A) Always")
print("      B) Only when an exception is raised")
print("      C) Only when no exception is raised in the try block")
print("      D) Only after finally")
a = input("    Your answer: ").strip().upper()
if a == "C":
    print("    ✅ Correct! else = the happy path, no exception occurred."); score += 1
else:
    print("    ❌ Correct answer: C.")
print()

# Q5
print("Q5. What does Path('data') / 'reports' / 'q1.csv' produce?")
print("      A) TypeError — cannot use / with strings")
print("      B) 'data/reports/q1.csv' (Path object, platform-correct)")
print("      C) 'data' + 'reports' + 'q1.csv' = 'datareportsq1.csv'")
print("      D) A tuple ('data', 'reports', 'q1.csv')")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! pathlib overloads / as a path join operator."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q6
print("Q6. Which statement about 'raise' (bare raise) is TRUE?")
print("      A) It raises a new RuntimeError")
print("      B) It silences the current exception")
print("      C) It re-raises the current exception, preserving its traceback")
print("      D) It is only valid outside an except block")
a = input("    Your answer: ").strip().upper()
if a == "C":
    print("    ✅ Correct! Bare raise re-raises without touching the traceback."); score += 1
else:
    print("    ❌ Correct answer: C.")
print()

# Q7
print("Q7. What does json.dump(data, f, indent=2) do?")
print("      A) Reads JSON from f into data")
print("      B) Serializes data to f as pretty-printed JSON")
print("      C) Compresses data and writes it to f")
print("      D) Appends data as JSON to the end of f")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! indent=2 makes the JSON human-readable."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q8
print("Q8. Why should custom exceptions inherit from Exception,")
print("    NOT from BaseException?")
print("      A) BaseException is deprecated")
print("      B) BaseException also covers KeyboardInterrupt/SystemExit;")
print("         a broad except would silently swallow Ctrl+C")
print("      C) Exception has a better default __str__")
print("      D) There is no difference")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! Inheriting BaseException is almost never correct."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q9
print("Q9. What happens to assertions when Python runs with the -O flag?")
print("      A) They raise AssertionError more loudly")
print("      B) They are silently disabled — all assert statements are skipped")
print("      C) They become warnings instead of errors")
print("      D) Nothing — -O has no effect on assert")
a = input("    Your answer: ").strip().upper()
if a == "B":
    print("    ✅ Correct! Never use assert for user-input validation."); score += 1
else:
    print("    ❌ Correct answer: B.")
print()

# Q10
print("Q10. Path.stem for Path('/home/berke/notes_2026.txt') returns:")
print("      A) '.txt'           B) 'notes_2026.txt'")
print("      C) 'notes_2026'     D) '/home/berke'")
a = input("    Your answer: ").strip().upper()
if a == "C":
    print("    ✅ Correct! .stem = filename without extension."); score += 1
else:
    print("    ❌ Correct answer: C.")
print()

# ─── PART B: Code Challenges (5 questions, 1 pt each) ─────────────────────────

print("── PART B: Code Challenges ──")
print("(Type your answer or press Enter to see the solution)")
print()

# CB1
print("CB1. Write one line to read all text from 'data.txt' as a string.")
print("     (Hint: use open() with 'with')")
ans = input("     Your answer: ").strip()
print("     Solution: with open('data.txt', encoding='utf-8') as f: content = f.read()")
correct = "open" in ans and "read" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: open() with encoding + f.read()")
print()

# CB2
print("CB2. Use pathlib to create the path: <current dir> / 'output' / 'log.txt'")
print("     and write 'started' to it (creating output/ if needed).")
ans = input("     Your answer: ").strip()
print("     Solution:")
print("       p = Path('.') / 'output' / 'log.txt'")
print("       p.parent.mkdir(exist_ok=True)")
print("       p.write_text('started', encoding='utf-8')")
correct = "Path" in ans and ("mkdir" in ans or "write_text" in ans)
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: Path / operator + mkdir(exist_ok=True) + write_text()")
print()

# CB3
print("CB3. Complete the try/except/else/finally:")
print("     def safe_div(a, b): ...")
print("     — catches ZeroDivisionError, prints 'Error' in except,")
print("       prints result in else, always prints 'Done' in finally.")
ans = input("     Your answer: ").strip()
print("     Solution:")
print("       try:")
print("           r = a / b")
print("       except ZeroDivisionError:")
print("           print('Error')")
print("       else:")
print("           print(r)")
print("       finally:")
print("           print('Done')")
correct = "except" in ans and "finally" in ans
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: try/except/else/finally structure.")
print()

# CB4
print("CB4. Write a custom exception InsufficientFundsError(Exception)")
print("     that stores 'balance' and 'amount' attributes.")
ans = input("     Your answer: ").strip()
print("     Solution:")
print("       class InsufficientFundsError(Exception):")
print("           def __init__(self, balance, amount):")
print("               super().__init__(f'balance {balance} < {amount}')")
print("               self.balance = balance")
print("               self.amount  = amount")
correct = "Exception" in ans and ("balance" in ans or "__init__" in ans)
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: inherit Exception, call super().__init__, store attributes.")
print()

# CB5
print("CB5. Write load_json(path) that wraps FileNotFoundError in")
print("     RuntimeError using exception chaining (raise ... from ...).")
ans = input("     Your answer: ").strip()
print("     Solution:")
print("       def load_json(path):")
print("           try:")
print("               with open(path) as f: return json.load(f)")
print("           except FileNotFoundError as e:")
print("               raise RuntimeError(f'File not found: {path}') from e")
correct = "from" in ans and ("RuntimeError" in ans or "raise" in ans)
if correct:
    print("     ✅ Good!"); score += 1
else:
    print("     Review: raise RuntimeError(...) from e  ← that 'from e' is the key.")
print()

# ─── Final Score ───────────────────────────────────────────────────────────────
print("=" * 62)
print(f"  Final Score: {score}/15")
print("=" * 62)
if score == 15:
    print("  Perfect! You've mastered Week 6.")
elif score >= 11:
    print("  Great work! Ready for Week 7.")
elif score >= 8:
    print("  Good effort. Review the topics where you lost points.")
else:
    print("  Re-read the lessons and retry the exercises before moving on.")
