# =============================================================================
# Week 07 - Day 02 | The os Module — Solutions
# =============================================================================

import os

# Solution 1
cwd = os.getcwd()
print(f"Full path:   {cwd}")
print(f"Folder name: {os.path.basename(cwd)}")
print(f"Parent:      {os.path.dirname(cwd)}")
print(f"Items:       {len(os.listdir(cwd))}")
print()

# Solution 2
a = os.path.join("projects", "myapp", "src", "main.py")
b = os.path.join(os.getcwd(), "output", "report.txt")
c = os.path.abspath(os.path.join(os.getcwd(), "..", "README.md"))
print(a)
print(b)
print(c)
print(f"Exists: {os.path.exists(c)}")
print()

# Solution 3
base = os.path.join(os.getcwd(), "sandbox")
for sub in ("data", "logs", "output"):
    path = os.path.join(base, sub)
    os.makedirs(path, exist_ok=True)
    print(f"Created: {path}")
    print(f"  isdir: {os.path.isdir(path)}")
for sub in ("output", "logs", "data"):
    os.rmdir(os.path.join(base, sub))
os.rmdir(base)
print("Cleaned up.")
print()

# Solution 4
path_val = os.getenv("PATH", "not set")
print(f"PATH: {path_val[:80]}...")
home = os.getenv("HOME") or os.getenv("USERPROFILE", "unknown")
print(f"Home: {home}")
venv = os.getenv("VIRTUAL_ENV")
if venv:
    print(f"venv active: {venv}")
else:
    print("No venv active")
os.environ["APP_VERSION"] = "1.0.0"
print(f"APP_VERSION = {os.getenv('APP_VERSION')}")
print()

# Solution 5
parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
py_files = []
ipynb_files = []

for dirpath, dirnames, filenames in os.walk(parent):
    dirnames[:] = [d for d in dirnames if not d.startswith(".")]
    for fname in filenames:
        full = os.path.join(dirpath, fname)
        if fname.endswith(".py"):
            py_files.append(full)
        elif fname.endswith(".ipynb"):
            ipynb_files.append(full)

print(f".py files found:    {len(py_files)}")
print(f".ipynb files found: {len(ipynb_files)}")

if py_files:
    largest = max(py_files, key=os.path.getsize)
    print(f"Largest .py file:   {os.path.basename(largest)} ({os.path.getsize(largest)} bytes)")
