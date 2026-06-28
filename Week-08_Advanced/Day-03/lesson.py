# =============================================================================
# Week 08 - Day 03 | Generators
# =============================================================================
# A generator is the easiest way to build an iterator. Instead of writing a
# class with __iter__ and __next__ (Day 02), you write a normal function and
# use `yield`. Python turns it into a lazy, memory-efficient iterator for you.
#
# Topics:
#   1. yield — turning a function into a generator
#   2. Generators ARE iterators (next, StopIteration, for loops)
#   3. Lazy evaluation & memory efficiency
#   4. Generator expressions
#   5. return inside a generator
#   6. Stateful generators (running totals)
#   7. send() — two-way communication
#   8. yield from — delegating to another generator
#   9. Building data pipelines

# -----------------------------------------------------------------------------
# 1. yield — Turning a Function into a Generator
# -----------------------------------------------------------------------------
# Any function containing `yield` becomes a GENERATOR FUNCTION. Calling it does
# NOT run the body — it returns a generator object. Code runs lazily, pausing
# at each `yield` and resuming on the next next().

def count_up_to(n):
    print("  (generator started)")
    i = 1
    while i <= n:
        yield i          # pause here, hand a value back to the caller
        i += 1
    print("  (generator finished)")

gen = count_up_to(3)
print(type(gen))         # <class 'generator'>  — body has NOT run yet
print(next(gen))         # (generator started) then 1
print(next(gen))         # 2
print(next(gen))         # 3
# next(gen)              # (generator finished) then raises StopIteration

# -----------------------------------------------------------------------------
# 2. Generators ARE Iterators
# -----------------------------------------------------------------------------
# A generator has both __iter__ and __next__, so it works everywhere an
# iterator does: for loops, list(), sum(), max(), unpacking, etc.

print(list(count_up_to(5)))      # [1, 2, 3, 4, 5]
print(sum(count_up_to(100)))     # 5050

for value in count_up_to(3):
    print(value, end=" ")        # 1 2 3
print()

# Like any iterator, a generator is exhausted after one full pass:
g = count_up_to(3)
print(list(g))                   # [1, 2, 3]
print(list(g))                   # []  (already consumed)

# -----------------------------------------------------------------------------
# 3. Lazy Evaluation & Memory Efficiency
# -----------------------------------------------------------------------------
# The big win: a generator holds ONE value at a time, not the whole sequence.
# Compare building a list of a million squares vs generating them lazily.

import sys

list_version = [x * x for x in range(1_000_000)]      # all in memory
gen_version  = (x * x for x in range(1_000_000))      # nothing computed yet

print(f"list size: {sys.getsizeof(list_version):>10,} bytes")
print(f"gen  size: {sys.getsizeof(gen_version):>10,} bytes")   # tiny & constant

# Generators also enable INFINITE sequences — impossible with a list:
def naturals():
    n = 1
    while True:           # never ends — safe because it's lazy
        yield n
        n += 1

nats = naturals()
print([next(nats) for _ in range(5)])    # [1, 2, 3, 4, 5]

# -----------------------------------------------------------------------------
# 4. Generator Expressions
# -----------------------------------------------------------------------------
# Same syntax as a list comprehension but with () instead of []. It produces a
# generator, evaluated lazily. Great for feeding straight into a consumer.

squares_gen = (x * x for x in range(5))
print(type(squares_gen))                 # <class 'generator'>
print(list(squares_gen))                 # [0, 1, 4, 9, 16]

# When a generator expression is the SOLE argument, the parens are optional:
print(sum(x * x for x in range(5)))      # 30
print(max(len(w) for w in ["a", "bbb", "cc"]))   # 3

# Chaining (pipeline) — each stage stays lazy:
nums    = (n for n in range(20))
evens   = (n for n in nums if n % 2 == 0)
doubled = (n * 2 for n in evens)
print(list(doubled))                     # [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]

# -----------------------------------------------------------------------------
# 5. return Inside a Generator
# -----------------------------------------------------------------------------
# `return` in a generator stops iteration (raises StopIteration). Any returned
# value is NOT yielded — it is attached to the StopIteration exception.

def first_negative(numbers):
    for n in numbers:
        if n < 0:
            return            # stop early — no more values yielded
        yield n

print(list(first_negative([3, 1, 4, -1, 5, 9])))   # [3, 1, 4]

# -----------------------------------------------------------------------------
# 6. Stateful Generators — Running Totals
# -----------------------------------------------------------------------------
# Because a generator remembers its local variables between yields, it's a
# natural fit for accumulating state.

def running_total(numbers):
    total = 0
    for n in numbers:
        total += n
        yield total

print(list(running_total([10, 20, 30, 40])))   # [10, 30, 60, 100]

# -----------------------------------------------------------------------------
# 7. send() — Two-Way Communication
# -----------------------------------------------------------------------------
# `yield` can also RECEIVE a value. value = yield evaluates to whatever is
# passed via gen.send(...). You must "prime" the generator first with next().

def accumulator():
    total = 0
    while True:
        x = yield total      # yield current total, receive next number
        if x is not None:
            total += x

acc = accumulator()
next(acc)                    # prime: run up to the first yield
print(acc.send(10))          # 10
print(acc.send(5))           # 15
print(acc.send(100))         # 115

# -----------------------------------------------------------------------------
# 8. yield from — Delegating to Another Iterable
# -----------------------------------------------------------------------------
# `yield from iterable` yields every value from that iterable. It flattens
# nested generators and forwards send()/return cleanly.

def chain(*iterables):
    for it in iterables:
        yield from it        # replaces: for x in it: yield x

print(list(chain([1, 2], (3, 4), "ab")))   # [1, 2, 3, 4, 'a', 'b']

def flatten(nested):
    for item in nested:
        if isinstance(item, list):
            yield from flatten(item)        # recurse into sub-lists
        else:
            yield item

print(list(flatten([1, [2, [3, 4], 5], [6]])))   # [1, 2, 3, 4, 5, 6]

# -----------------------------------------------------------------------------
# 9. A Practical Pipeline — Reading "Big" Data Lazily
# -----------------------------------------------------------------------------
# Generators shine for streaming: process records one at a time without
# loading everything into memory.

def read_lines(text):
    for line in text.splitlines():
        yield line

def parse_ints(lines):
    for line in lines:
        line = line.strip()
        if line:
            yield int(line)

def only_positive(numbers):
    for n in numbers:
        if n > 0:
            yield n

raw = "5\n-3\n8\n0\n  \n12\n-1\n"
pipeline = only_positive(parse_ints(read_lines(raw)))
print(list(pipeline))        # [5, 8, 12]
print("sum of positives:", sum(only_positive(parse_ints(read_lines(raw)))))

# -----------------------------------------------------------------------------
# Summary
# -----------------------------------------------------------------------------
# - A function with `yield` is a generator function; calling it returns a lazy
#   generator object (the body doesn't run until you iterate).
# - Generators are iterators: use them in for/list/sum, exhausted after one pass.
# - They use constant memory and can model infinite sequences.
# - Generator expressions: (expr for x in it) — like a comprehension, but lazy.
# - return ends a generator; send() passes values in; yield from delegates.
# - Chain generators into memory-efficient data pipelines.
