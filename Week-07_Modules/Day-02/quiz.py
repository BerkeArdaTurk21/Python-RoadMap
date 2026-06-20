# =============================================================================
# Week 07 - Day 02 | The os Module — Quiz
# =============================================================================

questions = [
    {
        "q": "What does os.getcwd() return?",
        "options": [
            "A) The home directory of the current user",
            "B) The absolute path of the current working directory",
            "C) A list of files in the current directory",
            "D) The name of the operating system",
        ],
        "answer": "B",
        "explanation": "os.getcwd() returns the absolute path of the current working directory as a string.",
    },
    {
        "q": "Which function creates all intermediate directories, like 'mkdir -p'?",
        "options": [
            "A) os.mkdir()",
            "B) os.makedir()",
            "C) os.makedirs()",
            "D) os.createdir()",
        ],
        "answer": "C",
        "explanation": "os.makedirs() creates all missing intermediate directories. os.mkdir() only creates one level.",
    },
    {
        "q": "What does os.walk() yield for each directory it visits?",
        "options": [
            "A) Just the file names",
            "B) (dirpath, dirnames, filenames)",
            "C) (filename, size, modified_time)",
            "D) A list of absolute file paths",
        ],
        "answer": "B",
        "explanation": "os.walk() yields a 3-tuple: the directory path, a list of subdirectory names, and a list of file names.",
    },
    {
        "q": "What is the safest way to read an environment variable that might not exist?",
        "options": [
            "A) os.environ['KEY']",
            "B) os.getenv('KEY')",
            "C) os.env('KEY')",
            "D) os.read_env('KEY')",
        ],
        "answer": "B",
        "explanation": "os.getenv('KEY') returns None if the variable doesn't exist. os.environ['KEY'] raises KeyError.",
    },
    {
        "q": "What is os.path.splitext('/data/report.csv') ?",
        "options": [
            "A) ('/data', 'report.csv')",
            "B) ('/data/report', '.csv')",
            "C) ('report', '.csv')",
            "D) ['/data/report', 'csv']",
        ],
        "answer": "B",
        "explanation": "os.path.splitext() splits the path into (root, ext). The extension includes the dot.",
    },
]

score = 0
print("=" * 55)
print(" Week 07 - Day 02 Quiz | os Module")
print("=" * 55)

for i, q in enumerate(questions, 1):
    print(f"\nQ{i}: {q['q']}")
    for opt in q["options"]:
        print(f"  {opt}")
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == q["answer"]:
        print("  Correct!")
        score += 1
    else:
        print(f"  Wrong. Answer: {q['answer']}")
    print(f"  {q['explanation']}")

print(f"\n{'=' * 55}")
print(f"Score: {score}/{len(questions)}")
if score == len(questions):
    print("Perfect! Move on to the exercises.")
elif score >= 3:
    print("Good. Review the questions you missed.")
else:
    print("Re-read lesson.py, then retake the quiz.")
