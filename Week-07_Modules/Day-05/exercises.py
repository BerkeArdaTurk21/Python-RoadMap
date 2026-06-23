# =============================================================================
# Week 07 - Day 05 | The random Module — Exercises
# =============================================================================

import random

# For reproducible output while you develop, you may uncomment this:
# random.seed(0)

# -----------------------------------------------------------------------------
# Exercise 1 — Dice Roller
# -----------------------------------------------------------------------------
# Simulate rolling two six-sided dice. Print:
#   a) The two individual rolls
#   b) Their total
#   c) Whether it's "Snake eyes!" (1+1), "Boxcars!" (6+6), or just the total
#
# Expected (varies):
#   Rolls: 3 and 5
#   Total: 8
#
# Hint: random.randint(1, 6).

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Random Password (NON-secure, practice only)
# -----------------------------------------------------------------------------
# Build a 10-character random password from letters + digits + symbols.
# Use random.choices() with this alphabet and k=10, then join into a string.
# (Reminder: for REAL passwords use the `secrets` module — random is not secure.)
#
# Expected (varies): "Password: a7$Kp2!mZq"
#
# Hint: import string; alphabet = string.ascii_letters + string.digits + "!@#$%"

import string
alphabet = string.ascii_letters + string.digits + "!@#$%"
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Lottery Draw
# -----------------------------------------------------------------------------
# Draw 6 UNIQUE numbers from 1 to 49, plus 1 separate "bonus" number that is
# NOT among the 6 main numbers. Print the main numbers sorted, then the bonus.
#
# Expected (varies):
#   Main:  [4, 11, 23, 28, 39, 45]
#   Bonus: 17
#
# Hint: random.sample(range(1, 50), 6) for the main numbers; then pick a bonus
#       from the remaining numbers (those not already drawn).

# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Shuffle a Deck (without destroying the original)
# -----------------------------------------------------------------------------
# Build a deck of cards: ranks 2..10, J, Q, K, A across suits S H D C
# (52 cards as strings like "AS"). Then:
#   a) Print the total number of cards (should be 52)
#   b) Produce a SHUFFLED copy WITHOUT changing the original ordered deck
#   c) Print the first 5 cards of the shuffled copy
#   d) Confirm the original deck is still in its original order (print first 3)
#
# Hint: random.sample(deck, len(deck)) returns a shuffled copy.

ranks = [str(n) for n in range(2, 11)] + ["J", "Q", "K", "A"]
suits = ["S", "H", "D", "C"]   # Spades, Hearts, Diamonds, Clubs
deck = [r + s for s in suits for r in ranks]
# TODO
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Weighted Random & Reproducibility
# -----------------------------------------------------------------------------
# A loot box drops one item with these weights:
#   "common" 70, "rare" 25, "legendary" 5
# Do the following:
#   a) Set random.seed(123)
#   b) Open 1000 boxes (random.choices with weights, k=1000)
#   c) Count how many of each rarity dropped and print the counts
#   d) Re-seed with 123 and open 1000 again; confirm the counts are IDENTICAL
#
# Expected: the two count dictionaries must be exactly equal (prove seed works).
#
# Hint: from collections import Counter; Counter(results).

items = ["common", "rare", "legendary"]
weights = [70, 25, 5]
# TODO
