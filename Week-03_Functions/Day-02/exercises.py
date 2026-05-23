# Week 3 - Day 2: Default & Keyword Arguments — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: Flexible Greeter
# ─────────────────────────────────────────────
# Write a function greet(name, greeting="Hello", punctuation="!")
# that prints a greeting message.
# Then call it five different ways:
#   1. Only name
#   2. Name + custom greeting
#   3. Name + custom punctuation
#   4. Name + both overridden, positionally
#   5. Name + both overridden, using keyword args in reverse order
#
# Expected output:
#   Hello, Berke!
#   Hi, Berke!
#   Hello, Berke.
#   Hey, Berke?
#   Hey, Berke?


# ─────────────────────────────────────────────
# Exercise 2: Text Box Printer
# ─────────────────────────────────────────────
# Write a function print_box(text, *, width=40, char="─", align="left")
# that prints text inside a decorative box.
# align can be "left", "center", or "right".
# All styling parameters must be keyword-only.
#
# Expected output for print_box("Hello"):
#   ────────────────────────────────────────
#   Hello
#   ────────────────────────────────────────
#
# Expected output for print_box("Hello", align="center", char="="):
#   ========================================
#                  Hello
#   ========================================


# ─────────────────────────────────────────────
# Exercise 3: Safe List Appender
# ─────────────────────────────────────────────
# Fix the mutable default bug by writing:
#   append_to(item, target=None)
# that appends item to target (creating a new list if None).
# Returns the list.
#
# Also write:
#   build_list(*items, target=None)
# that appends ALL items to the list one by one and returns it.
#
# Expected output:
#   append_to(1)          → [1]
#   append_to(2)          → [2]    ← fresh list, NOT [1, 2]
#   append_to(3, [10,20]) → [10, 20, 3]
#   build_list(1, 2, 3)   → [1, 2, 3]


# ─────────────────────────────────────────────
# Exercise 4: Invoice Generator
# ─────────────────────────────────────────────
# Write a function invoice(items, *, tax_rate=0.18,
#                          currency="USD", discount=0.0, title="Invoice")
# where items is a list of (name, price) tuples.
# All calculation params are keyword-only.
#
# It should print:
#   ── Invoice ──
#   Coffee            $3.50
#   Sandwich         $12.00
#   ─────────────────────
#   Subtotal         $15.50
#   Discount (0%)     $0.00
#   Tax (18%)         $2.79
#   TOTAL            $18.29
#
# Test with:
#   items = [("Coffee", 3.5), ("Sandwich", 12.0)]
#   invoice(items)
#   invoice(items, discount=0.10, title="Receipt", currency="EUR")


# ─────────────────────────────────────────────
# Exercise 5: Connection Config Builder
# ─────────────────────────────────────────────
# Write a function db_connect(host, port, /, *,
#                             dbname, user,
#                             password="", timeout=30,
#                             use_ssl=True)
# host and port are positional-only (before /).
# dbname and user are required keyword-only.
# password, timeout, use_ssl are optional keyword-only.
#
# The function prints a connection summary and returns
# a dictionary of the config.
#
# Expected output:
#   db_connect("localhost", 5432, dbname="mydb", user="admin")
#   → Connecting to localhost:5432/mydb as admin (ssl=True, timeout=30s)
#
#   db_connect("prod.db.com", 5432, dbname="sales", user="reader",
#              password="secret", use_ssl=True, timeout=60)
#   → Connecting to prod.db.com:5432/sales as reader (ssl=True, timeout=60s)
