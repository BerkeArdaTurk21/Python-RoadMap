# =============================================================================
# Week 08 - Day 03 | Generators — Quiz
# =============================================================================

questions = [
    {
        "q": "What does calling a generator function (one that contains yield) do?",
        "options": [
            "A) Runs the whole function body and returns a list",
            "B) Runs the body until the first yield and returns that value",
            "C) Returns a generator object without running the body yet",
            "D) Raises a SyntaxError unless you use return",
        ],
        "answer": "C",
        "explanation": (
            "Calling a generator function returns a generator object immediately. "
            "The body does not run until you call next() / iterate over it."
        ),
    },
    {
        "q": "What is the main advantage of a generator over building a full list?",
        "options": [
            "A) Generators are always faster to write to disk",
            "B) Generators hold one value at a time, using constant memory",
            "C) Generators can be indexed with [ ] like lists",
            "D) Generators can be iterated over an unlimited number of times",
        ],
        "answer": "B",
        "explanation": (
            "Generators are lazy: they produce values on demand and keep only the "
            "current state in memory, so they handle huge or infinite sequences."
        ),
    },
    {
        "q": "Which expression creates a GENERATOR (not a list)?",
        "options": [
            "A) [x * x for x in range(5)]",
            "B) {x * x for x in range(5)}",
            "C) (x * x for x in range(5))",
            "D) list(x * x for x in range(5))",
        ],
        "answer": "C",
        "explanation": (
            "Parentheses create a generator expression. Square brackets make a list, "
            "and curly braces make a set comprehension."
        ),
    },
    {
        "q": "What does `yield from sub_iterable` do?",
        "options": [
            "A) Returns the sub_iterable as a single value",
            "B) Yields every item from sub_iterable, delegating to it",
            "C) Imports a generator from another module",
            "D) Stops the generator and returns sub_iterable",
        ],
        "answer": "B",
        "explanation": (
            "yield from delegates to another iterable, yielding each of its items. "
            "It replaces 'for x in sub_iterable: yield x' and forwards send()/return."
        ),
    },
    {
        "q": "Before using gen.send(value) on a generator, what must you do first?",
        "options": [
            "A) Nothing — send() works immediately",
            "B) Call gen.close()",
            "C) Prime it by calling next(gen) (or gen.send(None)) once",
            "D) Convert it to a list",
        ],
        "answer": "C",
        "explanation": (
            "A generator must be advanced to its first yield before it can receive a "
            "value. Prime it with next(gen) or gen.send(None), then send real values."
        ),
    },
]

score = 0
print("=" * 55)
print(" Week 08 - Day 03 Quiz | Generators")
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
