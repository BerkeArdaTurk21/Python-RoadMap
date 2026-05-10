"""
================================================
Week 1 | Day 3 — Interactive Quiz
================================================
Run this file to test your knowledge:
    python quiz.py
================================================
"""

questions = [
    {
        "question": "Q1: What is the output of: 17 // 5",
        "options": {
            "A": "3.4",
            "B": "2",
            "C": "3",
            "D": "4",
        },
        "answer": "C",
        "explanation": (
            "The // operator performs floor division, which removes the decimal part. "
            "17 / 5 = 3.4, so the result is 3."
        )
    },
    {
        "question": "Q2: What does 10 / 2 return in Python 3?",
        "options": {
            "A": "5",
            "B": "5.0",
            "C": "2",
            "D": "0.5",
        },
        "answer": "B",
        "explanation": (
            "The / operator always returns a float in Python 3, "
            "even when the result is mathematically whole."
        ),
    },
    {
        "question": "Q3: What is the result of: 2 ** 3 ** 2",
        "options": {
            "A": "64",
            "B": "512",
            "C": "36",
            "D": "72",
        },
        "answer": "B",
        "explanation": (
            "** is right-to-left associative: 3**2 = 9 is evaluated first, "
            "then 2**9 = 512."
        ),
    },
    {
        "question": "Q4: What does -7 % 3 return?",
        "options": {
            "A": "-1",
            "B": "1",
            "C": "2",
            "D": "-2",
        },
        "answer": "C",
        "explanation": (
            "Python's modulo result always has the same sign as the divisor (3). "
            "-7 = (-3)*3 + 2, so the remainder is 2."
        ),
    },
    {
        "question": "Q5: Which function returns both the quotient and remainder in one call?",
        "options": {
            "A": "split(a, b)",
            "B": "modf(a, b)",
            "C": "divmod(a, b)",
            "D": "quotrem(a, b)",
        },
        "answer": "C",
        "explanation": "divmod(a, b) returns the tuple (a // b, a % b) in a single call.",
    },
]

print("=" * 52)
print("   Week 1 | Day 3 — Numbers & Math Quiz")
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
