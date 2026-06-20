# =============================================================================
# Week 07 - Day 02 | The os Module — Exercises
# =============================================================================

import os

# -----------------------------------------------------------------------------
# Exercise 1 — Directory Info
# -----------------------------------------------------------------------------
# Print the following about the current working directory:
#   a) The full absolute path
#   b) Just the folder name (last component)
#   c) The parent directory path
#   d) Number of items (files + folders) directly inside it
#
# Expected output (will vary by system):
#   Full path:   C:\Users\...\Day-02
#   Folder name: Day-02
#   Parent:      C:\Users\...\Week-07_Modules
#   Items:       5

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Build a Path Safely
# -----------------------------------------------------------------------------
# Using os.path.join(), build these paths from parts and print them:
#   a) Join "projects", "myapp", "src", "main.py"
#   b) Join os.getcwd(), "output", "report.txt"
#   c) Get the absolute path of "../README.md"
#      Then print whether it exists (True/False)
#
# Expected output:
#   projects\myapp\src\main.py    (or projects/myapp/src/main.py on Linux)
#   C:\...\Day-02\output\report.txt
#   C:\...\Week-07_Modules\README.md
#   Exists: False    (README.md may or may not exist — just print the result)

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Temporary Directory Sandbox
# -----------------------------------------------------------------------------
# Create the following structure inside the current directory, then clean it up:
#
#   sandbox/
#     data/
#     logs/
#     output/
#
# Steps:
#   1. Create all three subdirectories using ONE os.makedirs() call per subdir
#      (use exist_ok=True)
#   2. Print "Created: <path>" for each
#   3. Verify each exists with os.path.isdir()
#   4. Remove them using os.rmdir() (in reverse order: output, logs, data, sandbox)
#   5. Print "Cleaned up."
#
# Note: os.rmdir() only removes EMPTY directories.

base = os.path.join(os.getcwd(), "sandbox")
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Environment Variables
# -----------------------------------------------------------------------------
# a) Print the value of the "PATH" environment variable
#    (just the first 80 characters, followed by "...")
# b) Print the user's home directory
#    Hint: try "HOME" first (Linux/Mac), then "USERPROFILE" (Windows)
# c) Check if "VIRTUAL_ENV" is set (it's set when a venv is active)
#    Print: "venv active: <path>" or "No venv active"
# d) Set a temporary variable "APP_VERSION" = "1.0.0"
#    Then read it back and print: "APP_VERSION = 1.0.0"

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Walk and Collect
# -----------------------------------------------------------------------------
# Using os.walk(), scan the PARENT directory of this file (Day-02's parent
# is Week-07_Modules) and collect:
#   a) All .py files
#   b) All .ipynb files
#
# Print:
#   .py files found:    <count>
#   .ipynb files found: <count>
#   Largest .py file:   <filename> (<size> bytes)
#
# Hints:
#   - os.path.dirname(__file__) gives the directory of THIS script
#   - os.path.getsize(path) returns file size in bytes
#   - Skip hidden directories (names starting with '.')

parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# TODO
