# =============================================================================
# Week 04 - Day 07 | Weekly Review Quiz — Data Structures
# =============================================================================
# Run: python weekly_quiz.py
# 10 MCQ + 5 Code Challenges — covers all 6 days of Week 4
# =============================================================================
from collections import Counter, defaultdict, deque

score = 0
total = 15

print("=" * 60)
print("  Week 04 Weekly Review Quiz — Data Structures")
print("  10 Multiple Choice + 5 Code Challenges")
print("=" * 60)
print()

# ===========================================================================
# PART 1 — MULTIPLE CHOICE (10 questions)
# ===========================================================================
print("── PART 1: Multiple Choice ─────────────────────────────────")
print()

# ── Q1 ──────────────────────────────────────────────────────────────────────
print("Q1. What is the output?")
print()
print("  lst = [10, 20, 30, 40, 50]")
print("  print(lst[1:4:2])")
print()
print("  A) [20, 30, 40]")
print("  B) [20, 40]")
print("  C) [10, 30, 50]")
print("  D) [30, 40]")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! start=1, stop=4 (excluded), step=2 → indices 1,3 → values 20,40.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   lst[1:4:2]: starts at index 1 (20), step 2 → index 3 (40). Stop before 4.")
print()

# ── Q2 ──────────────────────────────────────────────────────────────────────
print("Q2. What happens when you do:  a = [1,2,3]  then  b = a  then  b.append(4)?")
print()
print("  A) a = [1,2,3,4]  b = [1,2,3,4]")
print("  B) a = [1,2,3]    b = [1,2,3,4]")
print("  C) a = [1,2,3,4]  b = [1,2,3]")
print("  D) ValueError")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "A":
    print("✅ Correct! b = a is a REFERENCE — both point to the same list object.")
    print("   To get an independent copy: b = a.copy() or b = a[:].")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: A.")
    print("   Assignment creates a reference, not a copy. Both a and b point to the same list.")
print()

# ── Q3 ──────────────────────────────────────────────────────────────────────
print("Q3. What is the type of x = (42) ?")
print()
print("  A) tuple")
print("  B) int")
print("  C) list")
print("  D) set")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! (42) is just parentheses around an int. For a tuple: (42,)")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   The COMMA makes a tuple: (42,). Without it, Python sees (42) = 42.")
print()

# ── Q4 ──────────────────────────────────────────────────────────────────────
print("Q4. What is the output?")
print()
print("  d = {'a': 1, 'b': 2, 'c': 3}")
print("  result = {v: k for k, v in d.items()}")
print("  print(result[2])")
print()
print("  A) KeyError")
print("  B) 'a'")
print("  C) 'b'")
print("  D) 2")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "C":
    print("✅ Correct! Dict inversion swaps keys/values. {1:'a', 2:'b', 3:'c'}")
    print("   result[2] → 'b'.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: C.")
    print("   {v: k for k, v in d.items()} inverts the dict. 2 was the value of 'b'.")
print()

# ── Q5 ──────────────────────────────────────────────────────────────────────
print("Q5. What is the output?")
print()
print("  a = {1, 2, 3, 4}")
print("  b = {3, 4, 5, 6}")
print("  print(a ^ b)")
print()
print("  A) {3, 4}")
print("  B) {1, 2, 5, 6}")
print("  C) {1, 2, 3, 4, 5, 6}")
print("  D) {1, 2}")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! ^ = symmetric difference: elements in ONE set but NOT BOTH.")
    print("   3 and 4 are in both → excluded. 1,2 only in a; 5,6 only in b → {1,2,5,6}.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   ^ = symmetric difference = (a | b) - (a & b) = {1,2,3,4,5,6} - {3,4}.")
print()

# ── Q6 ──────────────────────────────────────────────────────────────────────
print("Q6. Which creates an empty SET (not dict)?")
print()
print("  A) {}")
print("  B) set()")
print("  C) {,}")
print("  D) []")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! {} creates an empty dict. set() creates an empty set.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   {} → dict. set() → set. This is one of Python's most common traps.")
print()

# ── Q7 ──────────────────────────────────────────────────────────────────────
print("Q7. What is the output?")
print()
print("  result = [x**2 for x in range(6) if x % 2 == 0]")
print("  print(result)")
print()
print("  A) [0, 4, 16]")
print("  B) [1, 9, 25]")
print("  C) [0, 1, 4, 9, 16, 25]")
print("  D) [4, 16, 36]")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "A":
    print("✅ Correct! Even numbers in range(6): 0, 2, 4. Squared: 0, 4, 16.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: A.")
    print("   Filter (if at end): keeps 0,2,4. Then squares: 0**2=0, 2**2=4, 4**2=16.")
print()

# ── Q8 ──────────────────────────────────────────────────────────────────────
print("Q8. What is the key difference between a list comprehension and a generator?")
print()
print("  A) Generators use {} syntax")
print("  B) List comps build immediately in memory; generators compute lazily on demand")
print("  C) Generators support conditions; list comps do not")
print("  D) They are identical")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! [x**2 for x in range(1M)] → full list in RAM.")
    print("   (x**2 for x in range(1M)) → tiny generator object, values computed on demand.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   () = generator (lazy). [] = list comprehension (eager, all in memory).")
print()

