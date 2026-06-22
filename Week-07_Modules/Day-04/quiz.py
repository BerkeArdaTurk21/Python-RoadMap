# =============================================================================
# Week 07 - Day 04 | The datetime Module — Quiz
# =============================================================================

questions = [
    {
        "q": "Which function returns the current date AND time?",
        "options": [
            "A) date.today()",
            "B) datetime.now()",
            "C) time.now()",
            "D) datetime.current()",
        ],
        "answer": "B",
        "explanation": "datetime.now() returns a datetime with both date and time. date.today() returns only the date.",
    },
    {
        "q": "What do you get when you subtract one date from another?",
        "options": [
            "A) A datetime object",
            "B) An integer number of days",
            "C) A timedelta object",
            "D) A string",
        ],
        "answer": "C",
        "explanation": "Subtracting dates/datetimes yields a timedelta. Use .days or .total_seconds() to read it.",
    },
    {
        "q": "Which method turns a datetime INTO a formatted string?",
        "options": [
            "A) strptime()",
            "B) strftime()",
            "C) isoformat() only",
            "D) format_time()",
        ],
        "answer": "B",
        "explanation": "strftime() = 'string FORMAT time' (datetime -> string). strptime() = 'string PARSE time' (string -> datetime).",
    },
    {
        "q": "In strftime, what does %Y produce?",
        "options": [
            "A) The 2-digit year (e.g. 26)",
            "B) The 4-digit year (e.g. 2026)",
            "C) The day of the year",
            "D) The weekday name",
        ],
        "answer": "B",
        "explanation": "%Y is the 4-digit year. %y (lowercase) is the 2-digit year.",
    },
    {
        "q": "What does timedelta(weeks=2) represent?",
        "options": [
            "A) The date two weeks from today",
            "B) A duration of 14 days",
            "C) The 2nd week of the year",
            "D) An error — weeks is not a valid argument",
        ],
        "answer": "B",
        "explanation": "timedelta is a DURATION. timedelta(weeks=2) equals 14 days; add it to a date to move forward in time.",
    },
]

score = 0
print("=" * 55)
print(" Week 07 - Day 04 Quiz | datetime Module")
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
