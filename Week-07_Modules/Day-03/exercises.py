# =============================================================================
# Week 07 - Day 03 | sys & argparse — Exercises
# =============================================================================

import sys
import argparse

# -----------------------------------------------------------------------------
# Exercise 1 — Argument Echo
# -----------------------------------------------------------------------------
# Using sys.argv, print:
#   a) The script name (without any directory path — just the file name)
#   b) The number of real arguments passed (excluding the script name)
#   c) Each argument on its own line, numbered starting at 1
#
# Run:  python exercises.py apple banana cherry
# Expected output:
#   Script: exercises.py
#   Count:  3
#   1: apple
#   2: banana
#   3: cherry
#
# Hint: os.path.basename() strips the directory from a path.

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Sum the Numbers (with validation)
# -----------------------------------------------------------------------------
# Read all arguments from sys.argv[1:], convert them to integers, and print
# their sum. If ANY argument is not a valid integer, print an error message
# to stderr and exit with code 1.
#
# Run:  python exercises.py 10 20 30   ->  Sum: 60   (exit 0)
# Run:  python exercises.py 10 abc 30  ->  Error: 'abc' is not an integer (exit 1)
#
# Hint: use sys.exit(1) after printing to file=sys.stderr.

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Build a Calculator CLI with argparse
# -----------------------------------------------------------------------------
# Create an ArgumentParser for a calculator that accepts:
#   - two positional arguments 'a' and 'b' (type=float)
#   - an optional '--op' with choices [add, sub, mul, div], default 'add'
#   - a flag '--round' that, when present, rounds the result to a whole number
#
# Parse this demo list and print the result:
#   demo = ["12", "5", "--op", "mul"]   -> Result: 60.0
#   (with --round it would print 60)
#
# Handle division by zero gracefully (print a message, don't crash).

demo = ["12", "5", "--op", "mul"]
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 4 — File-Info Tool with Options
# -----------------------------------------------------------------------------
# Build a parser that takes:
#   - a positional 'path' (a file path)
#   - '--lines' flag: if set, also report the line count
#   - '--verbose' / '-v' flag: if set, print extra detail
#
# Parse demo = [__file__, "--lines", "-v"] and print:
#   Path:   <path>
#   Exists: True/False
#   Size:   <bytes> bytes        (only if the file exists)
#   Lines:  <n>                  (only if --lines AND the file exists)
#   [verbose] Absolute path: ... (only if --verbose)
#
# Hint: os.path.exists / os.path.getsize; count lines by reading the file.

demo = [__file__, "--lines", "-v"]
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Mini "note" Tool with Subcommands
# -----------------------------------------------------------------------------
# Build a parser with subcommands (add_subparsers, dest="command"):
#   add   -> positional 'text', optional '--tag' (default "general")
#   list  -> flag '--count' that prints how many notes would be listed
#   del   -> positional 'index' (type=int)
#
# Then dispatch and print for each of these demo invocations:
#   ["add", "Buy milk", "--tag", "shopping"] -> Added note 'Buy milk' [shopping]
#   ["list", "--count"]                      -> Listing notes (count mode)
#   ["del", "3"]                             -> Deleting note #3
#
# Hint: loop over the three demo arg-lists, call parser.parse_args(demo),
#       and branch on args.command.

demos = [
    ["add", "Buy milk", "--tag", "shopping"],
    ["list", "--count"],
    ["del", "3"],
]
# TODO
