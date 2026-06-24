# =============================================================================
# Week 07 - Day 06 | Regular Expressions — Quiz
# =============================================================================

questions = [
    {
        "q": "What is the difference between re.match() and re.search()?",
        "options": [
            "A) They are identical",
            "B) match() only matches at the START of the string; search() matches anywhere",
            "C) search() only matches at the start; match() matches anywhere",
            "D) match() returns a list; search() returns a string",
        ],
        "answer": "B",
        "explanation": "re.match() anchors at the beginning of the string. re.search() scans the whole string for the first match.",
    },
    {
        "q": "What does re.findall(r'\\d+', '12 a 345') return?",
        "options": [
            "A) ['1', '2', '3', '4', '5']",
            "B) ['12', '345']",
            "C) '12 345'",
            "D) [12, 345]",
        ],
        "answer": "B",
        "explanation": "\\d+ matches one or more digits greedily, so it returns the strings ['12', '345'].",
    },
    {
        "q": "Why should regex patterns be written as raw strings (r\"...\")?",
        "options": [
            "A) Raw strings run faster",
            "B) So Python does not interpret backslashes before regex sees them",
            "C) Raw strings allow Unicode",
            "D) It is only a style preference with no effect",
        ],
        "answer": "B",
        "explanation": "Without r'', Python would process escapes like \\b or \\d first. Raw strings pass the backslashes straight to the regex engine.",
    },
    {
        "q": "What does the '?' do in the pattern '<.+?>' compared to '<.+>'?",
        "options": [
            "A) Makes the match optional",
            "B) Makes the quantifier NON-greedy (matches as little as possible)",
            "C) Escapes the dot",
            "D) Repeats the group",
        ],
        "answer": "B",
        "explanation": "Adding ? after a quantifier makes it lazy/non-greedy, so '<.+?>' matches '<a>' and '<b>' separately instead of one big span.",
    },
    {
        "q": "How do you access the second captured group of a match object m?",
        "options": [
            "A) m.group(2)",
            "B) m[2] only",
            "C) m.findall(2)",
            "D) m.capture(2)",
        ],
        "answer": "A",
        "explanation": "m.group(2) returns the second captured group. m.group(0) is the whole match; m.groups() returns them all as a tuple.",
    },
]

score = 0
print("=" * 55)
print(" Week 07 - Day 06 Quiz | Regular Expressions")
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
