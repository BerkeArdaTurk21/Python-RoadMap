# Week 2 - Day 4: break / continue / pass — Solutions

# ─────────────────────────────────────────────
# Solution 1: First Negative Finder
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")
numbers = [4, 7, 2, 9, -3, 5, -1, 8]

for i, n in enumerate(numbers):
    if n < 0:
        print(f"First negative: {n} at index {i}")
        break
else:
    print("No negatives.")


# ─────────────────────────────────────────────
# Solution 2: Skip Banned Words
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")
sentence = "the quick brown fox jumps over the lazy dog"
banned = ["the", "over", "lazy"]

clean_words = []
for word in sentence.split():
    if word in banned:
        continue
    print(word)
    clean_words.append(word)

print(f"Cleaned: {' '.join(clean_words)}")


# ─────────────────────────────────────────────
# Solution 3: Prime Number Finder
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")
primes = []

for n in range(2, 51):
    for divisor in range(2, n):
        if n % divisor == 0:
            break
    else:
        primes.append(n)

print(" ".join(str(p) for p in primes))


# ─────────────────────────────────────────────
# Solution 4: Loop with pass Skeleton
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")
transactions = [200, -50, 0, 150, -30, 0, -10, 75]

for amount in transactions:
    if amount > 0:
        print(f"+{amount:<5} → Credit")
    elif amount < 0:
        print(f"{amount:<6} → Debit")
    else:
        pass                # zero-value transactions silently ignored


# ─────────────────────────────────────────────
# Solution 5: Smart Shopping Cart
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")
budget = 100.0
items = [
    ("Apple",    1.5),
    ("Laptop",   999),
    ("Book",     12),
    ("Free",     0),
    ("Pen",      2),
    ("Notebook", 5),
]

total_spent = 0.0

for item, price in items:
    if price <= 0:
        print(f"Skipped (invalid price): {item} ${price:.2f}")
        continue

    if price > budget - total_spent:
        print(f"Skipped (over budget): {item} ${price:.2f}")
        continue

    total_spent += price
    print(f"Added: {item:<10} ${price:<7.2f} | Remaining: ${budget - total_spent:.2f}")

print("─" * 26)
print(f"Total spent: ${total_spent:.2f}  |  Budget left: ${budget - total_spent:.2f}")
