"""
================================================
Week 1 — Weekly Review Quiz
================================================
10 Multiple Choice Questions  (2 per day)
 5 Code Challenges            (predict the output)
Run: python weekly_quiz.py
================================================
"""

import textwrap

# ── Helpers ──────────────────────────────────
def header(text):
    print()
    print("─" * 52)
    print(f"  {text}")
    print("─" * 52)

def show_result(correct, explanation, user_ans=None, right_ans=None):
    if correct:
        print(f"✅ Correct! {explanation}")
    else:
        if user_ans and right_ans:
            print(f"❌ Wrong! You chose {user_ans}. Correct: {right_ans}. {explanation}")
        else:
            print(f"❌ Wrong! {explanation}")

# ── MCQ bank ─────────────────────────────────
mcq = [
    # Day 1 — Variables & Data Types
    {
        "day": 1,
        "question": "Q1 [Day 1]: What does  type(3.0)  return?",
        "options": {"A": "<class 'int'>", "B": "<class 'float'>",
                    "C": "<class 'str'>", "D": "<class 'number'>"},
        "answer": "B",
        "explanation": (
            "3.0 has a decimal point, so Python stores it as float. "
            "type() returns the class of the object: <class 'float'>."
        ),
    },
    {
        "day": 1,
        "question": "Q2 [Day 1]: What does  bool([])  return?",
        "options": {"A": "True", "B": "None", "C": "False", "D": "0"},
        "answer": "C",
        "explanation": (
            "An empty list [] is falsy. bool() on any empty collection "
            "([], {}, set(), ()) returns False."
        ),
    },
    # Day 2 — String Operations
    {
        "day": 2,
        "question": 'Q3 [Day 2]: What does  "hello"[1:4]  return?',
        "options": {"A": '"hell"', "B": '"ell"', "C": '"hel"', "D": '"ello"'},
        "answer": "B",
        "explanation": (
            "Slicing [1:4] starts at index 1 (e) and stops BEFORE index 4. "
            "Indices 1,2,3 → 'e','l','l' → 'ell'."
        ),
    },
    {
        "day": 2,
        "question": 'Q4 [Day 2]: What does  "  hello  ".strip()  return?',
        "options": {
            "A": '"  hello  "  (unchanged)',
            "B": '"hello"',
            "C": '"hello  "',
            "D": '"  hello"',
        },
        "answer": "B",
        "explanation": (
            "strip() removes ALL leading and trailing whitespace from both ends. "
            "lstrip() removes only the left side, rstrip() only the right side."
        ),
    },
    # Day 3 — Numbers & Math
    {
        "day": 3,
        "question": "Q5 [Day 3]: What does  17 % 5  evaluate to?",
        "options": {"A": "3", "B": "2", "C": "3.4", "D": "1"},
        "answer": "B",
        "explanation": (
            "% is the modulo (remainder) operator. 17 ÷ 5 = 3 remainder 2. "
            "So 17 % 5 = 2. Useful for checking even/odd, cycling, etc."
        ),
    },
    {
        "day": 3,
        "question": "Q6 [Day 3]: What does  int(3.9)  return?",
        "options": {"A": "4  (rounds up)", "B": "3  (truncates)", "C": "3.9", "D": "ValueError"},
        "answer": "B",
        "explanation": (
            "int() truncates (cuts off) the decimal part — it does NOT round. "
            "int(3.9) → 3, int(3.1) → 3, int(-3.9) → -3. Use round() to round."
        ),
    },
    # Day 4 — User Input & Type Conversion
    {
        "day": 4,
        "question": "Q7 [Day 4]: What type does  input()  ALWAYS return?",
        "options": {"A": "int", "B": "float", "C": "str", "D": "depends on what user types"},
        "answer": "C",
        "explanation": (
            "input() ALWAYS returns str, no matter what the user types. "
            "Even if they type 42, you get the string '42'. "
            "You must explicitly convert with int() or float()."
        ),
    },
    {
        "day": 4,
        "question": 'Q8 [Day 4]: What does  "3.14".isdigit()  return?',
        "options": {"A": "True", "B": "False", "C": "ValueError", "D": "None"},
        "answer": "B",
        "explanation": (
            "isdigit() returns True only for strings that contain ONLY digit characters (0-9). "
            "The dot '.' in '3.14' is not a digit, so it returns False. "
            "Negative signs ('-') also cause False."
        ),
    },
    # Day 5 — Operators & Expressions
    {
        "day": 5,
        "question": "Q9 [Day 5]: What does  5 | 3  (bitwise OR) evaluate to?",
        "options": {"A": "1", "B": "7", "C": "2", "D": "15"},
        "answer": "B",
        "explanation": (
            "In binary: 5 = 101, 3 = 011. "
            "Bitwise OR gives 1 where AT LEAST ONE bit is 1: 101 | 011 = 111 = 7."
        ),
    },
    {
        "day": 5,
        "question": "Q10 [Day 5]: What does  not (True and False)  evaluate to?",
        "options": {"A": "False", "B": "True", "C": "None", "D": "TypeError"},
        "answer": "B",
        "explanation": (
            "Evaluate inside-out: True and False → False. "
            "Then not False → True. "
            "Parentheses force the and to evaluate first, then not inverts the result."
        ),
    },
]

