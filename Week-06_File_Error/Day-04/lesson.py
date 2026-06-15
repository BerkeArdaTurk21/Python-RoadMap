# =============================================================================
# Week 06 - Day 04 | try / except — Exception Handling
# =============================================================================
# Topics: try/except basics, specific exceptions, multiple except blocks,
#         except as e, else clause, finally clause, exception hierarchy
# =============================================================================

# -----------------------------------------------------------------------------
# 1. BASIC try / except
# -----------------------------------------------------------------------------

print("── basic try/except ──")
try:
    x = int("abc")        # raises ValueError
except ValueError:
    print("Cannot convert 'abc' to int")

# Without try/except the program would crash. With it we handle gracefully.

try:
    result = 10 / 0       # raises ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero")

# -----------------------------------------------------------------------------
# 2. CATCHING SPECIFIC VS BROAD EXCEPTIONS
# -----------------------------------------------------------------------------

print("\n── specific exceptions ──")

def safe_open(filename):
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        return f"File not found: {filename}"
    except PermissionError:
        return f"Permission denied: {filename}"

print(safe_open("nonexistent.txt"))

# -----------------------------------------------------------------------------
# 3. MULTIPLE except BLOCKS
# -----------------------------------------------------------------------------
# Python tries each except clause in order — the first match wins.

print("\n── multiple except ──")

def parse_index(data, index_str):
    try:
        index = int(index_str)
        return data[index]
    except ValueError:
        return f"'{index_str}' is not a valid integer"
    except IndexError:
        return f"Index {index_str} out of range (len={len(data)})"

data = [10, 20, 30]
print(parse_index(data, "1"))     # 20
print(parse_index(data, "abc"))   # ValueError message
print(parse_index(data, "99"))    # IndexError message

# -----------------------------------------------------------------------------
# 4. except as e — INSPECTING THE EXCEPTION
# -----------------------------------------------------------------------------
# The exception object carries the error message and type.

print("\n── except as e ──")

try:
    d = {"a": 1}
    print(d["missing_key"])       # KeyError
except KeyError as e:
    print(f"KeyError: {e}")                   # KeyError: 'missing_key'
    print(f"Type:     {type(e).__name__}")    # KeyError
    print(f"Args:     {e.args}")              # ('missing_key',)

# Catching multiple types in one line
try:
    x = int("bad") + [1][99]
except (ValueError, IndexError) as e:
    print(f"Caught {type(e).__name__}: {e}")

# -----------------------------------------------------------------------------
# 5. else CLAUSE — RUNS ONLY IF NO EXCEPTION
# -----------------------------------------------------------------------------
# else is cleaner than putting success code at the bottom of try, because
# it only runs when the try block succeeded without raising.

print("\n── else clause ──")

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero!")
    else:
        print(f"{a} / {b} = {result}")    # only runs on success
        return result

divide(10, 2)    # prints result
divide(10, 0)    # prints error

# -----------------------------------------------------------------------------
# 6. finally CLAUSE — ALWAYS RUNS
# -----------------------------------------------------------------------------
# finally runs whether or not an exception occurred — useful for cleanup
# (closing files, releasing locks, etc.).

print("\n── finally clause ──")

def read_file(path):
    f = None
    try:
        f = open(path, "r")
        return f.read()
    except FileNotFoundError:
        return "File not found."
    finally:
        if f:
            f.close()    # runs even when FileNotFoundError raised
            print("File handle closed.")

print(read_file("nonexistent.txt"))

# try/except/else/finally all together:
def process(value):
    try:
        result = 100 / value
    except ZeroDivisionError:
        print("  except: zero!")
    else:
        print(f"  else:   result = {result}")
    finally:
        print("  finally: always runs")

print("\ntry/except/else/finally:")
process(5)
print()
process(0)

# -----------------------------------------------------------------------------
# 7. EXCEPTION HIERARCHY
# -----------------------------------------------------------------------------
# Exceptions are classes. Catching a parent also catches all children.
# BaseException → Exception → (ValueError, TypeError, OSError, ...)
#
# Rule: catch the MOST SPECIFIC exception first.
#
# Bad — catches everything, hides bugs:
#   except Exception:
#
# Good — specific first, broad last:
#   except ValueError:
#   except OSError:
#   except Exception as e:   # last resort: log and re-raise

print("\n── hierarchy demo ──")
try:
    open("x.txt")
except OSError as e:          # FileNotFoundError IS-A OSError
    print(f"OSError caught: {type(e).__name__}: {e}")

# =============================================================================
# SUMMARY
# =============================================================================
# ┌─────────────────────────┬───────────────────────────────────────────────┐
# │  Clause                 │  When it runs                                 │
# ├─────────────────────────┼───────────────────────────────────────────────┤
# │  try:                   │  Always (the guarded block)                   │
# │  except ExcType:        │  When ExcType (or subclass) is raised         │
# │  except ExcType as e:   │  Same, plus e holds the exception object      │
# │  except (A, B):         │  When A or B is raised                        │
# │  else:                  │  Only if NO exception occurred in try         │
# │  finally:               │  Always — exception or not                    │
# └─────────────────────────┴───────────────────────────────────────────────┘
print("\nDay 04 — try/except complete!")
