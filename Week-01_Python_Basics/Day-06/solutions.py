"""
================================================
Week 1 | Day 6 — Solutions
================================================
Only open this after you've genuinely tried exercises.py!
================================================
"""

# ═══════════════════════════════════════════════════
# Exercise 1 — Receipt Formatter Solution
# ═══════════════════════════════════════════════════
# Explanation: Each row multiplies qty × price for the line total. Column widths
# are fixed with f-string alignment specs so every row lines up perfectly.
# The grand total is accumulated in a running sum and printed last with
# the same price alignment as the item rows.
items = [
    ("Coffee",    2, 3.50),
    ("Sandwich",  1, 6.99),
    ("Water",     3, 1.25),
    ("Chocolate", 4, 2.10),
]

W = 36
print(f"╔{'═' * W}╗")
print(f"{'COFFEE SHOP RECEIPT':^{W + 2}}")
print(f"╚{'═' * W}╝")
print(f"{'Item':<16}  {'Qty':>4}  {'Price':>7}")
print("─" * W)

total = 0.0
for name, qty, unit_price in items:
    line_total = qty * unit_price
    total += line_total
    print(f"{name:<16}  {qty:>4}  ${line_total:>6.2f}")

print("─" * W)
print(f"{'TOTAL':<22}  ${total:>6.2f}")
# Output:
# ╔════════════════════════════════════╗
#          COFFEE SHOP RECEIPT
# ╚════════════════════════════════════╝
# Item              Qty     Price
# ────────────────────────────────────
# Coffee              2     $7.00
# Sandwich            1     $6.99
# Water               3     $3.75
# Chocolate           4     $8.40
# ────────────────────────────────────
# TOTAL                    $26.14


# ═══════════════════════════════════════════════════
# Exercise 2 — Number Showcase Solution
# ═══════════════════════════════════════════════════
# Explanation: The # flag automatically adds the 0b / 0o / 0x prefix to
# binary, octal, and hex formats. All values are right-aligned in a
# field width of 12 so the column stays tidy regardless of how many digits
# the representation uses. Scientific notation uses :e which adapts to
# the magnitude automatically.
number = int(input("Enter a number: "))

print()
print(f"─── Number Formats: {number} ───")
print(f"{'Decimal':<12}: {number:>12d}")
print(f"{'Binary':<12}: {number:>12#b}")
print(f"{'Octal':<12}: {number:>12#o}")
print(f"{'Hex (lower)':<12}: {number:>12#x}")
print(f"{'Hex (upper)':<12}: {number:>12#X}")
print(f"{'Scientific':<12}: {number:>12.2e}")
# Output (number=255):
# ─── Number Formats: 255 ───
# Decimal     :        255
# Binary      : 0b11111111
# Octal       :      0o377
# Hex (lower) :      0xff
# Hex (upper) :      0XFF
# Scientific  :  2.55e+02


# ═══════════════════════════════════════════════════
# Exercise 3 — Student Table Solution
# ═══════════════════════════════════════════════════
# Explanation: Grade and status are derived per student using a helper
# function so the table loop stays clean. The class average is calculated
# once after the loop using sum() and len() on the scores list.
students = [
    ("Alice",   94),
    ("Bob",     73),
    ("Charlie", 88),
    ("Diana",   61),
    ("Eve",     97),
]

def get_grade(s):
    if s >= 90: return "A"
    if s >= 80: return "B"
    if s >= 70: return "C"
    if s >= 60: return "D"
    return "F"

W2 = 37
print(f"┌{'─' * W2}┐")
print(f"│{'STUDENT REPORT CARD':^{W2}}│")
print(f"└{'─' * W2}┘")
print(f"{'Name':<16}  {'Score':>5}  {'Grade':>5}  {'Status':>6}")
print("─" * W2)

scores = []
for name, score in students:
    grade  = get_grade(score)
    status = "Pass" if score >= 60 else "Fail"
    scores.append(score)
    print(f"{name:<16}  {score:>5}  {grade:>5}  {status:>6}")

print("─" * W2)
avg = sum(scores) / len(scores)
print(f"{'Class average:':<18} {avg:>5.1f}   ({len(scores)} students)")
# Output:
# ┌─────────────────────────────────────┐
# │         STUDENT REPORT CARD         │
# └─────────────────────────────────────┘
# Name             Score   Grade   Status
# ─────────────────────────────────────
# Alice               94       A     Pass
# Bob                 73       C     Pass
# Charlie             88       B     Pass
# Diana               61       D     Pass
# Eve                 97       A     Pass
# ─────────────────────────────────────
# Class average:    82.6   (5 students)


# ═══════════════════════════════════════════════════
# Exercise 4 — Progress Bar Solution
# ═══════════════════════════════════════════════════
# Explanation: end="\r" moves the cursor back to the start of the current
# line without advancing to the next, so the next print overwrites exactly
# the same row. flush=True forces the buffer to display immediately — without
# it the terminal might not update until a newline is written. The filled
# count is scaled proportionally: int(BAR_WIDTH * percent / 100).
import time

BAR_WIDTH = 30

for step in range(11):
    percent = step * 10
    filled  = int(BAR_WIDTH * percent / 100)
    empty   = BAR_WIDTH - filled
    bar     = "█" * filled + "░" * empty
    print(f"\r[{bar}] {percent:3d}%", end="", flush=True)
    time.sleep(0.15)

print()
print("Done!")
# Output (each frame rewrites the same line):
# [██████████████████████░░░░░░░░]  73%
# ... until:
# [██████████████████████████████] 100%
# Done!


# ═══════════════════════════════════════════════════
# Exercise 5 — Box Printer Solution
# ═══════════════════════════════════════════════════
# Explanation: The box width is driven by the longest line + 4 (2 spaces of
# padding each side). The top border embeds the title in the middle using
# string slicing — we build a full ─ border then splice in "─── Title ───".
# Each content line is padded to the content width with ljust so the right
# border │ always lands in the same column regardless of line length.
def print_box(title, lines):
    content_width = max(len(line) for line in lines)
    content_width = max(content_width, len(title) + 6)
    box_inner     = content_width + 2          # 1 space padding each side

    title_section = f"─── {title} "
    top_fill      = "─" * (box_inner - len(title_section))
    print(f"┌{title_section}{top_fill}┐")

    for line in lines:
        print(f"│ {line.ljust(content_width)} │")

    print(f"└{'─' * box_inner}┘")

print_box("Shopping List", ["Apples", "Bread", "Milk", "Eggs", "Coffee"])
print()
print_box("Note", ["Keep it simple.", "Format matters."])
# Output:
# ┌─── Shopping List ───────────────┐
# │ Apples                          │
# │ Bread                           │
# │ Milk                            │
# │ Eggs                            │
# │ Coffee                          │
# └─────────────────────────────────┘
#
# ┌─── Note ───────────────┐
# │ Keep it simple.        │
# │ Format matters.        │
# └────────────────────────┘
