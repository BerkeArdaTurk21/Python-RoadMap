"""
================================================
Week 1 | Day 2 — Interactive Quiz
================================================
Run this file to test your knowledge:
    python quiz.py
================================================
"""

questions = [
    {
        "question": 'Q1: What is the output of: "Python"[1:4]',
        "options": {
            "A": '"Pyt"',
            "B": '"yth"',
            "C": '"ytho"',
            "D": '"ython"',
        },
        "answer": "B",
        "explanation": (
            "Slicing is start-inclusive, stop-exclusive. "
            "Indices 1, 2, 3 give characters 'y', 't', 'h' → \"yth\"."
        ),
    },
    {
        "question": 'Q2: What does "  hello  ".strip() return?',
        "options": {
            "A": '"hello  "',
            "B": '"  hello"',
            "C": '"hello"',
            "D": '"  hello  "',
        },
        "answer": "C",
        "explanation": (
            "strip() removes all leading and trailing whitespace. "
            "lstrip() removes only the left side; rstrip() removes only the right."
        ),
    },
    {
        "question": 'Q3: What does "banana".find("x") return?',
        "options": {
            "A": "0",
            "B": "False",
            "C": "ValueError",
            "D": "-1",
        },
        "answer": "D",
        "explanation": (
            "find() returns -1 when the substring is not found — it never raises an error. "
            "index() would raise ValueError; find() is the safe alternative."
        ),
    },
    {
        "question": 'Q4: What is the output of: "abc"[::-1]',
        "options": {
            "A": '"abc"',
            "B": '"acb"',
            "C": '"cba"',
            "D": '"bca"',
        },
        "answer": "C",
        "explanation": (
            "A step of -1 reverses the sequence. Start defaults to the last character, "
            "stop defaults to before the first character, stepping backwards."
        ),
    },
    {
        "question": 'Q5: What is the output of: f"{\'hi\':*^6}"',
        "options": {
            "A": '"hi****"',
            "B": '"****hi"',
            "C": '"**hi**"',
            "D": '"hi    "',
        },
        "answer": "C",
        "explanation": (
            "*^6 means: center in a field of width 6, fill empty space with *. "
            "'hi' is 2 chars; 4 padding chars split evenly → ** on each side."
        ),
    },
]

print("=" * 52)
print("   Week 1 | Day 2 — String Operations Quiz")
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
