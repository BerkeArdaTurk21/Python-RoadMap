# =============================================================================
# Week 06 - Day 04 | try/except — Solutions
# =============================================================================

# Solution 1
# KEY INSIGHT: catch ValueError for bad strings, TypeError for None/non-string.
def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

print(safe_int("42"))    # 42
print(safe_int("abc"))   # None
print(safe_int(-7))      # -7
print(safe_int(None))    # None
print()

# Solution 2
# KEY INSIGHT: TypeError covers d being None, string, list, etc.
def get_value(d, key, default=None):
    try:
        return d[key]
    except (KeyError, TypeError):
        return default

data = {"name": "Alice", "age": 30}
print(get_value(data, "name"))               # Alice
print(get_value(data, "email", "N/A"))       # N/A
print(get_value(None, "name", "Unknown"))    # Unknown
print(get_value("not_a_dict", "x", "Unknown"))  # Unknown
print()

# Solution 3
# KEY INSIGHT: use a flag variable so finally can check if the file was opened.
def read_file(path, fallback=""):
    f = None
    try:
        f = open(path, "r", encoding="utf-8")
        return f.read()
    except FileNotFoundError:
        return fallback
    finally:
        if f:
            f.close()
        print("Closing file.")

content = read_file("nonexistent.txt", fallback="[file not found]")
print(repr(content))
print()

# Solution 4
# KEY INSIGHT: raise ValueError yourself when the range check fails — then
# a single except ValueError catches both the int() failure and the range error.
def validate_age(value):
    try:
        age = int(value)
        if not (0 <= age <= 150):
            raise ValueError(f"age must be 0-150, got {age}")
        return age
    except ValueError as e:
        if "invalid literal" in str(e):
            return f"Error: '{value}' is not a valid number"
        return f"Error: {e}"

print(validate_age("25"))    # 25
print(validate_age("abc"))   # Error: 'abc' is not a valid number
print(validate_age("200"))   # Error: age must be 0-150, got 200
print(validate_age("0"))     # 0
print()

# Solution 5
# KEY INSIGHT: finally with a counter lets you report totals even on error.
transactions = [
    ("Alice", "100"),
    ("Bob", "bad"),
    ("Carol", "250.50"),
    ("Dave", "N/A"),
]

def process_transactions(txns):
    count = len(txns)
    try:
        for name, amount_str in txns:
            try:
                amount = float(amount_str)
                print(f"Processed: {name} — ${amount}")
            except ValueError:
                print(f"Skipped: {name} — invalid amount '{amount_str}'")
    finally:
        print("---")
        print(f"Total processed: {count} transactions attempted")

process_transactions(transactions)
