# Week 3 - Day 2: Default & Keyword Arguments — Solutions

# ─────────────────────────────────────────────
# Solution 1: Flexible Greeter
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")

def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting}, {name}{punctuation}")

greet("Berke")                              # Hello, Berke!
greet("Berke", "Hi")                        # Hi, Berke!
greet("Berke", punctuation=".")             # Hello, Berke.
greet("Berke", "Hey", "?")                  # Hey, Berke?
greet("Berke", punctuation="?", greeting="Hey")  # Hey, Berke?


# ─────────────────────────────────────────────
# Solution 2: Text Box Printer
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")

def print_box(text, *, width=40, char="─", align="left"):
    """Print text inside a decorative box."""
    line = char * width
    if align == "center":
        content = text.center(width)
    elif align == "right":
        content = text.rjust(width)
    else:
        content = text
    print(line)
    print(content)
    print(line)

print_box("Hello")
print()
print_box("Hello", align="center", char="=")
print()
print_box("Right aligned", align="right", char="*", width=30)


# ─────────────────────────────────────────────
# Solution 3: Safe List Appender
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")

def append_to(item, target=None):
    """Append item to target list, creating a new one if None."""
    if target is None:
        target = []
    target.append(item)
    return target

def build_list(*items, target=None):
    """Append all items to target list and return it."""
    if target is None:
        target = []
    for item in items:
        target.append(item)
    return target

print(append_to(1))
print(append_to(2))
print(append_to(3, [10, 20]))
print(build_list(1, 2, 3))


# ─────────────────────────────────────────────
# Solution 4: Invoice Generator
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")

def invoice(items, *, tax_rate=0.18, currency="USD",
            discount=0.0, title="Invoice"):
    """Print a formatted invoice."""
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "TRY": "₺"}
    sym = symbols.get(currency, currency + " ")

    subtotal      = sum(price for _, price in items)
    discount_amt  = subtotal * discount
    taxable       = subtotal - discount_amt
    tax_amt       = taxable * tax_rate
    total         = taxable + tax_amt

    width = 30
    print(f"── {title} ──")
    for name, price in items:
        print(f"  {name:<18} {sym}{price:>6.2f}")
    print("  " + "─" * (width - 2))
    print(f"  {'Subtotal':<18} {sym}{subtotal:>6.2f}")
    print(f"  {f'Discount ({discount:.0%})':<18} {sym}{discount_amt:>6.2f}")
    print(f"  {f'Tax ({tax_rate:.0%})':<18} {sym}{tax_amt:>6.2f}")
    print(f"  {'TOTAL':<18} {sym}{total:>6.2f}")

items = [("Coffee", 3.5), ("Sandwich", 12.0)]
invoice(items)
print()
invoice(items, discount=0.10, title="Receipt", currency="EUR")


# ─────────────────────────────────────────────
# Solution 5: Connection Config Builder
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")

def db_connect(host, port, /, *,
               dbname, user,
               password="", timeout=30, use_ssl=True):
    """Build and display a database connection config."""
    print(f"Connecting to {host}:{port}/{dbname} as {user} "
          f"(ssl={use_ssl}, timeout={timeout}s)")
    return {
        "host": host, "port": port, "dbname": dbname,
        "user": user, "password": password,
        "timeout": timeout, "use_ssl": use_ssl,
    }

db_connect("localhost", 5432, dbname="mydb", user="admin")
db_connect("prod.db.com", 5432, dbname="sales", user="reader",
           password="secret", use_ssl=True, timeout=60)
