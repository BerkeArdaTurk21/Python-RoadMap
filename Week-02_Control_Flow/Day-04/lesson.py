# Week 2 - Day 4: break / continue / pass
# Topic: Loop control statements

# ─────────────────────────────────────────────
# 1. break — EXIT THE LOOP IMMEDIATELY
# ─────────────────────────────────────────────
# break stops the loop entirely, regardless of the condition.
# Execution jumps to the first line AFTER the loop.

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")       # 0 1 2 3 4
print()
print("Loop exited at i =", 5)

# break in a while loop
count = 0
while True:
    if count == 3:
        break
    print(count, end=" ")   # 0 1 2
    count += 1
print()


# ─────────────────────────────────────────────
# 2. continue — SKIP THE CURRENT ITERATION
# ─────────────────────────────────────────────
# continue skips the rest of the current iteration body
# and jumps back to the loop condition check.

for i in range(8):
    if i % 2 == 0:
        continue            # skip even numbers
    print(i, end=" ")       # 1 3 5 7
print()

# continue in a while loop
n = 0
while n < 10:
    n += 1
    if n % 3 == 0:
        continue            # skip multiples of 3
    print(n, end=" ")       # 1 2 4 5 7 8 10
print()


# ─────────────────────────────────────────────
# 3. pass — DO NOTHING (PLACEHOLDER)
# ─────────────────────────────────────────────
# pass is a no-op. Python requires at least one statement
# in a block — pass satisfies that requirement silently.
# Common uses: empty loops, empty functions, empty classes,
# placeholder branches you'll fill in later.

for i in range(5):
    pass                    # loop runs but does nothing visible

# Placeholder if branch
x = 10
if x > 100:
    pass                    # TODO: handle large values
else:
    print(f"x = {x}")

# Empty function skeleton
def future_feature():
    pass                    # to be implemented later

# Empty class skeleton
class MyModel:
    pass


# ─────────────────────────────────────────────
# 4. break vs continue — SIDE BY SIDE
# ─────────────────────────────────────────────

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# break — stop at first number > 6
print("break example:")
for n in numbers:
    if n > 6:
        break
    print(n, end=" ")       # 1 2 3 4 5 6
print()

# continue — skip numbers > 6
print("continue example:")
for n in numbers:
    if n > 6:
        continue
    print(n, end=" ")       # 1 2 3 4 5 6
print()
# Both print the same output here, but the difference is:
# break STOPS the loop; continue SKIPS one item and keeps going.

numbers2 = [1, 8, 2, 9, 3]
print("break with mixed list:")
for n in numbers2:
    if n > 6:
        break
    print(n, end=" ")       # 1  → stops at 8
print()

print("continue with mixed list:")
for n in numbers2:
    if n > 6:
        continue
    print(n, end=" ")       # 1 2 3  → skips 8 and 9
print()


# ─────────────────────────────────────────────
# 5. break IN NESTED LOOPS
# ─────────────────────────────────────────────
# break only exits the INNERMOST loop it's in.

for i in range(3):
    for j in range(3):
        if j == 1:
            break           # exits inner loop only
        print(f"({i},{j})", end=" ")
    print()
# (0,0) ← inner breaks at j=1
# (1,0)
# (2,0)

# To break out of both loops, use a flag variable:
found = False
for i in range(5):
    for j in range(5):
        if i * j == 6:
            found = True
            break
    if found:
        break

print(f"Found i={i}, j={j} where i*j=6")   # i=2, j=3


# ─────────────────────────────────────────────
# 6. continue IN NESTED LOOPS
# ─────────────────────────────────────────────
# continue also affects only the innermost loop.

for i in range(1, 4):
    for j in range(1, 4):
        if i == j:
            continue        # skip diagonal
        print(f"({i},{j})", end=" ")
    print()
# (1,2) (1,3)
# (2,1) (2,3)
# (3,1) (3,2)


# ─────────────────────────────────────────────
# 7. for / else AND while / else WITH break
# ─────────────────────────────────────────────
# else runs ONLY if the loop was NOT exited via break.
# This is the most useful pattern for search operations.

# Search pattern — did we find it?
def find_prime(numbers):
    for n in numbers:
        for divisor in range(2, n):
            if n % divisor == 0:
                break       # n is not prime
        else:
            print(f"{n} is prime")  # only runs if inner loop finished normally

find_prime([7, 8, 11, 12, 13])
# 7 is prime
# 11 is prime
# 13 is prime


# ─────────────────────────────────────────────
# 8. PRACTICAL PATTERNS
# ─────────────────────────────────────────────

# Pattern 1 — Search and stop (break)
items = ["apple", "grape", "mango", "banana", "kiwi"]
target = "mango"

for i, item in enumerate(items):
    if item == target:
        print(f"Found '{target}' at index {i}")
        break
else:
    print(f"'{target}' not found")
# Found 'mango' at index 2

# Pattern 2 — Filter (continue)
data = [15, -3, 42, -7, 0, 8, -1, 99]
print("Positive numbers only:")
for val in data:
    if val <= 0:
        continue
    print(val, end=" ")     # 15 42 8 99
print()

# Pattern 3 — pass as a stub while building logic
commands = ["start", "pause", "unknown", "stop"]
for cmd in commands:
    if cmd == "start":
        print("Starting...")
    elif cmd == "pause":
        print("Pausing...")
    elif cmd == "stop":
        print("Stopping...")
        break
    else:
        pass                # unknown commands silently ignored for now


# ─────────────────────────────────────────────
# 9. PRACTICAL EXAMPLE — Text Processor
# ─────────────────────────────────────────────

def process_lines(lines):
    results = []
    for line in lines:
        line = line.strip()

        if not line:
            continue                # skip blank lines

        if line.startswith("#"):
            continue                # skip comment lines

        if line == "STOP":
            break                   # stop processing entirely

        results.append(line.upper())

    return results

sample = [
    "# Header comment",
    "",
    "hello world",
    "  python is great  ",
    "# another comment",
    "loop control",
    "STOP",
    "this line is never reached",
]

output = process_lines(sample)
for line in output:
    print(line)
# HELLO WORLD
# PYTHON IS GREAT
# LOOP CONTROL
