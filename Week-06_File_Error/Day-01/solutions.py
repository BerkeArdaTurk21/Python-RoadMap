# =============================================================================
# Week 06 - Day 01 | Reading Files — Solutions
# =============================================================================
import os

def _setup():
    with open("names.txt", "w", encoding="utf-8") as f:
        f.write("Alice\nBob\nCarol\nDave\nEve\n")
    with open("scores.csv", "w", encoding="utf-8") as f:
        f.write("name,score\nAlice,88\nBob,72\nCarol,95\nDave,60\nEve,83\n")
    with open("poem.txt", "w", encoding="utf-8") as f:
        f.write("Roses are red\nViolets are blue\nPython is great\nAnd so are you\n")

_setup()

# Solution 1 — Count Lines
# KEY INSIGHT: readlines() keeps the \n on each line.
# Strip whitespace before using names to avoid trailing newlines.
with open("names.txt", "r", encoding="utf-8") as f:
    lines = [l.strip() for l in f.readlines() if l.strip()]
print(f"Lines: {len(lines)}")
print(f"First: {lines[0]}")
print(f"Last: {lines[-1]}")
print()

# Solution 2 — Word Count
# KEY INSIGHT: strip() each line before counting words/chars.
# Counting chars without newlines: strip() removes them first.
total_lines = 0
total_words = 0
total_chars = 0
with open("poem.txt", "r", encoding="utf-8") as f:
    for line in f:
        stripped = line.strip()
        total_lines += 1
        total_words += len(stripped.split())
        total_chars += len(stripped)
print(f"Lines: {total_lines}")
print(f"Words: {total_words}")
print(f"Characters: {total_chars}")
print()

# Solution 3 — CSV Reader
# KEY INSIGHT: next(f) skips the header line cleanly without loading all lines.
scores = []
with open("scores.csv", "r", encoding="utf-8") as f:
    next(f)   # skip header
    for line in f:
        name, score = line.strip().split(",")
        score = int(score)
        scores.append((name, score))
        print(f"{name}: {score}")
avg = sum(s for _, s in scores) / len(scores)
print(f"Average: {avg:.1f}")
print()

# Solution 4 — Find High Scorers
high = [(n, s) for n, s in scores if s >= 80]
passed = sum(1 for _, s in scores if s >= 60)
print("High scorers (>=80):")
for name, score in high:
    print(f"  {name}: {score}")
print(f"Passed (>=60): {passed}/{len(scores)}")
print()

# Solution 5 — File Statistics
# KEY INSIGHT: seek(0, 2) moves to the END of file.
# The second argument is the reference: 0=start, 1=current, 2=end.
with open("poem.txt", "r", encoding="utf-8") as f:
    f.seek(0, 2)
    size = f.tell()
    print(f"File size: {size} bytes")
    f.seek(0)
    print(f"First 5 chars: {f.read(5)}")
    f.seek(0)
    last = f.readlines()[-1].strip()
    print(f"Last line: {last}")

for fn in ["names.txt", "scores.csv", "poem.txt"]:
    if os.path.exists(fn):
        os.remove(fn)
