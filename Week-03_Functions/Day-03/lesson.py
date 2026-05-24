# Week 3 - Day 3: *args & **kwargs
# Topic: Variable length arguments and unpacking

# ─────────────────────────────────────────────
# 1. *args — VARIABLE NUMBER OF POSITIONAL ARGS
# ─────────────────────────────────────────────
# A parameter prefixed with * collects ALL extra positional
# arguments into a TUPLE.
# The name 'args' is convention only — *anything works.

def total(*numbers):
    print(f"  numbers = {numbers}  (type: {type(numbers).__name__})")
    return sum(numbers)

print(total(1, 2, 3))               # 6
print(total(10, 20, 30, 40, 50))    # 150
print(total())                      # 0   ← empty tuple is valid

# *args can be combined with normal parameters
def announce(prefix, *messages):
    for msg in messages:
        print(f"{prefix}: {msg}")

announce("INFO", "Server started", "Listening on 8080", "Ready")


# ─────────────────────────────────────────────
# 2. **kwargs — VARIABLE NUMBER OF KEYWORD ARGS
# ─────────────────────────────────────────────
# A parameter prefixed with ** collects ALL extra keyword
# arguments into a DICT.

def describe(**info):
    print(f"  info = {info}  (type: {type(info).__name__})")
    for key, value in info.items():
        print(f"  {key:<10} → {value}")

describe(name="Berke", age=22, city="Warsaw")
print()
describe(language="Python", level="Intermediate")


# ─────────────────────────────────────────────
# 3. COMBINING *args AND **kwargs
# ─────────────────────────────────────────────
# Order in the signature MUST be:
#   def f(positional, *args, keyword_only=default, **kwargs)

def log(level, *messages, timestamp=True, **meta):
    if timestamp:
        from datetime import datetime
        stamp = datetime.now().strftime("%H:%M:%S")
        print(f"[{stamp}] [{level}]", *messages)
    else:
        print(f"[{level}]", *messages)
    if meta:
        for k, v in meta.items():
            print(f"   {k}={v}")

log("INFO", "User logged in", user="berke", ip="192.168.1.1")
log("ERROR", "DB connection failed", timestamp=False, retries=3, host="db.local")


# ─────────────────────────────────────────────
# 4. UNPACKING WITH * AND ** AT THE CALL SITE
# ─────────────────────────────────────────────
# You can also use * and ** when CALLING a function:
#   *  unpacks an iterable into positional arguments
#   ** unpacks a dict     into keyword arguments

def greet(greeting, name, punctuation):
    print(f"{greeting}, {name}{punctuation}")

# Unpack a list/tuple into positional args
args_list = ["Hello", "Berke", "!"]
greet(*args_list)                       # Hello, Berke!

# Unpack a dict into keyword args
kwargs_dict = {"greeting": "Hi", "name": "Alice", "punctuation": "."}
greet(**kwargs_dict)                    # Hi, Alice.

# Mix both
def connect(host, port, *, user, password):
    print(f"{user}@{host}:{port}  (pw len={len(password)})")

conn_args   = ("db.example.com", 5432)
conn_kwargs = {"user": "admin", "password": "secret123"}
connect(*conn_args, **conn_kwargs)


# ─────────────────────────────────────────────
# 5. FORWARDING ARGUMENTS — A KEY PATTERN
# ─────────────────────────────────────────────
# *args and **kwargs let one function transparently pass
# arguments to another — common in wrappers, decorators, and
# subclass __init__ methods.

def debug_call(func, *args, **kwargs):
    print(f"→ Calling {func.__name__}({args}, {kwargs})")
    result = func(*args, **kwargs)
    print(f"← Returned {result}")
    return result

def add(a, b):
    return a + b

def power(base, exp=2):
    return base ** exp

debug_call(add, 3, 4)
debug_call(power, 2, exp=10)


# ─────────────────────────────────────────────
# 6. COUNTING — TYPICAL *args USE CASE
# ─────────────────────────────────────────────

def stats(*numbers):
    """Return (count, total, min, max, avg) of numbers."""
    if not numbers:
        return (0, 0, None, None, None)
    count = len(numbers)
    total = sum(numbers)
    return (count, total, min(numbers), max(numbers), total / count)

print(stats(10, 20, 30, 40, 50))
print(stats(7))
print(stats())


# ─────────────────────────────────────────────
# 7. **kwargs — FLEXIBLE CONFIGURATION
# ─────────────────────────────────────────────

def build_user(username, **fields):
    """Build a user dict — accepts any extra fields."""
    user = {"username": username}
    user.update(fields)
    return user

u1 = build_user("berke")
u2 = build_user("alice", age=30, city="London")
u3 = build_user("bob",   age=25, role="admin", active=True, score=95)

print(u1)
print(u2)
print(u3)


# ─────────────────────────────────────────────
# 8. PRACTICAL EXAMPLE — MINI EVENT EMITTER
# ─────────────────────────────────────────────

def emit(event, *receivers, sender="system", **payload):
    """
    Emit an event to multiple receivers.

    Args:
        event       (str):   Event name.
        *receivers  (str):   Any number of receiver names.
        sender      (str):   Who fired the event (keyword-only).
        **payload   (any):   Extra event data.
    """
    print(f"── Event: {event}  (from {sender}) ──")
    for r in receivers:
        print(f"  → delivered to {r}")
    if payload:
        print("  payload:")
        for k, v in payload.items():
            print(f"     {k} = {v}")

emit("login", "auth_service", "logger",
     sender="berke", ip="10.0.0.5", success=True)

print()

emit("order.created", "billing", "inventory", "email",
     sender="checkout",
     order_id=4821, total=129.99, currency="EUR")
