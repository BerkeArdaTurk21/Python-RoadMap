"""
================================================
Week 1 | Day 6 — Print & Formatting
================================================
Level       : Beginner
Topics      : print() parameters, f-strings advanced,
              format(), % formatting, number formatting,
              string alignment, print tricks
Goal        : Control exactly how output looks —
              aligned tables, formatted numbers,
              and clean terminal output
================================================
"""


# ── SECTION 1: print() Parameters ────────────────────
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#
#   sep   — string placed BETWEEN each object (default: one space)
#   end   — string placed AFTER the last object (default: newline)
#   file  — where to write output (default: terminal)
#   flush — force-flush the output buffer immediately

print("apple", "banana", "cherry")             # apple banana cherry
print("apple", "banana", "cherry", sep=", ")   # apple, banana, cherry
print("apple", "banana", "cherry", sep=" | ")  # apple | banana | cherry
print("apple", "banana", "cherry", sep="")     # applebananacherry
print("apple", "banana", "cherry", sep="\n")   # each on its own line

# end — default is \n; change it to stay on the same line
print("Loading", end="")
print("...", end="")
print(" Done!")             # Loading... Done!

# Combining sep and end
print("X", "Y", "Z", sep="-", end=" ✅\n")    # X-Y-Z ✅

# Printing nothing (blank line)
print()                     # empty line
print("", "")               # two spaces (two empty strings with default sep)


# ── SECTION 2: f-strings Review ──────────────────────
# f-strings (formatted string literals) embed expressions directly.
# Syntax: f"text {expression} text"

name  = "Berke"
score = 95
pi    = 3.14159

print(f"Hello, {name}!")            # Hello, Berke!
print(f"Score: {score}")            # Score: 95
print(f"2 + 2 = {2 + 2}")          # 2 + 2 = 4
print(f"Pi rounded: {round(pi, 2)}")# Pi rounded: 3.14

# Expressions inside braces
items = ["pen", "book", "ruler"]
print(f"First item: {items[0]}")    # First item: pen
print(f"Item count: {len(items)}")  # Item count: 3


# ── SECTION 3: f-string Format Specs ─────────────────
# Full spec: {value:[fill][align][sign][#][0][width][grouping][.precision][type]}
#
#   fill    — any character used to pad (used with align)
#   align   — <  left   >  right   ^  center   =  padding after sign
#   sign    — +  always show sign   -  only negative   space  space for positive
#   #       — alternate form: 0b / 0o / 0x prefix
#   0       — zero-pad (shorthand for fill=0, align==)
#   width   — minimum total field width
#   grouping— , or _ as thousands separator
#   precision — decimal places for floats; max chars for strings
#   type    — d int  f float  e scientific  % percent  s str  b binary  x hex  o octal

# ── Alignment ──
print(f"{'left':<10}|")        # left      |   (left-align in 10 chars)
print(f"{'right':>10}|")       #      right|   (right-align)
print(f"{'center':^10}|")      #   center  |   (centered)
print(f"{'fill':*^10}|")       # **fill****|   (centered, filled with *)

# ── Width & precision ──
print(f"{pi:10.3f}")           #      3.142   (width 10, 3 decimal places)
print(f"{pi:.2f}")             # 3.14          (2 decimal places, no width)
print(f"{'hello':.3s}")        # hel            (max 3 chars from string)

# ── Sign ──
print(f"{42:+d}")              # +42   (always show sign)
print(f"{-42:+d}")             # -42
print(f"{42: d}")              #  42   (space for positive)

# ── Zero padding ──
print(f"{42:06d}")             # 000042
print(f"{3.14:08.2f}")        # 00003.14

# ── Number types ──
n = 255
print(f"{n:d}")                # 255      (decimal int — default)
print(f"{n:b}")                # 11111111 (binary)
print(f"{n:o}")                # 377      (octal)
print(f"{n:x}")                # ff       (hex lowercase)
print(f"{n:X}")                # FF       (hex uppercase)
print(f"{n:#b}")               # 0b11111111 (with prefix)
print(f"{n:#x}")               # 0xff


# ── SECTION 4: format() Method ───────────────────────
# "template".format(*args, **kwargs)
# Same format spec syntax as f-strings.
# Useful when building template strings dynamically.

# Positional
print("{} + {} = {}".format(1, 2, 3))          # 1 + 2 = 3
print("{0} and {1} and {0}".format("A", "B"))  # A and B and A

# Keyword
print("{name} scored {pts} points".format(name="Berke", pts=95))

# Format spec inside format()
print("{:.2f}".format(3.14159))     # 3.14
print("{:>10}".format("hi"))        #         hi
print("{:,}".format(1234567))       # 1,234,567

# Storing a template
template = "Product: {item:<15} Price: ${price:>8.2f}"
print(template.format(item="Laptop", price=999.9))
print(template.format(item="Mouse",  price=29.99))