# ── Q9 ──────────────────────────────────────────────────────────────────────
print("Q9. What is the output?")
print()
print("  from collections import Counter")
print("  c = Counter('banana')")
print("  print(c['z'])")
print()
print("  A) KeyError")
print("  B) None")
print("  C) 0")
print("  D) ''")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "C":
    print("✅ Correct! Counter returns 0 for missing keys — never raises KeyError.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: C.")
    print("   Counter is designed to count — missing = zero occurrences = 0.")
print()

# ── Q10 ─────────────────────────────────────────────────────────────────────
print("Q10. Why is deque preferred over list for queue operations?")
print()
print("  A) deque uses less memory")
print("  B) deque.popleft() is O(1); list.pop(0) is O(n)")
print("  C) deque supports more methods")
print("  D) list cannot store mixed types")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! list.pop(0) shifts every element → O(n).")
    print("   deque.popleft() is O(1) — that's exactly why deque exists.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   For FIFO queues, always use deque — popleft is O(1) not O(n).")
print()

# ===========================================================================
# PART 2 — CODE CHALLENGES (5 questions)
# ===========================================================================
print("── PART 2: Code Challenges ─────────────────────────────────")
print()

# ── C1 ──────────────────────────────────────────────────────────────────────
print("C1. What is the output?")
print()
print("  first, *middle, last = (10, 20, 30, 40, 50)")
print("  print(first + last)")
print("  print(middle)")
print()
print("  A) 60 / [20, 30, 40]")
print("  B) 10 / [20, 30, 40, 50]")
print("  C) 60 / (20, 30, 40)")
print("  D) ValueError")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "A":
    print("✅ Correct! first=10, last=50 → 60. *middle = [20,30,40] (a LIST, not tuple).")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: A.")
    print("   Extended unpacking: first=10, last=50, *middle captures [20,30,40] as a list.")
print()

# ── C2 ──────────────────────────────────────────────────────────────────────
print("C2. What is the output?")
print()
print("  d1 = {'a': 1, 'b': 2}")
print("  d2 = {'b': 99, 'c': 3}")
print("  merged = {**d1, **d2}")
print("  print(sorted(merged.items()))")
print()
print("  A) [('a',1), ('b',2), ('c',3)]")
print("  B) [('a',1), ('b',99), ('c',3)]")
print("  C) [('b',99), ('c',3)]")
print("  D) TypeError")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! {**d1, **d2} merges dicts — right side wins on duplicate keys.")
    print("   'b':2 from d1 is overwritten by 'b':99 from d2.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   In {**d1, **d2}, d2 values overwrite d1 for duplicate keys.")
print()

# ── C3 ──────────────────────────────────────────────────────────────────────
print("C3. What is the output?")
print()
print("  words = ['hi', 'hello', 'hey', 'world']")
print("  result = {len(w) for w in words}")
print("  print(sorted(result))")
print()
print("  A) [2, 5, 3, 5]")
print("  B) [2, 3, 5]")
print("  C) {2, 3, 5}")
print("  D) [2, 3]")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! Set comprehension: lengths are {2,3,5,5} but 5 deduped → {2,3,5}.")
    print("   sorted() converts to a sorted list: [2, 3, 5].")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   {len(w) for w in words} → set (unique lengths). sorted() → list.")
print()

# ── C4 ──────────────────────────────────────────────────────────────────────
print("C4. What is the output?")
print()
print("  from collections import defaultdict")
print("  d = defaultdict(int)")
print("  for ch in 'abracadabra':")
print("      d[ch] += 1")
print("  print(d['a'])")
print()
print("  A) 1")
print("  B) 3")
print("  C) 5")
print("  D) KeyError")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "C":
    print("✅ Correct! 'abracadabra' has 5 'a' characters.")
    print("   defaultdict(int) starts at 0 for new keys, +=1 counts each occurrence.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: C.")
    print("   Count 'a' in 'abracadabra': a-b-r-a-c-a-d-a-b-r-a → 5 times.")
print()

# ── C5 ──────────────────────────────────────────────────────────────────────
print("C5. What is the output?")
print()
print("  matrix = [[1,2],[3,4],[5,6]]")
print("  flat = [n for row in matrix for n in row]")
print("  print(sum(x for x in flat if x % 2 == 0))")
print()
print("  A) 6")
print("  B) 12")
print("  C) 21")
print("  D) 9")
print()
a = input("Your answer (A/B/C/D): ").strip().upper()
if a == "B":
    print("✅ Correct! flat = [1,2,3,4,5,6]. Even numbers: 2,4,6. Sum = 12.")
    score += 1
else:
    print(f"❌ Wrong! You chose {a}. Correct answer: B.")
    print("   Flatten → [1,2,3,4,5,6]. Filter even → [2,4,6]. Sum → 12.")
print()

# ===========================================================================
# FINAL SCORE
# ===========================================================================
print("=" * 60)
print(f"  Final Score: {score}/{total}")
print("=" * 60)

if score == total:
    print("🏆 Perfect score! Week 4 — Data Structures fully mastered.")
elif score >= 12:
    print("👍 Great job! Review the questions you missed, then tackle the homework.")
elif score >= 8:
    print("📝 Decent start. Go back to the days where you struggled.")
else:
    print("📖 Review the lesson files for topics you missed, then retake this quiz.")
