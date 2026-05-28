# =============================================================================
# Week 03 - Day 07 | Weekly Homework — Functions
# =============================================================================
# Mini Project: Number Utilities Toolkit
#
# Build a small toolkit that applies EVERY concept from Week 3:
#   - def + docstrings             (Day 01)
#   - default & keyword args       (Day 02)
#   - *args & **kwargs             (Day 03)
#   - lambda + map / filter        (Day 04)
#   - closures                     (Day 05)
#   - recursion                    (Day 06)
#
# Work through the TODO sections yourself first.
# The full solution is at the bottom — scroll only after you try!
# =============================================================================

# =============================================================================
# YOUR TASK
# =============================================================================
#
# Build these 6 functions:
#
# 1. summarize(*numbers, label="Stats")
#    - Accepts any amount of numbers via *args
#    - Prints: "<label>: count=N, sum=S, avg=A, min=M, max=X"
#    - Default label is "Stats"
#
# 2. make_range_checker(low, high)
#    - CLOSURE: returns a function that checks if a value is in [low, high]
#    - Returned function: in_range(x) → True / False
#
# 3. apply_transforms(numbers, **transforms)
#    - Accepts a list and keyword functions as **kwargs
#    - Applies each transform to the list and prints: "<name>: <result>"
#    - Example: apply_transforms([1,2,3], doubled=lambda x: x*2)
#
# 4. recursive_product(lst)
#    - Recursively multiplies all numbers in a list
#    - product([2, 3, 4]) → 24
#    - Base case: single element → return it
#
# 5. pipeline(data, *funcs)
#    - Passes data through a sequence of functions in order
#    - pipeline([1,2,3,4,5], remove_odds, double_all) → applies them left to right
#
# 6. A main block that DEMONSTRATES all 5 functions together

# =============================================================================
# YOUR CODE HERE
# =============================================================================

# TODO 1: summarize
def summarize(*numbers, label="Stats"):
    pass


# TODO 2: make_range_checker
def make_range_checker(low, high):
    pass


# TODO 3: apply_transforms
def apply_transforms(numbers, **transforms):
    pass


# TODO 4: recursive_product
def recursive_product(lst):
    pass


# TODO 5: pipeline
def pipeline(data, *funcs):
    pass


# TODO 6: Demo block
if __name__ == "__main__":
    print("=== Number Utilities Toolkit ===")
    print()

    # Test summarize
    # summarize(4, 7, 2, 9, 1)
    # summarize(10, 20, 30, label="Scores")

    # Test make_range_checker
    # is_teen = make_range_checker(13, 19)
    # print(is_teen(15))   # True
    # print(is_teen(25))   # False

    # Test apply_transforms
    # apply_transforms([1, 2, 3, 4, 5],
    #     doubled=lambda x: x * 2,
    #     squared=lambda x: x ** 2)

    # Test recursive_product
    # print(recursive_product([2, 3, 4]))    # 24
    # print(recursive_product([1, 5, 2, 3])) # 30

    # Test pipeline
    # remove_odds = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
    # double_all  = lambda lst: list(map(lambda x: x * 2, lst))
    # print(pipeline([1, 2, 3, 4, 5], remove_odds, double_all))  # [4, 8]
    pass


# =============================================================================
# FULL SOLUTION — scroll down only after you have tried!
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

def summarize(*numbers, label="Stats"):
    """Print a statistical summary of any number of values."""
    if not numbers:
        print(f"{label}: no data")
        return
    count  = len(numbers)
    total  = sum(numbers)
    avg    = total / count
    print(f"{label}: count={count}, sum={total}, avg={avg:.2f}, min={min(numbers)}, max={max(numbers)}")


def make_range_checker(low, high):
    """Return a closure that checks whether a value is within [low, high]."""
    def in_range(x):
        return low <= x <= high
    return in_range


def apply_transforms(numbers, **transforms):
    """Apply each named transform function to numbers and print the result."""
    for name, func in transforms.items():
        result = list(map(func, numbers))
        print(f"{name}: {result}")


def recursive_product(lst):
    """Recursively multiply all elements in a list."""
    if len(lst) == 1:                              # base case
        return lst[0]
    return lst[0] * recursive_product(lst[1:])    # recursive case


def pipeline(data, *funcs):
    """Pass data through a sequence of functions left to right."""
    result = data
    for func in funcs:
        result = func(result)
    return result


# ── Demo ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Number Utilities Toolkit ===")
    print()

    # summarize — *args + default keyword arg
    summarize(4, 7, 2, 9, 1)
    summarize(10, 20, 30, label="Scores")
    summarize()
    print()

    # make_range_checker — closure
    is_teen      = make_range_checker(13, 19)
    is_positive  = make_range_checker(1, float("inf"))
    print("is_teen(15):", is_teen(15))       # True
    print("is_teen(25):", is_teen(25))       # False
    print("is_positive(-1):", is_positive(-1))  # False
    print()

    # apply_transforms — **kwargs + lambda + map
    apply_transforms(
        [1, 2, 3, 4, 5],
        doubled  = lambda x: x * 2,
        squared  = lambda x: x ** 2,
        negative = lambda x: -x,
    )
    print()

    # recursive_product — recursion
    print("product([2,3,4]):", recursive_product([2, 3, 4]))        # 24
    print("product([1,5,2,3]):", recursive_product([1, 5, 2, 3]))  # 30
    print()

    # pipeline — *args of functions + lambda + map/filter
    remove_odds = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
    double_all  = lambda lst: list(map(lambda x: x * 2, lst))
    add_100     = lambda lst: list(map(lambda x: x + 100, lst))

    result = pipeline([1, 2, 3, 4, 5], remove_odds, double_all, add_100)
    print("pipeline result:", result)   # [104, 108]
    print()

    # ── Putting it all together ───────────────────────────────────────────
    print("── Combined Demo ──────────────────────────────────────")
    data = [3, 7, 1, 8, 4, 6, 2, 9, 5]

    # Filter values in range [4, 8], then double them
    in_range_4_8 = make_range_checker(4, 8)
    filtered = list(filter(in_range_4_8, data))     # closure + filter
    print("In range [4,8]:", filtered)               # [7, 8, 4, 6, 5]

    summarize(*filtered, label="Filtered")           # *args unpacking

    apply_transforms(filtered, doubled=lambda x: x * 2)

    print("Product of filtered:", recursive_product(filtered))  # 7*8*4*6*5 = 6720
