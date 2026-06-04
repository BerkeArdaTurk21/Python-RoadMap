# =============================================================================
# Week 04 - Day 07 | Weekly Homework — Data Structures
# =============================================================================
# Mini Project: Library Book Tracker
#
# Build a small library system that applies EVERY concept from Week 4:
#   - namedtuple      (Day 02 / 06) — Book record
#   - dict            (Day 03)      — lookup by ISBN
#   - set             (Day 04)      — unique genres, available books
#   - list + slicing  (Day 01)      — ordered collection, recent additions
#   - Counter         (Day 06)      — most popular genres
#   - defaultdict     (Day 06)      — index books by genre
#   - comprehensions  (Day 05)      — filtering and transforming
#
# Work through the TODO sections yourself first.
# Full solution is below the scroll line — try before you look!
# =============================================================================
from collections import Counter, defaultdict, namedtuple

# =============================================================================
# DATA MODEL
# =============================================================================
# Book fields: isbn, title, author, year, genre, available (bool)
Book = namedtuple("Book", ["isbn", "title", "author", "year", "genre", "available"])

# Sample library data
LIBRARY = [
    Book("978-0-06-112008-4", "To Kill a Mockingbird", "Harper Lee",      1960, "fiction",   True),
    Book("978-0-7432-7356-5", "1984",                  "George Orwell",   1949, "fiction",   False),
    Book("978-0-14-028329-7", "The Great Gatsby",      "F. Scott Fitzgerald", 1925, "fiction", True),
    Book("978-0-13-468599-1", "Clean Code",            "Robert Martin",   2008, "technical", True),
    Book("978-0-20-161622-4", "The Pragmatic Programmer","David Thomas",  1999, "technical", False),
    Book("978-0-06-093546-9", "Sapiens",               "Yuval Noah Harari",2011,"history",   True),
    Book("978-0-39-333348-1", "A Brief History of Time","Stephen Hawking",1988,"science",    True),
    Book("978-0-74-326739-6", "Thinking, Fast and Slow","Daniel Kahneman",2011,"psychology", False),
    Book("978-0-74-327552-9", "Atomic Habits",         "James Clear",     2018, "self-help", True),
    Book("978-1-59-184021-4", "The Power of Habit",    "Charles Duhigg",  2012, "psychology",True),
]

# =============================================================================
# YOUR TASKS — implement each function
# =============================================================================

# TODO 1: available_books(library)
# Return a list of Book namedtuples that are currently available.
# Use a list comprehension.
def available_books(library):
    pass


# TODO 2: books_by_genre(library)
# Return a defaultdict(list) mapping genre → list of titles.
def books_by_genre(library):
    pass


# TODO 3: genre_stats(library)
# Return a Counter of genre → number of books (total, not just available).
def genre_stats(library):
    pass


# TODO 4: search_by_author(library, author_name)
# Return a list of titles whose author contains author_name (case-insensitive).
def search_by_author(library, author_name):
    pass


# TODO 5: books_after_year(library, year)
# Return a sorted list of (title, year) tuples for books published after `year`.
# Sort by year ascending.
def books_after_year(library, year):
    pass


# TODO 6: library_summary(library)
# Print a formatted summary:
#   Total books: N
#   Available:   N
#   Checked out: N
#   Genres:      genre1, genre2, ... (sorted, unique)
#   Most popular genre: GENRE (N books)
def library_summary(library):
    pass


# =============================================================================
# DEMO — uncomment to test as you implement
# =============================================================================
if __name__ == "__main__":
    print("=== Library Book Tracker ===\n")

    # print("Available books:")
    # for b in available_books(LIBRARY):
    #     print(f"  {b.title} — {b.author}")
    # print()

    # print("Books by genre:")
    # for genre, titles in sorted(books_by_genre(LIBRARY).items()):
    #     print(f"  {genre}: {titles}")
    # print()

    # print("Genre stats:", dict(genre_stats(LIBRARY)))
    # print()

    # print("Search 'orwell':", search_by_author(LIBRARY, "orwell"))
    # print()

    # print("After 2000:", books_after_year(LIBRARY, 2000))
    # print()

    # library_summary(LIBRARY)
    pass


# =============================================================================
# FULL SOLUTION
# =============================================================================
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# .
# =============================================================================

from collections import Counter, defaultdict, namedtuple

def available_books(library):
    return [b for b in library if b.available]


def books_by_genre(library):
    index = defaultdict(list)
    for book in library:
        index[book.genre].append(book.title)
    return index


def genre_stats(library):
    return Counter(book.genre for book in library)


def search_by_author(library, author_name):
    return [b.title for b in library if author_name.lower() in b.author.lower()]


def books_after_year(library, year):
    filtered = [(b.title, b.year) for b in library if b.year > year]
    return sorted(filtered, key=lambda x: x[1])


def library_summary(library):
    total      = len(library)
    available  = sum(1 for b in library if b.available)
    checked    = total - available
    genres     = sorted({b.genre for b in library})
    top_genre  = genre_stats(library).most_common(1)[0]

    print(f"Total books:        {total}")
    print(f"Available:          {available}")
    print(f"Checked out:        {checked}")
    print(f"Genres:             {', '.join(genres)}")
    print(f"Most popular genre: {top_genre[0]} ({top_genre[1]} books)")


# ── Run the full demo ────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Library Book Tracker ===\n")

    print("── Available books ─────────────────────────────────────")
    for b in available_books(LIBRARY):
        print(f"  [{b.genre:10}] {b.title} — {b.author}")
    print()

    print("── Books by genre ──────────────────────────────────────")
    for genre, titles in sorted(books_by_genre(LIBRARY).items()):
        print(f"  {genre}: {titles}")
    print()

    print("── Genre stats ─────────────────────────────────────────")
    for genre, count in genre_stats(LIBRARY).most_common():
        print(f"  {genre:12}: {count} book(s)")
    print()

    print("── Search 'orwell' ─────────────────────────────────────")
    print(" ", search_by_author(LIBRARY, "orwell"))
    print()

    print("── Books published after 2000 ──────────────────────────")
    for title, year in books_after_year(LIBRARY, 2000):
        print(f"  {year}: {title}")
    print()

    print("── Library Summary ─────────────────────────────────────")
    library_summary(LIBRARY)
