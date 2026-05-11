"""
================================================
Week 1 | Day 4 — Interactive Quiz
================================================
Run this file to test your knowledge:
    python quiz.py
================================================
"""

questions = [
    {
        "question": "Q1: What type does input() ALWAYS return?",
        "options": {
            "A": "int",
            "B": "float",
            "C": "str",
            "D": "The same type the user typed",
        },
        "answer": "C",
        "explanation": (
            "input() always returns str, no matter what the user types. "
            "Even if they type 42, you get the string \"42\". "
            "You must convert it yourself with int(), float(), etc."
        ),
    },
    {
        "question": "Q2: What is the output of: bool(\"False\")",
        "options": {
            "A": "False",
            "B": "True",
            "C": "None",
            "D": "ValueError",
        },
        "answer": "B",
        "explanation": (
            "bool(\"False\") is True because \"False\" is a non-empty string. "
            "Only the empty string \"\" is falsy. The word 'False' inside quotes "
            "is just text — it has nothing to do with the boolean False."
        ),
    },
    {
        "question": "Q3: Which line correctly reads an integer from the user?",
        "options": {
            "A": "age = input(int(\"Enter age: \"))",
            "B": "age = integer(input(\"Enter age: \"))",
            "C": "age = int(input(\"Enter age: \"))",
            "D": "int age = input(\"Enter age: \")",
        },
        "answer": "C",
        "explanation": (
            "int(input(\"...\")) is the correct pattern: input() runs first and "
            "returns a str, then int() converts that str to an integer. "
            "The other options have syntax errors or use non-existent functions."
        ),
    },
    {
        "question": "Q4: The user enters \"3.14\" at a prompt. Which call raises ValueError?",
        "options": {
            "A": "float(\"3.14\")",
            "B": "str(\"3.14\")",
            "C": "bool(\"3.14\")",
            "D": "int(\"3.14\")",
        },
        "answer": "D",
        "explanation": (
            "int() cannot parse a string that contains a decimal point. "
            "It raises ValueError: invalid literal for int() with base 10: '3.14'. "
            "float() handles it fine, str() and bool() never raise on a string."
        ),
    },
    {
        "question": "Q5: What does \"42\".isdigit() return?",
        "options": {
            "A": "42",
            "B": "\"42\"",
            "C": "False",
            "D": "True",
        },
        "answer": "D",
        "explanation": (
            "isdigit() returns True when every character in the string is a digit (0-9). "
            "\"42\" has only digit characters, so it returns True. "
            "Note: \"-5\".isdigit() is False (minus sign) and \"3.14\".isdigit() is False (dot)."
        ),
    },
]

print("=" * 52)
print("   Week 1 | Day 4 — User Input & Type Conversion")
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
