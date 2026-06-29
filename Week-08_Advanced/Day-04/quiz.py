# =============================================================================
# Week 08 - Day 04 | Context Managers — Quiz
# =============================================================================

questions = [
    {
        "q": "What problem does the `with` statement primarily solve?",
        "options": [
            "A) It makes code run faster",
            "B) It guarantees cleanup code runs even if an exception occurs",
            "C) It automatically converts functions into generators",
            "D) It replaces the need for try/except entirely",
        ],
        "answer": "B",
        "explanation": (
            "The with statement guarantees that __exit__ (cleanup logic) runs "
            "no matter how the block ends — normally or via an exception."
        ),
    },
    {
        "q": "What two methods must a class implement to be a context manager?",
        "options": [
            "A) __init__ and __del__",
            "B) __open__ and __close__",
            "C) __enter__ and __exit__",
            "D) __start__ and __stop__",
        ],
        "answer": "C",
        "explanation": (
            "__enter__ runs at the start of the with block (its return value becomes "
            "the 'as' variable), and __exit__ always runs at the end, even on exceptions."
        ),
    },
    {
        "q": "What does returning True from __exit__ do?",
        "options": [
            "A) Nothing special, True is ignored",
            "B) It suppresses any exception that occurred in the with block",
            "C) It re-raises the exception immediately",
            "D) It causes __enter__ to be called again",
        ],
        "answer": "B",
        "explanation": (
            "If __exit__ returns True, any exception raised inside the with block "
            "is suppressed (swallowed). Returning False or None lets it propagate normally."
        ),
    },
    {
        "q": "In a generator-based context manager (@contextlib.contextmanager), what does the code AFTER yield represent?",
        "options": [
            "A) The __enter__ logic",
            "B) Code that never runs",
            "C) The __exit__ / cleanup logic",
            "D) The value assigned to the 'as' variable",
        ],
        "answer": "C",
        "explanation": (
            "Code before yield is __enter__ logic; the yielded value becomes the 'as' "
            "variable; code after yield (commonly in a finally block) is __exit__/cleanup logic."
        ),
    },
    {
        "q": "What does contextlib.suppress(FileNotFoundError) do?",
        "options": [
            "A) Prevents the file from ever being deleted",
            "B) Logs every FileNotFoundError to a file",
            "C) Silently ignores a FileNotFoundError if one is raised in the with block",
            "D) Converts FileNotFoundError into a warning instead of stopping the program",
        ],
        "answer": "C",
        "explanation": (
            "contextlib.suppress(ExceptionType) is a shortcut context manager that "
            "catches and silently ignores the given exception type if it's raised."
        ),
    },
]

score = 0
print("=" * 55)
print(" Week 08 - Day 04 Quiz | Context Managers")
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
