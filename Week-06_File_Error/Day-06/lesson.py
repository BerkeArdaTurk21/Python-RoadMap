# =============================================================================
# Week 06 - Day 06 | Custom Exceptions
# =============================================================================
# Topics: defining exception classes, custom attributes, hierarchy,
#         best practices, when to use custom vs built-in
# =============================================================================

# -----------------------------------------------------------------------------
# 1. DEFINING A CUSTOM EXCEPTION
# -----------------------------------------------------------------------------
# A custom exception is just a class that inherits from Exception (or a subclass).
# Minimum definition: a class with a docstring.

print("── basic custom exception ──")

class AppError(Exception):
    """Base exception for this application."""

class DatabaseError(AppError):
    """Raised when a database operation fails."""

class NetworkError(AppError):
    """Raised when a network call fails."""

try:
    raise DatabaseError("connection refused on port 5432")
except AppError as e:              # catches both Database and Network errors
    print(f"{type(e).__name__}: {e}")

# Caller can catch all AppErrors or pick specific subtypes:
for exc_cls in [DatabaseError, NetworkError]:
    try:
        raise exc_cls("test")
    except DatabaseError:
        print("  database issue")
    except NetworkError:
        print("  network issue")

# -----------------------------------------------------------------------------
# 2. ADDING CUSTOM ATTRIBUTES
# -----------------------------------------------------------------------------
# Override __init__ to accept extra data alongside the message.

print("\n── custom attributes ──")

class ValidationError(AppError):
    """Raised when input validation fails."""
    def __init__(self, message, field, value):
        super().__init__(message)
        self.field = field
        self.value = value

    def __str__(self):
        return f"[{self.field}={self.value!r}] {super().__str__()}"

try:
    raise ValidationError("must be positive", field="age", value=-5)
except ValidationError as e:
    print(e)                 # [age=-5] must be positive
    print(f"  field: {e.field}")
    print(f"  value: {e.value}")

# -----------------------------------------------------------------------------
# 3. EXCEPTION HIERARCHY — REAL EXAMPLE
# -----------------------------------------------------------------------------
# Design a hierarchy that lets callers catch broadly or specifically.

print("\n── hierarchy ──")

class PaymentError(Exception):
    """Base class for all payment errors."""

class InsufficientFundsError(PaymentError):
    def __init__(self, balance, amount):
        super().__init__(f"balance ${balance:.2f} < amount ${amount:.2f}")
        self.balance = balance
        self.amount  = amount

class CardDeclinedError(PaymentError):
    def __init__(self, reason="unknown"):
        super().__init__(f"card declined: {reason}")
        self.reason = reason

class PaymentGatewayError(PaymentError):
    """Raised when the payment gateway is unreachable."""

def process_payment(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

# Catch specific
try:
    process_payment(50.00, 100.00)
except InsufficientFundsError as e:
    print(f"Insufficient funds: {e}")
    print(f"  short by ${e.amount - e.balance:.2f}")

# Catch broad
try:
    raise CardDeclinedError("expired")
except PaymentError as e:
    print(f"Payment failed: {e}")

# -----------------------------------------------------------------------------
# 4. BEST PRACTICES
# -----------------------------------------------------------------------------

# ✅ Always inherit from Exception (not BaseException)
#    BaseException also covers KeyboardInterrupt and SystemExit — you
#    almost never want to swallow those.

# ✅ Name ends with "Error" for error-like exceptions
#    class ConfigError, class ValidationError, class ParseError

# ✅ One hierarchy per domain / subsystem
#    class AppError → DatabaseError / NetworkError / AuthError

# ✅ Keep the message human-readable
#    raise ValidationError("email cannot be empty", field="email", value="")

# ✅ Use built-in exceptions when they fit
#    Don't create NumberTooSmallError — just raise ValueError

# ❌ Don't create an exception for every small thing
#    A deep hierarchy with 30 classes is hard to maintain.

print("\n── best practices demo ──")

class ConfigError(Exception):
    """Raised when application config is invalid or missing."""
    def __init__(self, key, reason):
        super().__init__(f"Config key '{key}': {reason}")
        self.key = key

def load_config(cfg: dict, key: str):
    if key not in cfg:
        raise ConfigError(key, "missing")
    val = cfg[key]
    if not val:
        raise ConfigError(key, "cannot be empty")
    return val

cfg = {"db_host": "localhost", "db_name": ""}
for k in ["db_host", "db_name", "db_port"]:
    try:
        print(f"  {k} = {load_config(cfg, k)!r}")
    except ConfigError as e:
        print(f"  ConfigError: {e}")

# -----------------------------------------------------------------------------
# 5. WHEN TO USE CUSTOM vs BUILT-IN EXCEPTIONS
# -----------------------------------------------------------------------------
#
# Use BUILT-IN:
#   - The standard type already semantically fits: ValueError, TypeError,
#     KeyError, IndexError, FileNotFoundError, etc.
#   - You want callers to use standard except clauses.
#
# Use CUSTOM:
#   - You need to attach extra data (field name, error code, HTTP status).
#   - You want callers to distinguish errors from your library vs others.
#   - You are building a library/package and want a stable public API.
#   - You need a hierarchy: callers can catch broad or specific.

# =============================================================================
# SUMMARY
# =============================================================================
# ┌──────────────────────────────┬────────────────────────────────────────────┐
# │  Pattern                     │  Purpose                                   │
# ├──────────────────────────────┼────────────────────────────────────────────┤
# │  class E(Exception): pass    │  Minimal custom exception                  │
# │  class E(AppError): ...      │  Part of an exception hierarchy            │
# │  super().__init__(msg)       │  Pass message to base Exception             │
# │  self.field = field          │  Store extra data on the exception          │
# │  except AppError as e:       │  Catch all subtypes of AppError            │
# └──────────────────────────────┴────────────────────────────────────────────┘
print("\nDay 06 — Custom Exceptions complete!")
