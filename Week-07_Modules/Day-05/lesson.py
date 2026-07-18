# =============================================================================
# Week 07 - Day 05 | The random Module
# =============================================================================
# The random module generates pseudo-random numbers and makes random choices.
# "Pseudo": the sequence is deterministic given a seed — great for reproducible
# tests, simulations, games, sampling, and shuffling.
#
# WARNING: random is NOT cryptographically secure. For passwords/tokens use the
# `secrets` module instead.

import random

# -----------------------------------------------------------------------------
# 1. random() — Float in [0.0, 1.0)
# -----------------------------------------------------------------------------
print(f"random():    {random.random():.4f}")     # 0.0 <= x < 1.0

# -----------------------------------------------------------------------------
# 2. uniform() — Float in a Range
# -----------------------------------------------------------------------------
print(f"uniform(1,10): {random.uniform(1, 10):.4f}")  # 1.0 <= x <= 10.0

# -----------------------------------------------------------------------------
# 3. randint() and randrange() — Integers
# -----------------------------------------------------------------------------
# randint(a, b): inclusive on BOTH ends -> a <= n <= b
print(f"\nrandint(1, 6):    {random.randint(1, 6)}")      # like a dice roll

# randrange(stop) / randrange(start, stop[, step]): like range(), end EXCLUSIVE
print(f"randrange(10):    {random.randrange(10)}")        # 0..9
print(f"randrange(0,100,5): {random.randrange(0, 100, 5)}")  # 0,5,10,...,95

# -----------------------------------------------------------------------------
# 4. choice() and choices() — Pick from a Sequence
# -----------------------------------------------------------------------------
colors = ["red", "green", "blue", "yellow"]
print(f"\nchoice:  {random.choice(colors)}")              # one random element

# choices(): pick k items WITH replacement (can repeat); supports weights
picks = random.choices(colors, k=3)
print(f"choices k=3: {picks}")
weighted = random.choices(colors, weights=[10, 1, 1, 1], k=5)
print(f"weighted (red heavy): {weighted}")

# -----------------------------------------------------------------------------
# 5. sample() — Pick Unique Items (WITHOUT replacement)
# -----------------------------------------------------------------------------
deck = list(range(1, 50))
lotto = random.sample(deck, 6)             # 6 distinct numbers, no repeats
print(f"\nsample (lotto): {sorted(lotto)}")

# -----------------------------------------------------------------------------
# 6. shuffle() — Reorder a List IN PLACE
# -----------------------------------------------------------------------------
cards = ["A", "K", "Q", "J", "10"]
random.shuffle(cards)                      # modifies the list, returns None
print(f"\nshuffled: {cards}")

# To shuffle WITHOUT mutating the original, sample the whole thing:
original = [1, 2, 3, 4, 5]
shuffled_copy = random.sample(original, len(original))
print(f"original kept: {original} -> copy: {shuffled_copy}")

# -----------------------------------------------------------------------------
# 7. seed() — Reproducible Randomness
# -----------------------------------------------------------------------------
# Setting the same seed makes the sequence repeat exactly. Essential for tests.
random.seed(42)
first = [random.randint(1, 100) for _ in range(3)]
random.seed(42)
second = [random.randint(1, 100) for _ in range(3)]
print(f"\nseed(42) run 1: {first}")
print(f"seed(42) run 2: {second}")
print(f"identical? {first == second}")

# Reset to unpredictable behavior (seed from system entropy/time)
random.seed()

# -----------------------------------------------------------------------------
# 8. A Small Example — Roll Two Dice 10,000 Times
# -----------------------------------------------------------------------------
random.seed(1)  # reproducible demo
rolls = [random.randint(1, 6) + random.randint(1, 6) for _ in range(10_000)]
sevens = rolls.count(7)
print(f"\nRolled 7 in {sevens} of 10,000 trials ({sevens / 100:.1f}%) "
      f"— theory ~16.7%")

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
# random()          — float in [0.0, 1.0)
# uniform(a, b)     — float in [a, b]
# randint(a, b)     — int in [a, b] (both inclusive)
# randrange(...)    — int like range() (end exclusive)
# choice(seq)       — one random element
# choices(seq, k=)  — k picks WITH replacement (weights allowed)
# sample(seq, k)    — k UNIQUE picks (no replacement)
# shuffle(list)     — reorder a list in place (returns None)
# seed(n)           — make the sequence reproducible
# NOTE: not secure — use `secrets` for passwords/tokens.
