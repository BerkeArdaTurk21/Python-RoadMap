# =============================================================================
# Week 07 - Day 03 | sys & argparse
# =============================================================================
# Two modules for building command-line programs:
#   - sys     : interpreter state — argv, exit codes, stdin/stdout, paths
#   - argparse: the standard way to build real CLI argument parsers

import sys

# -----------------------------------------------------------------------------
# 1. sys.argv — Raw Command-Line Arguments
# -----------------------------------------------------------------------------
# sys.argv is a list of strings passed to the script.
#   sys.argv[0] is always the script name/path.
#   sys.argv[1:] are the actual arguments.
#
# Run:  python lesson.py hello 42
#   -> sys.argv == ['lesson.py', 'hello', '42']

print(f"Script name:  {sys.argv[0]}")
print(f"Arguments:    {sys.argv[1:]}")
print(f"Arg count:    {len(sys.argv) - 1}")

# Note: every argument is a STRING. Convert manually if you need a number.
if len(sys.argv) > 2:
    try:
        n = int(sys.argv[2])
        print(f"Second arg as int + 1 = {n + 1}")
    except ValueError:
        print(f"'{sys.argv[2]}' is not an integer")

# -----------------------------------------------------------------------------
# 2. sys.exit() — Exit Codes
# -----------------------------------------------------------------------------
# sys.exit(0)  -> success (the default)
# sys.exit(1)  -> generic error
# sys.exit("message")  -> prints message to stderr, then exits with code 1
#
# Exit codes let other programs (shells, CI) know if your script succeeded.
#   echo $?      # Linux/Mac — shows last exit code
#   echo %ERRORLEVEL%   # Windows cmd

# Example (commented so this file runs top-to-bottom):
# if not sys.argv[1:]:
#     sys.exit("Error: no arguments given")

# -----------------------------------------------------------------------------
# 3. sys — Useful Attributes
# -----------------------------------------------------------------------------
print(f"\nPython version: {sys.version.split()[0]}")
print(f"Platform:       {sys.platform}")        # 'win32', 'linux', 'darwin'
print(f"Executable:     {sys.executable}")      # path to the python interpreter
print(f"Max int digits: {sys.maxsize}")         # largest 'small' int / index

# sys.path — where Python looks for modules (import search path)
print(f"sys.path[0]:    {sys.path[0]!r}")       # usually the script's directory

# -----------------------------------------------------------------------------
# 4. sys.stdin / stdout / stderr
# -----------------------------------------------------------------------------
# Three standard streams. print() writes to stdout by default.
print("This goes to stdout")
print("This goes to stderr", file=sys.stderr)

# Reading piped input:  echo "data" | python lesson.py
# for line in sys.stdin:
#     print(line.strip().upper())

# =============================================================================
# argparse — The Right Way to Build a CLI
# =============================================================================
# Parsing sys.argv by hand gets painful fast (flags, defaults, types, help).
# argparse handles all of that: --help, validation, error messages, exit codes.

import argparse

# -----------------------------------------------------------------------------
# 5. A Minimal Parser
# -----------------------------------------------------------------------------
parser = argparse.ArgumentParser(
    prog="greet",
    description="Greet a user a number of times.",
    epilog="Example: python greet.py Alice -n 3 --upper",
)

# Positional argument — required, order matters
parser.add_argument("name", help="who to greet")

# Optional argument with a type and default
parser.add_argument(
    "-n", "--times",
    type=int,
    default=1,
    help="how many times to greet (default: 1)",
)

# Flag (store_true) — present = True, absent = False
parser.add_argument(
    "--upper",
    action="store_true",
    help="shout the greeting in uppercase",
)

# choices — restrict allowed values
parser.add_argument(
    "--lang",
    choices=["en", "tr", "es"],
    default="en",
    help="greeting language",
)

# --version — built-in action
parser.add_argument("--version", action="version", version="%(prog)s 1.0")

# -----------------------------------------------------------------------------
# 6. Parsing
# -----------------------------------------------------------------------------
# parse_args() reads sys.argv by default. Here we pass an explicit list so the
# lesson runs without real CLI input. In a real script you'd just call
# parser.parse_args() with no arguments.
demo_args = ["Berke", "-n", "2", "--upper", "--lang", "tr"]
args = parser.parse_args(demo_args)

print(f"\nParsed: name={args.name!r}, times={args.times}, "
      f"upper={args.upper}, lang={args.lang}")

greetings = {"en": "Hello", "tr": "Merhaba", "es": "Hola"}
message = f"{greetings[args.lang]}, {args.name}!"
if args.upper:
    message = message.upper()

for _ in range(args.times):
    print(message)

# -----------------------------------------------------------------------------
# 7. Subcommands — argparse Subparsers
# -----------------------------------------------------------------------------
# Tools like git have subcommands: git add, git commit, git push.
# Subparsers let one program expose several commands, each with its own args.

tool = argparse.ArgumentParser(prog="taskman", description="Tiny task tool")
sub = tool.add_subparsers(dest="command", required=True)

add_p = sub.add_parser("add", help="add a task")
add_p.add_argument("title")
add_p.add_argument("--priority", choices=["low", "high"], default="low")

list_p = sub.add_parser("list", help="list tasks")
list_p.add_argument("--all", action="store_true")

# Dispatch on the chosen subcommand
parsed = tool.parse_args(["add", "Write lesson", "--priority", "high"])
print(f"\nSubcommand: {parsed.command}")
if parsed.command == "add":
    print(f"  Adding task '{parsed.title}' (priority={parsed.priority})")
elif parsed.command == "list":
    print(f"  Listing tasks (all={parsed.all})")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
# sys.argv            — raw argument list (all strings, argv[0] = script)
# sys.exit(code)      — exit with a status code (0 = success)
# sys.path            — module import search path
# sys.stdin/out/err   — standard streams
# argparse            — build real CLIs: positionals, options, flags, choices
# add_argument()      — define each argument (type, default, action, help)
# parse_args()        — returns a Namespace of parsed values
# add_subparsers()    — git-style subcommands
# --help / --version  — provided automatically
