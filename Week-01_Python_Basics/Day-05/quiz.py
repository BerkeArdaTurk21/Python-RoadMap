"""
================================================
Week 1 | Day 5 — Interactive Quiz
================================================
Run this file to test your knowledge:
    python quiz.py
================================================
"""

questions = [
    {
        "question": "Q1: What does  3 == 3.0  evaluate to?",
        "options": {
            "A": "False — they are different types",
            "B": "True — Python compares values across int and float",
            "C": "TypeError",
            "D": "3.0",
        },
        "answer": "B",
        "explanation": (
            "== compares VALUES, not types. 3 and 3.0 have the same numeric value, "
            "so 3 == 3.0 is True. If you need to check the type too, use isinstance()."
        ),
    },
    {
        "question": "Q2: What does  0 or \"hello\" or \"world\"  evaluate to?",
        "options": {
            "A": "True",
            "B": "False",
            "C": "\"hello\"",
            "D": "\"world\"",
        },
        "answer": "C",
        "explanation": (
            "or returns the FIRST truthy value it finds and stops. "
            "0 is falsy, so Python checks the next operand: \"hello\" is truthy, "
            "so it is returned immediately without ever evaluating \"world\"."
        ),
    },
    {
        "question": "Q3: What is  5 & 3  (bitwise AND)?",
        "options": {
            "A": "8",
            "B": "15",
            "C": "2",
            "D": "1",
        },
        "answer": "D",
        "explanation": (
            "In binary: 5 = 101, 3 = 011. "
            "Bitwise AND gives 1 only where BOTH bits are 1: 101 & 011 = 001 = 1."
        ),
    },
    {
        "question": "Q4: When should you use  is  instead of  == ?",
        "options": {
            "A": "Always — is is faster than ==",
            "B": "When comparing two strings",
            "C": "When checking if a value is None, True, or False",
            "D": "When comparing two integers",
        },
        "answer": "C",
        "explanation": (
            "is tests IDENTITY (same object in memory), not equality. "
            "None, True, and False are singletons, so is works correctly for them. "
            "For everything else (numbers, strings, lists), always use ==."
        ),
    },
    {
        "question": "Q5: What does  \"win\" if 10 > 5 else \"lose\"  evaluate to?",
        "options": {
            "A": "\"lose\"",
            "B": "True",
            "C": "\"win\"",
            "D": "10",
        },
        "answer": "C",
        "explanation": (
            "The ternary expression evaluates the condition first: 10 > 5 is True. "
            "When the condition is True, the expression returns the LEFT value: \"win\". "
            "If the condition were False, it would return \"lose\"."
        ),
    },
]

print("=" * 52)
print("   Week 1 | Day 5 — Operators & Expressions")
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
