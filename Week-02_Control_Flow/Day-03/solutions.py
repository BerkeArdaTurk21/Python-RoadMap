# Week 2 - Day 3: while Loops — Solutions

# ─────────────────────────────────────────────
# Solution 1: Sum Until Limit
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")
total = 0
count = 0

while total < 100:
    num = float(input("Enter number: "))
    total += num
    count += 1

print(f"Total reached: {total:.0f} after {count} numbers.")


# ─────────────────────────────────────────────
# Solution 2: Input Validator
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")
while True:
    raw = input("Enter a number (1-10): ")
    if not raw.lstrip("-").isdigit():
        print("Not a number. Try again.")
        continue
    num = int(raw)
    if 1 <= num <= 10:
        print(f"Accepted: {num}")
        break
    else:
        print("Out of range. Try again.")


# ─────────────────────────────────────────────
# Solution 3: Collatz Sequence
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")
n = int(input("Enter a positive integer: "))
steps = 0
sequence = [n]

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    sequence.append(n)
    steps += 1

print(" → ".join(str(x) for x in sequence))
print(f"Steps: {steps}")


# ─────────────────────────────────────────────
# Solution 4: ATM Simulator
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")
balance = 500.0

while True:
    print("\n── ATM ──")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose (1-4): ").strip()

    if choice == "1":
        print(f"Balance: ${balance:.2f}")

    elif choice == "2":
        amount = float(input("Deposit amount: $"))
        if amount <= 0:
            print("Amount must be greater than 0.")
        else:
            balance += amount
            print(f"Deposited ${amount:.2f}. Balance: ${balance:.2f}")

    elif choice == "3":
        amount = float(input("Withdraw amount: $"))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Withdrew ${amount:.2f}. Balance: ${balance:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")


# ─────────────────────────────────────────────
# Solution 5: Password Strength Checker
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")
while True:
    password = input("Enter password: ")
    errors = []

    if len(password) < 8:
        errors.append("✗ Too short (min 8 chars)")
    if not any(ch.isdigit() for ch in password):
        errors.append("✗ No digit found")
    if not any(ch.isupper() for ch in password):
        errors.append("✗ No uppercase letter")

    if errors:
        for error in errors:
            print(error)
    else:
        print("Strong password accepted.")
        break
