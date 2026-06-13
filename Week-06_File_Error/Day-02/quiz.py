# =============================================================================
# Week 06 - Day 02 | Writing Files — Quiz
# =============================================================================
score = 0
print("=" * 60)
print("  Week 06 - Day 02 Quiz: Writing Files")
print("=" * 60)
print()

print("Question 1:")
print("What happens to an existing file when you open it with 'w' mode?")
print()
print("  A) An error is raised")
print("  B) New content is appended after the existing content")
print("  C) The file is truncated to zero bytes (existing content erased)")
print("  D) The file is opened in read-only mode")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()
if ans1 == "C":
    print("✅ Correct! Opening with 'w' immediately truncates the file.")
    print("   Always use 'a' if you want to keep existing content."); score += 1
else:
    print("❌ Wrong! Correct answer: C.")
    print("   'w' destroys existing content the moment you open the file.")
print()

print("Question 2:")
print("What is the difference between write() and writelines()?")
print()
print("  A) write() handles lists; writelines() handles strings")
print("  B) write() writes a single string; writelines() writes each")
print("     string in an iterable — neither adds newlines automatically")
print("  C) writelines() adds a newline after each string automatically")
print("  D) They are identical")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()
if ans2 == "B":
    print("✅ Correct! writelines() does NOT add \\n — you must include")
    print("   them in the strings yourself."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   writelines() iterates and writes each string. No auto-newlines.")
print()

print("Question 3:")
print("Which mode should you use to add log entries to a file")
print("without overwriting previous logs?")
print()
print("  A) 'w'  B) 'r+'  C) 'x'  D) 'a'")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()
if ans3 == "D":
    print("✅ Correct! 'a' (append) always writes at the end of the file"); score += 1
else:
    print("❌ Wrong! Correct answer: D.")
    print("   'a' mode is perfect for log files — never overwrites old data.")
print()

print("Question 4:")
print("What does 'x' mode do that 'w' mode does NOT?")
print()
print("  A) 'x' opens the file for both reading and writing")
print("  B) 'x' raises FileExistsError if the file already exists,")
print("     preventing accidental overwrites")
print("  C) 'x' creates a compressed file")
print("  D) 'x' flushes the buffer after every write")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()
if ans4 == "B":
    print("✅ Correct! 'x' (exclusive create) is a safety net — it fails");
    print("   if the file exists. Use it when you must not overwrite."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   'x' refuses to open if the file already exists.")
print()

print("Question 5:")
print("json.dump(data, f) writes Python data to a file.")
print("What function reads it back?")
print()
print("  A) json.read(f)   B) json.load(f)   C) json.parse(f)   D) json.get(f)")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()
if ans5 == "B":
    print("✅ Correct! json.dump() writes, json.load() reads."); score += 1
else:
    print("❌ Wrong! Correct answer: B.")
    print("   json.dump(data, f) → file. json.load(f) → Python object.")
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
