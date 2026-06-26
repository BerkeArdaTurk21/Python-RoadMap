# =============================================================================
# Week 08 - Day 01 | Decorators
# =============================================================================
# Decorators let you wrap a function with extra behavior — without changing
# its source code. Used everywhere: logging, timing, auth, caching, retry.
#
# Topics:
#   1. Functions as first-class objects (the foundation)
#   2. Basic decorator pattern
#   3. *args/**kwargs in wrappers
#   4. functools.wraps — preserving function metadata
#   5. Stacked decorators
#   6. Decorator factories (decorators with arguments)
#   7. Practical examples: timer, tracer, validator

import functools
import time

# -----------------------------------------------------------------------------
# 1. Functions as First-Class Objects
# -----------------------------------------------------------------------------
# In Python, functions are objects like any other value:
#   - Assign to a variable
#   - Pass as an argument
#   - Return from another function
# This is the foundation that makes decorators possible.

def greet(name):
    return f"Hello, {name}!"

say_hello = greet               # assign — no parentheses!
print(say_hello("Alice"))       # Hello, Alice!
print(type(say_hello))          # <class 'function'>

def apply_twice(func, value):   # pass as argument
    return func(func(value))

print(apply_twice(str.upper, "python"))   # PYTHON

def make_adder(n):              # return a function
    def adder(x):
        return x + n
    return adder                # return without calling

add5 = make_adder(5)
print(add5(10))                 # 15
print(add5(20))                 # 25

# -----------------------------------------------------------------------------
# 2. Basic Decorator Pattern
# -----------------------------------------------------------------------------
# A decorator is a function that:
#   1. Takes a function as its only argument
#   2. Defines a wrapper function inside
#   3. Returns the wrapper

def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)   # call original
        return result.upper()            # add behavior
    return wrapper

# Manually applying the decorator:
def greet2(name):
    return f"Hello, {name}!"

greet2 = shout(greet2)
print(greet2("world"))          # HELLO, WORLD!

# @ syntax is exactly the same thing — just cleaner:
@shout
def greet3(name):
    return f"Hi, {name}!"

print(greet3("Bob"))            # HI, BOB!
# @shout is sugar for:  greet3 = shout(greet3)

# -----------------------------------------------------------------------------
# 3. *args and **kwargs in Wrappers
# -----------------------------------------------------------------------------
# Always use *args, **kwargs so the wrapper can forward any call signature.

def trace(func):
    def wrapper(*args, **kwargs):
        arg_parts = [repr(a) for a in args]
        kwarg_parts = [f"{k}={v!r}" for k, v in kwargs.items()]
        sig = ", ".join(arg_parts + kwarg_parts)
        print(f"  -> {func.__name__}({sig})")
        result = func(*args, **kwargs)
        print(f"  <- {result!r}")
        return result
    return wrapper

@trace
def multiply(a, b):
    return a * b

multiply(3, 4)
# -> multiply(3, 4)
# <- 12

@trace
def power(base, exp=2):
    return base ** exp

power(3, exp=4)
# -> power(3, exp=4)
# <- 81

# -----------------------------------------------------------------------------
# 4. functools.wraps — Preserving Function Metadata
# -----------------------------------------------------------------------------
# Without @functools.wraps, the wrapper replaces the original's __name__,
# __doc__, and other metadata. This breaks help(), logging tools, and debuggers.

def naive_dec(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@naive_dec
def compute():
    """Performs a computation."""
    pass

print(compute.__name__)     # wrapper              <- WRONG
print(compute.__doc__)      # None                 <- WRONG

# Fix: decorate the wrapper with @functools.wraps(func):
def proper_dec(func):
    @functools.wraps(func)   # copies __name__, __doc__, __module__, __wrapped__
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@proper_dec
def compute2():
    """Performs a computation."""
    pass

print(compute2.__name__)    # compute2             <- correct
print(compute2.__doc__)     # Performs a computation.  <- correct

# Rule: ALWAYS use @functools.wraps(func) inside every decorator you write.

# -----------------------------------------------------------------------------
# 5. Stacked Decorators
# -----------------------------------------------------------------------------
# Multiple decorators stack on one function.
# They are applied bottom-up (closest to the function first).

def bold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"**{func(*args, **kwargs)}**"
    return wrapper

def italic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return f"_{func(*args, **kwargs)}_"
    return wrapper

@bold           # applied second  =>  bold(italic(headline))
@italic         # applied first
def headline(text):
    return text

print(headline("Python"))   # **_Python_**
# Execution: bold wrapper -> italic wrapper -> headline

# Order matters — swapping gives different results:
@italic
@bold
def headline2(text):
    return text

print(headline2("Python"))  # _**Python**_

# -----------------------------------------------------------------------------
# 6. Decorator Factories (Decorators with Arguments)
# -----------------------------------------------------------------------------
# To pass arguments to a decorator, add one more level of nesting.
# The outermost function accepts the arguments and returns the real decorator.

def repeat(n):                          # Level 1: factory — receives args
    def decorator(func):                # Level 2: real decorator
        @functools.wraps(func)
        def wrapper(*args, **kwargs):   # Level 3: wrapper
            for _ in range(n - 1):
                func(*args, **kwargs)
            return func(*args, **kwargs)
        return wrapper
    return decorator                    # factory returns the decorator

@repeat(3)
def knock():
    print("Knock!")

knock()
# Knock!
# Knock!
# Knock!

# @repeat(3) is: knock = repeat(3)(knock)

# Another factory — configurable log prefix:
def log(prefix="LOG"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{prefix}] Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{prefix}] Done")
            return result
        return wrapper
    return decorator

@log(prefix="DEBUG")
def process(data):
    return data.strip()

process("  hello  ")
# [DEBUG] Calling process
# [DEBUG] Done

# -----------------------------------------------------------------------------
# 7. Practical Decorator: Timer
# -----------------------------------------------------------------------------

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} finished in {elapsed * 1000:.2f}ms")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

total = slow_sum(5_000_000)
print(f"Sum: {total}")

# -----------------------------------------------------------------------------
# 8. Practical Decorator: Input Validator
# -----------------------------------------------------------------------------

def require_positive(func):
    @functools.wraps(func)
    def wrapper(n, *args, **kwargs):
        if not isinstance(n, (int, float)) or n <= 0:
            raise ValueError(f"{func.__name__}: expected positive number, got {n!r}")
        return func(n, *args, **kwargs)
    return wrapper

@require_positive
def sqrt(n):
    return n ** 0.5

print(sqrt(25))      # 5.0
try:
    sqrt(-4)
except ValueError as e:
    print(e)         # sqrt: expected positive number, got -4
