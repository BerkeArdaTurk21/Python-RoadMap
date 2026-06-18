# =============================================================================
# Week 07 - Day 01 | Import System & venv — Solutions
# =============================================================================

# Solution 1
import math
print(f"Hypotenuse: {math.hypot(3, 4)}")
print(f"log10(1000): {math.log10(1000)}")
print(f"ceil(4.2)={math.ceil(4.2)}, floor(4.8)={math.floor(4.8)}")
print()

# Solution 2
import datetime as dt
import collections as col

today = dt.date.today()
print(f"Today: {today}")

C = col.Counter
counts = C("mississippi")
print(f"Letter counts: {counts}")

dd = col.defaultdict(list)
words = ["hi", "hello", "hey", "world"]
for w in words:
    dd[len(w)].append(w)
print(f"By length: {dict(dd)}")
print()

# Solution 3
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def main():
    print(f"3 + 4 = {add(3, 4)}")
    print(f"5 × 6 = {multiply(5, 6)}")

if __name__ == "__main__":
    main()
print()

# Solution 4
import sys
print(f"sys.path entries: {len(sys.path)}")
print(f"Current dir in path: {'' in sys.path}")
version = f"{sys.version_info.major}.{sys.version_info.minor}"
print(f"Python version: {version}")
print()

# Solution 5
import random
print(f"File: {random.__file__}")
print(f"Name: {random.__name__}")
public_names = [n for n in dir(random) if not n.startswith("_")][:5]
print(f"5 public names: {public_names}")
