# Week 3 - Day 3: *args & **kwargs — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: Average of Any Numbers
# ─────────────────────────────────────────────
# Write a function average(*numbers) that returns the average
# of any number of arguments. Return 0 if no arguments are given.
#
# Expected output:
#   average(10, 20, 30)         → 20.0
#   average(5)                  → 5.0
#   average()                   → 0
#   average(2, 4, 6, 8, 10, 12) → 7.0


# ─────────────────────────────────────────────
# Exercise 2: Tag Builder
# ─────────────────────────────────────────────
# Write a function build_tag(tag, *content, **attributes)
# that builds a simple HTML-like string.
#   - tag        : the element name (e.g. "a", "div")
#   - *content   : strings placed inside the tag
#   - **attributes : key=value pairs converted to attributes
#
# Expected output:
#   build_tag("a", "Click me", href="https://python.org")
#     → '<a href="https://python.org">Click me</a>'
#
#   build_tag("div", "Hello", "World", id="main", cls="box")
#     → '<div id="main" cls="box">Hello World</div>'


# ─────────────────────────────────────────────
# Exercise 3: Function Forwarder
# ─────────────────────────────────────────────
# Write a function call_twice(func, *args, **kwargs) that calls
# func with the given args/kwargs TWO times and returns a list
# of both results.
#
# Expected output:
#   call_twice(pow, 2, 3)              → [8, 8]
#   call_twice(max, 5, 9, 2)           → [9, 9]
#   call_twice(str.format, "Hi {}", "Berke") → ['Hi Berke', 'Hi Berke']


# ─────────────────────────────────────────────
# Exercise 4: Flexible Dict Merger
# ─────────────────────────────────────────────
# Write a function merge(*dicts, **extras) that:
#   - Merges any number of input dicts (later wins on conflicts)
#   - Adds the **extras keyword pairs on top (highest priority)
#   - Returns the resulting merged dict
#
# Expected output:
#   merge({"a": 1, "b": 2}, {"b": 99, "c": 3}, d=4)
#     → {'a': 1, 'b': 99, 'c': 3, 'd': 4}
#
#   merge({"x": 1}, x=42, y=10)
#     → {'x': 42, 'y': 10}


# ─────────────────────────────────────────────
# Exercise 5: Mini Logger
# ─────────────────────────────────────────────
# Write a function log(level, *messages, sep=" ", **meta) that:
#   - Prints "[LEVEL] msg1 sep msg2 sep msg3 ..."
#   - If **meta is provided, prints each key=value on its own line, indented
#   - level must be uppercased automatically
#
# Expected output:
#   log("info", "User", "logged in", user="berke", ip="10.0.0.1")
#     [INFO] User logged in
#        user=berke
#        ip=10.0.0.1
#
#   log("error", "Connection", "failed", sep=" → ", host="db.local", retries=3)
#     [ERROR] Connection → failed
#        host=db.local
#        retries=3
