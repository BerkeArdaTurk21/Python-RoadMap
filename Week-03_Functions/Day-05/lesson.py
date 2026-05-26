# Week 3 - Day 5: Scope & Closures
# Topic: local, global, nonlocal, LEGB rule, closures

# ─────────────────────────────────────────────
# 1. WHAT IS SCOPE?
# ─────────────────────────────────────────────
# A "scope" is the region of code where a name (variable) is
# visible. Python uses LEXICAL scoping — the visibility of a
# name is determined by WHERE the name is written in the source,
# not by who calls the function.

# Four kinds of scopes exist, ordered from innermost to outermost:
#   L  — Local       : inside the current function
#   E  — Enclosing   : inside any outer (enclosing) function
#   G  — Global      : at module (file) level
#   B  — Built-in    : names like print, len, range, ...

# This lookup order is called the LEGB rule.


# ─────────────────────────────────────────────
# 2. LOCAL SCOPE
# ─────────────────────────────────────────────
# A variable assigned INSIDE a function is local to that function.
# It does not exist outside.

def greet():
    message = "Hello!"          # local
    print(message)

greet()                         # Hello!
# print(message)                # ❌ NameError — message not defined here


# ─────────────────────────────────────────────
# 3. GLOBAL SCOPE
# ─────────────────────────────────────────────
# A variable assigned at module level (outside any function) is global.
# Functions can READ globals freely.

counter = 0                     # global

def show_counter():
    print(f"counter = {counter}")   # reads global

show_counter()                  # counter = 0


# ─────────────────────────────────────────────
# 4. ASSIGNING TO A GLOBAL — THE 'global' KEYWORD
# ─────────────────────────────────────────────
# Writing to a name inside a function creates a LOCAL by default,
# shadowing any global with the same name. To modify the GLOBAL,
# declare it with the 'global' keyword.

x = 10

def shadow():
    x = 99                      # local — does NOT change global x
    print(f"  inside shadow: x = {x}")

def modify_global():
    global x
    x = 99                      # now actually changes the global x
    print(f"  inside modify_global: x = {x}")

shadow()
print(f"after shadow:        x = {x}")    # still 10
modify_global()
print(f"after modify_global: x = {x}")    # now 99


# ─────────────────────────────────────────────
# 5. ENCLOSING SCOPE — NESTED FUNCTIONS
# ─────────────────────────────────────────────
# A function defined inside another function can READ names from
# the enclosing function.

def outer():
    msg = "hi from outer"
    def inner():
        print(msg)              # reads enclosing 'msg'
    inner()

outer()                         # hi from outer


# ─────────────────────────────────────────────
# 6. nonlocal — REBINDING AN ENCLOSING VARIABLE
# ─────────────────────────────────────────────
# To ASSIGN to an enclosing (but not global) variable, use 'nonlocal'.

def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = make_counter()
print(c())                      # 1
print(c())                      # 2
print(c())                      # 3


# ─────────────────────────────────────────────
# 7. THE LEGB RULE IN ACTION
# ─────────────────────────────────────────────
# Python searches scopes in order: Local → Enclosing → Global → Built-in.
# The first match wins.

name = "global Berke"           # G

def outer():
    name = "enclosing Berke"    # E
    def inner():
        name = "local Berke"    # L
        print(name)             # finds Local first
    inner()
    print(name)                 # finds Enclosing
outer()
print(name)                     # finds Global

# Shadowing a built-in (don't do this, but it demonstrates B)
# >>> len = 5
# >>> len([1, 2, 3])   ← TypeError: 'int' object is not callable


# ─────────────────────────────────────────────
# 8. WHAT IS A CLOSURE?
# ─────────────────────────────────────────────
# A closure is a function that REMEMBERS variables from its
# enclosing scope even after that scope has finished executing.
#
# Closures are created automatically when:
#   1. You define a nested function,
#   2. The nested function references names from the enclosing function,
#   3. The enclosing function RETURNS the nested function.

def make_multiplier(factor):
    def multiply(x):
        return x * factor       # 'factor' is captured from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))                # 10
print(triple(5))                # 15
print(double(double(4)))        # 16

# The 'factor' value is preserved inside each returned function.
# You can even inspect it:
print(double.__closure__[0].cell_contents)   # 2
print(triple.__closure__[0].cell_contents)   # 3


# ─────────────────────────────────────────────
# 9. PRACTICAL CLOSURES
# ─────────────────────────────────────────────

# Pattern 1 — Configuration baked into a function
def make_power(exp):
    def power(base):
        return base ** exp
    return power

square = make_power(2)
cube   = make_power(3)

print(square(7))                # 49
print(cube(3))                  # 27


# Pattern 2 — Stateful counter without a class
def counter(start=0, step=1):
    value = start
    def tick():
        nonlocal value
        current = value
        value  += step
        return current
    return tick

c1 = counter()
print(c1(), c1(), c1())         # 0 1 2

c2 = counter(start=100, step=10)
print(c2(), c2(), c2())         # 100 110 120


# Pattern 3 — Building specialised functions on the fly
def build_validator(min_len):
    def is_valid(text):
        return isinstance(text, str) and len(text) >= min_len
    return is_valid

valid_username = build_validator(3)
valid_password = build_validator(8)

print(valid_username("Berke"))      # True
print(valid_username("ab"))         # False
print(valid_password("12345"))      # False
print(valid_password("verysecret")) # True


# ─────────────────────────────────────────────
# 10. COMMON PITFALL — LATE BINDING IN LOOPS
# ─────────────────────────────────────────────
# Closures capture VARIABLES, not their current values. Inside a loop,
# all closures share the same loop variable, which only holds its
# FINAL value once the loop is done.

# ❌ BUG — every function prints 4:
funcs_bad = []
for i in range(5):
    funcs_bad.append(lambda: i)
print([f() for f in funcs_bad])     # [4, 4, 4, 4, 4]

# ✅ FIX — use a default argument to bind the current value
funcs_good = []
for i in range(5):
    funcs_good.append(lambda i=i: i)
print([f() for f in funcs_good])    # [0, 1, 2, 3, 4]
