# =============================================================================
# Week 04 - Day 03 | Dictionaries — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================

score = 0

print("=" * 60)
print("  Week 04 - Day 03 Quiz: Dictionaries")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the output?")
print()
print("  d = {'name': 'Alice', 'age': 30}")
print("  print(d.get('email', 'not found'))")
print()
print("  A) None")
print("  B) KeyError")
print("  C) not found")
print("  D) ''")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "C":
    print("✅ Correct! .get() returns the default value when the key doesn't exist.")
    print("   No KeyError is raised — that's the whole point of using .get().")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: C.")
    print("   d.get('key', default) returns default when key is missing.")
    print("   d['key'] would raise KeyError; d.get('key') returns None.")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What is the output?")
print()
print("  d = {'a': 1, 'b': 2, 'c': 3}")
print("  d.update({'b': 99, 'd': 4})")
print("  print(d)")
print()
print("  A) {'a': 1, 'b': 2, 'c': 3, 'd': 4}")
print("  B) {'a': 1, 'b': 99, 'c': 3, 'd': 4}")
print("  C) {'b': 99, 'd': 4}")
print("  D) KeyError")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "B":
    print("✅ Correct! update() overwrites existing keys and adds new ones.")
    print("   'b' was updated to 99, 'd' was added. 'a' and 'c' unchanged.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: B.")
    print("   update() merges: existing keys are overwritten, new keys are added.")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("Which method removes a key AND returns its value?")
print()
print("  A) del d['key']")
print("  B) d.remove('key')")
print("  C) d.discard('key')")
print("  D) d.pop('key')")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "D":
    print("✅ Correct! d.pop('key') removes the key and returns its value.")
    print("   del d['key'] deletes but returns nothing.")
    print("   .remove() and .discard() are set methods, not dict methods.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: D.")
    print("   pop(key) → removes and returns. del → removes, returns None.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("What is the output?")
print()
print("  d = {'x': 10, 'y': 20}")
print("  for k, v in d.items():")
print("      print(k, v)")
print()
print("  A) x y")
print("     10 20")
print("  B) x 10")
print("     y 20")
print("  C) ('x', 10) ('y', 20)")
print("  D) KeyError")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "B":
    print("✅ Correct! .items() yields (key, value) tuples, which unpack into k, v.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: B.")
    print("   d.items() → (key, value) pairs → 'for k, v in d.items()' unpacks each pair.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("What is the output?")
print()
print("  d1 = {'a': 1, 'b': 2}")
print("  d2 = {'b': 99, 'c': 3}")
print("  merged = {**d1, **d2}")
print("  print(merged['b'])")
print()
print("  A) 1")
print("  B) 2")
print("  C) 99")
print("  D) [2, 99]")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "C":
    print("✅ Correct! When merging with {**d1, **d2}, the RIGHT side wins on duplicate keys.")
    print("   d2's 'b': 99 overwrites d1's 'b': 2.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: C.")
    print("   {**d1, **d2} unpacks both; later keys overwrite earlier ones → d2 wins.")
print()

# ── Final Score ──────────────────────────────────────────────
print("=" * 60)
print(f"  Final Score: {score}/5")
print("=" * 60)

if score == 5:
    print("🏆 Perfect score! You're ready for the exercises.")
elif score >= 3:
    print("👍 Good job! Review your mistakes then try the exercises.")
else:
    print("📖 Review lesson.py again before attempting exercises.")
