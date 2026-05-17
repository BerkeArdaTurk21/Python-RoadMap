# Week 2 - Day 3: while Loops
# Topic: Condition loops, infinite loop prevention, input validation loops

# ─────────────────────────────────────────────
# 1. BASIC while LOOP
# ─────────────────────────────────────────────
# Syntax:
#   while condition:
#       <block runs as long as condition is True>
#
# The condition is checked BEFORE each iteration.
# When it becomes False, the loop exits.

count = 0
while count < 5:
    print(count, end=" ")   # 0 1 2 3 4
    count += 1              # CRITICAL: update the variable or loop runs forever
print()

# Countdown
n = 5
while n > 0:
    print(n, end=" ")       # 5 4 3 2 1
    n -= 1
print("Go!")


# ─────────────────────────────────────────────
# 2. while vs for — WHEN TO USE WHICH
# ─────────────────────────────────────────────
# Use for  → when you know the number of iterations in advance
# Use while → when you loop until a condition changes (unknown count)

# for loop — fixed iterations
for i in range(5):
    print(i, end=" ")
print()

# while loop — same result, but more verbose here
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()


# ─────────────────────────────────────────────
# 3. INFINITE LOOP PREVENTION
# ─────────────────────────────────────────────
# An infinite loop runs forever because the condition never becomes False.
# Always make sure the loop variable changes inside the body.

# ❌ INFINITE LOOP — DO NOT RUN:
# x = 1
# while x > 0:
#     print(x)              # x never changes → runs forever

# ✅ CORRECT — x eventually reaches 0:
x = 10
while x > 0:
    print(x, end=" ")
    x -= 3                  # 10 7 4 1 → then x=-2, condition False
print()

# Common safeguard: max iteration counter
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    print(f"Attempt {attempts + 1}")
    attempts += 1


# ─────────────────────────────────────────────
# 4. while WITH break
# ─────────────────────────────────────────────
# break exits the loop immediately, regardless of the condition.

number = 0
while True:                 # Intentional infinite loop — controlled by break
    if number == 5:
        break
    print(number, end=" ")  # 0 1 2 3 4
    number += 1
print()

# Sentinel value pattern — loop until specific input
# (simulated here without real input)
data = [10, 20, 30, -1, 50]  # -1 is the sentinel
index = 0
while True:
    value = data[index]
    if value == -1:
        print("Sentinel reached.")
        break
    print(f"Processing: {value}")
    index += 1


# ─────────────────────────────────────────────
# 5. while WITH continue
# ─────────────────────────────────────────────
# continue skips the rest of the current iteration and re-checks the condition.

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue            # skip even numbers
    print(i, end=" ")       # 1 3 5 7 9
print()


# ─────────────────────────────────────────────
# 6. while WITH else
# ─────────────────────────────────────────────
# The else block runs when the condition becomes False normally
# (not when the loop is exited via break).

n = 3
while n > 0:
    print(n, end=" ")
    n -= 1
else:
    print("→ Loop completed normally.")   # Runs

# With break — else does NOT run:
n = 5
while n > 0:
    if n == 3:
        break
    print(n, end=" ")
    n -= 1
else:
    print("This will NOT print.")         # Skipped — break was hit


# ─────────────────────────────────────────────
# 7. INPUT VALIDATION LOOP
# ─────────────────────────────────────────────
# One of the most common real-world uses of while:
# keep asking until the user provides valid input.

# Pattern:
#   while True:
#       get input
#       if valid: break
#       else: show error and loop again

def get_positive_number():
    while True:
        raw = input("Enter a positive number: ")
        if raw.isdigit() and int(raw) > 0:
            return int(raw)
        print("Invalid input. Please enter a positive integer.")

# Uncomment to test interactively:
# value = get_positive_number()
# print(f"You entered: {value}")

# Simulated version (no real input):
responses = ["abc", "-5", "0", "42"]
idx = 0
while True:
    raw = responses[idx]
    idx += 1
    print(f"Input: {raw}")
    if raw.isdigit() and int(raw) > 0:
        print(f"Valid! Accepted: {int(raw)}")
        break
    print("  → Invalid, try again.")


# ─────────────────────────────────────────────
# 8. MENU LOOP PATTERN
# ─────────────────────────────────────────────
# Present a menu repeatedly until the user chooses to quit.

def show_menu():
    print("\n── Menu ──")
    print("1. Say Hello")
    print("2. Show Date")
    print("3. Quit")

# Simulated menu interactions:
choices = ["1", "2", "x", "3"]
idx = 0

while True:
    show_menu()
    choice = choices[idx]
    idx += 1
    print(f"Choice: {choice}")

    if choice == "1":
        print("Hello, World!")
    elif choice == "2":
        print("Today is a great day to code.")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")


# ─────────────────────────────────────────────
# 9. ACCUMULATOR WITH while
# ─────────────────────────────────────────────
# Collect values until a condition is met.

values = [4, 7, 2, 9, 1, 8, 3]
total = 0
i = 0
while i < len(values) and total < 20:
    total += values[i]
    print(f"Added {values[i]} → total = {total}")
    i += 1

print(f"Stopped at index {i}, total = {total}")


# ─────────────────────────────────────────────
# 10. PRACTICAL EXAMPLE — Guess the Number Game
# ─────────────────────────────────────────────

import random

def guess_the_number():
    secret = random.randint(1, 10)
    attempts = 0
    max_tries = 4

    print("\n── Guess the Number (1–10) ──")
    while attempts < max_tries:
        guess = int(input(f"Attempt {attempts + 1}/{max_tries}: "))
        attempts += 1

        if guess == secret:
            print(f"✅ Correct! You got it in {attempts} attempt(s).")
            return
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

    print(f"❌ Out of attempts! The number was {secret}.")

# Uncomment to play:
# guess_the_number()
