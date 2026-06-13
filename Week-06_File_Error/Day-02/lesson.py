# =============================================================================
# Week 06 - Day 02 | Writing Files
# =============================================================================
# Topics: write(), writelines(), file modes (w/a/x/r+), overwrite vs append,
#         writing structured data, safe atomic writes
# =============================================================================

import os

# -----------------------------------------------------------------------------
# 1. WRITING WITH 'w' MODE
# -----------------------------------------------------------------------------
# 'w' creates the file if it doesn't exist, or OVERWRITES it if it does.
# DANGER: previous content is lost instantly when you open in 'w' mode.

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.write("Second line\n")
    f.write("Third line\n")

with open("output.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Opening again in 'w' erases everything:
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Overwritten!\n")

with open("output.txt", "r", encoding="utf-8") as f:
    print(f.read())   # only "Overwritten!"

# -----------------------------------------------------------------------------
# 2. APPENDING WITH 'a' MODE
# -----------------------------------------------------------------------------
# 'a' adds content to the END without touching existing content.

LOG = "log.txt"
for i in range(1, 4):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(f"Entry {i}\n")

with open(LOG, "r", encoding="utf-8") as f:
    print(f.read())   # Entry 1 \n Entry 2 \n Entry 3

# -----------------------------------------------------------------------------
# 3. write() vs writelines()
# -----------------------------------------------------------------------------
# write(str)         — writes one string, returns character count
# writelines(iterable) — writes each string in the iterable; NO auto \n added

lines = ["apple\n", "banana\n", "cherry\n"]

with open("fruits.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)   # NO newlines added — must be in the strings

with open("fruits.txt", "r", encoding="utf-8") as f:
    print(f.read())

# Common pattern: join with newlines
words = ["dog", "cat", "bird"]
with open("animals.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(words) + "\n")

# -----------------------------------------------------------------------------
# 4. FILE MODES SUMMARY
# -----------------------------------------------------------------------------
# Mode  | Reads? | Writes? | Creates? | Truncates? | Position
# ------|--------|---------|----------|------------|----------
# 'r'   |  yes   |   no    |   no     |    no      | start
# 'w'   |  no    |   yes   |   yes    |    YES     | start
# 'a'   |  no    |   yes   |   yes    |    no      | end
# 'x'   |  no    |   yes   | only new |    no      | start  (fails if exists)
# 'r+'  |  yes   |   yes   |   no     |    no      | start
# 'w+'  |  yes   |   yes   |   yes    |    YES     | start

# 'x' — exclusive create (prevents accidental overwrite):
try:
    with open("new_only.txt", "x", encoding="utf-8") as f:
        f.write("Created fresh\n")
    with open("new_only.txt", "x", encoding="utf-8") as f:  # second time fails
        f.write("This will fail\n")
except FileExistsError as e:
    print(f"FileExistsError: {e}")

# -----------------------------------------------------------------------------
# 5. READING AND WRITING — 'r+' MODE
# -----------------------------------------------------------------------------
# 'r+' opens for reading AND writing without truncating.
# Cursor starts at position 0.

with open("output.txt", "r+", encoding="utf-8") as f:
    content = f.read()
    f.seek(0)
    f.write("PATCHED: " + content)

with open("output.txt", "r", encoding="utf-8") as f:
    print(f.read())

# -----------------------------------------------------------------------------
# 6. WRITING STRUCTURED DATA
# -----------------------------------------------------------------------------

import json

data = {
    "name": "Alice",
    "scores": [90, 85, 92],
    "active": True
}

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["name"])     # Alice
print(loaded["scores"])   # [90, 85, 92]

# -----------------------------------------------------------------------------
# 7. ATOMIC / SAFE WRITE PATTERN
# -----------------------------------------------------------------------------
# Write to a temp file first, then rename — prevents partial writes
# from corrupting the real file if the process crashes mid-write.

import tempfile, shutil

def safe_write(path, content):
    dir_  = os.path.dirname(os.path.abspath(path))
    tmp   = tempfile.NamedTemporaryFile("w", dir=dir_,
                                        delete=False, encoding="utf-8")
    try:
        tmp.write(content)
        tmp.flush()
        tmp.close()
        shutil.move(tmp.name, path)   # atomic rename
    except Exception:
        os.unlink(tmp.name)
        raise

safe_write("safe_output.txt", "Safe content\n")
with open("safe_output.txt") as f:
    print(f.read())   # Safe content

# Cleanup
for fn in ["output.txt", "log.txt", "fruits.txt", "animals.txt",
           "new_only.txt", "data.json", "safe_output.txt"]:
    if os.path.exists(fn):
        os.remove(fn)

# =============================================================================
# SUMMARY
# =============================================================================
# ┌──────────────────┬──────────────────────────────────────────────────────┐
# │  Method/Mode     │  Key point                                           │
# ├──────────────────┼──────────────────────────────────────────────────────┤
# │  'w'             │  Create or OVERWRITE — existing content gone         │
# │  'a'             │  Append to end — safe for logs                       │
# │  'x'             │  Create only — raises FileExistsError if exists      │
# │  'r+'            │  Read + write without truncating                     │
# │  write(str)      │  Writes string, returns char count                   │
# │  writelines(it)  │  Writes each string — no auto newlines               │
# │  json.dump()     │  Write Python dict/list as JSON                      │
# │  Atomic write    │  Write to temp → rename (crash-safe)                 │
# └──────────────────┴──────────────────────────────────────────────────────┘
print("\nDay 02 — Writing Files complete!")
