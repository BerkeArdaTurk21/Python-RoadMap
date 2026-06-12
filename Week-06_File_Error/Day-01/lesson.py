# =============================================================================
# Week 06 - Day 01 | Reading Files
# =============================================================================
# Topics: open(), file modes, read(), readline(), readlines(),
#         with statement, iterating over file, seek(), tell()
# =============================================================================

# -----------------------------------------------------------------------------
# 1. OPENING A FILE — open()
# -----------------------------------------------------------------------------
# Syntax: open(filepath, mode, encoding)
#
# Common modes:
#   'r'  — read (default) — file must exist
#   'w'  — write — creates or OVERWRITES
#   'a'  — append — creates or adds to end
#   'b'  — binary mode (combine: 'rb', 'wb')
#   'x'  — exclusive create — fails if file exists
#
# Always specify encoding='utf-8' to avoid platform differences.

# We create a sample file first, then demonstrate reading.
import os

SAMPLE_PATH = "sample.txt"

# Create a sample file for the lesson
with open(SAMPLE_PATH, "w", encoding="utf-8") as f:
    f.write("Line 1: Hello, World!\n")
    f.write("Line 2: Python file I/O\n")
    f.write("Line 3: Reading is easy\n")
    f.write("Line 4: with statement rocks\n")
    f.write("Line 5: EOF")

# -----------------------------------------------------------------------------
# 2. THE with STATEMENT — ALWAYS USE IT
# -----------------------------------------------------------------------------
# 'with open(...) as f:' ensures the file is CLOSED automatically
# even if an exception occurs inside the block.
# Manually calling f.close() is error-prone — use 'with' instead.

with open(SAMPLE_PATH, "r", encoding="utf-8") as f:
    content = f.read()   # reads the ENTIRE file as one string

print("── read() ──")
print(content)

# After the 'with' block, f is closed:
print(f.closed)   # True

# -----------------------------------------------------------------------------
# 3. read() vs readline() vs readlines()
# -----------------------------------------------------------------------------

# read() — entire file as one string
with open(SAMPLE_PATH, "r", encoding="utf-8") as f:
    all_text = f.read()
print("read():", len(all_text), "chars")

# readline() — one line at a time
with open(SAMPLE_PATH, "r", encoding="utf-8") as f:
    print("readline() x2:")
    print(f.readline(), end="")   # Line 1
    print(f.readline(), end="")   # Line 2

# readlines() — all lines as a list
with open(SAMPLE_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()
print("readlines():", lines[:2])  # ['Line 1: ...\n', 'Line 2: ...\n']

# -----------------------------------------------------------------------------
# 4. ITERATING OVER A FILE — MOST MEMORY-EFFICIENT
# -----------------------------------------------------------------------------
# For large files, iterate line by line instead of loading everything at once.

print("── iterate ──")
with open(SAMPLE_PATH, "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())   # strip trailing newline

# -----------------------------------------------------------------------------
# 5. seek() AND tell()
# -----------------------------------------------------------------------------
# tell()     — returns current file position (bytes from start)
# seek(pos)  — moves to position pos (0 = start, use SEEK_END for end)

with open(SAMPLE_PATH, "r", encoding="utf-8") as f:
    print(f.tell())       # 0 — at start
    f.read(6)             # read 6 chars
    print(f.tell())       # 6

    f.seek(0)             # jump back to start
    first_line = f.readline()
    print(first_line.rstrip())   # Line 1: Hello, World!

# -----------------------------------------------------------------------------
# 6. READING NON-EXISTENT FILES SAFELY
# -----------------------------------------------------------------------------
# open() raises FileNotFoundError if the file doesn't exist.
# Always handle this — covered in detail in Day 04.

try:
    with open("does_not_exist.txt", "r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(f"File not found: {e}")

# -----------------------------------------------------------------------------
# 7. READING CSV-LIKE DATA
# -----------------------------------------------------------------------------
# Files can hold structured data. Here's a simple manual approach.
# (The 'csv' module is the proper tool — shown in Week 07.)

CSV_PATH = "students.csv"
with open(CSV_PATH, "w", encoding="utf-8") as f:
    f.write("name,grade\n")
    f.write("Alice,90\n")
    f.write("Bob,85\n")
    f.write("Carol,92\n")

print("── CSV read ──")
with open(CSV_PATH, "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")
    print("Columns:", header)
    for line in f:
        name, grade = line.strip().split(",")
        print(f"  {name}: {grade}")

# Cleanup
os.remove(SAMPLE_PATH)
os.remove(CSV_PATH)

# =============================================================================
# SUMMARY
# =============================================================================
# ┌─────────────────┬─────────────────────────────────────────────────────┐
# │  Method         │  What it does                                       │
# ├─────────────────┼─────────────────────────────────────────────────────┤
# │  open(f,'r')    │  Opens file for reading (default mode)              │
# │  f.read()       │  Reads entire file as one string                    │
# │  f.readline()   │  Reads one line (keeps \n)                          │
# │  f.readlines()  │  Returns list of all lines                          │
# │  for line in f  │  Iterates line by line (memory efficient)           │
# │  f.tell()       │  Returns current byte position                      │
# │  f.seek(n)      │  Jumps to byte position n                           │
# │  with open()    │  Auto-closes file — ALWAYS use this                 │
# └─────────────────┴─────────────────────────────────────────────────────┘
print("\nDay 01 — Reading Files complete!")
