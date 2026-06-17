# =============================================================================
# Week 06 - Day 06 | Custom Exceptions — Solutions
# =============================================================================

# Solution 1
class AppError(Exception):
    """Base exception for this application."""

class DatabaseError(AppError):
    """Raised on database failures."""

class NetworkError(AppError):
    """Raised on network failures."""

def connect(service):
    if service == "db":
        raise DatabaseError(f"could not connect to {service}")
    if service == "net":
        raise NetworkError(f"could not connect to {service}")
    return "connected"

for svc in ["db", "net", "api"]:
    try:
        print(connect(svc))
    except AppError as e:
        print(f"{type(e).__name__}: {e}")
print()

# Solution 2
class ValidationError(Exception):
    def __init__(self, message, field, value):
        super().__init__(message)
        self.field = field
        self.value = value

    def __str__(self):
        return f"[{self.field}={self.value!r}] {super().__str__()}"

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

# Solution 3
class PaymentError(Exception):
    """Base class for payment errors."""

class InsufficientFundsError(PaymentError):
    def __init__(self, balance, amount):
        super().__init__(f"balance ${balance:.2f} < required ${amount:.2f}")
        self.balance = balance
        self.amount  = amount

class CardDeclinedError(PaymentError):
    def __init__(self, reason="unknown"):
        super().__init__(f"card declined: {reason}")
        self.reason = reason

def charge(balance, amount, card_ok=True):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    if not card_ok:
        raise CardDeclinedError("expired")
    return balance - amount

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

# Solution 4
class ConfigError(Exception):
    def __init__(self, key, reason):
        super().__init__(f"Config '{key}': {reason}")
        self.key    = key
        self.reason = reason

def load_config(cfg, required_keys):
    for key in required_keys:
        if key not in cfg:
            raise ConfigError(key, "missing")
        if cfg[key] == "":
            raise ConfigError(key, "cannot be empty")

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

# Solution 5
orders = [
    ("Alice",  100.00,  20.00, True),
    ("Bob",     10.00,  50.00, True),
    ("Carol",  200.00,  75.00, True),
]

def process_order(orders):
    for name, balance, amount, card_ok in orders:
        try:
            remaining = charge(balance, amount, card_ok)
            print(f"OK   {name}: charged ${amount:.2f}")
        except InsufficientFundsError:
            print(f"SKIP {name}: insufficient funds")
        except CardDeclinedError:
            print(f"SKIP {name}: card declined")

process_order(orders)
