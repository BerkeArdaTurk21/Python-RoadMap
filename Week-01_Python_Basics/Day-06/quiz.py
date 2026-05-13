"""
================================================
Week 1 | Day 6 — Interactive Quiz
================================================
Run this file to test your knowledge:
    python quiz.py
================================================
"""

questions = [
    {
        "question": 'Q1: What does  print("a", "b", "c", sep="-")  output?',
        "options": {
            "A": "a b c",
            "B": "a-b-c",
            "C": "a, b, c",
            "D": "abc",
        },
        "answer": "B",
        "explanation": (
            "The sep parameter replaces the default space separator. "
            "print() places the sep string BETWEEN each item: "
            '"a" + "-" + "b" + "-" + "c" → a-b-c.'
        ),
    },
    {
        "question": 'Q2: What does  f"{3.14159:.2f}"  evaluate to?',
        "options": {
            "A": "3.14159",
            "B": "3.1",
            "C": "3.14",
            "D": "3.142",
        },
        "answer": "C",
        "explanation": (
            "The format spec .2f means: fixed-point notation with 2 decimal places. "
            "3.14159 rounded to 2 decimal places is 3.14. "
            "Use .3f for 3 places, .0f for no decimal point."
        ),
    },
    {
        "question": 'Q3: What does  f"{\'hello\':>10}"  produce?',
        "options": {
            "A": '"hello     "  (left-aligned, 10 wide)',
            "B": '"     hello"  (right-aligned, 10 wide)',
            "C": '"  hello   "  (centered, 10 wide)',
            "D": '"hello"  (no change)',
        },
        "answer": "B",
        "explanation": (
            "> means right-align within the given width. "
            "10 is the minimum field width. "
            "'hello' is 5 chars, so 5 spaces are added on the LEFT: '     hello'. "
            "Use < for left-align and ^ for center."
        ),
    },
    {
        "question": 'Q4: What does  "{:.1%}".format(0.875)  output?',
        "options": {
            "A": "0.9%",
            "B": "87.5%",
            "C": "87.6%",  # wrong — 87.5 rounded to 1 decimal is 87.5
            "D": "0.875%",
        },
        "answer": "B",
        "explanation": (
            "The % type multiplies the value by 100 and appends a % sign. "
            "0.875 × 100 = 87.5, then .1 rounds to 1 decimal place → 87.5%. "
            "So the output is 87.5%."
        ),
    },
    {
        "question": "Q5: What does  print(\"A\", end=\"\")  followed by  print(\"B\")  output?",
        "options": {
            "A": "A\nB  (on two lines)",
            "B": "AB  (on one line)",
            "C": "A B  (with a space)",
            "D": "A  (B is never printed)",
        },
        "answer": "B",
        "explanation": (
            "end=\"\" replaces the default newline with an empty string, "
            "so the cursor stays on the same line after printing A. "
            "The next print(\"B\") continues right after, producing AB on one line."
        ),
    },
]

print("=" * 52)
print("   Week 1 | Day 6 — Print & Formatting")
print("=" * 52)
print()

score = 0

for q in questions:
    print(q["question"])
    for letter, option in q["options"].items():
        print(f"  {letter}) {option}")

    user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print(f"✅ Correct! {q['explanation']}")
        score += 1
    else:
        print(
            f"❌ Wrong! You chose {user_answer}. "
            f"The correct answer is {q['answer']}. {q['explanation']}"
        )
    print()

print("=" * 52)
if score == 5:
    print(f"🏆 Perfect score! {score}/5 — You're ready for the exercises.")
elif score >= 3:
    print(f"👍 Good job! {score}/5 — Review any mistakes then try the exercises.")
else:
    print(f"📖 {score}/5 — Review lesson.py again before attempting the exercises.")
print("=" * 52)
