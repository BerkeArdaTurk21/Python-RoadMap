# =============================================================================
# Week 08 - Day 01 | Decorators — Quiz
# =============================================================================

questions = [
    {
        "q": "What does a decorator fundamentally do?",
        "options": [
            "A) Permanently modifies the source code of a function",
            "B) Takes a function, wraps it with extra behavior, and returns a new function",
            "C) Converts a class method into a static method",
            "D) Imports a module automatically when a function is called",
        ],
        "answer": "B",
        "explanation": (
            "A decorator takes a function, defines a wrapper with added behavior, "
            "and returns the wrapper — the original function's code is never changed."
        ),
    },
    {
        "q": "What is the @ syntax (e.g. @my_dec above a function) equivalent to?",
        "options": [
            "A) import my_dec",
            "B) func = func(my_dec)",
            "C) func = my_dec(func)",
            "D) my_dec.apply(func)",
        ],
        "answer": "C",
        "explanation": (
            "@my_dec is syntactic sugar for func = my_dec(func). "
            "Python calls my_dec with the function and reassigns the name to the result."
        ),
    },
    {
        "q": "Why should you use @functools.wraps(func) inside every decorator?",
        "options": [
            "A) It makes the decorator run faster",
            "B) It copies __name__, __doc__, and other metadata from func to the wrapper",
            "C) It automatically passes *args and **kwargs to the original function",
            "D) It prevents the decorator from being stacked with other decorators",
        ],
        "answer": "B",
        "explanation": (
            "Without @functools.wraps, the wrapper replaces the original function's "
            "metadata (__name__, __doc__, etc.) — breaking help(), debuggers, and logging tools."
        ),
    },
    {
        "q": "Given @bold above @italic on a function f, what is the correct call order?",
        "options": [
            "A) bold is applied first, italic second",
            "B) italic is applied first, bold second — result: bold(italic(f))",
            "C) Both decorators run at the same time",
            "D) The order doesn't matter — the output is always the same",
        ],
        "answer": "B",
        "explanation": (
            "Decorators are applied bottom-up. @italic is closest to the function so it wraps "
            "first, then @bold wraps the result. The equivalent is bold(italic(f))."
        ),
    },
    {
        "q": "How do you create a decorator that accepts its own arguments (e.g. @repeat(3))?",
        "options": [
            "A) Add a parameter directly to the wrapper function",
            "B) Use a global variable to store the argument",
            "C) Add one more level of nesting: a factory function that returns the decorator",
            "D) Pass the argument via **kwargs in the original function signature",
        ],
        "answer": "C",
        "explanation": (
            "A decorator factory adds one extra level: repeat(n) receives the argument and "
            "returns the real decorator. @repeat(3) is the same as func = repeat(3)(func)."
        ),
    },
]

score = 0
print("=" * 55)
print(" Week 08 - Day 01 Quiz | Decorators")
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
