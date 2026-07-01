# =============================================================================
# Week 08 - Day 06 | Testing with pytest — Quiz
# =============================================================================

questions = [
    {
        "q": "Which files does a bare `pytest` command collect tests from by default?",
        "options": [
            "A) Every .py file in the project",
            "B) Files named test_*.py or *_test.py",
            "C) Only files listed in pytest.txt",
            "D) Files that import the pytest module",
        ],
        "answer": "B",
        "explanation": (
            "pytest discovers tests by naming convention: files named test_*.py or *_test.py, "
            "functions named test_*, and classes named Test*. Other files are skipped unless "
            "passed explicitly (e.g. pytest lesson.py)."
        ),
    },
    {
        "q": "How do you check equality inside a pytest test function?",
        "options": [
            "A) self.assertEqual(a, b) — like unittest",
            "B) pytest.equal(a, b)",
            "C) a plain `assert a == b` statement",
            "D) check(a, b)",
        ],
        "answer": "C",
        "explanation": (
            "pytest needs no special assertion methods — it rewrites plain assert statements "
            "so a failure automatically shows both sides of the comparison."
        ),
    },
    {
        "q": "How do you test that calling divide(1, 0) raises ZeroDivisionError?",
        "options": [
            "A) assert divide(1, 0) == ZeroDivisionError",
            "B) with pytest.raises(ZeroDivisionError): divide(1, 0)",
            "C) try: divide(1, 0) — pytest counts the crash as a pass",
            "D) pytest.expect_error(divide, 1, 0)",
        ],
        "answer": "B",
        "explanation": (
            "pytest.raises is a context manager: the test PASSES only if the expected exception "
            "is raised inside the with-block, and FAILS if nothing (or something else) is raised."
        ),
    },
    {
        "q": "What is the purpose of a @pytest.fixture function?",
        "options": [
            "A) It marks a test as temporarily skipped",
            "B) It provides reusable setup data/resources, injected into tests by parameter name",
            "C) It makes a test run faster by caching results",
            "D) It converts a normal function into a test",
        ],
        "answer": "B",
        "explanation": (
            "A fixture prepares data or a resource. Any test that lists the fixture's name as a "
            "parameter receives its return value — fresh for each test, no copy-pasted setup."
        ),
    },
    {
        "q": "A test decorated with @pytest.mark.parametrize('x, y', [(1, 2), (3, 4), (5, 6)]) shows up in the report as…",
        "options": [
            "A) 1 test that loops internally over 3 tuples",
            "B) 3 separate tests, one per argument tuple",
            "C) 6 tests, one per individual value",
            "D) 0 tests — parametrized tests need a special runner",
        ],
        "answer": "B",
        "explanation": (
            "parametrize runs the same test body once per tuple, and each run is reported "
            "individually — so one failing case is pinpointed exactly."
        ),
    },
]

score = 0
print("=" * 55)
print(" Week 08 - Day 06 Quiz | Testing with pytest")
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