# ── Code challenges ───────────────────────────
challenges = [
    {
        "label": "C1 [Day 2 — String slicing]",
        "code": (
            'x = "hello"\n'
            'print(x[::2])'
        ),
        "answer": "hlo",
        "explanation": (
            "x[::2] steps through 'hello' with step 2: index 0('h'), 2('l'), 4('o') → 'hlo'."
        ),
    },
    {
        "label": "C2 [Day 3 — Integer division & modulo]",
        "code": (
            "a = 10\n"
            "b = 3\n"
            "print(a // b, a % b)"
        ),
        "answer": "3 1",
        "explanation": (
            "10 // 3 = 3 (floor division), 10 % 3 = 1 (remainder). "
            "print() separates them with a space by default → '3 1'."
        ),
    },
    {
        "label": "C3 [Day 5 — Ternary expression]",
        "code": (
            "x = 7\n"
            'print("odd" if x % 2 else "even")'
        ),
        "answer": "odd",
        "explanation": (
            "7 % 2 = 1, which is truthy. "
            "Ternary: condition is truthy → return 'odd'."
        ),
    },
    {
        "label": "C4 [Day 6 — f-string center fill]",
        "code": (
            'print(f"{\"hi\":*^8}")'
        ),
        "answer": "***hi***",
        "explanation": (
            "*^8 means: center-align in a field of width 8, fill with *. "
            "'hi' is 2 chars, leaving 6 spaces to fill → 3 stars each side."
        ),
    },
    {
        "label": "C5 [Day 6 — print sep & end]",
        "code": (
            'print("A", "B", sep="-", end="!")\n'
            'print("C")'
        ),
        "answer": "A-B!C",
        "explanation": (
            'First print: sep="-" joins A and B → "A-B", then end="!" replaces newline → cursor stays. '
            'Second print: "C" then default end="\\n". Result: A-B!C on one line.'
        ),
    },
]


# ── Run quiz ──────────────────────────────────
print("=" * 52)
print("   Week 1 — Weekly Review Quiz")
print("   10 MCQ + 5 Code Challenges")
print("=" * 52)

mcq_score  = 0
code_score = 0

# ── Part 1: MCQ ───────────────────────────────
header("PART 1 — Multiple Choice  (10 questions)")

for i, q in enumerate(mcq):
    print(f"\n{q['question']}")
    for letter, opt in q["options"].items():
        print(f"  {letter}) {opt}")
    ans = input("\nYour answer (A/B/C/D): ").strip().upper()
    correct = ans == q["answer"]
    if correct:
        mcq_score += 1
    show_result(correct, q["explanation"], ans, q["answer"])

# ── Part 2: Code Challenges ───────────────────
header("PART 2 — Code Challenges  (predict the output)")
print("  Type the EXACT output the code would print.")
print("  Spaces matter. No quotes around your answer.")

for c in challenges:
    print(f"\n{c['label']}")
    print("  Code:")
    for line in c["code"].split("\n"):
        print(f"    {line}")
    ans = input("\nOutput: ").strip()
    correct = ans == c["answer"]
    if correct:
        code_score += 1
    show_result(correct, c["explanation"],
                user_ans=f'"{ans}"' if not correct else None,
                right_ans=f'"{c["answer"]}"' if not correct else None)

# ── Final Score ───────────────────────────────
total = mcq_score + code_score
print()
print("=" * 52)
print(f"  MCQ score    : {mcq_score}/10")
print(f"  Code score   : {code_score}/5")
print(f"  TOTAL        : {total}/15")
print("─" * 52)
if total == 15:
    print("  🏆 Perfect! Week 1 mastered — on to Week 2!")
elif total >= 11:
    print("  👍 Great work! Review any mistakes, then start Week 2.")
elif total >= 8:
    print("  📖 Good effort. Re-read the days you struggled with.")
else:
    print("  📖 Review Week 1 lessons before moving on.")
print("=" * 52)
