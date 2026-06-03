# =============================================================================
# Week 04 - Day 06 | collections Module — Solutions
# =============================================================================
# Study AFTER attempting exercises.py on your own.
# =============================================================================
from collections import Counter, defaultdict, namedtuple, deque

# -----------------------------------------------------------------------------
# Solution 1 — Top 3 Most Common Words
# -----------------------------------------------------------------------------
# KEY INSIGHT: Counter(iterable) counts in one step.
# most_common(n) returns the top-n (word, count) pairs in descending order.
# Clean the text first: lower() + replace punctuation.

def top_words(text, n):
    for ch in ".,!?":
        text = text.replace(ch, "")
    return Counter(text.lower().split()).most_common(n)

print("Solution 1 — Top 3 Most Common Words")
print(top_words("to be or not to be that is the question", 3))
print(top_words("the cat sat on the mat the cat", 2))
print()

# -----------------------------------------------------------------------------
# Solution 2 — Group Anagrams
# -----------------------------------------------------------------------------
# KEY INSIGHT: Two words are anagrams iff their SORTED characters are equal.
# "eat" → "aet", "tea" → "aet", "ate" → "aet" — all the same key.
# defaultdict(list) auto-creates [] for each new sorted-word key.
# Return the .values() (list of lists).

def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))   # canonical form
        groups[key].append(word)
    return list(groups.values())

print("Solution 2 — Group Anagrams")
groups = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
for g in sorted(groups, key=len, reverse=True):
    print(sorted(g))
print()

# WHY defaultdict(list) instead of a plain dict?
# Without it: if key not in groups: groups[key] = []  (extra 2 lines every time)
# With it: groups[key].append(word)  — one line, key created automatically.

# -----------------------------------------------------------------------------
# Solution 3 — Named Tuple: Book Catalog
# -----------------------------------------------------------------------------
# KEY INSIGHT: namedtuple fields are accessible by name — readable code.
# min()/max() with key= function works cleanly on namedtuple collections.
# List comprehension filters by genre with .lower() for case-insensitivity.

Book = namedtuple("Book", ["title", "author", "year", "genre"])

books = [
    Book("1984",                     "George Orwell",   1949, "fiction"),
    Book("Clean Code",               "Robert Martin",   2008, "technical"),
    Book("Brave New World",          "Aldous Huxley",   1932, "fiction"),
    Book("The Pragmatic Programmer", "David Thomas",    1999, "technical"),
]

def oldest_book(books):
    return min(books, key=lambda b: b.year)

def books_by_genre(books, genre):
    return [b.title for b in books if b.genre.lower() == genre.lower()]

print("Solution 3 — Book Catalog")
print("Oldest:", oldest_book(books))
print("Fiction titles:", books_by_genre(books, "fiction"))
print()

# -----------------------------------------------------------------------------
# Solution 4 — Sliding Window Maximum
# -----------------------------------------------------------------------------
# KEY INSIGHT (simple approach): slice lst[i:i+k] for each window start i.
# There are len(lst)-k+1 windows.
#
# BONUS efficient approach with deque:
# Maintain a deque of INDICES in decreasing value order.
# The front of the deque is always the index of the window maximum.
# Remove indices that fall outside the current window from the front.
# Remove indices whose value is ≤ current value from the back (they can never
# be the max while the current element is in the window).

def sliding_max(lst, k):
    result = []
    dq = deque()   # stores indices, front = max of current window

    for i, val in enumerate(lst):
        # Remove out-of-window index from front
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove smaller values from back (they can't be max)
        while dq and lst[dq[-1]] <= val:
            dq.pop()
        dq.append(i)
        # Start recording once first full window is complete
        if i >= k - 1:
            result.append(lst[dq[0]])

    return result

print("Solution 4 — Sliding Window Maximum")
print(sliding_max([1, 3, -1, -3, 5, 3, 6, 7], 3))   # [3, 3, 5, 5, 6, 7]
print(sliding_max([4, 2, 5, 1, 3], 2))                # [4, 5, 5, 3]
print()

# Simple O(n*k) alternative — same results, easier to understand:
def sliding_max_simple(lst, k):
    return [max(lst[i:i+k]) for i in range(len(lst) - k + 1)]

print(sliding_max_simple([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]

# -----------------------------------------------------------------------------
# Solution 5 — Character Frequency Difference
# -----------------------------------------------------------------------------
# KEY INSIGHT: Build a Counter for each string, then compute the signed diff.
# Counter - Counter drops zeros and negatives — NOT what we want here.
# Instead: get all unique keys, compute c1[k] - c2[k] for each, skip zeros.

def char_diff(s1, s2):
    c1, c2 = Counter(s1), Counter(s2)
    all_keys = set(c1) | set(c2)
    result = {k: c1[k] - c2[k] for k in all_keys if c1[k] - c2[k] != 0}
    return result

print("Solution 5 — Character Frequency Difference")
print(char_diff("aabbcc", "abcdef"))
# {'a': 1, 'b': 1, 'c': 1, 'd': -1, 'e': -1, 'f': -1}
print()

# WHY not (c1 - c2)?
# Counter subtraction drops zero AND negative results — we'd lose 'd','e','f'.
# We want signed differences, so we compute manually.
