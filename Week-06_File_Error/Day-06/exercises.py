# =============================================================================
# Week 06 - Day 06 | Custom Exceptions — Exercises
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Minimal Hierarchy
# -----------------------------------------------------------------------------
# Create:
#   AppError(Exception)             — base for your app
#     DatabaseError(AppError)       — DB problems
#     NetworkError(AppError)        — network problems
#
# Write connect(service) that raises DatabaseError if service == "db"
# and NetworkError if service == "net", else returns "connected".
#
# Expected output:
#   DatabaseError: could not connect to db
#   NetworkError: could not connect to net
#   connected

class AppError(Exception):
    pass  # TODO

class DatabaseError(AppError):
    pass  # TODO

class NetworkError(AppError):
    pass  # TODO

def connect(service):
    pass  # TODO

for svc in ["db", "net", "api"]:
    try:
        print(connect(svc))
    except AppError as e:
        print(f"{type(e).__name__}: {e}")
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Exception with Extra Attributes
# -----------------------------------------------------------------------------
# Create ValidationError(Exception) with:
#   __init__(self, message, field, value)
#   __str__ returns "[<field>=<value!r>] <message>"
#
# Expected output:
#   [email=''] must not be empty
#   field=email, value=''
#   [age=-5] must be >= 0
#   field=age, value=-5

class ValidationError(Exception):
    pass  # TODO

try:
    raise ValidationError("must not be empty", field="email", value="")
except ValidationError as e:
    print(e)
    print(f"field={e.field}, value={e.value!r}")

try:
    raise ValidationError("must be >= 0", field="age", value=-5)
except ValidationError as e:
    print(e)
    print(f"field={e.field}, value={e.value!r}")
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Payment Error Hierarchy
# -----------------------------------------------------------------------------
# Create:
#   PaymentError(Exception)
#     InsufficientFundsError(PaymentError)  — stores balance and amount
#     CardDeclinedError(PaymentError)       — stores reason string
#
# Write charge(balance, amount) that raises the appropriate error.
#
# Expected output:
#   InsufficientFundsError: balance $30.00 < required $50.00
#   Short by: $20.00
#   CardDeclinedError: card declined: expired
#   Reason: expired
#   Charged! Remaining: $50.00

class PaymentError(Exception):
    pass  # TODO

class InsufficientFundsError(PaymentError):
    pass  # TODO

class CardDeclinedError(PaymentError):
    pass  # TODO

def charge(balance, amount, card_ok=True):
    pass  # TODO

try:
    charge(30.00, 50.00)
except InsufficientFundsError as e:
    print(f"InsufficientFundsError: {e}")
    print(f"Short by: ${e.amount - e.balance:.2f}")

try:
    charge(100.00, 50.00, card_ok=False)
except CardDeclinedError as e:
    print(f"CardDeclinedError: {e}")
    print(f"Reason: {e.reason}")

try:
    remaining = charge(100.00, 50.00)
    print(f"Charged! Remaining: ${remaining:.2f}")
except PaymentError as e:
    print(f"Payment failed: {e}")
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Config Loader
# -----------------------------------------------------------------------------
# Create ConfigError(Exception) with attributes: key, reason.
# __str__ returns "Config '<key>': <reason>"
#
# Write load_config(cfg, required_keys) that raises ConfigError for
# any missing key or empty-string value.
#
# Expected output:
#   Config 'port': missing
#   Config 'host': cannot be empty
#   Config 'name': missing

class ConfigError(Exception):
    pass  # TODO

def load_config(cfg, required_keys):
    pass  # TODO

try:
    load_config({"host": "", "user": "admin"}, ["host", "user", "port"])
except ConfigError as e:
    print(e)

try:
    load_config({"host": ""}, ["host"])
except ConfigError as e:
    print(e)

try:
    load_config({"db": "mydb"}, ["db", "name"])
except ConfigError as e:
    print(e)
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Catching the Right Level
# -----------------------------------------------------------------------------
# Using the PaymentError hierarchy from Exercise 3, write process_order(orders)
# that iterates a list of (balance, amount) tuples.
# For each:
#   - On InsufficientFundsError: print "SKIP <name>: insufficient funds"
#   - On CardDeclinedError: print "SKIP <name>: card declined"
#   - On success: print "OK   <name>: charged $<amount>"
#
# Expected output:
#   OK   Alice: charged $20.00
#   SKIP Bob: insufficient funds
#   OK   Carol: charged $75.00

orders = [
    ("Alice", 100.00, 20.00, True),
    ("Bob",    10.00, 50.00, True),
    ("Carol",  200.00, 75.00, True),
]

def process_order(orders):
    pass  # TODO

process_order(orders)
