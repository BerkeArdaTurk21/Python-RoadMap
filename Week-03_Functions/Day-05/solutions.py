# Week 3 - Day 5: Scope & Closures — Solutions

# ─────────────────────────────────────────────
# Solution 1: Predict the Output
# ─────────────────────────────────────────────
print("─── Exercise 1 ───")

x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print("1:", x)
    inner()
    print("2:", x)

outer()
print("3:", x)


# ─────────────────────────────────────────────
# Solution 2: Global Counter
# ─────────────────────────────────────────────
print("\n─── Exercise 2 ───")

hits = 0

def record_hit():
    global hits
    hits += 1

for _ in range(5):
    record_hit()

print(f"hits = {hits}")


# ─────────────────────────────────────────────
# Solution 3: Stateful Counter via Closure
# ─────────────────────────────────────────────
print("\n─── Exercise 3 ───")

def make_counter(start=0, step=1):
    value = start
    def tick():
        nonlocal value
        current = value
        value += step
        return current
    return tick

c1 = make_counter()
print(c1(), c1(), c1())

c2 = make_counter(start=100, step=10)
print(c2(), c2(), c2())

# c1 keeps its own state, unaffected by c2
print("c1 again:", c1(), c1())


# ─────────────────────────────────────────────
# Solution 4: Power Factory
# ─────────────────────────────────────────────
print("\n─── Exercise 4 ───")

def make_power(exp):
    def power(base):
        return base ** exp
    return power

square = make_power(2)
cube   = make_power(3)
fifth  = make_power(5)

print(square(5))
print(cube(3))
print(fifth(2))


# ─────────────────────────────────────────────
# Solution 5: Late-Binding Loop Fix
# ─────────────────────────────────────────────
print("\n─── Exercise 5 ───")

def make_funcs_good():
    funcs = []
    for i in range(5):
        # Bind current value of i via default argument
        funcs.append(lambda i=i: i)
    return funcs

print([f() for f in make_funcs_good()])
