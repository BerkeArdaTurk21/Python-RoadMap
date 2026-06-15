# =============================================================================
# Week 06 - Day 04 | try/except — Exercises
# =============================================================================

# -----------------------------------------------------------------------------
# Exercise 1 — Safe Integer Converter
# -----------------------------------------------------------------------------
# Write a function safe_int(value) that tries to convert value to an integer.
# Return the integer on success, or None on failure (no crash).
#
# Expected output:
#   42
#   None
#   -7
#   None

def safe_int(value):
    pass  # TODO

print(safe_int("42"))     # 42
print(safe_int("abc"))    # None
print(safe_int(-7))       # -7
print(safe_int(None))     # None
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Safe Dictionary Lookup
# -----------------------------------------------------------------------------
# Write a function get_value(d, key, default=None) that returns d[key],
# or default if the key doesn't exist or d is not a dict (TypeError).
#
# Expected output:
#   Alice
#   N/A
#   Unknown
#   Unknown

def get_value(d, key, default=None):
    pass  # TODO

data = {"name": "Alice", "age": 30}
print(get_value(data, "name"))          # Alice
print(get_value(data, "email", "N/A")) # N/A
print(get_value(None, "name", "Unknown"))  # Unknown (TypeError)
print(get_value("not_a_dict", "x", "Unknown"))  # Unknown
print()

# -----------------------------------------------------------------------------
# Exercise 3 — File Reader with Fallback
# -----------------------------------------------------------------------------
# Write a function read_file(path, fallback="") that:
#   - Returns the file contents if the file exists
#   - Returns fallback if the file does not exist
#   - Always prints "Closing file." in a finally block (use a flag variable)
#
# Expected output (for a non-existent file):
#   Closing file.
#   (empty string or fallback text)

def read_file(path, fallback=""):
    pass  # TODO

content = read_file("nonexistent.txt", fallback="[file not found]")
print(repr(content))    # '[file not found]'
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Multi-step Validator
# -----------------------------------------------------------------------------
# Write a function validate_age(value) that:
#   - Converts value to int (catches ValueError if not numeric)
#   - Checks that 0 <= age <= 150 (catches ValueError you raise manually)
#   - Returns the valid age, or an error message string
#
# Expected output:
#   25
#   Error: 'abc' is not a valid number
#   Error: age must be 0-150, got 200
#   0

def validate_age(value):
    pass  # TODO

print(validate_age("25"))    # 25
print(validate_age("abc"))   # Error: 'abc' is not a valid number
print(validate_age("200"))   # Error: age must be 0-150, got 200
print(validate_age("0"))     # 0
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Transaction Processor
# -----------------------------------------------------------------------------
# You have a list of (name, amount_str) transactions. Write process_transactions()
# that tries to convert each amount to float. For each transaction:
#   - Print "Processed: <name> — $<amount>" on success
#   - Print "Skipped: <name> — invalid amount '<amount_str>'" on ValueError
# Use a finally block to always print the transaction count at the end.
#
# Expected output:
#   Processed: Alice — $100.0
#   Skipped: Bob — invalid amount 'bad'
#   Processed: Carol — $250.5
#   Skipped: Dave — invalid amount 'N/A'
#   ---
#   Total processed: 4 transactions attempted

transactions = [
    ("Alice", "100"),
    ("Bob", "bad"),
    ("Carol", "250.50"),
    ("Dave", "N/A"),
]

def process_transactions(txns):
    pass  # TODO

process_transactions(transactions)
