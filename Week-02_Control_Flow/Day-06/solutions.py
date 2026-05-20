# Week 2 - Day 6: match / case — Solutions
# Requires Python 3.10+

import math

# ─────────────────────────────────────────────
# Solution 1: HTTP Status Dispatcher
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")

def http_message(code):
    match code:
        case 200: return "OK"
        case 201: return "Created"
        case 301: return "Moved Permanently"
        case 400: return "Bad Request"
        case 401: return "Unauthorized"
        case 403: return "Forbidden"
        case 404: return "Not Found"
        case 500: return "Internal Server Error"
        case _:   return "Unknown Status Code"

for code in [200, 404, 500, 999]:
    print(f"{code} → {http_message(code)}")


# ─────────────────────────────────────────────
# Solution 2: Grade Letter with Guard
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")

def letter_grade(score):
    match score:
        case s if 90 <= s <= 100: return "A"
        case s if 80 <= s <= 89:  return "B"
        case s if 70 <= s <= 79:  return "C"
        case s if 60 <= s <= 69:  return "D"
        case s if 0  <= s <= 59:  return "F"
        case _:                   return "Invalid score"

for s in [95, 83, 72, 61, 45, -5, 105]:
    print(f"{s:4} → {letter_grade(s)}")


# ─────────────────────────────────────────────
# Solution 3: Shape Area Calculator
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")

def area(shape):
    match shape:
        case ("circle", r):
            return round(math.pi * r ** 2, 2)
        case ("rectangle", w, h):
            return w * h
        case ("triangle", b, h):
            return 0.5 * b * h
        case ("square", s):
            return s * s
        case _:
            return "Unknown shape"

shapes = [
    ("circle",    5),
    ("rectangle", 4, 6),
    ("triangle",  3, 8),
    ("square",    7),
    ("hexagon",   5),
]
for s in shapes:
    print(f"{str(s):<30} → {area(s)}")


# ─────────────────────────────────────────────
# Solution 4: Simple Text Adventure Parser
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")

def parse(command):
    parts = command.strip().split()
    match parts:
        case ["look"]:
            return "You see a dark corridor."
        case ["go", direction]:
            return f"You walk {direction}."
        case ["take", item]:
            return f"You picked up the {item}."
        case ["drop", item]:
            return f"You dropped the {item}."
        case ["use", item, "on", target]:
            return f"You use {item} on {target}."
        case ["help"]:
            return "Commands: look, go, take, drop, use, help, quit"
        case ["quit"] | ["exit"]:
            return "Farewell, adventurer!"
        case _:
            return "I don't understand that command."

commands = ["look", "go east", "take lantern", "drop shield",
            "use key on door", "help", "quit", "fly"]
for cmd in commands:
    print(f"  {cmd:<25} → {parse(cmd)}")


# ─────────────────────────────────────────────
# Solution 5: Traffic Light Controller
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")

def traffic_action(color):
    match color:
        case "red":    return "Stop. Wait for green."
        case "yellow": return "Prepare to stop or go."
        case "green":  return "Go! Proceed safely."
        case other:    return f"Invalid signal: {other}"

def next_light(color):
    match color:
        case "red":    return "green"
        case "green":  return "yellow"
        case "yellow": return "red"
        case _:        return "red"

current = "red"
for _ in range(6):
    action = traffic_action(current)
    nxt    = next_light(current)
    print(f"{current:<7} → {action:<35} | Next: {nxt}")
    current = nxt
