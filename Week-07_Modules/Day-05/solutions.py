# =============================================================================
# Week 07 - Day 05 | The random Module — Solutions
# =============================================================================

import random
import string
from collections import Counter

# Solution 1
d1, d2 = random.randint(1, 6), random.randint(1, 6)
print(f"Rolls: {d1} and {d2}")
print(f"Total: {d1 + d2}")
if d1 == d2 == 1:
    print("Snake eyes!")
elif d1 == d2 == 6:
    print("Boxcars!")
print()

# Solution 2
alphabet = string.ascii_letters + string.digits + "!@#$%"
password = "".join(random.choices(alphabet, k=10))
print(f"Password: {password}")
print()

# Solution 3
main = random.sample(range(1, 50), 6)
remaining = [n for n in range(1, 50) if n not in main]
bonus = random.choice(remaining)
print(f"Main:  {sorted(main)}")
print(f"Bonus: {bonus}")
print()

# Solution 4
ranks = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
suits = ["S", "H", "D", "C"]   # Spades, Hearts, Diamonds, Clubs
deck = [r + s for s in suits for r in ranks]

print(f"Total cards: {len(deck)}")
shuffled = random.sample(deck, len(deck))   # shuffled copy, original intact
print(f"Shuffled first 5: {shuffled[:5]}")
print(f"Original first 3 (unchanged): {deck[:3]}")
print()

# Solution 5
items = ["common", "rare", "legendary"]
weights = [70, 25, 5]

random.seed(123)
run1 = Counter(random.choices(items, weights=weights, k=1000))
random.seed(123)
run2 = Counter(random.choices(items, weights=weights, k=1000))

print(f"Run 1: {dict(run1)}")
print(f"Run 2: {dict(run2)}")
print(f"Identical? {run1 == run2}")

# Reset to unpredictable behavior afterwards
random.seed()
