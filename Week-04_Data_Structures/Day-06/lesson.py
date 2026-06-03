# =============================================================================
# Week 04 - Day 06 | collections Module
# =============================================================================
# Topics: Counter, defaultdict, namedtuple, deque, OrderedDict
# =============================================================================
from collections import Counter, defaultdict, namedtuple, deque, OrderedDict

# -----------------------------------------------------------------------------
# 1. Counter
# -----------------------------------------------------------------------------
# Counter counts HASHABLE objects. It's a dict subclass where values are counts.

# From an iterable
words  = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = Counter(words)
print(counts)
# Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# From a string — counts characters
letters = Counter("mississippi")
print(letters)
# Counter({'i': 4, 's': 4, 'p': 2, 'm': 1})

# From a dict
scores = Counter({"alice": 5, "bob": 3, "carol": 5})
print(scores)

# Access like a dict — missing keys return 0 (no KeyError!)
print(counts["apple"])    # 3
print(counts["mango"])    # 0  ← no KeyError

# most_common(n) — top n elements by count
print(counts.most_common(2))   # [('apple', 3), ('banana', 2)]
print(letters.most_common(3))  # [('i', 4), ('s', 4), ('p', 2)]

# Arithmetic on Counters
a = Counter({"x": 3, "y": 2, "z": 1})
b = Counter({"x": 1, "y": 4, "w": 2})

print(a + b)   # Counter({'y': 6, 'x': 4, 'w': 2, 'z': 1})  — add counts
print(a - b)   # Counter({'x': 2, 'z': 1})  — subtract, drop zeros & negatives
print(a & b)   # Counter({'x': 1, 'y': 2})  — min of each
print(a | b)   # Counter({'y': 4, 'x': 3, 'w': 2, 'z': 1})  — max of each

# Update — add more counts
counts.update(["banana", "cherry", "cherry"])
print(counts)

# elements() — expand back to a list (each element repeated count times)
c = Counter(a=3, b=1)
print(list(c.elements()))   # ['a', 'a', 'a', 'b']

# Total count
print(sum(counts.values()))   # total items counted

# -----------------------------------------------------------------------------
# 2. defaultdict
# -----------------------------------------------------------------------------
# Like a regular dict but returns a DEFAULT VALUE for missing keys
# instead of raising KeyError.
# You pass a "default factory" function: list, int, set, str, etc.

# defaultdict(list) — missing keys get an empty list
groups = defaultdict(list)
data   = [("fruit", "apple"), ("veggie", "carrot"), ("fruit", "banana"),
          ("veggie", "potato"), ("fruit", "cherry")]

for category, item in data:
    groups[category].append(item)   # no need to check if key exists!

print(dict(groups))
# {'fruit': ['apple', 'banana', 'cherry'], 'veggie': ['carrot', 'potato']}

# Compare — WITHOUT defaultdict you'd need:
# if category not in groups:
#     groups[category] = []
# groups[category].append(item)
# defaultdict collapses that to ONE line.

# defaultdict(int) — missing keys get 0 → perfect for counting
word_count = defaultdict(int)
text = "the quick brown fox jumps over the lazy dog the"
for word in text.split():
    word_count[word] += 1   # no d.get(word, 0) + 1 needed

print(dict(word_count))
print(word_count["the"])     # 3
print(word_count["missing"]) # 0  (added to dict with value 0)

# defaultdict(set) — missing keys get an empty set
tags = defaultdict(set)
tags["python"].add("programming")
tags["python"].add("language")
tags["food"].add("cooking")
print(dict(tags))

# defaultdict(lambda: "N/A") — custom default
config = defaultdict(lambda: "N/A")
config["host"] = "localhost"
print(config["host"])     # localhost
print(config["port"])     # N/A

# -----------------------------------------------------------------------------
# 3. namedtuple (recap + more)
# -----------------------------------------------------------------------------
# Already covered in Day 02 — here we go deeper.

Point   = namedtuple("Point",   ["x", "y"])
Card    = namedtuple("Card",    ["rank", "suit"])
Student = namedtuple("Student", ["name", "age", "gpa"])

p = Point(3, 7)
print(p)          # Point(x=3, y=7)
print(p.x, p.y)   # 3  7
print(p[0], p[1]) # 3  7  ← index access still works

# _make — create from an iterable
coords = (10, 20)
p2 = Point._make(coords)
print(p2)   # Point(x=10, y=20)

