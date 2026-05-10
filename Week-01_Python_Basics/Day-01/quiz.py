"""
================================================
Week 1 | Day 1 — Interactive Quiz
================================================
Run this file to test your knowledge:
    python quiz.py
================================================
"""

questions = [
    {
        "question": "Q1: What is the output of: print(type(3.14))",
        "options": {
            "A": "<class 'int'>",
            "B": "<class 'float'>",
            "C": "<class 'str'>",
            "D": "<class 'number'>",
        },
        "answer": "B",
        "explanation": "3.14 has a decimal point, so Python classifies it as float.",
    },
    {
        "question": "Q2: Which variable name is valid in Python?",
        "options": {
            "A": "2fast",
            "B": "fast-car",
            "C": "fast_car",
            "D": "class",
        },
        "answer": "C",
        "explanation": (
            "fast_car uses snake_case with only letters and underscores — valid. "
            "2fast starts with a digit, fast-car uses a hyphen (minus operator), "
            "class is a reserved keyword."
        ),
    },
    {
        "question": "Q3: What does id(x) return?",
        "options": {
            "A": "The index of x in a list",
            "B": "The data type of x",
            "C": "The unique memory address of the object x points to",
            "D": "The length of x",
        },
        "answer": "C",
        "explanation": "id() returns the integer memory address of the object in CPython.",
    },
    {
        "question": "Q4: Which of the following correctly creates a multi-line string?",
        "options": {
            "A": 'name = "line1 \\n line2"',
            "B": 'name = """line1\n   line2"""',
            "C": "name = 'line1' + 'line2'",
            "D": "Both A and B",
        },
        "answer": "D",
        "explanation": (
            "\\n inserts a newline character inside a regular string; "
            "triple quotes let you span actual lines. Both create multi-line strings."
        ),
    },
    {
        "question": "Q5: What is the output of:\n    x = y = 5\n    y = 10\n    print(x)",
        "options": {
            "A": "10",
            "B": "5",
            "C": "None",
            "D": "Error",
        },
        "answer": "B",
        "explanation": (
            "x = y = 5 makes both point to the integer 5. "
            "Reassigning y to 10 doesn't affect x — integers are immutable, "
            "and x still points to the original 5 object."
        ),
    },
]

print("=" * 52)
print("   Week 1 | Day 1 — Variables & Data Types Quiz")
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
