"""
================================================
Week 1 — Weekly Homework
================================================
Mini Project: Personal Finance Tracker
================================================
Skills used from this week:
  Day 1 — variables, data types, f-strings
  Day 2 — string methods (.strip(), .title())
  Day 3 — arithmetic, round(), math operations
  Day 4 — input(), int()/float(), isdigit()
  Day 5 — comparison, logical, ternary operators
  Day 6 — f-string alignment, number formatting,
           print() sep/end, progress bar trick
================================================

PROJECT DESCRIPTION
────────────────────────────────────────────────
Build a Personal Finance Tracker that:

  1. Asks for the user's name and monthly income.
  2. Asks for amounts spent in 4 categories:
       Rent, Food, Transport, Entertainment
  3. Validates that all inputs are positive numbers.
  4. Calculates:
       - Total expenses
       - Remaining balance (savings)
       - Savings rate (savings / income × 100)
       - Each category's share of total expenses (%)
  5. Prints a formatted financial report including:
       - A header with the user's name
       - An itemized expense table with percentage bars
       - A summary section with savings and a status message

EXPECTED OUTPUT (example values below)
────────────────────────────────────────────────

  ╔══════════════════════════════════════════╗
             PERSONAL FINANCE TRACKER
                  Berke Arda Turk
  ╚══════════════════════════════════════════╝

  Monthly Income    :   $5,000.00

  ─── Expenses ──────────────────────────────
  Rent              :   $1,500.00   [████████░░░░░░░░░░░░]  30.0%
  Food              :     $600.00   [███░░░░░░░░░░░░░░░░░]  12.0%
  Transport         :     $300.00   [██░░░░░░░░░░░░░░░░░░]   6.0%
  Entertainment     :     $400.00   [██░░░░░░░░░░░░░░░░░░]   8.0%
  ───────────────────────────────────────────
  Total Expenses    :   $2,800.00

  ─── Summary ───────────────────────────────
  Savings           :   $2,200.00
  Savings Rate      :       44.0%
  Status            :   ✅ Great! You're saving well.

────────────────────────────────────────────────
Try to build this yourself before reading the
solution below. Scroll down only when you're done!
────────────────────────────────────────────────
"""

# ════════════════════════════════════════════════
#                   SOLUTION
# ════════════════════════════════════════════════

# ── Helper: safe float input ──────────────────
def get_positive_float(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            if value < 0:
                print("  Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("  Invalid input. Please enter a number.")

# ── Collect inputs ────────────────────────────
print()
name   = input("Your name         : ").strip().title()
income = get_positive_float("Monthly income ($): ")

print()
print("Enter your monthly expenses:")
rent          = get_positive_float("  Rent           ($): ")
food          = get_positive_float("  Food           ($): ")
transport     = get_positive_float("  Transport      ($): ")
entertainment = get_positive_float("  Entertainment  ($): ")

# ── Calculations ─────────────────────────────
expenses = [
    ("Rent",          rent),
    ("Food",          food),
    ("Transport",     transport),
    ("Entertainment", entertainment),
]

total_expenses = sum(amt for _, amt in expenses)
savings        = income - total_expenses
savings_rate   = (savings / income * 100) if income > 0 else 0.0

# ── Status message ────────────────────────────
if savings_rate >= 30:
    status = "✅ Great! You're saving well."
elif savings_rate >= 10:
    status = "👍 Decent. Try to push savings above 30%."
elif savings_rate > 0:
    status = "⚠️  Low savings. Review your expenses."
else:
    status = "❌ You're spending more than you earn!"

# ── Report ────────────────────────────────────
W       = 44
BAR_W   = 20

print()
print(f"╔{'═' * W}╗")
print(f"{'PERSONAL FINANCE TRACKER':^{W + 2}}")
print(f"{name:^{W + 2}}")
print(f"╚{'═' * W}╝")
print()
print(f"  {'Monthly Income':<18}: {income:>10,.2f}")
print()
print(f"  {'─── Expenses ':─<{W}}")

for label, amount in expenses:
    if total_expenses > 0:
        pct   = amount / total_expenses * 100
        filled = int(BAR_W * pct / 100)
    else:
        pct    = 0.0
        filled = 0
    bar = "█" * filled + "░" * (BAR_W - filled)
    print(f"  {label:<18}: ${amount:>9,.2f}   [{bar}] {pct:5.1f}%")

print(f"  {'─' * W}")
print(f"  {'Total Expenses':<18}: ${total_expenses:>9,.2f}")
print()
print(f"  {'─── Summary ':─<{W}}")
print(f"  {'Savings':<18}: ${savings:>9,.2f}")
print(f"  {'Savings Rate':<18}: {savings_rate:>9.1f}%")
print(f"  {'Status':<18}:   {status}")
print()
