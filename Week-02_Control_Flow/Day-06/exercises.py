# Week 2 - Day 6: match / case — Exercises
# Solve each challenge yourself. Check solutions.py when done.
# Requires Python 3.10+

# ─────────────────────────────────────────────
# Exercise 1: HTTP Status Dispatcher
# ─────────────────────────────────────────────
# Write a function http_message(code) that uses match/case
# to return a description for these status codes:
#   200 → "OK"
#   201 → "Created"
#   301 → "Moved Permanently"
#   400 → "Bad Request"
#   401 → "Unauthorized"
#   403 → "Forbidden"
#   404 → "Not Found"
#   500 → "Internal Server Error"
#   Any other → "Unknown Status Code"
#
# Test it with: 200, 404, 500, 999
#
# Expected output:
#   200 → OK
#   404 → Not Found
#   500 → Internal Server Error
#   999 → Unknown Status Code


# ─────────────────────────────────────────────
# Exercise 2: Grade Letter with Guard
# ─────────────────────────────────────────────
# Write a function letter_grade(score) that uses match/case
# with guard clauses to return the grade:
#   90–100 → "A"
#   80–89  → "B"
#   70–79  → "C"
#   60–69  → "D"
#   0–59   → "F"
#   anything else → "Invalid score"
#
# Test with: 95, 83, 72, 61, 45, -5, 105
#
# Expected output:
#   95  → A
#   83  → B
#   72  → C
#   61  → D
#   45  → F
#   -5  → Invalid score
#   105 → Invalid score


# ─────────────────────────────────────────────
# Exercise 3: Shape Area Calculator
# ─────────────────────────────────────────────
# Write a function area(shape) that receives a tuple
# and uses match/case to calculate the area:
#   ("circle",    r)      → π * r²
#   ("rectangle", w, h)   → w * h
#   ("triangle",  b, h)   → 0.5 * b * h
#   ("square",    s)      → s * s
#   anything else         → "Unknown shape"
#
# Expected output:
#   area(("circle", 5))          → 78.54
#   area(("rectangle", 4, 6))    → 24
#   area(("triangle", 3, 8))     → 12.0
#   area(("square", 7))          → 49
#   area(("hexagon", 5))         → Unknown shape


# ─────────────────────────────────────────────
# Exercise 4: Simple Text Adventure Parser
# ─────────────────────────────────────────────
# Write a function parse(command) that splits the input
# and uses match/case to handle these commands:
#   ["look"]              → "You see a dark corridor."
#   ["go", direction]     → "You walk {direction}." (any direction)
#   ["take", item]        → "You picked up the {item}."
#   ["drop", item]        → "You dropped the {item}."
#   ["use", item, "on", target] → "You use {item} on {target}."
#   ["help"]              → "Commands: look, go, take, drop, use, help, quit"
#   ["quit"] | ["exit"]   → "Farewell, adventurer!"
#   _                     → "I don't understand that command."
#
# Expected output:
#   parse("look")             → You see a dark corridor.
#   parse("go east")          → You walk east.
#   parse("take lantern")     → You picked up the lantern.
#   parse("use key on door")  → You use key on door.
#   parse("fly")              → I don't understand that command.


# ─────────────────────────────────────────────
# Exercise 5: Traffic Light Controller
# ─────────────────────────────────────────────
# Write a function traffic_action(color) using match/case:
#   "red"    → "Stop. Wait for green."
#   "yellow" → "Prepare to stop or go."
#   "green"  → "Go! Proceed safely."
#   any other color → "Invalid signal: {color}"
#
# Then write a function next_light(color) that returns
# the next color in the cycle: red→green, green→yellow, yellow→red
#
# Simulate 6 cycles starting from "red" and print both
# the action and the next color for each step.
#
# Expected output:
#   red    → Stop. Wait for green.       | Next: green
#   green  → Go! Proceed safely.         | Next: yellow
#   yellow → Prepare to stop or go.      | Next: red
#   red    → Stop. Wait for green.       | Next: green
#   ...
