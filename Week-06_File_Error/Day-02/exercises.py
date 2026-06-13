# =============================================================================
# Week 06 - Day 02 | Writing Files — Exercises
# =============================================================================
import os, json

# -----------------------------------------------------------------------------
# Exercise 1 — Write a Shopping List
# -----------------------------------------------------------------------------
# Write a list of items to "shopping.txt", one item per line.
# Then read the file back and print each line numbered.
#
# Items: ["Milk", "Eggs", "Bread", "Butter", "Cheese"]
#
# Expected output:
#   1. Milk
#   2. Eggs
#   3. Bread
#   4. Butter
#   5. Cheese

items = ["Milk", "Eggs", "Bread", "Butter", "Cheese"]
# TODO: write items to "shopping.txt"

# TODO: read back and print numbered
print()

# -----------------------------------------------------------------------------
# Exercise 2 — Append Log Entries
# -----------------------------------------------------------------------------
# Simulate a logger that appends timestamped messages to "app.log".
# Use a fixed fake timestamp string (no need to import datetime).
# Append 3 messages, read the file, and print it.
#
# Messages:
#   "[2026-06-13 10:00] INFO: App started"
#   "[2026-06-13 10:01] INFO: User logged in"
#   "[2026-06-13 10:02] ERROR: Connection timeout"
#
# Expected output (file contents):
#   [2026-06-13 10:00] INFO: App started
#   [2026-06-13 10:01] INFO: User logged in
#   [2026-06-13 10:02] ERROR: Connection timeout

messages = [
    "[2026-06-13 10:00] INFO: App started",
    "[2026-06-13 10:01] INFO: User logged in",
    "[2026-06-13 10:02] ERROR: Connection timeout",
]
# TODO: append each message to "app.log"

# TODO: read and print
print()

# -----------------------------------------------------------------------------
# Exercise 3 — Write JSON Data
# -----------------------------------------------------------------------------
# Write the following Python dict to "config.json" with indent=2.
# Then read it back and print the value of "app_name" and each "feature".
#
# data = {
#     "app_name": "MyApp",
#     "version": "1.0.0",
#     "features": ["dark_mode", "notifications", "sync"]
# }
#
# Expected output:
#   App: MyApp
#   Features:
#     - dark_mode
#     - notifications
#     - sync

data = {
    "app_name": "MyApp",
    "version": "1.0.0",
    "features": ["dark_mode", "notifications", "sync"]
}
# TODO: write to "config.json" with json.dump()

# TODO: read back and print
print()

# -----------------------------------------------------------------------------
# Exercise 4 — Count Words and Save Report
# -----------------------------------------------------------------------------
# Given the text below, count how many times each word appears
# (case-insensitive). Write the results to "word_count.txt",
# one "word: count" per line, sorted alphabetically.
# Then print the file contents.
#
# Expected output (sorted):
#   are: 2
#   great: 1
#   i: 1
#   love: 1
#   python: 2
#   pythonistas: 1
#   we: 1

text = "Python is great I love Python we are all Pythonistas we are"
# TODO: count words, write to "word_count.txt", print
print()

# -----------------------------------------------------------------------------
# Exercise 5 — Update JSON Config
# -----------------------------------------------------------------------------
# Read "config.json" (created in Exercise 3).
# Add a new key "debug": True and update "version" to "1.1.0".
# Write the updated data back to "config.json".
# Print the final JSON contents.
#
# Expected output:
#   {
#     "app_name": "MyApp",
#     "version": "1.1.0",
#     "features": ["dark_mode", "notifications", "sync"],
#     "debug": true
#   }

# TODO: read config.json, update, write back, print
print()

# Cleanup
for fn in ["shopping.txt", "app.log", "config.json", "word_count.txt"]:
    if os.path.exists(fn):
        os.remove(fn)
