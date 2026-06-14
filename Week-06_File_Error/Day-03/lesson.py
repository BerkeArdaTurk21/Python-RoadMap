# =============================================================================
# Week 06 - Day 03 | Working with Paths
# =============================================================================
# Topics: os module basics, os.path, pathlib.Path, directory operations,
#         globbing, cross-platform path handling
# =============================================================================

import os
from pathlib import Path

# -----------------------------------------------------------------------------
# 1. os MODULE BASICS
# -----------------------------------------------------------------------------

print("── os basics ──")
print(os.getcwd())                    # current working directory
print(os.listdir("."))                # list files/dirs in current dir (first 3)
print(os.path.abspath("lesson.py"))  # absolute path of a file

# Environment variable
home = os.environ.get("HOME") or os.environ.get("USERPROFILE", "N/A")
print(f"Home: {home}")

# -----------------------------------------------------------------------------
# 2. os.path — STRING-BASED PATH OPERATIONS
# -----------------------------------------------------------------------------

print("\n── os.path ──")
p = "/Users/alice/projects/app/main.py"

print(os.path.basename(p))      # main.py        — filename only
print(os.path.dirname(p))       # /Users/alice/projects/app — parent dir
print(os.path.splitext(p))      # ('/Users/alice/projects/app/main', '.py')
print(os.path.split(p))         # ('/Users/alice/projects/app', 'main.py')

# Join paths correctly (handles / on Linux, \ on Windows)
joined = os.path.join("data", "2024", "report.csv")
print(joined)                   # data/2024/report.csv  (or data\2024\report.csv)

# Check existence
print(os.path.exists("lesson.py"))   # True if this file is here
print(os.path.isfile("lesson.py"))   # True if it's a file
print(os.path.isdir("."))            # True if it's a directory

# File size
if os.path.exists("lesson.py"):
    print(os.path.getsize("lesson.py"), "bytes")

# -----------------------------------------------------------------------------
# 3. pathlib.Path — OBJECT-ORIENTED PATHS (MODERN PYTHON)
# -----------------------------------------------------------------------------
# pathlib is the modern, preferred approach.
# Path objects overload / for joining — much more readable than os.path.join().

print("\n── pathlib ──")

p = Path(".")                           # current directory
print(p.resolve())                      # absolute path

# Path / operator for joining
data_dir = Path("data") / "2024" / "report.csv"
print(data_dir)                         # data/2024/report.csv

# From a full path
full = Path("/Users/alice/projects/app/main.py")
print(full.name)        # main.py
print(full.stem)        # main
print(full.suffix)      # .py
print(full.parent)      # /Users/alice/projects/app
print(full.parts)       # ('/', 'Users', 'alice', 'projects', 'app', 'main.py')

# -----------------------------------------------------------------------------
# 4. CHECKING AND QUERYING PATHS
# -----------------------------------------------------------------------------

cwd = Path(".")
print("\n── path checks ──")
print(cwd.exists())      # True
print(cwd.is_dir())      # True
print(cwd.is_file())     # False

lesson = Path("lesson.py")
if lesson.exists():
    print(lesson.stat().st_size, "bytes")   # file size

# -----------------------------------------------------------------------------
# 5. DIRECTORY OPERATIONS
# -----------------------------------------------------------------------------

# Create directories
tmp = Path("tmp_demo")
tmp.mkdir(exist_ok=True)           # creates; no error if already exists
(tmp / "sub").mkdir(exist_ok=True) # nested dir

# Write and read via Path
(tmp / "hello.txt").write_text("Hello from pathlib!\n", encoding="utf-8")
content = (tmp / "hello.txt").read_text(encoding="utf-8")
print(content.strip())             # Hello from pathlib!

# List directory contents
print("\n── tmp_demo contents ──")
for item in tmp.iterdir():
    kind = "dir" if item.is_dir() else "file"
    print(f"  {item.name} ({kind})")

# -----------------------------------------------------------------------------
# 6. GLOBBING — FIND FILES BY PATTERN
# -----------------------------------------------------------------------------

print("\n── glob ──")
# Create some files to glob
for name in ["a.py", "b.py", "c.txt"]:
    (tmp / name).write_text("x")

for f in sorted(tmp.glob("*.py")):   # all .py files in tmp
    print(f"  {f.name}")

for f in sorted(Path(".").rglob("*.py")):  # recursive: all .py in tree
    if not str(f).startswith("tmp"):
        print(f"  {f}")
        break   # just show one

# -----------------------------------------------------------------------------
# 7. RENAMING AND DELETING
# -----------------------------------------------------------------------------

(tmp / "hello.txt").rename(tmp / "greeting.txt")   # rename
(tmp / "greeting.txt").unlink()                     # delete file

# Remove directory tree
import shutil
shutil.rmtree(tmp)   # deletes the whole tmp_demo folder

print("\n── tmp_demo removed ──")

# =============================================================================
# SUMMARY
# =============================================================================
# ┌─────────────────────────┬──────────────────────────────────────────────┐
# │  Tool                   │  Key operations                              │
# ├─────────────────────────┼──────────────────────────────────────────────┤
# │  os.path.join()         │  Cross-platform path joining (old style)     │
# │  os.path.exists/isfile  │  Check existence/type                        │
# │  Path("x") / "y"        │  Modern path joining with /                  │
# │  path.name / .stem      │  Filename / filename without extension        │
# │  path.suffix            │  Extension including dot: '.py'              │
# │  path.mkdir()           │  Create directory (exist_ok=True is safe)    │
# │  path.glob("*.py")      │  Find files matching pattern                 │
# │  path.rglob("*.py")     │  Recursive glob                              │
# │  path.unlink()          │  Delete a file                               │
# │  shutil.rmtree(path)    │  Delete a whole directory tree               │
# └─────────────────────────┴──────────────────────────────────────────────┘
print("\nDay 03 — Working with Paths complete!")
