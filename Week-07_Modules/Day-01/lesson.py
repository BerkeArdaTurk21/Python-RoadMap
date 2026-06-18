# =============================================================================
# Week 07 - Day 01 | Import System & venv
# =============================================================================
# Topics: import, from...import, as, __name__, __main__,
#         module search path, venv, pip, requirements.txt
# =============================================================================

# -----------------------------------------------------------------------------
# 1. IMPORT BASICS
# -----------------------------------------------------------------------------
# Python finds modules by searching sys.path in order:
#   1. The directory of the current script
#   2. PYTHONPATH environment variable dirs
#   3. Standard library dirs
#   4. site-packages (installed packages)

import math                        # import the whole module
print(math.sqrt(16))               # 4.0 — access with dot notation
print(math.pi)                     # 3.141592...

import os, sys                     # multiple imports on one line (ok for stdlib)

# -----------------------------------------------------------------------------
# 2. from ... import
# -----------------------------------------------------------------------------
from math import sqrt, pi          # import specific names into current namespace
print(sqrt(25))                    # 5.0 — no "math." prefix needed
print(pi)

from math import factorial as fac  # rename with 'as'
print(fac(5))                      # 120

# Wildcard import (generally avoid — pollutes namespace, hides origin)
# from math import *   ← don't do this in real code

# -----------------------------------------------------------------------------
# 3. import ... as — ALIASING
# -----------------------------------------------------------------------------
import datetime as dt               # common alias
today = dt.date.today()
print(today)                        # 2026-06-19

import collections as col
counter = col.Counter("aabbbc")
print(counter)                      # Counter({'b': 3, 'a': 2, 'c': 1})

# -----------------------------------------------------------------------------
# 4. __name__ AND __main__
# -----------------------------------------------------------------------------
# Every module has a __name__ attribute.
# When run directly:      __name__ == "__main__"
# When imported by other: __name__ == the module's filename (without .py)
#
# The if __name__ == "__main__": guard lets a file be:
#   - run as a script (executes the guarded block)
#   - imported as a module (skipped the guarded block)

print(f"\n__name__ = {__name__!r}")    # '__main__' when run directly

# Pattern every Python module should follow:
def greet(name):
    return f"Hello, {name}!"

def main():
    print(greet("World"))

if __name__ == "__main__":
    main()    # only runs when this file is the entry point, not on import

# -----------------------------------------------------------------------------
# 5. MODULE SEARCH PATH
# -----------------------------------------------------------------------------
import sys
print("\nModule search path (first 3 entries):")
for p in sys.path[:3]:
    print(f"  {p}")

# You can add to the path at runtime (rarely needed):
# sys.path.insert(0, "/my/custom/lib")

# Where is a module loaded from?
import json
print(f"\njson module: {json.__file__}")

# -----------------------------------------------------------------------------
# 6. VIRTUAL ENVIRONMENTS (venv)
# -----------------------------------------------------------------------------
# A venv is an isolated Python environment with its own site-packages.
# This prevents version conflicts between projects.
#
# ─── Create & activate ──────────────────────────────────────────────────────
#
#   python -m venv .venv          ← create (once per project)
#
#   # Windows PowerShell:
#   .venv\Scripts\Activate.ps1
#
#   # macOS / Linux:
#   source .venv/bin/activate
#
#   # Deactivate:
#   deactivate
#
# ─── Install packages ────────────────────────────────────────────────────────
#
#   pip install requests          ← install a package
#   pip install requests==2.31.0  ← pin a specific version
#   pip list                      ← show installed packages
#   pip show requests             ← info about one package
#   pip uninstall requests        ← remove
#
# ─── requirements.txt ────────────────────────────────────────────────────────
#
#   pip freeze > requirements.txt     ← snapshot current environment
#   pip install -r requirements.txt   ← recreate environment from file
#
# Example requirements.txt:
#   requests==2.31.0
#   pytest==8.1.0
#   jupyter==1.0.0

# Check current Python executable (will show venv path when active)
print(f"\nPython executable: {sys.executable}")
print(f"Python version:    {sys.version.split()[0]}")

# -----------------------------------------------------------------------------
# 7. CREATING YOUR OWN MODULE
# -----------------------------------------------------------------------------
# Any .py file is a module. If you have:
#
#   myproject/
#     utils.py       ← your module
#     main.py        ← your script
#
# In main.py:
#   import utils
#   from utils import some_function
#
# A folder with __init__.py is a PACKAGE:
#
#   myproject/
#     mypackage/
#       __init__.py     ← makes the folder a package
#       helpers.py
#     main.py
#
# In main.py:
#   from mypackage import helpers
#   from mypackage.helpers import my_func

# Demonstrate __all__ — controls what "from module import *" exposes
# (defined in the module, not used here, just shown for reference)
# __all__ = ["greet", "main"]   # only these names are exported

# =============================================================================
# SUMMARY
# =============================================================================
# ┌────────────────────────────┬──────────────────────────────────────────────┐
# │  Syntax                    │  What it does                                │
# ├────────────────────────────┼──────────────────────────────────────────────┤
# │  import math               │  Import whole module; use math.sqrt()        │
# │  from math import sqrt     │  Import one name; use sqrt()                 │
# │  from math import sqrt, pi │  Import multiple names                       │
# │  import math as m          │  Alias the module; use m.sqrt()              │
# │  from math import sqrt as s│  Alias the name; use s()                     │
# │  if __name__ == "__main__" │  Guard: only run when script is entry point  │
# │  python -m venv .venv      │  Create a virtual environment                │
# │  pip freeze > req.txt      │  Snapshot dependencies                       │
# └────────────────────────────┴──────────────────────────────────────────────┘
print("\nDay 01 — Import System & venv complete!")
