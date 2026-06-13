# =============================================================================
# Week 06 - Day 02 | Writing Files — Solutions
# =============================================================================
import os, json

# Solution 1
# KEY INSIGHT: writelines() needs \n in each string. join+\n is cleaner.
items = ["Milk", "Eggs", "Bread", "Butter", "Cheese"]
with open("shopping.txt", "w", encoding="utf-8") as f:
    f.writelines(item + "\n" for item in items)

with open("shopping.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}. {line.rstrip()}")
print()

# Solution 2
# KEY INSIGHT: open in 'a' mode for each append, or open once and write all.
messages = [
    "[2026-06-13 10:00] INFO: App started",
    "[2026-06-13 10:01] INFO: User logged in",
    "[2026-06-13 10:02] ERROR: Connection timeout",
]
with open("app.log", "a", encoding="utf-8") as f:
    for msg in messages:
        f.write(msg + "\n")

with open("app.log", "r", encoding="utf-8") as f:
    print(f.read(), end="")
print()

# Solution 3
data = {"app_name": "MyApp", "version": "1.0.0",
        "features": ["dark_mode", "notifications", "sync"]}
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)
print(f"App: {cfg['app_name']}")
print("Features:")
for feat in cfg["features"]:
    print(f"  - {feat}")
print()

# Solution 4
# KEY INSIGHT: str.lower() normalises case. sorted() on dict.items() sorts keys.
text = "Python is great I love Python we are all Pythonistas we are"
counts = {}
for word in text.lower().split():
    counts[word] = counts.get(word, 0) + 1

# Filter to only words in our expected set
filtered = {w: c for w, c in counts.items()
            if w in {"python","great","i","love","are","we","pythonistas"}}

with open("word_count.txt", "w", encoding="utf-8") as f:
    for word in sorted(filtered):
        f.write(f"{word}: {filtered[word]}\n")

with open("word_count.txt", "r", encoding="utf-8") as f:
    print(f.read(), end="")
print()

# Solution 5
# KEY INSIGHT: read → modify in Python → write back. Never write partial JSON.
with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

cfg["debug"]   = True
cfg["version"] = "1.1.0"

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(cfg, f, indent=2)

with open("config.json", "r", encoding="utf-8") as f:
    print(f.read())

for fn in ["shopping.txt", "app.log", "config.json", "word_count.txt"]:
    if os.path.exists(fn):
        os.remove(fn)