# _asdict — convert to OrderedDict
print(p._asdict())   # {'x': 3, 'y': 7}

# _replace — new instance with updated fields
p3 = p._replace(x=99)
print(p3)   # Point(x=99, y=7)
print(p)    # Point(x=3, y=7)  ← original unchanged

# _fields — tuple of field names
print(Point._fields)   # ('x', 'y')

# Useful for CSV/database rows — readable AND memory-efficient
students = [
    Student("Alice", 20, 3.8),
    Student("Bob",   22, 3.2),
    Student("Carol", 21, 3.9),
]
for s in students:
    print(f"{s.name}: GPA {s.gpa}")

top = max(students, key=lambda s: s.gpa)
print(f"Top student: {top.name}")

# -----------------------------------------------------------------------------
# 4. deque  (double-ended queue)
# -----------------------------------------------------------------------------
# deque supports O(1) append and pop from BOTH ends.
# list.insert(0, x) and list.pop(0) are O(n) — deque fixes this.

dq = deque([1, 2, 3, 4, 5])
print(dq)   # deque([1, 2, 3, 4, 5])

# Append / pop at both ends
dq.append(6)        # add to RIGHT
dq.appendleft(0)    # add to LEFT
print(dq)           # deque([0, 1, 2, 3, 4, 5, 6])

right = dq.pop()        # remove from RIGHT → 6
left  = dq.popleft()    # remove from LEFT  → 0
print(dq)               # deque([1, 2, 3, 4, 5])
print(right, left)

# extend / extendleft
dq.extend([6, 7])          # add multiple to right
dq.extendleft([-2, -1])    # add multiple to left (each prepended → reversed!)
print(dq)                  # deque([-1, -2, 1, 2, 3, 4, 5, 6, 7])

# rotate — shift elements
dq2 = deque([1, 2, 3, 4, 5])
dq2.rotate(2)     # rotate RIGHT by 2
print(dq2)        # deque([4, 5, 1, 2, 3])

dq2.rotate(-2)    # rotate LEFT by 2 (back to original)
print(dq2)        # deque([1, 2, 3, 4, 5])

# maxlen — fixed-size sliding window
recent = deque(maxlen=3)
for x in range(7):
    recent.append(x)
    print(list(recent))
# [0], [0,1], [0,1,2], [1,2,3], [2,3,4], [3,4,5], [4,5,6]
# Once full, adding to one end automatically removes from the other.

# USE deque when:
# - You need fast prepend (queue, BFS algorithm)
# - Sliding window of fixed size
# - You pop from BOTH ends frequently

# -----------------------------------------------------------------------------
# 5. OrderedDict
# -----------------------------------------------------------------------------
# Before Python 3.7 dicts didn't preserve insertion order — OrderedDict did.
# Today, regular dicts ARE ordered, so OrderedDict is mostly a legacy class.
# BUT it has one extra feature: move_to_end()

od = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
print(od)

od.move_to_end("a")          # move "a" to the END
print(od)                    # OrderedDict([('b',2),('c',3),('a',1)])

od.move_to_end("a", last=False)   # move "a" to the BEGINNING
print(od)                    # OrderedDict([('a',1),('b',2),('c',3)])

# Equality: OrderedDict considers ORDER when comparing
od1 = OrderedDict([("a", 1), ("b", 2)])
od2 = OrderedDict([("b", 2), ("a", 1)])
d1  = {"a": 1, "b": 2}
d2  = {"b": 2, "a": 1}

print(od1 == od2)   # False  ← order matters for OrderedDict
print(d1  == d2)    # True   ← order doesn't matter for regular dict

# =============================================================================
# SUMMARY
# =============================================================================
# ┌────────────────────────────────────────────────────────────────────┐
# │  Class          │  Use case                                        │
# ├────────────────────────────────────────────────────────────────────┤
# │  Counter        │  Count occurrences; top-N; arithmetic on counts  │
# │  defaultdict    │  Grouping, counting — no KeyError on new keys    │
# │  namedtuple     │  Lightweight immutable record with named fields  │
# │  deque          │  Fast append/pop at both ends; sliding windows   │
# │  OrderedDict    │  move_to_end(); legacy ordered dict use cases    │
# └────────────────────────────────────────────────────────────────────┘
print("\nDay 06 — collections Module complete!")
