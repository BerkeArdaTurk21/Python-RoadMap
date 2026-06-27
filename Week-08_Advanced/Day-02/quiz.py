# =============================================================================
# Week 08 - Day 02 | Iterators — Quiz
# =============================================================================

questions = [
    {
        "q": "What is the difference between an iterable and an iterator?",
        "options": [
            "A) They are the same thing — both terms mean the same in Python",
            "B) An iterable has __iter__, an iterator has both __iter__ and __next__",
            "C) An iterator has __iter__, an iterable has both __iter__ and __next__",
            "D) Iterables are for lists only; iterators work on any sequence",
        ],
        "answer": "B",
        "explanation": (
            "An iterable only needs __iter__ (e.g. list, tuple). "
            "An iterator needs both __iter__ and __next__ — it tracks position and yields one item at a time."
        ),
    },
    {
        "q": "What happens when you call next() on an exhausted iterator?",
        "options": [
            "A) It returns None",
            "B) It restarts from the beginning",
            "C) It raises StopIteration",
            "D) It raises IndexError",
        ],
        "answer": "C",
        "explanation": (
            "When an iterator has no more items, __next__ raises StopIteration. "
            "You can avoid this with next(it, default) which returns default instead."
        ),
    },
    {
        "q": "What should __iter__ return in a custom iterator class?",
        "options": [
            "A) A new copy of the iterator",
            "B) The first element of the sequence",
            "C) self",
            "D) A list of all remaining elements",
        ],
        "answer": "C",
        "explanation": (
            "In an iterator, __iter__ returns self. "
            "This makes the iterator usable in for loops and anywhere an iterable is expected."
        ),
    },
    {
        "q": "How does a for loop work internally with an iterator?",
        "options": [
            "A) It calls __getitem__ with increasing indices",
            "B) It calls iter() to get an iterator, then calls next() repeatedly until StopIteration",
            "C) It converts the object to a list first, then indexes through it",
            "D) It uses the len() function to determine how many times to loop",
        ],
        "answer": "B",
        "explanation": (
            "A for loop calls iter(obj) to get an iterator, then calls next() in a while loop. "
            "When StopIteration is raised, the loop ends cleanly."
        ),
    },
    {
        "q": "What does iter([1, 2, 3]) return?",
        "options": [
            "A) The same list [1, 2, 3]",
            "B) A list_iterator object",
            "C) A generator object",
            "D) A tuple (1, 2, 3)",
        ],
        "answer": "B",
        "explanation": (
            "iter() calls __iter__ on the list and returns a list_iterator. "
            "The original list is an iterable; the list_iterator is the actual iterator."
        ),
    },
]

score = 0
print("=" * 55)
print(" Week 08 - Day 02 Quiz | Iterators")
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
