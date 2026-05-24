# Week 3 - Day 3: *args & **kwargs — Solutions

# ─────────────────────────────────────────────
# Solution 1: Average of Any Numbers
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")

def average(*numbers):
    """Return the average of any number of arguments."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

print(average(10, 20, 30))
print(average(5))
print(average())
print(average(2, 4, 6, 8, 10, 12))


# ─────────────────────────────────────────────
# Solution 2: Tag Builder
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")

def build_tag(tag, *content, **attributes):
    """Build an HTML-like tag string."""
    attrs = "".join(f' {k}="{v}"' for k, v in attributes.items())
    inner = " ".join(content)
    return f"<{tag}{attrs}>{inner}</{tag}>"

print(build_tag("a", "Click me", href="https://python.org"))
print(build_tag("div", "Hello", "World", id="main", cls="box"))


# ─────────────────────────────────────────────
# Solution 3: Function Forwarder
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")

def call_twice(func, *args, **kwargs):
    """Call func twice with the same args/kwargs."""
    return [func(*args, **kwargs), func(*args, **kwargs)]

print(call_twice(pow, 2, 3))
print(call_twice(max, 5, 9, 2))
print(call_twice(str.format, "Hi {}", "Berke"))


# ─────────────────────────────────────────────
# Solution 4: Flexible Dict Merger
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")

def merge(*dicts, **extras):
    """Merge dicts (later wins), then apply extras on top."""
    result = {}
    for d in dicts:
        result.update(d)
    result.update(extras)
    return result

print(merge({"a": 1, "b": 2}, {"b": 99, "c": 3}, d=4))
print(merge({"x": 1}, x=42, y=10))


# ─────────────────────────────────────────────
# Solution 5: Mini Logger
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")

def log(level, *messages, sep=" ", **meta):
    """Log a message with optional metadata."""
    text = sep.join(str(m) for m in messages)
    print(f"[{level.upper()}] {text}")
    for k, v in meta.items():
        print(f"   {k}={v}")

log("info", "User", "logged in", user="berke", ip="10.0.0.1")
print()
log("error", "Connection", "failed", sep=" → ", host="db.local", retries=3)
