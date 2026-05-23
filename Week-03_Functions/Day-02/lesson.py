# Week 3 - Day 2: Default & Keyword Arguments
# Topic: Default values, keyword arguments, argument order

# ─────────────────────────────────────────────
# 1. DEFAULT PARAMETER VALUES
# ─────────────────────────────────────────────
# Assign a default value to a parameter with =
# If the caller does NOT provide that argument,
# the default is used automatically.

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Berke")              # Hello, Berke!      ← default used
greet("Alice", "Hi")        # Hi, Alice!         ← default overridden
greet("Bob",   "Welcome")   # Welcome, Bob!

# Multiple defaults
def create_user(username, role="member", active=True):
    print(f"User: {username} | Role: {role} | Active: {active}")

create_user("berke")                        # member, True
create_user("admin_user", "admin")          # admin, True
create_user("old_user", "member", False)    # member, False


# ─────────────────────────────────────────────
# 2. KEYWORD ARGUMENTS
# ─────────────────────────────────────────────
# When calling a function you can name the arguments explicitly.
# This lets you pass them in ANY order and makes the call clearer.

def power(base, exponent):
    return base ** exponent

# Positional — order matters
print(power(2, 8))              # 256

# Keyword — order does NOT matter
print(power(exponent=8, base=2))    # 256 — same result
print(power(base=3, exponent=3))    # 27

# Mix: positional first, then keyword
def connect(host, port, timeout=30, use_ssl=True):
    print(f"{host}:{port}  timeout={timeout}  ssl={use_ssl}")

connect("db.example.com", 5432)                         # defaults
connect("db.example.com", 5432, timeout=60)             # one keyword
connect("db.example.com", 5432, use_ssl=False)          # skip timeout
connect("db.example.com", 5432, timeout=10, use_ssl=False)


# ─────────────────────────────────────────────
# 3. ARGUMENT ORDER RULES
# ─────────────────────────────────────────────
# Python enforces a strict order in function signatures:
#
#   def f(positional, /, normal, *, keyword_only)
#
# Simplified everyday rule:
#   1. Required parameters (no default)      come FIRST
#   2. Optional parameters (with default)    come AFTER
#
# This is WRONG — SyntaxError:
#   def bad(greeting="Hi", name):    ← default before required

def describe(name, age, city="Unknown", country="Unknown"):
    print(f"{name}, {age}, from {city}, {country}")

describe("Berke", 22)
describe("Alice", 30, "London")
describe("Bob",   25, country="USA")
describe("Eve",   28, "Paris", "France")


# ─────────────────────────────────────────────
# 4. KEYWORD-ONLY ARGUMENTS (after *)
# ─────────────────────────────────────────────
# Parameters after a bare * can ONLY be passed by keyword,
# never positionally. This prevents mistakes in function calls.

def send_email(to, subject, *, cc="", bcc="", priority="normal"):
    print(f"To: {to} | Subject: {subject}")
    if cc:       print(f"  CC: {cc}")
    if bcc:      print(f"  BCC: {bcc}")
    print(f"  Priority: {priority}")

send_email("alice@example.com", "Hello")
send_email("bob@example.com",   "Meeting", cc="manager@example.com")
send_email("team@example.com",  "Alert",   priority="high", bcc="log@example.com")

# This would raise TypeError — 'cc' is keyword-only:
# send_email("x@x.com", "Subj", "copy@x.com")   ← wrong


# ─────────────────────────────────────────────
# 5. POSITIONAL-ONLY ARGUMENTS (before /)
# ─────────────────────────────────────────────
# Parameters before / can ONLY be passed positionally.
# Available since Python 3.8.

def circle_area(radius, /, precision=2):
    import math
    return round(math.pi * radius ** 2, precision)

print(circle_area(5))               # 78.54
print(circle_area(5, precision=4))  # 78.5398
# circle_area(radius=5)  ← TypeError: positional-only


# ─────────────────────────────────────────────
# 6. MUTABLE DEFAULT ARGUMENT — COMMON PITFALL
# ─────────────────────────────────────────────
# NEVER use a mutable object (list, dict) as a default value.
# The same object is shared across all calls.

# ❌ BUG — list is created ONCE and reused:
def append_bad(item, items=[]):
    items.append(item)
    return items

print(append_bad("a"))  # ['a']
print(append_bad("b"))  # ['a', 'b']  ← unexpected!
print(append_bad("c"))  # ['a', 'b', 'c']

# ✅ CORRECT — use None as default, create inside the function:
def append_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(append_good("a"))  # ['a']
print(append_good("b"))  # ['b']  ← fresh list every time
print(append_good("c"))  # ['c']


# ─────────────────────────────────────────────
# 7. PRACTICAL PATTERNS
# ─────────────────────────────────────────────

# Pattern 1 — Configuration function with many optional settings
def create_chart(data, *, title="Chart", xlabel="X", ylabel="Y",
                 color="blue", figsize=(10, 6), grid=True):
    print(f"Chart: '{title}'  size={figsize}  color={color}  grid={grid}")
    print(f"  axes: {xlabel} / {ylabel}")
    print(f"  data points: {len(data)}")

create_chart([1, 2, 3, 4])
create_chart([10, 20, 30], title="Sales", color="green", ylabel="Revenue")

# Pattern 2 — Flexible formatter
def format_price(amount, *, currency="USD", decimals=2, symbol_first=True):
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "TRY": "₺"}
    symbol  = symbols.get(currency, currency)
    num_str = f"{amount:,.{decimals}f}"
    if symbol_first:
        return f"{symbol}{num_str}"
    return f"{num_str} {symbol}"

print(format_price(1999.5))
print(format_price(1999.5, currency="EUR", symbol_first=False))
print(format_price(1999.5, currency="TRY", decimals=0))


# ─────────────────────────────────────────────
# 8. PRACTICAL EXAMPLE — Report Generator
# ─────────────────────────────────────────────

def print_report(title, data, *,
                 separator="─",
                 width=40,
                 show_count=True,
                 show_total=False):
    """
    Print a formatted report.

    Args:
        title      (str):  Report title.
        data       (list): List of numeric values.
        separator  (str):  Character for divider lines.
        width      (int):  Line width.
        show_count (bool): Show number of entries.
        show_total (bool): Show sum of values.
    """
    print(separator * width)
    print(f"  {title.upper():^{width - 4}}")
    print(separator * width)
    for i, value in enumerate(data, 1):
        print(f"  {i:2}. {value}")
    print(separator * width)
    if show_count:
        print(f"  Count : {len(data)}")
    if show_total:
        print(f"  Total : {sum(data)}")
    if show_count or show_total:
        print(separator * width)

scores = [88, 92, 75, 95, 60, 83]

print_report("Student Scores", scores)
print()
print_report("Monthly Sales", [1200, 980, 1500, 870],
             separator="=", width=35,
             show_count=True, show_total=True)
