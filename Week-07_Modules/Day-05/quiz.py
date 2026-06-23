# =============================================================================
# Week 07 - Day 05 | The random Module — Quiz
# =============================================================================

questions = [
    {
        "q": "What range does random.randint(1, 6) produce?",
        "options": [
            "A) 1 to 5 (6 excluded)",
            "B) 1 to 6 (both included)",
            "C) 0 to 6",
            "D) 0.0 to 6.0 as a float",
        ],
        "answer": "B",
        "explanation": "randint(a, b) is inclusive on BOTH ends, so 1..6 — perfect for a dice roll.",
    },
    {
        "q": "What is the difference between random.choices() and random.sample()?",
        "options": [
            "A) There is no difference",
            "B) choices() picks WITH replacement (can repeat); sample() picks WITHOUT replacement (unique)",
            "C) sample() can repeat items; choices() cannot",
            "D) choices() only works on strings",
        ],
        "answer": "B",
        "explanation": "choices() can return duplicates and supports weights; sample() returns k distinct items.",
    },
    {
        "q": "What does random.shuffle(my_list) return?",
        "options": [
            "A) A new shuffled list",
            "B) None — it shuffles the list in place",
            "C) The original list unchanged",
            "D) A tuple of the shuffled items",
        ],
        "answer": "B",
        "explanation": "shuffle() reorders the list IN PLACE and returns None. To keep the original, use sample(lst, len(lst)).",
    },
    {
        "q": "Why would you call random.seed(42) before generating numbers?",
        "options": [
            "A) To make the numbers more random",
            "B) To make the sequence reproducible (same numbers every run)",
            "C) To limit results to the number 42",
            "D) To make generation faster",
        ],
        "answer": "B",
        "explanation": "A fixed seed makes the pseudo-random sequence repeat exactly — essential for tests and reproducible simulations.",
    },
    {
        "q": "Which module should you use for security-sensitive randomness (passwords, tokens)?",
        "options": [
            "A) random",
            "B) math",
            "C) secrets",
            "D) os.random",
        ],
        "answer": "C",
        "explanation": "random is NOT cryptographically secure. Use the `secrets` module for passwords, tokens, and keys.",
    },
]

score = 0
print("=" * 55)
print(" Week 07 - Day 05 Quiz | random Module")
print("=" * 55)

for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['q']}")
    for opt in q["options"]:
        print(f"  {opt}")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == q["answer"]:
        print(f"  Correct! {q['explanation']}")
        score += 1
    else:
        print(f"  Wrong. You chose {answer or '(blank)'}. Correct answer: {q['answer']}. {q['explanation']}")

print(f"\n{'=' * 55}")
print(f"Score: {score}/{len(questions)}")
if score == len(questions):
    print("Perfect score! You're ready for the exercises.")
elif score >= 3:
    print("Good job! Review mistakes then try the exercises.")
else:
    print("Review lesson.py again before attempting exercises.")
