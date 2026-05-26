# Week 3 - Day 5: Scope & Closures — Exercises
# Solve each challenge yourself. Check solutions.py when done.

# ─────────────────────────────────────────────
# Exercise 1: Predict the Output
# ─────────────────────────────────────────────
# WITHOUT running the code, write down what each print() outputs.
# Then run your prediction in Python and compare.
#
#   x = "global"
#   def outer():
#       x = "enclosing"
#       def inner():
#           x = "local"
#           print("1:", x)
#       inner()
#       print("2:", x)
#   outer()
#   print("3:", x)
#
# Expected output:
#   1: local
#   2: enclosing
#   3: global


# ─────────────────────────────────────────────
# Exercise 2: Global Counter
# ─────────────────────────────────────────────
# Create a module-level variable hits = 0.
# Write a function record_hit() that increments hits by 1
# every time it is called. Use the 'global' keyword correctly.
#
# Then call record_hit() five times and print hits.
#
# Expected output:
#   hits = 5


# ─────────────────────────────────────────────
# Exercise 3: Stateful Counter via Closure
# ─────────────────────────────────────────────
# Write a function make_counter(start=0, step=1) that returns a
# closure with NO use of 'global'. Each call to the returned
# function should return the next value and advance internal state.
#
# Expected output:
#   c1 = make_counter()
#   c1() → 0
#   c1() → 1
#   c1() → 2
#
#   c2 = make_counter(start=100, step=10)
#   c2() → 100
#   c2() → 110
#   c2() → 120
#
# Crucially: c1 and c2 must keep INDEPENDENT state.


# ─────────────────────────────────────────────
# Exercise 4: Power Factory
# ─────────────────────────────────────────────
# Write a function make_power(exp) that returns a function which
# raises its argument to the power 'exp'.
#
# Build square, cube, and "to the fifth" using the same factory.
#
# Expected output:
#   square(5)  → 25
#   cube(3)    → 27
#   fifth(2)   → 32


# ─────────────────────────────────────────────
# Exercise 5: Late-Binding Loop Fix
# ─────────────────────────────────────────────
# The function below has the classic late-binding bug:
#
#   def make_funcs_bad():
#       funcs = []
#       for i in range(5):
#           funcs.append(lambda: i)
#       return funcs
#
# Calling each function returns 4, not 0..4. Fix it.
#
# Write make_funcs_good() that returns 5 closures such that calling
# them returns 0, 1, 2, 3, 4 in order.
#
# Expected output:
#   [f() for f in make_funcs_good()]  →  [0, 1, 2, 3, 4]
