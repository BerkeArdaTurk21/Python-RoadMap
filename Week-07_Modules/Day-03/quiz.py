# =============================================================================
# Week 07 - Day 03 | sys & argparse — Quiz
# =============================================================================

questions = [
    {
        "q": "What is always stored in sys.argv[0]?",
        "options": [
            "A) The first command-line argument",
            "B) The script name/path",
            "C) The number of arguments",
            "D) The Python version",
        ],
        "answer": "B",
        "explanation": "sys.argv[0] is the script name/path. The real arguments start at sys.argv[1].",
    },
    {
        "q": "What type are the elements of sys.argv?",
        "options": [
            "A) Always strings",
            "B) Automatically converted to int/float when numeric",
            "C) bytes objects",
            "D) A mix of the correct Python types",
        ],
        "answer": "A",
        "explanation": "Every element of sys.argv is a string. You must convert (e.g. int()) values yourself.",
    },
    {
        "q": "What exit code conventionally means 'success'?",
        "options": [
            "A) 1",
            "B) -1",
            "C) 0",
            "D) 200",
        ],
        "answer": "C",
        "explanation": "sys.exit(0) means success. Non-zero codes signal an error to the shell or calling program.",
    },
    {
        "q": "Which action makes an argparse argument a boolean flag (True when present)?",
        "options": [
            "A) action='flag'",
            "B) action='store_true'",
            "C) type=bool",
            "D) action='boolean'",
        ],
        "answer": "B",
        "explanation": "action='store_true' sets the value to True when the flag is present, False otherwise.",
    },
    {
        "q": "What does parser.add_subparsers() let you build?",
        "options": [
            "A) Multiple --help pages for one argument",
            "B) git-style subcommands (e.g. 'add', 'list') each with their own args",
            "C) Parsers that run in parallel threads",
            "D) Automatic config-file parsing",
        ],
        "answer": "B",
        "explanation": "Subparsers expose several subcommands under one program, each with its own arguments — like 'git add' vs 'git commit'.",
    },
]

score = 0
print("=" * 55)
print(" Week 07 - Day 03 Quiz | sys & argparse")
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
