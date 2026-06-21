# =============================================================================
# Week 07 - Day 03 | sys & argparse — Solutions
# =============================================================================

import os
import sys
import argparse

# Solution 1
print(f"Script: {os.path.basename(sys.argv[0])}")
print(f"Count:  {len(sys.argv) - 1}")
for i, arg in enumerate(sys.argv[1:], 1):
    print(f"{i}: {arg}")
print()


# Solution 2
def sum_args(values):
    total = 0
    for v in values:
        try:
            total += int(v)
        except ValueError:
            print(f"Error: '{v}' is not an integer", file=sys.stderr)
            sys.exit(1)
    return total

# Using a fixed demo list so the file runs without real CLI input.
demo_numbers = ["10", "20", "30"]
print(f"Sum: {sum_args(demo_numbers)}")
print()


# Solution 3
calc = argparse.ArgumentParser(prog="calc", description="Tiny calculator")
calc.add_argument("a", type=float)
calc.add_argument("b", type=float)
calc.add_argument("--op", choices=["add", "sub", "mul", "div"], default="add")
calc.add_argument("--round", action="store_true")

demo = ["12", "5", "--op", "mul"]
args = calc.parse_args(demo)

if args.op == "add":
    result = args.a + args.b
elif args.op == "sub":
    result = args.a - args.b
elif args.op == "mul":
    result = args.a * args.b
else:  # div
    if args.b == 0:
        print("Error: division by zero")
        result = None
    else:
        result = args.a / args.b

if result is not None:
    if args.round:
        result = round(result)
    print(f"Result: {result}")
print()


# Solution 4
info = argparse.ArgumentParser(prog="fileinfo")
info.add_argument("path")
info.add_argument("--lines", action="store_true")
info.add_argument("-v", "--verbose", action="store_true")

demo = [__file__, "--lines", "-v"]
args = info.parse_args(demo)

print(f"Path:   {args.path}")
exists = os.path.exists(args.path)
print(f"Exists: {exists}")
if exists:
    print(f"Size:   {os.path.getsize(args.path)} bytes")
    if args.lines:
        with open(args.path, encoding="utf-8") as f:
            count = sum(1 for _ in f)
        print(f"Lines:  {count}")
if args.verbose:
    print(f"[verbose] Absolute path: {os.path.abspath(args.path)}")
print()


# Solution 5
note = argparse.ArgumentParser(prog="note")
sub = note.add_subparsers(dest="command", required=True)

add_p = sub.add_parser("add")
add_p.add_argument("text")
add_p.add_argument("--tag", default="general")

list_p = sub.add_parser("list")
list_p.add_argument("--count", action="store_true")

del_p = sub.add_parser("del")
del_p.add_argument("index", type=int)

demos = [
    ["add", "Buy milk", "--tag", "shopping"],
    ["list", "--count"],
    ["del", "3"],
]

for d in demos:
    args = note.parse_args(d)
    if args.command == "add":
        print(f"Added note '{args.text}' [{args.tag}]")
    elif args.command == "list":
        mode = "count mode" if args.count else "normal mode"
        print(f"Listing notes ({mode})")
    elif args.command == "del":
        print(f"Deleting note #{args.index}")
