# =============================================================================
# Week 06 - Day 03 | Working with Paths — Exercises
# =============================================================================
import os
from pathlib import Path

# -----------------------------------------------------------------------------
# Exercise 1 — Explore a Directory
# -----------------------------------------------------------------------------
# Use pathlib to inspect the current directory (where this script lives).
# Print:
#   - The absolute path of the current directory
#   - The number of .py files directly in the current directory
#   - Each .py file's name and size in bytes
#
# Expected output (will vary, but format):
#   Directory: C:\...\Day-03
#   Python files: 4
#     lesson.py     — 3521 bytes
#     quiz.py       — 2108 bytes
#     exercises.py  — 2044 bytes
#     solutions.py  — 1876 bytes

here = Path(__file__).parent
# TODO: print absolute path, count .py files, print each name + size
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Build a File Tree
# -----------------------------------------------------------------------------
# Create the following directory/file structure inside a folder "project_root":
#
#   project_root/
#     src/
#       main.py       (content: "# main module\n")
#       utils.py      (content: "# utilities\n")
#     tests/
#       test_main.py  (content: "# tests\n")
#     README.md       (content: "# My Project\n")
#
# After creating, use rglob("*") to list every file (not directory) with its
# relative path from project_root, sorted alphabetically.
#
# Expected output:
#   README.md
#   src/main.py
#   src/utils.py
#   tests/test_main.py

root = Path("project_root")
# TODO: create structure and list files
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Path Inspector
# -----------------------------------------------------------------------------
# Given the path string below, use pathlib to extract and print:
#   parent directory, filename, stem (name without ext), extension, absolute path.
#
# path_str = "/home/berke/projects/data_analysis/report_2026.csv"
#
# Expected output:
#   Parent:    /home/berke/projects/data_analysis
#   Filename:  report_2026.csv
#   Stem:      report_2026
#   Extension: .csv
#   Absolute:  (absolute version of the same path)

path_str = "/home/berke/projects/data_analysis/report_2026.csv"
# TODO: use Path to extract each component
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Find All Text Files
# -----------------------------------------------------------------------------
# Inside "project_root" (created in Exercise 2), add two more files:
#   project_root/docs/notes.txt   (content: "notes\n")
#   project_root/docs/todo.txt    (content: "todo\n")
#
# Then use rglob to find all .txt and .md files.
# Print them sorted, with their size in bytes.
#
# Expected output:
#   README.md         13 bytes
#   docs/notes.txt     6 bytes
#   docs/todo.txt      5 bytes

# TODO: create docs/ folder and files, then search and print
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Safe File Rename
# -----------------------------------------------------------------------------
# In project_root/src, rename "utils.py" to "helpers.py".
# Before renaming, check that the source exists and the destination does NOT.
# Print a success message if renamed, or an appropriate message otherwise.
# Then verify by listing all files in project_root/src.
#
# Expected output:
#   Renamed utils.py -> helpers.py
#   Files in src/:
#     helpers.py
#     main.py

src_dir = Path("project_root") / "src"
# TODO: rename utils.py -> helpers.py with safety checks
print()

# Cleanup
import shutil
if Path("project_root").exists():
    shutil.rmtree("project_root")
