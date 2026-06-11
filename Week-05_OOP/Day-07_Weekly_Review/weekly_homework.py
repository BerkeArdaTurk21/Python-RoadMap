# =============================================================================
# Week 05 — Weekly Homework | Mini Project: Library System
# =============================================================================
# Build a small library management system using all OOP concepts from Week 5.
#
# Requirements:
#   1. LibraryItem (base)     — title, author, year
#   2. Book(LibraryItem)      — pages, isbn
#   3. DVD(LibraryItem)       — duration_min, director
#   4. Magazine(LibraryItem)  — issue_number
#   5. Library                — holds items, supports add/search/list/stats
#
# Concepts used:
#   Day 1: classes, __init__, instance methods
#   Day 2: class variable (item_count), @classmethod factory
#   Day 3: inheritance, super()
#   Day 4: @property with validation
#   Day 5: polymorphism — display() works for all item types
#   Day 6: __str__, __repr__, __len__, __contains__, __iter__
# =============================================================================

# ── Base Class ────────────────────────────────────────────────

class LibraryItem:
    item_count = 0   # class variable — shared counter

    def __init__(self, title, author, year):
        if year < 1000 or year > 2100:
            raise ValueError(f"Invalid year: {year}")
        self._title  = title
        self._author = author
        self._year   = year
        LibraryItem.item_count += 1

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    def display(self):
        return f"[{type(self).__name__}] {self._title} by {self._author} ({self._year})"

    def __str__(self):
        return self.display()

    def __repr__(self):
        return f"{type(self).__name__}({self._title!r}, {self._author!r}, {self._year})"

    def __eq__(self, other):
        return (isinstance(other, LibraryItem) and
                self._title == other._title and self._author == other._author)


# ── Subclasses ────────────────────────────────────────────────

class Book(LibraryItem):
    def __init__(self, title, author, year, pages, isbn):
        super().__init__(title, author, year)
        self._pages = pages
        self._isbn  = isbn

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if value <= 0:
            raise ValueError("Pages must be positive")
        self._pages = value

    def display(self):
        return super().display() + f" — {self._pages} pages (ISBN: {self._isbn})"


class DVD(LibraryItem):
    def __init__(self, title, author, year, duration_min, director):
        super().__init__(title, author, year)
        self._duration = duration_min
        self.director  = director

    def display(self):
        return super().display() + f" — {self._duration} min, dir. {self.director}"


class Magazine(LibraryItem):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self._issue = issue_number

    def display(self):
        return super().display() + f" — Issue #{self._issue}"


# ── Library ───────────────────────────────────────────────────

class Library:
    def __init__(self, name):
        self.name   = name
        self._items = []

    def add(self, item):
        self._items.append(item)

    def search(self, keyword):
        keyword = keyword.lower()
        return [i for i in self._items
                if keyword in i.title.lower() or keyword in i.author.lower()]

    def by_type(self, item_type):
        return [i for i in self._items if isinstance(i, item_type)]

    def stats(self):
        books     = len(self.by_type(Book))
        dvds      = len(self.by_type(DVD))
        magazines = len(self.by_type(Magazine))
        print(f"Library '{self.name}' — {len(self)} items")
        print(f"  Books: {books}, DVDs: {dvds}, Magazines: {magazines}")

    def __len__(self):
        return len(self._items)

    def __contains__(self, item):
        return item in self._items

    def __iter__(self):
        return iter(self._items)

    def __str__(self):
        return f"Library('{self.name}', {len(self)} items)"


# ── Demo ──────────────────────────────────────────────────────

lib = Library("City Library")

lib.add(Book("1984", "George Orwell", 1949, 328, "978-0451524935"))
lib.add(Book("Dune", "Frank Herbert", 1965, 688, "978-0441013593"))
lib.add(DVD("Inception", "Christopher Nolan", 2010, 148, "Nolan"))
lib.add(DVD("The Matrix", "Wachowskis", 1999, 136, "Wachowski sisters"))
lib.add(Magazine("Nature", "Various", 2024, 612))
lib.add(Magazine("Scientific American", "Various", 2024, 330))

print(lib)
lib.stats()
print()

# Polymorphism — display() works for all types
print("── All Items ──")
for item in lib:
    print(item.display())
print()

# Search
print("── Search: 'nolan' ──")
for item in lib.search("nolan"):
    print(item)
print()

# Magic methods
print(f"Total items: {len(lib)}")
book = Book("1984", "George Orwell", 1949, 328, "978-0451524935")
print(f"'1984' in library: {book in lib}")
print(f"Total items ever created: {LibraryItem.item_count}")
print()

# isinstance check
print("── Books only ──")
for b in lib.by_type(Book):
    print(repr(b))
