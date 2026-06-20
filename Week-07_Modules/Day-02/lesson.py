# =============================================================================
# Week 07 - Day 02 | The os Module
# =============================================================================
# The os module provides a portable interface to operating system features:
# directory navigation, file operations, environment variables, and more.

import os

# -----------------------------------------------------------------------------
# 1. Current Directory
# -----------------------------------------------------------------------------
cwd = os.getcwd()
print(f"Current directory: {cwd}")

# os.chdir() changes the working directory (avoid in scripts — use paths instead)
# os.chdir("/tmp")

# -----------------------------------------------------------------------------
# 2. Directory Listing
# -----------------------------------------------------------------------------
# os.listdir() — returns a list of names in the directory
entries = os.listdir(".")           # current dir
print(f"\nEntries in '.': {entries[:3]}...")

# os.scandir() — returns DirEntry objects (faster, more info)
print("\nScandir entries:")
with os.scandir(".") as it:
    for entry in list(it)[:3]:
        kind = "DIR " if entry.is_dir() else "FILE"
        print(f"  {kind} {entry.name}")

# -----------------------------------------------------------------------------
# 3. Path Operations — os.path
# -----------------------------------------------------------------------------
# os.path is a sub-module for path manipulation
# (pathlib is the modern alternative, but os.path is everywhere in legacy code)

p = os.path.join("Week-07_Modules", "Day-02", "lesson.py")
print(f"\nos.path.join: {p}")

print(f"exists:  {os.path.exists('.')}")
print(f"isfile:  {os.path.isfile('lesson.py')}")
print(f"isdir:   {os.path.isdir('.')}")

# Split operations
full = "/home/user/projects/app/main.py"
print(f"\ndirname:   {os.path.dirname(full)}")   # /home/user/projects/app
print(f"basename:  {os.path.basename(full)}")  # main.py
print(f"splitext:  {os.path.splitext(full)}")  # ('/home/user/projects/app/main', '.py')
print(f"abspath:   {os.path.abspath('.')}")

# -----------------------------------------------------------------------------
# 4. Creating and Removing Directories
# -----------------------------------------------------------------------------
# os.mkdir()    — one level only (fails if parent missing)
# os.makedirs() — creates all intermediate directories

test_dir = os.path.join(os.getcwd(), "_test_dir", "sub")
os.makedirs(test_dir, exist_ok=True)     # exist_ok=True: no error if exists
print(f"\nCreated: {test_dir}")
print(f"Exists:  {os.path.exists(test_dir)}")

# Cleanup: os.rmdir() for empty dirs, os.removedirs() for empty tree
os.removedirs(test_dir)
print(f"Removed. Exists now: {os.path.exists(test_dir)}")

# -----------------------------------------------------------------------------
# 5. File Operations
# -----------------------------------------------------------------------------
# os.rename(src, dst)  — rename or move a file
# os.remove(path)      — delete a file
# os.replace(src, dst) — atomic rename (overwrites dst if exists)

temp_file = "_temp_test.txt"
with open(temp_file, "w") as f:
    f.write("hello")

renamed = "_temp_renamed.txt"
os.rename(temp_file, renamed)
print(f"\nRenamed: {renamed} exists = {os.path.exists(renamed)}")
os.remove(renamed)
print(f"Removed: {renamed} exists = {os.path.exists(renamed)}")

# -----------------------------------------------------------------------------
# 6. Environment Variables
# -----------------------------------------------------------------------------
# os.environ is a dict-like object of all environment variables
# os.getenv(key, default) is safer — returns None (or default) if key missing

path_var = os.getenv("PATH", "not set")
print(f"\nPATH (first 60 chars): {path_var[:60]}...")

home = os.getenv("HOME") or os.getenv("USERPROFILE", "unknown")
print(f"Home directory: {home}")

# Set a variable for this process only
os.environ["MY_APP_DEBUG"] = "true"
print(f"MY_APP_DEBUG: {os.getenv('MY_APP_DEBUG')}")

# -----------------------------------------------------------------------------
# 7. Walking a Directory Tree — os.walk()
# -----------------------------------------------------------------------------
# os.walk(top) yields (dirpath, dirnames, filenames) for every directory

print("\nos.walk demo (current dir, depth 1):")
for dirpath, dirnames, filenames in os.walk("."):
    # Skip hidden dirs
    dirnames[:] = [d for d in dirnames if not d.startswith(".")]
    depth = dirpath.count(os.sep)
    if depth > 1:
        break
    indent = "  " * depth
    print(f"{indent}{os.path.basename(dirpath)}/")
    for fname in filenames[:2]:
        print(f"{indent}  {fname}")

# -----------------------------------------------------------------------------
# 8. Platform Constants
# -----------------------------------------------------------------------------
print(f"\nos.name:   {os.name}")        # 'nt' (Windows) or 'posix' (Unix)
print(f"os.sep:    {repr(os.sep)}")     # '\\' or '/'
print(f"os.linesep:{repr(os.linesep)}") # '\r\n' or '\n'
print(f"os.curdir: {repr(os.curdir)}")  # '.'
print(f"os.pardir: {repr(os.pardir)}")  # '..'

# -----------------------------------------------------------------------------
# 9. Running System Commands (avoid when possible — use subprocess instead)
# -----------------------------------------------------------------------------
# os.system("echo hello")   # runs in shell, returns exit code
# Better: use subprocess module (Week 07 Day 03 covers this)

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
# os.getcwd() / os.chdir()     — current dir navigation
# os.listdir() / os.scandir()  — list directory contents
# os.path.*                    — path join, split, exists checks
# os.makedirs() / os.removedirs() — create/remove directory trees
# os.rename() / os.remove()    — file operations
# os.environ / os.getenv()     — environment variables
# os.walk()                    — recursive directory traversal
# os.name / os.sep / os.linesep — platform info
