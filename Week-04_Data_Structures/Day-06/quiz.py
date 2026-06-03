# =============================================================================
# Week 04 - Day 06 | collections Module — Quiz
# =============================================================================
# Run: python quiz.py
# 5 questions — score 5/5 before moving to exercises!
# =============================================================================
from collections import Counter, defaultdict, deque

score = 0

print("=" * 60)
print("  Week 04 - Day 06 Quiz: collections Module")
print("=" * 60)
print()

# ── Question 1 ──────────────────────────────────────────────
print("Question 1:")
print("What is the output?")
print()
print("  from collections import Counter")
print("  c = Counter('banana')")
print("  print(c.most_common(2))")
print()
print("  A) [('b', 1), ('a', 1)]")
print("  B) [('a', 3), ('n', 2)]")
print("  C) [('b', 3), ('a', 2)]")
print("  D) {'a': 3, 'n': 2, 'b': 1}")
print()
ans1 = input("Your answer (A/B/C/D): ").strip().upper()

if ans1 == "B":
    print("✅ Correct! 'banana' → a:3, n:2, b:1. most_common(2) returns top 2: [('a',3),('n',2)].")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans1}. Correct answer: B.")
    print("   Counter('banana') = {'a':3,'n':2,'b':1}. most_common(2) = top 2 by count.")
print()

# ── Question 2 ──────────────────────────────────────────────
print("Question 2:")
print("What is printed?")
print()
print("  from collections import Counter")
print("  c = Counter(['x', 'y', 'x'])")
print("  print(c['z'])")
print()
print("  A) KeyError")
print("  B) None")
print("  C) 0")
print("  D) ''")
print()
ans2 = input("Your answer (A/B/C/D): ").strip().upper()

if ans2 == "C":
    print("✅ Correct! Counter returns 0 for missing keys — no KeyError.")
    print("   This is one of Counter's most useful properties.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans2}. Correct answer: C.")
    print("   Counter never raises KeyError — missing keys return 0.")
print()

# ── Question 3 ──────────────────────────────────────────────
print("Question 3:")
print("What is the output?")
print()
print("  from collections import defaultdict")
print("  d = defaultdict(list)")
print("  d['a'].append(1)")
print("  d['a'].append(2)")
print("  d['b'].append(3)")
print("  print(dict(d))")
print()
print("  A) KeyError")
print("  B) {'a': [1, 2], 'b': [3]}")
print("  C) {'a': 1, 'b': 3}")
print("  D) defaultdict(<class 'list'>, {'a':[1,2],'b':[3]})")
print()
ans3 = input("Your answer (A/B/C/D): ").strip().upper()

if ans3 == "B":
    print("✅ Correct! defaultdict(list) auto-creates [] for new keys.")
    print("   dict(d) converts it to a regular dict for clean printing.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans3}. Correct answer: B.")
    print("   d['a'] automatically gets [] on first access, then we append to it.")
print()

# ── Question 4 ──────────────────────────────────────────────
print("Question 4:")
print("What is the output?")
print()
print("  from collections import deque")
print("  dq = deque([1, 2, 3])")
print("  dq.appendleft(0)")
print("  dq.append(4)")
print("  dq.popleft()")
print("  print(list(dq))")
print()
print("  A) [0, 1, 2, 3]")
print("  B) [1, 2, 3, 4]")
print("  C) [0, 1, 2, 3, 4]")
print("  D) [2, 3, 4]")
print()
ans4 = input("Your answer (A/B/C/D): ").strip().upper()

if ans4 == "B":
    print("✅ Correct! Start: [1,2,3] → appendleft(0): [0,1,2,3]")
    print("   → append(4): [0,1,2,3,4] → popleft() removes 0: [1,2,3,4].")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans4}. Correct answer: B.")
    print("   appendleft adds to left, append adds to right, popleft removes from left.")
print()

# ── Question 5 ──────────────────────────────────────────────
print("Question 5:")
print("What is the main advantage of deque over a list for queue operations?")
print()
print("  A) deque uses less memory than a list")
print("  B) deque.popleft() is O(1); list.pop(0) is O(n)")
print("  C) deque supports indexing but list does not")
print("  D) deque is faster for sorting")
print()
ans5 = input("Your answer (A/B/C/D): ").strip().upper()

if ans5 == "B":
    print("✅ Correct! list.pop(0) shifts every element left → O(n).")
    print("   deque.popleft() is O(1) — that's the whole reason deque exists.")
    score += 1
else:
    print(f"❌ Wrong! You chose {ans5}. Correct answer: B.")
    print("   For queues (FIFO), always prefer deque — popleft is O(1) not O(n).")
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
