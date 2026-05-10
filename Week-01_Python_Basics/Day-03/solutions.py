"""
================================================
Week 1 | Day 3 — Solutions
================================================
Only open this after you've genuinely tried exercises.py!
================================================
"""

# ═══════════════════════════════════════════════════
# Exercise 1 — Receipt Calculator Solution
# ═══════════════════════════════════════════════════
# Explanation: Each amount builds on the previous result — subtotal first,
# then the discount amount, then after-discount, then tax on that reduced
# price, then the final total. The :>7.2f format spec right-aligns every
# number in a 7-character field with exactly 2 decimal places, giving a
# receipt-style column layout. The discount prints as negative by negating it.
item_price = 24.99
quantity   = 3
discount   = 0.10
tax_rate   = 0.18

subtotal       = item_price * quantity
discount_amt   = subtotal * discount
after_discount = subtotal - discount_amt
tax_amt        = after_discount * tax_rate
total          = after_discount + tax_amt

print(f"Subtotal   : {subtotal:>7.2f}")
print(f"Discount   : {-discount_amt:>7.2f}")
print(f"After disc : {after_discount:>7.2f}")
print(f"Tax (18%)  : {tax_amt:>7.2f}")
print(f"Total      : {total:>7.2f}")
# Output:
# Subtotal   :   74.97
# Discount   :   -7.50
# After disc :   67.47
# Tax (18%)  :   12.14
# Total      :   79.62


# ═══════════════════════════════════════════════════
# Exercise 2 — Time Converter Solution
# ═══════════════════════════════════════════════════
# Explanation: Floor division by 3600 extracts whole hours. The remaining
# seconds (modulo 3600) are then floor-divided by 60 to get minutes.
# The final seconds are what's left after removing all complete minutes.
# No import needed — // and % do all the work.
total_seconds = 9753

hours   = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{total_seconds} seconds = {hours}h {minutes}m {seconds}s")
# Output:
# 9753 seconds = 2h 42m 33s


# ═══════════════════════════════════════════════════
# Exercise 3 — Circle Calculator Solution
# ═══════════════════════════════════════════════════
# Explanation: import math gives access to math.pi, which is more precise than
# typing 3.14 manually. All three formulas are standard geometry. The :>6.2f
# format spec right-aligns each value in a 6-character column with 2 decimal
# places, producing a clean table regardless of the number of digits.
import math

radius        = 7
diameter      = 2 * radius
circumference = 2 * math.pi * radius
area          = math.pi * radius ** 2

print(f"Radius        : {radius:>6.2f}")
print(f"Diameter      : {diameter:>6.2f}")
print(f"Circumference : {circumference:>6.2f}")
print(f"Area          : {area:>6.2f}")
# Output:
# Radius        :   7.00
# Diameter      :  14.00
# Circumference :  43.98
# Area          : 153.94


# ═══════════════════════════════════════════════════
# Exercise 4 — Digit Extractor Solution
# ═══════════════════════════════════════════════════
# Explanation: Integer arithmetic extracts each positional digit without
# converting to a string. // 1000 shifts the thousands digit into the units
# place; % 10 then isolates just that digit. The same shift-and-mask pattern
# repeats for each place value. digit_sum simply adds the four digits.
number = 4827

thousands = number // 1000
hundreds  = number // 100 % 10
tens      = number // 10  % 10
units     = number        % 10
digit_sum = thousands + hundreds + tens + units

print(f"Thousands : {thousands}")
print(f"Hundreds  : {hundreds}")
print(f"Tens      : {tens}")
print(f"Units     : {units}")
print(f"Digit sum : {digit_sum}")
# Output:
# Thousands : 4
# Hundreds  : 8
# Tens      : 2
# Units     : 7
# Digit sum : 21


# ═══════════════════════════════════════════════════
# Exercise 5 — Compound Interest Calculator Solution
# ═══════════════════════════════════════════════════
# Explanation: The compound interest formula A = P * (1 + r) ** t is applied
# once per year inside a loop so every intermediate balance is shown. The final
# values are recalculated outside the loop for the summary. :>10,.2f uses a
# comma thousands separator and right-aligns in a 10-character field.
principal   = 1000
annual_rate = 0.12
years       = 5

print(f"Principal : {principal:>10,.2f} TL")
print(f"Rate      : {annual_rate * 100:.2f}%")
print()

for year in range(1, years + 1):
    amount = principal * (1 + annual_rate) ** year
    print(f"Year {year:>2} : {amount:>11,.2f} TL")

final        = principal * (1 + annual_rate) ** years
total_earned = final - principal
growth_pct   = (total_earned / principal) * 100

print()
print(f"Total earned : {total_earned:>10,.2f} TL")
print(f"Growth       : {growth_pct:>10.2f}%")
# Output:
# Principal : 1,000.00 TL
# Rate      : 12.00%
#
# Year  1 :   1,120.00 TL
# Year  2 :   1,254.40 TL
# Year  3 :   1,404.93 TL
# Year  4 :   1,573.52 TL
# Year  5 :   1,762.34 TL
#
# Total earned :     762.34 TL
# Growth       :      76.23%