# ── SECTION 5: % Formatting (Legacy) ─────────────────
# Older style still found in many codebases.
# "template" % (values,)
#
#   %s  string     %d  int     %f  float
#   %e  scientific %x  hex     %o  octal
#   %r  repr

name = "Berke"
age  = 25
gpa  = 3.87

print("Name: %s" % name)               # Name: Berke
print("Age: %d" % age)                 # Age: 25
print("GPA: %.2f" % gpa)              # GPA: 3.87
print("%s is %d years old." % (name, age))  # Berke is 25 years old.

# Width and alignment with %
print("%10s" % "right")               #      right
print("%-10s|" % "left")              # left      |
print("%08.2f" % 3.14)                # 00003.14

# NOTE: f-strings are preferred in modern Python (cleaner, faster, more powerful).


# ── SECTION 6: Number Formatting ─────────────────────
# Thousands separator
big = 1_234_567_890
print(f"{big:,}")           # 1,234,567,890  (comma separator)
print(f"{big:_}")           # 1_234_567_890  (underscore separator)

# Percentage
ratio = 0.8735
print(f"{ratio:.1%}")       # 87.4%  (multiplies by 100, adds %)
print(f"{ratio:.2%}")       # 87.35%

# Scientific notation
tiny = 0.000001234
large = 9_870_000.0
print(f"{tiny:e}")          # 1.234000e-06
print(f"{tiny:.2e}")        # 1.23e-06
print(f"{large:.3E}")       # 9.870E+06

# Currency style
price = 1234.5
print(f"${price:,.2f}")     # $1,234.50

# Binary / hex — useful for low-level work
byte = 0b10110011
print(f"decimal : {byte:d}")
print(f"binary  : {byte:08b}")
print(f"hex     : {byte:02x}")
print(f"octal   : {byte:o}")


# ── SECTION 7: String Alignment ──────────────────────
# str methods: ljust(width, fillchar) / rjust / center / zfill(width)

word = "Python"
print(word.ljust(12))           # Python        (padded right with spaces)
print(word.ljust(12, "-"))      # Python------
print(word.rjust(12))           #       Python
print(word.rjust(12, "."))      # ......Python
print(word.center(12))          #    Python
print(word.center(12, "="))     # ===Python===
print("42".zfill(6))            # 000042   (zero-fill from left)
print("-7".zfill(6))            # -00007   (sign stays at front)

# Building an aligned table with f-strings (cleaner than str methods)
print()
print(f"{'Name':<12} {'Score':>6} {'Grade':^8}")
print("-" * 28)
data = [("Alice", 95, "A"), ("Bob", 72, "C"), ("Charlie", 88, "B")]
for name, sc, grade in data:
    print(f"{name:<12} {sc:>6} {grade:^8}")


# ── SECTION 8: Print Tricks ───────────────────────────
# Rewriting the same line with \r (carriage return — moves cursor to line start)
import time

# Simulated countdown (without actual sleep for lesson purposes)
for i in range(5, 0, -1):
    print(f"\rCountdown: {i} ", end="", flush=True)
print("\rCountdown: Done! ")

# Printing a separator line
WIDTH = 50
print("=" * WIDTH)
print(f"{'REPORT':^{WIDTH}}")
print("=" * WIDTH)

# Multiple values on one line then move to next
print("Name:", end=" ")
print("Berke", end=" | ")
print("Score:", end=" ")
print(95)

# Printing a simple box around text
def print_box(text):
    border = "+" + "-" * (len(text) + 2) + "+"
    print(border)
    print(f"| {text} |")
    print(border)

print_box("Hello, Python!")
print_box("Week 1 — Day 6")


# ── QUICK REFERENCE ──────────────────────────────────
# print()
#   sep=" "   — separator between items
#   end="\n"  — suffix after all items
#
# f-string format spec: {value:[fill][align][sign][0][width][,][.prec][type]}
#   align:  <  left   >  right   ^  center
#   types:  d  int   f  float   e  sci   %  percent   b  bin   x  hex   s  str
#   {n:,}        → thousands comma          {n:.2f}     → 2 decimal places
#   {n:.2%}      → percentage               {n:08.2f}   → zero-padded float
#   {s:<10}      → left-align in 10 chars   {s:*^10}    → center with * fill
#   {n:#x}       → 0xff (hex with prefix)   {n:#b}      → 0b... (binary prefix)
#
# format()   → same spec, useful for templates
# % style    → legacy, use f-strings in new code
#
# str alignment methods:
#   .ljust(w, c)  .rjust(w, c)  .center(w, c)  .zfill(w)
#
# Print tricks:
#   end=""    → stay on same line
#   end="\r"  → rewrite current line (progress bars)
#   flush=True → force output immediately
