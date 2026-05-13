"""
================================================
Week 1 | Day 6 — Exercises
================================================
Instructions: Solve each exercise yourself.
              Do NOT open solutions.py until you have tried your best.
              Each exercise is a small runnable program — write real code.
================================================
"""

# ─────────────────────────────────────────────────
# Exercise 1 — Receipt Formatter (Difficulty: Easy)
# ─────────────────────────────────────────────────
# Description: Print a formatted shopping receipt using f-strings.
#   Use field widths and alignment to make columns line up perfectly.
#
#   Items to display:
#     ("Coffee",    2,  3.50)
#     ("Sandwich",  1,  6.99)
#     ("Water",     3,  1.25)
#     ("Chocolate", 4,  2.10)
#
#   Expected output:
#     ╔══════════════════════════════════╗
#            COFFEE SHOP RECEIPT
#     ╚══════════════════════════════════╝
#     Item              Qty     Price
#     ──────────────────────────────────
#     Coffee              2     $7.00
#     Sandwich            1     $6.99
#     Water               3     $3.75
#     Chocolate           4     $8.40
#     ──────────────────────────────────
#     TOTAL                    $26.14
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 2 — Number Showcase (Difficulty: Easy)
# ─────────────────────────────────────────────────
# Description: Ask the user for an integer and print it in 6 different formats.
#
#   Expected output (example: number = 255):
#     Enter a number: 255
#
#     ─── Number Formats: 255 ───
#     Decimal     :        255
#     Binary      : 0b11111111
#     Octal       :      0o377
#     Hex (lower) :      0xff
#     Hex (upper) :      0XFF
#     Scientific  :  2.55e+02
#
#   Hint: Use the # flag for binary/octal/hex prefixes.
#   Hint: Right-align all values in a field width of 12.
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 3 — Student Table (Difficulty: Medium)
# ─────────────────────────────────────────────────
# Description: Print a nicely formatted table of students.
#   Calculate each student's letter grade and include it in the table.
#   Print a footer showing the class average.
#
#   Grade scale: A≥90  B≥80  C≥70  D≥60  F<60
#
#   Students:
#     ("Alice",   94)
#     ("Bob",     73)
#     ("Charlie", 88)
#     ("Diana",   61)
#     ("Eve",     97)
#
#   Expected output:
#     ┌─────────────────────────────────────┐
#     │         STUDENT REPORT CARD         │
#     └─────────────────────────────────────┘
#     Name             Score   Grade   Status
#     ─────────────────────────────────────
#     Alice               94       A     Pass
#     Bob                 73       C     Pass
#     Charlie             88       B     Pass
#     Diana               61       D     Pass
#     Eve                 97       A     Pass
#     ─────────────────────────────────────
#     Class average:    82.6   (5 students)
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 4 — Progress Bar (Difficulty: Medium)
# ─────────────────────────────────────────────────
# Description: Simulate a loading progress bar that rewrites itself on one line.
#   Use end="\r" to move the cursor back to the start of the line each step.
#   Bar width: 30 characters.
#   Steps: 0% → 100% in 10 steps (0, 10, 20, ... 100).
#
#   Format of each frame (all on the same line, rewriting):
#     [████████████████████░░░░░░░░░░]  67%
#
#   Use "█" for filled portion and "░" for empty portion.
#   After reaching 100%, print a final newline and "Done!".
#
#   Hint: filled = int(BAR_WIDTH * percent / 100)
#         Use time.sleep(0.15) between steps so you can see it move.
#
# Write your solution below:


# ─────────────────────────────────────────────────
# Exercise 5 — Box Printer (Difficulty: Hard)
# ─────────────────────────────────────────────────
# Description: Build a function print_box(title, lines) that prints any list
#   of strings inside a decorative ASCII box. The box width adapts to the
#   longest line. The title is centered in the top border.
#
#   Requirements:
#     - Box width = max line length + 4 (2 padding each side)
#     - Title is embedded in the top border: ─── Title ───
#     - Each content line is left-aligned inside the box
#     - Bottom border is plain ─ characters
#
#   Call it with:
#     print_box("Shopping List", ["Apples", "Bread", "Milk", "Eggs", "Coffee"])
#     print_box("Note", ["Keep it simple.", "Format matters."])
#
#   Expected output:
#     ┌─── Shopping List ───────────────┐
#     │ Apples                          │
#     │ Bread                           │
#     │ Milk                            │
#     │ Eggs                            │
#     │ Coffee                          │
#     └─────────────────────────────────┘
#
#     ┌─── Note ───────────────┐
#     │ Keep it simple.        │
#     │ Format matters.        │
#     └────────────────────────┘
#
# Write your solution below:
