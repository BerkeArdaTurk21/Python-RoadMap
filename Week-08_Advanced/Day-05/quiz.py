# =============================================================================
# Week 08 - Day 05 | Type Hints — Quiz
# =============================================================================

questions = [
    {
        "q": "Does Python enforce type hints at runtime by default?",
        "options": [
            "A) Yes, calling a function with the wrong type raises TypeError",
            "B) No, type hints are purely informational unless checked by an external tool",
            "C) Only for built-in types like int and str",
            "D) Only inside classes, not regular functions",
        ],
        "answer": "B",
        "explanation": (
            "Type hints have zero effect at runtime by default. Python will happily run "
            "add('2', '3') even if add() is hinted to take ints — tools like mypy catch this statically."
        ),
    },
    {
        "q": "What does Optional[str] mean?",
        "options": [
            "A) The value must always be a string",
            "B) The value can be a string or None",
            "C) The value is an optional parameter with a default of ''",
            "D) The value can be any type except None",
        ],
        "answer": "B",
        "explanation": (
            "Optional[X] is shorthand for Union[X, None] — the value is either of type X or None. "
            "In Python 3.10+, X | None means the same thing."
        ),
    },
    {
        "q": "What is the modern (3.9+) way to type-hint a list of integers?",
        "options": [
            "A) List(int)",
            "B) list[int]",
            "C) list<int>",
            "D) [int]",
        ],
        "answer": "B",
        "explanation": (
            "Since Python 3.9, built-in collection types support generic syntax directly: "
            "list[int], dict[str, int], tuple[float, float], etc. — no typing import needed."
        ),
    },
    {
        "q": "What does Callable[[int, int], int] describe?",
        "options": [
            "A) A list containing exactly two integers",
            "B) A function that takes two int arguments and returns an int",
            "C) A dictionary mapping two ints to one int",
            "D) A tuple of three integers",
        ],
        "answer": "B",
        "explanation": (
            "Callable[[ArgTypes], ReturnType] hints a function's signature — here, a function "
            "taking (int, int) and returning int, e.g. an operator like multiply."
        ),
    },
    {
        "q": "What is the purpose of TypeVar in a generic function like `def first(items: list[T]) -> T`?",
        "options": [
            "A) It restricts the function to only work with strings",
            "B) It lets the function work with any type while preserving the relationship between input and output types",
            "C) It converts the input to a fixed type automatically",
            "D) It is only used for class inheritance, not functions",
        ],
        "answer": "B",
        "explanation": (
            "TypeVar makes a function generic: list[int] in means T is int, so the return type "
            "is also int. This preserves type accuracy across many possible input types."
        ),
    },
]

score = 0
print("=" * 55)
print(" Week 08 - Day 05 Quiz | Type Hints")
print("=" * 55)

for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['q']}")
    for opt in q["options"]:
        print(f"  {opt}")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == q["answer"]:
        print(f"  ✅ Correct! {q['explanation']}")
        score += 1
    else:
        print(
            f"  ❌ Wrong. You chose {answer or '(blank)'}. "
            f"Correct answer: {q['answer']}. {q['explanation']}"
        )

print(f"\n{'=' * 55}")
print(f"Score: {score}/{len(questions)}")
if score == len(questions):
    print("\U0001f3c6 Perfect score! You're ready for the exercises.")
elif score >= 3:
    print("\U0001f44d Good job! Review mistakes then try the exercises.")
else:
    print("\U0001f4d6 Review lesson.py again before attempting exercises.")
