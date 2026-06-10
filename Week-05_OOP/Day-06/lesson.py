# =============================================================================
# Week 05 - Day 06 | Magic Methods (Dunder Methods)
# =============================================================================
# Topics: __str__, __repr__, __len__, __bool__, __eq__, __lt__, __add__,
#         __contains__, __getitem__, __setitem__, __iter__
# =============================================================================

# -----------------------------------------------------------------------------
# 1. WHAT ARE MAGIC METHODS?
# -----------------------------------------------------------------------------
# Magic methods (aka dunder methods — double underscore) are special methods
# Python calls AUTOMATICALLY when you use built-in operations on objects.
#
#   print(obj)     → calls obj.__str__()
#   len(obj)       → calls obj.__len__()
#   obj1 + obj2    → calls obj1.__add__(obj2)
#   obj1 == obj2   → calls obj1.__eq__(obj2)
#   x in obj       → calls obj.__contains__(x)
#   obj[i]         → calls obj.__getitem__(i)

# -----------------------------------------------------------------------------
# 2. __str__ vs __repr__
# -----------------------------------------------------------------------------
# __str__  : human-readable, for print() and str()
# __repr__ : developer-readable, for repr() and interactive shell
#            Should ideally be valid Python that recreates the object.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"          # user-friendly

    def __repr__(self):
        return f"Point({self.x!r}, {self.y!r})"  # developer-friendly


p = Point(3, 4)
print(str(p))    # (3, 4)      ← __str__
print(repr(p))   # Point(3, 4) ← __repr__
print(p)         # (3, 4)      ← print() calls __str__ first

# If __str__ is not defined, Python falls back to __repr__.
# Always define __repr__; __str__ is optional.

# -----------------------------------------------------------------------------
# 3. __len__ AND __bool__
# -----------------------------------------------------------------------------

class Bag:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return len(self._items) > 0   # empty bag is falsy

    def __str__(self):
        return f"Bag({self._items})"


bag = Bag()
print(len(bag))   # 0
print(bool(bag))  # False

bag.add("apple")
bag.add("bread")
print(len(bag))   # 2
print(bool(bag))  # True

if bag:
    print("Bag has items!")   # Bag has items!

# -----------------------------------------------------------------------------
# 4. COMPARISON METHODS
# -----------------------------------------------------------------------------
# __eq__  (==)    __ne__  (!=)
# __lt__  (<)     __le__  (<=)
# __gt__  (>)     __ge__  (>=)

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __eq__(self, other):
        return self.celsius == other.celsius

    def __lt__(self, other):
        return self.celsius < other.celsius

    def __le__(self, other):
        return self.celsius <= other.celsius

    def __gt__(self, other):
        return self.celsius > other.celsius

    def __ge__(self, other):
        return self.celsius >= other.celsius

    def __repr__(self):
        return f"Temperature({self.celsius})"


t1 = Temperature(100)
t2 = Temperature(0)
t3 = Temperature(100)

print(t1 == t3)   # True
print(t1 > t2)    # True
print(t2 < t1)    # True
print(sorted([t1, t2, t3]))   # [Temperature(0), Temperature(100), Temperature(100)]

# TIP: Define __eq__ and __lt__, then use functools.total_ordering
# to auto-generate the rest (covered in advanced Python).

# -----------------------------------------------------------------------------
# 5. ARITHMETIC METHODS
# -----------------------------------------------------------------------------
# __add__ (+)   __sub__ (-)   __mul__ (*)   __truediv__ (/)
# __floordiv__ (//)   __mod__ (%)   __pow__ (**)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):   # handles: 3 * v (when int.__mul__ fails)
        return self.__mul__(scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)    # Vector(4, 6)
print(v2 - v1)    # Vector(2, 2)
print(v1 * 3)     # Vector(3, 6)
print(3 * v1)     # Vector(3, 6)  ← uses __rmul__
print(abs(v2))    # 5.0

# -----------------------------------------------------------------------------
# 6. __contains__ AND __getitem__
# -----------------------------------------------------------------------------

class Playlist:
    def __init__(self, name):
        self.name   = name
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __contains__(self, song):       # 'Bohemian Rhapsody' in playlist
        return song in self._songs

    def __getitem__(self, index):       # playlist[0]
        return self._songs[index]

    def __setitem__(self, index, song): # playlist[0] = 'new song'
        self._songs[index] = song

    def __len__(self):
        return len(self._songs)

    def __repr__(self):
        return f"Playlist({self.name!r}, {len(self)} songs)"


pl = Playlist("Chill Mix")
pl.add("Bohemian Rhapsody")
pl.add("Hotel California")
pl.add("Stairway to Heaven")

print("Bohemian Rhapsody" in pl)    # True
print("Yesterday" in pl)            # False
print(pl[0])                        # Bohemian Rhapsody
pl[0] = "Imagine"
print(pl[0])                        # Imagine
print(len(pl))                      # 3
print(repr(pl))                     # Playlist('Chill Mix', 3 songs)

# -----------------------------------------------------------------------------
# 7. __iter__ — MAKING OBJECTS ITERABLE
# -----------------------------------------------------------------------------

class Countdown:
    def __init__(self, start):
        self.start   = start
        self.current = start

    def __iter__(self):
        self.current = self.start   # reset on each iteration
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        value        = self.current
        self.current -= 1
        return value


for n in Countdown(5):
    print(n, end=" ")   # 5 4 3 2 1 0
print()

# list() works too because list() calls iter() internally
print(list(Countdown(3)))   # [3, 2, 1, 0]

# =============================================================================
# SUMMARY
# =============================================================================
# ┌─────────────────┬───────────────────────────────────────────────────────┐
# │  Magic Method   │  Triggered by                                         │
# ├─────────────────┼───────────────────────────────────────────────────────┤
# │  __str__        │  str(obj), print(obj)                                 │
# │  __repr__       │  repr(obj), interactive shell                         │
# │  __len__        │  len(obj)                                             │
# │  __bool__       │  bool(obj), if obj:                                   │
# │  __eq__         │  obj1 == obj2                                         │
# │  __lt__         │  obj1 < obj2  (enables sorting)                       │
# │  __add__        │  obj1 + obj2                                          │
# │  __mul__        │  obj * scalar                                         │
# │  __rmul__       │  scalar * obj                                         │
# │  __contains__   │  x in obj                                             │
# │  __getitem__    │  obj[i]                                               │
# │  __setitem__    │  obj[i] = v                                           │
# │  __iter__       │  for x in obj:                                        │
# │  __next__       │  next(obj)                                            │
# └─────────────────┴───────────────────────────────────────────────────────┘
print("\nDay 06 — Magic Methods complete!")
