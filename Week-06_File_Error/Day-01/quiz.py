# =============================================================================
# Week 06 - Day 01 | Reading Files — Quiz
# =============================================================================
score = 0
print("=" * 60)
print("  Week 06 - Day 01 Quiz: Reading Files")
print("=" * 60)
print()

print("Question 1:")
print("Why should you always use 'with open(...) as f:' instead")
print("of manually calling f.close()?")
print()
print("  A) 'with' is faster than calling close()")
print("  B) 'with' auto-closes the file even if an exception occurs")
print("  C) Manual close() deletes the file")
print("  D) 'with' is required for writing but not for reading")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "B":
    print("✅ Correct! 'with' is a context manager — it guarantees")
    print("   f.close() is called even if an error occurs mid-read."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   Forgetting close() leaks file handles. 'with' prevents that.")
print()

print("Question 2:")
print("What does f.readlines() return?")
print()
print("  A) One line at a time — you must call it repeatedly")
print("  B) A single string containing the whole file")
print("  C) A list where each element is one line (including \\n)")
print("  D) A generator that yields lines lazily")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "C":
    print("✅ Correct! readlines() returns a list: ['line1\\n', 'line2\\n', ...]"); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   readlines() loads ALL lines at once into a list.")
print()

print("Question 3:")
print("Which approach is MOST memory-efficient for reading a large file?")
print()
print("  A) content = f.read()")
print("  B) lines = f.readlines()")
print("  C) for line in f:")
print("  D) lines = list(f)")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "C":
    print("✅ Correct! 'for line in f:' reads one line at a time,")
    print("   keeping memory usage low regardless of file size."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   Iterating 'for line in f:' is lazy — only one line in memory.")
print()

print("Question 4:")
print("What does f.seek(0) do?")
print()
print("  A) Closes the file")
print("  B) Reads the first byte")
print("  C) Moves the read cursor back to the beginning of the file")
print("  D) Truncates the file to zero bytes")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()
if ans4 == "C":
    print("✅ Correct! seek(0) repositions the cursor to byte 0 (start)."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   seek(n) moves the file pointer to byte position n.")
print()

print("Question 5:")
print("Which exception is raised when you try to open a file")
print("that does not exist?")
print()
print("  A) FileError")
print("  B) IOError")
print("  C) OSError")
print("  D) FileNotFoundError")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()
if ans5 == "D":
    print("✅ Correct! FileNotFoundError is raised when open() cannot")
    print("   find the specified file. (It's a subclass of OSError.)"); score += 1
else:
    print("❌ Wrong! Correct answer: D.")
    print("   FileNotFoundError — a specific subclass of OSError.")
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
