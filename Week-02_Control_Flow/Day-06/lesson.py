# Week 2 - Day 6: match / case
# Topic: Python 3.10+ structural pattern matching, guard clauses

# ─────────────────────────────────────────────
# 1. WHAT IS match / case?
# ─────────────────────────────────────────────
# match / case is Python 3.10+'s structural pattern matching.
# It compares a value against multiple patterns and runs
# the first matching branch — similar to if/elif chains
# but more powerful for complex data structures.
#
# Syntax:
#   match subject:
#       case pattern1:
#           <block>
#       case pattern2:
#           <block>
#       case _:
#           <default block>

command = "quit"

match command:
    case "start":
        print("Starting the engine...")
    case "stop":
        print("Stopping the engine...")
    case "quit":
        print("Goodbye!")           # This runs
    case _:
        print("Unknown command.")


# ─────────────────────────────────────────────
# 2. _ (WILDCARD) — THE DEFAULT CASE
# ─────────────────────────────────────────────
# case _ is the catch-all, like else in if/elif/else.
# It matches anything not caught by earlier patterns.

status_code = 404

match status_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 400:
        print("Bad Request")
    case 404:
        print("Not Found")          # This runs
    case 500:
        print("Internal Server Error")
    case _:
        print(f"Unknown status: {status_code}")


# ─────────────────────────────────────────────
# 3. MATCHING MULTIPLE VALUES WITH |
# ─────────────────────────────────────────────
# Use | (OR) to match several values in one case.

day = "Saturday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Weekday")
    case "Saturday" | "Sunday":
        print("Weekend")            # This runs
    case _:
        print("Invalid day")


# ─────────────────────────────────────────────
# 4. CAPTURING VALUES IN A CASE
# ─────────────────────────────────────────────
# A bare name in a case pattern CAPTURES the value
# rather than comparing against a literal.
# Use this to catch any remaining value and name it.

def describe_number(n):
    match n:
        case 0:
            print("Zero")
        case 1:
            print("One")
        case other:                 # captures any value not matched above
            print(f"Some other number: {other}")

describe_number(0)      # Zero
describe_number(1)      # One
describe_number(42)     # Some other number: 42


# ─────────────────────────────────────────────
# 5. GUARD CLAUSES — if CONDITIONS INSIDE case
# ─────────────────────────────────────────────
# Add an if guard after a pattern to add extra conditions.
# The case only matches if BOTH the pattern AND the guard are True.

def classify_number(n):
    match n:
        case x if x < 0:
            print(f"{x} is negative")
        case 0:
            print("Zero")
        case x if x % 2 == 0:
            print(f"{x} is positive and even")
        case x:
            print(f"{x} is positive and odd")

classify_number(-5)     # -5 is negative
classify_number(0)      # Zero
classify_number(8)      # 8 is positive and even
classify_number(7)      # 7 is positive and odd


# ─────────────────────────────────────────────
# 6. MATCHING SEQUENCES (LISTS / TUPLES)
# ─────────────────────────────────────────────
# match can destructure sequences into their parts.

def describe_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (x, 0):
            print(f"On x-axis at x={x}")
        case (0, y):
            print(f"On y-axis at y={y}")
        case (x, y):
            print(f"Point at ({x}, {y})")

describe_point((0, 0))      # Origin
describe_point((5, 0))      # On x-axis at x=5
describe_point((0, 3))      # On y-axis at y=3
describe_point((4, 7))      # Point at (4, 7)

# Matching lists by length using *rest
def describe_list(lst):
    match lst:
        case []:
            print("Empty list")
        case [x]:
            print(f"Single item: {x}")
        case [x, y]:
            print(f"Two items: {x} and {y}")
        case [first, *rest]:
            print(f"First: {first}, rest: {rest}")

describe_list([])               # Empty list
describe_list([42])             # Single item: 42
describe_list([1, 2])           # Two items: 1 and 2
describe_list([1, 2, 3, 4])     # First: 1, rest: [2, 3, 4]


# ─────────────────────────────────────────────
# 7. MATCHING DICTIONARIES
# ─────────────────────────────────────────────
# case {key: value} matches dicts that contain at least those keys.

def handle_event(event):
    match event:
        case {"type": "click", "button": button}:
            print(f"Mouse click: button {button}")
        case {"type": "keypress", "key": key}:
            print(f"Key pressed: {key}")
        case {"type": "scroll", "direction": direction}:
            print(f"Scroll {direction}")
        case _:
            print("Unknown event")

handle_event({"type": "click",    "button": "left"})    # Mouse click: button left
handle_event({"type": "keypress", "key": "Enter"})      # Key pressed: Enter
handle_event({"type": "scroll",   "direction": "up"})   # Scroll up
handle_event({"type": "resize"})                        # Unknown event


# ─────────────────────────────────────────────
# 8. MATCHING WITH CLASSES
# ─────────────────────────────────────────────

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height

def describe_shape(shape):
    match shape:
        case Circle(radius=r) if r > 0:
            import math
            area = math.pi * r ** 2
            print(f"Circle with radius {r}, area = {area:.2f}")
        case Rectangle(width=w, height=h):
            print(f"Rectangle {w}×{h}, area = {w * h}")
        case _:
            print("Unknown shape")

describe_shape(Circle(5))           # Circle with radius 5, area = 78.54
describe_shape(Rectangle(4, 6))     # Rectangle 4×6, area = 24


# ─────────────────────────────────────────────
# 9. match vs if/elif — WHEN TO USE WHICH
# ─────────────────────────────────────────────
# Use if/elif when:
#   - Comparing with complex boolean expressions
#   - Working with ranges: if x > 10 and x < 20
#   - Python < 3.10 compatibility needed
#
# Use match when:
#   - Matching one value against many fixed patterns
#   - Destructuring tuples, lists, or dicts
#   - Matching class instances
#   - Code reads more clearly as pattern branches

# if/elif version — more verbose for simple dispatch
def get_day_type_if(day):
    if day in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
        return "Weekday"
    elif day in ("Saturday", "Sunday"):
        return "Weekend"
    else:
        return "Invalid"

# match version — cleaner and declarative
def get_day_type_match(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case "Saturday" | "Sunday":
            return "Weekend"
        case _:
            return "Invalid"

print(get_day_type_if("Monday"))        # Weekday
print(get_day_type_match("Saturday"))   # Weekend


# ─────────────────────────────────────────────
# 10. PRACTICAL EXAMPLE — Command Parser
# ─────────────────────────────────────────────

def parse_command(user_input):
    parts = user_input.strip().split()

    match parts:
        case ["quit"] | ["exit"]:
            return "Exiting program."
        case ["help"]:
            return "Available: quit, help, go <dir>, take <item>, drop <item>"
        case ["go", direction] if direction in ("north", "south", "east", "west"):
            return f"Moving {direction}..."
        case ["go", direction]:
            return f"Cannot go '{direction}'. Use north/south/east/west."
        case ["take", item]:
            return f"You picked up: {item}"
        case ["drop", item]:
            return f"You dropped: {item}"
        case []:
            return "Please enter a command."
        case _:
            return f"Unknown command: '{user_input}'"

commands = ["go north", "take sword", "drop shield", "go up", "help", "quit", "fly"]
for cmd in commands:
    print(f"> {cmd}  →  {parse_command(cmd)}")
